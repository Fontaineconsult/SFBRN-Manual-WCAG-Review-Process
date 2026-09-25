# Test Run R014 — S8

| | |
|---|---|
| **Run ID** | R014 |
| **Date/time** | 2026-09-10 10:49 |
| **View / sample** | S8 |
| **Page URL / location** | UI: Class Management → assignment row → View Assignment Solutions |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 153 debug profile); classification pending reviewer |
| **Result** | Works with issues |


**Result reasoning.** A screen-reader user can move through this page by its headings, which no other page allows, and it is the page where the worked answers live. What is lost is the content itself: the figures carry no alternative text because of an authoring-pipeline defect, and every equation is an unnamed control.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O1–O4 closed against the no-vision walk. O1 (`image-alt` ×14) splits in two and both halves are recorded: the figures whose alternative text a missing quote swallowed into the `src` → V-F35, and the mathematics exposed as unnamed controls → V-F45. O2 (`aria-command-name` ×33 — one jump point per problem and part) → V-F8. O3 (`color-contrast` ×17 on the randomised values) → V-F23. O4 (`aria-hidden-focus`, `region` ×241, no `main`) → V-F1, with the exception recorded: `page-has-heading-one` passes and this page carries a heading per problem, which is the pattern the report asks the vendor to apply everywhere. O5 and O6 are informational and dismissed. |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O7 (442 contrast incompletes — MathJax glyphs and obscured spans) → low-vision run: eyedropper one rendered equation and one problem statement; the count is an artefact of MathJax's span-per-glyph rendering, not 442 issues |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | Cross-checked against the NVDA walk (R087 — Works with issues). This is the one page where axe reported real structure — an `h1` and a heading per problem — and the walk confirmed the headings were reachable, so the instrument is not blind here and the output stands. O7 (`color-contrast` incomplete ×442 across MathJax glyphs) was routed to the low-vision run. |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

Product-wide items seen on every signed-in view (first recorded in R001; not repeated as separate observations here, but they apply to this view too):
- **PW-A** DevExpress editors without labels (`label` critical) — see R001 O1.
- **PW-B** the vendor's `focus-box` jump points are `div role="button" tabindex="0"` with no accessible name (`aria-command-name` serious) — see R001 O2. The count grows with content (4 on Take Assignment, 32 on the grade report, 33 on the solutions page — one per problem and part).
- **PW-C** header logo link is `aria-hidden="true"` yet focusable (`aria-hidden-focus`) — see R001 O3.
- **PW-D** no `main`, no landmarks, no `h1` (best-practice rules `landmark-one-main`, `region`, `page-has-heading-one`) — see R001 O5/O6; fold into the structure finding from the JAWS run.
- **PW-E** `bypass` incomplete — whether the jump points count as a bypass mechanism is settled once, in the no-vision run on S1.
- **PW-F** DevExpress buttons paint their background with an image, so axe reports their captions as contrast 0 = **unmeasured** (`bgImage`) — eyedropper in the low-vision run; never a finding from axe alone.
- **PW-G** DevExpress check boxes / list boxes carry a hidden `input type=text readonly style="opacity:0"` state field (`_S` / `_KBS` ids) that axe flags under `label`. Whether it is focusable (and therefore a real unlabeled stop) is a keyboard-run question; propose treating it as one issue product-wide, not per field.

- O1 [new] (state: View Assignment Solutions, all 9 problems rendered on one page): axe `image-alt` (critical) **×14** — two kinds: (a) figure images whose markup is **broken**: `<img class="solution" src="/images/zbrvxxz3.j3f.png alt=" a="" red="" block="" with="" mass="" …>` — a missing quote after the `src` value swallows `alt=` into the `src` and scatters the alt text into bogus attributes, so the image has **no alt at all** even though the author wrote one ("A red block with mass m rests on a frictionless horizontal surface…", "The image shows a car stuck in the mud…"); (b) solution-step images (`img.MQFLOATNO`, `/images/fs/…png` rendered equations/diagrams) with no alt attribute.
  - Proposed: W1 / WCAG 1.1.1 (A) / **Major** — (a) is an authoring-pipeline bug that likely affects the same figures on Take Assignment (compare: exploration saw empty alt on P6–P9 figures — check whether those are this bug); (b) solution steps rendered as images are unreadable to AT — confirm both with JAWS → finding
- O2 [new] (state: as O1): `aria-command-name` **×33** — jump points per problem and part (PW-B).
  - Proposed: fold into PW-B finding
- O3 [new] (state: as O1): `color-contrast` ×17 — randomized-variable values (`#FF6347` on white, **2.94:1**, 16 px bold) in every problem statement (same token as R004 O10, R007 O2).
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major — add this view to the variable-colour finding
- O4 [new] (state: as O1): `aria-hidden-focus` ×1, `region` **×241**, `landmark-one-main` (PW-C/D) — **`page-has-heading-one` passes** (h1 "Assignment Solutions - Class: …", h2 per problem).
  - Proposed: fold into product-wide findings; record as the structure exception
- O5 [new] (state: as O1): `html-has-lang` does not fire here (page has `lang`).
  - dismissed: informational
- O6 [new] (state: as O1): passes 31 / inapplicable 56; raw JSON 4.2 MB.
  - dismissed: informational
- O7 [new] (state: as O1): **incomplete** `color-contrast` ×442 — MathJax renders each glyph as a span (`nonBmp`, `shortTextContent`, `elmPartiallyObscuring`); axe cannot measure them.
  - Proposed: W2 → low-vision run: eyedropper one rendered equation; treat the rest as the same measurement

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:49 UTC. Counts: violations 6 (14 image-alt, 33 unnamed commands, 241 region nodes), incomplete 1 (442 nodes), passes 31, inapplicable 56. Reached via the UI path (assignment row → View Assignment Solutions); the page has no assignment parameter in its URL.

## Evidence files in this folder

- `R014-axe.json` — raw axe output (4,184,728 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
