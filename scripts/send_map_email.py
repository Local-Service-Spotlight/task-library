#!/usr/bin/env python3
"""Email the ownership map.

Sends a multipart message: an HTML body that renders the summary inline in the
mail client, a plain-text alternative for clients that won't, and the full
generated page as an attachment.

Standard library only. Credentials come from the environment, never from
arguments, so they don't land in a process list or a CI log.

    MAIL_SERVER  MAIL_PORT  MAIL_USERNAME  MAIL_PASSWORD  MAIL_TO
"""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import ssl
import sys
from email.message import EmailMessage
from pathlib import Path


def recipients(raw: str) -> list[str]:
    """Split a comma/semicolon/whitespace separated list, de-duplicated."""
    parts, seen, out = [], set(), []
    for chunk in (raw or "").replace(";", ",").replace("\n", ",").split(","):
        parts.extend(chunk.split())
    for p in parts:
        addr = p.strip().strip("<>")
        if addr and "@" in addr and addr.lower() not in seen:
            seen.add(addr.lower())
            out.append(addr)
    return out


def summarise(data: dict) -> tuple[str, list[str]]:
    """Return (headline, lines) describing today's map."""
    repos = sorted(data["repos"], key=lambda r: -r["commits"])
    names = {p["id"]: p["name"] for p in data["people"]}
    solo = [r["name"] for r in repos if len(r["contributors"]) == 1]
    total = sum(r["commits"] for r in repos)

    headline = (
        f"{len(repos)} repos · {total:,} commits · "
        f"{len(solo)} with a single contributor"
    )
    lines = [
        f"{r['name']} — {names.get(r['owner'], 'no clear owner')} — "
        f"{r['commits']:,} commits, {len(r['contributors'])} contributor"
        f"{'' if len(r['contributors']) == 1 else 's'}"
        f"{' ⚠ bus factor 1' if len(r['contributors']) == 1 else ''}"
        for r in repos
    ]
    return headline, lines


def build_message(data: dict, html_path: Path, url: str,
                  sender: str, to: list[str]) -> EmailMessage:
    headline, lines = summarise(data)
    solo = [r["name"] for r in data["repos"] if len(r["contributors"]) == 1]

    msg = EmailMessage()
    msg["Subject"] = f"Who owns what — {data['generated_at'][:10]} — {headline}"
    msg["From"] = sender
    msg["To"] = ", ".join(to)

    text = "\n".join([
        "Who owns what in " + data["org"],
        headline,
        "",
        *lines,
        "",
        ("Bus factor 1 (one person has ever committed): " + ", ".join(solo))
        if solo else "No repository depends on a single person.",
        "",
        "Full map: " + url,
        "",
        "Owner is the top committer unless a CODEOWNERS file says otherwise.",
        "If a name is wrong, fix it with a CODEOWNERS line in that repo — not by",
        "replying to this email. The map regenerates from the repos themselves.",
    ])
    msg.set_content(text)

    def esc(s):
        return (str(s).replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))

    rows = "".join(
        f"<tr><td style='padding:5px 12px 5px 0'>{esc(l.split(' — ')[0])}</td>"
        f"<td style='padding:5px 12px 5px 0;color:#52514e'>"
        f"{esc(' — '.join(l.split(' — ')[1:]))}</td></tr>"
        for l in lines
    )
    msg.add_alternative(
        "<div style=\"font-family:system-ui,-apple-system,'Segoe UI',sans-serif;"
        "font-size:14px;color:#0b0b0b;line-height:1.5\">"
        f"<h2 style='font-size:18px;margin:0 0 4px'>Who owns what in {esc(data['org'])}</h2>"
        f"<p style='margin:0 0 16px;color:#52514e'>{esc(headline)}</p>"
        f"<table style='border-collapse:collapse;font-size:13px'>{rows}</table>"
        + (f"<p style='margin:16px 0 0;color:#d03b3b'>Bus factor 1: "
           f"{esc(', '.join(solo))}</p>" if solo else "")
        + f"<p style='margin:16px 0 0'><a href='{esc(url)}'>Open the full map</a>"
        " — colour-coded, sized by commit volume, with the diagram.</p>"
        "<p style='margin:16px 0 0;color:#898781;font-size:12px'>Owner is the top "
        "committer unless a CODEOWNERS file says otherwise. If a name here is "
        "wrong, the fix is a CODEOWNERS line in that repository, not a reply to "
        "this email.</p></div>",
        subtype="html",
    )

    msg.add_attachment(
        html_path.read_bytes(), maintype="text", subtype="html",
        filename="ownership-map.html",
    )
    return msg


def send(msg: EmailMessage, server: str, port: int, user: str, password: str):
    context = ssl.create_default_context()
    if port == 465:
        with smtplib.SMTP_SSL(server, port, context=context, timeout=30) as s:
            s.login(user, password)
            s.send_message(msg)
    else:
        with smtplib.SMTP(server, port, timeout=30) as s:
            s.ehlo()
            s.starttls(context=context)
            s.login(user, password)
            s.send_message(msg)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html", required=True)
    ap.add_argument("--json", required=True)
    ap.add_argument("--url", default="")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the message instead of sending it")
    args = ap.parse_args(argv)

    to = recipients(os.environ.get("MAIL_TO", ""))
    if not to:
        sys.stderr.write("MAIL_TO is empty — nothing to send.\n")
        return 0

    user = os.environ.get("MAIL_USERNAME", "")
    password = os.environ.get("MAIL_PASSWORD", "")
    server = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    port = int(os.environ.get("MAIL_PORT") or 587)

    if not args.dry_run and not (user and password):
        sys.stderr.write("MAIL_USERNAME and MAIL_PASSWORD must both be set.\n")
        return 1

    data = json.loads(Path(args.json).read_text(encoding="utf-8"))
    msg = build_message(data, Path(args.html), args.url, user or "map@localhost", to)

    if args.dry_run:
        sys.stdout.write(msg.get_body(("plain",)).get_content())
        return 0

    try:
        send(msg, server, port, user, password)
    except (smtplib.SMTPException, OSError) as exc:
        sys.stderr.write(f"send failed: {exc}\n")
        return 2
    sys.stderr.write(f"Sent to {len(to)} recipient(s).\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
