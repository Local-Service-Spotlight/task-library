---
name: extract-15-60-second-clips-from-long-form-video
description: Cut a long-form recording into 15–60 second standalone clips that feed social posts, quote cards, and Dollar a Day creatives.
category: Content Factory — Process
stage: Process
definitive_article: GAP — to be written
status: needs-work
---

# Extract 15–60 second clips from long-form video

**Use this when** a long-form asset — conference talk, audit screen share, team conversation, client interview — is transcribed and timestamped and needs to become short-form content.

## Inputs
- The Descript project with verified transcript and Step 4 timestamps (run `use-descript-underlord-to-remove-filler-words` first)
- The GCT statement for the source video
- The Content Library tracker
- Platform specs for the intended destinations (vertical for Reels/TikTok-style placement, square/landscape for feed)

## Steps
1. Re-read the timestamped transcript and mark every candidate moment: a complete thought with a strong first line — one idea per clip, no setup required to understand it.
2. Apply the hook test: the first 3 seconds must earn attention on their own (a claim, a number, a question). If the moment needs 10 seconds of context, it is not a clip.
3. Cut each clip in Descript by selecting the transcript text — trim to the idea's boundaries, 15–60 seconds, never longer.
4. Start the clip on the speaker mid-energy (just before the key line), and end on the punch, not the trail-off.
5. Add captions to every clip — most social viewing is sound-off — and verify caption text against the transcript.
6. Export in the destination aspect ratios; name each `YYYY-MM-DD-source-clipNN-hookphrase`.
7. Log every clip in the Content Library tracker, linked to its source video row, with its GCT note and intended destination (social post, quote card source, or Dollar a Day creative).
8. Route the strongest clips onward: `create-social-media-posts-per-platform` and `create-dollar-a-day-ad-creatives`.

## Definition of done (QA checklist)
- [ ] Every clip is one complete, standalone idea, 15–60 seconds
- [ ] First 3 seconds of each clip pass the hook test
- [ ] Captions present and accurate on all clips
- [ ] Exports match destination specs and naming convention
- [ ] All clips logged against the source video in the tracker with routing
- [ ] Linked back to the definitive article and relevant siblings

## Failure modes
- Clip that needs 10 seconds of setup. If it is not standalone, it is not a clip.
- No captions. Most views are sound-off; the hook dies.
- Clipping before the Underlord/filler pass. You export jump cuts.

## Example(s)
- One hour of recording yields 10–20 clips (Content Factory assembly line). Each clip is one idea; the hub article remains the canonical piece.
- Descript: cut by selecting transcript text, not a timeline razor.

## Model routing
Computer-use (Descript). A local model can *propose* clip timestamps from `transcript.md`; a human or browser agent makes the cuts. Claude-only or Grok-only: propose from the file, then cut in Descript.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) sweeps the full timestamped transcript, hook-tests every candidate, captions everything, and loops until every clip is exported to spec, logged, and routed — not just the three obvious moments. Memory records which moments of each source are already clipped, so re-runs extend the clip set instead of duplicating it. Log a meta-article example per run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: GAP — no definitive article yet; this skill flags the missing hub. Until written, ground runs in /blog-posting-guidelines (Descript workflow) and /one-minute-video-guide (what a strong 60 seconds looks like).
- Related: /one-minute-video-guide, /social-amplification, /dad
- Sibling skills, in run order: `use-descript-underlord-to-remove-filler-words` → this → `create-quote-cards-from-strongest-statements` / `create-social-media-posts-per-platform`
