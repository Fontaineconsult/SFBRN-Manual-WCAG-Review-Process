# Test Run R041 — S4

| | |
|---|---|
| **Run ID** | R041 |
| **Date/time** | 2026-08-14 14:06 |
| **View / sample** | S4 |
| **Page URL / location** | UI: cross-cutting error-path probe across S1 Upload, S3 editor, S4 Your stuff (delete modal) and profile settings - session-error-paths-reviewer-walkthrough.md |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | reviewer (D. Fontaine) |
| **Result** | Works |

**Result reasoning** (set 2026-08-14). Nothing failed on any probed path.
The product's one destructive action — file deletion — is guarded by an
**announced** confirmation modal with an explicit cancel (O2, O3), which
satisfies 3.3.4. No input-error path was found to exist at all (O1), which
makes 3.3.1 and 3.3.3 Not Applicable rather than unevaluated. **Scope
note:** this is a cross-cutting probe run, not a view sweep of S4 — it is
filed against S4 because the substantive evidence (the delete modal) lives
there.

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

Cross-cutting error-path probe per
`session-error-paths-reviewer-walkthrough.md`. Targets 3.3.1, 3.3.3, 3.3.4.

- **O1 [classified]** (3.3.1 / 3.3.3 — reviewer, 2026-08-14): *"It is not
  clear to me where I would produce a failure; it doesn't seem any of the
  functionality here would allow a wrong input."*
  - **This is the applicability answer, and it has a clean logical basis.**
    3.3.1 is conditional: it applies *"if an input error is automatically
    detected."* 3.3.3 is conditional on the same trigger. A product that
    detects no input errors engages neither — they are **Not Applicable**,
    not failed and not unevaluated.
  - **Consistent with everything else on file.** Express has no checkout,
    no multi-field forms, no required-field submissions and no validated
    text entry. Its inputs are a search box (accepts any string), a
    document-name field (accepts any string), an AI prompt (accepts any
    string) and a file picker. Ten reviewer sessions and five automated
    sweeps have never surfaced an error message of any kind — which until
    now read as a coverage gap and is better explained as an absence.
  - **One probe would firm this from "none found" to "none exists", and it
    is named rather than assumed:** uploading a file the product should
    reject — a `.exe`, a `.zip`, or something oversized. If that is refused
    with a message, 3.3.1/3.3.3 become live and this entry is superseded.
    Recorded as the specific thing that would change the outcome.
  - Classified: WCAG **3.3.1**, **3.3.3** / **Not Applicable** — no finding

- **O2 [classified]** (3.3.4, file deletion — reviewer): **deleting a file
  uses a modal, which is announced and provides a cancel / delete
  option.**
  - **3.3.4 is satisfied by the "Confirmed" mechanism.** The criterion
    offers three routes — Reversible, Checked, or Confirmed — and requires
    only one. A confirmation step with an explicit cancel is exactly the
    third. File deletion is also **the only path in scope** that modifies
    or deletes user-controllable data: there is no checkout, no legal
    commitment and no test submission in this product.
  - **A genuine positive, and the review should say so.** This is the
    product's most destructive action and it is properly guarded.

- **O3 [classified]** — **the delete modal is announced, and that is a
  direct counter-example to T2-F3.** The export popover and the download
  dialog announce as *nothing* (R037 O1/O4); this dialog announces as a
  dialog. **Same product, same component library, opposite outcomes.**
  - This is the review's recurring shape — *the capability exists and is
    applied unevenly* — appearing for a fifth time (alongside: text
    insertion announces but image insertion does not; the layers list is
    named but 17 other grids are not; documents retitle but views do not;
    captions exist but audio description does not).
  - **It materially strengthens remediation item 20.** A vendor cannot
    argue that announcing the export dialogs is difficult when their own
    delete dialog already does it. Reclassify item 20 from "add a missing
    behaviour" to "apply an existing internal pattern consistently".
  - Classified: supporting evidence for **T2-F3** and exhibit item 20 — no
    new finding

- **O4 [classified]** (3.3.4, profile name — reviewer): *"only user data is
  profile name, which is editable but no undo."*
  - **Assessed and does not change the outcome.** Editing a profile name
    is a modification of stored user data, but it is **reversible by the
    user in the ordinary way**: the previous value was chosen by them and
    can simply be re-entered. 3.3.4's "Reversible" route is satisfied
    without a dedicated undo. Contrast file deletion, which without a
    trash would be irreversible — and which is separately confirmed (O2).
  - Recorded because the reviewer raised it and a later reader may ask the
    same question; the absence of undo is noted, and judged not to defeat
    the criterion.
  - Classified: WCAG **3.3.4** / **Supports** — no finding

- **O5 [classified]** (authentication scope — reviewer, 2026-08-14): *"my
  sign in is via SSO, which is accessible; can't test Adobe's directly."*
  - **This is a scoping fact, and it resolves 3.3.8 and 3.3.7 by
    determining what is on the path rather than by testing.** In this
    deployment the authentication a user performs belongs to the
    **institution's identity provider**, not to Adobe Express. The IdP is
    a **different product**, outside the boundary this review declares
    (03 §1.1 — authenticated app content at `new.express.adobe.com`);
    assessing it would be a separate review with its own sample.
  - **Adobe's native sign-in is therefore untested and untestable here.**
    Not because it was skipped, but because the reviewer cannot reach it
    without leaving the deployment configuration under review — and the
    assistant never authenticates in any case (CLAUDE.md).
  - **The residual is real and belongs in the report, not buried in a
    run.** Any campus that adopts Express **without** SSO puts users on
    Adobe's own authentication, which **no evidence in this review
    touches** — and which the vendor's ACR **never claimed**, since 3.3.8
    is one of the six WCAG 2.2 additions absent from their 2023 document.
    So for that configuration there is neither independent evidence nor a
    vendor assertion: a genuine blind spot, and the only one in the review
    where *nothing at all* is known.
  - **Actionable consequence:** this converts cleanly into a procurement
    question rather than a test — require Adobe to state a 3.3.8 position
    for Adobe ID sign-in, and make SSO the assumed deployment mode.
  - Classified: WCAG **3.3.8**, **3.3.7** / **Not Applicable** to this
    review's scope, with a recorded residual — no finding

- **O6 [classified]** (MO8 / 2.5.2 Pointer Cancellation — reviewer,
  2026-08-14): **"no, large random sample, no issue."** No down-event
  activation on any control tested; press-and-drag-off aborts the action,
  which is the abort mechanism the criterion requires.
  - **Worth testing rather than assuming.** Standard HTML buttons satisfy
    2.5.2 by default, but this product's interactive layer is almost
    entirely **custom Spectrum web components** — `sp-button`,
    `sp-action-button`, `x-toolbar-button`, `hz-sortable-list` — the same
    family behind V-F4, V-F10, V-F12 and T2-F4. A custom component binding
    its handler to `pointerdown` is a realistic defect in exactly this
    codebase, and **the sample size is what makes the negative result
    carry weight**: one or two controls would not have.
  - **This is the review's final criterion.** With it, all 55 WCAG 2.2 A+AA
    criteria in scope have an outcome.
  - Classified: MO8 / WCAG **2.5.2** / **Supports** — no finding

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R041-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
