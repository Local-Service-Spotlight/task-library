---
name: ensure-no-text-only-sections-spanning-full-viewport
description: Scans every page for sections that fill an entire screen with nothing but text, the wall-of-words pattern that makes visitors bounce.
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Ensure no text-only sections spanning full viewport

**Use this when** running Layer 2 (Content Architecture Checks) of the Website QA Audit — if a full screen scrolls by with no visual, you've lost the skimmer.

## Inputs
- Site URL plus the key pages (homepage, services, about, top posts)
- Desktop browser and a real phone (the mobile viewport is where text walls happen first)
- The audit report/spreadsheet for logging results

## Steps
1. Scroll each key page slowly on DESKTOP and note any point where the entire visible viewport contains only text — no photo, video, diagram, screenshot, or meaningful visual element.
2. Repeat on MOBILE: text stacks taller on phones, so sections that pass desktop often fail mobile — judge each viewport-height of scroll.
3. Record each violation with the page, the section heading, and which viewport(s) it fails in.
4. For each violation, name the fix: insert a relevant real image, embed the source video, break copy with a diagram or screenshot, or tighten the copy.
5. Re-check long blog posts specifically — body copy between images must not exceed one full viewport on mobile (matches the visual-rhythm intent of /blog-posting-guidelines).
6. Log violations and fixes in the audit report.

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
- [ ] The opening earns attention and explains this reader's situation, reason to care, useful outcome and mechanism under `step-7-write-hook-and-establish-context`; saved quoted meaning review is separate from image geometry
- [ ] Preview and ordinary-live first-screen geometry plus source-backed screenshot review pass on both viewports; actual evidence stored
- [ ] Zero sections on audited pages span a full viewport with text only, on both desktop and mobile
- [ ] Every violation has a named visual fix queued or applied
- [ ] Scroll-audit results logged per page in the audit report, linked back to /website-qa-audit

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run.

## Run on a persistent agent (Fable 5)
A persistent agent (Fable 5 / comparable OpenAI or Google models) scroll-audits every page on the site — not just the key ones — measuring rendered viewport-heights of unbroken text at both desktop and mobile widths, and loops insert-visual-recheck until zero full-viewport text walls remain anywhere.
Memory keeps per-page verdicts, so re-runs only re-measure pages with edited or new content — and every new long post triggers the mobile pass automatically.
Each run logs one worked example to ## Example(s) so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /website-qa-audit
- Related: /blog-posting-guidelines (short paragraphs, images throughout) · previous: verify-at-least-one-video-embed-on-homepage · next check: verify-minimum-5-distinct-images-on-homepage
