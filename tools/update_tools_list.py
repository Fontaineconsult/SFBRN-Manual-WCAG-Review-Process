"""Fetch the W3C WAI Web Accessibility Evaluation Tools List and convert it
into the searchable markdown catalog wai-evaluation-tools.md.

Usage: python update_tools_list.py
"""
import datetime
import html as htmlmod
import os
import re
import urllib.request

URL = "https://www.w3.org/WAI/test-evaluate/tools/list/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "wai-evaluation-tools.md")

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    raw = resp.read().decode("utf-8")


def strip_tags(s):
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = htmlmod.unescape(s)
    return s


def slugify(s):
    s = htmlmod.unescape(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def clean_inline(s):
    """Collapse whitespace and tidy comma-separated value lists."""
    s = strip_tags(s)
    s = re.sub(r"\s+", " ", s).strip()
    # tidy artifacts like "Subscription, ," or trailing commas
    parts = [p.strip() for p in s.split(",")]
    parts = [p for p in parts if p]
    return ", ".join(parts)


# Grab everything inside the tools list body, then split into tool boxes.
body_start = raw.find('id="tools-list-body"')
body = raw[body_start:]

boxes = re.findall(
    r'<aside class="box" id="([^"]+)">(.*?)</aside>', body, re.DOTALL
)

tools = []
for anchor, box in boxes:
    m = re.search(
        r'<header class="box-h\s*">\s*<a href="([^"]*)"[^>]*><h3>(.*?)</h3>',
        box,
        re.DOTALL,
    )
    if not m:
        continue
    url, name = htmlmod.unescape(m.group(1)), clean_inline(m.group(2))

    vendor = ""
    mv = re.search(r'<p class="leftColHeader">(.*?)</p>', box, re.DOTALL)
    if mv:
        vendor = clean_inline(mv.group(1))
        vendor = re.sub(r"^by\s+", "", vendor)

    updated = ""
    mu = re.search(r'<p class="rightColHeader">(.*?)</p>', box, re.DOTALL)
    if mu:
        updated = clean_inline(mu.group(1))
        updated = re.sub(r"^Last updated:\s*", "", updated)

    desc = ""
    md = re.search(
        r"<h4>Description</h4>(.*?)(?:<h4>Guidelines</h4>|<div class=\"rightCol\">)",
        box,
        re.DOTALL,
    )
    if md:
        text = strip_tags(md.group(1))
        # collapse whitespace but keep deliberate line breaks from <br>
        lines = [re.sub(r"\s+", " ", ln).strip() for ln in text.split("\n")]
        desc = " ".join(ln for ln in lines if ln)

    guidelines = []
    mg = re.search(r"<h4>Guidelines</h4>(.*?)</div>\s*<div class=\"rightCol\">",
                   box, re.DOTALL)
    if mg:
        for tag in re.findall(r'<div class="tag">(.*?)</div>', mg.group(1), re.DOTALL):
            g = clean_inline(tag)
            if g:
                guidelines.append(g)

    features = []  # list of (label, value) preserving page order
    for alt, val in re.findall(
        r'<img src="[^"]*"\s+alt="([^"]+)"\s*/>\s*<p>(.*?)</p>', box, re.DOTALL
    ):
        v = clean_inline(val)
        if v:
            features.append((alt.strip(), v))

    tools.append({
        "anchor": slugify(anchor),
        "name": name,
        "url": url,
        "vendor": vendor,
        "updated": updated,
        "desc": desc,
        "guidelines": guidelines,
        "features": features,
    })

# de-duplicate anchors used twice (details element reuses the box id)
print(f"Parsed {len(tools)} tools")

today = datetime.date.today().isoformat()
out = []
out.append(f"""<!--
  Source: https://www.w3.org/WAI/test-evaluate/tools/list/
  Web Accessibility Evaluation Tools List - W3C Web Accessibility Initiative (WAI)
  Retrieved and converted to markdown on {today}.
  Tool information is submitted by vendors and others; W3C does not endorse
  specific products. Copyright (c) W3C (MIT, ERCIM, Keio, Beihang).
  https://www.w3.org/copyright/
-->

# Web Accessibility Evaluation Tools List

Source: <https://www.w3.org/WAI/test-evaluate/tools/list/>

Web accessibility evaluation tools are software programs or online services
that help you determine if web content meets accessibility guidelines. This
catalog lists the tools from the W3C WAI Evaluation Tools List so they can be
searched locally (grep / IDE search) when selecting tools for an evaluation.

> **Disclaimer:** Information is provided by tool vendors and others.
> W3C/WAI does not endorse specific products and does not verify claims.
> For guidance on choosing tools, see
> [Selecting Web Accessibility Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/).

""")

out.append(f"**{len(tools)} tools.**\n")

# Index table
out.append("## Index\n")
out.append("| Tool | Provider | Guidelines |")
out.append("|------|----------|------------|")
for t in tools:
    gl = ", ".join(t["guidelines"]) if t["guidelines"] else "—"
    out.append(f"| [{t['name']}](#{t['anchor']}) | {t['vendor'] or '—'} | {gl} |")
out.append("")

out.append("---\n")
out.append("## Tools\n")

for t in tools:
    out.append(f'### <a id="{t["anchor"]}"></a>{t["name"]}\n')
    out.append(f"- **Website:** <{t['url']}>")
    if t["vendor"]:
        out.append(f"- **Provider:** {t['vendor']}")
    if t["updated"]:
        out.append(f"- **Last updated:** {t['updated']}")
    if t["guidelines"]:
        out.append(f"- **Guidelines:** {', '.join(t['guidelines'])}")
    for label, val in t["features"]:
        out.append(f"- **{label}:** {val}")
    if t["desc"]:
        out.append("")
        out.append(t["desc"])
    out.append("")

open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(f"Wrote {OUT}")
