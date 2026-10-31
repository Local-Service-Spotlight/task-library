---
name: run-network-wikidata-kp-audit
description: "Keep a shared roster of people scored for Wikidata, Knowledge Panel, and Person schema — reviewed weekly."
category: Personal Branding
stage: —
definitive_article: /knowledge-panel
status: needs-work
---

# Run a Network Wikidata & Knowledge Panel audit

Keep one shared sheet for everyone in a network you care about. Each week, check Wikidata, Knowledge Graph / Knowledge Panel, Person schema, and canonical articles — fix what you control, queue what needs the person, and log the change.

**The path:** Shared roster → Tiered weekly pass → Proactive fixes we control → Claims with the person → Weekly Log

**Start when:** You have a Network Audit spreadsheet (or are ready to create one from the Playbook pattern) and an assigned Tracker / Ops owner.

## Inputs

- Canonical Network Audit sheet with tabs: Network Audit, Playbook & Owners, Weekly Log.
  - Worked example: [Network Audit — Wikidata & Knowledge Panel Tracker](https://docs.google.com/spreadsheets/d/15O3sN3KC_sqM7_oB8Gz7Q4w3w1ED4TNZNvtJJ34L0Ks/edit)
- Skill: [network-wikidata-kp-audit](https://github.com/dennisyu/local-service-spotlight-skills) (folder `skills/network-wikidata-kp-audit/`)
- Related tasks: [Implement Person schema with sameAs links](https://local-service-spotlight.github.io/task-library/?task=implement-person-schema-with-sameas-links#task-implement-person-schema-with-sameas-links), [Claim and verify Knowledge Panel when it appears](https://local-service-spotlight.github.io/task-library/?task=claim-and-verify-knowledge-panel-when-it-appears#task-claim-and-verify-knowledge-panel-when-it-appears), [Classify and offer Knowledge Panel](https://local-service-spotlight.github.io/task-library/?task=classify-and-offer-knowledge-panel#task-classify-and-offer-knowledge-panel)
- Fleet setup note (worked example): `agent-notes/2026-10-25-happy-network-wikidata-audit-sheet.md` on Local-Service-Spotlight/agent-runtime

## Steps

1. Read the Playbook & Owners tab. Confirm who owns Claims, Client ops, Content, Tracker/Ops, and personal-brand schema. Do not invent owners.
2. Open Network Audit. Sort by Tier, then Status. Cap a weekly batch (finish one batch before another). Tier 1 Unverified first.
3. For each person in the batch: fill or refresh QID, Wikipedia/Grokipedia, KGMID + confidence, panel live/claimed, Person schema, sameAs, Top Gap, Last/Next Check. Label Unverified when a two-key check is incomplete.
4. Proactive lane (no person required): Person schema + sameAs on sites you control; canonical articles; verified mention gathering; sourced Wikidata proposals only. Never invent facts.
5. Claims lane: queue Waiting on person for the Claims owner. Do not fake a claim or submit without the person.
6. Append Weekly Log lines with date, who/system, what changed, evidence URL or cell, and next step.
7. Surface to the network owner only: a verified win, a blocker that needs the person, or a decision only they can make. No process chatter.
8. Save an agent-note after a substantive pass. Keep Happy/Ops Monday sheet sweep ownership separate from the personal-brand schema lane.

## Definition of done (QA checklist)

Quality assurance (QA) means checking the actual result against its agreed requirements. Follow the [Article Guidelines](https://localservicespotlight.com/article-guidelines/).

- [ ] Every person touched this week has OBSERVED sheet fields or an explicit Unverified label with the missing check named.
- [ ] Two-key rule held for any Missing/Failed claim (two independent checks, one at the canonical destination).
- [ ] No invented QID, KGMID, notability, or claim outcome.
- [ ] Weekly Log has one verified line per meaningful change.
- [ ] Schema/canonical drafts on controlled sites are staged with owner yes before live inject when required.
- [ ] For any reader-facing output, the short grade-five opening states the reader’s useful outcome; a useful authentic visual appears in the first screen.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional advisor network has 40 people on a Network Audit sheet. Monday, Ops sorts Tier 1 and finds three Unverified KIDs. The personal-brand desk live-checks two sites they control: one missing Person schema gets a staged JSON-LD draft; one already has schema and only needs a Weekly Log “no change” note. A third person is claim-ready and moves to Waiting on person for the Claims owner. Nothing is invented on Wikidata.

## Handoff and Content Factory context

[Implement Person schema with sameAs links](https://local-service-spotlight.github.io/task-library/?task=implement-person-schema-with-sameas-links#task-implement-person-schema-with-sameas-links) receives schema gaps on controlled sites. [Claim and verify Knowledge Panel when it appears](https://local-service-spotlight.github.io/task-library/?task=claim-and-verify-knowledge-panel-when-it-appears#task-claim-and-verify-knowledge-panel-when-it-appears) receives claim-ready people. Tracker/Ops keeps the sheet current.

This task supports the [Content Factory: Produce, Process, Post and Promote](https://localservicespotlight.com/content-factory/) as a **support / measurement** task for entity health across a roster. It does not create unrelated transcripts, clips, or ads merely because the diagram has four stages.

## Start with an agent

Give the [AI worker](https://blitzmetrics.com/build-agents/) this recipe, the sheet URL, authorized edit access, the skill `network-wikidata-kp-audit`, and which lane they own (Tracker sweep vs personal-brand schema). Ask for updated rows, Weekly Log lines, staged drafts, and next owner. Recurring work needs its own configured job, trigger, timezone, and observed result; this guide creates no schedule by itself.

## Record the real execution

Open the run record when work begins. Keep one execution ID, starting recipe revision, real inputs and current state. Write the [meta article, the record of this execution](https://blitzmetrics.com/meta-article-prompt/) with actual steps, results, checks, failures and next owner. Writing is required; public release follows existing authority. Link it to this recipe and the [Task Library](https://local-service-spotlight.github.io/task-library/).

## Definitive article & links

- [Maintained source guide (Knowledge Panel)](https://blitzmetrics.com/knowledge-panel/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=run-network-wikidata-kp-audit#task-run-network-wikidata-kp-audit)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Definitive article and task recipe standard](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records fit together](https://localservicespotlight.com/meta-articles/)

### Primary method references

- Skill `network-wikidata-kp-audit` in dennisyu/local-service-spotlight-skills
- Skill `knowledge-panel-entity-seo`
- [Schema.org sameAs](https://schema.org/sameAs)

## Review and evidence still needed

The contributor status is `needs-work`. It is preserved until a named semantic reviewer checks the opening, full method, sources, and handoff, and a real authorized run fills the execution ledger. The fictional example teaches the method and does not fill a real-run evidence gap.
