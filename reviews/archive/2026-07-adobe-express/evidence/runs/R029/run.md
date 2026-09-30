# Test Run R029 — S4

| | |
|---|---|
| **Run ID** | R029 |
| **Date/time** | 2026-08-13 13:04 |
| **View / sample** | S4 |
| **Page URL / location** | https://new.express.adobe.com/your-stuff/files/recent?filter=express |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B4 |
| **Tester** | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| **Result** | Works with issues |

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | fail | product-wide V-F8 (title "Adobe Express" on every view, S4 included in the 7-view verification) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | partial | O1 — reviewer confirms structure matches the fingerprint: sparse (2 headings, `h3` "Files" mis-levelled — the S2/V-F9 pattern recurring) but landmarks sound (`main`/header/search/nav) |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O2 → **V-F12** (checkbox and per-card action button have no unique name); card names themselves work (rename-by-name task succeeded) |
| NV4 — Images announce appropriate alternatives; decorative images are silent | partial | axe clean on image alts (R017); not separately walked with `G` |
| NV5 — Reading order matches the meaning of the visual order | pass | O3 — full rename task completed via Tab/arrows without disorientation |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | partial | rename field operable (O3); no error path on this view |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | fail | O4 → **V-F13** (filter change updates the list with no announcement — 4th product instance) |
| NV8 — Nothing is conveyed only by visual position, shape, or size | partial | not separately narrated; no contrary signal in the completed walk + grayscale evidence (R023) — reviewer may spot-confirm |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | partial | not separately narrated; no mispronunciation reported across S1–S4 sessions |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
Reviewer session 2026-08-13, NVDA 2026.1.1 / Chrome 150, baseline B4.

- O1 [classified] (W22 — structure): *"headings and nav match your scan"* —
  2 headings with the mis-levelled `h3` "Files", landmarks
  main/header/search/Primary nav. Same sparse-headings pattern as S2
  (V-F9); not raised separately, recorded as the pattern's third view.
  - Classified: NV2 / 1.3.1 / partial — no new finding
- O2 [classified] (W23 — **the R017 O4 candidate, CONFIRMED by ear**):
  *"correct that the checkbox and the action button have no unique name."*
  Both per-card controls — the bulk-select **checkbox** and the card's
  **action button** — announce without a unique name, so a user cannot tell
  *which file* they are selecting or acting on. The card links themselves
  are named (the reviewer located files by name to rename them), so this is
  scoped to the two per-card controls, exactly matching axe's `label`
  violation (hidden `<label>`, R017 O4) plus the action-button widening it.
  - Classified: NV3 / WCAG 4.1.2 / Major → **finding V-F12**
- O3 [classified] (W24 — rename, and the R016 O11 discrepancy): renaming is
  **fully operable keyboard-only** ("possible with just tab and arrows"),
  in both surfaces (listing and canvas edit), and **the discrepancy cannot
  be reproduced** — names now persist and display correctly after renames
  in both places. R016 O11 is closed as *unreproducible* (not explained):
  candidate readings remain stale-listing or a one-time sync miss. One
  **inconsistency** observed en route: the rename **action button was not
  initially exposed in the listing** — it appeared only after the reviewer
  had entered the canvas edit window once, and remained exposed thereafter.
  One-time state, not reproducible on demand; recorded as an observation
  (candidate 3.2.x consistency / lazy menu registration), not a finding.
  - Classified: NV3/MO2 / pass for operability — no finding; R016 O11
    closed. Registry note: display names were changed again this session
    (reviewer mentions "sdcsdc" and renames in two surfaces) — **the URN
    registry in 03 §2.6 is the locator authority; display names in it are
    now stale and marked as drift-prone by design.** Reviewer to state the
    Aug-10 document's current name for the registry when convenient.
- O4 [classified] (W25 — filter): *"filter change does not announce search
  or file changes."* Operating the filter updates the file list with **no
  announcement of any kind** — the **fourth** verified instance of the
  product-wide silent-update pattern (S2 lazy grid, S2 search results, S3
  image insert/AI generate, now S4 filter).
  - Classified: NV7 / WCAG 4.1.3 / Major → **finding V-F13**
- O5 [classified — W26 closures, reviewer]: **(a) Consistency: "yes it is
  consistent"** — navigation and component identification are consistent
  across all four tested views, and help appears in a consistent location.
  This is the cross-view answer CO1/CO2 required (they could not be settled
  from any single view) — recorded here and back-filled into R010 (S1
  cognition), and it stands as ready evidence for the S2/S3/S4 cognition
  runs when they open. **(b) Motor spot-check: "no"** concerns on S4 — no
  tab-order surprises, no visibly undersized targets. A signal for the B2
  sweep, not a substitute for it. **(c) No voice input** anywhere
  (recorded in R030 O3).
  - Classified: CO1, CO2 / 3.2.3, 3.2.4, 3.2.6 / pass (cross-view) — no
    finding.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R029-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
