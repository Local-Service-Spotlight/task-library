import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import executions

NOW = datetime(2026, 9, 5, tzinfo=timezone.utc)
KNOWN = {'first-task', 'second-task', 'untracked-task'}


def record(eid='execution-001', status='completed'):
    r = {'executionId': eid, 'taskSlugs': ['first-task'],
         'startedAt': '2026-09-01T10:00:00Z', 'recordedAt': '2026-09-01T10:00:00Z',
         'updatedAt': '2026-09-01T11:00:00Z', 'status': status,
         'result': 'The source and output were checked.',
         'recipeRevisions': {'first-task': {'articleUrl': 'https://example.com/recipe', 'sourceSha256': 'c' * 64}},
         'evidence': [{'visibility': 'public', 'url': 'https://example.com/proof'}],
         'metaArticle': {'status': 'draft', 'draftSha256': 'a' * 64}}
    if status in executions.TERMINAL:
        r['finishedAt'] = '2026-09-01T11:00:00Z'
    return r


class ExecutionLedgerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'ledger.json'
        self.path.write_text('{"schemaVersion":1,"executions":[]}\n')

    def test_duplicate_execution_ids_fail_even_when_meta_urls_differ(self):
        a = record(); b = record()
        b['metaArticle'] = {'status': 'published', 'url': 'https://example.com/derivative'}
        with self.assertRaisesRegex(ValueError, 'duplicate executionId'):
            executions.validate_ledger({'schemaVersion': 1, 'executions': [a, b]}, KNOWN)

    def test_idempotency_revision_conflict_and_failure_leave_file_unchanged(self):
        a = record(); first = executions.upsert(self.path, a, KNOWN)
        original = self.path.read_bytes()
        self.assertEqual(executions.upsert(self.path, a, KNOWN)['action'], 'unchanged')
        b = copy.deepcopy(a); b['result'] = 'A corrected result.'; b['updatedAt'] = '2026-09-02T11:00:00Z'
        with self.assertRaisesRegex(ValueError, 'expected-revision'):
            executions.upsert(self.path, b, KNOWN)
        self.assertEqual(self.path.read_bytes(), original)
        with patch('executions.os.replace', side_effect=OSError('write failed')):
            with self.assertRaises(OSError):
                executions.upsert(self.path, b, KNOWN, first['revision'])
        self.assertEqual(self.path.read_bytes(), original)
        executions.upsert(self.path, b, KNOWN, first['revision'])
        self.assertEqual(len(executions.load(self.path, KNOWN)), 1)

    def test_same_run_lifecycle_and_meta_publication_do_not_add_runs(self):
        a = record(status='running'); first = executions.upsert(self.path, a, KNOWN)
        b = record(); b['updatedAt'] = '2026-09-02T11:00:00Z'
        second = executions.upsert(self.path, b, KNOWN, first['revision'])
        b['metaArticle'] = {'status': 'published', 'url': 'https://example.com/meta'}
        b['updatedAt'] = '2026-09-03T11:00:00Z'
        executions.upsert(self.path, b, KNOWN, second['revision'])
        tasks = [{'slug': s} for s in KNOWN]
        public = executions.attach(tasks, executions.load(self.path, KNOWN), NOW)
        self.assertEqual(public['completedExecutions'], 1)

    def test_completed_failed_and_untracked_are_separate(self):
        completed = record(); completed['taskSlugs'].append('second-task'); completed['recipeRevisions']['second-task'] = copy.deepcopy(completed['recipeRevisions']['first-task'])
        failed = record('execution-002', 'failed')
        tasks = [{'slug': s, 'status': 'needs-work', 'articleState': 'wip'} for s in KNOWN]
        public = executions.attach(tasks, [completed, failed], NOW)
        by_slug = {t['slug']: t for t in tasks}
        self.assertEqual(public['recordedExecutions'], 2)
        self.assertEqual(public['completedExecutions'], 1)
        self.assertEqual(by_slug['first-task']['executionHistory']['completedRuns'], 1)
        self.assertEqual(by_slug['first-task']['executionHistory']['failedRuns'], 1)
        self.assertEqual(by_slug['second-task']['executionHistory']['completedRuns'], 1)
        self.assertIsNone(by_slug['untracked-task']['executionHistory']['completedRuns'])
        self.assertEqual(by_slug['untracked-task']['executionHistory']['status'], 'unknown')
        self.assertTrue(all(t['status'] == 'needs-work' and t['articleState'] == 'wip' for t in tasks))

    def test_private_proof_and_unpublished_draft_hashes_never_reach_public_output(self):
        r = record(); r['evidence'] = [{'visibility': 'private', 'sha256': 'b' * 64}]
        result = executions.attach([{'slug': 'first-task'}], [r], NOW)
        serialized = json.dumps(result)
        self.assertNotIn('b' * 64, serialized)
        self.assertNotIn('a' * 64, serialized)
        self.assertEqual(result['executions'][0]['evidenceUrls'], [])
        self.assertTrue(result['executions'][0]['privateEvidenceRecorded'])
        r['evidence'][0]['path'] = '/private/client/notes'
        with self.assertRaisesRegex(ValueError, 'private evidence'):
            executions.validate_record(r, KNOWN)

    def test_private_urls_credentials_and_missing_proof_rejected(self):
        for url in ['https://localhost/proof', 'https://127.0.0.1/proof',
                    'https://example.com/?token=secret', 'https://user:pass@example.com/']:
            with self.subTest(url=url):
                r = record(); r['evidence'][0]['url'] = url
                with self.assertRaises(ValueError): executions.validate_record(r, KNOWN)
        r = record(); r['evidence'] = []
        with self.assertRaisesRegex(ValueError, 'completed work requires'):
            executions.validate_record(r, KNOWN)

    def test_dry_run_validates_updates_without_writing(self):
        a = record(); before = self.path.read_bytes()
        self.assertFalse(executions.upsert(self.path, a, KNOWN, dry_run=True)['written'])
        self.assertEqual(before, self.path.read_bytes())
        result = executions.upsert(self.path, a, KNOWN)
        b = copy.deepcopy(a); b['updatedAt'] = '2026-09-02T11:00:00Z'; b['taskSlugs'] = ['second-task']; b['recipeRevisions'] = {'second-task': b['recipeRevisions']['first-task']}
        with self.assertRaisesRegex(ValueError, 'taskSlugs is immutable'):
            executions.upsert(self.path, b, KNOWN, result['revision'], dry_run=True)

    def test_window_is_completion_time_and_future_runs_fail(self):
        old = record(); old.update(startedAt='2026-07-01T10:00:00Z', recordedAt='2026-07-01T10:00:00Z', finishedAt='2026-07-01T11:00:00Z')
        tasks = [{'slug': 'first-task'}]
        executions.attach(tasks, [old], NOW)
        self.assertEqual(tasks[0]['executionHistory']['completedLast30Days'], 0)
        with self.assertRaisesRegex(ValueError, 'future'):
            executions.attach(tasks, [record()], datetime(2026, 8, 1, tzinfo=timezone.utc))

    def test_existing_legacy_meta_volume_does_not_create_execution_history(self):
        tasks = [{'slug': 'first-task', 'metaArticleCount': 85}]
        projection = executions.attach(tasks, [], NOW)
        self.assertIsNone(projection['recordedExecutions'])
        self.assertIsNone(tasks[0]['executionHistory']['completedRuns'])
        self.assertEqual(tasks[0]['metaArticleCount'], 85)

    def test_separately_scoped_child_keeps_parent_count_distinct(self):
        parent = record('parent-run')
        child = record('child-run'); child['parentExecutionId'] = 'parent-run'
        child['taskSlugs'] = ['second-task']
        child['recipeRevisions'] = {'second-task': child['recipeRevisions']['first-task']}
        tasks = [{'slug': s} for s in KNOWN]
        public = executions.attach(tasks, [parent, child], NOW)
        self.assertEqual(public['completedExecutions'], 2)
        self.assertEqual(next(t for t in tasks if t['slug'] == 'first-task')['executionHistory']['completedRuns'], 1)
        self.assertEqual(public['executions'][1]['parentExecutionId'], 'parent-run')
        with self.assertRaisesRegex(ValueError, 'existing ledger'):
            executions.upsert(self.path, child, KNOWN)
        self.assertEqual(executions.load(self.path, KNOWN), [])
        parent['parentExecutionId'] = 'child-run'
        with self.assertRaisesRegex(ValueError, 'cycle'):
            executions.validate_ledger({'schemaVersion': 1, 'executions': [parent, child]}, KNOWN)

    def test_recipe_revisions_require_matching_tasks_and_exact_hash(self):
        r = record(); r['recipeRevisions'] = {}
        with self.assertRaisesRegex(ValueError, 'recipeRevisions'):
            executions.validate_record(r, KNOWN)
        r = record(); r['recipeRevisions']['first-task']['sourceSha256'] = 'unverified'
        with self.assertRaisesRegex(ValueError, 'sourceSha256'):
            executions.validate_record(r, KNOWN)

    def test_future_record_is_rejected_before_write(self):
        r = record(); r['updatedAt'] = '2099-01-01T00:00:00Z'
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'future'):
            executions.upsert(self.path, r, KNOWN)
        self.assertEqual(self.path.read_bytes(), before)

    def test_ended_partial_run_has_its_own_count_not_completed(self):
        r = record('partial-run', 'partial')
        executions.upsert(self.path, r, KNOWN)
        tasks = [{'slug': s} for s in KNOWN]
        public = executions.attach(tasks, [r], NOW)
        self.assertEqual(public['completedExecutions'], 0)
        self.assertEqual(public['partialExecutions'], 1)
        task = next(t for t in tasks if t['slug'] == 'first-task')
        self.assertEqual(task['executionHistory']['partialRuns'], 1)
        self.assertEqual(task['executionHistory']['completedRuns'], 0)
        self.assertEqual(public['executions'][0]['status'], 'partial')

    def test_partial_is_terminal_and_requires_finish_time(self):
        r = record('partial-run', 'partial'); del r['finishedAt']
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'terminal status requires finishedAt'):
            executions.upsert(self.path, r, KNOWN)
        self.assertEqual(self.path.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
