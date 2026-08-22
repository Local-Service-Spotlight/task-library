---
name: maa-cycle-metrics-analysis-action
description: Run the continuous MAA cycle — Metrics, Analysis, Action — so every number collected leads to a diagnosis and every diagnosis leads to a concrete change.
category: Strategy & Measurement
stage: —
definitive_article: /9-triangles-framework-scalable-home-service-businesses/
status: complete
---

# MAA cycle (Metrics, Analysis, Action)

**Use this when** reporting has become numbers-without-decisions, or decisions are being made on gut feel — the loop reconnects measurement to action.

## Inputs
- Access to the measurement stack: analytics, search console, ad platforms, CRM/revenue data
- The goals and target CPA/ROAS these metrics are judged against (from GCT)
- Last period's MAA report, so this cycle compares against the previous one

## Steps
1. Define the loop: **Metrics** (what happened — the numbers), **Analysis** (why it happened — the diagnosis), **Action** (what we change — kill, scale, or iterate). One without the other two is waste.
2. **Metrics:** pull the same standing metric set every cycle, across the full pipeline (content → rankings → traffic → revenue) and across funnel levels. Consistency beats volume.
3. **Analysis:** for each metric materially above or below target, write one plain-language sentence on why — creative, targeting, or offer for ads; placement, title, or content for organic.
4. **Action:** convert every analysis into a dated, owned action — kill the underperformer, scale the winner (gradually), or iterate one variable and retest.
5. Close the loop weekly: the actions from this cycle become the first metrics checked next cycle (did the change work?).
6. Measure it: every Friday MAA report must show all three columns — a metric with no analysis, or an analysis with no action, fails QA.

## Definition of done (QA checklist)
- [ ] Standing metric set pulled for the period, same definitions as last cycle
- [ ] Every outlier metric has a one-sentence analysis (why)
- [ ] Every analysis has a dated, owned action (kill / scale / iterate)
- [ ] Last cycle's actions reviewed for effect before new actions are set
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. (The hub at /9-triangles-framework-scalable-home-service-businesses/ links live examples; pull the closest match into this slot.)

## Run on a persistent agent (Fable 5)

This task is the natural home for a persistent, max-effort agent (Claude Fable 5 or comparable OpenAI/Google models): it pulls the same standing metric set every cycle with zero definition drift and loops until all three columns are complete — every outlier metric carries a one-sentence analysis and a dated, owned action, not 90% of them.
It self-verifies by failing its own report whenever a metric lacks an analysis or an analysis lacks an action.
Memory makes the loop real: the agent opens each cycle by checking last cycle's actions against this cycle's numbers — a true memory cycle, compared period over period — and logs a meta-article example from every run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /9-triangles-framework-scalable-home-service-businesses/ (parent methodology: /maa)
- Related, in run order: submit-weekly-maa-report-every-friday, show-whats-working-and-what-isnt, analyze-why-underperformers-fail, kill-underperformers-scale-winners, measure-content-rankings-traffic-revenue
