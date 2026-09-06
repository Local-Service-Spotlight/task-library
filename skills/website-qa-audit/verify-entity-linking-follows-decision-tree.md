---
name: verify-entity-linking-follows-decision-tree
description: "Send readers to the right source for each name or idea. Keep each topic tied to its main guide."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify entity linking follows decision tree

A useful link should take readers where they expect to go. This guide helps you check links for people, firms and ideas. Start with the site’s trusted topic map, then read the target page.

**The path:** Mention and purpose → Verified owner → Exact target → Public recheck.

**Use this when:** A page set needs its first-mention links checked against the maintained entity decision tree.

## Inputs
- The full scoped body-link inventory with page, anchor text, destination and surrounding sentence.
- The maintained [entity-linking guide](https://blitzmetrics.com/entity-linking/) and verified person/network-company destinations.
- The [SEO Tree](https://blitzmetrics.com/seo-tree/) map of maintained owned explainers and current canonical URLs.
- Supported edit scope and a tracker for missing owned guides or unresolved identities.

## First-run prompt

> Use the supplied page set, current entity decision tree and owned topic map. Classify each link’s purpose, preserve exact primary-proof/action links, and fix authorized first-mention routes. Verify canonical targets and return precise missing-guide or identity gaps.

## Steps
1. Read each linked mention in context. Identify whether it names a person, a network organization, an outside tool/entity, a concept, or a specific proof/action destination. A string alone does not reveal the link’s purpose.
2. For a person, use the verified personal entity home. For an organization in our network, use its verified entity home. Do not invent a domain from a name or treat a similar search result as identity proof.
3. For a BlitzMetrics concept, choose its one maintained canonical guide. For an outside tool, concept or well-known entity used as an explanation, link the first meaningful mention to our maintained guide when it exists. If it does not, leave plain text and record the real guide gap.
4. Keep direct external links when the exact destination supplies primary evidence or a needed sign-in, installation or download action. Label that purpose clearly. Replacing a necessary download with a generic owned article can break the task just as indiscriminate outbound explanations weaken the tree.
5. Read the selected target and resolve its canonical URL and any #anchor. Confirm it teaches the same topic or establishes the named identity. Do not route to a competing duplicate, unrelated support story or empty task search.
6. Use the actual entity name or a short descriptive phrase as the anchor. Link the first meaningful body mention rather than every occurrence. Three to six words is a useful house preference, not a reason to distort a person’s two-word name.
7. Apply the authorized exact-source changes. Preserve necessary proof and action links, and give missing owned destinations a named owner rather than creating an unreviewed rival hub.
8. Recheck changed links on the normal canonical pages and save the internal routing table with scope, purposes, targets, exceptions and remaining gaps. Do not claim rankings or full-site routing coverage from a sample.

## Definition of done (QA checklist)

- [ ] People, network organizations and owned concepts use their verified canonical destinations.
- [ ] Outside explanatory mentions use the maintained owned guide or a recorded gap.
- [ ] Precise external proof and execution links retain their actual purpose.
- [ ] First-mention anchors are descriptive and resolve correctly, including fragments.
- [ ] Scope, unresolved identity and missing guide work are recorded without inventing routes.

## Example(s)

**Fictional teaching example — no link was changed.** Maple Cycle’s article explains how a video becomes a guide. The first explanatory mention of an editing tool points to the maintained owned training when one exists. A later “Download the editor” step may still need the provider’s real download page.

The founder’s name links to the verified personal home, while the business name links to Maple Cycle’s verified company home. An unmapped concept remains plain text with an internal guide request; it does not get an invented `/best-guide/` target.

## Handoff and Content Factory context

The content owner receives the accepted routing table. [Follow the canonical entity decision tree](https://local-service-spotlight.github.io/task-library/?task=follow-entity-linking-decision-tree#task-follow-entity-linking-decision-tree) owns the policy; [Check broken targets](https://local-service-spotlight.github.io/task-library/?task=check-for-broken-links#task-check-for-broken-links) verifies destination failures separately.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before publication and when named entities, guide owners or URLs change. A reused mapping must be checked against the current source rather than assumed remembered by a model.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify entity linking follows decision tree](https://local-service-spotlight.github.io/task-library/?task=verify-entity-linking-follows-decision-tree#task-verify-entity-linking-follows-decision-tree)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Current owned entity decision tree](https://blitzmetrics.com/entity-linking/)
- [SEO Tree](https://blitzmetrics.com/seo-tree/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The actual verified entity map and any missing maintained owned guide remain project-specific.
