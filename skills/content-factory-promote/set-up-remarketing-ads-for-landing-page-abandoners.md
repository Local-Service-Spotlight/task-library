---
name: set-up-remarketing-ads-for-landing-page-abandoners
description: Build Google and Facebook remarketing ads aimed at 1-day landing page abandoners (SAE Stage 5) — the hottest audience you have, recovered for $1/day.
category: Content Factory — Promote
stage: Promote
definitive_article: /social-amplification
status: needs-work
---

# Set up remarketing ads for landing page abandoners

**Use this when** traffic is flowing to landing pages from boosts and sequencing, but visitors leave without converting — recover them while intent is fresh.

## Inputs
- Meta pixel and Google tracking firing on every page with conversion events defined (/digital-plumbing; verified per /website-qa-audit Layer 1)
- The landing page URL(s) and their thank-you/conversion confirmation URLs
- Warm-stage creative: testimonials, objection-answer videos, Thank You Machine clips

## Steps
1. Verify plumbing first: pixel/tag present on the landing page AND the conversion confirmation page — without both, you cannot build the audience or exclude converters.
2. Build the abandoner audience on **both Facebook and Google**: visited the landing page in the last **1 day**, excluding anyone who hit the conversion event. One day, because intent decays by the hour.
3. Choose creative that resumes the conversation instead of repeating it: a testimonial from someone like them, the answer to the most common objection, or a personal "still have questions?" one-minute video — not the same cold ad they already saw.
4. Launch at **$1/day per ad set**. The audience is small but the hottest you own; tiny budget, outsized share of conversions.
5. Monitor frequency weekly — a 1-day window refreshes constantly, but if frequency climbs while results stall, rotate creative.
6. Compare cost per result against cold and warm campaigns in the weekly review; remarketing should be your cheapest conversions. If it isn't, the landing page itself is the suspect (decompose it).

## Definition of done (QA checklist)
- [ ] Pixel verified on landing and conversion pages; converters excluded from the audience
- [ ] 1-day abandoner audiences live on both Facebook and Google with conversation-resuming creative
- [ ] $1/day per ad set; weekly frequency and creative-rotation check scheduled
- [ ] Cost per result benchmarked as cheapest tier in the budget review
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Failure modes
- Pixel not on the thank-you page. You remarket converters and waste the hottest money on the line.
- Window longer than 1 day "to get a bigger audience." Intent is gone; you are just retargeting.
- Same cold creative. They already bounced. Resume the conversation.

## Example(s)
- Quote-page abandoners for a local service brand recovered with a testimonial video at $1/day — cheapest conversions on the account when plumbing is live.
- If remarketing CPA is worse than cold, the landing page is the suspect, not the audience.

## Model routing
Computer-use. **Gating 5:** this skill is illegal to run without `install-meta-pixel-with-standard-events`. Claude-only or Grok-only: same UI.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5 or comparable OpenAI/Google models) verifies the plumbing before building anything — pixel on landing AND conversion pages — and refuses to proceed on a partial pass, because the Definition of done is binary; once live, it returns weekly to check frequency, rotate fatigued creative, and confirm remarketing is still the cheapest tier.
It pulls warm creative and conversion URLs from the memory records of prior stages instead of asking again.
Each build and weekly check is logged as a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /social-amplification (Stage 5: Amplification)
- Related: /dad · /digital-plumbing (the pixels this depends on) · sequence-content-cold-warm-conversion (this is its conversion layer)
- Run order (Promote stage): sequence-content-cold-warm-conversion → **set-up-remarketing-ads-for-landing-page-abandoners** → Stage 6 optimization skills
