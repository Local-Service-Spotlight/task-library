# Keep an opened guide on the screen

This repair helps people open a task guide and reach its first steps. It keeps a page scroll from hiding the controls they need. The [Task Library](https://blitzmetrics.com/task-library-dashboard/) uses these controls to help a team choose one job before doing work in the [Content Factory](https://blitzmetrics.com/content-factory/).

Date: October 10, 2026. Scope: the shared guide viewer, with one publishing maintenance attempt. This is an agent browser test, not a new user's first completed task.

## Existing opening and useful connection

The public entrance still says:

> Find clear steps for a job that helps your business grow. Pick one guide, give your AI the facts, and check its work. These guides support the Content Factory, which turns your real stories into useful posts, pages, and ads.

It explains what to do, the business purpose and how the guide connects to turning real stories into content. The linked Content Factory destination was read on October 10: it explains turning one real recording into posts and guides through Produce, Process, Post and Promote; its body describes task inputs and receiving handoffs. This supports the stated connection. Some older body branding remains outside this scoped repair. The opening, four-step visual, task instructions, download contents and public wrapper source are unchanged by this runtime fix.

## What failed and why

An ordinary phone test reproduced a Copy button at screen y=-2157.515625, outside the viewport. A controlled test that delayed the existing frame-height report from 150 to 800 milliseconds produced the same result. The embedded frame retained 2200 pixels of internal scroll. The viewer added that scroll offset to a position already measured relative to the embedded viewport, then the parent added the frame's position. This counted internal scroll twice.

The fix sends the viewport-relative position, resets residual inner-frame scrolling when opening or closing a guide, and recalculates the opened panel position after the frame resizes. Embedded panels also skip their entrance transform so the first reveal uses the final position; otherwise a later height report causes a second 19-pixel adjustment. It preserves the parent origin/source checks, all guide content and ordinary top-level behavior. It does not infer an install, account connection or scheduled job from a visible button.

## Acceptance checks

The controlled failing case must pass with the candidate. Phone and desktop tests cover ordinary and delayed frame heights, two openings, return to the same row after closing, and reading within the guide without moving the outside page. Both Copy guide and Copy first-run prompt must be inside the actual viewport. Actual images are inspected with media muted and volume zero. Direct, unembedded viewing is checked separately.

The final source, browser, public release and archive results below were observed after publication. Existing task verification gates and past run history remain separate and unchanged.

## Next use

The operator of the next already-authorized task still needs to save its inputs, exact recipe, checked output and receiving handoff. This repair removes a navigation obstacle; it does not supply that person's setup or task acceptance evidence.

Candidate evidence: five phone/desktop timing cases, each opened twice, passed viewport, inner-body scrolling and close-to-row checks. The delayed-height fixture changes only the existing report delay from 150 to 800 milliseconds; it is a controlled test, not an ordinary production session. The repeatable browser check is `scripts/check_embedded_reveal.cjs`; run with Playwright available and `candidate` or `public`. The release and direct-view acceptance results are recorded below.

## Observed public release

Source PR81 merged as `8cea393817d411734cbc485a24b30e92a19ccea0`; deployment `38055302328` succeeded. Anonymous `app.js` exactly matches reviewed SHA-256 `4cc78165b5bcab5d565928923b6d1fc8691cb447777509495f78e08cbc66c8ce`. All six runtime projections agree with committed sources, excluding only generated build timestamps. The committed files passed 176 tests. Seven public archives passed; guide and setup payloads are unchanged, with only dated snapshot metadata regenerated.

Ordinary public phone and desktop tests and the controlled slow-height cases passed all 30 open/read/close gates. A separate reviewer also tested delayed close/reopen and standalone phone/desktop views. Media stayed muted or blocked. This checks visibility and navigation, not clipboard transfer, account access, human setup or task execution.

The unchanged WordPress outer source and its anonymous text, media and inline scripts match. The saved maintenance section has SHA-256 `079a562432cbb4eb9259ce9bc405f3c63e6b89bc05aef59c2ce197f9c255027d` for its full article source; ordinary anonymous content matches, and the section's phone/desktop visual fits with no horizontal overflow. Independent review accepted this narrow observed public release. Twenty guides pass written standards; zero tasks are fully verified.

The actual public lesson opens: “We fixed a scroll error that could hide an opened guide. Now its first-step buttons stay in view when the page grows. This helps you start one job in the Task Library, where you choose a guide and check the work.” Its maintained Task Library link was checked through the actual outer page. The body explains the cause, repair, checked states and limits, delivering that specific promise.
