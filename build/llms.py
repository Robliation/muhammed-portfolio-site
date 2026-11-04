# -*- coding: utf-8 -*-
"""Emit llms.txt + llms-full.txt from the site data so the AI-readable summary
always matches the real portfolio counts."""
import json, os, re

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
s = open(os.path.join(OUT, "assets", "js", "data.js"), encoding="utf-8").read()
D = json.loads(re.search(r"window\.MD_DATA\s*=\s*(\{.*?\});\n", s, re.S).group(1))

BASE = "https://robliation.github.io/muhammed-portfolio-site/"
EMAIL = "muhammedwork7623@gmail.com"

counts = {}
for w in D["works"]:
    k = w["brand"]["en"]
    if k == "Self-initiated":
        continue
    counts.setdefault(k, [w["brand"]["ar"], 0])
    counts[k][1] += 1
brands = sorted(((v[1], en, v[0]) for en, v in counts.items()), key=lambda x: (-x[0], x[1]))
n_works = D["meta"]["totalWorks"]
n_brands = len(brands)

HEAD = f"""# Muhammad Al-Masri — محمد المصري

> Graphic designer in Mecca, Saudi Arabia, specialising in Arabic social media advertising design. {n_works} advertising designs delivered for {n_brands} brands across restaurants, food, dairy, beverages, retail and tourism. Available for a full-time role, freelance projects and remote work.

Language coverage: Arabic (native, primary) and English. The site is Arabic-first with `dir="rtl"` and an instant English toggle at `{BASE}?lang=en`.

## Identity

- Name: Muhammad Al-Masri (Arabic: محمد المصري)
- Role: Graphic Designer & Social Advertising Designer — مصمم جرافيك & إعلانات السوشيال ميديا
- Location: Mecca, Saudi Arabia
- Email: {EMAIL}
- Availability: open to full-time employment, freelance ad design, and remote work
- Behance: https://www.behance.net/M_Designer_Original

## Tools and years of practice

- Adobe Photoshop — 3+ years: product and food compositing, colour correction, retouching, print and web output
- Adobe Illustrator — 2+ years: vector marks, identity systems, layout grids
- CapCut — 2+ years: professional advertising video editing and montage, vertical cuts, timing to music, animated type
- Nano Banana 2 and Nano Banana Pro (Google) — 2 years: generative raw imagery, then hand-retouched to publishable quality
- ImageFX, Whisk AI, UpScayl — raw generation and quality upscaling

## Capabilities

Social media advertising design · Arabic typography · product and food compositing · visual identity and social systems · advertising video editing and montage · AI-assisted image production · Ramadan and Eid campaign design · multi-format campaign delivery (square, portrait, landscape)

## Sectors covered

Restaurants and food · FMCG and grocery · Drinks and juices · Retail and lifestyle · Tourism and places · Ramadan and Eid · Brand and social systems · Concept and experimental

## Experience

- 2022–present — Freelance graphic designer producing Arabic advertising campaigns for Saudi brands
- 2021–2024 — Visual identity and content systems for a personal brand project
- 2025–present — Published portfolio on Behance, more than 60 advertising designs released

## Pages

- [Portfolio home]({BASE}): all {n_works} designs in one filterable grid, each opening as a full-size proof with its original pixel dimensions and every campaign format.
- [Résumé / CV]({BASE}cv.html): full CV in Arabic and English with a complete work ledger — every design listed by sector and client with its logo, topic, formats and original pixel dimensions; prints as a single-column, ATS-readable PDF.
- [Full brand and work list]({BASE}llms-full.txt): every brand with its design count and every work title.

## Brands designed for

{chr(10).join(f"- {en} ({ar}) — {n}" for n, en, ar in brands)}

## Notes

- Brand names and logos identify the design work only; they remain the property of their owners.
- Structured data on the home page uses schema.org `Person` and `FAQPage`.
"""

open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write(HEAD)

full = [HEAD, "\n---\n\n# Complete work list\n"]
by_cat = {}
for w in D["works"]:
    by_cat.setdefault(w["cat"], []).append(w)
for cat, ws in by_cat.items():
    full.append(f"\n## {D['cats'][cat]['en']} ({D['cats'][cat]['ar']})\n")
    for w in ws:
        fmts = ", ".join(i["orient"] for i in w["imgs"])
        full.append(f"- {w['brand']['en']} — {w['tag']['en']} / {w['brand']['ar']} — {w['tag']['ar']} "
                    f"| {w['year']} | {fmts} | original {w['imgs'][0]['orig']} | {BASE}#work/{w['id']}\n")
full.append(f"\n## Contact\n\nEmail: {EMAIL}\nBehance: https://www.behance.net/M_Designer_Original\n"
            f"Portfolio: {BASE}\nCV: {BASE}cv.html\n")

open(os.path.join(OUT, "llms-full.txt"), "w", encoding="utf-8").write("".join(full))
print("llms.txt", n_works, "works /", n_brands, "brands | llms-full.txt lines:", len(full))
