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
python scripts/review.py coverage <review>     # criteria → POUR principles → 508 FPC: which have an
                                               # answered check, and whether 05 agrees (reliability flags)
python scripts/review.py sync-checks <review>  # add check rows introduced after a run was logged
python scripts/review.py next <review>         # highest-value cell to test next
python scripts/review.py gaps <review> [--view S1]
                                               # unanswered check rows — the session's question list
python scripts/view_probe.py <review> --view S# --url URL [--dry-run]
                                               # answer the instrument-decidable checks of a view by
                                               # measurement (media absent → n/a, lang, title, target size,
                                               # reflow, text spacing, autocomplete) into its runs
python scripts/cdp_probe.py [URL] [--ax] [--shot PNG] [--js EXPR] [--key K --ctrl --shift]
                                               # per-view exploration probe over CDP: frames, text, controls,
                                               # accessibility-tree summary, screenshot, real key chords
python scripts/crawl_map.py harvest|map URL... [--out FILE]
                                               # enclosure mapping over CDP: harvest candidate links,
                                               # fingerprint allowlisted views (never auto-follows —
                                               # see ontology/assisted-exploration.md)
python scripts/review_db.py sync --all|<review>   # rebuild the review's database reviews/<id>/<id>.sqlite from its files (byte-stable)
python scripts/review_db.py state <review> [--log]   # review state dashboard from the database: definition of done,
                                               # POUR / FPC / matrix / findings / vendor delta / what moves the needle;
                                               # repeatable (same files → same text); --log appends a row to state-log.md
python scripts/review_db.py completion <review>   # the definition of done, measured in the database (C1–C12)
python scripts/review_db.py check <review>     # integrity queries: finding ↔ 05 rollup, withdrawn-but-cited,
                                               # runs cited that don't exist, Works with blank/failed checks …
python scripts/review_db.py query "SELECT …" --review <r> | --all   # read-only SQL over criteria / checks / runs / outcomes / findings
python scripts/review_db.py criteria [--level AA] [--principle 2]
python scripts/export_report.py <review> [--out PATH]
                                               # render 06-report.md as a styled .docx (real heading
                                               # styles + tables; needs `pip install python-docx`)
python scripts/export_report.py <review> --format wcag-em
                                               # (planned) render the org-neutral WCAG-EM report
                                               # (templates/review/wcag-em-report.html) from 01/03/05/06
```

Testing runs as an interactive loop (`ontology/testing-loop.md`): `next`
picks the target (vendor-claim discrepancies first), `log-test` scaffolds the
run with its modality checklist, the reviewer narrates while the assistant
structures observations, asks gap-driven questions, and writes results back
into the run, findings, criterion rollup — and the enclosure itself when
testing reveals unmapped views.

`gaps` is the loop's question list made explicit: `validate` reports which
*runs* lack a Result, `gaps` reports which *checks* are still unanswered —
the rows a reviewer session actually works through, grouped by run. Use it
to open a session (`gaps <review> --view S1`) and to see what a walkthrough
still needs.

**Findings come from the reviewer's testing.** Automated sweeps are
supporting instruments: every violation is human-confirmed into a finding or
dismissed in writing, and every `incomplete` is routed to a modality check.
A scan result is never itself a finding.

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
  exploration. Seeding replaces §2.1–2.5 and the process skeletons; the
  template's §2.6 exploration notes (recon) block is kept, and
  `save-enclosure` strips it again, because recon is review-specific.
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
| `06-report.md` | **Independent verification report** (not a VPAT/ACR — see `ontology/reporting.md`): procurement decision (Approved / Needs TAAP / Denied) driven by task verdicts; RFP-comparable "At a glance" box; key findings by user impact with root causes; **vendor ACR audit** (coverage + reliability, both directions); contract-ready remediation exhibit; coverage/limitations honesty box; TAAP inputs when required. `05-results.md` remains the ACR-shaped technical appendix. |
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

## Continuing on another machine

Everything the review needs is in the repo: the stage files, the runs and
their evidence, the walkthrough, the state log, and the review's database
(`reviews/<id>/<id>.sqlite`, committed and byte-stable — a sync on a machine
whose files are identical leaves it untouched). What is *not* in the repo,
and must exist on the machine:

1. **Python 3.10+** and `python -m pip install -r requirements.txt`.
2. **The debug-profile Chrome** — launch with the full flag set in
   `ontology/testing-tools.md` §axe-core (the profile directory is created on
   first launch), then **sign in once in that window** with the review's
   account; the assistant never authenticates. Products with a one-session
   rule (Expert TA) must not be open in another browser at the same time.
3. **The screen reader** for reviewer sessions (NVDA/JAWS, versions in
   `03` §1.3/§1.5).

First commands on the new machine, from the repo root:

    python scripts/review_db.py state <review> --log   # where things stand, from the database
    python scripts/review.py validate <review>         # [md] extraction health, [done], [db]
    python scripts/review.py gaps <review> --view S#   # the reviewer's question list

The `.sqlite` will show as modified after the first sync only if the
markdown differs from what built it — commit it together with the markdown.
