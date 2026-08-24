---
name: step-1-upload-video-to-google-drive-and-descript
description: Move a raw video into the designated Google Drive folder and a Descript project so the Content Factory Process stage can begin (Blog Posting Guidelines Step 1).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 1: Upload video to Google Drive and Descript

**Use this when** a raw video from the Produce stage is ready to enter the 18-step blog posting pipeline.

## Inputs
- The raw video file (one-minute video, client story, talk, screen share, or team conversation)
- Access to the brand's Content Library Google Drive folder (`01-Raw` intake)
- Descript account access with permission to create projects
- The Content Library tracker

## Steps
1. Pull the next raw video from the Content Library `01-Raw` queue (oldest unprocessed first, unless the tracker flags a priority).
2. Verify the file plays end to end and the audio is intelligible before uploading anywhere — a bad file caught now saves the whole pipeline.
3. Confirm the filename follows convention (`YYYY-MM-DD-topic-person`); rename if intake missed it.
4. Upload the file to the designated Google Drive folder for this brand/client. Drive is the permanent archive; never let the only copy live on a phone or in Descript.
5. Create a new Descript project named to match the filename and upload the same file into it.
6. Wait for Descript's import to finish and spot-check that the media plays inside the project.
7. Update the Content Library tracker: status "In Process — Step 1 done," with links to both the Drive file and the Descript project.
8. Hand off to `step-2-transcribe-video-using-descript`.

## Definition of done (QA checklist)
- [ ] Video verified playable with intelligible audio before upload
- [ ] File in the correct Google Drive folder with convention-compliant name
- [ ] Descript project created, named to match, media imported and playing
- [ ] Tracker updated with both links and status
- [ ] Source row in the Produce queue marked as picked up (no double-processing)
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Every published Content Factory article began with this step; worked runs are linked from the hub at https://localservicespotlight.com/article-guidelines/.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

This step is fully agent-runnable: a persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) pulls the oldest raw file, verifies playback, fixes naming, uploads to Drive and Descript, and loops until both links sit in the tracker and the Produce row is marked picked up — every Definition-of-done box, not five of six. Memory holds the queue position, so the next run resumes exactly where intake left off with no double-processing. Log a meta-article example each documented run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 1 of the 18-step SOP)
- Related: /content-factory, /one-minute-video-guide
- Sibling skills, in run order: `set-up-content-library` → this → `step-2-transcribe-video-using-descript`
