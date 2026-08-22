---
name: write-meta-article-documenting-agent-work
description: Turn an authorized, public-safe, reusable task run into a Meta Article linked to its governing Definitive Article.
category: Content Factory — Process
stage: Process
definitive_article: /meta-article-prompt
status: complete
---

# Write meta-article documenting agent work

**Use this when** an AI agent (or human + agent) has completed a real task run and the run has passed the publication gate: it is authorized for public release, contains no secret or private material, teaches a reusable lesson, and has a governing Definitive Article to link to. Every substantive organization job still gets a private internal receipt; most runs do not need a public page.

## Inputs
- The private internal run receipt: owner, timestamp, scope, evidence, outcome, failures, and next action
- The approved public evidence from the completed run: safe prompts, tool outputs, before/after states, and final deliverable
- The Meta-Article Prompt (the hub at /meta-article-prompt)
- The task's definitive article short URL (the hub this example will link up to)
- Explicit publication approval or standing authority for this class of public-safe work
- WordPress access only when the current authority explicitly includes publishing

## Steps
1. Write or verify the private internal run receipt first. This preserves the work even when no public article is appropriate.
2. Apply the publication gate. Confirm authorization, public safety, reusable value, and the parent Definitive Article. If any condition fails, stop the public path, record why in the private receipt, and do not draft or publish a Meta Article.
3. Gather only the approved public artifacts while fresh: safe prompts, key decisions, screenshots of before/after, the output, time taken, and honest friction.
4. Run the Meta-Article Prompt against those artifacts to draft the article: what the task was, why it was run, what the agent actually did step by step, and what resulted.
5. Show the real work without exposing credentials, private-source links, client-confidential facts, or internal-only evidence. The value is reproducibility, not a polished success story.
6. State results concretely: what shipped, what changed, and what was measured. Preserve UNKNOWN when measurement is unavailable.
7. Link the Meta Article UP to its Definitive Article. Never write it as a competing explanation of the concept; it documents one run.
8. Apply the entity-linking decision tree for every person, company, and concept mentioned.
9. Publish only under the approved authority and per the Blog Posting Guidelines pipeline (title <60, meta <160, keyword in first paragraph, real screenshots as images, RankMath 70+ at the Post stage).
10. Register the public example on the Definitive Article and Task Library tracker. Internal-only receipts remain registered only in the approved private system.

## Definition of done (QA checklist)
- [ ] Private internal receipt exists and the public/private decision is recorded
- [ ] Publication gate passed: authorized, public-safe, reusable, and linked to a governing hub
- [ ] Documents one real run with approved prompts and honest results — no hypotheticals
- [ ] Contains no secret values, private-source links, client-confidential facts, or unapproved personal data
- [ ] Links up to the task's definitive article; does not compete with the hub
- [ ] Concrete outcomes stated; unavailable measurements remain UNKNOWN
- [ ] Complies with Blog Posting Guidelines (it publishes content)
- [ ] Example registered on the hub's examples list and in the tracker
- [ ] Linked back to the definitive article and relevant siblings

## Example(s)
- The hub at /meta-article-prompt carries the maintained examples list for this loop.

## Run on a persistent agent

Do not run this automatically after every skill. Every substantive organization job writes its private receipt. Invoke this task only when the completed run passes the publication gate; stop at an approved draft unless the current authority explicitly includes publishing. After publication, verify the live URL and register the example. An internal-only run is complete when its private receipt and reusable-learning decision are recorded.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /meta-article-prompt
- Related: /blog-posting-guidelines (publishing pipeline), /internal-linking (its hub ships a skill file — a documented precedent), /knowledge-system-maintenance (capture loop)
- Sibling skills, in run order: completed task run → private receipt → publication gate → this skill when approved → `step-12-post-article-on-wordpress` (Post stage)
