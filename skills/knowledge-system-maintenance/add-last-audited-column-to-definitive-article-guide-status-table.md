---
name: add-last-audited-column-to-definitive-article-guide-status-table
description: An old green label can hide missed checks.
category: Knowledge System Maintenance
stage: —
definitive_article: /knowledge-system-maintenance
status: gap
---

# Add Last Audited column to Definitive Article Guide status table

An old green label can hide missed checks. This guide makes the last real check easy to see. Start with the live audit list and keep any proof it already has.

**The path:** Current audit list → Preserve proof → Add date field → Check rows

**Start when:** The current audit register lacks a usable last-check field or its audit history needs reconciliation.

## Inputs

- [current article guide](https://blitzmetrics.com/definitive-article-guide/) and the current audit register it points to. The guide’s old teaching table is historical, not the live status authority.
- The current page inventory, prior audit receipts, and editor access to the maintained register.

## Steps

1. Identify the source that owns current audit status. Read the live guide and record that destination and revision. Do not turn the historical example table back into a live database.
2. Inspect whether an equivalent audit-date field already exists. Reuse it rather than adding a duplicate. If missing, propose “Last audited” alongside result, reviewer, evidence link and source revision.
3. Reconcile inventory URLs to rows, normalizing only known canonical redirects. Preserve existing verified dates and evidence; record conflicts for review.
4. For a row with no audit evidence, use “Unknown — no verified audit recorded.” Use “Not yet audited” only if the retained record actually establishes that no audit has occurred. Never erase a real date to make a clean starting table.
5. Save the scoped register/schema change through its supported source workflow. Reopen the saved rows and compare their count, dates and links against the pre-change snapshot.
6. Explain how later audit closeout records the actual check date and result. Hand unresolved inventory rows to the audit owner and prepare any authorized team notice.

## Definition of done (QA checklist)

[Quality assurance (QA)](https://localservicespotlight.com/article-guidelines/) means checking the work against the agreed result.

- [ ] One maintained date field exists without a competing current-status table.
- [ ] Verified old history remains intact; unknown history is explicit.
- [ ] Saved row counts and proof links reconcile; every mismatch has an owner.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A sample register has three pages: one checked on 2 August with a receipt, one carrying an undated green badge, and one known to be new. Keep 2 August for the first, use unknown for the second, and use not yet audited for the third only if the new-page record supports it. Adding a column creates no new audit.

## Handoff and Content Factory context

This work supports the [Content Factory, our four stages of using real content](https://blitzmetrics.com/content-factory/): Produce → Process → Post → Promote. Use the specific inputs and next task below to place the work; a maintenance task does not manufacture transcripts, clips or other stage outputs it does not call for.

[Record the audit result](https://local-service-spotlight.github.io/task-library/?task=update-status-table-in-definitive-article-guide#task-update-status-table-in-definitive-article-guide) writes later check results. [Assign auditors](https://local-service-spotlight.github.io/task-library/?task=schedule-and-assign-quarterly-auditors#task-schedule-and-assign-quarterly-auditors) receives rows needing a new check.

## Run with an agent

Give the AI worker this recipe, the real Inputs above, the intended result and the actions already authorized. Ask it to return the saved output, checks, evidence and remaining owner. Check its work against this guide; loading a skill does not prove access, installation of a job, or successful execution. Keep media muted with volume at zero if playback is needed.

For recurring work, keep the actual trigger, owner and runtime in the job record. Scheduling and observed firings are separate. Do not create a schedule merely because this guide mentions a review interval.

## Record the real execution

Open the run record when the work starts. Keep the exact starting recipe revision, one execution ID, source evidence and actual state. Write a [meta article, the record of one run](https://blitzmetrics.com/meta-article-prompt/) with decisions, results, checks, failures and next owner. Link it to this task and register it through the [Task Library](https://local-service-spotlight.github.io/task-library/) execution process. Writing is part of the work; public release follows existing authority.

Reuse the same execution ID for revisions, QA, meta writing and retries within that run. A blocked run stays open with its dependency and next owner; do not invent a finish time. Use supported findings to propose and verify a better recipe. A historical public-example count without distinct run IDs remains dated article volume, not verified execution frequency.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/knowledge-system-maintenance/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=add-last-audited-column-to-definitive-article-guide-status-table#task-add-last-audited-column-to-definitive-article-guide-status-table)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [current article guide](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records work together](https://localservicespotlight.com/meta-articles/)

## Review and evidence still needed

The inherited contributor status is `gap`. It is preserved, not promoted by this rewrite. That label alone does not verify document readiness, a client outcome, access or an executed task.

A real execution still needs its own source, reviewer, saved result and handoff evidence. The fictional example teaches the method; a real example with relevant proof is still needed where required. The task-specific flow above is source guidance; its visible presentation and the full document need a named reviewer and desktop/mobile checks.
