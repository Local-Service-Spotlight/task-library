---
name: step-17-final-formatting-and-qa-checks
description: Run the final formatting, link, and quality pass across the live article and its distribution so the piece is verifiably done before handing off to the Promote stage.
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 17: Final formatting and QA checks

**Use this when** the article is live, distributed, and the client notified — this is the closing gate of the Post stage before amplification launches.

## Inputs
- Live article URL plus its distribution URLs (YouTube, Facebook page, LinkedIn, 44K group)
- The Blog Posting checklist (sibling skill: verify-all-items-on-blog-posting-checklist)
- Editor access to fix anything found

## Steps
1. Open the live post on desktop **and** mobile. Check heading hierarchy, paragraph spacing, image rendering, and that no Gutenberg block broke after publish. Read the rendered copy, not only the editor text.
2. Click-test every link: internal links (anchors and targets per the entity-linking decision tree), external links, and any CTA. Fix or remove broken ones immediately.
3. Confirm the embedded video plays, the featured image renders in social share previews, and all images still carry alt text. On an authority, relationship, or story page, confirm each material proof block includes a real scene in photo/video/primary record form and a compact source receipt.
4. Fail public copy that contains a trophy-name paragraph, repeated defensive caveats, or internal scoring/inventory/repurposing language. Also fail relationship nouns stronger than their source and anonymous or domain-only testimonials. A materially necessary legal, regulatory, or compliance disclosure remains allowed when it is scoped to the claim it governs.
5. On a personal-brand site, confirm the narrative is first person. Route a voice failure back to Step 5 or Step 7, and route a proof/attribution failure to its Website QA owner. Do not "fix" a weak claim by adding more reassurance; narrow it, source it, or place it on HOLD.
6. Re-check RankMath after any post-publish edits — score must still be 70+, SEO title under 60 characters, meta description under 160.
7. Verify housekeeping: author = site owner, category = correct SEO Tree branch, tags intact, permalink unchanged since indexing.
8. Verify the distribution loop is closed: article embeds the YouTube video; YouTube description links the article; Facebook, LinkedIn, and group posts are live and logged.
9. Run verify-all-items-on-blog-posting-checklist as the formal item-by-item gate, fix any failure at its owning step, then mark the piece **done** in the tracker and hand the post URL set to the Promote stage.

## Required first-screen visual gate

Every visitor-facing page, including home, money, relationship, archive and
utility pages, must show a relevant authentic photograph, source-video poster
or useful diagram above the fold. At 390x844 and 1280x800, test the anonymous
unscrolled first visit with JavaScript on and off. A logo, social icon, decorative
background, thin strip, broken image or empty player rectangle fails.

Use the [canonical numeric standard](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/standards/visuals-above-the-fold.md) and its
[shared browser checker](https://github.com/dennisyu/local-service-spotlight-skills/blob/main/scripts/rendered_visual_check.mjs) in the real builder/publisher:
`rendered_visual_check.mjs --url URL --selector CSS --output DIRECTORY`.
Measure the complete preview with site chrome before release and the ordinary
public URL after the authorized release. Save both screenshot/JSON receipts.
The checker can measure a loaded photographic CSS background as well as images,
diagrams and video posters. Its geometry pass remains `REVIEW_REQUIRED` until
an independent reviewer opens the actual screenshots and source evidence and
accepts the relevance, authentic moment, useful crop, labels and permission.
A source-order regex or an `<img>` count cannot mark this gate complete.

YouTube uses youtube-nocookie.com with rel=0, cc_load_policy=1 and cc_lang_pref.
No media autoplays on first paint. Before any separate playback verification,
mute and set volume zero; if that cannot be verified, use metadata, captions,
frames or a loaded poster and record playback NOT_TESTED. Never play through
the user's speakers without their explicit current request.

## Definition of done (QA checklist)
- [ ] The live first 2–3 sentences pass `step-7-write-hook-and-establish-context`: actual reader/situation, reason to care, useful outcome and supporting mechanism; exact text and quoted reviewer evidence retained, and the body delivers its promise
- [ ] Preview and ordinary-live first-screen geometry plus source-backed screenshot review pass on both viewports; actual evidence stored
- [ ] Live post renders cleanly on desktop and mobile; zero broken links or blocks
- [ ] Video plays; featured image and alt text intact; authority/story proof blocks show real scenes with compact receipts
- [ ] First-person personal-brand voice; zero trophy-name paragraphs, repeated defensive caveats, or public internal production metadata
- [ ] Relationship language matches evidence; published testimonials are exact, named, attributable, and source-linked; anonymous/domain-only praise is HOLD
- [ ] Any retained legal/compliance disclosure is materially necessary, scoped, and not counted as a voice failure
- [ ] RankMath still 70+
- [ ] Author, category, tags, and permalink verified correct
- [ ] Distribution loop closed and logged (YouTube ↔ article, FB, LinkedIn, 44K group)
- [ ] Full Blog Posting checklist passed; piece marked done and handed to Promote
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run documenting a full Step 12→17 pass on one client article.

## Run on a persistent agent (Fable 5)
This closing gate is where a persistent agent (Fable 5, or comparable OpenAI/Google models) earns its keep: it re-opens the live post on desktop and mobile, click-tests every link, re-runs RankMath, verifies the distribution loop, and cycles fix → re-verify until every Definition-of-done box passes — six of seven is a failing grade, not a pass.
Because it ran Steps 12–16 itself, memory tells it exactly what to re-check and which step owns any failure it finds.
Each gate run is logged as a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /website-qa-audit (the site-wide audit this per-post QA rolls up into) · /content-factory
- Run order (Post stage): share-in-44k-facebook-group → **step-17-final-formatting-and-qa-checks** → Promote stage (boost-top-3-5-facebook-posts)
