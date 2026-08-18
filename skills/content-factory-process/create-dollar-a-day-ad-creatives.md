---
name: create-dollar-a-day-ad-creatives
description: Format proven content into ad creatives for Facebook, Instagram, and YouTube so the Promote stage can put $1/day behind validated winners.
category: Content Factory — Process
stage: Process
definitive_article: GAP — to be written
status: needs-work
---

# Create Dollar a Day ad creatives

**Use this when** organic signals (engagement, watch time, shares, comments) have identified winning content and Promote needs campaign-ready creative.

## Inputs
- The winning content: clips, quote cards, or posts with proven organic engagement (Dollar a Day amplifies validated winners — it does not gamble on untested creative)
- The GCT statement for each piece (Goal and Targeting drive placement and copy)
- Platform specs for Facebook/Instagram feed, Reels/Stories, and YouTube in-stream
- The Content Library tracker and the brand's ad account structure

## Steps
1. Select only content with real organic signal — check the tracker/post metrics first. If nothing has signal yet, stop and route back to posting, not ad-making.
2. For each winner, cut the creative to platform spec: square/vertical for FB/IG feed and Reels, vertical for Stories, horizontal with a hook-first edit for YouTube in-stream.
3. Front-load the hook: the first 3 seconds must work sound-off — captions on everything, the key claim on screen immediately.
4. Write primary text and headline from the content's own proven language (the post copy or article hook that already engaged people), trimmed to platform limits. No new unproven messaging.
5. Produce 2–3 variants per concept (different hook line or thumbnail) so Promote can run multiple simultaneous $1/day tests per the Dollar a Day method.
6. Keep each creative mapped to its GCT: note Goal (e.g., warm-audience engagement vs. conversion) and Targeting on the tracker row — this drives which ad set it enters and where it sits in the cold → warm → conversion sequence.
7. Name files `YYYY-MM-DD-source-platform-variant` and store in the Content Library `04-Promote-Creatives` folder.
8. Hand off to the Promote stage (Dollar a Day campaign setup) with the tracker rows complete.

## Definition of done (QA checklist)
- [ ] Every creative traces to content with documented organic signal
- [ ] First 3 seconds work with sound off; captions on all video creatives
- [ ] Correct specs per placement (FB/IG feed, Reels/Stories, YouTube in-stream)
- [ ] 2–3 variants per concept, GCT noted per creative
- [ ] Files in `04-Promote-Creatives` and tracker rows ready for campaign build
- [ ] Linked back to the definitive article and relevant siblings

## Failure modes
- Creative for a post with no organic signal. Dollar a Day amplifies winners; it does not rescue a hook that already failed at $0.
- Sound-on-only hook. First 3 seconds must work captions-on, sound-off.
- New messaging that was not in the winning post. You are testing spend, not copy.

## Example(s)
- Marko Sipila / HVAC Quote: the ad creative is the conference clip that already performed on YouTube, not a new studio shoot.
- Public method: https://blitzmetrics.com/content-factory/ (Dollar a Day is taught inside the factory) and `dollar-a-day-strategist` in the skill packs.

## Model routing
Lane `any` for cutting copy/variants from the winning post's own language. Computer-use to export from Descript. Do not spend a dollar in this skill — that is Promote (`run-dollar-a-day-campaign-on-winning-content`).

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) checks organic signal first and refuses to cut creative for unproven content; for real winners it builds every placement spec, 2–3 variants per concept, and loops until each creative carries its GCT note and sits in `04-Promote-Creatives` — partial variant sets are not done. Memory holds which creatives already ran and how they performed, so new variants build on results instead of guesses. Log a meta-article example per batch.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: GAP — no definitive article yet; this skill flags the missing hub. Until written, ground runs in /dad (the campaign method these creatives feed) and /social-amplification.
- Related: /dad, /social-amplification, /one-minute-video-guide
- Sibling skills, in run order: `create-social-media-posts-per-platform` → this → Promote-stage Dollar a Day campaign skills
