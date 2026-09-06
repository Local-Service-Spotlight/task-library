---
name: check-all-cta-buttons-lead-to-correct-destinations
description: "Check that each button does what its words say. Find wrong links before a customer gets stuck."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: needs-work
---

# Check all CTA buttons lead to correct destinations

A wrong button can stop a customer from taking the next step. This guide helps you check each button on a phone and a large screen. Start by writing down what the button should do.

**The path:** Button promise → Expected action → Safe check → Fixed or pending result.

**Use this when:** A site, landing page or changed form needs its call-to-action buttons checked. A call to action is the next step you ask a visitor to take.

## Inputs
- The exact pages and button inventory, including menus, sticky bars, forms and mobile-only versions.
- The intended destination or action for each button, plus the correct public phone/email details where applicable.
- Desktop and phone browser views, supported page-edit access, and the existing scope for repairs and any real submissions.
- A designated test receiver and authorized test details only when a form, booking or other submitted action is part of the job.

## First-run prompt

> Use the provided pages and expected button actions. Check targets and desktop/phone behavior, perform only the real submissions already in scope, and verify their receipts. Fix authorized issues and return a button-by-button result that separates navigation from actual delivery or transactions.

## Steps
1. List every button in scope with its page, visible words, location and expected result. Distinguish links, local section jumps, script-driven dialogs and actual submitted actions.
2. Inspect each link target before interacting. Check final URLs and named anchors. A “Home” button can correctly lead home; a # link can correctly open a real dialog or jump to an existing section. Decide by the stated purpose, not by a blanket URL rule.
3. Open ordinary page links and harmless dialogs, then verify the visible destination and close behavior. Check redirects, accidental draft URLs, overlays and buttons that appear active but do nothing.
4. For phone and email buttons, inspect the tel: or mailto: value and confirm the intended receiver. A correctly formatted link or opened handler does not prove a completed call or delivered email. Do not place a call or send a message merely to check the link.
5. For forms, checkout, booking, downloads behind an opt-in and other state-changing actions, use the real authorized test scope. If submission is not included, finish link/layout checks and mark delivery or transaction behavior untested. If included, use the designated receiver and verify the resulting record and receipt without inventing a customer action.
6. Repeat the relevant check at 1440×860 and 390×844. Confirm the visible button is usable, is not hidden by a banner and has a meaningful accessible name. Record mobile-specific targets separately when they differ.
7. Repair exact wrong targets or broken behavior already in scope through the supported source. Preserve existing working targets and recheck changed buttons on the normal canonical page.
8. Log a row per button: expected action, inspected target, interaction performed, observed outcome, result and next owner. Separate link pass, submission pass and receiver confirmation.

## Definition of done (QA checklist)

- [ ] Every in-scope visible button has an expected action and an observed result on the intended viewports.
- [ ] Targets, anchors and dialogs match the button promise; legitimate local actions are not falsely failed.
- [ ] No call, send, booking, subscription or payment is inferred from a link check.
- [ ] Authorized repairs are rechecked; delivery and transaction tests outside scope remain explicitly untested.
- [ ] Failures and unknown results name the exact button and next owner.

## Example(s)

**Fictional teaching example — no button was clicked or request sent.** Maple Cycle has “Get a repair quote,” “Call the shop,” and “See our work.”

The sample quote button opens the correct form. Its layout passes, but delivery remains untested without a submitted test and receiver receipt. The call button contains the wrong phone number, so it fails the target check without placing a call. “See our work” points to `#work`, and that section exists; the local jump is valid.

The report separates these outcomes instead of calling all three buttons “working” because they look blue.

## Handoff and Content Factory context

The page owner receives exact target fixes. [Verify the opt-in form](https://local-service-spotlight.github.io/task-library/?task=verify-email-opt-in-form-exists-and-works#task-verify-email-opt-in-form-exists-and-works) owns a required form test, while the designated business receiver confirms delivery when that test is in scope.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before launch and after a relevant button, form or destination change. This guide does not schedule calls, messages or repeat submissions.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Check all CTA buttons lead to correct destinations](https://local-service-spotlight.github.io/task-library/?task=check-all-cta-buttons-lead-to-correct-destinations#task-check-all-cta-buttons-lead-to-correct-destinations)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The intended action map, actual receiver and authorized submission scope must come from the site’s project.
