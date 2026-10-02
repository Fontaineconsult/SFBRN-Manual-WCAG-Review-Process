# Test Run R019 — S3

| | |
|---|---|
| **Run ID** | R019 |
| **Date/time** | 2026-09-30 14:07 |
| **View / sample** | S3 |
| **Page URL / location** | https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123 — `UI: My Courses → Start course → 1 Intro to the Course → Icebreaker` (video lesson); Classic experience |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | keyboard (probe measurements kept: MO9, MO10) |
| **Baseline** | B2 |
| **Tester** | assistant (automated walk); reviewer confirms MO2/MO4 — assistant records |
| **Result** | Not set — MO1, MO2, MO3, MO4, MO5, MO6, MO7, MO8, MO11 need the reviewer (keyboard, B2); measured fail on MO9 awaits confirmation |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | pass | O4 — every interactive element is a Tab stop: outline section and lesson buttons, the video and its control bar, Transcript, Complete & continue, plus the header walked on S2 — assistant walk, working result |
| MO2 — Every reached element can be operated (activate, select, dismiss) | | |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | pass | O6, O4 — no trap: Tab leaves the video's control bar and the page; the lesson drawer and disclosures toggle and release focus |
| MO4 — A visible focus indicator exists at all times | | |
| MO5 — Focus order follows the meaning and operation order of the view | pass | O4 — outline (top to bottom) → lesson body (video → transcript → complete) matches the visual/operational order |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | O7 — no single-character shortcuts (measured) |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | n/a | O8 — no drag or gesture; the seek bar is a native slider |
| MO8 — Pointer actions can be cancelled (up-event activation) | pass | O8 — native controls — up-event activation |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | fail | O2 — 1 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): a.sr-only.rounded-md "Skip to main content" 32×16 px next to a.rounded.px-2 "My Courses" |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (4 inline + 11 external scripts scanned) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | pass | O8 — skip link is the first Tab stop of the page header (S2 R013 O4); the lesson drawer can also be hidden with "Hide lessons" |

**view_probe 2026-09-30:** answered MO9=fail, MO10=n/a by measurement; facts in `R019-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): 1 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): a.sr-only.rounded-md "Skip to main content" 32×16 px next to a.rounded.px-2 "My Courses"
  - Classified: MO9 / WCAG 2.5.8 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): no devicemotion/deviceorientation use in scripts (4 inline + 11 external scripts scanned)
  - Classified: MO10 / WCAG 2.5.4 / measured → n/a
- O4 [new] (state: course player on Icebreaker, 1280×1000, real Tab key events with focus emulation (two walks: one from the lesson body, one after reload)): Stops observed: the course outline's section buttons ("2 What is AI? 0/8 lessons" … aria-expanded) and lesson buttons (e.g. "How AI is Changing the Way Students Learn 0m"), then the native **video** (three Tab stops: the element, then its user-agent control bar), the **Transcript** disclosure (`summary`), and **"Complete & continue"** (never activated), then browser chrome. The header (My Courses / Certificates / Profile / avatar), "My Courses" back link, "Hide lessons" and the section-1 buttons precede the start point and were not re-walked — they are the S2 header already walked. **After a reload the sequential-focus start point sits on the current lesson's outline button** (the first Tab lands on the next lesson), i.e. the app places focus on the current lesson on load — the NVDA walk should confirm what is announced on load.
- O5 [new] (state: same walks, screenshots R019-walk*.png / R019-tab*.png): Visible lilac outline (rgb(201,168,236) ≈ 1.3 px at this scale) on every outline button, the video element, the Transcript summary and the Complete button; inside the native control bar the user agent draws its own focus ring.
- O6 [new] (state: Space / Enter dispatched on focused controls): **Space** on a collapsed section button expands it (aria-expanded false → true) and collapses it again; **Space** opens and closes the Transcript disclosure (R019-transcript-open.png); **Space** on "Hide lessons" removes the outline from the DOM and the button becomes "Lessons" (aria-expanded false; R019-lessons-hidden.png), Space again restores it. **Space** on the focused video starts playback (user-agent behaviour) — paused again immediately. **Enter on a lesson button did not change the lesson** in automation (h1 stayed "Icebreaker"), while a pointer click does; on S2 the same synthetic-Enter limitation turned out to be an automation artefact (the reviewer's Enter worked). **Reviewer confirms with a physical keyboard that Enter/Space on a lesson button opens that lesson (MO2 — KEY).**
- O7 [new] (state: focus on body, letters s l h n / ? k j dispatched): No single-character shortcut: URL, text, DOM and current lesson unchanged; the video stayed paused (no j/k/space hijack).
- O8 [new] (state: inspection): Controls are native buttons, a native `<video controls>`, a native `<details>` and links; nothing draggable; no gesture. The skip link is first in the header (S2 walk). No pointer-only control was found: the video's seek bar is a user-agent slider operable with arrows inside the control bar.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02 (keyboard, Chrome automation).** Method as S1/S2. Left for the reviewer: **MO2** — Enter/Space on a lesson button opens the lesson (synthetic Enter did not; pointer does) and the native video controls operate with Space/arrows; **MO4** — ring presence observed at every stop. **Probe caveat (MO9):** the measured fail names the visually-hidden skip link (same artefact as S2 — fixed in the probe 2026-09-30); all visible targets ≥ 24 px or spacing-exempt. Evidence: `R019-walk01…10.png`, `R019-tab01…05.png`, `R019-transcript-open.png`, `R019-lessons-hidden.png`.

**Assistant, 2026-09-30 (probe caveat).** The MO9 measured fail names the "Skip to main content" link, which is a visually-hidden skip link (`sr-only`, shown only while focused). While hidden it is not a pointer target, so 2.5.8 does not apply to it in that state; while focused it is a keyboard stop. The probe measured it because its visibility test did not exclude clipped/off-screen elements (fixed in `view_probe.py` the same day). Reviewer decides when closing this run: expect n/a or pass unless the focused link itself is under 24×24 px and clashes.

## Evidence files in this folder

- (screenshots/exports named R019-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
