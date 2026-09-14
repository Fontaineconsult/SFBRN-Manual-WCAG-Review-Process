# Per-View Modality Checks

The standardized "does this page work?" procedure, run for **each sensory /
functional modality on each sampled view** of the enclosure. Modalities here
follow the Section 508 **Functional Performance Criteria** (36 CFR 1194,
Chapter 3): they describe *how a user perceives and operates* — not the tool
used to test. Tools (JAWS, keyboard, zoom, WAVE — 03 §1.5) are the
instruments we use to verify a modality.

Task testing (04 §A) proves the flows work end-to-end; these checks prove
every individual view works in every modality. Same checklist every view,
every reviewer — that is what makes per-view verdicts reliable and comparable.

**The seven matrix modalities** (FPC collapsed where testing is identical):

| Modality ID | Section 508 FPC | Tested with |
|-------------|-----------------|-------------|
| `no-vision` | 302.1 Without Vision | JAWS (B1) |
| `low-vision` | 302.2 With Limited Vision | 400% zoom / reflow / text spacing (B3), contrast inspection |
| `no-color` | 302.3 Without Perception of Color | OS grayscale filter |
| `no-hearing` | 302.4 Without Hearing, 302.5 With Limited Hearing | Sound off; captions/transcript inspection |
| `no-speech` | 302.6 Without Speech | Inspection: no function requires voice input |
| `motor` | 302.7 With Limited Manipulation, 302.8 With Limited Reach and Strength | Keyboard only (B2); pointer-alternative inspection |
| `cognition` | 302.9 With Limited Language, Cognitive, and Learning Abilities | Structured inspection |

**How a check session runs:**

1. Log a run: `review.py log-test <review> --view S1 --modality no-vision
   --tool jaws --baseline B1`.
2. Work through that modality's checklist on the view, including significant
   states (menus open, dialogs, error states).
3. Set the run **Result** in its `run.md`: **Works** / **Works with issues** /
   **Broken** / **N/A** (no content relevant to this modality on this view —
   e.g., `no-hearing` on a view with no audio).
4. Record each failure as a finding in 04 §B citing the check ID and run ID.
5. `review.py matrix <review>` shows the views × modalities grid and gaps.

## no-vision — Without Vision (302.1)

Navigate with JAWS only, screen ignored: virtual cursor, headings (H),
landmarks (R), forms mode. Copy exact announcements from Speech History
(Insert+Space, H).

| ID | Check | WCAG |
|----|-------|------|
| NV1 | Page/view title identifies its purpose | 2.4.2 |
| NV2 | Headings and landmarks exist, are hierarchical, and support navigation | 1.3.1, 2.4.6 |
| NV3 | Every control announces an accurate name, role, and value/state | 4.1.2, 2.5.3 |
| NV4 | Images announce appropriate alternatives; decorative images are silent | 1.1.1 |
| NV5 | Reading order matches the meaning of the visual order | 1.3.2 |
| NV6 | Form fields announce labels and instructions (the visible label is the accessible name, or the name says the same thing) | 3.3.2 |
| NV7 | Dynamic updates (toasts, async results, validation) are announced without stealing focus | 4.1.3 |
| NV8 | Nothing is conveyed only by visual position, shape, or size | 1.3.3 |
| NV9 | Language of the view (and passages) is announced/pronounced from the correct language | 3.1.1, 3.1.2 |
| NV10 | Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | 2.4.4 |
| NV11 | Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | 1.2.3, 1.2.5 |
| NV12 | Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | 3.3.1 |

## low-vision — With Limited Vision (302.2)

Browser zoom 400% at a 1280px-wide window; text-spacing override applied;
contrast inspected (WAVE contrast data assists).

| ID | Check | WCAG |
|----|-------|------|
| LV1 | At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | 1.4.10 |
| LV2 | No content or functionality is lost at zoom; nothing overlaps or clips | 1.4.10, 1.4.4 |
| LV3 | The view tolerates text-spacing overrides without loss | 1.4.12 |
| LV4 | Text contrast ≥ 4.5:1 (3:1 for large text) | 1.4.3 |
| LV5 | UI component and meaningful graphic contrast ≥ 3:1 | 1.4.11 |
| LV6 | Content appearing on hover/focus is dismissible, hoverable, persistent | 1.4.13 |
| LV7 | Focus indicator remains visible and unobscured at zoom | 2.4.7, 2.4.11 |
| LV8 | The view works in both portrait and landscape | 1.3.4 |
| LV9 | Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | 1.4.5 |

## no-color — Without Perception of Color (302.3)

Apply the OS grayscale filter (Windows: Color Filters) and re-read the view.

| ID | Check | WCAG |
|----|-------|------|
| NC1 | Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | 1.4.1 |
| NC2 | Links are distinguishable from surrounding text without color | 1.4.1 |
| NC3 | Everything remains operable and understandable in grayscale | 1.4.1 |

## no-hearing — Without Hearing / With Limited Hearing (302.4, 302.5)

Sound off. **N/A** when the view has no audio or audio-video content.

| ID | Check | WCAG |
|----|-------|------|
| NH1 | Prerecorded video has accurate captions | 1.2.2 |
| NH2 | Live audio content has captions | 1.2.4 |
| NH3 | Audio-only content has a transcript | 1.2.1 |
| NH4 | No information or feedback is conveyed by sound alone (visual equivalent exists) | 1.1.1, 1.4.2 |

## no-speech — Without Speech (302.6)

Inspection. **N/A** unless the view offers voice input or voice-driven features.

| ID | Check | WCAG |
|----|-------|------|
| NS1 | No function requires speech input; any voice feature has a full non-speech alternative | — (FPC 302.6) |

## motor — With Limited Manipulation / Reach and Strength (302.7, 302.8)

Keyboard only — Tab/Shift+Tab, Enter, Space, arrows, Esc; plus inspection of
pointer interactions.

| ID | Check | WCAG |
|----|-------|------|
| MO1 | Every interactive element can be reached with the keyboard | 2.1.1 |
| MO2 | Every reached element can be operated (activate, select, dismiss) | 2.1.1 |
| MO3 | Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | 2.1.2 |
| MO4 | A visible focus indicator exists at all times | 2.4.7, 2.4.11 |
| MO5 | Focus order follows the meaning and operation order of the view | 2.4.3 |
| MO6 | Single-character shortcuts can be switched off or remapped | 2.1.4 |
| MO7 | Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | 2.5.7, 2.5.1 |
| MO8 | Pointer actions can be cancelled (up-event activation) | 2.5.2 |
| MO9 | Targets are ≥ 24×24 CSS px or adequately spaced | 2.5.8 |
| MO10 | Nothing requires device motion (shake/tilt) without an alternative | 2.5.4 |
| MO11 | A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | 2.4.1 |

## cognition — With Limited Language, Cognitive, and Learning Abilities (302.9)

Structured inspection of the view's demands on memory, language, and attention.

| ID | Check | WCAG |
|----|-------|------|
| CO1 | Navigation and component identification are consistent with the rest of the product | 3.2.3, 3.2.4 |
| CO2 | Help (if offered) appears in a consistent location | 3.2.6 |
| CO3 | Labels and instructions make the required input clear | 3.3.2 |
| CO4 | Errors suggest how to fix the problem | 3.3.3 |
| CO5 | Previously entered information is not demanded again | 3.3.7 |
| CO6 | Authentication does not require transcription or memorization (no cognitive-function test) | 3.3.8 |
| CO7 | Time limits are adjustable/extendable; moving content can be paused | 2.2.1, 2.2.2 |
| CO8 | Focus/input does not trigger unexpected context changes | 3.2.1, 3.2.2 |
| CO9 | Fields collecting the user's own information (name, email, address, phone, …) carry the matching `autocomplete` purpose so browsers and AT can fill them | 1.3.5 |
| CO10 | Each view is reachable in more than one way (navigation plus search, site map, index, or related links) unless it is a step in a process | 2.4.5 |
| CO11 | Submissions with legal, financial, or data-changing consequences are reversible, checked for input errors, or confirmable before commit | 3.3.4 |
| CO12 | Nothing flashes more than three times per second (photosensitive-safety check; WCAG-only — no 508 FPC counterpart) | 2.3.1 |

## Modality → WCAG map (the report's spine)

The consolidated view of the per-check tables above: which WCAG criteria
each sensory/functional modality exercises. `06-report.md` **must** report
findings sliced by this map (§Findings by sensory/functional modality) —
procurement reads in 508 FPC terms ("can a blind user…", "a deaf user…"),
not criterion numbers, and this table is what ties the two vocabularies
together. A criterion can serve several modalities; a finding is listed
under every modality whose users it affects.

| Modality | 508 FPC | WCAG criteria exercised (via checks above) |
|----------|---------|--------------------------------------------|
| no-vision | 302.1 | 1.1.1, 1.2.3, 1.2.5, 1.3.1, 1.3.2, 1.3.3, 2.4.2, 2.4.4, 2.4.6, 2.5.3, 3.1.1, 3.1.2, 3.3.1, 3.3.2, 4.1.2, 4.1.3 |
| low-vision | 302.2 | 1.3.4, 1.4.3, 1.4.4, 1.4.5, 1.4.10, 1.4.11, 1.4.12, 1.4.13, 2.4.7, 2.4.11 |
| no-color | 302.3 | 1.4.1 |
| no-hearing | 302.4, 302.5 | 1.1.1, 1.2.1, 1.2.2, 1.2.4, 1.4.2 |
| no-speech | 302.6 | — (FPC-only; any voice feature needs a non-speech alternative) |
| motor | 302.7, 302.8 | 2.1.1, 2.1.2, 2.1.4, 2.4.1, 2.4.3, 2.4.7, 2.4.11, 2.5.1, 2.5.2, 2.5.4, 2.5.7, 2.5.8 |
| cognition | 302.9 | 1.3.5, 2.2.1, 2.2.2, 2.3.1, 2.4.5, 3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.6, 3.3.2, 3.3.3, 3.3.4, 3.3.7, 3.3.8 |

### Completeness contract (enforced 2026-09-11)

**Every criterion in the WCAG 2.2 AA target (the 55 blocks of `05`) has at
least one check row above, and every check row maps to at least one
criterion or to a 508 FPC** (`NS1` is FPC-only; `CO12` is WCAG-only). That
is what makes "we tested for X" a property of the *process* rather than of
a reviewer's memory. `review.py validate` checks the map statically on every
run — a future edit that orphans a criterion (as happened before this date:
1.2.3, 1.2.5, 1.3.5, 1.4.5, 2.3.1, 2.4.4, 2.4.5 and 3.3.4 had no check row,
and 2.4.4 was already being cited in findings) fails validation until a row
is added. `review.py coverage <review>` then reports, per review, which
criteria / POUR principles / FPC have an **answered** check in a logged run.

**Adding or renaming a check row is a process change**: after editing this
file run `review.py sync-checks <review>` on every in-flight review so its
existing runs gain the new rows (blank, dated) instead of silently lacking
them; `validate` lists runs that are behind the checklist.

**One row, one kind of failure.** A row that bundles two criteria whose
failures are independent turns every fail into a false alarm on the other
criterion: until 2026-09-14 NV6 read "labels and instructions; errors are
announced and identified" and mapped to 3.3.1 + 3.3.2, so a label defect
(3.3.2) raised "failed check, 05 undecided" on 3.3.1, which nobody had
tested. Split it (NV6 labels → 3.3.2; NV12 errors → 3.3.1). When a fail
on a row could belong to only one of its criteria, split the row.

## Assistant-answerable checks (`scripts/view_probe.py`)

The reviewer's time goes to what only a person can judge. Every check that a
**structural fact about the view** decides is answered by the assistant first,
over CDP in the debug-profile Chrome, before the reviewer is asked anything:
`python scripts/view_probe.py <review> --view S# --url URL` (run it on every
sampled view as soon as the sample exists; then `gaps` lists only the human
rows). The probe writes into the cell's run — the latest run for that view ×
modality, or a new one logged with `--tool probe` — and never overwrites an
outcome a person entered. The reviewer completes that same run (updating
**Tool**/**Baseline** to the instrument actually used) rather than logging a
second run for the cell.

| Check | Fact the probe establishes | Answer it may write |
|---|---|---|
| NH1, NH2, NH3 | no `<video>`/`<audio>`/media embed, iframe or media link in the view or its same-origin frames | **n/a** (by absence); if media exists: nothing — the reviewer inspects captions/transcripts |
| NH4 | as above **and** no `Audio()`/`AudioContext` use in readable scripts | **n/a** |
| NV11 | no video/media embed | **n/a** |
| NS1 | no SpeechRecognition / getUserMedia / speechSynthesis use and no microphone/voice control | **n/a** |
| NV1 | `document.title` non-empty and not generic ("Untitled", a filename) | **pass** (wording confirmed on the NVDA walk); empty title → **fail** |
| NV9 | `<html lang>` present and well-formed / absent | **pass** / **fail** (pronunciation of foreign passages stays with the reviewer) |
| MO9 | every visible target ≥ 24×24 CSS px, or smaller ones spacing-exempt (no other target inside a 24 px circle), inline-in-text, or user-agent-sized checkbox/radio | **pass**; clashes → **fail** with the element list (reviewer rules on essential/equivalent exceptions) |
| MO10 | no devicemotion/deviceorientation use in scripts | **n/a** |
| LV1 | `scrollWidth` at 320 CSS px (≈400 % of 1280) ≤ 320, or overflow confined to data tables / canvas / images | **pass**; other overflow → **fail** with the widest elements |
| LV3 | text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) creates no newly clipped text container | **pass**; new clipping → **fail** with the containers |
| LV8 | no orientation media query and no `screen.orientation.lock` | **pass** |
| CO6 | no password field **and** no sign-in form | **n/a** (on a sign-in view: nothing — the reviewer judges) |
| CO9 | no field collects the user's own data; or all such fields carry `autocomplete`; or some lack it | **n/a** / **pass** / **fail** ("name"-only candidates are listed, not decided) |
| CO12 | no CSS animation, animated image, marquee/blink, canvas, SVG animation or video | **n/a** |

Everything else — reading order, names on focus, error announcement,
contrast, focus visibility, consistency, help, timing — needs the person and
is never answered by the probe. Facts it gathers but cannot decide (timer
text for CO7, "name" fields for CO9, unreadable cross-origin scripts) are
printed and saved in `<RID>-probe.json` so the reviewer starts from evidence.

**A measured fail is not a finding.** It is a `fail` outcome with the
measurement as its observation; the reviewer confirms it (or rules an
exception) before it is promoted in `04`. The run's Result stays unset and
names the outstanding rows, exactly as §Result semantics requires.

**Wrong-view guard.** The probe refuses when the tab lands on a different
path than requested (2026-09-11: `default2.aspx` silently redirected to
`default.aspx` and the first attempt measured the standard page under the
Accessibility Mode label). Views with no stable URL are reached through the
UI first and probed with a `UI: …` locator.

**Sign-in views.** Never navigate the authenticated tab to the product's
sign-in page — on Expert TA (2026-09-11) that ended the reviewer's session and
the assistant cannot restore it. Probe sign-in views in a second, signed-out
debug profile (testing-tools.md §view_probe).

## Coverage tracking — criterion, principle, FPC

The matrix (`review.py matrix`) tracks *views × modalities*. That is
necessary but not sufficient: a run can exist with half its checks blank,
and a `05` Outcome can be typed without any check behind it. Three views of
the same evidence are therefore kept, all computed live from the run files:

| Question | Command | Unit |
|---|---|---|
| Which views × modalities have a run? | `matrix` | cell |
| Which checks are still unanswered? | `gaps` | check row |
| Which **criteria**, **POUR principles** and **508 FPC** have an answered check, and does `05` agree? | `coverage` | criterion → principle / FPC |

`coverage` counts a criterion as **exercised** when at least one check
mapped to it carries `pass`, `fail`, `partial` or `n/a` in any logged run
(blank = not answered; anything else = unrecognised, reported). It then
rolls up by principle (1 Perceivable … 4 Robust) and by FPC (302.1–302.9
via the modality table at the top of this file), and flags:

- **outcome without evidence** — a `05` Outcome other than Not Evaluated on
  a criterion with no answered check (typed from memory or from a tool;
  either is a process violation);
- **failed check without rollup** — a `fail`/`partial` check on a criterion
  whose `05` Outcome is still Not Evaluated or Supports;
- **runs behind the checklist** — runs logged before a check row existed
  (fix: `sync-checks`);
- **FPC never exercised** — a modality with no answered check on any view.

`validate` raises each of these as an issue, so a review cannot reach FINAL
with a criterion, principle or FPC that was asserted but never checked.
`06` §Coverage & limitations and the WCAG-EM report's evaluation specifics
quote the `coverage` tables; §Findings by modality takes its "Coverage so
far" column from the FPC rows.

The unit of reliability is the **check row**: a criterion is only as
covered as the checks that cite it, on the views where they were answered.
`coverage` never infers a pass from silence — an unanswered check is a gap,
not a Supports.

## Supporting instrument — automated sweep (axe-core / WAVE)

Not a modality: the automated sweep is an instrument whose output feeds
several modalities (NV2–NV4, LV4–LV5, NC1, CO3). Every sampled view (and
significant state) gets one sweep run, logged with `--modality` unset.
**Primary instrument: axe-core** via `scripts/axe_scan.py` —
assistant-runnable, traverses open shadow DOM, saves raw JSON into the run
folder (`log-test --tool axe`, or let the script log the run itself).
**Secondary: WAVE extension** — reviewer-run; blind on shadow-DOM apps (see
testing-tools.md), use where it can parse (e.g., marketing pages).

| ID | Check |
|----|-------|
| W1 | Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |
| W2 | Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality |
| W3 | Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |

## Result semantics

- **Works** — every check in the modality's list passes on this view.
- **Works with issues** — one or more checks fail; each failure is a Minor or
  Major finding citing the check ID (e.g., `MO4`) and run ID.
- **Broken** — the view cannot be meaningfully used in this modality; at
  least one Blocker finding. A Broken cell on a view used by an essential
  task forces that task's verdict to Fail for the affected user group.
- **N/A** — the view has no content relevant to this modality (common for
  `no-hearing`, `no-speech`). Counts as covered in the matrix.
- **Not run** — initial state; the coverage matrix treats it as a gap.

**The case these five terms do not cover: no check failed, but a check is
unfinished.** It is the most common state in this review — an assistant
measured what an instrument can reach and one check needs the reviewer.
There is no term for it and one must not be invented: a run with an
incomplete check is **not** "Works" (that requires *every* check to pass)
and **not** "Works with issues" (that requires a failure and a finding).

Leave the Result **unset**, and replace the placeholder text with the
outstanding check and the instrument that closes it:

    | **Result** | Not set — NC2 (link hover/focus cues in grayscale) needs a reviewer pass; NC1/NC3 pass |

`validate` lists the run as resultless, which is correct — it *is*
unfinished — and `matrix` shows the cell as `run?`. An **n/a** check is
different: it is answered, not outstanding, so a run whose remaining checks
are pass + n/a closes as **Works**.

Write the outstanding check into the cell rather than leaving the generic
"Not set (→ Works / …)" placeholder. A bare placeholder tells the next
session nothing; naming the check turns the resultless-run list in
`validate` into an actionable reviewer to-do list.
