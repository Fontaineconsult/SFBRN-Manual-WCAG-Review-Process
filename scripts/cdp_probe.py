#!/usr/bin/env python3
"""cdp_probe.py — exploration probe over Chrome DevTools Protocol (WCAG-EM step 2).

Companion to crawl_map.py for sessions without the Claude-in-Chrome extension.
Attaches to the first page tab of the debug-profile Chrome (port 9222) and, for
the current page (or a URL it navigates to first), prints:

  * frames (surfaces iframes that host whole sub-forms),
  * visible text (first N chars),
  * visible interactive elements (tag | type | role | name | id | href/onclick | tabindex),
  * an accessibility-tree summary (role histogram, unnamed controls) via
    Accessibility.getFullAXTree — the AT-facing view, which outranks DOM checks,
  * optionally a role/name dump of the AX tree (--ax), a screenshot (--shot),
    the result of an arbitrary JS expression (--js, async allowed), and a
    real key chord dispatched through Input.dispatchKeyEvent (--key), which
    goes through the app's own key handling unlike element.click()/focus().

Recon only: nothing this prints is a finding until a logged run verifies it
(ontology/assisted-exploration.md). Screenshots are disposable working context —
write them to the scratchpad, never into evidence/runs/.

Examples
  python scripts/cdp_probe.py                                   # current tab
  python scripts/cdp_probe.py https://app/x.aspx --settle 4 --ax --shot out.png
  python scripts/cdp_probe.py --js "[...document.querySelectorAll('select')].map(s=>[...s.options].map(o=>o.text+' => '+o.value))"
  python scripts/cdp_probe.py --focus "input[type=radio]" --key 5 --ctrl --shift
"""
import argparse, base64, collections, json, pathlib, sys, time, urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import crawl_map  # noqa: E402  (CDP client + fingerprint JS live there)

# Windows consoles default to cp1252; page text routinely carries ⋮, ≥, math.
for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

CTL_JS = r"""(() => {
  const vis = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return r.width>0 && r.height>0 && cs.visibility!=='hidden' && cs.display!=='none'; };
  const out = [];
  for (const e of document.querySelectorAll('a,button,input,select,textarea,[role],[onclick],[tabindex]')) {
    if (!vis(e)) continue;
    const name = (e.getAttribute('aria-label') || e.getAttribute('title') || e.value || e.textContent || '').replace(/\s+/g,' ').trim().slice(0,50);
    out.push([e.tagName.toLowerCase(), e.getAttribute('type')||'', e.getAttribute('role')||'', name, e.id||'',
              (e.getAttribute('href')||e.getAttribute('onclick')||'').slice(0,60), e.getAttribute('tabindex')||'']);
  }
  return out;
})()"""

NAMED_ROLES = {"button", "link", "textbox", "combobox", "checkbox", "radio", "tab", "menuitem",
               "switch", "slider", "spinbutton", "searchbox", "listbox", "option"}
NOISE_ROLES = {"generic", "none", "InlineTextBox", "StaticText", "LineBreak"}
KEY_CODES = {"Enter": (13, "Enter"), "Tab": (9, "Tab"), "Escape": (27, "Escape"), " ": (32, "Space"),
             "ArrowDown": (40, "ArrowDown"), "ArrowUp": (38, "ArrowUp"),
             "ArrowLeft": (37, "ArrowLeft"), "ArrowRight": (39, "ArrowRight")}


def frames(node, depth=0):
    f = node["frame"]
    print("  " * depth + f"frame: {f.get('url')}  name={f.get('name', '')}")
    for ch in node.get("childFrames", []):
        frames(ch, depth + 1)


def send_key(c, key, ctrl=False, shift=False, alt=False):
    mods = (1 if alt else 0) | (2 if ctrl else 0) | (8 if shift else 0)   # CDP: Alt=1 Ctrl=2 Meta=4 Shift=8
    if key in KEY_CODES:
        vk, code = KEY_CODES[key]
    elif len(key) == 1:
        vk = ord(key.upper()); code = ("Digit" if key.isdigit() else "Key") + key.upper()
    else:
        vk, code = 0, key
    base = {"modifiers": mods, "key": key, "code": code, "windowsVirtualKeyCode": vk, "nativeVirtualKeyCode": vk}
    c.cmd("Input.dispatchKeyEvent", dict(base, type="rawKeyDown"))
    if len(key) == 1 and not ctrl and not alt:
        c.cmd("Input.dispatchKeyEvent", dict(base, type="char", text=key))
    c.cmd("Input.dispatchKeyEvent", dict(base, type="keyUp"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?", help="navigate here first (omit to probe the current tab)")
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--tab", help="attach to the page tab whose URL/title contains this (default: the URL's host if a URL is given, else the first http(s) tab — never a blank tab)")
    ap.add_argument("--settle", type=float, default=3, help="seconds to wait after navigation / key")
    ap.add_argument("--text", type=int, default=2500, help="chars of visible text to print (0 = none)")
    ap.add_argument("--controls", type=int, default=150, help="max controls to list (0 = none)")
    ap.add_argument("--ax", metavar="FILE", nargs="?", const="-", help="dump AX role/name lines (to FILE, or stdout with no value)")
    ap.add_argument("--shot", metavar="PNG", help="save a screenshot here")
    ap.add_argument("--js", help="JS expression to evaluate after everything else (async IIFE ok)")
    ap.add_argument("--focus", metavar="SELECTOR", help="focus this element before --key")
    ap.add_argument("--key", help="key to dispatch (e.g. 5, Enter, Tab, ArrowDown)")
    ap.add_argument("--ctrl", action="store_true"); ap.add_argument("--shift", action="store_true"); ap.add_argument("--alt", action="store_true")
    a = ap.parse_args()

    needle = a.tab
    if not needle and a.url:
        from urllib.parse import urlsplit
        needle = urlsplit(a.url).netloc
    c = crawl_map.CDP(a.port, tab=needle) if needle else crawl_map.CDP(a.port)
    if a.url and needle and needle.lower() not in c.tab.get("url", "").lower():
        sys.exit(f"refusing to navigate: no open tab on {needle}; open the product in the debug window first (a second tab can invalidate the session)")
    print("tab:", c.tab.get("url", "")[:100])
    if a.url:
        c.cmd("Page.navigate", {"url": a.url}); time.sleep(a.settle)
    if a.focus:
        print("focus:", c.ev(f"(() => {{ const e=document.querySelector({json.dumps(a.focus)}); if(!e) return 'not found'; e.focus(); return document.activeElement.outerHTML.slice(0,120); }})()"))
    if a.key:
        send_key(c, a.key, a.ctrl, a.shift, a.alt); time.sleep(a.settle)
        print("active element after key:", c.ev("document.activeElement ? document.activeElement.tagName+'#'+document.activeElement.id : 'none'"))

    print("URL:", c.ev("location.href"))
    print("TITLE:", c.ev("document.title"))
    print("FRAMES:"); frames(c.cmd("Page.getFrameTree")["frameTree"])
    if a.shot:
        p = pathlib.Path(a.shot); p.write_bytes(base64.b64decode(c.cmd("Page.captureScreenshot", {"format": "png"})["data"]))
        print("SCREENSHOT:", p)
    if a.text:
        txt = c.ev("document.body ? document.body.innerText : ''") or ""
        print(f"TEXT (first {a.text} chars):"); print(txt[:a.text])
    if a.controls:
        ctls = c.ev(CTL_JS) or []
        print(f"CONTROLS ({len(ctls)}): tag | type | role | name | id | href-or-onclick | tabindex")
        for r in ctls[:a.controls]:
            print("  " + " | ".join(str(x) for x in r))

    c.cmd("Accessibility.enable")
    nodes = c.cmd("Accessibility.getFullAXTree").get("nodes", [])
    roles, unnamed, lines = collections.Counter(), collections.Counter(), []
    for n in nodes:
        if n.get("ignored"):
            continue
        role = n.get("role", {}).get("value", ""); name = n.get("name", {}).get("value", "")
        roles[role] += 1
        if role in NAMED_ROLES and not name:
            unnamed[role] += 1
        if role not in NOISE_ROLES:
            lines.append(f"{role}: {name[:80]}")
    print("AX nodes (unignored):", sum(roles.values()))
    print("AX roles:", dict(roles.most_common(30)))
    print("AX unnamed controls:", dict(unnamed) or "none")
    if a.ax:
        if a.ax == "-":
            print("AX DUMP:"); print("\n".join(lines))
        else:
            pathlib.Path(a.ax).write_text("\n".join(lines), encoding="utf-8"); print("AX dump:", a.ax, f"({len(lines)} lines)")
    if a.js:
        print("JS:", json.dumps(c.ev(a.js), indent=1, ensure_ascii=False)[:6000])


if __name__ == "__main__":
    main()
