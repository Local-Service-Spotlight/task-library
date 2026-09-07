---
name: verify-xml-sitemap-exists-and-in-robotstxt
description: "Check the map that helps search tools find pages. Use the real map address and the right page list."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify XML sitemap exists and in robots.txt

Search tools need a clear list of the pages you want found. This guide helps you check that list and where it is shared. Start with the site’s real sitemap address, not a file name guessed from another site.

**The path:** Actual sitemap → Intended canonical URLs → Discovery records → Exact gaps.

**Use this when:** A launch, migration or search audit needs sitemap discovery, contents and recorded submission checked.

## Inputs
- The canonical site, intended public/indexable URL inventory and deliberate exclusions.
- The actual sitemap provider/configuration, robots.txt and current sitemap/index URLs.
- Supported source access for repairs, plus Search Console access when its processing/submission evidence is in scope.
- A report for listed URLs, reachable child maps, duplicates, missing intended pages and excluded variants.

## First-run prompt

> Use the supplied site and intended canonical-page inventory. Find and parse the actual configured sitemap, compare its contents and robots reference, and inspect Search Console only with actual access. Make authorized supported-source fixes and return public versus account evidence separately without promising indexing.

## Steps
1. Read robots.txt and the site’s supported sitemap settings to find the actual address. It may be an index, a core WordPress sitemap, a custom path or a query URL. A 404 at /sitemap_index.xml does not fail a site with another valid configured sitemap.
2. Read the real response and parse its contents as the intended sitemap format, not an HTML error behind a 200 status. For an index, follow and check its child sitemaps and count unique page URLs separately from index entries.
3. Compare listed URLs with intended canonical public search pages, not every CMS row. Drafts, private pages, noindexed variants and intentionally excluded archives need not be added just to match a total. Investigate meaningful missing pages and stale/redirecting entries.
4. Check representative or fully scoped listed URLs for actual status, canonical destination and visibility intent, recording coverage. A crawler cannot alone find every unlinked CMS page; use the known inventory too.
5. Verify the robots Sitemap declaration points to the actual accessible map as required by the house checklist. Google also accepts other submission methods, so a missing robots line is a house discovery gap rather than proof the map can never be found.
6. In the correct Search Console property, inspect the actual submission/processing status and last-read date when access exists. An authorized submission can be made under the existing job, but submitted, processed and indexed URLs are different states. Without access, finish public checks and leave this account result unknown.
7. Repair the exact supported sitemap/robots source already in scope. Do not cycle an unrelated SEO plugin or replace a valid map path by habit. Preserve private exclusions and intentional verified cross-site configurations.
8. Recheck the normal sitemap and robots responses after changes and record current Search Console evidence separately. A successful submission is a hint, not a guarantee Google downloads, indexes or ranks every listed page.

## Definition of done (QA checklist)

- [ ] The real configured sitemap and child maps parse and are accessible in the scoped checks.
- [ ] Contents match intended canonical public pages, with exclusions and coverage explicit.
- [ ] The house robots declaration uses the actual map, while alternative Google discovery methods remain recognized.
- [ ] Search Console submission, processing and actual indexing remain separate evidence states.
- [ ] Authorized source changes are publicly rechecked without inventing path or plugin requirements.

## Example(s)

**Fictional teaching example — no sitemap was requested.** Maple Cycle’s robots file names `https://maplecycle.example/?sitemap=1`. That map contains the intended public pages. The familiar `/sitemap_index.xml` URL returns 404.

The audit follows the declared valid map, rather than disabling and re-enabling a plugin to force another path. A private staff page is correctly absent. If Search Console access is missing, the public-map result can be recorded while processing status remains unknown.

## Handoff and Content Factory context

The search/site owner receives exact missing or stale URL findings. [Check index visibility rules](https://local-service-spotlight.github.io/task-library/?task=ensure-robots-meta-not-blocking-indexing--qa-audit#task-ensure-robots-meta-not-blocking-indexing--qa-audit) verifies a separate reason a listed page may still be excluded.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and after content-visibility, sitemap or migration changes. A new sitemap read/index observation needs the existing configured review or a named manual owner.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify XML sitemap exists and in robots.txt](https://local-service-spotlight.github.io/task-library/?task=verify-xml-sitemap-exists-and-in-robotstxt#task-verify-xml-sitemap-exists-and-in-robotstxt)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google sitemap creation and submission](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google robots meta and headers](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual sitemap provider, intended public inventory and Search Console readback require the site.
