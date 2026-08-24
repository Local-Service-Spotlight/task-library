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

    def test_blog_posting_mappings_remain_on_existing_hub(self):
        key = 'blitzmetrics.com/blog-posting-guidelines'
        mapped = [t for t in self.tasks
                  if task_build.normalize_article_url(t.get('article')) == key]
        self.assertEqual(len(mapped), 21)
        self.assertEqual({t['article'] for t in mapped},
                         {'https://blitzmetrics.com/blog-posting-guidelines'})

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


if __name__ == '__main__':
    unittest.main()
