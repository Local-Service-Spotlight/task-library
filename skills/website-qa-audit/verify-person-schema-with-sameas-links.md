---
name: verify-person-schema-with-sameas-links
description: "Check the site data about a real person. Link it to the same person’s trusted public pages."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: needs-work
---

# Verify Person schema with sameAs links

Your personal site should describe the right person to search tools. This guide helps you check that data and its profile links. Start with the real page, the person’s known facts and trusted public sources.

**The path:** Visible person → Correct data node → Same-identity links → Source and tool checks.

**Use this when:** A personal site or another page genuinely about a person needs its Person structured data checked.

## Inputs
- The exact page set that emits or should emit Person data, plus the visible person’s source-backed facts.
- Verified public identity URLs and the supported schema source, including existing plugin/custom graph relationships.
- A general schema validator and a Google-supported feature test only where that feature applies.
- Read/edit scope and a record of current nodes, IDs and unresolved identity evidence.

## First-run prompt

> Inspect the supplied pages, person facts and identity map. Verify the appropriate Person node, sameAs targets and graph relationships, correct authorized supported-source faults, and report syntax, facts, access limits and Google feature eligibility separately.

## Steps
1. Confirm Person is the correct subject. A local-business home page may primarily describe an Organization or LocalBusiness. Do not rename a business to match its owner or force Person markup onto every site.
2. Inspect the normal served structured data and identify the actual Person node, stable @id and relevant links from other nodes. Record duplicate/conflicting identities rather than deleting all but one without understanding the graph.
3. Compare the name, URL and any additional facts with the visible page and approved source record. Job title, image and other properties are not universally mandatory simply because an old checklist lists them; do not invent values to remove a generic warning.
4. Review sameAs references as identity claims. Use canonical public pages that identify the same person unambiguously, not the company’s profile, an unrelated article or an unverified similar name.
5. Open or otherwise verify each applicable profile with permitted read access. A restricted profile is a precise access/identity gap, not automatic proof it is dead. Confirm actual source identity rather than matching a face by appearance.
6. Validate the graph’s syntax and vocabulary. Use Google’s test for supported rich-result features when relevant, but do not require generic Person markup to appear as a standalone rich result. No detected Google feature is not the same as malformed schema.
7. Apply authorized corrections through the supported owner of that graph. Preserve real @id relationships and visible factual consistency; do not add a second plugin simply to create another Person block.
8. Recheck the actual canonical served data, relevant profiles and validator results. Save separate syntax, facts, identity and feature-eligibility findings. A clean graph does not guarantee a Knowledge Panel or search ranking.

## Definition of done (QA checklist)

- [ ] Person is the correct entity for the declared page role and has source-backed visible facts.
- [ ] sameAs URLs identify the same person without company/profile conflation.
- [ ] Existing graph relationships and supported implementation source are preserved.
- [ ] Generic schema validity and Google feature eligibility remain separate results.
- [ ] Canonical readback and exact unresolved identity evidence support the outcome.

## Example(s)

**Fictional teaching example — no markup was deployed.** Alex’s personal about page has a Person node linked to Alex’s verified personal home and public profile. Maple Cycle’s business listing belongs to a separate business node.

The sample Person node omits jobTitle because the source record does not establish a current title. The reviewer does not invent “CEO” to complete a field. Syntax can pass while a restricted profile remains unverified and Google reports no supported rich-result feature. Those are three separate findings.

## Handoff and Content Factory context

The technical/content owner receives the served graph and remaining identity proof. [Review all applicable profile links](https://local-service-spotlight.github.io/task-library/?task=check-schema-connects-to-all-verified-profiles#task-check-schema-connects-to-all-verified-profiles) handles the broader person-and-business map without combining their identities.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at identity setup and after relevant source, profile or schema changes. No profile creation or automatic lifetime monitoring is implied.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify Person schema with sameAs links](https://local-service-spotlight.github.io/task-library/?task=verify-person-schema-with-sameas-links#task-verify-person-schema-with-sameas-links)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Schema.org sameAs](https://schema.org/sameAs)
- [Google structured-data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The actual graph, approved identity facts, accessible profiles and served validation evidence require the site.
