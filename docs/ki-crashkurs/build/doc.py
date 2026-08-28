#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Builder for the Marion AI crash-course PDF.
Assembles designed A4 pages into a single HTML file for Chromium to print."""

import os, sys, html as _html
from qr import qr_svg

BUILD = os.path.dirname(os.path.abspath(__file__))
FONTDIR = "/home/user/fonts"

# ── page registry ────────────────────────────────────────────
PAGES = []
_SECTION = {"name": "", "num": ""}


def set_section(name, num=""):
    _SECTION["name"] = name
    _SECTION["num"] = num


ANCHORS = {}


def page(inner, cls="", pn=True, rh=True, rh_left=None, rh_right=None,
         foot=None, anchor=None):
    """Register one A4 page. Page number is assigned at render time."""
    PAGES.append({
        "inner": inner, "cls": cls, "pn": pn, "rh": rh,
        "rh_left": rh_left if rh_left is not None else _SECTION["name"],
        "rh_right": rh_right, "foot": foot,
    })
    if anchor:
        if anchor in ANCHORS:
            raise ValueError(f"duplicate anchor: {anchor}")
        ANCHORS[anchor] = len(PAGES)


def ref(name):
    """Emit a page-number placeholder resolved after layout is known.

    Hand-written 'Seite 13' references rot the moment a page is added; this
    keeps every cross-reference correct by construction.
    """
    return "{{P:" + name + "}}"


def render_pages():
    out = []
    n = 0
    for p in PAGES:
        n += 1
        parts = [f'<div class="page {p["cls"]}">']
        if p["rh"] and p["rh_left"]:
            right = p["rh_right"] if p["rh_right"] is not None else "KI-Crashkurs für Marion"
            parts.append(
                f'<div class="rh"><span class="rh-sec">{p["rh_left"]}</span>'
                f'<span>{right}</span></div>')
        parts.append(p["inner"])
        if p["foot"]:
            parts.append(f'<div class="foot-note">{p["foot"]}</div>')
        if p["pn"]:
            parts.append(f'<div class="pn">{n}</div>')
        parts.append("</div>")
        out.append("\n".join(parts))
    return "\n".join(out), n


# ── component helpers ────────────────────────────────────────
def esc(s):
    return _html.escape(s, quote=False)


def kicker(t, cls=""):
    return f'<span class="kicker {cls}">{t}</span>'


def fact(big, unit, text, src):
    u = f"<small>{unit}</small>" if unit else ""
    return (f'<div class="fact no-break"><div class="big">{big}{u}</div>'
            f'<div><p>{text}</p><span class="src">{src}</span></div></div>')


def callout(label, body, kind="honest"):
    return (f'<div class="callout co-{kind} no-break"><span class="clabel">{label}</span>'
            f'{body}</div>')


def prompt(label, body, light=False):
    cls = "prompt prompt-light" if light else "prompt"
    return (f'<div class="{cls} no-break"><span class="pl">{label}</span>{body}</div>')


def card(body, kind=""):
    return f'<div class="card {kind} no-break">{body}</div>'


def resource(title, desc, url, kind, lang, cost, time, qr_size=16):
    pills = []
    lang_cls = "de" if lang.lower().startswith("de") else "en"
    pills.append(f'<span class="pill {lang_cls}">{lang}</span>')
    if cost:
        cost_cls = "free" if cost.lower() in ("kostenlos", "free", "gratis") else ""
        pills.append(f'<span class="pill {cost_cls}">{cost}</span>')
    if time:
        pills.append(f'<span class="pill">{time}</span>')
    if kind:
        pills.append(f'<span class="pill">{kind}</span>')
    show_url = url.replace("https://", "").replace("http://", "")
    return (
        f'<div class="res no-break">{qr_svg(url, size_mm=qr_size)}'
        f'<div><h4>{title}</h4><p>{desc}</p>'
        f'<div class="meta">{"".join(pills)}</div>'
        f'<span class="url">{show_url}</span></div></div>')


def wk(day, title, mins, body):
    return (f'<div class="wk no-break"><div class="day">{day}</div><div class="body">'
            f'<h4>{title}</h4><span class="mins">{mins}</span>'
            f'<div class="sp-2"></div>{body}</div></div>')


def toc_row(n, title, desc, pageno):
    return (f'<div class="toc-row"><span class="t-n">{n}</span>'
            f'<span><span class="t-t">{title}</span>'
            f'<span class="t-d">{desc}</span></span>'
            f'<span class="t-p">{pageno}</span></div>')


def gloss(term, definition):
    return f'<div class="gloss"><dt>{term}</dt><dd>{definition}</dd></div>'


def opener(num, title, sub, items=None):
    lis = ""
    if items:
        lis = '<div class="toc-mini">' + "".join(
            f'<div><b>{a}</b> &nbsp;·&nbsp; {b}</div>' for a, b in items) + "</div>"
    return (f'<div class="num-xl">{num}</div><h1>{title}</h1>'
            f'<p class="sub">{sub}</p>{lis}')


# ── assembly ─────────────────────────────────────────────────
def build(out_html, title="KI-Crashkurs für Marion"):
    css = open(os.path.join(BUILD, "styles.css"), encoding="utf-8").read()
    css = css.replace("FONTDIR", FONTDIR)
    body, n = render_pages()

    # Resolve {{P:anchor}} cross-references now that pagination is final.
    import re as _re
    missing = set()

    def _sub(mo):
        key = mo.group(1)
        if key == "TOTAL":
            return str(n)
        if key not in ANCHORS:
            missing.add(key)
            return "??"
        return str(ANCHORS[key])

    body = _re.sub(r"\{\{P:([A-Za-z0-9_]+)\}\}", _sub, body)
    if missing:
        raise ValueError(f"unknown page anchors: {sorted(missing)}")
    # An f-string collapses {{P:x}} to {P:x}, which the resolver above cannot
    # see; that shipped a literal placeholder onto the cover once. Fail loudly.
    stray = _re.findall(r"\{P:[A-Za-z0-9_]+\}", body)
    if stray:
        raise ValueError(f"unresolved placeholders (escape braces in f-strings): {set(stray)}")

    doc = f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>{title}</title>
<style>
{css}
</style></head>
<body>
{body}
</body></html>"""
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(doc)
    return n
