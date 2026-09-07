---
name: step-2-fix-categories-and-tags-in-wordpress
description: "Help readers browse your posts in groups that make sense."
category: SEO & Content Architecture
stage: —
definitive_article: /internal-linking
status: complete
---

# Step 2: Fix categories and tags in WordPress

Help readers browse your posts in groups that make sense. This guide fixes mixed-up page groups and labels without breaking the site. Start with your page list and the groups the site already uses.

**The path:** Page roles + current terms → Term mapping → Approved assignments → Archive and API checks

**Start when:** Step 1 is accepted and the WordPress site’s categories or tags need a scoped cleanup.

## Inputs

- [Inventory pages and their purpose](https://local-service-spotlight.github.io/task-library/?task=step-1-inventory-content-and-establish-gct-per-page#task-step-1-inventory-content-and-establish-gct-per-page) with actual post/page types, page roles, current term IDs and source owner.
- The live WordPress category/tag definitions, archive routes, theme/plugin dependencies and any taxonomy-enabled custom types.
- The approved term mapping and edit scope, preserved source copy and current site permalink rules.

## Steps

1. Read the current terms and supported content types from the actual WordPress source. Record term ID, name, slug, parent, count and archive URL. Default WordPress Posts support categories and tags; Pages need explicit registered support, so do not assume every page accepts the same fields.
2. Compare categories with real topic groups and reader navigation. A category can support a branch but is not automatically the canonical hub itself. Preserve valid site-specific roles and distinguish task-definitive pages from topic, comparison and historical content instead of assigning every important page the same label.
3. Prepare an old-to-new mapping with the exact affected content items. Reuse stable valid terms and IDs where possible. Use tags for useful cross-cutting attributes such as an actual stage or topic; do not invent a Content Factory stage for support work that spans several stages.
4. Review empty, one-off and similar terms for purpose and dependencies before proposing removal. Low count alone does not prove a term is useless. Check archive use, menus, inbound links, permalink settings and integrations; term deletion or slug changes may require a separately reviewed routing plan.
5. Apply accepted assignments through the supported editor or REST API when authorized. For the standard Posts API, categories and tags use term-ID arrays, and list filters use the documented plural parameters. Resolve real IDs; a guessed category-slug query is not evidence that an agent can retrieve the desired group.
6. Inspect the affected archive pages and representative content after the change. Check that visible labels, links, pagination and relevant grouping work, that useful hubs still lead correctly, and that unrelated categories or media were not overwritten by a partial update.
7. Read back the saved term assignments and test the actual retrieval request used downstream. Compare affected counts and routes with the approved mapping, accounting for unpublished content as appropriate. Save exact before/after records and unresolved dependencies; pass the accepted taxonomy to the link planner without claiming taxonomy alone creates incoming body links.

## Definition of done (QA checklist)

Quality assurance (QA) means checking the actual result against its agreed requirements. Follow the [Article Guidelines](https://localservicespotlight.com/article-guidelines/).

- [ ] The mapping matches real page roles and supported content types while retaining valid term IDs and dependencies.
- [ ] Only authorized term/assignment changes are saved, and the actual archives and retrieval query work.
- [ ] Categories are not substituted for hub content or contextual links; unrelated taxonomy is preserved.
- [ ] The exact output, source revision, reviewer evidence and remaining owner action are saved.
- [ ] For any reader-facing output, the short grade-five opening states the reader’s useful outcome and supporting method or proof. The body delivers that promise; a useful authentic visual appears in the first screen. Retain exact text and quoted reviewer evidence.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional firm has a “Roof Repair” category and a separate roof-repair service page. The team keeps both because the archive groups stories and the service page explains the offer. It assigns three Posts to the real category ID, leaves an ordinary Page’s unsupported fields alone, and checks the archive and documented API filter.

## Handoff and Content Factory context

[Plan relevant links and orphan repairs](https://local-service-spotlight.github.io/task-library/?task=step-3-identify-money-pages-and-orphan-pages#task-step-3-identify-money-pages-and-orphan-pages) receives the accepted assignments and exact term-ID mapping. The site/source owner receives any term-removal or routing dependency that remains outside the approved edit.

This task supports the [Content Factory: Produce, Process, Post and Promote](https://blitzmetrics.com/content-factory/). Identity, proof, access or coordination can support several stages. Use the real inputs and receiving owner above; this task does not create unrelated transcripts, clips or ads merely because the diagram has four stages.

## Start with an agent

Give the [AI worker](https://blitzmetrics.com/build-agents/) this recipe, the real inputs, desired result and actions already authorized. Ask for the saved output, sources, checks and next owner. A [skill is a written recipe](https://localservicespotlight.com/plugin/); loading one does not prove account access or perform the task. Use the [installation guide](https://localservicespotlight.com/install/) if reusable setup is needed. A ZIP is a source snapshot, not an access grant or automatic update.

Use the app’s actual supported tools and verified file/account access. Keep a missing human verification step with its real owner. Recurring work needs its own configured job, trigger, timezone and observed result; this guide creates no schedule. Before any media playback, mute the player and set its volume to zero. If silence cannot be verified first, use captions, frames, metadata or another silent check.

## Record the real execution

Open the run record when work begins. Keep one execution ID, starting recipe revision, real inputs and current state. Write the [meta article, the record of this execution](https://blitzmetrics.com/meta-article-prompt/) with actual steps, results, checks, failures and next owner. Writing is required; public release follows existing authority. Link it to this recipe and the [Task Library](https://local-service-spotlight.github.io/task-library/).

Reuse the same execution ID for internal checks, revisions, retries and meta writing. A blocked run stays open with its dependency and owner, without an invented finish time. Dated public examples and distinct verified execution counts remain separate. Propose the smallest source-backed recipe improvement when the actual evidence reveals a defect.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/internal-linking/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=step-2-fix-categories-and-tags-in-wordpress#task-step-2-fix-categories-and-tags-in-wordpress)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Definitive article and task recipe standard](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records fit together](https://localservicespotlight.com/meta-articles/)

### Primary method references

- [WordPress Posts REST reference](https://developer.wordpress.org/rest-api/reference/posts/)
- [WordPress Categories REST reference](https://developer.wordpress.org/rest-api/reference/categories/)

## Review and evidence still needed

The inherited contributor status is `complete`. It is preserved, not promoted by this rewrite. That label alone does not prove document readiness, account access, an actual execution or a client result.

The fictional example teaches the method and does not fill a real-run evidence gap. A named semantic reviewer must check the actual opening, full method, sources and handoff. Check the useful opening visual in the normal rendered guide at the current required desktop and mobile sizes, including 1280 × 800 and 390 × 844. Source readability checks do not prove public presentation or task execution.
