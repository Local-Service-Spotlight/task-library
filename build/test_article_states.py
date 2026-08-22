#!/usr/bin/env python3
"""Lock status-aware article labels and the current article inventory."""
import copy
import json
import os
import re
import sys
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
        self.assertEqual(self.data['stats']['articleHubs'], 23)
        self.assertEqual(self.data['stats']['definitiveArticles'], 13)

        tasks = copy.deepcopy(self.tasks)
        derived = task_build.derive_article_states(tasks)
        self.assertEqual(derived, {'articleHubs': 23, 'definitiveArticles': 13})

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
            self.assertGreaterEqual(source.count('articleLink(t)'), 3)
        self.assertEqual(blocks[0], blocks[1])

    def test_dashboard_prose_uses_derived_article_counts(self):
        with open(os.path.join(ROOT, 'dashboard', 'index.html'), encoding='utf-8') as fh:
            source = fh.read()
        self.assertIn('stats.articleHubs', source)
        self.assertIn('stats.definitiveArticles', source)
        self.assertIn('btl-live-article-wip', source)
        self.assertNotIn('every task documented to the definitive-article standard', source)


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
