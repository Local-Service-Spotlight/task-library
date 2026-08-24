---
name: step-5-write-article-from-transcript
description: Transform the cleaned transcript into a structured article that keeps the speaker's voice and stories while following GCT (Blog Posting Guidelines Step 5).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 5: Write article from transcript

**Use this when** the outline, timestamps, and GCT statement are ready (Step 4 complete) and the article body needs to be drafted.

## Inputs
- The cleaned, timestamped transcript and the H2/H3 outline
- The GCT statement and the primary keyword (the customer's phrasing)
- Research notes from Step 4
- The article working doc

## Steps
1. Write INTO the outline, section by section, using the transcript as the source of truth. The video is the experience; the article is its written form — not an AI essay on the same theme.
2. Keep the speaker's voice: first person, their phrasing, their stories, their numbers. If the speaker says "we lost the first three quotes," that line survives — specificity is the E-E-A-T.
3. Never let drafting tools invent claims, statistics, or anecdotes that are not in the video or the verified research notes. Everything stated must be traceable.
4. Place the primary keyword naturally in the first paragraph (the hook work in Step 7 will refine this paragraph — keyword presence is non-negotiable either way).
5. Write short paragraphs (2–4 sentences), active voice, plain language. No AI-fluff phrases — "in today's fast-paced world," "delve," "game-changer" and kin are banned by the guidelines.
6. Weave research in as support, clearly framed ("according to…"), keeping the speaker's first-hand experience as the spine.
7. Expand each section to fully answer its heading's promise — a reader landing on any H2 from search should get a complete answer.
8. Read the draft against the GCT statement once: does it serve the Goal, deliver the Content, speak to the Target? Fix or cut what fails. Update the tracker and hand off to `step-6-write-title-and-headings`.

## Definition of done (QA checklist)
- [ ] Every claim traces to the transcript or cited research — nothing invented
- [ ] First person, speaker's voice and stories preserved (spot-check against video)
- [ ] Primary keyword appears in the first paragraph
- [ ] Short paragraphs, active voice, zero AI-fluff phrases
- [ ] Each H2/H3 section fully answers its heading
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Articles produced for clients like Marko Sipila (HVAC Quote) and Zach Peyton (Superior Fence & Rail) follow this transcript-first drafting method; runs are linked from https://localservicespotlight.com/article-guidelines/.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) drafts section by section from the transcript, then self-audits the full Definition of done — every claim traceable, keyword in the first paragraph, zero banned fluff phrases — and rewrites until all checks pass, not until it "reads fine." Memory holds the speaker's voice patterns and the banned-phrase list from prior articles, so each draft starts closer to the standard. Log a meta-article example per run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 5 of the 18-step SOP)
- Related: /one-minute-video-guide (the source asset), /seo-tree
- Sibling skills, in run order: `step-4-research-edit-add-timestamps-and-outline` → this → `step-6-write-title-and-headings`
