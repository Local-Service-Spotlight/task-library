"""Validate and evaluate exact-revision article semantic review evidence."""
from datetime import datetime, timedelta, timezone
import json
import re
from urllib.parse import urlsplit

import executions


SCHEMA_VERSION = 1
FRESHNESS_HOURS = 24
CRITERION_ORDER = (
    'openingContext', 'roleScope', 'owner', 'steps', 'links', 'sourceEvidence',
    'handoffContext', 'visualAndLayout', 'publicationStandards', 'acceptanceResults')
STATES = {'pass', 'unmet', 'hold', 'unknown'}
REPRESENTATIONS = {
    'public-rendered-html',
    'public-visible-text',
    'wordpress-content-html',
    'repository-source',
}
SHA256_RE = re.compile(r'^[0-9a-f]{64}$')
RFC3339_RE = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$')
PRIVATE_MARKERS = ('/users/', '/home/', 'file://', '\\users\\', 'localhost')
CREDENTIAL_RE = re.compile(r'token|secret|password|signature|api.?key|credential', re.I)


def _record_error(path, section, index, message):
    raise ValueError(f'{path}: {section}[{index}] {message}')


def _public_text(value, field, limit, path, section, index):
    if not isinstance(value, str) or not value.strip():
        _record_error(path, section, index, f'requires nonempty {field}')
    value = value.strip()
    if len(value) > limit:
        _record_error(path, section, index, f'{field} exceeds {limit} characters')
    lowered = value.lower()
    if any(marker in lowered for marker in PRIVATE_MARKERS) or any(
            ord(character) < 32 and character not in '\t\n\r' for character in value):
        _record_error(path, section, index, f'{field} is not public-safe')
    return value


def _timestamp(value, field, path, section, index):
    if not isinstance(value, str) or not RFC3339_RE.fullmatch(value):
        _record_error(path, section, index, f'requires RFC3339 UTC {field}')
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        _record_error(path, section, index, f'has invalid {field}')
    return parsed


def _sha256(value, field, path, section, index, allow_null=False):
    if allow_null and value is None:
        return None
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        _record_error(path, section, index, f'requires lowercase SHA-256 {field}')
    return value


def _public_evidence_refs(value, path, section, index):
    if not isinstance(value, list) or not value or len(value) > 10:
        _record_error(path, section, index, 'requires 1-10 evidenceRefs')
    refs = []
    for position, ref in enumerate(value):
        if not isinstance(ref, str) or not ref.strip() or len(ref.strip()) > 1200:
            _record_error(path, section, index,
                          f'evidenceRefs[{position}] must be a nonempty string up to 1200 characters')
        ref = ref.strip()
        if ref.startswith('sha256:') and SHA256_RE.fullmatch(ref[7:]):
            refs.append(ref)
            continue
        try:
            executions.public_url(ref, f'{section}[{index}].evidenceRefs[{position}]')
        except ValueError as exc:
            _record_error(path, section, index, str(exc))
        if CREDENTIAL_RE.search(urlsplit(ref).fragment):
            _record_error(path, section, index,
                          f'evidenceRefs[{position}] credential-like fragment is forbidden')
        refs.append(ref)
    return refs


def _common(record, expected, path, section, index):
    if not isinstance(record, dict) or set(record) != expected:
        missing = sorted(expected - set(record)) if isinstance(record, dict) else sorted(expected)
        extra = sorted(set(record) - expected) if isinstance(record, dict) else []
        _record_error(path, section, index,
                      f'must have exact fields; missing={missing}, extra={extra}')
    if type(record['version']) is not int or record['version'] != SCHEMA_VERSION:
        _record_error(path, section, index, f'requires version {SCHEMA_VERSION}')
    task_slug = _public_text(record['taskSlug'], 'taskSlug', 200, path, section, index)
    canonical_url = _public_text(
        record['canonicalURL'], 'canonicalURL', 1200, path, section, index)
    try:
        executions.public_url(canonical_url, f'{section}[{index}].canonicalURL')
    except ValueError as exc:
        _record_error(path, section, index, str(exc))
    parsed = urlsplit(canonical_url)
    if parsed.scheme != 'https' or not parsed.netloc or parsed.query or parsed.fragment:
        _record_error(path, section, index,
                      'canonicalURL must be an exact HTTPS article URL without query or fragment')
    representation = record['representation']
    if representation not in REPRESENTATIONS:
        _record_error(path, section, index,
                      f'representation must be one of {sorted(REPRESENTATIONS)}')
    return task_slug, canonical_url, representation


def _review(record, path, index):
    section = 'semanticReviews'
    fields = {'version', 'taskSlug', 'canonicalURL', 'sourceSha256', 'representation',
              'reviewedAt', 'reviewer', 'criteria'}
    task_slug, canonical_url, representation = _common(
        record, fields, path, section, index)
    source_hash = _sha256(record['sourceSha256'], 'sourceSha256', path, section, index)
    reviewed_at = _timestamp(record['reviewedAt'], 'reviewedAt', path, section, index)
    reviewer = _public_text(record['reviewer'], 'reviewer', 120, path, section, index)
    criteria = record['criteria']
    if not isinstance(criteria, dict) or set(criteria) != set(CRITERION_ORDER):
        _record_error(path, section, index,
                      f'criteria must contain exactly {list(CRITERION_ORDER)}')
    clean_criteria = {}
    check_fields = {'state', 'reason', 'evidenceRefs'}
    for name in CRITERION_ORDER:
        check = criteria[name]
        if not isinstance(check, dict) or set(check) != check_fields:
            _record_error(path, section, index,
                          f'criterion {name} must contain exactly {sorted(check_fields)}')
        if check['state'] not in STATES:
            _record_error(path, section, index,
                          f'criterion {name} has invalid state {check["state"]!r}')
        clean_criteria[name] = {
            'state': check['state'],
            'reason': _public_text(
                check['reason'], f'criteria.{name}.reason', 600, path, section, index),
            'evidenceRefs': _public_evidence_refs(
                check['evidenceRefs'], path, f'{section}.{name}', index),
        }
    return {
        'version': SCHEMA_VERSION, 'taskSlug': task_slug, 'canonicalURL': canonical_url,
        'sourceSha256': source_hash, 'representation': representation,
        'reviewedAt': record['reviewedAt'], '_reviewedAt': reviewed_at,
        'reviewer': reviewer, 'criteria': clean_criteria,
    }


def _observation(record, path, index):
    section = 'revisionObservations'
    fields = {'version', 'taskSlug', 'canonicalURL', 'sourceSha256', 'representation',
              'observedAt', 'observer', 'state', 'reason', 'evidenceRefs'}
    task_slug, canonical_url, representation = _common(
        record, fields, path, section, index)
    if record['state'] not in {'observed', 'failed'}:
        _record_error(path, section, index, 'state must be observed or failed')
    source_hash = _sha256(record['sourceSha256'], 'sourceSha256', path, section, index,
                          allow_null=record['state'] == 'failed')
    if record['state'] == 'failed' and source_hash is not None:
        _record_error(path, section, index, 'failed observation must use null sourceSha256')
    if record['state'] == 'observed' and source_hash is None:
        _record_error(path, section, index, 'observed revision requires sourceSha256')
    observed_at = _timestamp(record['observedAt'], 'observedAt', path, section, index)
    return {
        'version': SCHEMA_VERSION, 'taskSlug': task_slug, 'canonicalURL': canonical_url,
        'sourceSha256': source_hash, 'representation': representation,
        'observedAt': record['observedAt'], '_observedAt': observed_at,
        'observer': _public_text(record['observer'], 'observer', 120, path, section, index),
        'state': record['state'],
        'reason': _public_text(record['reason'], 'reason', 600, path, section, index),
        'evidenceRefs': _public_evidence_refs(record['evidenceRefs'], path, section, index),
    }


def load(path):
    """Load optional versioned semantic reviews and separate revision observations."""
    with open(path, encoding='utf-8') as source:
        raw = json.load(source)
    if not isinstance(raw, dict):
        raise ValueError(f'{path}: expected an object')
    review_rows = raw.get('semanticReviews', [])
    observation_rows = raw.get('revisionObservations', [])
    if not isinstance(review_rows, list) or not isinstance(observation_rows, list):
        raise ValueError(f'{path}: semanticReviews and revisionObservations must be arrays')
    reviews = [_review(row, path, index) for index, row in enumerate(review_rows)]
    observations = [_observation(row, path, index)
                    for index, row in enumerate(observation_rows)]
    review_ids = [(r['taskSlug'], r['canonicalURL'], r['representation'], r['reviewedAt'])
                  for r in reviews]
    observation_ids = [(r['taskSlug'], r['canonicalURL'], r['representation'], r['observedAt'])
                       for r in observations]
    if len(review_ids) != len(set(review_ids)):
        raise ValueError(f'{path}: duplicate semantic review identity')
    if len(observation_ids) != len(set(observation_ids)):
        raise ValueError(f'{path}: duplicate revision observation identity')
    return {'semanticReviews': reviews, 'revisionObservations': observations}


def validate_task_mappings(tasks, evidence, normalize_url):
    """Require every evidence record to name an exact existing task/article mapping."""
    mapped = {task['slug']: task.get('article') for task in tasks}
    for section in ('semanticReviews', 'revisionObservations'):
        for record in evidence[section]:
            expected = mapped.get(record['taskSlug'])
            if expected is None:
                raise ValueError(f'{section}: unknown taskSlug {record["taskSlug"]!r}')
            if record['canonicalURL'] != expected:
                raise ValueError(
                    f'{section}: {record["taskSlug"]} canonicalURL does not exactly match '
                    'the final task mapping')
            if normalize_url(record['canonicalURL']) != normalize_url(expected):
                raise ValueError(f'{section}: invalid canonicalURL for {record["taskSlug"]}')


def evaluate(task, evidence, now=None):
    """Evaluate one task without treating a review's own hash as current observation."""
    now = now or datetime.now(timezone.utc)
    reviews = [row for row in evidence.get('semanticReviews', ())
               if row['taskSlug'] == task['slug'] and row['canonicalURL'] == task.get('article')]
    if not reviews:
        return {'state': 'unknown',
                'reason': 'No exact-revision positive semantic review is recorded for this article.'}
    review = max(reviews, key=lambda row: row['_reviewedAt'])
    observations = [row for row in evidence.get('revisionObservations', ())
                    if row['taskSlug'] == task['slug'] and
                    row['canonicalURL'] == review['canonicalURL'] and
                    row['representation'] == review['representation']]
    public_review = {key: value for key, value in review.items() if not key.startswith('_')}
    if not observations:
        return {'state': 'unknown',
                'reason': 'The semantic review has no separate current revision observation.',
                'semanticReview': public_review}
    observation = max(observations, key=lambda row: row['_observedAt'])
    public_observation = {key: value for key, value in observation.items()
                          if not key.startswith('_')}
    common = {'semanticReview': public_review, 'revisionObservation': public_observation}
    if observation['state'] == 'failed':
        return {'state': 'unknown',
                'reason': 'The latest separate article revision observation failed.', **common}
    if observation['_observedAt'] < review['_reviewedAt']:
        return {'state': 'unknown',
                'reason': 'The latest article revision observation is older than the semantic review.',
                **common}
    age = now - observation['_observedAt']
    if age < timedelta(0) or age > timedelta(hours=FRESHNESS_HOURS):
        return {'state': 'unknown',
                'reason': f'The article revision observation is outside the {FRESHNESS_HOURS}-hour freshness window.',
                **common}
    if observation['sourceSha256'] != review['sourceSha256']:
        return {'state': 'unmet',
                'reason': 'The observed article source hash does not match the reviewed revision.',
                **common}
    states = [review['criteria'][name]['state'] for name in CRITERION_ORDER]
    state = next((candidate for candidate in ('hold', 'unmet', 'unknown')
                  if candidate in states), 'pass')
    if state == 'pass':
        reason = ('All ten semantic criteria pass for the separately observed current article '
                  'revision.')
    else:
        affected = [name for name in CRITERION_ORDER
                    if review['criteria'][name]['state'] == state]
        reason = f'Current article semantic criteria are {state}: {", ".join(affected)}.'
    return {'state': state, 'reason': reason, **common}
