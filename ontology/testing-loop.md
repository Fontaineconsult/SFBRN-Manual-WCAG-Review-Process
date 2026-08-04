# The Testing Loop

The interactive improve-loop between the **reviewer** (testing the product)
and the **assistant/system** (structuring results, tracking coverage, asking
the questions). Capture mode: **hybrid** — the reviewer narrates freely; the
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
   question list.
3. **Reviewer narrates.** Test the page in any order and report what you see,
   free-form. No need to follow the checklist sequence.
4. **Assistant structures.** Each narrated item becomes a numbered
   observation (`O1, O2…`) in the run file; check outcomes fill in
   (pass / fail / partial / n/a) as narration covers them.
5. **Assistant asks gap questions.** Questions are generated from
   deterministic gaps, not improvisation:
   - a check row still empty → ask that check, quoting its text
   - a fail/partial without reproduction detail → ask for exact behavior
     (JAWS: paste the Speech History; WAVE: the summary counts)
   - an observation without a view state → ask which state
   - promotion to finding missing a required field (where / observed /
     affected users / WCAG SC / severity / evidence) → ask for that field
   - a screenshot-worthy moment without a file → ask for one
     (`R###-<what>.png`)
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

## Roles in one line each

- **Reviewer:** drives the product, narrates honestly, answers gap questions,
  drops screenshots into the run folder.
- **Assistant:** never loses a narrated fact; converts narration to
  structure; asks only what the structure still needs; keeps every dashboard
  truthful mid-session.
- **CLI:** deterministic memory — `next` (target), `log-test` (scaffold),
  `runs`/`matrix`/`status` (reflection), `validate` (the finish line).
