---
name: check-social-profiles-linked-and-prominent
description: "Help people find your real public profiles. Check the links and make them easy to use."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Check social profiles linked and prominent

Visitors may want to see your work on another site. This guide helps you link to the right public profiles. Start with a checked list so you do not send people to someone else.

**The path:** Verified profiles → Clear placement → Right destinations → Phone check.

**Use this when:** A site launch, identity change or social-link audit needs public profile navigation checked.

## Inputs
- The exact site and approved public-profile inventory with person/company identity evidence.
- The current home, about and footer layouts, including mobile navigation.
- Supported edit access and the scope for link/label changes.
- A record of restricted or retired profiles and the actual owner who can resolve identity gaps.

## First-run prompt

> Use the supplied site and verified public-profile list. Check the right entity, visible placement and labels at desktop and phone widths. Fix already-authorized link issues, preserve private-account limits, and return exact public destinations with unresolved identity evidence.

## Steps
1. Review the public-profile inventory and classify each owner as the person or business. Include useful public accounts approved for this site; do not expose private accounts or create new ones to fill an icon row.
2. Inspect the home page, about page and footer on desktop and phone. Record where visitors can find the relevant profiles. The house goal is clear discovery, not repeating every icon in every section.
3. Check each link’s exact destination and visible owner where accessible. Use canonical profile URLs instead of search-result links or unrelated posts. A shared display name alone is not enough to establish identity.
4. Read the link or icon’s accessible name and visible context. A visitor should know whether it leads to the founder’s LinkedIn or the company’s page. Icons that depend only on color or an absent label need correction.
5. Verify phone placement, tap usability and overlays. A footer icon hidden on mobile is not a passed phone check. Keep ordinary profile navigation separate from logging in, following, messaging or claiming an account.
6. Review schema consistency with the applicable entity map. Do not require a business footer link to appear in the owner’s personal sameAs array. Use [Check schema profile identity](https://local-service-spotlight.github.io/task-library/?task=check-schema-connects-to-all-verified-profiles#task-check-schema-connects-to-all-verified-profiles) for that distinct check.
7. Apply authorized destination, label or placement repairs through the supported source. Preserve valid profile links and record any owner evidence still missing rather than guessing an account.
8. Reopen the canonical pages at both viewports and save the actual link inventory, checked date and remaining access limitations. A login-restricted profile can remain unknown without being called dead.

## Definition of done (QA checklist)

- [ ] Useful approved public profiles are easy to find on desktop and phone.
- [ ] Each destination is the intended person or company, with evidence or a precise unknown.
- [ ] Labels explain the destination, and icons remain usable on mobile.
- [ ] Navigation checks do not imply follows, messages, login success or account ownership.
- [ ] Schema identity and navigation are related but not falsely forced to have identical lists.

## Example(s)

**Fictional teaching example — no profile was opened or linked.** Maple Cycle’s footer has two LinkedIn icons. One belongs to founder Alex; the other belongs to the company, but both are labeled only “LinkedIn.”

The teaching fix labels them “Alex on LinkedIn” and “Maple Cycle on LinkedIn,” uses their verified canonical profile URLs and checks the phone layout. A third profile with a similar name lacks owner evidence, so it remains pending rather than being added to complete a row.

## Handoff and Content Factory context

The site owner receives the profile map and any identity questions. [Review footer navigation](https://local-service-spotlight.github.io/task-library/?task=verify-footer-includes-social-links-and-secondary-nav#task-verify-footer-includes-social-links-and-secondary-nav) covers the broader footer layout when that task is in scope.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at launch and when public profile identity or navigation changes. Any periodic check needs the real site cadence; no follows or outreach are created by this guide.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Check social profiles linked and prominent](https://local-service-spotlight.github.io/task-library/?task=check-social-profiles-linked-and-prominent#task-check-social-profiles-linked-and-prominent)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Entity linking](https://blitzmetrics.com/entity-linking/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The verified public-profile inventory and actual desktop/phone checks require the site.
