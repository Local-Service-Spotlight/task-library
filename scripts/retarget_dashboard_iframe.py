#!/usr/bin/env python3
"""Point the public Task Library dashboard iframe at the org Pages site.

Prints replacement counts only — never page HTML.
"""
import sys
sys.path.insert(0, "/Users/dennisyu/Documents/Claude/tools")
from wp import WP  # noqa: E402

OLD_HOST = "goodrich-dev.github.io"
NEW_HOST = "local-service-spotlight.github.io"
PAGE_ID = 104693


def main():
    w = WP("blitzmetrics.com")
    p = w.get(f"/wp/v2/pages/{PAGE_ID}", context="edit")
    raw = (p.get("content") or {}).get("raw") or ""
    n_content = raw.count(OLD_HOST)
    payload = {}
    if n_content:
        payload["content"] = raw.replace(OLD_HOST, NEW_HOST)
    el = (p.get("meta") or {}).get("_elementor_data")
    n_el = 0
    if isinstance(el, str) and OLD_HOST in el:
        n_el = el.count(OLD_HOST)
        payload.setdefault("meta", {})
        payload["meta"]["_elementor_data"] = el.replace(OLD_HOST, NEW_HOST)
    print(f"content_replacements={n_content} elementor_replacements={n_el}")
    if not payload:
        print("nothing to change")
        return
    res = w.post(f"/wp/v2/pages/{PAGE_ID}", **payload)
    new_raw = (res.get("content") or {}).get("raw") or ""
    print("old_host_remaining", new_raw.count(OLD_HOST))
    print("new_host_present", new_raw.count(NEW_HOST))
    print("link", res.get("link"))


if __name__ == "__main__":
    main()
