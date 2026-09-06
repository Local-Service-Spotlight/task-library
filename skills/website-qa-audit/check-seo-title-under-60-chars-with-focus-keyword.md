---
name: check-seo-title-under-60-chars-with-focus-keyword
description: "Check that each page has a clear title. Use words that fit the page and help people choose it."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Check SEO title under 60 chars with focus keyword

A clear title tells people what they will find. This guide helps you check the page name used by browsers and search. Start by reading the live page and its real title tag.

**The path:** Page purpose → Served title → Clear wording → Canonical recheck.

**Use this when:** A page set needs its browser/search titles reviewed before launch or after content changes.

## Inputs
- The exact public pages, actual content and intended topics.
- The served title tags, visible H1 headings and supported CMS/SEO template settings if edits are in scope.
- The current house title-length target and brand naming rules.
- A dated report with URL, before/after title and counting method.

## First-run prompt

> Read the supplied pages and served title tags. Correct misleading or weak titles within the authorized scope, use the house length target as guidance, and verify live source without changing stable URLs. Report exact text, count and any template or delivery gap.

## Steps
1. Read each page’s purpose. Identify what a reader should expect there and whether it is a guide, service page, story or reference. Choose specific words that reflect the content.
2. Inspect the served HTML title, the visible main heading and the CMS value. These can differ because of templates or stale delivery. Record blank titles, duplicate declarations and misleading generated text.
3. Review concision and useful topic wording. The old task name’s 60-character target is a house guideline, not a Google limit. Google may truncate by display width and may construct a different title link from other page signals.
4. Use the natural main topic where it helps clarity. A Rank Math focus-keyword field is an editorial aid, not a required search-engine input. Avoid repetitive keyword lists or a promise that the page cannot support.
5. Assess repeated titles in context. Distinct useful pages usually need distinct clear titles; similar variants may have another canonicalization issue. A normal “Page title | Brand” format can be valid and is not automatically unfinished.
6. Write or apply the authorized title through the supported source. Keep the page’s existing URL and content type. Do not change a stable slug merely to satisfy the keyword phrase or character target.
7. Reopen the normal canonical source and browser tab to verify the actual title. Record H1 consistency without forcing exact duplication where a useful editorial variation makes sense.
8. Save before/after text, character count, house-target exceptions and checked date. A search preview is a simulation; only a dated actual search result shows what Google displayed then, and neither promises future ranking.

## Definition of done (QA checklist)

- [ ] The actual served title clearly and truthfully represents the page.
- [ ] The approximate 60-character house target is not labeled a Google requirement.
- [ ] Topic wording is natural and template/duplicate issues are reviewed in context.
- [ ] Authorized changes preserve the canonical URL and survive public source readback.
- [ ] Browser title, H1 and observed Google title link remain distinct evidence fields.

## Example(s)

**Fictional teaching example — no title was saved.** Maple Cycle’s quote guide uses “Home | Maple Cycle” because an old template value was copied.

The teaching title is “Bike repair photos to send | Maple Cycle.” It names the guide and retains the real brand. The editor checks the decoded character count and the actual served tag. There is no need to rename the established `/repair-quote/` URL.

A separate brake-wear guide should use its own specific title; forcing “bike repair quote” into both titles would make their purposes less clear.

## Handoff and Content Factory context

The content owner receives the title report. [Check search summaries](https://local-service-spotlight.github.io/task-library/?task=check-meta-description-under-160-chars#task-check-meta-description-under-160-chars) follows as a related metadata task; the title check alone does not complete it.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run for new pages and material topic/template changes. An existing search review can observe later title links; this guide does not schedule one automatically.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Check SEO title under 60 chars with focus keyword](https://local-service-spotlight.github.io/task-library/?task=check-seo-title-under-60-chars-with-focus-keyword#task-check-seo-title-under-60-chars-with-focus-keyword)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google title links](https://developers.google.com/search/docs/appearance/title-link)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The actual title template, page topics and canonical served checks remain site-specific.
