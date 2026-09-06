---
name: configure-spf-dkim-dmarc-for-deliverability
description: "Help real mail from your business pass sender checks. Test each mail service you use."
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: needs-work
---

# Configure SPF/DKIM/DMARC for Deliverability

Do your real emails land in spam? This guide helps a business owner set up checks that show who sent the mail. Start by listing each service that sends mail for your business.

**The path:** Sender list → DNS records → Received headers → Policy review.

**Use this when:** domain email is new, a sender is added, messages fail authentication, or the business reviews its email protection.

## Inputs
- The real sending services, visible From domains and envelope-sender domains, including forms and customer-management tools.
- Access to the authoritative DNS zone and each sender’s domain settings; existing records, policy and rollback evidence. Keep secrets in the approved store, not this guide.
- A controlled receiving inbox and authorized test scope for each service, plus an approved destination and owner for any aggregate DMARC reports.

## First-run prompt

> Map actual senders and existing mail-authentication policy. Prepare or apply the authorized provider-specific SPF, DKIM and DMARC changes. Test controlled messages at a receiver and report alignment and delivery separately. Do not weaken an existing policy or send a campaign as a test.

## Steps
1. Inventory each sending service, its From domain, envelope domain and DKIM signing domain where known. Read the current records first. An unused guessed service must not be added just because it appears in a generic setup example.
2. SPF is the sender list checked against the envelope domain. Publish one SPF TXT policy per applicable DNS name using the actual providers’ current instructions. Preserve valid senders and verify recursive DNS-query terms stay within the SPF limit of ten; ten visible include entries is not a safe shortcut.
3. DKIM is a signed-mail check. In each provider, obtain its public selector record and follow its exact TXT or CNAME instructions. Keep private signing keys private. Confirm the public record resolves, then enable signing in the provider where that separate step is required.
4. DMARC checks whether a passing SPF or DKIM identity aligns with the visible From domain. Read the existing DMARC policy before editing it. Preserve an established enforcement policy; do not automatically replace it with p=none.
5. For a new policy, choose the authorized monitoring or enforcement plan based on actual sender readiness. A p=none policy requests no DMARC enforcement; the optional rua field requests aggregate reports. Add aggregate reports only to an approved receiving destination, accounting for the information those reports disclose.
6. Send clearly marked controlled messages through each in-scope service to the agreed receiver. Inspect Authentication-Results and the relevant domains. A message can pass DMARC through aligned DKIM even when SPF fails after forwarding; inspect the cause instead of declaring every such message broken.
7. Check whether each test reached the intended inbox, spam folder or failed delivery. Authentication helps establish sender legitimacy but does not guarantee inbox placement. Use real receiver evidence, not merely a saved DNS screen.
8. Save a sender-by-sender result table and exact changed public records. Review report coverage and legitimate failures before any later policy change; no fixed number of weeks guarantees safe enforcement. Route unresolved sender configuration to its actual owner.

## Definition of done (QA checklist)

- [ ] The sender inventory covers all known in-scope services and applicable domains.
- [ ] SPF is syntactically valid, single per name and within lookup limits; DKIM signing is actually enabled where applicable.
- [ ] DMARC policy and report handling match the authorized plan, with existing protections preserved.
- [ ] Each tested service has receiving-header alignment evidence and a separate delivery result.
- [ ] Untested services, propagation state and policy follow-up have named owners; no campaign was sent as a test.

## Example(s)

**Fictional teaching example.** Oak Repair uses a mailbox service and a quote tool. A lesson test from the mailbox has aligned SPF and DKIM, so DMARC passes. The quote tool passes SPF for the vendor’s domain but has no aligned DKIM; DMARC fails for Oak Repair’s From address. The useful next action is to configure that tool’s supported domain signing, not add a second SPF record or weaken DMARC. These are invented teaching results, not real messages or a ready-to-paste DNS policy.

## Handoff and Content Factory context

Give the sender matrix and policy decision to the domain and mail owners. Continue with [ensure working contact form delivers notifications](https://local-service-spotlight.github.io/task-library/?task=ensure-working-contact-form-delivers-notifications#task-ensure-working-contact-form-delivers-notifications) for website form delivery, or [set up professional email on domain](https://local-service-spotlight.github.io/task-library/?task=set-up-professional-email-on-domain#task-set-up-professional-email-on-domain) if the mailbox itself is missing.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Run at setup and after changes to a sender, domain or policy. Report review can recur on an agreed configured schedule; policy enforcement is a separate evidence-based change, not an automatic timed transition.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. Use the maintained owned training below until that article gap is reviewed.
- Exact task: [Configure SPF/DKIM/DMARC for Deliverability](https://local-service-spotlight.github.io/task-library/?task=configure-spf-dkim-dmarc-for-deliverability#task-configure-spf-dkim-dmarc-for-deliverability)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [Google Workspace SPF setup](https://knowledge.workspace.google.com/admin/security/set-up-spf)
- [Google Workspace DKIM setup](https://knowledge.workspace.google.com/admin/security/set-up-dkim)
- [Google Workspace DMARC setup](https://knowledge.workspace.google.com/admin/security/set-up-dmarc)
- [SPF standard, sections 3 and 4.6.4](https://www.rfc-editor.org/info/rfc7208/)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- Provider-specific record values and the approved reporting receiver must come from the actual project. No real sending or DNS changes were performed while drafting.
