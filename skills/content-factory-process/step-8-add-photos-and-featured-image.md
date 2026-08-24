---
name: step-8-add-photos-and-featured-image
description: Add real photos — never stock — and set a unique featured image so the article carries visual proof instead of decoration (Blog Posting Guidelines Step 8).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 8: Add photos and featured image

**Use this when** the article text is complete through the hook (Step 7) and needs its imagery before linking and embedding.

## Inputs
- The drafted article
- Real image sources: stills from the source video, client/job-site photos, screenshots of real dashboards or results, event photos from the Content Library
- Image editing/compression tool access
- The brand's WordPress media conventions (file naming, alt text)

## Steps
1. Inventory image needs: every major section should have a relevant visual; no text-only stretch should span a full viewport (per the Website QA Audit content checks).
2. Pull candidates from real sources only — video stills, the client's actual photos, screenshots of the actual work. Stock photography is banned: it signals fake experience and fails the audit.
3. Choose or create a unique featured image for this post. Never reuse another post's featured image; uniqueness is checked at audit.
4. Crop and compress every image for sub-3-second mobile load (web-sized files, not camera originals).
5. Name files descriptively (`marko-sipila-hvac-quote-jobsite.jpg`, not `IMG_2041.jpg`).
6. Write descriptive alt text for every image — what is actually shown, useful to a screen reader, naturally including the keyword only where true.
7. Place images at the sections they evidence; add captions where a sentence of context helps (who, where, what result).
8. Update the tracker ("Step 8 done") and hand off to `step-9-add-internal-links-with-proper-anchor-text`.

## Definition of done (QA checklist)
- [ ] Zero stock images — every photo traceable to the real person, job, or screen
- [ ] Featured image is unique to this post
- [ ] Every image has descriptive alt text
- [ ] Files descriptively named and compressed for mobile speed
- [ ] No full-viewport text-only sections remain
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- The no-stock and unique-featured-image rules are enforced on every run at https://localservicespotlight.com/article-guidelines/ and re-verified by /website-qa-audit checks.
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or comparable OpenAI/Google models that loop and hold memory) inventories every section, pulls real images from the Content Library, writes alt text, compresses, and loops until zero stock, zero missing alt text, and no full-viewport text walls remain. Memory is what makes the uniqueness rule enforceable: the agent remembers every featured image already used, so duplicates get caught before publish, not at audit. Document the run with a meta-article example.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 8 of the 18-step SOP)
- Related: /website-qa-audit (image and alt-text audits), /content-factory
- Sibling skills, in run order: `step-7-write-hook-and-establish-context` → this → `step-9-add-internal-links-with-proper-anchor-text`
