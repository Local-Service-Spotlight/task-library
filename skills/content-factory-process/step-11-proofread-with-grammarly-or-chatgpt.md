---
name: step-11-proofread-with-grammarly-or-chatgpt
description: Run the finished draft through Grammarly or ChatGPT for grammar, tone, and readability — without letting the tools sand off the speaker's voice (Blog Posting Guidelines Step 11).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 11: Proofread with Grammarly or ChatGPT

**Use this when** the article is complete with links, images, and embed (Step 10 done) — the final Process-stage pass before the Post stage takes over.

## Inputs
- The complete article draft
- Grammarly or ChatGPT access
- The verified transcript (fact-check source) and the GCT statement
- The correct spellings list (Marko Sipila, Zach Peyton, George Paladichuk, NaiL AI, etc.)

## Steps
1. Run the draft through Grammarly or ChatGPT scoped to grammar, punctuation, readability, and tone consistency — explicitly instruct the tool NOT to rewrite voice, add content, or "enhance" phrasing.
2. Review every suggestion individually. Accept mechanical fixes; reject any change that genericizes the speaker's phrasing or injects AI-fluff vocabulary.
3. Fact-check against the transcript: every number, name, claim, and quote in the article must match what was actually said or the cited research.
4. Verify all proper nouns against the spellings list — proofreading tools routinely "correct" real names into wrong ones.
5. Read the article aloud (or via text-to-speech) top to bottom — the strongest catch for clunky sentences, repeated words, and broken flow.
6. Re-verify the load-bearing SEO elements survived editing: focus keyword still in the first paragraph, title under 60 characters, meta under 160, headings intact.
7. Check formatting hygiene: short paragraphs held, no double spaces, consistent capitalization in headings, captions present.
8. Update the tracker ("Step 11 done — Process stage complete") and hand off to the Post stage (`step-12-post-article-on-wordpress`).

## Definition of done (QA checklist)
- [ ] Grammar/readability pass completed with each suggestion reviewed, not bulk-accepted
- [ ] Speaker's voice intact — spot-check 3 passages against the transcript
- [ ] All facts, numbers, and names verified (spellings list applied)
- [ ] Keyword, title, and meta specs still satisfied post-edit
- [ ] Read-aloud pass completed with fixes applied
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- The proofread gate is Step 11 of every run documented at https://localservicespotlight.com/article-guidelines/, immediately before WordPress posting.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) reviews every suggestion individually — never bulk-accepts — and loops the fact-check until each number, name, and quote matches the transcript and the SEO specs still hold after edits. Memory keeps the growing correct-spellings list, so every name a past run verified protects every future article. Log a meta-article example each run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 11 of the 18-step SOP)
- Related: /website-qa-audit (the standards this pass pre-empts)
- Sibling skills, in run order: `step-10-embed-source-video` → this → `step-12-post-article-on-wordpress` (Post stage)
