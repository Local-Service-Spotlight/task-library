---
name: verify-meta-pixel-installed-with-lead-events
description: "Check that the right site events reach the right ad account. Keep a click separate from a real lead."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify Meta pixel installed with lead events

An ad report should count the action that really happened. This guide helps you check the site’s event signals and where they go. Start with the agreed event map, not a guess that every click is a lead.

**The path:** Event plan → Browser behavior → Received event → Real business result.

**Use this when:** A site with an authorized Meta measurement setup needs its Pixel and intended lead-event behavior audited. A Pixel is browser-side event code; a separate server integration needs its own evidence.

## Inputs
- The exact site, expected business-controlled Pixel/data source and intended event map.
- Authorized read access to its current diagnostic tools and supported tag source; edit scope if repairs are included.
- The required consent behavior and controlled test receiver/identity for any real form, booking or other action.
- The current accessible provider event definitions and an event log recording browser/server origin, duplicates and actual business outcomes.

## First-run prompt

> Use the supplied Meta measurement plan and actual data-source access. Check event meaning, browser behavior, received origin and business outcome separately. Perform only authorized controlled actions, fix scoped faults using current supported guidance, and report consent, duplicate and evidence gaps without launching ads.

## Steps
1. Confirm the measurement setup is actually part of the site’s plan and belongs to the intended business. Do not install ad tracking on every audited site or create an ad campaign merely to satisfy this task.
2. Map each business action to its intended event and firing condition. A page view, phone-link click, accepted inquiry and completed booking are different outcomes. Use Lead only where the current event definition and measurement plan support it, not for every button or page visit.
3. Inspect the existing public tag source and controlled browser diagnostics for expected IDs and consent behavior. Record code presence and observed event attempts separately. Honor the site’s actual privacy controls rather than forcing blocked tags to run.
4. Use current supported provider diagnostics to inspect received events in the exact data source. An event shown in Events Manager is not automatically server-side evidence; record its actual reported connection/origin. The browser Pixel and Conversions API are distinct delivery paths.
5. Perform the real business-action test only when it is already authorized and has a controlled receiver. Verify the form/list/booking outcome separately from the event. A fired Lead event cannot prove the business received an inquiry.
6. Check whether one action is counted as intended. Unexpected repeated browser events or browser/server duplicates need investigation against the real integration’s deduplication design. Do not delete a valid second data source solely because the old checklist said exactly one Pixel.
7. Repair only the authorized event/source issue with the current supported implementation and documented event semantics. Inspect parameters and URLs for unintended private form data, preserve consent, and avoid fabricated customer records or paid actions.
8. Recheck the normal published configuration and actual received event evidence after changes. Save coverage, test identity privately, timestamps, expected/observed event and business result. If current provider docs or account access cannot be read, finish the bounded evidence review and keep the exact implementation question pending.

## Definition of done (QA checklist)

- [ ] The intended business-controlled source and event meanings are defined.
- [ ] Code presence, browser firing, received browser/server evidence and business delivery are separate results.
- [ ] Consent, controlled test scope and private data handling are preserved.
- [ ] One action’s actual counting/deduplication is checked under the real integration.
- [ ] Unverified current provider instructions or missing account evidence remain explicit, not a claimed live pass.

## Example(s)

**Fictional teaching example — no event or lead was created.** Maple Cycle’s sample quote button fires Lead when the form opens. The customer can close it without sending anything, so the event does not match the plan’s “accepted inquiry” definition.

The teaching repair waits for the actual accepted form result, then checks both the business receiver and the measured event. If the diagnostics show a browser event only, record browser receipt; do not label it a working server integration. A closed form should not be counted as a completed inquiry.

## Handoff and Content Factory context

The measurement owner receives the exact event/source issue. [Verify the actual form flow](https://local-service-spotlight.github.io/task-library/?task=verify-email-opt-in-form-exists-and-works#task-verify-email-opt-in-form-exists-and-works) supplies delivery evidence where relevant. A Conversions API implementation is separate work unless already in this job.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at setup and after relevant tag, consent or conversion-flow changes. Recurring live tests require a controlled identity, receiver and configured cadence; no campaign or repeat lead submission is started by this guide.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify Meta pixel installed with lead events](https://local-service-spotlight.github.io/task-library/?task=verify-meta-pixel-installed-with-lead-events#task-verify-meta-pixel-installed-with-lead-events)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Meta Pixel event reference — check current accessible version before implementation](https://developers.facebook.com/docs/meta-pixel/reference/)
- [Meta Conversions API — separate from browser Pixel evidence](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Meta event/reference and Conversions API pages returned 429 during this authoring pass; their contents and current menus were not verified. Recheck accessible current official instructions before an implementation change.
- The actual measurement plan, test receiver, privacy requirements, integration source and live event receipts require the project.
