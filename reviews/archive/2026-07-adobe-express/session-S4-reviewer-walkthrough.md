# Reviewer Session Walkthrough — S4 Your stuff

Built 2026-08-13 from the live sources: R017 (axe triage), the crawl
fingerprint, and `review.py gaps`. S4 is the least-tested sample — one axe
sweep, no human run. **One session here closes the whole view**: it is a
small listing page (2 headings, ~4 file cards, tabs, filter/sort controls).

Setup: NVDA Speech Viewer on (`NVDA+N` → Tools); don't press `Insert+Space`;
unfocus the assistant panel. URL:
`https://new.express.adobe.com/your-stuff/files/recent?filter=express`.
The four documents present are the review's registry (03 §2.6) — **do not
delete any**; renaming *one specific* file is part of W24.

## W22 — no-vision sweep (run logged when you start)

**Do:** `NVDA+F7` headings/landmarks, then Tab the whole page.
**Tell me:** What structure exists (fingerprint says: 2 headings, `main` +
header + search + Primary nav; h3 "Files" with nothing above it); anything
unnamed; do the file cards announce their names? (axe says card names ARE
exposed — the one view where items are named.)
**Feedback:** 2026-08-13 — structure matches the fingerprint (2 headings incl. mis-levelled h3 Files; landmarks sound). Card links are named (rename-by-name succeeded). Recorded R029 O1.

## W23 — KEY STEP: the selection checkboxes (R017 O4, candidate finding)

**Do:** Focus a file card's selection checkbox (the bulk-select control).
**Tell me:** Exact speech. axe flags all four as `label` **critical** —
explicit `<label>` exists but is hidden, so the name may not compute. If
you hear bare "checkbox" with no file name, that confirms a Major 4.1.2
finding (you can't tell *which file* you're selecting for bulk actions).
If it announces the file name, the candidate dies — say which.
**Feedback:** 2026-08-13 — CONFIRMED: checkbox AND card action button have no unique name -> finding V-F12 (R029 O2).

## W24 — the rename discrepancy (R016 O11, still open)

**Do:** Open "Untitled - August 10, 2026 at 13.09.20"
(`/id/urn:aaid:sc:US:b1ab530f-…`), check its in-editor title; if it shows
"Test-With-Keyboard" there, we have title≠filename; if not, rename it again
and watch whether this listing updates.
**Tell me:** What you find — this settles whether the keyboard rename you
performed in R016 actually persisted (a feedback-integrity question).
**Feedback:** 2026-08-13 — cannot reproduce: renamed again in both listing and canvas-edit surfaces, names persist and display correctly. R016 O11 closed as unreproducible. Note: the listing's rename action button was not initially exposed until the canvas edit window had been entered once — inconsistency recorded as an observation (R029 O3).

## W25 — tabs, filter, sort, view toggle (NV3; feeds motor too)

**Do:** Operate the Files/Projects/Libraries/Favorites tabs, the filter,
sort, and grid/list toggle, by keyboard.
**Tell me:** Reachable? Announced with state (selected tab, current sort)?
Does the list update announce (4.1.3 pattern watch — three instances
product-wide already)?
**Feedback:** 2026-08-13 — filter change does NOT announce list/search changes -> finding V-F13, fourth instance of the product-wide 4.1.3 pattern (R029 O4).

## W26 — quick modality closures (same sitting)

- **no-hearing / no-speech:** expected N/A (media audit will confirm no
  audible media — I'll have the DOM numbers by then); just confirm nothing
  talks or listens.
- **cognition (CO1/CO2):** with S1–S4 all seen now — is navigation and
  component identification consistent across views? Is help in a
  consistent place?
- **motor spot-check:** any tab-order surprises; target sizes look fine
  (cards are large).
**Feedback:** 2026-08-13 — all closed: no voice input anywhere (R030 O3);
no audible media encountered; **consistency across S1–S4 confirmed**
(CO1/CO2 pass, cross-view — R029 O5, back-filled into R010); no motor
spot-concerns on S4. Bonus from this sitting: the S3 caption-capability
inspection (R030 O1/O2 → 06 §Concerns).

## Close-out (assistant)

Runs filled + Results derived; checkbox candidate → finding or dismissed;
rename discrepancy resolved in R016 O11; coverage baseline (03 §3.1b) and
06 tables updated; `validate` re-run.
