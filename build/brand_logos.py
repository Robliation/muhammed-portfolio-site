# -*- coding: utf-8 -*-
"""Collect official client logos for the brand index and the hero ticker.

Best-first per brand:
  1. hand-checked URLs (Wikipedia/Wikimedia SVG wordmarks, official site assets)
  2. a broad probe of the brand's own homepage for header/icon/og assets
  3. typographic wordmark (kind: "wordmark") — no blurry accepts

Output: ../assets/brands/<slug>.<ext> + manifest.json consumed by build_data.py.

    python brand_logos.py            # fetch + normalise
    python brand_logos.py --report   # just print what was found
"""
import json, os, re, subprocess, sys

OUT = os.path.join("..", "assets", "brands")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# slug -> (display name, [direct candidates], homepage to probe)
BRANDS = {
    "albaik":        ("Al Baik", ["https://www.albaik.com/assets/logo_en-4bbf33854ea7afd49a4f426871af04b642becbab3bd4487267047144d176b80c.png"], "https://www.albaik.com/"),
    "almarai":       ("Almarai", ["https://commons.wikimedia.org/wiki/Special:FilePath/Almarai%20Corporate%20Logo.svg"], "https://www.almarai.com/"),
    "jarir":         ("Jarir Bookstore", ["https://www.jarir.com/assets/images/logo/jarir.svg"], "https://www.jarir.com/"),
    "hungerstation": ("Hungerstation", ["https://hungerstation.com/_next/static/media/hungerstation-logo-shadow.1vx_waus0h43y.svg"], "https://hungerstation.com/"),
    "vimto":         ("Vimto", ["https://www.vimto.com/wp-content/themes/vimto-international/assets/images/logo.svg"], "https://www.vimto.com/"),
    "indomie":       ("Indomie", ["https://indomie.com/img/icon/logo-indomie.png"], "https://indomie.com/"),
    "shawarmer":     ("Shawarmer", ["https://commons.wikimedia.org/wiki/Special:FilePath/Shawarmer%20logo.jpg"], "https://www.shawarmer.com/"),
    "saudia":        ("Saudia Cheese", [], "https://www.saudiacheese.com/"),
    "jahez":         ("Jahez", [], "https://jahez.app/"),
    "tazaj":         ("Tazaj", [], "https://www.tazaj.sa/"),
    "qiddiya":       ("Qiddiya", ["https://qiddiya.com/etc.clientlibs/qiddiya-corporate/clientlibs/clientlib-site/resources/metadata/favicons/android/android-icon-192x192.png"], "https://qiddiya.com/"),
    "dubai":         ("Dubai", ["https://commons.wikimedia.org/wiki/Special:FilePath/Government%20of%20Dubai%20logo.svg"], "https://www.visitdubai.com/en"),
    "centrepoint":   ("Centrepoint", [], "https://www.centrepoint.com.sa/"),
    "kinza":         ("Kinza", [], "https://www.kinza.co/"),
    "national-poultry": ("National Poultry", [], "https://www.np.com.sa/"),
    "al-ulali":      ("Al Ulali", [], "https://alulali.com/"),
    "sadia":         ("Sadia", [], "https://sadia.com.sa/"),
    "berain":        ("Berain", [], "https://berain.com/"),
    "aseer-time":    ("Aseer Time", [], "https://aseertime.com/"),
    "marami":        ("Marami", [], "https://maramichips.com/"),
    "country":       ("Country Corn Flakes", [], "https://www.country-foods.com/"),
    "al-yawm":       ("Al Yawm", [], "https://alyawm.com/"),
    "al-adnan":      ("Al Adnan", [], "https://al-adnan.com/"),
    "al-musafir":    ("Al Musafir", [], "https://almusafir.com/"),
    "alromansia":    ("Al Romansia", [], "https://alromansia.com/"),
    "bajah":         ("Bajah", [], "https://bajah.com/"),
    "burger-mish":   ("Burger Mish", [], ""),
    "falafel-burak": ("Falafel Burak", [], ""),
    "ful-wazir":     ("Ful Al-Wazir", [], ""),
    "just-samboosa": ("Just Samboosa", [], ""),
    "kayal":         ("Kayal", [], ""),
    "mazaaq":        ("Mazaaq", [], ""),
    "pizza-offers":  ("Pizza Offers", [], ""),
    "sultan-fish":   ("Sultan Al-Samak", [], ""),
    "takohat":       ("Takohat", [], ""),
    "cake-house":    ("The Cake House", [], ""),
}

GUESS_PATHS = ["/favicon.ico", "/apple-touch-icon.png", "/logo.svg", "/images/logo.svg",
               "/assets/img/logo.svg", "/assets/images/logo.svg", "/static/logo.svg",
               "/wp-content/uploads/logo.png", "/media/logo.png", "/img/logo.svg",
               "/img/logo.png", "/_next/static/media/logo.svg"]


def run(cmd):
    return subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="ignore")


def fetch_bytes(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, "--fail", url],
                       capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return None
    return r.stdout


def html(url):
    if not url:
        return ""
    r = run(["curl", "-sL", "--max-time", "25", "-A", UA, url])
    return r.stdout or ""


def probe(home):
    """Pull every plausible brand asset URL out of a homepage."""
    h = html(home)
    if not h:
        return []
    cand = []
    pats = [
        r'<img[^>]+alt="[^"]*(?:logo|brand|شعار)[^"]*"[^>]+src="([^"]+)"',
        r'<img[^>]+src="([^"]+)"[^>]*alt="[^"]*(?:logo|brand|شعار)',
        r'rel="(?:icon|apple-touch-icon|fluid-icon)"[^>]*href="([^"]+)"',
        r'href="([^"]+)"[^>]*rel="(?:icon|apple-touch-icon)"',
        r'property="og:image"[^>]*content="([^"]+)"',
        r'content="([^"]+)"[^>]*property="og:image"',
        r'["\']([^"\']*(?:logo|Logo|LOGO|brand|Brand|wordmark)[^"\']*\.(?:svg|png|webp))["\']',
    ]
    for p in pats:
        for m in re.finditer(p, h, re.I):
            u = m.group(1).strip()
            if u.startswith("//"):
                u = "https:" + u
            elif u.startswith("/"):
                u = home.rstrip("/") + u
            elif not u.startswith("http"):
                continue
            if "data:" in u or u in cand:
                continue
            cand.append(u)
    for g in GUESS_PATHS:
        cand.append(home.rstrip("/") + g)
    return cand[:14]


def looks_like_logo(data, url):
    if not data or len(data) < 1400:
        return None
    # placeholder icons from site builders, CDNs, and stock-photo houses are not brand marks
    if re.search(r"(?i)(logo-default|placeholder|generic|1x1|spacer)\.(png|jpg|svg|webp)", url):
        return None
    if re.search(r"(?i)(gettyimages|isteam|wsimg|shutterstock|pexels|unsplash|adobe-stock|wikia|mwstatic)", url):
        return None
    head = data[:64]
    if head[1:4] == b"PNG":
        kind = "png"
    elif head[3:7] == b"ftyp":
        kind = "heif"
    elif head[:3] == b"\xff\xd8\xff":
        kind = "jpg"
    elif head[:4] == b"RIFF" and data[8:12] == b"WEBP":
        kind = "webp"
    elif b"<svg" in data[:400] or data[:5] in (b"<?xml", b"<svg ") or data[:4] == b"<svg":
        kind = "svg"
    elif head[:6] in (b"GIF89a", b"GIF87a"):
        kind = "gif"
    elif head[:1] == b"<":
        kind = "html"
    else:
        kind = "bin"
    if kind in ("html", "bin", "heif"):
        return None
    if kind == "svg" and re.search(r"(?i)<(title|h1)\b", data.decode("utf-8", "ignore")[:3000]):
        pass
    return kind


def save(slug, data, kind):
    ext = {"svg": "svg", "png": "png", "jpg": "jpg", "webp": "webp", "gif": "gif"}[kind]
    path = os.path.join(OUT, slug + "." + ext)
    with open(path, "wb") as f:
        f.write(data)
    return slug + "." + ext, len(data)


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest, report = {}, []
    for slug, (name, direct, home) in BRANDS.items():
        got = None
        for url in direct + probe(home):
            data = fetch_bytes(url)
            kind = looks_like_logo(data, url)
            if kind:
                fn, size = save(slug, data, kind)
                got = {"file": fn, "kind": "official", "bytes": size, "src": url}
                break
        if not got:
            got = {"file": None, "kind": "wordmark", "src": ""}
        manifest[name] = got
        flag = "OK  " if got["kind"] == "official" else "--  "
        report.append("%s %-20s %s %7s  %s" % (flag, name, got["kind"], got.get("bytes", ""), (got.get("src") or "")[:78]))
    json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\n".join(report))
    n = sum(1 for v in manifest.values() if v["kind"] == "official")
    print("\nofficial %d / %d, wordmark fallback %d" % (n, len(manifest), len(manifest) - n))
    print("manifest ->", os.path.join(OUT, "manifest.json"))


if __name__ == "__main__":
    main()
