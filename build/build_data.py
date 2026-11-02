# -*- coding: utf-8 -*-
"""Emit assets/js/data.js + sitemap.xml + robots.txt from the manifest."""
import json, os, datetime

OUT = os.path.join("..", "site")
man = json.load(open("manifest.json", encoding="utf-8"))
assets = json.load(open("assets.json", encoding="utf-8"))

BASE = "https://robliation.github.io/muhammed-portfolio-site/"
NOW = "2026-11-02"

works = []
for w in man["works"]:
    ents = assets[w["id"]]
    imgs = [{
        "stem": e["full"].rsplit("/", 1)[-1], "tw": e["thumb_w"], "th": e["thumb_h"],
        "fw": e["full_w"], "fh": e["full_h"], "orient": e["orient"],
        "year": e["year"], "orig": f'{e["orig_w"]}×{e["orig_h"]}',
    } for e in ents]
    works.append({
        "id": w["id"], "brand": {"ar": w["brand_ar"], "en": w["brand_en"]},
        "tag": {"ar": w["tagline_ar"], "en": w["tagline_en"]},
        "cat": w["cat"], "year": w["year"], "behance": w["behance"],
        "imgs": imgs,
    })

cats = {k: {"ar": v[1], "en": v[0]} for k, v in man["cats"].items()}
payload = {
    "meta": {
        "sourceFiles": man["source_count"],
        "totalWorks": len(works),
        "brands": len({w["brand"]["en"] for w in works}),
        "published": NOW,
    },
    "cats": cats,
    "works": works,
}
js = "window.MD_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";"
p = os.path.join(OUT, "assets", "js")
os.makedirs(p, exist_ok=True)
open(os.path.join(p, "data.js"), "w", encoding="utf-8").write(js)
print("data.js", round(len(js) / 1024, 1), "KB |", len(works), "works")

sm = os.path.join(OUT, "sitemap.xml")
with open(sm, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for loc, pr in [(BASE, "1.0"), (BASE + "cv.html", "0.8")]:
        f.write(f'  <url><loc>{loc}</loc><lastmod>{NOW}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n')
    f.write("</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
    f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("sitemap/robots/.nojekyll written")
