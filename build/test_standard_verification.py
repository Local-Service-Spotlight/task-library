import json
from datetime import datetime, timezone
from pathlib import Path
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build as task_build  # noqa: E402
import executions  # noqa: E402
import standard_verification as verification  # noqa: E402


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
        'recordedAt': '2026-09-15T10:00:00Z', 'updatedAt': '2026-09-15T11:00:00Z',
        'status': 'completed', 'result': 'Output checked.',
        'evidence': [{'visibility': 'public', 'url': 'https://example.com/proof/'}],
        'metaArticle': {'status': 'draft', 'draftSha256': 'b' * 64},
    }


class StandardVerificationTests(unittest.TestCase):
    def derive(self, tasks, audits=None, records=None, reviews=None):
        records = records or []
        executions.attach(tasks, records, datetime(2026, 9, 16, tzinfo=timezone.utc))
        return verification.derive(
            tasks, reviews or {t['slug']: t.get('instructionReview') for t in tasks},
            audits or {}, task_build.normalize_article_url)

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
        counts = payload['stats']['gateCounts']
        self.assertEqual(payload['stats']['tasks'], 276)
        self.assertEqual(payload['stats']['fullyVerifiedTasks'], 0)
        self.assertEqual(payload['stats']['semanticHoldHubs'], 3)
        self.assertEqual(counts['instructionRevisionReviewed']['pass'], 275)
        self.assertEqual(counts['contributorComplete']['pass'], 125)
        self.assertEqual(counts['articleMapped']['pass'], 234)
        self.assertEqual(counts['articleCatalogGate']['pass'], 42)
        self.assertEqual(counts['articleSemanticCertification']['pass'], 0)
        self.assertEqual(counts['taskExampleEvidence']['pass'], 10)
        self.assertEqual(counts['recordedExecution']['pass'], 1)
        self.assertEqual(counts['acceptedExecution']['unknown'], 276)
        self.assertEqual(counts['setupSuccess']['unknown'], 276)

    def test_normal_dashboard_and_static_index_link_to_queue(self):
        dashboard = (HERE.parent / 'dashboard' / 'index.html').read_text()
        static_index = (HERE.parent / 'dashboard' / 'library-index.html').read_text()
        self.assertIn('href="verification-queue.html"', dashboard)
        self.assertIn('/verification-queue.html', static_index)


if __name__ == '__main__':
    unittest.main()
