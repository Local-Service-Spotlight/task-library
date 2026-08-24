---
name: step-3-watch-video-and-identify-gct
description: Watch the full video and pin down Goals, Content, and Targeting — in that order — so every downstream writing decision serves a defined purpose (Blog Posting Guidelines Step 3).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 3: Watch video and identify GCT

**Use this when** the transcript is verified (Step 2 complete) and before a single word of the article is outlined or written.

## Inputs
- The full video and verified transcript in Descript
- The brand's mission and 90-day goals (from SAE Stage 2) for Goal alignment
- The Topic Wheel entry this video came from, if logged
- A working doc for the article (where the GCT statement will live)

## Steps
1. Watch the ENTIRE video, not a skim — tone, emphasis, and throwaway stories carry meaning the transcript alone loses.
2. Identify the **Goal** first: what business outcome should this content drive (rank for a question, prove expertise, support a service page, feed an ad)? Tie it to the brand's stated goals.
3. Identify the **Content** second: the single core insight, story, or answer actually present in the video. The article may only claim what the video supports.
4. Identify the **Targeting** third: exactly who this is for — which customer, at which funnel level (Audience, Engagement, or Conversion), asking which question in which words.
5. Keep the order strict: Goals → Content → Targeting. Content decisions made before goals produce orphan articles; targeting chosen before content produces clickbait.
6. Write a three-line GCT statement at the top of the working doc. Example shape: "G: rank for [customer question] and feed the [service] page. C: [the one insight]. T: [who, funnel level]."
7. Derive the primary keyword candidate from the Targeting line — the customer's own phrasing of the question.
8. Update the tracker ("Step 3 done — GCT set") and hand off to `step-4-research-edit-add-timestamps-and-outline`.

## Definition of done (QA checklist)
- [ ] Video watched in full (not transcript-skimmed)
- [ ] GCT statement written in Goals → Content → Targeting order, three concrete lines
- [ ] Goal traces to a real business outcome, not "post content"
- [ ] Content claim is supported by what is actually said in the video
- [ ] Primary keyword candidate captured in the customer's own words
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- GCT-before-writing is the discipline behind every article documented at https://localservicespotlight.com/article-guidelines/; the framework itself is one of the Nine Triangles (/nine-triangles).
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) watches the full video, drafts the GCT statement in strict Goals → Content → Targeting order, then self-verifies every Definition-of-done line — Goal tied to a real outcome, Content actually in the video, keyword in the customer's words — and loops until all pass. Memory holds the brand's Stage 2 goals across runs, so every video's Goal line stays consistent with the 90-day plan instead of being reinvented per article. Log a meta-article example each run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 3 of the 18-step SOP)
- Related: /nine-triangles (GCT triangle), /topic-wheel (where the question came from)
- Sibling skills, in run order: `step-2-transcribe-video-using-descript` → this → `step-4-research-edit-add-timestamps-and-outline`
