"""Rasterise the SVG wordmark to PNG so the Word export can carry it.

python-docx cannot embed SVG, and nothing in this repo's dependency set can
rasterise one. But a headless Chrome is already part of the toolchain and is
the best SVG renderer on the machine, so it does the job: load the SVG at
four times its intended height on a transparent background and screenshot it.

Writes next to the SVG, which is where brand_header() looks for it.
"""
import base64
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path("scripts").resolve()))
from crawl_map import CDP  # noqa: E402

SVG = pathlib.Path("scripts/sfbrn-logo.svg")
OUT = SVG.with_suffix(".png")
HEIGHT = 42 * 4          # 4x the rendered height, so it stays sharp in print
ASPECT = 151.99 / 31.63

svg = SVG.read_text(encoding="utf-8")
w, h = round(HEIGHT * ASPECT), HEIGHT
page = (
    "<!doctype html><meta charset='utf-8'>"
    "<style>html,body{margin:0;padding:0;background:transparent}"
    f"svg{{display:block;width:{w}px;height:{h}px}}</style>" + svg
)
url = "data:text/html;base64," + base64.b64encode(page.encode("utf-8")).decode("ascii")

c = CDP(9223)
c.cmd("Page.navigate", {"url": url})
c.cmd("Runtime.evaluate", {"expression": "1", "awaitPromise": False})
c.cmd("Emulation.setDeviceMetricsOverride",
      {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": False})
c.cmd("Emulation.setDefaultBackgroundColorOverride",
      {"color": {"r": 0, "g": 0, "b": 0, "a": 0}})
shot = c.cmd("Page.captureScreenshot",
             {"format": "png", "captureBeyondViewport": True,
              "clip": {"x": 0, "y": 0, "width": w, "height": h, "scale": 1}})
OUT.write_bytes(base64.b64decode(shot["data"]))
print(f"{OUT} — {OUT.stat().st_size:,} bytes, {w}x{h}")
c.cmd("Emulation.clearDeviceMetricsOverride")
