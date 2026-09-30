# Test Run R011 — S2

| | |
|---|---|
| **Run ID** | R011 |
| **Date/time** | 2026-08-06 12:29 |
| **View / sample** | S2 |
| **Page URL / location** | https://new.express.adobe.com/explore/templates?assetCollection=urn%3Aaaid%3Asc%3AVA6C2%3A07c69ce7-24fd-488c-bac5-d18f464c5997 |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | — |
| **Result** | Works with issues |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | fail | O1 (root cause of T1-F2), O2 (V-F4 scope widened), O3 (dismissed — best practice) |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | O4, O5 — routed; contrast deferred with a named method |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | O6 — axe penetrated the shadow DOM and its heading picture matches the NVDA walk |

## Observations

axe-core 4.10.3, full ruleset, on the authenticated S2 view. **violations 4,
incomplete 4, passes 47, inapplicable 42.** Raw output: `R011-axe.json`
(2.86 MB). Triaged 2026-08-06, after the NVDA walk (R013) — the ordering
matters: the reviewer's experience was recorded first and independently, so
the agreement below is corroboration, not confirmation bias.

- O1 [classified] (violations `aria-required-parent` **critical, wcag131**
  and `aria-allowed-attr` **critical, wcag412** — both on the *same node*):
  **this is the mechanism behind T1-F2.** The template grid container is

      <x-masonry role="row" aria-orientation="vertical" …>

  `role="row"` is declared with **no required parent present** — axe:
  *"Required ARIA parents role not present: grid, rowgroup, table,
  treegrid"* — and `aria-orientation="vertical"` is **not permitted** on
  `role="row"`. So the results grid announces itself as a table row that
  belongs to no table.
  - **This explains every symptom the reviewer reported by ear in R013**,
    which none of them individually made obvious:
    - items announced as *both a form element and a button* (O6 there) —
      role semantics resolve incoherently inside an orphaned `row`;
    - **arrow-key movement silent** (O5 there) — grid/row navigation
      semantics require a valid grid ancestor; without one there is no
      structure for the AT to move within;
    - the grid **not announced on entry** (O3 there) — an orphaned `row`
      is not a landmark, region, or list, so there is nothing to announce;
    - **item boundaries not conveyed** — no `gridcell`/`row` relationship
      survives.
  - Why this matters more than the symptom list: a vendor can act on
    *"`x-masonry` declares `role="row"` with no grid parent"*. They cannot
    act on *"the template grid is hard to navigate"*. This gives T1-F2 a
    single, specific, fixable root cause.
  - Classified: W1 / WCAG 1.3.1, 4.1.2 / Major → **corroborates and
    explains T1-F2** (04 §A); no separate finding raised, to avoid
    double-counting the same defect.
- O2 [classified] (violation `aria-command-name`, serious, wcag412): the
  **same unnamed community icon button as S1** — identical node path through
  `af-headerbar` → `x-community-discovery-trigger`.
  - **Scope consequence for V-F4:** the control lives in the persistent app
    header, not in S1's content. It was recorded as "one control on S1";
    it is in fact **one control on every view**. V-F4 updated accordingly.
    The defect count does not grow, but its reach does.
  - Classified: W1 / WCAG 4.1.2 / Major → **V-F4 (scope widened)**
- O3 [dismissed] (violation `heading-order`, moderate): `<h3>Filters</h3>`
  appears with no preceding `h1`/`h2`. Tagged **best-practice, not a WCAG
  success criterion**, so it is not a finding on its own.
  - Not discarded, though: it independently corroborates **V-F9** — S2's
    heading structure is not merely sparse ("Explore" and "Filters" only,
    R013 O2) but also **mis-levelled**, an `h3` with nothing above it. Cited
    there as supporting evidence.
  - Dismissed: best-practice rule; substance folded into V-F9.
- O4 [classified] (incomplete `aria-valid-attr-value`, critical, 2 nodes):
  `aria-controls="spillover-dialog"` on "More apps" and
  `aria-controls="profile-dropdown-id"` on the account button — axe cannot
  tell whether the referenced IDs exist while the popups are closed.
  **Identical to R009 O5 on S1**, and for the same reason: both controls are
  in the shared header.
  - Routed: still open from S1's W5; resolve once for all views by opening
    each control and checking the target ID appears.
- O5 [classified] (incomplete `aria-required-children`, critical): the empty
  `div role="list"` in the app bar — **identical to R009 O6 on S1**, shared
  header again.
  - Routed: unchanged; likely harmless if it stays empty and silent, but
    confirm by ear once.
  - Also here: `aria-prohibited-attr` (serious) on the Region filter's
    `<div id="content" aria-labelledby="header">` — `aria-labelledby` on a
    `div` with no role is not reliably supported. Low impact; the filters
    were all reachable and announced in R013 O9, so this is a latent
    markup issue rather than an observed barrier. Recorded, not raised.
  - The 12 `color-contrast` incompletes are the **same image-background
    class as R009 O9** — not measurable by DOM inspection; needs
    rendered-pixel sampling or the eyedropper. Deferred with that method
    named, not silently dropped.
- O6 [classified] (W3 instrument sanity): axe traversed the open shadow DOM
  on S2 as it did on S1 — node paths run through `x-explore` →
  `hz-inspire-*` → `x-masonry`. Its heading picture (an `h3` "Filters", no
  `h1`) matches what NVDA reported independently (R013 O2), so the
  instrument penetrated and its output is trustworthy for this view.
  - Classified: W3 / — / pass

**Pattern worth carrying to the report:** three of this run's items
(O2, O4, O5) are *the same defects already recorded on S1*, because they
live in the persistent app header rather than in view content. Header
defects are paid once per view by the user and should be counted once, but
scoped as product-wide — not re-raised per view.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R011-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
