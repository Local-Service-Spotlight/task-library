---
name: step-10-embed-source-video
description: "Put the real source video beside your article. Make it clear, easy to view, and ready for captions."
category: Content Factory — Process
stage: Process
definitive_article: https://localservicespotlight.com/article-guidelines/
status: complete
---

# Step 10: Embed source video

Some readers want to see the person behind the words. This guide adds the real source video to your article. Start with the correct video and the page’s current editor.

**The path:** Verified video → Supported page embed → Caption and layout checks → Source links.

**Use this when:** A video-based article has an embeddable source and needs an actual playable player in the supported page source.

## Inputs
- The actual source video ID/URL, host/channel, rights and intended visibility.
- The article’s canonical record and supported editor or builder source, plus existing embed if present.
- Available captions/language, source context and the content tracker linking the assets.
- Already-authorized edit/publication scope and the next proofreader.

## First-run prompt

> Embed the exact authorized source video in the page’s supported editor or builder. Preserve its URL and source type. Use the actual caption/default policy, no autoplay, and silent player checks. Verify phone/desktop layout and record which reciprocal links and public states are actually complete.

## Steps
1. Verify the source video matches the article and its host allows embedding at the intended visitor visibility. Prefer the brand’s own hosted source when available and appropriate, but an original third-party interview can be embedded with permission; do not reupload someone else’s media merely to make the channel ours.
2. If hosting is needed, hand the actual source and scope to [Upload the video to YouTube](https://local-service-spotlight.github.io/task-library/?task=upload-processed-video-to-youtube#task-upload-processed-video-to-youtube). Keep this embed pending until a suitable host/player is available. Upload visibility and public article publication are distinct decisions.
3. Inspect the current page source. Use its supported block, builder or existing component; preserve the canonical Page/builder and URL. Do not convert it to Gutenberg solely because a legacy task demanded it.
4. Place the real player near the introduction or section it supports and add short context naming the speaker and lesson. A watch link, thumbnail or transcript panel alone is not an embedded player.
5. Apply [YouTube captions by default](https://local-service-spotlight.github.io/task-library/?task=enable-youtube-captions-by-default#task-enable-youtube-captions-by-default) through the existing supported helper/filter or explicit embed. Use the verified ID and page language, privacy-enhanced host where supported, cc_load_policy=1, cc_lang_pref, rel=0 and autoplay=0. rel=0 limits related videos to the same channel; it does not disable all suggestions.
6. Check that actual captions exist. The default parameter cannot create a missing track. Keep agent previews muted at volume zero; inspect player state, captions and frames without claiming audio playback.
7. Check actual desktop and phone layout, aspect ratio and initial visible content. Do not assume generic lazy-loading behavior; a lead asset that remains hidden or empty fails. Preserve the source’s portrait/landscape shape.
8. Connect article and video in the tracker. Add a live article link to an editable authorized video description when available; otherwise note that reciprocal edit as pending. Do not claim control of a third-party description.
9. Save through the supported route, record actual preview/public state and hand source/player evidence to proofreading. A draft embed check is not proof that the public canonical page has updated.

## Definition of done (QA checklist)

- [ ] The actual source player matches the article and has permitted use/visibility.
- [ ] Existing supported page/builder source and URL are preserved.
- [ ] Caption defaults and actual track availability are distinguished; no first-load autoplay is added.
- [ ] Phone/desktop layout and actual cross-link state are recorded without a false public or audio pass.

## Example(s)

**Fictional teaching example — no real video ID or embed.** The sample repair-quote article has a six-minute source hosted by the shop. The editor records the real ID from that project, places its player after the short opening and captions the context: “The mechanic shows the three details that help us prepare.”

If the article is still a draft, the tracker says “player verified in draft; public article link pending.” If a permitted interview is on the host’s channel, the editor embeds that original and records that the host controls its description. Neither case justifies a copied upload or a made-up video ID.

## Handoff and Content Factory context

The proofreader gets the article, source player and real verification limits for [Step 11: proofread the complete draft](https://local-service-spotlight.github.io/task-library/?task=step-11-proofread-with-grammarly-or-chatgpt#task-step-11-proofread-with-grammarly-or-chatgpt).

Produce supplies the real source. **Process**, this stage of the [Content Factory](https://blitzmetrics.com/content-factory/), turns it into useful finished assets. Post saves or publishes them on the agreed channels. Promote tests and distributes suitable work within its own scope. The handoff above names this task’s actual next step; catalog neighbors alone are not prerequisites.

## When this runs

Once per article embed or source-video replacement. Recheck after an actual player/template policy change.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://localservicespotlight.com/article-guidelines/
- Exact task: [Step 10: Embed source video](https://local-service-spotlight.github.io/task-library/?task=step-10-embed-source-video#task-step-10-embed-source-video)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Task recipe and publishing standard](https://blitzmetrics.com/definitive-article-guide/)
- [Our YouTube caption-default method](https://blitzmetrics.com/youtube-captions-on-by-default/)
- [YouTube’s documented player parameters](https://developers.google.com/youtube/player_parameters)
- [YouTube’s current upload controls](https://support.google.com/youtube/answer/57407?hl=en)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual host rights, caption availability and rendered player need real source access; no example player was created.
