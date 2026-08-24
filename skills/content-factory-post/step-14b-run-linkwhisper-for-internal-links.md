---
name: step-14b-run-linkwhisper-for-internal-links
description: Use LinkWhisper to surface and implement internal link suggestions in both directions, so the new post is woven into the SEO Tree instead of published as an orphan.
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 14b: Run LinkWhisper for internal links

**Use this when** RankMath is configured (Step 14a done) and the post needs its internal link web completed before publication.

## Inputs
- Draft post in WordPress with LinkWhisper active
- The site's SEO Tree map (which branch this post belongs to, from Step 13)
- The entity-linking decision tree: people → personal sites, companies → company sites, concepts → definitive articles

## Steps
1. Open LinkWhisper's suggestions for the post and review **outbound** candidates: links from this post to existing content.
2. Accept only suggestions that are topically real and respect SEO Tree direction — a leaf links up to its branch and across to true siblings; never link to a page that competes with an existing hub.
3. Rewrite every accepted anchor to 3–6 descriptive, keyword-relevant words. Reject generic anchors ("click here", "read more", bare URLs).
4. Review LinkWhisper's **inbound** suggestions: older related posts that should now link TO this post. Add links from the strongest, most relevant existing pages so the new post is not an orphan.
5. Check each link against the entity-linking decision tree — concept mentions go to the concept's definitive article, not to a random blog post about it.
6. Keep it contextual and restrained: a handful of links placed in body copy where they help the reader, not a link dump. Every post should link to at least one other post and one service page (the /website-qa-audit standard).
7. Preview, click-test every added link, and save the draft.

## Definition of done (QA checklist)
- [ ] Post links upward to its SEO Tree branch and to at least one other post and one service page
- [ ] At least one inbound link added from an existing relevant post (no orphan)
- [ ] All anchors 3–6 descriptive words; zero generic anchors
- [ ] Every link target follows the entity-linking decision tree; all links click-tested
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- The /internal-linking definitive article ("includes skill file for AI agents") documents the full 6-step linking process this step executes per-post. Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5 or comparable OpenAI/Google models) works LinkWhisper's full suggestion queue in both directions, rewrites every anchor to 3–6 descriptive words, then click-tests each link and re-checks the Definition of done — an orphaned post or one generic anchor sends it back through the loop, not into "done."
Because it holds the SEO Tree map and prior runs' accepted/rejected suggestions in memory, its accept/reject judgment sharpens with every post.
It closes each run by logging a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /internal-linking · /entity-linking · /seo-tree · /link-building
- Run order (Post stage): step-14a-configure-rankmath-seo-plugin → **step-14b-run-linkwhisper-for-internal-links** → set-wordpress-author-to-correct-person
