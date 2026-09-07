---
name: implement-technical-schema-markup
description: "Keep the facts on your site clear as your work changes."
category: Personal Branding
stage: —
definitive_article: /knowledge-panel
status: needs-work
---

# Implement technical schema markup

Keep the facts on your site clear as your work changes. This guide checks your existing identity data and adds only what the sources support. Start with the live page and the last checked version of its facts.

**The path:** Existing graph + new proof → Verified fact changes → Source patch → Live graph check

**Start when:** A verified role, profile or source change requires maintenance of the existing identity graph.

## Inputs

- [Add verified Person markup](https://local-service-spotlight.github.io/task-library/?task=implement-person-schema-with-sameas-links#task-implement-person-schema-with-sameas-links) with the stable Person ID, source owner and prior validation receipt.
- The current identity/proof inventory and evidence for changed roles or new identity pages.
- Actual site source access, visible page copy and the supported markup editor.

## Steps

1. Read the complete current graph from the live page and its maintained source. Identify which component emits each node. Record existing Person, Organization, WebPage and other IDs before editing so one task cannot silently overwrite unrelated structured content.
2. Compare the new facts with current visible copy and source evidence. Confirm a role change is current, not an old biography, and distinguish the person’s identity from an employer or business. Use separate nodes and a supported relationship such as worksFor only when it is true.
3. Assess each proposed identity link under [Schema.org’s sameAs definition](https://schema.org/sameAs). A durable speaker profile may qualify when it clearly identifies the same person; a press article or an organization’s GBP is not automatically that person’s identity. Exclude missing, wrong-person or unresolved targets and retain the review reason.
4. Add only supported fields such as current jobTitle, worksFor, alumniOf or knowsAbout. An expertise claim needs real visible evidence; an unearned title in machine-readable form is still a false claim. Update the visible page when an authorized fact correction requires it.
5. Prepare a focused source change that preserves the stable Person ID and other valid nodes. Check JSON syntax, Schema.org properties and any actually applicable Google feature requirements. “Knowledge Panel grade” is not a validator outcome or a published Google certification.
6. After authorized save, inspect the normal public page and its rendered markup. Verify the changed fields, one identity for the person, retained graph nodes and accepted profile links. Save exact source revision and validation results; a stale cached body is not a fresh readback.
7. Record a Google entity ID only when independently observed for the correct person. Panel appearance, claim state and commercial milestones stay in their own records. Set a named review trigger for future fact changes; do not claim that a skill file automatically maintains the graph.

## Definition of done (QA checklist)

Quality assurance (QA) means checking the actual result against its agreed requirements. Follow the [Article Guidelines](https://localservicespotlight.com/article-guidelines/).

- [ ] The focused graph change preserves the existing source owner, stable person identity and unrelated nodes.
- [ ] Every added field or identity link is current and evidence-backed.
- [ ] Live readback and validation are retained; panel and payment states are not inferred.
- [ ] The exact output, source revision, reviewer evidence and remaining owner action are saved.
- [ ] For any reader-facing output, the short grade-five opening states the reader’s useful outcome and supporting method or proof. The body delivers that promise; a useful authentic visual appears in the first screen. Retain exact text and quoted reviewer evidence.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional analyst joins a new firm. The current site names the new firm but markup still names the old one. The developer changes the supported employer link under the existing Person ID and checks the public graph. A recent news story is added as visible proof, not as a second person identity or guaranteed panel trigger.

## Handoff and Content Factory context

[Check the actual claim opportunity](https://local-service-spotlight.github.io/task-library/?task=claim-and-verify-knowledge-panel-when-it-appears#task-claim-and-verify-knowledge-panel-when-it-appears) receives verified identity evidence when applicable; [Review search and real inquiries](https://local-service-spotlight.github.io/task-library/?task=measure-search-impressions-traffic-inbound-opportunities#task-measure-search-impressions-traffic-inbound-opportunities) receives the observed search state.

This task supports the [Content Factory: Produce, Process, Post and Promote](https://blitzmetrics.com/content-factory/). Identity, proof, access or coordination can support several stages. Use the real inputs and receiving owner above; this task does not create unrelated transcripts, clips or ads merely because the diagram has four stages.

## Start with an agent

Give the [AI worker](https://blitzmetrics.com/build-agents/) this recipe, the real inputs, desired result and actions already authorized. Ask for the saved output, sources, checks and next owner. A [skill is a written recipe](https://localservicespotlight.com/plugin/); loading one does not prove account access or perform the task. Use the [installation guide](https://localservicespotlight.com/install/) if reusable setup is needed. A ZIP is a source snapshot, not an access grant or automatic update.

Use the app’s actual supported tools and verified file/account access. Keep a missing human verification step with its real owner. Recurring work needs its own configured job, trigger, timezone and observed result; this guide creates no schedule. Before any media playback, mute the player and set its volume to zero. If silence cannot be verified first, use captions, frames, metadata or another silent check.

## Record the real execution

Open the run record when work begins. Keep one execution ID, starting recipe revision, real inputs and current state. Write the [meta article, the record of this execution](https://blitzmetrics.com/meta-article-prompt/) with actual steps, results, checks, failures and next owner. Writing is required; public release follows existing authority. Link it to this recipe and the [Task Library](https://local-service-spotlight.github.io/task-library/).

Reuse the same execution ID for internal checks, revisions, retries and meta writing. A blocked run stays open with its dependency and owner, without an invented finish time. Dated public examples and distinct verified execution counts remain separate. Propose the smallest source-backed recipe improvement when the actual evidence reveals a defect.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/knowledge-panel/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=implement-technical-schema-markup#task-implement-technical-schema-markup)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Definitive article and task recipe standard](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records fit together](https://localservicespotlight.com/meta-articles/)

### Primary method references

- [Schema.org sameAs](https://schema.org/sameAs)
- [Google structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

## Review and evidence still needed

The inherited contributor status is `needs-work`. It is preserved, not promoted by this rewrite. That label alone does not prove document readiness, account access, an actual execution or a client result.

The fictional example teaches the method and does not fill a real-run evidence gap. A named semantic reviewer must check the actual opening, full method, sources and handoff. Check the useful opening visual in the normal rendered guide at the current required desktop and mobile sizes, including 1280 × 800 and 390 × 844. Source readability checks do not prove public presentation or task execution.
