---
name: ensure-site-loads-under-3-seconds-on-mobile
description: "Find what slows your site on a phone. Make a small fix and check the result."
category: Digital Plumbing
stage: —
definitive_article: /digital-plumbing
status: needs-work
---

# Ensure Site Loads Under 3 Seconds on Mobile

A slow page can make a visitor give up. This guide helps a site owner find and fix the main delay on a phone. Start by testing the pages that matter most, then save the results.

**The path:** Baseline → One useful fix → Same test → Business checks.

**Use this when:** key mobile pages are slow, performance regresses, or a launch needs a defined mobile speed check.

## Inputs
- The home page and top landing pages, chosen from actual traffic or the launch plan.
- The named metric and test conditions for the house under-three-second target. If none is set, define it before work; do not equate a PageSpeed score with elapsed seconds.
- Access to the responsible image, template, script or cache source and a rollback plan; existing performance and consent requirements.

## First-run prompt

> Measure the supplied mobile pages under stated conditions. Fix the largest supported cause within scope and re-test the same metric. Keep lab results, real-user data and real-phone observations separate. Preserve forms, accessibility, consent and necessary tracking.

## Steps
1. State the measurement contract: pages, mobile test tool, conditions and timing metric. For example, use mobile lab Largest Contentful Paint, the time until the main visible content appears, as the house under-three-second target. That is not proof that the whole page has finished loading.
2. Save at least two comparable baseline runs per page and use the slower run for this house check. Record scores separately from timings. In PageSpeed Insights, distinguish current lab tests from the available 28-day field data and note whether field scope is the URL or wider origin.
3. Read the diagnostics and page behavior to identify the main delay. Large images, slow server response and blocking scripts need different repairs; do not remove a plugin just because it exists.
4. Optimize the actual problem image or asset: size it for display, compress appropriately and preserve meaningful detail. Lazy-load suitable below-page images, but do not delay the main hero image that the visitor needs first.
5. For script or template weight, remove confirmed unused code or defer appropriate non-critical work through the supported source. Check dependencies before changing a builder or script. Preserve form behavior, accessibility, consent and agreed measurement.
6. Use the actual host’s cache controls where beneficial. Verify cache behavior for suitable public pages without caching private or transactional responses by mistake. A content delivery service is an option, not a universal purchase requirement.
7. Repeat the same tests and compare the same metric with baseline. Check the page on a real phone under a stated connection when available. Field Core Web Vitals use a different population and thresholds; no single lab pass certifies them.
8. Stop when the agreed target and functional checks pass, or when the next change has a clear unresolved dependency. Save the measured improvements and remaining bottleneck with an owner; do not loop indefinitely or cut useful content just to raise a score.

## Definition of done (QA checklist)

- [ ] The under-three-second claim names its metric, pages and test conditions.
- [ ] Before/after tests are comparable and the actual numbers are saved.
- [ ] The chosen house target passes for the declared scope, or the exact residual delay is stated.
- [ ] Forms, accessibility, consent, images and necessary tracking still work.
- [ ] Lab, field and phone evidence are separate; no universal user-speed or ranking guarantee is made.

## Example(s)

**Fictional teaching example.** Two mobile lab LCP runs on a repair page take 4.2 and 4.5 seconds. Resizing its oversized hero image produces lesson runs of 2.6 and 2.8 seconds under the same conditions. The slower result, 2.8 seconds, meets the house under-three-second LCP target. It does not meet Google’s separate good field-LCP threshold merely by being under three, and these invented lab values provide no real-user evidence.

## Handoff and Content Factory context

Give the measurements and changed assets to the site owner. Use [ensure working contact form delivers notifications](https://local-service-spotlight.github.io/task-library/?task=ensure-working-contact-form-delivers-notifications#task-ensure-working-contact-form-delivers-notifications) if the optimization touched a lead form. Route an unresolved server delay to the actual hosting owner.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before a relevant launch and after major theme, asset or hosting changes. Optional monitoring needs configured pages, conditions and a trigger; the guide does not install a paid monitor.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/digital-plumbing
- Exact task: [Ensure Site Loads Under 3 Seconds on Mobile](https://local-service-spotlight.github.io/task-library/?task=ensure-site-loads-under-3-seconds-on-mobile#task-ensure-site-loads-under-3-seconds-on-mobile)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [Google PageSpeed Insights data](https://developers.google.com/speed/docs/insights/v5/about)
- [Google Core Web Vitals](https://web.dev/articles/vitals)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The project must choose the house metric; no original source defined a precise load event. Real mobile and field coverage remain unverified until measured.
