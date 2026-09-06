---
name: provide-knowledge-capture-note-template
description: Make a short form that helps your team save and use a lesson from its work.
category: Knowledge System Maintenance
stage: —
definitive_article: /knowledge-system-maintenance
status: gap
---

# Provide Knowledge Capture Note template

Help your team save lessons before they get lost. Use this guide to make a short note form with one filled example. Start with a real lesson from a call, a campaign, or a task.

## Inputs
- The maintained four-field method in the [knowledge system guide](https://blitzmetrics.com/knowledge-system-maintenance/): source, insight, destination and priority.
- One real lesson with a dated source you can check.
- The shared capture location and permission to save the template. Identify its owner and one person or agent who will use it.

## First-run prompt
> Make a one-page lesson form with exactly four fields: source, insight, destination and priority. Use this real lesson: [source and lesson]. Add one short hint per field and a filled example. Show any missing facts. Save it in [shared location] within my existing instructions, then check that the next user can read it.

## Steps
1. Make the blank form with exactly four fields. Under Source, ask for a dated link or record and who supplied it. Under Insight, ask what was learned in one to three sentences. Under Destination, ask which current guide or task should use it. Under Priority, ask how soon it needs attention.
2. Fill a second copy with one real lesson. Keep the source link and distinguish the observed fact from a proposed fix. Do not invent a date, result, person or destination.
3. Keep the form and hints to one page at normal reading size. Open the actual file to check it; a word-count guess does not prove the layout.
4. Save one canonical copy in the shared capture location. Link to it from the maintained knowledge guide under the existing publishing authority. Copies should identify their source and revision.
5. Have the receiving user or agent open the saved form. Record the location, source revision and read-back result. A local file that the receiver cannot reach is not a shared template.
6. Hand the template, filled example and access check to the distribution task below. That task owns rollout and the later adoption check.

## Definition of done (QA checklist)
- [ ] The blank form has exactly four fields and one useful hint per field.
- [ ] The filled example has a real dated source and a one-to-three-sentence insight.
- [ ] The form fits one readable page; the saved copy and source link open.
- [ ] The receiving owner can read the canonical copy; missing access is recorded honestly.
- [ ] The knowledge guide points to the canonical copy, or publication is explicitly pending.
- [ ] The distribution handoff names the next owner and the later adoption check.

## Example(s)
**Worked example from this Task Library review, 6 September 2026.** This records a source finding; it does not claim a repaired release or a completed rollout.

| Field | Filled example |
|---|---|
| Source | The all-task ZIP builder in [Task Library commit 02ea7b3](https://github.com/Local-Service-Spotlight/task-library/blob/02ea7b3d2d981b7011cdd48afb64ec7a4bf3a953/build/build.py), reviewed on 6 September 2026 by Codex for this audit. |
| Insight | That builder writes guide files and a manifest but no first-start file. A new user needs a clear first job, required files and access, and a way to check one result. |
| Destination | The Task Library ZIP builder and its START-HERE instructions. |
| Priority | Before the next ZIP release; people are already being directed to download it. |

The record supports the missing-start-file finding at that source revision. It does not prove that every user got stuck or that any business lost revenue.

## Handoff
[Share the template and check adoption](https://local-service-spotlight.github.io/task-library/?task=create-knowledge-capture-note-template-and-distribute#task-create-knowledge-capture-note-template-and-distribute) receives the canonical file, filled example and access proof. Review the first real notes during that rollout. Keep proposed form changes in the normal amendment process.

## When it runs
Run when the team lacks a usable shared form. The authoring result is the checked template and handoff. The later two-week adoption review belongs to the distribution task; downloading this guide does not schedule it.

## Using this guide with AI
A guide is a set of steps. Ask an AI worker to use it with the files for this job. Confirm it can read the files and save the result where the next owner can find it. Use the existing authority for the work; identify the exact missing grant before an action outside that scope.

For repeat work, agree on the trigger, time zone, runtime and receiving owner. Check one run before relying on the schedule. The guide itself does not create a schedule, access or shared memory.

Record the actual work in a [meta article: the run record and its proof](https://blitzmetrics.com/meta-article-prompt/). Keep one execution ID for the same run and its retries. A teaching example does not add a completed run.


## Definitive article & links
- Method: [How the knowledge system learns](https://blitzmetrics.com/knowledge-system-maintenance/)
- [This exact Task Library task](https://local-service-spotlight.github.io/task-library/?task=provide-knowledge-capture-note-template#task-provide-knowledge-capture-note-template)
- [Writing and visual guidelines](https://localservicespotlight.com/article-guidelines/)
