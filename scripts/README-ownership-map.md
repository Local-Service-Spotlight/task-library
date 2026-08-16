# Ownership map

Daily “who owns what” map for `Local-Service-Spotlight`.

## Files

- `.github/workflows/ownership-map.yml` — daily job
- `scripts/build_ownership_map.py` — generator
- `scripts/template.html` — page (data injected at `__DATA__`)
- `scripts/send_map_email.py` — optional mailer
- `scripts/test_*.py` — 87 tests, no network

## Remaining human step

Create a fine-grained PAT, resource owner `Local-Service-Spotlight`, all repositories, **Contents: Read-only** and **Metadata: Read-only**. Save it as org secret `OWNERSHIP_MAP_TOKEN`.

`GITHUB_TOKEN` alone will not work: it is scoped to one repository and cannot see the other nine.

Pages source is already GitHub Actions. Leave `MAIL_TO` unset until you want the morning email.

Preview offline:

```
python3 scripts/build_ownership_map.py --sample --out preview.html
```

This workflow writes the map into `dashboard/` and uploads that whole tree, so it cannot wipe the Task Library dashboard.
