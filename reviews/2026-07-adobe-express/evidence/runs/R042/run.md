# Test Run R042 — S1

| | |
|---|---|
| **Run ID** | R042 |
| **Date/time** | 2026-08-14 14:14 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ - plus S2 /explore/templates, S3 /id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86, S4 /your-stuff/files/recent (four-view sweep) |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | assistant (CDP structural measurement, Chrome 151, extensions inert) |
| **Result** | Works |

**Result reasoning** (set 2026-08-14). Structural measurement across all
four sampled views to ground the criteria that could be rolled up from
evidence rather than re-walked. Nothing measured here failed: **zero
unnamed links on any view**, no foreign-language passages, no inputs
collecting personal information, and search plus navigation landmarks
present on every non-editor view. **This run measures structure only** —
what a user can *reach* remains the reviewer's question (CLAUDE.md), and
nothing here overrides a screen-reader result.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (inspection sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | | |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | | |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | | |

## Observations

Four-view structural sweep, 2026-08-14, on the clean debug profile.

| | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| document `lang` | en-us | en-us | en-us | en-us |
| elements with a differing `lang` | 0 | 0 | 0 | 0 |
| visible inputs | 2 | 13 | 1 | 12 |
| links (visible) | 2 | 17 | 1 | 9 |
| **unnamed links** | **0** | **0** | **0** | **0** |
| search controls | 1 | 1 | 0 | 1 |
| nav/search landmarks | 2 | 3 | 0 | 4 |

- **O1 [classified]** (3.1.2 Language of Parts): **zero elements carrying a
  `lang` different from the document's `en-us`, on any view.** No
  foreign-language passage exists for the criterion to govern.
  - Classified: WCAG **3.1.2** / **Not Applicable** — no finding

- **O2 [classified]** (1.3.5 Identify Input Purpose): the product's visible
  inputs are **search boxes and selection checkboxes**. None collects
  information *about the user* — no name, email, address, phone or payment
  field appears anywhere in the four views. 1.3.5 governs fields collecting
  user information against the 53 defined input purposes; there are none.
  - Consistent with why 3.3.1/3.3.3/3.3.7 also came out Not Applicable
    (R041): this product simply does not gather data about its users.
  - Classified: WCAG **1.3.5** / **Not Applicable** — no finding

- **O3 [classified]** (2.4.4 Link Purpose): **every visible link on every
  view carries an accessible name — 0 unnamed of 29 across the four
  views.** The duplicate names found (S2: "Templates" ×2, "Photos" ×2,
  "Videos" ×2; S4: "Files" ×2, "Projects" ×2) are the same destinations
  surfaced in two places, which 2.4.4 permits.
  - **The precision that matters for the report:** this product's naming
    defects are real but they are **not on links**. Template grid items
    announce with conflicting form-element/button roles (T1-F2), the ten
    "Browse templates" controls are `sp-button`s (V-F5), the community
    icon and page-nav "more" are buttons (V-F4, V-F10), and the layer rows
    are grid cells (T2-F4). All are recorded under **4.1.2 / 2.4.6**,
    where they belong. Rolling them into 2.4.4 would double-count them and
    would be easy for a vendor to rebut.
  - Classified: WCAG **2.4.4** / **Supports** — no finding

- **O4 [classified]** (2.4.5 Multiple Ways): S1, S2 and S4 each expose a
  **search control plus 2–4 navigation landmarks**, which is two
  independent mechanisms — the criterion asks for more than one.
  **S3 the editor has neither (0 search, 0 nav landmarks)** and needs
  none: 2.4.5 exempts a page that is *"a step in a process"*, which the
  editor is by definition — it is where the design process happens, and it
  is reached from the views that do provide navigation.
  - Classified: WCAG **2.4.5** / **Supports** — no finding

- **O5 [new, routed to the reviewer]**: **one unnamed `<input>` appears on
  every view** (S1, S2, S3, S4 alike), suggesting a shared component —
  most likely the hidden file-upload input behind the "browse" affordance.
  - **Not recorded as a defect.** A file input that is visually hidden and
    operated through a correctly-labelled button is a normal, accessible
    pattern, and this review's own doctrine is that names are confirmed
    **on focus**, never from a DOM or elements list (R012 O9 nearly
    produced a false finding that way).
  - **Routed:** if a reviewer session ever reaches an unnamed edit field by
    Tab on any view, this is the candidate. Otherwise it stays an
    observation.
  - Classified: pending — no finding, no criterion moved

- **O6 [ATTEMPTED AND ABANDONED]** (1.4.11 Non-text Contrast / LV5,
  2026-08-14, assistant): **an automated rendered-pixel measurement was
  built, produced wrong results three times, and was discarded. 1.4.11
  stays Not Evaluated and returns to the reviewer's eyedropper.** Written
  up in full because the next agent will otherwise rebuild the same
  instrument.
  - **Attempt 1 — boundary scan.** Sampled across each control's edge for
    a border step. Reported **20 of 21 controls below 3:1**, with pairs
    like `bg=rgb(17,0,54) edge=rgb(17,0,54)` — identical pixels. Cause:
    most controls here are **borderless icon buttons**, so there is no
    edge step to find. **Measuring the wrong thing:** Understanding 1.4.11
    asks for the contrast of the visual information *required to identify*
    a control, and does not require a boundary to exist at all. A result
    of "almost everything fails" was the signal to stop, not to record.
  - **Attempt 2 — glyph sampling.** Rewritten to find each control's
    dominant interior colour and its most-distant interior pixel (the icon
    against its own background). Ratios became plausible — 6.22, 12.18,
    12.85, 13.45 — but **7 controls still sampled as uniform dark
    purple**, and a "View all" text link sampled as **pure white with no
    text in it**, which is impossible for a rendered text link.
  - **Root cause, found by saving the capture and looking at it:** a
    consistent **~56 px vertical offset** between `getBoundingClientRect`
    coordinates and `Page.captureScreenshot(fromSurface=true)` pixels. The
    Adobe cross-product app bar occupies the top ~55 px of the captured
    surface but is outside the document's viewport coordinate space, so
    every rect samples ~56 px too high — controls in the black Express bar
    were being sampled in the purple Adobe bar above it.
  - **Attempt 3 — `fromSurface=false`.** Ignored the device-metrics
    override and returned a **2112×1486** image; everything sampled white.
    Worse, not better.
  - **Why it stopped there.** A fourth attempt would mean deriving the
    offset empirically and trusting it — and an offset-corrected number
    that nobody has visually verified is exactly the "confident wrong
    number" the process forbids. Three corrections on one measurement is
    the point at which the instrument, not the criterion, has become the
    subject.
  - **What was salvaged:** the corrected 1280×900 capture is saved as
    **`R002/R002-lv5-uicontrast-reference-1280.png`** — a true rendered
    reference the reviewer can eyedropper directly, which is what LV5
    specified in the first place.
  - Classified: WCAG **1.4.11** / **not measured** — remains Not
    Evaluated; routed to LV5 (reviewer eyedropper)

- **O7 [classified]** (2.5.3 Label in Name, four-view sweep 2026-08-14):
  compared **visible text against computed accessible name** for every
  control carrying visible text. Icon-only controls are out of scope —
  with no visible label there is nothing for 2.5.3 to govern (their
  missing names are 4.1.2, recorded as V-F4/V-F10).

  | View | Controls with visible text | `aria-label` set | Name omits visible label |
  |---|---|---|---|
  | S1 | 23 | 8 | **0** |
  | S2 | 22 | 8 | **0** |
  | S4 | 12 | 5 | **0** |
  | S3 | 7 | 4 | **1** |
  | **Total** | **64** | **25** | **1** |

  - **63 of 64 pass.** Notably, all 25 controls whose `aria-label`
    *overrides* the visible text — the only way to break this criterion —
    reproduce that text exactly ("Photos" → "photos", "Files" → "files",
    "Premium member" → "premium member"). The product is doing this
    correctly and deliberately nearly everywhere.
  - **The single exception, verified individually:** the editor's zoom
    control is
    `<sp-action-button role="button" aria-label="View options"
    aria-haspopup="true">` whose **only visible text is the zoom
    percentage** ("100%", "67%" — it changes with zoom level). Visible
    label and accessible name **share nothing**. A speech-input user
    saying *"click 100 percent"* would not activate it.
  - **An interpretive question sits under this, and it is flagged rather
    than decided.** 2.5.3 governs *labels*; the percentage is arguably a
    **value** (what the zoom currently is) rather than a label (what the
    control does), and on that reading the criterion is not engaged and
    S3 passes too. Against that: it is the control's *only* visible text,
    so it is what a speech user sees and would say. **Recorded as a
    failure with the ambiguity stated** — the same treatment 2.5.1
    received before the reviewer ruled.
  - **Mitigating, and it caps the severity:** the value is dynamic, so no
    user could rely on it as a stable name in any case; and the control is
    reachable by every other means. One control of 64.
  - Classified: WCAG **2.5.3** / **Minor** → finding **V-F19**

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R042-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
