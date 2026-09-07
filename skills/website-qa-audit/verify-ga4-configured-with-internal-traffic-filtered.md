---
name: verify-ga4-configured-with-internal-traffic-filtered
description: "Keep team visits from skewing site reports. Check the right data source and test the filter with care."
category: Website QA Audit
stage: —
definitive_article: /website-qa-audit
status: complete
---

# Verify GA4 configured with internal traffic filtered

Your own visits can change the numbers in a site report. This guide helps you check how team traffic is marked and kept out. Start with the right account and the real rule the team uses.

**The path:** Right property → Real events → Tested internal rule → Verified report state.

**Use this when:** A site’s Google Analytics 4 measurement and internal-traffic treatment need verification. GA4 is the site’s visitor/event reporting tool.

## Inputs
- The canonical site, expected GA4 property/web stream and measurement IDs from the actual measurement plan.
- Read access for checks and appropriate Editor access for authorized filter changes; supported tag/container configuration access as needed.
- Approved current internal network definitions and controlled internal/external test sessions, kept in the private project record.
- Existing filter state, event/consent requirements, change scope and a dated before-state snapshot.

## First-run prompt

> Use the supplied measurement plan, GA4 access and authorized filter scope. Verify actual event destinations and internal/external classification, preserve Testing until the real evidence supports an authorized activation, and return exact state and gaps without exposing private networks or bypassing consent.

## Steps
1. Confirm the intended property and stream IDs against the project plan and served implementation. Multiple streams or a multi-domain setup can be legitimate; investigate unexpected duplicate event delivery rather than enforcing exactly one web stream per property.
2. Trace an authorized controlled visit to an actual received event using the supported tools. Record the page, consent state, measurement destination and timestamp. A tag found in HTML or fired in a preview does not alone prove that this property received the event.
3. Inspect the actual internal-traffic rule and its traffic_type value. Check relevant current IPv4/IPv6 ranges or the approved alternative classification method. A home/office IP list will not automatically cover travel, changed networks or every remote team member.
4. Record whether the data filter is Testing, Active or Inactive. For a new or changed rule, use the documented Testing state to verify classification before an authorized activation. Active exclusions permanently remove matching incoming data from processing; they do not clean old reports.
5. Use controlled internal and external sessions to check the intended classification. In Testing, the Test data filter name dimension in an exploration provides evidence while retaining the data. Allow documented processing delay; immediate absence in Realtime alone cannot prove a correct exclusion.
6. If activation is part of the already-authorized measurement change and the test demonstrates the correct scope, apply it and record the exact filter state. Otherwise keep the tested/pending state truthful; do not activate merely to make the checklist green.
7. Check the continuing expected external event flow and any observed internal behavior with timestamps and consent context. DebugView can be affected by privacy/consent settings; do not disable those controls to force an event through. Label delayed or unavailable evidence as pending.
8. Save configuration and test evidence privately, then report coverage and remaining gaps without exposing team IPs or personal test data. Recheck authorized changes using actual received/report evidence rather than a missing dot in Realtime.

## Definition of done (QA checklist)

- [ ] The intended property/stream and actual received events are identified without a false one-stream requirement.
- [ ] Internal rules match the real approved network/classification scope and unknown coverage is stated.
- [ ] Testing and Active are separate states; permanent exclusions are activated only within the actual authorized change after evidence.
- [ ] Internal/external test evidence and processing delay are recorded without using absence alone as proof.
- [ ] Consent controls and private team/network details are preserved.

## Example(s)

**Fictional teaching example — no Analytics account was changed.** Maple Cycle’s team works from an office and a changing mobile hotspot. The sample rule covers the office network only.

A controlled office session receives the test-filter label in the expected exploration; an external session does not. The hotspot coverage remains unknown until its approved classification is defined. That result supports the office rule, not a claim that all team visits are excluded.

If the filter is still Testing, the report says so. A zero in Realtime is not enough reason to activate permanent exclusion or claim the old reports were cleaned.

## Handoff and Content Factory context

The measurement owner receives private configuration evidence and remaining classification work. [Verify the tag container](https://local-service-spotlight.github.io/task-library/?task=verify-gtm-installed-and-firing-on-every-page#task-verify-gtm-installed-and-firing-on-every-page) is relevant if GTM actually delivers these tags; direct supported Google-tag setups are not automatically failures.

This is a supporting quality check for the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at initial measurement QA and after relevant stream, tag, consent, filter or team-network changes. Repeated work needs a defined state source and actual trigger; no automatic IP-change detection is promised.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Canonical article: https://blitzmetrics.com/website-qa-audit
- Exact task: [Verify GA4 configured with internal traffic filtered](https://local-service-spotlight.github.io/task-library/?task=verify-ga4-configured-with-internal-traffic-filtered#task-verify-ga4-configured-with-internal-traffic-filtered)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Website QA Audit](https://blitzmetrics.com/website-qa-audit/)
- [Google Analytics internal-traffic filters](https://support.google.com/analytics/answer/10104470?hl=en)
- [Google Analytics DebugView](https://support.google.com/analytics/answer/7201382?hl=en)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Actual account access, approved internal classification, activation scope and received/report evidence require the project.
