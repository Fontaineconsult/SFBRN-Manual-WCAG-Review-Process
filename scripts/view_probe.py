#!/usr/bin/env python3
r"""view_probe.py — answer the instrument-decidable checks for a sampled view.

Purpose: take work off the reviewer. Many modality checks are decided by a
structural fact about the view ("there is no video here", "no script uses
speech input", "every target is ≥ 24 px") that an instrument establishes
more reliably than a person can. This script gathers those facts over CDP
from the debug-profile Chrome, writes the resulting outcomes into the
view's runs (pass / n/a / a *measured* fail with the evidence), and names
what is left for the reviewer. It never answers a check that needs human
judgment, and a measured fail becomes a finding only after the reviewer
confirms it (CLAUDE.md: findings are human-confirmed).

Which checks it may answer, and the rule for each, is the table
"Assistant-answerable checks" in ontology/modality-checks.md — this script
implements that table and nothing more. Facts it cannot decide are still
recorded in the run (as measured observations) so the reviewer starts from
evidence, not from a blank row.

Usage
    python scripts/view_probe.py <review> --view S4 --url https://...  [--settle 6]
    python scripts/view_probe.py <review> --view S3 --url "UI: Class Management → …"
                                   # 'UI:' locator = probe the tab as it is now
    python scripts/view_probe.py <review> --view S1 --url URL --dry-run
                                   # print facts + would-be answers, write nothing

Writes: outcomes + observations into the latest run for each (view ×
modality) it can speak to — creating the run with `review.py log-test
--tool probe` when none exists — and `<RID>-probe.json` (the facts) beside
it. Never overwrites an outcome a person already entered.

Preconditions: the debug-profile Chrome is up and signed in (testing-tools.md
§axe-core pre-flight); the product is open in ONE tab — the probe navigates
that tab and only that tab.
"""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import crawl_map  # noqa: E402  (CDP client)
import review as rv  # noqa: E402  (review-file helpers)

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

# --------------------------------------------------------------------------
# Facts (JS, evaluated in the top document; walks same-origin frames)
# --------------------------------------------------------------------------
FACTS_JS = r"""(async () => {
  const PERSONAL = /(^|[^a-z])(e-?mail|phone|tel(ephone)?|mobile|street|address|zip|postal|password|passwd|user ?name|login|birth|bday|card ?number|cvv|cvc|expir|first ?name|last ?name|full ?name|your ?name|given ?name|family ?name|surname|ssn|social security)/i;
  const NAMEISH = /(^|[^a-z])name([^a-z]|$)/i;
  const MEDIA_HOST = /youtube|youtu\.be|vimeo|wistia|kaltura|brightcove|panopto|mediaspace|vidyard|loom\.com|dailymotion|soundcloud|spotify|twitch/i;
  const MEDIA_EXT = /\.(mp4|m4v|webm|ogv|mov|mp3|m4a|wav|ogg|aac|flac)(\?|#|$)/i;

  const vis = e => { try { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; } catch (x) { return false; } };
  const txt = e => (e.getAttribute && (e.getAttribute('aria-label') || e.getAttribute('title')) || e.textContent || e.value || '').replace(/\s+/g, ' ').trim();
  const desc = e => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).slice(0,2).join('.') : '');

  const docs = [];
  const walk = (win, depth) => {
    let d; try { d = win.document; if (!d) return; } catch (x) { docs.push({href: '(cross-origin frame)', doc: null}); return; }
    docs.push({href: win.location.href, doc: d});
    if (depth > 3) return;
    for (const f of Array.from(win.frames)) walk(f, depth + 1);
  };
  walk(window, 0);

  const F = {
    href: location.href, title: document.title,
    lang: document.documentElement.getAttribute('lang'), xmlLang: document.documentElement.getAttribute('xml:lang'),
    docs: docs.map(x => x.href),
    metaRefresh: [], media: {video: 0, audio: 0, tracks: 0, autoplay: 0, embeds: [], mediaIframes: [], mediaLinks: []},
    scripts: {inline: 0, external: 0, unreadable: [], hits: {speech: 0, motion: 0, orientationLock: 0, audioApi: 0, animationFrame: 0, timers: 0}},
    micControls: [], inputs: [], passwordFields: 0, timerText: [],
    animation: {animated: [], gifs: [], marqueeBlink: 0, canvas: 0, svgAnimate: 0},
    orientationRules: [], targets: {total: 0, small: [], failing: []},
  };

  const scriptTexts = [];
  for (const {doc} of docs) {
    if (!doc) continue;
    for (const m of doc.querySelectorAll('meta[http-equiv="refresh" i]')) F.metaRefresh.push(m.getAttribute('content'));
    F.media.video += doc.querySelectorAll('video').length;
    F.media.audio += doc.querySelectorAll('audio').length;
    F.media.tracks += doc.querySelectorAll('track').length;
    F.media.autoplay += doc.querySelectorAll('video[autoplay],audio[autoplay]').length;
    for (const e of doc.querySelectorAll('object,embed')) F.media.embeds.push((e.getAttribute('data') || e.getAttribute('src') || e.getAttribute('type') || '?').slice(0, 120));
    for (const e of doc.querySelectorAll('iframe')) { const s = e.getAttribute('src') || ''; if (MEDIA_HOST.test(s) || MEDIA_EXT.test(s)) F.media.mediaIframes.push(s.slice(0, 120)); }
    for (const a of doc.querySelectorAll('a[href]')) { const h = a.getAttribute('href') || ''; if (MEDIA_EXT.test(h) || MEDIA_HOST.test(h)) F.media.mediaLinks.push(h.slice(0, 120)); }
    for (const e of doc.querySelectorAll('button,[role=button],a,input[type=button],input[type=image]')) {
      const t = txt(e); if (vis(e) && /microphone|\bmic\b|voice|speak now|dictat|speech/i.test(t)) F.micControls.push(t.slice(0, 60));
    }
    for (const e of doc.querySelectorAll('input,select,textarea')) {
      const type = (e.getAttribute('type') || (e.tagName === 'INPUT' ? 'text' : e.tagName.toLowerCase())).toLowerCase();
      if (['hidden', 'submit', 'button', 'reset', 'image'].includes(type)) continue;
      if (!vis(e)) continue;
      if (type === 'password') F.passwordFields++;
      let label = '';
      if (e.id) { const l = doc.querySelector('label[for="' + CSS.escape(e.id) + '"]'); if (l) label = txt(l); }
      if (!label && e.closest('label')) label = txt(e.closest('label'));
      const aria = e.getAttribute('aria-label') || '';
      const key = [e.getAttribute('name') || '', e.id || '', label, aria, e.getAttribute('placeholder') || ''].join(' | ');
      const personal = PERSONAL.test(key) ? 'personal' : NAMEISH.test(key) ? 'name-candidate' : '';
      if (personal || type === 'password' || type === 'email' || type === 'tel')
        F.inputs.push({type, name: e.getAttribute('name') || '', id: e.id || '', label: (label || aria || e.getAttribute('placeholder') || '').slice(0, 60),
                       autocomplete: e.getAttribute('autocomplete'), personal: personal || 'personal'});
    }
    const body = doc.body ? doc.body.innerText || '' : '';
    for (const m of body.matchAll(/[^.\n]{0,60}(time remaining|remaining time|time left|minutes? left|session (will )?(expire|time ?out)|will be logged out)[^.\n]{0,60}/gi)) { F.timerText.push(m[0].trim().slice(0, 140)); if (F.timerText.length > 5) break; }
    for (const e of doc.querySelectorAll('*')) {
      if (!vis(e)) continue;
      let cs; try { cs = getComputedStyle(e); } catch (x) { continue; }
      if (cs.animationName && cs.animationName !== 'none' && parseFloat(cs.animationDuration) > 0 && cs.animationIterationCount !== '1') F.animation.animated.push(desc(e) + ' [' + cs.animationName + ' ' + cs.animationDuration + ' ' + cs.animationIterationCount + ']');
      if (F.animation.animated.length > 20) break;
    }
    for (const img of doc.querySelectorAll('img')) { const s = (img.currentSrc || img.src || ''); if (/\.(gif|apng)(\?|#|$)/i.test(s) && vis(img)) F.animation.gifs.push(s.slice(-80)); }
    F.animation.marqueeBlink += doc.querySelectorAll('marquee,blink').length;
    F.animation.canvas += Array.from(doc.querySelectorAll('canvas')).filter(vis).length;
    F.animation.svgAnimate += doc.querySelectorAll('animate,animateTransform,animateMotion').length;
    for (const ss of Array.from(doc.styleSheets)) {
      let rules; try { rules = ss.cssRules; } catch (x) { continue; }
      for (const r of Array.from(rules || [])) if (r.media && /orientation/i.test(r.media.mediaText)) F.orientationRules.push(r.media.mediaText + ' {' + Array.from(r.cssRules || []).slice(0, 3).map(x => x.cssText.slice(0, 80)).join(' ') + '}');
    }
    for (const s of doc.querySelectorAll('script')) {
      if (s.src) { F.scripts.external++; try { const r = await fetch(s.src, {credentials: 'include'}); if (r.ok) scriptTexts.push(await r.text()); else F.scripts.unreadable.push(s.src.slice(-80)); } catch (x) { F.scripts.unreadable.push(s.src.slice(-80)); } }
      else { F.scripts.inline++; scriptTexts.push(s.textContent || ''); }
    }
    // targets (document coordinates of the top doc only for frames = approximated by their own coords)
    const sel = 'a[href],button,input:not([type=hidden]),select,textarea,[role=button],[role=link],[role=checkbox],[role=radio],[role=tab],[role=menuitem],[role=option],[role=switch],[onclick],[tabindex="0"]';
    // [onclick] on table structure / layout containers is event delegation, not a target
    const CONTAINER = /^(table|tbody|thead|tr|td|th|ul|ol|form|body|html)$/i;
    const els = Array.from(doc.querySelectorAll(sel)).filter(vis)
      .filter(e => !(CONTAINER.test(e.tagName) && !e.hasAttribute('role') && !e.hasAttribute('tabindex')));
    const rects = els.map(e => e.getBoundingClientRect());
    F.targets.total += els.length;
    els.forEach((e, i) => {
      const r = rects[i];
      if (r.width >= 24 && r.height >= 24) return;
      const type = (e.getAttribute('type') || '').toLowerCase();
      if (e.tagName === 'INPUT' && (type === 'checkbox' || type === 'radio')) return;  // user-agent sized (exception)
      const inline = e.tagName === 'A' && getComputedStyle(e).display.startsWith('inline') && e.parentElement && (e.parentElement.textContent || '').trim().length > (e.textContent || '').trim().length + 15;
      if (inline) return;  // inline-in-text exception
      const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
      let clash = null;
      for (let j = 0; j < els.length; j++) { if (j === i) continue; const o = rects[j];
        if (els[j].contains(e) || e.contains(els[j])) continue;  // ancestors/descendants are not neighbours
        const ox = Math.max(o.left, Math.min(cx, o.right)), oy = Math.max(o.top, Math.min(cy, o.bottom));
        if (Math.hypot(cx - ox, cy - oy) < 12) { clash = desc(els[j]) + ' "' + txt(els[j]).slice(0, 30) + '"'; break; } }
      const item = {el: desc(e), name: txt(e).slice(0, 40), w: Math.round(r.width), h: Math.round(r.height), clash};
      F.targets.small.push(item);
      if (clash) F.targets.failing.push(item);
    });
  }
  const all = scriptTexts.join('\n');
  const H = F.scripts.hits;
  H.speech = (all.match(/SpeechRecognition|webkitSpeechRecognition|speechSynthesis|getUserMedia\s*\(/g) || []).length;
  H.motion = (all.match(/devicemotion|deviceorientation|DeviceMotionEvent|DeviceOrientationEvent/g) || []).length;
  H.orientationLock = (all.match(/orientation\.lock|lockOrientation/g) || []).length;
  H.audioApi = (all.match(/new Audio\s*\(|AudioContext|webkitAudioContext/g) || []).length;
  H.animationFrame = (all.match(/requestAnimationFrame/g) || []).length;
  H.timers = (all.match(/setTimeout\s*\([^,]+,\s*(\d{5,})/g) || []).length;
  F.targets.small = F.targets.small.slice(0, 40); F.targets.failing = F.targets.failing.slice(0, 25);
  F.inputs = F.inputs.slice(0, 40);
  return F;
})()"""

CLIP_JS = r"""(() => {
  const out = [];
  for (const e of document.querySelectorAll('body *')) {
    if (!(e.textContent || '').trim()) continue;
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const ox = cs.overflowX, oy = cs.overflowY;
    if (!(ox === 'hidden' || ox === 'clip' || oy === 'hidden' || oy === 'clip')) continue;
    if (e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1)
      out.push(e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + ' "' + (e.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40) + '"');
  }
  return out;
})()"""

OVERFLOW_JS = r"""(() => {
  const W = 320, out = [], se = document.scrollingElement || document.documentElement;
  let tableOnly = true;
  for (const e of document.querySelectorAll('body *')) {
    const r = e.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
    if (r.right > W + 2 && r.width > 40) {
      // only DATA tables are exempt from reflow; layout tables (no th/caption/role) are not
      const tbl = e.closest('table');
      const dataTable = tbl && (tbl.querySelector('th') || tbl.querySelector('caption') || /grid|table/.test(tbl.getAttribute('role') || ''));
      const inTable = !!dataTable || !!e.closest('pre,canvas,video,img,svg,iframe,[role=grid],[role=table]');
      if (!inTable) tableOnly = false;
      if (out.length < 12) out.push(e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + ' right=' + Math.round(r.right) + (inTable ? ' (in table/exempt)' : ''));
    }
  }
  return {scrollWidth: se.scrollWidth, clientWidth: se.clientWidth, overflowing: out, tableOnly};
})()"""

# NC2 — links inside running text that differ from their surroundings by colour only
LINK_CUES_JS = r"""(() => {
  // Resting state: does the link differ from its surrounding text by anything
  // but colour? If not, the accepted technique (WCAG G183) still passes when
  // the link is >= 3:1 against the surrounding text AND gains a non-colour cue
  // on hover and on focus. Hover cues are read from the same-origin
  // stylesheets (rules whose selector carries :hover and matches the link);
  // focus cues are measured for real by focusing the element.
  const out = {inText: 0, colorOnly: [], failing: [], unreadableSheets: 0};
  const vis = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const lum = c => { const m = c.match(/[\d.]+/g); if (!m) return null; const [r,g,b] = m.slice(0,3).map(Number).map(v => { v /= 255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); }); return 0.2126*r + 0.7152*g + 0.0722*b; };
  const ratio = (c1, c2) => { const a = lum(c1), b = lum(c2); if (a === null || b === null) return null; const [h,l] = a > b ? [a,b] : [b,a]; return Math.round((h+0.05)/(l+0.05)*100)/100; };
  const cueIn = (st, base) => /underline|overline|line-through/.test(st.textDecorationLine || st.textDecoration || '') || (st.borderBottomStyle && st.borderBottomStyle !== 'none') || (st.outlineStyle && st.outlineStyle !== 'none' && parseFloat(st.outlineWidth) > 0) || (st.backgroundColor && st.backgroundColor !== 'rgba(0, 0, 0, 0)' && st.backgroundColor !== base.backgroundColor) || (parseInt(st.fontWeight) >= parseInt(base.fontWeight) + 200);
  // hover rules from stylesheets
  const hoverRules = [];
  for (const sh of Array.from(document.styleSheets)) {
    let rules; try { rules = sh.cssRules; } catch (x) { out.unreadableSheets++; continue; }
    const walk = rs => { for (const r of Array.from(rs || [])) { if (r.cssRules && !r.selectorText) walk(r.cssRules); if (r.selectorText && /:hover/.test(r.selectorText)) hoverRules.push(r); } };
    walk(rules);
  }
  const hoverCue = a => { for (const r of hoverRules) { const sel = r.selectorText.split(',').map(s => s.trim()).filter(s => /:hover/.test(s)).map(s => s.replace(/:hover/g, ''));
      let hit = false; for (const s of sel) { try { if (s && a.matches(s)) { hit = true; break; } } catch (x) {} }
      if (!hit) continue; const st = r.style; if (/underline/.test(st.textDecoration || st.textDecorationLine || '') || (st.borderBottom && st.borderBottom !== 'none') || st.backgroundColor || parseInt(st.fontWeight) >= 600 || st.outline) return r.selectorText.slice(0, 60); }
    return null; };
  for (const a of document.querySelectorAll('a[href]')) {
    if (!vis(a)) continue;
    const p = a.parentElement; if (!p) continue;
    const own = (a.textContent || '').trim(); if (!own) continue;
    // "running text" = the parent has its OWN text nodes around the link (a
    // sentence), not merely other child elements (a breadcrumb or a list of
    // links is not running text, and its parent's colour is not "the
    // surrounding text" — learned 2026-09-14 when the S4 breadcrumb measured 1:1)
    const direct = Array.from(p.childNodes).filter(n => n.nodeType === 3).map(n => n.textContent).join('').replace(/\s+/g, ' ').trim();
    if (direct.length < 15) continue;                          // not in running text
    out.inText++;
    const ca = getComputedStyle(a), cp = getComputedStyle(p);
    const underlined = /underline|overline|line-through/.test(ca.textDecorationLine) || ca.borderBottomStyle !== 'none' || ca.backgroundColor !== cp.backgroundColor && ca.backgroundColor !== 'rgba(0, 0, 0, 0)';
    const bold = parseInt(ca.fontWeight) >= parseInt(cp.fontWeight) + 200 || ca.fontStyle !== cp.fontStyle || ca.fontFamily !== cp.fontFamily;
    if (underlined || bold) continue;
    const label = (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 50) + ' → ' + (a.getAttribute('href') || '').slice(0, 60);
    const contrast = ratio(ca.color, cp.color);
    const hover = hoverCue(a);
    let focus = null;
    try { const prev = document.activeElement; a.focus({preventScroll: true}); const cf = getComputedStyle(a); if (cueIn(cf, cp)) focus = 'focus: ' + (cf.textDecorationLine !== 'none' ? cf.textDecorationLine : cf.outlineStyle !== 'none' ? 'outline' : 'style change'); a.blur(); if (prev && prev.focus) prev.focus({preventScroll: true}); } catch (x) {}
    const rec = {label, contrast, hover, focus};
    out.colorOnly.push(rec);
    if (!(hover && focus && contrast !== null && contrast >= 3)) out.failing.push(rec);
  }
  out.colorOnly = out.colorOnly.slice(0, 20); out.failing = out.failing.slice(0, 20);
  return out;
})()"""

TEXT_SPACING_CSS = ("* { line-height: 1.5 !important; letter-spacing: 0.12em !important; "
                    "word-spacing: 0.16em !important; } p { margin-bottom: 2em !important; }")


# --------------------------------------------------------------------------
# Decision rules — one function per check; returns (outcome, note) or None
# (None = the probe cannot decide; the fact is still recorded)
# --------------------------------------------------------------------------
def media_present(F):
    m = F["media"]
    items = []
    if m["video"]: items.append(f"{m['video']} <video>")
    if m["audio"]: items.append(f"{m['audio']} <audio>")
    if m["embeds"]: items.append(f"{len(m['embeds'])} object/embed ({'; '.join(m['embeds'][:3])})")
    if m["mediaIframes"]: items.append(f"{len(m['mediaIframes'])} media iframe(s) ({'; '.join(m['mediaIframes'][:3])})")
    if m["mediaLinks"]: items.append(f"{len(m['mediaLinks'])} media link(s) ({'; '.join(m['mediaLinks'][:3])})")
    return items


def decide(F, extra):
    """Return {modality: {check: (outcome, note)}} for the decidable checks."""
    A = {m: {} for m in rv.REQUIRED_MODALITIES}
    media = media_present(F)
    audio_api = F["scripts"]["hits"]["audioApi"]
    scripts_note = (f"{F['scripts']['inline']} inline + {F['scripts']['external']} external scripts scanned"
                    + (f", {len(F['scripts']['unreadable'])} unreadable" if F["scripts"]["unreadable"] else ""))
    no_media = f"no video, audio, media embed/iframe or media link on the view as loaded ({', '.join(F['docs'][:3])}{'…' if len(F['docs']) > 3 else ''})"

    # ---- no-hearing: n/a by absence of media
    if not media:
        A["no-hearing"]["NH1"] = ("n/a", no_media)
        A["no-hearing"]["NH2"] = ("n/a", no_media)
        A["no-hearing"]["NH3"] = ("n/a", no_media)
        if not audio_api:
            A["no-hearing"]["NH4"] = ("n/a", no_media + f"; no Audio()/AudioContext use in scripts ({scripts_note})")
    # ---- no-vision NV11: same absence rule (video only)
    if not F["media"]["video"] and not F["media"]["mediaIframes"] and not F["media"]["embeds"]:
        A["no-vision"]["NV11"] = ("n/a", "no <video>, media iframe or embed on the view")

    # ---- no-speech
    if not F["scripts"]["hits"]["speech"] and not F["micControls"]:
        A["no-speech"]["NS1"] = ("n/a", f"no SpeechRecognition/getUserMedia/speechSynthesis use and no microphone/voice control ({scripts_note})")

    # ---- no-vision NV1 title, NV9 lang
    title = (F["title"] or "").strip()
    if title and not re.fullmatch(r"(untitled|document|page|home|index(\.\w+)?|.*\.aspx?)", title, re.I):
        A["no-vision"]["NV1"] = ("pass", f'document.title = "{title[:80]}" (non-empty, specific; the reviewer\'s NVDA+T confirms wording on the walk)')
    elif not title:
        A["no-vision"]["NV1"] = ("fail", "document.title is empty (measured)")
    lang = F["lang"] or F["xmlLang"]
    if lang and re.fullmatch(r"[A-Za-z]{2,3}(-[A-Za-z0-9]{2,8})*", lang):
        A["no-vision"]["NV9"] = ("pass", f'<html lang="{lang}"> present and well-formed (measured; pronunciation of passages is the reviewer\'s call if any foreign-language content exists)')
    elif not lang:
        A["no-vision"]["NV9"] = ("fail", "<html> has no lang attribute (measured — 3.1.1)")

    # ---- motor MO9 target size, MO10 motion
    t = F["targets"]
    if t["total"] and not t["failing"]:
        A["motor"]["MO9"] = ("pass", f"{t['total']} visible targets measured; {len(t['small'])} under 24×24 px, all spacing-exempt (no other target within a 24 px circle) or inline/user-agent-sized")
    elif t["failing"]:
        ex = "; ".join(f"{x['el']} \"{x['name']}\" {x['w']}×{x['h']} px next to {x['clash']}" for x in t["failing"][:6])
        A["motor"]["MO9"] = ("fail", f"{len(t['failing'])} target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): {ex}")
    if not F["scripts"]["hits"]["motion"]:
        A["motor"]["MO10"] = ("n/a", f"no devicemotion/deviceorientation use in scripts ({scripts_note})")

    # ---- low-vision LV1 reflow, LV3 text spacing, LV8 orientation
    rf = extra.get("reflow")
    if rf:
        if rf["scrollWidth"] <= 322:
            A["low-vision"]["LV1"] = ("pass", f"at 320 CSS px (≈400 % zoom of 1280) scrollingElement.scrollWidth = {rf['scrollWidth']}: no horizontal scrolling (measured)")
        elif rf["tableOnly"]:
            A["low-vision"]["LV1"] = ("pass", f"at 320 CSS px scrollWidth = {rf['scrollWidth']}, but every overflowing element is inside a data table / exempt content: {'; '.join(rf['overflowing'][:4])} (measured; exempt under 1.4.10)")
        else:
            A["low-vision"]["LV1"] = ("fail", f"at 320 CSS px scrollWidth = {rf['scrollWidth']} (two-dimensional scrolling); non-exempt overflow: {'; '.join(x for x in rf['overflowing'] if 'exempt' not in x)[:300]} (measured)")
    ts = extra.get("text_spacing")
    if ts is not None:
        new = ts["after"]
        if not new:
            A["low-vision"]["LV3"] = ("pass", f"text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; {ts['baseline']} container(s) were already clipped before the override)")
        else:
            A["low-vision"]["LV3"] = ("fail", f"text-spacing override applied: {len(new)} container(s) newly clip their text: {'; '.join(new[:5])} (measured)")
    if not F["orientationRules"] and not F["scripts"]["hits"]["orientationLock"]:
        A["low-vision"]["LV8"] = ("pass", f"no orientation media query and no screen.orientation.lock use ({scripts_note}) — content is not restricted to one orientation")

    # ---- cognition CO6 auth, CO9 autocomplete, CO12 flashing
    login_like = (re.search(r"\b(log ?in|sign ?in|login)\b", (F["title"] or ""), re.I)
                  or any(re.search(r"user ?name|login", (i["label"] or i["name"] or i["id"] or ""), re.I) for i in F["inputs"]))
    if not F["passwordFields"] and not login_like:
        A["cognition"]["CO6"] = ("n/a", "no password field and no sign-in form on the view — authentication happens elsewhere")
    personal = [i for i in F["inputs"] if i["personal"] == "personal"]
    cands = [i for i in F["inputs"] if i["personal"] == "name-candidate"]
    if not personal and not cands:
        A["cognition"]["CO9"] = ("n/a", "no field collects the user's own information (name/email/phone/address/… not present)")
    elif personal and not cands:
        missing = [i for i in personal if not i["autocomplete"]]
        if not missing:
            A["cognition"]["CO9"] = ("pass", f"{len(personal)} personal-data field(s) all carry autocomplete: " + "; ".join(f"{i['label'] or i['name']}={i['autocomplete']}" for i in personal[:6]))
        else:
            A["cognition"]["CO9"] = ("fail", f"{len(missing)} personal-data field(s) without autocomplete (measured): " + "; ".join(f"{i['type']} {i['label'] or i['name'] or i['id']}" for i in missing[:6]))
    an = F["animation"]
    if not an["animated"] and not an["gifs"] and not an["marqueeBlink"] and not an["canvas"] and not an["svgAnimate"] and not F["media"]["video"] and not F["media"]["autoplay"]:
        A["cognition"]["CO12"] = ("n/a", "no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash")
    return A


# --------------------------------------------------------------------------
# Run-file writing
# --------------------------------------------------------------------------
def latest_run(review, view, modality):
    hits = [d for d in rv.run_dirs(review)
            if rv.run_meta(d)["view"].lower() == view.lower()
            and rv.run_meta(d)["modality"].lower() == modality]
    return hits[-1] if hits else None


def log_run(review, view, modality, locator):
    out = subprocess.run([sys.executable, str(HERE / "review.py"), "log-test", review.name,
                          "--view", view, "--modality", modality, "--tool", "probe",
                          "--url", locator, "--tester", "assistant (view_probe)"],
                         capture_output=True, text=True, encoding="utf-8")
    if out.returncode != 0:
        sys.exit(f"log-test failed:\n{out.stdout}\n{out.stderr}")
    m = re.search(r"Run (R\d{3}) logged", out.stdout)
    if not m:
        sys.exit(f"could not parse run ID:\n{out.stdout}")
    return review / "evidence" / "runs" / m.group(1)


def write_answers(run_dir, answers, facts, modality, today, refresh=()):
    """Fill blank check rows; append measured observations; set Result when
    every row is answered with pass/n-a. Returns a summary dict.

    `refresh`: check IDs whose row may be re-measured — overwritten only when
    the existing outcome is itself a measurement (its note says "measured");
    an outcome a person entered is never touched (2026-09-14: NC2 gained a
    hover/focus measurement and the resting-state rows had to be replaced)."""
    path = run_dir / "run.md"
    text = path.read_text(encoding="utf-8")
    eol = "\r\n" if "\r\n" in text else "\n"
    existing_o = [int(x) for x in re.findall(r"(?m)^- O(\d+) ", text)]
    onum = max(existing_o) if existing_o else 0
    written, skipped, obs_lines = [], [], []
    for cid, (outcome, note) in answers.items():
        pat = re.compile(rf"(?m)^(\|\s*{cid}\s*—\s*[^|]+?\s*\|)([^|]*)\|([^|]*)\|\s*$")
        m = pat.search(text)
        if not m:
            skipped.append(f"{cid} (no row)")
            continue
        if m.group(2).strip():
            if cid in refresh and "measured" in m.group(3):
                note = f"{note} (re-measured {today}; replaces the earlier resting-state measurement)"
            else:
                skipped.append(f"{cid} (already {m.group(2).strip()})")
                continue
        onum += 1
        cell_note = f"O{onum} — {note}"
        cell_note = cell_note.replace("|", "/")
        text = text[:m.start()] + f"{m.group(1)} {outcome} | {cell_note} |" + text[m.end():]
        sc = ", ".join(sorted(rv.check_map().get(cid, {}).get("sc", [])) ) or "FPC"
        obs_lines.append(f"- O{onum} [measured] (state: view as loaded, {today} view_probe): {note.replace('|', '/')}")
        obs_lines.append(f"  - Classified: {cid} / WCAG {sc} / measured → {outcome}")
        written.append(f"{cid}={outcome}")
    if obs_lines:
        block = eol.join(obs_lines) + eol
        if "(none yet)" in text:
            text = text.replace("(none yet)", block.rstrip(eol), 1)
        else:
            text = re.sub(r"(?m)^## Notes", block + eol + "## Notes", text, count=1)
    # Result
    parsed = re.findall(r"(?m)^\|\s*([A-Z]+\d+)\s*—\s*.+?\s*\|(.*?)\|", text)
    outcomes = {cid: o.strip().strip("*` ").lower() for cid, o in parsed}
    blanks = [c for c, o in outcomes.items() if not o]
    fails = [c for c, o in outcomes.items() if o in ("fail", "partial")]
    result_line = re.search(r"(?m)^\|\s*\*\*Result\*\*\s*\|\s*(.*?)\s*\|\s*$", text)
    new_result = None
    if result_line and result_line.group(1).startswith("Not set"):
        tool, baseline = rv.MODALITY_DEFAULTS.get(modality, ("inspection", "—"))
        if not blanks and not fails:
            new_result = "N/A" if all(o == "n/a" for o in outcomes.values()) else "Works"
        elif fails and not blanks:
            new_result = f"Not set — measured fail on {', '.join(fails)}: reviewer confirms → finding, then set"
        elif blanks:
            new_result = (f"Not set — {', '.join(blanks)} need the reviewer ({tool}"
                          + (f", {baseline}" if baseline != "—" else "") + ")"
                          + (f"; measured fail on {', '.join(fails)} awaits confirmation" if fails else ""))
        if new_result:
            text = text[:result_line.start(1)] + new_result + text[result_line.end(1):]
    if written:
        stamp = f"{eol}**view_probe {today}:** answered {', '.join(written)} by measurement; facts in `{run_dir.name}-probe.json`.{eol}"
        text = re.sub(r"(?m)^## Observations", stamp.strip(eol) + eol + eol + "## Observations", text, count=1)
        path.write_text(text, encoding="utf-8")
        (run_dir / f"{run_dir.name}-probe.json").write_text(json.dumps(facts, indent=1, ensure_ascii=False), encoding="utf-8")
    return {"run": run_dir.name, "written": written, "skipped": skipped,
            "result": new_result, "blanks": blanks, "fails": fails}


def grayscale(c, review, view, locator, today, dry_run=False):
    """no-color: emulate achromatopsia over CDP, save the screenshot as evidence in
    the view's no-color run, answer NC2 by measurement (links in running text
    that differ by colour only); NC1/NC3 stay with the reviewer, who judges
    from the screenshot instead of switching the OS filter."""
    import base64
    cues = c.ev(LINK_CUES_JS) or {"inText": 0, "colorOnly": []}
    shot = None
    try:
        c.cmd("Emulation.setEmulatedVisionDeficiency", {"type": "achromatopsia"})
        time.sleep(1.5)
        # an occluded/background window never produces a frame, so
        # captureScreenshot hangs; bring the tab to front first (learned
        # 2026-09-11 — this, not "heavy views", was the hang in testing-tools.md)
        c.cmd("Page.bringToFront")
        c.ws.settimeout(25)
        try:
            shot = c.cmd("Page.captureScreenshot", {"format": "png"})
        except Exception as e:  # noqa: BLE001
            print(f"  [no-color] screenshot skipped: {type(e).__name__} — NC2 still measured")
            # a timed-out reply may arrive later; drain what we can
            try:
                c.ws.settimeout(2); c.ws.recv()
            except Exception:  # noqa: BLE001
                pass
        finally:
            c.ws.settimeout(120)
    finally:
        c.cmd("Emulation.setEmulatedVisionDeficiency", {"type": "none"})
    png = base64.b64decode(shot.get("data", "")) if shot else b""
    def fmt(r):
        return (f"{r['label']} [{r['contrast'] if r['contrast'] is not None else '?'}:1 vs text; "
                f"hover {'cue: ' + r['hover'] if r['hover'] else 'none'}; {r['focus'] or 'focus: none'}]")
    failing, rest = cues.get("failing", []), cues.get("colorOnly", [])
    if failing:
        nc2 = ("fail", f"{len(failing)} of {cues['inText']} link(s) in running text are told from the surrounding text by colour only — "
                       f"no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) "
                       f"does not hold — measured: " + "; ".join(fmt(r) for r in failing[:6])
                       + (f"; {len(rest) - len(failing)} colour-only link(s) DO satisfy G183" if len(rest) > len(failing) else "")
                       + (f"; {cues['unreadableSheets']} cross-origin stylesheet(s) unreadable for hover rules" if cues.get("unreadableSheets") else ""))
    elif rest:
        nc2 = ("pass", f"{len(rest)} of {cues['inText']} link(s) in running text are colour-only at rest but satisfy G183 (≥ 3:1 against the text, "
                       f"non-colour cue on hover and on focus) — measured: " + "; ".join(fmt(r) for r in rest[:6]))
    elif cues["inText"]:
        nc2 = ("pass", f"all {cues['inText']} link(s) in running text carry a non-colour cue (underline/border/weight) — measured")
    else:
        nc2 = ("n/a", "no links inside running text on the view (links are standalone controls/menu items) — measured")
    print(f"  [no-color] screenshot {len(png) // 1024} KB (achromatopsia emulation); NC2={nc2[0]}"
          + (f" — {len(failing)} failing / {len(rest)} colour-only link(s)" if rest else ""))
    if dry_run:
        return
    run_dir = latest_run(review, view, "no-color") or log_run(review, view, "no-color", locator)
    if png:
        (run_dir / f"{run_dir.name}-grayscale.png").write_bytes(png)
    facts = {"view": view, "locator": locator, "probed_at": today, "grayscale": {"screenshot": f"{run_dir.name}-grayscale.png",
             "emulation": "CDP Emulation.setEmulatedVisionDeficiency achromatopsia", "link_cues": cues}}
    ans = {"NC2": nc2,
           }
    s = write_answers(run_dir, ans, facts, "no-color", today, refresh={"NC2"})
    # name the evidence for the reviewer in the Result line
    path = run_dir / "run.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("NC1, NC3 need the reviewer (grayscale)",
                        f"NC1, NC3 need the reviewer — judge from `{run_dir.name}-grayscale.png` (achromatopsia emulation) or the OS filter", 1)
    path.write_text(text, encoding="utf-8")
    print(f"  [no-color] {s['run']}: wrote {', '.join(s['written']) or 'nothing'}"
          + (f"; skipped {', '.join(s['skipped'])}" if s["skipped"] else "")
          + (f"; Result → {s['result']}" if s["result"] else "") + f"; evidence {run_dir.name}-grayscale.png")


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("review")
    ap.add_argument("--view", required=True, help="sample ID (S1, R2 …)")
    ap.add_argument("--url", required=True, help="URL to navigate to, or a 'UI: …' locator to probe the tab as it is")
    ap.add_argument("--settle", type=float, default=6.0)
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--dry-run", action="store_true", help="print facts and would-be answers; write nothing")
    ap.add_argument("--skip-reflow", action="store_true", help="skip the 320 px and text-spacing measurements")
    ap.add_argument("--facts-out", help="also write the facts JSON to this path (useful with --dry-run)")
    ap.add_argument("--grayscale", action="store_true",
                    help="also do the no-color pass: achromatopsia screenshot into the run + NC2 by measurement")
    ap.add_argument("--grayscale-only", action="store_true", help="only the no-color pass (skip facts/answers)")
    args = ap.parse_args()

    review = rv.resolve(args.review)
    today = datetime.date.today().isoformat()
    c = crawl_map.CDP(args.port)
    if args.url.startswith("http"):
        here = c.ev("location.href") or ""
        if here.split("#")[0] != args.url.split("#")[0]:
            c.goto(args.url, settle=args.settle)
    landed = c.ev("location.href")
    print(f"probe {args.view}: {landed}")
    if args.url.startswith("http"):
        # verify the landed view by PATH before measuring — the product may
        # redirect (Expert TA: default2.aspx → default.aspx unless the mode is
        # switched in the UI) and a probe of the wrong view is worse than none
        want = re.sub(r"/+$", "", args.url.split("?")[0].split("#")[0]).lower()
        got = re.sub(r"/+$", "", (landed or "").split("?")[0].split("#")[0]).lower()
        if want != got:
            sys.exit(f"REFUSING: asked for {want} but the tab landed on {got}. "
                     "Reach the view through the UI and re-run with a 'UI: …' locator.")
    if args.grayscale_only:
        grayscale(c, review, args.view, args.url, today, dry_run=args.dry_run)
        if not args.dry_run:
            rv.db_sync(review)
        return
    facts = c.ev(FACTS_JS)
    if not isinstance(facts, dict):
        sys.exit(f"facts script failed: {facts!r}")
    facts["probed_at"] = today
    facts["locator"] = args.url
    facts["view"] = args.view

    extra = {}
    if not args.skip_reflow:
        try:
            c.cmd("Emulation.setDeviceMetricsOverride",
                  {"width": 320, "height": 900, "deviceScaleFactor": 1, "mobile": False})
            time.sleep(2.0)
            extra["reflow"] = c.ev(OVERFLOW_JS)
        finally:
            c.cmd("Emulation.clearDeviceMetricsOverride")
            time.sleep(1.0)
        baseline = c.ev(CLIP_JS) or []
        c.ev("(() => { const s = document.createElement('style'); s.id = '__sfbrn_ts'; s.textContent = "
             + json.dumps(TEXT_SPACING_CSS) + "; document.head.appendChild(s); return true; })()")
        time.sleep(1.5)
        after = c.ev(CLIP_JS) or []
        c.ev("(() => { const s = document.getElementById('__sfbrn_ts'); if (s) s.remove(); return true; })()")
        extra["text_spacing"] = {"baseline": len(baseline), "after": [x for x in after if x not in baseline]}
    facts["measurements"] = extra

    if args.facts_out:
        pathlib.Path(args.facts_out).write_text(json.dumps(facts, indent=1, ensure_ascii=False), encoding="utf-8")
    answers = decide(facts, extra)
    print(f"  title={facts['title']!r} lang={facts['lang']!r} media={media_present(facts) or 'none'} "
          f"speech={facts['scripts']['hits']['speech']} motion={facts['scripts']['hits']['motion']} "
          f"password={facts['passwordFields']} targets={facts['targets']['total']} "
          f"(small {len(facts['targets']['small'])}, failing {len(facts['targets']['failing'])}) "
          f"anim={len(facts['animation']['animated'])}/{len(facts['animation']['gifs'])}gif/{facts['animation']['canvas']}canvas"
          + (f" reflow={extra['reflow']['scrollWidth']}" if extra.get("reflow") else "")
          + (f" ts_new_clips={len(extra['text_spacing']['after'])}" if extra.get("text_spacing") else ""))
    if facts["timerText"]:
        print(f"  timer text (CO7 for the reviewer): {facts['timerText'][:2]}")
    if facts["inputs"]:
        print(f"  personal/name fields: " + "; ".join(f"{i['type']} {i['label'] or i['name'] or i['id']} ac={i['autocomplete']} [{i['personal']}]" for i in facts["inputs"][:8]))

    for modality, ans in answers.items():
        if not ans:
            continue
        line = ", ".join(f"{k}={v[0]}" for k, v in ans.items())
        if args.dry_run:
            print(f"  [{modality}] would answer: {line}")
            continue
        run_dir = latest_run(review, args.view, modality) or log_run(review, args.view, modality, args.url)
        s = write_answers(run_dir, ans, facts, modality, today)
        print(f"  [{modality}] {s['run']}: wrote {', '.join(s['written']) or 'nothing'}"
              + (f"; skipped {', '.join(s['skipped'])}" if s["skipped"] else "")
              + (f"; Result → {s['result']}" if s["result"] else ""))
    if args.grayscale:
        grayscale(c, review, args.view, args.url, today, dry_run=args.dry_run)
    if args.dry_run:
        print(f"  (dry run — facts not saved; run without --dry-run to write)")
    else:
        rv.db_sync(review)


if __name__ == "__main__":
    main()
