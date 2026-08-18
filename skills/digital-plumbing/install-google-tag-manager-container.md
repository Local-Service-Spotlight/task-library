---
name: install-google-tag-manager-container
description: Install one Google Tag Manager container on every page of the site so all future tracking (GA4, Meta pixel, call events) deploys without editing code.
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: gap
---

# Install Google Tag Manager Container

**Use this when** tracking tags are hard-coded into the theme, scattered across plugins, or missing entirely — GTM becomes the single tap point for all measurement.

## Inputs
- Google account owned by the business (GTM container must live in the client's account, with agency added as a user)
- WordPress admin access (theme header editing or a header/footer plugin)
- Google Tag Assistant for verification

## Steps
1. In the business owner's Google account, create a GTM account (company name) and one Web container named for the domain. One site, one container — never share containers across sites.
2. Copy the two install snippets GTM provides: the script for the head and the noscript for the opening of the body.
3. Install both snippets on every page — via the theme's header template or a header/footer plugin, so all templates (pages, posts, archives) carry it.
4. Publish the container. An unpublished container shows installed but fires nothing — this is the most common silent failure.
5. Verify with Tag Assistant: load the homepage, a service page, a blog post, and the contact/thank-you page; the container ID must appear and fire on each.
6. Migrate existing hard-coded tags (GA4, Meta pixel) into GTM as tags, then remove the hard-coded copies to prevent double-firing.
7. Add the agency/operator as a container User (the owner stays Admin). Record the container ID (GTM-XXXXXXX) in the client record.

## Definition of done (QA checklist)
- [ ] GTM container ID present and fires on every page in Tag Assistant (home, service, post, thank-you tested)
- [ ] Container is published — current live version, not just preview
- [ ] No duplicate/hard-coded tags left outside GTM (no double-firing in Tag Assistant)
- [ ] Container lives in the client's Google account; container ID documented
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Failure modes
- Installed but never **published**. Tag Assistant shows the ID; nothing fires. Most common silent failure.
- One container shared across sites. Never. One site, one container, in the *client's* Google account.
- Hard-coded GA4 left in the theme after migrating to GTM = double counting.

## Example(s)
- anthonyhilb.com (July 2026): no GTM, no GA4, no pixel. Sixteen articles, zero measurement. GTM is the tap point the other Gate skills deploy into.
- Website QA Layer 1: "GTM installed and firing on every page" is this skill's DoD, not a later audit surprise.

## Model routing
Computer-use (GTM + theme/header). Claude-only or Grok-only: browser. Scripts can verify the container ID in page HTML after install.

## Definitive article & links
- Hub: GAP — to be written. "How to Install and Configure GTM" is queued (High Priority) in Gaps & Tasks to Create; until it ships, /digital-plumbing is the parent hub.
- Related (run order): this → set-up-ga4-with-internal-traffic-filtering → install-meta-pixel-with-standard-events → set-up-call-tracking-for-phone-conversions
- Cross-links: /website-qa-audit (Layer 1: "GTM installed and firing on every page") · /dad (working pixels are a prerequisite)
