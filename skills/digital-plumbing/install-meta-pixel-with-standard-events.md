---
name: install-meta-pixel-with-standard-events
description: Install the Meta pixel on every page with standard events (Lead, Contact) on the actions that matter, so Dollar a Day campaigns can optimize and retarget.
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: gap
---

# Install Meta Pixel With Standard Events

**Use this when** the site has no Meta pixel, the pixel sits in an agency's Business Manager, or it fires PageView only with no events on leads — Dollar a Day is blind without it.

## Inputs
- Client's own Meta Business Manager with the ad account and Facebook page (see set-up siblings under /dad if missing)
- GTM container installed and firing (run install-google-tag-manager-container first)
- Defined conversion actions: form thank-you state, click-to-call links
- Meta Pixel Helper browser extension for verification

## Steps
1. In the client's Meta Events Manager, create or locate the pixel/dataset. It must live in the client's Business Manager — pixels in an agency's BM hold the client's data hostage.
2. Deploy the base pixel through GTM on All Pages (Meta's GTM integration or a custom HTML tag with the pixel base code). Remove any old hard-coded pixel to prevent double-firing.
3. Add standard events on the real conversion moments: fire Lead on the form thank-you state and Contact on click-to-call taps, using the GTM triggers built in those sibling skills.
4. Verify page coverage with Meta Pixel Helper: homepage, service page, blog post, thank-you page — base PageView green on each, no duplicate-pixel warnings.
5. Verify events with Events Manager's Test Events: submit a test form and tap a tel: link; Lead and Contact must appear with the correct pixel ID.
6. Confirm events keep arriving in Events Manager over the next day, then document the pixel ID in the client record.
7. Hand off to amplification: the pixel now powers custom audiences and conversion optimization for /dad campaigns.

## Definition of done (QA checklist)
- [ ] Base pixel fires on every tested page (Pixel Helper green, no duplicates)
- [ ] Lead fires on real form submission; Contact fires on click-to-call (seen in Test Events)
- [ ] Events arriving in Events Manager under the client's Business Manager, correct pixel ID
- [ ] Old hard-coded pixel code removed; pixel ID documented
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Failure modes
- Pixel in the *agency* Business Manager. The client's data is hostage; Dollar a Day cannot be handed off. Always the client's BM.
- Hard-coded pixel plus GTM pixel = double fire. Ads Manager will look "healthy" and attribution will lie.
- PageView only. Without Lead/Contact, $1/day optimizes for nothing.

## Example(s)
- anthonyhilb.com (July 2026): 16 articles shipped with **no pixel, no GA4, no GTM**. Promote could not run; MAA had no events. The Gate was the work; the articles were decoration until plumbing existed.
- HVAC Quote / Marko Sipila: $1/day on winners only works because the pixel and the YouTube line were already in place.

## Model routing
Computer-use (Events Manager + GTM UI). Claude-only or Grok-only: same steps, browser required. Scripts cannot mint a pixel.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude, ChatGPT, or Grok with a browser) deploys via GTM, fires real test events, then checks back over the following day to confirm Lead and Contact keep arriving — looping until the entire Definition of done passes, not 90%.
Write the pixel ID into the access register so the next engine does not have to hunt Events Manager.

## Definitive article & links
- Hub: GAP — to be written (no dedicated hub yet; flagged in Gaps & Tasks to Create scope; parent concept: /digital-plumbing)
- Related (run order): install-google-tag-manager-container → set-up-ga4-with-internal-traffic-filtering → this → set-up-call-tracking-for-phone-conversions
- Cross-links: /dad (pixels are a stated prerequisite) · /website-qa-audit (Layer 1: "Meta pixel installed with lead events") · /social-amplification (Stage 1 Plumbing)
