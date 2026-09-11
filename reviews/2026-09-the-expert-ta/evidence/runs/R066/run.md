# Test Run R066 — R1

| | |
|---|---|
| **Run ID** | R066 |
| **Date/time** | 2026-09-11 14:09 |
| **View / sample** | R1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Instructor/AcademicIntegrityTemplates.aspx |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — LV2, LV4, LV5, LV6, LV7, LV9 need the reviewer (zoom, B3); measured fail on LV1 awaits confirmation |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; tr right=1300; td right=1300; div#TemplateMenu1_divUserMenu right=1300 (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | | |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | | |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | | |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | | |
| LV7 — Focus indicator remains visible and unobscured at zoom | | |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (33 inline + 45 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | | |

**view_probe 2026-09-11:** answered LV1=fail, LV3=pass, LV8=pass by measurement; facts in `R066-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; tr right=1300; td right=1300; div#TemplateMenu1_divUserMenu right=1300 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (33 inline + 45 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R066-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
