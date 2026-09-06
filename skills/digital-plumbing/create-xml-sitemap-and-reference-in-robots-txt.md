---
name: create-xml-sitemap-and-reference-in-robots-txt
description: "Make a page list that search tools can read. Check that it lists the right public pages."
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: needs-work
---

# Create XML Sitemap and Reference in robots.txt

Search tools need a clear list of the pages you want people to find. This guide helps a site owner build and check that list. Start with your site’s real page list and the tool that already makes it.

**The path:** Public page plan → Sitemap → Discovery link → Submission evidence.

**Use this when:** a site launches, its sitemap is missing or stale, or a migration changes the pages meant for search.

## Inputs
- The canonical hostname and intended public, indexable pages, with drafts, private pages and deliberate exclusions identified.
- The actual sitemap owner: CMS, SEO plugin or generator, plus supported access to its settings and robots.txt source.
- The correct Search Console property and submission access if account submission is in scope. Public sitemap work does not itself prove that access.

## First-run prompt

> Find or generate the sitemap using the site’s existing supported source. Compare it with intended public canonical pages, add its real URL to robots.txt when appropriate, and verify the served files. Keep submission, processing and indexing as separate states.

## Steps
1. Discover any current sitemap through robots.txt, CMS settings and the actual generator. Preserve a valid existing custom or query-based URL; do not assume every site uses /sitemap_index.xml or install Rank Math just for that path.
2. Define the intended URL set. Include suitable canonical public pages and exclude drafts, private pages, duplicate redirects and intentional noindex pages. Taxonomies and archives need a real policy decision, not a blanket include or exclude rule.
3. Enable or configure the existing sitemap source to emit that set. If the site has no generator, create a valid XML sitemap through its supported publishing system. Use absolute canonical URLs and truthful modification dates when known.
4. Fetch and parse the XML with an XML-aware tool. If it is a sitemap index, open its child maps and count actual page URLs separately from child-map entries. Decode XML escaping correctly.
5. Compare the sitemap URLs with the intended set. Resolve missing key pages, broken destinations and stale hostnames at their owning source. A cross-host sitemap arrangement requires its actual supported verification setup; do not silently accept or reject it by string matching.
6. Add or correct the Sitemap declaration in the served robots.txt using the real complete sitemap URL. Preserve existing rules and the actual virtual or physical file source. A robots reference helps discovery but does not itself submit or index anything.
7. Open the ordinary public robots and sitemap URLs again. Check status, parseability and coverage after any supported cache refresh. Machine-readable files need valid machine content; they are not editorial pages requiring a lead image.
8. If submission is included, submit the real sitemap in the correct Search Console property and record its actual pending or processed result. Investigate reported fetch errors. Search Console success does not guarantee that every listed page is indexed.

## Definition of done (QA checklist)

- [ ] The actual sitemap URL and owning source are documented.
- [ ] XML parses; child maps and page counts are separated.
- [ ] The intended canonical public page set matches, with explained exclusions.
- [ ] Served robots.txt points to the working map without unintended crawl-rule changes.
- [ ] Submission, processing and indexing have distinct evidence or explicit unverified states.

## Example(s)

**Fictional teaching example.** A site has eight intended public pages and two private drafts. Its sitemap index contains two child maps, not two pages. Parsing the children yields seven public URLs; the missing repair page is enabled in the generator. The next read finds eight of eight intended pages and neither draft. The lesson records “public coverage passes; Search Console submission pending” if account access has not been supplied.

## Handoff and Content Factory context

Give the URL-set comparison to the search owner. Use [ensure robots meta not blocking indexing](https://local-service-spotlight.github.io/task-library/?task=ensure-robots-meta-not-blocking-indexing#task-ensure-robots-meta-not-blocking-indexing) for a conflicting index rule, or [verify google search console and connect to ga4](https://local-service-spotlight.github.io/task-library/?task=verify-google-search-console-and-connect-to-ga4#task-verify-google-search-console-and-connect-to-ga4) for the actual account connection.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Set up once; the generator should maintain the list as content changes. Recheck after migrations or generator changes. A recurring audit needs a configured trigger, not a model-name promise.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. Use the maintained owned training below until that article gap is reviewed.
- Exact task: [Create XML Sitemap and Reference in robots.txt](https://local-service-spotlight.github.io/task-library/?task=create-xml-sitemap-and-reference-in-robots-txt#task-create-xml-sitemap-and-reference-in-robots-txt)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [Google sitemap creation and submission](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google robots meta and headers](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- No dedicated canonical article is mapped in this source record. Actual intended-page policy and generator access must be supplied for execution.
