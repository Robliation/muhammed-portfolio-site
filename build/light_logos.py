# -*- coding: utf-8 -*-
"""Emit light-plate variants of the client logos.

Some client logos are drawn in white ink (Jahez, Kinza, Mazaaq, Vimto, Berain and
others), which is why the dark stage was originally used behind them. On the CV
work ledger the owner wants light plates, so this step maps near-white ink to the
site ink colour while leaving every coloured pixel untouched. Shapes, letterforms
and brand colours are preserved; only white ink is darkened, which is the
standard mono-on-light treatment for a logo wall.

Output: assets/brands/light/<file>.png
A brand without a light variant simply falls back to the original file.
"""
import json, os
import colorsys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, ".."))
BRANDS = os.path.join(OUT, "assets", "brands")
LIGHT = os.path.join(BRANDS, "light")

INK = (14, 17, 22)          # --ink
MIN_CHANNEL = 168           # a pixel this light in every channel reads as "white ink"
MAX_SAT = 0.30              # ...as long as it is nearly neutral
MIN_ALPHA = 10

# Artwork whose white area is a container, not ink: darkening it would turn the
# logo into a solid block. Kept on their original colours (they read fine on white).
CONTAINER_ART = {"indomie.png"}

# Only artwork that is *mostly* white ink needs the treatment. Logos with a strong
# coloured core (Tazaj, GoFood, Al Ulali, Country, National Poultry, Falafel Burak,
# Al Yawm) already read on a light plate and keep their original colours.
MIN_FRAC = 0.45

os.makedirs(LIGHT, exist_ok=True)
man = json.load(open(os.path.join(BRANDS, "manifest.json"), encoding="utf-8"))

made, skipped = [], []
for name, m in man.items():
    f = m["file"]
    if not f.lower().endswith(".png"):
        continue
    src = os.path.join(BRANDS, f)
    im = Image.open(src).convert("RGBA")
    px = im.load()
    touched = 0
    opaque = 0
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a < MIN_ALPHA:
                continue
            opaque += 1
            mn = min(r, g, b)
            if mn < MIN_CHANNEL:
                continue
            _h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            if s > MAX_SAT:
                continue
            px[x, y] = (INK[0], INK[1], INK[2], a)
            touched += 1
    frac = touched / max(opaque, 1)
    if touched == 0 or frac < MIN_FRAC or f in CONTAINER_ART:
        skipped.append((name, round(frac, 3)))
        continue
    im.save(os.path.join(LIGHT, f), "PNG", optimize=True)
    made.append((name, round(frac, 3)))

print("light variants:", len(made), "| kept original:", len(skipped))
print("made:", ", ".join(f"{n} {p}" for n, p in made))
print("kept:", ", ".join(f"{n} {p}" for n, p in skipped))
