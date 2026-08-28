#!/usr/bin/env python
"""Render PDF pages to PNG for visual review.
Usage: preview.py <file.pdf> <outdir> [scale] [pages e.g. 1-4,7]"""
import sys, os
import pypdfium2 as pdfium

pdf_path, outdir = sys.argv[1], sys.argv[2]
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.6
spec = sys.argv[4] if len(sys.argv) > 4 else None

os.makedirs(outdir, exist_ok=True)
doc = pdfium.PdfDocument(pdf_path)
n = len(doc)

if spec:
    idx = []
    for part in spec.split(','):
        if '-' in part:
            a, b = part.split('-')
            idx += list(range(int(a) - 1, int(b)))
        else:
            idx.append(int(part) - 1)
    idx = [i for i in idx if 0 <= i < n]
else:
    idx = range(n)

for i in idx:
    img = doc[i].render(scale=scale).to_pil()
    out = os.path.join(outdir, f"p{i+1:02d}.png")
    img.save(out)
    print(f"{out}  {img.width}x{img.height}")
print(f"total pages: {n}")
