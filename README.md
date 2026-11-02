# Muhammed Portfolio Site

A bilingual (Arabic-first) portfolio site for **Muhammed**, a graphic designer in Mecca, Saudi Arabia, presenting 68 advertising designs made for 38 brands.

**Live site:** https://robliation.github.io/muhammed-portfolio-site/
**Behance:** https://www.behance.net/M_Designer_Original

## What is in it

| Section | Content |
|---|---|
| Hero board | Four latest proofs on a dark review stage, animated in on load |
| The work | All 68 designs in a column masonry that preserves each artwork's real aspect ratio, filterable by 8 sectors and searchable by brand or headline |
| Proof view | Any design opens full size with its specs: sector, year, original pixel dimensions, available formats, and a direct Behance link when the piece is published |
| About | Profile, capabilities, tools, creative fields, and a spec sheet |
| Brands | Every brand in the work with its design count |
| Path | 2024 → 2026 timeline |
| Contact | Behance messaging, GitHub, availability |
| [`cv.html`](cv.html) | Printable résumé, Arabic and English in one page (`Ctrl/Cmd+P` → Save as PDF) |

## Stack

Plain HTML, CSS and ES5 JavaScript — no framework, no build step at deploy time, no dependencies. Chosen deliberately: GitHub Pages serves the files exactly as they are, so nothing can break between a commit and the live site.

- **Typography** — Zain (Arabic display), Archivo (Latin display), IBM Plex Sans Arabic (body)
- **Colour** — the designer's own brand blue `#286BF8` on a paper workspace, with a dark "review stage" surface for the artwork
- **Language** — Arabic is the default (`dir="rtl"`); the EN/عربي toggle is stored in `localStorage` and every layout uses CSS logical properties, so one stylesheet serves both directions

## Structure

```
index.html            landing page — hero, work grid, about, brands, path, contact
cv.html               printable résumé (AR + EN)
404.html              not-found page
sitemap.xml  robots.txt  .nojekyll
assets/css/site.css   design tokens + all components
assets/js/data.js     the work catalogue, generated
assets/js/site.js     i18n, filtering, search, proof lightbox
assets/img/           68 works, each as thumb + full in WebP and JPEG
assets/brand/         logo lockup and mark in blue/white/ink, plus favicon
build/                the pipeline that produced the above
```

## Deep links

Every design has a stable URL: `index.html#work/<slug>` opens it straight into the proof view. The logo mark is used at 1:1 from the designer's own artwork files; the recoloured variants are generated in `build/optimize.py` from the original transparent PNGs.

## Regenerating the data and images

`build/` holds the pipeline that produced this site, kept verbatim for provenance. It reads the original design folder and writes `assets/img/`, `assets/brand/`, `assets/js/data.js`, `sitemap.xml` and `robots.txt`.

```bash
pip install Pillow
cd build
PYTHONIOENCODING=utf-8 python inventory.py     # scan the source folder
PYTHONIOENCODING=utf-8 python manifest.py      # dedupe into the canonical work list
PYTHONIOENCODING=utf-8 python optimize.py ../  # resize, strip metadata, emit jpg+webp+logo
PYTHONIOENCODING=utf-8 python build_data.py    # emit data.js, sitemap, robots, .nojekyll
```

`ROOT` in `inventory.py` and `SRC` / `LOGO_SRC` in `manifest.py` and `optimize.py` are absolute paths to the designer's original artwork — change them to your own folders before re-running. `optimize.py` writes its output to the directory given as its first argument. `manifest.py` is the file that records which source images collapse into one work, and which of the twelve Behance projects each work corresponds to.

## Local preview

```bash
python -m http.server 8000   # then open http://localhost:8000
```

## Notes on the work itself

Unless a project says otherwise, these are **concept (spec) advertisements** for existing brands — produced as portfolio training for the Saudi market, not as commissioned campaigns. The site states this rather than implying client relationships.
