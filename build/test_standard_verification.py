import json
from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import executions  # noqa: E402
import standard_verification as verification  # noqa: E402
SPEC = importlib.util.spec_from_file_location('task_library_builder', HERE / 'build.py')
task_build = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(task_build)


def task(slug, status='complete', article='https://example.com/hub/', importance=3,
         source_hash='a' * 64):
    return {
        'slug': slug, 'title': slug.replace('-', ' ').title(), 'status': status,
        'article': article, 'articleState': 'ready', 'importance': importance,
        'category': 'Test', '_sourceSha256': source_hash,
        'instructionReview': {'source_sha256': source_hash, 'reviewed_at': '2026-09-15',
                              'reviewer': 'Reviewer', 'scope': 'Exact source review.'},
        'executionHistory': {'status': 'unknown', 'executionIds': []},
    }


def audit(records, status='verified'):
    return {
        'hubUrl': 'https://example.com/hub/', 'metaCountStatus': status,
        'audited': '2026-09-15', 'evidenceSourceUrl': 'https://example.com/audit/',
        'evidenceMethod': 'Exact public source review.', 'records': records,
    }


def execution(source_hash='a' * 64):
    return {
        'executionId': 'execution-001', 'taskSlugs': ['first-task'],
        'recipeRevisions': {'first-task': {
            'articleUrl': 'https://example.com/hub/', 'sourceSha256': source_hash}},
        'startedAt': '2026-09-15T10:00:00Z', 'finishedAt': '2026-09-15T11:00:00Z',
        'recordedAt': '2026-09-15T10:00:00Z', 'updatedAt': '2026-09-15T12:00:00Z',
        'status': 'completed', 'result': 'Output checked.',
        'evidence': [{'visibility': 'public', 'url': 'https://example.com/proof/'}],
        'metaArticle': {'status': 'draft', 'draftSha256': 'b' * 64},
    }


def acceptance(source_hash='a' * 64, instruction_hash='a' * 64, state='pass', **overrides):
    value = {'version': 1, 'reviewId': 'acceptance-001', 'taskSlug': 'first-task',
            'canonicalURL': 'https://example.com/hub/', 'recipeSourceSha256': source_hash,
            'representation': 'wordpress-content-html', 'instructionSourceSha256': instruction_hash,
            'reviewedAt': '2026-09-15T11:30:00Z', 'reviewer': 'Independent reviewer',
            'executor': 'Run executor', 'nextHandoff': 'Hand the checked result to the owner.',
            'criteria': {'result': {'state': state, 'expectedResult': 'A checked result exists.', 'observedResult': 'The result was checked.',
                                    'sourceRef': 'https://example.com/guide/', 'evidenceRefs': ['https://example.com/result/']},
                         'handoff': {'state': state, 'expectedResult': 'The owner receives it.', 'observedResult': 'The owner received it.',
                                     'sourceRef': 'https://example.com/handoff/', 'evidenceRefs': ['https://example.com/handoff-proof/']}}}
    value.update(overrides)
    return value


def observation(source_hash='a' * 64, observed='2026-09-15T12:00:00Z', state='observed'):
    return {'taskSlug': 'first-task', 'canonicalURL': 'https://example.com/hub/',
            'representation': 'wordpress-content-html', 'sourceSha256': source_hash if state == 'observed' else None,
            'observedAt': observed, '_observedAt': datetime.fromisoformat(observed.replace('Z', '+00:00')),
            'state': state, 'reason': 'Current public source observed.', 'observer': 'Separate observer', 'evidenceRefs': ['https://example.com/observe/']}


class StandardVerificationTests(unittest.TestCase):
    def derive(self, tasks, audits=None, records=None, reviews=None):
        records = records or []
        executions.attach(tasks, records, datetime(2026, 9, 16, tzinfo=timezone.utc))
        return verification.derive(
            tasks, reviews or {t['slug']: t.get('instructionReview') for t in tasks},
            audits or {}, task_build.normalize_article_url,
            article_evidence={'semanticReviews': [], 'revisionObservations': []})

    def derive_acceptance(self, current, records, observations):
        executions.attach([current], records, datetime(2026, 9, 16, 12, tzinfo=timezone.utc))
        verification.derive([current], {current['slug']: current['instructionReview']}, {},
                            task_build.normalize_article_url,
                            article_evidence={'semanticReviews': [], 'revisionObservations': observations},
                            now=datetime(2026, 9, 15, 13, tzinfo=timezone.utc))
        return current['standardVerification']['gates']['acceptedExecution']

    def test_proxies_cannot_certify_semantics_acceptance_or_setup(self):
        current = task('first-task', importance=5)
        records = [execution()]
        self.derive([current], {
            'example.com/hub': audit([{
                'sourceUrl': 'https://example.com/meta/', 'hubUrl': 'https://example.com/hub/',
                'evidenceMethod': 'Public source review.', 'counted': True,
                'reason': 'A historical meta article.'}])}, records)
        gates = current['standardVerification']['gates']

        self.assertEqual(gates['instructionRevisionReviewed']['state'], 'pass')
        self.assertEqual(gates['contributorComplete']['state'], 'pass')
        self.assertEqual(gates['articleCatalogGate']['state'], 'pass')
        self.assertEqual(gates['taskExampleEvidence']['state'], 'pass')
        self.assertEqual(gates['recordedExecution']['state'], 'pass')
        self.assertEqual(gates['articleSemanticCertification']['state'], 'unknown')
        self.assertEqual(gates['acceptedExecution']['state'], 'unknown')
        self.assertEqual(gates['setupSuccess']['state'], 'unknown')
        self.assertFalse(current['standardVerification']['fullyVerified'])

    def test_shared_hub_example_requires_matching_task_slug(self):
        first, second = task('first-task'), task('second-task')
        source = {
            'example.com/hub': audit([{
                'sourceUrl': 'https://example.com/meta/', 'hubUrl': 'https://example.com/hub/',
                'evidenceMethod': 'Public source review.', 'counted': True,
                'reason': 'Names only the first task.', 'taskSlugs': ['first-task']}])}
        self.derive([first, second], source)

        self.assertEqual(first['standardVerification']['gates']['taskExampleEvidence']['state'],
                         'pass')
        self.assertEqual(second['standardVerification']['gates']['taskExampleEvidence']['state'],
                         'unmet')
        source['example.com/hub']['records'][0].pop('taskSlugs')
        self.derive([first, second], source)
        self.assertEqual(first['standardVerification']['gates']['taskExampleEvidence']['state'],
                         'unknown')

    def test_source_edit_expires_instruction_review_but_does_not_change_unknown_outcomes(self):
        current = task('first-task')
        records = [execution()]
        self.derive([current], records=records)
        gates = current['standardVerification']['gates']
        self.assertEqual(gates['acceptedExecution']['state'], 'unknown')
        self.assertEqual(gates['setupSuccess']['state'], 'unknown')

        current['_sourceSha256'] = 'd' * 64
        current.pop('instructionReview')
        self.derive([current], records=records,
                    reviews={'first-task': {'source_sha256': 'a' * 64}})
        gates = current['standardVerification']['gates']
        self.assertEqual(gates['instructionRevisionReviewed']['state'], 'unmet')
        self.assertIn('expired', gates['instructionRevisionReviewed']['reason'])
        self.assertEqual(gates['acceptedExecution']['state'], 'unknown')
        self.assertIn('canonical article revision', gates['acceptedExecution']['reason'])

    def test_hold_and_gap_sort_before_importance_only(self):
        held = task('held-task', importance=2)
        held['articleState'] = 'wip'
        held['articleStateReason'] = 'Reviewed semantic conflict.'
        held['articleStateReviewed'] = '2026-09-15'
        gap = task('gap-task', status='gap', article=None, importance=2)
        gap.pop('articleState')
        important = task('important-task', importance=5)

        rows = self.derive([important, gap, held])

        self.assertEqual([row['slug'] for row in rows],
                         ['held-task', 'gap-task', 'important-task'])
        self.assertEqual(held['standardVerification']['priority'], 'P0')
        self.assertEqual(gap['standardVerification']['priority'], 'P1')
        self.assertEqual(important['standardVerification']['priority'], 'P2')

    def test_report_artifacts_are_sorted_searchable_and_escaped(self):
        first = task('first-task')
        first['title'] = '<Unsafe task>'
        rows = self.derive([first])
        payload = verification.report(rows, '2026-09-15T12:00:00+00:00')
        with tempfile.TemporaryDirectory() as temp_dir:
            verification.write_artifacts(payload, temp_dir)
            html_text = (Path(temp_dir) / 'verification-queue.html').read_text()
            csv_text = (Path(temp_dir) / 'verification-queue.csv').read_text()
            data = json.loads((Path(temp_dir) / 'verification-queue.json').read_text())

        self.assertIn('&lt;Unsafe task&gt;', html_text)
        self.assertNotIn('<Unsafe task>', html_text)
        self.assertIn('Evidence state', html_text)
        self.assertIn('0 of 1 tasks currently pass every check', html_text)
        self.assertIn('Read guide', html_text)
        self.assertIn('Try task', html_text)
        self.assertIn('@media(max-width:760px)', html_text)
        self.assertEqual(data['queue'][0]['queuePosition'], 1)
        self.assertIn('unknownStandardGates', csv_text.splitlines()[0])
        self.assertIn('acceptedExecution', csv_text.splitlines()[0])

    def test_checked_in_queue_matches_current_evidence_boundaries(self):
        payload = json.loads((HERE.parent / 'dashboard' / 'verification-queue.json').read_text())
        data = json.loads((HERE.parent / 'dashboard' / 'data.json').read_text())
        tasks = [task for category in data['categories'] for task in category['tasks']]
        counts = payload['stats']['gateCounts']
        self.assertEqual(payload['stats']['tasks'], len(tasks))
        self.assertEqual(payload['stats']['fullyVerifiedTasks'], 0)
        self.assertEqual(
            payload['stats']['semanticHoldHubs'],
            len({task['standardVerification']['articleKey'] for task in tasks
                 if task.get('articleStateReason')}))
        self.assertEqual(counts['instructionRevisionReviewed']['pass'],
                         sum(bool(task.get('instructionReview')) for task in tasks))
        self.assertEqual(counts['contributorComplete']['pass'],
                         sum(task['status'] == 'complete' for task in tasks))
        self.assertEqual(counts['articleMapped']['pass'],
                         sum(bool(task.get('article')) for task in tasks))
        self.assertEqual(counts['articleCatalogGate']['pass'],
                         sum(task.get('articleState') == 'ready' for task in tasks))
        self.assertEqual(counts['articleSemanticCertification']['pass'], 0)
        exact_examples = {
            slug for hub in data['articleHubs'] for slug, count in
            (hub.get('taskMetaCounts') or {}).items() if count > 0}
        self.assertEqual(counts['taskExampleEvidence']['pass'], len(exact_examples))
        self.assertEqual(counts['recordedExecution']['pass'],
                         sum(bool(task['executionHistory']['executionIds']) for task in tasks))
        self.assertEqual(counts['acceptedExecution']['unknown'], len(tasks))
        self.assertEqual(counts['setupSuccess']['unknown'], len(tasks))

    def test_normal_dashboard_and_static_index_link_to_queue(self):
        dashboard = (HERE.parent / 'dashboard' / 'index.html').read_text()
        static_index = (HERE.parent / 'dashboard' / 'library-index.html').read_text()
        self.assertIn('href="verification-queue.html"', dashboard)
        self.assertIn('/verification-queue.html', static_index)

    def test_acceptance_requires_current_hash_and_all_criteria(self):
        r = execution(); r['acceptanceReviews'] = [acceptance()]
        current = task('first-task')
        self.assertEqual(self.derive_acceptance(current, [r], [observation()])['state'], 'pass')
        gates = current['standardVerification']['gates']
        self.assertEqual(gates['setupSuccess']['state'], 'unknown')
        self.assertEqual(gates['articleSemanticCertification']['state'], 'unknown')
        self.assertEqual(current['status'], 'complete')
        self.assertFalse(current['standardVerification']['fullyVerified'])
        current = task('first-task')
        self.assertEqual(self.derive_acceptance(current, [r], [observation('c' * 64)])['state'], 'unmet')
        current = task('first-task')
        self.assertEqual(self.derive_acceptance(current, [r], [observation(observed='2026-09-14T11:00:00Z')])['state'], 'unknown')
        r['acceptanceReviews'][0]['criteria']['result']['state'] = 'hold'
        current = task('first-task')
        self.assertEqual(self.derive_acceptance(current, [r], [observation()])['state'], 'hold')

    def test_later_partial_run_cannot_be_promoted_by_older_acceptance(self):
        accepted = execution(); accepted['acceptanceReviews'] = [acceptance()]
        partial = execution(); partial['executionId'] = 'execution-002'; partial['status'] = 'partial'; partial['finishedAt'] = '2026-09-15T12:30:00Z'; partial['updatedAt'] = '2026-09-15T12:30:00Z'
        current = task('first-task')
        gate = self.derive_acceptance(current, [accepted, partial], [observation()])
        self.assertEqual(gate['state'], 'unmet')

    def test_latest_review_wins_by_instant_and_ties_or_future_fail_closed(self):
        first = execution(); first['updatedAt'] = '2026-09-15T14:00:00Z'; first['acceptanceReviews'] = [acceptance(reviewedAt='2026-09-15T10:30:00-02:00', state='hold')]
        second = execution(); second['updatedAt'] = '2026-09-16T11:00:00Z'; second['executionId'] = 'execution-002'; second['acceptanceReviews'] = [acceptance(reviewId='acceptance-002', reviewedAt='2026-09-15T11:30:00Z')]
        current = task('first-task')
        self.assertEqual(self.derive_acceptance(current, [first, second], [observation(observed='2026-09-15T12:45:00Z')])['state'], 'hold')
        second['acceptanceReviews'][0]['reviewedAt'] = '2026-09-15T10:30:00-02:00'
        current = task('first-task')
        self.assertEqual(self.derive_acceptance(current, [first, second], [observation()])['state'], 'unknown')
        second['acceptanceReviews'][0]['reviewedAt'] = '2026-09-16T10:30:00Z'
        current = task('first-task')
        self.assertEqual(self.derive_acceptance(current, [first, second], [observation()])['state'], 'unknown')

    def test_acceptance_instruction_or_mapping_mismatch_cannot_promote_other_gates(self):
        r = execution(); r['acceptanceReviews'] = [acceptance()]
        current = task('first-task'); current['_sourceSha256'] = 'd' * 64
        gate = self.derive_acceptance(current, [r], [observation()])
        self.assertEqual(gate['state'], 'unmet')
        self.assertEqual(current['standardVerification']['gates']['setupSuccess']['state'], 'unknown')
        current = task('first-task', article='https://example.com/other/')
        gate = self.derive_acceptance(current, [r], [observation()])
        self.assertEqual(gate['state'], 'unmet')

    def test_partial_correction_and_later_blocked_cannot_pass(self):
        r = execution(); r['acceptanceReviews'] = [acceptance()]
        r['status'] = 'partial'
        self.assertEqual(self.derive_acceptance(task('first-task'), [r], [observation()])['state'], 'unmet')
        r['status'] = 'completed'
        blocked = execution(); blocked.update(executionId='later-blocked', status='blocked',
            startedAt='2026-09-15T12:30:00Z', recordedAt='2026-09-15T12:30:00Z', updatedAt='2026-09-15T12:30:00Z')
        blocked.pop('finishedAt')
        self.assertEqual(self.derive_acceptance(task('first-task'), [r, blocked], [observation()])['state'], 'unmet')


    def test_late_review_of_old_success_cannot_hide_later_failure(self):
        old = execution(); old['updatedAt'] = '2026-09-15T13:00:00Z'
        old['acceptanceReviews'] = [acceptance(reviewedAt='2026-09-15T12:45:00Z')]
        failed = execution(); failed.update(executionId='later-failed', status='failed',
            finishedAt='2026-09-15T12:00:00Z', updatedAt='2026-09-15T12:00:00Z')
        gate = self.derive_acceptance(task('first-task'), [old, failed],
                                     [observation(observed='2026-09-15T12:50:00Z')])
        self.assertEqual(gate['state'], 'unmet')


if __name__ == '__main__':
    unittest.main()
