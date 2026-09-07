---
name: apply-metrics-decomposition
description: "Find which part of the ad path changed. Use the facts to choose the next check."
category: Content Factory — Promote
stage: Promote
definitive_article: /social-amplification
status: complete
---

# Apply Metrics Decomposition

Your ad cost changed, but the total does not tell you why. This guide helps you break the result into clear parts. Start with the same goal and the numbers from each step.

**The path:** Top-line change → matching parts → likely driver → next check.

**Use this when:** A campaign’s cost or result changes and the team needs an evidence-backed explanation to guide the next action.

## Inputs
- Dated ad exports for the same goal and comparable periods, including spend, impressions, link clicks and counted results.
- Website visits/events only when they belong to that measured path; currency, time zone, attribution settings and tracking-change log.
- Written target and source definitions for each metric; read access and a calculation sheet are sufficient for this analysis.

## First-run prompt

> Break this changed result into matching components. Show units and arithmetic, reconcile the total where possible and label unmatched data. Distinguish a measured driver from a causal explanation. Return one useful next check with its owner; do not change campaigns from the analysis alone.

## Steps
1. Choose the goal’s actual top-line measure: cost per useful visit, qualified lead, sale or return on ad spend. Define what counts and keep different goal types separate.
2. Align account, period, time zone, currency and attribution scope. A platform conversion that includes view-through credit is not automatically part of a click-only site path. Record that mismatch before calculating.
3. For a consistently measured click path, collect spend, impressions, link clicks, landing-page visits and conversions. Keep missing counts unknown. A missing stage prevents full reconciliation; do not fill it from a different report just to get a zero residual.
4. Compute cost per thousand impressions (CPM), click rate (clicks ÷ impressions), visit rate (visits ÷ clicks) and conversion rate (conversions ÷ visits). Use rates as decimals in the identity: cost per conversion = CPM ÷ (1000 × click rate × visit rate × conversion rate). This works only when all counts describe the same path and denominators are nonzero.
5. Check the computed cost against spend ÷ matching conversions. Explain rounding, attribution or tracking differences instead of forcing agreement. For return on ad spend, use matched attributed revenue ÷ spend and keep profit separate.
6. Compare each component with the baseline. A lower click rate directs attention to the creative, offer or delivery mix; a weaker visit-to-conversion rate directs attention to the measured destination path. These are diagnostic leads, not proof of one cause.
7. Inspect the corresponding change log and evidence. Audience mix, auction conditions, site speed, consent, device mix and reporting lag can all matter. State a supported finding, a plausible explanation and what remains unknown separately.
8. Write the [Metrics, Analysis, and Action](https://blitzmetrics.com/maa/) line and name a specific next check or authorized repair. Preserve the worksheet so another reviewer can reproduce every number.

## Definition of done (QA checklist)

- [ ] The chosen metric and each component have matching units and scope.
- [ ] Arithmetic handles missing or zero denominators without invented rates.
- [ ] Any residual or attribution mismatch is explained, not hidden.
- [ ] Measured changes and causal hypotheses are kept distinct.
- [ ] The next check has evidence, owner and an acceptance test.

## Example(s)

**Fictional teaching example:** A test spends $100 for 10,000 impressions, 200 link clicks, 160 visits and eight matched leads. CPM is $10; the three rates are 0.02, 0.8 and 0.05. The formula gives $10 ÷ (1000 × 0.02 × 0.8 × 0.05) = $12.50 per lead, matching $100 ÷ 8. In a comparable period, only four leads occur with the same earlier counts, so cost becomes $25. The conversion stage changed. The next check is the form and offer evidence; the calculation alone does not prove the page caused the drop.

## Handoff and Content Factory context

Give the worksheet to [compare current vs last period performance](https://local-service-spotlight.github.io/task-library/?task=compare-current-vs-last-period-performance#task-compare-current-vs-last-period-performance) and [list top 3 5 recommendations for next 7 days](https://local-service-spotlight.github.io/task-library/?task=list-top-3-5-recommendations-for-next-7-days#task-list-top-3-5-recommendations-for-next-7-days). The actual site or campaign owner receives any specific verification or repair task.

This task is in Promote within the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. Use the proof and checked posts from earlier stages; a Promote task does not automatically redo all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run when a material result changes or during the agreed optimization review. The read-only calculation can be a one-off; recurring exports need a real connector, trigger and saved baseline.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/social-amplification
- Exact task: [Apply Metrics Decomposition](https://local-service-spotlight.github.io/task-library/?task=apply-metrics-decomposition#task-apply-metrics-decomposition)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Metrics, Analysis, and Action](https://blitzmetrics.com/maa/)
- [Goals, Content, and Targeting](https://blitzmetrics.com/gct-business-strategy/)
- [Social Amplification Engine](https://blitzmetrics.com/social-amplification/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- No real matched export or causal experiment is supplied.
- The current SAE hub has broad access gates; this read-only analysis only needs the actual evidence named in Inputs.
