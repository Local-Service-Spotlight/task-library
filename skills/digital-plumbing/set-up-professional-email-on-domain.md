---
name: set-up-professional-email-on-domain
description: "Set up mail at your business web address. Check that it sends, arrives and reaches the right team."
category: Digital Plumbing
stage: —
definitive_article: GAP — to be written
status: needs-work
---

# Set Up Professional Email on Domain

Mail from your own web address helps people know who wrote it. This guide helps you set it up and keep old mail safe. Start with the mail you need and the service you use.

**The path:** Address plan → Mailboxes → DNS cutover → Send and receive checks.

**Use this when:** a business adopts domain email or changes its mail provider under an approved migration plan.

## Inputs
- The owned domain, authoritative DNS provider and actual mail-provider account or approved purchase/setup plan.
- The required people, role addresses and mailbox, alias or shared-inbox behavior, with business-controlled administration.
- Current mail routing, legacy account ownership, migration/retention plan, rollback values and a controlled external test receiver.

## First-run prompt

> Set up the agreed domain-mail addresses through the actual provider. Preserve current mail and privacy during the planned cutover. Test both directions and each important alias or role address, then update only the authorized public contact surfaces.

## Steps
1. Inventory existing mailboxes, aliases, shared inboxes and senders. Decide which addresses need stored mail, delegated team access or only an alias. One generic forwarding rule is not enough for every support or shared-mailbox need.
2. Use the chosen business-controlled provider account and current setup instructions. Create only the authorized mailboxes and roles, accounting for actual licenses and costs. Verify the operator’s legitimate access without publishing login details.
3. Verify the domain using the provider’s supplied method and prepare sender authentication with the email-authentication task. A mailbox’s existence does not mean it can yet send authenticated mail or receive public mail.
4. Plan the actual cutover: existing delivery, data migration, recovery and monitoring. Copy the current provider-supplied MX values and preserve intentional gateways or coexistence routes. Do not replace nameservers or unrelated website records to set up mail.
5. Apply the authorized MX change at authoritative DNS and verify public resolution after applicable caching. Follow the provider’s real routing design rather than assuming every old-looking MX record is disposable.
6. Send marked controlled mail from the new address to the agreed external receiver and reply back. Check visible From identity, authenticated headers, destination and any role-address behavior. Test inbox receipt separately from a provider dashboard’s acceptance.
7. Bridge old mail only for accounts and data within scope. Forwarding a mixed personal mailbox into a business inbox may expose private mail; use the agreed migration or handoff plan instead. Confirm the actual bridge works before claiming no mail will be missed.
8. Update the approved website, form and profile contact fields plus signatures. Read back each change and keep private recovery addresses distinct. Save the mailbox map, routing state, test evidence and any unfinished data-migration item.

## Definition of done (QA checklist)

- [ ] The planned people and role addresses have the intended mailbox or alias behavior.
- [ ] Business-controlled administration and the actual license scope are documented.
- [ ] MX and sender-authentication setup match the provider and authorized migration plan.
- [ ] Controlled sending, receiving and important role-address paths have actual receipts.
- [ ] Legacy-mail handling, public updates and unresolved migration work are explicit and private data is protected.

## Example(s)

**Fictional teaching example.** Oak Repair needs Lee’s mailbox and a team support inbox. “Support” must keep its own shared history, so it is not treated as a personal alias by default. In the lesson plan, a marked message goes from Lee’s new address to an external test receiver and a reply reaches Lee. A separate support test proves the team inbox. The old personal Gmail account is not broadly forwarded because it also contains private mail.

## Handoff and Content Factory context

Give the address and routing map to the mail owner. Continue with [configure spf dkim dmarc for deliverability](https://local-service-spotlight.github.io/task-library/?task=configure-spf-dkim-dmarc-for-deliverability#task-configure-spf-dkim-dmarc-for-deliverability) for complete sender validation and [ensure working contact form delivers notifications](https://local-service-spotlight.github.io/task-library/?task=ensure-working-contact-form-delivers-notifications#task-ensure-working-contact-form-delivers-notifications) for website notification receipt.

This setup supports the [Content Factory](https://blitzmetrics.com/content-factory/). Produce gathers real source material; Process makes useful assets; Post places and checks them; Promote distributes suitable work within its own scope. This check does not automatically execute all four stages. Use the actual next step above; catalog neighbors are not prerequisites.

## When this runs

Set up once or during a planned migration. Later mailbox, sender and staff changes use their own scope; no subscription purchase, forwarding rule or recurring send test is implied by this guide.

## First-run setup and continuity

Open the supplied task file and its linked source. Verify the project’s real inputs, account, access and output folder before work. This Markdown file is a guide; it does not install an app, connect an account, supply a subscription or create a schedule. Carry out work already authorized; do not ask for the same approval again. Keep any unsupplied destination or new action outside that scope clearly pending.

Save source IDs, versions, decisions, checked outputs and next owner in the project tracker. Before a retry, check the saved state and other workers’ changes. A model name does not guarantee memory or a running timer. Repeated work needs an actual configured trigger and durable state; one-off work can be started by the prompt above.

Keep agent media muted with volume zero before playback. If mute cannot be verified, use captions, metadata or still frames. State the limit: silent visual checks do not prove spoken-word accuracy or audio quality. Do not start sound through the user’s speakers unless explicitly asked.

## Write up the real run

For every actual attempt, [write its meta article](https://blitzmetrics.com/meta-article-prompt/) with this recipe and revision, trigger, steps performed, output evidence, measured result, gaps and next owner. Failed, blocked and partial attempts also get a written record. A draft can satisfy writing; publishing it follows the existing job scope.

Keep one stable execution ID across retries and edits. A separately scoped child task may have its own ID linked to its parent. Writing the parent’s meta record is part of that run, not an endless new chain. The [recipe and meta-article guide](https://localservicespotlight.com/meta-articles/) explains this distinction. Teaching examples are not real executions and must not enter the run count.

## Definitive article & links

- Dedicated canonical article: not mapped in this source record. Use the maintained owned training below until that article gap is reviewed.
- Exact task: [Set Up Professional Email on Domain](https://local-service-spotlight.github.io/task-library/?task=set-up-professional-email-on-domain#task-set-up-professional-email-on-domain)
- Writing standard: [Article Guidelines](https://localservicespotlight.com/article-guidelines/)
- [Digital Plumbing training](https://blitzmetrics.com/digital-plumbing/)
- [DNS record types in Cloudflare documentation](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/)
- [Google Workspace SPF setup](https://knowledge.workspace.google.com/admin/security/set-up-spf)
- [Google Workspace DKIM setup](https://knowledge.workspace.google.com/admin/security/set-up-dkim)

## Review and evidence still needed

The source contributor status is preserved. It is not certification of this draft or proof of account access, completed work or a live outcome. The worked example teaches the method and is explicitly fictional.
- The dedicated task article is absent. Current chosen-provider mailbox and migration instructions are needed for its actual account; no provider was purchased or configured.
