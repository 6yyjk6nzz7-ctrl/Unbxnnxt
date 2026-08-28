#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import doc

MODULES = ["content_a", "content_b", "content_c", "content_d", "content_e", "content_f"]

for m in MODULES:
    try:
        mod = __import__(m)
    except ImportError as e:
        print(f"  (skip {m}: {e})")
        continue
    fn = getattr(mod, "build_" + m.split("_")[1])
    fn()

n = doc.build("/home/user/build/marion.html")
print(f"pages: {n}")
