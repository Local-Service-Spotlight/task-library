import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import standard_verification as verification  # noqa: E402

SPEC = importlib.util.spec_from_file_location('instruction_standard_build', HERE / 'build.py')
task_build = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(task_build)


def standards(**states):
    checks = {}
    for name in verification.INSTRUCTION_CHECK_ORDER:
        state = states.get(name, 'pass')
        checks[name] = {
            'state': state,
            'reason': f'{name.title()} requirement is {state}.',
            'evidence': f'Reviewed the {name.title()} section and its named acceptance text.',
        }
    return {'version': 1, 'checks': checks}


def review(source_hash, checklist=None):
    result = {
        'source_sha256': source_hash,
        'reviewed_at': '2026-09-17',
        'reviewer': 'Independent reviewer',
        'scope': 'Exact source and five instruction requirements.',
    }
    if checklist is not None:
        result['standards'] = checklist
    return result


def task(source_hash='a' * 64, current_review=None):
    result = {
        'slug': 'sample-task', 'title': 'Sample task', 'status': 'complete',
        'article': 'https://example.com/guide/', 'articleState': 'ready',
        'importance': 3, 'category': 'Test', '_sourceSha256': source_hash,
        'executionHistory': {'status': 'unknown', 'executionIds': []},
    }
    if current_review is not None:
        result['instructionReview'] = current_review
    return result


def derive(current, reviews):
    verification.derive([current], reviews, {}, task_build.normalize_article_url)
    return current['standardVerification']['gates']['instructionStandards']


class InstructionStandardsTests(unittest.TestCase):
    def test_legacy_review_cannot_imply_instruction_standards_pass(self):
        current_review = review('a' * 64)
        gate = derive(task(current_review=current_review), {'sample-task': current_review})

        self.assertEqual(gate['state'], 'unknown')
        self.assertIn('no structured', gate['reason'])

    def test_stale_standards_review_expires(self):
        old_review = review('a' * 64, standards())
        text = 'changed source'
        self.assertIsNone(task_build.current_instruction_review(
            'sample-task', text, {'sample-task': old_review}))
        current_hash = hashlib.sha256(text.encode()).hexdigest()
        current = task(source_hash=current_hash)

        gate = derive(current, {'sample-task': old_review})

        self.assertEqual(gate['state'], 'unmet')
        self.assertIn('expired', gate['reason'])

    def test_incomplete_extra_and_invalid_criteria_are_rejected(self):
        valid = standards()
        cases = []
        missing = copy.deepcopy(valid)
        missing['checks'].pop('handoff')
        cases.append(missing)
        extra = copy.deepcopy(valid)
        extra['checks']['privacy'] = extra['checks']['links']
        cases.append(extra)
        extra_field = copy.deepcopy(valid)
        extra_field['checks']['opening']['note'] = 'Not part of the schema.'
        cases.append(extra_field)
        bad_state = copy.deepcopy(valid)
        bad_state['checks']['recipe']['state'] = 'reviewed'
        cases.append(bad_state)
        non_string_state = copy.deepcopy(valid)
        non_string_state['checks']['recipe']['state'] = ['pass']
        cases.append(non_string_state)
        empty_reason = copy.deepcopy(valid)
        empty_reason['checks']['links']['reason'] = '  '
        cases.append(empty_reason)
        long_evidence = copy.deepcopy(valid)
        long_evidence['checks']['handoff']['evidence'] = 'x' * 1201
        cases.append(long_evidence)
        private_path = copy.deepcopy(valid)
        private_path['checks']['evidence']['evidence'] = '/Users/reviewer/private/receipt.txt'
        cases.append(private_path)
        windows_private_path = copy.deepcopy(valid)
        windows_private_path['checks']['evidence']['evidence'] = r'C:\Users\reviewer\receipt.txt'
        cases.append(windows_private_path)

        for checklist in cases:
            with self.subTest(checklist=checklist):
                candidate = review('a' * 64, checklist)
                with self.assertRaises(ValueError):
                    task_build.current_instruction_review(
                        'sample-task', 'source', {'sample-task': candidate})

    def test_mixed_pass_and_unmet_is_unmet(self):
        current_review = review('a' * 64, standards(recipe='unmet'))

        gate = derive(task(current_review=current_review), {'sample-task': current_review})

        self.assertEqual(gate['state'], 'unmet')
        self.assertIn('recipe', gate['reason'])
        self.assertEqual(gate['standards']['checks']['opening']['state'], 'pass')

    def test_hold_wins_and_unknown_remains_unknown(self):
        unknown_review = review('a' * 64, standards(links='unknown'))
        unknown_gate = derive(
            task(current_review=unknown_review), {'sample-task': unknown_review})
        self.assertEqual(unknown_gate['state'], 'unknown')

        held_review = review('a' * 64, standards(recipe='unmet', evidence='hold'))
        held_gate = derive(task(current_review=held_review), {'sample-task': held_review})
        self.assertEqual(held_gate['state'], 'hold')
        self.assertIn('evidence', held_gate['reason'])

    def test_html_escapes_checklist_reason_and_evidence(self):
        checklist = standards()
        checklist['checks']['opening']['reason'] = '<script>alert("reason")</script>'
        checklist['checks']['opening']['evidence'] = '<img src=x onerror="evidence">'
        current_review = review('a' * 64, checklist)
        current = task(current_review=current_review)
        verification.derive(
            [current], {'sample-task': current_review}, {}, task_build.normalize_article_url)
        payload = verification.report([current], '2026-09-17T00:00:00+00:00')

        with tempfile.TemporaryDirectory() as temp_dir:
            verification.write_artifacts(payload, temp_dir)
            rendered = (Path(temp_dir) / 'verification-queue.html').read_text()
            saved = json.loads((Path(temp_dir) / 'verification-queue.json').read_text())

        self.assertIn('&lt;script&gt;alert(&quot;reason&quot;)&lt;/script&gt;', rendered)
        self.assertIn('&lt;img src=x onerror=&quot;evidence&quot;&gt;', rendered)
        self.assertNotIn('<script>alert', rendered)
        self.assertEqual(
            saved['queue'][0]['standardVerification']['gates']['instructionStandards']
            ['standards']['checks']['opening']['reason'],
            '<script>alert("reason")</script>')

    def test_all_five_pass_only_the_instruction_standards_gate(self):
        current_review = review('a' * 64, standards())
        current = task(current_review=current_review)

        gate = derive(current, {'sample-task': current_review})

        self.assertEqual(gate['state'], 'pass')
        self.assertFalse(current['standardVerification']['fullyVerified'])
        self.assertEqual(
            current['standardVerification']['gates']['articleSemanticCertification']['state'],
            'unknown')


if __name__ == '__main__':
    unittest.main()
