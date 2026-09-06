import hashlib
import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location('review_build',Path(__file__).with_name('build.py'))
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
class InstructionReviews(unittest.TestCase):
    def review(self,text):
        return {'job':{'source_sha256':hashlib.sha256(text.encode()).hexdigest(),'reviewed_at':'2026-09-06','reviewer':'Reviewer','scope':'Instructions only'}}
    def test_exact_revision_carries_review_without_a_status_promotion(self):
        r=build.current_instruction_review('job','Source',self.review('Source'))
        self.assertEqual(r['scope'],'Instructions only');self.assertNotIn('status',r)
    def test_edited_source_expires_review(self):
        self.assertIsNone(build.current_instruction_review('job','Changed',self.review('Source')))
    def test_unknown_source_and_missing_reviewer_cannot_claim_review(self):
        self.assertIsNone(build.current_instruction_review('other','Source',self.review('Source')))
        r=self.review('Source');r['job']['reviewer']=''
        with self.assertRaises(ValueError):build.current_instruction_review('job','Source',r)
