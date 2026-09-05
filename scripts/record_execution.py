#!/usr/bin/env python3
"""Validate or record a real task execution. Never publish or run a task."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'build'))
import executions  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path, help='JSON execution record; see EXECUTION-LEDGER.md')
    parser.add_argument('--ledger', type=Path, default=ROOT / 'build/task-executions.json')
    parser.add_argument('--task-data', type=Path, default=ROOT / 'dashboard/data.json',
                        help='Current built Task Library, including sheet-owned tasks')
    parser.add_argument('--expected-revision', help='Current record SHA-256 required for updates')
    parser.add_argument('--check', action='store_true', help='Validate without writing the ledger')
    args = parser.parse_args()
    tasks = json.loads(args.task_data.read_text(encoding='utf-8'))
    known = {t['slug'] for c in tasks['categories'] for t in c['tasks']}
    record = json.loads(args.record.read_text(encoding='utf-8'))
    result = executions.upsert(args.ledger, record, known, args.expected_revision, dry_run=args.check)
    if args.check:
        result['written'] = False
    print(json.dumps(result))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
