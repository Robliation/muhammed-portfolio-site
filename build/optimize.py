# -*- coding: utf-8 -*-
"""Web asset pipeline: strip metadata, emit responsive JPEG + WebP at two sizes."""
import os, json, io, sys
from PIL import Image, ImageOps

SRC = r"C:\Users\M Deisgner\Pictures\Pictures Photoshop\Designs"
LOGO_SRC = r"C:\Users\M Deisgner\Pictures\Pictures illustrator\Wallpapers & Profiles"
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.getcwd(), "site")
FULL_LONG, THUMB_LONG = 1720, 720
FULL_Q, THUMB_Q = 82, 78
FULL_WEBP, THUMB_WEBP = 80, 76

man = json.load(open("manifest.json", encoding="utf-8"))
os.makedirs(os.path.join(OUT, "assets", "img"), exist_ok=True)


def emit(im, base, long_edge, q, wq):
    """Write base.jpg + base.webp, downscaled so the long edge <= long_edge."""
    im = ImageOps.exif_transpose(im)
    w, h = im.size
    scale = min(1.0, long_edge / max(w, h))
    if scale < 1.0:
        im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
    rgb = im.convert("RGB")
    rgb.save(base + ".jpg", "JPEG", quality=q, optimize=True, progressive=True)
    rgb.save(base + ".webp", "WebP", quality=wq, method=6, optimize=True)
    return rgb.size


def load(name):
    im = Image.open(os.path.join(SRC, name))
    im = ImageOps.exif_transpose(im)
    im.format = None  # drop source format so nothing leaks into output
    return im


assets = {}
for work in man["works"]:
    entries = []
    for i, img in enumerate(work["images"]):
        stem = os.path.join(OUT, "assets", "img", f'{work["id"]}-{i}')
        im = load(img["file"])
        fw, fh = emit(im, stem, FULL_LONG, FULL_Q, FULL_WEBP)
        tw, th = emit(im, stem + "-thumb", THUMB_LONG, THUMB_Q, THUMB_WEBP)
        entries.append({
            "src": img["file"], "full": f'assets/img/{work["id"]}-{i}',
            "thumb": f'assets/img/{work["id"]}-{i}-thumb',
            "full_w": fw, "full_h": fh, "thumb_w": tw, "thumb_h": th,
            "orig_w": img["w"], "orig_h": img["h"], "orient": img["orient"],
            "year": img["year"], "date": img["date"],
            "kb": {k: round(os.path.getsize(stem + "." + k) / 1024, 1) for k in ("jpg", "webp")},
            "kb_thumb": {k: round(os.path.getsize(stem + "-thumb." + k) / 1024, 1) for k in ("jpg", "webp")},
        })
    assets[work["id"]] = entries
    print(f'{work["id"]:<38} {len(entries)} fmt  full {entries[0]["kb"]}  thumb {entries[0]["kb_thumb"]}')

json.dump(assets, open("assets.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# --- personal logo lockups (transparent, trimmed, recoloured from the blue originals) ---
os.makedirs(os.path.join(OUT, "assets", "brand"), exist_ok=True)
BLUE = (40, 107, 248)  # #286BF8, sampled from the source artwork
VARIANTS = {"blue": BLUE, "white": (255, 255, 255), "ink": (17, 19, 24)}
SOURCES = {"lockup": "موقع شعار بس كل الأوان أزرق M Designer.png", "mark": "أزرق موقع شعار M-01.png"}


def recolour(path, colour, max_px=1200):
    im = Image.open(path).convert("RGBA")
    r, g, b, a = im.split()
    solid = Image.new("RGBA", im.size, colour + (255,))
    out = Image.composite(solid, Image.new("RGBA", im.size, (0, 0, 0, 0)), a)
    box = a.getbbox()
    if box:
        pad = 12
        box = (max(0, box[0] - pad), max(0, box[1] - pad), min(im.size[0], box[2] + pad), min(im.size[1], box[3] + pad))
        out = out.crop(box)
    out.thumbnail((max_px, max_px), Image.LANCZOS)
    return out


for kind, fname in SOURCES.items():
    for name, colour in VARIANTS.items():
        img = recolour(os.path.join(LOGO_SRC, fname), colour, 1400 if kind == "lockup" else 900)
        p = os.path.join(OUT, "assets", "brand", f"m-{kind}-{name}.png")
        img.save(p, "PNG", optimize=True)
        print(f"logo m-{kind}-{name}", img.size, round(os.path.getsize(p) / 1024, 1), "KB")

favicon = recolour(os.path.join(LOGO_SRC, SOURCES["mark"]), BLUE, 96)
favicon.save(os.path.join(OUT, "assets", "brand", "favicon.png"), "PNG", optimize=True)

total = 0
for root, _, fs in os.walk(OUT):
    for f in fs:
        total += os.path.getsize(os.path.join(root, f))
print("TOTAL site bytes:", round(total / 1e6, 1), "MB")
