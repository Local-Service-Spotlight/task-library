---
name: validate-cross-reference-integrity-across-articles
description: A link should take people to the help its words promise.
category: Knowledge System Maintenance
stage: —
definitive_article: /knowledge-system-maintenance
status: needs-work
---

# Validate cross-reference integrity across articles

Check that each link leads to the help its words promise. Read the source page and its linked page so readers get the right answer. Next, [record the full article audit result](https://local-service-spotlight.github.io/task-library/?task=update-status-table-in-definitive-article-guide#task-update-status-table-in-definitive-article-guide) once the topic, steps, and facts are also checked.

**The path:** Reference list → Read both pages → Scoped fixes → Check again

**Start when:** An audit needs to check whether the links around a page still describe their targets accurately.

## Inputs

- The audited article’s current URL, known aliases, role and source revision.
- A scoped site export or internal-link report, with its coverage and collection time; access to the current source and rendered pages, or a named owner for pages the auditor cannot open.
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/) and the owned [SEO Tree, how related pages link to their main topic](https://blitzmetrics.com/seo-tree/) for topic relationships.

## Steps

1. Build a working table with source URL, source revision, anchor and surrounding claim, destination URL or fragment, direction (inbound or outbound), and status. Populate inbound links from the available site export or link report, checking known aliases and title mentions. Search can find more candidates, but it cannot prove a complete inventory; record covered sites, collection dates and inaccessible sources.
2. Read each inbound anchor with its surrounding sentence and then read its current destination. Record whether the destination teaches or proves the promised task, concept or claim and whether any cited section still exists. If access fails, mark meaning UNKNOWN rather than passing the link from its URL.
3. Mark wrong subject links, removed fragments, misleading descriptions and redirects to the wrong page. A successful page load proves reachability only, not that the linked claim is true.
4. Inventory the major concepts and prerequisites mentioned in the article, including ones with no link yet. Explain unfamiliar terms in a short phrase and link the first useful mention to the existing maintained guide. Follow the [SEO Tree](https://blitzmetrics.com/seo-tree/): a supporting page links to its main topic, and the main guide links back when that example or subtask helps readers. Search the Task Library and owned sites before proposing a new article. Create one only for a distinct reader need with enough evidence, useful instruction and a clear place in the tree; otherwise improve the existing guide or define the term in place. Record a missing-guide gap rather than inventing a destination.
5. Use concise descriptive anchors that fit the sentence. Retain an external primary source when it supports a provider-specific fact or required tool action. Never retarget an external documentation link solely because an internal page mentions the same product. Check relationship status before linking a named business. Ardmor and Pure Plumbing are former clients: verified historical examples may remain as plain text, without links to those companies or claims of a current client relationship. Use Local Service Spotlight (LSS) for the current organization; the publishing domain can remain blitzmetrics.com. Preserve exact historical quotations and technical identifiers.
6. Repeat the same table and meaning check for outbound links, including related task and topic links. A task recipe, entity hub, comparison and story have distinct purposes; do not relabel one just to fill a required link slot.
7. Prepare exact source edits for inaccurate references and preserve all unrelated content/media. Release only through the owning source and existing authority; otherwise hand the owner the precise sentence, destination and reason.
8. Reopen each changed link and read the rendered sentence at both ends. Save the dated table with one result per listed link: correct, repaired and read back, wrong and handed off, or UNKNOWN with access reason. Count each result, name coverage limits and remaining owners, and propose a source-workflow fix if repeated renames or edits leave references stale.

## Definition of done (QA checklist)

[Quality assurance (QA)](https://localservicespotlight.com/article-guidelines/) means checking the work against the agreed result.

- [ ] The dated reference table states actual coverage, source revision and counts; every listed link has a semantic result or explicit UNKNOWN.
- [ ] Major concepts have a helpful maintained link, an in-place definition, or a recorded missing-guide gap; former-client examples and current LSS naming follow the publishing rules.
- [ ] Wrong destinations and descriptions have a verified repair or an exact owner handoff.
- [ ] Readback covers changed anchors and targets; reachability is not substituted for meaning.

## Example(s)

**Fictional teaching example. This is not a client result or proof of a completed run.**

A fictional article links “how to set up your library” to a story about one team’s library. The story loads, but it does not teach setup. Change the link only after locating and reading the actual setup guide. A separate vendor link for a supported file limit stays as primary evidence; the owned guide does not establish that limit.

## Handoff and Content Factory context

This work supports the [Content Factory, our four stages of using real content](https://blitzmetrics.com/content-factory/): Produce → Process → Post → Promote. Use the specific inputs and next task below to place the work; a maintenance task does not manufacture transcripts, clips or other stage outputs it does not call for.

The article owner receives the dated link table, confirmed repairs, source sentences, coverage limits and unresolved issues. [Record the article audit result](https://local-service-spotlight.github.io/task-library/?task=update-status-table-in-definitive-article-guide#task-update-status-table-in-definitive-article-guide) receives these link findings when the topic, structure and facts checks are also ready; a link-only pass stays partial.

## Run with an agent

Give the AI worker this recipe, the real Inputs above, the intended result and the actions already authorized. Ask it to return the saved output, checks, evidence and remaining owner. Check its work against this guide; loading a skill does not prove access, installation of a job, or successful execution. Keep media muted with volume at zero if playback is needed.

For recurring work, keep the actual trigger, owner and runtime in the job record. Scheduling and observed firings are separate. Do not create a schedule merely because this guide mentions a review interval.

## Record the real execution

Open the run record when the work starts. Keep the exact starting recipe revision, one execution ID, source evidence and actual state. Write a [meta article, the record of one run](https://blitzmetrics.com/meta-article-prompt/) with decisions, results, checks, failures and next owner. Link it to this task and register it through the [Task Library](https://local-service-spotlight.github.io/task-library/) execution process. Writing is part of the work; public release follows existing authority.

Reuse the same execution ID for revisions, QA, meta writing and retries within that run. A blocked run stays open with its dependency and next owner; do not invent a finish time. Use supported findings to propose and verify a better recipe. A historical public-example count without distinct run IDs remains dated article volume, not verified execution frequency.

## Definitive article & links

- [Maintained source guide](https://blitzmetrics.com/knowledge-system-maintenance/)
- [This task in the Task Library](https://local-service-spotlight.github.io/task-library/?task=validate-cross-reference-integrity-across-articles#task-validate-cross-reference-integrity-across-articles)
- [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [current article guide](https://blitzmetrics.com/definitive-article-guide/)
- [How recipes and run records work together](https://localservicespotlight.com/meta-articles/)

## Review and evidence still needed

The inherited contributor status is `needs-work`. It is preserved, not promoted by this rewrite. That label alone does not verify document readiness, a client outcome, access or an executed task.

A real execution still needs its own source, reviewer, saved result and handoff evidence. The fictional example teaches the method; a real example with relevant proof is still needed where required. The task-specific flow above is source guidance; its visible presentation and the full document need a named reviewer and desktop/mobile checks.
