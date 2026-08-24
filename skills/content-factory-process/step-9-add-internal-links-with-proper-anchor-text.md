---
name: step-9-add-internal-links-with-proper-anchor-text
description: Insert internal links using the entity-linking decision tree — people to personal sites, companies to company sites, concepts to definitive articles — with descriptive 3–6 word anchors (Blog Posting Guidelines Step 9).
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 9: Add internal links with proper anchor text

**Use this when** the article text and images are in place (Step 8 complete) and the piece must be wired into the entity graph and SEO Tree.

## Inputs
- The drafted article
- The link-candidate list from Step 4 (related posts, definitive articles, service page)
- The entity-linking decision tree and the site's SEO Tree map
- List of every person, company, and concept mentioned in the article

## Steps
1. List every entity the article mentions: people, companies, and concepts. Each is a link decision, not an afterthought.
2. Apply the decision tree per entity: **people → their personal site** (e.g., a mention of Dennis Yu links to dennisyu.com), **companies → the company site** (Superior Fence & Rail to its own domain), **concepts → the concept's definitive article** (Dollar a Day to /dad, the pipeline to /content-factory).
3. Link UP the SEO Tree: this article (leaf) links to its branch/trunk pages and the relevant service page — at minimum one other post and one money page.
4. Write anchor text of 3–6 descriptive words that say where the link goes ("the Dollar a Day strategy," "Blog Posting Guidelines SOP"). "Click here," "this post," and bare URLs are banned.
5. Place links in body sentences where the entity naturally appears — contextual placement, not a link dump at the end.
6. Link each entity on first meaningful mention only; do not re-link the same target repeatedly.
7. Verify every URL resolves (no drafts, no typos, no redirects to the homepage when a hub exists).
8. Update the tracker ("Step 9 done") and hand off to `step-10-embed-source-video`. (LinkWhisper in Step 14b adds machine-suggested links later; this step is the human/agent judgment pass.)

## Definition of done (QA checklist)
- [ ] Every person, company, and concept mention resolved through the decision tree
- [ ] Article links to ≥1 other post and ≥1 service/money page, upward along the SEO Tree
- [ ] All anchors are 3–6 descriptive words — zero generic anchors
- [ ] Links placed contextually in body copy, first mention only
- [ ] Every link tested and resolving
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- The decision tree and anchor standards are documented at https://localservicespotlight.com/article-guidelines/ and in depth at /internal-linking (whose hub ships its own skill file — the model this library copies).
- Example needed as a standalone meta-article — run the Meta-Article Prompt after first documented run.

## Run on a persistent agent (Fable 5)

A persistent agent (Claude Fable 5, or a comparable OpenAI/Google model that loops and holds memory) lists every entity, resolves each through the decision tree, and loops until every anchor is descriptive and every URL actually resolves — one untested link fails the run. Memory compounds the entity-to-URL map with every article processed, so linking gets faster and stays consistent across the site instead of being re-researched per post. Log a meta-article example each run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/ (Step 9 of the 18-step SOP)
- Related: /internal-linking, /entity-linking, /seo-tree, /link-building
- Sibling skills, in run order: `step-8-add-photos-and-featured-image` → this → `step-10-embed-source-video`
