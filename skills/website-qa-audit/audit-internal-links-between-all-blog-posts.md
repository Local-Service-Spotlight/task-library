---
name: audit-internal-links-between-all-blog-posts
description: "Help readers find the next useful page. Check links in each post and fix gaps in the site map."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Audit internal links between all blog posts

Your best post is less useful if no one can find it. This guide helps you link each post to the next useful page. Start with a full list of live posts, not just the pages a tool found.

**The path:** Full post list → Link map → Relevant fixes → Fresh check.

**Use this when:** A site launch, content review or defined batch of posts needs its internal links checked.

## Inputs
- The exact site, published post inventory and scope of pages to inspect. Include posts known to the CMS even if a crawl cannot reach them.
- The site’s [SEO Tree](https://blitzmetrics.com/seo-tree/): the main guide for each topic and the actual service or offer pages.
- A browser and a link report from an available crawler or supported CMS tool. Link Whisper is optional; a report is useful only when its scan date and coverage are known.
- Access for authorized edits, the current page source, and a tracker for unresolved inbound links owned by another editor.

## First-run prompt

> Use the supplied site, published inventory and topic map. Reconcile them with a fresh link report. Check relevant body links and incoming links separately. Perform already-authorized edits, verify canonical destinations, and return coverage, exact remaining gaps and next owners.

## Steps
1. Join the published post inventory with the crawl list by final canonical URL. Record exclusions such as private drafts and identify published pages absent from the crawl. A crawler that starts at the home page cannot alone prove that it found every orphan.
2. For each post, list body links to other posts, its main topic guide and any genuinely useful service page. Separate navigation/footer links from contextual links in the article. Record live status and named-anchor destinations.
3. Build inbound links from the same inventory. An orphan has no known incoming link in the defined scope; it is not the same as a page with no outgoing links. Mark missing coverage as unknown instead of asserting a site-wide zero.
4. Read each page’s purpose. Add a link to the maintained guide where the reader needs that explanation. Add another post or service link when it answers the next question; a policy or reference page does not need a forced sales link.
5. Choose an existing relevant article or hub for each missing inbound link. Write the exact sentence and descriptive anchor. Follow [entity linking](https://blitzmetrics.com/entity-linking/) for people, brands, owned explainers and primary proof. Do not turn every mention into a link.
6. Make the edits already authorized through the supported page source. Preserve the canonical URL and check for concurrent changes. If the inbound source is outside this job, give its owner the exact proposed placement and keep that link pending.
7. Refresh the report after the edits and open the changed canonical pages as a visitor. Confirm the intended body links, final targets and fragments. A plugin’s count from yesterday does not verify today’s links.
8. Save the inspected denominator, relevant link additions, remaining orphans, unknown pages and next owners. Report coverage separately from findings; do not promise rankings or traffic from link counts.

## Definition of done (QA checklist)

- [ ] The published inventory and crawl are reconciled, with scope, date and missing coverage stated.
- [ ] Body links follow the page’s role and lead to relevant working canonical targets.
- [ ] Inbound and outbound gaps are separate; no page is called an orphan merely because it lacks outgoing links.
- [ ] Authorized repairs are visible on the canonical pages; other-owner placements remain pending.
- [ ] A fresh report and exact unresolved list support the result.

## Example(s)

**Fictional teaching example — no site was scanned or edited.** Maple Cycle’s CMS lists three posts: “Repair quote,” “Photos to send,” and “Brake wear.” The crawler finds the first two. The CMS list reveals that “Brake wear” still needs an inbound-link check.

“Repair quote” already links to “Photos to send.” The proposed new sentence in “Photos to send” is “Use the brake-wear guide if you are not sure which close-up to take.” That is a relevant inbound placement for the third post. The audit still checks the target and public source after saving.

The teaching result is “3 known posts; 1 newly proposed inbound placement; public repair not yet verified.” It is not “all orphan pages fixed” based on a two-page crawl.

## Handoff and Content Factory context

The content owner receives the updated topic map and unresolved placements. [Check broken links](https://local-service-spotlight.github.io/task-library/?task=check-for-broken-links#task-check-for-broken-links) verifies link destinations; it does not decide the editorial relevance of every link.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run for a launch or a defined content audit, then after relevant new posts or link changes. Use an existing recurring review only if it is configured for this site.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Audit internal links between all blog posts](https://local-service-spotlight.github.io/task-library/?task=audit-internal-links-between-all-blog-posts#task-audit-internal-links-between-all-blog-posts)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [SEO Tree](https://blitzmetrics.com/seo-tree/)
- [Entity linking](https://blitzmetrics.com/entity-linking/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The actual published inventory, current crawl coverage, edit access and public before/after evidence require the site.
