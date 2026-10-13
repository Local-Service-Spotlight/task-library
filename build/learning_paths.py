"""Public learning paths composed from the existing pack source and resolved tasks.

Never load private workshop inventories here. This allowlisted projection contains
only existing public task metadata and reviewed public teaching-path metadata.
"""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlencode

TRIANGLES = {
    "SBP": ["Specialist", "Business", "Partner"],
    "AEC": ["Audience", "Engagement", "Conversion"],
    "GCT": ["Goals", "Content", "Targeting"],
    "MAA": ["Metrics", "Analysis", "Action"],
    "DDD": ["Do", "Delegate", "Delete"],
    "CID": ["Communicate", "Iterate", "Delegate"],
    "LDT": ["Learn", "Do", "Teach"],
    "CCS": ["Content", "Checklist", "Software"],
    "MOF": ["Marketing", "Operations", "Finance"],
}
FRAMEWORK = {
    "version": "2026-08-06",
    "acceptanceStatus": "Accepted by framework owner Dennis Yu.",
    "decisionDate": "2026-08-09",
    "decisionTimezone": "America/Los_Angeles",
    "acceptingCommit": "3a82b85071e47a9e4ee336cec854d3e004ff0c5f",
    "sourceReference": "nine-triangles/references/canonical-framework.md",
    "triangles": TRIANGLES,
}
PATH_FIELDS = {"id", "title", "audience", "goal", "governingTriangle",
               "prerequisites", "boundary", "lessonSlugs", "exercise", "sessionMinutes"}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: nonempty text required")
    if "<" in value or ">" in value or "\x00" in value:
        raise ValueError(f"{label}: plain text only")
    return value


def strings(value, label):
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label}: nonempty list required")
    return [text(v, label) for v in value]


def https_url(value, label, optional=False):
    if value is None and optional:
        return None
    p = urlsplit(text(value, label))
    if p.scheme != "https" or not p.netloc or p.username or p.password:
        raise ValueError(f"{label}: public HTTPS URL required")
    return value


def compose(data, source):
    paths = source.get("learningPaths")
    if not isinstance(paths, list) or not paths:
        raise ValueError("learningPaths: nonempty list required")
    tasks = {}
    for category in data["categories"]:
        for task in category["tasks"]:
            slug = task["slug"]
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug) or slug in tasks:
                raise ValueError(f"invalid or duplicate task slug: {slug}")
            # Do not copy task internals, source credentials, reviews or arbitrary
            # newly added fields into this public projection.
            tasks[slug] = {
                "slug": slug,
                "title": text(task["title"], "title"),
                "description": text(task["desc"], "description"),
                "article": https_url(task.get("article"), "article", optional=True),
                "taskLibraryUrl": https_url(task.get("taskLibraryUrl") or
                    data["taskLibraryUrl"].rstrip("/") + "/?" +
                    urlencode({"task": slug}) + "#task-" + slug, "taskLibraryUrl"),
                "status": task["status"],
                "contentSha256": hashlib.sha256(task["content"].encode()).hexdigest(),
            }
    result, ids = [], set()
    for item in paths:
        if set(item) != PATH_FIELDS:
            raise ValueError("unknown/missing path fields; never embed protected material")
        pid = text(item["id"], "id")
        if not SLUG.fullmatch(pid) or pid in ids:
            raise ValueError(f"invalid or duplicate path id: {pid}")
        ids.add(pid)
        for key in ("title", "audience", "goal", "boundary"):
            text(item[key], key)
        if item["governingTriangle"] not in TRIANGLES:
            raise ValueError("unknown Nine Triangles identifier")
        strings(item["prerequisites"], "prerequisites")
        slugs = strings(item["lessonSlugs"], "lessonSlugs")
        if len(set(slugs)) != len(slugs) or any(s not in tasks for s in slugs):
            raise ValueError(f"{pid}: duplicate or unresolved lesson")
        ex = item["exercise"]
        if not isinstance(ex, dict) or set(ex) != {"prompt", "deliverable", "checks"}:
            raise ValueError("exercise: public practice fields only")
        text(ex["prompt"], "prompt")
        text(ex["deliverable"], "deliverable")
        strings(ex["checks"], "checks")
        if type(item["sessionMinutes"]) is not int or item["sessionMinutes"] not in (10, 30, 60):
            raise ValueError("sessionMinutes: supported planning estimate required")
        result.append(item)
    return {"version": 1, "framework": FRAMEWORK,
            "libraryUpdated": data["updated"], "paths": result,
            "tasks": sorted(tasks.values(), key=lambda t: t["slug"])}


def write(data, pack_source, output_dir):
    source = json.loads(Path(pack_source).read_text())
    output = compose(data, source)
    target = Path(output_dir) / "learning-paths.json"
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    return output


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    write(json.loads((root / "dashboard/data.json").read_text()),
          root / "build/packs.json", root / "dashboard")
