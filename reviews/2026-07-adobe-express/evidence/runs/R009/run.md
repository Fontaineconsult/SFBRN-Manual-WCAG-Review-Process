# Test Run R009 — S1

| | |
|---|---|
| **Run ID** | R009 |
| **Date/time** | 2026-08-04 16:38 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (Claude, scripts/axe_scan.py; dedicated debug-profile Chrome, reviewer-authenticated) |
| **Result** | Works with issues |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**) is human-confirmed → finding, or dismissed with a written reason in the run notes | fail | O1 (V-F2 corroborated), O2 (new V-F4), O3 (best-practice, held as observation) |
| W2 — Every warning (axe **incomplete**) is reviewed; relevant ones investigated in the matching modality | pass | O4, O5, O6 — all routed to walkthrough steps |
| W3 — Structure output sane and cross-checked against the JAWS walk | pass | O3, O7 — axe penetrated the shadow DOM (unlike WAVE, R007); its landmark picture matches JAWS |

## Observations

axe-core 4.10.3, full ruleset: **violations 3, incomplete 3, passes 47,
inapplicable 42.** Raw output: `R009-axe.json` (1.65 MB).

- O1 [classified] (violation `color-contrast`, serious, wcag143): the exact
  node is `.browse-text` — the Upload card's "browse" link. **Independently
  corroborates finding V-F2** (R002's computed 3.96:1). Two instruments now
  agree.
  - Classified: W1 / WCAG 1.4.3 / Minor → finding V-F2 (evidence added)
- O2 [classified] (violation `aria-command-name`, serious, wcag412): icon-only
  `sp-action-button` inside `x-community-discovery-trigger` (the "community"
  people-icon in the header) has **no accessible name** — its x-icon is
  aria-hidden with an empty label. Vendor claims Does Not Support for 4.1.2 —
  consistent.
  - Classified: W1 / WCAG 4.1.2 / Major → finding V-F4 — JAWS confirmation in
    W5 (what announces on that button?)
- O3 [classified] (violation `region`, moderate, **best-practice tag — not a
  WCAG criterion**): the entire Recent bar (`x-home-recent-bar`: "Recent" h3,
  file card, "View all") sits **outside all landmarks**. Explains the W4
  reading-order oddity (Recent reads 3rd: it precedes `main` in the DOM).
  - Held as observation (no WCAG criterion failed); feeds the W4 NV5
    discussion — dismissal or finding is the reviewer's call there.
- O4 [classified] (incomplete `color-contrast`, serious, 15 nodes): the Adobe
  app-bar labels on the purple gradient (Adobe Home, Firefly, Express…) —
  axe cannot compute gradient backgrounds either. **Exactly the W13
  eyedropper queue** (matches R002 O3).
  - Routed: W13 (low-vision eyedropper measurements)
- O5 [classified] (incomplete `aria-valid-attr-value`, critical, 2 nodes):
  (a) "More apps" button has `aria-controls="spillover-dialog"` — verify the
  target ID exists when closed; (b) profile-thumbnail (account button)
  `aria-expanded`/`aria-haspopup="dialog"` — verify states toggle. Routed to
  W5 (JAWS behavior on both controls).
- O6 [classified] (incomplete `aria-required-children`, critical, 1 node):
  an **empty** `div role="list"` in the app bar (secondary app tiles) — no
  list items. Likely a latent/harmless empty container; verify it stays
  empty and silent in JAWS (W5); dismiss if so.
- O7 [classified]: **Refutation of an exploration recon item**: the
  Recent-file card link is NOT unlabeled — it contains
  `<span class="sr-only">Kaiser Permanente Mobile App - Letter Details</span>`
  and the thumbnail img has proper alt. The 2026-08-04 DOM-walk recon
  (03 §2.6) read only the light text and missed the sr-only span. Recon note
  corrected. axe reports no name violation on it.
  - Classified: W1 / — / recon corrected, no finding

## Notes

First production run of `scripts/axe_scan.py` (see testing-tools.md §axe-core
for setup). Instrument reach confirmed: axe traversed the open shadow DOM
(node targets show full custom-element paths) — contrast with WAVE's
blindness (R007). Remaining blind spots: closed shadow roots, cross-origin
iframes.

Process bug found and fixed in the same session: the script logged the run
before attempting the CDP connection, orphaning R008 when the connection
failed. Fixed — connection now precedes logging.

## Evidence files in this folder

- R009-axe.json — raw axe-core output (violations, incomplete, passes,
  inapplicable, full node targets/HTML)

## Findings raised from this run

- V-F2 (corroborating evidence added), V-F4 (new — 4.1.2 unnamed community
  button); recorded in 04-task-testing.md §B
