#!/usr/bin/env python3
"""Lock status-aware article labels and the current article inventory."""
import copy
import json
import os
import re
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build as task_build  # noqa: E402


class ArticleStateDerivation(unittest.TestCase):
    def test_shared_url_with_complete_and_wip_tasks_is_wip(self):
        tasks = [
            {'slug': 'done', 'status': 'complete',
             'article': 'http://www.blitzmetrics.com/shared/?utm_source=test#top'},
            {'slug': 'unfinished', 'status': 'needs-work',
             'article': 'https://blitzmetrics.com/shared'},
        ]

        stats = task_build.derive_article_states(tasks)

        self.assertEqual(stats, {'articleHubs': 1, 'definitiveArticles': 0})
        self.assertEqual({t['articleState'] for t in tasks}, {'wip'})

    def test_all_complete_tasks_on_shared_url_are_ready(self):
        tasks = [
            {'slug': 'one', 'status': 'complete',
             'article': 'https://example.com/ready/'},
            {'slug': 'two', 'status': 'complete',
             'article': 'http://example.com:80/ready'},
        ]

        stats = task_build.derive_article_states(tasks)

        self.assertEqual(stats, {'articleHubs': 1, 'definitiveArticles': 1})
        self.assertEqual({t['articleState'] for t in tasks}, {'ready'})

    def test_reviewed_semantic_hold_downgrades_complete_hub_only(self):
        url = 'https://example.com/semantically-wrong/'
        tasks = [
            {'slug': 'one', 'status': 'complete', 'article': url},
            {'slug': 'two', 'status': 'complete', 'article': url},
        ]
        holds = {
            task_build.normalize_article_url(url): {
                'state': 'wip',
                'reason': 'Reviewed framework labels do not match the canonical source.',
                'reviewed': '2026-08-22',
            }
        }

        stats = task_build.derive_article_states(tasks, certifications=holds)

        self.assertEqual(stats, {'articleHubs': 1, 'definitiveArticles': 0})
        self.assertEqual({t['status'] for t in tasks}, {'complete'})
        self.assertEqual({t['articleState'] for t in tasks}, {'wip'})
        self.assertEqual(
            {t['articleStateReason'] for t in tasks},
            {'Reviewed framework labels do not match the canonical source.'})
        self.assertEqual({t['articleStateReviewed'] for t in tasks}, {'2026-08-22'})

    def test_certification_config_cannot_force_a_hub_ready(self):
        payload = {
            'articles': {
                'https://example.com/not-reviewed/': {
                    'state': 'ready',
                    'reason': 'An override must never promote a hub.',
                    'reviewed': '2026-08-22',
                }
            }
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = os.path.join(temp_dir, 'article-certifications.json')
            with open(path, 'w', encoding='utf-8') as fh:
                json.dump(payload, fh)
            with self.assertRaisesRegex(ValueError, 'fail-closed "wip" hold'):
                task_build.load_article_certifications(path)

    def test_unused_hold_is_rejected_after_final_url_resolution(self):
        tasks = [
            {'slug': 'tracker-won', 'status': 'complete',
             'article': 'https://example.com/tracker-override/'},
        ]
        holds = {
            'example.com/canonical': {
                'state': 'wip', 'reason': 'Reviewed hold.', 'reviewed': '2026-08-22'}
        }

        with self.assertRaisesRegex(ValueError, 'do not match any final article URL'):
            task_build.validate_article_certifications(tasks, holds)

    def test_certification_reason_and_date_must_be_valid(self):
        invalid_entries = (
            {'state': 'wip', 'reason': 123, 'reviewed': '2026-08-22'},
            {'state': 'wip', 'reason': 'Reviewed hold.', 'reviewed': '2026-99-99'},
        )
        for entry in invalid_entries:
            with self.subTest(entry=entry), tempfile.TemporaryDirectory() as temp_dir:
                path = os.path.join(temp_dir, 'article-certifications.json')
                with open(path, 'w', encoding='utf-8') as fh:
                    json.dump({'articles': {'https://example.com/held/': entry}}, fh)
                with self.assertRaises(ValueError):
                    task_build.load_article_certifications(path)

    def test_missing_or_invalid_article_is_excluded(self):
        tasks = [
            {'slug': 'none', 'status': 'complete', 'article': None},
            {'slug': 'blank', 'status': 'complete', 'article': ''},
            {'slug': 'gap', 'status': 'complete', 'article': 'GAP — to be written'},
            {'slug': 'bad-port', 'status': 'complete', 'article': 'https://example.com:nope/hub'},
            {'slug': 'absent', 'status': 'complete'},
        ]

        stats = task_build.derive_article_states(tasks)

        self.assertEqual(stats, {'articleHubs': 0, 'definitiveArticles': 0})
        self.assertTrue(all('articleState' not in t for t in tasks))

    def test_meta_orbit_strength_never_overrides_a_semantic_hold(self):
        url = 'https://example.com/held/'
        tasks = [{'slug': 'held-task', 'status': 'complete', 'article': url,
                  'importance': 5}]
        holds = {
            task_build.normalize_article_url(url): {
                'state': 'wip', 'reason': 'Reviewed mismatch.',
                'reviewed': '2026-08-24'}
        }
        task_build.derive_article_states(tasks, certifications=holds)
        records = [{'sourceUrl': f'https://example.com/meta-{i}/',
                    'evidenceMethod': 'Public backlink read-back.',
                    'counted': True, 'reason': 'Verified meta-article.',
                    'taskSlugs': ['held-task']} for i in range(11)]
        audits = {task_build.normalize_article_url(url): {
            'hubUrl': url, 'metaCountStatus': 'verified',
            'audited': '2026-08-24',
            'evidenceSourceUrl': 'https://example.com/audit-receipt/',
            'evidenceMethod': 'Complete source inventory and backlink read-back.',
            'records': records}}

        hubs, stats = task_build.derive_article_hub_inventory(
            tasks, audits, 'https://local-service-spotlight.github.io/task-library/')

        self.assertEqual(hubs[0]['state'], 'wip')
        self.assertEqual(hubs[0]['metaArticleCount'], 11)
        self.assertEqual(hubs[0]['metaOrbitStrength'], 4)
        self.assertEqual(hubs[0]['metaOrbitTier'], 'Deep')
        self.assertEqual(hubs[0]['taskMetaCounts'], {'held-task': 11})
        self.assertEqual(hubs[0]['tasksWithMeta'], 1)
        self.assertEqual(hubs[0]['taskCoverage'], 1.0)
        self.assertEqual(hubs[0]['priorityCoverage'], 1.0)
        self.assertEqual(stats['verifiedMetaArticles'], 11)

    def test_unaudited_meta_count_is_unknown_not_zero(self):
        tasks = [{'slug': 'one', 'status': 'complete',
                  'article': 'https://example.com/ready/', 'importance': 4}]
        task_build.derive_article_states(tasks, certifications={})

        hubs, stats = task_build.derive_article_hub_inventory(
            tasks, {}, 'https://local-service-spotlight.github.io/task-library/')

        self.assertIsNone(hubs[0]['metaArticleCount'])
        self.assertEqual(hubs[0]['metaCountStatus'], 'unknown')
        self.assertIsNone(hubs[0]['metaOrbitStrength'])
        self.assertEqual(hubs[0]['metaOrbitTier'], 'Unknown')
        self.assertEqual(stats['metaOrbitHubsUnknown'], 1)
        self.assertNotIn('metaArticleCount', tasks[0])

    def test_bidirectional_hub_and_task_routes_use_stable_live_shape(self):
        tasks = [{'slug': 'exact-task', 'status': 'complete',
                  'article': 'https://example.com/ready/', 'importance': 4}]
        task_build.derive_article_states(tasks, certifications={})
        hubs, _ = task_build.derive_article_hub_inventory(
            tasks, {}, 'https://local-service-spotlight.github.io/task-library/')

        self.assertEqual(
            hubs[0]['taskLibraryUrl'],
            'https://local-service-spotlight.github.io/task-library/'
            '?article=https%3A%2F%2Fexample.com%2Fready%2F')
        self.assertEqual(
            task_build.task_library_route(
                'https://local-service-spotlight.github.io/task-library/',
                'task', tasks[0]['slug']),
            'https://local-service-spotlight.github.io/task-library/?task=exact-task'
            '#task-exact-task')
        self.assertEqual(
            tasks[0]['taskLibraryUrl'],
            'https://local-service-spotlight.github.io/task-library/?task=exact-task'
            '#task-exact-task')


class MetaOrbitEvidenceSchema(unittest.TestCase):
    def write_manifest(self, payload, temp_dir):
        path = os.path.join(temp_dir, 'article-meta-orbits.json')
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(payload, fh)
        return path

    def valid_audit(self):
        return {
            'hub_url': 'https://example.com/hub/',
            'meta_count_status': 'verified',
            'audited': '2026-08-24',
            'evidence_source_url': 'https://example.com/audit/',
            'evidence_method': 'Complete live inventory with backlink read-back.',
            'records': [{
                'source_url': 'https://example.com/meta/',
                'hub_url': 'http://www.example.com/hub#canonical',
                'evidence_method': 'Rendered backlink and canonical URL verified.',
                'counted': True,
                'reason': 'Documents a real run and links to the canonical hub.',
                'task_slugs': ['one'],
            }],
        }

    def test_valid_records_are_normalized_and_preserve_evidence(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_manifest({'hubs': [self.valid_audit()]}, temp_dir)
            audits = task_build.load_article_meta_orbits(path)

        self.assertEqual(set(audits), {'example.com/hub'})
        record = audits['example.com/hub']['records'][0]
        self.assertTrue(record['counted'])
        self.assertEqual(record['hubUrl'], 'https://example.com/hub/')
        self.assertEqual(record['taskSlugs'], ['one'])
        self.assertIn('backlink', record['evidenceMethod'])

    def test_empty_manifest_leaves_every_hub_unknown(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_manifest({'hubs': []}, temp_dir)
            self.assertEqual(task_build.load_article_meta_orbits(path), {})

    def test_invalid_or_unverifiable_record_fails_closed(self):
        mutations = [
            lambda a: a['records'][0].pop('reason'),
            lambda a: a['records'][0].update(counted='yes'),
            lambda a: a['records'][0].update(hub_url='https://example.com/other/'),
            lambda a: a.update(meta_count_status='unknown'),
            lambda a: a.update(audited='2026-99-99'),
        ]
        for mutate in mutations:
            audit = self.valid_audit()
            mutate(audit)
            with self.subTest(audit=audit), tempfile.TemporaryDirectory() as temp_dir:
                path = self.write_manifest({'hubs': [audit]}, temp_dir)
                with self.assertRaises(ValueError):
                    task_build.load_article_meta_orbits(path)

    def test_task_evidence_must_belong_to_the_same_hub(self):
        audit = self.valid_audit()
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_manifest({'hubs': [audit]}, temp_dir)
            audits = task_build.load_article_meta_orbits(path)
        tasks = [{'slug': 'different-task', 'article': 'https://example.com/hub/'}]
        with self.assertRaisesRegex(ValueError, 'not mapped'):
            task_build.validate_article_meta_orbits(tasks, audits)

    def test_wordpress_strength_manifest_shape_is_accepted_and_rederived(self):
        payload = {
            'schemaVersion': 1,
            'generatedAt': '2026-08-24T07:05:18+00:00',
            'countDefinition': 'Published meta taxonomy plus exact normalized body link.',
            'hubs': [{
                'url': 'https://example.com/hub/',
                'taskLibrarySourceUrl': 'https://example.com/hub/',
                'taskCount': 1,
                'taskImportanceTotal': 5,
                'tasks': [{'slug': 'one', 'title': 'One', 'importance': 5}],
                'metaCountStatus': 'verified',
                'metaArticleCount': 1,
                'strength': {'score': 1, 'label': 'Emerging', 'band': '1-2'},
                'metaArticles': [{
                    'url': 'https://example.com/meta/',
                    'sourceUrl': 'https://example.com/meta/',
                    'hubUrl': 'https://example.com/hub/',
                    'title': 'A verified run',
                    'postId': 123,
                    'primaryParentHub': 'https://example.com/hub/',
                    'evidenceMethod': 'Exact normalized URL in editable body.',
                    'counted': True,
                    'reason': 'Published and explicitly classified.',
                }],
            }],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_manifest(payload, temp_dir)
            audits = task_build.load_article_meta_orbits(
                path, evidence_url='https://example.com/meta-orbits.json')

        audit = audits['example.com/hub']
        self.assertEqual(audit['metaCountStatus'], 'verified')
        self.assertEqual(audit['expectedTaskCount'], 1)
        self.assertEqual(audit['expectedImportanceTotal'], 5)
        self.assertEqual(audit['expectedTasks'], {'one': 5})
        self.assertEqual(audit['evidenceSourceUrl'],
                         'https://example.com/meta-orbits.json')
        self.assertEqual(audit['records'][0]['title'], 'A verified run')
        self.assertEqual(audit['records'][0]['postId'], 123)
        self.assertEqual(audit['records'][0]['hubUrl'],
                         'https://example.com/hub/')
        self.assertEqual(audit['records'][0]['primaryParentHub'],
                         'https://example.com/hub/')
        tasks = [{'slug': 'one', 'article': 'https://example.com/hub/',
                  'importance': 5}]
        task_build.validate_article_meta_orbits(tasks, audits)

    def test_one_meta_article_may_prove_multiple_hubs_but_global_count_is_unique(self):
        tasks = [
            {'slug': 'one', 'status': 'complete', 'article': 'https://example.com/a/',
             'importance': 5},
            {'slug': 'two', 'status': 'complete', 'article': 'https://example.com/b/',
             'importance': 4},
        ]
        task_build.derive_article_states(tasks, certifications={})
        shared = 'https://example.com/shared-meta/'
        audits = {}
        for suffix in ('a', 'b'):
            key = f'example.com/{suffix}'
            audits[key] = {
                'hubUrl': f'https://example.com/{suffix}/',
                'metaCountStatus': 'verified', 'audited': '2026-08-24',
                'evidenceSourceUrl': 'https://example.com/meta-orbits.json',
                'evidenceMethod': 'Complete backlink inventory.',
                'records': [{'sourceUrl': shared, 'evidenceMethod': 'Exact backlink.',
                             'counted': True, 'reason': 'Documents both systems.'}],
            }

        hubs, stats = task_build.derive_article_hub_inventory(tasks, audits)

        self.assertEqual([hub['metaArticleCount'] for hub in hubs], [1, 1])
        self.assertEqual(stats['verifiedMetaArticles'], 1)

    def test_public_orbit_projection_uses_current_build_stats(self):
        audit = {
            'hubUrl': 'https://example.com/hub/',
            'metaCountStatus': 'verified', 'audited': '2026-08-24',
            'evidenceSourceUrl': 'https://example.com/meta-orbits.json',
            'evidenceMethod': 'Complete backlink inventory.',
            'records': [{'sourceUrl': 'https://example.com/meta/',
                         'hubUrl': 'https://example.com/hub/',
                         'evidenceMethod': 'Exact backlink.', 'counted': True,
                         'reason': 'Verified run.', 'taskSlugs': ['one']}],
        }
        data = {
            'stats': {'articleHubs': 1, 'definitiveArticles': 1,
                      'verifiedMetaArticles': 1,
                      'metaOrbitHubsWithEvidence': 1,
                      'metaOrbitHubsUnknown': 0},
            'articleHubs': [{
                'key': 'example.com/hub', 'url': 'https://example.com/hub/',
                'state': 'ready', 'taskCount': 1, 'completeTaskCount': 1,
                'importance': 5, 'importanceTotal': 5, 'taskSlugs': ['one'],
                'metaArticleCount': 1, 'metaCountStatus': 'verified',
                'metaOrbitStrength': 1, 'metaOrbitTier': 'Emerging',
                'metaArticles': ['https://example.com/meta/'],
                'priorityCoverage': 1.0,
            }],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = os.path.join(temp_dir, 'meta-orbits.json')
            task_build.write_meta_orbit_index(
                data, {'example.com/hub': audit}, path)
            with open(path, encoding='utf-8') as fh:
                public = json.load(fh)

        self.assertEqual(public['stats']['verifiedMetaArticles'], 1)
        self.assertEqual(public['hubs'][0]['metaArticleCount'], 1)
        self.assertEqual(public['hubs'][0]['records'][0]['sourceUrl'],
                         'https://example.com/meta/')
        self.assertEqual(public['hubs'][0]['records'][0]['hubUrl'],
                         'https://example.com/hub/')
        self.assertNotIn('taskLibraryStats', public)

    def test_manifest_task_totals_must_match_final_task_mapping(self):
        audit = self.valid_audit()
        audit['_expected_task_count'] = 2
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_manifest({'hubs': [audit]}, temp_dir)
            audits = task_build.load_article_meta_orbits(path)
        tasks = [{'slug': 'one', 'article': 'https://example.com/hub/', 'importance': 5}]
        with self.assertRaisesRegex(ValueError, 'task count disagrees'):
            task_build.validate_article_meta_orbits(tasks, audits)


class BuiltArticleInventory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(ROOT, 'dashboard', 'data.json'), encoding='utf-8') as fh:
            cls.data = json.load(fh)
        cls.tasks = [t for c in cls.data['categories'] for t in c['tasks']]

    def test_current_inventory_has_exact_derived_counts(self):
        self.assertEqual(self.data['stats']['articleHubs'], 24)
        self.assertEqual(self.data['stats']['definitiveArticles'], 13)

        tasks = copy.deepcopy(self.tasks)
        derived = task_build.derive_article_states(tasks)
        self.assertEqual(derived, {'articleHubs': 24, 'definitiveArticles': 13})

    def test_every_mapped_task_has_a_derived_state(self):
        for task in self.tasks:
            if task.get('article'):
                self.assertIn(task.get('articleState'), ('ready', 'wip'), task['slug'])
            else:
                self.assertNotIn('articleState', task, task['slug'])

    def test_known_redirecting_thank_you_hub_is_not_called_definitive(self):
        mapped = [t for t in self.tasks
                  if task_build.normalize_article_url(t.get('article')) ==
                  'blitzmetrics.com/thank-you-machine']
        self.assertEqual(len(mapped), 8)
        self.assertEqual({t['articleState'] for t in mapped}, {'wip'})

    def test_nine_triangles_uses_direct_url_and_semantic_hold(self):
        direct_url = ('https://blitzmetrics.com/'
                      '9-triangles-framework-scalable-home-service-businesses/')
        key = task_build.normalize_article_url(direct_url)
        mapped = [t for t in self.tasks
                  if task_build.normalize_article_url(t.get('article')) == key]

        self.assertEqual(len(mapped), 10)
        self.assertEqual({t['article'] for t in mapped}, {direct_url})
        self.assertEqual({t['status'] for t in mapped}, {'complete'})
        self.assertEqual({t['articleState'] for t in mapped}, {'wip'})
        reasons = {t.get('articleStateReason') for t in mapped}
        self.assertEqual(len(reasons), 1)
        reason = reasons.pop()
        for label in ('AEC', 'CID', 'SBP'):
            self.assertIn(label, reason)
        self.assertEqual({t.get('articleStateReviewed') for t in mapped},
                         {'2026-08-22'})
        self.assertFalse(any(
            task_build.normalize_article_url(t.get('article')) ==
            'blitzmetrics.com/nine-triangles' for t in self.tasks))

    def test_meta_article_mapping_uses_direct_url(self):
        mapped = [t for t in self.tasks
                  if t['slug'] == 'write-meta-article-documenting-agent-work']
        self.assertEqual(len(mapped), 1)
        self.assertEqual(mapped[0]['article'],
                         'https://blitzmetrics.com/meta-article-prompt/')
        self.assertEqual(mapped[0]['articleState'], 'ready')
        self.assertFalse(any(
            task_build.normalize_article_url(t.get('article')) ==
            'blitzmetrics.com/meta-article-prompt-template' for t in self.tasks))

    def test_positive_mentions_task_and_article_are_certified(self):
        mapped = [t for t in self.tasks
                  if t['slug'] == 'positive-mentions-harvester']

        self.assertEqual(len(mapped), 1)
        self.assertEqual(mapped[0]['status'], 'complete')
        self.assertEqual(mapped[0]['articleState'], 'ready')
        self.assertEqual(
            mapped[0]['article'],
            'https://blitzmetrics.com/how-to-collect-organize-positive-mentions-to-build-authority/')
        self.assertNotIn('flag', mapped[0])
        self.assertNotIn('articleStateReason', mapped[0])

    def test_blog_posting_mappings_use_current_lss_canonical_not_bm_archive(self):
        key = 'localservicespotlight.com/article-guidelines'
        mapped = [t for t in self.tasks
                  if task_build.normalize_article_url(t.get('article')) == key]
        self.assertEqual(len(mapped), 21)
        self.assertEqual({t['article'] for t in mapped},
                         {'https://localservicespotlight.com/article-guidelines/'})
        self.assertEqual({t['articleState'] for t in mapped}, {'ready'})
        self.assertFalse(any(
            task_build.normalize_article_url(t.get('article')) ==
            'blitzmetrics.com/blog-posting-guidelines' for t in self.tasks))

    def test_every_hub_has_a_reverse_article_route(self):
        self.assertEqual(len(self.data['articleHubs']), 24)
        for hub in self.data['articleHubs']:
            self.assertTrue(hub['taskLibraryUrl'].startswith(
                'https://local-service-spotlight.github.io/task-library/?article='))
            self.assertEqual(hub['taskCount'], len(hub['taskSlugs']))
        for task in self.tasks:
            if task.get('article'):
                self.assertEqual(
                    task['taskLibraryUrl'],
                    'https://local-service-spotlight.github.io/task-library/?task=' +
                    task['slug'] + '#task-' + task['slug'])

    def test_production_primary_orbit_manifest_is_exact_and_fail_closed(self):
        expected = {
            'localservicespotlight.com/article-guidelines': (3, 'Supported'),
            'blitzmetrics.com/content-factory': (10, 'Strong'),
            'blitzmetrics.com/how-to-collect-organize-positive-mentions-to-build-authority':
                (4, 'Supported'),
            'blitzmetrics.com/how-to-inventory-a-podcast-on-youtube':
                (1, 'Emerging'),
            'blitzmetrics.com/how-to-inventory-every-podcast-youve-been-on-and-why-its-one-of-the-highest-roi-things-you-can-do':
                (1, 'Emerging'),
            'blitzmetrics.com/how-we-use-listen-notes-to-find-track-and-repurpose-every-podcast-appearance':
                (1, 'Emerging'),
            'blitzmetrics.com/how-we-use-podchaser-to-amplify-authority-and-repurpose-podcast-content':
                (0, 'No verified examples'),
            'blitzmetrics.com/internal-linking': (1, 'Emerging'),
            'blitzmetrics.com/meta-article-prompt': (59, 'Deep'),
            'blitzmetrics.com/one-minute-video-guide':
                (0, 'No verified examples'),
            'blitzmetrics.com/overnight-content-worker': (1, 'Emerging'),
            'blitzmetrics.com/speaker-kit': (1, 'Emerging'),
            'blitzmetrics.com/topic-wheel': (2, 'Emerging'),
        }
        hubs = {hub['key']: hub for hub in self.data['articleHubs']}

        self.assertEqual(self.data['stats']['verifiedMetaArticles'], 84)
        self.assertEqual(self.data['stats']['metaOrbitHubsWithEvidence'], 13)
        self.assertEqual(self.data['stats']['metaOrbitHubsUnknown'], 11)
        self.assertEqual({key for key, hub in hubs.items()
                          if hub['state'] == 'ready'}, set(expected))
        for key, (count, tier) in expected.items():
            with self.subTest(hub=key):
                self.assertEqual(hubs[key]['metaCountStatus'], 'verified')
                self.assertEqual(hubs[key]['metaArticleCount'], count)
                self.assertEqual(hubs[key]['metaOrbitTier'], tier)
        self.assertTrue(all(hub['metaCountStatus'] == 'unknown'
                            for hub in hubs.values() if hub['state'] == 'wip'))
        self.assertTrue(all(hub['metaArticleCount'] is None
                            for hub in hubs.values() if hub['state'] == 'wip'))
        self.assertNotIn('blitzmetrics.com/blog-posting-guidelines', hubs)

        # Multi-task hubs need record-level task assignments before claiming
        # breadth. Their verified volume is still exact, but coverage is UNKNOWN.
        for key in ('localservicespotlight.com/article-guidelines',
                    'blitzmetrics.com/internal-linking',
                    'blitzmetrics.com/topic-wheel'):
            self.assertIsNone(hubs[key]['priorityCoverage'])

    def test_certification_config_is_reviewed_and_fail_closed(self):
        reviews = task_build.load_article_certifications()
        key = ('blitzmetrics.com/'
               '9-triangles-framework-scalable-home-service-businesses')
        self.assertIn(key, reviews)
        self.assertEqual(reviews[key]['state'], 'wip')
        self.assertEqual(reviews[key]['reviewed'], '2026-08-22')
        self.assertTrue(reviews[key]['reason'])
        self.assertEqual({review['state'] for review in reviews.values()}, {'wip'})


class ArticleLabelUI(unittest.TestCase):
    def test_root_and_dashboard_use_the_same_fail_closed_article_label(self):
        blocks = []
        for rel in ('app.js', os.path.join('dashboard', 'app.js')):
            with open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
                source = fh.read()
            match = re.search(r'function articleLink\(t\)\{.*?\n\}', source, re.S)
            self.assertIsNotNone(match, rel)
            blocks.append(match.group(0))
            self.assertIn("t.articleState === 'ready'", source)
            self.assertIn("'Definitive article ↗'", source)
            self.assertIn("'Article in progress ↗'", source)
            self.assertIn('t.articleStateReason', source)
            self.assertIn('no reviewed semantic hold is active', source)
            self.assertIn('orbitData.metaCountStatus', source)
            self.assertIn('verified meta-', source)
            self.assertIn('Meta count unknown', source)
            self.assertIn('Examples unknown', source)
            self.assertIn('Examples 0', source)
            self.assertNotIn('t._ex =', source)
            self.assertGreaterEqual(source.count('articleLink(t)'), 3)
        self.assertEqual(blocks[0], blocks[1])

    def test_dashboard_prose_uses_derived_article_counts(self):
        with open(os.path.join(ROOT, 'dashboard', 'index.html'), encoding='utf-8') as fh:
            source = fh.read()
        self.assertIn('stats.articleHubs', source)
        self.assertIn('stats.definitiveArticles', source)
        self.assertIn('btl-live-article-wip', source)
        self.assertNotIn('every task documented to the definitive-article standard', source)
        with open(os.path.join(ROOT, 'dashboard', 'library-index.html'), encoding='utf-8') as fh:
            static_index = fh.read()
        self.assertIn('no reviewed semantic hold is active', static_index)


class DurableArticleStandard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(ROOT, 'Task-Library-Standard.md'), encoding='utf-8') as fh:
            cls.standard = fh.read()

    def test_entity_destination_rules_are_explicit(self):
        self.assertIn('## Entity Destination Rules', self.standard)
        self.assertIn('verified personal-brand site', self.standard)
        self.assertIn('verified official site', self.standard)
        self.assertIn('BlitzMetrics training article', self.standard)
        self.assertIn('Never guess a domain', self.standard)

    def test_canonical_diagram_and_ready_marker_are_gated(self):
        self.assertIn('full canonical Content Factory diagram', self.standard)
        self.assertIn('every task mapped to that URL is `complete`', self.standard)
        self.assertIn('no reviewed semantic-certification hold is active', self.standard)
        self.assertIn('build/article-certifications.json', self.standard)
        self.assertIn('may only downgrade readiness', self.standard)
        self.assertIn('does not by itself certify a shared article hub', self.standard)
        self.assertIn('Only a `ready` hub may show', self.standard)
        self.assertIn('Article in progress', self.standard)

    def test_hubs_support_approved_domains_without_premature_remapping(self):
        self.assertIn('approved canonical domain', self.standard)
        self.assertIn('Declare one working copy', self.standard)
        self.assertIn('content parity and passes validation', self.standard)
        self.assertIn('absolute URL on another approved canonical domain', self.standard)

    def test_article_specific_visual_leads_framework_context(self):
        self.assertIn('Article-specific lead visual', self.standard)
        self.assertIn('The framework map is orientation, not generic hero art', self.standard)
        self.assertIn('must not displace the article\'s primary evidence', self.standard)
        self.assertIn('do not force a generic Content Factory diagram', self.standard)

    def test_taxonomy_is_canonical_and_not_self_declared(self):
        self.assertIn('Definitive Articles** category only after', self.standard)
        self.assertIn('using names from `build/categories.json`', self.standard)
        self.assertIn('every **Content Factory stage** represented', self.standard)
        self.assertIn('a shared hub may represent several', self.standard)
        self.assertIn('Reuse canonical tag slugs', self.standard)

    def test_standard_does_not_hardcode_task_count(self):
        self.assertNotRegex(self.standard, r'bring all \d+ tasks')
        self.assertIn('Counts are always derived', self.standard)

    def test_bidirectional_routes_and_orbit_evidence_are_explicit(self):
        self.assertIn('## Bidirectional Task Library links', self.standard)
        self.assertIn('?task=<permanent-task-slug>#task-<permanent-task-slug>',
                      self.standard)
        self.assertIn('?article=<URL-encoded-canonical-article-URL>', self.standard)
        self.assertIn('articleHubs[]', self.standard)
        self.assertIn('unknown**, never zero', self.standard)
        self.assertIn('build/article-meta-orbits.json', self.standard)
        self.assertIn('Level 4 — Deep: 11+', self.standard)
        self.assertIn('priorityCoverage', self.standard)
        self.assertIn('canonical `/meta-article-prompt/`', self.standard)
        self.assertNotIn('/meta-article-prompt-template` (29', self.standard)


if __name__ == '__main__':
    unittest.main()
