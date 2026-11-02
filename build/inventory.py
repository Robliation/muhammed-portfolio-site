import os, json
from PIL import Image, ExifTags
ROOT = r"C:\Users\M Deisgner\Pictures\Pictures Photoshop"
out = []
for sub in ["Designs", "Logos", "Others"]:
    d = os.path.join(ROOT, sub)
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        if not os.path.isfile(p): continue
        ext = os.path.splitext(name)[1].lower()
        rec = {"folder": sub, "file": name, "bytes": os.path.getsize(p)}
        if ext in (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"):
            try:
                with Image.open(p) as im:
                    rec["w"], rec["h"] = im.size
                    rec["mode"] = im.mode
                    rec["fmt"] = im.format
                    rec["ratio"] = round(im.size[0] / im.size[1], 3)
            except Exception as e:
                rec["err"] = str(e)
        out.append(rec)
json.dump(out, open(os.path.join(ROOT, "..", "..", "Documents", "muhammed portifolo site", "_work", "inventory.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "files")
for r in out:
    if r["folder"] == "Designs":
        orient = "portrait" if r.get("ratio", 1) < 0.95 else ("landscape" if r.get("ratio", 1) > 1.05 else "square")
        print(f'{r.get("w","-")}x{r.get("h","-"):>5} {r["ratio"] if "ratio" in r else "-":>7} {orient:>9} {r["bytes"]/1e6:6.2f}MB  {r["file"]}')
