#!/usr/bin/env python3
"""Tests for task-specific exact-revision article semantic evidence."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import article_semantic_reviews as semantic
import build as task_build
import standard_verification


NOW = datetime(2026, 9, 18, 7, 0, 0, tzinfo=timezone.utc)
ARTICLE = 'https://example.com/article/'
SOURCE_HASH = 'a' * 64


def criterion(state='pass'):
    return {
        'state': state,
        'reason': f'Exact article evidence supports {state}.',
        'evidenceRefs': ['https://example.com/article/#evidence'],
    }


def review(**overrides):
    row = {
        'version': 1,
        'taskSlug': 'example-task',
        'canonicalURL': ARTICLE,
        'sourceSha256': SOURCE_HASH,
        'representation': 'wordpress-content-html',
        'reviewedAt': '2026-09-18T06:40:00Z',
        'reviewer': 'Independent reviewer',
        'criteria': {name: criterion() for name in semantic.CRITERION_ORDER},
    }
    row.update(overrides)
    return row


def observation(**overrides):
    row = {
        'version': 1,
        'taskSlug': 'example-task',
        'canonicalURL': ARTICLE,
        'sourceSha256': SOURCE_HASH,
        'representation': 'wordpress-content-html',
        'observedAt': '2026-09-18T06:45:00Z',
        'observer': 'Revision observer',
        'state': 'observed',
        'reason': 'Captured the current canonical article representation.',
        'evidenceRefs': ['sha256:' + SOURCE_HASH],
    }
    row.update(overrides)
    return row


def task(slug='example-task', article=ARTICLE):
    return {
        'slug': slug, 'title': 'Example task', 'status': 'complete',
        'article': article, 'articleState': 'ready', 'importance': 3,
        'category': 'Test', '_sourceSha256': 'b' * 64,
        'instructionReview': {
            'source_sha256': 'b' * 64, 'reviewed_at': '2026-09-18',
            'reviewer': 'Guide reviewer', 'scope': 'Exact guide review.'},
        'executionHistory': {'status': 'unknown', 'executionIds': []},
    }


class ArticleSemanticEvidenceTests(unittest.TestCase):
    def load(self, semantic_reviews=None, observations=None, extra=None):
        payload = {'articles': {}}
        if semantic_reviews is not None:
            payload['semanticReviews'] = semantic_reviews
        if observations is not None:
            payload['revisionObservations'] = observations
        if extra:
            payload.update(extra)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / 'article-certifications.json'
            path.write_text(json.dumps(payload), encoding='utf-8')
            return semantic.load(path)

    def derive(self, evidence, current=None):
        current = current or task()
        standard_verification.derive(
            [current], {current['slug']: current['instructionReview']}, {},
            task_build.normalize_article_url, article_evidence=evidence, now=NOW)
        return current['standardVerification']['gates']['articleSemanticCertification']

    def test_legacy_file_without_new_sections_remains_valid_and_unknown(self):
        evidence = self.load()
        self.assertEqual(evidence, {'semanticReviews': [], 'revisionObservations': []})
        self.assertEqual(self.derive(evidence)['state'], 'unknown')

    def test_all_criteria_need_fresh_separate_matching_observation_to_pass(self):
        evidence = self.load([review()], [observation()])
        gate = self.derive(evidence)
        self.assertEqual(gate['state'], 'pass')
        self.assertEqual(gate['semanticReview']['sourceSha256'], SOURCE_HASH)
        self.assertEqual(gate['revisionObservation']['sourceSha256'], SOURCE_HASH)

    def test_semantic_criteria_render_with_public_evidence_safely_escaped(self):
        row = review()
        row['criteria']['links'] = {
            'state': 'unmet', 'reason': '<b>Wrong target</b>',
            'evidenceRefs': ['https://example.com/check/?a=1&b=2']}
        current = task()
        evidence = self.load([row], [observation()])
        standard_verification.derive(
            [current], {current['slug']: current['instructionReview']}, {},
            task_build.normalize_article_url, article_evidence=evidence, now=NOW)
        payload = standard_verification.report([current], NOW.isoformat())
        rendered = standard_verification._html_report(payload)
        self.assertIn('Role and scope', rendered)
        self.assertIn('&lt;b&gt;Wrong target&lt;/b&gt;', rendered)
        self.assertNotIn('<b>Wrong target</b>', rendered)
        self.assertIn('a=1&amp;b=2', rendered)

    def test_review_hash_alone_cannot_pass(self):
        gate = self.derive(self.load([review()], []))
        self.assertEqual(gate['state'], 'unknown')
        self.assertIn('separate', gate['reason'])

    def test_failed_older_and_stale_observations_are_unknown(self):
        cases = (
            observation(state='failed', sourceSha256=None,
                        reason='Public capture did not complete.'),
            observation(observedAt='2026-09-18T06:30:00Z'),
            observation(observedAt='2026-09-17T06:59:59Z'),
        )
        for row in cases:
            with self.subTest(row=row):
                self.assertEqual(self.derive(self.load([review()], [row]))['state'], 'unknown')

    def test_separate_observation_hash_mismatch_is_unmet(self):
        gate = self.derive(self.load([review()], [observation(sourceSha256='c' * 64)]))
        self.assertEqual(gate['state'], 'unmet')
        self.assertIn('does not match', gate['reason'])

    def test_criterion_precedence_is_hold_then_unmet_then_unknown(self):
        for expected, states in (
                ('hold', {'owner': 'unknown', 'links': 'unmet', 'sourceEvidence': 'hold'}),
                ('unmet', {'owner': 'unknown', 'links': 'unmet'}),
                ('unknown', {'owner': 'unknown'})):
            row = review()
            for name, state_value in states.items():
                row['criteria'][name] = criterion(state_value)
            with self.subTest(expected=expected):
                self.assertEqual(
                    self.derive(self.load([row], [observation()]))['state'], expected)

    def test_malformed_or_incomplete_criteria_are_rejected(self):
        for missing in ('openingContext', 'visualAndLayout', 'handoffContext',
                        'publicationStandards'):
            bad = review()
            bad['criteria'].pop(missing)
            with self.subTest(missing=missing), self.assertRaisesRegex(
                    ValueError, 'criteria must contain exactly'):
                self.load([bad], [])
        bad = review(version=2)
        with self.assertRaisesRegex(ValueError, 'requires version 1'):
            self.load([bad], [])
        bad = review(version=True)
        with self.assertRaisesRegex(ValueError, 'requires version 1'):
            self.load([bad], [])
        bad = review()
        bad['criteria']['links']['extra'] = True
        with self.assertRaisesRegex(ValueError, 'must contain exactly'):
            self.load([bad], [])

    def test_private_or_malformed_evidence_is_rejected(self):
        for evidence_ref in (
                'file:///Users/person/private/review.html',
                'https://localhost/review',
                'https://127.0.0.1/review',
                '/Users/person/private/review.html'):
            bad = review()
            bad['criteria']['links']['evidenceRefs'] = [evidence_ref]
            with self.subTest(evidence_ref=evidence_ref), self.assertRaisesRegex(
                    ValueError, 'public'):
                self.load([bad], [])

    def test_credential_urls_and_canonical_userinfo_are_rejected(self):
        for evidence_ref in (
                'https://example.com/review?token=secret',
                'https://example.com/review#api-key=secret',
                'https://user:pass@example.com/review'):
            bad = review()
            bad['criteria']['links']['evidenceRefs'] = [evidence_ref]
            with self.subTest(evidence_ref=evidence_ref), self.assertRaisesRegex(
                    ValueError, 'credential|credentials'):
                self.load([bad], [])
        for canonical_url in (
                'https://user:pass@example.com/article/',
                'https://127.0.0.1/article/'):
            with self.subTest(canonical_url=canonical_url), self.assertRaisesRegex(
                    ValueError, 'credentials|private'):
                self.load([review(canonicalURL=canonical_url)], [])

    def test_wrong_task_or_exact_url_mapping_is_rejected(self):
        for row, message in (
                (review(taskSlug='missing-task'), 'unknown taskSlug'),
                (review(canonicalURL='https://example.com/other/'), 'does not exactly match')):
            evidence = self.load([row], [])
            with self.subTest(row=row), self.assertRaisesRegex(ValueError, message):
                semantic.validate_task_mappings(
                    [task()], evidence, task_build.normalize_article_url)

    def test_existing_url_hold_wins_for_all_19_mapped_tasks(self):
        tasks = []
        for index in range(19):
            current = task(f'held-{index}', f'https://example.com/held-{index % 3}/')
            current['articleState'] = 'wip'
            current['articleStateReason'] = 'Existing URL-level semantic hold.'
            current['articleStateReviewed'] = '2026-09-18'
            tasks.append(current)
        standard_verification.derive(
            tasks, {item['slug']: item['instructionReview'] for item in tasks}, {},
            task_build.normalize_article_url,
            article_evidence=self.load([review()], [observation()]), now=NOW)
        states = [item['standardVerification']['gates']['articleSemanticCertification']['state']
                  for item in tasks]
        self.assertEqual(states.count('hold'), 19)

    def test_production_file_has_no_positive_semantic_review_records(self):
        path = Path(__file__).with_name('article-certifications.json')
        evidence = semantic.load(path)
        self.assertEqual(evidence['semanticReviews'], [])
        self.assertEqual(evidence['revisionObservations'], [])


if __name__ == '__main__':
    unittest.main()
