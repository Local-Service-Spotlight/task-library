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

The initial release was followed by an embedded-view repair when screenshots showed an off-screen panel. Final verification follows below. They must be recorded before this repair is marked completed. Review coverage, contributor status, actual executions and full task certification stay separate. There are still no fully verified tasks; this repair does not claim otherwise.

## Canonical entry-page correction and embedded-view repair

The public dashboard wrapper also advertised 243 skills and an August ZIP. It now links the maintained all-guides archive, tells readers to open START-HERE.md, supply facts and access, try once, and schedule only when repetition is needed. Dated history is explicitly marked as history. Current setup no longer claims installation in one paste, automatic work, or public release of every run.

Its opening now reads: “Find clear steps for a job that helps your business grow. Pick one guide, give your AI the facts, and check its work. These guides support the Content Factory, which turns your real stories into useful posts, pages, and ads.” This names the task, the value and the explained connection. The linked Content Factory page returned 200 and describes Produce, Process, Post and Promote, with the Task Library as the recipe directory. The linked install page returned 200 and gives a first-result path plus separate product-specific setup. The opening diagram and first-run instructions were inspected at desktop1280x800 and phone390x844. No horizontal overflow or empty visual.

A candidate LSS /system link returned 200 but redirected to an unrelated task. It was corrected to the checked Content Factory destination. A 200 alone does not establish a useful link.

The embedded dialog's DOM-visible state was not sufficient: the parent page scrolled past it when the iframe grew. The app now sends a geometry-only reveal message after open/close and focuses without implicit scrolling. The wrapper trusts only the expected origin and its iframe window, bounds reveal coordinates, preserves scroll after resizing, and avoids overriding a newer reveal. An independent source reviewer examined this follow-up; final judgment includes actual browser coordinates and screenshots. The local phone panel stayed visible after the resize.

WordPress rendered ampersands in inline JavaScript as HTML entities. The wrapper avoids those operators and the six behavior checks run against its actual saved rendered script. They cover untrusted origin/window rejection, invalid coordinates, reveal, resize restoration and a newer reveal arriving before restoration.

Release PR55 merged as `482f6f0db638674101126c2645a71b49322402bf` (deployment37018860516). Embedded app PR56 merged as `58c1553f10e8dc4b6953dbcc6f0fc62fd1d58321` (deployment37020980351). Final app SHA-256: `e028ed1a6b0a63898e962c163a861ea375f9bface22ced62fbb6e0a15da9b802`; anonymous public bytes matched. Final committed source tests:161 build and89 scripts pass; all seven local and downloaded archives pass. The eight new app tests and six rendered-wrapper checks are scoped behavior evidence, not novice setup evidence.

Final saved hub source SHA-256: `dc6de005d58a002e7a9b3cd5073ac1bef30a4743d72d118bc3d2cf4759ffc4e0`. Final saved meta source SHA-256: `a0816a1eb71f6461f9bd61f44ea057921f9f54ab6731e4859e93e3e3211268d5`. On October2 at14:43:54UTC the ordinary anonymous URL served exact final rendered text, media and inline script. The same six script behavior checks pass on those public bytes. Original stale-cache failures are retained in the run evidence.

All task recipe members and START-HERE.md in the seven archives are byte-unchanged from the prior reviewed release. Changed archive metadata is only the build date in README/manifest. This reuses setup-instruction checks, not novice-user success.

Final public browser verification: the normal canonical page loaded the final executable wrapper (no escaped JavaScript operators). Its embedded Step4 guide opened with title and copy controls visible at1280x800 and390x844. Closing returned to the selected row. Final meta section was inspected at both sizes. The result is one completed publishing repair; the next maintenance pass must read the generated queue and select the next missing gate, provisionally internal-linking inventory Step1. No task certification or novice-success gate changes.
