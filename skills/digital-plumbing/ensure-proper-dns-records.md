---
name: ensure-proper-dns-records
description: "Check the records that route your website and email. Fix the wrong ones and keep a clear change log."
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: needs-work
---

# Ensure Proper DNS Records

Your web address needs to lead to the right site and mail service. This guide helps a business owner check those routes. Start with the live services you use and a copy of the current records.

**The path:** Service map → DNS plan → Scoped change → Public resolution.

**Use this when:** a domain is taken over, a host or mail service changes, or a routing defect is suspected.

## Inputs
- The actual authoritative DNS provider, registrar and domain scope from [verify domain ownership and registrar access](https://local-service-spotlight.github.io/task-library/?task=verify-domain-ownership-and-registrar-access#task-verify-domain-ownership-and-registrar-access).
- Current web host targets, required hostnames, mail routing design and active service-verification requirements from the real providers.
- Supported DNS editing access or the named DNS owner, a zone export and a rollback plan. Public records may still include sensitive infrastructure context; store full exports in the approved project record.

## First-run prompt

> Compare the authorized domain’s DNS records with its actual services. Prepare or apply only the scoped fixes using the supported provider route. Preserve uncertain records and existing mail routing until their purpose is established. Verify public results and document each change.

## Steps
1. Confirm where DNS is authoritative; the registrar may be a different service. Export the current zone with record names, types, values and TTLs, which control how long answers may be cached. Record the change owner and recovery route.
2. Map each intended hostname to the provider’s required record. A records name IPv4 addresses, AAAA records name IPv6 addresses, and CNAME records alias another name. Apex alias features vary by DNS provider. Do not force a www hostname that the approved design does not use.
3. Compare the web records with the actual host configuration. With a proxy or content delivery service, public addresses may correctly be proxy addresses rather than the origin. Fix stale A and AAAA paths together where relevant; changing one does not repair the other.
4. Check MX records against the actual mail design, including intentional routing gateways or migration arrangements. Multiple MX records can be normal. Do not delete one merely because it is not the mailbox brand’s default.
5. Check active TXT and other verification records against current service needs. Preserve valid ownership tokens and mail policy. Use the email-authentication task for SPF, DKIM and DMARC details rather than merging unrelated TXT text.
6. For a suspected obsolete record, identify its service and owner first. Classify uncertain records for review. Remove only a confirmed retired record within the authorized change scope; this task does not test whether another party can claim a service or bypass any access control.
7. Apply the minimal supported edit with its before value and time. Check authoritative answers and ordinary recursive resolution after the relevant caches expire. Record resolver and observation time; a saved DNS panel is not proof of public propagation.
8. Verify the affected public website or controlled mail path as included in the job. Save the final purpose-per-record map, exact change list and any pending cache or receiver checks. Revert through the approved recovery route if the planned service check fails.

## Definition of done (QA checklist)

- [ ] Authoritative DNS and registrar roles are identified correctly.
- [ ] Web and mail records match the actual approved design, including legitimate proxies and gateways.
- [ ] No unknown record was removed based on a guess.
- [ ] Changed records have before/after evidence and public resolution checks with timestamps.
- [ ] Affected service checks pass or have precise pending limits; the final record-purpose map is saved.

## Example(s)

**Fictional teaching example.** A zone has a web A record, a stale AAAA record and two valid mail MX records. The provider confirms the old IPv6 route was retired. The scoped change removes that AAAA record and preserves both MX routes. The lesson compares the authoritative answer and a recursive answer after their recorded TTLs. It does not declare every resolver worldwide updated, and it does not probe a retired service for takeover.

## Handoff and Content Factory context

Give the DNS map to the domain owner. Continue with [configure https with no mixed content](https://local-service-spotlight.github.io/task-library/?task=configure-https-with-no-mixed-content#task-configure-https-with-no-mixed-content) for web delivery or [configure spf dkim dmarc for deliverability](https://local-service-spotlight.github.io/task-library/?task=configure-spf-dkim-dmarc-for-deliverability#task-configure-spf-dkim-dmarc-for-deliverability) for sender authentication, according to the actual changed service.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run after approved routing changes or a reported defect. Optional periodic comparisons need a stored known-good zone and configured read-only trigger; no automatic deletion of newly found records.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. Use the maintained owned training below until that article gap is reviewed.
- Exact task: [Ensure Proper DNS Records](https://local-service-spotlight.github.io/task-library/?task=ensure-proper-dns-records#task-ensure-proper-dns-records)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [DNS record types in Cloudflare documentation](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Dedicated canonical article is missing. Provider targets, zone access and the exact service checks must be supplied for a real run.
