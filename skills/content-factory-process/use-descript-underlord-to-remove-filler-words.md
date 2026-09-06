---
name: use-descript-underlord-to-remove-filler-words
description: "Trim speech that gets in the way. Keep words and pauses that help the speaker sound natural."
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Use Descript Underlord to remove filler words

Too many stray words can slow a good story. This guide helps you trim them without changing what the person says. Start with a checked transcript and keep a copy of the source cut.

**The path:** Source cut → Review each filler → Selective edits → Checked natural cut.

**Use this when:** A transcribed recording has distracting filler speech and the requested edit includes a cleaner working cut.

## Inputs
- The speaker-labeled source transcript, original recording and a separate editable composition.
- Descript access to the filler tool or Underlord with actual available credits/role; current automatic filler detection supports English.
- The intended tone, source limits and a place to log removed/retained moments.
- An authorized way to review speech quality without playing sound through the user’s speakers.

## First-run prompt

> Review fillers in this separate Descript work copy. Preserve meaningful words and the original source. Choose edit modes deliberately, inspect each boundary, and record removals and retains. Keep speakers silent and state any missing audio-quality review. Do not regenerate the speaker’s words or consume new unapproved tools.

## Steps
1. Keep the original composition and transcript. Create a working copy for filler editing so the factual source is not overwritten.
2. Read representative passages first. Decide whether fillers actually obstruct the message. A natural pause or emotional phrase can be useful; a cleaner waveform is not the goal.
3. Open AI Tools → Remove filler words, or ask Underlord for the equivalent bounded pass on the work copy. Review available usage before consuming it. If the tool cannot support the source language or role, use a reviewed manual edit instead of pretending it ran.
4. Review each detected instance in context. Preserve a real comparison such as “a bike like this.” The detector can flag meaningful words, so do not apply all suggestions blindly.
5. Choose the intended edit behavior. Delete removes text and audio; replace with gap preserves timing. Ignore also removes the audio despite retaining struck text. Remove from transcript leaves the audio in place. Select the operation that actually matches the goal.
6. Use Avoid harsh cuts when available, then check affected boundaries. Restore or loosen a cut that clips a syllable or harms meaning. Do not generate replacement speech as an unnoticed repair to a first-hand source.
7. Review cadence and source accuracy with authorized audio evidence, keeping agent speaker output silent. Frames and captions alone cannot certify natural sound. If that review is unavailable, mark audio-quality review pending and keep the original recoverable.
8. Save the working cut and export/reference it as requested. Log the actual reviewed, removed and intentionally retained instances, output version and remaining checks. Point downstream editors at the correct cut while retaining the original source clock.

## Definition of done (QA checklist)

- [ ] The original recording/transcript are retained separately.
- [ ] Every applied removal was reviewed for meaning and the correct edit mode.
- [ ] Speech/cadence review is evidenced or explicitly pending; automatic harsh-cut avoidance is not proof by itself.
- [ ] The final cut, original source mapping and intentional retains are recorded.

## Example(s)

**Fictional teaching example — no audio was edited.** A sample sentence is “Um, a bike like this needs a close look.” The editor proposes removing the opening “Um” and keeping “like this,” which carries meaning.

At another cut, the start of “needs” is clipped. The editor restores the boundary rather than making a synthetic replacement voice. A sample review log says “2 proposed removals; 1 kept; 1 applied; audio review pending.” It does not say “natural sound passed” from reading the text alone.

## Handoff and Content Factory context

The clip editor receives the checked cut and source map for [Extract short clips](https://local-service-spotlight.github.io/task-library/?task=extract-15-60-second-clips-from-long-form-video#task-extract-15-60-second-clips-from-long-form-video). The article writer can use the faithful transcript; filler removal is not a mandatory prerequisite for all writing.

Produce supplies the real source. **Process**, this stage of the [Content Factory](https://blitzmetrics.com/content-factory/), turns it into useful finished assets. Post saves or publishes them on the agreed channels. Promote tests and distributes suitable work within its own scope. The handoff above names this task’s actual next step; catalog neighbors alone are not prerequisites.

## When this runs

A single requested cleanup pass per recording/cut. Recheck changed sections after later edits; do not strip every new source automatically.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://localservicespotlight.com/article-guidelines/
- Exact task: [Use Descript Underlord to remove filler words](https://local-service-spotlight.github.io/task-library/?task=use-descript-underlord-to-remove-filler-words#task-use-descript-underlord-to-remove-filler-words)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Descript filler-word choices](https://help.descript.com/script-editing/filler-words)
- [Descript media minutes and AI credits](https://help.descript.com/hc/en-us/articles/27841674958221-Track-and-understand-your-Media-minutes-and-AI-Credits)
- [Descript composition copies](https://help.descript.com/hc/en-us/articles/10612359826061-Duplicating-a-composition)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Real tool access, removals and sound-quality review need the actual project.
