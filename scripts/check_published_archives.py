#!/usr/bin/env python3
"""Validate every archive advertised by a Task Library dashboard release."""

import argparse
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import sys
import time
from urllib.parse import urljoin
from urllib.request import Request, urlopen
import zipfile


def safe_member(name):
    path = PurePosixPath(name)
    return not path.is_absolute() and '..' not in path.parts


def archive(raw, label):
    try:
        result = zipfile.ZipFile(BytesIO(raw))
    except zipfile.BadZipFile as exc:
        raise ValueError(f'{label}: invalid ZIP') from exc
    bad = result.testzip()
    if bad:
        raise ValueError(f'{label}: corrupt member {bad}')
    unsafe = [name for name in result.namelist() if not safe_member(name)]
    if unsafe:
        raise ValueError(f'{label}: unsafe member path {unsafe[0]}')
    return result


def require_member(zipped, name, label):
    try:
        return zipped.read(name)
    except KeyError as exc:
        raise ValueError(f'{label}: missing {name}') from exc


def validate(read_bytes):
    data = json.loads(read_bytes('data.json'))
    tasks = {
        task['slug']: task
        for category in data['categories']
        for task in category['tasks']
    }
    checks = []

    library_targets = (
        (data['bundleUrl'], set(tasks)),
        ('TaskLibrary-Skills-ready.zip', {
            slug for slug, task in tasks.items() if task['status'] == 'complete'
        }),
    )
    for relative, expected_slugs in library_targets:
        with archive(read_bytes(relative), relative) as zipped:
            root = 'TaskLibrary-Skills'
            require_member(zipped, f'{root}/START-HERE.md', relative)
            require_member(zipped, f'{root}/README.md', relative)
            manifest = json.loads(require_member(
                zipped, f'{root}/manifest.json', relative))
            actual_slugs = {row['slug'] for row in manifest['tasks']}
            if manifest['total'] != len(expected_slugs) or actual_slugs != expected_slugs:
                raise ValueError(f'{relative}: manifest task set/count is stale')
            for row in manifest['tasks']:
                actual = require_member(zipped, f'{root}/{row["path"]}', relative)
                expected = tasks[row['slug']]['content'].encode()
                if actual != expected:
                    raise ValueError(f'{relative}: stale content for {row["slug"]}')
        checks.append({'path': relative, 'skills': len(expected_slugs)})

    pack_index = json.loads(read_bytes('packs/index.json'))
    for pack in pack_index['packs']:
        relative = pack['file']
        with archive(read_bytes(relative), relative) as zipped:
            root = Path(relative).stem
            require_member(zipped, f'{root}/START-HERE.md', relative)
            require_member(zipped, f'{root}/README.md', relative)
            manifest = json.loads(require_member(
                zipped, f'{root}/MANIFEST.json', relative))
            slugs = manifest['skills']
            if manifest['skill_count'] != pack['skill_count'] or len(slugs) != pack['skill_count']:
                raise ValueError(f'{relative}: manifest skill count is stale')
            for slug in slugs:
                if slug not in tasks:
                    raise ValueError(f'{relative}: unknown task {slug}')
                actual = require_member(
                    zipped, f'{root}/skills/{slug}/skill.md', relative)
                if actual != tasks[slug]['content'].encode():
                    raise ValueError(f'{relative}: stale content for {slug}')
        checks.append({'path': relative, 'skills': len(slugs)})

    return {'archives': len(checks), 'tasks': len(tasks), 'checks': checks}


def local_reader(directory):
    root = Path(directory).resolve()

    def read(relative):
        path = (root / relative).resolve()
        if root not in path.parents:
            raise ValueError(f'path leaves dashboard root: {relative}')
        return path.read_bytes()

    return read


def http_reader(base_url, timeout):
    base = base_url.rstrip('/') + '/'

    def read(relative):
        url = urljoin(base, relative)
        request = Request(url, headers={
            'User-Agent': 'task-library-deployment-check',
            'Cache-Control': 'no-cache',
        })
        with urlopen(request, timeout=timeout) as response:
            if response.status != 200:
                raise ValueError(f'{url}: HTTP {response.status}')
            return response.read()

    return read


def main():
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--dashboard-dir')
    source.add_argument('--base-url')
    parser.add_argument('--retries', type=int, default=1)
    parser.add_argument('--retry-delay', type=float, default=5)
    parser.add_argument('--timeout', type=float, default=30)
    args = parser.parse_args()
    if args.retries < 1:
        parser.error('--retries must be at least 1')

    reader = (local_reader(args.dashboard_dir) if args.dashboard_dir else
              http_reader(args.base_url, args.timeout))
    for attempt in range(1, args.retries + 1):
        try:
            result = validate(reader)
            print(json.dumps({'status': 'pass', **result}, sort_keys=True))
            return 0
        except Exception as exc:
            print(f'archive check {attempt}/{args.retries} failed: {exc}',
                  file=sys.stderr)
            if attempt == args.retries:
                return 1
            time.sleep(args.retry_delay)
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
