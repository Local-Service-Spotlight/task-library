---
name: make-a-personal-brand-poster
description: "Turn a person's public record into an 18 x 24 inch poster they can frame, where every fact has a source and every photo has an owner who said yes."
category: Personal Branding
stage: Process
definitive_article: GAP — pending publication at /personal-brand-poster
status: gap
---

# Make a personal brand poster

Give someone a poster of their real story that they will want to frame. This recipe turns their public record into an 18 x 24 inch print where every fact can be checked and every photo has an owner who said yes. It builds on the sourced record from the [podcast inventory](https://local-service-spotlight.github.io/task-library/?task=how-to-inventory-a-podcast-on-youtube#task-how-to-inventory-a-podcast-on-youtube) and the [positive mentions harvest](https://local-service-spotlight.github.io/task-library/?task=positive-mentions-harvester#task-positive-mentions-harvester).

**The path:** Public record → Theme from their story → Fact sheet → Photo permission → Draft proof → Final print file → Client approval

**Start when:** A person, or the leader of a company, wants a printed piece for a wall, a gift, an event or a stage, and enough of their record is public to fill it with checkable facts. If most facts would come from memory or private files, build the record first.

## Inputs

- The subject's own site and About page, their company's site and team page, and their media, speaking and book pages. Each fact on the poster must come from a page a stranger can open.
- Prerequisite outputs, when they exist: a de-duplicated list of recordings, such as the [podcast inventory](https://local-service-spotlight.github.io/task-library/?task=how-to-inventory-a-podcast-on-youtube#task-how-to-inventory-a-podcast-on-youtube), and named, linked quotes from the [positive mentions harvest](https://local-service-spotlight.github.io/task-library/?task=positive-mentions-harvester#task-positive-mentions-harvester).
- Photos with a known owner: the client's own photos, their company's team photos, or photos whose owner gave written permission. Record the owner and the permission before a photo goes on the poster.
- A person on the client's team who can confirm name spellings, supply photos and approve the proof.
- The kit at [local-service-spotlight.github.io/task-library/kits/poster/](https://local-service-spotlight.github.io/task-library/kits/poster/): the 18 x 24 artboard template, `render_poster.py`, the fact and photo sheets, the QA checklist and a prompt to paste into an AI app. An editable design canvas, such as Claude's Design artifact, works for the layout step too.
- No account access is needed. Nothing is published or printed during this task.

## Steps

1. **Collect the public record.** List every source URL. Note when the subject's own pages disagree with another page about a title, a date or a count. *Decision:* if the record is too thin to fill the main zones honestly, stop and hand back the gap instead of padding.
2. **Choose a theme from their real story.** Look for a true thread in their background or their own branding, such as a former career or the name they give their program. Use it for the title line and section names. *Decision:* if no true thread exists, use a plain "record" theme. Never invent a nickname, title or award.
3. **Fill the fact sheet.** Write one row per printed fact with the exact text, who is making the claim, the source URL, what the source says and the date checked.
   - Keep the company's published claims ("as published") apart from numbers you counted yourself ("on the public record").
   - Remove duplicates before counting: one episode posted as audio and as video counts once, and a short clip is not an interview.
   - Use the subject's own About page for titles and employers. Note any page that disagrees.
   - Label results that clients reported to the subject as their report, not audited case studies.
   - Give each person the narrowest verb the source supports, such as "Had her on [show]" or "Wrote the foreword to [book]". Never write friend, partner or mentor unless the source does.
   - Drop anything you cannot source, including an "award" that was only a mention from a stage.
4. **Clear every photo before it goes on the poster.** Record who owns it, where their permission is kept, the exact file you downloaded and its original pixel width. A photo found on a public post is not permission. Use the client's own photos, or get the owner's written OK. Do not pull photos of public figures or partners from the web. Ask the client's team for photos they own instead. *Decision:* if the right photo has no permission yet, leave the slot open or use a photo the client owns, and keep asking. Do not print around the gap.
5. **Check photo resolution at printed size.** Count the original pixels across the printed width. 150 ppi or more passes. 100 to 149 is a warning that may be fine from about three feet, so ask for a larger original. Under 100 fails. Enlarging a small file adds no detail.
6. **Lay out the artboard.** Use the template zones: masthead with name, title, one-sentence story and a quote in their own words; a proof band with their claims and your counts side by side; places; client-reported results; people and team; named quotes; and a footer listing every source. Keep text at least 0.5 in from every edge, because a frame covers the outer edge.
7. **Render a draft and fix it.** Run `render_poster.py --draft`. Fix every FAIL: unfilled slots, unsourced facts, unowned photos, tags that open and never close, overflow, text under 9 pt, text near the edge and low-resolution photos. Read anything under 10.5 pt that is not fine print at arm's length on a 100% view.
8. **Render the final with a new version number and date.** The script writes `<Subject>-<Deliverable>-18x24-v<N>-<YYYY-MM-DD>.pdf`, a preview PNG with the same suffix and a QA JSON. It refuses to reuse a version number, so earlier versions are kept. Confirm the PDF is exactly 1296 x 1728 pt, every font is embedded and the PDF title carries the version and date.
9. **Get the proof approved.** Send the PDF, preview and fact sheet to the client's team with a short list of what they must confirm, such as name spellings and photo permissions. Record the approval. Ask the printer about bleed and color before ordering.
10. **Record the run.** Write the meta article with an execution ID, the recipe revision used, what changed in each version, the check results, open items and the next owner.

## Definition of done (QA checklist)

Quality assurance (QA) means checking the actual file against these requirements. The kit's `QA-CHECKLIST.md` marks which checks `render_poster.py` runs automatically.

- [ ] Every printed fact has a fact-sheet row with a source URL, a claim owner and a check date; there are no unfilled slots.
- [ ] The company's claims and your own counts are labeled separately, counts are de-duplicated, and client-reported results say whose report they are.
- [ ] Every person has the narrowest verb the source supports, and every quote is exact, named and linked.
- [ ] Every photo has an owner and a permission record: the client's own photo or the owner's written OK. None was taken from a public post as if it were permission.
- [ ] Photos are at least 150 ppi at printed size, counted on the original pixels, or carry a recorded warning and a request for a bigger original.
- [ ] Tags balance, nothing overflows, no text is under 9 pt, and all text is at least 0.25 in from the trim (0.5 in for framing).
- [ ] The PDF is one page at exactly 18 x 24 in (1296 x 1728 pt), all fonts are embedded and the title carries the version and date.
- [ ] File names carry the version and date, every new version has a new name, and earlier versions are kept.
- [ ] The client's team approved the proof, and the approval is recorded.
- [ ] Linked back to the definitive article and relevant siblings.
- [ ] Complies with the [Article Guidelines](https://localservicespotlight.com/article-guidelines/) for any reader-facing page made from the poster.
- [ ] If it creates a reader-facing artifact, the short opening makes relevance, useful outcome and supporting mechanism clear; quoted reviewer evidence is retained and the artifact delivers its promise.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A coach's media page lists 31 interviews. The fact sheet finds two episodes posted twice, once as audio and once as video, and one 60-second clip. The poster prints 28 and cites the page. The coach's company page says "30+ shows", so that figure appears only in the "as published" half, in the company's words. A stage photo the coach reposted belongs to an event photographer, so its slot stays open until the photographer's written OK arrives. The team photo from the company's own site goes in instead.

### First recorded run

The first run of this recipe produced a client poster in November 2026. Its run record is held privately until the client approves using that poster as a public example. When the record is published, it will be linked here.

## Handoff and Content Factory context

This task sits in **Process** in the [Content Factory: Produce, Process, Post and Promote](https://blitzmetrics.com/content-factory/): it turns an existing record into a finished print asset. It records nothing new.

- **Before it:** the sourced record from the [podcast inventory](https://local-service-spotlight.github.io/task-library/?task=how-to-inventory-a-podcast-on-youtube#task-how-to-inventory-a-podcast-on-youtube), the [positive mentions harvest](https://local-service-spotlight.github.io/task-library/?task=positive-mentions-harvester#task-positive-mentions-harvester) and, for the portrait, [consistent headshots](https://local-service-spotlight.github.io/task-library/?task=add-consistent-headshots-and-bios-across-profiles#task-add-consistent-headshots-and-bios-across-profiles).
- **Hand off:** the approved PDF, preview, fact sheet and QA JSON go to the client's account lead (client success), who orders the print and records delivery.
- **Next, only if the client wants it shown online:** the approved preview goes to their personal brand site through [Link all content back to the personal brand site](https://local-service-spotlight.github.io/task-library/?task=link-all-content-back-to-personal-brand-site#task-link-all-content-back-to-personal-brand-site), with a photo record for every image on that page.
- **Gap:** no Task Library task yet covers ordering prints and confirming delivery.

## Start with an agent

Give the [AI worker](https://blitzmetrics.com/build-agents/) this recipe, the kit and the subject's public URLs. Ask it to stop after the fact sheet, so a person can check the sources before any design work. A [skill is a written recipe](https://localservicespotlight.com/plugin/); loading one does not prove account access or perform the task. Use the app's actual supported tools and verified file access. Keep a missing human step, such as photo permission or proof approval, with its real owner. This guide creates no schedule.

## Record the real execution

Open the run record when work begins. Keep one execution ID, the starting recipe revision, the real inputs and the current state. Write the [meta article, the record of this execution](https://blitzmetrics.com/meta-article-prompt/) with the actual steps, every version and what changed in it, the results, checks, failures and next owner. Writing is required; public release follows existing authority and, for a client poster, the client's OK. Link it to this recipe and the [Task Library](https://local-service-spotlight.github.io/task-library/).

## Definitive article & links

- Definitive article: pending publication at blitzmetrics.com/personal-brand-poster/ (not live yet, so not linked)
- [The poster kit](https://local-service-spotlight.github.io/task-library/kits/poster/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=make-a-personal-brand-poster#task-make-a-personal-brand-poster)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Definitive article and task recipe standard](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records fit together](https://localservicespotlight.com/meta-articles/)
- Related: [Keep speaker bureau profile bookable](https://local-service-spotlight.github.io/task-library/?task=keep-speaker-bureau-profile-bookable#task-keep-speaker-bureau-profile-bookable) uses the same approved facts and photos.

## Review and evidence still needed

Status is `gap` because the definitive article is written but not yet published. Once it is live, set `definitive_article` to `/personal-brand-poster`, link it above and request review.

No independent reviewer has checked this recipe yet. The first real run is recorded privately until the client approves public use. The kit's script was tested on a synthetic fixture: one passing final render and refusals for a missing source, a photo found on a public post, a photo with no owner, a reused version number and a low-resolution photo. A synthetic test does not prove a client run. A reviewer must check the opening, the full method, the links and the handoff against this exact revision.
