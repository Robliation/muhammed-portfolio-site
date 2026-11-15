# -*- coding: utf-8 -*-
"""Canonical work list: every design, grouped by client sector.

Sources are resolved BY NAME, never by a list index: adding, renaming or
sorting files in the Designs library can no longer silently re-point an
existing work at the wrong artwork. A source carrying a slash is a
workspace-relative finished file (sources/...); anything else is a filename
inside the Designs library.
"""
import os, json, datetime
from PIL import Image

SRC = r"C:\\Users\\M Deisgner\\Pictures\\Pictures Photoshop\\Designs"
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

CATS = {
    "restaurants": ("Restaurants & food", "مطاعم وأغذية"),
    "apps": ("Apps & ordering", "تطبيقات وطلبات"),
    "dairy": ("Dairy & cheese", "ألبان وأجبان"),
    "drinks": ("Drinks & juices", "مشروبات وعصائر"),
    "fmcg": ("FMCG & grocery", "سلع استهلاكية"),
    "retail": ("Retail & tech", "تجزئة وتقنية"),
    "travel": ("Tourism & places", "سياحة وأماكن"),
    "seasonal": ("Ramadan & Eid", "مواسم ورمضان"),
    "concept": ("Concept & experimental", "مفاهيم تجريبية"),
}

# Behance galleries by work id, only where a published gallery exists.
BEHANCE = {
    "albaik-love-of-the-years": 225611763,
    "tazaj-crazy-taste": 229800805,
    "al-musafir-eat-anywhere": 221799605,
    "almarai-labneh-worries": 222872961,
    "almarai-labneh-heart": 221496423,
    "indomie-other-world": 221449035,
    "almarai-strawberry-milk": 221261353,
    "almarai-respectable-laban": 229800671,
    "kinza-cola-splash": 225431617,
    "bajah-coffee-day": 221889365,
    "jarir-cook-in-comfort": 221360445,
    "jarir-eid-mubarak": 222550607,
}
BEHANCE_SLUG = {
    221261353: "-(-)",
    221360445: "-(-)",
    221449035: "-(-)",
    221496423: "-(-)",
    221799605: "-(-)",
    221889365: "-(-)",
    222550607: "-(-)",
    222872961: "-(-)",
    225431617: "Kinza-cola-Design",
    225611763: "Design-about-ALBAIK",
    229800671: "-(-)",
    229800805: "-(-)",
}

# (slug, brand_en, brand_ar, tagline_ar, tagline_en, category, [sources])
W = [
    # --- Restaurants & food
    ("albaik-crispy-chicken", "Al Baik", "البيك", "دجاج Crispy", "Crispy chicken, square", "restaurants", ["تصميم لشركة بيك (Crispy دجاج) مربع.jpg"]),
    ("albaik-best-with-us", "Al Baik", "البيك", "الأفضل لك عندنا", "The best for you is with us", "restaurants", ["تصميم لشركة بيك (الأفضل لك عنـــــــــــدنا) بالعرض.jpg", "تصميم لشركة بيك (الأفضل لك عنـــــــــــدنا) بالطولpsd.jpg"]),
    ("albaik-love-of-the-years", "Al Baik", "البيك", "البيك حب السنين", "Al Baik, the love of the years", "restaurants", ["تصميم لمطعم البيك (البيك حب السنين).jpg"]),
    ("tazaj-crazy-taste", "Tazaj", "الطازج", "طعم بجنن", "A crazy-good taste", "restaurants", ["تصميم لمطعم الطازج ( طعم بجنن).jpg"]),
    ("tazaj-city-of-crispy", "Tazaj", "الطازج", "TAZAJ", "TAZAJ — city of crispy", "restaurants", ["تصميم لمطعم الطازج (TAZAJ).jpg"]),
    ("tazaj-changes-your-mood", "Tazaj", "الطازج", "الطازج يغير مزاجك", "Tazaj changes your mood", "restaurants", ["تصميم لمطعم الطازج (الطازج يغير مزاجك) بالعرض.jpg", "تصميم لمطعم الطازج (الطازج يغير مزاجك) بالطول.jpg"]),
    ("shawarmer-different", "Shawarmer", "شاورمر", "شاورما غير", "A different shawarma", "restaurants", ["تصميم لشركة شاورمر (شاورما غير).jpg"]),
    ("shawarmer-golden", "Shawarmer", "شاورمر", "لا تفوت الشاورما الذهبية", "Don't miss the golden shawarma", "restaurants", ["تصميم لشركة شاورمر (لا تفوت الشاورما الذهبية).jpg"]),
    ("takohat-forget-your-troubles", "Takohat", "تاكوهت", "الأكلة تخليك توكل أصعابك", "The meal that makes you forget your troubles", "restaurants", ["تصميم لشركة تاكوهت (الأكلة تخليك توكل أصعابك) بالطول.jpg", "تصميم لشركة تاكوهت (الأكلة تخليك توكل أصعابك).jpg"]),
    ("just-samboosa-authentic", "Just Samboosa", "جست سمبوسة", "على أصولها متعة مالها حدود", "The authentic way, boundless enjoyment", "restaurants", ["تصميم لشركة جست سمبوسة (على أصولها متعة مالها حدود).png"]),
    ("just-samboosa-mindblown", "Just Samboosa", "جست سمبوسة", "سمبوسة هتجنن عقلك", "Samosa that blows your mind", "restaurants", ["تصميم لمطعم جست سمبوسة (سمبوسة هتجنن عقلك).jpg"]),
    ("falafel-burak-done-right", "Falafel Burak", "فلافل بوراك", "عندنا فلافل صح", "We make falafel right", "restaurants", ["تصميم لشركة فلافل بوراك (عندنا فلافل صح) بالطول.jpg", "تصميم لشركة فلافل بوراك (عندنا فلافل صح) بالعرض.jpg"]),
    ("al-yawm-goes-with-your-day", "Al Yawm", "اليوم", "تمشي مع اليوم", "Goes with your day", "restaurants", ["تصميم لشركة اليوم (تمشي مع اليوم).jpg"]),
    ("al-adnan-dawali", "Al Adnan", "العدنان", "دوالي", "Dawali — stuffed vine leaves", "restaurants", ["تصميم لمطعم العدنان (دوالي).jpg"]),
    ("burger-mish-best-in-world", "Burger Mish", "برجر مش", "أفضل برجر في العالم", "The best burger in the world", "restaurants", ["تصميم لمطعم برجر مش (أفضل برجر في العالم).jpg"]),
    ("the-cake-house-makes-your-day", "The Cake House", "بيت الكيك", "كيك يصنع يومك", "Cake that makes your day", "restaurants", ["تصميم لمطعم بيت الكيك (كيك يصنع يومك).jpg"]),
    ("kayal-kunafa", "Kayal", "خيال", "كنافة فوق الخيال", "Kunafa beyond imagination", "restaurants", ["تصميم لمطعم خيال (كنافة فوق الخيال).jpg"]),
    ("kayal-al-tawool", "Kayal", "خيال", "الطول يفرق", "Length makes the difference", "restaurants", ["sources/khayal-al-tawool.png"]),
    ("sultan-fish-crispy", "Sultan Al-Samak", "سلطان السمك", "سمك مقرمش", "Crispy fish", "restaurants", ["تصميم لمطعم سلطان السمك (سمك مقرمش).jpg"]),
    ("ful-wazir-exceptional", "Ful Al-Wazir", "فول الوزير", "فول حقنا متميز", "Our ful is exceptional", "restaurants", ["تصميم لمطعم فول الوزير (فول حقنا متميز).jpg"]),
    ("romansia-ideal-restaurant", "Al Romansia", "الرومانسية", "مطعم المثالي", "The ideal restaurant", "restaurants", ["تصميم لمطعم الرومانسية (مطعم المـــــــثـــــــالـــــــــــي).jpg"]),
    ("mazaaq-irresistible-burger", "Mazaaq", "مذاق", "البرجر المثالي لا يقاوم", "The perfect burger is irresistible", "restaurants", ["تصميم لشركة مذاق بالطول.png", "تصميم لشركة مذاق بالعرض.png"]),
    ("pizza-offers-beyond-imagination", "Pizza Offers", "عروض بيتزا", "بيتزا فوق الخيال", "Pizza beyond imagination", "restaurants", ["تصميم لشركة عروض بيتزا بالطول.png", "تصميم لشركة عروض بيتزا بالعرض.png"]),
    # --- Apps & ordering
    ("jahez-delivery-flies", "Jahez", "جاهز", "توصيلنا مثل الطيارة", "Our delivery flies like a plane", "apps", ["تصميم لشركة جاهز (توصيلنا مثل الطيارة) بالطول.jpg", "تصميم لشركة جاهز (توصيلنا مثل الطيارة).jpg"]),
    ("jahez-pizza-feast", "Jahez", "جاهز", "عروض بيتزا", "Floating pizza feast", "apps", ["تصميم لشركة جاهز.jpg"]),
    ("hungerstation-legendary-speed", "Hungerstation", "هنقرستيشن", "سرعة خرافية", "Legendary speed", "apps", ["تصميم لشركة هنقرستيشن (سرعة خرافية).jpg"]),
    ("gofood-at-your-door", "GoFood", "جوفود", "طلبك على الباب", "Your order at your door", "apps", ["sources/gofood-at-your-door.png"]),
    ("notion-arrab-afkarak", "Notion", "نوتشن", "رتب أفكارك", "Get your ideas in order", "apps", ["sources/notion-arrab-afkarak.png"]),
    # --- Dairy & cheese
    ("almarai-all-vitamins", "Almarai", "المراعي", "حليب كلو فيتامينات", "Milk, all vitamins", "dairy", ["(تصميم لشركة المراعي (حليب كلو فيتامينات.jpg"]),
    ("almarai-labneh-worries", "Almarai", "المراعي", "لبنة المراعي تنسيك همك", "Labneh that makes you forget your worries", "dairy", ["تصميم لشركة المراعي (لبنة المراعي تنسيك همك).jpg"]),
    ("almarai-labneh-heart", "Almarai", "المراعي", "لبنة يحبو قلبك", "A labneh your heart loves", "dairy", ["تصميم لشركة المراعي (لبنة يحبو قلبك).jpg"]),
    ("almarai-irresistible-taste", "Almarai", "المراعي", "مذاق لا يقاوم", "An irresistible taste", "dairy", ["تصميم لشركة المراعي (مذاق لا يقاوم).jpg"]),
    ("almarai-chocolate-milk", "Almarai", "المراعي", "حليب شوكولاتة", "Chocolate milk", "dairy", ["تصميم لشركة المراعي لحليب شوكولاتة_upscayl_4x_upscayl-standard-4x.png"]),
    ("saudia-cheese-of-kings", "Saudia Cheese", "السعودية", "جبنة الملوك", "Cheese of kings", "dairy", ["تصميم لشركة السعودية (جبنة الملوك).jpg"]),
    ("almarai-strawberry-milk", "Almarai", "المراعي", "حليب المراعي غير", "Almarai milk is different", "dairy", ["تصميم لشركة المراعي (حليب المراعي غيــــــــــــــر) بالطول.jpg", "تصميم لشركة مراعي (حليب المراعي غيــــــــــــــر) بالعرض.jpg"]),
    ("almarai-respectable-laban", "Almarai", "المراعي", "لبن محترم", "Respectable laban", "dairy", ["تصميم لشركة المراعي (لبن محترم).jpg"]),
    # --- Drinks & juices
    ("almarai-different-juices", "Almarai", "المراعي", "عصائر المراعي غير", "Almarai juices are different", "drinks", ["تصميم لشركة المراعي (عصائر المراعي غيـــــــــــر) بالطول.jpg", "تصميم لشركة المراعي (عصائر المراعي غيـــــــــــر) بالعرض.jpg"]),
    ("kinza-cola-splash", "Kinza", "كينزا", "كينزا كولا", "Kinza Cola", "drinks", ["تصميم لشركة كينزا_upscayl_4x_upscayl-standard-4x.png"]),
    ("kinza-forget-thirst", "Kinza", "كينزا", "مشروب ينسيك العطش", "A drink that makes you forget thirst", "drinks", ["تصميم لشركة كينزا (مشروب ينسيك العطش).jpg"]),
    ("berain-ice-water", "Berain", "بيرين", "ماء ثلج", "Ice water", "drinks", ["تصميم لشركة بيرين (ماء ثلج).jpg"]),
    ("bajah-coffee-day", "Bajah", "باجة", "قهوة تمتع يومك", "Coffee that makes your day", "drinks", ["تصميم لشركة باجة (قهوة تمتع يومك).jpg"]),
    ("aseer-time-flavour", "Aseer Time", "عصير تايم", "استمتع بالنكهة", "Enjoy the flavour", "drinks", ["تصميم لشركة عصير تايم (استمتع بلنكهــــــة).jpg"]),
    ("aseer-time-indulge", "Aseer Time", "عصير تايم", "تمتع", "Indulge", "drinks", ["تصميم لشركة عصير تايم (تمتع).jpg"]),
    ("aseer-time-real-refresh", "Aseer Time", "عصير تايم", "الانتعاش الحقيقي يسرسح على قلبك", "The real refreshment that swooshes your heart", "drinks", ["تصميم لشركة عصير تايم (الانتعاش الحقيقي يسرسح على قلبك).png"]),
    # --- FMCG & grocery
    ("national-poultry-mandi", "National Poultry", "دواجن الوطنية", "مندي طيب مع دواجن الوطنية", "Tayyib mandi with National Poultry", "fmcg", ["تصميم لشركة دواجن الوطنية (مندي طيب مع دواجن الوطنية) بالعرض.jpg", "تصميم لشركة دواجن الوطنية (مندي طيب مع دواجن الوطنية) بالطول.jpg"]),
    ("almarai-royal-hummus", "Almarai", "المراعي", "حمص ملكي", "Royal hummus", "fmcg", ["تصميم لشركة المراعي (حمص ملكي).jpg"]),
    ("almarai-mood-car", "Almarai", "المراعي", "تمشي مزاجك", "Moves with your mood", "fmcg", ["تصميم لشركة المراعي (تمشي مزاجك).jpg"]),
    ("al-ulali-no-other-taste", "Al Ulali", "العلالي", "طعم ولا أحلى", "A taste like no other", "fmcg", ["(..تصميم لشركة العلالي (طعم ولا احلا.jpg"]),
    ("al-ulali-for-the-ones-who-matter", "Al Ulali", "العلالي", "لأنها للغالي", "For the ones who matter", "fmcg", ["sources/al-ulali-for-the-ones-who-matter.png"]),
    ("indomie-other-world", "Indomie", "إندومي", "عالم غير", "A whole other world", "fmcg", ["تصميم لشركة إندومي (عالم غير).jpg"]),
    ("marami-different-chips", "Marami", "مرامي", "شبس حقنا غير", "Our chips are different", "fmcg", ["تصميم لشركة مرامي (شبس حقنا غيــــــــــــر).jpg"]),
    ("sadia-field-fry", "Sadia", "ساديا", "طلعة ممتعة مع ساديا", "A delightful outing with Sadia", "fmcg", ["تصميم لشركة ساديا (طلعة ممتعة مع ساديا).jpg"]),
    ("country-cornflakes-protein", "Country Corn Flakes", "كونتري", "بروتين ينفع مع كورن فليكس", "Protein that works with corn flakes", "fmcg", ["تصميم لشركة كونتري كورن فليكس (بروتين ينفع مع كورن فليكس).jpg"]),
    ("almarai-real-watermelon", "Almarai", "المراعي", "بطيخ أصلي", "Real watermelon", "fmcg", ["تصميم لشركة المراعي (بطيخ أصلي).jpg"]),
    # --- Retail & tech
    ("jarir-best-devices", "Jarir Bookstore", "مكتبة جرير", "أفضل أجهزة عندنا", "The best devices are with us", "retail", ["تصميم لشركة مكتبة جرير (أفضل أجهزة عندنــــــــــــــــــــــا) بالعرض.jpg", "تصميم لشركة مكتبة جرير (أفضل أجهزة عندنــــــــــــــــــــــا) بالطول.jpg"]),
    ("jarir-cook-in-comfort", "Jarir Bookstore", "مكتبة جرير", "اطبخ وأنت مرتاح", "Cook in comfort", "retail", ["تصميم لشركة مكتبة جرير (أطبخ وأنتا مرتــــــــــــاح).jpg"]),
    ("jarir-safety-backpack", "Jarir Bookstore", "مكتبة جرير", "شنطة أمان لا تفوتك", "A safety backpack you can't miss", "retail", ["تصميم لشركة مكتبة جرير (شنطة أمان لا تفوتك).jpg"]),
    ("centrepoint-travel-bag", "Centrepoint", "سنتربوينت", "شنطة سفرك في أمان", "Your travel bag is safe", "retail", ["تصميم لشركة سنتربوينت (شنطة سفرك في أمـــــــــــــــان).jpg"]),
    # --- Tourism & places
    ("al-musafir-eat-anywhere", "Al Musafir", "المسافر", "أستمتع بأكلك في أي مكان", "Enjoy your meal anywhere", "travel", ["تصميم لشركة المسافر (أستمتع بأكلك في أي مكان).jpg"]),
    ("qiddiya-best-tourism-city", "Qiddiya", "القدية", "الأفضل مدينة سياحة", "The best city of tourism", "travel", ["تصميم لشركة القدية (الأفضل مدينة ســـــــــــياحـــــــــــــة) بالطول.jpg", "تصميم لشركة القدية (الأفضل مدينة ســـــــــــياحـــــــــــــة) بالعرض.jpg"]),
    ("dubai-enjoy-the-vibe", "Dubai", "دبي", "أستمتع بأجواء دبي", "Enjoy the vibe of Dubai", "travel", ["تصميم لشركة دبي (أستمتع بأجواء دبي).jpg"]),
    ("dubai-present-meets-future", "Dubai", "دبي", "دبي حيث يلتقي الحاضر بالمستقبل", "Dubai, where the present meets the future", "travel", ["تصميم لشركة دبي (دبي حيث يلتقي الحاضر بالمستقبل).jpg"]),
    # --- Ramadan & Eid
    ("almarai-ramadan-kareem", "Almarai", "المراعي", "رمضان كريم", "Ramadan Kareem", "seasonal", ["تصميم لشركة المراعي (رمضان كريم).jpg"]),
    ("sadia-ramadan-offers", "Sadia", "ساديا", "عروض رمضان", "Ramadan offers", "seasonal", ["تصميم لشركة ساديا (عروض رمضان).jpg"]),
    ("vimto-ramadan-kareem", "Vimto", "فيمتو", "رمضان كريم", "Ramadan Kareem", "seasonal", ["تصميم لشركة فيمتو (رمضان كريم).jpg"]),
    ("jarir-eid-mubarak", "Jarir Bookstore", "مكتبة جرير", "عيد مبارك علينا وعليكم", "Blessed Eid to us and you", "seasonal", ["تصميم لشركة مكتبة جرير (أستمتع بعروض عيد مبارك علينا وعليكم).jpg"]),
    # --- Concept & experimental
    ("concept-hummus", "Self-initiated", "ذاتي", "تصميم حمص", "Hummus concept ad", "concept", ["تصميم حمص.jpg"]),
    ("concept-perfume", "Self-initiated", "ذاتي", "تصميم عطر", "Perfume concept ad", "concept", ["تصميم عطر.jpg"]),
]


def resolve(src):
    return os.path.join(ROOT, src) if "/" in src else os.path.join(SRC, src)


works, seen_slugs, seen_files, missing = [], set(), {}, []
for slug, ben, bar, tar, ten, cat, srcs in W:
    if slug in seen_slugs:
        raise SystemExit("duplicate work id: " + slug)
    if cat not in CATS:
        raise SystemExit("unknown category %r on work %s" % (cat, slug))
    seen_slugs.add(slug)
    imgs = []
    for s in srcs:
        if s in seen_files:
            raise SystemExit("source %r used by both %s and %s" % (s, seen_files[s], slug))
        seen_files[s] = slug
        p = resolve(s)
        if not os.path.exists(p):
            missing.append((slug, s))
            continue
        with Image.open(p) as im:
            w, h = im.size
        mt = datetime.date.fromtimestamp(os.path.getmtime(p))
        imgs.append({
            "file": s, "w": w, "h": h, "ratio": round(w / h, 4),
            "bytes": os.path.getsize(p), "year": mt.year, "date": mt.isoformat(),
            "orient": "square" if 0.95 <= w / h <= 1.05 else ("portrait" if w < h else "landscape"),
        })
    bid = BEHANCE.get(slug)
    works.append({
        "id": slug, "brand_en": ben, "brand_ar": bar,
        "tagline_ar": tar, "tagline_en": ten, "cat": cat,
        "images": imgs, "sources": srcs,
        "behance": ("https://www.behance.net/gallery/%d/%s" % (bid, BEHANCE_SLUG[bid])) if bid else None,
        "behance_id": bid,
        "year": max((i["year"] for i in imgs), default=datetime.date.today().year),
    })

if missing:
    raise SystemExit("MISSING SOURCE FILES:\n" + "\n".join("  %s: %s" % m for m in missing))

library = sorted(f for f in os.listdir(SRC) if f.lower().endswith((".jpg", ".jpeg", ".png")))
unused = [f for f in library if f not in seen_files]
json.dump({"works": works, "cats": CATS, "source_count": len(seen_files)},
          open("manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("works: %d | versions: %d | sources used: %d" % (
    len(works), sum(len(w["images"]) for w in works), len(seen_files)))
print("brands:", len({w["brand_en"] for w in works}))
print("by cat:", {c: sum(1 for w in works if w["cat"] == c) for c in CATS})
print("library files not used:", len(unused))
for f in unused:
    print("   -", f)

