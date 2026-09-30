# Test Run R003 — R1

| | |
|---|---|
| **Run ID** | R003 |
| **Date/time** | 2026-09-30 13:32 |
| **View / sample** | R1 |
| **Page URL / location** | https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123 — `UI: My Courses → Start course → 3 AI & Ethics → Finding Hidden Scholarships with AI (article lesson, iframe m1-article-05-opening-doors-to-your-future.html)`; Classic experience active; lesson selected in the outline before the scan |
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

- O1 [new] (state: as scanned): axe **incomplete** `frame-tested` × 1 node(s) — Frames should be tested with axe-core. axe could not decide; a human must.
  - Proposed: W2 / no WCAG tag — route to the modality run that can settle it
- O2 [new] (state: as scanned): passes 39 / inapplicable 49.
  - dismissed: informational
- O3 [new] (state: article opened directly, signed-out window): axe on the article page itself — **2 violations, 0 incomplete**: `landmark-one-main` × 1 (no `main` landmark) and `region` × 19 (no page content inside any landmark); both axe best-practice rules with no WCAG tag. No violation on any WCAG-tagged rule; 13 rules passed, 75 inapplicable (no images, links, forms or media in the article). The in-article accordion `div onclick` cards and the `Quick Question` buttons are not caught by any axe rule — they stay routed to the S4 keyboard and JAWS runs (03 §2.6).
  - Proposed: W2 — settles the `frame-tested` incomplete above (the frame *was* tested, separately); W1 for the two best-practice violations: note under 2.4.1 / 1.3.1 in the no-vision run, not a finding on their own

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- `R003-axe.json` / `R003-axe.md` — sweep of the host page (course player with the lesson selected)
- `R003-axe-article.json` / `R003-axe-article.md` — ad-hoc sweep (`axe_scan.py --out`, signed-out window, 2026-09-30) of the lesson's cross-origin article `https://mnowak-ai.github.io/ai-academics-articles/m1-article-05-opening-doors-to-your-future.html` opened directly, because axe cannot enter the iframe from the host page (`frame-tested`)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
