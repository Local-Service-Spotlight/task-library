---
name: step-13-categorize-post-and-add-tags
description: Assign the WordPress post to its SEO Tree branch category and add attribute tags so readers, agents, and the REST API can pull it by topic, stage, and entity.
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 13: Categorize post and add tags

**Use this when** the article exists as a WordPress draft (Step 12 done) and its taxonomy must be set before SEO configuration.

## Inputs
- Draft post in WordPress
- The site's category taxonomy — categories are SEO Tree branches, established per /internal-linking Step 2
- The article's GCT and its intended position on the SEO Tree

## Steps
1. Identify the SEO Tree branch this article supports: which trunk topic, which branch subtopic? If no branch fits, stop — you may be about to create an orphan; resolve placement (see place-content-on-seo-tree-with-proper-links) before continuing.
2. In the Categories panel, check the one branch category that matches. One primary category; add a second only when the piece genuinely serves two branches. Never leave a post "Uncategorized."
3. Add tags as **attributes, not topics**: content stage (e.g., `Stage: Post` where the site uses Content Factory stage tags), format (one-minute video, case study, audit), people and companies featured, and cross-cutting `Topic:` tags.
4. Reuse existing tags via autocomplete. Never create near-duplicates ("dollar-a-day" vs "dollar a day") — duplicate tags fracture the taxonomy.
5. Open the category archive and confirm the post will sit beside true siblings; if the archive is empty or mismatched, re-check the taxonomy against /internal-linking Step 2 before publishing.
6. Save the draft and proceed to Step 14a (RankMath).

## Definition of done (QA checklist)
- [ ] Post assigned to exactly one correct SEO Tree branch category (two max) — not Uncategorized
- [ ] Tags are reused attributes (stage, format, people, companies, topics); zero new duplicate tags
- [ ] Category archive lists the post among genuine topical siblings
- [ ] An agent could retrieve this post via REST API by category + stage tag
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. Good first candidate: a Marko Sipila (HVAC Quote) article categorized under its service branch with `Stage: Post` tagging.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5 or a comparable OpenAI/Google model) reads the site's full category and tag taxonomy via the REST API before touching the post, assigns the branch, then re-queries the archive to self-verify every Definition-of-done item — a non-sibling archive or a near-duplicate tag triggers a fix and a full re-check, not a partial pass.
It keeps the SEO Tree map and the canonical tag list in memory across runs, so taxonomy stays consistent article after article instead of drifting.
Each run it logs a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /seo-tree · /internal-linking
- Run order (Post stage): step-12-post-article-on-wordpress → **step-13-categorize-post-and-add-tags** → step-14a-configure-rankmath-seo-plugin
