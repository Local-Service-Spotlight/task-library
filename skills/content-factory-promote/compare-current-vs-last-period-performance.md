---
name: compare-current-vs-last-period-performance
description: "Compare two fair time spans. Show what changed, what is known and what to check next."
category: Content Factory — Promote
stage: Promote
definitive_article: /social-amplification
status: complete
---

# Compare current vs last period performance

You want to know if this week went better than the last. This guide helps you compare the same kinds of results. Start with two clear time spans and the goal the work was meant to serve.

**The path:** Matched periods → checked changes → evidence limits → next-week report.

**Use this when:** A weekly or monthly promotion review is due, or the owner needs a fair before/after comparison.

## Inputs
- Current and prior source exports, matching metric definitions and the actual reporting goal.
- Exact dates, time zone, currency, campaign changes, outages and known reporting delay.
- Prior decisions and their actual execution evidence; read-only reporting access and the agreed report destination.

## First-run prompt

> Compare these periods using consistent definitions. Show absolute changes and percentages, handle zero baselines and note calendar or attribution limits. Treat the source’s 20% rule as a review flag, not proof of statistical significance. Return evidence-qualified findings and next actions without changing campaigns.

## Steps
1. Set exact current and prior dates. Prefer equal-length complete periods with comparable weekdays. Calendar months differ in length; show per-day measures or that limit if month-over-month reporting is required.
2. Use the same account, currency, time zone, metric definition and attribution window. Keep incomplete current periods or late conversion data labeled provisional; do not make them look like closed periods.
3. Compare the appropriate funnel measures: attention, useful engagement and actual business results. Separate spend, count, rate and cost. Do not add reach across overlapping channels as unique people.
4. For each metric, show prior value, current value, absolute change and relative change: (current − prior) ÷ prior. If the prior value is zero, the percentage is undefined; show the counts. For rates, distinguish percentage points from relative percent.
5. Use the source’s ±20% threshold as a triage flag alongside sample size, money and the goal. A 5% move can matter at scale; a 100% move from one to two results can be weak evidence. Neither threshold alone proves signal or noise.
6. Use [apply metrics decomposition](https://local-service-spotlight.github.io/task-library/?task=apply-metrics-decomposition#task-apply-metrics-decomposition) to locate the changed component, then consult the actual change log. Label causes verified, plausible or unknown. Do not force a cause onto every flagged row.
7. Separate supported improvements, deterioration, stable performance and unresolved evidence. A flat winner does not prove fatigue is coming. Check whether last period’s recommended action actually happened before crediting it.
8. Deliver the table through the already authorized report route, or save the report draft when delivery is outside scope. Give the next-week planner a small set of evidence-backed findings, with provisional data and due rechecks visible.

## Definition of done (QA checklist)

- [ ] Dates and definitions are comparable or the precise limits are stated.
- [ ] Absolute, relative and percentage-point changes are correctly calculated.
- [ ] Zero baselines and incomplete periods are handled honestly.
- [ ] 20% flags are not called statistical proof or mandatory cause attribution.
- [ ] Actual actions and observed outcomes are separate in the report.

## Example(s)

**Fictional teaching example:** A shop records 10 leads last week and 12 this week: two more, or a 20% rise. Spend rises from $100 to $144, so cost per lead rises from $10 to $12, also 20%. More leads did not mean better cost. A click rate moves from 2% to 2.4%: that is 0.4 percentage points and a 20% relative rise. The report notes a holiday and no verified causal explanation, then names the next tracking and quality checks.

## Handoff and Content Factory context

Send the checked table to [review budget allocation by channel](https://local-service-spotlight.github.io/task-library/?task=review-budget-allocation-by-channel#task-review-budget-allocation-by-channel) and [list top 3 5 recommendations for next 7 days](https://local-service-spotlight.github.io/task-library/?task=list-top-3-5-recommendations-for-next-7-days#task-list-top-3-5-recommendations-for-next-7-days). Use the existing report owner and agreed weekly day; do not impose Friday when a different cadence was agreed.

This task is in Promote within the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. Use the proof and checked posts from earlier stages; a Promote task does not automatically redo all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Weekly or monthly as agreed for the campaign. The source’s Friday example is a standing variant, not an automatic scheduling change. Preserve actual stored baselines; a model name does not guarantee them.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/social-amplification
- Exact task: [Compare current vs last period performance](https://local-service-spotlight.github.io/task-library/?task=compare-current-vs-last-period-performance#task-compare-current-vs-last-period-performance)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Metrics, Analysis, and Action](https://blitzmetrics.com/maa/)
- [Goals, Content, and Targeting](https://blitzmetrics.com/gct-business-strategy/)
- [Social Amplification Engine](https://blitzmetrics.com/social-amplification/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- No real historical report or existing delivery route is supplied.
- Missing or incompatible data may support only a partial comparison; it must remain labeled.
