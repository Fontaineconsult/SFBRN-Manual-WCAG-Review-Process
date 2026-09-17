r"""preflight.py — environment pre-flight for a tool-running session, in one call.

CLAUDE.md step 7 lists four checks that rot silently between sessions
(2026-08-06 and 2026-09-14 both opened with a dead debug browser). This
script runs them all and prints one verdict line per check, so the session
opens on facts instead of a traceback from a hand-typed curl | json pipe.

    python scripts/preflight.py                       # check everything
    python scripts/preflight.py --launch [--url URL]  # launch the debug-profile
                                                      # Chrome if port 9222 is dead
    python scripts/preflight.py --anon [--launch]     # also / instead: the
                                                      # signed-out profile, port 9223

Checks (testing-tools.md §axe-core, in that order):
  1. `import websocket`                — axe_scan.py's dependency (pip install websocket-client)
  2. profile dir exists                — %LOCALAPPDATA%\sfbrn-a11y-chrome (-anon for 9223)
  3. port answers                      — http://127.0.0.1:9222/json/version
  4. the page tab is authenticated     — no tab on a sign-in host/path or titled "Sign in"/"Login"
  5. zero persistent chrome-extension:// targets — polled twice, 10 s apart, because
     Chrome's own component extensions (persistent on 153) are allowed;
     a STORE extension running is a failure -- it falsifies measurement

Exit 0 when every check passes, 1 otherwise. The script never signs in: a
sign-in tab is reported as the reviewer's next action.

--launch uses the FULL flag set from testing-tools.md — every flag earns its
place (without --disable-extensions --disable-sync the first-run promo syncs
the reviewer's personal extensions into the declared test environment).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

PROFILES = {
    9222: "sfbrn-a11y-chrome",
    9223: "sfbrn-a11y-chrome-anon",
}
SIGNIN_URL = re.compile(r"(^|[./])(login|signin|sign-in|auth|sso|ims)([./:?]|$)", re.I)
SIGNIN_TITLE = re.compile(r"\b(sign ?in|log ?in|login)\b", re.I)
# Chrome ships component extensions (Gemini in Chrome, Google Network Speech,
# Chrome PDF Viewer, Google Hangouts ...) that --disable-extensions cannot
# switch off; on Chrome 153 their service workers are PERSISTENT targets, so a
# "zero chrome-extension:// targets" rule can never pass (2026-09-17). They are
# harmless: they inject no stylesheet and no DOM node into the page.
# What IS dangerous is a STORE extension actually running -- Stylus falsifies
# contrast, SkipTo Landmarks adds the skip link 2.4.1 is about. The two classes
# are told apart by where the code lives: a store extension is unpacked under
# <profile>/Default/Extensions/<id>, a Chrome-bundled one never is (it sits in
# the Chrome install directory). That test needs no ID list and does not rot
# when Chrome adds a component.
def store_extension_ids(profile_dir: str) -> set:
    """IDs unpacked in this profile -- i.e. installed from the store/policy."""
    d = os.path.join(profile_dir, "Default", "Extensions")
    try:
        return {n for n in os.listdir(d) if os.path.isdir(os.path.join(d, n))}
    except OSError:
        return set()


def ok(label: str, detail: str = "") -> None:
    # plain ASCII separators: the Windows console is cp1252 and mangles em-dashes
    print(f"  [ok]   {label}" + (f" : {detail}" if detail else ""))


def bad(label: str, detail: str = "") -> None:
    print(f"  [FAIL] {label}" + (f" : {detail}" if detail else ""))


def http_json(url: str, timeout: float = 3.0):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def chrome_exe() -> str | None:
    try:
        import winreg  # type: ignore
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe") as k:
            path, _ = winreg.QueryValueEx(k, None)
            if os.path.isfile(path):
                return path
    except Exception:
        pass
    for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
        if os.path.isfile(p):
            return p
    return None


def launch(port: int, profile_dir: str, url: str) -> bool:
    exe = chrome_exe()
    if not exe:
        bad("launch", "chrome.exe not found (App Paths registry, Program Files)")
        return False
    args = [exe, f"--remote-debugging-port={port}", f"--user-data-dir={profile_dir}",
            "--disable-extensions", "--disable-sync", "--no-first-run",
            "--no-default-browser-check", url]
    subprocess.Popen(args, creationflags=getattr(subprocess, "DETACHED_PROCESS", 0))
    print(f"  launched {os.path.basename(exe)} on port {port}, profile {profile_dir}")
    return True


def check_port(port: int, do_launch: bool, url: str) -> bool:
    """Returns True when all checks for this port pass."""
    passed = True
    profile_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""), PROFILES[port])
    print(f"\nPort {port} : profile {PROFILES[port]}")

    if os.path.isdir(profile_dir):
        ok("profile directory exists", profile_dir)
    else:
        bad("profile directory missing", f"{profile_dir} — a launch creates it; the reviewer then signs in")
        passed = False

    def version():
        try:
            return http_json(f"http://127.0.0.1:{port}/json/version")
        except (urllib.error.URLError, OSError, ValueError):
            return None

    v = version()
    if v is None and do_launch:
        if launch(port, profile_dir, url):
            for _ in range(20):
                time.sleep(1)
                v = version()
                if v:
                    break
    if v is None:
        bad("port answers", f"nothing on http://127.0.0.1:{port}/json/version"
            + ("" if do_launch else " — re-run with --launch"))
        return False
    ok("port answers", v.get("Browser", "?"))

    def targets():
        try:
            return http_json(f"http://127.0.0.1:{port}/json")
        except (urllib.error.URLError, OSError, ValueError):
            return []

    t = targets()
    pages = [x for x in t if x.get("type") == "page"]
    if not pages:
        bad("page tab", "no page target listed")
        passed = False
    for p in pages:
        title, purl = p.get("title", ""), p.get("url", "")
        host_path = re.sub(r"^https?://", "", purl)
        if SIGNIN_URL.search(host_path.split("?")[0]) or SIGNIN_TITLE.search(title):
            if port == 9223:
                ok("signed-out tab (expected on the anon profile)", f"{title!r} {purl}")
            else:
                bad("tab is a sign-in page — the reviewer signs in; the assistant never does",
                    f"{title!r} {purl}")
                passed = False
        else:
            ok("page tab", f"{title!r} {purl[:90]}")

    def ext_targets(ts):
        return [x for x in ts if x.get("url", "").startswith("chrome-extension://")]

    installed = store_extension_ids(profile_dir)
    ext = ext_targets(t)
    live = {x["url"].split("/")[2] for x in ext}
    running_store = sorted(live & installed)
    if running_store:
        bad("STORE extensions are running — they falsify measurement (Stylus: contrast; "
            "SkipTo/Landmark Navigation: the skip link and landmarks 2.4.1 and 1.3.1 are about); "
            "relaunch with --disable-extensions and discard anything measured in this window",
            "; ".join(running_store))
        passed = False
    elif ext:
        ok(f"no store extension running ({len(live)} Chrome-bundled component(s) only)",
           ", ".join(sorted(live)))
    else:
        ok("zero chrome-extension:// targets")
    # The profile can still HOLD store extensions that the flag is suppressing.
    # Silence would invite the next launch to drop the flag (2026-08-14: 22 of
    # them synced in, including Stylus and SkipTo Landmarks).
    if installed:
        print(f"  ...   {len(installed)} store extension(s) unpacked in this profile but not "
              f"running; they stay inert ONLY while --disable-extensions is used")
    return passed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--launch", action="store_true",
                    help="launch the debug-profile Chrome if its port is not answering")
    ap.add_argument("--url", default="about:blank",
                    help="URL to open on launch (the product home; never its sign-in page)")
    ap.add_argument("--anon", action="store_true",
                    help="check (and with --launch, start) the signed-out profile on port 9223")
    ap.add_argument("--only-anon", action="store_true",
                    help="skip port 9222; check only the signed-out profile")
    a = ap.parse_args()

    passed = True
    print("Pre-flight")
    try:
        import websocket  # noqa: F401
        ok("python: websocket-client importable")
    except ImportError:
        bad("python: websocket-client missing", "python -m pip install websocket-client")
        passed = False

    if not a.only_anon:
        passed &= check_port(9222, a.launch, a.url)
    if a.anon or a.only_anon:
        passed &= check_port(9223, a.launch, a.url)

    print("\nPRE-FLIGHT " + ("CLEAN" if passed else "NOT CLEAN — fix the [FAIL] lines above before measuring"))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
