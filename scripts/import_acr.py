"""Import vendor ACR claims into a review.

Accepts two ACR shapes, chosen by file extension:

  .html  Adobe's published format (VPAT div-grid: each WCAG criterion block
         followed by conformance-level and remarks divs; scoped claims such
         as "Web:" / "Electronic Docs:")
  .pdf   the ITI VPAT 2.5 template as most vendors export it — three-column
         tables "Criteria | Conformance Level | Remarks and Explanations"
         (needs `pymupdf`; the claim scope is recorded as "Product")

Either way it:

  1. writes <review>/vendor-acr/acr-wcag-claims.md — extracted per-criterion
     claims with full remarks, greppable
  2. fills the empty "- **Vendor claim:**" lines in <review>/05-results.md
     with the claimed conformance level (criteria the ACR does not cover —
     e.g. WCAG 2.2 additions missing from a WCAG 2.1 ACR — are marked so)

Usage: python scripts/import_acr.py <review> <acr.html|acr.pdf>
"""
import html as htmlmod
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REVIEWS = ROOT / "reviews"

CONFORMANCE_TERMS = ("Supports", "Partially Supports", "Does Not Support",
                     "Not Applicable", "Not Evaluated")


def resolve(query):
    dirs = sorted(d for d in REVIEWS.iterdir() if d.is_dir())
    matches = [d for d in dirs if d.name == query] or \
              [d for d in dirs if query.lower() in d.name.lower()]
    if len(matches) != 1:
        sys.exit(f"Review '{query}' not found or ambiguous. "
                 + "Existing: " + ", ".join(d.name for d in dirs))
    return matches[0]


def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def clean_paragraphs(s):
    """Strip tags but keep paragraph breaks."""
    s = re.sub(r"</p>|</li>|<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in s.split("\n")]
    return "\n".join(ln for ln in lines if ln)


def parse_claims(html):
    """Return {sc_number: {name, level, claims, remarks}} from the WCAG report
    section (stops before the Section 508 / EN 301 549 functional chapters)."""
    end = html.find("Chapter 3")
    wcag = html[:end] if end != -1 else html

    claims = {}
    # split at each criterion heading link, e.g.
    # <p><strong><a href="...">1.1.1 Non-text Content</a></strong> (Level A)
    parts = re.split(
        r'(?=<p><strong><a[^>]*>\d+\.\d+\.\d+ )', wcag)
    for part in parts:
        head = re.match(
            r'<p><strong><a[^>]*>(\d+\.\d+\.\d+) ([^<]+)</a></strong>\s*'
            r'\(Level (A+)[^)]*\)', part)
        if not head:
            continue
        num, name, level = head.group(1), clean(head.group(2)), head.group(3)

        # conformance div: pairs like <strong>Web:</strong> Partially Supports
        pairs = re.findall(
            r"<strong>([^<:]+):</strong>\s*(" + "|".join(CONFORMANCE_TERMS) + ")",
            part)
        # remarks: the div following the conformance div
        remarks = ""
        m = re.search(
            r"<div><strong>[^<:]+:</strong>\s*(?:" + "|".join(CONFORMANCE_TERMS)
            + r")\s*</div>\s*<div>(.*?)</div>\s*</div>", part, re.S)
        if m:
            remarks = clean_paragraphs(m.group(1))

        claims[num] = {
            "name": name,
            "level": level,
            "claims": [(scope, term) for scope, term in pairs],
            "remarks": remarks,
        }
    return claims


CRITERION_CELL = re.compile(
    r"^\s*(\d+\.\d+\.\d+)\s+(.+?)\s*\(Level (A+)(?:[,;][^)]*)?\)\s*$", re.S)


def parse_claims_pdf(pdf_path):
    """Return the same {sc_number: {...}} dict from an ITI VPAT 2.5 PDF.

    Walks every table on every page; a row counts when its first cell is
    "d.d.d Name (Level X[, WCAG 2.2])" and its second cell starts with a
    conformance term. Cells are read by table geometry (PyMuPDF
    find_tables), never from the flowed text — `pdftotext -layout`
    interleaves the remarks column with the rows above and below it.
    Section 508 / EN 301 549 chapters have no such first cell and are
    skipped. Rows split across a page break arrive as two rows; the
    second has an empty criterion cell and its remarks are appended.
    """
    try:
        import pymupdf
    except ImportError:
        sys.exit("PDF import needs pymupdf: python -m pip install -r requirements.txt")
    claims, last = {}, None
    with pymupdf.open(str(pdf_path)) as doc:
        for page in doc:
            for table in page.find_tables():
                for row in table.extract():
                    cells = [re.sub(r"\s+", " ", (c or "")).strip() for c in row]
                    if len(cells) < 3:
                        continue
                    head = CRITERION_CELL.match(cells[0])
                    if not head:
                        if last and not cells[0] and not cells[1] and cells[2]:
                            claims[last]["remarks"] = (
                                claims[last]["remarks"] + " " + cells[2]).strip()
                        continue
                    term = next((t for t in sorted(CONFORMANCE_TERMS, key=len, reverse=True)
                                 if cells[1].startswith(t)), None)
                    if not term:
                        continue
                    num, name, level = head.group(1), clean(head.group(2)), head.group(3)
                    claims[num] = {"name": name, "level": level,
                                   "claims": [("Product", term)],
                                   "remarks": cells[2]}
                    last = num
    return claims


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scripts/import_acr.py <review> <acr.html|acr.pdf>")
    review = resolve(sys.argv[1])
    acr_path = Path(sys.argv[2])

    if acr_path.suffix.lower() == ".pdf":
        title = acr_path.stem
        claims = parse_claims_pdf(acr_path)
        if not claims:
            sys.exit("No WCAG criterion claims found — is this an ITI VPAT 2.5 PDF "
                     "with 'Criteria | Conformance Level | Remarks' tables?")
    else:
        html = acr_path.read_text(encoding="utf-8", errors="replace")
        title = clean(re.search(r"<title>(.*?)</title>", html, re.S).group(1)) \
            if "<title>" in html else acr_path.name
        claims = parse_claims(html)
        if not claims:
            sys.exit("No WCAG criterion claims found — is this an Adobe-format HTML ACR?")

    # 1. extracted claims file
    out = [f"# Extracted WCAG claims — {title}",
           "",
           f"Source file: `{acr_path.name}` (as received; see `02-vendor.md` for report metadata).",
           f"Extracted by `scripts/import_acr.py`. {len(claims)} criteria found.",
           ""]
    for num in sorted(claims, key=lambda n: [int(x) for x in n.split(".")]):
        c = claims[num]
        claimed = ", ".join(f"{s}: {t}" for s, t in c["claims"]) or "(no level found)"
        out += [f"## {num} {c['name']} (Level {c['level']})",
                f"**Claimed:** {claimed}", ""]
        if c["remarks"]:
            out += [c["remarks"], ""]
    claims_path = review / "vendor-acr" / "acr-wcag-claims.md"
    claims_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {claims_path.relative_to(ROOT)}")

    # 2. fill Vendor claim lines in 05-results.md
    results_path = review / "05-results.md"
    text = results_path.read_text(encoding="utf-8")
    filled = missing = already = 0

    blocks = re.split(r"(?=^### )", text, flags=re.M)
    for i, block in enumerate(blocks):
        head = re.match(r"### (\d+\.\d+\.\d+) ", block)
        if not head:
            continue
        num = head.group(1)
        if not re.search(r"(?m)^- \*\*Vendor claim:\*\*\s*$", block):
            already += 1
            continue
        if num in claims:
            summary = ", ".join(f"{t} ({s})" for s, t in claims[num]["claims"]) \
                or "(level not stated)"
            filled += 1
        else:
            summary = "Not covered by vendor ACR"
            missing += 1
        blocks[i] = re.sub(r"(?m)^- \*\*Vendor claim:\*\*\s*$",
                           f"- **Vendor claim:** {summary}", block, count=1)
    results_path.write_text("".join(blocks), encoding="utf-8")
    print(f"05-results.md: {filled} vendor claims filled, "
          f"{missing} marked not covered by the ACR"
          + (f", {already} already had a value (untouched)" if already else ""))

    uncovered = [num for num in claims
                 if not re.search(rf"(?m)^### {re.escape(num)} ", text)]
    if uncovered:
        print("In ACR but not in our WCAG 2.2 A/AA tables: "
              + ", ".join(sorted(uncovered)))


if __name__ == "__main__":
    main()
