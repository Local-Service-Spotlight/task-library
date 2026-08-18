---
name: set-up-ga4-with-internal-traffic-filtering
description: Stand up a correctly-owned GA4 property that collects on every page and filters out the owner's and team's own visits, so the numbers mean something.
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: gap
---

# Set Up GA4 With Internal Traffic Filtering

**Use this when** the site has no GA4, GA4 lives in some agency's account, or analytics are polluted by the owner refreshing their own homepage all day.

## Inputs
- Business owner's Google account (the GA4 property must be owned by the client; operators get added as users)
- GTM container installed and firing (run install-google-tag-manager-container first)
- The office/home/team IP addresses to exclude

## Steps
1. In the owner's Google account, create the GA4 account and property with correct business name, time zone, and currency. Add the operator with Editor access — ownership never leaves the client.
2. Create the Web data stream for the https domain and note the Measurement ID (G-XXXXXXX).
3. Deploy via GTM: add the Google tag / GA4 configuration tag firing on All Pages. No hard-coded snippets — GTM is the tap point.
4. Define internal traffic: in the data stream's tag settings, add an internal-traffic rule listing the owner's office/home IPs and team IPs.
5. Activate the filter: in Admin → Data settings → Data filters, switch the Internal Traffic filter from Testing to Active. In Testing it still counts everything — the most common GA4 mistake.
6. Mark the conversions: register form-submit and click-to-call as key events (fed by the GTM events from those sibling skills).
7. Verify: with Realtime/DebugView open, browse the site from an excluded IP — your visits must NOT appear. Then confirm a normal visit (phone on cellular) does appear, and key events fire.
8. Record property ID, Measurement ID, and excluded IPs in the client record.

## Definition of done (QA checklist)
- [ ] GA4 property owned by the client's account; correct time zone/currency; operator added as user
- [ ] GA4 collects on every page via GTM (verified in Tag Assistant + Realtime)
- [ ] Internal Traffic data filter is Active, and visits from excluded IPs do not appear in Realtime
- [ ] External test visit appears, and form-submit + click-to-call register as key events
- [ ] Measurement ID and excluded IPs documented
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Failure modes
- Filter left in **Testing**. Internal visits still count. Flip to Active, then prove it with a cellular visit vs an office IP.
- GA4 in the agency's account. Same hostage problem as a pixel in the agency BM.
- Deployed as a hard-coded snippet instead of a GTM tag. You just created a second tap point.

## Example(s)
- Same July 2026 Hilb incident: no GA4 at all. Weekly reports said "needs more time." There was nothing to read.
- Internal-traffic filter in Testing is the most common GA4 mistake on our own fleet audits.

## Model routing
Computer-use. Run after GTM. Claude-only or Grok-only: same Admin UI.

## Definitive article & links
- Hub: GAP — to be written. "How to Configure GA4 with Internal Traffic Filtering" is queued (High Priority) in Gaps & Tasks to Create; until it ships, /digital-plumbing is the parent hub.
- Related (run order): install-google-tag-manager-container → this → verify-google-search-console-and-connect-to-ga4 → install-meta-pixel-with-standard-events
- Cross-links: /website-qa-audit (Layer 1 GA4 check) · /maa (clean metrics feed the MAA loop) · /dad
