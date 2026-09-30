# Test Run R003 — S1

| | |
|---|---|
| **Run ID** | R003 |
| **Date/time** | 2026-08-04 15:44 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | grayscale |
| **Baseline** | — |
| **Tester** | assistant (Claude, Chrome automation) |
| **Result** | Works with issues |

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | pass | O1 |
| NC2 — Links are distinguishable from surrounding text without color | pass | O2 + **reviewer hover confirmation 2026-08-14 (R002 O-LV17)** — the hover/focus cue pass this row was deferred for is done; no colour-alone cue found |
| NC3 — Everything remains operable and understandable in grayscale | pass | O1 |

## Observations

- O1 [classified] (states: default + rail hover flyout): Full view inspected
  in grayscale. Selected rail item (Home) stays distinguishable by its
  lighter tile background; BETA badges remain readable; cards are identified
  by imagery and text labels; no status/error/required indicator on this
  view relies on hue.
  - Classified: NC1, NC3 / WCAG 1.4.1 / pass — no finding
- O2 [classified] (state: default): Action links ("View all" beside section
  headings, "browse" in the Upload card) are blue-on-light with no underline.
  In grayscale they retain a luminance difference from neighboring text
  (mid-gray vs black) and sit in positions that convention marks as actions,
  so this is not a clear color-alone failure — but F73-style confirmation is
  needed: check for underline/weight cue on hover and focus.
  - Classified: NC2 / WCAG 1.4.1 / partial — observation only, reviewer to
    confirm before any finding

## Notes

Assistant-driven run. Instrument: CSS proxy `html{filter:grayscale(1)}`
(documented accepted proxy; canonical OS Color Filters `Win+Ctrl+C` available
to the reviewer for spot-check). States inspected: default page and the rail
hover flyout (which was still open from R002's LV6 test — see R002 O5).

## Evidence files in this folder

- R003-grayscale-home.jpg — full view in grayscale (rail flyout visible top-left)
- R003-grayscale-viewall.png — "Quick edits / View all" region in grayscale (O2)
- R003-grayscale-browse.png — Upload card "browse" link in grayscale (O2)

## Findings raised from this run

- none (O2 held at observation pending reviewer confirmation of hover/focus
  link cues)
