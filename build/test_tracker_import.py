"""Tracker import provenance is separate from task verification."""
import unittest

from build import apply_existing_tracker_source, tracker_import_state


class TrackerImportTests(unittest.TestCase):
    def test_missing_tracker_is_explicitly_not_configured(self):
        self.assertEqual(
            tracker_import_state(False, 0, 0, True),
            {'state': 'not_configured', 'inputRows': 0, 'matchedRows': 0},
        )

    def test_loaded_counts_include_unmatched_rows_without_calling_them_task_failures(self):
        self.assertEqual(
            tracker_import_state(True, 4, 2, True),
            {'state': 'loaded', 'inputRows': 4, 'matchedRows': 2},
        )

    def test_validation_failure_cannot_claim_loaded(self):
        self.assertEqual(
            tracker_import_state(True, 3, 2, False),
            {'state': 'unknown', 'inputRows': 3, 'matchedRows': 2},
        )

    def test_malformed_existing_source_is_reported_and_keeps_old_source_only_as_fallback(self):
        registry = {'known-task': {'source': 'local', 'format': 'task-library'}}
        errors = []
        handled = apply_existing_tracker_source(
            'known-task', {'Source Repo': 'https://example.com/not-github'}, registry, errors)
        self.assertTrue(handled)
        self.assertEqual(registry['known-task']['source'], 'local')
        self.assertEqual(len(errors), 1)
        self.assertIn('known-task', errors[0])
        self.assertIn('not a recognizable GitHub URL', errors[0])


if __name__ == '__main__':
    unittest.main()
