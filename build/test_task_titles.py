import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('library_title_build',Path(__file__).with_name('build.py'))
build=importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

class TaskTitles(unittest.TestCase):
    def test_heading_keeps_human_words_and_acronyms(self):
        self.assertEqual(build.display_title('---\nname: check-ga4\n---\n# Check GA4 for your business\n','check-ga4'),'Check GA4 for your business')
    def test_example_heading_in_code_is_not_the_task_title(self):
        self.assertEqual(build.display_title('```md\n# Example\n```\n# Real task\n','real-task'),'Real task')
    def test_slug_remains_usable_when_no_heading_exists(self):
        self.assertEqual(build.display_title('## Inputs\nUse the source.','write-a-note'),'Write a note')
