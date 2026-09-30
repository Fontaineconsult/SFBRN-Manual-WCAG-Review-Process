# The Testing Loop

The interactive improve-loop between the **reviewer** (testing the product)
and the **assistant/system** (structuring results, tracking coverage, asking
the questions). Before the loop starts, the enclosure is usually mapped by
**assisted exploration** (`assisted-exploration.md`) — there the roles flip
and the assistant drives the browser. Capture mode: **hybrid** — the reviewer narrates freely; the
assistant maps narration to the checklist in the background and asks only
about gaps.

## The loop — one page at a time

```
next → automate → gaps --view → reviewer walks → write-back → close-page → next
```

**The unit of work is a page, not a view×modality cell.** Ranking cells sent
sessions hopping between pages and left every page half-walked; the reviewer
pays for that twice, once in context-switching and once in re-reading a page
they have already been through. `next` names a page, prefers one already
started, and will not call the review finished while a task cluster is unrun.

1. **Pick the page.** `review.py next <review>` names it and lists what is
   open on it. `review.py page <review> --view S#` is the same page in full:
   every modality, its run, its Result, its unanswered checks, and whether the
   sweep's raw JSON is on disk.

2. **Automate before you ask the reviewer anything.** This is the step that
   decides how much of their time the review costs.
   - `python scripts/axe_scan.py <review> --view S# --url URL` — logs the
     sweep run, saves `R###-axe.json`, and **writes an observation per
     violation and per incomplete**, each with the WCAG criteria taken from
     axe's own rule tags. It does not answer W1 or W3: transcription is
     automatable, confirmation is not.
   - `python scripts/view_probe.py <review> --view S# --url URL` — answers by
     measurement what a structural fact decides (~17 check rows: title, lang,
     media, speech API, target size, reflow, text spacing, autocomplete,
     orientation, and NC2 by colour measurement) and names the rest.
   - Never point the authenticated tab at the sign-in page — it ends the
     session. Sign-in views go through the signed-out profile on port 9223.

3. **Ask only what is left.** `review.py gaps <review> --view S#` prints every
   check row on that page still without an outcome, across every modality,
   **whether or not a run exists yet**. That is the session's question list;
   never improvise one, and never ask something the record already answers.
   The list is annotated with the sweep: under every check whose criteria
   match an axe observation on that page, `gaps` prints `← R### O#: axe
   violation|incomplete rule ×nodes`, and under W1/W2 it lists the
   observations each row has to triage. Read the annotated list *before*
   the walk — it is the structure of the session: the instrument's hits are
   the first things to confirm or dismiss on that page, and the checks with
   no annotation are where only the walk can see (added 2026-09-30, after
   the reviewer asked why the sweep was not shaping the manual review).

4. **The reviewer walks the page and narrates.** Free-form, any order. The
   assistant converts narration into numbered observations, answers check
   rows, and asks a gap question when a row is still open — quoting the
   check's own wording.

   **Do not re-interpret the reviewer's words into something stronger.** When
   a narrated phrase matches a checklist item's own wording, it is the answer
   to *that check*, not a finding in disguise.

   **Ask before recording any assistant hypothesis.** A question costs one
   exchange; a withdrawn finding in a delivered report costs far more.

5. **Write back immediately**, in this order: the run's checks and
   observations → the run **Result** (`review.py close-run`) → findings in
   `04` §B → the rollup in `05` → the enclosure in `03` when testing reveals
   views or functionality the map missed.

6. **Close the page.** `review.py close-page <review> S#` refuses, with
   reasons, until every modality has a resulted run, every check row is
   answered, and the sweep is triaged with its JSON on disk. **Do not open
   the next page until it passes.**

**Then the tasks.** When every page is closed, `next` names the task clusters
still to walk (`04` §A). A review that only ever swept views has not done the
work — the reports' task verdicts, and the internal report's "core
functionality" line, come from there and nowhere else.

**Finally**, regenerate both reports: C13 fails while either is stale.

## Closing a run (`review.py close-run`)

A run's Result is set with the CLI, never by hand:

    python scripts/review.py close-run <review> R007 \
        --result "Broken" --reason "..." \
        --answer "W1=pass=how each violation was confirmed or dismissed" \
        --answer "W3=pass=what the cross-check against the walk found"

It writes the bare term into the Result cell (`matrix` matches that cell
against the exact strings and prints anything else verbatim, which blew the
grid apart on 2026-08-14), puts the sentences in the `**Result reasoning.**`
paragraph under the table where there is no length limit, answers the named
check rows, and resyncs the database. `--answer-open <outcome>` answers every
still-blank row the same way, for a run being closed wholesale.

**Why it exists.** On 2026-09-24 the review carried 47 runs at "Not set" and
243 unanswered check rows, and the definition of done counted every one. The
split, once queried, was:

- **35 runs and 217 rows against views that had left the sample.** Six views
  were withdrawn on 2026-09-15 as not student-facing; their probe and axe runs
  stayed on record at "Not set". These can never be finished — the page is out
  of scope — so they close as **N/A with the withdrawal as the reason**, and
  their open rows as `n/a`. The measurements stay in the folder and can be
  reopened unchanged if scope is ever extended.
- **Eight sweeps whose violations the later walks had already resolved.** W1
  ("every reported failure is human-confirmed → finding, or dismissed with a
  written reason") and W3 (structure cross-checked against the screen-reader
  walk) were left open on eight axe runs while the findings they point to were
  raised and rolled up months later. Closing them is bookkeeping against
  evidence that exists — but it is bookkeeping that must name, per violation,
  which finding took it or why it was dismissed. Two of the eight had their
  axe output saved and never written up as observations at all; those were
  written first, from the saved JSON, then closed.
- **Eight rows that genuinely needed a page in front of someone.**

**The rule the split teaches.** A predicate that counts work against withdrawn
scope reports a backlog that does not exist. C6 and C7 scope to the sample and
were right; C4 and C5 count every run and every row, and were reporting 47
outstanding when the honest number was 12. Rather than narrow the predicates —
which would have left 35 runs looking permanently unfinished — the runs are
closed and say why. **The record states what happened; the predicate counts
it.**

**What close-run must never do.** Invent an outcome. Every note it writes
names its basis: a finding ID, a walk's run ID, a measurement, or an explicit
statement that the answer is generalised from another view and on what
grounds. Generalising a *failure* across views that share a style is something
the reviewer has authorised; generalising a *pass* needs the pages to be the
same template, and the note says so.


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
   **A resumed page states what is already recorded.** When a step returns to
   a view that was partly walked before, the step — and any task list built
   from it — says how many rows are already answered, and *why* the remainder
   is open (a step skipped on the day, a row added later by `sync-checks`, a
   question routed elsewhere). 2026-09-21: the reviewer was handed "Class
   Management, Accessibility Mode — 3 rows" and read it as being asked to redo
   a walk they had finished on 2026-09-10. Nine of the twelve rows *were*
   recorded; the run file said so ("not narrated (W6 skipped)"), but the task
   list did not carry it. Row counts without that history look like lost work.
   **Name the page in words, every time** (learned 2026-09-14: the reviewer
   answered "I don't know what S1 S2 S3 S4 means" to a confirmation list
   written in view codes). View IDs are the process's bookkeeping, not the
   reviewer's vocabulary: every **Do** says *which page and which state* —
   "Class Management in standard mode (`/common/default.aspx`, the button
   reads 'Accessibility Page')", "Take Assignment → Problem 8" — with the
   S# in brackets after it, never alone. A confirmation of a **measured
   fail** carries the reproduction recipe inside the step (window width,
   zoom level, the bookmarklet text to paste, which element to look at, and
   what "fail" looks like) — "confirm the reflow fail" and "target size" are
   not instructions ("I don't know what that means" is the reviewer's
   correct answer to them). Test: could a reviewer who has never seen the
   scope file reproduce the finding from the step alone?
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
