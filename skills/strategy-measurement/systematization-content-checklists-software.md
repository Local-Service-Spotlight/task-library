---
name: systematization-content-checklists-software
description: Move any recurring task up the Systematization ladder — from documented content, to a checklist anyone can run, to software/agent automation — so quality stops depending on memory.
category: Strategy & Measurement
stage: —
definitive_article: /9-triangles-framework-scalable-home-service-businesses/
status: complete
---

# Systematization (Content → Checklists → Software)

**Use this when** a task is done repeatedly but lives in someone's head, results vary by who does it, or you're correcting the same mistake for the third time.

## Inputs
- One recurring task that currently runs ad-hoc
- The person who does it best (their walkthrough is the raw material)
- A home for the artifacts: the definitive article hub and the Task Library skills folder

## Steps
1. Define the ladder: **Content** (the knowledge is written down once, canonically), **Checklists** (the knowledge becomes numbered steps with pass/fail criteria), **Software** (the stable steps run automatically). Never skip a rung — automating an undocumented process automates the errors.
2. **Content:** record the best operator doing the task while narrating; turn it into (or fold it into) the concept's definitive article so there is one canonical write-up, not competing versions.
3. **Checklists:** extract the SOP into a skill.md per the Task Library Standard — inputs, imperative steps, and a Definition-of-done checklist an agent or new hire can run without asking questions.
4. Run the checklist manually at least three times with different operators; every question they ask is a missing step — edit the checklist until runs are question-free.
5. **Software:** automate only the steps that survived unchanged across runs (e.g., agent runs the skill.md, scripts handle the repetitive parts); keep judgment steps human until they stabilize.
6. Measure it: track time-per-run, error/rework rate, and what fraction of runs are done by someone other than the original expert — all three should improve as the task climbs the ladder.

## Definition of done (QA checklist)
- [ ] The task has a single canonical write-up on its definitive article (no competing docs)
- [ ] A skill.md exists with inputs, steps, and an objective Definition-of-done
- [ ] Checklist validated by 3+ runs, including by someone other than the expert
- [ ] Stable steps automated or assigned to an agent; judgment steps explicitly flagged
- [ ] Time-per-run and rework rate baselined and tracked
- [ ] Linked back to the definitive article and relevant siblings
- [ ] Complies with Blog Posting Guidelines (if it publishes content)

## Example(s)
- Example needed — run the Meta-Article Prompt after first real run. (The Task Library itself — definitive article → skill.md → examples — is this triangle applied to Local Service Spotlight' own SOPs.)

## Run on a persistent agent (Fable 5)

This triangle is what a persistent, max-effort agent (Claude Fable 5 or comparable OpenAI/Google models) embodies: it drafts the canonical write-up, extracts the skill.md, then runs the checklist itself repeatedly — treating every question it has to ask as a missing step — and loops until the Definition of done fully passes, including validated runs by operators other than the expert.
It self-verifies by re-running the finished checklist cold and refusing to mark Software-rung steps automated until they survive unchanged across runs.
Memory baselines time-per-run and rework rate and compares them against prior periods in the MAA loop — a true memory cycle — with a meta-article example logged each run.
See `boil-the-ocean.md` for the full operating principles.

## Definitive article & links
- Hub: /9-triangles-framework-scalable-home-service-businesses/
- Related: management-communicate-iterate-delegate, learn-do-teach-apprentice-model, /content-factory
