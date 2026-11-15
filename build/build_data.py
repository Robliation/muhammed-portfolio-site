# -*- coding: utf-8 -*-
"""Emit assets/js/data.js + sitemap.xml + robots.txt + .nojekyll from the manifest.

Inputs and outputs are resolved from this file's own location, so it can be run
from anywhere:  python site/build/build_data.py
"""
import json, os, re, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, ".."))
SRC = lambda name: os.path.join(HERE, name)
man = json.load(open(SRC("manifest.json"), encoding="utf-8"))
assets = json.load(open(SRC("assets.json"), encoding="utf-8"))

BASE = "https://robliation.github.io/muhammed-portfolio-site/"
NOW = datetime.date.today().isoformat()

# Brands the owner asked to take out of the site entirely.
EXCLUDE_BRANDS = {"MyRoqia"}

works = []
dropped = 0
for w in man["works"]:
    if w["brand_en"] in EXCLUDE_BRANDS:
        dropped += len(assets[w["id"]])
        continue
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
NOT_A_CLIENT = {"Self-initiated"}
payload = {
    "meta": {
        "sourceFiles": man["source_count"] - dropped,
        "totalWorks": len(works),
        "versions": sum(len(w["imgs"]) for w in works),
        "brands": len({w["brand"]["en"] for w in works}),
        "clients": len({w["brand"]["en"] for w in works} - NOT_A_CLIENT),
        "published": NOW,
    },
    "cats": cats,
    "works": works,
}
js = "window.MD_DATA = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"

# Official client logos collected by brand_logos.py; absent = typographic fallback.
logo_path = os.path.join(OUT, "assets", "brands", "manifest.json")
brands = {}
if os.path.exists(logo_path):
    brands = json.load(open(logo_path, encoding="utf-8"))
js += "window.MD_BRANDS = " + json.dumps(brands, ensure_ascii=False, separators=(",", ":")) + ";"

p = os.path.join(OUT, "assets", "js")
os.makedirs(p, exist_ok=True)
open(os.path.join(p, "data.js"), "w", encoding="utf-8").write(js)
print("data.js", round(len(js) / 1024, 1), "KB |", len(works), "works |",
      payload["meta"]["brands"], "brands |", len(brands), "logos | dropped", dropped, "images")

sm = os.path.join(OUT, "sitemap.xml")
with open(sm, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for loc, pr in [(BASE, "1.0"), (BASE + "cv.html", "0.9")]:
        f.write(f'  <url><loc>{loc}</loc><lastmod>{NOW}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n')
    f.write("</urlset>\n")

BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web", "anthropic-ai",
        "PerplexityBot", "Google-Extended", "Applebot-Extended", "DuckAssistBot", "Bytespider", "CCBot"]
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\n\n")
    f.write("# Answer engines and search assistants are explicitly welcome.\n")
    for b in BOTS:
        f.write(f"User-agent: {b}\nAllow: /\n\n")
    f.write(f"Sitemap: {BASE}sitemap.xml\n")

open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("sitemap/robots/.nojekyll written")


# --- cache busting -----------------------------------------------------------
# GitHub Pages serves these files with caching, so a returning visitor could keep
# an old data.js after a publish (a new design would look "missing"). Stamp every
# local script/style/stylesheet reference with a hash of its content: the URL
# changes exactly when the file changes, so browsers always fetch the new build.
def stamp():
    names = ["assets/js/data.js", "assets/js/site.js", "assets/css/site.css"]
    vers = {}
    for n in names:
        fp = os.path.join(OUT, *n.split("/"))
        if os.path.exists(fp):
            vers[n] = hashlib.md5(open(fp, "rb").read()).hexdigest()[:8]
    for page in ["index.html", "cv.html", "404.html"]:
        fp = os.path.join(OUT, page)
        if not os.path.exists(fp):
            continue
        html = open(fp, encoding="utf-8").read()
        before = html
        for n, v in vers.items():
            base = re.escape(n)
            html = re.sub(base + r"(?:\?v=[0-9a-f]+)?", n + "?v=" + v, html)
        if html != before:
            open(fp, "w", encoding="utf-8").write(html)
            print("stamped", page, vers)


stamp()
