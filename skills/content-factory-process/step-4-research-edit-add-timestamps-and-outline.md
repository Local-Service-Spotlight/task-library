---
name: step-4-research-edit-add-timestamps-and-outline
description: Research the topic, clean the transcript, mark timestamps at topic shifts, and build the H2/H3 outline that the article will be written into (Blog Posting Guidelines Step 4).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 4: Research, edit, add timestamps and outline

**Use this when** GCT is defined (Step 3 complete) and the raw transcript needs to become a structured writing plan.

## Inputs
- The verified transcript and the GCT statement from Step 3
- Access to the brand's site to survey existing related content (SEO Tree placement, internal-link candidates)
- Search access to see what currently answers this customer question
- The article working doc

## Steps
1. Research the topic: search the customer question (the Targeting phrasing) and note what already ranks — what they cover, what they miss, what only this video's first-hand experience can add.
2. Survey the brand's own site for related posts and the definitive articles this piece should link to later — note where this article fits on the SEO Tree (which trunk/branch it hangs from) before writing.
3. Clean the transcript: cut false starts, redundancies, and tangents that serve no point. Preserve the speaker's voice, phrasing, and stories — edit for clarity, never into generic AI-speak.
4. Add a timestamp marker at every topic shift in the transcript (e.g., `[02:14]` where the story starts). These drive the outline now and clip extraction later.
5. Build the outline: map each timestamped segment to a proposed H2 (or H3 under it), ordered for the reader rather than strictly chronologically if the spoken order rambles.
6. Check the outline against GCT: every section must serve the Goal and speak to the Target; cut sections that do neither.
7. Slot research findings into the outline as expansion notes ("add data here," "compare to X") — clearly separated from what the speaker said.
8. Update the tracker ("Step 4 done — outline ready") and hand off to `step-5-write-article-from-transcript`.

## Definition of done (QA checklist)
- [ ] Competing answers to the question reviewed and gaps noted
- [ ] SEO Tree placement and internal-link candidates identified before writing
- [ ] Transcript cleaned with speaker's voice intact (spot-check 3 passages against audio)
- [ ] Timestamps marked at every topic shift
- [ ] H2/H3 outline maps to timestamps and survives the GCT check
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Step 4 of every article run documented at https://localservicespotlight.com/article-guidelines/; the timestamp work also powers `extract-15-60-second-clips-from-long-form-video`.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or comparable OpenAI/Google models that loop and hold memory) runs the search research, surveys the site, cleans the transcript, timestamps every topic shift, then loops the outline against the GCT check until every section earns its place — an outline with one orphan section is not done. Memory makes this step compound: SEO Tree placement and internal-link candidates learned each run carry into the next, so research starts from accumulated site knowledge, not a blank page. Document the run with a meta-article example.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 4 of the 18-step SOP)
- Related: /seo-tree (placement), /internal-linking (link candidates)
- Sibling skills, in run order: `step-3-watch-video-and-identify-gct` → this → `step-5-write-article-from-transcript`
