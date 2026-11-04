# Muhammad Al-Masri — Portfolio Site

Bilingual (Arabic-first) portfolio site for **Muhammad Al-Masri / محمد المصري**, a graphic designer in Mecca, Saudi Arabia, presenting **65 advertising designs** created for **37 brands** across restaurants, food, dairy, beverages, retail and tourism.

**Live site:** https://robliation.github.io/muhammed-portfolio-site/
**Behance:** https://www.behance.net/M_Designer_Original
**Email:** muhammedwork7623@gmail.com

## What is in it

| Section | Content |
|---|---|
| Hero board | Four latest proofs on a dark review stage, animated in on load, with the headline, lede and key figures |
| Client strip | "Designed for 35+ brands" over a logo marquee of the actual client marks |
| The work | All 64 designs in a column masonry that preserves each artwork's real aspect ratio, filterable by 8 sectors and searchable by brand or headline |
| Craft | Three curated showcases — product and food compositing, Arabic typography, seasonal campaigns — each with its own selected work |
| Tools | Adobe Photoshop, Adobe Illustrator, CapCut and Google's Nano Banana 2 / Nano Banana Pro with years of practice and app marks |
| About | Profile, capabilities, creative fields and a spec sheet including email and availability |
| Brands | Every client as a card with its official logo (or a lettermark where no logo is published), sector and design count; clicking filters the grid |
| Path | 2021 → 2026 year-by-year learning and application timeline |
| FAQ | Six questions employers and agencies ask, mirrored as `FAQPage` structured data |
| Contact | Email as the primary action, Behance as the portfolio reference |
| [`cv.html`](cv.html) | Full résumé in Arabic and English, with two print buttons — the default export is a single-column ATS-readable PDF |

## Stack

Plain HTML, CSS and ES5 JavaScript — no framework, no build step at deploy time, no dependencies. GitHub Pages serves the files exactly as they are, so nothing can break between a commit and the live site.

- **Typography** — Zain (Arabic display), Archivo (Latin display), IBM Plex Sans Arabic (body)
- **Colour** — the designer's own brand blue `#286BF8` on a paper workspace, with a dark "review stage" surface for the artwork
- **Language** — Arabic is the default (`dir="rtl"`); the EN/عربي toggle is stored in `localStorage` and every layout uses CSS logical properties, so one stylesheet serves both directions
- **Motion** — IntersectionObserver reveals, a scroll-linked hero transition and hover states, all disabled under `prefers-reduced-motion`

## Structure

```
index.html            landing page — hero, client strip, work, craft, tools, about, brands, path, faq, contact
cv.html               printable résumé (AR + EN, ATS print path)
404.html              not-found page
llms.txt              AI-readable summary of the designer, tools, brands and pages
llms-full.txt         every work with its brand, year, formats and deep link
sitemap.xml  robots.txt  .nojekyll
assets/css/site.css   design tokens + all components
assets/js/data.js     the work catalogue and the brand logo map, generated
assets/js/site.js     i18n, filtering, search, proof lightbox, scroll motion
assets/img/           65 works, each as thumb + full in WebP and JPEG
assets/brand/         logo lockup and mark in blue/white/ink, plus favicon
assets/brands/        official client logos + manifest.json
assets/tools/         CapCut and Gemini marks used in the tools section
build/                the pipeline that produced the above
```

## Deep links

Every design has a stable URL: `index.html#work/<slug>` opens it straight into the proof view. The logo mark is used at 1:1 from the designer's own artwork files; the recoloured variants are generated in `build/optimize.py` from the original transparent PNGs.

## Regenerating the site data

```bash
pip install Pillow
cd build
PYTHONIOENCODING=utf-8 python inventory.py      # scan the source design folder
PYTHONIOENCODING=utf-8 python manifest.py       # dedupe into the canonical work list
PYTHONIOENCODING=utf-8 python optimize.py ../   # resize, strip metadata, emit jpg+webp+logo
PYTHONIOENCODING=utf-8 python brand_logos.py    # collect and normalise client logos
PYTHONIOENCODING=utf-8 python build_data.py     # emit data.js, sitemap, robots, .nojekyll
PYTHONIOENCODING=utf-8 python llms.py           # emit llms.txt and llms-full.txt
```

`ROOT` in `inventory.py` and `SRC` / `LOGO_SRC` in `manifest.py` and `optimize.py` are absolute paths to the original artwork — change them before re-running. `EXCLUDE_BRANDS` in `build_data.py` lists brands kept out of the site. `brand_logos.py` tries hand-checked official URLs first, then probes each brand's own site, and falls back to a typographic lettermark when no logo is published — it never substitutes a low-resolution stand-in.

Commit and push; GitHub Pages rebuilds automatically.

## Local preview

```bash
python -m http.server 8000   # then open http://localhost:8000
```

## SEO and AI discoverability

- Unique title and meta description per page, with the primary keyword early
- `keywords`, `author`, canonical, `hreflang` (ar / en / x-default) and full Open Graph + Twitter summary cards with an absolute image URL
- `Person` and `FAQPage` JSON-LD, including email, location, languages and `knowsAbout`
- `sitemap.xml` and a `robots.txt` that explicitly allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Google-Extended, Applebot-Extended, DuckAssistBot, Bytespider and CCBot
- `llms.txt` and `llms-full.txt` at the site root for answer engines and assistants
- Every image carries descriptive `alt` text and intrinsic `width`/`height`, so the layout reserves space and the artwork stays describable

## Brand marks

Client names and logos are the property of their owners and appear only to identify the design work.
