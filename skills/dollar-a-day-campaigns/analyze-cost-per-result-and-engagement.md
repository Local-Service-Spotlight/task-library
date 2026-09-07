---
name: analyze-cost-per-result-and-engagement
description: "Check what each ad cost and what it did. Choose the next step from the facts."
category: Dollar a Day Campaigns
stage: Promote
definitive_article: /dad
status: complete
---

# Analyze cost per result and engagement

You need to know which ads earn their keep. This guide helps you read the cost and the result of each test. Start with the test log and the goal you set before the ads ran.

**The path:** Test log → checked costs → fair verdict → next action.

**Use this when:** A test reaches its planned seven-day review, or a budget, delivery or safety issue needs an earlier check.

## Inputs
- Read access to the exact ad account and a dated export for each test; currency, time zone, objective and reporting window.
- The written goal, target cost per result, business definition of a useful lead or sale, and any agreed minimum evidence for a decision.
- Creative and audience IDs, start/end times, changes, spend ceiling, tracking check and attribution setting. Missing data stays unknown.

## First-run prompt

> Read these test records and score each against its stated goal. Reconcile spend and results, show each calculation and mark weak evidence. Return a dated keep, stop, change or hold recommendation with the next owner. Do not change ads unless that action is in the supplied scope.

## Steps
1. Use the exact account and date range from the test log. Export each full planned window. Keep a test that started later separate; do not compare its two days with another test’s seven days as if the exposure were equal.
2. Reconcile row totals to the campaign export. Label paid versus organic results, currency, time zone, attribution window and known reporting delay. A tracking failure is a measurement gap, not proof that no customer responded.
3. Compute cost per result as spend divided by the matching counted result. With zero results, show spend and zero results; cost per result is undefined. Keep cost per view, click, lead and sale in separate columns.
4. Compare each result with the target written before launch. For leads, check the agreed quality test in the permitted customer system. State whether a reported sale is platform-attributed, matched to an order or still unverified.
5. Read shares, substantive comments and the platform’s actual view or watch-time fields. Compare similar video lengths and formats. Do not invent retention by dividing unlike metrics or claim every reaction is a unique person.
6. Use same-creative or same-audience comparisons to form a possible explanation. Auction delivery, time and overlap may also differ. A simple side-by-side test does not prove the changed variable caused the gap.
7. Give each test a verdict with its reason: eligible winner, stop, change for a new test, or hold for insufficient evidence. A hold needs a due date and a spending decision within the existing ceiling; it is not permission to leave an ad running forever.
8. Write a short [Metrics, Analysis, and Action report](https://blitzmetrics.com/maa/): what happened, what the evidence suggests, and what happens next. Record early emergency pauses separately from the planned day-seven verdict.

## Definition of done (QA checklist)

- [ ] Every row has its exact IDs, full or partial dates, currency and result definition.
- [ ] Spend totals reconcile; zero or missing denominators are not shown as a zero cost.
- [ ] The verdict uses the pre-set goal and states sample or attribution limits.
- [ ] Every action has an owner, due date and scope; no unauthorized spend was inferred.
- [ ] Source export and calculations can reproduce the report.

## Example(s)

**Fictional teaching example:** A shop tests two clips for seven days. Each spends $7. The target is at most $2 per useful site visit. Clip A records five such visits, so $7 ÷ 5 = $1.40. Clip B records two, so $7 ÷ 2 = $3.50. A is a candidate for the next small test; B misses the target. These seven visits are not seven leads. A third clip has no tracking data, so its outcome is unknown, not a $0 cost winner. The report names the ad operator to check A’s next budget and end date.

## Handoff and Content Factory context

Send stopped candidates to [kill underperforming ads](https://local-service-spotlight.github.io/task-library/?task=kill-underperforming-ads#task-kill-underperforming-ads) and qualified winners to [scale winners by increasing budget gradually](https://local-service-spotlight.github.io/task-library/?task=scale-winners-by-increasing-budget-gradually#task-scale-winners-by-increasing-budget-gradually). The campaign owner receives the report; missing tracking goes to [set up digital plumbing pixels tracking](https://local-service-spotlight.github.io/task-library/?task=set-up-digital-plumbing-pixels-tracking#task-set-up-digital-plumbing-pixels-tracking).

This task is in Promote within the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. Use the proof and checked posts from earlier stages; a Promote task does not automatically redo all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at each test’s due date. A recurring review is useful only for an active campaign with an agreed cadence, connected reporting access and a real trigger. Continue any already authorized delivery and spend checks between reviews.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Maintained method: https://blitzmetrics.com/dollar-a-day/
- Source mapping needs reconciliation: the preserved `definitive_article: /dad` points to the coaching program. The method page above is `/dollar-a-day/`; this record does not certify the coaching page as a task recipe.
- Exact task: [Analyze cost per result and engagement](https://local-service-spotlight.github.io/task-library/?task=analyze-cost-per-result-and-engagement#task-analyze-cost-per-result-and-engagement)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Dollar-a-Day method](https://blitzmetrics.com/dollar-a-day/)
- [Goals, Content, and Targeting](https://blitzmetrics.com/gct-business-strategy/)
- [Metrics, Analysis, and Action](https://blitzmetrics.com/maa/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- No real account export or execution result is supplied by this guide.
- Each campaign must supply its own target and minimum decision evidence; no universal cost threshold is invented.
