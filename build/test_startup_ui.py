import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]

@unittest.skipUnless(shutil.which('node'), 'Node is required for UI behavior checks')
class StartupUI(unittest.TestCase):
    def render(self, task):
        source=(ROOT/'dashboard/app.js').read_text()
        functions='\n'.join(re.search(r'function '+name+r'\([^)]*\)\{.*?\n\}',source,re.S).group() for name in ('starterPrompt','firstRunHTML'))
        js="const esc=s=>String(s).replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',\"'\":'&#39;'}[c]));\nconst STATUS={complete:{label:'Reported complete'},gap:{label:'Gap'}};\n"+functions+'\nconst t='+json.dumps(task)+'; process.stdout.write(JSON.stringify({prompt:starterPrompt(t),html:firstRunHTML(t)}));'
        return json.loads(subprocess.check_output(['node','-e',js],text=True))

    def test_prompt_preserves_selected_guide_and_exact_task(self):
        guide='## Inputs\nUse the supplied call notes.\n## Steps\n1. Draft two titles.'
        got=self.render({'title':'Draft two titles','slug':'draft-titles','content':guide,'status':'complete'})
        self.assertTrue(got['prompt'].endswith(guide))
        self.assertIn('?task=draft-titles#task-draft-titles',got['prompt'])
        self.assertIn('My business and the result I want: [fill in]',got['prompt'])
        self.assertIn('required account access',got['prompt'])
        self.assertIn('one draft or read-only check',got['prompt'])
        self.assertIn('only when I ask for it',got['prompt'])
        self.assertIn('This is a contributor claim',got['html'])
        self.assertIn('installation and account access are not checked here',got['html'])

    def test_empty_guide_copy_reports_the_gap_without_writing_clipboard(self):
        source=(ROOT/'dashboard/app.js').read_text()
        fn=re.search(r'function copyGuide\([^)]*\)\{.*?\n\}',source,re.S).group()
        js="let wrote=false,message='';const copyText=()=>{wrote=true};const toast=s=>{message=s};\n"+fn+"\ncopyGuide({content:'   '});process.stdout.write(JSON.stringify({wrote,message}));"
        got=json.loads(subprocess.check_output(['node','-e',js],text=True))
        self.assertFalse(got['wrote'])
        self.assertIn('Guide missing',got['message'])

    def test_missing_guide_does_not_become_an_executable_recipe(self):
        got=self.render({'slug':'missing','status':'gap'})
        self.assertIn('Guide missing: ask for the maintained instructions',got['prompt'])
        self.assertNotIn('Reported complete',got['html'])

    def test_incomplete_example_is_visible_without_promoting_the_task(self):
        got=self.render({'slug':'example','status':'complete','content':'Example needed — run the Meta-Article Prompt after first real run.'})
        self.assertIn('This guide still asks for an example.',got['html'])
        self.assertNotIn('verified ready',got['html'].lower())

if __name__=='__main__':unittest.main()
