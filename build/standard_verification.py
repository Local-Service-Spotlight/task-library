"""Truthful per-task projection of the Task Library standard gates.

This module derives a review queue from the existing task, article, example and
execution records. It never promotes a missing proof item from a nearby proxy.
"""
import csv
import html
import json
import os
from collections import Counter
from datetime import datetime, timedelta, timezone

import article_semantic_reviews


GATE_ORDER = (
    'instructionRevisionReviewed',
    'instructionStandards',
    'contributorComplete',
    'articleMapped',
    'articleCatalogGate',
    'articleSemanticCertification',
    'taskExampleEvidence',
    'recordedExecution',
    'acceptedExecution',
    'setupSuccess',
)

GATE_LABELS = {
    'instructionRevisionReviewed': 'Exact instruction revision reviewed',
    'instructionStandards': 'Instruction requirements checked',
    'contributorComplete': 'Contributor reports guide complete',
    'articleMapped': 'Canonical article mapped',
    'articleCatalogGate': 'Article catalog gate',
    'articleSemanticCertification': 'Article semantic certification',
    'taskExampleEvidence': 'Task-attributed example evidence',
    'recordedExecution': 'Recorded real execution',
    'acceptedExecution': 'Accepted execution result',
    'setupSuccess': 'New-user setup success',
}

INSTRUCTION_CHECK_ORDER = ('opening', 'recipe', 'links', 'evidence', 'handoff')
ARTICLE_CRITERION_LABELS = {
    'openingContext': 'Opening and useful connection',
    'roleScope': 'Role and scope',
    'owner': 'Owner',
    'steps': 'Detailed steps',
    'links': 'Links',
    'sourceEvidence': 'Source evidence',
    'handoffContext': 'Content Factory and handoff',
    'visualAndLayout': 'Visual and layout',
    'publicationStandards': 'Publication standards',
    'acceptanceResults': 'Acceptance results',
}


def gate(gate_id, state, reason, **evidence):
    if state not in {'pass', 'unmet', 'hold', 'unknown'}:
        raise ValueError(f'{gate_id}: invalid standard-verification state {state}')
    result = {'id': gate_id, 'label': GATE_LABELS[gate_id],
              'state': state, 'reason': reason}
    result.update({key: value for key, value in evidence.items()
                   if value is not None and value != []})
    return result


def acceptance_result(task, history, article_evidence, now):
    """Evaluate only a structured, current, independent result review."""
    reviews = history.get('acceptanceReviews') or []
    if not reviews:
        return {'state': 'unknown', 'reason': ('No structured acceptance review is recorded for the current '
                'canonical article revision. A completed run label is not acceptance.')}
    parsed_reviews = [(item, datetime.fromisoformat(item['reviewedAt'].replace('Z', '+00:00'))) for item in reviews]
    latest_time = max(when for _, when in parsed_reviews)
    latest = [item for item, when in parsed_reviews if when == latest_time]
    if len(latest) != 1:
        return {'state': 'unknown', 'reason': 'Multiple acceptance reviews have the same latest timestamp; resolve the ambiguity.',
                'acceptanceReviewIds': sorted(item['reviewId'] for item in latest)}
    review = latest[0]
    common = {'acceptanceReview': review}
    if latest_time > now:
        return {'state': 'unknown', 'reason': 'The latest acceptance review timestamp is in the future.', **common}
    selected_run = next((row for row in history.get('executionOutcomes', ())
                         if row['executionId'] == review['executionId']), None)
    if not selected_run or selected_run['status'] != 'completed':
        return {'state': 'unmet', 'reason': 'The execution carrying this acceptance review is not completed.', **common}
    if review['canonicalURL'] != task.get('article'):
        return {'state': 'unmet', 'reason': 'The acceptance review canonical URL no longer matches this task mapping.', **common}
    if review['instructionSourceSha256'] != task.get('_sourceSha256'):
        return {'state': 'unmet', 'reason': 'The acceptance review instruction hash no longer matches the current task instruction.', **common}
    outcomes = history.get('executionOutcomes') or []
    reviewed_at = datetime.fromisoformat(review['reviewedAt'].replace('Z', '+00:00'))
    run_finished_at = datetime.fromisoformat(selected_run['finishedAt'].replace('Z', '+00:00'))
    later_unsuccessful = [row for row in outcomes if row['status'] in {'partial', 'failed', 'blocked', 'cancelled'} and
                          datetime.fromisoformat((row.get('finishedAt') or row['startedAt']).replace('Z', '+00:00')) > run_finished_at]
    if later_unsuccessful:
        return {'state': 'unmet', 'reason': 'A later recorded execution did not complete; it cannot be promoted by an older acceptance review.', **common}
    observations = [row for row in article_evidence.get('revisionObservations', ())
                    if row['taskSlug'] == task['slug'] and row['canonicalURL'] == task.get('article') and
                    row['representation'] == review['representation']]
    if not observations:
        return {'state': 'unknown', 'reason': 'No separately fetched current article revision observation is recorded.', **common}
    observed = max(observations, key=lambda row: row['_observedAt'])
    common['revisionObservation'] = {key: value for key, value in observed.items() if not key.startswith('_')}
    if observed['state'] == 'failed' or observed['_observedAt'] < reviewed_at:
        return {'state': 'unknown', 'reason': 'The separate current article revision observation failed or predates the acceptance review.', **common}
    age = now - observed['_observedAt']
    if age < timedelta(0) or age > timedelta(hours=article_semantic_reviews.FRESHNESS_HOURS):
        return {'state': 'unknown', 'reason': 'The separate current article revision observation is outside the 24-hour freshness window.', **common}
    if observed['sourceSha256'] != review['recipeSourceSha256']:
        return {'state': 'unmet', 'reason': 'The observed article source hash does not match the accepted run recipe revision.', **common}
    states = [criterion['state'] for criterion in review['criteria'].values()]
    state = next((value for value in ('hold', 'unmet', 'unknown') if value in states), 'pass')
    if state == 'pass':
        reason = 'All named measurable acceptance criteria pass for the separately observed current recipe revision.'
    else:
        failed = [name for name, item in review['criteria'].items() if item['state'] == state]
        reason = f'Acceptance criteria are {state}: {", ".join(failed)}.'
    return {'state': state, 'reason': reason, **common}


def setup_result(task, history, accepted, now):
    """A scoped manual-guide receipt cannot certify agents as human novices."""
    limits = {'supportedRoute': 'manual-guide', 'installationCertified': False,
              'schedulingCertified': False}
    reviews = history.get('setupReviews') or []
    if not reviews:
        return {'state': 'unknown', 'reason': ('No structured receipt shows a novice human loaded the needed files, '
                'had access and completed this task successfully. Installation and scheduling are not certified.'), **limits}
    parsed = [(item, datetime.fromisoformat(item['reviewedAt'].replace('Z', '+00:00'))) for item in reviews]
    latest_time = max(when for _, when in parsed)
    latest = [item for item, when in parsed if when == latest_time]
    if len(latest) != 1:
        return {'state': 'unknown', 'reason': 'Multiple setup reviews share the latest timestamp; resolve the ambiguity.',
                'setupReviewIds': sorted(item['reviewId'] for item in latest), **limits}
    review = latest[0]
    common = {'setupReview': review, **limits}
    if latest_time > now:
        return {'state': 'unknown', 'reason': 'The latest setup review timestamp is in the future.', **common}
    # Show observed failures even when result acceptance or fresh source proof is absent.
    states = [item['state'] for item in review['criteria'].values()]
    for state in ('hold', 'unmet'):
        if state in states:
            names = ', '.join(name for name, item in review['criteria'].items() if item['state'] == state)
            return {'state': state, 'reason': f'The latest manual-guide setup review is {state}: {names}.', **common}
    if review['canonicalURL'] != task.get('article') or review['instructionSourceSha256'] != task.get('_sourceSha256'):
        return {'state': 'unmet', 'reason': 'The setup receipt no longer matches the current canonical recipe mapping or maintained instruction revision.', **common}
    run = next((item for item in history.get('executionOutcomes', ()) if item['executionId'] == review['executionId']), None)
    if not run or run['status'] != 'completed':
        return {'state': 'unmet', 'reason': 'The execution carrying this setup receipt is not completed.', **common}
    if 'unknown' in states:
        return {'state': 'unknown', 'reason': 'The latest manual-guide setup review still has unknown criteria.', **common}
    accepted_review = accepted.get('acceptanceReview') or {}
    if (not review['acceptanceReviewId'] or accepted_review.get('executionId') != review['executionId'] or
            accepted_review.get('reviewId') != review['acceptanceReviewId']):
        return {'state': 'unknown', 'reason': 'The setup receipt does not reference the current acceptance review for the same completed run.', **common}
    if accepted['state'] != 'pass':
        return {'state': accepted['state'], 'reason': f'The same run has no currently passing accepted result: {accepted["reason"]}', **common}
    # Acceptance already checks representation, source hash, future time and freshness.
    # Setup needs an observation at or after its own review, not merely after acceptance.
    observed = accepted.get('revisionObservation')
    if not observed or datetime.fromisoformat(observed['observedAt'].replace('Z', '+00:00')) < latest_time:
        return {'state': 'unknown', 'reason': 'A separate current recipe observation must follow the setup review within the 24-hour freshness window.', **common}
    if review['participantType'] != 'novice-human':
        return {'state': 'unknown', 'reason': (f'The {review["participantType"]} manual-guide rehearsal is recorded; '
                'it does not establish new-user success for a novice human. Installation and scheduling are not certified.'), **common}
    if review['assistance'] != 'none':
        return {'state': 'unknown', 'reason': (
            f'The novice-human attempt records assistance as {review["assistance"]}; '
            'unassisted new-user setup success remains unknown.'), **common}
    return {'state': 'pass', 'reason': (
        f'A novice human completed the manual-guide route without assistance in {review["app"]} ({review["surface"]}) '
        'with independently reviewed file loading, inputs/access, output and handoff for this exact package and recipe. '
        'This scoped result does not certify installation, scheduling or other apps.'),
        'revisionObservation': observed, **common}


def derive(tasks, instruction_reviews, meta_audits, normalize_url,
           article_evidence=None, now=None):
    """Attach ``standardVerification`` and return a deterministic review queue."""
    article_evidence = article_evidence or {
        'semanticReviews': [], 'revisionObservations': []}
    groups = {}
    for task in tasks:
        key = normalize_url(task.get('article'))
        if key:
            groups.setdefault(key, []).append(task)

    for task in tasks:
        slug = task['slug']
        key = normalize_url(task.get('article'))
        checks = {}

        candidate_review = task.get('instructionReview')
        review = (candidate_review if candidate_review and
                  candidate_review.get('source_sha256') == task.get('_sourceSha256') else None)
        if review:
            checks['instructionRevisionReviewed'] = gate(
                'instructionRevisionReviewed', 'pass',
                f'Current source bytes match the review recorded {review["reviewed_at"]}. '
                f'Review scope and limits: {review["scope"]}',
                reviewedAt=review['reviewed_at'], reviewer=review['reviewer'],
                sourceSha256=review['source_sha256'])
        else:
            prior = instruction_reviews.get(slug)
            reason = ('The recorded instruction review expired because its source hash no longer '
                      'matches the current bytes.' if prior else
                      'No exact-byte instruction review is recorded for this task.')
            checks['instructionRevisionReviewed'] = gate(
                'instructionRevisionReviewed', 'unmet', reason,
                sourceSha256=task.get('_sourceSha256'))

        standards = review.get('standards') if review else None
        if standards:
            criterion_states = [standards['checks'][name]['state']
                                for name in INSTRUCTION_CHECK_ORDER]
            standard_state = next(
                (state for state in ('hold', 'unmet', 'unknown')
                 if state in criterion_states), 'pass')
            affected = [name for name in INSTRUCTION_CHECK_ORDER
                        if standards['checks'][name]['state'] == standard_state]
            if standard_state == 'pass':
                standard_reason = ('All five instruction requirements have explicit passing '
                                   'checks for the current source revision.')
            else:
                standard_reason = (
                    f'Current-revision instruction requirements are {standard_state}: '
                    f'{", ".join(affected)}.')
            checks['instructionStandards'] = gate(
                'instructionStandards', standard_state, standard_reason,
                reviewedAt=review['reviewed_at'], reviewer=review['reviewer'],
                reviewScope=review['scope'], sourceSha256=review['source_sha256'],
                standards=standards)
        else:
            prior = instruction_reviews.get(slug)
            stale_standards = (prior.get('standards') if isinstance(prior, dict) and
                               prior.get('source_sha256') != task.get('_sourceSha256') else None)
            if stale_standards:
                checks['instructionStandards'] = gate(
                    'instructionStandards', 'unmet',
                    'The recorded instruction-requirements checklist expired because its source '
                    'hash no longer matches the current bytes.',
                    sourceSha256=task.get('_sourceSha256'))
            else:
                checks['instructionStandards'] = gate(
                    'instructionStandards', 'unknown',
                    ('The current exact-byte review has no structured instruction-requirements '
                     'checklist.' if review else
                     'No current exact-byte instruction-requirements checklist is recorded.'),
                    sourceSha256=task.get('_sourceSha256'))

        complete = task.get('status') == 'complete'
        checks['contributorComplete'] = gate(
            'contributorComplete', 'pass' if complete else 'unmet',
            ('The contributor status is complete; this is a source claim, not execution proof.'
             if complete else
             f'The contributor status is {task.get("status", "unknown")}; finish and review the guide.'))

        checks['articleMapped'] = gate(
            'articleMapped', 'pass' if key else 'unmet',
            ('The task maps to a normalized canonical article URL.' if key else
             'No valid canonical article URL is mapped for this task.'),
            articleUrl=task.get('article') if key else None)

        if not key:
            catalog = gate('articleCatalogGate', 'unmet',
                           'The catalog gate cannot pass until the task has a valid article mapping.')
        elif task.get('articleStateReason'):
            catalog = gate('articleCatalogGate', 'hold', task['articleStateReason'],
                           reviewedAt=task.get('articleStateReviewed'))
        elif task.get('articleState') == 'ready':
            catalog = gate(
                'articleCatalogGate', 'pass',
                'Every task mapped to this hub is contributor-complete and no reviewed hold is active. '
                'This is catalog readiness only.')
        else:
            catalog = gate(
                'articleCatalogGate', 'unmet',
                'At least one task mapped to this hub is not contributor-complete.')
        checks['articleCatalogGate'] = catalog

        if key and task.get('articleStateReason'):
            semantic = gate('articleSemanticCertification', 'hold',
                            task['articleStateReason'],
                            reviewedAt=task.get('articleStateReviewed'))
        elif key:
            result = article_semantic_reviews.evaluate(task, article_evidence, now=now)
            semantic = gate('articleSemanticCertification', result.pop('state'),
                            result.pop('reason'), **result)
        else:
            semantic = gate(
                'articleSemanticCertification', 'unknown',
                'There is no mapped article revision to review semantically.')
        checks['articleSemanticCertification'] = semantic

        audit = meta_audits.get(key) if key else None
        exact_examples = []
        if audit:
            mapped = groups[key]
            for record in audit['records']:
                if not record['counted']:
                    continue
                # A one-task hub is exact by construction. Shared hubs require the
                # evidence record to name this task slug explicitly.
                if len(mapped) == 1 or slug in record.get('taskSlugs', ()):
                    exact_examples.append(record['sourceUrl'])
        if exact_examples:
            example = gate(
                'taskExampleEvidence', 'pass',
                f'{len(set(exact_examples))} audited example URL(s) are attributable to this task.',
                exampleUrls=sorted(set(exact_examples)), auditedAt=audit['audited'])
        elif not audit:
            example = gate(
                'taskExampleEvidence', 'unknown',
                'No source-backed example audit exists for the mapped hub.' if key else
                'No mapped article exists from which to audit task examples.')
        else:
            positive = [r for r in audit['records'] if r['counted']]
            all_explicit = all(r.get('taskSlugs') for r in positive)
            if audit['metaCountStatus'] == 'verified' and (not positive or all_explicit):
                example = gate(
                    'taskExampleEvidence', 'unmet',
                    'The verified audit contains no counted example attributable to this task.',
                    auditedAt=audit['audited'])
            else:
                example = gate(
                    'taskExampleEvidence', 'unknown',
                    'The hub has historical example volume, but no audited record attributes an '
                    'example to this task slug.', auditedAt=audit['audited'])
        checks['taskExampleEvidence'] = example

        history = task.get('executionHistory') or {}
        run_ids = history.get('executionIds') or []
        if run_ids:
            recorded = gate(
                'recordedExecution', 'pass',
                f'{len(run_ids)} distinct execution ID(s) name this task; outcomes remain separate.',
                executionIds=run_ids, historyStatus=history.get('status'))
        else:
            recorded = gate(
                'recordedExecution', 'unknown',
                'No execution ledger record names this task. Historical run frequency is unknown.')
        checks['recordedExecution'] = recorded
        result = acceptance_result(task, history, article_evidence, now or datetime.now(timezone.utc))
        checks['acceptedExecution'] = gate('acceptedExecution', result.pop('state'), result.pop('reason'), **result)
        setup = setup_result(task, history, checks['acceptedExecution'], now or datetime.now(timezone.utc))
        checks['setupSuccess'] = gate('setupSuccess', setup.pop('state'), setup.pop('reason'), **setup)

        ordered = [checks[gate_id] for gate_id in GATE_ORDER]
        unmet = [item['id'] for item in ordered if item['state'] == 'unmet']
        held = [item['id'] for item in ordered if item['state'] == 'hold']
        unknown = [item['id'] for item in ordered if item['state'] == 'unknown']
        task['standardVerification'] = {
            'instructionSourceSha256': task.get('_sourceSha256'),
            'articleKey': key,
            'gates': {item['id']: item for item in ordered},
            'unmetStandardGates': unmet,
            'heldStandardGates': held,
            'unknownStandardGates': unknown,
            'fullyVerified': not unmet and not held and not unknown,
        }

    rows = sorted(tasks, key=_queue_sort_key)
    for index, task in enumerate(rows, 1):
        verification = task['standardVerification']
        priority, priority_reason = _queue_priority(task)
        verification['queuePosition'] = index
        verification['priority'] = priority
        verification['priorityReason'] = priority_reason
        verification['nextAction'] = _next_action(verification)
    return rows


def _queue_priority(task):
    verification = task['standardVerification']
    gates = verification['gates']
    if gates['setupSuccess']['state'] in {'unmet', 'hold'}:
        return 'P0', 'Recorded setup failure or hold'
    if verification['heldStandardGates']:
        return 'P0', 'Explicit evidence hold'
    if verification['unmetStandardGates']:
        return 'P1', 'Known standard gap'
    if int(task.get('importance') or 0) == 5:
        return 'P2', 'Importance 5; missing proof remains'
    return 'P3', 'Missing proof remains'


def _queue_sort_key(task):
    verification = task['standardVerification']
    priority, _ = _queue_priority(task)
    return (
        {'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3}[priority],
        0 if task.get('status') == 'gap' else 1,
        -len(verification['heldStandardGates']),
        -len(verification['unmetStandardGates']),
        -int(task.get('importance') or 0),
        task['slug'],
    )


def _next_action(verification):
    gates = verification['gates']
    order = (
        'articleSemanticCertification', 'instructionRevisionReviewed',
        'instructionStandards', 'articleMapped', 'contributorComplete', 'articleCatalogGate',
        'taskExampleEvidence', 'recordedExecution', 'acceptedExecution', 'setupSuccess')
    for state in ('hold', 'unmet', 'unknown'):
        for gate_id in order:
            if gates[gate_id]['state'] == state:
                return gates[gate_id]['reason']
    return 'All recorded standard gates pass for the current revisions.'


def report(tasks, generated_at=None):
    """Return a compact public queue; full guide content stays in data.json."""
    generated_at = generated_at or datetime.now(timezone.utc).isoformat(timespec='seconds')
    gate_counts = {}
    for gate_id in GATE_ORDER:
        counts = Counter(t['standardVerification']['gates'][gate_id]['state'] for t in tasks)
        gate_counts[gate_id] = {state: counts.get(state, 0)
                                for state in ('pass', 'unmet', 'hold', 'unknown')}
    rows = []
    for task in tasks:
        rows.append({
            'queuePosition': task['standardVerification']['queuePosition'],
            'priority': task['standardVerification']['priority'],
            'priorityReason': task['standardVerification']['priorityReason'],
            'slug': task['slug'], 'title': task['title'],
            'category': task.get('category'), 'importance': task.get('importance'),
            'status': task.get('status'), 'articleUrl': task.get('article'),
            'taskLibraryUrl': task.get('taskLibraryUrl'),
            'nextAction': task['standardVerification']['nextAction'],
            'standardVerification': task['standardVerification'],
        })
    return {
        'schemaVersion': 1,
        'generatedAt': generated_at,
        'definition': ('Per-task standard gates derived from exact instruction reviews, explicit '
                       'instruction-requirement checks, contributor status, article mapping/catalog '
                       'holds, exact-revision article semantic reviews, task-attributed examples '
                       'and the execution ledger. Unknown proof is never turned into a pass.'),
        'stats': {
            'tasks': len(tasks),
            'fullyVerifiedTasks': sum(t['standardVerification']['fullyVerified'] for t in tasks),
            'semanticHoldHubs': len({normalize for t in tasks
                                     if t['standardVerification']['gates']['articleSemanticCertification']['state'] == 'hold'
                                     for normalize in [t['standardVerification'].get('articleKey')] if normalize}),
            'tasksWithHolds': sum(bool(t['standardVerification']['heldStandardGates']) for t in tasks),
            'tasksWithUnmetGates': sum(bool(t['standardVerification']['unmetStandardGates']) for t in tasks),
            'tasksWithUnknownGates': sum(bool(t['standardVerification']['unknownStandardGates']) for t in tasks),
            'gateCounts': gate_counts,
        },
        'queue': rows,
    }


def write_artifacts(payload, out_dir):
    """Write JSON, CSV and an accessible human review page from one payload."""
    json_path = os.path.join(out_dir, 'verification-queue.json')
    csv_path = os.path.join(out_dir, 'verification-queue.csv')
    html_path = os.path.join(out_dir, 'verification-queue.html')
    with open(json_path, 'w', encoding='utf-8') as target:
        json.dump(payload, target, ensure_ascii=False, indent=2)
        target.write('\n')
    fields = ['queuePosition', 'priority', 'priorityReason', 'slug', 'title',
              'category', 'importance', 'status', 'articleUrl', 'taskLibraryUrl',
              'unmetStandardGates', 'heldStandardGates', 'unknownStandardGates',
              'nextAction'] + list(GATE_ORDER)
    with open(csv_path, 'w', encoding='utf-8', newline='') as target:
        writer = csv.DictWriter(target, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        for row in payload['queue']:
            verification = row['standardVerification']
            writer.writerow({
                **{key: row.get(key) for key in fields},
                'unmetStandardGates': ';'.join(verification['unmetStandardGates']),
                'heldStandardGates': ';'.join(verification['heldStandardGates']),
                'unknownStandardGates': ';'.join(verification['unknownStandardGates']),
                **{gate_id: verification['gates'][gate_id]['state']
                   for gate_id in GATE_ORDER},
            })
    with open(html_path, 'w', encoding='utf-8') as target:
        target.write(_html_report(payload))


def _html_report(payload):
    esc = lambda value: html.escape(str(value or ''), quote=True)
    stats = payload['stats']
    rows = []
    for row in payload['queue']:
        verification = row['standardVerification']
        state_set = set()
        cells = []
        for gate_id in GATE_ORDER:
            item = verification['gates'][gate_id]
            state_set.add(item['state'])
            checklist = ''
            if gate_id == 'instructionStandards' and item.get('standards'):
                criteria = []
                for check_name in INSTRUCTION_CHECK_ORDER:
                    check = item['standards']['checks'][check_name]
                    criteria.append(
                        f'<li><strong>{esc(check_name.title())}</strong>: '
                        f'<span class="state {esc(check["state"])}">'
                        f'{esc(check["state"])}</span> {esc(check["reason"])} '
                        f'<small>Evidence: {esc(check["evidence"])}</small></li>')
                checklist = f'<ul class="criteria">{"".join(criteria)}</ul>'
            elif gate_id == 'articleSemanticCertification' and item.get('semanticReview'):
                criteria = []
                for check_name in article_semantic_reviews.CRITERION_ORDER:
                    check = item['semanticReview']['criteria'][check_name]
                    refs = ', '.join(check['evidenceRefs'])
                    criteria.append(
                        f'<li><strong>{esc(ARTICLE_CRITERION_LABELS[check_name])}</strong>: '
                        f'<span class="state {esc(check["state"])}">'
                        f'{esc(check["state"])}</span> {esc(check["reason"])} '
                        f'<small>Evidence: {esc(refs)}</small></li>')
                checklist = f'<ul class="criteria">{"".join(criteria)}</ul>'
            cells.append(
                f'<li><strong>{esc(item["label"])}</strong>: '
                f'<span class="state {esc(item["state"])}">{esc(item["state"])}</span> '
                f'{esc(item["reason"])}{checklist}</li>')
        task_link = row.get('taskLibraryUrl') or row.get('articleUrl')
        title = (f'<a href="{esc(task_link)}">{esc(row["title"])}</a>' if task_link else
                 esc(row['title']))
        rows.append(
            f'<tr data-priority="{esc(row["priority"])}" '
            f'data-states="{esc(" ".join(sorted(state_set)))}" '
            f'data-search="{esc((row["slug"] + " " + row["title"] + " " + (row.get("category") or "")).lower())}">'
            f'<td data-label="Queue">{row["queuePosition"]}</td><td data-label="Priority"><strong>{esc(row["priority"])}</strong><br>'
            f'<small>{esc(row["priorityReason"])}</small></td>'
            f'<td data-label="Task">{title}<br><code>{esc(row["slug"])}</code><br><small>{esc(row.get("category"))}</small></td>'
            f'<td data-label="Importance">{esc(row.get("importance"))}</td>'
            f'<td data-label="Checks"><span class="state unmet">{len(verification["unmetStandardGates"])} unmet</span> '
            f'<span class="state hold">{len(verification["heldStandardGates"])} held</span> '
            f'<span class="state unknown">{len(verification["unknownStandardGates"])} unknown</span>'
            f'<details><summary>Read all gates</summary><ul>{"".join(cells)}</ul></details></td>'
            f'<td data-label="Next action">{esc(row["nextAction"])}</td></tr>')
    gate_cards = []
    for gate_id in GATE_ORDER:
        counts = stats['gateCounts'][gate_id]
        gate_cards.append(
            f'<li><strong>{esc(GATE_LABELS[gate_id])}</strong><br>'
            f'{counts["pass"]} pass · {counts["unmet"]} unmet · '
            f'{counts["hold"]} held · {counts["unknown"]} unknown</li>')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Task Library standard verification queue</title>
<style>
:root{{--ink:#18212f;--muted:#5c6779;--line:#d8dee8;--paper:#fff;--wash:#f5f7fb;--hold:#8b2d2d;--unmet:#8a4b08;--pass:#17613a;--unknown:#586174}}*{{box-sizing:border-box}}body{{margin:0;background:var(--wash);color:var(--ink);font:16px/1.5 system-ui,-apple-system,sans-serif}}main{{max-width:1500px;margin:auto;padding:clamp(20px,4vw,52px)}}h1{{font-size:clamp(2rem,5vw,3.6rem);line-height:1.05;margin:.2em 0}}.lead{{max-width:850px;font-size:1.15rem;color:var(--muted)}}.process{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:22px 0}}.process li{{background:#e9eef8;border:1px solid var(--line);border-radius:999px;padding:8px 12px;font-weight:700}}.process li+li::before{{content:'→';margin-right:14px;color:var(--muted)}}.summary,.filters,.table-wrap{{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:18px;margin-top:22px}}.summary ul{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;list-style:none;padding:0}}.summary li{{border-left:4px solid var(--line);padding:8px 12px}}.filters{{display:flex;gap:14px;flex-wrap:wrap;align-items:end}}label{{font-weight:700}}input,select{{display:block;margin-top:5px;padding:9px;border:1px solid #aab4c4;border-radius:7px;font:inherit;min-width:180px}}.table-wrap{{overflow:auto;padding:0}}table{{border-collapse:collapse;width:100%;min-width:1050px}}caption{{text-align:left;font-weight:700;padding:16px}}th,td{{padding:12px;border-top:1px solid var(--line);text-align:left;vertical-align:top}}th{{position:sticky;top:0;background:#eef2f8}}td:first-child{{font-variant-numeric:tabular-nums}}code{{font-size:.82em}}small{{color:var(--muted)}}.state{{display:inline-block;border:1px solid currentColor;border-radius:999px;padding:1px 7px;font-size:.78rem;font-weight:700;margin:2px}}.pass{{color:var(--pass)}}.unmet{{color:var(--unmet)}}.hold{{color:var(--hold)}}.unknown{{color:var(--unknown)}}details{{margin-top:8px}}details ul{{padding-left:20px}}details li{{margin:.45em 0}}a{{color:#174ea6}}[hidden]{{display:none!important}}@media(max-width:760px){{.process{{display:grid;grid-template-columns:1fr}}.process li+li::before{{content:'↓';margin-right:10px}}.table-wrap{{background:transparent;border:0;overflow:visible}}table,tbody,tr,td{{display:block;width:100%}}table{{min-width:0}}thead{{position:absolute;left:-9999px}}caption{{background:var(--paper);border:1px solid var(--line);border-radius:12px;margin-bottom:12px}}tr{{background:var(--paper);border:1px solid var(--line);border-radius:12px;margin:0 0 14px;padding:10px}}td{{border:0;padding:8px}}td::before{{content:attr(data-label);display:block;color:var(--muted);font-size:.75rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}}}}
</style></head><body><main>
<h1>Task Library standard verification queue</h1>
<p class="lead">Use this list to find which work guides in the <a href="./">Task Library</a> still need checks before your team relies on them. It shows what we know, what is missing, and what to check next. These checks help keep the Task Library useful as each real job teaches us more.</p>
<ol class="process" aria-label="How real work improves a guide"><li>Read guide</li><li>Try task</li><li>Check result</li><li>Improve guide</li></ol>
<p><strong>{stats['fullyVerifiedTasks']} of {stats['tasks']} tasks currently pass every check.</strong> A guide can be listed and reviewed while its real result or first-user setup is still unknown. Generated {esc(payload['generatedAt'])}. Download the <a href="verification-queue.json">JSON report</a> or <a href="verification-queue.csv">CSV queue</a>.</p>
<section class="summary" aria-labelledby="gate-summary"><h2 id="gate-summary">Gate counts</h2><ul>{''.join(gate_cards)}</ul></section>
<section class="filters" aria-label="Queue filters"><label>Search tasks<input id="search" type="search" autocomplete="off" placeholder="Name, slug or category"></label><label>Priority<select id="priority"><option value="">All priorities</option><option>P0</option><option>P1</option><option>P2</option><option>P3</option></select></label><label>Evidence state<select id="state"><option value="">All states</option><option value="hold">Has a hold</option><option value="unmet">Has an unmet gate</option><option value="unknown">Has an unknown gate</option><option value="pass">Has a passing gate</option></select></label><p id="shown" aria-live="polite"></p></section>
<div class="table-wrap"><table><caption>Tasks sorted by setup failures, evidence holds, known gaps, importance and slug.</caption><thead><tr><th>Queue</th><th>Priority</th><th>Task</th><th>Importance</th><th>Gate states</th><th>Next action</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<script>
const rows=[...document.querySelectorAll('tbody tr')], search=document.querySelector('#search'), priority=document.querySelector('#priority'), state=document.querySelector('#state'), shown=document.querySelector('#shown');
function apply(){{const q=search.value.trim().toLowerCase();let count=0;for(const row of rows){{const visible=(!q||row.dataset.search.includes(q))&&(!priority.value||row.dataset.priority===priority.value)&&(!state.value||row.dataset.states.split(' ').includes(state.value));row.hidden=!visible;if(visible)count++;}}shown.textContent=count+' of '+rows.length+' tasks shown';}}
for(const control of [search,priority,state])control.addEventListener('input',apply);apply();
</script></main></body></html>'''
