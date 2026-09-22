"""Real task runs, independent of article volume and certification.

The ledger references existing task slugs. Public output is an allowlisted
projection, not a copy of the ledger. Missing history remains unknown.
"""
import copy
import fcntl
import hashlib
import ipaddress
import json
import os
import re
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import parse_qsl, unquote, urlsplit

STATUSES = {'running', 'completed', 'partial', 'failed', 'blocked', 'cancelled'}
TERMINAL = {'completed', 'partial', 'failed', 'cancelled'}
META_STATES = {'draft', 'published', 'withheld'}
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._:-]{2,159}$')
FIELDS = {'executionId', 'taskSlugs', 'startedAt', 'finishedAt', 'status',
          'result', 'evidence', 'metaArticle', 'recipeRevisions', 'parentExecutionId', 'recordedAt', 'updatedAt',
          'acceptanceReviews', 'setupReviews'}
ACCEPTANCE_STATES = {'pass', 'unmet', 'hold', 'unknown'}
REPRESENTATIONS = {'public-rendered-html', 'public-visible-text', 'wordpress-content-html', 'repository-source'}
SETUP_CRITERIA = {'filesLoaded', 'inputsAndAccess', 'result', 'handoff'}
SETUP_PARTICIPANTS = {'novice-human', 'fresh-agent', 'experienced-agent'}
SETUP_PUBLIC_FIELDS = ('version', 'reviewId', 'executionId', 'taskSlug', 'canonicalURL',
                       'recipeSourceSha256', 'representation', 'instructionSourceSha256',
                       'reviewedAt', 'reviewer', 'participantType', 'assistance', 'app', 'surface',
                       'loadingRoute', 'package', 'acceptanceReviewId')


def timestamp(value, where):
    if not isinstance(value, str):
        raise ValueError(f'{where}: an ISO timestamp with timezone is required')
    try:
        result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValueError(f'{where}: invalid ISO timestamp') from exc
    if result.tzinfo is None:
        raise ValueError(f'{where}: timezone is required')
    return result.astimezone(timezone.utc)


def public_url(value, where):
    if not isinstance(value, str):
        raise ValueError(f'{where}: a public HTTPS URL is required')
    p = urlsplit(value)
    host = (p.hostname or '').lower()
    if p.scheme != 'https' or not host or p.username or p.password:
        raise ValueError(f'{where}: public HTTPS URL without credentials required')
    if host == 'localhost' or host.endswith(('.localhost', '.local', '.internal')):
        raise ValueError(f'{where}: local/private host is not public evidence')
    try:
        if not ipaddress.ip_address(host).is_global:
            raise ValueError(f'{where}: private address is not public evidence')
    except ValueError as exc:
        if 'private address' in str(exc):
            raise
    if any(re.search(r'token|secret|password|signature|api.?key|credential', k, re.I)
           for k, _ in parse_qsl(p.query)):
        raise ValueError(f'{where}: credential-like query parameters are forbidden')
    return value


def _acceptance_refs(value, where):
    if not isinstance(value, list) or not value or len(value) > 10:
        raise ValueError(f'{where}: requires 1-10 public HTTPS refs or private SHA-256 hashes')
    clean = []
    for ref in value:
        if not isinstance(ref, str) or len(ref) > 1200:
            raise ValueError(f'{where}: reference must be a string up to 1200 characters')
        if isinstance(ref, str) and re.fullmatch(r'sha256:[a-f0-9]{64}', ref):
            clean.append(ref)
        else:
            public_url(ref, where)
            if re.search(r'token|secret|password|signature|api.?key|credential', unquote(urlsplit(ref).fragment), re.I):
                raise ValueError(f'{where}: credential-like URL fragments are forbidden')
            clean.append(ref)
    return clean


def _safe_text(value, where, limit=600):
    if not isinstance(value, str) or not value.strip() or len(value.strip()) > limit:
        raise ValueError(f'{where}: requires nonempty public-safe text up to {limit} characters')
    value = value.strip()
    if re.search(r'file:|/(?:users|home|tmp|var/folders)/|[a-z]:\\|\\\\', value, re.I):
        raise ValueError(f'{where}: private paths are forbidden')
    return value


def validate_acceptance_review(review, record, known_slugs):
    fields = {'version', 'reviewId', 'taskSlug', 'canonicalURL', 'recipeSourceSha256',
              'representation', 'instructionSourceSha256', 'reviewedAt', 'reviewer',
              'executor', 'criteria', 'nextHandoff'}
    if not isinstance(review, dict) or set(review) != fields:
        raise ValueError('acceptance review has unsupported or missing fields')
    if type(review['version']) is not int or review['version'] != 1:
        raise ValueError('acceptance review requires version 1')
    if not isinstance(review['reviewId'], str) or not ID.fullmatch(review['reviewId']):
        raise ValueError('acceptance review requires stable reviewId')
    slug = review['taskSlug']
    if slug not in record['taskSlugs'] or slug not in known_slugs:
        raise ValueError('acceptance review taskSlug must be named by its execution')
    revision = record['recipeRevisions'][slug]
    if review['canonicalURL'] != revision['articleUrl']:
        raise ValueError('acceptance review canonicalURL must match the run recipe revision')
    public_url(review['canonicalURL'], 'acceptance review canonicalURL')
    if urlsplit(review['canonicalURL']).query or urlsplit(review['canonicalURL']).fragment:
        raise ValueError('acceptance review canonicalURL cannot contain query or fragment')
    if review['representation'] not in REPRESENTATIONS:
        raise ValueError('acceptance review has unsupported recipe representation')
    for key in ('recipeSourceSha256', 'instructionSourceSha256'):
        if not isinstance(review[key], str) or not re.fullmatch(r'[a-f0-9]{64}', review[key]):
            raise ValueError(f'acceptance review {key} must be a SHA-256')
    if review['recipeSourceSha256'] != revision['sourceSha256']:
        raise ValueError('acceptance review recipeSourceSha256 must match the run recipe revision')
    reviewer = _safe_text(review['reviewer'], 'acceptance review reviewer', 120)
    executor = _safe_text(review['executor'], 'acceptance review executor', 120)
    if reviewer.casefold().split() == executor.casefold().split():
        raise ValueError('acceptance review reviewer must be distinct from executor')
    reviewed = timestamp(review['reviewedAt'], 'acceptance review reviewedAt')
    if reviewed < timestamp(record['startedAt'], 'execution startedAt'):
        raise ValueError('acceptance review cannot predate its execution')
    finish = timestamp(record['finishedAt'], 'execution finishedAt') if record.get('finishedAt') else None
    if finish and reviewed < finish:
        raise ValueError('acceptance review reviewedAt must be at or after the run finish')
    criteria = review['criteria']
    if not isinstance(criteria, dict) or not criteria:
        raise ValueError('acceptance review requires named measurable criteria')
    if not {'result', 'handoff'} <= set(criteria):
        raise ValueError('acceptance review requires measurable result and handoff criteria')
    cleaned = {}
    for name, criterion in criteria.items():
        if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9 _.-]{0,119}', name):
            raise ValueError('acceptance review criterion name is invalid')
        if not isinstance(criterion, dict) or set(criterion) != {'state', 'expectedResult', 'observedResult', 'sourceRef', 'evidenceRefs'}:
            raise ValueError('acceptance review criterion requires expectedResult, observedResult, sourceRef and evidenceRefs')
        if criterion['state'] not in ACCEPTANCE_STATES:
            raise ValueError('acceptance review criterion has invalid state')
        cleaned[name] = {'state': criterion['state'],
                         'expectedResult': _safe_text(criterion['expectedResult'], 'acceptance expectedResult'),
                         'observedResult': _safe_text(criterion['observedResult'], 'acceptance observedResult'),
                         'sourceRef': _acceptance_refs([criterion['sourceRef']], 'acceptance sourceRef')[0],
                         'evidenceRefs': _acceptance_refs(criterion['evidenceRefs'], 'acceptance evidenceRefs')}
    return dict(review, reviewer=reviewer, executor=executor, criteria=cleaned,
                nextHandoff=_safe_text(review['nextHandoff'], 'acceptance nextHandoff'))


def _setup_text(value, where, limit=600):
    value = _safe_text(value, where, limit)
    if re.search(r'~[/\\]|/(?:private|etc|root|Applications|Volumes|var)/', value, re.I):
        raise ValueError(f'{where}: private paths are forbidden')
    if re.search(r'(?i)(?:token|secret|password|signature|api[ _-]?key|credential)\s*[:=]|'
                 r'\bBearer\s+\S+|\b(?:sk-|gh[pousr]_|github_pat_)[A-Za-z0-9_-]{12,}|'
                 r'-----BEGIN [A-Z ]*PRIVATE KEY-----', value):
        raise ValueError(f'{where}: credential-like text is forbidden')
    return value


def _setup_refs(value, where):
    refs = _acceptance_refs(value, where)
    for ref in refs:
        if not ref.startswith('sha256:'):
            _setup_text(unquote(ref), where, 1200)
            sensitive_keys = {'sig', 'sas', 'auth', 'authorization', 'authcode', 'code',
                              'accesscode', 'key', 'accesskey', 'session', 'sessionid', 'sessionkey'}
            parsed = urlsplit(ref)
            if any(re.sub(r'[^a-z0-9]', '', key.casefold()) in sensitive_keys
                   for part in (parsed.query, parsed.fragment) for key, _ in parse_qsl(part)):
                raise ValueError(f'{where}: signed or credential-like URL parameters are forbidden')
    return refs


def validate_setup_review(review, record, known_slugs):
    """Version 1 records one observed manual-guide attempt, never installation."""
    fields = set(SETUP_PUBLIC_FIELDS) | {'participant', 'criteria'}
    if not isinstance(review, dict) or set(review) != fields:
        raise ValueError('setup review has unsupported or missing fields')
    if type(review['version']) is not int or review['version'] != 1:
        raise ValueError('setup review requires version 1')
    if not isinstance(review['reviewId'], str) or not ID.fullmatch(review['reviewId']):
        raise ValueError('setup review requires stable reviewId')
    if review['executionId'] != record['executionId']:
        raise ValueError('setup review executionId must match its execution')
    if not isinstance(review['taskSlug'], str) or review['taskSlug'] not in known_slugs or review['taskSlug'] not in record['taskSlugs']:
        raise ValueError('setup review taskSlug must be named by its execution')
    revision = record['recipeRevisions'][review['taskSlug']]
    if review['canonicalURL'] != revision['articleUrl']:
        raise ValueError('setup review canonicalURL must match the run recipe revision')
    _setup_refs([review['canonicalURL']], 'setup canonicalURL')
    if urlsplit(review['canonicalURL']).query or urlsplit(review['canonicalURL']).fragment:
        raise ValueError('setup canonicalURL cannot contain query or fragment')
    if not isinstance(review['representation'], str) or review['representation'] not in REPRESENTATIONS:
        raise ValueError('setup review has unsupported recipe representation')
    for key in ('recipeSourceSha256', 'instructionSourceSha256'):
        if not isinstance(review[key], str) or not re.fullmatch(r'[a-f0-9]{64}', review[key]):
            raise ValueError(f'setup review {key} must be a SHA-256')
    if review['recipeSourceSha256'] != revision['sourceSha256']:
        raise ValueError('setup recipeSourceSha256 must match the run recipe revision')
    if review['loadingRoute'] != 'manual-guide':
        raise ValueError('setup version 1 supports only manual-guide; installation and scheduling are not certified')
    if not isinstance(review['participantType'], str) or review['participantType'] not in SETUP_PARTICIPANTS:
        raise ValueError('setup review requires the actual participantType')
    if not isinstance(review['assistance'], str) or review['assistance'] not in {'none', 'provided', 'unknown'}:
        raise ValueError('setup assistance must be none, provided or unknown')
    clean = copy.deepcopy(review)
    for key in ('participant', 'reviewer', 'app', 'surface'):
        clean[key] = _setup_text(review[key], f'setup {key}', 120)
    if clean['participant'].casefold().split() == clean['reviewer'].casefold().split():
        raise ValueError('setup reviewer must be distinct from participant')
    package = review['package']
    if not isinstance(package, dict) or set(package) != {'url', 'sha256', 'memberPath', 'memberSha256', 'onboardingSha256'}:
        raise ValueError('setup package requires URL, archive SHA-256, member path/hash and onboarding hash')
    _setup_refs([package['url']], 'setup package URL')
    if package['url'].startswith('sha256:'):
        raise ValueError('setup package requires a public HTTPS URL')
    for key in ('sha256', 'memberSha256', 'onboardingSha256'):
        if not isinstance(package[key], str) or not re.fullmatch(r'[a-f0-9]{64}', package[key]):
            raise ValueError(f'setup package {key} must be a SHA-256')
    member = package['memberPath']
    if (not isinstance(member, str) or len(member) > 400 or
            not re.fullmatch(r'[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*', member) or
            any(part in {'.', '..'} for part in member.split('/')) or
            not (member.split('/')[-1] == review['taskSlug'] + '.md' or
                 member.split('/')[-2:] == [review['taskSlug'], 'skill.md'])):
        raise ValueError('setup memberPath must be a safe relative path to the named task Markdown guide')
    # Archive, generated member and maintained source are different identities.
    # Their hashes must not be compared for equality (the builder injects content).
    reviewed = timestamp(review['reviewedAt'], 'setup reviewedAt')
    start = timestamp(record['startedAt'], 'execution startedAt')
    if not start <= reviewed <= timestamp(record['updatedAt'], 'execution updatedAt'):
        raise ValueError('setup reviewedAt must be within the recorded execution timeline')
    if record.get('finishedAt') and reviewed < timestamp(record['finishedAt'], 'execution finishedAt'):
        raise ValueError('setup reviewedAt must be at or after the run finish')
    criteria = review['criteria']
    if not isinstance(criteria, dict) or set(criteria) != SETUP_CRITERIA:
        raise ValueError('setup requires filesLoaded, inputsAndAccess, result and handoff criteria')
    for name, item in criteria.items():
        if not isinstance(item, dict) or set(item) != {'state', 'expectedResult', 'observedResult', 'sourceRef', 'evidenceRefs', 'observedAt'}:
            raise ValueError('setup criterion requires dated expected/observed results and source/evidence references')
        if not isinstance(item['state'], str) or item['state'] not in ACCEPTANCE_STATES:
            raise ValueError('setup criterion has invalid state')
        observed = timestamp(item['observedAt'], 'setup criterion observedAt')
        if not start <= observed <= reviewed:
            raise ValueError('setup criterion observedAt must be within the run and no later than review')
        clean['criteria'][name] = {
            'state': item['state'], 'observedAt': item['observedAt'],
            'expectedResult': _setup_text(item['expectedResult'], 'setup expectedResult'),
            'observedResult': _setup_text(item['observedResult'], 'setup observedResult'),
            'sourceRef': _setup_refs([item['sourceRef']], 'setup sourceRef')[0],
            'evidenceRefs': _setup_refs(item['evidenceRefs'], 'setup evidenceRefs')}
    acceptance_id = review['acceptanceReviewId']
    if acceptance_id is not None:
        if not isinstance(acceptance_id, str) or not ID.fullmatch(acceptance_id):
            raise ValueError('setup acceptanceReviewId must be a stable ID or null')
        accepted = next((item for item in record.get('acceptanceReviews', ()) if item['reviewId'] == acceptance_id), None)
        if not accepted or any(accepted[key] != review[key] for key in (
                'taskSlug', 'canonicalURL', 'recipeSourceSha256', 'representation', 'instructionSourceSha256')):
            raise ValueError('setup acceptanceReviewId must bind the same run, task and exact revisions')
        if accepted['executor'].casefold().split() != clean['participant'].casefold().split():
            raise ValueError('setup participant must match the referenced acceptance executor')
        if timestamp(accepted['reviewedAt'], 'acceptance reviewedAt') > reviewed:
            raise ValueError('setup cannot reference a later acceptance review')
    return clean


def validate_record(record, known_slugs):
    if not isinstance(record, dict) or set(record) - FIELDS:
        raise ValueError('execution has unsupported fields; do not store private notes or credentials')
    required = FIELDS - {'finishedAt', 'parentExecutionId', 'acceptanceReviews', 'setupReviews'}
    if required - set(record):
        raise ValueError(f'execution missing fields: {sorted(required - set(record))}')
    eid = record['executionId']
    if not isinstance(eid, str) or not ID.fullmatch(eid):
        raise ValueError('executionId must be a stable identifier, not an article URL or title')
    parent = record.get('parentExecutionId')
    if parent is not None and (not isinstance(parent, str) or not ID.fullmatch(parent) or parent == eid):
        raise ValueError(f'{eid}: parentExecutionId must identify a different real execution')
    slugs = record['taskSlugs']
    if (not isinstance(slugs, list) or not slugs or
            any(not isinstance(s, str) or s not in known_slugs for s in slugs) or
            len(slugs) != len(set(slugs))):
        raise ValueError(f'{eid}: taskSlugs must be distinct existing Task Library slugs')
    revisions = record['recipeRevisions']
    if not isinstance(revisions, dict) or set(revisions) != set(slugs):
        raise ValueError(f'{eid}: recipeRevisions must identify the actual canonical source for each task')
    for slug, source in revisions.items():
        if (not isinstance(source, dict) or set(source) != {'articleUrl', 'sourceSha256'} or
                not isinstance(source.get('sourceSha256'), str) or
                not re.fullmatch(r'[a-f0-9]{64}', source['sourceSha256'])):
            raise ValueError(f'{eid}: each recipe revision needs articleUrl and sourceSha256')
        public_url(source['articleUrl'], f'{eid}.recipeRevisions.{slug}')
    status = record['status']
    if status not in STATUSES:
        raise ValueError(f'{eid}: unknown execution status')
    start = timestamp(record['startedAt'], f'{eid}.startedAt')
    recorded = timestamp(record['recordedAt'], f'{eid}.recordedAt')
    updated = timestamp(record['updatedAt'], f'{eid}.updatedAt')
    if recorded < start or updated < recorded:
        raise ValueError(f'{eid}: timestamps are out of order')
    finish = record.get('finishedAt')
    if status in TERMINAL and not finish:
        raise ValueError(f'{eid}: terminal status requires finishedAt')
    if status not in TERMINAL and finish:
        raise ValueError(f'{eid}: unfinished run cannot have finishedAt')
    if finish and not start <= timestamp(finish, f'{eid}.finishedAt') <= updated:
        raise ValueError(f'{eid}: finishedAt is out of order')
    result = record['result']
    if not isinstance(result, str) or not result.strip() or len(result) > 600:
        raise ValueError(f'{eid}: result requires a short public-safe description')
    evidence = record['evidence']
    if not isinstance(evidence, list):
        raise ValueError(f'{eid}: evidence must be a list')
    for item in evidence:
        if not isinstance(item, dict):
            raise ValueError(f'{eid}: evidence must be an object')
        if item.get('visibility') == 'public':
            if set(item) != {'visibility', 'url'}:
                raise ValueError(f'{eid}: public evidence accepts only visibility and URL')
            public_url(item['url'], f'{eid}.evidence')
        elif item.get('visibility') == 'private':
            if set(item) != {'visibility', 'sha256'} or not isinstance(item.get('sha256'), str) or not re.fullmatch(r'[a-f0-9]{64}', item.get('sha256', '')):
                raise ValueError(f'{eid}: private evidence accepts only a SHA-256; keep paths and data outside this repo')
        else:
            raise ValueError(f'{eid}: evidence visibility must be explicit')
    if status == 'completed' and not evidence:
        raise ValueError(f'{eid}: completed work requires recorded evidence')
    meta = record['metaArticle']
    if not isinstance(meta, dict) or meta.get('status') not in META_STATES:
        raise ValueError(f'{eid}: every run needs a meta-article writing state')
    allowed = {'status', 'url'} if meta['status'] == 'published' else {'status', 'draftSha256'}
    if set(meta) != allowed:
        raise ValueError(f'{eid}: meta article requires a public URL or saved-draft hash; publication is separate')
    if meta['status'] == 'published':
        public_url(meta['url'], f'{eid}.metaArticle.url')
    elif not isinstance(meta.get('draftSha256'), str) or not re.fullmatch(r'[a-f0-9]{64}', meta.get('draftSha256', '')):
        raise ValueError(f'{eid}: draft/withheld meta article requires its saved-content hash')
    reviews = record.get('acceptanceReviews', [])
    if not isinstance(reviews, list):
        raise ValueError(f'{eid}: acceptanceReviews must be a list')
    clean_reviews = [validate_acceptance_review(item, record, known_slugs) for item in reviews]
    ids = [item['reviewId'] for item in clean_reviews]
    if len(ids) != len(set(ids)):
        raise ValueError(f'{eid}: acceptance review IDs must be unique per run')
    review_times = [(item['taskSlug'], timestamp(item['reviewedAt'], 'acceptance review reviewedAt')) for item in clean_reviews]
    if len(review_times) != len(set(review_times)):
        raise ValueError(f'{eid}: acceptance reviews need distinct task and review timestamps')
    if any(when > updated for _, when in review_times):
        raise ValueError(f'{eid}: acceptance review reviewedAt cannot be after updatedAt')
    clean = copy.deepcopy(record)
    if 'acceptanceReviews' in clean or clean_reviews:
        clean['acceptanceReviews'] = clean_reviews
    setup_reviews = record.get('setupReviews', [])
    if not isinstance(setup_reviews, list):
        raise ValueError(f'{eid}: setupReviews must be a list')
    clean_setup = [validate_setup_review(item, clean, known_slugs) for item in setup_reviews]
    if len({item['reviewId'] for item in clean_setup}) != len(clean_setup):
        raise ValueError(f'{eid}: setup review IDs must be unique per run')
    if len({(item['taskSlug'], timestamp(item['reviewedAt'], 'setup reviewedAt')) for item in clean_setup}) != len(clean_setup):
        raise ValueError(f'{eid}: setup reviews need distinct task and review timestamps')
    if 'setupReviews' in clean:
        clean['setupReviews'] = clean_setup
    return clean


def validate_ledger(raw, known_slugs):
    if not isinstance(raw, dict) or set(raw) != {'schemaVersion', 'executions'} or (type(raw['schemaVersion']) is not int or raw['schemaVersion'] != 1):
        raise ValueError('execution ledger requires schemaVersion 1 and executions')
    if not isinstance(raw['executions'], list):
        raise ValueError('executions must be a list')
    records = [validate_record(r, known_slugs) for r in raw['executions']]
    ids = [r['executionId'] for r in records]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate executionId: revisions and derivative articles are not new runs')
    by_id = {r['executionId']: r for r in records}
    for record in records:
        seen = {record['executionId']}
        parent = record.get('parentExecutionId')
        while parent:
            if parent not in by_id:
                raise ValueError('parentExecutionId must reference an existing ledger execution')
            if parent in seen:
                raise ValueError('parentExecutionId cannot form a cycle')
            seen.add(parent)
            parent = by_id[parent].get('parentExecutionId')
    return records


def load(path, known_slugs):
    return validate_ledger(json.loads(Path(path).read_text(encoding='utf-8')), known_slugs)


def public_record(record):
    result = {key: record[key] for key in
              ('executionId', 'taskSlugs', 'startedAt', 'status', 'result', 'recipeRevisions')}
    if record.get('finishedAt'):
        result['finishedAt'] = record['finishedAt']
    if record.get('parentExecutionId'):
        result['parentExecutionId'] = record['parentExecutionId']
    result['evidenceUrls'] = [e['url'] for e in record['evidence'] if e['visibility'] == 'public']
    result['privateEvidenceRecorded'] = any(e['visibility'] == 'private' for e in record['evidence'])
    result['metaArticle'] = {'status': record['metaArticle']['status']}
    if record['metaArticle']['status'] == 'published':
        result['metaArticle']['url'] = record['metaArticle']['url']
    if record.get('acceptanceReviews'):
        result['acceptanceReviews'] = [public_acceptance_review(review) for review in record['acceptanceReviews']]
    if record.get('setupReviews'):
        result['setupReviews'] = [public_setup_review(review) for review in record['setupReviews']]
    return result


def _public_review_criteria(review):
    criteria = {}
    for name, item in review['criteria'].items():
        criteria[name] = {'state': item['state'], 'expectedResult': item['expectedResult'], 'observedResult': item['observedResult'],
                          'sourceUrl': item['sourceRef'] if not item['sourceRef'].startswith('sha256:') else None,
                          'sourcePrivateEvidenceRecorded': item['sourceRef'].startswith('sha256:'),
                          'evidenceUrls': [ref for ref in item['evidenceRefs'] if not ref.startswith('sha256:')],
                          'privateEvidenceRecorded': any(ref.startswith('sha256:') for ref in item['evidenceRefs'])}
    return criteria


def public_acceptance_review(review):
    # Keep executor identity in the source ledger for independence validation.
    # A linked setup review can make that executor a private novice participant.
    return {key: review[key] for key in ('version', 'reviewId', 'taskSlug', 'canonicalURL', 'recipeSourceSha256',
            'representation', 'instructionSourceSha256', 'reviewedAt', 'reviewer', 'nextHandoff')} | {'criteria': _public_review_criteria(review)}


def public_setup_review(review):
    # Reuse the acceptance evidence allowlist; private refs become booleans.
    criteria = _public_review_criteria(review)
    for name, item in criteria.items():
        item['observedAt'] = review['criteria'][name]['observedAt']
    return {key: copy.deepcopy(review[key]) for key in SETUP_PUBLIC_FIELDS} | {'criteria': criteria}


def check_times_not_future(records, now):
    for record in records:
        for key in ('startedAt', 'finishedAt', 'recordedAt', 'updatedAt'):
            if record.get(key) and timestamp(record[key], key) > now:
                raise ValueError('execution timestamps cannot be in the future')
        for review in record.get('acceptanceReviews', ()):
            if timestamp(review['reviewedAt'], 'acceptance review reviewedAt') > now:
                raise ValueError('acceptance review timestamps cannot be in the future')
        for review in record.get('setupReviews', ()):
            if timestamp(review['reviewedAt'], 'setup reviewedAt') > now or any(
                    timestamp(item['observedAt'], 'setup observedAt') > now for item in review['criteria'].values()):
                raise ValueError('setup review timestamps cannot be in the future')


def attach(tasks, records, as_of=None):
    """Count each execution once per named task; never infer runs from meta URLs."""
    now = as_of or datetime.now(timezone.utc)
    records = validate_ledger({'schemaVersion': 1, 'executions': records},
                              {t['slug'] for t in tasks})
    check_times_not_future(records, now)
    recent = now - timedelta(days=30)
    for task in tasks:
        runs = [r for r in records if task['slug'] in r['taskSlugs']]
        completed = [r for r in runs if r['status'] == 'completed']
        task['executionHistory'] = {
            'status': 'partial' if runs else 'unknown',
            'recordedRuns': len(runs) if runs else None,
            'completedRuns': len(completed) if runs else None,
            'failedRuns': sum(r['status'] == 'failed' for r in runs) if runs else None,
            'partialRuns': sum(r['status'] == 'partial' for r in runs) if runs else None,
            'completedLast30Days': sum(recent <= timestamp(r['finishedAt'], 'finishedAt') <= now
                                       for r in completed) if runs else None,
            'lastCompletedAt': max((r['finishedAt'] for r in completed),
                                   key=lambda value: timestamp(value, 'finishedAt'), default=None),
            'executionIds': sorted(r['executionId'] for r in runs),
            'executionOutcomes': [{'executionId': r['executionId'], 'status': r['status'],
                                   'startedAt': r['startedAt'], 'finishedAt': r.get('finishedAt')} for r in runs],
            'acceptanceReviews': [dict(public_acceptance_review(review), executionId=r['executionId']) for r in runs
                                  for review in r.get('acceptanceReviews', ()) if review['taskSlug'] == task['slug']],
            'setupReviews': [public_setup_review(review) for r in runs
                             for review in r.get('setupReviews', ()) if review['taskSlug'] == task['slug']],
        }
    return {'schemaVersion': 1, 'asOf': now.isoformat(),
            'countDefinition': 'Distinct recorded execution IDs, separate from meta-article URLs. History is partial; absent history is unknown, not zero. The last-30-day count is a documented lower bound, not total task frequency.',
            'recordedExecutions': len(records) if records else None,
            'completedExecutions': sum(r['status'] == 'completed' for r in records) if records else None,
            'partialExecutions': sum(r['status'] == 'partial' for r in records) if records else None,
            'executions': [public_record(r) for r in records]}


def digest(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def _upsert_locked(path, record, known_slugs, expected_revision=None, dry_run=False):
    """Atomic, idempotent recording. Failed validation leaves the ledger unchanged."""
    path = Path(path)
    candidate = validate_record(record, known_slugs)
    check_times_not_future([candidate], datetime.now(timezone.utc))
    with path.open(encoding='utf-8') as source:
        raw = json.load(source)
    records = validate_ledger(raw, known_slugs)
    found = next((r for r in records if r['executionId'] == candidate['executionId']), None)
    # Older clients do not know optional review fields; preserve their history.
    for field in ('acceptanceReviews', 'setupReviews'):
        if found and field not in record and found.get(field):
            candidate[field] = copy.deepcopy(found[field])
    if found:
        by_id = {item['reviewId']: item for item in candidate.get('setupReviews', ())}
        if any(by_id.get(item['reviewId']) != item for item in found.get('setupReviews', ())):
            raise ValueError('setup review history is append-only; add a later correction review')
        linked_acceptance = {item['acceptanceReviewId'] for item in found.get('setupReviews', ())}
        acceptance_by_id = {item['reviewId']: item for item in candidate.get('acceptanceReviews', ())}
        if any(acceptance_by_id.get(item['reviewId']) != item
               for item in found.get('acceptanceReviews', ()) if item['reviewId'] in linked_acceptance):
            raise ValueError('acceptance reviews referenced by setup history are immutable; add a later correction review')
    if found == candidate:
        return {'action': 'unchanged', 'executionId': candidate['executionId'], 'revision': digest(found)}
    if found:
        if expected_revision != digest(found):
            raise ValueError('execution exists: supply its current --expected-revision to update it')
        for key in ('executionId', 'taskSlugs', 'startedAt', 'recordedAt'):
            if found[key] != candidate[key]:
                raise ValueError(f'{key} is immutable; a retry with different work is a new execution')
        if timestamp(candidate['updatedAt'], 'updatedAt') <= timestamp(found['updatedAt'], 'updatedAt'):
            raise ValueError('an update must have a later updatedAt')
        # Correcting a false completion requires an explicit revision, never a new ID.
        records[records.index(found)] = candidate
    else:
        if expected_revision is not None:
            raise ValueError('cannot update an execution ID that is not recorded')
        records.append(candidate)
    validate_ledger({'schemaVersion': 1, 'executions': records}, known_slugs)
    outcome = {'action': 'updated' if found else 'created',
               'executionId': candidate['executionId'], 'revision': digest(candidate)}
    if dry_run:
        return dict(outcome, written=False)
    encoded = json.dumps({'schemaVersion': 1, 'executions': records}, indent=2) + '\n'
    handle, temporary = tempfile.mkstemp(prefix=path.name + '.', dir=path.parent)
    try:
        with os.fdopen(handle, 'w', encoding='utf-8') as target:
            target.write(encoded)
            target.flush()
            os.fsync(target.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return outcome


def upsert(path, record, known_slugs, expected_revision=None, dry_run=False):
    path = Path(path)
    # Stable sidecar survives os.replace and serializes CLI or library callers.
    with path.with_suffix('.lock').open('a', encoding='utf-8') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return _upsert_locked(path, record, known_slugs, expected_revision, dry_run)
