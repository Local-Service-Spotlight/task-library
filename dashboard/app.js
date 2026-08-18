
(function(){
'use strict';

/* ============================================================
   DATA — injected by the build script. Do not edit by hand.
   ============================================================ */
const DATA = window.__TASK_DATA;
/* ============================================================
   Tiny DOM + format helpers
   ============================================================ */
const root = document.getElementById('btl-app');
const el = function(sel){ return root.querySelector(sel); };
const ESC = {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'};
function esc(s){ return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){ return ESC[c]; }); }
function fmt(n){ return Number(n || 0).toLocaleString('en-US'); }
function debounce(fn, ms){ let t; return function(){ clearTimeout(t); const a = arguments; t = setTimeout(function(){ fn.apply(null, a); }, ms); }; }
const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const STATUS = {
  'complete':   { label: 'Complete' },
  'needs-work': { label: 'Needs work' },
  'gap':        { label: 'Gap' }
};

/* ============================================================
   Markdown renderer — purpose-built for skill.md files:
   frontmatter, headings, tables, lists + checkboxes, fenced
   code, blockquotes, links. All input is HTML-escaped first.
   ============================================================ */
function inline(md){
  let s = esc(md);
  s = s.replace(/`([^`]+)`/g, function(m, c){ return '<code>' + c + '</code>'; });
  s = s.replace(/!\[([^\]]*)\]\(([^)\s]+)(?:\s[^)]*)?\)/g, function(m, a, u){
    return '<a href="' + u + '" target="_blank" rel="noopener">' + (a || u) + '</a>'; });
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s[^)]*)?\)/g, function(m, a, u){
    return '<a href="' + u + '" target="_blank" rel="noopener">' + a + '</a>'; });
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  s = s.replace(/(^|[\s(>])\*([^*\n]+)\*/g, '$1<em>$2</em>');
  s = s.replace(/(^|[\s(>])_([^_\n]+)_(?=[\s).,;:!?]|$)/g, '$1<em>$2</em>');
  s = s.replace(/(^|[\s(>])(https?:\/\/[^\s<)]+)/g, function(m, pre, u){
    return pre + '<a href="' + u + '" target="_blank" rel="noopener">' + u + '</a>'; });
  return s;
}
function splitRow(l){
  let s = l.trim();
  if (s.charAt(0) === '|') s = s.slice(1);
  if (s.charAt(s.length - 1) === '|') s = s.slice(0, -1);
  return s.split('|').map(function(c){ return c.trim(); });
}
function liHtml(txt){
  const cb = txt.match(/^\[([ xX])\]\s*(.*)$/);
  if (cb){
    const on = cb[1] !== ' ';
    return '<li class="task"><span class="cb' + (on ? ' on' : '') + '">' + (on ? '✓' : '') + '</span><span>' + inline(cb[2]) + '</span></li>';
  }
  return '<li>' + inline(txt) + '</li>';
}
function buildList(items, ordered){
  if (!items.length) return '';
  const base = Math.min.apply(null, items.map(function(x){ return x.ind; }));
  const tops = [];
  items.forEach(function(it){
    if (it.ind <= base + 1 || !tops.length) tops.push({ txt: it.txt, kids: [] });
    else tops[tops.length - 1].kids.push(it.txt);
  });
  const tag = ordered ? 'ol' : 'ul';
  return '<' + tag + '>' + tops.map(function(t){
    let li = liHtml(t.txt);
    if (t.kids.length) li = li.replace(/<\/li>$/, '<ul>' + t.kids.map(liHtml).join('') + '</ul></li>');
    return li;
  }).join('') + '</' + tag + '>';
}
function renderMD(src){
  const out = [];
  const lines = String(src == null ? '' : src).replace(/\r\n?/g, '\n').split('\n');
  let i = 0;
  /* --- frontmatter → labeled meta block --- */
  if (lines[0] === '---'){
    let j = 1;
    while (j < lines.length && lines[j] !== '---') j++;
    if (j < lines.length){
      const rows = [];
      for (let k = 1; k < j; k++){
        const m = lines[k].match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
        if (m) rows.push('<div class="fm-row"><span class="fm-k">' + esc(m[1]) + '</span><span class="fm-v">' + inline(m[2].replace(/^["']|["']$/g, '')) + '</span></div>');
        else if (lines[k].trim()) rows.push('<div class="fm-row"><span class="fm-k"></span><span class="fm-v">' + inline(lines[k].trim()) + '</span></div>');
      }
      if (rows.length) out.push('<div class="btl-fm"><div class="fm-t">skill.md frontmatter</div>' + rows.join('') + '</div>');
      i = j + 1;
    }
  }
  while (i < lines.length){
    const L = lines[i];
    if (!L.trim()){ i++; continue; }
    /* fenced code */
    let m = L.match(/^\s*```/);
    if (m){
      const buf = []; i++;
      while (i < lines.length && !/^\s*```/.test(lines[i])){ buf.push(lines[i]); i++; }
      i++;
      out.push('<pre><code>' + esc(buf.join('\n')) + '</code></pre>');
      continue;
    }
    /* heading */
    m = L.match(/^(#{1,6})\s+(.*)$/);
    if (m){
      const lv = m[1].length;
      out.push('<h' + lv + '>' + inline(m[2].replace(/\s#+\s*$/, '')) + '</h' + lv + '>');
      i++; continue;
    }
    /* hr */
    if (/^\s*(?:-{3,}|\*{3,}|_{3,})\s*$/.test(L)){ out.push('<hr>'); i++; continue; }
    /* blockquote */
    if (/^\s*>/.test(L)){
      const buf = [];
      while (i < lines.length && /^\s*>/.test(lines[i])){ buf.push(lines[i].replace(/^\s*>\s?/, '')); i++; }
      out.push('<blockquote>' + renderMD(buf.join('\n')) + '</blockquote>');
      continue;
    }
    /* table */
    const sep = lines[i + 1] || '';
    if (L.indexOf('|') !== -1 && /-/.test(sep) && /^\s*\|?[\s:|-]+\|?\s*$/.test(sep)){
      const head = splitRow(L); i += 2;
      const body = [];
      while (i < lines.length && lines[i].indexOf('|') !== -1 && lines[i].trim()){ body.push(splitRow(lines[i])); i++; }
      out.push('<div class="btl-tbl"><table><thead><tr>' +
        head.map(function(c){ return '<th>' + inline(c) + '</th>'; }).join('') +
        '</tr></thead><tbody>' +
        body.map(function(r){ return '<tr>' + r.map(function(c){ return '<td>' + inline(c) + '</td>'; }).join('') + '</tr>'; }).join('') +
        '</tbody></table></div>');
      continue;
    }
    /* list */
    m = L.match(/^(\s*)([-*+]|\d+[.)])\s+/);
    if (m){
      const ordered = /\d/.test(m[2]);
      const items = [];
      const re = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/;
      while (i < lines.length){
        const mm = lines[i].match(re);
        if (mm){ items.push({ ind: mm[1].length, txt: mm[3] }); i++; }
        else if (lines[i].trim() && /^\s{2,}/.test(lines[i]) && items.length){ items[items.length - 1].txt += ' ' + lines[i].trim(); i++; }
        else break;
      }
      out.push(buildList(items, ordered));
      continue;
    }
    /* paragraph */
    const buf = [L]; i++;
    while (i < lines.length && lines[i].trim() &&
           !/^(#{1,6}\s|\s*```|\s*>|\s*(?:[-*+]|\d+[.)])\s|\s*(?:-{3,}|\*{3,}|_{3,})\s*$)/.test(lines[i]) &&
           !(lines[i].indexOf('|') !== -1 && /^\s*\|?[\s:|-]+\|?\s*$/.test(lines[i + 1] || '') && /-/.test(lines[i + 1] || ''))){
      buf.push(lines[i]); i++;
    }
    out.push('<p>' + inline(buf.join(' ')) + '</p>');
  }
  return out.join('\n');
}
/* ============================================================
   Boot guard — graceful pre-injection preview
   ============================================================ */
if (!DATA || !DATA.categories || !DATA.categories.length){
  const note = el('#btl-noinject');
  if (note) note.hidden = false;
  return;
}

/* ============================================================
   Enrich data once: ids, lowercase haystacks, provenance flags
   ============================================================ */
const byId = {};
const bySlug = {};
DATA.categories.forEach(function(c, ci){
  c._ci = ci;
  c.tasks.forEach(function(t, ti){
    t._id = ci + '-' + ti;
    t._cat = c;
    const content = t.content || '';
    t._hay = ((t.title || '') + ' ' + (t.desc || '') + ' ' + (t.slug || '') + ' ' + content).toLowerCase();
    t._qa = /definition of done/i.test(content);
    t._ex = /^##\s+example/im.test(content) || /meta-article/i.test(content);
    t._vis = true;
    byId[t._id] = t;
    if (t.slug) bySlug[t.slug] = t;
  });
});

/* ============================================================
   Hero, footer, stats, health bar
   ============================================================ */
const dl = el('#btl-dl');
if (DATA.bundleUrl){
  dl.href = DATA.bundleUrl;
  dl.textContent = '⬇ Download all ' + (DATA.stats.total || 0) + ' skills (.zip)';
  var readyLink = document.createElement('a');
  readyLink.href = 'TaskLibrary-Skills-ready.zip';
  readyLink.className = 'btl-btn';
  readyLink.textContent = 'Owner-signed only (' + (DATA.stats.complete || 0) + ') ⬇';
  dl.parentNode.insertBefore(readyLink, dl.nextSibling);
} else { dl.hidden = true; }
const metaBtn = el('#btl-meta');
if (DATA.metaArticleUrl){ metaBtn.href = DATA.metaArticleUrl; metaBtn.hidden = false; }
el('#btl-updated').textContent = DATA.updated || '—';
const footMeta = el('#btl-foot-meta');
if (DATA.metaArticleUrl){
  footMeta.href = DATA.metaArticleUrl;
  footMeta.hidden = false;
  el('#btl-foot-sep').hidden = false;
}

const S = DATA.stats || {};
function countUp(node, val){
  if (reduced || !val){ node.textContent = fmt(val); return; }
  const t0 = performance.now(), dur = 950;
  (function tick(now){
    const p = Math.min(1, (now - t0) / dur);
    const e = 1 - Math.pow(1 - p, 3);
    node.textContent = fmt(Math.round(val * e));
    if (p < 1) requestAnimationFrame(tick);
  })(t0);
}
const cards = [
  { k:'total',              label:'Total tasks',         cls:'c-total', icon:'🗂️' },
  { k:'complete',           label:'Complete',            cls:'c-ok',    icon:'✅', chip:'complete' },
  { k:'needsWork',          label:'Needs work',          cls:'c-warn',  icon:'🛠️', chip:'needs-work' },
  { k:'gaps',               label:'Gaps',                cls:'c-bad',   icon:'⛳', chip:'gap' },
  { k:'owners',             label:'Owners',              cls:'c-art',   icon:'👤' },
  { k:'categories',         label:'Categories',          cls:'c-cat',   icon:'🧭' }
];
el('#btl-statgrid').innerHTML = cards.map(function(c){
  return '<div class="btl-stat ' + c.cls + '"' + (c.chip ? ' data-statchip="' + c.chip + '" role="button" tabindex="0" style="cursor:pointer"' : '') + '><span class="ic">' + c.icon + '</span><div class="n" data-stat="' + c.k + '">0</div><div class="l">' + c.label + '</div></div>';
}).join('');
el('#btl-statgrid').addEventListener('click', function(e){
  const tile = e.target.closest('[data-statchip]');
  if (!tile) return;
  state.status = state.status === tile.getAttribute('data-statchip') ? 'all' : tile.getAttribute('data-statchip');
  syncChips(); applyFilters();
  const chips = el('#btl-chips'); if (chips) chips.scrollIntoView({behavior:'smooth', block:'center'});
});
cards.forEach(function(c){ countUp(el('[data-stat="' + c.k + '"]'), S[c.k] || 0); });

(function health(){
  const total = S.total || 1;
  const ok = S.complete || 0, warn = S.needsWork || 0, bad = S.gaps || 0;
  const pc = function(n){ return Math.max(n > 0 ? 1.5 : 0, n / total * 100); };
  el('#btl-health-bar').innerHTML =
    '<span class="hb-ok" style="width:' + pc(ok) + '%" title="Complete: ' + ok + '"></span>' +
    '<span class="hb-warn" style="width:' + pc(warn) + '%" title="WIP: ' + warn + '"></span>' +
    '<span class="hb-bad" style="width:' + pc(bad) + '%" title="Gaps: ' + bad + '"></span>';
  el('#btl-health-pct').textContent = Math.round(ok / total * 100) + '% complete';
  el('#btl-health-legend').innerHTML =
    '<span><span class="d d-ok"></span><b>' + fmt(ok) + '</b> complete</span>' +
    '<span><span class="d d-warn"></span><b>' + fmt(warn) + '</b> needs work</span>' +
    '<span><span class="d d-bad"></span><b>' + fmt(bad) + '</b> gaps</span>';
})();

(function factoryUI(){
  const F = DATA.factory || {};
  const phases = F.phases || [];
  const host = el('#btl-phases');
  if (host){
    const counts = {};
    DATA.categories.forEach(function(c){
      c.tasks.forEach(function(t){
        const p = t.phase || '—';
        counts[p] = (counts[p] || 0) + 1;
      });
    });
    host.innerHTML = phases.map(function(p){
      return '<button type="button" class="btl-phase" data-phase="' + esc(p.id) + '" style="--pc:' + esc(p.color || '#4f8cff') + '" aria-pressed="false">' +
        '<div class="pn">' + esc(p.label) + '</div>' +
        '<div class="pb">' + esc(p.blurb) + '</div>' +
        '<div class="pc">' + fmt(counts[p.id] || 0) + ' tasks</div></button>';
    }).join('');
  }
  const rt = el('#btl-routing');
  if (rt && F.doctrine){
    rt.innerHTML = '<strong>Single-engine path.</strong> ' + esc(F.doctrine) +
      (F.scoring ? ' <strong>Scoring:</strong> ' + esc(F.scoring) : '');
  }
  const lanes = el('#btl-lanes');
  if (lanes && F.lanes){
    lanes.innerHTML = Object.keys(F.lanes).map(function(k){
      return '<div class="btl-lane"><div class="lk">' + esc(k) + '</div><div class="lv">' + esc(F.lanes[k]) + '</div></div>';
    }).join('');
  }
})();

/* ============================================================
   Status chips
   ============================================================ */
const CHIPS = [
  { key:'all',        label:'All',        cls:'' },
  { key:'complete',   label:'Complete',   cls:'ch-ok' },
  { key:'needs-work', label:'Needs work', cls:'ch-warn' },
  { key:'gap',        label:'Gaps',       cls:'ch-bad' },
  { key:'vol5',       label:'★5 only',    cls:'ch-vol' },
  { key:'vol4',       label:'★4+',        cls:'ch-vol' }
];
el('#btl-chips').innerHTML = CHIPS.map(function(c){
  return '<button type="button" class="btl-chip ' + c.cls + '" data-chip="' + c.key + '" aria-pressed="' + (c.key === 'all') + '">' +
    '<span class="cd"></span>' + c.label + '<span class="cn" data-chipcount="' + c.key + '">0</span></button>';
}).join('');

/* ============================================================
   Category sections (rows render lazily on first expand)
   ============================================================ */
function volBar(n){
  n = Math.max(1, Math.min(5, Number(n) || 1));
  let html = '<span class="btl-vol" data-n="' + n + '" title="Importance ' + n + '/5 — max of frequency, ads/revenue, and gating">';
  for (let i = 1; i <= 5; i++) html += '<i' + (i <= n ? ' class="on"' : '') + '></i>';
  html += '<span class="btl-vol-n">' + n + '</span></span>';
  return html;
}
function rowHTML(t){
  const st = STATUS[t.status] || STATUS.gap;
  let badges = '<span class="btl-tag tag-sop" title="Step-by-step SOP included">SOP</span>';
  if (t._qa) badges += '<span class="btl-tag tag-qa" title="Has a Definition of Done QA gate">QA</span>';
  if (t._ex) badges += '<span class="btl-tag tag-ex" title="Has a worked example / meta-article slot">Example</span>';
  if (t.lane) badges += '<span class="btl-tag tag-sop" title="' + esc(t.lane_label || t.lane) + '">' + esc(t.lane) + '</span>';
  const stage = (t.stage && t.stage !== '—') ? '<span class="btl-stage">' + esc(t.stage) + '</span>' : '';
  const art = (t.article ? '<a class="btl-art" href="' + esc(t.article) + '" target="_blank" rel="noopener">Definitive article ↗</a>' : '') +
    (t.download ? '<a class="btl-art" href="' + esc(t.download) + '" target="_blank" rel="noopener">Download full skill suite ⬇</a>' : '');
  let chain = '';
  if (t.before || t.after || t.phase){
    chain = '<p class="btl-chain">' +
      (t.phase ? '<b>' + esc(t.phase) + '</b> · ' : '') +
      (t.before ? 'before <button type="button" data-goto="' + esc(t.before) + '">' + esc(t.before) + '</button>' : '') +
      (t.before && t.after ? ' → ' : '') +
      (t.after ? 'after <button type="button" data-goto="' + esc(t.after) + '">' + esc(t.after) + '</button>' : '') +
      '</p>';
  }
  return '<article class="btl-row" data-id="' + t._id + '" data-slug="' + esc(t.slug) + '">' +
    '<span class="btl-dot dot-' + esc(t.status) + '" aria-hidden="true"></span>' +
    '<div class="btl-row-main">' +
      '<div class="btl-row-top"><h4 class="btl-row-title">' + esc(t.title) + '</h4>' +
        volBar(t.importance) +
        '<span class="btl-status st-' + esc(t.status) + '">' + st.label + '</span>' + stage + '</div>' +
      (t.desc ? '<p class="btl-row-desc">' + esc(t.desc) + '</p>' : '') +
      chain +
      '<div class="btl-row-meta">' + badges + art + '</div>' +
    '</div>' +
    '<div class="btl-row-actions">' +
      '<button type="button" class="btl-mini btl-view" data-view="' + t._id + '">View skill</button>' +
      '<button type="button" class="btl-mini" data-copy="' + t._id + '">Copy</button>' +
    '</div></article>';
}
el('#btl-cats').innerHTML = DATA.categories.map(function(c, ci){
  return '<section class="btl-cat" id="btl-cat-' + ci + '" style="--cat:' + esc(c.color || '#4f8cff') + '">' +
    '<button type="button" class="btl-cat-head" data-cat="' + ci + '" aria-expanded="false" aria-controls="btl-cat-body-' + ci + '">' +
      '<span class="btl-cat-icon" aria-hidden="true">' + esc(c.icon || '📁') + '</span>' +
      '<span class="btl-cat-info"><span class="btl-cat-name">' + esc(c.name) + '</span>' +
        '<span class="btl-cat-desc">' + esc(c.description || '') + '</span></span>' +
      '<span class="btl-cat-side">' +
        '<span class="btl-cat-match" data-catmatch="' + ci + '" hidden></span>' +
        '<span class="btl-cat-count">' + c.tasks.length + ' tasks</span>' +
        '<span class="btl-chev" aria-hidden="true">▾</span></span>' +
    '</button>' +
    '<div class="btl-cat-body" id="btl-cat-body-' + ci + '" hidden><div class="btl-rows" data-rows="' + ci + '"></div></div>' +
  '</section>';
}).join('');

const renderedCats = new Set();
function ensureRendered(ci){
  if (renderedCats.has(ci)) return;
  const host = el('[data-rows="' + ci + '"]');
  host.innerHTML = DATA.categories[ci].tasks.map(rowHTML).join('');
  renderedCats.add(ci);
}
/* ============================================================
   Filtering engine — search (incl. full skill.md text) + chips
   ============================================================ */
const state = { q: '', status: 'all', open: new Set(), userClosed: new Set(), phase: 'all', minImp: 0 };
const qInput = el('#btl-q'), clearBtn = el('#btl-clear'), resline = el('#btl-resline'), emptyBox = el('#btl-empty');

function setOpen(ci, open){
  const head = el('[data-cat="' + ci + '"]');
  const body = el('#btl-cat-body-' + ci);
  if (!head || !body) return;
  if (open) ensureRendered(ci);
  head.setAttribute('aria-expanded', open ? 'true' : 'false');
  body.hidden = !open;
}
function filterActive(){ return !!(state.q.trim() || state.status !== 'all' || state.phase !== 'all' || state.minImp > 0); }

function statusMatch(t){
  if (state.status === 'all') return true;
  if (state.status === 'vol5') return (t.importance || 0) >= 5;
  if (state.status === 'vol4') return (t.importance || 0) >= 4;
  return t.status === state.status;
}
function phaseMatch(t){
  if (state.phase === 'all') return true;
  return (t.phase || t.stage) === state.phase;
}

function applyFilters(){
  const q = state.q.trim().toLowerCase();
  const active = filterActive();
  if (!active) state.userClosed.clear();
  let total = 0, shown = 0;
  const counts = { all: 0, 'complete': 0, 'needs-work': 0, 'gap': 0 };

  DATA.categories.forEach(function(c, ci){
    let catMatch = 0;
    c.tasks.forEach(function(t){
      total++;
      const qok = !q || t._hay.indexOf(q) !== -1;
      if (qok){
        counts.all++;
        counts[t.status] = (counts[t.status] || 0) + 1;
        if ((t.importance || 0) >= 5) counts.vol5 = (counts.vol5 || 0) + 1;
        if ((t.importance || 0) >= 4) counts.vol4 = (counts.vol4 || 0) + 1;
      }
      t._vis = qok && statusMatch(t) && phaseMatch(t);
      if (t._vis){ catMatch++; shown++; }
    });
    c._match = catMatch;

    const pill = el('[data-catmatch="' + ci + '"]');
    if (pill){
      if (active && catMatch > 0){ pill.hidden = false; pill.textContent = catMatch + (catMatch === 1 ? ' match' : ' matches'); }
      else pill.hidden = true;
    }
    el('#btl-cat-' + ci).classList.toggle('is-zero', active && catMatch === 0);

    const shouldOpen = active ? (catMatch > 0 && !state.userClosed.has(ci)) : state.open.has(ci);
    setOpen(ci, shouldOpen);

    if (renderedCats.has(ci)){
      c.tasks.forEach(function(t){
        const r = el('[data-id="' + t._id + '"]');
        if (r) r.hidden = !t._vis;
      });
    }
  });

  CHIPS.forEach(function(ch){
    const n = el('[data-chipcount="' + ch.key + '"]');
    if (n) n.textContent = fmt(counts[ch.key] || 0);
  });

  resline.innerHTML = (!active)
    ? '<b>' + fmt(total) + '</b> tasks across <b>' + fmt(DATA.categories.length) + '</b> categories — search runs through the full text of every skill.md'
    : '<b>' + fmt(shown) + '</b> of <b>' + fmt(total) + '</b> tasks match' + (q ? ' “' + esc(state.q.trim()) + '”' : '') + (state.status !== 'all' ? ' · ' + (STATUS[state.status] ? STATUS[state.status].label.toLowerCase() : state.status) : '') + (state.phase !== 'all' ? ' · phase: ' + esc(state.phase) : '');
  emptyBox.hidden = shown !== 0;
}

function syncChips(){
  CHIPS.forEach(function(ch){
    const b = el('[data-chip="' + ch.key + '"]');
    if (b) b.setAttribute('aria-pressed', state.status === ch.key ? 'true' : 'false');
  });
}
function syncPhases(){
  root.querySelectorAll('[data-phase]').forEach(function(b){
    b.setAttribute('aria-pressed', state.phase === b.getAttribute('data-phase') ? 'true' : 'false');
  });
}
function gotoSlug(slug){
  const t = bySlug[slug];
  if (!t){ toast('No skill named ' + slug + ' in this build'); return; }
  state.q = slug; qInput.value = slug; clearBtn.hidden = false;
  state.status = 'all'; syncChips(); applyFilters();
  ensureRendered(t._cat._ci);
  const row = el('[data-slug="' + slug + '"]');
  if (row){
    row.scrollIntoView({behavior:'smooth', block:'center'});
    row.style.outline = '2px solid #4f8cff';
    setTimeout(function(){ row.style.outline = ''; }, 1600);
  }
}
function resetFilters(){
  state.q = ''; qInput.value = ''; clearBtn.hidden = true;
  state.status = 'all'; state.phase = 'all'; syncChips(); syncPhases(); applyFilters();
}

/* ============================================================
   Copy + toast
   ============================================================ */
const toastEl = el('#btl-toast');
let toastTimer = null;
function toast(msg){
  toastEl.textContent = msg;
  toastEl.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(function(){ toastEl.classList.remove('show'); }, 2400);
}
function copyText(txt, msg){
  function fallback(){
    try{
      const ta = document.createElement('textarea');
      ta.value = txt; ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;left:-9999px;top:0';
      document.body.appendChild(ta); ta.select();
      const ok = document.execCommand('copy');
      document.body.removeChild(ta);
      toast(ok ? msg : 'Copy failed — open the skill and copy manually');
    }catch(e){ toast('Copy failed — open the skill and copy manually'); }
  }
  if (navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(txt).then(function(){ toast(msg); }, fallback);
  } else fallback();
}
function trunc(s, n){ s = String(s || ''); return s.length > n ? s.slice(0, n - 1) + '…' : s; }

/* ============================================================
   Modal — full skill.md, focus-trapped, Esc/backdrop close
   ============================================================ */
const modal = el('#btl-modal'), mPanel = root.querySelector('.btl-m-panel'),
      mMeta = el('#btl-m-meta'), mTitle = el('#btl-m-title'),
      mSub = el('#btl-m-sub'), mBody = el('#btl-m-body'),
      mCopy = el('#btl-m-copy'), mClose = root.querySelector('.btl-m-close');
let modalTask = null, lastFocus = null, prevOverflow = '';

function openModal(t){
  if (!t) return;
  modalTask = t;
  lastFocus = document.activeElement;
  const st = STATUS[t.status] || STATUS.gap;
  mMeta.innerHTML = '<span class="btl-status st-' + esc(t.status) + '">' + st.label + '</span>' +
    volBar(t.importance) +
    '<span class="btl-m-cat">' + esc((t._cat.icon ? t._cat.icon + ' ' : '') + t._cat.name) + '</span>' +
    ((t.stage && t.stage !== '—') ? '<span class="btl-stage">' + esc(t.stage) + '</span>' : '') +
    (t.lane ? '<span class="btl-stage">' + esc(t.lane) + '</span>' : '');
  mTitle.textContent = t.title;
  mSub.innerHTML = '<code class="btl-slug">' + esc(t.slug || 'skill') + '.skill.md</code>' +
    (t.article ? '<a class="btl-art" href="' + esc(t.article) + '" target="_blank" rel="noopener">Definitive article ↗</a>' : '') +
    (t.download ? '<a class="btl-art" href="' + esc(t.download) + '" target="_blank" rel="noopener">Download full skill suite ⬇</a>' : '');
  mBody.innerHTML = renderMD(t.content || '*No skill.md captured yet — this task is a gap to close on the next run of the loop.*');
  prevOverflow = document.body.style.overflow;
  const embedded = window.self !== window.top;
  if (embedded){
    /* Inside the WP iframe the frame is content-height, so fixed+vh sizing
       breaks: anchor the panel at the clicked row (guaranteed on-screen)
       and cap its height to a real screen's worth. */
    const anchorY = lastFocus ? lastFocus.getBoundingClientRect().top + window.scrollY : 0;
    const cap = Math.min(Math.round((screen.availHeight || 900) * 0.78), 760);
    modal.style.position = 'absolute';
    modal.style.height = document.documentElement.scrollHeight + 'px';
    modal.style.alignItems = 'flex-start';
    const panel = modal.querySelector('.btl-m-panel');
    if (panel){
      panel.style.marginTop = Math.max(anchorY - 120, 8) + 'px';
      panel.style.maxHeight = cap + 'px';
    }
  } else {
    document.body.style.overflow = 'hidden';
  }
  modal.hidden = false;
  mBody.scrollTop = 0;
  mClose.focus();
}
function closeModal(){
  if (modal.hidden) return;
  modal.hidden = true;
  modal.style.position = ''; modal.style.height = ''; modal.style.alignItems = '';
  const panel = modal.querySelector('.btl-m-panel');
  if (panel){ panel.style.marginTop = ''; panel.style.maxHeight = ''; }
  modalTask = null;
  document.body.style.overflow = prevOverflow;
  if (lastFocus && lastFocus.focus) lastFocus.focus();
}
function trapFocus(e){
  const items = modal.querySelectorAll('button, a[href], [tabindex]:not([tabindex="-1"])');
  const list = Array.prototype.filter.call(items, function(n){ return n.offsetParent !== null || n === mBody; });
  if (!list.length) return;
  const first = list[0], last = list[list.length - 1];
  if (e.shiftKey && document.activeElement === first){ e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last){ e.preventDefault(); first.focus(); }
}

/* ============================================================
   Events — one delegated listener keeps the DOM light
   ============================================================ */
root.addEventListener('click', function(e){
  const view = e.target.closest('[data-view]');
  if (view){ openModal(byId[view.getAttribute('data-view')]); return; }

  const cp = e.target.closest('[data-copy]');
  if (cp){
    const t = byId[cp.getAttribute('data-copy')];
    if (t) copyText(t.content || '', 'Copied “' + trunc(t.title, 44) + '” skill.md');
    return;
  }

  const head = e.target.closest('.btl-cat-head');
  if (head){
    const ci = parseInt(head.getAttribute('data-cat'), 10);
    const isOpen = head.getAttribute('aria-expanded') === 'true';
    if (filterActive()){
      if (isOpen) state.userClosed.add(ci); else state.userClosed.delete(ci);
    } else {
      if (isOpen) state.open.delete(ci); else state.open.add(ci);
    }
    setOpen(ci, !isOpen);
    return;
  }

  const chip = e.target.closest('[data-chip]');
  if (chip){
    state.status = chip.getAttribute('data-chip');
    syncChips(); applyFilters();
    return;
  }
  const ph = e.target.closest('[data-phase]');
  if (ph){
    const id = ph.getAttribute('data-phase');
    state.phase = state.phase === id ? 'all' : id;
    syncPhases(); applyFilters();
    const chips = el('#btl-chips'); if (chips) chips.scrollIntoView({behavior:'smooth', block:'center'});
    return;
  }
  const go = e.target.closest('[data-goto]');
  if (go){
    gotoSlug(go.getAttribute('data-goto'));
    return;
  }

  if (e.target.closest('#btl-expand')){
    state.userClosed.clear();
    DATA.categories.forEach(function(c, ci){ state.open.add(ci); });
    applyFilters();
    return;
  }
  if (e.target.closest('#btl-collapse')){
    state.open.clear();
    DATA.categories.forEach(function(c, ci){ state.userClosed.add(ci); });
    applyFilters();
    return;
  }
  if (e.target.closest('#btl-reset')){ resetFilters(); return; }
  if (e.target.closest('#btl-clear')){
    state.q = ''; qInput.value = ''; clearBtn.hidden = true;
    applyFilters(); qInput.focus();
    return;
  }
  if (e.target.closest('#btl-m-copy')){
    if (modalTask) copyText(modalTask.content || '', 'Copied “' + trunc(modalTask.title, 44) + '” skill.md');
    return;
  }
  if (e.target.closest('[data-close]')){ closeModal(); return; }
});

qInput.addEventListener('input', debounce(function(){
  state.q = qInput.value;
  clearBtn.hidden = !qInput.value;
  applyFilters();
}, 120));
qInput.addEventListener('search', function(){
  state.q = qInput.value;
  clearBtn.hidden = !qInput.value;
  applyFilters();
});

document.addEventListener('keydown', function(e){
  if (modal.hidden) return;
  if (e.key === 'Escape'){ e.preventDefault(); closeModal(); }
  else if (e.key === 'Tab'){ trapFocus(e); }
});

/* ============================================================
   Go
   ============================================================ */
applyFilters();
})();
