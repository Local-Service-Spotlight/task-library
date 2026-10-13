"""Strict, link-only projection of reviewed teaching materials.

No downloader, private catalog, paid lesson content or authentication belongs here.
The manifest contains public source/entry metadata, reviewed before release.
"""
import hashlib
import json
import re
from datetime import datetime
from urllib.parse import urlsplit, parse_qs

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA = re.compile(r"^[a-f0-9]{64}$")
MATERIAL_FIELDS = {"id", "title", "kind", "access", "url", "sourceOwner",
                   "sourceVersion", "checkedAt", "useNote", "pathIds", "verification"}
SESSION_FIELDS = {"id", "title", "pathId", "audience", "goal", "minutes",
                  "materialIds", "steps", "deliverable", "checks", "sourceVersion"}
HOSTS = {"dennisyu.com", "blitzmetrics.com", "digimarcon.com",
         "localservicespotlight.com", "www.youtube.com", "youtu.be"}


def plain(value, label):
    if not isinstance(value, str) or not value.strip() or any(c in value for c in "<>\x00"):
        raise ValueError(f"{label}: nonempty plain text required")
    return value


def identifier(value):
    if not SLUG.fullmatch(plain(value, "id")):
        raise ValueError("invalid material/session id")
    return value


def ids(value, known, label, allow_empty=False):
    if (not isinstance(value, list) or (not value and not allow_empty)
            or any(not isinstance(v, str) for v in value)
            or len(set(value)) != len(value) or any(v not in known for v in value)):
        raise ValueError(f"{label}: duplicate or unresolved reference")


def public_url(value):
    p = urlsplit(plain(value, "url"))
    if (p.scheme != "https" or p.hostname not in HOSTS or p.username or p.password
            or p.port is not None or "\\" in value or "%" in value):
        raise ValueError("material URL must use a reviewed public host")
    if p.hostname == "www.youtube.com":
        if p.path != "/watch" or set(parse_qs(p.query)) != {"v"} or not re.fullmatch(r"v=[A-Za-z0-9_-]{11}", p.query):
            raise ValueError("only exact public YouTube watch links are supported")
    elif p.hostname == "youtu.be":
        if p.query or not re.fullmatch(r"/[A-Za-z0-9_-]{11}", p.path):
            raise ValueError("invalid public recording link")
    elif p.query:
        raise ValueError("signed, tokenized and query-bearing source links are not supported")
    if re.search(r"/(?:wp-admin|wp-json|private|instructor|offline|lesson|lessons|account)(?:/|$)", p.path, re.I):
        raise ValueError("protected asset path cannot enter the public catalog")
    return p


def compose(source, paths):
    known_paths = {p["id"] for p in paths}
    materials = source.get("teachingMaterials", [])
    sessions = source.get("practiceSessions", [])
    if not isinstance(materials, list) or not isinstance(sessions, list):
        raise ValueError("materials and sessions must be lists")
    result, known = [], {}
    for item in materials:
        if not isinstance(item, dict) or set(item) != MATERIAL_FIELDS:
            raise ValueError("material: unknown/missing fields; no protected source data")
        mid = identifier(item["id"])
        if mid in known:
            raise ValueError("duplicate material id")
        for key in ("title", "sourceOwner", "sourceVersion", "useNote"):
            plain(item[key], key)
        if item["kind"] not in {"deck", "recording", "exercise", "workbook", "course"}:
            raise ValueError("unknown material kind")
        if item["access"] not in {"public", "protected-entry"}:
            raise ValueError("unknown access tier")
        url = public_url(item["url"])
        if item["access"] == "protected-entry":
            if item["kind"] != "course" or url.hostname not in {"blitzmetrics.com", "localservicespotlight.com"} or "/wp-content/" in url.path:
                raise ValueError("protected entry must be a public course information page, never a file")
        if item["kind"] == "course" and item["access"] != "protected-entry":
            raise ValueError("course content is not a public asset")
        try:
            dt = datetime.fromisoformat(item["checkedAt"].replace("Z", "+00:00"))
            if dt.utcoffset() is None:
                raise ValueError("timezone missing")
        except (AttributeError, TypeError, ValueError) as exc:
            raise ValueError("checkedAt needs an ISO timestamp and timezone") from exc
        ids(item["pathIds"], known_paths, "material paths", allow_empty=True)
        verification = item["verification"]
        if (not isinstance(verification, dict) or set(verification) != {"method", "status", "sha256"}
                or verification["method"] != "anonymous-get" or type(verification["status"]) is not int
                or verification["status"] != 200 or not SHA.fullmatch(str(verification["sha256"]))):
            raise ValueError("material needs a dated successful anonymous source check")
        known[mid] = item
        result.append(dict(item))
    examples, seen = [], set()
    for item in sessions:
        if not isinstance(item, dict) or set(item) != SESSION_FIELDS:
            raise ValueError("session: unknown/missing fields")
        sid = identifier(item["id"])
        if sid in seen:
            raise ValueError("duplicate session id")
        seen.add(sid)
        for key in ("title", "audience", "goal", "deliverable", "sourceVersion"):
            plain(item[key], key)
        if item["pathId"] not in known_paths:
            raise ValueError("unresolved session path")
        if type(item["minutes"]) is not int or not 10 <= item["minutes"] <= 180:
            raise ValueError("session time is a 10–180 minute planning estimate")
        ids(item["materialIds"], known, "session materials")
        if any(known[m]["access"] != "public" for m in item["materialIds"]):
            raise ValueError("public rehearsal must not depend on paid access")
        if any(item["pathId"] not in known[m]["pathIds"] for m in item["materialIds"]):
            raise ValueError("session material must fit the same reviewed path")
        if not isinstance(item["steps"], list) or not item["steps"]:
            raise ValueError("ordered session steps required")
        for step in item["steps"]:
            if not isinstance(step, dict) or set(step) != {"title", "instruction", "materialIds"}:
                raise ValueError("step: public instructions only")
            plain(step["title"], "step title")
            plain(step["instruction"], "instruction")
            ids(step["materialIds"], item["materialIds"], "step materials", allow_empty=True)
        if not isinstance(item["checks"], list) or not item["checks"]:
            raise ValueError("session checks required")
        for check in item["checks"]:
            plain(check, "check")
        example = dict(item)
        example["contentSha256"] = hashlib.sha256(json.dumps(item, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        examples.append(example)
    return result, examples
