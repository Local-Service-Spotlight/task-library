---
name: step-2-transcribe-video-using-descript
description: "Turn speech into checked text. Fix names and words so the article says what the speaker meant."
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 2: Transcribe video using Descript

A wrong word can change your whole story. This guide helps you turn a video into text you can trust. Start with the full source and a list of the people who speak.

**The path:** Full source → Draft transcript → Word and speaker checks → Verified text or clear gaps.

**Use this when:** The source is imported into the correct Descript project and needs a faithful transcript.

## Inputs
- The completed source composition from [Step 1](https://local-service-spotlight.github.io/task-library/?task=step-1-upload-video-to-google-drive-and-descript#task-step-1-upload-video-to-google-drive-and-descript) and access to the original recording.
- A Descript role and usage balance that permit transcription for the source language; confirm actual plan support rather than assuming an Enterprise subscription.
- Verified names, companies, places and specialist terms from project records, plus known speaker identities.
- A place to save the original transcript, corrections, unclear timestamps and review coverage.

## First-run prompt

> Make or review the transcript for this exact source. Use text-correction mode, preserve the media, and check speaker names, numbers and negatives. Keep source versions and timestamp every uncertainty. Report actual review coverage; never call blue-underlined words a complete error list or claim an audio review you did not perform.

## Steps
1. Confirm the source is in the script and select the correct language when transcription is requested. Let the job finish. Check whether a transcript already exists before consuming usage again.
2. Save the initial transcript as a source version. Identify each speaker from actual evidence. If identity is unknown, mark it unresolved in the working transcript; do not assign a famous name by guess.
3. Use Descript’s Correct text action for transcription mistakes. Ordinary text deletion can cut the underlying video; correction mode fixes the words without making that media edit.
4. Check names, numbers, negatives and technical terms against the source. Use the verified spelling list for identity, but do not replace a different spoken person merely because a familiar name is in that list.
5. Review the whole recording and transcript with an authorized speech-review method. Agents keep speaker output muted; if no suitable silent audio analysis or prior reviewer evidence exists, retain the exact unverified intervals for that review. Do not claim a listen-through from a skim or frames.
6. Do not use blue underlines as an accuracy score: current Descript uses light-blue marks for fillers and also has separate alignment/error indicators. Check unmarked words too. Mark unclear speech with its timestamp instead of inventing a clean sentence.
7. Keep this transcript faithful to the recording. Put later summary, grammar edits and filler cuts in a separate working version. Do not generate replacement speech to make an uncertain quote sound correct.
8. Save the checked version with source ID, language, speaker map, review coverage and remaining uncertainties. Only label it verified to the extent supported, then send it to GCT review.

## Definition of done (QA checklist)

- [ ] The transcript covers the full source with correct language and evidence-backed speaker labels.
- [ ] Names, numbers, negatives and quotations are checked against the recording, with unclear spans flagged.
- [ ] Text corrections have not silently changed the source media.
- [ ] Review coverage and remaining gaps are recorded; zero colored underlines is not the acceptance test.

## Example(s)

**Fictional teaching example — no transcript was processed.** The sample audio says, “We do not give a final quote from one photo.” The draft transcript drops “not.” The reviewer restores that word with Correct text and keeps the source video unchanged.

At 02:18, “gear hanger” is unclear. The working row records `02:18 — term unresolved; ask source reviewer`, rather than silently changing it to a familiar part. A transcript with this gap may support other checked passages, but cannot support a precise quote of that term. Blue filler marks on “um” do not alter this decision.

## Handoff and Content Factory context

The writer receives checked text and explicit source-review gaps for [Step 3: review the source and set GCT](https://local-service-spotlight.github.io/task-library/?task=step-3-watch-video-and-identify-gct#task-step-3-watch-video-and-identify-gct). Filler editing is optional and uses a separate cut.

Produce supplies the real source. **Process**, this stage of the [Content Factory](https://blitzmetrics.com/content-factory/), turns it into useful finished assets. Post saves or publishes them on the agreed channels. Promote tests and distributes suitable work within its own scope. The handoff above names this task’s actual next step; catalog neighbors alone are not prerequisites.

## When this runs

Once per source transcript. Recheck the affected spans when the recording or transcript changes; do not retranscribe every retry.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://localservicespotlight.com/article-guidelines/
- Exact task: [Step 2: Transcribe video using Descript](https://local-service-spotlight.github.io/task-library/?task=step-2-transcribe-video-using-descript#task-step-2-transcribe-video-using-descript)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Descript transcript corrections](https://help.descript.com/hc/en-us/articles/23054692507661-Unable-to-toggle-capitalization-or-punctuation-on-Windows)
- [Descript text edits and media](https://help.descript.com/hc/en-us/articles/10164808475149-Inline-notes)
- [Descript filler-word choices](https://help.descript.com/script-editing/filler-words)
- [Descript media minutes and AI credits](https://help.descript.com/hc/en-us/articles/27841674958221-Track-and-understand-your-Media-minutes-and-AI-Credits)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Real speech accuracy and identity need source review; unsupported language/usage or inaudible passages remain explicit.
