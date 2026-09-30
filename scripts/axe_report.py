"""Render a run's raw axe JSON as a human-readable Markdown report.

`axe_scan.py` saves `evidence/runs/R###/R###-axe.json` (the record) and
transcribes one observation per rule into `run.md`. That JSON is 50–300 KB of
selectors and check data nobody reads back; this script renders it as
`R###-axe.md` beside it — what fired, on which elements, why axe thinks so,
and what it could not decide — so a reviewer can triage W1/W2 without
opening the JSON.

Recon shape, not a finding: every violation still has to be confirmed
against the page's walk or dismissed in writing (testing-tools.md §axe-core).
Contrast numbers in particular are unreliable where axe assumed a
background (bgGradient / bgImage / pseudo-element cases) — the report says
so next to each such node.

Usage
    python scripts/axe_report.py <review>            # every run holding an R###-axe.json
    python scripts/axe_report.py <review> R004 R008  # just these runs
    python scripts/axe_report.py --json PATH [--out PATH]   # one file, anywhere

`axe_scan.py` calls `write(run_dir, run_id, result)` after every scan, so a
scan always leaves both files; this CLI exists for re-rendering (after a
renderer change) and for JSON captured some other way.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REVIEWS = ROOT / "reviews"
sys.path.insert(0, str(ROOT / "scripts"))
from axe_scan import tag_criteria  # noqa: E402  (one source for tag → criterion)

IMPACT_ORDER = {"critical": 0, "serious": 1, "moderate": 2, "minor": 3, None: 4, "": 4}
IMPACT_GLOSS = {
    "critical": "blocks the task for the affected users",
    "serious": "a serious barrier, a workaround is unlikely",
    "moderate": "a barrier with a plausible workaround",
    "minor": "a nuisance rather than a barrier",
}
# axe messageKeys that mean "I assumed a background" — the number is fiction
# until a human samples the pixels (testing-tools.md §axe-core, §zoom)
UNMEASURED_KEYS = {"bgGradient", "bgImage", "bgOverlap", "pseudoContent", "imgNode", "elmPartiallyObscured", "elmPartiallyObscuring"}
MAX_NODES = 12


def _code(s: str, limit: int = 220) -> str:
    """One-line inline code span; never lets a backtick or newline break the table."""
    s = re.sub(r"\s+", " ", s or "").strip()
    if len(s) > limit:
        s = s[: limit - 1] + "…"
    s = s.replace("`", "'")
    return f"`{s}`" if s else "—"


def _target(node: dict) -> str:
    t = node.get("target") or []
    parts = []
    for sel in t:
        parts.append(" › ".join(sel) if isinstance(sel, list) else str(sel))  # shadow-DOM targets are lists
    return " ; ".join(parts)


def _check_lines(node: dict) -> list[str]:
    """Why axe decided what it decided, from the node's any/all/none checks."""
    out = []
    for group, label in (("any", "any of"), ("all", "all of"), ("none", "none of")):
        for c in node.get(group) or []:
            msg = c.get("message") or c.get("id")
            data = c.get("data")
            extra = ""
            if isinstance(data, dict) and data:
                keep = {k: v for k, v in data.items() if k in (
                    "contrastRatio", "expectedContrastRatio", "fontSize", "fontWeight", "fgColor", "bgColor",
                    "messageKey", "role", "name", "accessibleText", "minSize", "width", "height", "reason")}
                if keep:
                    extra = " — " + ", ".join(f"{k} {v}" for k, v in keep.items())
                if data.get("messageKey") in UNMEASURED_KEYS:
                    extra += " — **treat as unmeasured**: axe could not resolve the real background; settle by rendered-pixel sampling"
            out.append(f"    - ({label}) {msg}{extra}")
    return out


def _rule_section(rule: dict, kind: str) -> list[str]:
    scs = tag_criteria(rule.get("tags"))
    sc_txt = ", ".join(f"WCAG {x}" for x in scs) if scs else "no WCAG criterion (axe best practice)"
    impact = rule.get("impact") or "n/a"
    nodes = rule.get("nodes") or []
    lines = [f"### `{rule['id']}` — {rule.get('help', '')}",
             "",
             f"- **Impact:** {impact}" + (f" ({IMPACT_GLOSS[impact]})" if impact in IMPACT_GLOSS else ""),
             f"- **Criteria:** {sc_txt}",
             f"- **Nodes:** {len(nodes)}",
             f"- **Rule:** {rule.get('description', '')} ([axe docs]({rule.get('helpUrl', '')}))"]
    if kind == "incomplete":
        lines.append("- **Status:** axe could not decide — a human must; route to the modality run that can settle it (W2)")
    else:
        lines.append("- **Status:** reported failure — confirm against this page's walk → finding, or dismiss with a written reason (W1)")
    lines.append("")
    for i, node in enumerate(nodes[:MAX_NODES], 1):
        lines.append(f"{i}. **Element:** {_code(node.get('html', ''))}")
        lines.append(f"    - **Selector:** {_code(_target(node), 160)}")
        lines += _check_lines(node)
        related = [rn for c in (node.get("any") or []) + (node.get("all") or []) + (node.get("none") or []) for rn in (c.get("relatedNodes") or [])]
        if related:
            lines.append(f"    - Related: " + "; ".join(_code(rn.get('html', ''), 100) for rn in related[:3]))
    if len(nodes) > MAX_NODES:
        lines.append(f"{MAX_NODES + 1}. … and {len(nodes) - MAX_NODES} more node(s) — see the JSON")
    lines.append("")
    return lines


def render(result: dict, run_id: str | None = None, view: str | None = None) -> str:
    v = sorted(result.get("violations", []), key=lambda r: IMPACT_ORDER.get(r.get("impact"), 4))
    inc = sorted(result.get("incomplete", []), key=lambda r: IMPACT_ORDER.get(r.get("impact"), 4))
    passes = result.get("passes", [])
    inapp = result.get("inapplicable", [])
    eng = result.get("testEngine", {})
    env = result.get("testEnvironment", {})
    opts = result.get("toolOptions", {})
    run_only = opts.get("runOnly", {}).get("values") if isinstance(opts.get("runOnly"), dict) else None

    title = f"axe sweep — {run_id}" + (f" ({view})" if view else "") if run_id else "axe sweep"
    L = [f"# {title}", "",
         "Rendered from the raw axe JSON by `scripts/axe_report.py`. Recon, not findings: "
         "a violation becomes a finding only when the page's walk confirms it, and a clean "
         "sweep is not a pass (testing-tools.md §axe-core). Cross-origin iframes and closed "
         "shadow roots are invisible to axe — anything inside them is untested here.",
         "",
         "| | |", "|---|---|",
         f"| URL scanned | {result.get('url', '')} |",
         f"| Scanned at | {result.get('timestamp', '')} |",
         f"| Engine | {eng.get('name', 'axe-core')} {eng.get('version', '')} |",
         f"| Browser | {(env.get('userAgent') or '')[:120]} |",
         f"| Viewport | {env.get('windowWidth', '')} × {env.get('windowHeight', '')} |",
         f"| Rules run | {', '.join(run_only) if run_only else 'default ruleset (all tags)'} |",
         "",
         "## Summary", "",
         "| Bucket | Rules | Nodes | Meaning |", "|---|---|---|---|",
         f"| Violations | {len(v)} | {sum(len(r.get('nodes', [])) for r in v)} | axe is confident these fail — each needs a human yes/no (W1) |",
         f"| Incomplete | {len(inc)} | {sum(len(r.get('nodes', [])) for r in inc)} | axe could not decide — route to the modality that can (W2) |",
         f"| Passes | {len(passes)} | {sum(len(r.get('nodes', [])) for r in passes)} | rules that ran and found nothing wrong on the nodes they apply to |",
         f"| Inapplicable | {len(inapp)} | — | rules with nothing on this page to test |",
         ""]
    if v:
        L += ["### Violations by impact", ""]
        for imp in ("critical", "serious", "moderate", "minor"):
            rs = [r for r in v if r.get("impact") == imp]
            if rs:
                L.append(f"- **{imp}** ({IMPACT_GLOSS[imp]}): " + ", ".join(f"`{r['id']}` ×{len(r.get('nodes', []))}" for r in rs))
        L.append("")
    L += ["## Violations", ""]
    if v:
        for r in v:
            L += _rule_section(r, "violation")
    else:
        L += ["None reported.", ""]
    L += ["## Incomplete (needs a human)", ""]
    if inc:
        for r in inc:
            L += _rule_section(r, "incomplete")
    else:
        L += ["None reported.", ""]
    L += ["## Passes", "",
          "Rules that ran and found nothing wrong. A pass covers only what axe can see and only the "
          "nodes it matched — it is not a WCAG pass for the criterion.", "",
          "| Rule | Criteria | Nodes checked |", "|---|---|---|"]
    for r in sorted(passes, key=lambda r: r["id"]):
        scs = tag_criteria(r.get("tags"))
        L.append(f"| `{r['id']}` — {r.get('help', '')} | {', '.join(scs) if scs else '—'} | {len(r.get('nodes', []))} |")
    L += ["", "## Inapplicable", "",
          "Rules with nothing to test on this page (no matching element). Useful as a structural fact: "
          "e.g. no `video-caption` here means the page holds no `<video>`.", "",
          ", ".join(f"`{r['id']}`" for r in sorted(inapp, key=lambda r: r["id"])) or "None.", ""]
    return "\n".join(L)


def write(run_dir: Path, run_id: str, result: dict, view: str | None = None) -> Path:
    """Write R###-axe.md beside the JSON; returns the path. Called by axe_scan.py."""
    if view is None:
        m = re.search(r"\| \*\*View / sample\*\* \| (\S+) \|", (run_dir / "run.md").read_text(encoding="utf-8")) \
            if (run_dir / "run.md").exists() else None
        view = m.group(1) if m else None
    out = run_dir / f"{run_id}-axe.md"
    out.write_text(render(result, run_id, view), encoding="utf-8")
    return out


def resolve_review(token: str) -> Path:
    dirs = [d for d in REVIEWS.iterdir() if d.is_dir()]
    exact = [d for d in dirs if d.name == token]
    if exact:
        return exact[0]
    subs = [d for d in dirs if token.lower() in d.name.lower()]
    if len(subs) == 1:
        return subs[0]
    sys.exit(f"review '{token}' not found or ambiguous: {[d.name for d in subs] or [d.name for d in dirs]}")


def main():
    ap = argparse.ArgumentParser(description="render R###-axe.json as R###-axe.md")
    ap.add_argument("review", nargs="?", help="review dir or substring")
    ap.add_argument("runs", nargs="*", help="run IDs (default: every run with an axe JSON)")
    ap.add_argument("--json", help="render this one JSON file instead")
    ap.add_argument("--out", help="with --json: output path (default: next to it, .md)")
    a = ap.parse_args()

    if a.json:
        src = Path(a.json)
        result = json.loads(src.read_text(encoding="utf-8"))
        out = Path(a.out) if a.out else src.with_suffix(".md")
        out.write_text(render(result), encoding="utf-8")
        print(f"wrote {out}")
        return
    if not a.review:
        sys.exit("give a review (or --json PATH)")
    review = resolve_review(a.review)
    runs_dir = review / "evidence" / "runs"
    run_dirs = [runs_dir / r for r in a.runs] if a.runs else sorted(d for d in runs_dir.iterdir() if d.is_dir())
    n = 0
    for d in run_dirs:
        src = d / f"{d.name}-axe.json"
        if not src.exists():
            if a.runs:
                print(f"{d.name}: no {src.name}", file=sys.stderr)
            continue
        out = write(d, d.name, json.loads(src.read_text(encoding="utf-8")))
        result = json.loads(src.read_text(encoding="utf-8"))
        print(f"{d.name}: {out.relative_to(ROOT)}  violations {len(result.get('violations', []))}, "
              f"incomplete {len(result.get('incomplete', []))}, passes {len(result.get('passes', []))}, "
              f"inapplicable {len(result.get('inapplicable', []))}")
        n += 1
    if not n:
        sys.exit("no axe JSON found")


if __name__ == "__main__":
    main()
