# Reviewer Session Walkthrough — Error paths (cross-cutting)

Built 2026-08-14 to close the **3.3.x error cluster**, which has stayed
Not Evaluated longer than anything else in this review. Targets:

| Criterion | Level | What it actually asks |
|---|---|---|
| **3.3.1 Error Identification** | A | When input is rejected, is the error **identified in text** — not by colour, an icon or a shake alone — and is the erroring field named? |
| **3.3.2 Labels or Instructions** | A | Do inputs carry labels/instructions **before** anything goes wrong? *(partly rolled up already — see below)* |
| **3.3.3 Error Suggestion** | AA | Does the message say **how to fix it**, not just that something is wrong? |
| **3.3.4 Error Prevention** | AA | For submissions that **delete or modify user data**, is the action reversible, checked, or confirmed? |

**Note on convention:** this is the review's first walkthrough that is not
scoped to a single sample — error paths cut across S1, S3 and S4. Named
`session-error-paths-…` rather than `session-S#-…` for that reason.

---

## Why this cluster is still open — read this first

**Adobe Express is a design tool, not a form application.** It has almost
no validated inputs: no checkout, no multi-field forms, no required-field
submissions. That is *why* five sweeps and ten reviewer sessions never
touched 3.3.x — nothing in normal use produces an error. The criteria are
not inapplicable, though; they are **unprovoked**.

So this session is different in kind from the others. Every previous
walkthrough asked *"what happens when you use the product?"* This one asks
*"what happens when you make the product fail?"* You have to go and break
things on purpose, which is why it needs its own script.

**Two outcomes are both fine, and one is not.** If a path produces a clean,
announced, text-described error → the criterion passes on that path. If a
path produces a silent or visual-only failure → that is a finding. What is
**not** acceptable is recording "Not Applicable" because we could not be
bothered to provoke it — 3.3.1 is only N/A if the product genuinely accepts
no user input anywhere, which is false (upload, rename, search, AI prompt,
share).

---

## Safety constraints — these bound the session

- **Do not actually delete anything.** W4 checks whether a confirmation
  step *exists*, then cancels. The four documents in Your stuff are the
  review's registry (03 §2.6) and are part of S4's tested state.
- **No purchases.** Premium upsell paths are out of scope; do not complete
  any transaction to provoke a payment error.
- **The assistant never authenticates.** W6 (sign-in errors) is yours alone
  if you choose to run it — deliberately mistyping your own password is
  safe, but it is your account and your call.

---

## W1 — Upload an invalid file (S1 Home, Upload card) — BEST STARTING POINT

**Why first:** the most reliable error generator in the product, on a
control already characterised (V-F2 lives on this same card), and it costs
nothing to trigger.

**Do:** From the Upload card, choose **browse** and pick a file the product
should reject — a `.txt`, a `.exe`, a `.zip`, or a deliberately huge file.

**Tell me:**
- Does anything happen at all, or does the file silently not appear?
- Is the failure **announced** by NVDA without moving focus?
- Is the message **in text**, and does it name **which file** and **why**?
- Does it say **what to do instead** (e.g. "use JPG, PNG or PDF")? That
  distinction is exactly 3.3.1 (identified) versus 3.3.3 (suggested).

**Feedback:** _(pending)_

---

## W2 — Rename a document to something invalid (S4 or the editor)

**Do:** Rename a document to an **empty string**, and then to something
with characters the product may reject (`/ \ : * ?`) or something absurdly
long.

**Tell me:** Is it rejected or silently accepted? If rejected, is the
rejection announced, and does the field keep your input so you can correct
it rather than retyping? (Losing the input is a 3.3.7 Redundant Entry
concern as well.)

**Note:** renaming is already known to work cleanly by keyboard (R016 O4) —
this is specifically about the **failure** case.

**Feedback:** _(pending)_

---

## W3 — Provoke an AI generation failure (S3 editor) — HIGHEST VALUE

**Why this one matters most:** "Generate with AI" is the product's most
promoted capability (03 §2.2 F8) and **already fails 4.1.3** — it announces
no progress, completion or failure (T2-F2). This step asks the sharper
question: when it *actually errors*, is the user told?

**Do:** Trigger a generation that will fail — an empty prompt, or one the
content policy will refuse.

**Tell me:** Is the refusal announced? Is it distinguishable **by ear**
from "still working" and from "finished"? Does it explain why?

**Why the answer is consequential:** if failure is silent, then for a
screen-reader user the product's flagship feature has **three
indistinguishable states**. That converts T2-F2 from "no completion
message" into something considerably worse.

**Feedback:** _(pending)_

---

## W4 — Deletion confirmation (S4 Your stuff) — 3.3.4, and DO NOT CONFIRM

**Do:** Begin deleting a file — the `sdcsdc` document, **not** the Kaiser
one and **not** the R038 test document — and go **only** as far as seeing
whether a confirmation appears. **Then cancel.**

**Tell me:** Is there a confirmation step at all? Is it announced as a
dialog (recall T2-F3 — the export dialogs were not)? Is the file it will
delete **named** in the confirmation? Is deletion reversible afterwards
(a trash/restore), which would satisfy 3.3.4 by a different route?

**Why 3.3.4 applies here:** the criterion covers submissions that modify or
delete **user-controllable data**. File deletion is squarely that, and it
is the only such path in the product — there is no checkout or legal
commitment in scope.

**Feedback:** _(pending)_

---

## W5 — Share to an invalid address (any view)

**Do:** Open Share and enter a malformed email (`notanemail`).

**Tell me:** Is it rejected, announced, and explained? Is the offending
field identified by name?

**Feedback:** _(pending)_

---

## W6 — Sign-in error (optional, yours alone)

**Do:** *Only if you want to.* Sign out and mistype your own password once.

**Tell me:** Is the failure announced and described in text? Does it
preserve your username so you are not re-entering everything (3.3.7)?

**Also relevant to 3.3.8 Accessible Authentication** — one of the six
criteria the vendor ACR never addressed: does sign-in require solving a
puzzle, transcribing a code, or recalling something, with **no alternative**
and no paste support?

**Feedback:** _(pending)_

---

## Optional assistant assist — provoking a network failure

If the above produce too few errors, I can put a page **offline** via CDP
in the debug window and you can watch what the product does when a save or
load fails. Say the word. Not scripted by default because an offline app
tends to fail in ways that are not representative of normal use.

---

## Close-out (assistant does)

- Run logged when you start; checks + observations written as you narrate
- Findings raised in `04`; 3.3.1/3.3.3/3.3.4 rolled up in `05`
- 3.3.2 already rolled up 2026-08-14 from existing evidence (see `05`)
- `validate` + `matrix` re-run
