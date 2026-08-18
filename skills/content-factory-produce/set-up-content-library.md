---
name: set-up-content-library
description: Organize all raw and processed content into one structured, trackable library so the Content Factory has a single intake and nothing gets lost (SAE Stage 3).
category: Content Factory — Produce
stage: Produce
definitive_article: /social-amplification
status: needs-work
---

# Set up Content Library

**Use this when** a brand starts producing content at volume, or when existing footage is scattered across phones, desktops, and chat threads.

## Inputs
- A Google Drive location owned by the brand (owner's account, not a VA's personal Drive)
- All existing raw assets: videos, photos, transcripts, published-article links
- The Topic Wheel map (so assets can be tagged to topics)
- A spreadsheet or tracker for the content log

## Steps
1. Create the Drive folder structure by pipeline stage: `01-Raw` → `02-In-Process` → `03-Published` → `04-Promote-Creatives`, mirroring Produce → Process → Post → Promote. Add per-brand subfolders if managing multiple entities.
2. Set the naming convention and write it in a README in the root folder: `YYYY-MM-DD-topic-person` for every file. No `IMG_4203.mov` survives intake.
3. Build the tracker (sheet) with one row per asset: filename, date, topic (Topic Wheel ring/spoke), GCT notes, pipeline status, links to outputs (Descript project, article URL, clips, ad creative).
4. Ingest everything that already exists: collect footage off phones and desktops, rename to convention, file into the right stage folder, log each row.
5. Make `01-Raw` the single intake point — every Produce skill uploads here, and Process Step 1 (`step-1-upload-video-to-google-drive-and-descript`) pulls only from here.
6. Set permissions: owner controls the Drive; the team gets edit access to the working folders. Ownership stays with the brand, never an agency or VA account.
7. Review the tracker weekly: anything sitting in `01-Raw` longer than a week is a Process backlog signal — feed it into the weekly MAA review.

## Definition of done (QA checklist)
- [ ] Folder structure mirrors the four Content Factory stages and is owned by the brand's account
- [ ] Naming convention documented in a root README and applied to all existing assets
- [ ] Tracker logs every asset with topic, status, and output links — zero unlogged files
- [ ] All legacy footage ingested, renamed, and filed
- [ ] Produce skills point intake at `01-Raw`; Process pulls only from there
- [ ] Linked back to the definitive article and relevant siblings

## Failure modes
- Files only in a Slack thread or a vendor's chat memory. The next engine cannot see them. Drive + tracker is the factory.
- VA-owned Drive. When they leave, the library leaves.
- `IMG_4203.mov` in `01-Raw`. Naming is the logging system.

## Example(s)
- The four folders *are* the four phases. If Process is looking in Downloads, the factory has already stalled.
- Overnight writer (`run-overnight-local-writer`) reads the same client folder spine — do not invent a second tree.

## Model routing
Lane `script` / `any`. Claude-only or Grok-only: create folders and the README, then stop. Humans drop the phone footage in.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) can run this nearly end to end: build the stage folders, write the README convention, construct the tracker, then loop the ingest sweep until zero unlogged or misnamed files remain — "mostly organized" is the failure mode this task exists to kill. Memory carries tracker state week to week, so each weekly review builds on the last instead of re-auditing from scratch. Document the build with a meta-article example.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /social-amplification (Stage 3: Content)
- Related: /content-factory (the pipeline this library feeds), /topic-wheel (tagging taxonomy), /blog-posting-guidelines (what Process needs from intake)
- Sibling skills, in run order: `create-a-3x3-video-grid` → this → `step-1-upload-video-to-google-drive-and-descript`
