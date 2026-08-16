#!/usr/bin/env python3
"""Build the "who owns what" map for a GitHub organization.

Hits the GitHub REST API for every repository in an org, works out who actually
owns each one (top committer, unless a CODEOWNERS file says otherwise), and
renders a single self-contained HTML page.

No third-party dependencies -- standard library only, so it runs on a bare
`ubuntu-latest` runner with no pip step.

Usage
-----
    GITHUB_TOKEN=ghp_xxx python3 build_ownership_map.py \
        --org Local-Service-Spotlight \
        --out ../public/ownership-map.html

    # See the design without touching the network:
    python3 build_ownership_map.py --sample --out preview.html

Exit codes: 0 ok, 1 bad usage / config, 2 upstream API failure.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com"
UA = "lss-ownership-map/1.0"
TEMPLATE = Path(__file__).with_name("template.html")

# Where each repo sits in the flow of work. Repos not listed here land in
# "Unclassified" so a new repo shows up loudly instead of vanishing.
LAYERS = [
    {
        "title": "Shared runtime",
        "note": "Everything else imports these. A break here breaks the rest.",
        "repos": ["agent-runtime", "dennis-os"],
    },
    {
        "title": "Content and data",
        "note": "Produce and hold the material the surfaces render.",
        "repos": ["task-library", "content-agent", "hq"],
    },
    {
        "title": "Site machinery",
        "note": "WordPress themes and the builder behind the spotlight sites.",
        "repos": ["bm-wordpress", "sitebuilder-wordpress-themes"],
    },
    {
        "title": "Public surfaces",
        "note": "What a customer or prospect actually looks at.",
        "repos": [
            "second-ring",
            "white-label-dash-front-end",
            "white-label-dash-back-end",
        ],
    },
]

CODEOWNERS_PATHS = (
    ".github/CODEOWNERS",
    "CODEOWNERS",
    "docs/CODEOWNERS",
)


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

class ApiError(RuntimeError):
    pass


def api_get(path: str, token: str, *, allow_404: bool = False, retries: int = 4):
    """GET a GitHub API path. Returns (payload, link_header).

    Retries on 5xx and on secondary-rate-limit responses, honouring
    Retry-After and x-ratelimit-reset when GitHub supplies them.
    """
    url = path if path.startswith("http") else API + path
    last = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": UA,
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read()
                link = resp.headers.get("Link", "") or ""
                if resp.status == 204 or not body:
                    return [], link
                return json.loads(body.decode("utf-8")), link
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code == 404 and allow_404:
                return None, ""
            if exc.code in (403, 429):
                wait = _rate_limit_wait(exc)
                if wait is not None and attempt < retries - 1:
                    sys.stderr.write(f" rate limited, sleeping {wait}s\n")
                    time.sleep(wait)
                    continue
            if 500 <= exc.code < 600 and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise ApiError(f"{exc.code} {exc.reason} for {url}") from exc
        except urllib.error.URLError as exc:
            last = exc
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise ApiError(f"network error for {url}: {exc}") from exc
    raise ApiError(f"gave up on {url}: {last}")


def _rate_limit_wait(exc) -> int | None:
    retry_after = exc.headers.get("Retry-After")
    if retry_after and retry_after.isdigit():
        return min(int(retry_after), 120)
    reset = exc.headers.get("x-ratelimit-reset")
    remaining = exc.headers.get("x-ratelimit-remaining")
    if reset and remaining == "0":
        delta = int(reset) - int(time.time())
        if 0 < delta <= 120:
            return delta + 1
    return None


def api_paged(path: str, token: str, *, cap: int = 20):
    """Follow rel="next" links and yield every item across pages."""
    out, url, pages = [], path, 0
    while url and pages < cap:
        payload, link = api_get(url, token)
        if not isinstance(payload, list):
            break
        out.extend(payload)
        pages += 1
        url = _next_link(link)
    return out


def _next_link(link_header: str) -> str | None:
    for part in (link_header or "").split(","):
        m = re.search(r'<([^>]+)>\s*;\s*rel="next"', part.strip())
        if m:
            return m.group(1)
    return None


# --------------------------------------------------------------------------
# Data assembly
# --------------------------------------------------------------------------

def parse_codeowners(text: str) -> str | None:
    """Return the first @handle that owns the repository root, if any.

    Only a root-level rule ('*' or '/') is treated as repo ownership; a rule
    scoped to a subdirectory says nothing about who owns the whole thing.
    """
    for raw in (text or "").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        pattern, owners = parts[0], parts[1:]
        if pattern not in ("*", "/", "/*", "**"):
            continue
        for owner in owners:
            if owner.startswith("@") and "/" not in owner:
                return owner[1:]
    return None


def fetch_codeowners(org: str, repo: str, token: str) -> str | None:
    for path in CODEOWNERS_PATHS:
        payload, _ = api_get(
            f"/repos/{org}/{repo}/contents/{path}", token, allow_404=True
        )
        if not payload or not isinstance(payload, dict):
            continue
        content = payload.get("content")
        if not content:
            continue
        try:
            text = base64.b64decode(content).decode("utf-8", "replace")
        except (ValueError, TypeError):
            continue
        handle = parse_codeowners(text)
        if handle:
            return handle
    return None


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-") or "unknown"


def build(org: str, token: str, *, include_archived: bool = False) -> dict:
    sys.stderr.write(f"Listing repositories in {org}...\n")
    repos_raw = api_paged(f"/orgs/{org}/repos?per_page=100&type=all&sort=full_name", token)
    if not repos_raw:
        raise ApiError(
            f"no repositories returned for org '{org}'. Check the org name and "
            "that the token has read access to private repos."
        )

    repos, contributor_index = [], {}
    for meta in repos_raw:
        name = meta["name"]
        if meta.get("archived") and not include_archived:
            sys.stderr.write(f"  {name}: archived, skipping\n")
            continue
        sys.stderr.write(f"  {name}: contributors...\n")

        stats = api_paged(f"/repos/{org}/{name}/contributors?per_page=100&anon=0", token)
        contributors = []
        for c in stats or []:
            login = c.get("login") or c.get("name") or "unknown"
            contributors.append({
                "login": login,
                "name": c.get("login") or login,
                "commits": int(c.get("contributions") or 0),
            })
        contributors.sort(key=lambda c: -c["commits"])

        if contributors:
            owner_login = contributors[0]["login"]
            owner_source = "top committer"
        else:
            owner_login, owner_source = None, "no commits"

        declared = fetch_codeowners(org, name, token)
        if declared:
            owner_login, owner_source = declared, "CODEOWNERS"

        for c in contributors:
            contributor_index.setdefault(c["login"], 0)
            contributor_index[c["login"]] += c["commits"]

        repos.append({
            "name": name,
            "commits": sum(c["commits"] for c in contributors),
            "contributors": contributors,
            "owner": slugify(owner_login) if owner_login else "unassigned",
            "owner_login": owner_login,
            "owner_source": owner_source,
            "visibility": "public" if not meta.get("private") else "private",
            "last_push": (meta.get("pushed_at") or "")[:10] or "unknown",
        })

    # People ordered by total commits, so the loudest contributor takes slot 1
    # and colours stay stable as long as the ordering does.
    owners = {r["owner"]: r["owner_login"] for r in repos if r["owner"] != "unassigned"}
    people = [
        {"id": pid, "name": login, "login": login,
         "total": contributor_index.get(login, 0)}
        for pid, login in owners.items()
    ]
    people.sort(key=lambda p: (-p["total"], p["name"]))
    for i, p in enumerate(people):
        p["slot"] = i if i < 8 else None
        p.pop("total", None)
    if any(r["owner"] == "unassigned" for r in repos):
        people.append({"id": "unassigned", "name": "No clear owner",
                       "login": "", "slot": None})

    return assemble(org, repos, people, sample=False)


def assemble(org: str, repos: list, people: list, *, sample: bool,
             sample_note: str = "") -> dict:
    known = {r["name"] for r in repos}
    layers, placed = [], set()
    for layer in LAYERS:
        present = [n for n in layer["repos"] if n in known]
        placed.update(present)
        if present:
            layers.append({**layer, "repos": present})
    leftover = sorted(known - placed)
    if leftover:
        layers.append({
            "title": "Unclassified",
            "note": "Not yet placed in the flow. Add it to LAYERS in the generator.",
            "repos": leftover,
        })

    now = datetime.now(timezone.utc)
    return {
        "org": org,
        "generated_at": now.isoformat(timespec="seconds"),
        "generated_at_display": now.strftime("%a %d %b %Y, %H:%M UTC"),
        "sample": sample,
        "sample_note": sample_note,
        "people": people,
        "repos": repos,
        "layers": layers,
    }


def render(data: dict, template: Path = TEMPLATE) -> str:
    html = template.read_text(encoding="utf-8")
    if "__DATA__" not in html:
        raise ValueError(f"{template} has no __DATA__ placeholder")
    payload = json.dumps(data, ensure_ascii=False)
    # Keep a stray "</script>" inside the JSON from closing the host tag.
    payload = payload.replace("</", "<\\/")
    return html.replace("__DATA__", payload)


# --------------------------------------------------------------------------
# Sample data -- design preview only, clearly flagged in the output
# --------------------------------------------------------------------------

def sample_data() -> dict:
    people = [
        {"id": "dennis-yu", "name": "Dennis Yu", "login": "dennisyu", "slot": 0},
        {"id": "daniel-goodrich", "name": "Daniel Goodrich", "login": "Goodrich-Dev", "slot": 1},
        {"id": "austin-stierler", "name": "Austin Stierler", "login": "astierler", "slot": 2},
        {"id": "josh", "name": "Josh", "login": "josh-lss", "slot": 3},
    ]

    def c(*pairs):
        return [{"login": l, "name": l, "commits": n} for l, n in pairs]

    rows = [
        ("agent-runtime",                  c(("dennisyu", 74), ("Goodrich-Dev", 12)), "dennis-yu",      "private", "2026-08-13"),
        ("dennis-os",                      c(("dennisyu", 66)),                       "dennis-yu",      "private", "2026-08-14"),
        ("task-library",                   c(("Goodrich-Dev", 48), ("dennisyu", 21)),  "daniel-goodrich", "public",  "2026-08-14"),
        ("content-agent",                  c(("dennisyu", 39), ("josh-lss", 8)),       "dennis-yu",      "private", "2026-08-11"),
        ("hq",                             c(("josh-lss", 27), ("dennisyu", 9)),       "josh",           "private", "2026-08-09"),
        ("bm-wordpress",                   c(("astierler", 31), ("Goodrich-Dev", 4)),  "austin-stierler", "private", "2026-07-30"),
        ("sitebuilder-wordpress-themes",   c(("astierler", 22)),                       "austin-stierler", "private", "2026-06-18"),
        ("second-ring",                    c(("dennisyu", 55)),                       "dennis-yu",      "private", "2026-08-14"),
        ("white-label-dash-front-end",     c(("Goodrich-Dev", 44), ("astierler", 6)),  "daniel-goodrich", "private", "2026-08-12"),
        ("white-label-dash-back-end",      c(("Goodrich-Dev", 30), ("dennisyu", 6)),   "daniel-goodrich", "private", "2026-08-12"),
    ]
    repos = [{
        "name": n,
        "commits": sum(x["commits"] for x in contribs),
        "contributors": contribs,
        "owner": owner,
        "owner_login": owner,
        "owner_source": "top committer",
        "visibility": vis,
        "last_push": pushed,
    } for n, contribs, owner, vis, pushed in rows]

    note = (
        "The ten repository names, the org, and the 502-commit total are real - they come "
        "straight from the mirror. The per-repo split, the contributor lists and the dates "
        "are placeholders so the layout can be reviewed before the job has run. "
        "The first run of the workflow replaces all of it with figures from the GitHub API."
    )
    return assemble("Local-Service-Spotlight", repos, people, sample=True, sample_note=note)


# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--org", default=os.environ.get("GH_ORG", "Local-Service-Spotlight"))
    ap.add_argument("--out", default="ownership-map.html")
    ap.add_argument("--json-out", help="also write the raw data as JSON")
    ap.add_argument("--sample", action="store_true",
                    help="render the layout with placeholder data, no network")
    ap.add_argument("--include-archived", action="store_true")
    args = ap.parse_args(argv)

    if args.sample:
        data = sample_data()
    else:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not token:
            sys.stderr.write(
                "GITHUB_TOKEN is not set.\n"
                "In Actions add:  env:\n                  GITHUB_TOKEN: ${{ secrets.OWNERSHIP_MAP_TOKEN }}\n"
                "Locally:         export GITHUB_TOKEN=$(gh auth token)\n"
                "Or run with --sample to preview the layout offline.\n")
            return 1
        try:
            data = build(args.org, token, include_archived=args.include_archived)
        except ApiError as exc:
            sys.stderr.write(f"GitHub API failed: {exc}\n")
            return 2

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(data), encoding="utf-8")
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    total = sum(r["commits"] for r in data["repos"])
    solo = [r["name"] for r in data["repos"] if len(r["contributors"]) == 1]
    sys.stderr.write(
        f"\nWrote {out} - {len(data['repos'])} repos, {total} commits, "
        f"{len(data['people'])} people.\n")
    if solo:
        sys.stderr.write(f"Bus factor 1: {', '.join(solo)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
