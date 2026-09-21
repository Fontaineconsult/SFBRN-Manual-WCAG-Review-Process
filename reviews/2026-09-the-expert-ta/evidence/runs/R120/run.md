# Test Run R120 — S7

| | |
|---|---|
| **Run ID** | R120 |
| **Date/time** | 2026-09-17 12:30 |
| **View / sample** | S7 |
| **Page URL / location** | https://login.theexpertta.com/Login.aspx |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — NC1, NC3 need the reviewer — judge from `R120-grayscale.png` (achromatopsia emulation) or the OS filter; measured fail on NC2 awaits confirmation |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | | |
| NC2 — Links are distinguishable from surrounding text without color | fail | O2 — 1 of 6 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: (e-mail reset) → /ResetPassword.aspx [1.7:1 vs text; hover cue: a:hover; focus: outline]; 5 colour-only link(s) DO satisfy G183 |
| NC3 — Everything remains operable and understandable in grayscale | | |

**view_probe 2026-09-17:** answered NC2=fail by measurement; facts in `R120-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-17 view_probe): 1 of 6 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: (e-mail reset) → /ResetPassword.aspx [1.7:1 vs text; hover cue: a:hover; focus: outline]; 5 colour-only link(s) DO satisfy G183
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O3 [clarified] (state: sign-in page, reviewer on NVDA, 2026-09-21 — step W70): *"e-mail reset appears as a link to NVDA and is tabbable."* The control's **programmatic** presentation is sound — the role is exposed and it is reachable from the keyboard. This does **not** answer NC2 / 1.4.1, which asks about the **visual** presentation to a sighted user who cannot use colour to tell the link from the sentence around it; the measured fail (1.7:1 against the surrounding bold text, no underline until hover or focus) is untouched by it and still awaits the looking question → W73.
  - Classified: 4.1.2 and 2.1.1 / **pass** for this control (recorded here because the reviewer raised it on this view; no finding); NC2 unchanged — still a measured fail awaiting confirmation

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R120-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
