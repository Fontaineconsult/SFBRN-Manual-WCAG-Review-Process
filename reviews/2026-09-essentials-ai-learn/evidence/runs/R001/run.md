# Test Run R001 — S3

| | |
|---|---|
| **Run ID** | R001 |
| **Date/time** | 2026-09-30 13:31 |
| **View / sample** | S3 |
| **Page URL / location** | https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123 — `UI: My Courses → Start course → 1 Intro to the Course → Icebreaker (video lesson)`; Classic experience active; lesson selected in the outline before the scan |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 154 debug profile); triage from R064 and the NVDA walk (R016) |
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
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O3 — axe reported no violations on the video lesson |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | | |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | | |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:

- O1 [new] (state: as scanned): axe **incomplete** `video-caption` × 1 node(s) — <video> elements must have captions. axe could not decide; a human must.
  - Proposed: W2 / WCAG 1.2.2 — route to the modality run that can settle it
- O2 [new] (state: as scanned): passes 38 / inapplicable 50.
  - dismissed: informational
- O3 [new] (state: triage 2026-10-02): W1: no violation reported. W2: the one incomplete, `video-caption` (axe cannot see burned-in captions), is routed to the no-hearing run R064 NH1 (reviewer judges the open captions). W3 waits for the NVDA structure answer (one h1, one outline navigation).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02.** W2 closes when R064 NH1 is answered; W3 from R016.

## Evidence files in this folder

- (screenshots/exports named R001-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
