# Shared task links open the right guide

A shared link should take a business owner straight to the steps they need. This repair reduces searching before a first run. It supports the [skill publishing process](https://blitzmetrics.com/skill-publishing-standard/), which checks that a saved recipe is usable where readers receive it.

## Exact scope and source

Execution `task-direct-open-20261002-1404` started at 2026-10-02T14:04:50.931255Z. Base: `b8c62c3436e3774ec3c5694dc6474d3dd7231d6f`. Maintained app `dashboard/app.js` SHA-256: `61607abc67bb757c62c3e3aa6092b0978e885d4cf154fb8b98e406fdbdfbd11b`. This is one publishing usability repair, not a customer job or proof that another task has worked.

The current generated queue selected the publisher and exposed Step 4 as a useful affected guide. No article or task certification gate is promoted by this repair.

## Behavior and review

A direct task URL previously used full-text search: the Step 4 slug matched six guides. It now selects the exact slug, clears incompatible filters and opens the guide with its first-run controls. Closing returns focus to its row. Typing a new search or selecting an article hub resumes ordinary browsing. Unknown names show a message and do not open another guide.

Standalone factory-layer start/end markers no longer appear as reading-view paragraphs. Code examples, inline examples, raw files, copied guides and first-run prompt source remain intact. The useful Content Factory diagram and explanation remain visible.

Seven regression checks cover these behaviors. The pre-fix app fails the exact-route negative control. A separate Codex reviewer using GPT-6 Luna inspected the final app and tests and found no scoped defect; the primary agent owns actual test and browser verification. Local desktop (1280 x 800) and phone (390 x 844) previews showed the right title, copy controls and diagram with no horizontal overflow. Closing restored focus and body scrolling; typing the same slug restored six full-text matches.

## Editorial review of actual words

The new meta section opens: “A shared task link should take you straight to the steps you need. We fixed the Task Library so business owners can open one guide and find its first-run prompt with less searching. This supports the skill publishing process, which checks that a saved recipe is usable where readers receive it.” The first sentence names the job, the second explains value, and the third explains the linked prerequisite/process. The body describes exact selection, normal search, marker handling and checks; it does not promise automatic execution. The named publishing destination is the maintained recipe read for this run.

README now says: “The dashboard accepts a permanent `?task=<slug>` query and opens that exact guide with its first-run controls. Closing the guide returns focus to its task row. Typing a new search or choosing an article hub returns to ordinary browsing; an unknown task name shows a message without opening a different guide.” Behavior tests and browser checks support those words.

[Public run record](https://blitzmetrics.com/making-task-guides-easier-to-use/#task-direct-open-20261002-1404). Saved WordPress source and metadata matched exactly; the anonymous normal URL returned 200 with all rendered text and matching media on 2026-10-02T14:13:27Z. Raw source SHA-256: `4515a1ac40a4ad92c7214613a989d41a00d57215c8732d96f401b9f902b07254`.

## Release gate

Public app deployment, final suites, archives and embedded-dashboard verification are pending at this commit. They must be recorded before this repair is marked completed. Review coverage, contributor status, actual executions and full task certification stay separate. There are still no fully verified tasks; this repair does not claim otherwise.
