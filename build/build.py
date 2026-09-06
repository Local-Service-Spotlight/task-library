#!/usr/bin/env python3
"""Task Library build: resolve registry -> validate skills -> compose dashboard data.json.

Sources per skill (build/registry.json):
  "local"                                   -> skills/<category-folder>/<slug>.md
  "github:<owner>/<repo>@<ref>:<path>"      -> fetched from raw.githubusercontent.com

External fetches are cached in build/.cache/; on fetch failure the last good
copy is used (with a warning) so a deleted or renamed repo never blanks a skill.

Optional: --tracker-csv <file> overrides status/owner/article per slug from the
Asset Tracker's published CSV (columns: Slug, Status, Owner, Definitive Article URL).

Usage:
  python3 build/build.py [--tracker-csv tracker.csv] [--out dashboard/data.json]
Exit code 1 if any skill fails validation (build still writes valid skills).
"""
import argparse, csv, hashlib, json, os, re, sys, urllib.request
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import urlencode, urlsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
CACHE = os.path.join(BUILD, '.cache')
sys.path.insert(0, BUILD)
import factory  # noqa: E402
import executions  # noqa: E402

STAGES = {'Produce', 'Process', 'Post', 'Promote', '—', ''}
STATUSES = {'complete', 'needs-work', 'gap'}
ARTICLE_KINDS = {'task-recipe', 'topic-hub', 'entity-hub', 'reference', 'supporting', 'unknown'}
REQUIRED_FM = ['name', 'description', 'category', 'stage', 'definitive_article', 'status']
REQUIRED_SECTIONS = ['## Inputs', '## Steps', '## Definition of done (QA checklist)',
                     '## Example(s)', '## Definitive article & links']
STUB = re.compile(r'(placeholder|TBD|to be (written|documented|filled)|coming soon|lorem ipsum)', re.I)
ARTICLE_CERTIFICATIONS = os.path.join(BUILD, 'article-certifications.json')
ARTICLE_META_ORBITS = os.path.join(BUILD, 'article-meta-orbits.json')
META_COUNT_STATUSES = {'verified', 'partial'}
META_ORBIT_TIERS = (
    (0, 0, 'No verified examples'),
    (1, 2, 'Emerging'),
    (3, 5, 'Supported'),
    (6, 10, 'Strong'),
    (11, None, 'Deep'),
)


def folder_of(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower().replace('—', ' ')).strip('-')


def parse_frontmatter(text):
    m = re.match(r'---\s*\n(.*?)\n---\s*\n', text, re.S)
    if not m:
        return None, text
    fm, key = {}, None
    for line in m.group(1).splitlines():
        if line[:1] in (' ', '\t') and key:          # continuation of folded/multiline value
            fm[key] = (fm[key] + ' ' + line.strip()).strip()
            continue
        if ':' in line:
            k, v = line.split(':', 1)
            v = v.strip()
            if v in ('>', '>-', '|', '|-'):
                v = ''                                # folded block scalar starts
            elif len(v) > 1 and v[0] == v[-1] and v[0] in '"\'':
                v = v[1:-1]
            key = k.strip()
            fm[key] = v
    return fm, text[m.end():]


def current_instruction_review(slug, text, reviews):
    """A source edit expires its review; this never promotes task or article status."""
    review = reviews.get(slug)
    if review is None:
        return None
    if not isinstance(review, dict) or not re.fullmatch(r'[0-9a-f]{64}', review.get('source_sha256', '')):
        raise ValueError(f'{slug}: invalid instruction review source hash')
    valid_review_date(review.get('reviewed_at'), f'{slug}: instruction review date')
    if not review.get('reviewer') or not review.get('scope'):
        raise ValueError(f'{slug}: instruction review needs reviewer and scope')
    if hashlib.sha256(text.encode('utf-8')).hexdigest() != review['source_sha256']:
        return None
    return dict(review)


def display_title(text, slug):
    """Use the maintained heading for readers; keep the registry slug for identity."""
    _, body = parse_frontmatter(text)
    fence = None
    for line in body.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            kind = marker.group(1)[0]
            fence = None if fence == kind else (kind if fence is None else fence)
            continue
        if fence is None:
            heading = re.match(r'^#\s+(.+?)\s*#*\s*$', line)
            if heading:
                return heading.group(1).strip()
    return slug.replace('-', ' ').capitalize()


def resolve(slug, entry, errors, warnings):
    src = entry['source']
    if src == 'local':
        path = os.path.join(ROOT, 'skills', folder_of(entry['category']), slug + '.md')
        if not os.path.exists(path):
            errors.append(f'{slug}: local file missing ({os.path.relpath(path, ROOT)})')
            return None
        return open(path, encoding='utf-8').read()

    m = re.match(r'github:([^/]+)/([^@]+)@([^:]+):(.+)', src)
    if not m:
        errors.append(f'{slug}: unrecognized source "{src}"')
        return None
    owner, repo, ref, path = m.groups()
    url = f'https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{path}'
    cache_file = os.path.join(CACHE, slug + '.md')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'task-library-build'})
        tok = os.environ.get('SKILLS_READ_TOKEN')
        if tok:
            req.add_header('Authorization', 'Bearer ' + tok)
        with urllib.request.urlopen(req, timeout=30) as r:
            text = r.read().decode('utf-8')
        os.makedirs(CACHE, exist_ok=True)
        open(cache_file, 'w', encoding='utf-8').write(text)
        return text
    except Exception as e:
        if os.path.exists(cache_file):
            warnings.append(f'{slug}: fetch failed ({e}); using cached copy')
            return open(cache_file, encoding='utf-8').read()
        errors.append(f'{slug}: fetch failed ({e}) and no cached copy')
        return None


def validate(slug, entry, text, errors, warnings):
    fm, body = parse_frontmatter(text)
    if fm is None:
        errors.append(f'{slug}: missing frontmatter block')
        return None
    if entry.get('format') == 'claude-skill':
        # Standard Claude skill: frontmatter has name+description only.
        # Library metadata (category/stage/status/article) comes from the
        # registry entry (overridable by the tracker CSV), not the file.
        for k in ('name', 'description'):
            if not fm.get(k):
                errors.append(f'{slug}: claude-skill missing frontmatter "{k}"')
                return None
        if fm['name'] != slug:
            warnings.append(f'{slug}: claude-skill name "{fm["name"]}" differs from registry slug (registry wins)')
        stage = entry.get('stage', '—')
        status = entry.get('status', 'needs-work')
        if stage not in STAGES or status not in STATUSES:
            errors.append(f'{slug}: registry has invalid stage/status for claude-skill')
            return None
        desc = re.split(r'(?<=[.!?]) ', fm['description'])[0][:300]
        return {'name': slug, 'description': desc, 'category': entry['category'],
                'stage': stage, 'status': status,
                'definitive_article': entry.get('article', '')}
    for k in REQUIRED_FM:
        if k not in fm or not fm[k]:
            errors.append(f'{slug}: frontmatter missing "{k}"')
            return None
    if fm['name'] != slug:
        errors.append(f'{slug}: frontmatter name "{fm["name"]}" must equal registry slug')
        return None
    if fm['category'] != entry['category']:
        warnings.append(f'{slug}: frontmatter category "{fm["category"]}" != registry "{entry["category"]}" (registry wins)')
    if fm['stage'] not in STAGES:
        errors.append(f'{slug}: invalid stage "{fm["stage"]}"')
        return None
    if fm['status'] not in STATUSES:
        errors.append(f'{slug}: invalid status "{fm["status"]}"')
        return None
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    if missing:
        errors.append(f'{slug}: missing sections {missing}')
        return None
    if len(re.findall(r'^\d+\.', body, re.M)) < 3:
        warnings.append(f'{slug}: fewer than 3 numbered steps')
    if fm['status'] == 'complete' and STUB.search(text):
        warnings.append(f'{slug}: status complete but contains stub language')
    return fm


def article_url(v):
    if not v or v.lower().startswith('gap'):
        return None
    if v.startswith('http'):
        return v
    if v.startswith('/'):
        return 'https://blitzmetrics.com' + v
    return None


def normalize_article_url(url):
    """Return a stable key for grouping tasks that map to the same article.

    Article identity is independent of http/https, a leading ``www.``, a
    trailing slash, query parameters, and fragments. Paths remain
    case-sensitive because that is part of URL semantics outside WordPress.
    """
    if not url:
        return None
    raw = str(url).strip()
    if not raw:
        return None
    parsed = urlsplit(raw)
    if not parsed.netloc:
        return None
    host = (parsed.hostname or '').lower()
    if host.startswith('www.'):
        host = host[4:]
    if not host:
        return None
    try:
        port = parsed.port
    except ValueError:
        return None
    if port and not ((parsed.scheme.lower() == 'http' and port == 80) or
                     (parsed.scheme.lower() == 'https' and port == 443)):
        host = f'{host}:{port}'
    path = re.sub(r'/+', '/', parsed.path or '/')
    if path != '/':
        path = path.rstrip('/')
    return host + path


def require_absolute_http_url(value, field):
    """Return a stripped absolute HTTP(S) URL or fail with field context."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{field} requires a non-empty absolute URL')
    value = value.strip()
    parsed = urlsplit(value)
    if parsed.scheme.lower() not in ('http', 'https') or not parsed.netloc:
        raise ValueError(f'{field} requires an absolute HTTP(S) URL')
    if not normalize_article_url(value):
        raise ValueError(f'{field} has an invalid URL "{value}"')
    return value


def valid_review_date(value, field):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError(f'{field} requires a YYYY-MM-DD date')
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except ValueError as exc:
        raise ValueError(f'{field} has an invalid date "{value}"') from exc
    return value


def adapt_strength_manifest(raw, path, evidence_url=None):
    """Convert the WordPress inventory receipt into the strict orbit schema."""
    if not isinstance(raw, dict) or 'schemaVersion' not in raw:
        return raw
    if raw.get('schemaVersion') != 1:
        raise ValueError(f'{path}: unsupported strength manifest schemaVersion')
    generated = raw.get('generatedAt')
    if not isinstance(generated, str) or not re.match(r'^\d{4}-\d{2}-\d{2}T', generated):
        raise ValueError(f'{path}: generatedAt requires an ISO timestamp')
    audited = valid_review_date(raw.get('metaAuditedAt', generated[:10]), f'{path}.metaAuditedAt')
    definition = raw.get('countDefinition')
    if not isinstance(definition, str) or not definition.strip():
        raise ValueError(f'{path}: countDefinition requires a non-empty method')
    hubs = raw.get('hubs')
    if not isinstance(hubs, list):
        raise ValueError(f'{path}: expected a "hubs" array')

    adapted = []
    for index, hub in enumerate(hubs):
        where = f'{path}: hubs[{index}]'
        if not isinstance(hub, dict):
            raise ValueError(f'{where} must be an object')
        hub_url = hub.get('url')
        manifest_tasks = hub.get('tasks')
        if not isinstance(manifest_tasks, list):
            raise ValueError(f'{where}.tasks must be an array')
        expected_tasks = {}
        for task_index, task in enumerate(manifest_tasks):
            twhere = f'{where}.tasks[{task_index}]'
            if not isinstance(task, dict):
                raise ValueError(f'{twhere} must be an object')
            slug = task.get('slug')
            importance = task.get('importance')
            if not isinstance(slug, str) or not slug.strip():
                raise ValueError(f'{twhere}.slug requires a non-empty string')
            slug = slug.strip()
            if slug in expected_tasks:
                raise ValueError(f'{twhere}.slug duplicates "{slug}"')
            if type(importance) is not int or not 1 <= importance <= 5:
                raise ValueError(f'{twhere}.importance must be an integer from 1 to 5')
            expected_tasks[slug] = importance
        declared_task_count = hub.get('taskCount')
        declared_importance = hub.get('taskImportanceTotal')
        if declared_task_count != len(expected_tasks):
            raise ValueError(f'{where}.taskCount disagrees with tasks')
        if declared_importance != sum(expected_tasks.values()):
            raise ValueError(f'{where}.taskImportanceTotal disagrees with tasks')
        records = hub.get('metaArticles')
        if not isinstance(records, list):
            raise ValueError(f'{where}.metaArticles must be an array')
        adapted_records = []
        counted_keys = set()
        for record_index, record in enumerate(records):
            rwhere = f'{where}.metaArticles[{record_index}]'
            if not isinstance(record, dict):
                raise ValueError(f'{rwhere} must be an object')
            # The reconciled manifest carries both the public post URL and the
            # explicit source/hub evidence fields. Require those evidence fields
            # instead of silently reconstructing them from array position.
            source_url = record.get('sourceUrl')
            record_url = record.get('url')
            record_hub_url = record.get('hubUrl')
            counted = record.get('counted')
            source_key = normalize_article_url(source_url)
            if normalize_article_url(record_url) != source_key:
                raise ValueError(f'{rwhere}.url disagrees with sourceUrl')
            if normalize_article_url(record_hub_url) != normalize_article_url(hub_url):
                raise ValueError(f'{rwhere}.hubUrl disagrees with its parent hub')
            primary_parent = record.get('primaryParentHub')
            if counted is True and normalize_article_url(primary_parent) != normalize_article_url(hub_url):
                raise ValueError(f'{rwhere}.primaryParentHub disagrees with its counted hub')
            if counted is True and source_key:
                counted_keys.add(source_key)
            if ('taskSlugs' in record and 'task_slugs' in record and
                    record['taskSlugs'] != record['task_slugs']):
                raise ValueError(f'{rwhere}: conflicting taskSlugs and task_slugs')
            adapted_records.append({
                'source_url': source_url,
                'hub_url': record_hub_url,
                'evidence_method': record.get('evidenceMethod'),
                'counted': counted,
                'reason': record.get('reason'),
                'title': record.get('title'),
                'post_id': record.get('postId'),
                'published_at': record.get('publishedAt'),
                'modified_at': record.get('modifiedAt'),
                'taxonomy_evidence': record.get('taxonomyEvidence'),
                'primary_parent_hub': primary_parent,
                **({'task_slugs': record.get('taskSlugs', record.get('task_slugs'))}
                   if 'taskSlugs' in record or 'task_slugs' in record else {}),
            })
        declared_count = hub.get('metaArticleCount')
        if type(declared_count) is not int or declared_count < 0:
            raise ValueError(f'{where}.metaArticleCount must be a non-negative integer')
        if declared_count != len(counted_keys):
            raise ValueError(f'{where}.metaArticleCount disagrees with unique counted sources')
        tier = meta_orbit_tier(declared_count)
        strength = hub.get('strength')
        if (not isinstance(strength, dict) or strength.get('score') != tier['level'] or
                strength.get('label') != tier['label']):
            raise ValueError(f'{where}.strength disagrees with derived count band')
        source = evidence_url or hub.get('taskLibrarySourceUrl') or hub_url
        adapted.append({
            'hub_url': hub_url,
            'meta_count_status': hub.get('metaCountStatus'),
            'audited': audited,
            'evidence_source_url': source,
            'evidence_method': definition.strip(),
            'records': adapted_records,
            '_expected_task_count': hub.get('taskCount'),
            '_expected_importance_total': hub.get('taskImportanceTotal'),
            '_expected_tasks': expected_tasks,
        })
    return {'hubs': adapted}


def load_article_meta_orbits(path=ARTICLE_META_ORBITS, evidence_url=None):
    """Load evidence-backed meta-article orbit audits.

    Missing hubs are UNKNOWN, never zero. A hub appears here only after a
    source-backed audit. ``verified`` means the recorded count is exhaustive as
    of the audit date; ``partial`` means the count is a proven lower bound.
    Every candidate record preserves why it did or did not count.
    """
    with open(path, encoding='utf-8') as fh:
        raw = json.load(fh)
    raw = adapt_strength_manifest(raw, path, evidence_url=evidence_url)
    hubs = raw.get('hubs') if isinstance(raw, dict) else None
    if not isinstance(hubs, list):
        raise ValueError(f'{path}: expected a "hubs" array')

    audited = {}
    for index, audit in enumerate(hubs):
        where = f'{path}: hubs[{index}]'
        if not isinstance(audit, dict):
            raise ValueError(f'{where} must be an object')
        required = {'hub_url', 'meta_count_status', 'audited',
                    'evidence_source_url', 'evidence_method', 'records'}
        missing = sorted(required - set(audit))
        if missing:
            raise ValueError(f'{where} missing required fields {missing}')
        hub_url = require_absolute_http_url(audit['hub_url'], f'{where}.hub_url')
        hub_key = normalize_article_url(hub_url)
        if hub_key in audited:
            raise ValueError(f'{where} duplicates normalized hub URL "{hub_url}"')
        status = audit['meta_count_status']
        if status not in META_COUNT_STATUSES:
            raise ValueError(f'{where}.meta_count_status must be verified or partial; '
                             'omit unaudited hubs so they remain unknown')
        audited_at = valid_review_date(audit['audited'], f'{where}.audited')
        evidence_source_url = require_absolute_http_url(
            audit['evidence_source_url'], f'{where}.evidence_source_url')
        evidence_method = audit['evidence_method']
        if not isinstance(evidence_method, str) or not evidence_method.strip():
            raise ValueError(f'{where}.evidence_method requires a non-empty method')
        records = audit['records']
        if not isinstance(records, list):
            raise ValueError(f'{where}.records must be an array')
        if status == 'partial' and not records:
            raise ValueError(f'{where}: a partial audit requires at least one source record')

        clean_records = []
        seen_in_hub = set()
        for record_index, record in enumerate(records):
            rwhere = f'{where}.records[{record_index}]'
            if not isinstance(record, dict):
                raise ValueError(f'{rwhere} must be an object')
            required_record = {'source_url', 'hub_url', 'evidence_method',
                               'counted', 'reason'}
            missing_record = sorted(required_record - set(record))
            if missing_record:
                raise ValueError(f'{rwhere} missing required fields {missing_record}')
            source_url = require_absolute_http_url(
                record['source_url'], f'{rwhere}.source_url')
            record_hub = require_absolute_http_url(
                record['hub_url'], f'{rwhere}.hub_url')
            if normalize_article_url(record_hub) != hub_key:
                raise ValueError(f'{rwhere}.hub_url does not match its normalized parent hub')
            record_method = record['evidence_method']
            reason = record['reason']
            if not isinstance(record_method, str) or not record_method.strip():
                raise ValueError(f'{rwhere}.evidence_method requires a non-empty method')
            if type(record['counted']) is not bool:
                raise ValueError(f'{rwhere}.counted must be true or false')
            if not isinstance(reason, str) or not reason.strip():
                raise ValueError(f'{rwhere}.reason requires a non-empty explanation')
            source_key = normalize_article_url(source_url)
            if source_key in seen_in_hub:
                raise ValueError(f'{rwhere} duplicates source URL "{source_url}" in this hub')
            seen_in_hub.add(source_key)
            if record['counted']:
                if source_key == hub_key:
                    raise ValueError(f'{rwhere}: a hub cannot count itself as its meta-article')
            task_slugs = record.get('task_slugs')
            if task_slugs is not None:
                if (not isinstance(task_slugs, list) or not task_slugs or
                        any(not isinstance(slug, str) or not slug.strip()
                            for slug in task_slugs)):
                    raise ValueError(f'{rwhere}.task_slugs must be a non-empty string array')
                task_slugs = [slug.strip() for slug in task_slugs]
                if len(set(task_slugs)) != len(task_slugs):
                    raise ValueError(f'{rwhere}.task_slugs contains duplicates')
            clean = {
                'sourceUrl': source_url,
                # Preserve the audited canonical URL on every decision record.
                # The submitted record URL may be an equivalent http/www/hash
                # variant, but downstream consumers should not have to infer
                # the normalized parent only from array position.
                'hubUrl': hub_url,
                'evidenceMethod': record_method.strip(),
                'counted': record['counted'],
                'reason': reason.strip(),
            }
            if task_slugs is not None:
                clean['taskSlugs'] = task_slugs
            optional_strings = {
                'title': 'title',
                'published_at': 'publishedAt',
                'modified_at': 'modifiedAt',
            }
            for source_field, output_field in optional_strings.items():
                value = record.get(source_field)
                if value is not None:
                    if not isinstance(value, str) or not value.strip():
                        raise ValueError(f'{rwhere}.{source_field} must be a non-empty string')
                    clean[output_field] = value.strip()
            post_id = record.get('post_id')
            if post_id is not None:
                if type(post_id) is not int or post_id <= 0:
                    raise ValueError(f'{rwhere}.post_id must be a positive integer')
                clean['postId'] = post_id
            taxonomy = record.get('taxonomy_evidence')
            if taxonomy is not None:
                if (not isinstance(taxonomy, list) or
                        any(not isinstance(item, str) or not item.strip()
                            for item in taxonomy)):
                    raise ValueError(f'{rwhere}.taxonomy_evidence must be a string array')
                clean['taxonomyEvidence'] = [item.strip() for item in taxonomy]
            primary_parent = record.get('primary_parent_hub')
            if primary_parent is not None:
                clean['primaryParentHub'] = require_absolute_http_url(
                    primary_parent, f'{rwhere}.primary_parent_hub')
                if (record['counted'] and
                        normalize_article_url(primary_parent) != hub_key):
                    raise ValueError(
                        f'{rwhere}.primary_parent_hub does not match its counted hub')
            clean_records.append(clean)

        audited[hub_key] = {
            'hubUrl': hub_url,
            'metaCountStatus': status,
            'audited': audited_at,
            'evidenceSourceUrl': evidence_source_url,
            'evidenceMethod': evidence_method.strip(),
            'records': clean_records,
        }
        if audit.get('_expected_task_count') is not None:
            audited[hub_key]['expectedTaskCount'] = audit['_expected_task_count']
        if audit.get('_expected_importance_total') is not None:
            audited[hub_key]['expectedImportanceTotal'] = audit['_expected_importance_total']
        if audit.get('_expected_tasks') is not None:
            audited[hub_key]['expectedTasks'] = audit['_expected_tasks']
    return audited


def validate_article_meta_orbits(tasks, audits):
    """Fail if an audit or task-level evidence misses the final mappings."""
    groups = {}
    for task in tasks:
        key = normalize_article_url(task.get('article'))
        if key:
            groups.setdefault(key, set()).add(task['slug'])
    unused = sorted(set(audits) - set(groups))
    if unused:
        raise ValueError('meta-orbit audit(s) do not match any final article URL: ' +
                         ', '.join(unused))
    for key, audit in audits.items():
        mapped_slugs = groups[key]
        if ('expectedTaskCount' in audit and
                audit['expectedTaskCount'] != len(mapped_slugs)):
            raise ValueError(
                f'meta-orbit audit task count disagrees with final mapping for {audit["hubUrl"]}')
        if 'expectedImportanceTotal' in audit:
            importance_total = sum(int(t.get('importance') or 0) for t in tasks
                                   if normalize_article_url(t.get('article')) == key)
            if audit['expectedImportanceTotal'] != importance_total:
                raise ValueError(
                    f'meta-orbit audit importance total disagrees with final mapping for '
                    f'{audit["hubUrl"]}')
        if 'expectedTasks' in audit:
            actual_tasks = {
                t['slug']: int(t.get('importance') or 0) for t in tasks
                if normalize_article_url(t.get('article')) == key
            }
            if audit['expectedTasks'] != actual_tasks:
                raise ValueError(
                    f'meta-orbit audit exact task mapping disagrees with final build for '
                    f'{audit["hubUrl"]}')
        for record in audit['records']:
            unknown = sorted(set(record.get('taskSlugs', ())) - mapped_slugs)
            if unknown:
                raise ValueError(
                    f'meta-orbit source {record["sourceUrl"]} names task(s) not mapped '
                    f'to {audit["hubUrl"]}: {", ".join(unknown)}')


def meta_orbit_tier(count):
    if count is None:
        return {'level': None, 'label': 'Unknown'}
    for level, (lower, upper, label) in enumerate(META_ORBIT_TIERS):
        if count >= lower and (upper is None or count <= upper):
            return {'level': level, 'label': label}
    raise AssertionError(f'no meta-orbit tier for count {count}')


def preferred_article_url(mapped):
    """Choose the most common exact mapped URL without inventing a redirect."""
    counts = Counter(t['article'] for t in mapped)
    return sorted(counts, key=lambda url: (-counts[url], url))[0]


def task_library_route(base_url, parameter, value):
    route = base_url.rstrip('/') + '/?' + urlencode({parameter: value})
    if parameter == 'task':
        route += '#task-' + value
    return route


def load_article_certifications(path=ARTICLE_CERTIFICATIONS):
    """Load reviewed URL-level holds that may only downgrade a hub to WIP."""
    with open(path, encoding='utf-8') as fh:
        raw = json.load(fh)
    articles = raw.get('articles') if isinstance(raw, dict) else None
    if not isinstance(articles, dict):
        raise ValueError(f'{path}: expected an "articles" object')

    holds = {}
    for url, review in articles.items():
        key = normalize_article_url(url)
        if not key:
            raise ValueError(f'{path}: invalid article URL "{url}"')
        if key in holds:
            raise ValueError(f'{path}: duplicate normalized article URL "{url}"')
        if not isinstance(review, dict) or review.get('state') != 'wip':
            raise ValueError(f'{path}: {url} must be a fail-closed "wip" hold')
        reason = review.get('reason')
        reviewed = review.get('reviewed')
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f'{path}: {url} requires a reason')
        reason = reason.strip()
        if not isinstance(reviewed, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', reviewed):
            raise ValueError(f'{path}: {url} requires a YYYY-MM-DD review date')
        try:
            datetime.strptime(reviewed, '%Y-%m-%d')
        except ValueError as exc:
            raise ValueError(f'{path}: {url} has an invalid review date "{reviewed}"') from exc
        holds[key] = {'state': 'wip', 'reason': reason, 'reviewed': reviewed}
    return holds


def validate_article_certifications(tasks, certifications):
    """Fail if a reviewed hold misses the final post-override article mapping."""
    mapped = {normalize_article_url(t.get('article')) for t in tasks}
    mapped.discard(None)
    unused = sorted(set(certifications) - mapped)
    if unused:
        raise ValueError('semantic-certification hold(s) do not match any final article URL: ' +
                         ', '.join(unused))


def derive_article_states(tasks, certifications=None):
    """Label hubs from task status plus reviewed semantic-certification holds.

    A hub is ready/definitive only when every task mapped to its normalized
    URL is complete and no URL-level hold is active. Holds only downgrade a
    hub; they never falsify an individual task's completion status. Tasks
    without a valid article mapping are excluded.
    """
    if certifications is None:
        certifications = load_article_certifications()
    groups = {}
    for task in tasks:
        task.pop('articleState', None)
        task.pop('articleStateReason', None)
        task.pop('articleStateReviewed', None)
        key = normalize_article_url(task.get('article'))
        if key:
            groups.setdefault(key, []).append(task)

    ready = 0
    for key, mapped in groups.items():
        state = 'ready' if all(t.get('status') == 'complete' for t in mapped) else 'wip'
        review = certifications.get(key)
        if review:
            state = 'wip'
        ready += state == 'ready'
        for task in mapped:
            task['articleState'] = state
            if review:
                task['articleStateReason'] = review['reason']
                task['articleStateReviewed'] = review['reviewed']

    return {'articleHubs': len(groups), 'definitiveArticles': ready}


def derive_article_hub_inventory(tasks, meta_audits=None, task_library_url=None):
    """Build the bidirectional hub index and attach orbit facts to each task.

    This runs after ``derive_article_states``. Article readiness and meta-orbit
    strength stay separate: a semantic hold still wins, while a high example
    count never promotes a WIP hub. An absent meta audit remains UNKNOWN.
    """
    if meta_audits is None:
        meta_audits = load_article_meta_orbits()
    groups = {}
    for task in tasks:
        task.pop('taskLibraryUrl', None)
        key = normalize_article_url(task.get('article'))
        if key:
            groups.setdefault(key, []).append(task)

    hubs = []
    unique_counted = set()
    evidenced_hubs = 0
    for key in sorted(groups):
        mapped = groups[key]
        kinds = {t.get('articleKind', 'unknown') for t in mapped} - {'unknown'}
        if len(kinds) > 1:
            raise ValueError(f'conflicting article roles for {key}')
        article_kind = next(iter(kinds), 'unknown')
        for task in mapped:
            task['articleKind'] = article_kind
        if task_library_url:
            for task in mapped:
                task['taskLibraryUrl'] = task_library_route(
                    task_library_url, 'task', task['slug'])
        canonical_url = preferred_article_url(mapped)
        state = mapped[0].get('articleState') or 'wip'
        if {t.get('articleState') for t in mapped} != {state}:
            raise ValueError(f'article state drift inside normalized hub {key}')
        audit = meta_audits.get(key)
        meta_count = None
        meta_status = 'unknown'
        meta_articles = []
        audited_at = None
        priority_coverage = None
        task_meta_counts = None
        tasks_with_meta = None
        task_coverage = None
        if audit:
            evidenced_hubs += 1
            meta_status = audit['metaCountStatus']
            audited_at = audit['audited']
            meta_articles = sorted({
                record['sourceUrl'] for record in audit['records'] if record['counted']
            })
            meta_count = len(meta_articles)
            unique_counted.update(normalize_article_url(url) for url in meta_articles)
            positive_records = [r for r in audit['records'] if r['counted']]
            if not positive_records:
                priority_coverage = 0.0
                task_meta_counts = {t['slug']: 0 for t in mapped}
            elif len(mapped) == 1:
                task_meta_counts = {mapped[0]['slug']: meta_count}
            elif all(r.get('taskSlugs') for r in positive_records):
                task_meta_counts = {t['slug']: 0 for t in mapped}
                for record in positive_records:
                    for slug in record['taskSlugs']:
                        task_meta_counts[slug] += 1
            if task_meta_counts is not None:
                covered = {slug for slug, count in task_meta_counts.items() if count > 0}
                weight_by_slug = {t['slug']: int(t.get('importance') or 0) for t in mapped}
                denominator = sum(weight_by_slug.values())
                priority_coverage = (sum(weight_by_slug[slug] for slug in covered) /
                                     denominator) if denominator else 0.0
                tasks_with_meta = len(covered)
                task_coverage = (tasks_with_meta / len(mapped)) if mapped else 0.0
        tier = meta_orbit_tier(meta_count)
        library_route = (task_library_route(task_library_url, 'article', canonical_url)
                         if task_library_url else None)
        reason = next((t.get('articleStateReason') for t in mapped
                       if t.get('articleStateReason')), None)
        reviewed = next((t.get('articleStateReviewed') for t in mapped
                         if t.get('articleStateReviewed')), None)
        hub = {
            'key': key,
            'url': canonical_url,
            'state': state,
            'articleKind': article_kind,
            'taskCount': len(mapped),
            'completeTaskCount': sum(t.get('status') == 'complete' for t in mapped),
            'importance': max(int(t.get('importance') or 0) for t in mapped),
            'importanceTotal': sum(int(t.get('importance') or 0) for t in mapped),
            'taskSlugs': sorted(t['slug'] for t in mapped),
            'metaArticleCount': meta_count,
            'metaCountStatus': meta_status,
            'metaOrbitStrength': tier['level'],
            'metaOrbitTier': tier['label'],
            'metaArticles': meta_articles,
            'taskMetaCounts': task_meta_counts,
            'tasksWithMeta': tasks_with_meta,
            'taskCoverage': task_coverage,
            'priorityCoverage': priority_coverage,
        }
        if library_route:
            hub['taskLibraryUrl'] = library_route
        if reason:
            hub['stateReason'] = reason
        if reviewed:
            hub['stateReviewed'] = reviewed
        if audit:
            hub['metaOrbitAudited'] = audited_at
            hub['metaOrbitEvidenceUrl'] = audit['evidenceSourceUrl']
            hub['metaOrbitEvidenceMethod'] = audit['evidenceMethod']
        hubs.append(hub)

    stats = {
        'verifiedMetaArticles': len(unique_counted),
        'metaOrbitHubsWithEvidence': evidenced_hubs,
        'metaOrbitHubsUnknown': len(groups) - evidenced_hubs,
    }
    return hubs, stats


def html_escape(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def write_library_index(data, out_path):
    """Crawlable HTML fragment for the WordPress page (paste below the iframe).

    Plain semantic markup, no scripts/styles: categories as H2s, each task
    linking to its definitive article on blitzmetrics.com. This is the
    indexable representation of the library; the iframe stays the interactive one.
    """
    L = []
    st = data['stats']
    L.append('<!-- Task Library static index — generated by build.py; do not edit by hand -->')
    L.append('<section id="task-library-index">')
    L.append(f"<p>The BlitzMetrics Task Library documents <strong>{st['total']} operational tasks</strong> "
             f"across {st['categories']} categories. Its task-to-article mappings resolve to "
             f"<strong>{st['articleHubs']} article hubs</strong>: "
             f"<strong>{st['definitiveArticles']} catalog-ready</strong> because their mapped tasks are complete "
             f"and no reviewed semantic hold is active, "
             f"and {st['articleHubs'] - st['definitiveArticles']} still in progress. "
             f"A Definitive marker also requires semantic review of the actual page. "
             f"Contributors report {st['complete']} complete guides, {st['needsWork']} in progress, and {st['gaps']} identified gaps. "
             f"These labels do not prove independent review, installed skills or completed client work. "
             f"Updated {html_escape(data['updated'])}.</p>")
    for c in data['categories']:
        L.append(f"<h2>{html_escape(c['name'])}</h2>")
        L.append(f"<p>{html_escape(c['description'])}</p>")
        L.append('<ul>')
        for t in c['tasks']:
            label = html_escape(t['title'])
            desc = html_escape(t['desc'])
            if t.get('article'):
                task_route = html_escape(t.get('taskLibraryUrl') or '')
                reverse = (f' <a href="{task_route}">View exact Task Library entry</a>.'
                           if task_route else '')
                L.append(f'<li><a href="{html_escape(t["article"])}">{label}</a> — '
                         f'{desc}.{reverse}</li>')
            else:
                L.append(f'<li>{label} — {desc}</li>')
        L.append('</ul>')
    L.append('</section>')
    open(out_path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


def write_meta_orbit_index(data, audits, out_path):
    """Write the public, build-reconciled orbit evidence artifact.

    The input inventory can carry a stale snapshot of Task Library stats. This
    projection always takes hub/task counts and tiers from the same current
    build as ``data.json`` while preserving each source decision and method.
    """
    hubs = []
    for hub in data['articleHubs']:
        audit = audits.get(hub['key'])
        records = []
        if audit:
            for record in audit['records']:
                public = {
                    'sourceUrl': record['sourceUrl'],
                    'hubUrl': record['hubUrl'],
                    'evidenceMethod': record['evidenceMethod'],
                    'counted': record['counted'],
                    'reason': record['reason'],
                }
                if record.get('taskSlugs'):
                    public['taskSlugs'] = record['taskSlugs']
                for field in ('title', 'postId', 'publishedAt', 'modifiedAt',
                              'taxonomyEvidence', 'primaryParentHub'):
                    if field in record:
                        public[field] = record[field]
                records.append(public)
        public_hub = dict(hub)
        public_hub['records'] = records
        hubs.append(public_hub)
    payload = {
        'schemaVersion': 1,
        'generatedAt': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'countDefinition': ('Verified meta-article sources explicitly classified by the '
                            'recorded evidence method and linked to the normalized canonical '
                            'hub. Unknown is never coerced to zero.'),
        'strengthBands': [
            {'level': level, 'label': label,
             'minimum': lower, 'maximum': upper}
            for level, (lower, upper, label) in enumerate(META_ORBIT_TIERS)
        ],
        'stats': {
            'articleHubs': data['stats']['articleHubs'],
            'definitiveArticles': data['stats']['definitiveArticles'],
            'verifiedMetaArticles': data['stats']['verifiedMetaArticles'],
            'metaOrbitHubsWithEvidence': data['stats']['metaOrbitHubsWithEvidence'],
            'metaOrbitHubsUnknown': data['stats']['metaOrbitHubsUnknown'],
        },
        'hubs': hubs,
    }
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)


def source_from_repo_url(url, slug):
    """Turn a pasted GitHub URL into a github:owner/repo@ref:path source.

    Accepts:
      github:owner/repo@ref:path            (already a source ref — used as-is)
      https://github.com/owner/repo         -> @main:skills/<slug>/SKILL.md
      https://github.com/owner/repo/tree/<ref>/<folder>  -> <folder>/SKILL.md
      https://github.com/owner/repo/blob/<ref>/<file.md> -> that file
    """
    url = url.strip().rstrip('/')
    if url.startswith('github:'):
        return url
    m = re.match(r'https?://github\.com/([^/]+)/([^/]+)(?:/(tree|blob)/([^/]+)/(.+))?$', url)
    if not m:
        return None
    owner, repo, kind, ref, path = m.groups()
    if not kind:
        return f'github:{owner}/{repo}@main:skills/{slug}/SKILL.md'
    if kind == 'blob':
        return f'github:{owner}/{repo}@{ref}:{path}'
    return f'github:{owner}/{repo}@{ref}:{path}/SKILL.md'


def download_from_source(source):
    m = re.match(r'github:([^/]+)/([^@]+)@([^:]+):', source or '')
    if not m:
        return None
    owner, repo, ref = m.groups()
    return f'https://github.com/{owner}/{repo}/archive/refs/heads/{ref}.zip' if not re.fullmatch(r'[0-9a-f]{7,40}', ref) \
        else f'https://github.com/{owner}/{repo}/archive/{ref}.zip'


def write_zip(data, out_dir, fname, note, only_complete):
    import zipfile
    ready = [(c, t) for c in data['categories'] for t in c['tasks']
             if (t.get('content') or '').strip() and (t['status'] == 'complete' or not only_complete)]
    path = os.path.join(out_dir, fname)
    with open(os.path.join(BUILD, 'pack-start-here.md'), encoding='utf-8') as source:
        start_here = source.read()
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('TaskLibrary-Skills/START-HERE.md', start_here)
        z.writestr('TaskLibrary-Skills/README.md',
                   '# Use one guide for one business job\n\n'
                   'Choose a job, share its guide and your files, then check one result. '
                   'Open START-HERE.md for the first steps and a prompt to copy.\n\n'
                   f'Library snapshot: {data.get("updated", "not recorded")}. '
                   f'This archive holds {len(ready)} guides. '
                   'See manifest.json for their paths and contributor status claims. '
                   'The archive is separate from the curated plugin and does not install or schedule itself.\n')
        manifest = {'total': len(ready), 'note': note, 'tasks': []}
        for c, t in ready:
            cf = folder_of(c['name'])
            z.writestr(f'TaskLibrary-Skills/skills/{cf}/{t["slug"]}.md', t['content'])
            manifest['tasks'].append({'slug': t['slug'], 'category': c['name'], 'status': t['status'],
                                      'owner': t.get('owner', ''), 'path': f'skills/{cf}/{t["slug"]}.md'})
        z.writestr('TaskLibrary-Skills/manifest.json', json.dumps(manifest, ensure_ascii=False, indent=1))
    return len(ready)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tracker-csv')
    ap.add_argument('--out', default=os.path.join(ROOT, 'dashboard', 'data.json'))
    args = ap.parse_args()

    registry = json.load(open(os.path.join(BUILD, 'registry.json'), encoding='utf-8'))['skills']
    with open(os.path.join(BUILD, 'instruction-reviews.json'), encoding='utf-8') as fh:
        instruction_reviews = json.load(fh)['reviews']
    cats_meta = json.load(open(os.path.join(BUILD, 'categories.json'), encoding='utf-8'))
    site = json.load(open(os.path.join(BUILD, 'site-meta.json'), encoding='utf-8'))

    overrides = {}
    if args.tracker_csv:
        for row in csv.DictReader(open(args.tracker_csv, encoding='utf-8-sig')):
            overrides[row['Slug'].strip()] = row
        # A tracker was explicitly requested, so zero rows means the fetch broke
        # upstream - not that there is nothing to apply. Fail loudly instead of
        # publishing a silently shrunken library.
        # (2026-08-05: a hung publish-to-web fetch returned 0 bytes, the GitHub
        #  build reported SUCCESS, and the live dashboard lost 13 skills and every
        #  owner. Nothing failed anywhere. This guard is that incident.)
        if not overrides:
            sys.exit(f"ERROR: --tracker-csv {args.tracker_csv} parsed 0 data rows. "
                     f"The Asset Tracker fetch failed upstream. Refusing to build "
                     f"without it rather than shipping a shrunken library.")

    # Sheet-first onboarding: a tracker row with a Source Repo link whose slug
    # is not in the registry becomes a new external skill (format claude-skill).
    valid_cats = {c['name'] for c in cats_meta}
    errors, warnings = [], []
    sheet_only = {}   # rows with no source anywhere: rendered as named gap cards
    for slug, row in list(overrides.items()):
        src_cell = (row.get('Source Repo') or '').strip()
        if slug in registry and src_cell:
            # SHEET WINS: a repo link on an existing row re-points the skill
            # to the owner's repo; the hub copy is ignored from now on.
            src = source_from_repo_url(src_cell, slug)
            if src and src != registry[slug].get('source'):
                registry[slug] = dict(registry[slug], source=src, format='claude-skill',
                                      flag='claimed via sheet — hub copy superseded')
                dl = (row.get('Download URL') or '').strip() or download_from_source(src)
                if dl:
                    registry[slug]['download'] = dl
            continue
        if slug in registry:
            continue
        if not src_cell:
            cat = (row.get('Category') or '').strip()
            if cat in valid_cats and slug:
                rec = factory.annotate(slug, cat, (row.get('Stage') or '').strip())
                sheet_only[slug] = {
                    'title': (row.get('Task Title') or slug).strip() or slug,
                    'slug': slug, 'status': 'gap',
                    'stage': (row.get('Stage') or '—').strip() or '—',
                    'article': (row.get('Definitive Article URL') or '').strip() or None,
                    'desc': (row.get('Description') or '').strip(),
                    'content': '',
                    'flag': 'defined in sheet — not yet built',
                    'category': cat,
                    'importance': rec['importance'], 'freq': rec['freq'],
                    'revenue': rec['revenue'], 'gating': rec['gating'],
                    'phase': rec['phase'], 'before': rec['before'],
                    'after': rec['after'], 'lane': rec['lane'],
                    'lane_label': rec['lane_label'], 'why': rec['why']}
                if (row.get('Owner') or '').strip():
                    sheet_only[slug]['owner'] = row['Owner'].strip()
            continue
        src = source_from_repo_url(row['Source Repo'], slug)
        if not src:
            errors.append(f'{slug}: sheet Source Repo not a recognizable GitHub URL: {row["Source Repo"]}')
            continue
        cat = (row.get('Category') or '').strip()
        if cat not in valid_cats:
            errors.append(f'{slug}: sheet Category "{cat}" is not one of the {len(valid_cats)} library categories')
            continue
        entry = {'source': src, 'format': 'claude-skill', 'category': cat,
                 'stage': (row.get('Stage') or '—').strip() or '—',
                 'status': {'ready': 'complete', 'complete': 'complete', 'wip': 'needs-work', 'needs-work': 'needs-work', 'gap': 'gap'}.get(
                     (row.get('Status') or '').strip().lower(), 'needs-work'),
                 'flag': 'added via Asset Tracker sheet'}
        dl = (row.get('Download URL') or '').strip() or download_from_source(src)
        if dl:
            entry['download'] = dl
        registry[slug] = entry
    by_cat = {c['name'] for c in cats_meta} and {c['name']: [] for c in cats_meta}
    for slug, entry in registry.items():
        if entry.get('article_kind', 'unknown') not in ARTICLE_KINDS:
            errors.append(f'{slug}: unknown article_kind')
            continue
        text = resolve(slug, entry, errors, warnings)
        if text is None:
            continue
        fm = validate(slug, entry, text, errors, warnings)
        if fm is None:
            continue
        status, art = fm['status'], article_url(fm['definitive_article'])
        ov = overrides.get(slug)
        if ov:
            s = (ov.get('Status') or '').strip().lower()
            status = {'ready': 'complete', 'complete': 'complete', 'wip': 'needs-work', 'needs-work': 'needs-work', 'gap': 'gap'}.get(s, status)
            if (ov.get('Definitive Article URL') or '').strip():
                art = ov['Definitive Article URL'].strip()   # sheet overrides only when filled; file frontmatter is the default
        rec = factory.annotate(slug, entry['category'], fm.get('stage') or '', text)
        content = factory.apply_layer(text.strip(), factory.layer_markdown(slug, rec))
        task = {'title': display_title(text, slug), 'slug': slug, 'status': status,
                'stage': fm['stage'] or '—', 'article': art,
                'articleKind': (entry.get('article_kind', 'unknown') if
                                normalize_article_url(art) == normalize_article_url(article_url(fm['definitive_article']))
                                else 'unknown'),
                'desc': fm['description'], 'content': content,
                'importance': rec['importance'], 'freq': rec['freq'],
                'revenue': rec['revenue'], 'gating': rec['gating'],
                'phase': rec['phase'], 'before': rec['before'],
                'after': rec['after'], 'lane': rec['lane'],
                'lane_label': rec['lane_label'], 'why': rec['why']}
        review = current_instruction_review(slug, text, instruction_reviews)
        if review:
            task['instructionReview'] = review
        if entry.get('flag'):
            task['flag'] = entry['flag']
        if entry.get('download'):
            task['download'] = entry['download']
        if ov and (ov.get('Owner') or '').strip():
            task['owner'] = ov['Owner'].strip()
        if entry['category'] not in by_cat:
            errors.append(f'{slug}: unknown category "{entry["category"]}"')
            continue
        by_cat[entry['category']].append(task)

    # governance: ready/wip means someone owns it; unclaimed skills are gaps
    for slug, row in overrides.items():
        st_ = (row.get('Status') or '').strip().lower()
        if st_ in ('ready', 'wip') and not (row.get('Owner') or '').strip():
            warnings.append(f'{slug}: sheet says "{st_}" but Owner is blank — unclaimed skills should be "gap"')
    # one file, one skill: flag rows resolving to the same source file
    seen_src = {}
    for slug, entry in registry.items():
        src = entry.get('source')
        if src and src != 'local':
            if src in seen_src:
                warnings.append(f'{slug}: same source file as "{seen_src[src]}" ({src}) — two rows, one file')
            seen_src[src] = slug
    for slug, t in sheet_only.items():
        cat = t.pop('category')
        by_cat[cat].append(t)
    all_tasks = [t for ts in by_cat.values() for t in ts]
    certifications = load_article_certifications()
    validate_article_certifications(all_tasks, certifications)
    article_stats = derive_article_states(all_tasks, certifications)
    meta_audits = load_article_meta_orbits(evidence_url=site['metaOrbitUrl'])
    validate_article_meta_orbits(all_tasks, meta_audits)
    article_hubs, meta_stats = derive_article_hub_inventory(
        all_tasks, meta_audits, site['taskLibraryUrl'])
    execution_records = executions.load(os.path.join(BUILD, 'task-executions.json'),
                                        {t['slug'] for t in all_tasks})
    execution_history = executions.attach(all_tasks, execution_records)
    # Owner attribution comes ONLY from the Asset Tracker. A tracker that parsed
    # rows but still yields zero owners is a malformed or partial feed - the same
    # failure class as above, caught one stage later.
    if args.tracker_csv and not {t['owner'] for t in all_tasks if t.get('owner')}:
        sys.exit("ERROR: a tracker CSV was supplied but the build produced 0 owners. "
                 "The Asset Tracker feed is empty or malformed. Refusing to publish.")
    data = {'stats': {'total': len(all_tasks),
                      'complete': sum(t['status'] == 'complete' for t in all_tasks),
                      'reviewedInstructions': sum(bool(t.get('instructionReview')) for t in all_tasks),
                      'needsWork': sum(t['status'] == 'needs-work' for t in all_tasks),
                      'gaps': sum(t['status'] == 'gap' for t in all_tasks),
                      **article_stats,
                      **meta_stats,
                      'owners': len({t['owner'] for t in all_tasks if t.get('owner')}),
                      'categories': len(cats_meta)},
            'bundleUrl': 'TaskLibrary-Skills-all.zip', 'metaArticleUrl': site['metaArticleUrl'],
            'taskLibraryUrl': site['taskLibraryUrl'],
            'metaOrbitUrl': site['metaOrbitUrl'],
            'updated': datetime.now(timezone.utc).strftime('%B %-d, %Y'),  # real build stamp (was a static label from site-meta.json)
            'factory': factory.factory_meta(),
            'articleHubs': article_hubs,
            'executionHistory': execution_history,
            'categories': [dict(c, tasks=by_cat[c['name']]) for c in cats_meta]}
    # Drop dangling before/after pointers that are not in this build.
    known = {t['slug'] for t in all_tasks}
    for t in all_tasks:
        if t.get('before') and t['before'] not in known:
            t['before'] = None
        if t.get('after') and t['after'] not in known:
            t['after'] = None
    dist = {str(i): sum(t.get('importance') == i for t in all_tasks) for i in range(1, 6)}
    data['stats']['importance'] = dist
    data['stats']['fives'] = dist.get('5', 0)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump(data, open(args.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(os.path.dirname(args.out), 'executions.json'), 'w', encoding='utf-8') as fh:
        json.dump(execution_history, fh, ensure_ascii=False, indent=2)
    write_meta_orbit_index(
        data, meta_audits,
        os.path.join(os.path.dirname(args.out), 'meta-orbits.json'))
    write_library_index(data, os.path.join(os.path.dirname(args.out), 'library-index.html'))
    nall = write_zip(data, os.path.dirname(args.out), 'TaskLibrary-Skills-all.zip',
                     'All registered guide files. Dated snapshot; includes contributor-reported complete, needs-work and gap entries.', False)
    nready = write_zip(data, os.path.dirname(args.out), 'TaskLibrary-Skills-ready.zip',
                       'Guides with contributor-reported complete status. Owner sign-off, independent review and actual execution are not established by this label.', True)
    print(f'zips: all={nall}, ready={nready}')
    inv = os.path.join(ROOT, "INCOMPLETE-INVENTORY.md")
    ninc = factory.write_incomplete_inventory(all_tasks, inv)
    print(f"incomplete inventory: {ninc} rows -> {os.path.relpath(inv, ROOT)}")

    print(f"built {len(all_tasks)}/{len(registry) + len(sheet_only)} skills -> {os.path.relpath(args.out, ROOT)}")
    print(f"stats: {data['stats']}")
    for w in warnings:
        print('WARN ', w)
    for e in errors:
        print('ERROR', e)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
