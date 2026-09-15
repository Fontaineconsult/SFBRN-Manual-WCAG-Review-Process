# Test Run R112 — S13

| | |
|---|---|
| **Run ID** | R112 |
| **Date/time** | 2026-09-15 13:06 |
| **View / sample** | S13 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/ViewAssignmentDetails.aspx |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | — |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | | |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | | |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | | |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

(none yet)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R112-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
