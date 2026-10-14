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
        names = ('articleLink', 'proofSummaryHTML', 'acceptedOutputHTML', 'historicalEvidenceHTML', 'executionHistoryHTML')
        functions = '\n'.join(match.group() for n in names
                              if (match := re.search(r'function ' + n + r'\([^)]*\)\{.*?\n\}', source, re.S)))
        script = r'''
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt = n => String(n);
const DATA = {executionHistory:{executions:[{executionId:'one', status:'running', startedAt:'2026-09-05T01:00:00Z', result:'<script>bad</script>', metaArticle:{status:'draft'}, evidenceUrls:['https://example.com/proof'], privateEvidenceRecorded:true}]}};
''' + functions + r'''
const known = {executionHistory:{status:'partial',completedRuns:0,completedLast30Days:0,failedRuns:0,executionIds:['one']}};
const historical={historicalDeliveryEvidence:{count:1,candidateCount:1,records:[{outcome:'<script>old</script>',recipeRevision:{state:'unknown'},observedAt:'2026-10-01',review:Object.fromEntries(['identity','output','acceptance','handoff'].map(k=>[k,{state:'unknown',notes:'<b>private-safe</b>'}])),evidenceUrls:[],privateEvidenceRecorded:true}]}};
const proof={recordedAcceptedOutputCount:1,historicalVerifiedOutputCount:2,historicalAcceptedOutputCount:1,historicalIdentityOutputOnlyCount:1,historicalAcceptedHandoffPassCount:0,historicalAcceptedHandoffHoldCount:1,historicalAcceptedHandoffUnresolvedCount:0,acceptedRecordedOutputs:[{executionId:'one',reviewedAt:'2026-09-01',result:'<script>accepted</script>',nextHandoff:'Output scope only',canonicalURL:'https://example.com/recipe',representation:'public-visible-text',recipeSourceSha256:'recipe-hash',instructionSourceSha256:'instruction-hash',criteria:{result:{state:'pass',observedResult:'<b>delivered</b>',evidenceUrls:['https://example.com/proof'],privateEvidenceRecorded:true}}}]};
proof.acceptedRecordedOutputs[0].criteria.result.expectedResult='The required output exists';
proof.acceptedRecordedOutputs[0].criteria.result.sourceUrl='https://example.com/source-requirement';
const accepted=typeof acceptedOutputHTML==='function' ? acceptedOutputHTML({...known,proofSummary:proof,standardVerification:{gates:{acceptedExecution:{state:'unmet',reason:'Current instructions changed'}}}},true) : '';
const summary=typeof proofSummaryHTML==='function' ? proofSummaryHTML(proof) : '';
process.stdout.write(JSON.stringify({accepted,summary,historical:executionHistoryHTML(historical,true),unknown:executionHistoryHTML({},true),known:executionHistoryHTML(known,true),reference:articleLink({article:'https://example.com/guide',articleState:'ready',articleKind:'reference',metaCountStatus:'verified',metaArticleCount:85,metaOrbitAudited:'2026-08-24'})}));
'''
        return json.loads(subprocess.check_output(['node', '-e', script], text=True))

    def test_source_ui_shows_dated_scope_beside_current_failure_and_handoff_hold(self):
        result = self.run_ui('app.js')
        self.assertIn('1 recorded job has an accepted result', result['accepted'])
        self.assertIn('Accepted 2026-09-01', result['accepted'])
        self.assertIn('Current recipe acceptance: unmet', result['accepted'])
        self.assertIn('Current instructions changed', result['accepted'])
        self.assertIn('instruction-hash', result['accepted'])
        self.assertIn('Scope: named criteria', result['accepted'])
        self.assertIn('Expected: The required output exists', result['accepted'])
        self.assertIn('https://example.com/source-requirement', result['accepted'])
        self.assertIn('&lt;script&gt;', result['accepted'])
        self.assertNotIn('<script>', result['accepted'])
        self.assertIn('1 were accepted for the scope described below', result['summary'])
        self.assertIn('1 have identity/output proof without recorded acceptance', result['summary'])
        self.assertIn('0 pass, 1 held, 0 unresolved', result['summary'])
        self.assertIn('Installation and scheduling are not certified', result['summary'])
        self.assertIn('Exact recipe and instruction identities', result['accepted'])
        self.assertIn('overflow-wrap:anywhere', result['accepted'])

    def test_both_ui_sources_show_truthful_counts_and_escape_public_text(self):
        for filename in ('app.js', 'dashboard/app.js'):
            with self.subTest(filename=filename):
                result = self.run_ui(filename)
                self.assertIn('Run frequency unknown', result['unknown'])
                self.assertNotIn('0 recorded', result['unknown'])
                self.assertIn('1 checked historical delivery', result['historical'])
                self.assertIn('Acceptance: unknown', result['historical'])
                self.assertIn('Run frequency unknown', result['historical'])
                self.assertIn('&lt;script&gt;', result['historical'])
                self.assertNotIn('<script>', result['historical'])
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
