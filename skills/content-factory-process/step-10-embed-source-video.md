---
name: step-10-embed-source-video
description: Embed the original source video in the article so readers get the first-hand footage alongside the written version (Blog Posting Guidelines Step 10).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 10: Embed source video

**Use this when** the article is linked and illustrated (Step 9 complete) and the source video is hosted somewhere embeddable.

## Inputs
- The article draft in progress
- The hosted source video (typically the brand's YouTube upload of the processed video; the Post stage's YouTube task handles hosting if not yet done)
- The Content Library tracker row linking article and video

## Steps
1. Confirm the source video is hosted on the brand's own channel (YouTube upload with proper title/description). If it is not yet hosted, trigger the Post-stage YouTube upload task first — do not embed from someone else's channel.
2. Embed the video into the article near the content it supports — usually directly after the hook/intro, so readers immediately see the real person behind the words.
3. Use the standard WordPress/Gutenberg embed block (paste the YouTube URL), not a custom player or builder widget — builder content is opaque to agents and breaks updates.
4. Add one line of context above or below the embed: who is speaking and what the clip covers ("Marko Sipila explains why the lowest HVAC quote cost the most").
5. Preview on mobile: the embed must render responsively and not block page load (lazy-load is WordPress default behavior; verify the page still feels fast).
6. Verify article and video reinforce each other: the article should reference the video naturally ("in the video above"), and the YouTube description should link back to the article.
7. Update the Content Library tracker so the article row and video row reference each other.
8. Update the tracker ("Step 10 done") and hand off to `step-11-proofread-with-grammarly-or-chatgpt`.

## Definition of done (QA checklist)
- [ ] Source video embedded from the brand's own channel
- [ ] Placed adjacent to the content it supports, with a line of context
- [ ] Standard Gutenberg embed block used (no proprietary builder)
- [ ] Plays and renders responsively on mobile without wrecking load time
- [ ] Article ↔ video cross-references in place (and logged in the tracker)
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- Every Content Factory article embeds its source video per https://localservicespotlight.com/article-guidelines/; the homepage video-embed requirement in /website-qa-audit applies the same principle site-wide.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or comparable long-horizon OpenAI/Google models) verifies the video sits on the brand's own channel (triggering the Post-stage upload task if not), embeds via the standard block, checks mobile rendering, and loops until the article-video cross-references are live in both directions and logged — one-way linking is not done. Memory ties article rows to video rows across runs, so nothing orphans in the tracker. Close with a logged meta-article example.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 10 of the 18-step SOP)
- Related: /website-qa-audit (video-embed checks), /content-factory
- Sibling skills, in run order: `step-9-add-internal-links-with-proper-anchor-text` → this → `step-11-proofread-with-grammarly-or-chatgpt`
