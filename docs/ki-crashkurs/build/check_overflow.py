#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flag pages whose content runs into the bottom margin, and pages that are
suspiciously empty. Catches the class of bug where overflow:hidden silently
slices a card off at the page trim.

Usage: check_overflow.py <file.pdf>
"""
import sys
import pypdfium2 as pdfium

PDF = sys.argv[1]
SCALE = 2.0                     # px per pt
MM = 297.0                      # A4 height in mm

doc = pdfium.PdfDocument(PDF)
bad, empty = [], []

for i in range(len(doc)):
    img = doc[i].render(scale=SCALE).to_pil().convert("RGB")
    W, H = img.size
    px = img.load()
    mm2y = lambda mm: int(H * mm / MM)

    # Page ground: sample a spot inside the top margin, away from the running head.
    ground = px[int(W * 0.5), mm2y(4)]

    def differs(c, ref, tol=26):
        return (abs(c[0] - ref[0]) > tol or abs(c[1] - ref[1]) > tol
                or abs(c[2] - ref[2]) > tol)

    # Forbidden zone: below the text block, excluding the page-number corner.
    y0, y1 = mm2y(280), mm2y(296)
    x0, x1 = int(W * 0.06), int(W * 0.86)  # excludes the page-number corner
    hits = sum(1 for y in range(y0, y1, 2) for x in range(x0, x1, 2)
               if differs(px[x, y], ground))
    if hits > 40:
        bad.append((i + 1, hits))

    # How far down does content actually reach?
    last = 0
    for y in range(mm2y(275), mm2y(22), -3):
        row = sum(1 for x in range(x0, x1, 4) if differs(px[x, y], ground))
        if row > 2:
            last = y
            break
    fill_mm = last / H * MM
    if fill_mm < 205:
        empty.append((i + 1, round(fill_mm)))

print("── BOTTOM-MARGIN OVERFLOW ──")
print("  none" if not bad else "\n".join(f"  page {p}: {h} stray marks" for p, h in bad))
print("\n── UNDER-FILLED (content ends above 205mm of 297mm) ──")
print("  none" if not empty else "\n".join(f"  page {p}: content ends at {mm}mm" for p, mm in empty))
