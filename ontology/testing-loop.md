# The Testing Loop

The interactive improve-loop between the **reviewer** (testing the product)
and the **assistant/system** (structuring results, tracking coverage, asking
the questions). Before the loop starts, the enclosure is usually mapped by
**assisted exploration** (`assisted-exploration.md`) — there the roles flip
and the assistant drives the browser. Capture mode: **hybrid** — the reviewer narrates freely; the
assistant maps narration to the checklist in the background and asks only
about gaps.

## The loop

```
next → log-test → narrate/observe → gap questions → write-back → reflect → next
```

1. **Pick the target.** `review.py next <review>` names the highest-value
   uncovered view×modality cell. Priority: cells whose modality verifies
   vendor-claim discrepancies (Does Not Support weighted over Partially
   Supports), then sample order. It prints the ready `log-test` command.
2. **Open the run.** `log-test` scaffolds `run.md` with that modality's
   checklist as an empty outcomes table — the empty rows are the session's
   question list. `--url` takes the **replicable locator**: a durable URL
   (transient params stripped; documents by `/id/urn:…` ID from the `03`
   §2.6 registry, never display name) or `UI: <action path>` for
   unaddressable states. If the target doesn't exist yet (a document the
   run will create), resolve the placeholder **in the same session** the
   artifact appears — `validate` flags unresolved locators.
3. **Reviewer narrates.** Test the page in any order and report what you see,
   free-form. No need to follow the checklist sequence.
4. **Assistant structures.** Each narrated item becomes a numbered
   observation (`O1, O2…`) in the run file; check outcomes fill in
   (pass / fail / partial / n/a) as narration covers them.
5. **Assistant asks gap questions.** Questions are generated from
   deterministic gaps, not improvisation — `review.py gaps <review> [--view
   S#]` prints exactly that list (every check row still without an outcome,
   grouped by run). Open a session with it; re-run it to see what is left:
   - a check row still empty → ask that check, quoting its text
   - a fail/partial without reproduction detail → ask for exact behavior
     (JAWS: paste the Speech History; WAVE: the summary counts)
   - an observation without a view state → ask which state
   - promotion to finding missing a required field (where / observed /
     affected users / WCAG SC / severity / evidence) → ask for that field
   - a screenshot-worthy moment without a file → ask for one
     (`R###-<what>.png`)

   **Do not re-interpret the reviewer's words into something stronger.**
   When a narrated phrase matches a checklist item's own wording, it is the
   answer to *that check* — not a finding in disguise. "Focus is not
   trapped" was an MO3 pass (you can always get out); the assistant read it
   as focus escaping an open modal and raised a Major 2.4.3 finding, which
   the reviewer's next sentence retracted. Ask what happened before writing
   what it means.

   **Ask before recording any assistant hypothesis.** On 2026-08-06 three
   assistant conclusions were wrong and all three were caught this way,
   costing one question each instead of a retraction in the report. A
   withdrawn finding in a delivered ACR is far more expensive than a
   question.
6. **Write-back.** The assistant updates, immediately, in this order:
   - the run's checks table and observations (with lifecycle status:
     `new → clarified → classified → finding:<ID> | dismissed`)
   - the run **Result** (derived: any Blocker-level fail → Broken; any fail →
     Works with issues; all pass → Works; no relevant content → N/A)
   - findings in `04-task-testing.md` §B (citing check ID, observation IDs,
     run ID, evidence files)
   - the criterion rollup in `05-results.md` (outcome + finding refs)
   - **the enclosure itself** in `03-scope-and-sample.md` when testing
     reveals unmapped views, states, or functionality — new S rows widen the
     matrix; corrected user stories reshape the tasks
7. **Reflect.** `matrix` and `validate` parse the same files, so coverage
   and the gap list update the moment the write-back lands. Then `next`
   again.

## Why the enclosure update matters

Step 6's last bullet is what makes this a genuine improvement loop rather
than checklist execution: what the reviewer tests changes the map, and the
map changes what is left to test. At the end of the review the corrected
enclosure is saved back to the library (`save-enclosure`) so the next review
of this product — or a similar product — starts from truth instead of
hypotheses.

## Reviewer session walkthroughs

When a batch of reviewer-driven work accumulates (JAWS runs, zoom checks,
confirmations of assistant-driven fails), the assistant generates a
**walkthrough**: `reviews/<id>/session-<sample>-reviewer-walkthrough.md` — an
ordered script of numbered steps (`W1, W2…`), each with **Do** (exact
actions/keystrokes), **Tell me** (what to narrate), why-it-matters context
for key steps, and a **Feedback** line. The reviewer works top to bottom
narrating freely; the assistant records feedback in place AND converts it
into the normal structures (run observations/outcomes, findings, rollup,
enclosure) in the same breath — the walkthrough is a capture surface, not a
new system of record. Steps that need a new run say so, and the assistant
logs it via `log-test` the moment the step starts. Close each walkthrough
with a check that every Feedback line is filled or the step explicitly
skipped.

### How to build one (the derivation is mechanical — no invention)

1. **Collect the open work for the sample** from the live sources, never
   from memory:
   - `review.py gaps <review> --view S#` — every unanswered check row for
     this sample, grouped by run. Start here: it is the walkthrough's
     backbone, and each row becomes a **Tell me** line.
   - `review.py validate` — runs without Results, missing WAVE sweeps
   - `scripts/view_probe.py` first — the instrument-answerable checks are
     written by measurement so the reviewer never verifies by hand what a
     structural fact already decides (modality-checks.md §Assistant-answerable)
   - `review.py matrix` — unrun view×modality cells for this sample
   - `review.py coverage` — criteria / POUR / 508-FPC with an answered check,
     and whether `05` agrees (the reliability flags)
   - `review.py next` — the priority rationale (vendor-claim discrepancies)
   - each run's `run.md` — check rows left empty or marked "reviewer",
     instrument caveats in Notes
   - `04-task-testing.md` — findings marked *pending reviewer confirmation*
   - `03-scope-and-sample.md` §2.6 — recon items ("verify X under check Y")
   - `03` §1.5 — tool versions still unrecorded
2. **Keep only reviewer-driven work.** Anything the assistant may drive
   itself (per `testing-tools.md` §Assistant-driven runs) is done by the
   assistant, not scripted for the human.
3. **Group into parts, one per instrument/run** (setup; JAWS run; zoom
   completion; keyboard confirmation; short one-off confirmations; new runs
   like WAVE/cognition last).
4. **Order by value**, the same priority `next` encodes: version-recording
   setup first (it unblocks the record), then vendor-claim discrepancies and
   recon-resolving steps early within their part, quick confirmations and
   fresh sweeps at the end.
5. **Write each step** from the modality checklist + tool conventions:
   `W#` + title naming the run/checks it feeds; **Do** with the exact
   keystrokes (JAWS: `H`/`R`/lists/Speech History; zoom: window width +
   `Ctrl+plus` to 400%; keyboard: reload-first-Tab, counts); **Tell me**
   asking for precisely what the check outcome needs; a why-it-matters line
   whenever the step confirms/refutes a pending finding or vendor claim
   (mark those **KEY STEP**); `**Feedback:** _(pending)_`.
6. **End with a close-out block**: the assistant's write-back duties, every
   Feedback line filled-or-skipped, `validate` re-run, and the
   next-target decision.

Regenerating an existing walkthrough (new open work accumulated): append new
`W#` steps or a dated section — never renumber or overwrite steps that
already carry feedback.

## Roles in one line each

- **Reviewer:** drives the product, narrates honestly, answers gap questions,
  drops screenshots into the run folder.
- **Assistant:** never loses a narrated fact; converts narration to
  structure; asks only what the structure still needs; keeps every dashboard
  truthful mid-session.
- **CLI:** deterministic memory — `next` (target), `log-test` (scaffold),
  `runs`/`matrix`/`status` (reflection), `validate` (the finish line).
