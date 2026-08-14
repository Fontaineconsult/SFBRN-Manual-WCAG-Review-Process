# Test Run R040 — S1

| | |
|---|---|
| **Run ID** | R040 |
| **Date/time** | 2026-08-14 13:50 |
| **View / sample** | S1 |
| **Page URL / location** | WAVE extension over a **5-page sample, supplied by the reviewer 2026-08-14**: **https://new.express.adobe.com/** (S1 Home) · `/id/urn:aaid:sc:US:a767278e-deed-4656-b424-f01495fad229` ("Can-I-find-the-right-text", the R038 editor document) · `/brands` · `/your-stuff/files` (S4) · `/learn`. Counter-example (O2) measured on S1 Home |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | wave |
| **Baseline** | — |
| **Tester** | reviewer (D. Fontaine) |
| **Result** | N/A |

**Result reasoning** (set 2026-08-14). **Instrument-blind — the clean
result is a false negative, and this run proves it rather than assuming
it.** WAVE reported **no contrast errors across a 5-page sample**. On the
same day, on S1, the assistant re-measured the `browse` link at
**3.96:1** — a confirmed contrast failure (V-F2) that WAVE's clean sweep
did not report. Recorded as N/A, not as a pass, exactly as R007 was on
2026-08-04.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (wave sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | | |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | | |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | | |

## Observations

- **O1 [classified]** (reviewer, 2026-08-14): **WAVE reports no contrast
  errors on a sampling of 5 pages.**
  - **Dismissed as evidence of conformance — with proof, not by
    reputation.** The reviewer's sweep is accurately reported; what it
    cannot do is establish that contrast passes on this product.

- **O2 [classified]** — **the controlled counter-example.** On the same
  day, the assistant re-measured the exact node behind **V-F2** — the
  Upload card's "browse" link on S1 Home:

    | | |
    |---|---|
    | Text | "browse", 11px, weight 400 |
    | Colour | `rgb(59, 99, 251)` |
    | Background | resolved on a real `<div>` — **not** the white fallback |
    | **Contrast** | **3.96:1** — fails 4.5:1 |

  - **So a confirmed contrast failure was live on S1 while WAVE reported
    zero contrast errors. Page list supplied 2026-08-14: S1 Home *was* in
    the sample** — so this is a **direct false negative**, not a sampling
    gap. WAVE analysed the exact page carrying a 3.96:1 link and reported
    it clean.
  - **Three instruments now agree the failure is real**, across ten days
    and a browser major version: computed-style sampling 2026-08-04
    (R002), axe-core `color-contrast` on the same node (R009), and this
    re-measurement 2026-08-14 on **Chrome 151**. Per 03 §1.5, a finding
    that *survives* a browser upgrade is strengthened by it — the rule
    there anticipated the opposite case, a finding vanishing and being
    mistaken for a fix.
  - **The measurement's own weak point was checked and is clean.** The
    documented failure mode for contrast probes is silent fallback to a
    white background when a pseudo-element or image paints it, yielding a
    fictional 21:1. The probe reported the background as resolved from a
    real `<div>`, so the ancestor walk terminated on an actual opaque
    colour. Had it reported an assumed background, the number would have
    been discarded.
  - **Why WAVE fails here specifically** (testing-tools.md): Adobe Express
    renders into hundreds of open shadow roots — 351 on S1 — and WAVE
    parses only the light DOM. It is not reporting "no contrast errors"; it
    is reporting "no contrast errors **in the fraction of the page I can
    see**". A clean WAVE result on this product carries no information
    about the product.
  - Classified: dismissed as a conformance signal; retained as corroboration
    that **automated instruments are structurally blind here** — a point
    the report already makes and which this run now evidences twice over
    (WAVE blind to the light-DOM gap; axe blind to the canvas)
  - **No change to 1.4.3**, which stays Partially Supports on V-F2.

## Page list — supplied and resolved 2026-08-14

| Page | In the review's sample set? |
|---|---|
| `/` — S1 Home | **yes** — and the page carrying the 3.96:1 failure |
| `/id/urn:aaid:sc:US:a767278e…` — "Can-I-find-the-right-text" | the **R038** editor document (03 §2.6) |
| `/brands` | no — outside the sampled views |
| `/your-stuff/files` — S4 | yes |
| `/learn` | no — outside the sampled views, though **R039** covers its media |

Two of the five (**Brands**, **Learn**) sit outside the sampled views, so
the sweep touched surfaces no other run has. That does not rescue the
result — a tool that misses a known failure on a page it *did* analyse
tells us nothing about pages it analysed the same way — but it is worth
noting that the sample was reasonable and the instrument still failed.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R040-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
