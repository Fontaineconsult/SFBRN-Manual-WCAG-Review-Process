# Archived reviews

Reviews here are **complete and on the record, but they predate the current
process** and must not be copied as examples.

## 2026-07-adobe-express (archived 2026-09-30)

Ran before three contracts that now govern every review:

- **`Plain summary`** on every finding (23 of its findings have none)
- **`Remediation`** on every published criterion (14 missing)
- the **SQLite mirror** and its integrity checks (15 findings are not rolled
  up into `05`; 2 blocks cite withdrawn findings)

It also carries the pre-2026-09-25 decision vocabulary, and its
`06-report.md` is a hand-written narrative report — the artifact the process
replaced with two generated ones.

`review_db.py check` reports 72 issues against it. That is expected and is
not a defect in the review: it is what a 2026-07 review looks like measured
by a 2026-09 contract. Its evidence and run IDs are still cited by
`ontology/testing-tools.md`, which is why it was archived rather than
deleted.

**For a worked example, read `reviews/2026-09-the-expert-ta`.**
