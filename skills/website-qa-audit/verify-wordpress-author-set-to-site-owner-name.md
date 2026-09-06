---
name: verify-wordpress-author-set-to-site-owner-name
description: "Check that each byline names the right author. Keep real guest writers and fix default account names."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify WordPress author set to site owner name

A byline should name the person behind the work. This guide helps you check the names readers see on posts. Start with the real author record, so you do not give someone credit by mistake.

**The path:** Real authorship → Stored author → Visible byline → Verified correction.

**Use this when:** A personal-brand WordPress site needs its author-account assignments and public bylines audited.

## Inputs
- The complete scoped published-post inventory and actual authorship/voice plan for each post.
- The approved public author identities, bios and portraits, with supported WordPress/user read access.
- Authorized scope for byline assignments/profile edits and the current source revision.
- The live post/author-template behavior, including any legitimate guest or team authors.

## First-run prompt

> Use the supplied post inventory and actual authorship records. Reconcile stored authors with public bylines, fix authorized default or mistaken assignments, and preserve genuine guest/team exceptions and account roles. Verify canonical output and return exact counts and unresolved source decisions.

## Steps
1. Confirm who the content represents. Owner-authored personal-brand work should normally use the owner’s public identity; real guest posts or a genuine multi-author site retain truthful attribution. The login that uploaded a post is not necessarily its public author.
2. Build a complete post-to-author map from the supported CMS or paginated API. The posts endpoint defaults to a limited first page; a single response is not a complete inventory. Reconcile the result with the known published count.
3. Inspect the existing author account and public display name, bio and approved image. Avoid default “admin” or misspellings in the public byline, but do not expose login names or create a privileged account just for display.
4. Compare stored author IDs with the actual visible bylines and any author archive/bio link. Theme/builder output may not match the field, or may deliberately suppress an archive. Record the actual intended behavior rather than creating thin archives automatically.
5. Review each mismatch against the authorship record. Do not bulk-assign all posts to the owner solely because the old task name says so. Preserve guest speakers, joint/organizational attribution and accurate published source context.
6. Apply authorized exact assignments or profile-display corrections through the supported route, checking current revisions before saving. Keep user roles, access, passwords, URLs and other account settings outside an ordinary byline correction.
7. Reopen the canonical changed posts and intended author pages on desktop/phone. Verify the correct public name, source-supported bio/image and working destinations; saved author IDs alone do not prove the visible output.
8. Save the count checked, corrected, legitimately excepted and still unresolved with evidence. No authorship or E-E-A-T gain is inferred from changing a display name.

## Definition of done (QA checklist)

- [ ] Each scoped post has source-backed intended authorship, including legitimate exceptions.
- [ ] Inventory pagination/coverage and stored author IDs are recorded.
- [ ] Public bylines and intended author links match the actual content owner and source facts.
- [ ] Authorized corrections preserve access roles, account privacy and stable URLs.
- [ ] Canonical readback supports the result; no false owner credit or automatic bulk reassignment occurs.

## Example(s)

**Fictional teaching example — no author assignment was changed.** Maple Cycle’s founder wrote two personal guides, and a named mechanic supplied a guest article. The founder guides show “admin” because an editor uploaded them; the guest article already names its actual writer.

The teaching correction assigns the two owner guides to the approved public author identity and preserves the guest writer. Changing all three to the founder would make the audit less truthful. A first API response with only ten posts would also need pagination before a site-wide claim.

## Handoff and Content Factory context

The content owner receives the attribution map. [Check intended page voice](https://local-service-spotlight.github.io/task-library/?task=verify-all-pages-written-in-first-person#task-verify-all-pages-written-in-first-person) is related, but a first-person passage does not by itself determine authorship.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run before publication and after relevant imports, author-template or attribution changes. No standing user-account changes or access grants are created by this check.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify WordPress author set to site owner name](https://local-service-spotlight.github.io/task-library/?task=verify-wordpress-author-set-to-site-owner-name#task-verify-wordpress-author-set-to-site-owner-name)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [WordPress post fields and list pagination](https://developer.wordpress.org/rest-api/reference/posts/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The real authorship record, existing public profiles and canonical template behavior require the site.
