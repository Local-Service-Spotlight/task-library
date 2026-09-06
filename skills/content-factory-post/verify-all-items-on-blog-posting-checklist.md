---
name: verify-all-items-on-blog-posting-checklist
description: Walk the complete Blog Posting verification checklist item by item as a binary gate, so nothing publishes (or ships to Promote) with a known miss.
category: Content Factory — Post
stage: Post
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Verify all items on Blog Posting checklist

**Use this when** a post is staged for publication, and again inside Step 17 — this checklist is the formal gate; every item is pass/fail, no judgment calls.

## Inputs
- The staged or live post URL
- The Blog Posting Guidelines checklist (hub: https://localservicespotlight.com/article-guidelines/)
- Access to fix failures or route them back to the owning step

## Steps
1. Verify the content items: SEO title under 60 characters with focus keyword · meta description under 160 characters · primary keyword in the first paragraph · H2/H3 structure · short paragraphs · active voice · no AI-fluff phrases · first person on a personal-brand site.
2. Verify the story and authority items: every material proof point is a source-linked real scene, lesson, quote, photo, video, or primary record with a compact receipt · a recognizable name supplies context rather than status · no trophy-name paragraph · relationship nouns do not outrun the evidence.
3. Verify the public-copy hygiene items: no repeated defensive caveats · no confidence scores, proof-record IDs, inventory/harvester labels, or repurposing instructions unless that system is the article's actual subject. Preserve a materially necessary legal, regulatory, or compliance disclosure, scoped to the claim it governs; do not classify editorial reassurance as compliance.
4. Verify testimonials and praise: quotation is exact · person is named · applicable role/company or city is shown · primary source is linked · permission is recorded where required. First-name-only, initials, "happy customer," unattributed paraphrases, and domain/company-only attribution fail publication and remain HOLD.
5. Verify the media items: no stock images anywhere · descriptive alt text on every image · unique featured image · source video embedded and playing · proof image/video matches the captioned person, place/event, and claim.
6. Verify the linking items: internal links follow the entity-linking decision tree (people → personal sites, companies → company sites, concepts → definitive articles) · anchors are 3–6 descriptive words · post links to at least one other post and one service page · upward SEO Tree link present.
7. Verify the WordPress items: built in Gutenberg (no builder) · category = SEO Tree branch · tags set · author = site owner · permalink contains focus keyword · RankMath score 70+.
8. Mark each item pass/fail in the tracker. A single fail blocks publication — fix it now or send it back to the owning step: story/voice to Step 5 or Step 7, grading to Jennifer, media to Step 8, WordPress to Steps 12–14b, and sitewide proof to the Website QA checks.
9. Re-run until every item passes, then record the completed checklist with date and operator so the audit trail exists.

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
- [ ] Every checklist item explicitly marked pass — zero skipped, zero "close enough"
- [ ] Story/authority voice passed: first-person personal site, sourced scenes, compact receipts, no trophy-name paragraphs, and evidence-bound relationship nouns
- [ ] Zero repeated defensive caveats or stray internal production metadata; any retained legal/compliance disclosure is materially necessary and scoped
- [ ] Every testimonial/praise item is exact, named, attributable, source-linked, and permissioned where required; anonymous/domain-only items remain HOLD
- [ ] All failures fixed at their owning step and re-verified
- [ ] Completed checklist logged with date and operator
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. Candidate: a published checklist run on a Marko Sipila (HVAC Quote) article showing one caught failure and its fix.

## Run on a persistent agent (Fable 5)
This skill IS the self-verification loop a persistent agent (Fable 5 or comparable OpenAI/Google models) runs by default: every item binary pass/fail, any fail routed to its owning step, fixed, and the whole checklist re-run from the top — repeating until 100% pass, because "close enough" is exactly what this gate exists to block.
The agent keeps each completed checklist in memory as the audit trail, so recurring failure patterns surface across runs and get fixed upstream.
It logs a meta-article example per run so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: https://localservicespotlight.com/article-guidelines/
- Related: /website-qa-audit · /entity-linking · /seo-tree
- Run order (Post stage): runs before publish and again inside **step-17-final-formatting-and-qa-checks** as the closing gate
