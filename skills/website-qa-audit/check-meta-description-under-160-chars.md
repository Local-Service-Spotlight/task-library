---
name: check-meta-description-under-160-chars
description: "Give each page a clear short search summary. Check what the live page actually sends."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Check meta description under 160 chars

A clear search summary helps people know what a page offers. This guide helps you check that summary and trim weak words. Start with the live page, since a saved draft may say something else.

**The path:** Page purpose → Served summary → Useful wording → Saved and live check.

**Use this when:** A defined set of public pages needs its meta descriptions checked. A meta description is the page’s suggested search summary.

## Inputs
- The exact public pages and intended search topics, with intentional private/non-indexable pages identified.
- Public source inspection and supported CMS/SEO metadata access for authorized changes.
- The actual page content and any current house length target.
- A report with URL, served description, character-count method and result.

## First-run prompt

> Read each supplied page and its actual served description. Draft or apply authorized specific summaries, record the house length target separately from Google behavior, and verify the canonical result. Return exact text, count method and unresolved delivery issues without promising search display.

## Steps
1. Define the page set. A page listed by a crawler is not proof that Google indexed it. Separate intended public search pages from private or deliberately excluded pages.
2. Read the actual meta name="description" content in the served page and compare it with the saved source setting where access is available. Note blank, duplicate or conflicting declarations and site templates that generate unexpected text.
3. Read the page’s purpose and proposed summary together. Write a specific truthful sentence or two that tells the reader what is useful. Use the topic’s normal words naturally; a plugin’s focus keyword is not a compulsory phrase in every description.
4. Treat roughly 160 characters as the existing house brevity target, not a Google technical maximum. Google has no fixed meta-description length limit and may use page text or truncate a snippet to the display width. Keep any justified longer description distinct from a factual failure.
5. Count the decoded text using a stated method, then review clarity, repeated boilerplate and misleading claims. Duplicate summaries deserve page-context review; do not force meaningless unique wording on equivalent variants just to satisfy a count.
6. Update the correct supported metadata source for authorized pages. Preserve canonical URLs, titles and visibility unless those changes are separately part of the job. Avoid writing a second description tag into body content.
7. Reopen the canonical page and verify the actual served description. Record saved-but-stale delivery separately if a cache or static layer still shows the old tag.
8. Save the before/after summary, count, reason for any house-target exception and public check date. Observed search snippets are a separate dated observation; this edit cannot promise a specific snippet or click-through increase.

## Definition of done (QA checklist)

- [ ] Each intended page has a truthful useful served description or a precise unresolved issue.
- [ ] The house length target is recorded separately from Google requirements.
- [ ] Descriptions fit page content and are not keyword-stuffed or copied blindly.
- [ ] Changes preserve unrelated URL/visibility settings and are checked on canonical source.
- [ ] Search display and traffic claims are not inferred from the metadata edit.

## Example(s)

**Fictional teaching example — no search metadata was saved.** Maple Cycle’s quote guide has the summary “Welcome to our website, the best service for everyone.” It says little about this page.

The teaching replacement is “See which bike photos to send for a repair quote, what details to include, and when the shop needs to inspect it.” The editor counts the actual decoded string and checks the house target. The main test is that the sentence accurately describes the guide.

If Google later shows a different excerpt for one query, that alone does not mean the description tag was missing or broken.

## Handoff and Content Factory context

The content owner receives the metadata report. [Check page titles](https://local-service-spotlight.github.io/task-library/?task=check-seo-title-under-60-chars-with-focus-keyword#task-check-seo-title-under-60-chars-with-focus-keyword) is a related check, not evidence that descriptions have been tested.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at page launch or when its purpose or summary changes. Search-result observations follow an existing review cadence rather than a guaranteed instant update.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Check meta description under 160 chars](https://local-service-spotlight.github.io/task-library/?task=check-meta-description-under-160-chars#task-check-meta-description-under-160-chars)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google snippets](https://developers.google.com/search/docs/appearance/snippet)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The actual page set, current metadata and canonical readback require the site.
