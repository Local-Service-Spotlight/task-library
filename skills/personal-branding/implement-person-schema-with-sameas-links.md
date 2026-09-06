---
name: implement-person-schema-with-sameas-links
description: "Help search tools tell which profiles belong to you."
category: Personal Branding
stage: —
definitive_article: /personal-brand
status: needs-work
---

# Implement Person schema with sameAs links

Help search tools tell which profiles belong to you. This guide adds a clear set of facts to your site and checks each profile link. Start with your true name, your site and the profiles you have verified.

**The path:** Visible facts + verified profiles → One Person ID → Valid markup → Live identity check

**Start when:** The site and accepted profiles are ready for structured Person identity markup.

## Inputs

- [Build the personal brand site](https://local-service-spotlight.github.io/task-library/?task=build-personal-brand-website#task-build-personal-brand-website) and [Align photos and bio facts](https://local-service-spotlight.github.io/task-library/?task=add-consistent-headshots-and-bios-across-profiles#task-add-consistent-headshots-and-bios-across-profiles) with accepted facts and actual live profile URLs.
- The current site source, theme/plugin markup owners and authorized edit rail.
- Approved public name, image URL, role, site URL and identity evidence; [Schema.org’s sameAs definition](https://schema.org/sameAs).

## Steps

1. Inspect all structured data already emitted on the relevant page. Find the existing Person ID, theme/plugin owner and graph relationships. Reuse or reconcile the maintained identity instead of pasting a second conflicting block just because its syntax is valid.
2. List only facts visible on the site or supported by current public evidence: name, site URL, real image and role where known. Person describes the human; a separate business profile describes the business. Do not use the business’s identity URL as the person’s sameAs by default.
3. Build the sameAs list from pages that unambiguously identify the same person, following [Schema.org’s sameAs definition](https://schema.org/sameAs). Inspect each target’s identity and current accessibility. A news story mentioning the person is normally a citation; a wrong-person URL or uncertain profile remains excluded.
4. Prepare JSON-LD, the structured-data format, with @context, Person type and one stable @id for the person. Include the verified fields and accepted URLs. Preserve existing WebSite, WebPage, Organization and other valid graph nodes and their distinct IDs.
5. Validate JSON syntax and Schema.org vocabulary with an appropriate schema validator. Google’s Rich Results Test covers its supported search features; a bare Person can be valid without a detected rich-result type. Use ProfilePage only where the actual page meets [Google’s ProfilePage requirements](https://developers.google.com/search/docs/appearance/structured-data/profile-page).
6. Apply the reviewed change through the supported source owner when authorized. Read back the actual public markup, count unique Person IDs for this person and verify visible facts and links. A reciprocal profile link is useful when supported, not a requirement imposed by sameAs itself.
7. Save the exact before/after revision, validator outputs, accepted identity URLs and remaining gaps. Use [Google’s structured data rules](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) for search requirements. Valid markup is a checked description, not a promise of indexing, rich results or a Knowledge Panel.

## Definition of done (QA checklist)

Quality assurance (QA) means checking the actual result against its agreed requirements. Follow the [Article Guidelines](https://localservicespotlight.com/article-guidelines/).

- [ ] The intended person has one stable identity ID and no competing or wrong-person claims.
- [ ] Markup is syntactically valid and its fields and sameAs identities are verified against visible evidence.
- [ ] Saved and public markup match; feature eligibility and actual search appearance remain separate.
- [ ] The exact output, source revision, reviewer evidence and remaining owner action are saved.
- [ ] For any reader-facing output, the short grade-five opening states the reader’s useful outcome and supporting method or proof. The body delivers that promise; a useful authentic visual appears in the first screen. Retain exact text and quoted reviewer evidence.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional architect’s theme already creates a Person node. A proposed custom block would create another ID, so the developer updates the existing node instead. Her own profile is accepted as sameAs; an article about her firm stays a normal citation. A valid schema result is saved without claiming that Google displayed a panel.

## Handoff and Content Factory context

[Maintain the fuller identity graph](https://local-service-spotlight.github.io/task-library/?task=implement-technical-schema-markup#task-implement-technical-schema-markup) receives the source owner, stable ID and accepted URLs; [Review search and real inquiries](https://local-service-spotlight.github.io/task-library/?task=measure-search-impressions-traffic-inbound-opportunities#task-measure-search-impressions-traffic-inbound-opportunities) records any later search observations.

This task supports the [Content Factory: Produce, Process, Post and Promote](https://blitzmetrics.com/content-factory/). Identity, proof, access or coordination can support several stages. Use the real inputs and receiving owner above; this task does not create unrelated transcripts, clips or ads merely because the diagram has four stages.

## Start with an agent

Give the [AI worker](https://blitzmetrics.com/build-agents/) this recipe, the real inputs, desired result and actions already authorized. Ask for the saved output, sources, checks and next owner. A [skill is a written recipe](https://localservicespotlight.com/plugin/); loading one does not prove account access or perform the task. Use the [installation guide](https://localservicespotlight.com/install/) if reusable setup is needed. A ZIP is a source snapshot, not an access grant or automatic update.

Use the app’s actual supported tools and verified file/account access. Keep a missing human verification step with its real owner. Recurring work needs its own configured job, trigger, timezone and observed result; this guide creates no schedule. Before any media playback, mute the player and set its volume to zero. If silence cannot be verified first, use captions, frames, metadata or another silent check.

## Record the real execution

Open the run record when work begins. Keep one execution ID, starting recipe revision, real inputs and current state. Write the [meta article, the record of this execution](https://blitzmetrics.com/meta-article-prompt/) with actual steps, results, checks, failures and next owner. Writing is required; public release follows existing authority. Link it to this recipe and the [Task Library](https://local-service-spotlight.github.io/task-library/).

Reuse the same execution ID for internal checks, revisions, retries and meta writing. A blocked run stays open with its dependency and owner, without an invented finish time. Dated public examples and distinct verified execution counts remain separate. Propose the smallest source-backed recipe improvement when the actual evidence reveals a defect.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/personal-brand/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=implement-person-schema-with-sameas-links#task-implement-person-schema-with-sameas-links)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Definitive article and task recipe standard](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records fit together](https://localservicespotlight.com/meta-articles/)

### Primary method references

- [Schema.org sameAs](https://schema.org/sameAs)
- [Google ProfilePage](https://developers.google.com/search/docs/appearance/structured-data/profile-page)
- [Google structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

## Review and evidence still needed

The inherited contributor status is `needs-work`. It is preserved, not promoted by this rewrite. That label alone does not prove document readiness, account access, an actual execution or a client result.

The fictional example teaches the method and does not fill a real-run evidence gap. A named semantic reviewer must check the actual opening, full method, sources and handoff. Check the useful opening visual in the normal rendered guide at the current required desktop and mobile sizes, including 1280 × 800 and 390 × 844. Source readability checks do not prove public presentation or task execution.
