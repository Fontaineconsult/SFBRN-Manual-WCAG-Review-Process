# SFBRN Manual WCAG Review Process

A guided, reliable, repeatable manual accessibility review process for ICT
procured by the CSU Chancellor's Office. This is a procurement gate: the
review determines whether a product can enter the campus ecosystem. Each
review records procurement information, vendor contacts, test procedures, and
testing outputs, and produces a report with one of three decisions:

- **Approved** — the product may enter the campus ecosystem
- **Needs TAAP** — procurable only with a Technology Accessibility
  Accommodation Plan and a vendor remediation roadmap
- **Denied** — the product may not enter the campus ecosystem

- **Conformance target:** WCAG 2.2 Level AA
- **Methodology:** [WCAG-EM 2.0](ontology/wcag-em.md) (scope → explore → sample → audit → report)
- **Record structure:** ACR/VPAT 2.5, WCAG edition — outcomes use the ACR
  vocabulary (Supports / Partially Supports / Does Not Support / Not
  Applicable / Not Evaluated)

## The review CLI

Reviews are isolated: each one is a self-contained directory under `reviews/`
holding its stage files, evidence, and the vendor's ACR — nothing is shared
between reviews except the templates they were scaffolded from. The CLI is the
management interface (designed to be callable by people and by AI agents —
stable arguments, `--json` output, meaningful exit codes):

```
python scripts/review.py new "Product Name" [--enclosure NAME]
                                               # scaffold reviews/<YYYY-MM>-<slug>/
python scripts/review.py list                  # all reviews: decision, progress
python scripts/review.py status <review>       # stages, task verdicts, criteria counts
python scripts/review.py validate <review>     # completeness checks; exit 1 if issues
python scripts/review.py enclosures            # available enclosure templates
python scripts/review.py seed <review> --enclosure NAME
                                               # apply an enclosure to an existing review
python scripts/review.py save-enclosure <review>
                                               # save the documented enclosure for reuse
python scripts/review.py log-test <review> --view S1 --modality no-vision \
    --tool jaws --url URL --baseline B1        # log a test run; creates its evidence folder
python scripts/review.py runs <review>         # list logged test runs
python scripts/review.py matrix <review>       # views × modalities coverage grid
python scripts/review.py next <review>         # highest-value cell to test next
```

Testing runs as an interactive loop (`ontology/testing-loop.md`): `next`
picks the target (vendor-claim discrepancies first), `log-test` scaffolds the
run with its modality checklist, the reviewer narrates while the assistant
structures observations, asks gap-driven questions, and writes results back
into the run, findings, criterion rollup — and the enclosure itself when
testing reveals unmapped views.

Modalities are sensory/functional, per the Section 508 Functional Performance
Criteria: `no-vision`, `low-vision`, `no-color`, `no-hearing`, `no-speech`,
`motor`, `cognition`. Tools (JAWS, keyboard, zoom, WAVE) are the instruments
used to test them — per-view checklists in `ontology/modality-checks.md`.

`<review>` is the directory name or any unique substring (`adobe` matches
`2026-07-adobe-express`); enclosure names resolve the same way. `list`,
`status`, `validate`, and `enclosures` accept `--json`.

## Enclosures — starting a review blind

Reviews usually start without any map of the product. The `enclosures/`
library solves this:

- `enclosures/archetypes/` — generic starting points by product type
  (`web-app`, `creative-authoring-tool`, `content-site`, `lms`). Seeding a
  review pre-fills its scope file's Step 2 exploration tables (common views,
  user stories, sample types, technologies) and process skeletons with
  **hypotheses** the reviewer confirms, corrects, or deletes during
  exploration.
- `enclosures/products/` — product-specific enclosures saved from completed
  exploration via `save-enclosure`. Re-reviews and similar products seed from
  these instead of a generic archetype, so the library gets better with every
  review.

Each review contains:

| File | Stage |
|------|-------|
| `01-intake.md` | Procurement and product information |
| `02-vendor.md` | Vendor contacts and their ACR/VPAT |
| `03-scope-and-sample.md` | WCAG-EM steps 1–3: product enclosure, conformance target, accessibility support baseline, exploration (common views, essential functionality as user stories, sample types, technologies), structured + random sample, complete processes |
| `04-task-testing.md` | WCAG-EM step 4: testing clustered around tasks (user stories) — task verdicts (Pass / Pass with barriers / Fail) with findings that cite the WCAG criteria failed, plus a view sweep and random-sample comparison |
| `05-results.md` | Per-criterion rollup of task findings for all 55 WCAG 2.2 A/AA criteria, in VPAT/ACR table structure with vendor-claim comparison |
| `06-report.md` | Report: procurement decision (Approved / Needs TAAP / Denied) driven by task verdicts, task outcomes table, vendor-claim discrepancies, key findings, TAAP plan when required |
| `evidence/` | Test-run record: `test-log.md` index plus `runs/R###/` per session (run metadata, JAWS notes / WAVE counts, screenshots) — see `ontology/testing-tools.md` |
| `vendor-acr/` | The vendor's ACR/VPAT as received |

## Repository layout

- `CLAUDE.md` — agent operating manual, auto-loaded into every Claude Code
  session: session-start protocol, task routing to the ontology docs, hard
  rules, and the process-gap ratchet (agents fix the process doc they had to
  figure out, in the same session)
- `templates/review/` — the stage templates scaffolded into each review
- `enclosures/` — enclosure library: generic archetypes and saved product enclosures
- `reviews/` — one directory per review (the system of record)
- `ontology/` — reference documents converted from W3C sources
  ([WCAG-EM 2.0](ontology/wcag-em.md), [selecting evaluation tools](ontology/selecting-evaluation-tools.md))
  plus this process's own methods: the [testing loop](ontology/testing-loop.md),
  [modality checks](ontology/modality-checks.md), [testing tools](ontology/testing-tools.md),
  and [assisted exploration](ontology/assisted-exploration.md) (the assistant
  drives the browser during WCAG-EM step 2 and writes the map back into the
  enclosure)
- `tools/` — [searchable catalog](tools/wai-evaluation-tools.md) of the W3C
  WAI evaluation tools list (refresh with `python tools/update_tools_list.py`)
- `scripts/` — process automation (`review.py` — the review CLI;
  `import_acr.py` — parse a vendor's HTML ACR and fill the review's
  vendor-claim lines; `axe_scan.py` — per-view automated sweep: runs the
  vendored axe-core inside the authenticated Chrome session via the
  DevTools port and saves raw JSON into the run's evidence folder)
