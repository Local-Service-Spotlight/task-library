import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('node'), 'Node is needed for direct UI function evaluation')
class ExecutionUI(unittest.TestCase):
    def run_ui(self, filename):
        source = (ROOT / filename).read_text()
        names = ('articleLink', 'executionHistoryHTML')
        functions = '\n'.join(re.search(r'function ' + n + r'\([^)]*\)\{.*?\n\}', source, re.S).group() for n in names)
        script = r'''
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt = n => String(n);
const DATA = {executionHistory:{executions:[{executionId:'one', status:'running', startedAt:'2026-09-05T01:00:00Z', result:'<script>bad</script>', metaArticle:{status:'draft'}, evidenceUrls:['https://example.com/proof'], privateEvidenceRecorded:true}]}};
''' + functions + r'''
const known = {executionHistory:{status:'partial',completedRuns:0,completedLast30Days:0,failedRuns:0,executionIds:['one']}};
process.stdout.write(JSON.stringify({unknown:executionHistoryHTML({},true),known:executionHistoryHTML(known,true),reference:articleLink({article:'https://example.com/guide',articleState:'ready',articleKind:'reference',metaCountStatus:'verified',metaArticleCount:85,metaOrbitAudited:'2026-08-24'})}));
'''
        return json.loads(subprocess.check_output(['node', '-e', script], text=True))

    def test_both_ui_sources_show_truthful_counts_and_escape_public_text(self):
        for filename in ('app.js', 'dashboard/app.js'):
            with self.subTest(filename=filename):
                result = self.run_ui(filename)
                self.assertIn('Run frequency unknown', result['unknown'])
                self.assertNotIn('0 recorded', result['unknown'])
                self.assertIn('0 recorded completed runs', result['known'])
                self.assertIn('running', result['known'])
                self.assertIn('Meta article draft', result['known'])
                self.assertIn('https://example.com/proof', result['known'])
                self.assertIn('Private evidence retained', result['known'])
                self.assertIn('&lt;script&gt;', result['known'])
                self.assertNotIn('<script>', result['known'])
                self.assertIn('Reference ↗', result['reference'])
                self.assertIn('2026-08-24', result['reference'])
                self.assertIn('not execution frequency', result['reference'])
                self.assertNotIn('Definitive article ↗', result['reference'])
