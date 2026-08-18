---
name: execute-switch-boost-to-target-new-audiences
description: Extend a proven winner to new audience segments by switching the boost's targeting while keeping the same post — social proof compounds on one post object.
category: Content Factory — Promote
stage: Promote
definitive_article: /dad
status: needs-work
---

# Execute switch boost to target new audiences

**Use this when** a boosted post or Dollar a Day ad has proven itself on its first audience and you want to test whether the win travels.

## Inputs
- A validated winner: 7+ days of data, cost per result at or better than target
- The audience library: saved audiences, lookalikes, geo and interest segments not yet tested (see create-new-saved-audiences-from-audience-insights)
- The boost/ad-set log from prior Promote runs

## Steps
1. Pick the winning post — the one whose engagement and cost per result survived the kill round.
2. **Switch the targeting, keep the post**: point the boost (or a duplicated $1/day ad set) at one new untested audience segment. Because it's the same post object, every new like, comment, and share stacks onto the existing social proof instead of starting from zero.
3. Change one variable at a time — new audience, same creative, same budget ($1/day). If you change audience and creative together, the result is unreadable.
4. Run 7 days untouched, then compare cost per result against the original audience's baseline.
5. Keep audiences that match or beat baseline; kill the rest. Log every audience-creative pair so you build a map of which messages travel to which segments.
6. Feed surviving audience-creative pairs into the cold → warm → conversion sequence and into scaling (≤2× per step).

## Definition of done (QA checklist)
- [ ] Switch applied to a proven winner only — same post object, social proof preserved
- [ ] One new audience per test, $1/day, 7 untouched days
- [ ] Cost per result compared to original-audience baseline; losers killed, winners logged
- [ ] Audience-creative map updated for sequencing and scaling
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Failure modes
- Switching creative AND audience together. The result is unreadable.
- Boosting a loser to "give it a new audience." Switch-boost is for proven winners only.
- New post object. Social proof must stack on the same post.

## Example(s)
- Dollar a Day method: https://blitzmetrics.com/content-factory/ — $1/day × 7, kill the bottom 90%, then travel the winner to a new saved audience.
- Candidate worked example: switching a winning Superior Fence & Rail (Zach Peyton) post from its home metro to an adjacent service-area audience.

## Model routing
Computer-use (Ads Manager). Claude-only or Grok-only: same UI. Scripts can read the CSV export after day 7; they cannot click Boost.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5 or a comparable OpenAI/Google model) enforces the one-variable rule mechanically: same post object, one new audience, $1/day, 7 untouched days — then compares against the baseline it stored from the original run and self-verifies every Definition-of-done box before logging the verdict.
The audience-creative map it maintains in memory is the compounding asset: each switch adds a data point on which messages travel to which segments.
It logs a meta-article example per run so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /dad
- Related: /social-amplification (Stage 5–6) · create-new-saved-audiences-from-audience-insights (supplies the segments)
- Run order (Promote stage): run-dollar-a-day-campaign-on-winning-content → **execute-switch-boost-to-target-new-audiences** → sequence-content-cold-warm-conversion
