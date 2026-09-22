"""Synthetic receipts only; these fixtures must never enter the run ledger."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
import unittest

import executions
import standard_verification as verification
from test_standard_verification import acceptance, execution, observation, task


NOW = datetime(2026, 9, 15, 13, tzinfo=timezone.utc)
KNOWN = {'first-task'}


def setup(**changes):
    value = {
        'version': 1, 'reviewId': 'setup-001', 'executionId': 'execution-001',
        'taskSlug': 'first-task', 'canonicalURL': 'https://example.com/hub/',
        'recipeSourceSha256': 'a' * 64, 'representation': 'wordpress-content-html',
        'instructionSourceSha256': 'a' * 64, 'reviewedAt': '2026-09-15T11:45:00Z',
        'reviewer': 'Independent setup reviewer', 'participant': 'Run executor',
        'participantType': 'novice-human', 'assistance': 'none', 'app': 'Example Chat',
        'surface': 'Browser file attachment', 'loadingRoute': 'manual-guide',
        'package': {'url': 'https://example.com/TaskLibrary.zip', 'sha256': 'b' * 64,
                    'memberPath': 'TaskLibrary-Skills/skills/category/first-task.md',
                    'memberSha256': 'c' * 64, 'onboardingSha256': 'd' * 64},
        'acceptanceReviewId': 'acceptance-001',
        'criteria': {
            'filesLoaded': {'state': 'pass', 'observedAt': '2026-09-15T10:10:00Z',
                            'expectedResult': 'The named guide and onboarding are readable in the app.',
                            'observedResult': 'The saved transcript identifies both supplied files and their content.'},
            'inputsAndAccess': {'state': 'pass', 'observedAt': '2026-09-15T10:20:00Z',
                                'expectedResult': 'All required inputs and scoped access are available.',
                                'observedResult': 'The full source and brief were read and required links opened.'},
            'result': {'state': 'pass', 'observedAt': '2026-09-15T11:00:00Z',
                       'expectedResult': 'The saved result satisfies the named result checks.',
                       'observedResult': 'Independent result review accepted the saved artifact.'},
            'handoff': {'state': 'pass', 'observedAt': '2026-09-15T11:00:00Z',
                        'expectedResult': 'The next owner receives the checked result.',
                        'observedResult': 'The source-system handoff record identifies the saved artifact.'},
        },
    }
    for item in value['criteria'].values():
        item.update(sourceRef='https://example.com/requirements/',
                    evidenceRefs=['sha256:' + 'e' * 64])
    value.update(changes)
    return value


def reviewed_execution(**changes):
    value = execution()
    value['acceptanceReviews'] = [acceptance()]
    value['setupReviews'] = [setup()]
    value.update(changes)
    return value


def evaluate(records, current=None, observations=None, now=NOW):
    current = current or task('first-task')
    executions.attach([current], records, now)
    evidence = {'revisionObservations': [observation()] if observations is None else observations}
    accepted = verification.acceptance_result(current, current['executionHistory'], evidence, now)
    return verification.setup_result(current, current['executionHistory'], accepted, now)


class SetupReviewTests(unittest.TestCase):
    def test_manual_receipt_keeps_archive_member_onboarding_and_instruction_identities_distinct(self):
        record = executions.validate_record(reviewed_execution(), KNOWN)
        receipt = record['setupReviews'][0]
        hashes = {receipt['instructionSourceSha256'], receipt['package']['sha256'],
                  receipt['package']['memberSha256'], receipt['package']['onboardingSha256']}
        self.assertEqual(len(hashes), 4)
        result = evaluate([record])
        self.assertEqual(result['state'], 'pass')
        self.assertIn('Example Chat', result['reason'])
        self.assertIn('other apps', result['reason'])
        self.assertFalse(result['installationCertified'])
        self.assertFalse(result['schedulingCertified'])
        for member in ('TaskLibrary-Skills/skills/category/first-task.md',
                       'editorial/skills/first-task/skill.md'):
            record['setupReviews'][0]['package']['memberPath'] = member
            self.assertEqual(evaluate([record])['state'], 'pass')

    def test_unsupported_missing_and_wrong_scope_fields_are_rejected(self):
        changes = (
            {'version': True}, {'version': 2}, {'reviewId': 'x'},
            {'executionId': 'another-run'}, {'taskSlug': 'another-task'},
            {'canonicalURL': 'https://example.com/other/'},
            {'recipeSourceSha256': 'b' * 64}, {'instructionSourceSha256': 'short'},
            {'representation': 'screenshot'}, {'loadingRoute': 'installed-plugin'},
            {'participantType': 'new-user'}, {'participantType': []},
            {'assistance': False}, {'assistance': 'minimal'},
            {'reviewer': ' RUN   EXECUTOR '}, {'participant': 'Different executor'},
            {'acceptanceReviewId': 'missing-review'}, {'installed': True},
        )
        for change in changes:
            with self.subTest(change=change), self.assertRaises(ValueError):
                executions.validate_record(reviewed_execution(setupReviews=[setup(**change)]), KNOWN)
        for key in setup():
            record = reviewed_execution()
            del record['setupReviews'][0][key]
            with self.subTest(missing=key), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)

    def test_acceptance_reference_binds_task_recipe_instruction_representation_and_actor(self):
        for field, value in (('instructionSourceSha256', 'f' * 64),
                             ('representation', 'public-visible-text'),
                             ('executor', 'Other operator')):
            record = reviewed_execution()
            record['acceptanceReviews'][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)
        record = reviewed_execution()
        record['acceptanceReviews'][0]['reviewedAt'] = '2026-09-15T11:50:00Z'
        with self.assertRaisesRegex(ValueError, 'later acceptance'):
            executions.validate_record(record, KNOWN)

    def test_member_and_package_validation_rejects_unsafe_paths_and_confused_fields(self):
        for path in ('../first-task.md', 'skills/../first-task.md', '/skills/first-task.md',
                     'skills//first-task.md', 'skills/./first-task.md',
                     'C:\\skills\\first-task.md', 'skills/%2e%2e/first-task.md',
                     '~/first-task.md', 'skills/other-task.md', 'skills/first-task.html',
                     'pack/skills/other-task/skill.md', 'pack/skills/first-task/not-skill.md'):
            record = reviewed_execution()
            record['setupReviews'][0]['package']['memberPath'] = path
            with self.subTest(path=path), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)
        for field in ('sha256', 'memberSha256', 'onboardingSha256'):
            record = reviewed_execution()
            record['setupReviews'][0]['package'][field] = 'invalid'
            with self.subTest(field=field), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)
        record = reviewed_execution()
        record['setupReviews'][0]['package']['manifestPath'] = 'manifest.json'
        with self.assertRaisesRegex(ValueError, 'package requires'):
            executions.validate_record(record, KNOWN)

    def test_credentials_and_private_paths_are_rejected_in_all_free_text_and_refs(self):
        for value in ('/Users/person/private', '/private/client/notes', '~/private',
                      '/Applications/Private.app', 'C:\\Users\\person\\private.txt',
                      'api_key=should-not-be-recorded', 'Bearer should-not-be-recorded'):
            for field in ('reviewer', 'participant', 'app', 'surface'):
                record = reviewed_execution()
                record['setupReviews'][0][field] = value
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    executions.validate_record(record, KNOWN)
            record = reviewed_execution()
            record['setupReviews'][0]['criteria']['result']['observedResult'] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)
        for url in ('https://localhost/proof', 'https://127.0.0.1/proof',
                    'https://example.com/proof?token=secret',
                    'https://example.com/proof#access%5Ftoken=secret',
                    'https://user:password@example.com/proof',
                    'https://example.com/Users/person/private',
                    'https://storage.example.com/proof.json?sv=2025-01-05&sp=r&sig=SYNTHETIC_SIGNATURE',
                    'https://example.com/proof?auth=SYNTHETIC_AUTH',
                    'https://example.com/proof?code=SYNTHETIC_CODE',
                    'https://example.com/proof?access_key=SYNTHETIC_KEY',
                    'https://example.com/proof?session-id=SYNTHETIC_SESSION',
                    'https://example.com/proof#sig=SYNTHETIC_SIGNATURE',
                    'https://example.com/proof#code=SYNTHETIC_CODE'):
            for field in ('sourceRef', 'evidenceRefs', 'package'):
                record = reviewed_execution()
                receipt = record['setupReviews'][0]
                if field == 'package':
                    receipt['package']['url'] = url
                else:
                    receipt['criteria']['result'][field] = [url] if field == 'evidenceRefs' else url
                with self.subTest(field=field, url=url), self.assertRaises(ValueError):
                    executions.attach([task('first-task')], [record], NOW)

    def test_every_criterion_requires_dated_observation_source_and_actual_evidence(self):
        for name in executions.SETUP_CRITERIA:
            record = reviewed_execution()
            del record['setupReviews'][0]['criteria'][name]
            with self.subTest(name=name), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)
        for field in setup()['criteria']['result']:
            record = reviewed_execution()
            del record['setupReviews'][0]['criteria']['result'][field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)
        for change in ({'evidenceRefs': []}, {'observedResult': ''}, {'state': 'failed'},
                       {'path': '/tmp/private'}, {'observedAt': '2026-09-15'}):
            record = reviewed_execution()
            record['setupReviews'][0]['criteria']['result'].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)

    def test_inconsistent_duplicate_and_future_review_times_fail_closed(self):
        for reviewed in ('2026-09-15T09:59:00Z', '2026-09-15T10:59:00Z',
                         '2026-09-15T12:01:00Z', '2026-09-15T11:45:00'):
            with self.subTest(reviewed=reviewed), self.assertRaises(ValueError):
                executions.validate_record(reviewed_execution(setupReviews=[setup(reviewedAt=reviewed)]), KNOWN)
        for observed in ('2026-09-15T09:59:00Z', '2026-09-15T11:46:00Z'):
            record = reviewed_execution()
            record['setupReviews'][0]['criteria']['result']['observedAt'] = observed
            with self.subTest(observed=observed), self.assertRaises(ValueError):
                executions.validate_record(record, KNOWN)
        record = reviewed_execution()
        record['setupReviews'].append(setup(reviewId='setup-002', reviewedAt='2026-09-15T13:45:00+02:00'))
        with self.assertRaisesRegex(ValueError, 'distinct task and review timestamps'):
            executions.validate_record(record, KNOWN)
        record = reviewed_execution(updatedAt='2026-09-16T12:00:00Z',
                                    setupReviews=[setup(reviewedAt='2026-09-16T11:45:00Z')])
        with self.assertRaisesRegex(ValueError, 'future'):
            executions.attach([task('first-task')], [record], NOW)

    def test_public_projection_has_exact_allowlist_and_hides_private_refs_and_participant(self):
        record = reviewed_execution()
        receipt = record['setupReviews'][0]
        receipt['criteria']['filesLoaded']['sourceRef'] = 'sha256:' + 'f' * 64
        projected = executions.public_setup_review(receipt)
        self.assertEqual(set(projected), {
            'version', 'reviewId', 'executionId', 'taskSlug', 'canonicalURL',
            'recipeSourceSha256', 'representation', 'instructionSourceSha256',
            'reviewedAt', 'reviewer', 'participantType', 'assistance', 'app', 'surface',
            'loadingRoute', 'package', 'acceptanceReviewId', 'criteria'})
        self.assertEqual(set(projected['criteria']['filesLoaded']), {
            'state', 'expectedResult', 'observedResult', 'sourceUrl',
            'sourcePrivateEvidenceRecorded', 'evidenceUrls', 'privateEvidenceRecorded', 'observedAt'})
        self.assertEqual(set(projected['package']), {'url', 'sha256', 'memberPath', 'memberSha256', 'onboardingSha256'})
        self.assertNotIn('Run executor', json.dumps(projected))
        tasks = [task('first-task')]
        public = executions.attach(tasks, [record], NOW)
        verification.derive(tasks, {}, {}, lambda url: url,
                            article_evidence={'revisionObservations': [observation()]}, now=NOW)
        report = verification.report(tasks, NOW.isoformat())
        for value in (public, tasks, report):
            encoded = json.dumps(value)
            self.assertNotIn('e' * 64, encoded)
            self.assertNotIn('f' * 64, encoded)
            self.assertNotIn('Run executor', encoded)
            self.assertNotIn('"participant"', encoded)
            self.assertNotIn('"executor"', encoded)
        self.assertEqual(set(public['executions'][0]['acceptanceReviews'][0]), {
            'version', 'reviewId', 'taskSlug', 'canonicalURL', 'recipeSourceSha256',
            'representation', 'instructionSourceSha256', 'reviewedAt', 'reviewer',
            'nextHandoff', 'criteria'})
        self.assertEqual(projected['participantType'], 'novice-human')
        self.assertEqual(projected['assistance'], 'none')
        self.assertIsNone(projected['criteria']['filesLoaded']['sourceUrl'])
        self.assertTrue(projected['criteria']['filesLoaded']['sourcePrivateEvidenceRecorded'])
        self.assertTrue(projected['criteria']['result']['privateEvidenceRecorded'])

    def test_legacy_upsert_preserves_both_histories_and_setup_history_is_append_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'ledger.json'
            path.write_text('{"schemaVersion":1,"executions":[]}\n')
            record = reviewed_execution()
            first = executions.upsert(path, record, KNOWN)
            legacy = execution()
            legacy.update(updatedAt='2026-09-15T12:05:00Z', result='Legacy client correction.')
            changed = executions.upsert(path, legacy, KNOWN, first['revision'])
            stored = executions.load(path, KNOWN)[0]
            self.assertEqual(stored['setupReviews'], record['setupReviews'])
            self.assertEqual(stored['acceptanceReviews'], record['acceptanceReviews'])
            for replacement in ([], [setup(app='Changed app')]):
                candidate = copy.deepcopy(stored)
                candidate.update(updatedAt='2026-09-15T12:10:00Z', setupReviews=replacement)
                with self.subTest(replacement=replacement), self.assertRaisesRegex(ValueError, 'append-only'):
                    executions.upsert(path, candidate, KNOWN, changed['revision'])
                self.assertEqual(executions.load(path, KNOWN)[0], stored)
            candidate = copy.deepcopy(stored)
            candidate['updatedAt'] = '2026-09-15T12:10:00Z'
            correction = setup(reviewId='setup-002', reviewedAt='2026-09-15T12:10:00Z')
            correction['criteria']['filesLoaded']['state'] = 'unmet'
            candidate['setupReviews'].append(correction)
            executions.upsert(path, candidate, KNOWN, changed['revision'])
            self.assertEqual(evaluate(executions.load(path, KNOWN))['state'], 'unmet')

    def test_agents_cannot_pass_human_novice_gate(self):
        for kind in ('fresh-agent', 'experienced-agent'):
            record = reviewed_execution(setupReviews=[setup(participantType=kind)])
            result = evaluate([record])
            self.assertEqual(result['state'], 'unknown')
            self.assertEqual(result['setupReview']['participantType'], kind)
            self.assertIn(kind, result['reason'])
        self.assertEqual(evaluate([reviewed_execution()])['state'], 'pass')

    def test_bound_acceptance_history_cannot_be_rewritten_to_turn_hold_into_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'ledger.json'
            path.write_text('{"schemaVersion":1,"executions":[]}\n')
            record = reviewed_execution()
            record['acceptanceReviews'][0]['criteria']['result']['state'] = 'hold'
            first = executions.upsert(path, record, KNOWN)
            self.assertEqual(evaluate(executions.load(path, KNOWN))['state'], 'hold')
            candidate = copy.deepcopy(record)
            candidate['updatedAt'] = '2026-09-15T12:05:00Z'
            candidate['acceptanceReviews'][0]['criteria']['result']['state'] = 'pass'
            with self.assertRaisesRegex(ValueError, 'referenced by setup history are immutable'):
                executions.upsert(path, candidate, KNOWN, first['revision'])
            self.assertEqual(evaluate(executions.load(path, KNOWN))['state'], 'hold')
            # Corrections need new review identities while retaining the original hold.
            candidate = copy.deepcopy(record)
            candidate['updatedAt'] = '2026-09-15T12:05:00Z'
            candidate['acceptanceReviews'].append(acceptance(reviewId='acceptance-002', reviewedAt='2026-09-15T11:50:00Z'))
            candidate['setupReviews'].append(setup(reviewId='setup-002', reviewedAt='2026-09-15T11:55:00Z',
                                                  acceptanceReviewId='acceptance-002'))
            executions.upsert(path, candidate, KNOWN, first['revision'])
            self.assertEqual(evaluate(executions.load(path, KNOWN))['state'], 'pass')
            self.assertEqual(executions.load(path, KNOWN)[0]['acceptanceReviews'][0]['criteria']['result']['state'], 'hold')

    def test_unbound_legacy_acceptance_updates_keep_existing_behavior(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'ledger.json'
            path.write_text('{"schemaVersion":1,"executions":[]}\n')
            record = execution()
            record['acceptanceReviews'] = [acceptance(state='hold')]
            first = executions.upsert(path, record, KNOWN)
            record['updatedAt'] = '2026-09-15T12:05:00Z'
            record['acceptanceReviews'][0]['criteria']['result']['state'] = 'pass'
            self.assertEqual(executions.upsert(path, record, KNOWN, first['revision'])['action'], 'updated')

    def test_assisted_or_unspecified_help_does_not_certify_unassisted_novice_success(self):
        for assistance in ('provided', 'unknown'):
            result = evaluate([reviewed_execution(setupReviews=[setup(assistance=assistance)])])
            self.assertEqual(result['state'], 'unknown')
            self.assertEqual(result['setupReview']['assistance'], assistance)
            self.assertIn(f'assistance as {assistance}', result['reason'])
        with self.assertRaises(ValueError):
            record = reviewed_execution()
            del record['setupReviews'][0]['assistance']
            executions.validate_record(record, KNOWN)

    def test_absent_receipt_unknown_criteria_or_unaccepted_result_remains_unknown(self):
        self.assertEqual(evaluate([execution()])['state'], 'unknown')
        record = reviewed_execution()
        record['setupReviews'][0]['criteria']['result']['state'] = 'unknown'
        self.assertEqual(evaluate([record])['state'], 'unknown')
        record = reviewed_execution(acceptanceReviews=[], setupReviews=[setup(acceptanceReviewId=None)])
        self.assertEqual(evaluate([record])['state'], 'unknown')
        record = reviewed_execution()
        record['acceptanceReviews'].append(acceptance(reviewId='newer-acceptance', reviewedAt='2026-09-15T11:50:00Z'))
        self.assertEqual(evaluate([record])['state'], 'unknown')

    def test_same_completed_run_and_current_exact_revisions_are_required(self):
        for status in ('partial', 'failed', 'cancelled', 'blocked', 'running'):
            record = reviewed_execution(status=status)
            if status not in executions.TERMINAL:
                record.pop('finishedAt')
            with self.subTest(status=status):
                self.assertEqual(evaluate([record])['state'], 'unmet')
        record = reviewed_execution()
        for current in (task('first-task', source_hash='f' * 64),
                        task('first-task', article='https://example.com/new/')):
            self.assertEqual(evaluate([record], current=current)['state'], 'unmet')
        self.assertEqual(evaluate([record], observations=[observation(source_hash='f' * 64)])['state'], 'unmet')
        newer = execution()
        newer.update(executionId='execution-002', acceptanceReviews=[acceptance(reviewId='acceptance-002', reviewedAt='2026-09-15T11:50:00Z')])
        self.assertEqual(evaluate([record, newer])['state'], 'unknown')

    def test_observation_must_follow_setup_review_and_be_fresh_and_successful(self):
        record = reviewed_execution()
        for observations in ([], [observation(observed='2026-09-15T11:40:00Z')],
                             [observation(state='failed')],
                             [observation(observed='2026-09-15T13:01:00Z')]):
            with self.subTest(observations=observations):
                self.assertEqual(evaluate([record], observations=observations)['state'], 'unknown')
        self.assertEqual(evaluate([record], now=datetime(2026, 9, 16, 13, tzinfo=timezone.utc))['state'], 'unknown')

    def test_later_setup_failure_or_hold_overrides_old_pass_even_for_agent_rehearsal(self):
        for state in ('hold', 'unmet'):
            record = reviewed_execution()
            newer = setup(reviewId='setup-002', reviewedAt='2026-09-15T13:55:00+02:00',
                          participantType='fresh-agent', acceptanceReviewId=None)
            newer['criteria']['filesLoaded']['state'] = state
            record['setupReviews'].append(newer)
            result = evaluate([record], observations=[])
            self.assertEqual(result['state'], state)
            self.assertEqual(result['setupReview']['reviewId'], 'setup-002')

    def test_late_review_of_old_success_does_not_hide_later_unsuccessful_run(self):
        old = reviewed_execution(updatedAt='2026-09-15T12:55:00Z')
        old['setupReviews'][0]['reviewedAt'] = '2026-09-15T12:45:00Z'
        for status in ('failed', 'partial', 'cancelled', 'blocked'):
            later = execution()
            later.update(executionId='execution-002', status=status,
                         startedAt='2026-09-15T12:00:00Z', recordedAt='2026-09-15T12:00:00Z',
                         finishedAt='2026-09-15T12:30:00Z', updatedAt='2026-09-15T12:30:00Z')
            if status == 'blocked':
                later.pop('finishedAt')
            with self.subTest(status=status):
                self.assertEqual(evaluate([old, later], observations=[observation(observed='2026-09-15T12:50:00Z')])['state'], 'unmet')

    def test_cross_run_tied_latest_setup_reviews_cannot_pass(self):
        first = reviewed_execution()
        second = reviewed_execution(executionId='execution-002')
        second['setupReviews'][0]['executionId'] = 'execution-002'
        second['setupReviews'][0]['reviewedAt'] = '2026-09-15T13:45:00+02:00'
        result = evaluate([first, second])
        self.assertEqual(result['state'], 'unknown')
        self.assertIn('ambiguity', result['reason'])


if __name__ == '__main__':
    unittest.main()
