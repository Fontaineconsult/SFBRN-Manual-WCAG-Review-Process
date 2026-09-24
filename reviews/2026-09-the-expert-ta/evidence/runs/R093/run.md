# Test Run R093 — S7

| | |
|---|---|
| **Run ID** | R093 |
| **Date/time** | 2026-09-11 14:13 |
| **View / sample** | S7 |
| **Page URL / location** | https://login.theexpertta.com/Login.aspx |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | probe; nvda (reviewer, W63/W76) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-24, every row answered. The task this page exists for — sign in, and be told when you get it wrong — works without sight: the field is properly labelled and a wrong password produces an announced error. What does not work is structural: no headings or landmarks (V-F1) and an unnamed link that leaves the product (V-F43). Works with issues.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Expert TA - Login" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O5 — measured 2026-09-24: **0 headings and 0 landmarks** on the view. "Welcome to Expert TA!" is a `<font size=8>` inside `<strong>` and "Log In" is a styled `div`; neither is a heading → V-F1 |
| NV3 — Every control announces an accurate name, role, and value/state | pass | O6 — reviewer 2026-09-24: "they are both accessible, just not best practice, we can pass them". The submit control carries `value="Next"` and the field is labelled (NV6) |
| NV4 — Images announce appropriate alternatives; decorative images are silent | fail | O7 — the logo is an `<img>` with **no `alt` attribute** inside a link, and neither is `aria-hidden` (measured). It is the page's only image → V-F43 |
| NV5 — Reading order matches the meaning of the visual order | pass | O6 — covered by the reviewer's ruling; the page is a caption, a field, a button and two sentences |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | pass | O6, O8 — measured: `#MainContent_UserName` carries a real `<label for=…>` reading "User Name:". This page does it correctly, which is what makes the reset page's omission an oversight (V-F30) |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | n/a | O8 — the view has no update that happens without a navigation: submitting posts back and the page reloads. The dynamic-update question does not arise here |
| NV8 — Nothing is conveyed only by visual position, shape, or size | pass | O6 — covered by the reviewer's ruling; nothing is identified by position alone |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | fail | O4 — <html> has no lang attribute (measured — 3.1.1) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | fail | O7 — measured: 7 links, of which **one has no accessible name at all** — the logo link, an image with no `alt`, not `aria-hidden`. The other six name themselves → V-F43 |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | pass | O8 — reviewer 2026-09-24: **"error is announced on wrong password"**. Recorded with the mechanism, which matters: the page carries **zero live regions**, so the error is heard because submitting causes a **full postback** and the screen reader reads the reloaded page. It works, but nothing is wired to announce it |
**view_probe 2026-09-11:** answered NV11=n/a, NV1=pass, NV9=fail by measurement; facts in `R093-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): document.title = "Expert TA - Login" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): <html> has no lang attribute (measured — 3.1.1)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → fail

- O5 [measured] (state: sign-in page as loaded, signed-out profile, 2026-09-24): **0 headings and 0 landmarks.** The page's two visual titles are a `<font size="8">` inside `<strong>` and a styled `div`, so neither carries heading semantics. Same pattern as the rest of the product (V-F1), on a page of six visible elements where it costs least to fix.
  - Classified: NV2 / WCAG 1.3.1 / → V-F1
- O6 [clarified] (state: as O5, reviewer 2026-09-24 — step W63): **"they are both accessible, just not best practice, we can pass them."** Recorded as a pass on NV3, NV5 and NV8 for this view, as for the reset page.
  - Classified: NV3, NV5, NV8 / pass
- O7 [measured] (state: as O5): the view has **7 links and one of them has no accessible name at all** — `<a href="http://theexpertta.com/"><img src="/images/loginlogo.png" …>` with no `alt`, no `aria-label`, no `title` and **no `aria-hidden`**. The other six name themselves. It is also the page's only image.
  - Classified: NV4, NV10 / WCAG 1.1.1, 2.4.4, 4.1.2 / Minor → **V-F43**
- O8 [clarified + measured] (state: as O5, wrong password submitted, reviewer 2026-09-24): **"error is announced on wrong password."** NV12 passes — and the mechanism is worth recording because it is not what it looks like. The page has **zero `aria-live`, `role=status` or `role=alert` regions**, and its required-field marker (`title="User Name is required."`) is `visibility:hidden`, so it is hidden from everyone. What actually happens is a **full postback**: the page reloads with the error text in it and the screen reader reads the new page. The outcome is correct and the mechanism is incidental — an inline validation on this page would be silent, exactly as the Calendar's and Practice Area's updates are (V-F40, V-F42). Measured: `#MainContent_UserName` also carries a real `<label for>`, so NV6 passes here.
  - Classified: NV12 / WCAG 3.3.1 / pass; NV6 / pass; NV7 / n/a (nothing updates without a navigation)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R093-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
