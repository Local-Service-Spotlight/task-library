---
name: step-1-inventory-content-and-establish-gct-per-page
description: "Audit every URL on the site into one inventory and write Goals, Content, Targeting for each major page — the foundation document the entire 6-step internal linking process runs on."
category: SEO & Content Architecture
stage: —
definitive_article: /internal-linking
status: complete
---

# Step 1: Inventory content and establish GCT per page

**Use this when** starting the 6-step internal linking process (/internal-linking) from the top, or whenever the content inventory has gone stale.

## Inputs
- Export of every published URL: posts, pages, landing pages
- Crawl or LinkWhisper data for internal links in/out per URL
- The GCT framework: Goals, Content, Targeting

## Steps
1. Export every published URL into one working sheet with columns: URL, title, category, tags, publish date.
2. Add link data per URL: internal links in, internal links out (from the crawl or LinkWhisper report).
3. For every major page, write its GCT — **Goal**: what the page must accomplish (rank, convert, prove); **Content**: what it actually covers; **Targeting**: who it serves.
4. Mark each page's SEO Tree role: root, trunk, branch (definitive article), or leaf (case study / meta-article).
5. Flag pages with no defensible GCT — they are candidates for the orphan-elimination and thin-page-removal skills, not for new links.
6. Save the inventory as the single working document for Steps 2–6 of the internal linking process.

## Definition of done (QA checklist)
- [ ] Existing page rows retain the exact opening/revision and `step-7-write-hook-and-establish-context` review for reader/situation, reason to care, useful outcome and supporting mechanism; unchecked pages stay UNKNOWN, and failures route to the existing owner
- [ ] Every published URL present in one inventory — nothing missing from the sitemap or crawl
- [ ] GCT written for every major page; no blanks on money pages
- [ ] SEO Tree role marked for every URL; links in/out counts populated
- [ ] No-GCT pages flagged and routed for consolidation
- [ ] Linked back to the definitive article (/internal-linking) and ready to hand to Step 2

## Example(s)
- The /internal-linking definitive article — the hub that "includes skill file for AI agents" — documents this step as it was run on blitzmetrics.com.
- Example needed — run the Meta-Article Prompt (/meta-article-prompt-template) after the next full inventory.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude Fable 5 or a comparable OpenAI/Google model) builds the inventory and loops until the Definition of done fully passes — every URL from sitemap and crawl present, GCT on every major page, zero blanks on money pages — verifying by diffing the finished sheet against a fresh crawl rather than declaring it complete.
The inventory is the persistent artifact: held in memory, each re-run diffs new and changed URLs instead of rebuilding from zero, which is what keeps Steps 2–6 honest.
Each full inventory pass logs a meta-article example via /meta-article-prompt-template.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /internal-linking
- Related (run order): step-2-fix-categories-and-tags-in-wordpress → step-3-identify-money-pages-and-orphan-pages → step-4-create-links-with-proper-anchor-text-and-placement → step-5-qa-links-against-google-guidelines → step-6-measure-and-iterate-with-maa · map-content-hierarchically-root-trunk-branches-leaves (/seo-tree)
