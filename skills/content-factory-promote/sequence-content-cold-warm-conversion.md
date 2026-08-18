---
name: sequence-content-cold-warm-conversion
description: Arrange winning content into a cold → warm → conversion funnel so strangers meet the WHY first, engagers get depth, and only warm audiences see the offer.
category: Content Factory — Promote
stage: Promote
definitive_article: /dad
status: needs-work
---

# Sequence content: cold → warm → conversion

**Use this when** several pieces are winning in isolation and need to be ordered into a funnel instead of blasting offers at strangers.

## Inputs
- Validated content inventory tagged by funnel level (Nine Triangles: Audience, Engagement, Conversion)
- Working pixel + engagement custom audiences (video viewers, page engagers, site visitors)
- Target CPA/ROAS and 90-day goals from SAE Stage 2

## Steps
1. Classify each winning piece by funnel level: **cold/audience** = WHY video, one-minute answers, story content; **warm/engagement** = how-tos, case studies, testimonials, 3×3 grid depth; **conversion** = offer, consult, lead magnet content.
2. Build the audience per level: cold = saved/interest/lookalike audiences; warm = engagement custom audiences (video viewers, page engagers, recent site visitors); conversion = high-intent remarketing (landing page abandoners, lead-form openers).
3. Launch $1/day ad sets per level, matching content to temperature — never run conversion offers at cold audiences; cold traffic gets the WHY.
4. Wire the escalator: people who watch the cold video automatically enter the warm audience; warm engagers automatically enter the conversion remarketing pool. The sequence runs itself once audiences are defined.
5. Watch level-to-level flow weekly: if warm audiences aren't growing, the cold content isn't engaging; if conversions stall with a full warm pool, the offer or landing page is the weak link (apply-metrics-decomposition tells you which).
6. Kill and scale within each level by Dollar a Day rules (kill bottom 90%, scale winners ≤2×), keeping the three levels budgeted in balance (review-budget-allocation-by-channel).

## Definition of done (QA checklist)
- [ ] Every running creative mapped to exactly one funnel level; no conversion offers aimed at cold audiences
- [ ] Engagement custom audiences feed warm; remarketing pool feeds conversion — escalator verified live
- [ ] $1/day ad sets per level; weekly flow check (cold→warm growth, warm→conversion rate) logged
- [ ] Kill/scale decisions applied per level under Dollar a Day rules
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Failure modes
- Conversion offer aimed at cold traffic. Strangers meet the WHY first; the quote form comes last.
- Escalator not wired. If watching the cold video does not add the person to the warm audience, you are running three disconnected $1 tests, not a funnel.
- Pixel missing. Sequence cannot escalate. Run Gate skills first.

## Example(s)
- Local-service funnel (Marko Sipila, HVAC Quote): one-minute answer video (cold) → install case study (warm) → quote offer (conversion), $1/day per layer.
- Nine Triangles funnel levels and SAE Stages 4–5 are the same temperature model.

## Model routing
Computer-use (Ads Manager audiences). Classification of creatives is lane `any`. Claude-only or Grok-only: classify in chat, then click the same Ads Manager screens.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5, or comparable OpenAI/Google models) wires the escalator once, then watches it weekly for as long as the funnel runs — checking cold→warm growth and warm→conversion flow, decomposing any stall, and re-verifying the full Definition of done each cycle instead of assuming last week's pass still holds.
It pulls each creative's funnel-level tag and performance history from memory, so re-sequencing is a lookup, not a rebuild.
Every weekly pass logs a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /dad
- Related: /social-amplification (Stages 4–5) · /nine-triangles (funnel levels) · set-up-remarketing-ads-for-landing-page-abandoners (the conversion layer)
- Run order (Promote stage): execute-switch-boost-to-target-new-audiences → **sequence-content-cold-warm-conversion** → set-up-remarketing-ads-for-landing-page-abandoners
