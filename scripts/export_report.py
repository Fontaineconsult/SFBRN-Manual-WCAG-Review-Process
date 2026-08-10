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
HEADER_SHADE = "D9D9D9"          # light grey for table header rows


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

    for row in body:
        cells = table.add_row().cells
        for i in range(ncols):
            add_runs(cells[i].paragraphs[0], row[i] if i < len(row) else "")
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    if r.font.size is None:
                        r.font.size = Pt(9.5)


def convert(md_path: Path, out_path: Path):
    doc = docx.Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    for name, size in (("Heading 1", 17), ("Heading 2", 14), ("Heading 3", 12)):
        s = doc.styles[name]
        s.font.size = Pt(size)
        s.font.color.rgb = RGBColor(0x1F, 0x1F, 0x1F)
    for sec in doc.sections:
        sec.left_margin = sec.right_margin = Inches(0.9)

    lines = md_path.read_text(encoding="utf-8").splitlines()
    i, first_h1 = 0, True
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
                first_h1 = False
            else:
                p = doc.add_paragraph(style=f"Heading {min(level, 3)}")
                add_runs(p, text)
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
    convert(src, out)
    print(f"wrote {out}  ({out.stat().st_size:,} bytes)")
    print("Reminder: the .docx is generated output — edit the markdown and "
          "re-export. Run Word's Accessibility Checker before distribution.")


if __name__ == "__main__":
    main()
