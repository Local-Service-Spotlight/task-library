---
name: step-2-fix-categories-and-tags-in-wordpress
description: "Help readers browse your posts in groups that make sense."
category: SEO & Content Architecture
stage: —
definitive_article: /internal-linking
status: complete
---

# Step 2: Fix categories and tags in WordPress

Put your posts in clear groups so readers can find what they need. This guide helps you fix those groups while keeping useful labels and links. Use the checked [page list](https://local-service-spotlight.github.io/task-library/?task=step-1-inventory-content-and-establish-gct-per-page#task-step-1-inventory-content-and-establish-gct-per-page) to decide what belongs together before you plan new links.

**The path:** Read the page list → Plan group changes → Save agreed labels → Check pages and hand off

WordPress calls its grouping systems **taxonomies**. Categories are broad groups; tags are more specific labels. A **term** is one saved category or tag. The [internal-linking guide](https://blitzmetrics.com/internal-linking/) shows how these groups help prepare the later link plan; a group label does not create a link inside a post.

**Start when:** Step 1 is accepted and the WordPress site’s categories or tags need a scoped cleanup.

## Inputs

- [Inventory pages and their purpose](https://local-service-spotlight.github.io/task-library/?task=step-1-inventory-content-and-establish-gct-per-page#task-step-1-inventory-content-and-establish-gct-per-page) with actual post/page types, page roles, current term IDs and source owner.
- The live WordPress category/tag definitions, archive routes, theme/plugin dependencies and any taxonomy-enabled custom types.
- The approved term mapping and edit scope, a dated export of affected items and all their current term IDs, current site permalink rules, and a way to restore approved changes if checks fail.
- Verified editor or API access for the intended site and content type. An API is the app’s way to read or change site data. A read-only account can prepare the plan but cannot complete a write; keep that result partial.

## Steps

1. Read the current terms and supported content types from the actual WordPress source. Record term ID, name, slug, parent, count and archive URL. Include every page of the term listing and note any access gaps; the first API response is not necessarily the full list. Default WordPress Posts support categories and tags; Pages need explicit registered support, so do not assume every page accepts the same fields.
2. Compare categories with real topic groups and reader navigation. A category can support a branch but is not automatically the canonical hub itself. Preserve valid site-specific roles and distinguish task-definitive pages from topic, comparison and historical content instead of assigning every important page the same label.
3. Prepare an old-to-new mapping with the exact affected content items. For each row record the source item ID/type, current full category/tag sets, approved additions/removals, intended full final sets, reason, source date/revision and release owner. Reuse stable valid terms and IDs where possible. Use tags for useful cross-cutting attributes such as an actual stage or topic; do not invent a Content Factory stage for support work that spans several stages.
4. Review empty, one-off and similar terms for purpose and dependencies before proposing removal. Low count alone does not prove a term is useless. Check archive use, menus, inbound links, permalink settings and integrations; do not delete a term or change its slug until its dependencies, intended routing and recovery plan are reviewed and included in the authorized scope. Removing a term from one post is different from deleting the shared term. An unresolved dependency stays held; preserve the existing term and route.
5. Re-read each affected item immediately before saving. If its term sets or relevant source fields changed since the plan, stop that row and reconcile the new values; do not overwrite another editor’s work. Apply only accepted changes through the supported editor or API. For the standard Posts API, `POST /wp/v2/posts/<id>` accepts complete term-ID arrays in `categories` and `tags`. A supplied array replaces that taxonomy’s current set; it does not just add the listed IDs. Build the final set from the fresh existing IDs plus approved additions minus approved removals. Omit any taxonomy field you are not changing, and never send an empty list unless clearing that set is approved. Keep unrelated content fields out of the update. Save the exact sent values and response. A pre-save read reduces conflicts but is not an atomic lock; readback is still required.
6. Inspect the affected archive pages and representative content after the change. Check that visible labels, links, pagination and relevant grouping work, that useful hubs still lead correctly, and that unrelated categories or media were not overwritten by a partial update.
7. Read back every changed item and compare its complete saved term sets with the intended sets, including retained unrelated IDs. Test the actual downstream retrieval request: standard Posts filters use `categories=<term-ID>` or `tags=<term-ID>`, not a guessed category-slug parameter. Record the full pagination and visibility scope when comparing counts; draft or private items may not appear publicly. Check each changed archive route and any approved redirect, plus the declared representative content and pagination checks. A failed save, mismatch or unchecked route keeps that row partial or held. Preserve its evidence and next owner/action; use the reviewed recovery plan only if authorized and after checking for newer edits. Pass accepted rows and clearly separated exceptions to the link planner.

## Definition of done (QA checklist)

Quality assurance (QA) means checking the actual result against its agreed requirements. Follow the [Article Guidelines](https://localservicespotlight.com/article-guidelines/).

- [ ] The mapping matches real page roles and supported content types while retaining valid term IDs and dependencies.
- [ ] Every changed item’s complete saved term sets match the intended sets. Unrelated IDs and omitted fields remain intact; each mismatch is a named open item.
- [ ] Only authorized term/assignment changes are saved. Each changed route and required retrieval query works within the recorded coverage; unchecked cases stay unknown.
- [ ] The record lists accepted, no-change and unresolved rows separately. No unresolved required check is called complete, and recovery values plus the next owner/action are saved.
- [ ] Categories are not substituted for hub content or contextual links; unrelated taxonomy is preserved.
- [ ] The exact output, source revision, reviewer evidence and remaining owner action are saved.
- [ ] For any reader-facing output, the short grade-five opening states the reader’s useful outcome and supporting method or proof. The body delivers that promise; a useful authentic visual appears in the first screen. Retain exact text and quoted reviewer evidence.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional firm has a “Roof Repair” category and a separate roof-repair service page. Keep both: the archive groups stories, while the service page explains an offer. In this made-up example, one Post has categories `[7, 12]` and tags `[5]`. The plan adds category `34`. Its intended categories become `[7, 12, 34]`, and the update omits `tags` so `[5]` stays. Sending only `[34]` would lose categories `7` and `12`. These IDs are fictional; resolve the real site’s IDs before acting.

If a fresh read shows `[7, 12, 28]`, do not send the older plan. Reconcile the new category first. After a valid save, check the complete returned sets, the archive route and the real category filter. An ordinary Page without registered category support stays unchanged. This example is a reasoning check, not a live API test or accepted site result.

## Handoff and Content Factory context

[Plan relevant links and orphan repairs](https://local-service-spotlight.github.io/task-library/?task=step-3-identify-money-pages-and-orphan-pages#task-step-3-identify-money-pages-and-orphan-pages) receives the dated inventory with actual incoming-path counts, the counted scope and extraction date/method, accepted before/after term-ID mapping, saved-source readbacks, tested archive URLs, retrieval query and coverage. It uses the actual page roles and groups to plan useful links. The site/source owner receives any term-removal or routing dependency that remains outside the approved edit.

This task supports the [Content Factory: Produce, Process, Post and Promote](https://blitzmetrics.com/content-factory/). The page inventory supplies the inputs. Reviewing the grouping plan supports Process; saving and checking approved assignments supports Post. The checked mapping then goes to link planning. This support task may span stages; it does not create clips or ads.

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
- [WordPress REST term-update implementation](https://developer.wordpress.org/reference/classes/wp_rest_posts_controller/handle_terms/) and [term replacement behavior](https://developer.wordpress.org/reference/functions/wp_set_object_terms/) — primary evidence for preserving the full intended set. Site-specific extensions still need their own check.

## Review and evidence still needed

The inherited contributor status is `complete`. It is preserved, not promoted by this rewrite. That label alone does not prove document readiness, account access, an actual execution or a client result.

The fictional example teaches the method and does not fill a real-run evidence gap. A named semantic reviewer must check the actual opening, full method, sources and handoff. Check the useful opening visual in the normal rendered guide at the current required desktop and mobile sizes, including 1280 × 800 and 390 × 844. Source readability checks do not prove public presentation or task execution.
