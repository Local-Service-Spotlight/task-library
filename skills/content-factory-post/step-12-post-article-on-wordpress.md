---
name: step-12-post-article-on-wordpress
description: Publish a finished Content Factory article on the client's WordPress site in the Gutenberg block editor with clean formatting, ready for categorization, SEO, and distribution.
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 12: Post article on WordPress

**Use this when** an article has cleared Process (Steps 1–11: written, photographed, linked, video-embedded, proofread) and is ready to go onto the site.

## Inputs
- Final proofread article with title, headings, hook, photos, internal links, and embedded source video
- WordPress editor access to the target site with the Gutenberg block editor enabled
- Unique featured image file (real photo, never stock) plus all in-article photos
- The article's GCT (Goals, Content, Targeting) established in Step 3

## Steps
1. Create a new **Post** (not a Page) and build the article in the **Gutenberg block editor** — never Cornerstone or any proprietary builder; builder content is opaque to AI agents and hard to update programmatically.
2. Rebuild the structure in blocks: one H1 (the title), H2s for major sections, H3s for subsections, short paragraphs (2–4 sentences), active voice, no AI-fluff phrases.
3. Confirm the primary keyword appears in the first paragraph (Blog Posting Guidelines requirement).
4. Insert every image at its planned position with descriptive alt text; set the unique featured image. All photos real — zero stock imagery.
5. Embed the source video where Step 10 placed it and confirm it plays in preview.
6. Verify every internal link from Step 9 survived the paste: descriptive 3–6 word anchor text (never "click here"), targets per the entity-linking decision tree (people → personal sites, companies → company sites, concepts → definitive articles).
7. Set the permalink slug: short, lowercase, contains the focus keyword.
8. Save as **draft**, preview on desktop and mobile, fix any broken blocks or image overflow. Do not publish yet — Steps 13–14b, author check, SEO Tree placement, and the Blog Posting checklist gate publication.

## Definition of done (QA checklist)
- [ ] Post exists as a draft in Gutenberg with zero builder shortcodes; previews cleanly on desktop and mobile
- [ ] H1/H2/H3 hierarchy correct; paragraphs short; active voice; primary keyword in first paragraph
- [ ] All images real with alt text; unique featured image set; source video embedded and playing
- [ ] All internal links intact with 3–6 word descriptive anchors following the entity-linking decision tree
- [ ] Permalink contains the focus keyword
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- First documented run candidate: a Marko Sipila (HVAC Quote) one-minute-video article posted through this step. Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude Fable 5, or a comparable OpenAI/Google frontier model) builds the draft in Gutenberg and loops preview → fix → re-preview until every Definition-of-done box passes — one broken anchor or a keyword missing from the first paragraph means another pass, not "close enough."
It pulls the GCT, link map, and video placement from Steps 3/9/10 out of memory instead of re-deriving them, and writes the slug and block structure back for Steps 13–14b.
Each run it logs a meta-article example into Example(s), so the next article starts from a worked case.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /content-factory · /entity-linking · /one-minute-video-guide
- Run order (Post stage): **step-12-post-article-on-wordpress** → step-13-categorize-post-and-add-tags → step-14a-configure-rankmath-seo-plugin → step-14b-run-linkwhisper-for-internal-links
