/* Public lesson metadata only. This planner does not fetch protected course material. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const state = { data: null, path: null, rows: [], selected: new Set(), minutes: 30, slides: [], slide: 0, presentationReturn: 'present-session', sourceWarnings: [], practice: null, practiceDrafts: new Map(), practiceWarnings: [], practiceProvenance: null };
  const text = value => typeof value === 'string' ? value : '';
  const strings = value => Array.isArray(value) ? value.filter(item => typeof item === 'string') : [];
  function node(tag, className, value) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (value !== undefined) element.textContent = value;
    return element;
  }
  function safeLink(value) {
    if (typeof value !== 'string' || !value) return null;
    try {
      const url = new URL(value, window.location.href);
      return ['http:', 'https:'].includes(url.protocol) ? url.href : null;
    } catch (_) { return null; }
  }
  function taskLink(task) {
    return safeLink(task.taskLibraryUrl) || new URL('./?task=' + encodeURIComponent(task.slug), window.location.href).href;
  }
  function appendLink(parent, label, href) {
    if (!href) return;
    const link = node('a', '', label);
    link.href = href;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.setAttribute('aria-label', label.replace('↗', '').trim() + ' (opens in a new tab)');
    parent.append(link);
  }
  function taskFor(slug) { return state.data.tasks.find(task => task.slug === slug); }
  function materialFor(id) { return (state.data.materials || []).find(material => material.id === id); }
  function pathMaterials() { return (state.data.materials || []).filter(material => strings(material.pathIds).includes(state.path?.id)); }
  function materialRefs(materials) { return materials.map(material => ({ id: material.id, sha256: text(material.verification?.sha256) || null })); }
  function materialCard(material) {
    const card = node('article', 'material-card');
    card.dataset.material = material.id;
    const protectedEntry = material.access === 'protected-entry';
    card.append(node('p', 'eyebrow', material.kind + ' · ' + (protectedEntry ? 'Protected course · public entry only' : 'Public source')),
      node('h4', '', material.title), node('p', '', text(material.useNote)));
    const metadata = node('p', 'muted small', 'Source owner: ' + text(material.sourceOwner) + ' · Version: ' + text(material.sourceVersion));
    const label = protectedEntry ? 'View course information / sign in ↗' : material.kind === 'recording' ? 'Open recording source page ↗' : 'Open ' + material.kind + ' source ↗';
    const links = node('div', 'material-links');
    appendLink(links, label, safeLink(material.url));
    card.append(metadata, links, node('p', 'muted small', 'Link checked: ' + text(material.checkedAt) + ' · HTTP ' + String(material.verification?.status || 'unknown') + '. Access and content can change.'));
    if (protectedEntry) card.append(node('p', 'material-boundary', 'This public entry does not provide paid lessons, grant enrollment, or verify your account access.'));
    if (material.kind === 'recording') card.append(node('p', 'material-boundary', 'Opens a separate source tab. Nothing is played here. Keep the source player muted unless you choose to hear it.'));
    return card;
  }
  function renderCatalog() {
    const materials = state.data.materials || [];
    $('materials-catalog').hidden = !materials.length;
    const kind = $('material-kind').value;
    const filtered = materials.filter(material => kind === 'all' || material.kind === kind);
    $('materials-count').textContent = filtered.length + ' of ' + materials.length + ' connected sources';
    $('catalog-materials').replaceChildren(...(filtered.length ? filtered.map(materialCard) : [node('p', 'muted', 'No connected materials of this type yet.')]));
  }
  const practiceFields = { firstAttempt: 'practice-first-attempt', checkNotes: 'practice-check-notes', revisedOutput: 'practice-revised-output', nextStep: 'practice-next-step' };
  const practiceLimits = { firstAttempt: 50000, checkNotes: 30000, revisedOutput: 50000, nextStep: 10000 };
  function copyPracticeProvenance(value) {
    return { sessionVersion: value.sessionVersion, recipeSha256: value.recipeSha256, materials: value.materials.map(ref => ({ id: ref.id, sha256: ref.sha256 })) };
  }
  function currentPracticeProvenance(session) {
    return { sessionVersion: text(session.sourceVersion), recipeSha256: text(session.contentSha256), materials: materialRefs(strings(session.materialIds).map(materialFor).filter(Boolean)) };
  }
  function savePracticeDraft() {
    if (!state.practice) return;
    const draft = {};
    for (const [key, id] of Object.entries(practiceFields)) draft[key] = $(id).value;
    state.practiceDrafts.set(state.practice.id, { draft, warnings: [...state.practiceWarnings], provenance: copyPracticeProvenance(state.practiceProvenance || currentPracticeProvenance(state.practice)) });
  }
  function updatePractice() {
    $('download-practice').disabled = !state.practice || ['firstAttempt', 'checkNotes', 'nextStep'].some(key => !$(practiceFields[key]).value.trim());
    $('practice-source-warning').hidden = !state.practiceWarnings.length;
    $('practice-source-warning').textContent = state.practiceWarnings.join(' ');
    savePracticeDraft();
  }
  function choosePractice(id) {
    savePracticeDraft();
    const session = (state.data.practiceSessions || []).find(item => item.id === id && item.pathId === state.path?.id);
    state.practice = session || null;
    $('practice-detail').hidden = !session;
    $('practice-choice').value = session?.id || '';
    $('practice-message').textContent = '';
    if (!session) return;
    $('practice-title').textContent = session.title;
    $('practice-goal').textContent = session.goal;
    $('practice-context').textContent = 'For: ' + session.audience + ' · ' + session.minutes + ' minutes (planning estimate, not an observed learner duration).';
    $('practice-steps').replaceChildren(...session.steps.map(step => {
      const item = node('li');
      item.append(node('h4', '', text(step.title).replace(/^\d+\.\s+/, '')), node('p', '', step.instruction));
      const links = node('div', 'material-links');
      for (const material of strings(step.materialIds).map(materialFor).filter(Boolean)) appendLink(links, material.title + ' ↗', safeLink(material.url));
      item.append(links);
      return item;
    }));
    $('practice-deliverable').textContent = session.deliverable;
    listInto('practice-checks', strings(session.checks));
    const prior = state.practiceDrafts.get(session.id);
    for (const [key, field] of Object.entries(practiceFields)) $(field).value = prior?.draft[key] || '';
    state.practiceWarnings = [...(prior?.warnings || [])];
    state.practiceProvenance = copyPracticeProvenance(prior?.provenance || currentPracticeProvenance(session));
    $('practice-version').textContent = 'Current recipe version: ' + text(session.sourceVersion) + ' · Record source version: ' + state.practiceProvenance.sessionVersion + '. Downloading keeps the record’s original recipe and material hashes; editing your notes does not certify a recheck.';
    updatePractice();
  }
  function renderPathMaterials() {
    const materials = pathMaterials();
    $('path-materials').replaceChildren(...(materials.length ? materials.map(materialCard) : [node('p', 'muted', 'No additional materials are connected to this path yet. Its public task guides remain available above.')]));
    const sessions = (state.data.practiceSessions || []).filter(session => session.pathId === state.path.id);
    $('practice-section').hidden = !sessions.length;
    const placeholder = node('option', '', 'Choose a complete practice example');
    placeholder.value = '';
    $('practice-choice').replaceChildren(placeholder, ...sessions.map(session => { const option = node('option', '', session.title); option.value = session.id; return option; }));
    choosePractice('');
  }
  function checkMaterialRefs(refs) {
    if (!Array.isArray(refs) || refs.length > 1000) throw new Error('Invalid material references.');
    const ids = new Set();
    for (const ref of refs) {
      if (!ref || typeof ref !== 'object' || Array.isArray(ref) || Object.keys(ref).some(key => !['id', 'sha256'].includes(key)) || typeof ref.id !== 'string' || !ref.id || ref.id.length > 200 || ids.has(ref.id) || (ref.sha256 !== null && (typeof ref.sha256 !== 'string' || !/^[a-f0-9]{64}$/i.test(ref.sha256)))) throw new Error('Invalid material identity or source hash.');
      ids.add(ref.id);
    }
  }
  function materialWarnings(refs, currentIds) {
    const warnings = [];
    for (const ref of refs) {
      const current = materialFor(ref.id);
      if (!current) warnings.push('Material no longer in the current catalog: ' + ref.id + '. No saved link has been used.');
      else if (!currentIds.includes(ref.id)) warnings.push('Material no longer belongs to this current recipe or path: ' + current.title + '. Review the current selection.');
      else if (!ref.sha256 || !text(current.verification?.sha256)) warnings.push('Source revision cannot be compared for ' + current.title + '.');
      else if (ref.sha256 !== current.verification.sha256) warnings.push('Material source changed since this record was saved: ' + current.title + '. Review it again.');
    }
    for (const id of currentIds) if (!refs.some(ref => ref.id === id)) warnings.push('New material in the current recipe or path: ' + (materialFor(id)?.title || id) + '. Review it before teaching.');
    return warnings;
  }
  function downloadJSON(value, filename) {
    const href = URL.createObjectURL(new Blob([JSON.stringify(value, null, 2) + '\n'], { type: 'application/json' }));
    const link = node('a');
    link.href = href;
    link.download = filename;
    document.body.append(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(href), 1000);
  }
  function downloadPractice() {
    updatePractice();
    if ($('download-practice').disabled) return;
    const session = state.practice;
    const savedDraft = state.practiceDrafts.get(session.id);
    downloadJSON({ type: 'task-library-practice', version: 1, sessionId: session.id, ...copyPracticeProvenance(savedDraft.provenance), ...savedDraft.draft }, 'task-library-practice-' + session.id.replace(/[^a-zA-Z0-9_-]/g, '-') + '.json');
    $('practice-message').textContent = 'Practice record downloaded with its original recipe and material hashes. Reopen the downloaded file below to check that your first attempt, check notes, and next step were preserved. Any source-change warnings still apply; this is not a learner certification.';
  }
  async function importPractice(file) {
    if (!file) return;
    try {
      if (file.size > 2 * 1024 * 1024) throw new Error('The practice file is too large.');
      const saved = JSON.parse(await file.text());
      const fields = ['type', 'version', 'sessionId', 'sessionVersion', 'recipeSha256', 'materials', ...Object.keys(practiceFields)];
      if (!saved || typeof saved !== 'object' || Array.isArray(saved) || Object.keys(saved).some(key => !fields.includes(key)) || saved.type !== 'task-library-practice' || saved.version !== 1 || typeof saved.sessionId !== 'string' || saved.sessionId.length > 200 || typeof saved.sessionVersion !== 'string' || saved.sessionVersion.length > 1000 || typeof saved.recipeSha256 !== 'string' || !/^[a-f0-9]{64}$/i.test(saved.recipeSha256)) throw new Error('This is not a supported practice record.');
      for (const [key, limit] of Object.entries(practiceLimits)) if (typeof saved[key] !== 'string' || saved[key].length > limit || (key !== 'revisedOutput' && !saved[key].trim())) throw new Error('Invalid or missing practice field: ' + key + '.');
      checkMaterialRefs(saved.materials);
      const session = (state.data.practiceSessions || []).find(item => item.id === saved.sessionId);
      if (!session) throw new Error('This practice recipe is not available in the current library. Your current work has not been replaced.');
      const warnings = materialWarnings(saved.materials, strings(session.materialIds));
      if (saved.recipeSha256 !== session.contentSha256 || saved.sessionVersion !== session.sourceVersion) warnings.unshift('The practice recipe changed since this record was saved. Your original work is preserved below; compare it with the current steps and checks.');
      savePracticeDraft();
      const draft = Object.fromEntries(Object.keys(practiceFields).map(key => [key, saved[key]]));
      const provenance = copyPracticeProvenance(saved);
      const existing = state.practiceDrafts.get(session.id);
      const hasExistingText = existing && Object.values(existing.draft).some(value => value.trim());
      const differs = existing && (Object.keys(practiceFields).some(key => existing.draft[key] !== draft[key]) || JSON.stringify(existing.provenance) !== JSON.stringify(provenance));
      if (hasExistingText && differs && !window.confirm('Replace the existing text and saved source versions for this practice session with the imported record? Cancel to keep your current draft. Download it first if you want to keep both.')) {
        $('practice-message').textContent = 'Practice import canceled. Your existing draft and its source versions are unchanged.';
        return;
      }
      choosePath(session.pathId);
      state.practiceDrafts.set(session.id, { draft, warnings, provenance });
      choosePractice(session.id);
      $('practice-message').textContent = 'Practice record reopened using the current library recipe and material links. Your first attempt, check notes, revised output, and next step are preserved.';
      $('practice-choice').focus();
    } catch (error) { $('practice-message').textContent = 'Practice not imported: ' + (error instanceof Error ? error.message : 'Invalid practice file.'); }
    finally { $('import-practice').value = ''; }
  }
  function selectedTasks() { return state.rows.filter(slug => state.selected.has(slug)).map(taskFor).filter(Boolean); }
  function sourceStatus(task) {
    return task.status === 'complete' ? 'Contributor-reported complete' : (text(task.status) || 'unknown');
  }
  function isCustomized() {
    return $('session-audience').value.trim() !== text(state.path.audience).trim()
      || $('session-goal').value.trim() !== text(state.path.goal).trim()
      || JSON.stringify(selectedTasks().map(task => task.slug)) !== JSON.stringify(strings(state.path.lessonSlugs));
  }
  function validSession() {
    return state.path && selectedTasks().length > 0 && $('session-audience').value.trim() && $('session-goal').value.trim();
  }
  function listInto(id, items) {
    $(id).replaceChildren(...items.map(value => node('li', '', value)));
  }
  function routeId() { return new URL(window.location.href).searchParams.get('path'); }
  function pathURL(id) {
    const url = new URL(window.location.href);
    url.searchParams.set('path', id);
    return url;
  }
  function choosePath(id, updateRoute = true, moveFocus = false) {
    savePracticeDraft();
    state.practice = null;
    const path = state.data.paths.find(item => item.id === id);
    $('route-message').hidden = true;
    if (!path) {
      state.path = null;
      $('path-detail').hidden = true;
      document.querySelectorAll('.path-choice').forEach(button => button.setAttribute('aria-pressed', 'false'));
      if (id) {
        $('route-message').textContent = 'That teaching path was not found. Choose a path below; no other path has been opened in its place.';
        $('route-message').hidden = false;
      }
      return;
    }
    state.path = path;
    state.sourceWarnings = [];
    state.rows = [...new Set(strings(path.lessonSlugs))];
    state.selected = new Set(state.rows.filter(slug => taskFor(slug)));
    state.minutes = [10, 30, 60].includes(path.sessionMinutes) ? path.sessionMinutes : 30;
    if (updateRoute) window.history.pushState({}, '', pathURL(id));
    $('path-title').textContent = path.title;
    $('path-goal').textContent = text(path.goal);
    $('path-audience').textContent = text(path.audience) || 'Audience not specified in this path.';
    const triangle = text(path.governingTriangle);
    const terms = state.data.framework?.triangles?.[triangle];
    $('path-triangle').textContent = triangle + (Array.isArray(terms) ? ' · ' + terms.join(' → ') : '');
    listInto('path-prerequisites', strings(path.prerequisites).length ? strings(path.prerequisites) : ['No prerequisites listed in this path.']);
    $('path-boundary').textContent = text(path.boundary);
    const framework = state.data.framework || {};
    $('framework-reference').textContent = 'Framework operational version: ' + (text(framework.version) || 'unknown')
      + (text(framework.acceptanceStatus) ? ' · ' + framework.acceptanceStatus : '')
      + (text(framework.decisionDate) ? ' Decision: ' + framework.decisionDate + (text(framework.decisionTimezone) ? ' (' + framework.decisionTimezone + ')' : '') + '.' : '')
      + ' Framework acceptance does not mean these teaching paths are owner-approved.';
    $('session-audience').value = text(path.audience);
    $('session-goal').value = text(path.goal);
    $('session-minutes').value = String(state.minutes);
    $('path-permalink').href = pathURL(id).href;
    $('exercise-prompt').textContent = text(path.exercise?.prompt);
    $('exercise-deliverable').textContent = text(path.exercise?.deliverable);
    listInto('exercise-checks', strings(path.exercise?.checks));
    $('plan-message').textContent = '';
    $('add-message').textContent = '';
    $('lesson-search').value = '';
    document.querySelectorAll('.path-choice').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.path === id)));
    $('path-detail').hidden = false;
    renderLessons();
    renderOptions();
    renderPathMaterials();
    updateSummary();
    if (moveFocus) $('path-title').focus();
  }
  function renderLessons(focusSlug, focusDirection) {
    const cards = state.rows.map((slug, index) => {
      const task = taskFor(slug);
      const card = node('li', 'lesson-card' + (!task ? ' missing-lesson' : ''));
      card.dataset.selected = String(state.selected.has(slug));
      if (!task) {
        card.append(node('h4', '', 'Lesson unavailable: ' + slug), node('p', 'muted', 'This lesson is missing from the current public metadata. It cannot be added to the session.'));
        return card;
      }
      const top = node('div', 'lesson-top');
      const label = node('label', 'lesson-select');
      const input = node('input');
      input.type = 'checkbox';
      input.checked = state.selected.has(slug);
      input.setAttribute('aria-label', 'Include ' + task.title + ' in this session');
      input.addEventListener('change', () => {
        if (input.checked) state.selected.add(slug); else state.selected.delete(slug);
        card.dataset.selected = String(input.checked);
        updateSummary();
      });
      label.append(input, node('span', '', 'Include'));
      const copy = node('div', 'lesson-copy');
      copy.append(node('h4', '', task.title), node('p', '', text(task.description)));
      const meta = node('div', 'lesson-meta');
      appendLink(meta, 'Open task guide ↗', taskLink(task));
      appendLink(meta, 'Read article ↗', safeLink(task.article));
      meta.append(node('span', 'source-status', 'Source status: ' + sourceStatus(task)));
      copy.append(meta);
      top.append(label, copy);
      card.append(top);
      const order = node('div', 'lesson-order');
      for (const [direction, labelText, offset] of [['up', '↑ Up', -1], ['down', '↓ Down', 1]]) {
        const button = node('button', 'order-button', labelText);
        button.type = 'button';
        button.dataset.slug = slug;
        button.dataset.direction = direction;
        button.setAttribute('aria-label', 'Move ' + task.title + ' ' + direction);
        button.disabled = index + offset < 0 || index + offset >= state.rows.length;
        button.addEventListener('click', () => {
          [state.rows[index], state.rows[index + offset]] = [state.rows[index + offset], state.rows[index]];
          renderLessons(slug, direction);
          updateSummary();
          $('plan-message').textContent = task.title + ' moved ' + direction + '.';
        });
        order.append(button);
      }
      card.append(order);
      return card;
    });
    $('lesson-list').replaceChildren(...cards);
    if (focusSlug) {
      const buttons = [...$('lesson-list').querySelectorAll('button')];
      const target = buttons.find(button => button.dataset.slug === focusSlug && button.dataset.direction === focusDirection && !button.disabled)
        || buttons.find(button => button.dataset.slug === focusSlug && !button.disabled);
      if (target) target.focus();
    }
  }
  function renderOptions() {
    const query = $('lesson-search').value.trim().toLowerCase();
    const matches = state.data.tasks.filter(task => !state.rows.includes(task.slug) && (task.title + ' ' + text(task.description)).toLowerCase().includes(query));
    const empty = node('option', '', matches.length ? 'Choose a lesson' : 'No matching lessons to add');
    empty.value = '';
    const options = matches.map(task => {
      const option = node('option', '', task.title);
      option.value = task.slug;
      return option;
    });
    $('lesson-option').replaceChildren(empty, ...options);
    $('add-lesson').disabled = true;
  }
  function updateSummary() {
    const count = selectedTasks().length;
    $('session-summary').textContent = count + ' lesson' + (count === 1 ? '' : 's') + ' selected · ' + state.minutes + '-minute session';
    ['present-session', 'print-session', 'download-session'].forEach(id => { $(id).disabled = !validSession(); });
    if (!count) $('plan-message').textContent = 'Select at least one available public lesson to build a session.';
    else if (!$('session-audience').value.trim() || !$('session-goal').value.trim()) $('plan-message').textContent = 'Enter an audience and intended result before using this plan.';
    else if (/^(Select at least|Enter an audience)/.test($('plan-message').textContent)) $('plan-message').textContent = '';
    $('custom-warning').hidden = !isCustomized();
    $('source-warning').hidden = state.sourceWarnings.length === 0;
    $('source-warning').textContent = state.sourceWarnings.join(' ');
    $('print-session-details').replaceChildren(node('p', '', 'Audience: ' + $('session-audience').value), node('p', '', 'Intended result: ' + $('session-goal').value), node('p', '', 'Planning estimate: ' + state.minutes + ' minutes'));
  }
  function planData() {
    return {
      version: 1,
      pathId: state.path.id,
      pathTitle: state.path.title,
      libraryVersion: state.data.version,
      libraryUpdated: state.data.libraryUpdated,
      frameworkVersion: state.data.framework?.version ?? null,
      frameworkAcceptance: {
        status: text(state.data.framework?.acceptanceStatus) || null,
        decisionDate: text(state.data.framework?.decisionDate) || null,
        decisionTimezone: text(state.data.framework?.decisionTimezone) || null,
        acceptingCommit: text(state.data.framework?.acceptingCommit) || null,
        sourceReference: text(state.data.framework?.sourceReference) || null,
        appliesTo: 'Canonical operational framework only; not approval of these teaching paths.'
      },
      governingTriangle: state.path.governingTriangle,
      audience: $('session-audience').value.trim(),
      goal: $('session-goal').value.trim(),
      sessionMinutes: state.minutes,
      timingBasis: 'Planning estimate; not mastery or certification.',
      accessBoundary: text(state.path.boundary),
      publicOnly: true,
      customized: isCustomized(),
      reviewWarnings: [...(isCustomized() ? ['The original exercise and governing triangle may not fit this customized plan. Review before teaching.'] : []), ...state.sourceWarnings],
      protectedMaterial: 'Paid courses and instructor material remain at their own sources; no access is granted by this plan.',
      materials: materialRefs(pathMaterials()),
      lessons: selectedTasks().map(task => ({ slug: task.slug, title: task.title, contentSha256: text(task.contentSha256) || null, taskLibraryUrl: taskLink(task), article: safeLink(task.article), sourceStatus: sourceStatus(task) })),
      exercise: { prompt: text(state.path.exercise?.prompt), deliverable: text(state.path.exercise?.deliverable), checks: strings(state.path.exercise?.checks) }
    };
  }
  function downloadPlan() {
    if (!validSession()) return;
    const plan = planData();
    const blob = new Blob([JSON.stringify(plan, null, 2) + '\n'], { type: 'application/json' });
    const href = URL.createObjectURL(blob);
    const link = node('a');
    link.href = href;
    link.download = 'task-library-session-' + state.path.id.replace(/[^a-zA-Z0-9_-]/g, '-') + '.json';
    document.body.append(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(href), 1000);
    $('plan-message').textContent = 'Plan downloaded as JSON. It contains public lesson references, not a slide deck or protected course.';
  }
  function startPresentation() {
    if (!validSession()) return;
    if (typeof $('presentation').showModal !== 'function') {
      $('plan-message').textContent = 'This browser does not support presentation mode. Use Print session plan or Download plan JSON.';
      return;
    }
    state.slides = [{ kind: 'overview' }, ...selectedTasks().map(task => ({ kind: 'lesson', task })), { kind: 'exercise' }];
    state.presentationReturn = 'present-session';
    state.slide = 0;
    renderSlide();
    $('presentation').showModal();
    $('exit-presentation').focus();
  }
  function startPracticePresentation() {
    if (!state.practice) return;
    if (typeof $('presentation').showModal !== 'function') {
      $('practice-message').textContent = 'This browser does not support presentation mode. Follow the ordered practice steps on this page.';
      return;
    }
    const recipe = state.practice;
    state.slides = [{ kind: 'practice-overview', recipe }, ...recipe.steps.map(step => ({ kind: 'practice-step', step })), { kind: 'practice-check', recipe }];
    state.presentationReturn = 'present-practice';
    state.slide = 0;
    renderSlide();
    $('presentation').showModal();
    $('exit-presentation').focus();
  }
  function renderSlide() {
    const slide = state.slides[state.slide];
    const content = $('slide-content');
    const title = node('h2');
    title.id = 'slide-title';
    const children = [];
    if (slide.kind === 'practice-overview') {
      title.textContent = slide.recipe.title;
      children.push(node('p', 'eyebrow', 'Complete practice example'), title, node('p', '', slide.recipe.goal), node('p', '', 'For: ' + slide.recipe.audience), node('p', 'muted', slide.recipe.minutes + ' minutes · planning estimate'), node('p', 'boundary', 'Use fictional or already-public inputs. This example is not proof of learner competence or course completion. Keep the original attempt, check the result, then save and reopen the record.'));
      if (state.practiceWarnings.length) children.push(node('p', 'plan-warning small', state.practiceWarnings.join(' ')));
    } else if (slide.kind === 'practice-step') {
      title.textContent = slide.step.title;
      const links = node('div', 'slide-links');
      for (const material of strings(slide.step.materialIds).map(materialFor).filter(Boolean)) appendLink(links, material.title + ' ↗', safeLink(material.url));
      children.push(node('p', 'eyebrow', 'Follow the source · keep your work'), title, node('p', '', slide.step.instruction), links);
    } else if (slide.kind === 'practice-check') {
      title.textContent = 'Check, save, and reopen';
      const checks = node('ul');
      checks.append(...strings(slide.recipe.checks).map(check => node('li', '', check)));
      children.push(node('p', 'eyebrow', 'Practice evidence, not certification'), title, node('p', '', slide.recipe.deliverable), checks, node('p', 'boundary', 'Exit presentation to record your first attempt, check notes, any revision, and one owned next step. Download the practice JSON and reopen that file to verify it was saved.'));
    } else if (slide.kind === 'overview') {
      title.textContent = state.path.title;
      children.push(node('p', 'eyebrow', 'Session overview'), title, node('p', '', $('session-goal').value), node('p', '', 'For: ' + $('session-audience').value), node('p', 'muted', state.minutes + ' minutes · planning estimate'), node('p', 'boundary', text(state.path.boundary)), node('p', 'muted small', 'Public lessons only. This session does not unlock paid courses, reveal instructor material, or certify training.'));
      if (isCustomized()) children.push(node('p', 'plan-warning small', $('custom-warning').textContent));
      if (state.sourceWarnings.length) children.push(node('p', 'plan-warning small', state.sourceWarnings.join(' ')));
    } else if (slide.kind === 'lesson') {
      const task = slide.task;
      title.textContent = task.title;
      const links = node('div', 'slide-links');
      appendLink(links, 'Open task guide ↗', taskLink(task));
      appendLink(links, 'Read article ↗', safeLink(task.article));
      children.push(node('p', 'eyebrow', 'Read the source · try the task · show the result'), title, node('p', '', text(task.description)), node('span', 'source-status', 'Source status: ' + sourceStatus(task) + ' · not learner acceptance or training certification'), links, node('p', 'boundary', 'Follow the maintained guide at its source. This slide is a lesson reference, not a substitute for its steps.'));
    } else {
      title.textContent = 'Practice, then check';
      const checks = node('ul');
      checks.append(...strings(state.path.exercise?.checks).map(check => node('li', '', check)));
      children.push(node('p', 'eyebrow', 'Public path exercise'), title, node('p', '', text(state.path.exercise?.prompt)), node('h3', '', 'Bring back'), node('p', '', text(state.path.exercise?.deliverable)), node('h3', '', 'Check the result'), checks);
      if (isCustomized()) children.push(node('p', 'plan-warning small', $('custom-warning').textContent));
    }
    content.replaceChildren(...children);
    content.scrollTop = 0;
    $('slide-position').textContent = 'Slide ' + (state.slide + 1) + ' of ' + state.slides.length;
    $('previous-slide').disabled = state.slide === 0;
    $('next-slide').disabled = state.slide === state.slides.length - 1;
  }
  function moveSlide(offset) {
    const next = state.slide + offset;
    if (next < 0 || next >= state.slides.length) return;
    state.slide = next;
    renderSlide();
    // Keep focus on a usable control when reaching either end.
    const active = document.activeElement;
    if (active?.disabled) $('exit-presentation').focus();
  }
  async function importPlan(file) {
    if (!file) return;
    try {
      if (file.size > 2 * 1024 * 1024) throw new Error('The plan file is too large.');
      const saved = JSON.parse(await file.text());
      const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
      const allowed = (value, fields) => object(value) && Object.keys(value).every(key => fields.includes(key));
      const shortString = (value, limit) => typeof value === 'string' && value.length <= limit;
      const fields = ['version', 'pathId', 'pathTitle', 'libraryVersion', 'libraryUpdated', 'frameworkVersion', 'frameworkAcceptance', 'governingTriangle', 'audience', 'goal', 'sessionMinutes', 'timingBasis', 'accessBoundary', 'publicOnly', 'customized', 'reviewWarnings', 'protectedMaterial', 'lessons', 'exercise', 'materials'];
      if (!allowed(saved, fields) || saved.version !== 1 || saved.publicOnly !== true || !shortString(saved.pathId, 200) || !shortString(saved.audience, 500) || !saved.audience.trim() || !shortString(saved.goal, 2000) || !saved.goal.trim() || ![10, 30, 60].includes(saved.sessionMinutes) || !Array.isArray(saved.lessons) || !saved.lessons.length || saved.lessons.length > 1000) throw new Error('This is not a supported public session plan.');
      for (const key of ['pathTitle', 'governingTriangle', 'timingBasis', 'accessBoundary', 'protectedMaterial']) if (saved[key] !== undefined && !shortString(saved[key], 10000)) throw new Error('Invalid plan field: ' + key + '.');
      if (saved.libraryVersion !== undefined && !(typeof saved.libraryVersion === 'number' && Number.isFinite(saved.libraryVersion)) && !shortString(saved.libraryVersion, 100)) throw new Error('Invalid library version.');
      for (const key of ['libraryUpdated', 'frameworkVersion']) if (saved[key] !== undefined && saved[key] !== null && !shortString(saved[key], 1000)) throw new Error('Invalid plan field: ' + key + '.');
      if (saved.frameworkAcceptance !== undefined && (!allowed(saved.frameworkAcceptance, ['status', 'decisionDate', 'decisionTimezone', 'acceptingCommit', 'sourceReference', 'appliesTo']) || Object.values(saved.frameworkAcceptance).some(value => value !== null && !shortString(value, 1000)))) throw new Error('Invalid framework provenance.');
      if (saved.customized !== undefined && typeof saved.customized !== 'boolean') throw new Error('Invalid customization flag.');
      if (saved.reviewWarnings !== undefined && (!Array.isArray(saved.reviewWarnings) || saved.reviewWarnings.some(value => !shortString(value, 10000)))) throw new Error('Invalid review warnings.');
      if (saved.exercise !== undefined && (!allowed(saved.exercise, ['prompt', 'deliverable', 'checks']) || !shortString(saved.exercise.prompt, 20000) || !shortString(saved.exercise.deliverable, 20000) || !Array.isArray(saved.exercise.checks) || saved.exercise.checks.some(value => !shortString(value, 10000)))) throw new Error('Invalid exercise fields.');
      if (saved.materials !== undefined) checkMaterialRefs(saved.materials);
      const ids = [];
      for (const lesson of saved.lessons) {
        if (!allowed(lesson, ['slug', 'title', 'contentSha256', 'taskLibraryUrl', 'article', 'sourceStatus']) || !shortString(lesson.slug, 200) || !lesson.slug || (lesson.contentSha256 !== null && lesson.contentSha256 !== undefined && (typeof lesson.contentSha256 !== 'string' || !/^[a-f0-9]{64}$/i.test(lesson.contentSha256)))) throw new Error('Invalid lesson identity or content hash.');
        for (const key of ['title', 'taskLibraryUrl', 'article', 'sourceStatus']) if (lesson[key] !== undefined && lesson[key] !== null && !shortString(lesson[key], 10000)) throw new Error('Invalid lesson field: ' + key + '.');
        if (ids.includes(lesson.slug)) throw new Error('A lesson appears more than once in the saved plan.');
        ids.push(lesson.slug);
      }
      if (!state.data.paths.some(path => path.id === saved.pathId)) throw new Error('The saved path is not in this library. Choose a current path instead.');
      // Resolve every lesson from current metadata. File URLs, exercise, triangle, and boundary are never trusted or fetched.
      choosePath(saved.pathId);
      state.rows = [...ids, ...strings(state.path.lessonSlugs).filter(slug => !ids.includes(slug))];
      state.selected = new Set(ids.filter(slug => taskFor(slug)));
      state.minutes = saved.sessionMinutes;
      $('session-minutes').value = String(state.minutes);
      $('session-audience').value = saved.audience;
      $('session-goal').value = saved.goal;
      for (const lesson of saved.lessons) {
        const current = taskFor(lesson.slug);
        if (!current) state.sourceWarnings.push('Missing from this library: ' + lesson.slug + '. It is not selected.');
        else if (!lesson.contentSha256 || !text(current.contentSha256)) state.sourceWarnings.push('Source revision cannot be compared for ' + current.title + '. Read the current guide before teaching.');
        else if (lesson.contentSha256 !== current.contentSha256) state.sourceWarnings.push('Source changed since this plan was saved: ' + current.title + '. Review the current guide.');
      }
      if (saved.materials !== undefined) state.sourceWarnings.push(...materialWarnings(saved.materials, pathMaterials().map(material => material.id)));
      else if (pathMaterials().length) state.sourceWarnings.push('This older plan did not pin connected materials. Review the current material sources before teaching.');
      renderLessons();
      renderOptions();
      updateSummary();
      $('plan-message').textContent = 'Saved plan reopened using current public lesson metadata. Exercise, triangle, and access boundary come from the current path.';
      $('path-title').focus();
    } catch (error) {
      $('plan-message').textContent = 'Plan not imported: ' + (error instanceof Error ? error.message : 'Invalid plan file.');
    } finally { $('import-session').value = ''; }
  }
  const printable = node('div', 'print-session-details');
  printable.id = 'print-session-details';
  $('session-title').after(printable);
  $('session-minutes').addEventListener('change', () => { state.minutes = Number($('session-minutes').value); updateSummary(); });
  ['session-audience', 'session-goal'].forEach(id => $(id).addEventListener('input', updateSummary));
  $('lesson-search').addEventListener('input', renderOptions);
  $('lesson-option').addEventListener('change', () => { $('add-lesson').disabled = !$('lesson-option').value; });
  $('add-lesson').addEventListener('click', () => {
    const slug = $('lesson-option').value;
    const task = taskFor(slug);
    if (!task || state.rows.includes(slug)) return;
    state.rows.push(slug);
    state.selected.add(slug);
    renderLessons();
    renderOptions();
    updateSummary();
    $('add-message').textContent = task.title + ' added to the end of this session.';
    $('lesson-option').focus();
  });
  $('download-session').addEventListener('click', downloadPlan);
  $('material-kind').addEventListener('change', renderCatalog);
  $('practice-choice').addEventListener('change', () => choosePractice($('practice-choice').value));
  for (const id of Object.values(practiceFields)) $(id).addEventListener('input', updatePractice);
  $('download-practice').addEventListener('click', downloadPractice);
  $('present-practice').addEventListener('click', startPracticePresentation);
  $('import-practice').addEventListener('change', () => importPractice($('import-practice').files[0]));
  $('print-session').addEventListener('click', () => { updateSummary(); if (validSession()) window.print(); });
  $('import-session').addEventListener('change', () => importPlan($('import-session').files[0]));
  $('present-session').addEventListener('click', startPresentation);
  $('exit-presentation').addEventListener('click', () => $('presentation').close());
  $('presentation').addEventListener('close', () => $(state.presentationReturn).focus());
  $('previous-slide').addEventListener('click', () => moveSlide(-1));
  $('next-slide').addEventListener('click', () => moveSlide(1));
  $('presentation').addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey || ['INPUT', 'TEXTAREA', 'SELECT'].includes(event.target.tagName)) return;
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') { event.preventDefault(); moveSlide(event.key === 'ArrowRight' ? 1 : -1); }
  });
  window.addEventListener('popstate', () => { if (state.data) choosePath(routeId(), false); });
  fetch('learning-paths.json', { cache: 'no-cache' })
    .then(response => { if (!response.ok) throw new Error('Metadata unavailable'); return response.json(); })
    .then(data => {
      if (!data || !Array.isArray(data.paths) || !Array.isArray(data.tasks) || !data.paths.length || data.paths.some(path => !text(path.id) || !text(path.title) || !Array.isArray(path.lessonSlugs)) || data.tasks.some(task => !text(task.slug) || !text(task.title))) throw new Error('Invalid metadata');
      if (new Set(data.paths.map(path => path.id)).size !== data.paths.length || new Set(data.tasks.map(task => task.slug)).size !== data.tasks.length) throw new Error('Duplicate metadata');
      if (data.materials !== undefined && (!Array.isArray(data.materials) || data.materials.some(material => !text(material.id) || !text(material.title) || !['deck', 'recording', 'exercise', 'workbook', 'course'].includes(material.kind) || !['public', 'protected-entry'].includes(material.access) || !safeLink(material.url) || !Array.isArray(material.pathIds)) || new Set(data.materials.map(material => material.id)).size !== data.materials.length)) throw new Error('Invalid material metadata');
      if (data.practiceSessions !== undefined && (!Array.isArray(data.practiceSessions) || data.practiceSessions.some(session => !text(session.id) || !text(session.title) || !data.paths.some(path => path.id === session.pathId) || !text(session.sourceVersion) || !/^[a-f0-9]{64}$/i.test(text(session.contentSha256)) || !Array.isArray(session.materialIds) || session.materialIds.some(id => !(data.materials || []).some(material => material.id === id && material.access === 'public')) || !Array.isArray(session.steps) || !session.steps.length || session.steps.some(step => !text(step.title) || !text(step.instruction) || !Array.isArray(step.materialIds) || step.materialIds.some(id => !session.materialIds.includes(id)))) || new Set(data.practiceSessions.map(session => session.id)).size !== data.practiceSessions.length)) throw new Error('Invalid practice recipe metadata');
      state.data = data;
      renderCatalog();
      $('load-state').hidden = true;
      $('library-stamp').textContent = data.libraryUpdated ? 'Library updated: ' + String(data.libraryUpdated) : 'Library update date not supplied';
      $('path-choices').replaceChildren(...data.paths.map((path, index) => {
        const button = node('button', 'path-choice');
        button.type = 'button';
        button.dataset.path = path.id;
        button.setAttribute('aria-pressed', 'false');
        button.append(node('span', 'choice-number', String(index + 1).padStart(2, '0') + ' / PATH'), node('strong', '', path.title), node('small', '', text(path.audience)));
        button.addEventListener('click', () => choosePath(path.id, true, true));
        return button;
      }));
      choosePath(routeId(), false);
    })
    .catch(() => {
      $('load-state').textContent = 'The public lesson list could not be loaded. Reload this page, or browse the public Task Library using the links above. No lesson data has been substituted.';
      $('path-detail').hidden = true;
    });
})();
