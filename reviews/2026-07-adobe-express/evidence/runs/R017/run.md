# Test Run R017 — S4

| | |
|---|---|
| **Run ID** | R017 |
| **Date/time** | 2026-08-10 16:15 |
| **View / sample** | S4 |
| **Page URL / location** | https://new.express.adobe.com/your-stuff/files/recent?filter=express |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | — |
| **Result** | Works with issues |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | partial | O1–O3 attributed to existing findings; O4 (checkbox labels) is a **candidate needing the S4 no-vision run** |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | O5 — same shared-header `aria-controls` items as S1/S2/S3; 9 contrast incompletes deferred to measurement as before |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | shadow DOM penetrated (`x-your-stuff` → `x-organizer-*` paths); heading picture matches the crawl fingerprint (2 headings) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
axe-core 4.10.3, full ruleset, authenticated S4. **violations 4, incomplete
3, passes 45, inapplicable 44.** Raw: `R017-axe.json`. Triaged same session.

- O1 [classified] (`aria-command-name`, serious, wcag412): the **same
  unnamed community button, same header node path — fourth view running.**
  - Classified: W1 / 4.1.2 → **V-F4** (scope already product-wide; no change)
- O2 [classified] (`aria-required-children`, critical, wcag131, 4 nodes):
  `role="row"` divs in the file grid whose children are
  `x-organizer-grid-card` elements, not gridcells — **the same broken-grid
  family as T1-F2's root cause and V-F11**, in a third component
  (`x-organizer-*`). One genuinely positive detail: the cards themselves
  carry `aria-label`s, so **file names are exposed** — unlike S2's
  templates. The structure is wrong; the names exist.
  - Classified: W1 / 1.3.1 → **V-F11** (evidence added; component list
    extended)
- O3 [dismissed as finding, substance retained] (`heading-order`,
  best-practice): `h3 "Files"` with nothing above it — same mis-levelled
  pattern as S2 (V-F9). S4 exposes 2 headings total (crawl fingerprint
  agrees).
  - Dismissed: best-practice tag; noted as the S2 pattern recurring.
- O4 [classified] (`label`, **critical**, wcag412, 4 nodes — **new defect
  class, first seen on S4**): four `<input type="checkbox">` controls whose
  explicit `<label>` exists but is **hidden**, so the accessible name may
  not compute. These are almost certainly the **file-card selection
  checkboxes** — the mechanism for selecting files for bulk actions.
  - If confirmed by ear, a screen-reader user hears "checkbox" with no
    indication of *which file* it selects.
  - Classified: W1 / 4.1.2 / Major → **CONFIRMED by ear 2026-08-13**
    (R029 O2): checkbox and card action button announce with no unique
    name → **finding V-F12**.
- O5 [classified] (incompletes): `aria-valid-attr-value` ×2 = the shared
  header's `aria-controls` items, unchanged from S1/S2/S3 (resolve once,
  product-wide). `aria-prohibited-attr` ×4 routed with them.
  `color-contrast` ×9 = image-background class; deferred to
  rendered-pixel measurement per testing-tools.md, not eyedropper-queued.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R017-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
