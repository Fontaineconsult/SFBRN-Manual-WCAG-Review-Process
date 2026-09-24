# Test Run R121 — S14

| | |
|---|---|
| **Run ID** | R121 |
| **Date/time** | 2026-09-21 13:29 |
| **View / sample** | S14 |
| **Page URL / location** | https://login.theexpertta.com/ResetPassword.aspx |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B5 |
| **Tester** | Daniel Fontaine (reviewer, NVDA); assistant records |
| **Result** | Not set — NV2, NV3, NV4, NV5, NV6, NV7, NV8, NV10, NV12 need the reviewer (jaws, B1); measured fail on NV9 awaits confirmation |

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
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Expert TA - Reset Password" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | | |
| NV3 — Every control announces an accurate name, role, and value/state | pass | O8 — reviewer 2026-09-24, from the markup they supplied: the submit control carries `value="Request Reset"`, so it names itself; there is no other control on the page. Their ruling: "they are both accessible, just not best practice, we can pass them" |
| NV4 — Images announce appropriate alternatives; decorative images are silent | | |
| NV5 — Reading order matches the meaning of the visual order | pass | O8 — a single row of caption, field and button followed by the explanatory Note; the reviewer's ruling covers it |
| NV6 — Form fields announce labels and instructions (the visible label is the accessible name, or the name says the same thing) | fail | O5 — the user-name field carries no proper label; what the reviewer hears on tabbing in is the whole reset **table** read out. Usable, not labelled — the reviewer's ruling is "accessible, but not best practice" → V-F30 (Minor). Confirmed by axe `label` (critical, 1 node, R122) |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | | |
| NV8 — Nothing is conveyed only by visual position, shape, or size | pass | O8 — nothing on the page is identified by position alone |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | fail | O4 — <html> has no lang attribute (measured — 3.1.1) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | | |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | | |

**view_probe 2026-09-21:** answered NV11=n/a, NV1=pass, NV9=fail by measurement; facts in `R121-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-21 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-21 view_probe): document.title = "Expert TA - Reset Password" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-21 view_probe): <html> has no lang attribute (measured — 3.1.1)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → fail

- O5 [clarified] (state: Password reset page as loaded, `https://login.theexpertta.com/ResetPassword.aspx`, reviewer on NVDA, 2026-09-21): **"The form field for the user name in password reset isn't properly labeled, and like the rest of the app the whole reset form is structured in a table — tabbing into the form field launches a voice notification describing the whole reset table, so it is accessible, but not best practice."** The field has no label of its own; what the screen reader announces on focus is the surrounding layout table, from which the reviewer could work out what to type. The reviewer's ruling is explicit: **accessible, not a failure of the task** — the defect is the labelling, not the reachability. Independently confirmed by axe on the same page: `label` (critical) on one form element (R122).
  - Classified: NV6 / WCAG 1.3.1, 3.3.2, 4.1.2 / Minor (the reviewer's "not best practice") → finding **V-F30**; NV8 / partial (purpose carried by table position)
- O6 [measured] (state: as O5, 2026-09-21 view_probe): `<html>` on this page declares **no `lang`** attribute — the fourth page in the sample to do so, after Take Assignment (S3), Sign in (S7) and the Edit Class popup (S11).
  - Classified: NV9 / WCAG 3.1.1 / Minor → extends **V-F18** to S14
- O7 [measured] (state: as O5, 2026-09-21 view_probe): the page does not reflow — content still needs 1024 px at the 320 px viewport, the same fixed-width container as every other page.
  - Classified: LV1 (recorded on the low-vision run R123) / WCAG 1.4.10 → extends **V-F19** to S14

- O8 [clarified] (state: password reset and sign-in pages, reviewer 2026-09-24 — steps W75/W63): the reviewer supplied the **rendered markup of both pages** and ruled: **"they are both accessible, just not best practice, we can pass them."** Recorded as a pass on NV3, NV5 and NV8 for this view. The markup also settles the labelling question exactly, and the comparison is the useful part — see O9.
  - Classified: NV3, NV5, NV8 / pass
- O9 [measured, from the reviewer's markup] (state: as O8): **the two pages label the same field to two different standards.** Sign in writes `<label for="MainContent_UserName" id="MainContent_UserNameLabel"><strong>User&nbsp;Name:</strong></label>` — a correct, associated label. Password reset writes the identical caption as `<strong><font color="#3A7C89">User&nbsp;Name:</font></strong>` with **no `<label>` element at all**, sitting in the same `<td>` as `#MainContent_txtUserToRequest`, which carries no `aria-label`, `title` or `placeholder`. So the product already does this correctly one click away, on the page a user reaches this one *from*. That is what makes V-F30 an omission rather than a house style, and it is why the finding is worth keeping even under a "we can pass them" ruling — the fix is to copy the neighbouring page.
  - Classified: NV6 — the reviewer's pass stands on usability; the omission recorded against **V-F30**, whose severity is now a question for the reviewer (→ W76)
- O10 [measured, from the reviewer's markup] (state: as O8, on **both** pages): the Expert TA logo is `<a href="http://theexpertta.com/"><img src="/images/loginlogo.png" border="0" height="250px"></a>` — **an image with no `alt` attribute inside a link, and no `aria-hidden` on either**. Unlike the in-app header logo (V-F29, advisory) this one is not hidden from the AT, so it is a link whose accessible name is computed from nothing. This was not part of what the reviewer ruled on — they were answering the form question — so it is raised rather than passed → **V-F43**.
  - Classified: NV4, NV10 / → finding **V-F43**, awaiting the reviewer at W76
- O11 [measured, from the reviewer's markup] (state: as O8): both pages hold an **empty container waiting for a message** and neither is a live region — sign in has `<td align="center" colspan="2" style="color:Red;"></td>`, reset has `<span id="MainContent_lblOut"></span>`. There is no `aria-live`, `role=status` or `role=alert` on either, and sign in's required-field marker `<span title="User Name is required." style="visibility:hidden;">*</span>` is hidden from everything. So an error or a result message would appear as text with nothing to announce it — the same mechanism as V-F40 and V-F42. **NV12 is not answered by this**: it needs a submission to see what actually happens.
  - Classified: NV12 — still open; measured groundwork for it

## Notes

2026-09-21 — The reviewer walked the password reset page with NVDA and reported the labelling of the user-name field. The page had never been sampled: it was on record as part of the authentication surface (`03` §1 C1 and A3) but carried no view ID, so it is added as **S14** (proposed — the reviewer confirms the sample addition) and swept (axe R122) and probed the same day. Only NV6/NV8 come from the reviewer; NV1/NV9/NV11 are measured; the rest of the no-vision rows are still open.

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R121-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
