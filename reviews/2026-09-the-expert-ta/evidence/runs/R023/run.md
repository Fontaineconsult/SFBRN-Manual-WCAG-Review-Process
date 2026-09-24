# Test Run R023 — S1

| | |
|---|---|
| **Run ID** | R023 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default.aspx |
| **Task / process** | — |
| **Modality** | cognition |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — CO1, CO2, CO3, CO4, CO5, CO7, CO8, CO10, CO11 need the reviewer (inspection) |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (cognition)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| CO1 — Navigation and component identification are consistent with the rest of the product | pass | reviewer 2026-09-24: **"main navigation remains consistent"** — the top menu is in the same place and the same order on every view, and components that do the same job are identified the same way across the product |
| CO2 — Help (if offered) appears in a consistent location | pass | reviewer 2026-09-24: **"help is in the main nav"** — the Help link sits in the top menu on every view, in the same position |
| CO3 — Labels and instructions make the required input clear | pass | reviewer 2026-09-24: **"labels are clear"**. This is the *visible* labelling question and it passes: a sighted user can see what each field wants. The product's labelling defects are programmatic — the label is not associated with the field (V-F7, V-F30) — and are recorded under NV6 and 1.3.1, not here |
| CO4 — Errors suggest how to fix the problem | n/a | The view has **no validated input**, so there is no error for which a correction could be suggested (NV12 n/a on this view, established on the no-vision walk). Where errors *do* occur — Take Assignment, Sign in, Password reset — the row is answered on those runs |
| CO5 — Previously entered information is not demanded again | pass | reviewer 2026-09-24: **"this has not been encountered"** — nothing in the product asked for information that had already been given earlier in the same process |
| CO6 — Authentication does not require transcription or memorization (no cognitive-function test) | n/a | O2 — no password/authentication field on the view |
| CO7 — Time limits are adjustable/extendable; moving content can be paused | n/a | reviewer 2026-09-24: **"no timeouts have been encountered in this entire test"**, across five sessions and ten views. The criterion's other half is already measured n/a — nothing on any view animates, moves, blinks or auto-updates (CO12). With neither a time limit nor moving content, there is nothing to adjust or pause |
| CO8 — Focus/input does not trigger unexpected context changes | pass | reviewer 2026-09-24: **"no"** — no unexpected change of context on focus or input anywhere in the review. (The Practice Area's full-page re-render on selection is a *silent* change, not an unexpected one, and is recorded as V-F42 under 4.1.3.) |
| CO9 — Fields collecting the user's own information (name, email, address, phone, …) carry the matching `autocomplete` purpose so browsers and AT can fill them | n/a | O3 — no field collects the user's own information (name/email/phone/address/… not present) |
| CO10 — Each view is reachable in more than one way (navigation plus search, site map, index, or related links) unless it is a step in a process | fail | reviewer 2026-09-24: **"there is no site map, the only way to reach the relevant content is through the Class Assignments Table"**. No search, no site map, no index, no A-Z — a single route to every destination in the product |
| CO11 — Submissions with legal, financial, or data-changing consequences are reversible, checked for input errors, or confirmable before commit | n/a | The view has no submission carrying legal, financial or data-changing consequences: its controls select, filter or authenticate. The criterion bites on Take Assignment, where a submission affects the grade, and is answered there |
| CO12 — Nothing flashes more than three times per second (photosensitive-safety check; WCAG-only — no 508 FPC counterpart) | n/a | O4 — no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash |
**view_probe 2026-09-11:** answered CO6=n/a, CO9=n/a, CO12=n/a by measurement; facts in `R023-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no password/authentication field on the view
  - Classified: CO6 / WCAG 3.3.8 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): no field collects the user's own information (name/email/phone/address/… not present)
  - Classified: CO9 / WCAG 1.3.5 / measured → n/a
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash
  - Classified: CO12 / WCAG 2.3.1 / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R023-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
