# Test Run R008 — S2

| | |
|---|---|
| **Run ID** | R008 |
| **Date/time** | 2026-09-30 13:34 |
| **View / sample** | S2 |
| **Page URL / location** | https://learn.essentials-ai.com/learning |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 154 debug profile); triage from R010 measurement and the NVDA walk (R009) |
| **Result** | Works |

**Result reasoning.** axe sweep of My Courses (signed-in profile): no violations; the one incomplete (color-contrast on the gradient course card, 3 nodes) was measured on rendered pixels in R010 and passes; structure (banner, complementary, navigation, main, h1 + h2) matches what NVDA found on the walk.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O3 — axe reported no violations on My Courses |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | O3 — the contrast incomplete was measured on rendered pixels (R010) and passes |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | O4 — structure cross-checked against the NVDA walk: identical |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:

- O1 [new] (state: as scanned): axe **incomplete** `color-contrast` × 3 node(s) — Elements must meet minimum color contrast ratio thresholds. axe could not decide; a human must.
  - Proposed: W2 / WCAG 1.4.3 — route to the modality run that can settle it
- O2 [new] (state: as scanned): passes 42 / inapplicable 47.
  - dismissed: informational
- O3 [new] (state: triage 2026-10-02): W2: the single incomplete `color-contrast` ×3 (gradient card) was settled by rendered-pixel sampling in R010 O-pixel — all three pass (6.4:1, 15.3:1, ≥ 9:1). W1: no violation reported. W3 waits for the NVDA walk's structure (expected: banner, complementary, navigation, main, h1 + h2).
- O4 [classified] (triage 2026-10-02): W3: NVDA finds the same structure axe saw (banner, complementary, navigation, main; h1 + h2) — R009 O8.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02.** W3 closes from the reviewer's NVDA structure answers (R009).

## Evidence files in this folder

- (screenshots/exports named R008-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
