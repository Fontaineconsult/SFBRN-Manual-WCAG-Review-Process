#!/usr/bin/env python3
r"""export_report.py — render a review's 06-report.md as a Word document.

Usage:
    python scripts/export_report.py <review> [--out PATH] [--file STAGE.md]

    <review>     review directory name or unique substring (as review.py)
    --out PATH   output .docx (default: reviews/<id>/<id>-report.docx)
    --file NAME  render a different stage file (default 06-report.md)

Converts the markdown subset our templates use — ATX headings (#/##/###),
pipe tables, nested bullet/numbered lists, and inline **bold**, *italic*,
`code` — into a styled .docx via python-docx (pip install python-docx; no
pandoc dependency, so it runs on any team machine).

The .docx is generated OUTPUT, not a system-of-record file: edit
06-report.md and re-export; never hand-edit facts into the Word file.
An accessible document needs real heading styles and real tables — which is
exactly what this produces (Heading 1–3 styles, header-row tables) — but
run the exported file through Word's own Accessibility Checker before
sending it anywhere official.
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import docx
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, RGBColor, Inches
except ImportError:
    sys.exit("python-docx not installed: python -m pip install python-docx")

ROOT = Path(__file__).resolve().parent.parent
REVIEWS = ROOT / "reviews"

MONO = "Consolas"

# Palette. Restrained on purpose: this is a procurement document, and an
# accessibility report that is itself hard to read undermines its own case.
# Every colour below is decoration only — outcome and severity are always
# carried by the words as well, so nothing here depends on colour
# perception (the report would otherwise fail the 1.4.1 it tests for).
ACCENT = RGBColor(0x1F, 0x38, 0x64)      # deep navy — headings
ACCENT_HEX = "1F3864"
HEADER_SHADE = "DCE6F1"                  # light blue — table header rows
ZEBRA_SHADE = "F4F7FB"                   # barely-there tint — alternate rows
RULE_HEX = "8EAADB"                      # heading underline

# Outcome/severity tints. Text is never removed or replaced by these.
SEV_COLORS = {
    "does not support": RGBColor(0xA6, 0x1B, 0x1B),
    "fail": RGBColor(0xA6, 0x1B, 0x1B),
    "blocker": RGBColor(0xA6, 0x1B, 0x1B),
    "partially supports": RGBColor(0x9C, 0x50, 0x00),
    "pass with barriers": RGBColor(0x9C, 0x50, 0x00),
    "major": RGBColor(0x9C, 0x50, 0x00),
    "needs taap": RGBColor(0x9C, 0x50, 0x00),
    "works with issues": RGBColor(0x9C, 0x50, 0x00),
    "supports": RGBColor(0x1E, 0x60, 0x2E),
    "pass": RGBColor(0x1E, 0x60, 0x2E),
    "works": RGBColor(0x1E, 0x60, 0x2E),
}
# Longest first, so "does not support" wins over "supports".
SEV_KEYS = sorted(SEV_COLORS, key=len, reverse=True)


def tint_outcome(cell):
    """Colour a table cell whose whole text is an outcome/severity term.

    Applied only when the cell is *just* the term — never mid-sentence — so
    the cue reinforces the word instead of decorating prose.
    """
    text = cell.text.strip().lower().strip("*")
    for key in SEV_KEYS:
        if text == key or text.startswith(key + " "):
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.color.rgb = SEV_COLORS[key]
                    r.bold = True
            return


def resolve_review(token: str) -> Path:
    dirs = [d for d in REVIEWS.iterdir() if d.is_dir()]
    exact = [d for d in dirs if d.name == token]
    if exact:
        return exact[0]
    subs = [d for d in dirs if token.lower() in d.name.lower()]
    if len(subs) == 1:
        return subs[0]
    sys.exit(f"review '{token}' not found or ambiguous: "
             f"{[d.name for d in subs] or [d.name for d in dirs]}")


# ---------------------------------------------------------------- inline ----

INLINE = re.compile(
    r"(\*\*\*(?P<bi>.+?)\*\*\*"      # ***bold italic***
    r"|\*\*(?P<b>.+?)\*\*"           # **bold**
    r"|\*(?P<i>[^*]+?)\*"            # *italic*
    r"|`(?P<c>[^`]+?)`)"             # `code`
)


def add_runs(paragraph, text):
    """Append runs to a paragraph, honouring **bold**, *italic*, `code`."""
    pos = 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        if m.group("bi") is not None:
            r = paragraph.add_run(m.group("bi"))
            r.bold = r.italic = True
        elif m.group("b") is not None:
            paragraph.add_run(m.group("b")).bold = True
        elif m.group("i") is not None:
            paragraph.add_run(m.group("i")).italic = True
        else:
            r = paragraph.add_run(m.group("c"))
            r.font.name = MONO
            r.font.size = Pt(9.5)
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


# ----------------------------------------------------------------- blocks ---

def shade_cell(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_separator(line):
    return bool(re.fullmatch(r"\|?[\s:|-]+\|?", line.strip())) and "-" in line


def add_table(doc, rows):
    header, body = rows[0], rows[1:]
    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=0, cols=ncols)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = True

    header_is_empty = all(not c for c in header)
    if not header_is_empty:
        cells = table.add_row().cells
        for i, text in enumerate(header):
            p = cells[i].paragraphs[0]
            add_runs(p, text)
            for r in p.runs:
                r.bold = True
            shade_cell(cells[i], HEADER_SHADE)
        # repeat header row across pages
        trPr = table.rows[0]._tr.get_or_add_trPr()
        th = OxmlElement("w:tblHeader")
        th.set(qn("w:val"), "true")
        trPr.append(th)

    for n, row in enumerate(body):
        cells = table.add_row().cells
        for i in range(ncols):
            add_runs(cells[i].paragraphs[0], row[i] if i < len(row) else "")
            if n % 2 == 1:
                shade_cell(cells[i], ZEBRA_SHADE)
            tint_outcome(cells[i])
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                for r in p.runs:
                    if r.font.size is None:
                        r.font.size = Pt(9.5)


def add_rule(paragraph, hex_color=RULE_HEX, size=6):
    """Draw a bottom border under a paragraph (used to underline H1s)."""
    pPr = paragraph._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), hex_color)
    borders.append(bottom)
    pPr.append(borders)


def add_field(paragraph, instr):
    """Insert a Word field (PAGE, NUMPAGES, TOC...) into a paragraph."""
    r = paragraph.add_run()
    for el, attrs, text in (("w:fldChar", {"w:fldCharType": "begin"}, None),
                            ("w:instrText", {"xml:space": "preserve"}, instr),
                            ("w:fldChar", {"w:fldCharType": "separate"}, None),
                            ("w:fldChar", {"w:fldCharType": "end"}, None)):
        e = OxmlElement(el)
        for k, v in attrs.items():
            e.set(qn(k), v)
        if text:
            e.text = text
        r._r.append(e)


def add_footer(doc, stamp):
    from docx.enum.text import WD_TAB_ALIGNMENT
    sec = doc.sections[0]
    p = sec.footer.paragraphs[0]
    p.text = ""
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.7), WD_TAB_ALIGNMENT.RIGHT)
    r = p.add_run(stamp + "\t")
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
    pg = p.add_run("Page ")
    pg.font.size = Pt(8.5)
    add_field(p, "PAGE")
    of = p.add_run(" of ")
    of.font.size = Pt(8.5)
    add_field(p, "NUMPAGES")
    for run in p.runs:
        run.font.size = Pt(8.5)
        run.font.color.rgb = RGBColor(0x59, 0x59, 0x59)


def add_toc(doc):
    p = doc.add_paragraph(style="Heading 1")
    p.add_run("Contents")
    tp = doc.add_paragraph()
    add_field(tp, r'TOC \o "1-2" \h \z \u')
    note = doc.add_paragraph()
    r = note.add_run("(In Word: right-click the table of contents → "
                     "Update Field, or select all and press F9, to populate "
                     "page numbers.)")
    r.italic = True
    r.font.size = Pt(9)
    doc.add_page_break()


def convert(md_path: Path, out_path: Path):
    import datetime
    doc = docx.Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(8)
    style.paragraph_format.line_spacing = 1.12   # easier on the eye at length

    for name, size in (("Heading 1", 17), ("Heading 2", 13.5),
                       ("Heading 3", 11.5)):
        s = doc.styles[name]
        s.font.size = Pt(size)
        s.font.color.rgb = ACCENT
        s.font.bold = True
        s.paragraph_format.keep_with_next = True   # heading never orphaned
        s.paragraph_format.space_before = Pt(16 if size > 13 else 12)
        s.paragraph_format.space_after = Pt(4)

    title = doc.styles["Title"]
    title.font.color.rgb = ACCENT
    title.font.size = Pt(26)

    for sec in doc.sections:
        sec.left_margin = sec.right_margin = Inches(0.9)
    add_footer(doc, f"Generated {datetime.date.today().isoformat()} from "
                    f"{md_path.name} — edit the markdown and re-export")

    lines = md_path.read_text(encoding="utf-8").splitlines()
    i, first_h1, pending_toc = 0, True, False
    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            if level == 1 and first_h1:
                p = doc.add_paragraph(style="Title")
                add_runs(p, text)
                add_rule(p, ACCENT_HEX, size=12)
                first_h1 = False
                pending_toc = True   # emit TOC after the metadata table
            else:
                p = doc.add_paragraph(style=f"Heading {min(level, 3)}")
                add_runs(p, text)
                if level <= 2:
                    add_rule(p)
            i += 1
            continue

        if line.lstrip().startswith("|"):
            rows, j = [], i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                if not is_separator(lines[j]):
                    rows.append(split_row(lines[j]))
                j += 1
            if rows:
                add_table(doc, rows)
                doc.add_paragraph().paragraph_format.space_after = Pt(2)
            if pending_toc:      # first table = the metadata block; TOC after it
                add_toc(doc)
                pending_toc = False
            i = j
            continue

        if re.match(r"^\s*[-*]\s+", line) or re.match(r"^\s*\d+\.\s+", line):
            # one list item; unwrap its continuation lines
            indent = len(line) - len(line.lstrip())
            numbered = bool(re.match(r"^\s*\d+\.\s+", line))
            text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line).rstrip()
            j = i + 1
            while (j < len(lines) and lines[j].strip()
                   and not re.match(r"^\s*(?:[-*]|\d+\.)\s+", lines[j])
                   and not lines[j].lstrip().startswith(("|", "#"))
                   and (len(lines[j]) - len(lines[j].lstrip())) > indent):
                text += " " + lines[j].strip()
                j += 1
            depth = min(indent // 2, 2)
            base = "List Number" if numbered else "List Bullet"
            style_name = base if depth == 0 else f"{base} {depth + 1}"
            p = doc.add_paragraph(style=style_name)
            add_runs(p, text)
            i = j
            continue

        if line.strip() in ("---", "***", "___"):
            i += 1
            continue

        if line.lstrip().startswith(">"):
            text = re.sub(r"^\s*>\s?", "", line).rstrip()
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith(">"):
                text += " " + re.sub(r"^\s*>\s?", "", lines[j]).strip()
                j += 1
            p = doc.add_paragraph(style="Intense Quote")
            add_runs(p, text)
            i = j
            continue

        # ordinary paragraph; unwrap hard-wrapped source lines
        text, j = line.rstrip(), i + 1
        while (j < len(lines) and lines[j].strip()
               and not lines[j].lstrip().startswith(("|", "#", "-", "*", ">"))
               and not re.match(r"^\s*\d+\.\s+", lines[j])):
            text += " " + lines[j].strip()
            j += 1
        p = doc.add_paragraph()
        add_runs(p, text)
        i = j

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("review", help="review directory name or unique substring")
    ap.add_argument("--out", help="output .docx path")
    ap.add_argument("--file", default="06-report.md",
                    help="stage file to render (default 06-report.md)")
    args = ap.parse_args()

    review = resolve_review(args.review)
    src = review / args.file
    if not src.exists():
        sys.exit(f"{src} does not exist")
    out = Path(args.out) if args.out else review / f"{review.name}-report.docx"
    try:
        convert(src, out)
    except PermissionError:
        # The target is almost certainly open in Word, which locks it.
        import datetime
        alt = out.with_name(f"{out.stem}-"
                            f"{datetime.datetime.now():%H%M%S}{out.suffix}")
        convert(src, alt)
        print(f"NOTE: {out.name} is locked (open in Word?) — wrote {alt.name}"
              f" instead. Close the old copy in Word; it is now stale.")
        out = alt
    print(f"wrote {out}  ({out.stat().st_size:,} bytes)")
    print("Reminder: the .docx is generated output — edit the markdown and "
          "re-export. Run Word's Accessibility Checker before distribution.")


if __name__ == "__main__":
    main()
