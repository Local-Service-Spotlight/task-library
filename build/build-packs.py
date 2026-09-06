#!/usr/bin/env python3
"""
build-packs.py — emit one downloadable .zip per skill pack.

Runs AFTER build.py, reading the composed dashboard/data.json (which already
carries every skill's content) plus build/packs.json (the pack definitions).
Writes dashboard/packs/<id>.zip and dashboard/packs/index.json.

Because the workflow uploads the whole dashboard/ folder as the Pages artifact,
these zips deploy automatically to:
    https://<pages-host>/packs/<id>.zip
So a landing page can link straight to a pack's zip — no navigation, one click.

A pack in packs.json:
  { "id","name","kind","emoji","blurb",
    "slugs":[...],            # explicit Task Library slugs (optional)
    "category":"<folder>" }   # expands to every skill in that category (optional)
Provide slugs, category, or both. A slug not in the library is skipped and logged.
"""
import json, os, zipfile, sys

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
DASH  = os.path.join(ROOT, 'dashboard')


def load_skills(data):
    """slug -> {content,status,title,catName,folder}."""
    by = {}
    order = []
    for c in data.get('categories', []):
        for t in c.get('tasks', []):
            by[t['slug']] = {
                'content': t.get('content') or '',
                'status': t.get('status', ''),
                'title': t.get('title', t['slug']),
                'catName': c.get('name', ''),
                'folder': c.get('folder', ''),
            }
            order.append((c.get('folder', ''), t['slug']))
    return by, order


def resolve_slugs(pack, by, order):
    """Explicit slugs first (in listed order), then category expansion, de-duped."""
    out, seen = [], set()
    for s in pack.get('slugs', []):
        if s not in seen:
            out.append(s); seen.add(s)
    cat = pack.get('category')
    if cat:
        for folder, slug in order:
            if folder == cat and slug not in seen:
                out.append(slug); seen.add(slug)
    return out


def write_pack_zip(pack, slugs, by, out_dir, updated):
    present = [s for s in slugs if by.get(s) and by[s]['content'].strip()]
    missing = [s for s in slugs if s not in by]
    empty   = [s for s in slugs if s in by and not by[s]['content'].strip()]
    pid = pack['id']
    path = os.path.join(out_dir, pid + '.zip')

    manifest = {
        'pack': pid, 'name': pack.get('name', pid), 'kind': pack.get('kind', ''),
        'library_updated': updated, 'skill_count': len(present),
        'generated_by': 'build-packs.py',
        'skills': present,
        'missing_from_library': missing,   # registered later -> appears next build
    }
    readme = (
        f"# {pack.get('name', pid)}\n\n{pack.get('blurb','')}\n\n"
        f"{len(present)} skills from the Local Service Spotlight Task Library "
        f"(library updated {updated}).\n\n"
        "This download is a dated snapshot. Open START-HERE.md for one useful first job. "
        "A status is a contributor claim, not proof of installation or completed client work.\n\n## Skills\n\n"
        + "\n".join(f"- **{by[s]['title']}** (`{s}`) — {by[s]['status']}" for s in present)
        + "\n"
    )
    with open(os.path.join(BUILD, 'pack-start-here.md'), encoding='utf-8') as source:
        start_here = source.read()
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{pid}/START-HERE.md", start_here)
        z.writestr(f"{pid}/README.md", readme)
        z.writestr(f"{pid}/MANIFEST.json", json.dumps(manifest, ensure_ascii=False, indent=1))
        for s in present:
            z.writestr(f"{pid}/skills/{s}/skill.md", by[s]['content'])
    return {'id': pid, 'name': pack.get('name', pid), 'kind': pack.get('kind', ''),
            'emoji': pack.get('emoji', ''), 'blurb': pack.get('blurb', ''),
            'file': f"packs/{pid}.zip", 'skill_count': len(present),
            'missing': missing, 'empty': empty,
            'bytes': os.path.getsize(path)}


def main():
    data = json.load(open(os.path.join(DASH, 'data.json'), encoding='utf-8'))
    packs = json.load(open(os.path.join(BUILD, 'packs.json'), encoding='utf-8'))['packs']
    updated = data.get('updated', '')
    by, order = load_skills(data)

    out_dir = os.path.join(DASH, 'packs')
    os.makedirs(out_dir, exist_ok=True)

    index = {'updated': updated, 'packs': []}
    for pack in packs:
        slugs = resolve_slugs(pack, by, order)
        info = write_pack_zip(pack, slugs, by, out_dir, updated)
        index['packs'].append({k: info[k] for k in
                               ('id', 'name', 'kind', 'emoji', 'blurb', 'file', 'skill_count')})
        note = ''
        if info['missing']:
            note += f"  [skipped {len(info['missing'])} not in library: {', '.join(info['missing'])}]"
        if info['empty']:
            note += f"  [skipped {len(info['empty'])} empty]"
        print(f"  {info['id']:22s} {info['skill_count']:3d} skills  {info['bytes']//1024:4d} KB{note}")

    json.dump(index, open(os.path.join(out_dir, 'index.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f"packs: {len(index['packs'])} zips -> dashboard/packs/  (+ index.json)")


if __name__ == '__main__':
    sys.exit(main())
