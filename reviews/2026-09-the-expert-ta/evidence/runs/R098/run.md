# Test Run R098 — S7

| | |
|---|---|
| **Run ID** | R098 |
| **Date/time** | 2026-09-11 14:13 |
| **View / sample** | S7 |
| **Page URL / location** | https://login.theexpertta.com/Login.aspx |
| **Task / process** | — |
| **Modality** | cognition |
| **Tool** | probe; inspection (reviewer, 2026-09-24) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-24, every row answered. The page is understandable and predictable to use: navigation and component identification are consistent with the rest of the product, help is where it always is, nothing changes context on focus or input, no time limit or moving content, and no information is demanded twice. Two failures: the product-wide single-route problem (CO10), and the user-name field carrying no `autocomplete` token, so its purpose is not programmatically identified (CO9, 1.3.5, V-F17) — mitigated, as the reviewer records, by Chrome's password manager filling it anyway. Authentication itself passes: no CAPTCHA, puzzle or transcription step, and a password manager is not blocked (CO6, 3.3.8).

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
| CO4 — Errors suggest how to fix the problem | pass | reviewer 2026-09-24: **"it announces the issue successfully"** — a wrong password produces an announced error that identifies the problem |
| CO5 — Previously entered information is not demanded again | pass | reviewer 2026-09-24: **"this has not been encountered"** — nothing in the product asked for information that had already been given earlier in the same process |
| CO6 — Authentication does not require transcription or memorization (no cognitive-function test) | pass | O5 — the reviewer 2026-09-24: authentication was checked as part of the sign-in walk. Signing in needs a username and password, which is a cognitive-function test, but 3.3.8 is satisfied when a mechanism exists to assist — and it does: **"works fine with chrome password manager"** (the reviewer, recorded on O3). Paste and autofill are not blocked, there is no CAPTCHA, puzzle or transcription step, and recovery is an e-mailed link rather than a memory task (S14). The missing `autocomplete` token is a **different** criterion — 1.3.5, V-F17 |
| CO7 — Time limits are adjustable/extendable; moving content can be paused | n/a | reviewer 2026-09-24: **"no timeouts have been encountered in this entire test"**, across five sessions and ten views. The criterion's other half is already measured n/a — nothing on any view animates, moves, blinks or auto-updates (CO12). With neither a time limit nor moving content, there is nothing to adjust or pause |
| CO8 — Focus/input does not trigger unexpected context changes | pass | reviewer 2026-09-24: **"no"** — no unexpected change of context on focus or input anywhere in the review. (The Practice Area's full-page re-render on selection is a *silent* change, not an unexpected one, and is recorded as V-F42 under 4.1.3.) |
| CO9 — Fields collecting the user's own information (name, email, address, phone, …) carry the matching `autocomplete` purpose so browsers and AT can fill them | fail | O3 — 1 personal-data field(s) without autocomplete (measured): text User Name: |
| CO10 — Each view is reachable in more than one way (navigation plus search, site map, index, or related links) unless it is a step in a process | fail | reviewer 2026-09-24: **"there is no site map, the only way to reach the relevant content is through the Class Assignments Table"**. No search, no site map, no index, no A-Z — a single route to every destination in the product |
| CO11 — Submissions with legal, financial, or data-changing consequences are reversible, checked for input errors, or confirmable before commit | n/a | The view has no submission carrying legal, financial or data-changing consequences: its controls select, filter or authenticate. The criterion bites on Take Assignment, where a submission affects the grade, and is answered there |
| CO12 — Nothing flashes more than three times per second (photosensitive-safety check; WCAG-only — no 508 FPC counterpart) | n/a | O4 — no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash |
**view_probe 2026-09-11:** answered CO9=fail, CO12=n/a (CO6 left for the reviewer — this IS the sign-in view) by measurement; facts in `R098-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): 1 personal-data field(s) without autocomplete (measured): text User Name:
  - Classified: CO9 / WCAG 1.3.5 / measured → fail
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash
  - Classified: CO12 / WCAG 2.3.1 / measured → n/a

- O5 [clarified] (state: sign-in page, reviewer 2026-09-24): authentication was covered during the sign-in walk and the row can be answered from it. The sign-in is username plus password with **no CAPTCHA, no puzzle, no transcription step and no second factor**, and the reviewer has already confirmed that **Chrome's password manager fills it** (O3) — so the mechanism 3.3.8 asks for is present and nothing blocks paste or autofill. Account recovery is an e-mailed reset link (S14), which is also not a memory task. The criterion is met even though the field lacks an `autocomplete` token, because that token is what **1.3.5** requires (V-F17), not 3.3.8.
  - Classified: CO6 / WCAG 3.3.8 / pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R098-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
