---
name: use-descript-underlord-to-remove-filler-words
description: Use Descript's Underlord to strip filler words (uh, um, like, you know) from the video and transcript while preserving natural human cadence.
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Use Descript Underlord to remove filler words

**Use this when** a transcribed Descript project (Step 2 complete) is headed for clip extraction, YouTube upload, or article writing and the raw speech is filler-heavy.

## Inputs
- The transcribed, speaker-labeled Descript project
- Descript Underlord access
- 10–15 minutes for review — the removals must be checked, not blind-applied

## Steps
1. Open the transcribed project and run Underlord's filler-word removal across the full transcript (targets: uh, um, like, you know, sort of, I mean).
2. Review the flagged removals as a list BEFORE applying. Watch for false positives: "like" as a comparison ("a quote like that") and "you know" as a direct address are real speech, not filler.
3. Apply the approved removals, then play the affected sections and listen for jump cuts — audio that stutters where words were cut needs the edit loosened or smoothed.
4. Protect cadence over cleanliness: a few fillers in an emotional or emphatic moment can stay. Over-scrubbed speech sounds robotic and kills the authenticity the Produce stage was built on.
5. Confirm the cleaned transcript still reads true to the speaker — this version feeds Step 4's editing and Step 5's article drafting.
6. Export/save the cleaned composition so clip extraction (`extract-15-60-second-clips-from-long-form-video`) and the YouTube upload inherit the cleaned cut.
7. Update the Content Library tracker: "Underlord pass done" with a note of anything intentionally left in.

## Definition of done (QA checklist)
- [ ] Filler-word pass run across the entire project
- [ ] Removal list reviewed item-by-item; false positives restored
- [ ] No audible jump cuts on playback of edited sections
- [ ] Speaker still sounds like themselves (cadence check on 2–3 passages)
- [ ] Cleaned composition saved and downstream steps pointed at it
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Filler removal is part of the Descript workflow documented at https://localservicespotlight.com/article-guidelines/.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or comparable OpenAI/Google models that loop and hold memory) reviews the removal list item by item, restores false positives, then loops the playback check until no audible jump cuts remain and the speaker still sounds like themselves — clean-but-robotic fails the checklist. Memory learns each speaker's verbal patterns (when their "like" is real speech, not filler), so review gets sharper every run. Document the pass with a meta-article example.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Descript processing within the 18-step SOP)
- Related: /one-minute-video-guide (the authenticity standard that limits over-editing)
- Sibling skills, in run order: `step-2-transcribe-video-using-descript` → this → `step-3-watch-video-and-identify-gct` / `extract-15-60-second-clips-from-long-form-video`
