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

Final source, browser, public release and archive results are appended only after they are observed. Existing task verification gates and past run history remain separate and unchanged.

## Next use

The operator of the next already-authorized task still needs to save its inputs, exact recipe, checked output and receiving handoff. This repair removes a navigation obstacle; it does not supply that person's setup or task acceptance evidence.

Candidate evidence: five phone/desktop timing cases, each opened twice, passed viewport, inner-body scrolling and close-to-row checks. The delayed-height fixture changes only the existing report delay from 150 to 800 milliseconds; it is a controlled test, not an ordinary production session. The repeatable browser check is `scripts/check_embedded_reveal.cjs`; run with Playwright available and `candidate` or `public`. Public deployment and separate direct-view acceptance remain pending.
