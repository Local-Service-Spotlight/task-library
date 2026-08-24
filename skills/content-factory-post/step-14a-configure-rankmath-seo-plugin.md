---
name: step-14a-configure-rankmath-seo-plugin
description: Set the focus keyword, SEO title, and meta description in RankMath and tune the post until it scores 70+ so the article competes in search from day one.
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 14a: Configure RankMath SEO plugin

**Use this when** the draft post is categorized and tagged (Step 13 done) and needs its on-page SEO locked in before internal linking and publication.

## Inputs
- Draft post in WordPress with RankMath active
- The article's primary keyword (chosen in Step 6 when the title and headings were written)
- The article's GCT — who the post targets and what it should rank for

## Steps
1. Open the RankMath panel on the post and set the **focus keyword** to the article's primary keyword.
2. Write the **SEO title**: under 60 characters, focus keyword near the front, written for a human click — no clickbait, no truncation in the SERP preview.
3. Write the **meta description**: under 160 characters, contains the focus keyword, gives a concrete reason to click.
4. Verify keyword placement RankMath checks for: in the SEO title, the permalink, the first paragraph, at least one H2/subheading, and image alt text where it reads naturally.
5. Run the RankMath analysis and resolve flagged items until the score is **70 or higher**. Fix real issues (missing keyword placements, thin sections, missing links) — never keyword-stuff to game the score.
6. Confirm the snippet preview renders correctly for desktop and mobile, and that canonical/schema defaults are sane for a standard post.
7. Save the draft and proceed to Step 14b (LinkWhisper).

## Definition of done (QA checklist)
- [ ] Focus keyword set; RankMath score 70+ achieved without keyword stuffing
- [ ] SEO title under 60 characters with focus keyword; meta description under 160 characters with focus keyword
- [ ] Keyword present in permalink, first paragraph, and at least one subheading
- [ ] SERP snippet preview reads cleanly with no truncation
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. The /website-qa-audit Layer 2 check "Verify Rank Math score above 70 on every page" is the site-wide audit twin of this per-post step.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5, or comparable OpenAI/Google models) works the RankMath loop mechanically — set keyword, write title and description, run analysis, fix flagged items, re-run — and does not stop at 68 or "mostly green"; it loops until the score is 70+ and every Definition-of-done box verifies, without keyword stuffing.
It remembers which fixes moved the score on prior posts (thin sections vs missing placements) and applies those first, then records this run's score path as a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /website-qa-audit · /seo-audit
- Run order (Post stage): step-13-categorize-post-and-add-tags → **step-14a-configure-rankmath-seo-plugin** → step-14b-run-linkwhisper-for-internal-links
