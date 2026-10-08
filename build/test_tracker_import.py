"""Offline tests for canonical membership and operational field authority."""
import copy
import hashlib
from datetime import datetime, timezone
import csv
import io
import json
import os
import re
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

import build
from build import parse_tracker_csv, tracker_import_state


class TrackerImportTests(unittest.TestCase):
    def setUp(self):
        self.registry = {'known-task': {
            'source': 'github:example/recipes@' + 'a' * 40 + ':skills/known-task/SKILL.md',
            'download': 'https://github.com/example/recipes/archive/' + 'a' * 40 + '.zip',
            'category': 'Strategy & Measurement', 'status': 'needs-work'}}
        self.headers = ['Slug', 'Catalog match', 'Approved display Owner', 'Status']

    def csv(self, rows, extra=()):
        out = io.StringIO()
        writer = csv.DictWriter(out, fieldnames=self.headers + list(extra))
        writer.writeheader()
        writer.writerows(rows)
        return out.getvalue()

    def row(self, **values):
        return dict({'Slug': 'known-task', 'Catalog match': 'catalog',
                     'Approved display Owner': '', 'Status': ''}, **values)

    def receipt(self, input_bytes, registry=None, **updates):
        registry = self.registry if registry is None else registry
        receipt = {'schemaVersion': 1, 'catalogCommit': 'a' * 40,
                   'catalogSha256': hashlib.sha256(json.dumps(registry, sort_keys=True).encode()).hexdigest(),
                   'inputSha256': hashlib.sha256(input_bytes).hexdigest(),
                   'exportedAt': '2026-10-08T12:00:00Z',
                   'approvedPublicFields': ['Approved display Owner', 'Status']}
        receipt.update(updates)
        return receipt

    def main_receipt_args(self, tracker):
        registry = json.loads((Path(build.BUILD) / 'registry.json').read_text())['skills']
        catalog_commit = build.subprocess.check_output(
            ['git', 'rev-parse', '--verify', 'HEAD^{commit}'], cwd=build.ROOT, text=True).strip()
        receipt = self.receipt(tracker.read_bytes(), registry,
                               catalogCommit=catalog_commit,
                               exportedAt=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'))
        receipt_path = tracker.parent / 'receipt.json'
        receipt_path.write_text(json.dumps(receipt))
        return ['--tracker-receipt', str(receipt_path), '--tracker-max-age-seconds', '60']

    def offline_resolve(self, slug, entry, errors, warnings, states):
        states[slug] = 'local' if entry['source'] == 'local' else 'cached'
        if entry['source'] == 'local':
            return (Path(build.ROOT) / 'skills' / build.folder_of(entry['category']) /
                    (slug + '.md')).read_text()
        return ('---\nname: ' + slug + '\ndescription: Synthetic offline fixture.\n---\n'
                '# Synthetic fixture\n\nUse the synthetic recipe.\n')

    def test_import_states_preserve_existing_dashboard_contract(self):
        for supplied, valid, state in [(False, True, 'not_configured'),
                                      (True, True, 'loaded'), (True, False, 'unknown')]:
            self.assertEqual(tracker_import_state(supplied, 4, 2, valid),
                             {'state': state, 'inputRows': 4, 'matchedRows': 2})

    def test_held_rows_cannot_create_or_override_even_known_slug(self):
        for slug in ['candidate-task', 'known-task']:
            rows = [self.row(**{'Slug': slug, 'Catalog match': 'held', 'Approved display Owner': 'Hidden',
                               'Status': 'ready'})]
            registry = {} if slug == 'known-task' else self.registry
            if registry:
                rows.insert(0, self.row())
            overrides, receipt = parse_tracker_csv(self.csv(rows), registry)
            self.assertNotIn(slug, overrides)
            self.assertEqual(receipt['excludedHeldRows'], 1)
        with self.assertRaisesRegex(ValueError, 'partial'):
            parse_tracker_csv(self.csv([self.row(**{'Catalog match': 'held'})]), self.registry)

    def test_missing_unknown_membership_fail_closed(self):
        for value in ['', 'ready', 'unknown', 'CATALOG']:
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'Catalog match'):
                parse_tracker_csv(self.csv([self.row(**{'Catalog match': value})]), self.registry)
        with self.assertRaisesRegex(ValueError, 'headers'):
            parse_tracker_csv('Slug,Owner\nknown-task,Someone\n', self.registry)

    def test_duplicates_including_held_and_catalog_fail(self):
        for membership in ['held', 'catalog']:
            with self.assertRaisesRegex(ValueError, 'duplicate Slug'):
                parse_tracker_csv(self.csv([self.row(), self.row(**{'Catalog match': membership})]),
                                  self.registry)

    def test_empty_invalid_or_mismatched_slug_fail_without_private_values(self):
        for slug in ['', 'Known-task', 'other-task', 'https://private.invalid/client']:
            with self.assertRaises(ValueError) as error:
                parse_tracker_csv(self.csv([self.row(**{'Slug': slug})]), self.registry)
            self.assertNotIn('private.invalid', str(error.exception))

    def test_allowlist_preserves_reviewed_pins_and_authorized_updates(self):
        extra = ['Source Repo', 'Download URL', 'Description', 'Flags',
                 'Definitive Article URL', 'Category', 'Stage', 'Task Title']
        row = self.row(**{'Approved display Owner': 'Approved Display', 'Status': 'ready'})
        row.update({field: 'https://private.invalid/client-secret' for field in extra})
        row['Source Repo'] = 'https://github.com/example/recipes'
        row['Download URL'] = 'https://github.com/example/recipes/archive/refs/heads/main.zip'
        before = copy.deepcopy(self.registry)
        overrides, receipt = parse_tracker_csv(self.csv([row], extra), self.registry)
        self.assertEqual(self.registry, before)
        self.assertEqual(overrides['known-task'], {'Slug': 'known-task',
                                                  'Approved display Owner': 'Approved Display', 'Status': 'ready'})
        self.assertNotIn('private.invalid', json.dumps([overrides, receipt]))
        self.assertEqual(len(receipt['inputSha256']), 64)
        self.assertIsNone(receipt['exportedAt'])

    def test_blank_operational_values_preserve_source_status(self):
        overrides, _ = parse_tracker_csv(self.csv([self.row()]), self.registry)
        row = overrides['known-task']
        self.assertEqual(build.TRACKER_STATUSES.get(row['Status'], 'needs-work'), 'needs-work')
        self.assertEqual(row['Approved display Owner'], '')

    def test_unknown_status_and_non_display_owner_rejected(self):
        for field, value in [('Status', 'verified'), ('Approved display Owner', 'https://private.invalid'),
                             ('Approved display Owner', '<script>'), ('Approved display Owner', 'name\nsecret')]:
            with self.assertRaises(ValueError) as error:
                parse_tracker_csv(self.csv([self.row(**{field: value})]), self.registry)
            self.assertNotIn(value, str(error.exception))

    def test_synthetic_full_catalog_and_held_candidates(self):
        registry = {f'task-{i}': {} for i in range(276)}
        rows = [self.row(**{'Slug': slug, 'Approved display Owner': 'Approved Display' if i < 6 else ''})
                for i, slug in enumerate(registry)]
        rows += [self.row(**{'Slug': f'candidate-{i}', 'Catalog match': 'held',
                            'Approved display Owner': 'Hidden', 'Status': 'ready'}) for i in range(12)]
        overrides, receipt = parse_tracker_csv(self.csv(rows), registry)
        self.assertEqual(len(overrides), 276)
        self.assertEqual(receipt['inputRows'], 288)
        self.assertEqual(receipt['excludedHeldRows'], 12)
        self.assertEqual(sum(bool(row['Approved display Owner']) for row in overrides.values()), 6)

    def test_empty_html_malformed_partial_or_duplicate_headers_fail(self):
        for text in ['', '<html>Private error</html>', 'Slug,Catalog match\n',
                     'Slug,Catalog match\nknown-task\n',
                     'Slug,Catalog match\nknown-task,catalog,extra\n',
                     'Slug,Catalog match\n"known-task,catalog',
                     'Slug,Slug,Catalog match\nknown-task,known-task,catalog\n']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_tracker_csv(text, self.registry)
        with self.assertRaisesRegex(ValueError, 'partial'):
            parse_tracker_csv(self.csv([self.row()]), dict(self.registry, **{'second-task': {}}))

    def test_invalid_import_leaves_last_output_and_never_fetches_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'data.json'
            output.write_text('last successful artifact')
            tracker = Path(directory) / 'private-path.csv'
            tracker.write_text('Slug,Owner\nknown-task,Private Owner\n')
            with patch.object(sys, 'argv', ['build.py', '--tracker-csv', str(tracker),
                                          '--out', str(output)] + self.main_receipt_args(tracker)), patch.object(build, 'resolve') as resolve:
                with self.assertRaises(SystemExit) as error:
                    build.main()
                self.assertNotIn('Private Owner', str(error.exception))
                self.assertNotIn('private-path', str(error.exception))
                resolve.assert_not_called()
            self.assertEqual(output.read_text(), 'last successful artifact')

    def test_authorized_import_reaches_artifacts_without_private_fields_or_pin_changes(self):
        registry = json.loads((Path(build.BUILD) / 'registry.json').read_text())['skills']
        pinned_slug = next(slug for slug, entry in registry.items()
                           if '@86e7acdd22325566203e213b8c0c86e8583576e9:' in entry['source'])
        pinned_download = registry[pinned_slug]['download']
        rows = [self.row(**{'Slug': slug, 'Approved display Owner': 'Approved Display' if slug == pinned_slug else '',
                            'Status': 'wip' if slug == pinned_slug else '',
                            'Source Repo': 'https://github.com/example/recipes',
                            'Download URL': 'https://private.invalid/secret',
                            'Description': 'PRIVATE-TRACKER-MARKER',
                            'Flags': 'PRIVATE-TRACKER-MARKER'}) for slug in registry]
        rows.append(self.row(**{'Slug': 'held-candidate', 'Catalog match': 'held',
                                'Approved display Owner': 'PRIVATE-TRACKER-MARKER', 'Status': 'ready',
                                'Source Repo': 'https://private.invalid/candidate'}))
        rows.append(self.row(**{'Slug': 'source-less-candidate', 'Catalog match': 'held',
                                'Approved display Owner': 'PRIVATE-TRACKER-MARKER', 'Status': 'ready'}))

        with tempfile.TemporaryDirectory() as directory:
            tracker = Path(directory) / 'tracker.csv'
            tracker.write_text(self.csv(rows, ['Source Repo', 'Download URL', 'Description', 'Flags']))
            output = Path(directory) / 'data.json'
            with patch.object(sys, 'argv', ['build.py', '--tracker-csv', str(tracker),
                                          '--out', str(output)] + self.main_receipt_args(tracker)), \
                    patch.object(build, 'resolve', side_effect=self.offline_resolve), \
                    patch.object(build.factory, 'write_incomplete_inventory', return_value=0), \
                    patch('builtins.print'):
                with self.assertRaises(SystemExit) as result:
                    build.main()
                self.assertEqual(result.exception.code, 0)
            data = json.loads(output.read_text())
            tasks = {task['slug']: task for category in data['categories'] for task in category['tasks']}
            self.assertEqual(set(tasks), set(registry))
            self.assertEqual(tasks[pinned_slug]['owner'], 'Approved Display')
            self.assertEqual(tasks[pinned_slug]['status'], 'needs-work')
            self.assertEqual(tasks[pinned_slug]['download'], pinned_download)
            self.assertEqual(data['trackerImport']['excludedHeldRows'], 2)
            self.assertEqual(data['trackerImport']['matchedRows'], len(registry))
            self.assertIn('cached', data['trackerImport']['sourceStates'])
            for artifact in Path(directory).iterdir():
                if artifact in {tracker, tracker.parent / 'receipt.json'}:
                    continue
                if artifact.suffix == '.zip':
                    with zipfile.ZipFile(artifact) as archive:
                        content = b'\n'.join(archive.read(name) for name in archive.namelist())
                else:
                    content = artifact.read_bytes()
                self.assertNotIn(b'PRIVATE-TRACKER-MARKER', content)
                self.assertNotIn(b'private.invalid', content)

    def test_both_workflows_use_shared_import_validation(self):
        for name in ['build.yml', 'ownership-map.yml']:
            source = (Path(build.ROOT) / '.github' / 'workflows' / name).read_text()
            self.assertIn('python3 build/build.py --tracker-csv tracker.csv', source)
            self.assertIn('tracker activation blocked', source)
            self.assertIn('exit 1', source)
            self.assertNotIn('curl ', source)


    def test_workflow_activation_guard_rejects_feed_and_preserves_no_feed_path(self):
        for name in ['build.yml', 'ownership-map.yml']:
            source = (Path(build.ROOT) / '.github' / 'workflows' / name).read_text()
            step = source.split('      - name: Fetch Asset Tracker CSV', 1)[1].split('      - name:', 1)[0]
            script = step.split('        run: |\n', 1)[1]
            script = '\n'.join(line[10:] for line in script.splitlines())
            with tempfile.TemporaryDirectory() as directory:
                for feed, expected in [('', 0), ('https://example.invalid/export', 1)]:
                    result = build.subprocess.run(
                        ['sh', '-c', script], cwd=directory, capture_output=True, text=True,
                        env={'PATH': os.environ['PATH'], 'TRACKER_CSV_URL': feed})
                    self.assertEqual(result.returncode, expected)
                    self.assertIn('activation blocked' if feed else 'building without the sheet', result.stdout)
                    self.assertFalse((Path(directory) / 'tracker.csv').exists())

    def test_invalid_encoding_never_echoes_private_bytes_or_path(self):
        with tempfile.TemporaryDirectory() as directory:
            tracker = Path(directory) / 'private-path.csv'
            tracker.write_bytes(b'PRIVATE-TRACKER-MARKER' + bytes([255]))
            with patch.object(sys, 'argv', ['build.py', '--tracker-csv', str(tracker)] + self.main_receipt_args(tracker)):
                with self.assertRaises(SystemExit) as result:
                    build.main()
            self.assertEqual(str(result.exception), 'ERROR: tracker could not be read as UTF-8 CSV')


    def validate_receipt(self, receipt, raw=b'fixture', policy=60, now=None):
        return build.validate_tracker_receipt(
            receipt, raw, self.registry, 'a' * 40, policy,
            now=now or datetime(2026, 10, 8, 12, 0, 30, tzinfo=timezone.utc))

    def test_receipt_binds_exact_checkout_registry_and_csv_bytes(self):
        receipt = self.receipt(b'fixture')
        provenance = self.validate_receipt(receipt)
        self.assertEqual(provenance['exportedAt'], '2026-10-08T12:00:00Z')
        self.assertEqual(provenance['maxAgeSeconds'], 60)
        for key, value in [('catalogCommit', 'b' * 40), ('catalogCommit', ''),
                           ('catalogSha256', 'b' * 64), ('inputSha256', 'b' * 64)]:
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                self.validate_receipt(dict(receipt, **{key: value}))
        with self.assertRaisesRegex(ValueError, 'exactly'):
            del receipt['catalogCommit']
            self.validate_receipt(receipt)

    def test_freshness_requires_explicit_policy_and_rejects_missing_stale_future_dates(self):
        receipt = self.receipt(b'fixture')
        for policy in [None, 0, -1, True, '60']:
            with self.subTest(policy=policy), self.assertRaisesRegex(ValueError, 'policy'):
                self.validate_receipt(receipt, policy=policy)
        for timestamp in [None, '', '2026-10-08', '2026-10-08T12:00:00',
                          '2026-10-08T11:59:00Z', '2026-10-08T12:01:00Z']:
            with self.subTest(timestamp=timestamp), self.assertRaises(ValueError):
                self.validate_receipt(dict(receipt, exportedAt=timestamp))
        self.validate_receipt(receipt, now=datetime(2026, 10, 8, 12, 1, tzinfo=timezone.utc))
        with self.assertRaisesRegex(ValueError, 'stale'):
            self.validate_receipt(receipt, now=datetime(2026, 10, 8, 12, 1, 0, 1, tzinfo=timezone.utc))

    def test_no_feed_build_succeeds_without_receipt_or_policy(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'data.json'
            with patch.object(sys, 'argv', ['build.py', '--out', str(output)]), \
                    patch.object(build, 'resolve', side_effect=self.offline_resolve), \
                    patch.object(build, 'load_tracker_import') as importer, \
                    patch.object(build.factory, 'write_incomplete_inventory', return_value=0), \
                    patch('builtins.print'):
                with self.assertRaises(SystemExit) as result:
                    build.main()
                self.assertEqual(result.exception.code, 0)
                importer.assert_not_called()
            data = json.loads(output.read_text())
            self.assertEqual(data['trackerImport']['state'], 'not_configured')
            self.assertEqual(data['stats']['total'], 276)

    def test_import_cannot_activate_without_receipt_or_freshness_policy(self):
        for options, message in [([], 'tracker-receipt'),
                                 (['--tracker-receipt', 'unused'], 'tracker-max-age-seconds')]:
            with patch.object(sys, 'argv', ['build.py', '--tracker-csv', 'unused'] + options), \
                    patch.object(build, 'resolve') as resolve:
                with self.assertRaisesRegex(SystemExit, message):
                    build.main()
                resolve.assert_not_called()

    def test_missing_or_renamed_operational_headers_fail_before_sources_or_output(self):
        registry = json.loads((Path(build.BUILD) / 'registry.json').read_text())['skills']
        valid = self.csv([self.row(**{'Slug': slug}) for slug in registry])
        for header in ['Approved display Owner', 'Status']:
            for replacement in ['', 'Renamed internal column']:
                text = valid.replace(header, replacement, 1)
                with tempfile.TemporaryDirectory() as directory:
                    tracker = Path(directory) / 'tracker.csv'
                    tracker.write_text(text)
                    output = Path(directory) / 'data.json'
                    output.write_text('last successful artifact')
                    with patch.object(sys, 'argv', ['build.py', '--tracker-csv', str(tracker),
                                                   '--out', str(output)] + self.main_receipt_args(tracker)), \
                            patch.object(build, 'resolve') as resolve:
                        with self.assertRaisesRegex(SystemExit, 'headers'):
                            build.main()
                        resolve.assert_not_called()
                    self.assertEqual(output.read_text(), 'last successful artifact')

    def test_internal_owner_never_becomes_public_display_owner(self):
        rows = [self.row(**{'Owner': 'PRIVATE-TRACKER-MARKER'})]
        overrides, _ = parse_tracker_csv(self.csv(rows, ['Owner']), self.registry)
        self.assertEqual(overrides['known-task']['Approved display Owner'], '')
        self.assertNotIn('PRIVATE-TRACKER-MARKER', json.dumps(overrides))
        with self.assertRaisesRegex(ValueError, 'headers'):
            parse_tracker_csv('Slug,Catalog match,Owner,Status\nknown-task,catalog,Someone,wip\n',
                              self.registry)

    def test_display_owner_publication_requires_receipt_field_approval(self):
        with tempfile.TemporaryDirectory() as directory:
            tracker = Path(directory) / 'tracker.csv'
            registry = json.loads((Path(build.BUILD) / 'registry.json').read_text())['skills']
            rows = [self.row(**{'Slug': slug, 'Approved display Owner': 'Reviewed Display'})
                    for slug in registry]
            tracker.write_text(self.csv(rows))
            args = self.main_receipt_args(tracker)
            receipt_path = tracker.parent / 'receipt.json'
            receipt = json.loads(receipt_path.read_text())
            receipt['approvedPublicFields'] = ['Status']
            receipt_path.write_text(json.dumps(receipt))
            with patch.object(build, 'resolve') as resolve, \
                    patch.object(sys, 'argv', ['build.py', '--tracker-csv', str(tracker)] + args):
                with self.assertRaisesRegex(SystemExit, 'explicit receipt approval'):
                    build.main()
                resolve.assert_not_called()
            receipt['approvedPublicFields'] = ['Owner', 'Status']
            with self.assertRaisesRegex(ValueError, 'allowlist'):
                self.validate_receipt(self.receipt(b'fixture', approvedPublicFields=['Owner']))

    def test_enabled_import_revision_stale_future_or_missing_receipt_never_writes_output(self):
        with tempfile.TemporaryDirectory() as directory:
            tracker = Path(directory) / 'tracker.csv'
            tracker.write_text(self.csv([self.row()]))
            args = self.main_receipt_args(tracker)
            receipt_path = tracker.parent / 'receipt.json'
            baseline = json.loads(receipt_path.read_text())
            variants = [dict(baseline, catalogCommit='b' * 40),
                        dict(baseline, exportedAt='2000-01-01T00:00:00Z'),
                        dict(baseline, exportedAt='9999-01-01T00:00:00Z'),
                        {key: value for key, value in baseline.items() if key != 'exportedAt'}]
            output = Path(directory) / 'data.json'
            for receipt in variants:
                receipt_path.write_text(json.dumps(receipt))
                output.write_text('last successful artifact')
                with patch.object(sys, 'argv', ['build.py', '--tracker-csv', str(tracker),
                                               '--out', str(output)] + args), \
                        patch.object(build, 'resolve') as resolve:
                    with self.assertRaises(SystemExit):
                        build.main()
                    resolve.assert_not_called()
                self.assertEqual(output.read_text(), 'last successful artifact')



if __name__ == '__main__':
    unittest.main()
