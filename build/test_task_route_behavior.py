"""Behavior regressions for exact task entry and readable recipe rendering."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / 'dashboard/app.js').read_text()

def functions(*names):
    return '\n'.join((re.search(r'^function esc.*$', SOURCE, re.M).group() if name == 'esc' else re.search(r'function ' + name + r'\([^)]*\)\{.*?\n\}', SOURCE, re.S).group()) for name in names)

@unittest.skipUnless(shutil.which('node'), 'Node is required for UI behavior checks')
class TaskRouteBehavior(unittest.TestCase):
    def js(self, source):
        return json.loads(subprocess.check_output(['node', '-e', source], text=True))

    def fixture(self):
        return r'''
const state={q:'',status:'gap',phase:'Produce',minImp:5,articleKey:'old',taskSlug:'',open:new Set(),userClosed:new Set([0])};
const a={slug:'place-links',_hay:'place-links current recipe',status:'complete',_cat:{_ci:0},_articleKey:'hub'};
const b={slug:'check-links',_hay:'check-links prerequisite place-links',status:'complete',_cat:{_ci:0},_articleKey:'hub'};
const DATA={categories:[{tasks:[a,b]}]};
const bySlug=Object.assign(Object.create(null),{'place-links':a,'check-links':b});
const byArticle=Object.assign(Object.create(null),{hub:[a,b]});
const qInput={value:''},clearBtn={hidden:true},resline={},emptyBox={};
const CHIPS=[],renderedCats=new Set();let opened=null,closed=0,message='',focused=false;
const node={classList:{toggle(){}},style:{},setAttribute(){},scrollIntoView(){},querySelector(){return {focus(){focused=true}}}};
const el=()=>node,fmt=String,esc=String,setOpen=()=>{},ensureRendered=()=>{};
const syncChips=()=>{},syncPhases=()=>{},closeModal=()=>{closed++;},openModal=t=>{opened=t.slug};
const toast=s=>{message=s},setTimeout=fn=>fn(),reduced=true,normalizeArticleUrl=x=>x;
''' + functions('filterActive', 'statusMatch', 'phaseMatch', 'applyFilters', 'gotoSlug', 'gotoArticle', 'resetFilters')

    def test_known_task_opens_exact_guide_despite_cross_references_and_filters(self):
        got=self.js(self.fixture()+"\ngotoSlug('place-links');process.stdout.write(JSON.stringify({visible:[a,b].filter(t=>t._vis).map(t=>t.slug),opened,closed,focused,phase:state.phase,minImp:state.minImp,catClosed:state.userClosed.has(0)}));")
        self.assertEqual(got,{'visible':['place-links'],'opened':'place-links','closed':1,'focused':True,'phase':'all','minImp':0,'catClosed':False})

    def test_typing_search_restores_full_text_matches(self):
        handler=re.search(r"qInput.addEventListener\('input', debounce\(function\(\)\{(.*?)\n\}, 120\)\);",SOURCE,re.S).group(1)
        got=self.js(self.fixture()+"\ngotoSlug('place-links');qInput.value='place-links';(function(){"+handler+"})();process.stdout.write(JSON.stringify([a,b].filter(t=>t._vis).map(t=>t.slug)));")
        self.assertEqual(got,['place-links','check-links'])

    def test_query_entered_before_data_load_is_applied_on_startup(self):
        bootstrap=SOURCE.rsplit('   Go\n',1)[1].split('*/',1)[1].rsplit('})();',1)[0]
        got=self.js(self.fixture()+"\nstate.status='all';state.phase='all';state.minImp=0;state.articleKey='';qInput.value='check-links';const routeFromUrl=()=>({});\n"+bootstrap+"\nprocess.stdout.write(JSON.stringify({visible:[a,b].filter(t=>t._vis).map(t=>t.slug),query:qInput.value,clearHidden:clearBtn.hidden}));")
        self.assertEqual(got,{'visible':['check-links'],'query':'check-links','clearHidden':False})

    def test_exact_linked_task_takes_precedence_over_a_restored_search(self):
        bootstrap=SOURCE.rsplit('   Go\n',1)[1].split('*/',1)[1].rsplit('})();',1)[0]
        got=self.js(self.fixture()+"\nstate.status='all';state.phase='all';state.minImp=0;state.articleKey='';qInput.value='check-links';const routeFromUrl=()=>({task:'place-links'});\n"+bootstrap+"\nprocess.stdout.write(JSON.stringify({visible:[a,b].filter(t=>t._vis).map(t=>t.slug),opened}));")
        self.assertEqual(got,{'visible':['place-links'],'opened':'place-links'})

    def test_article_route_clears_exact_task_constraint(self):
        got=self.js(self.fixture()+"\ngotoSlug('place-links');gotoArticle('hub');process.stdout.write(JSON.stringify({task:state.taskSlug,visible:[a,b].filter(t=>t._vis).map(t=>t.slug),closed}));")
        self.assertEqual(got,{'task':'','visible':['place-links','check-links'],'closed':2})

    def test_unknown_or_inherited_name_does_not_open_or_change_selection(self):
        got=self.js(self.fixture()+"\ngotoSlug('place-links');gotoSlug('constructor');process.stdout.write(JSON.stringify({opened,task:state.taskSlug,closed,message}));")
        self.assertEqual(got['opened'],'place-links');self.assertEqual(got['task'],'place-links');self.assertEqual(got['closed'],1)
        self.assertIn('No skill named constructor',got['message'])

    def test_reset_allows_browsing_other_tasks(self):
        got=self.js(self.fixture()+"\ngotoSlug('place-links');resetFilters();process.stdout.write(JSON.stringify({task:state.taskSlug,query:qInput.value,visible:[a,b].filter(t=>t._vis).map(t=>t.slug)}));")
        self.assertEqual(got,{'task':'','query':'','visible':['place-links','check-links']})

    def test_embedded_reveal_reports_position_only_for_parent_frame(self):
        got=self.js("const messages=[];const window={self:1,top:2,scrollY:40,parent:{postMessage:(m,o)=>messages.push([m,o])}};"+functions('revealEmbeddedElement')+"revealEmbeddedElement({getBoundingClientRect:()=>({top:80})});window.top=1;revealEmbeddedElement({getBoundingClientRect:()=>({top:9})});process.stdout.write(JSON.stringify(messages));")
        self.assertEqual(got,[[{'btlRevealY':120},'*']])

    def render(self, md):
        helpers="const ESC={'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',\"'\":'&#39;'};\n"+functions('esc','inline','splitRow','liHtml','buildList','isFactoryMarker','renderMD')
        return self.js(helpers+'\nconst src='+json.dumps(md)+';process.stdout.write(JSON.stringify({html:renderMD(src),src}));')

    def test_only_standalone_build_markers_are_hidden(self):
        md='Before\r\n<!-- factory-layer:start -->\r\n## Next step\r\nKeep the output.\r\n  <!-- factory-layer:end -->  \r\nAfter'
        got=self.render(md)
        self.assertNotIn('factory-layer:',got['html']);self.assertIn('<h2>Next step</h2>',got['html']);self.assertIn('Before',got['html']);self.assertIn('After',got['html']);self.assertEqual(got['src'],md)

    def test_code_and_inline_examples_are_not_removed_or_executed(self):
        md='```html\n<!-- factory-layer:start -->\n<script>alert(1)</script>\n```\n\nExplain <!-- factory-layer:end --> here.'
        got=self.render(md)['html'];self.assertEqual(got.count('factory-layer:'),2);self.assertIn('&lt;script&gt;',got);self.assertNotIn('<script>',got)

if __name__=='__main__':unittest.main()
