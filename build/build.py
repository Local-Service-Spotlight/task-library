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
import argparse, csv, json, os, re, sys, urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
CACHE = os.path.join(BUILD, '.cache')

STAGES = {'Produce', 'Process', 'Post', 'Promote', '—', ''}
STATUSES = {'complete', 'needs-work', 'gap'}
REQUIRED_FM = ['name', 'description', 'category', 'stage', 'definitive_article', 'status']
REQUIRED_SECTIONS = ['## Inputs', '## Steps', '## Definition of done (QA checklist)',
                     '## Example(s)', '## Definitive article & links']
STUB = re.compile(r'(placeholder|TBD|to be (written|documented|filled)|coming soon|lorem ipsum)', re.I)


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
             f"across {st['categories']} categories — each one a runnable SOP tied to a definitive article. "
             f"{st['complete']} are ready, {st['needsWork']} in progress, {st['gaps']} identified gaps. "
             f"Updated {html_escape(data['updated'])}.</p>")
    for c in data['categories']:
        L.append(f"<h2>{html_escape(c['name'])}</h2>")
        L.append(f"<p>{html_escape(c['description'])}</p>")
        L.append('<ul>')
        for t in c['tasks']:
            label = html_escape(t['title'].replace('-', ' ').capitalize())
            desc = html_escape(t['desc'])
            if t.get('article'):
                L.append(f'<li><a href="{html_escape(t["article"])}">{label}</a> — {desc}</li>')
            else:
                L.append(f'<li>{label} — {desc}</li>')
        L.append('</ul>')
    L.append('</section>')
    open(out_path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


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
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
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
                sheet_only[slug] = {
                    'title': (row.get('Task Title') or slug).strip() or slug,
                    'slug': slug, 'status': 'gap',
                    'stage': (row.get('Stage') or '—').strip() or '—',
                    'article': (row.get('Definitive Article URL') or '').strip() or None,
                    'desc': (row.get('Description') or '').strip(),
                    'content': '',
                    'flag': 'defined in sheet — not yet built',
                    'category': cat}
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
        task = {'title': fm['name'], 'slug': slug, 'status': status,
                'stage': fm['stage'] or '—', 'article': art,
                'desc': fm['description'], 'content': text.strip()}
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
    # Owner attribution comes ONLY from the Asset Tracker. A tracker that parsed
    # rows but still yields zero owners is a malformed or partial feed - the same
    # failure class as above, caught one stage later.
    if args.tracker_csv and not {t['owner'] for t in all_tasks if t.get('owner')}:
        sys.exit("ERROR: a tracker CSV was supplied but the build produced 0 owners. "
                 "The Asset Tracker feed is empty or malformed. Refusing to publish.")
    data = {'stats': {'total': len(all_tasks),
                      'complete': sum(t['status'] == 'complete' for t in all_tasks),
                      'needsWork': sum(t['status'] == 'needs-work' for t in all_tasks),
                      'gaps': sum(t['status'] == 'gap' for t in all_tasks),
                      'definitiveArticles': len({t['article'] for t in all_tasks if t.get('article')}),
                      'owners': len({t['owner'] for t in all_tasks if t.get('owner')}),
                      'categories': len(cats_meta)},
            'bundleUrl': 'TaskLibrary-Skills-all.zip', 'metaArticleUrl': site['metaArticleUrl'],
            'updated': datetime.now(timezone.utc).strftime('%B %-d, %Y'),  # real build stamp (was a static label from site-meta.json)
            'categories': [dict(c, tasks=by_cat[c['name']]) for c in cats_meta]}

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump(data, open(args.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    write_library_index(data, os.path.join(os.path.dirname(args.out), 'library-index.html'))
    nall = write_zip(data, os.path.dirname(args.out), 'TaskLibrary-Skills-all.zip',
                     'The complete Task Library. Rebuilt on every library build.', False)
    nready = write_zip(data, os.path.dirname(args.out), 'TaskLibrary-Skills-ready.zip',
                       'Owner-signed skills only. Rebuilt on every library build.', True)
    print(f'zips: all={nall}, ready={nready}')

    print(f"built {len(all_tasks)}/{len(registry) + len(sheet_only)} skills -> {os.path.relpath(args.out, ROOT)}")
    print(f"stats: {data['stats']}")
    for w in warnings:
        print('WARN ', w)
    for e in errors:
        print('ERROR', e)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
