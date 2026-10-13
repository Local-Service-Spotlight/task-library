/* Public lesson metadata only. This planner does not fetch protected course material. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const state = { data: null, path: null, rows: [], selected: new Set(), minutes: 30, slides: [], slide: 0, sourceWarnings: [] };
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
    if (slide.kind === 'overview') {
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
      const fields = ['version', 'pathId', 'pathTitle', 'libraryVersion', 'libraryUpdated', 'frameworkVersion', 'frameworkAcceptance', 'governingTriangle', 'audience', 'goal', 'sessionMinutes', 'timingBasis', 'accessBoundary', 'publicOnly', 'customized', 'reviewWarnings', 'protectedMaterial', 'lessons', 'exercise'];
      if (!allowed(saved, fields) || saved.version !== 1 || saved.publicOnly !== true || !shortString(saved.pathId, 200) || !shortString(saved.audience, 500) || !saved.audience.trim() || !shortString(saved.goal, 2000) || !saved.goal.trim() || ![10, 30, 60].includes(saved.sessionMinutes) || !Array.isArray(saved.lessons) || !saved.lessons.length || saved.lessons.length > 1000) throw new Error('This is not a supported public session plan.');
      for (const key of ['pathTitle', 'governingTriangle', 'timingBasis', 'accessBoundary', 'protectedMaterial']) if (saved[key] !== undefined && !shortString(saved[key], 10000)) throw new Error('Invalid plan field: ' + key + '.');
      if (saved.libraryVersion !== undefined && !(typeof saved.libraryVersion === 'number' && Number.isFinite(saved.libraryVersion)) && !shortString(saved.libraryVersion, 100)) throw new Error('Invalid library version.');
      for (const key of ['libraryUpdated', 'frameworkVersion']) if (saved[key] !== undefined && saved[key] !== null && !shortString(saved[key], 1000)) throw new Error('Invalid plan field: ' + key + '.');
      if (saved.frameworkAcceptance !== undefined && (!allowed(saved.frameworkAcceptance, ['status', 'decisionDate', 'decisionTimezone', 'acceptingCommit', 'sourceReference', 'appliesTo']) || Object.values(saved.frameworkAcceptance).some(value => value !== null && !shortString(value, 1000)))) throw new Error('Invalid framework provenance.');
      if (saved.customized !== undefined && typeof saved.customized !== 'boolean') throw new Error('Invalid customization flag.');
      if (saved.reviewWarnings !== undefined && (!Array.isArray(saved.reviewWarnings) || saved.reviewWarnings.some(value => !shortString(value, 10000)))) throw new Error('Invalid review warnings.');
      if (saved.exercise !== undefined && (!allowed(saved.exercise, ['prompt', 'deliverable', 'checks']) || !shortString(saved.exercise.prompt, 20000) || !shortString(saved.exercise.deliverable, 20000) || !Array.isArray(saved.exercise.checks) || saved.exercise.checks.some(value => !shortString(value, 10000)))) throw new Error('Invalid exercise fields.');
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
  $('print-session').addEventListener('click', () => { updateSummary(); if (validSession()) window.print(); });
  $('import-session').addEventListener('change', () => importPlan($('import-session').files[0]));
  $('present-session').addEventListener('click', startPresentation);
  $('exit-presentation').addEventListener('click', () => $('presentation').close());
  $('presentation').addEventListener('close', () => $('present-session').focus());
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
      state.data = data;
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
