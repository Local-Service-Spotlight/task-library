import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
def module(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'build'/file)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
B=module('zip_start_build','build.py')
P=module('zip_start_packs','build-packs.py')

class ZipStart(unittest.TestCase):
    def fixture(self):
        return {'updated':'2026-09-06','categories':[{'name':'Content Factory — Post','folder':'content-factory-post','tasks':[
            {'slug':'one-job','title':'One job','content':'# One job\n\nExact source ✓\n','status':'complete'},
            {'slug':'unfinished','title':'Unfinished','content':'# Unfinished\n\nMissing example\n','status':'needs-work'}]}]}
    def check_start(self,z,root):
        text=z.read(root+'/START-HERE.md').decode()
        for part in ('If you run a business','Copy this first-run prompt','A one-time draft does not need a schedule','does not update itself',"contributor's claim",'https://localservicespotlight.com/install/'):
            self.assertIn(part,text)
        self.assertIn(root+'/README.md',z.namelist())
    def test_broad_archives_keep_legacy_paths_source_bytes_and_manifest(self):
        data=self.fixture()
        with tempfile.TemporaryDirectory() as d:
            for complete,count in ((False,2),(True,1)):
                B.write_zip(data,d,'bundle.zip','Test note',complete)
                with zipfile.ZipFile(Path(d)/'bundle.zip') as z:
                    self.check_start(z,'TaskLibrary-Skills')
                    m=json.loads(z.read('TaskLibrary-Skills/manifest.json'))
                    self.assertEqual(set(m),{'total','note','tasks'});self.assertEqual(m['total'],count)
                    self.assertEqual(m['note'],'Test note')
                    for r in m['tasks']:
                        source=next(t for t in data['categories'][0]['tasks'] if t['slug']==r['slug'])
                        self.assertEqual(r['path'],'skills/content-factory-post/'+r['slug']+'.md')
                        self.assertEqual(z.read('TaskLibrary-Skills/'+r['path']),source['content'].encode())
                    self.assertNotIn('TaskLibrary-Skills/MANIFEST.json',z.namelist())
    def test_curated_archive_keeps_legacy_layout_and_reports_omitted_tasks(self):
        data=self.fixture();by,order=P.load_skills(data)
        with tempfile.TemporaryDirectory() as d:
            r=P.write_pack_zip({'id':'pack','name':'My pack'},['one-job','unfinished','missing'],by,d,data['updated'])
            with zipfile.ZipFile(Path(d)/'pack.zip') as z:
                self.check_start(z,'pack')
                m=json.loads(z.read('pack/MANIFEST.json'))
                self.assertEqual(m['skills'],['one-job','unfinished']);self.assertEqual(m['missing_from_library'],['missing'])
                self.assertEqual(z.read('pack/skills/one-job/skill.md'),by['one-job']['content'].encode())
                self.assertNotIn('always current',z.read('pack/README.md').decode())
            self.assertEqual(r['missing'],['missing'])
