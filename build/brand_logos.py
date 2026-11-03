# -*- coding: utf-8 -*-
"""Assemble the client logo wall from real marks — no typographic stand-ins.

Three provenance tiers, in the order the designer asked for:

  artwork  the logo lifted out of a corner of Muhammad's own design for that
           client (the mark as it actually ships in the work)
  asset    the logo file from his working library (Pictures/Pictures Photoshop/Logos)
  web      the official mark fetched from the brand's own site / Wikimedia

Every mark is then plated onto one shared transparent canvas sized to the tile's
inner box, with its drawn area equalised across the wall. Contain-fit size is a
function of aspect alone, so the padding baked into the plate — not the pixel
count — is what makes a 6:1 wordmark and a 1:1 emblem read at the same weight.
Marks whose colour is too dark for the ink tile get their value raised and their
saturation eased, in small steps, until they clear a 3.6:1 contrast ratio — hue
is kept, so the brand still reads as itself.

    python brand_logos.py

Output: ../assets/brands/<slug>.<ext> + manifest.json consumed by build_data.py.
"""
import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "brands")
LIB = r"C:\Users\M Deisgner\Pictures\Pictures Photoshop\Logos"
ART = r"C:\Users\M Deisgner\Pictures\Pictures Photoshop\Designs"

TILE_RGB = (11, 16, 32)           # the ink the marks are finally seen on
CR_FLOOR = 3.6                    # WCAG 1.4.11 asks 3:1 for graphics; we clear it with margin

# The tile's inner box once padding and border are taken off (.logo-slot is
# 168x84 with 12px/9px padding and a 1px border). Every mark is finally plated
# onto a transparent canvas of exactly this aspect, so object-fit:contain maps
# the canvas 1:1 onto the tile and the plated area is the area the user sees.
PLATE_W, PLATE_H = 284, 128
# Marks whose natural fit is heavier than this get padded back down to it.
# Contain-fit size depends only on aspect, so padding is the only lever that can
# equalise a 6:1 wordmark and a 1:1 emblem; growing a small mark is impossible.
PLATE_TARGET = int(PLATE_W * PLATE_H * 0.50)

# slug -> (display name, source kind, source ref, extra)
#   asset   -> filename in the designer's Logos folder
#   artwork -> (design filename, fractional corner box)
#   web     -> existing file already in assets/brands
BRANDS = [
    ("albaik",           "Al Baik",             "web",     "albaik.png"),
    ("almarai",          "Almarai",             "web",     "almarai.svg"),
    ("jarir",            "Jarir Bookstore",     "web",     "jarir.svg"),
    ("hungerstation",    "Hungerstation",       "web",     "hungerstation.svg"),
    ("dubai",            "Dubai",               "web",     "dubai.svg"),
    ("indomie",          "Indomie",             "web",     "indomie.png"),
    ("shawarmer",        "Shawarmer",           "web",     "shawarmer.jpg"),
    ("qiddiya",          "Qiddiya",             "asset",   "Qiddiya_Logo.svg"),
    ("tazaj",            "Tazaj",               "asset",   "Al_Tazaj_logo.png"),
    ("marami",           "Marami",              "asset",   "Marami Logo.jpeg"),
    ("al-ulali",         "Al Ulali",            "asset",   "شعار العلالي_upscayl_4x_upscayl-standard-4x.png"),
    ("sadia",            "Sadia",               "asset",   "شعار ساديا.png"),
    ("aseer-time",       "Aseer Time",          "asset",   "شعار عصير تايم_upscayl_4x_upscayl-standard-4x.png"),
    ("burger-mish",      "Burger Mish",         "asset",   "شعار برجر مش_upscayl_2x_upscayl-standard-4x.png"),
    ("just-samboosa",    "Just Samboosa",       "asset",   "شعار جست سمبوسة_upscayl_4x_upscayl-standard-4x.png"),
    ("kayal",            "Kayal",               "asset",   "شعار مطعم خيال.png"),
    ("ful-wazir",        "Ful Al-Wazir",        "asset",   "شعار مطعم فول الوزير.png"),
    ("sultan-fish",      "Sultan Al-Samak",     "asset",   "شعار سلطان السمك_upscayl_4x_upscayl-standard-4x.png"),
    ("cake-house",       "The Cake House",      "asset",   "شعار مطعم بيت الكيك_upscayl_4x_upscayl-standard-4x.png"),
    ("al-adnan",         "Al Adnan",            "artwork", ("تصميم لمطعم العدنان (دوالي).jpg", (0.900, 0.000, 0.998, 0.115))),
    ("al-musafir",       "Al Musafir",          "artwork", ("تصميم لشركة المسافر (أستمتع بأكلك في أي مكان).jpg", (0.850, 0.895, 0.999, 0.998))),
    ("al-romansia",      "Al Romansia",         "artwork", ("تصميم لمطعم الرومانسية (مطعم المـــــــثـــــــالـــــــــــي).jpg", (0.895, 0.000, 0.998, 0.105))),
    ("al-yawm",          "Al Yawm",             "artwork", ("تصميم لشركة اليوم (تمشي مع اليوم).jpg", (0.402, 0.250, 0.558, 0.375))),
    ("bajah",            "Bajah",               "artwork", ("تصميم لشركة باجة (قهوة تمتع يومك).jpg", (0.865, 0.000, 0.992, 0.085))),
    ("berain",           "Berain",              "artwork", ("تصميم لشركة بيرين (ماء ثلج).jpg", (0.855, 0.010, 0.985, 0.115))),
    ("centrepoint",      "Centrepoint",         "artwork", ("تصميم لشركة سنتربوينت (شنطة سفرك في أمـــــــــــــــان).jpg", (0.852, 0.000, 0.996, 0.062))),
    ("country",          "Country Corn Flakes", "artwork", ("تصميم لشركة كونتري كورن فليكس (بروتين ينفع مع كورن فليكس).jpg", (0.838, 0.008, 0.986, 0.135))),
    ("falafel-burak",    "Falafel Burak",       "artwork", ("تصميم لشركة فلافل بوراك (عندنا فلافل صح) بالعرض.jpg", (0.872, 0.000, 0.996, 0.125))),
    ("jahez",            "Jahez",               "artwork", ("تصميم لشركة جاهز.jpg", (0.402, 0.000, 0.568, 0.085))),
    ("kinza",            "Kinza",               "artwork", ("تصميم لشركة كينزا (مشروب ينسيك العطش).jpg", (0.852, 0.000, 0.988, 0.085))),
    ("mazaaq",           "Mazaaq",              "artwork", ("تصميم لشركة مذاق بالعرض.png", (0.852, 0.000, 0.988, 0.085))),
    ("national-poultry", "National Poultry",    "artwork", ("تصميم لشركة دواجن الوطنية (مندي طيب مع دواجن الوطنية) بالعرض.jpg", (0.872, 0.000, 0.996, 0.062))),
    ("pizza-offers",     "Pizza Offers",        "artwork", ("تصميم لشركة عروض بيتزا بالعرض.png", (0.850, 0.000, 0.996, 0.115))),
    ("saudia",           "Saudia Cheese",       "artwork", ("تصميم لشركة السعودية (جبنة الملوك).jpg", (0.872, 0.000, 0.996, 0.125))),
    ("takohat",          "Takohat",             "artwork", ("تصميم لشركة تاكوهت (الأكلة تخليك توكل أصعابك).jpg", (0.004, 0.000, 0.215, 0.105))),
    ("vimto",            "Vimto",               "artwork", ("تصميم لشركة فيمتو (رمضان كريم).jpg", (0.852, 0.000, 0.992, 0.085))),
]

# Marks that read as a silhouette on the ink tile get a value lift in CSS instead
# of a raster re-encode (they stay vector).
SVG_LIFT = {"almarai", "hungerstation"}


# ---------------------------------------------------------------- keying helpers

def has_alpha(im):
    if im.mode != "RGBA":
        return False
    lo, hi = im.getchannel("A").getextrema()
    return lo < 250


def maxdiff(rgb, bg):
    """Per-pixel distance keyed on the widest channel gap — a gold mark on cream
    differs almost entirely in blue, which luma would average away."""
    d = ImageChops.difference(rgb, bg)
    r, g, b = d.split()
    return ImageChops.lighter(ImageChops.lighter(r, g), b)


def key_flat_bg(im, want="white"):
    """Turn a solid white/black background transparent, keeping the mark."""
    rgb = im.convert("RGB")
    edge = []
    w, h = rgb.size
    step = max(1, w // 60)
    for x in range(0, w, step):
        edge.append(rgb.getpixel((x, 0)))
        edge.append(rgb.getpixel((x, h - 1)))
    step = max(1, h // 60)
    for y in range(0, h, step):
        edge.append(rgb.getpixel((0, y)))
        edge.append(rgb.getpixel((w - 1, y)))
    ref = tuple(sum(c[i] for c in edge) // len(edge) for i in range(3))
    bg = Image.new("RGB", rgb.size, ref)
    d = maxdiff(rgb, bg)
    lo, hi = (34, 120) if want == "white" else (30, 110)
    alpha = d.point(lambda p: 0 if p < lo else (255 if p > hi else int((p - lo) * 255 / (hi - lo))))
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.5))
    out = rgb.convert("RGBA")
    out.putalpha(alpha)
    return out


def key_local_bg(im):
    """Lift a mark off a gradient or photographic corner by local background distance."""
    w, h = im.size
    small = im.resize((max(1, w // 16), max(1, h // 16))).filter(ImageFilter.GaussianBlur(2.0))
    bg = small.resize((w, h), Image.BILINEAR)
    d = maxdiff(im, bg)
    t0, t1 = 26, 88
    alpha = d.point(lambda p: 0 if p < t0 else (255 if p > t1 else int((p - t0) * 255 / (t1 - t0))))
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.6))
    out = im.convert("RGBA")
    out.putalpha(alpha)
    return out


def defringe(im, cut=96):
    """Kill the low-alpha haze a soft matte leaves behind, then pull the edge in."""
    a = im.getchannel("A").point(lambda p: 0 if p < cut else p)
    a = a.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.4))
    out = im.copy()
    out.putalpha(a)
    return out


def trim(im, pad=6):
    a = im.getchannel("A").point(lambda p: 255 if p > 44 else 0)
    bb = a.getbbox()
    if not bb:
        return im
    return im.crop((max(0, bb[0] - pad), max(0, bb[1] - pad),
                    min(im.width, bb[2] + pad), min(im.height, bb[3] + pad)))


def _lin(ch):
    v = ch / 255.0
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def _lum_of(r, g, b):
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


BG_LUM = _lum_of(*TILE_RGB)


def mark_lum(im):
    """Mean linear luminance of the mark's own pixels, edges and padding excluded."""
    px = list(im.convert("RGBA").getdata())[::5]
    keep = [_lum_of(r, g, b) for r, g, b, a in px if a > 200]
    return sum(keep) / len(keep) if keep else 1.0


def tile_contrast(im):
    m = mark_lum(im)
    return (max(m, BG_LUM) + 0.05) / (min(m, BG_LUM) + 0.05)


def readable(im):
    """Bring a mark up to the ink tile without throwing its hue away.

    A saturated maroon sits at a low luminance that no amount of value lift fixes
    on its own, so value climbs and saturation eases in small steps together until
    the mark clears WCAG 1.4.11's 3:1 bar for graphics with margin over it.
    """
    for _ in range(5):
        if tile_contrast(im) >= CR_FLOOR:
            break
        h, s, v = im.convert("HSV").split()
        v = v.point(lambda p: min(255, int(p * 1.18 + 6)))
        s = s.point(lambda p: int(p * 0.86))
        out = Image.merge("HSV", (h, s, v)).convert("RGBA")
        out.putalpha(im.getchannel("A"))
        im = out
    return im


def cap(im, edge=760):
    if max(im.size) > edge:
        f = edge / max(im.size)
        im = im.resize((max(1, int(im.width * f)), max(1, int(im.height * f))), Image.LANCZOS)
    return im


def fit_area(a):
    """Area a mark of aspect a occupies when contained in the plate box."""
    return PLATE_W ** 2 / a if a >= PLATE_W / PLATE_H else a * PLATE_H ** 2


def plate(im):
    """Re-plate a trimmed mark onto the shared canvas at an equalised area."""
    a = im.width / float(im.height)
    area = min(fit_area(a), PLATE_TARGET)
    mh = max(1.0, (area / a) ** 0.5)
    mw = a * mh
    if mw > PLATE_W or mh > PLATE_H:            # very extreme aspect: just contain it
        f = min(PLATE_W / float(im.width), PLATE_H / float(im.height))
        mw, mh = im.width * f, im.height * f
    canvas = Image.new("RGBA", (PLATE_W, PLATE_H), (0, 0, 0, 0))
    scaled = im.resize((max(1, int(round(mw))), max(1, int(round(mh)))), Image.LANCZOS)
    canvas.paste(scaled, ((PLATE_W - scaled.width) // 2, (PLATE_H - scaled.height) // 2), scaled)
    return canvas


def plate_svg(raw, name):
    """Pad an SVG's viewBox so its mark lands on the same plate as the PNGs."""
    import re
    txt = raw.decode("utf-8", "ignore")
    m = re.search(r'viewBox="([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)"', txt)
    if not m:
        return raw, None
    vx, vy, vw, vh = (float(g) for g in m.groups())
    if vw <= 0 or vh <= 0:
        return raw, None
    a = vw / vh
    area = min(fit_area(a), PLATE_TARGET)
    mh = (area / a) ** 0.5
    mw = a * mh
    if mw > PLATE_W or mh > PLATE_H:
        f = min(PLATE_W / vw, PLATE_H / vh)
        mw, mh = vw * f, vh * f
    # viewBox units are the mark's own; grow it so the mark covers mw x mh of the
    # plate, keeping the plate aspect.
    scale = max(vw / mw, vh / mh)
    pw, ph = PLATE_W * scale, PLATE_H * scale
    cx, cy = vx + vw / 2.0, vy + vh / 2.0
    new = 'viewBox="%.3f %.3f %.3f %.3f"' % (cx - pw / 2.0, cy - ph / 2.0, pw, ph)
    txt = txt[:m.start()] + new + txt[m.end():]
    # Only the root <svg> tag: nested rect/image width+height are geometry.
    tag = re.search(r"<svg\b[^>]*>", txt)
    if tag:
        cleaned = re.sub(r'\s(?:width|height)="[^"]*"', "", tag.group(0))
        txt = txt[:tag.start()] + cleaned + txt[tag.end():]
    return txt.encode("utf-8"), (PLATE_W, PLATE_H)


# ---------------------------------------------------------------- source loaders

def from_artwork(fn, frac):
    im = Image.open(os.path.join(ART, fn)).convert("RGB")
    W, H = im.size
    crop = im.crop((int(frac[0] * W), int(frac[1] * H), int(frac[2] * W), int(frac[3] * H)))
    if max(crop.size) < 460:
        f = round(460 / max(crop.size)) or 2
        crop = crop.resize((crop.width * f, crop.height * f), Image.LANCZOS)
    return trim(defringe(key_local_bg(crop)))


def from_asset(fn):
    p = os.path.join(LIB, fn)
    if fn.lower().endswith(".svg"):
        return ("svg", open(p, "rb").read())
    im = Image.open(p)
    im.load()
    if im.mode == "P":
        im = im.convert("RGBA")
    if has_alpha(im):
        return trim(im.convert("RGBA"))
    return trim(defringe(key_flat_bg(im.convert("RGB"), "white")))


def from_web(fn):
    p = os.path.join(HERE, "_websrc", fn)
    if fn.lower().endswith(".svg"):
        return ("svg", open(p, "rb").read())
    im = Image.open(p)
    im.load()
    if im.mode == "P":
        im = im.convert("RGBA")
    if has_alpha(im):
        return trim(im.convert("RGBA"))
    return trim(defringe(key_flat_bg(im.convert("RGB"), "white")))


# ---------------------------------------------------------------- main

def main():
    os.makedirs(OUT, exist_ok=True)
    manifest, report = {}, []
    for slug, name, kind, ref in BRANDS:
        try:
            if kind == "artwork":
                data = from_artwork(ref[0], ref[1])
            elif kind == "asset":
                data = from_asset(ref)
            else:
                data = from_web(ref)
        except Exception as e:
            report.append("FAIL %-18s %s" % (slug, e))
            continue

        if isinstance(data, tuple) and data[0] == "svg":
            ext = "svg"
            fn = "%s.%s" % (slug, ext)
            plated, dims = plate_svg(data[1], name)
            with open(os.path.join(OUT, fn), "wb") as f:
                f.write(plated)
            manifest[name] = {"file": fn, "kind": "official", "src": kind,
                              "w": (dims or (0, 0))[0], "h": (dims or (0, 0))[1],
                              "lift": slug in SVG_LIFT,
                              "bytes": len(plated)}
            report.append("OK   %-18s svg   %10s  %s" % (name, len(plated), kind))
            continue

        data = cap(data)
        before = tile_contrast(data)
        data = plate(readable(trim(data)))
        after = tile_contrast(data)
        if before < CR_FLOOR:
            report.append("     %-18s contrast %.2f -> %.2f on the ink tile" % (name, before, after))
        fn = "%s.png" % slug
        data.save(os.path.join(OUT, fn), optimize=True)
        manifest[name] = {"file": fn, "kind": "official", "src": kind,
                          "w": data.width, "h": data.height,
                          "lift": False, "bytes": os.path.getsize(os.path.join(OUT, fn))}
        report.append("OK   %-18s png  %4dx%-4d %7s  %s" % (
            name, data.width, data.height, manifest[name]["bytes"], kind))

    keep = {v["file"] for v in manifest.values()} | {"manifest.json"}
    for stale in os.listdir(OUT):
        if stale not in keep and os.path.splitext(stale)[1] in (".png", ".jpg", ".svg", ".jpeg"):
            os.remove(os.path.join(OUT, stale))
            report.append("     purged stale %s" % stale)

    json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\n".join(report))
    print("\n%d brands, %d with a real mark" % (len(manifest),
          sum(1 for v in manifest.values() if v["kind"] == "official")))


if __name__ == "__main__":
    main()
