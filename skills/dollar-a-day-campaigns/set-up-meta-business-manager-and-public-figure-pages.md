---
name: set-up-meta-business-manager-and-public-figure-pages
description: Configure Meta Business Manager under the owner's control and stand up a Public Figure page so a personal brand can run Dollar a Day cleanly, with the person — not just the company — accruing the audience.
category: Dollar a Day Campaigns
stage: Promote
definitive_article: /dad
status: needs-work
---

# Set up Meta Business Manager and Public Figure pages

**Use this when** a personal brand (founder, owner, expert) needs the Meta-side structure to run $1/day — before campaigns, the accounts themselves must be owned, connected, and seeded.

## Inputs
- The owner's personal Facebook login (Business Manager must hang off their identity, not an agency's)
- Brand assets: real headshot, bio consistent with the personal site, payment method
- Seed content: one-minute videos, the WHY story, endorsements

## Steps
1. Create (or claim) **Meta Business Manager owned by the business owner's own account**. Agencies and VAs get partner/role access; they never get ownership — recovering a hijacked BM later is brutal.
2. Attach the assets inside Business Manager: ad account, pixel, Facebook page(s), Instagram professional account, payment method. Assign roles deliberately and minimally.
3. Create the **Public Figure page** for the person. The human is a separate entity from the company page — real name, real headshot, bio matching the personal brand site, links to it.
4. Connect the plumbing: pixel shared to the ad account, Instagram linked to the page, domain verified in Business Manager.
5. Seed the Public Figure page before spending: a handful of one-minute videos, the WHY story, and proof/endorsements. An ad click landing on a bare page is a dollar refunded to nobody.
6. Verify the machine end-to-end with a $1/day test boost from the Public Figure page — confirm delivery, billing, and pixel attribution.
7. Document access in writing: who owns, who administers, who can spend. File it with the digital-plumbing records.

## Definition of done (QA checklist)
- [ ] Business Manager owned by the owner; agency/VA access role-based only
- [ ] Ad account, pixel, pages, IG, payment, and domain all attached and connected
- [ ] Public Figure page live with consistent headshot, bio, and seed content
- [ ] $1/day test boost delivered and attributed; access map documented
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Failure modes
- Agency-owned Business Manager. Recovering it later is a months-long fight. Owner's login, always.
- Bare Public Figure page. An ad click onto an empty wall refunds the dollar to nobody.
- Pixel not attached to the ad account. Spend will not attribute.

## Example(s)
- Personal-brand Dollar a Day requires a Public Figure page *and* a company page as separate entities. The person accrues the audience.
- Seed content before spend: WHY video + one-minute answers + one lighthouse clip.

## Model routing
Computer-use, gating 5. Claude-only or Grok-only: browser. This unblocks every Promote skill; do it first.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude Fable 5 or comparable OpenAI/Google models) runs this setup to the full Definition of done — ownership under the owner, every asset attached, Public Figure page seeded, the $1 test boost delivered and attributed — and loops on whatever fails; "BM created, rest pending" is a failed run that leaves the brand unable to spend.
It self-verifies with the live test boost rather than the settings screens, and writes the access map to memory so later runs catch ownership drift (an agency quietly added as owner) before it becomes a recovery project.
Log each setup or recovery as a meta-article example so the library compounds.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /dad
- Related: /digital-plumbing (ownership and profile standards) · /personal-brand (Phase 1: plumbing for people)
- Run order (platform setup): **set-up-meta-business-manager-and-public-figure-pages** → create-facebook-instagram-campaigns-with-location-targeting → boost-one-minute-videos-for-personal-branding
