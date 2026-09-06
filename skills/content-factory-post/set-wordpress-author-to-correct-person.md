---
name: set-wordpress-author-to-correct-person
description: "Put the right name on the article. Check the saved author and the name readers see."
category: Content Factory — Post
stage: Post
definitive_article: GAP — to be written
status: needs-work
---

# Set WordPress author to correct person

Readers should know whose work and voice an article shows. This guide helps you put the right name on the page. Start with the agreed author, then check both the saved record and the public byline.

**The path:** Real author → Correct user record → Saved assignment → Visible byline.

**Use this when:** An article needs its correct author set, or a defined list of posts has a byline problem.

## Inputs
- The exact site and post IDs in scope, current author values, and a saved before record.
- The agreed author and identity evidence. On a personal-brand site, follow the maintained rule that the person is the author and voice. Company or guest content needs its correct editorial attribution.
- An existing WordPress user that represents that person, with correct public name and approved profile details.
- Permission to edit the scoped article author, and separate user/profile access if those details need changes. A new user is not automatically required.

## First-run prompt

> Use the exact post list and confirmed author mapping I provide. Check the current values, make only the already-authorized author changes, and compare the saved record with the public byline. Preserve other fields and guest credit. Report template or identity gaps without sweeping unrelated posts.

## Steps
1. Read the article and assignment. Confirm who is responsible for the published voice. Follow [Article Guidelines](https://localservicespotlight.com/article-guidelines/) for personal-brand first person; do not reassign a genuine guest’s work to a site owner merely to remove an admin-looking name.
2. Find the existing user record. Match the actual person using more than a similar name. Check the public display name, approved bio and photo. Keep login identity and public byline separate.
3. Open the exact post’s settings and select the correct author. Use the supported site editor or publishing tool. A REST route is suitable only when it is already the approved source path for that site and content type.
4. Save the change and read the same post back. Confirm the author ID changed as intended while content, URL, date, status and other fields stayed as scoped. If another writer changed the post, reconcile the current version before saving.
5. Open the public article after an authorized update. Check the visible byline and any author box. A template may show a custom byline that differs from the stored author; correct the actual supported source rather than pretending the data change fixed the display.
6. Check an author archive only where the site intentionally uses one. Confirm its displayed name and scoped posts. Do not enable an archive or change indexing merely to satisfy a generic checklist.
7. For a requested multi-post repair, repeat only for the explicit list and record each result. Do not turn a one-post fix into a site-wide reassignment. Route unresolved identity or template issues to the editorial/site owner.

## Definition of done (QA checklist)

- [ ] The author matches the person responsible for the article and the site’s voice policy.
- [ ] The exact saved author ID/display name is checked, with unrelated fields preserved.
- [ ] The served byline and any author box match the intended attribution.
- [ ] Archive behavior is checked where applicable, with an honest not-applicable reason otherwise.
- [ ] The scoped before/after list and remaining attribution issues are recorded.

## Example(s)

**Fictional teaching example — no WordPress user was changed.** Maple Cycle has two sample records: user 7 is “Site Admin,” and user 18 is the confirmed owner “Alex Reed.” A personal story in Alex’s voice should use user 18.

After the sample change, the stored author is 18 but the theme still prints “Maple Cycle Team” from a separate field. The data check passes; the visible-byline check fails. The next action is a scoped template/byline repair, not claiming the article is fixed.

A separate guest article by a real outside writer would keep that writer’s agreed credit. The invented IDs in this example are not commands to run on a real site.

## Handoff and Content Factory context

The publisher receives the checked author mapping and any display issue, then runs [Place the content on the SEO Tree](https://local-service-spotlight.github.io/task-library/?task=place-content-on-seo-tree-with-proper-links#task-place-content-on-seo-tree-with-proper-links) or [Final formatting and QA checks](https://local-service-spotlight.github.io/task-library/?task=step-17-final-formatting-and-qa-checks#task-step-17-final-formatting-and-qa-checks) as the actual workflow requires.

This task serves **Post** in the [Content Factory](https://blitzmetrics.com/content-factory/). Produce supplies the source, Process prepares it, Post places and checks it on the agreed channels, and Promote distributes proven work under its own scope. The task’s actual handoff above defines the next step; list order alone does not create a prerequisite.

## When this runs

Run for a new article or an explicitly scoped attribution repair. No recurring whole-site sweep is installed or implied.

## First-run setup and continuity

Use the exact account, source, destination and authority recorded for the job. Carry out publication, messages or repairs already authorized once their required checks pass; do not ask for the same approval again. If an action is outside that scope, finish the authorized work and state the specific remaining need. A login, plugin, or task file does not itself grant new authority.

Keep the latest state, record IDs, revisions and next owner in the project tracker or files. Before a retry, check the current saved/sent/published item to avoid duplicates or overwriting another edit. A model has no guaranteed memory, scheduler or account access just because it is called persistent. A future check needs a configured timer or a named person.

Keep all agent media previews muted with volume zero before playback. If this cannot be verified, use captions, metadata or still frames and state what was not tested. No first-load autoplay is part of these page instructions.

## Write up the real run

For each actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this exact task, source revision, trigger, work, decisions, evidence, result and next owner. Failed, partial and blocked attempts still get a written record. A private draft is a valid writing outcome; public publication follows the existing scope.

Keep one stable execution ID for the actual task run. Retries, checks and changed artifacts do not add runs. A separately scoped child task may have its own ID linked to its parent; writing the parent’s meta record is part of that same run. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains the distinction. Teaching examples below or above are not execution evidence and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. The owned training references below remain the method until that gap is reviewed.
- Exact Task Library record: [Set WordPress author to correct person](https://local-service-spotlight.github.io/task-library/?task=set-wordpress-author-to-correct-person#task-set-wordpress-author-to-correct-person)
- Working writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [WordPress author display](https://wordpress.org/documentation/article/post-author-block/)
- [WordPress post/page settings](https://wordpress.org/documentation/article/page-post-settings-sidebar/)

## Review and evidence still needed

The original contributor status in the header is preserved. It does not certify this proposed rewrite or prove that this account, publication, message, player or check has run. Every worked teaching example is explicitly invented; replace it with actual evidence when documenting a real execution.
- The real author identity, user record and theme behavior must be verified; no dedicated canonical task article is mapped.
