# Test Run R006 — S1

| | |
|---|---|
| **Run ID** | R006 |
| **Date/time** | 2026-09-30 13:33 |
| **View / sample** | S1 |
| **Page URL / location** | https://learn.essentials-ai.com/login |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 154 signed-out debug profile); triage from the reviewer's NVDA walk (R050) |
| **Result** | Works |

**Result reasoning.** axe sweep of the sign-in page (signed-out profile): no violations; the one incomplete (form-field-multiple-labels on the password field) was investigated with NVDA on the walk and routed to NV6/CO3; structure (one main, one h1) matches what NVDA found.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O3 — axe reported no violations on the sign-in page; nothing to confirm or dismiss |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | O3 — the one incomplete was investigated with NVDA (R050 O10) and routed to NV6/CO3 |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | O4 — structure cross-checked against the NVDA walk: identical (one main, one h1) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:

- O1 [classified] (state: as scanned): axe **incomplete** `form-field-multiple-labels` × 1 node(s) — Form field must not have multiple label elements. axe could not decide; a human must.
  - Proposed: W2 / WCAG 3.3.2 — route to the modality run that can settle it
- O2 [new] (state: as scanned): passes 35 / inapplicable 54.
  - dismissed: informational
- O3 [new] (triage 2026-09-30): W2: the single incomplete `form-field-multiple-labels` (password field) was put to NVDA on the walk — announced "Password Show Password Edit Protected Show Blank" (R050 O10). Routed to NV6/CO3; the reviewer's call on severity is pending there. W1: no violation was reported, nothing to confirm or dismiss.
- O4 [classified] (triage 2026-09-30): W3: axe saw one main landmark and one h1; NVDA found "Main landmark" and one heading "Sign in" level 1 (R050 O11, O12). The instrument penetrated the page; structure output is sane.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R006-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
