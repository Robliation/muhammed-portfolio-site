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

Cutting the marks is the part that decides whether the wall looks professional.
A soft key (distance from an estimated background, ramped into alpha) leaves a
15-29% haze of half-transparent background behind: on the dark ink tile it hides,
anywhere else it is obvious. So every source without real alpha goes through a
hard matte instead — a plane fitted to the crop's own border ring scores each
pixel on hue shift and brightness gain (the two things a shadow never has),
Otsu turns that into a binary mask, closing repairs it, flood fill drops debris,
and only then does one pixel of feather soften the rim. The mark's colour is
spread under the transparent area afterwards, because a browser blending a
downscaled PNG reads whatever RGB sits under alpha=0 — near-black from a
photograph would grey out thin strokes that are otherwise solid.

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
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))

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
#   upload  -> workspace-relative file the owner handed over ready-made
#   web     -> existing file already in assets/brands
BRANDS = [
    ("albaik",           "Al Baik",             "web",     "albaik.png"),
    ("almarai",          "Almarai",             "web",     "almarai.svg"),
    ("jarir",            "Jarir Bookstore",     "web",     "jarir.svg"),
    ("hungerstation",    "Hungerstation",       "web",     "hungerstation.svg"),
    ("gofood",           "GoFood",              "upload",  "sources/gofood-logo.png"),
    ("dubai",            "Dubai",               "web",     "dubai.svg"),
    ("indomie",          "Indomie",             "web",     "indomie.png"),
    ("shawarmer",        "Shawarmer",           "web",     "shawarmer.jpg"),
    ("qiddiya",          "Qiddiya",             "asset",   "Qiddiya_Logo.svg"),
    ("tazaj",            "Tazaj",               "asset",   "Al_Tazaj_logo.png"),
    ("marami",           "Marami",              "asset",   "Marami Logo.jpeg"),
    ("al-ulali",         "Al Ulali",            "upload",  "sources/al-ulali-official.png"),
    ("sadia",            "Sadia",               "asset",   "شعار ساديا.png"),
    ("aseer-time",       "Aseer Time",          "asset",   "شعار عصير تايم_upscayl_4x_upscayl-standard-4x.png"),
    ("burger-mish",      "Burger Mish",         "asset",   "شعار برجر مش_upscayl_2x_upscayl-standard-4x.png"),
    ("just-samboosa",    "Just Samboosa",       "asset",   "شعار جست سمبوسة_upscayl_4x_upscayl-standard-4x.png"),
    ("kayal",            "Kayal",               "asset",   "شعار مطعم خيال.png"),
    ("ful-wazir",        "Ful Al-Wazir",        "asset",   "شعار مطعم فول الوزير.png"),
    ("sultan-fish",      "Sultan Al-Samak",     "asset",   "شعار سلطان السمك_upscayl_4x_upscayl-standard-4x.png"),
    ("cake-house",       "The Cake House",      "asset",   "شعار مطعم بيت الكيك_upscayl_4x_upscayl-standard-4x.png"),
    ("notion",           "Notion",              "upload",  "sources/notion-logo.png"),
    ("al-adnan",         "Al Adnan",            "artwork", ("تصميم لمطعم العدنان (دوالي).jpg", (0.895, 0.000, 0.999, 0.130))),
    ("al-musafir",       "Al Musafir",          "artwork", ("تصميم لشركة المسافر (أستمتع بأكلك في أي مكان).jpg", (0.83523, 0.90495, 0.98011, 0.96094))),
    ("al-romansia",      "Al Romansia",         "artwork", ("تصميم لمطعم الرومانسية (مطعم المـــــــثـــــــالـــــــــــي).jpg", (0.890, 0.000, 0.999, 0.115))),
    ("al-yawm",          "Al Yawm",             "artwork", ("تصميم لشركة اليوم (تمشي مع اليوم).jpg", (0.4185, 0.2570, 0.5881, 0.3540))),
    ("bajah",            "Bajah",               "artwork", ("تصميم لشركة باجة (قهوة تمتع يومك).jpg", (0.860, 0.000, 0.994, 0.095))),
    ("berain",           "Berain",              "artwork", ("تصميم لشركة بيرين (ماء ثلج).jpg", (0.850, 0.005, 0.988, 0.125))),
    ("centrepoint",      "Centrepoint",         "artwork", ("تصميم لشركة سنتربوينت (شنطة سفرك في أمـــــــــــــــان).jpg", (0.872, 0.020, 0.985, 0.092))),
    ("country",          "Country Corn Flakes", "artwork", ("تصميم لشركة كونتري كورن فليكس (بروتين ينفع مع كورن فليكس).jpg", (0.834, 0.006, 0.990, 0.142))),
    ("falafel-burak",    "Falafel Burak",       "artwork", ("تصميم لشركة فلافل بوراك (عندنا فلافل صح) بالعرض.jpg", (0.868, 0.000, 0.998, 0.135))),
    ("jahez",            "Jahez",               "artwork", ("تصميم لشركة جاهز.jpg", (0.398, 0.000, 0.572, 0.095))),
    ("kinza",            "Kinza",               "artwork", ("تصميم لشركة كينزا (مشروب ينسيك العطش).jpg", (0.848, 0.000, 0.992, 0.095))),
    ("mazaaq",           "Mazaaq",              "artwork", ("تصميم لشركة مذاق بالعرض.png", (0.91797, 0.02539, 0.98225, 0.11133))),
    ("national-poultry", "National Poultry",    "artwork", ("تصميم لشركة دواجن الوطنية (مندي طيب مع دواجن الوطنية) بالعرض.jpg", (0.9512, 0.0115, 0.9943, 0.0585))),
    ("pizza-offers",     "Pizza Offers",        "artwork", ("تصميم لشركة عروض بيتزا بالعرض.png", (0.845, 0.000, 0.998, 0.128))),
    ("saudia",           "Saudia Cheese",       "artwork", ("تصميم لشركة السعودية (جبنة الملوك).jpg", (0.868, 0.000, 0.998, 0.135))),
    ("takohat",          "Takohat",             "artwork", ("تصميم لشركة تاكوهت (الأكلة تخليك توكل أصعابك).jpg", (0.028, 0.015, 0.185, 0.145))),
    ("vimto",            "Vimto",               "artwork", ("تصميم لشركة فيمتو (رمضان كريم).jpg", (0.868, 0.005, 0.992, 0.085))),
]

# Marks that read as a silhouette on the ink tile get a value lift in CSS instead
# of a raster re-encode (they stay vector).
SVG_LIFT = {"almarai", "hungerstation"}

# National Poultry's mark is only 233px wide in the source artwork, so its gold
# AL WATANIA POULTRY tagline is a few pixels tall and scores just under Otsu's
# split — the I was being erased. A ceiling on the threshold keeps the letters
# without admitting the pure-black field around them.
THR_CEIL = {"national-poultry": 40}


# ---------------------------------------------------------------- keying helpers

def has_alpha(im):
    if im.mode != "RGBA":
        return False
    lo, hi = im.getchannel("A").getextrema()
    return lo < 250


def solve3(m, v):
    """Gaussian elimination with partial pivoting on a 3x3 normal-equation system."""
    a = [row[:] + [v[i]] for i, row in enumerate(m)]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(a[r][i]))
        a[i], a[p] = a[p], a[i]
        if abs(a[i][i]) < 1e-9:
            return [v[0] / 3.0] * 3
        for r in range(3):
            if r != i:
                f = a[r][i] / a[i][i]
                for c in range(i, 4):
                    a[r][c] -= f * a[i][c]
    return [a[i][3] / a[i][i] for i in range(3)]


def plane_bg(rgb, band=6, step=2):
    """Least-squares plane fitted to the crop's border ring.

    Coordinates are centred and scaled to about [-0.5, 0.5] first: with raw pixel
    indices the normal matrix spans 1e3 to 1e9, the solve loses that much
    precision, and the resulting "background" is noise that hollows out every
    wide stroke it was supposed to sit under.
    """
    w, h = rgb.size
    r0, g0, b0 = rgb.split()
    px = (r0.load(), g0.load(), b0.load())
    pts = []
    for y in range(0, h, step):
        for x in range(0, w, step):
            if x < band or y < band or x >= w - band or y >= h - band:
                pts.append((x, y))
    if not pts:
        pts = [(0, 0), (w - 1, 0), (0, h - 1)]
    acc = [[0.0, 0.0, 0.0] for _ in range(3)]
    nu = nv = nuv = nu2 = nv2 = 0.0
    for x, y in pts:
        u = (x - w / 2.0) / w
        v = (y - h / 2.0) / h
        for i in range(3):
            p = px[i][x, y]
            acc[i][0] += p
            acc[i][1] += p * u
            acc[i][2] += p * v
        nu += u; nv += v; nuv += u * v; nu2 += u * u; nv2 += v * v
    n = float(len(pts))
    s = [[n, nu, nv], [nu, nu2, nuv], [nv, nuv, nv2]]
    coef = [solve3(s, acc[i]) for i in range(3)]
    out = Image.new("RGB", (64, 64))
    op = out.load()
    for j in range(64):
        v = ((j + 0.5) * h / 64.0 - h / 2.0) / h
        for k in range(64):
            u = ((k + 0.5) * w / 64.0 - w / 2.0) / w
            op[k, j] = tuple(max(0, min(255, int(c[0] + c[1] * u + c[2] * v))) for c in coef)
    return out.resize((w, h), Image.BILINEAR)


def score_map(rgb, bg, shadow_allow=70):
    """Evidence per pixel that it belongs to a mark rather than to the background
    it sits on or to a shadow that mark casts.

    Two things a real mark has and a drop shadow does not: a hue/saturation shift
    (chroma, which a shadow preserves) and a brightness *gain* (a shadow is a
    darkening). A genuinely dark mark on a light field still scores, once it
    darkens by more than the shadow_allow allowance.
    """
    r, g, b = rgb.split()
    br, bg_, bb = bg.split()
    c_rg = ImageChops.difference(ImageChops.difference(r, g), ImageChops.difference(br, bg_))
    c_rb = ImageChops.difference(ImageChops.difference(r, b), ImageChops.difference(br, bb))
    c_gb = ImageChops.difference(ImageChops.difference(g, b), ImageChops.difference(bg_, bb))
    chroma = ImageChops.lighter(ImageChops.lighter(c_rg, c_rb), c_gb)
    lp, lb = rgb.convert("L"), bg.convert("L")
    gain = ImageChops.subtract(lp, lb)
    loss = ImageChops.subtract(lb, lp).point(lambda p: max(0, p - shadow_allow))
    return ImageChops.lighter(ImageChops.lighter(chroma, gain), loss)


def otsu(hist):
    total = sum(hist)
    sum_all = float(sum(i * hist[i] for i in range(256)))
    best, bthr, w_b, sum_b = -1.0, 128, 0, 0.0
    for t in range(256):
        w_b += hist[t]
        if w_b == 0:
            continue
        w_f = total - w_b
        if w_f == 0:
            break
        sum_b += t * hist[t]
        var = w_b * w_f * (sum_b / w_b - (sum_all - sum_b) / w_f) ** 2
        if var > best:
            best, bthr = var, t
    return bthr


def components(mask, min_area):
    """Drop debris. Runs flood fill on a 4x-reduced grid.

    The relative bar is deliberately tiny. Aseer Time's roundel is one enormous blob
    ringed by letters, and the "I" in TIME is a bare 1,200 pixels next to it — at any
    percentage worth naming, the filter would file a real glyph under rubbish. Arabic
    dots and thin strokes are the same story: they are small because the mark is thin,
    not because they are noise, so min_area carries the cleanup and the ratio only
    catches fragments that are genuinely negligible."""
    w, h = mask.size
    sc = 4
    rw, rh = (w + sc - 1) // sc, (h + sc - 1) // sc
    small = mask.resize((rw, rh), Image.BILINEAR).point(lambda p: 255 if p > 90 else 0)
    px = small.load()
    seen = [[False] * rw for _ in range(rh)]
    lab = [[0] * rw for _ in range(rh)]
    nid, areas = 0, []
    for y in range(rh):
        for x in range(rw):
            if px[x, y] != 255 or seen[y][x]:
                continue
            nid += 1
            stack, area = [(x, y)], 0
            seen[y][x] = True
            while stack:
                cx, cy = stack.pop()
                area += 1
                lab[cy][cx] = nid
                for nx, ny in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
                    if 0 <= nx < rw and 0 <= ny < rh and not seen[ny][nx] and px[nx, ny] == 255:
                        seen[ny][nx] = True
                        stack.append((nx, ny))
            areas.append(area)
    if not areas:
        return mask
    biggest = max(areas)
    keep = set(i + 1 for i, a in enumerate(areas)
               if a * sc * sc >= min_area and a >= biggest * 0.002)
    if not keep:
        keep = {areas.index(biggest) + 1}
    out = Image.new("L", (rw, rh), 0)
    op = out.load()
    for y in range(rh):
        for x in range(rw):
            if lab[y][x] in keep:
                op[x, y] = 255
    return out.resize((w, h), Image.BILINEAR).point(lambda p: 255 if p > 100 else 0)


def spread(rgb, alpha, iters=10, rad=3.0):
    """Push the mark's own colour out under the transparent area.

    A cutout keeps whatever RGB sat under its alpha=0 pixels, which for a mark
    lifted off a photograph is near-black. Browsers blend that black in when they
    scale the PNG down, so thin strokes turn grey in the tile even though every
    one of their own pixels is solid. After this, downscaling blends mark with
    mark.
    """
    cur = rgb
    for _ in range(iters):
        cur = Image.composite(cur, cur.filter(ImageFilter.GaussianBlur(rad)), alpha)
    return cur


def hard_cut(rgb, floor=52, min_area=260, thr_ceil=None):
    """Return an RGBA mark: interior fully opaque, exterior fully transparent,
    one anti-aliased pixel between. No haze, no shadow, no background."""
    bg = plane_bg(rgb)
    s = score_map(rgb, bg)
    thr = max(otsu(s.histogram()), floor)
    if thr_ceil is not None:
        thr = min(thr, thr_ceil)
    mask = s.point(lambda p: 255 if p >= thr else 0)
    # closing, never opening: an opening severs thin calligraphy, and Arabic
    # wordmarks are nothing but thin calligraphy.
    mask = mask.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
    mask = components(mask, min_area)
    if mask.getbbox() is None:
        return rgb.convert("RGBA")
    alpha = mask.filter(ImageFilter.GaussianBlur(0.7))
    alpha = alpha.point(lambda p: 0 if p < 30 else (255 if p > 128 else int(p * 255 / 128)))
    out = spread(rgb, alpha).convert("RGBA")
    out.putalpha(alpha)
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


MIN_LUM = 0.116          # the darkest a mark's own pixel may be: 3:1 on the ink tile


def floor_lum(im, target=MIN_LUM):
    """Give every mark pixel enough light that the ink tile cannot swallow it.

    Cutting faithfully is only half the job. Sadia's black S, Sultan Al-Samak's navy
    lockup, Just Samboosa's script, Ful Al-Wazir's brown: lifted off a light source
    exactly as the brand draws them, they are precisely the pixels a dark tile
    erases, and a mark that reads as half a word looks like a broken image. So add
    the missing luminance to the pixels that have too little of it and leave the
    rest alone. Hue and the contrast *inside* the mark survive; only the floor moves.
    """
    r, g, b, a = im.split()
    rp, gp, bp, ap = r.load(), g.load(), b.load(), a.load()
    for y in range(im.height):
        for x in range(im.width):
            if ap[x, y] < 160:
                continue
            lin = [_lin(rp[x, y]), _lin(gp[x, y]), _lin(bp[x, y])]
            cur = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
            if cur >= target:
                continue
            d = target - cur
            for i, band in enumerate((rp, gp, bp)):
                v = min(1.0, lin[i] + d)
                s = v * 12.92 if v <= 0.0031308 else 1.055 * (v ** (1 / 2.4)) - 0.055
                band[x, y] = max(0, min(255, int(round(s * 255))))
    return Image.merge("RGBA", (r, g, b, a))


def premul_resize(im, tw, th):
    """Scale through premultiplied alpha.

    Pillow blends straight RGBA, so a thin white stroke shrunk into a tile picks
    up the colour of the transparent pixels either side of it and turns grey —
    which is exactly how a clean cut ends up looking hollow. Premultiply, scale,
    then divide back out and the stroke blends only with itself.
    """
    tw, th = max(1, tw), max(1, th)
    r, g, b, a = im.split()
    na = a.resize((tw, th), Image.LANCZOS)
    nap = na.load()
    bands = []
    for c in (r, g, b):
        pm = ImageChops.multiply(c, a).resize((tw, th), Image.LANCZOS).load()
        band = Image.new("L", (tw, th))
        bp = band.load()
        for y in range(th):
            for x in range(tw):
                al = nap[x, y]
                bp[x, y] = 255 if al == 0 else min(255, pm[x, y] * 255 // al)
        bands.append(band)
    out = Image.merge("RGB", bands)
    out.putalpha(na)
    return out


def cap(im, edge=760):
    if max(im.size) > edge:
        f = edge / max(im.size)
        im = premul_resize(im, int(im.width * f), int(im.height * f))
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
    scaled = premul_resize(im, int(round(mw)), int(round(mh)))
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

def from_artwork(fn, frac, slug=None):
    im = Image.open(os.path.join(ART, fn)).convert("RGB")
    W, H = im.size
    crop = im.crop((int(frac[0] * W), int(frac[1] * H), int(frac[2] * W), int(frac[3] * H)))
    if max(crop.size) < 1200:                       # thin calligraphy needs pixels to survive the matte
        f = round(1200 / max(crop.size)) or 2
        crop = crop.resize((crop.width * f, crop.height * f), Image.LANCZOS)
    return trim(hard_cut(crop, thr_ceil=THR_CEIL.get(slug)))


def _from_file(p, slug=None):
    if p.lower().endswith(".svg"):
        return ("svg", open(p, "rb").read())
    im = Image.open(p)
    im.load()
    if im.mode == "P":
        im = im.convert("RGBA")
    if has_alpha(im):                               # already a real cutout — trust its own alpha
        return trim(im.convert("RGBA"))
    rgb = im.convert("RGB")
    if max(rgb.size) < 1200:
        f = round(1200 / max(rgb.size)) or 2
        rgb = rgb.resize((rgb.width * f, rgb.height * f), Image.LANCZOS)
    return trim(hard_cut(rgb, thr_ceil=THR_CEIL.get(slug)))


def from_asset(fn, slug=None):
    return _from_file(os.path.join(LIB, fn), slug)


def from_upload(rel, slug=None):
    return _from_file(os.path.join(ROOT, *rel.split("/")), slug)


def from_web(fn, slug=None):
    return _from_file(os.path.join(HERE, "_websrc", fn), slug)


# ---------------------------------------------------------------- main

def main():
    os.makedirs(OUT, exist_ok=True)
    manifest, report = {}, []
    for slug, name, kind, ref in BRANDS:
        try:
            if kind == "artwork":
                data = from_artwork(ref[0], ref[1], slug)
            elif kind == "upload":
                data = from_upload(ref, slug)
            elif kind == "asset":
                data = from_asset(ref, slug)
            else:
                data = from_web(ref, slug)
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
        data = floor_lum(plate(trim(data)))
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
