import json
from pathlib import Path
import importlib.util
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
DASHBOARD = ROOT / 'dashboard'
SPEC = importlib.util.spec_from_file_location(
    'published_archive_checker', ROOT / 'scripts' / 'check_published_archives.py')
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class PublishedArchives(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((DASHBOARD / 'data.json').read_text())
        cls.tasks = {
            task['slug']: task
            for category in cls.data['categories']
            for task in category['tasks']
        }

    def check_library_archive(self, relative_path, expected_slugs):
        path = DASHBOARD / relative_path
        self.assertTrue(path.is_file(), f'advertised archive is missing: {relative_path}')
        with zipfile.ZipFile(path) as archive:
            self.assertIsNone(archive.testzip())
            root = 'TaskLibrary-Skills'
            self.assertIn(f'{root}/START-HERE.md', archive.namelist())
            self.assertIn(f'{root}/README.md', archive.namelist())
            manifest = json.loads(archive.read(f'{root}/manifest.json'))
            self.assertEqual(manifest['total'], len(expected_slugs))
            self.assertEqual({row['slug'] for row in manifest['tasks']}, expected_slugs)
            for row in manifest['tasks']:
                self.assertEqual(
                    archive.read(f'{root}/{row["path"]}'),
                    self.tasks[row['slug']]['content'].encode(),
                    row['slug'],
                )

    def test_dashboard_library_downloads_are_present_and_current(self):
        all_slugs = set(self.tasks)
        self.check_library_archive(self.data['bundleUrl'], all_slugs)
        complete = {slug for slug, task in self.tasks.items()
                    if task['status'] == 'complete'}
        self.assertEqual(len(complete), self.data['stats']['complete'])
        self.check_library_archive('TaskLibrary-Skills-ready.zip', complete)

    def test_every_advertised_pack_is_present_and_current(self):
        index = json.loads((DASHBOARD / 'packs' / 'index.json').read_text())
        for pack in index['packs']:
            relative_path = pack['file']
            path = DASHBOARD / relative_path
            self.assertTrue(path.is_file(), f'advertised pack is missing: {relative_path}')
            with zipfile.ZipFile(path) as archive:
                self.assertIsNone(archive.testzip())
                root = Path(relative_path).stem
                self.assertIn(f'{root}/START-HERE.md', archive.namelist())
                manifest = json.loads(archive.read(f'{root}/MANIFEST.json'))
                self.assertEqual(manifest['skill_count'], pack['skill_count'])
                self.assertEqual(len(manifest['skills']), pack['skill_count'])
                for slug in manifest['skills']:
                    self.assertIn(slug, self.tasks)
                    self.assertEqual(
                        archive.read(f'{root}/skills/{slug}/skill.md'),
                        self.tasks[slug]['content'].encode(),
                        slug,
                    )

    def test_release_checker_covers_every_advertised_archive(self):
        result = CHECKER.validate(CHECKER.local_reader(DASHBOARD))
        advertised = {
            self.data['bundleUrl'],
            'TaskLibrary-Skills-ready.zip',
            *(pack['file'] for pack in json.loads(
                (DASHBOARD / 'packs' / 'index.json').read_text())['packs']),
        }
        self.assertEqual(result['archives'], len(advertised))
        self.assertEqual({check['path'] for check in result['checks']}, advertised)


if __name__ == '__main__':
    unittest.main()
