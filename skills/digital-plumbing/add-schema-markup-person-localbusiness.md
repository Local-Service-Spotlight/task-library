---
name: add-schema-markup-person-localbusiness
description: "Help search tools read the facts on your site. Add the right person or business record and check it."
category: Digital Plumbing
stage: —
definitive_article: /digital-plumbing
status: needs-work
---

# Add Schema Markup (Person/LocalBusiness)

Search tools can mix up a person and a business. This guide helps a site owner add a small fact record to the page. Start with facts and profile links that you can prove.

**The path:** Proven facts → Right entity → Page record → Validation.

**Use this when:** a site lacks structured facts, has conflicting entity records, or changes its public business information.

## Inputs
- The canonical public name, page URL, entity type and verified same-entity profile links. Keep private addresses and personal contact details out unless approved for publication.
- The existing structured-data output and its owner: SEO plugin, theme or code. Access only to the source needed for this change.
- Public page content that supports each proposed fact and the search feature, if any, that you intend to support.

## First-run prompt

> Read the existing page and structured records. Add or correct the actual person or business entity using supported facts and the current owning source. Keep distinct entities separate. Validate syntax and any applicable Google feature without promising a Knowledge Panel or rich result.

## Steps
1. Read the visible page and all existing JSON-LD, microdata or plugin output. List existing entity IDs so a new record will not create a second conflicting business.
2. Choose the right entity: Person for an individual, an appropriate LocalBusiness type for an eligible local business, or Organization when that better fits. A founder and their company are separate records, connected only by a true stated relationship.
3. Build a fact table with value, public source and entity. Define `sameAs` as a link that identifies this same person or business. A news mention or a person’s employer page is not automatically the same entity.
4. Edit the current owning plugin or code field. Use a stable URL-based identifier and absolute public URLs. Include only supported properties; an invented job title, street address or rating is not a way to satisfy a validator.
5. For a relevant Google feature, read that feature’s current required and recommended fields. Generic Person markup is not itself a promise of a supported rich-result feature. Keep non-applicable recommendations separate from real errors.
6. Save the change through the supported publishing route. Read the ordinary public page and compare the served record with the intended values, including correct characters and valid JSON.
7. Validate syntax and entity relationships, then use Google’s Rich Results Test only for applicable features. Inspect warnings individually and fix factual or syntax defects at the source. “No supported item detected” is not proof that generic schema is invalid.
8. Check representative templates for duplicate or stale records and visible facts that disagree. Save the final entity IDs, public URLs, validator results and remaining search-feature limits.

## Definition of done (QA checklist)

- [ ] Each record represents the correct entity and agrees with visible, supported facts.
- [ ] Same-entity profile links are separated from relationship and reference links.
- [ ] JSON parses and no conflicting duplicate entity has been added.
- [ ] Applicable validation errors are resolved; non-applicable feature results are labeled accurately.
- [ ] Public read-back and the owning source are recorded; no ranking or Knowledge Panel outcome is claimed.

## Example(s)

**Fictional teaching example.** A workshop site describes an owner named Lee Hart and the company Oak Repair. A minimal business record is `{"@context":"https://schema.org","@type":"LocalBusiness","@id":"https://example.com/#business","name":"Oak Repair","url":"https://example.com/"}`. A separate Person record holds Lee’s facts. The company’s LinkedIn Page belongs with the business; Lee’s personal profile belongs with the Person. This teaches record identity and valid JSON. It is deliberately not a complete Google LocalBusiness feature example, and it proves no actual search display.

## Handoff and Content Factory context

Give the maintained entity record to the content and site owners. Use [ensure nap consistency across platforms](https://local-service-spotlight.github.io/task-library/?task=ensure-nap-consistency-across-platforms#task-ensure-nap-consistency-across-platforms) if public business facts conflict; use the owned entity-linking method for article links.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Set up once, then review when names, locations, profiles or the schema-owning plugin change. Use an actual maintenance trigger if recurring checks are wanted.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/digital-plumbing
- Exact task: [Add Schema Markup (Person/LocalBusiness)](https://local-service-spotlight.github.io/task-library/?task=add-schema-markup-person-localbusiness#task-add-schema-markup-person-localbusiness)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [Entity linking](https://blitzmetrics.com/entity-linking/)
- [Schema.org sameAs](https://schema.org/sameAs)
- [Google structured-data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The project must supply verified facts and the actual schema source. A dedicated task article is not established by the broad hub link.
