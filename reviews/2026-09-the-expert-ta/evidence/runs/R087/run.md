# Test Run R087 — S8

| | |
|---|---|
| **Run ID** | R087 |
| **Date/time** | 2026-09-11 14:13 |
| **View / sample** | S8 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/ViewAssignmentSolutionsV2.aspx?z=1&vmid=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | probe; nvda (reviewer, W58) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-21, every row answered. This is the best-built page in the sample for a screen reader: a real heading outline per problem (NV2), controls that name themselves, a sensible reading order, nothing carried by position, a clean link inventory, and MathJax that voices correctly. One row fails and it is the content — the worked figures have no text alternative (V-F35), and on 7 of them the markup shows alternative text was written and lost to a missing quote. So a screen-reader user navigates this page well and reaches an explanation they cannot read. Works with issues rather than Broken: the solution text and the mathematics are available, which is more than the grade report can say.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "View Assignment Solutions" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | pass | O5 — reviewer 2026-09-21: **"headings work"**. Measured: 10 headings, `h1` for the assignment and one `h2` per problem ("Problem 1 - 5.3.5(iFBD)" …). **The only view in the sample with a real heading outline** — the counter-example that shows the product can do it |
| NV3 — Every control announces an accurate name, role, and value/state | pass | O8 — reviewer 2026-09-21: "generally yes, controls announce name and role". The unnamed **images** are not an exception to this row — they are a missing text alternative (NV4, V-F35), not a control without a name |
| NV4 — Images announce appropriate alternatives; decorative images are silent | fail | O6 — "graphics have no meaningful alt text, just random characters are announced". Measured: 14 of 15 images carry **no `alt` attribute at all**, so NVDA falls back to the file name (`zbrvxxz3.j3f.png`) — the "random characters". **7 of them show why**: the markup is `src="/images/….png alt="` — an `alt=` swallowed into the `src` by a missing quote → V-F35 |
| NV5 — Reading order matches the meaning of the visual order | pass | O8 — reviewer 2026-09-21: "there is a sensible order". With the heading outline working (NV2), the page reads problem by problem as it looks |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | n/a | O7 — measured 2026-09-21: no visible input, select or textarea on the view; it is a read-only solutions page |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | n/a | O8 — reviewer 2026-09-21: "this page seems static, so no reloads". A read-only solutions page: no form fields (O7), nothing that updates without a navigation |
| NV8 — Nothing is conveyed only by visual position, shape, or size | pass | O8 — reviewer 2026-09-21: "nothing only id by position". The heading per problem is what makes this true here and false on the other views |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | pass | O9 — measured 2026-09-21 and consistent with the reviewer's "controls announce name and role": 10 visible links, every one with a distinct descriptive name, **no** bare "click here"/"more"/"view", and **no** text pointing at two different targets. The assignment and class links even name what they open ("Open Assignment Chapter 5 Sample Assignment") |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | O7 — measured: no form fields, so no validated input to submit |
**view_probe 2026-09-11:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R087-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): document.title = "View Assignment Solutions" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass

- O5 [clarified] (state: View Assignment Solutions, NVDA, reviewer 2026-09-21 — step W58): **"headings work"**, and **"math expressions on this page voice as expected"**. Measured alongside: 10 real headings (`h1` + one `h2` per problem) and 402 MathJax nodes. Both matter as counter-examples rather than defects. This is the **only** view in the sample with a heading outline, so V-F1's recommendation is not a request for something the vendor has never done — it is a request to do elsewhere what it already does here. And the math reading contrasts with Take Assignment: the MathJax itself is fine in browse mode (V-F10 was withdrawn on that basis); what fails there is the `Ctrl+Shift+2` answer read-back (V-F9), not the notation.
  - Classified: NV2 / pass; math — no finding, recorded as the positive control for V-F9/V-F10
- O6 [clarified + measured] (state: as O5): **"graphics have no meaningful alt text, just random characters are announced an 'unlabled graphic clickable'."** Measured: **15 images, 14 of them with no `alt` attribute whatsoever**, which is why the screen reader reads the file name — `zbrvxxz3.j3f.png`, `22tfvbot.c0p.png` — the "random characters". The cause is visible in the markup and is a **typo, not a policy**: 7 of the images are written `src="/images/zbrvxxz3.j3f.png alt="`, an `alt=` attribute swallowed into the `src` value by a missing quote. The author intended alternative text; the browser never sees an `alt` attribute at all. This confirms with the reviewer's AT what R014 flagged as "broken `alt=` markup" on 2026-09-10.
  - Classified: NV4 / WCAG 1.1.1, 4.1.2 / Major → finding **V-F35**
- O7 [measured] (state: as loaded, 2026-09-21): no visible input, select or textarea on the view.
  - Classified: NV6 / n/a; NV12 / n/a

- O8 [clarified] (state: View Assignment Solutions, NVDA, reviewer 2026-09-21 — step W58, the five rows left open): **"Generally yes, controls announce name and role, there is a sensible order, this page seems static, so no reloads, nothing only id by position."** NV3, NV5 and NV8 pass; NV7 is n/a on a static read-only page. The heading outline (O5) is what makes NV8 true here and false elsewhere — on the other views the only thing telling one block from another is where it sits.
  - Classified: NV3 / pass; NV5 / pass; NV7 / n/a; NV8 / pass
- O9 [measured] (state: as loaded, 2026-09-21): link inventory — **10 visible links, every one with a distinct descriptive accessible name**; no bare "click here", "more", "view" or empty name; no text pointing at two different targets. Two of them name their destination in full ("Open Assignment Chapter 5 Sample Assignment", "Open Class Testing Course for CSU East Bay"). These are the same two title-line links W41 asks about visually — worth noting that their *names* are sound and only their *appearance* is in question (1.4.1, not 2.4.4).
  - Classified: NV10 / WCAG 2.4.4 / pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R087-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
