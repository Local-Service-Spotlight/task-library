---
name: step-2-transcribe-video-using-descript
description: Produce a clean, accurate verbatim transcript in Descript — correcting every blue-underlined low-confidence word — so the article is written from what was actually said (Blog Posting Guidelines Step 2).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 2: Transcribe video using Descript

**Use this when** the video is loaded into its Descript project (Step 1 complete) and needs a transcript before any watching, outlining, or writing.

## Inputs
- The Descript project from `step-1-upload-video-to-google-drive-and-descript`
- Descript Enterprise transcription access
- Correct spellings of all people, companies, and product names likely mentioned (e.g., Marko Sipila, Zach Peyton, Superior Fence & Rail, NaiL AI)
- The Content Library tracker

## Steps
1. Run Descript's transcription on the project media.
2. Assign speaker labels correctly (interviewer vs. client, each team member by name).
3. Work through every blue-underlined word — Descript's low-confidence flags — playing the audio at each one and correcting to what was actually said.
4. Pay special attention to proper nouns: client names, company names, place names, and jargon are the most common mis-transcriptions ("Marco" for Marko Sipila, "nail AI" for NaiL AI). Fix against the provided spelling list.
5. Keep the transcript verbatim at this step — do not paraphrase, reorder, or "improve" the speech. Cleaning happens in Step 4; voice preservation depends on an honest source transcript.
6. Read the full transcript top to bottom once while the audio plays to catch errors Descript did not flag.
7. Update the tracker: "Step 2 done — transcript verified."
8. Hand off to `step-3-watch-video-and-identify-gct` (and run `use-descript-underlord-to-remove-filler-words` when filler cleanup is wanted before editing).

## Definition of done (QA checklist)
- [ ] Zero blue-underlined words remain unreviewed
- [ ] All names of people and companies spelled correctly throughout
- [ ] Speaker labels accurate for every segment
- [ ] Transcript is verbatim — no paraphrasing introduced
- [ ] Full-pass listen-through completed
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Transcription is Step 2 of every article run documented at https://localservicespotlight.com/article-guidelines/.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

Zero blue underlines is a number an agent can verify: a persistent agent (Claude Fable 5, or comparable long-horizon OpenAI/Google models) works the low-confidence flags one by one and loops until none remain unreviewed and every proper noun matches the spellings list — "mostly corrected" ships wrong names. Memory compounds here: each new name a run verifies (client, company, product) joins the spelling list for every future transcript. Close the run with a logged meta-article example.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 2 of the 18-step SOP)
- Related: /content-factory
- Sibling skills, in run order: `step-1-upload-video-to-google-drive-and-descript` → this → `use-descript-underlord-to-remove-filler-words` → `step-3-watch-video-and-identify-gct`
