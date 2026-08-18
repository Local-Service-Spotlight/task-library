---
name: classify-and-offer-knowledge-panel
description: Classify each personal-brand client as Claim, Build, or Decline-or-contested-quote from a logged-out name search, then offer the matching price band without waiting on a human gate.
category: Personal Branding
stage: —
definitive_article: /knowledge-panel
status: needs-work
---

# Classify and offer Knowledge Panel

**Use this when** a personal-brand client has a live entity home (or we are about to build one) and we need to decide whether to sell Claim, Standard Build, or a contested quote — Phase 4 intake. Dylan is not the gate.

## Inputs
- Exact canonical name string and entity-home URL
- Ability to search Google logged out / incognito (no personalization)
- Current SKUs: Claim/correct $2,500; Standard Build $7,500; contested quoted after audit
- Qualification bar on the live package page (revenue, reviews, personal brand, podcast access)

## Steps
1. Search the exact canonical name logged out and in incognito. Capture the SERP (right rail on desktop, top card on mobile). Note other people or companies sharing the name.
2. Classify the fork:
   - **Claim** if a Knowledge Panel already shows, or a KGMID / `/m/` / `/g/` entity exists for this person.
   - **Build** if there is no panel and no usable entity, the name is distinct enough, and notability can be earned.
   - **Decline or contested-quote** if the SERP is crowded with the same name, the wrong person dominates, or independent notability is too thin. Sean Kelly (Digital Social Hour) is this class: never a generic Wikidata item, never an easy $7,500 Claim.
3. Do not promise a 15-day panel. Stage 1 is entity existence (KGMID or a thin card). Stage 2 is the full panel, then claim. Typical Build is 6–12 months; competitive names 12–18 months; under 60 days is rare.
4. Offer the matching band only: Claim/correct $2,500; Standard Build $7,500; contested quoted after audit. Payment is 50% at intake and 50% when Stage 1 is evidenced (or when the Claim is verified / corrections are live).
5. State in the offer: nobody can pay Google; the client’s Google account owns the claim; we may be second manager and they can revoke us; Standard and Contested Build keep the 18-month refund if Stage 2 is not live.
6. Log date, SERP evidence, fork, band, and the offer sent. Do not blast one SKU across the roster. First queue is people we already operate.

## Definition of done (QA checklist)
- [ ] Logged-out search of the exact canonical name is dated and stored
- [ ] Fork is Claim, Build, or Decline-or-contested-quote with evidence, not a vibe
- [ ] Offer matches the band; 50/50 and claim-ownership language included
- [ ] Crowded names were not sold as easy Claim; no generic Wikidata created
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Reza Deghati — panel / `/m/` already exists → **Claim/correct**, not a from-scratch Build.
- Sean Kelly, host of Digital Social Hour — crowded SERP → **Decline-or-contested-quote**; entity home seankelly.io; never a generic Wikidata “Sean Kelly.”
- Standard Build — distinct local-service owner with a personal-brand site (or we build one) and no panel yet → **$7,500**, 50/50 at Stage 1.

## Run on a persistent agent (Fable 5)
A persistent agent (Claude Fable 5 or a comparable OpenAI/Google model) runs the logged-out name search for each personal-brand client on the roster, classifies the fork, and drafts the matching offer — looping until the Definition-of-done fully passes, not 90%.
It does not wait on Dylan. It does not invent competitor-scale panel counts or a secret method name. It self-verifies the SERP against the canonical name held in memory and refuses generic Wikidata for common names.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /knowledge-panel
- Related: /personal-brand · next: establish-entity-identity · then: build-third-party-validation · implement-technical-schema-markup · claim-and-verify-knowledge-panel-when-it-appears
- Sean overlay: sean-kelly-growth `docs/KNOWLEDGE-PANEL-SOP.md`
- Live SKU page: https://localservicespotlight.com/knowledge-panel-package/
