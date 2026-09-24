r"""export_acr.py — an independently-verified ACR, rendered from the database.

    python scripts/export_acr.py <review> [--open] [--out PATH]

Writes reviews/<id>/<id>-acr.html: a VPAT(R) 2.5-shaped Accessibility
Conformance Report built **entirely from reviews/<id>/<id>.sqlite**.

Why this exists, given ontology/reporting.md says "Not a VPAT/ACR --
deliberately" (2026-08-10)
--------------------------------------------------------------------------
That section rules out shaping the *review report* (`06`) like an ACR, and
its reasons still hold: `06` carries a procurement decision, an audit of the
vendor's own ACR, and contract-ready remediation asks, none of which fit an
ACR's per-criterion grid. This script does not replace `06`. It is a third
output alongside it and the WCAG-EM report, added 2026-09-24 at the
reviewer's request, for the case `06` cannot serve: a counterparty who can
only consume the standard grid -- a campus procurement office, an RFP
response packet, a vendor being handed verified results in the format their
own paperwork uses.

The distinction the document itself must carry, and does, in its header:
a vendor's ACR is a **self-attestation**; this one is an **independent
evaluation**, every cell of it traceable to a logged run.

Rules
-----
* **Database only.** Every value is read from the mirror. Nothing is written
  from prose, memory or an assistant's summary. If a fact is not in an
  extracted field it does not appear, which is the same contract the
  dashboard and completion predicates run under (ontology/data-store.md).
* **No invention in Remarks.** A criterion's remark is the `05` remark plus
  its findings, verbatim from `criterion_outcomes`. The script adds only
  structure, never judgement.
* **Untested is said out loud.** Any criterion still `Not Evaluated`, and
  any functional performance criterion whose views are not all resulted,
  is reported as such rather than left to read as a pass.
* Deterministic: no timestamps in the body, so a diff on the committed page
  means the review changed. Never hand-edit it.
"""
from __future__ import annotations

import argparse
import html
import pathlib
import re
import sys
import webbrowser

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import review as rv  # noqa: E402
import review_db as db  # noqa: E402

CONFORMANCE = ("Supports", "Partially Supports", "Does Not Support", "Not Applicable", "Not Evaluated")
CLS = {"Supports": "ok", "Partially Supports": "part", "Does Not Support": "no",
       "Not Applicable": "na", "Not Evaluated": "unk"}

TERMS = [
    ("Supports", "The functionality of the product has at least one method that meets the criterion "
                 "without known defects, or meets with equivalent facilitation."),
    ("Partially Supports", "Some functionality of the product does not meet the criterion."),
    ("Does Not Support", "The majority of product functionality does not meet the criterion."),
    ("Not Applicable", "The criterion is not relevant to the product."),
    ("Not Evaluated", "The product has not been evaluated against the criterion. This can be used only in "
                      "WCAG 2.x Level AAA."),
]


def e(s) -> str:
    return html.escape(str(s or ""), quote=True)


def md(s) -> str:
    """Escape, then honour the light Markdown the stage files write.

    `05` remarks are authored as Markdown (that is the record's format), so a
    report rendered straight from them would print literal ** and backticks at
    a counterparty. Escaping happens first, so this can never inject markup."""
    t = e(s)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t, flags=re.S)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    # A shortened cell can cut a pair in half; never show a reader a stray
    # marker just because the text was trimmed.
    return t.replace("**", "").replace("*", "").replace("`", "")


def severity(s) -> str:
    """The bare rating word. The record keeps the reviewer's reasoning in the
    same field ("Minor (proposed ...)", "**Minor - confirmed ...**"); a report
    column wants the rating alone."""
    t = re.sub(r"[*`]", "", s or "").strip()
    m = re.match(r"(Blocker|Major|Minor)", t, re.I)
    return m.group(1).capitalize() if m else (t.split(" (")[0][:24] or "Unrated")


def trim(s, n: int) -> str:
    """Shorten to a word boundary, with an ellipsis when something was cut."""
    s = (s or "").strip()
    if len(s) <= n:
        return s
    cut = s[:n]
    sp = cut.rfind(" ")
    return (cut[:sp] if sp > n * 0.6 else cut).rstrip(" ,;:") + "\u2026"



# Internal identifiers the record uses and a reader must never see: finding IDs
# (V-F31, T1-F3), run IDs (R109), observation numbers (O5), walkthrough steps
# (W32), check codes (NV6, LV1, NC2, MO9, CO12, W1) and view codes (S1, R2).
JARGON = re.compile(
    r"""(?x)
      \b(?:V-F\d+|T\d+-F\d+)\b          # finding IDs
    | \bR\d{3}\b                        # run IDs
    | \bO\d{1,2}\b                       # observation numbers
    | \bW\d{1,2}\b                       # walkthrough steps / sweep checks
    | \b(?:NV|LV|NC|NH|NS|MO|CO)\d{1,2}\b  # check codes
    """)
VIEWCODE = re.compile(r"\b(S\d{1,2}|R[12])\b")


def depunct(t: str) -> str:
    """Tidy the holes left behind when identifiers are removed."""
    t = re.sub(r"\(\s*[;,\u2014-]*\s*\)", "", t)          # "()" and "( , )"
    t = re.sub(r"\[\s*\]", "", t)
    t = re.sub(r"\s*,\s*(?=[,.;)])", "", t)
    t = re.sub(r"\(\s*,", "(", t)
    t = re.sub(r",\s*\)", ")", t)
    t = re.sub(r"\s{2,}", " ", t)
    t = re.sub(r"\s+([,.;:)])", r"\1", t)
    t = re.sub(r"(?:\s*[;,]\s*)+\.", ".", t)
    t = re.sub(r"\.\s*\.", ".", t)
    t = re.sub(r"\(\s*[^)]{0,4}\s*\)", "", t)        # "( on )" left by a removed token
    if t.count("(") > t.count(")"):                  # never leave one hanging open
        t = t[:t.rfind("(")].rstrip(" ,;")
    t = re.sub(r"\s{2,}", " ", t)
    t = t.strip(" ,;\u2014-")
    t = re.sub(r"^[\s.,;:\u2014-]+", "", t)
    return t


# The record attributes each observation to the person who made it, which is
# how a review file should read. In the report the whole document is already
# attributed -- the header says it is an independent evaluation -- so repeating
# "the reviewer found" on every line is noise between the reader and the fact.
ATTRIB = re.compile(
    r"""(?ix)^\s*(?:
          (?:found\ |confirmed\ |established\ )?by\ the\ reviewer[^:.]{0,70}[:.]
        | reviewer(?:'s|\u2019s)?(?:\ (?:call|ruling|judgement|judgment|verdict|narration|own\ words))?
          [^:.]{0,70}[:.]
        | the\ reviewer[^:.]{0,70}[:.]
        )\s*""")


# Dates belong to the review's own record, not to a conformance statement: a
# reader wants to know what is wrong and where, not when it was decided
# (reviewer, 2026-09-24, asking for half the detail).
DATES = re.compile(r"""(?ix)
      \s*\(\s*20\d\d-\d\d-\d\d[^)]{0,40}\)     # "(2026-09-21)" / "(2026-09-15, reviewer)"
    | \s*,?\s*(?:on|since|as\ of)\ 20\d\d-\d\d-\d\d
    | \s*\b20\d\d-\d\d-\d\d\b
    """)
# Provenance openers that only existed to carry a date.
PROV = re.compile(r"""(?ix)^\s*(?:
      decided | revised | corrected | recorded | added | extended | confirmed
    | tested | measured | established | reopened | withdrawn | clarified
    )\b[^.:;,]{0,140}[.:;,]\s*""")
# Bracketed status markers the stage files use while work is in flight.
MARKER = re.compile(r"(?i)\s*\[(?:provisional|draft|pending|tbc)[^\]]{0,160}\]\s*")
# Attribution can also appear mid-paragraph, after a sentence boundary.
ATTRIB_MID = re.compile(
    r"(?i)(?<=[.;])\s+(?:the\s+)?reviewer(?:'s|\u2019s)?[^:.]{0,40}:\s*")
# "the markup the reviewer saved explains it" -> "the markup explains it"
# "(reviewer)", "(reviewer;, partial)", "(revised from the reviewer's first
# impression)" -- the record's marginalia, meaningless to a reader.
ATTRIB_PAREN = re.compile(r"(?i)\s*\([^)]{0,80}\breviewer\b[^)]{0,80}\)")
ATTRIB_CLAUSE = re.compile(
    r"(?i)\s+the\s+reviewer(?:'s|\u2019s)?\s+"
    r"(?:saved|reported|noted|found|confirmed|observed|recorded|narrated|walked|ruled)\b")


# A sentence can end inside a closing quote or bracket ("... earned." All three),
# so consume those before the space or the boundary is missed.
SENT = re.compile(r"(?<=[.!?])[\"\u201d\u2019')\]]*\s+")


def sentences(t: str):
    """Split into sentences, dropping fragments orphaned by an identifier that
    was stripped from the head ("MO3 is recorded pass ..." -> "is recorded ...")."""
    parts = [x.strip() for x in SENT.split(t or "") if x.strip()]
    keep = [x for x in parts if x[:1].isupper() or not x[:1].isalpha()]
    return keep or parts


def brief(t: str, limit: int = 170) -> str:
    """The first complete statement, whole.

    Length is controlled by taking **one sentence**, never by cutting one
    short: a clause-boundary trim produced fragments like "Tab reaches nothing
    in the row, and Enter." and an ellipsis reads as if something was withheld
    (reviewer, 2026-09-24). A long source sentence is published long."""
    t = (t or "").strip()
    parts = sentences(t)
    out = (parts[0] if parts else t).strip()
    out = out.rstrip(" ,;:\u2014-")
    if out and out[-1] not in ".!?\u201d)":
        out += "."
    return out


# Quotation is right for text the PRODUCT shows ("Problem N Click To Activate")
# and wrong for the reviewer's own words, which a conformance report should
# state as fact. Product strings here are short and start capitalised or with a
# symbol; reviewer speech runs longer or opens lower-case.
def is_product_string(q: str) -> bool:
    """Text the product itself shows, which stays quoted: a button caption, a
    field label, an announcement. Short, and capitalised or punctuation-led."""
    q = q.strip()
    return len(q) <= 45 and bool(q) and (q[:1].isupper() or not q[:1].isalpha())


def unquote(t: str):
    """Drop the reviewer's quotation marks, keep the product's.

    Returns the text with product strings replaced by placeholders, plus the
    list to restore afterwards, so the first-person and ellipsis passes cannot
    rewrite a button called "I give up"."""
    kept = []

    def sub(m):
        q = m.group(1)
        if is_product_string(q):
            kept.append(m.group(0))
            return f"\x00{len(kept) - 1}\x00"
        return q
    t = re.sub(r"\u201c([^\u201d]{2,400})\u201d", sub, t)
    t = re.sub(r'"([^"]{2,400})"', sub, t)
    return t, kept


def restore(t: str, kept) -> str:
    return re.sub(r"\x00(\d+)\x00", lambda m: kept[int(m.group(1))], t)


# First person belongs to a test narrative, not to a statement about a product.
def _ing(v: str) -> str:
    v = v.lower()
    return v[:-1] + "ing" if v.endswith("e") and not v.endswith("ee") else v + "ing"


PERSON = [
    (r"(?i)\bI have (?:not|never) (?:encountered|found|seen|observed)\s+(?:any\s+)?(.+?)"
     r"(?:\s*[,.]?\s*(?:through|across|in)\b[^.]*)?(?=[.]|$)",
     lambda m: "No " + m.group(1).strip(" .,") + " encountered"),
    (r"(?i)\bno (.+?) (?:have|has) been encountered\b[^.]*",
     lambda m: "No " + m.group(1).strip(" .,") + " encountered"),
    (r"(?i)^[\s*_“\"']*I (?:see|saw|found|noticed)\s+(.+)$",
     lambda m: m.group(1)[:1].upper() + m.group(1)[1:]),
    (r"(?i)\b(?:if|when)\s+we\s+(\w+)\b", lambda m: "on " + _ing(m.group(1))),
    (r"(?i)\bwe\s+(?:can'?t|cannot|could\s+not)\s+", "cannot "),
    (r"(?i)\bwe\s+(?:hear|heard|see|saw|find|found|get|got)\s+", ""),
]


def impersonal(t: str) -> str:
    for pat, fn in PERSON:
        t = re.sub(pat, fn, t)
    return re.sub(r"(?i)\b(?:my|our)\b\s*", "", t)


# Record-keeping progression: a report is a statement of the product's state,
# not a log of how the evidence accumulated.
PROGRESS = re.compile(r"(?i)\b(?:now (?:stands?|reads?|covers?)|and now\b|also now\b)")


def plain(t, pages: dict) -> str:
    """Reader-facing text: identifiers out, view codes replaced by page names,
    attribution clauses dropped."""
    t = VIEWCODE.sub(lambda m: pages.get(m.group(1), {}).get("name", m.group(1)), t or "")
    t = JARGON.sub("", t)
    t = DATES.sub("", t)
    t = MARKER.sub(" ", t)
    t = ATTRIB_MID.sub(". ", t)
    t = ATTRIB_PAREN.sub("", t)
    t = ATTRIB_CLAUSE.sub("", t)
    t = ATTRIB.sub("", t)
    for _ in range(3):                      # provenance can be stacked
        t2 = PROV.sub("", t)
        if t2 == t:
            break
        t = t2
    t = re.sub(r"^[\s\u2014-]*", "", t)
    t, kept = unquote(t)
    t = impersonal(t)
    # The record elides with "..." when narration was pasted; in a report that
    # reads as if the statement was cut short (reviewer, 2026-09-24).
    t = re.sub(r"\s*\u2026\s*", ". ", t)
    t = restore(t, kept)
    t = PROGRESS.sub(lambda m: m.group(0).lower().replace("now ", "").replace("and now", "and")
                     .replace("also now", "also") or "", t)
    t = depunct(t)
    # Removing a check code from the head of a sentence can orphan its verb
    # ("CO10 fails on all 10 views" -> "fails on all 10 views"). Start at the
    # next complete sentence rather than publish a fragment.
    t = re.sub(r"^[*_\"“‘']+", "", t)
    if t and t[0].islower():
        parts = sentences(t)
        t = parts[0] if parts and parts[0][:1].isupper() else (t[0].upper() + t[1:])
    return t


def page_name(raw: str) -> str:
    """The page in words, without the record's bookkeeping suffixes."""
    n = re.split(r"\s+\u2014\s+proposed|\s+\u2014\s+removed", raw or "")[0]
    n = re.sub(r'\s*\u2014\s*".*$', "", n)
    return n.strip(" \u2014-") or raw


def short_path(loc: str) -> str:
    """A simple address a reader can recognise: /Common/Calendar.aspx."""
    loc = (loc or "").strip().strip("`")
    m = re.search(r"https?://[^/\s`)]+(/[^\s`)\]]*)", loc)
    if m:
        return re.sub(r"\?.*$", "", m.group(1)) or "/"
    m = re.search(r"UI:\s*([^`\n]{0,60})", loc)
    return m.group(1).strip() if m else ""


def reason(t: str) -> str:
    """An exclusion reason without the record's date stamp or attribution."""
    t = re.sub(r"^\s*20\d\d-\d\d-\d\d\s*:\s*", "", t or "")
    t = re.sub(r"\s*\((?:reviewer|assistant)\)\s*$", "", t)
    return t.strip().rstrip(".")


def gather(con, review: pathlib.Path) -> dict:
    """Everything the report prints, read from the mirror and nowhere else."""
    q = lambda sql, *a: con.execute(sql, a).fetchall()
    rid = review.name

    row = q("SELECT product, decision, report_status, source_sha FROM reviews WHERE review_id=?", rid)
    product, decision, report_status, source_sha = row[0] if row else ("", "", "", "")

    criteria = q("""
        SELECT w.sc, w.name, w.level, w.principle_no, w.principle, w.version_added, w.understanding_url,
               co.outcome, co.remarks, co.task_findings, co.vendor_claim
        FROM wcag_criteria w
        LEFT JOIN criterion_outcomes co ON co.sc = w.sc AND co.review_id = ?
        WHERE w.in_target = 1
        ORDER BY w.sort_key""", rid)

    # evidence counts per criterion: answered check rows and failing ones
    ev = {}
    for sc, answered, failing in q("""
        SELECT cc.sc,
               SUM(CASE WHEN o.outcome IN ('pass','fail','partial','n/a') THEN 1 ELSE 0 END),
               SUM(CASE WHEN o.outcome IN ('fail','partial') THEN 1 ELSE 0 END)
        FROM check_criteria cc
        JOIN check_outcomes o ON o.check_id = cc.check_id AND o.review_id = ?
        JOIN runs r ON r.run_id = o.run_id AND r.review_id = o.review_id
        JOIN views v ON v.view_id = r.view_id AND v.review_id = r.review_id
        WHERE COALESCE(v.removed,'') = ''
        GROUP BY cc.sc""", rid):
        ev[sc] = (answered or 0, failing or 0)

    # functional performance criteria: views resulted vs sampled, per modality
    views_live = q("SELECT COUNT(*) FROM views WHERE review_id=? AND COALESCE(removed,'')=''", rid)[0][0]
    fpc = []
    for code, name, modality in q("SELECT code, name, modality FROM fpc ORDER BY code"):
        done = q("""SELECT COUNT(DISTINCT r.view_id) FROM runs r
                    JOIN views v ON v.view_id=r.view_id AND v.review_id=r.review_id
                    WHERE r.review_id=? AND r.modality=? AND COALESCE(v.removed,'')=''
                      AND r.result IN ('Works','Works with issues','Broken','N/A')""", rid, modality)[0][0]
        blank = q("""SELECT COUNT(*) FROM runs r
                     JOIN check_outcomes o ON o.run_id=r.run_id AND o.review_id=r.review_id
                     JOIN views v ON v.view_id=r.view_id AND v.review_id=r.review_id
                     WHERE r.review_id=? AND r.modality=? AND COALESCE(v.removed,'')=''
                       AND COALESCE(o.outcome,'')=''""", rid, modality)[0][0]
        fails = q("""SELECT COUNT(*) FROM runs r
                     JOIN check_outcomes o ON o.run_id=r.run_id AND o.review_id=r.review_id
                     JOIN views v ON v.view_id=r.view_id AND v.review_id=r.review_id
                     WHERE r.review_id=? AND r.modality=? AND COALESCE(v.removed,'')=''
                       AND o.outcome IN ('fail','partial')""", rid, modality)[0][0]
        broken = q("""SELECT COUNT(DISTINCT r.view_id) FROM runs r
                      JOIN views v ON v.view_id=r.view_id AND v.review_id=r.review_id
                      WHERE r.review_id=? AND r.modality=? AND COALESCE(v.removed,'')=''
                        AND r.result='Broken'""", rid, modality)[0][0]
        # findings whose evidence includes a run of this modality
        fnames = [f[0] for f in q("""SELECT DISTINCT f.finding_id FROM findings f
                     JOIN finding_runs fr ON fr.finding_id=f.finding_id AND fr.review_id=f.review_id
                     JOIN runs r ON r.run_id=fr.run_id AND r.review_id=fr.review_id
                     WHERE f.review_id=? AND f.withdrawn=0 AND r.modality=?
                     ORDER BY f.finding_id""", rid, modality)]
        answered = q("""SELECT COUNT(*) FROM runs r
                        JOIN check_outcomes o ON o.run_id=r.run_id AND o.review_id=r.review_id
                        JOIN views v ON v.view_id=r.view_id AND v.review_id=r.review_id
                        WHERE r.review_id=? AND r.modality=? AND COALESCE(v.removed,'')=''
                          AND COALESCE(o.outcome,'')<>''""", rid, modality)[0][0]
        missing = [page_name(x[0]) for x in q("""SELECT v.name FROM views v
                     WHERE v.review_id=? AND COALESCE(v.removed,'')=''
                       AND v.view_id NOT IN (SELECT r.view_id FROM runs r
                            WHERE r.review_id=v.review_id AND r.modality=?
                              AND r.result IN ('Works','Works with issues','Broken','N/A'))
                     ORDER BY CAST(SUBSTR(v.view_id,2) AS INT)""", rid, modality)]
        broken_names = [page_name(x[0]) for x in q("""SELECT v.name FROM runs r
                     JOIN views v ON v.view_id=r.view_id AND v.review_id=r.review_id
                     WHERE r.review_id=? AND r.modality=? AND COALESCE(v.removed,'')=''
                       AND r.result='Broken' ORDER BY CAST(SUBSTR(v.view_id,2) AS INT)""", rid, modality)]
        fpc.append(dict(code=code, name=name, modality=modality, done=done, views=views_live,
                        blank=blank, fails=fails, broken=broken, findings=fnames,
                        answered=answered, missing=missing, broken_names=broken_names))

    findings = q("""SELECT finding_id, severity, where_text, observed,
                           (SELECT GROUP_CONCAT(sc, ', ') FROM finding_criteria fc
                             WHERE fc.finding_id=f.finding_id AND fc.review_id=f.review_id) AS sc
                    FROM findings f WHERE review_id=? AND withdrawn=0
                    ORDER BY CASE severity WHEN 'Blocker' THEN 0 END, finding_id""", rid)

    views = q("""SELECT view_id, name, locator FROM views
                 WHERE review_id=? AND COALESCE(removed,'')='' ORDER BY CAST(SUBSTR(view_id,2) AS INT)""", rid)
    removed = q("""SELECT view_id, name, removed FROM views
                   WHERE review_id=? AND COALESCE(removed,'')<>'' ORDER BY view_id""", rid)
    runs_total = q("SELECT COUNT(*) FROM runs WHERE review_id=?", rid)[0][0]
    runs_resulted = q("""SELECT COUNT(*) FROM runs WHERE review_id=?
                         AND result IN ('Works','Works with issues','Broken','N/A')""", rid)[0][0]
    tasks = q("SELECT task_id, name, verdict FROM tasks WHERE review_id=? ORDER BY task_id", rid)

    pages = {v[0]: {"name": page_name(v[1]), "path": short_path(v[2])} for v in
             q("SELECT view_id, name, locator FROM views WHERE review_id=?", rid)}

    # which findings bear on each criterion, with the page each was found on
    by_sc = {}
    for sc, fid, where, observed, sev in q("""
            SELECT fc.sc, f.finding_id, f.where_text, f.observed, f.severity
            FROM finding_criteria fc
            JOIN findings f ON f.finding_id = fc.finding_id AND f.review_id = fc.review_id
            WHERE fc.review_id = ? AND f.withdrawn = 0
            ORDER BY fc.sc, f.finding_id""", rid):
        vids = VIEWCODE.findall(where or "")
        by_sc.setdefault(sc, []).append(dict(fid=fid, where=where or "", observed=observed or "",
                                             sev=severity(sev), views=vids))

    return dict(rid=rid, pages=pages, by_sc=by_sc,
                product=product, decision=decision, report_status=report_status,
                source_sha=source_sha, criteria=criteria, ev=ev, fpc=fpc, findings=findings,
                views=views, removed=removed, runs_total=runs_total, runs_resulted=runs_resulted,
                tasks=tasks)


def statements(sc: str, d: dict) -> str:
    """One bullet per distinct statement, each naming the page.

    Findings that say the same thing on different pages are merged into a
    single bullet with both pages, so a product-wide pattern reads once rather
    than five times (reviewer, 2026-09-24: "combine issues where possible")."""
    merged = {}
    for f in d["by_sc"].get(sc, []):
        text = brief(plain(f["observed"], d["pages"]), 130)
        if text and text[:1].islower():
            text = text[0].upper() + text[1:]
        key = re.sub(r"[^a-z0-9 ]", "", text.lower())[:70]
        pgs = [d["pages"][v]["name"] for v in dict.fromkeys(f["views"]) if v in d["pages"]]
        if key in merged:
            for n in pgs:
                if n not in merged[key]["pages"]:
                    merged[key]["pages"].append(n)
            if f["sev"] == "Blocker":
                merged[key]["sev"] = "Blocker"
        else:
            merged[key] = dict(text=text, pages=list(pgs), sev=f["sev"])

    RANK = {"Blocker": 0, "Major": 1, "Minor": 2}
    rows = sorted(merged.values(), key=lambda m: (RANK.get(m["sev"], 3), -len(m["pages"])))
    extra = max(0, len(rows) - 5)
    items = []
    for m in rows[:5]:
        if len(m["pages"]) > 3:
            where = f"<b>{e(m['pages'][0])}</b> and {len(m['pages']) - 1} other pages"
        elif m["pages"]:
            where = ", ".join(f"<b>{e(n)}</b>" for n in m["pages"])
        else:
            where = "<b>Product-wide</b>"
        items.append(f"<li><span class='where'>{where}</span> \u2014 {md(m['text'])}"
                     f"<span class='sev sev-{m['sev'].lower()}'>{e(m['sev'])}</span></li>")
    if extra:
        items.append(f"<li class='more'>{extra} further issue{'s' if extra != 1 else ''} on this criterion "
                     f"{'are' if extra != 1 else 'is'} listed in \u201cIssues found\u201d below.</li>")
    return f"<ul class='stmts'>{''.join(items)}</ul>" if items else ""


# Count markers and check-outcome shorthand the record uses inside prose.
COUNTS = re.compile(r"\s*\(\s*(?:n/?a|pass|fail|partial)?\s*[\u00d7x]?\s*\d*\s*\)|\s*[\u00d7x]\s*\d+\b", re.I)


def na_reason(note: str) -> str:
    """One plain sentence saying why the criterion does not apply.

    A Not Applicable needs no justification, only a statement (reviewer,
    2026-09-24). The record's remark is mined for a self-contained first
    clause; where it yields only a cross-reference ("As 1.2.3."), a dangling
    pronoun ("... on any of them") or a check outcome ("n/a on all 10 views"),
    the standard sentence is used instead. That asserts nothing beyond the
    conformance level itself."""
    STD = "Not present in the evaluated sample."
    t = COUNTS.sub("", note or "").strip()
    for clause in re.split(r"\s*[:;]\s+|\s+\u2014\s+", t):
        c = depunct(clause).rstrip(".,;: ")
        if (len(c) >= 18
                and not re.match(r"(?i)^(as|see|same as)\b", c)
                and not re.search(r"(?i)\b(any of them|this criterion|n/?a)\b", c)
                and not re.match(r"(?i)^\s*\d", c)):
            return c[:1].upper() + c[1:] + "."
    return STD


def echoes(lead: str, stmts_html: str) -> bool:
    """True when the lead says what a bullet already says.

    Compared on content words, so a paraphrase counts: the record often
    summarises a finding in the criterion remark and then states it again in
    the finding itself."""
    def bag(x):
        x = re.sub(r"<[^>]+>", " ", x).lower()
        return {w for w in re.findall(r"[a-z]{4,}", x)
                if w not in {"page", "pages", "this", "that", "with", "from", "have", "been",
                             "which", "their", "there", "when", "only", "does", "also"}}
    a = bag(lead)
    if len(a) < 4:
        return False
    for li in re.findall(r"<li[^>]*>(.*?)</li>", stmts_html, re.S):
        b = bag(li)
        if b and len(a & b) / min(len(a), len(b)) >= 0.6:
            return True
    return False


def crit_rows(d: dict, level: str) -> str:
    out = []
    for (sc, name, lv, pno, pr, ver, url, outcome, remarks, tf, vendor) in d["criteria"]:
        if lv != level:
            continue
        outcome = outcome or "Not Evaluated"
        answered, failing = d["ev"].get(sc, (0, 0))
        note = brief(plain((remarks or "").strip(), d["pages"]), 170)
        if outcome == "Not Applicable":
            note = na_reason(note)
        if not note:
            note = ("No evaluation was carried out against this criterion."
                    if outcome == "Not Evaluated" else "")
        # Where bullets carry the detail, the lead is a summary only; where
        # there are none (a pass, or an n/a) it is the whole explanation.
        stmts = statements(sc, d)
        # A lead that repeats a bullet is noise: the bullet is better, because
        # it names the page and the severity (reviewer, 2026-09-24).
        if stmts and note and echoes(note, stmts):
            note = ""
        body = f"<p class='lead'>{md(note)}</p>" if note else ""
        body += stmts
        # Neither check counts nor the supplier's own claim: the first describes
        # how the review was run, the second belongs to an audit of the
        # supplier's paperwork. This document is a standalone conformance
        # report about the product (reviewer, 2026-09-24).
        sup = f" <a class='u' href='{e(url)}'>Understanding</a>" if url else ""
        newer = f" <span class='badge'>WCAG {e(ver)}</span>" if ver and ver != "2.0" else ""
        out.append(
            f"<tr><th scope='row'><a class='sc' href='{e(url)}'>{e(sc)}</a> {e(name)}{newer}{sup}</th>"
            f"<td class='lvl'><span class='pill {CLS.get(outcome,'unk')}'>{e(outcome)}</span></td>"
            f"<td class='rem'>{body}</td></tr>")
    return "\n".join(out)


def issue_row(n: int, f, d: dict) -> str:
    """One issue, numbered for reference within this report only.

    The record's own identifiers (finding, run and observation IDs) are the
    review's bookkeeping and mean nothing to a reader, so they do not appear;
    the page is named instead, which is what a reader needs in order to go and
    look (reviewer, 2026-09-24)."""
    fid, sev_raw, where, observed, scs = f[0], f[1], f[2] or "", f[3] or "", f[4] or ""
    pgs = []
    for v in dict.fromkeys(VIEWCODE.findall(where)):
        pg = d["pages"].get(v)
        if pg:
            pgs.append(f"<b>{e(pg['name'])}</b>"
                       + (f"<br><span class='pth'>{e(pg['path'])}</span>" if pg["path"] else ""))
    page = "<br>".join(pgs) if pgs else "<b>Product-wide</b>"
    # the "where" text minus the page prefix the column now carries
    what = plain(where, d["pages"])
    what = re.sub(r"^[^\u2014-]{0,80}[\u2014-]\s*", "", what).strip() or plain(observed, d["pages"])
    sev = severity(sev_raw)
    return (f"<tr><th scope='row'>{n}</th>"
            f"<td><span class='sev sev-{sev.lower()}'>{e(sev)}</span></td>"
            f"<td class='pth'>{e(scs)}</td><td>{page}</td>"
            f"<td class='rem'>{md(brief(what, 120))}</td></tr>")


def render(d: dict) -> str:
    prod = d["product"] or d["rid"]
    interim = "INTERIM" in (d["report_status"] or "").upper()

    fpc_rows = []
    for f in d["fpc"]:
        # Derive the level from the evidence that exists, then state the coverage
        # limit. Reporting "Not Evaluated" over a modality with a hundred answered
        # rows because one view lacks a Result would misrepresent the work and
        # understate the risk (corrected 2026-09-24 at the reviewer's request).
        tested = f["done"] > 0 or (f["answered"] - f["blank"]) > 0
        full = f["done"] >= f["views"] and f["blank"] == 0
        if not tested:
            lvl, cls = "Not Evaluated", "unk"
        elif f["broken"]:
            lvl, cls = "Does Not Support", "no"
        elif f["fails"]:
            lvl, cls = "Partially Supports", "part"
        else:
            lvl, cls = "Supports", "ok"

        if not tested:
            note = "This functional performance criterion was not evaluated."
        elif f["broken"]:
            note = (f"{f['broken']} of the {f['views']} pages evaluated could not be used by this method, and "
                    f"{f['fails']} recorded check{'s' if f['fails'] != 1 else ''} failed.")
        elif f["fails"]:
            note = (f"Every page evaluated could be used by this method, but {f['fails']} recorded "
                    f"check{'s' if f['fails'] != 1 else ''} failed.")
        else:
            note = "Every page evaluated could be used by this method with no failing checks."

        if tested and not full:
            missing = ", ".join(f"<b>{e(n)}</b>" for n in f["missing"][:4]) or ""
            gap = (f" <b>Coverage limit:</b> {f['done']} of {f['views']} pages carry a completed result"
                   + (f", and {f['blank']} check row{'s' if f['blank'] != 1 else ''} elsewhere "
                      f"{'remain' if f['blank'] != 1 else 'remains'} unanswered" if f["blank"] else "")
                   + (f". Still outstanding: {missing}." if missing else ".")
                   + " The level above reflects the pages that were evaluated.")
        else:
            gap = f" All {f['views']} pages in scope were evaluated for this criterion."
        pages_hit = ", ".join(f"<b>{e(n)}</b>" for n in f["broken_names"][:4])
        where = f" Affected: {pages_hit}." if pages_hit else ""
        fpc_rows.append(f"<tr><th scope='row'>{e(f['code'])} {e(f['name'])}</th>"
                        f"<td class='lvl'><span class='pill {cls}'>{lvl}</span></td>"
                        f"<td class='rem'><p class='lead'>{note}{where}</p>"
                        f"<div class='ev'>{gap}</div></td></tr>")

    sev = {}
    for fid, s, *_ in d["findings"]:
        k = (s or "").split(" ")[0].strip("*") or "Unrated"
        sev[k] = sev.get(k, 0) + 1
    sev_txt = ", ".join(f"{v} {k}" for k, v in sorted(sev.items())) or "none"

    counts = {}
    for c in d["criteria"]:
        counts[c[7] or "Not Evaluated"] = counts.get(c[7] or "Not Evaluated", 0) + 1
    tally = " · ".join(f"<b>{counts.get(k,0)}</b> {k}" for k in CONFORMANCE if counts.get(k))

    views_txt = "".join(
        f"<li><b>{e(page_name(v[1]))}</b>"
        + (f" <span class='pth'>{e(short_path(v[2]))}</span>" if short_path(v[2]) else "")
        + "</li>" for v in d["views"])
    excluded = ("<ul class='pages'>" + "".join(
        f"<li><b>{e(page_name(v[1]))}</b> \u2014 {e(reason(v[2]))}</li>" for v in d["removed"]) + "</ul>"
        ) if d["removed"] else "none"
    tasks_txt = "".join(f"<li>{e(t[1].split(' \u2014 ')[0])} \u2014 <b>{e(t[2])}</b></li>"
                        for t in d["tasks"])
    terms = "\n".join(f"<tr><th scope='row'>{e(t)}</th><td>{e(x)}</td></tr>" for t, x in TERMS)

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Accessibility Conformance Report — {e(prod)}</title>
<style>
 :root {{ --ink:#14181d; --mut:#5a6472; --line:#d7dce3; --bg:#fff; --panel:#f6f8fa;
   --ok:#1c6b3f; --okbg:#e6f4ec; --part:#8a5a00; --partbg:#fdf3e0; --no:#9a1f2e; --nobg:#fcebed;
   --na:#4a5260; --nabg:#eef1f4; --unk:#5a3b8a; --unkbg:#f0ebf8; }}
 @media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
   --ink:#e7ebf0; --mut:#9aa6b6; --line:#2b323c; --bg:#11151a; --panel:#161b22;
   --okbg:#10291c; --ok:#6fd39b; --partbg:#2a2110; --part:#e8b45c; --nobg:#2c1418; --no:#f08b98;
   --nabg:#1b2028; --na:#a8b2c0; --unkbg:#1e1a2c; --unk:#b79ce8; }} }}
 :root[data-theme="dark"] {{ --ink:#e7ebf0; --mut:#9aa6b6; --line:#2b323c; --bg:#11151a; --panel:#161b22;
   --okbg:#10291c; --ok:#6fd39b; --partbg:#2a2110; --part:#e8b45c; --nobg:#2c1418; --no:#f08b98;
   --nabg:#1b2028; --na:#a8b2c0; --unkbg:#1e1a2c; --unk:#b79ce8; }}
 * {{ box-sizing:border-box; }}
 body {{ margin:0; background:var(--bg); color:var(--ink); font:16px/1.55 -apple-system,BlinkMacSystemFont,
   "Segoe UI",Roboto,Helvetica,Arial,sans-serif; }}
 .wrap {{ max-width:60rem; margin:0 auto; padding:2rem 16px 5rem; }}
 h1 {{ font-size:1.7rem; margin:0 0 .2rem; line-height:1.25; }}
 h2 {{ font-size:1.25rem; margin:2.4rem 0 .6rem; padding-bottom:.3rem; border-bottom:2px solid var(--line); }}
 h3 {{ font-size:1rem; margin:1.6rem 0 .4rem; }}
 p, li {{ max-width:56rem; }}
 .sub {{ color:var(--mut); margin:.1rem 0 1.2rem; }}
 .note {{ background:var(--panel); border:1px solid var(--line); border-left:4px solid var(--unk);
   padding:.8rem 1rem; border-radius:6px; margin:1rem 0; }}
 table {{ border-collapse:collapse; width:100%; margin:.6rem 0 1.4rem; font-size:.94rem; }}
 th, td {{ border:1px solid var(--line); padding:.55rem .65rem; text-align:left; vertical-align:top; }}
 thead th {{ background:var(--panel); font-size:.82rem; text-transform:uppercase; letter-spacing:.04em; }}
 tbody th {{ font-weight:600; width:34%; }}
 td.lvl {{ width:9.5rem; white-space:nowrap; }}
 .pill {{ display:inline-block; padding:.12rem .5rem; border-radius:999px; font-size:.82rem; font-weight:700; }}
 .pill.ok {{ background:var(--okbg); color:var(--ok); }} .pill.part {{ background:var(--partbg); color:var(--part); }}
 .pill.no {{ background:var(--nobg); color:var(--no); }} .pill.na {{ background:var(--nabg); color:var(--na); }}
 .pill.unk {{ background:var(--unkbg); color:var(--unk); }}
 .rem {{ font-size:.9rem; }}
 .lead {{ margin:.1rem 0 .4rem; }}
 ul.stmts {{ margin:.3rem 0 .2rem; padding-left:1.1rem; }}
 ul.stmts li {{ margin:0 0 .45rem; }}
 ul.stmts li.more {{ list-style:none; margin-left:-1.1rem; color:var(--mut); font-size:.85rem; }}
 .where {{ font-weight:600; }}
 ul.pages {{ margin:.2rem 0 0; padding-left:1.1rem; }}
 ul.pages li {{ margin:0 0 .2rem; }}
 .pth {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.82em; color:var(--mut); }}
 .sev {{ display:inline-block; margin-left:.4rem; font-size:.72rem; font-weight:700; padding:0 .35rem;
   border-radius:4px; vertical-align:.08em; }}
 .sev-blocker {{ background:var(--nobg); color:var(--no); }}
 .sev-major {{ background:var(--partbg); color:var(--part); }}
 .sev-minor {{ background:var(--nabg); color:var(--na); }}
 .fnd, .ev {{ margin-top:.35rem; color:var(--mut); font-size:.85rem; }}
 .lbl {{ font-weight:700; color:var(--ink); }}
 .badge {{ font-size:.72rem; background:var(--panel); border:1px solid var(--line); border-radius:4px;
   padding:0 .3rem; color:var(--mut); }}
 a {{ color:inherit; }} a.sc {{ font-weight:700; text-decoration:none; }} a.sc:hover {{ text-decoration:underline; }}
 a.u {{ font-size:.75rem; color:var(--mut); }}
 dl.meta {{ display:grid; grid-template-columns:13rem 1fr; gap:.35rem 1rem; margin:1rem 0; }}
 dl.meta dt {{ font-weight:700; }} dl.meta dd {{ margin:0; }}
 @media (max-width:640px) {{ dl.meta {{ grid-template-columns:1fr; gap:.1rem; }}
   dl.meta dd {{ margin:0 0 .6rem; }} tbody th {{ width:auto; }} }}
 @media print {{ .pill {{ border:1px solid currentColor; }} }}
</style></head><body><div class="wrap">

<h1>Accessibility Conformance Report</h1>
<p class="sub">{e(prod)} — based on VPAT<sup>&reg;</sup> 2.5</p>

<div class="note">
<p><b>This is an independent evaluation, not a vendor self-attestation.</b> A VPAT/ACR is normally completed by
the supplier about its own product. This report was produced by the evaluating body named below from its own
testing, and every conformance level in it is derived from logged test runs rather than from supplier statements.
No claim made by the supplier is reproduced or relied on anywhere in this document.</p>
<p>Generated from the review's database ({e(d['rid'])}.sqlite) by <code>scripts/export_acr.py</code>. No cell is
authored by hand. {"<b>This report is INTERIM: testing is in progress and levels may change.</b>" if interim else ""}</p>
</div>

<h2>Report information</h2>
<dl class="meta">
<dt>Product</dt><dd>{e(prod)}</dd>
<dt>Report status</dt><dd>{e(d['report_status'])}</dd>
<dt>Evaluation methods</dt><dd>Manual testing by a human reviewer driving the product with assistive technology
 (screen reader, keyboard-only operation, browser zoom, colour filters, contrast measurement), supported by
 automated scanning (axe-core) and programmatic measurement over the Chrome DevTools Protocol. Automated results
 were used to direct attention only; no conformance level rests on a tool's output alone.</dd>
<dt>Pages evaluated</dt><dd>{len(d['views'])} pages:<ul class="pages">{views_txt}</ul></dd>
<dt>Excluded from scope</dt><dd>{excluded}</dd>
<dt>Test runs</dt><dd>{d['runs_resulted']} of {d['runs_total']} logged runs carry a recorded result</dd>
<dt>Task walk-throughs</dt><dd><ul class="pages">{tasks_txt}</ul></dd>
<dt>Findings</dt><dd>{len(d['findings'])} live ({e(sev_txt)})</dd>
<dt>Criteria</dt><dd>{tally}</dd>
</dl>

<h2>Applicable standards</h2>
<ul>
<li>Web Content Accessibility Guidelines 2.2, Level A and Level AA (W3C Recommendation)</li>
<li>Revised Section 508 standards — Chapter 3, Functional Performance Criteria</li>
</ul>

<h2>Terms</h2>
<table><caption class="sub">Conformance levels used throughout this report.</caption>
<thead><tr><th scope="col">Term</th><th scope="col">Definition</th></tr></thead>
<tbody>{terms}</tbody></table>

<h2>Table 1: Success Criteria, Level A</h2>
<table><thead><tr><th scope="col">Criterion</th><th scope="col">Conformance level</th>
<th scope="col">Remarks and explanations</th></tr></thead>
<tbody>{crit_rows(d, 'A')}</tbody></table>

<h2>Table 2: Success Criteria, Level AA</h2>
<table><thead><tr><th scope="col">Criterion</th><th scope="col">Conformance level</th>
<th scope="col">Remarks and explanations</th></tr></thead>
<tbody>{crit_rows(d, 'AA')}</tbody></table>

<h2>Chapter 3: Functional Performance Criteria</h2>
<p class="sub">Derived from the proportion of sampled views evaluated for each functional modality and the
check rows recorded against them. A criterion whose views are not all evaluated is reported as Not Evaluated
rather than inferred.</p>
<table><thead><tr><th scope="col">Criterion</th><th scope="col">Conformance level</th>
<th scope="col">Remarks and explanations</th></tr></thead>
<tbody>{chr(10).join(fpc_rows)}</tbody></table>

<h2>Chapters 4, 5 and 6</h2>
<table><thead><tr><th scope="col">Chapter</th><th scope="col">Conformance level</th>
<th scope="col">Remarks and explanations</th></tr></thead>
<tbody>
<tr><th scope="row">Chapter 4: Hardware</th><td class="lvl"><span class="pill na">Not Applicable</span></td>
<td class="rem">The product is web-delivered software with no hardware component.</td></tr>
<tr><th scope="row">Chapter 5: Software</th><td class="lvl"><span class="pill na">Not Applicable</span></td>
<td class="rem">The product is a web application evaluated against WCAG 2.2 in Tables 1 and 2 above;
501.1 applies the WCAG results rather than a separate software evaluation.</td></tr>
<tr><th scope="row">Chapter 6: Support Documentation and Services</th>
<td class="lvl"><span class="pill unk">Not Evaluated</span></td>
<td class="rem">Support documentation and services were not part of the evaluated sample.</td></tr>
</tbody></table>

<h2>Issues found</h2>
<p class="sub">Every conformance level other than Supports or Not Applicable traces to one or more of these.
Each was observed by a person testing the product, and is recorded against the page it was found on.</p>
<table><thead><tr><th scope="col">#</th><th scope="col">Severity</th><th scope="col">Criteria</th>
<th scope="col">Page</th><th scope="col">Issue</th></tr></thead><tbody>
{chr(10).join(issue_row(i, f, d) for i, f in enumerate(d['findings'], 1))}
</tbody></table>

<p class="sub">Source database hash {e((d['source_sha'] or '')[:16])}. VPAT<sup>&reg;</sup> is a registered
service mark of the Information Technology Industry Council (ITI); this report follows the structure of
VPAT<sup>&reg;</sup> 2.5 and is not endorsed by ITI.</p>

</div></body></html>
"""


def out_path(review: pathlib.Path, override=None) -> pathlib.Path:
    return pathlib.Path(override) if override else review / f"{review.name}-acr.html"


def write(review: pathlib.Path, con=None, override=None) -> pathlib.Path:
    own = con is None
    con = con or db.connect(review)
    try:
        page = render(gather(con, review))
    finally:
        if own:
            con.close()
    path = out_path(review, override)
    prev = path.read_text(encoding="utf-8") if path.is_file() else None
    if prev != page:
        path.write_text(page, encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("review", help="review directory name or unique substring")
    ap.add_argument("--out", help="write somewhere other than reviews/<id>/<id>-acr.html")
    ap.add_argument("--open", action="store_true", help="open the report in a browser")
    a = ap.parse_args()
    review = rv.resolve(a.review)
    path = write(review, override=a.out)
    print(f"ACR written: {path}")
    if a.open:
        webbrowser.open(path.resolve().as_uri())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
