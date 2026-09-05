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
from urllib.parse import parse_qsl, urlsplit

STATUSES = {'running', 'completed', 'partial', 'failed', 'blocked', 'cancelled'}
TERMINAL = {'completed', 'partial', 'failed', 'cancelled'}
META_STATES = {'draft', 'published', 'withheld'}
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._:-]{2,159}$')
FIELDS = {'executionId', 'taskSlugs', 'startedAt', 'finishedAt', 'status',
          'result', 'evidence', 'metaArticle', 'recipeRevisions', 'parentExecutionId', 'recordedAt', 'updatedAt'}


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


def validate_record(record, known_slugs):
    if not isinstance(record, dict) or set(record) - FIELDS:
        raise ValueError('execution has unsupported fields; do not store private notes or credentials')
    required = FIELDS - {'finishedAt', 'parentExecutionId'}
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
    return copy.deepcopy(record)


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
    return result


def check_times_not_future(records, now):
    for record in records:
        for key in ('startedAt', 'finishedAt', 'recordedAt', 'updatedAt'):
            if record.get(key) and timestamp(record[key], key) > now:
                raise ValueError('execution timestamps cannot be in the future')


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
