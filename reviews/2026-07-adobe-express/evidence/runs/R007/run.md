# Test Run R007 — S1

| | |
|---|---|
| **Run ID** | R007 |
| **Date/time** | 2026-08-04 16:21 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | wave |
| **Baseline** | — |
| **Tester** | reviewer (D. Fontaine), WAVE extension; recorded via walkthrough W19 |
| **Result** | N/A — instrument-blind: WAVE analyzed only the light DOM (see O2); its output does not describe the app content |

## Checks (wave sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every WAVE **Error** and **Contrast Error** is human-confirmed → finding, or dismissed with a written reason in the run notes | n/a | O1 — zero errors reported, but see O2: absence of errors is non-penetration, not cleanliness |
| W2 — Every **Alert** is reviewed; relevant ones investigated in the matching modality | pass | O1, O2 — all three alerts reviewed and explained as shadow-DOM blindness |
| W3 — Structure panel reviewed: heading outline and landmarks are sane (feeds NV2) | n/a | O2 — WAVE saw no structure; JAWS (R001 O3/O7) is authoritative and contradicts it |

## Observations

- O1 [classified] (state: default): WAVE summary — **Errors 0, Contrast
  Errors 0, Alerts 3, Features 1, Structural 2, ARIA 2. AIM Score 10/10,
  "No errors detected".** Alerts: "No heading structure" (1), "No page
  regions" (1), "Noscript element" (1, visually hidden). Feature: Language
  (1). Structural: Inline frame ×2 (visually hidden). ARIA: ARIA (1),
  ARIA alert or live region (1) — both visually hidden.
  - Classified: W1/W2 — reviewed; no findings raised from counts
- O2 [classified] (state: default): **WAVE did not penetrate the app's
  shadow DOM.** Its "No heading structure" and "No page regions" alerts are
  directly contradicted by JAWS (R001: 13+ headings, 5 labeled landmarks) —
  WAVE saw only the light-DOM shell (noscript, two hidden iframes, one
  top-level live region, the lang attribute). The 0-error count and 10/10
  AIM score therefore say nothing about the product's content. Same
  root cause as the assistant-extraction emptiness (03 §2.6, resolved).
  - Classified: instrument limitation → Result N/A; ontology updated
    (testing-tools.md WAVE caveat; modality-checks.md W-section semantics)
- O3 [new]: Useful residue despite blindness: `lang` attribute present
  (corroborates NV9 direction); a top-level ARIA live region exists (worth
  correlating with NV7 announcements in W8); two hidden iframes noted.

## Notes

Reviewer-supplied WAVE panel output, pasted in session (walkthrough W19,
2026-08-04). WAVE extension version still unrecorded — pending W1.

Instrument verdict for this product: WAVE cannot audit Adobe Express app
views from the extension; treat any future "0 errors + no structure" WAVE
result on this product as non-penetration (Result N/A), not a pass. A
shadow-DOM-capable checker (axe DevTools, IBM Equal Access — see
tools/wai-evaluation-tools.md) is the candidate secondary instrument if the
reviewer wants automated coverage of app views; WAVE remains the declared
standard for views it can parse (marketing/landing pages likely qualify).

## Evidence files in this folder

- (reviewer: WAVE overlay + details-panel screenshots welcome as
  R007-wave-overlay.png / R007-wave-details.png, per testing-tools.md)

## Findings raised from this run

- none (all alerts dismissed as instrument blindness; no errors to confirm)
