# Teach from one maintained library

Use these paths when you teach a group and need a clear starting point. Choose
the result, adapt the lesson list, then check what learners make. The paths
reference the same Task Library guides used for real work.

## What is connected

`build/packs.json` owns the existing skill packs and the new `learningPaths`
metadata. The registry and source repositories still own the task recipes.
`build/learning_paths.py` resolves path slugs against the current library build,
preserves contributor status, pins the content hashes, and emits an allowlisted
`dashboard/learning-paths.json` projection. Missing lessons fail the build.

`dashboard/training.html?path=<id>` opens one starting path. It is a noindex
teaching utility inside the existing Task Library runtime—not a competing
SEO hub or a new learning-management system. The public canonical entry remains
https://blitzmetrics.com/task-library-dashboard/.

The five initial paths cover preparing an agent workflow, Content Factory, ad review,
team operations and agency leadership. They are **suggested teaching sequences**,
not newly certified prerequisites, accredited courses, accepted conference cuts,
or a claim that every guide is complete.

## How to teach

1. Choose a path and read its actual source guides before class.
2. Set the audience and intended result. Select, add and reorder public guide
   references to fit that goal; a custom lesson does not automatically fit the
   original exercise.
3. Choose a planning time, not a promised completion time. Preserve practice and
   checking time. Short sessions may need fewer lessons.
4. Use browser presentation mode to introduce each guide and open its maintained
   recipe when teaching the work. This is a source-linked teaching outline, not
   an editable PowerPoint or a replacement for the complete lesson.
5. Save the session-plan JSON with the exact guide hashes. Reopen it in the planner
   to resolve current sources and see changed or missing guide warnings. Imported
   URLs and exercise text are never fetched or substituted for current sources.
   Source links open separately so they do not discard your session. Print the plan if useful.
   A saved plan records intended teaching; it is not a record of attendance,
   competence, installation or execution.
6. In actual practice use the existing execution ledger. Learn means explaining
   the method; Do needs checked work; Teach needs another learner's checked result.
   Proposed improvements return to the owning recipe once, through review.

## Nine Triangles application

The exact labels use accepted operational version **2026-08-06**, as documented
in the maintained `nine-triangles/references/canonical-framework.md` skill.
Acceptance status: **Accepted by framework owner Dennis Yu.** Decision date:
**2026-08-09** (`America/Los_Angeles`), accepting commit
`3a82b85071e47a9e4ee336cec854d3e004ff0c5f`. This acceptance is for the operational
framework, not a separate approval of these suggested teaching paths.
The public explanation is
https://blitzmetrics.com/9-triangles-framework-scalable-home-service-businesses/.

- **GCT — Goals, Content, Targeting:** each path names the result, source and audience.
- **CCS — Content, Checklist, Software:** maintain the lesson and check before automation.
- **LDT — Learn, Do, Teach:** viewing a lesson is not proof of doing or teaching it.
- **MAA — Metrics, Analysis, Action:** use observed results to improve the owning source.
- **CID — Communicate, Iterate, Delegate:** operations practice has scope, early review and a checked handoff.
- **MOF — Marketing, Operations, Finance:** agency decisions consider all three functions.

Each path chooses one governing triangle. This is a teaching application of the
accepted framework, not a new reconstruction or a demand to force all nine
triangles onto every lesson. SBP, AEC and DDD remain available in the versioned
reference without invented path mappings.

## Public and protected material

Dennis chose public paths and public lessons with protected course material.
This release projects only existing public task metadata plus public path briefs.
It does not read private workshop inventories, lead rows, paid lessons,
instructor keys or offline packs. Browser presentation mode has no privileged
instructor view. It is safe to share only because it carries public metadata.

Protected materials stay at their existing authorized source. Hiding a field in
CSS or JavaScript is not access control. Do not add paid/instructor contents,
private URLs, tokens, or client examples to this public repository or its JSON.
A future protected viewer must use the existing authentication and permission
boundary before fetching its files, never a public bundle with hidden answers.

## Register existing workshop and presentation assets next

Keep the existing master and paired participant/instructor release workflow.
Before attaching an existing deck, recording, exercise or course segment, resolve:

- canonical owner/source revision and exact asset hash;
- permitted audience and public/protected access tier, rights and reusable scope;
- exact lesson/task references, prerequisites, learning output and pass checks;
- participant versus instructor/offline role, slide/page range and companion pair;
- current route, download, reading order, desktop/phone and media checks;
- whether the source owner accepted cross-audience reuse.

An old public download, internal review, or organizer approval is not current
cross-audience permission or curriculum adoption. Held conference review decks
are not exposed here. Adding these assets is unfinished consolidation work,
not something the five paths silently complete.

## Tests and release

Run `python3 -m unittest discover -s build -p "test_*.py"` and the normal
`build/build.py` + `build/build-packs.py` pipeline. Recheck the public
projection for private content, all five deep links, unknown path handling,
lesson selection/reordering, custom audience/goal, plan download and browser
presentation controls. Inspect at desktop and phone widths with sound muted.
Merge only the reviewed exact change through the existing release workflow.
A merged commit is not a successful Pages deployment; open the live result.

With Playwright already available, run the portable browser regression:
`node scripts/check_training_ui.cjs <training.html URL> [evidence directory]`.
It checks desktop/phone layout, every path, a simulated deployed subpath,
actual plan download/reopen, untrusted imported links, print and keyboard/focus
controls. It mutes audio and permits only the chosen origin; it does not submit
forms or certify remote article content, screen-reader use or physical printing.

Rollback is a reviewed revert of the feature commit. No access grants, course
migration, ad spend or scheduler changes are part of this feature.
