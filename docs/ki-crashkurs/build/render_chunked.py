#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Render a large multi-page HTML to PDF in chunks, then merge.

Chromium's printToPDF stalls on very long documents; splitting the page divs
into batches and concatenating the resulting PDFs is fast and lossless.

Usage: render_chunked.py <input.html> <output.pdf> [pages_per_chunk]
"""
import os, re, subprocess, sys, tempfile
from pypdf import PdfWriter, PdfReader

BUILD = os.path.dirname(os.path.abspath(__file__))
inp, outp = sys.argv[1], sys.argv[2]
CHUNK = int(sys.argv[3]) if len(sys.argv) > 3 else 8

html = open(inp, encoding="utf-8").read()

m = re.search(r"^(.*?<body>\s*)(.*?)(\s*</body>.*)$", html, re.S)
if not m:
    sys.exit("could not split html into head/body/tail")
head, body, tail = m.group(1), m.group(2), m.group(3)

# Split on top-level page divs.
parts = re.split(r'(?=<div class="page )', body)
pages = [p for p in parts if p.strip().startswith('<div class="page ')]
if not pages:
    sys.exit("no .page divs found")
print(f"{len(pages)} page blocks, {CHUNK} per chunk")

tmpdir = tempfile.mkdtemp(prefix="chunks-")
pdfs = []
for i in range(0, len(pages), CHUNK):
    grp = pages[i:i + CHUNK]
    # Last page of every chunk must not force a trailing blank page.
    chunk_html = head + "\n".join(grp) + tail
    chunk_html = chunk_html.replace(
        "</style>",
        ".page:nth-last-child(1){page-break-after:auto!important;"
        "break-after:auto!important}</style>")
    hp = os.path.join(tmpdir, f"c{i:03d}.html")
    pp = os.path.join(tmpdir, f"c{i:03d}.pdf")
    open(hp, "w", encoding="utf-8").write(chunk_html)
    r = subprocess.run(["node", os.path.join(BUILD, "render.js"), hp, pp],
                       capture_output=True, text=True, timeout=300)
    if r.returncode != 0:
        sys.exit(f"chunk {i} failed: {r.stdout} {r.stderr}")
    n = len(PdfReader(pp).pages)
    print(f"  chunk {i//CHUNK+1}: pages {i+1}-{i+len(grp)} -> {n} pdf pages")
    if n != len(grp):
        print(f"  !! expected {len(grp)} pages, got {n}")
    pdfs.append(pp)

w = PdfWriter()
for p in pdfs:
    for pg in PdfReader(p).pages:
        w.add_page(pg)
with open(outp, "wb") as f:
    w.write(f)
total = len(PdfReader(outp).pages)
print(f"OK  {outp}  {os.path.getsize(outp)//1024} KB  {total} pages")
