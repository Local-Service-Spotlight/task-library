---
name: test-mobile-load-time-under-3-seconds
description: "Find slow pages on a phone. Save clear speed results and the next fix to check."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Test mobile load time under 3 seconds

A slow page can make a customer wait for the useful part. This guide helps you check mobile speed and find the cause of a delay. Start with the pages people need most, then record what the test measured.

**The path:** Known pages → Lab and real-user data → Cause → Measured fix.

**Use this when:** A launch, template change or defined performance audit needs mobile page-speed evidence.

## Inputs
- The canonical page list and priority templates, with traffic evidence when it exists. Do not assume most traffic is mobile without the actual report.
- PageSpeed Insights or an available Lighthouse setup, plus a place to save full reports and test conditions.
- The site’s house target, repair scope and actual technical owner.
- Existing baseline reports, source revisions and any real-user data available for the page or origin.

## First-run prompt

> Measure the supplied page set with mobile reports. Keep lab, house target and real-user metrics separate, preserve test conditions and coverage, and diagnose actual reported causes. Complete authorized fixes and return comparable before/after evidence plus remaining owners.

## Steps
1. Define the sample or full page set. Start with the home page, important service pages and representative articles from the requested scope. Record the denominator; a template sample is not every page.
2. Run a mobile PageSpeed or Lighthouse test and retain the report, date, URL and environment. Read its mobile result rather than desktop. LCP, Largest Contentful Paint, measures when the largest visible content element renders; it is not the moment every page function has finished loading.
3. Record lab LCP and the performance score separately. For the source’s house check, compare mobile lab LCP with under 3.0 seconds. Label that target explicitly; a 2.8-second result is not automatically a good Core Web Vitals result.
4. Read real-user data separately when available. Record whether it describes this URL or the entire origin and its time window. No field data means insufficient evidence, not zero delay or an automatic failure.
5. For current Core Web Vitals, evaluate the reported 75th-percentile LCP, INP and CLS together. Good thresholds are LCP at most 2.5 seconds, INP at most 200 milliseconds and CLS at most 0.1. Do not substitute a single lab score for that field assessment.
6. Repeat a suspect or failing lab test under the same conditions once and retain both results. The source’s conservative house comparison may use the worse run, labeled as such. Do not repeatedly retest until a lucky pass replaces the original evidence.
7. Read the report’s actual diagnostics. Match the suggested issue to the page: oversized lead image, delayed server response or blocking work, for example. Prepare or perform the exact authorized supported-source fix without removing useful first-screen content just to improve a score.
8. Recheck changed pages under comparable conditions and save before/after reports plus visual/function regression results. Field history will not instantly reflect a new deployment. Hand remaining causes to the technical owner with an actual next check.

## Definition of done (QA checklist)

- [ ] Each scoped page has a dated mobile report and stated coverage.
- [ ] Lab LCP, house under-3-second target, performance score and field Core Web Vitals are separate results.
- [ ] URL/origin field scope and missing data are explicit.
- [ ] Repeated measurements are retained without cherry-picking.
- [ ] Repairs have comparable evidence and preserve useful content and function.

## Example(s)

**Fictional teaching example — no speed test was run.** Maple Cycle’s sample home page has lab LCP readings of 2.8 and 3.2 seconds. Its origin-level field report shows LCP 2.7 seconds, INP 150 milliseconds and CLS 0.06.

Using the house’s worse-run rule, the lab check fails the under-3-second target. The field LCP is also outside the good threshold, even though the other two metrics are good. The origin report cannot prove this one URL’s field result.

The next action is to inspect the delayed hero-image load shown in the sample diagnostic, then retain a comparable new report. It is not to declare the page fixed because one run was 2.8 seconds.

## Handoff and Content Factory context

The technical owner receives the exact diagnostic and source revision. [Recheck useful home-page visuals](https://local-service-spotlight.github.io/task-library/?task=check-each-homepage-section-includes-relevant-image#task-check-each-homepage-section-includes-relevant-image) catches a speed fix that accidentally hides or degrades the lead visual.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and after material performance changes. An ongoing monitor requires the existing page set, rate limits and configured cadence; this task does not schedule unlimited whole-site tests.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Test mobile load time under 3 seconds](https://local-service-spotlight.github.io/task-library/?task=test-mobile-load-time-under-3-seconds#task-test-mobile-load-time-under-3-seconds)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google PageSpeed Insights data](https://developers.google.com/speed/docs/insights/v5/about)
- [Google Core Web Vitals](https://web.dev/articles/vitals)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual reports, traffic mix, repair source and comparable runtime evidence require the site.
