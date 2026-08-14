#!/usr/bin/env python3
r"""crawl_map.py — enclosure mapping: harvest a product's views and
fingerprint each one over CDP (WCAG-EM step 2 support).

Two operations, deliberately separated:

  harvest   visit the given URL(s), collect same-origin link targets from
            the rendered page (shadow-piercing) — the CANDIDATE view map.
  map       visit each ALLOWLISTED URL and record its structure
            fingerprint: title, landmarks, heading outline, named/unnamed
            grid counts, unnamed interactive controls, canvases, custom
            -element histogram. This is what feeds the enclosure (03 §2.1
            /§2.3/§2.4 rows) and flags per-view risk before any run.

Usage:
    python scripts/crawl_map.py harvest URL [URL ...]
    python scripts/crawl_map.py map URL [URL ...] [--out FILE.md]
        [--port 9222]

**Hard guardrail — no autonomous crawling.** `harvest` never follows the
links it finds; a human (or the assistant, explicitly) promotes candidates
to `map`'s allowlist. On authenticated products a "link" can be an action —
in Adobe Express, navigating to certain URLs silently CREATES a document
(03 §2.6, 2026-08-06). For the same reason `map` refuses URL patterns that
look like actions or documents unless --allow-documents is set, verifies
the landed URL after navigation, and reports (rather than fingerprints) any
navigation that bounced somewhere else.

Output is RECON, not evidence: work it into `03-scope-and-sample.md` as
confirmed/hypothesis rows per ontology/assisted-exploration.md. It never
logs runs and never becomes findings.
"""
import argparse
import datetime
import json
import sys
import time
import urllib.parse
import urllib.request

try:
    import websocket
except ImportError:
    sys.exit("websocket-client not installed: pip install websocket-client")

REFUSE_DEFAULT = ("/new", "logout", "signout", "delete", "remove", "create",
                  "?action=", "purchase", "checkout", "upgrade")


class CDP:
    def __init__(self, port):
        tabs = json.load(urllib.request.urlopen(
            f"http://localhost:{port}/json", timeout=5))
        pages = [t for t in tabs if t.get("type") == "page"
                 and "service-worker" not in t.get("url", "")]
        if not pages:
            sys.exit(f"no page tab on port {port}")
        self.ws = websocket.create_connection(
            pages[0]["webSocketDebuggerUrl"], timeout=120,
            max_size=128 * 1024 * 1024, suppress_origin=True)
        self.mid = 0
        self.cmd("Page.enable")

    def cmd(self, method, params=None):
        self.mid += 1
        my = self.mid
        self.ws.send(json.dumps({"id": my, "method": method,
                                 "params": params or {}}))
        while True:
            m = json.loads(self.ws.recv())
            if m.get("id") == my:
                return m.get("result", {})

    def ev(self, expr):
        r = self.cmd("Runtime.evaluate",
                     {"expression": expr, "returnByValue": True,
                      "awaitPromise": True})
        return r.get("result", {}).get("value")

    def goto(self, url, settle=10):
        self.cmd("Page.navigate", {"url": url})
        time.sleep(settle)
        return self.ev("location.href") or ""


HARVEST_JS = r"""(() => {
  function deepAll(sel, root, out) { out=out||[]; root=root||document;
    try { out.push(...root.querySelectorAll(sel)); } catch(e){}
    for (const el of root.querySelectorAll('*')) if (el.shadowRoot) deepAll(sel, el.shadowRoot, out);
    return out; }
  const here = new URL(location.href);
  const seen = new Set(), out = [];
  for (const a of deepAll('a[href],sp-link[href],[role=link][href]')) {
    let href = a.getAttribute('href'); if (!href) continue;
    let u; try { u = new URL(href, location.href); } catch (e) { continue; }
    if (u.origin !== here.origin) continue;
    const key = u.pathname + u.search;
    if (seen.has(key)) continue; seen.add(key);
    let name=''; const c=n=>{if(n.nodeType===3)name+=n.textContent;
      else if(n.nodeType===1){if(n.shadowRoot)[...n.shadowRoot.childNodes].forEach(c);[...n.childNodes].forEach(c);}};c(a);
    name = (a.getAttribute('aria-label') || name).replace(/\s+/g,' ').trim();
    out.push({link: key, name: name.slice(0, 44)});
  }
  return out;
})()"""

FINGERPRINT_JS = r"""(() => {
  function deepAll(sel, root, out) { out=out||[]; root=root||document;
    try { out.push(...root.querySelectorAll(sel)); } catch(e){}
    for (const el of root.querySelectorAll('*')) if (el.shadowRoot) deepAll(sel, el.shadowRoot, out);
    return out; }
  const vis = e => { const r = e.getBoundingClientRect();
    const cs = getComputedStyle(e);
    return r.width>0 && r.height>0 && cs.visibility!=='hidden' && cs.display!=='none'; };
  const LM = 'main,nav,header,footer,aside,[role=main],[role=navigation],[role=banner],[role=contentinfo],[role=search],[role=region][aria-label],[role=application]';
  const landmarks = [...new Set(deepAll(LM).filter(vis).map(e =>
    (e.getAttribute('role')||e.tagName.toLowerCase()) +
    (e.getAttribute('aria-label') ? `"${e.getAttribute('aria-label').slice(0,24)}"` : '')))];
  const headings = deepAll('h1,h2,h3,h4').filter(vis).map(h =>
    h.tagName + ' ' + (h.getAttribute('aria-label')||h.textContent||'').replace(/\s+/g,' ').trim().slice(0,40));
  const grids = deepAll('[role=grid],[role=table],[role=treegrid]').filter(vis);
  const gridsNamed = grids.filter(e => e.getAttribute('aria-label')||e.getAttribute('aria-labelledby'));
  let unnamedCtl = 0;
  for (const e of deepAll('button,[role=button],a[href],sp-button,sp-action-button')) {
    if (!vis(e)) continue;
    const al = e.getAttribute('aria-label'); if (al && al.trim()) continue;
    let t=''; const c=n=>{if(n.nodeType===3)t+=n.textContent;
      else if(n.nodeType===1){if(n.getAttribute&&n.getAttribute('aria-hidden')==='true')return;
        if(n.shadowRoot)[...n.shadowRoot.childNodes].forEach(c);[...n.childNodes].forEach(c);}};c(e);
    if (!t.replace(/\s+/g,'').length) unnamedCtl++;
  }
  const custom = {};
  let shadow = 0;
  const walk = (root) => { for (const e of root.querySelectorAll('*')) {
    const t = e.tagName.toLowerCase();
    if (t.includes('-')) custom[t] = (custom[t]||0)+1;
    if (e.shadowRoot) { shadow++; walk(e.shadowRoot); } } };
  walk(document);
  const topCustom = Object.entries(custom).sort((a,b)=>b[1]-a[1]).slice(0,8)
    .map(([k,v])=>`${k}(${v})`);
  return {
    title: document.title,
    lang: document.documentElement.lang || null,
    landmarks, hasMain: landmarks.some(l => l.startsWith('main')||l.startsWith('[role=main]')||l==='main'),
    headings: headings.slice(0, 14), headingCount: headings.length,
    grids: grids.length, gridsNamed: gridsNamed.length,
    unnamedControls: unnamedCtl,
    canvases: deepAll('canvas').filter(vis).length,
    iframes: deepAll('iframe').filter(f=>f.clientWidth>0).length,
    shadowRoots: shadow, topCustomElements: topCustom,
  };
})()"""


def refuse(url, allow_documents):
    # Patterns apply to the path+query only — hosts legitimately contain
    # words like "new" (learned on new.express.adobe.com).
    parsed = urllib.parse.urlparse(url)
    low = (parsed.path + ("?" + parsed.query if parsed.query else "")).lower()
    for p in REFUSE_DEFAULT:
        if p in low:
            return f"path matches refused pattern '{p}'"
    if "/id/" in low and not allow_documents:
        return "document URL (pass --allow-documents to fingerprint documents)"
    return None


def main():
    ap = argparse.ArgumentParser(
        description="enclosure mapping over CDP — harvest links, fingerprint views")
    ap.add_argument("mode", choices=["harvest", "map"])
    ap.add_argument("urls", nargs="+", help="explicit URL allowlist")
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--settle", type=int, default=10,
                    help="seconds to wait after navigation (SPA render)")
    ap.add_argument("--allow-documents", action="store_true")
    ap.add_argument("--out", help="write markdown to this file (map mode)")
    args = ap.parse_args()

    cdp = CDP(args.port)
    stamp = datetime.date.today().isoformat()
    lines = [f"# View map — {stamp} (crawl_map.py, recon only — "
             f"work into 03 per assisted-exploration.md)", ""]

    for url in args.urls:
        why = refuse(url, args.allow_documents)
        if why:
            print(f"REFUSED  {url}  ({why})")
            lines += [f"## {url}", "", f"REFUSED — {why}", ""]
            continue
        landed = cdp.goto(url, settle=args.settle)
        bounced = urllib.parse.urlparse(landed).path.rstrip("/") != \
            urllib.parse.urlparse(url).path.rstrip("/")
        if bounced:
            print(f"BOUNCED  {url}\n     ->  {landed[:90]}")
            lines += [f"## {url}", "",
                      f"**BOUNCED** to `{landed[:120]}` — the URL is not a "
                      "stable locator for this view; record the action path "
                      "instead, and investigate what the navigation did.", ""]
            continue

        if args.mode == "harvest":
            links = cdp.ev(HARVEST_JS) or []
            print(f"\n== {url}  ({len(links)} same-origin links)")
            for l in links:
                print(f"   {l['link']:<64} {l['name']}")
            lines += [f"## {url} — {len(links)} candidate links", ""]
            lines += [f"- `{l['link']}` — {l['name']}" for l in links] + [""]
        else:
            fp = cdp.ev(FINGERPRINT_JS) or {}
            print(f"\n== {landed[:80]}")
            print(f"   title: {fp.get('title')!r}   lang: {fp.get('lang')}")
            print(f"   landmarks ({len(fp.get('landmarks', []))}, "
                  f"main={'YES' if fp.get('hasMain') else 'NO'}): "
                  f"{', '.join(fp.get('landmarks', []))[:110]}")
            print(f"   headings: {fp.get('headingCount')}   "
                  f"grids: {fp.get('grids')} ({fp.get('gridsNamed')} named)   "
                  f"unnamed controls: {fp.get('unnamedControls')}   "
                  f"canvases: {fp.get('canvases')}")
            print(f"   shadow roots: {fp.get('shadowRoots')}   "
                  f"components: {', '.join(fp.get('topCustomElements', []))[:100]}")
            lines += [f"## {url}", "",
                      f"| field | value |", "|---|---|",
                      f"| landed | `{landed[:110]}` |",
                      f"| title | {fp.get('title')} |",
                      f"| lang | {fp.get('lang')} |",
                      f"| landmarks | {', '.join(fp.get('landmarks', [])) or '(none)'} |",
                      f"| `main` present | {'yes' if fp.get('hasMain') else '**NO**'} |",
                      f"| headings | {fp.get('headingCount')}: "
                      f"{'; '.join(fp.get('headings', []))[:220]} |",
                      f"| grids | {fp.get('grids')} ({fp.get('gridsNamed')} named, "
                      f"**{(fp.get('grids') or 0) - (fp.get('gridsNamed') or 0)} unnamed**) |",
                      f"| unnamed controls | {fp.get('unnamedControls')} |",
                      f"| canvases | {fp.get('canvases')} |",
                      f"| iframes | {fp.get('iframes')} |",
                      f"| shadow roots | {fp.get('shadowRoots')} |",
                      f"| components | {', '.join(fp.get('topCustomElements', []))} |",
                      ""]

    if args.out:
        from pathlib import Path
        Path(args.out).write_text("\n".join(lines), encoding="utf-8")
        print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
