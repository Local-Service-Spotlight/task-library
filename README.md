# BlitzMetrics Task Library

Hub-and-spoke skill library. This repo is the **hub**: the registry, the dashboard, and the default home for skill files. Skills can also live in their owner's own repo (the **spokes**) — the build pulls them in at build time.

## Layout

```
skills/<category-folder>/<slug>.md   skill files that live in this repo ("local")
build/registry.json                  slug -> source; THE index of the library
build/categories.json                the 13 categories (order, icons, colors)
build/site-meta.json                 meta-article URL (counts and build date are derived)
build/build.py                       resolve -> validate -> compose dashboard/data.json
dashboard/                           index.html + app.js + generated data.json
Task-Library-Standard.md             the spec every skill.md must meet
.github/workflows/build.yml          CI: build + deploy to GitHub Pages
```

> **Bringing your own skill repo?** See [CONTRIBUTING-SKILLS.md](CONTRIBUTING-SKILLS.md) — the full guide to formatting and registering an external skill (spoiler: if it's a normal Claude skill, it already qualifies).

## Owning a skill in your own repo

Nobody edits this repo to own a skill. Everything happens in the **Asset Tracker's Task Library sheet**:

1. Put your `SKILL.md` in your repo at `skills/<slug>/SKILL.md` (standard Claude skill format — `name` + `description` frontmatter, `name` = the slug).
2. On your skill's row in the sheet: put your name in **Owner**, your repo URL in **Source Repo**, and set **Status** (`wip` while you work it, `ready` when you stand behind it).
3. Done. The next build (daily, or manual run) fetches your file, and if a hub draft existed it's superseded automatically. From then on you only ever push to your own repo.

The precedence rule: **sheet beats registry beats hub file** — a skill has exactly one live source, and the sheet's Source Repo cell is the switch. The Slug column completes the address, so a bare repo URL is enough when you follow the standard layout; use a deeper `/tree/` or `/blob/` link only if your file lives elsewhere.

`build/registry.json` is maintainer plumbing, not a contributor surface: it holds the hub-resident skills and the advanced cases (commit-SHA pinning, release-asset downloads). Fetch failures fall back to the last good cached copy, so a deleted repo never blanks the dashboard. Private repos need `SKILLS_READ_TOKEN` set in Actions secrets.

## Validation

`build/build.py` rejects skills that: lack frontmatter or any required field, have `name` ≠ slug, use an unknown category/stage/status, or miss required sections (Inputs, Steps, Definition of done, Examples, Definitive article & links). It warns (build passes) on: stub language in a `complete` skill, <3 numbered steps, frontmatter/registry category mismatch.

## Asset Tracker

The Asset Tracker's *Task Library* tab stays the ops-facing index (status, owner, flags). Publish it to web as CSV and set `TRACKER_CSV_URL` repo variable — the build then overrides `status`/`owner`/`article` per slug from the sheet. Content always comes from git; workflow state comes from the sheet.

The sheet is also the **onboarding path**: a row whose Slug isn't in the registry but has a Source Repo link becomes a new external skill on the next build — no PR to this repo needed. See CONTRIBUTING-SKILLS.md.

## SEO

The dashboard itself is `noindex` (it's a utility, not the ranking surface — and it must never compete with the hub articles from a github.io origin). The build also emits **`dashboard/library-index.html`**: a plain semantic HTML fragment — category H2s, every task with its description, and links to mapped article hubs. Its summary derives the number of mapped hubs and the subset that is actually definitive from task status. Paste it into the WordPress task-library page *below* the iframe (or template it in) so blitzmetrics.com serves an indexable representation of the library with internal links to the hubs. Refresh the paste when categories/articles change materially; the fragment is deterministic, so a diff shows when.

## Local build

```
python3 build/build.py          # writes dashboard/data.json + library-index.html, exit 1 on validation errors
```
