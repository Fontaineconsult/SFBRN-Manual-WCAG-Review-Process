#!/usr/bin/env python3
"""axe_scan.py — per-view automated accessibility scan with axe-core.

Runs Deque's axe-core (vendored at tools/axe/axe.min.js) inside an
already-open, already-authenticated Chrome tab via the DevTools protocol,
and saves the RAW axe JSON into the run's evidence folder.

Setup (one-time per session): Chrome must expose a debugging port. Close
Chrome fully, then relaunch it with:

    chrome.exe --remote-debugging-port=9222

(The normal profile loads — you stay signed in.)

Usage:
    python scripts/axe_scan.py <review> --view S1 --url https://...
        [--run R###]        attach to an existing run instead of logging one
        [--port 9222]       CDP port (default 9222)
        [--tab TEXT]        substring to pick the tab (default: the --url)
        [--tags LIST]       axe runOnly tags, e.g. wcag2a,wcag2aa,wcag22aa
                            (default: full ruleset)

Behavior:
    1. Finds (or requires) the run: without --run it calls
       `review.py log-test <review> --view <view> --tool axe --url <url>`
       and uses the new run ID.
    2. Attaches to the Chrome tab whose URL contains --tab/--url text.
    3. Injects the vendored axe source, executes `axe.run(document)`.
    4. Saves evidence/runs/R###/R###-axe.json (raw, as returned).
    5. Prints a summary: counts + violations by impact with rule IDs.

The script only captures raw output; check outcomes, observations, and the
run Result are recorded in run.md by the assistant/reviewer per
ontology/modality-checks.md (automated-sweep checks) and testing-tools.md.
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

try:
    import websocket  # websocket-client
except ImportError:
    sys.exit("websocket-client not installed: pip install websocket-client")

ROOT = Path(__file__).resolve().parent.parent
AXE_SRC = ROOT / "tools" / "axe" / "axe.min.js"
REVIEWS = ROOT / "reviews"


def resolve_review(token: str) -> Path:
    dirs = [d for d in REVIEWS.iterdir() if d.is_dir()]
    exact = [d for d in dirs if d.name == token]
    if exact:
        return exact[0]
    subs = [d for d in dirs if token.lower() in d.name.lower()]
    if len(subs) == 1:
        return subs[0]
    sys.exit(f"review '{token}' not found or ambiguous: {[d.name for d in subs] or [d.name for d in dirs]}")


def log_new_run(review: Path, view: str, url: str) -> str:
    out = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "review.py"), "log-test",
         review.name, "--view", view, "--tool", "axe", "--url", url],
        capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"log-test failed:\n{out.stdout}\n{out.stderr}")
    for tok in out.stdout.split():
        if tok.startswith("R") and tok[1:4].isdigit():
            return tok.rstrip(":")
    sys.exit(f"could not parse run ID from log-test output:\n{out.stdout}")


def pick_tab(port: int, needle: str) -> dict:
    try:
        with urllib.request.urlopen(f"http://localhost:{port}/json", timeout=3) as r:
            tabs = json.load(r)
    except Exception as e:
        sys.exit(
            f"Cannot reach Chrome DevTools on port {port} ({e}).\n"
            "Close Chrome fully, then relaunch with:\n"
            "  chrome.exe --remote-debugging-port=9222")
    pages = [t for t in tabs if t.get("type") == "page"]
    hits = [t for t in pages if needle.lower() in t.get("url", "").lower()]
    if not hits:
        listing = "\n".join(f"  {t['url']}" for t in pages)
        sys.exit(f"no tab matching '{needle}'. Open tabs:\n{listing}")
    return hits[0]


class CDP:
    def __init__(self, ws_url: str):
        self.ws = websocket.create_connection(ws_url, timeout=120,
                                              max_size=64 * 1024 * 1024,
                                              suppress_origin=True)
        self.mid = 0

    def call(self, method: str, **params):
        self.mid += 1
        self.ws.send(json.dumps({"id": self.mid, "method": method,
                                 "params": params}))
        deadline = time.time() + 120
        while time.time() < deadline:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})
        raise TimeoutError(method)

    def eval(self, expression: str, await_promise=False):
        res = self.call("Runtime.evaluate", expression=expression,
                        awaitPromise=await_promise, returnByValue=True,
                        timeout=90_000)
        if res.get("exceptionDetails"):
            raise RuntimeError(json.dumps(res["exceptionDetails"])[:2000])
        return res.get("result", {}).get("value")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("review", nargs="?",
                    help="review dir or substring (omit with --out for an "
                         "ad-hoc scan outside any run)")
    ap.add_argument("--view", help="sample ID (required unless --out)")
    ap.add_argument("--url", required=True)
    ap.add_argument("--run", help="existing run ID (default: log a new run)")
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--tab", help="tab-picking substring (default: --url)")
    ap.add_argument("--tags", help="comma list for axe runOnly tags")
    ap.add_argument("--out", help="ad-hoc mode: save raw JSON to this path "
                                  "instead of a run folder (no run logged)")
    args = ap.parse_args()

    review = None
    if not args.out:
        if not (args.review and args.view):
            sys.exit("review and --view are required (or use --out)")
        review = resolve_review(args.review)

    # Connect BEFORE logging a run, so a connection failure never orphans a
    # freshly-scaffolded run folder (learned from R008, 2026-08-04).
    tab = pick_tab(args.port, args.tab or args.url)
    print(f"tab: {tab['url'][:100]}")
    cdp = CDP(tab["webSocketDebuggerUrl"])

    if args.out:
        run_dir, run_id = None, None
        out_path = Path(args.out)
    else:
        run_id = args.run or log_new_run(review, args.view, args.url)
        run_dir = review / "evidence" / "runs" / run_id
        if not run_dir.is_dir():
            sys.exit(f"run folder not found: {run_dir}")
        out_path = run_dir / f"{run_id}-axe.json"

    axe_js = AXE_SRC.read_text(encoding="utf-8")
    cdp.eval(axe_js + "\n;axe.version")
    print(f"axe-core injected: v{cdp.eval('axe.version')}")

    opts = {"reporter": "v1"}
    if args.tags:
        opts["runOnly"] = {"type": "tag",
                           "values": [t.strip() for t in args.tags.split(",")]}
    raw = cdp.eval(
        f"axe.run(document, {json.dumps(opts)}).then(r => JSON.stringify(r))",
        await_promise=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(raw, encoding="utf-8")
    result = json.loads(raw)

    try:
        shown = out_path.relative_to(ROOT)
    except ValueError:
        shown = out_path
    print(f"\nraw output: {shown}  ({len(raw):,} bytes)")
    print(f"engine: axe-core {result.get('testEngine', {}).get('version')}"
          f"  url: {result.get('url', '')[:80]}")
    for bucket in ("violations", "incomplete", "passes", "inapplicable"):
        print(f"  {bucket}: {len(result.get(bucket, []))}")
    if result.get("violations"):
        print("\nviolations by impact:")
        by_impact = {}
        for v in result["violations"]:
            by_impact.setdefault(v.get("impact") or "none", []).append(v)
        for impact in ("critical", "serious", "moderate", "minor", "none"):
            for v in by_impact.get(impact, []):
                print(f"  [{impact:8}] {v['id']}: {v['help']}"
                      f"  (nodes: {len(v['nodes'])})")
    inc = result.get("incomplete", [])
    if inc:
        print("\nincomplete (needs human review):")
        for v in inc:
            print(f"  [{(v.get('impact') or 'n/a'):8}] {v['id']}"
                  f"  (nodes: {len(v['nodes'])})")
    if run_dir is not None:
        print(f"\nNext: record outcomes in {run_dir.relative_to(ROOT)}\\run.md "
              "(automated-sweep checks; testing-tools.md conventions).")


if __name__ == "__main__":
    main()
