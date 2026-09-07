---
name: ensure-robots-meta-not-blocking-indexing
description: "Check that public pages can be found by search tools. Keep private pages out on purpose."
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: needs-work
---

# Ensure Robots Meta Not Blocking Indexing

A page can be live and still tell search tools to leave it out. This guide helps a site owner find and fix that mistake. Start with the pages you want people to find.

**The path:** Page intent → Crawl and index rules → Scoped fix → Eligibility check.

**Use this when:** a launch or migration may have carried over staging rules, or intended public pages have unexpected indexing restrictions.

## Inputs
- The intended indexable page list and deliberate exclusions such as private, staging or thank-you pages.
- Read access to served HTML, HTTP headers and robots.txt, plus editing access to the actual CMS, plugin or host source involved.
- The correct Search Console property and inspection access if account verification is in scope.

## First-run prompt

> Check the supplied pages for unintended crawl and index restrictions. Preserve deliberate exclusions. Fix the actual owning source within scope and verify the served result. Keep indexing eligibility separate from a promise that Google will index or rank the page.

## Steps
1. Record each page’s intent: meant for search or deliberately excluded. Include representative home, service and article pages, but do not assume that every page on a live domain should be indexed.
2. On WordPress, inspect the Reading setting that discourages search engines only when WordPress owns the site. Check the current SEO plugin defaults and per-page rules; other platforms have different sources.
3. Read served HTML for robots and crawler-specific directives, and inspect HTTP X-Robots-Tag headers. A noindex rule concerns indexing; nofollow concerns following links. They are not interchangeable, and restrictive rules can combine across sources.
4. Read robots.txt for relevant crawl disallows. Crawl blocking may prevent Google from seeing a page’s noindex rule and does not reliably keep its URL out of search. Do not add unsupported noindex text to robots.txt.
5. Trace each unintended rule to the setting, template, plugin or host response that supplies it. Save the before state, then make the smallest authorized correction at that source. Preserve intentional private or duplicate-page exclusions.
6. Fetch the ordinary public response again after the supported cache process. Check both HTML and headers; a corrected editor checkbox alone does not prove the served page changed. Keep crawler-specific and page-specific tests explicit.
7. If Search Console access is included, compare the last indexed snapshot with a live inspection. Record whether the current page allows indexing and any other reported obstacle. Request indexing only within the actual scope; submitting a request is not a guaranteed index event.
8. Save the page-by-page result, intended exclusions, source changes and remaining search status. If a rule returned from a deployment template, give its source owner the exact recurrence cause for a durable fix.

## Definition of done (QA checklist)

- [ ] Every checked page has a recorded search intent.
- [ ] No unintended restrictive rule remains in the served HTML, headers or crawl policy for those pages.
- [ ] Intentional exclusions remain intact and have a reason.
- [ ] Public response and any Search Console checks are dated and distinguished from older snapshots.
- [ ] Eligibility, request submission, actual indexing and ranking are not collapsed into one pass.

## Example(s)

**Fictional teaching example.** A new repair page should be searchable but returns X-Robots-Tag: noindex from a staging rule. The site’s thank-you page is intentionally excluded. The guide removes the inherited staging header from the public repair page and preserves the thank-you rule. The follow-up response shows indexing allowed for the repair page. The lesson result is “restriction fixed,” not “Google now ranks this page.”

## Handoff and Content Factory context

Give the exact policy and changed source to the site/search owner. Use [create xml sitemap and reference in robots txt](https://local-service-spotlight.github.io/task-library/?task=create-xml-sitemap-and-reference-in-robots-txt#task-create-xml-sitemap-and-reference-in-robots-txt) to check page discovery or the configured deployment owner to prevent a staging-rule recurrence.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch, after migrations or template changes, and when a real indexing issue is reported. A recurring check needs the intended-page policy and a configured trigger.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. Use the maintained owned training below until that article gap is reviewed.
- Exact task: [Ensure Robots Meta Not Blocking Indexing](https://local-service-spotlight.github.io/task-library/?task=ensure-robots-meta-not-blocking-indexing#task-ensure-robots-meta-not-blocking-indexing)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [Google robots meta and headers](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [Google sitemap creation and submission](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- No dedicated canonical article is mapped. Actual intended-page policy and optional Search Console evidence are required for execution.
