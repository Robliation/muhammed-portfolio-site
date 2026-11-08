# -*- coding: utf-8 -*-
"""Canonical work list: 89 source files -> unique designs (orientation pairs merged)."""
import os, json, datetime
from PIL import Image

SRC = r"C:\Users\M Deisgner\Pictures\Pictures Photoshop\Designs"
FILES = sorted(f for f in os.listdir(SRC) if f.lower().endswith((".jpg", ".jpeg", ".png")))

BEHANCE = {
    79: 229800805, 30: 229800671, 77: 225611763, 66: 225431617, 31: 222872961,
    71: 222550607, 37: 221889365, 35: 221799605, 32: 221496423, 19: 221449035,
    72: 221360445, 25: 221261353,
}
BEHANCE_SLUG = {
    229800805: "-(-)", 229800671: "-(-)", 225611763: "Design-about-ALBAIK",
    225431617: "Kinza-cola-Design", 222872961: "-(-)", 222550607: "-(-)",
    221889365: "-(-)", 221799605: "-(-)", 221496423: "-(-)", 221449035: "-(-)",
    221360445: "-(-)", 221261353: "-(-)",
}

# (slug, brand_en, brand_ar, tagline_ar, tagline_en, category, sources)
# A source is either a 1-based index into FILES or, for artwork the owner handed
# over as a finished file rather than dropping into the Designs library, a
# workspace-relative path. A path carrying a slash is read that way by optimize.py.
W = [
    ("albaik-crispy-chicken", "Al Baik", "البيك", "دجاج Crispy", "Crispy chicken, square", "food", [39]),
    ("albaik-best-with-us", "Al Baik", "البيك", "الأفضل لك عندنا", "The best for you is with us", "food", [41, 40]),
    ("albaik-love-of-the-years", "Al Baik", "البيك", "البيك حب السنين", "Al Baik, the love of the years", "food", [77]),
    ("tazaj-crazy-taste", "Tazaj", "الطازج", "طعم بجنن", "A crazy-good taste", "food", [79]),
    ("tazaj-city-of-crispy", "Tazaj", "الطازج", "TAZAJ", "TAZAJ — city of crispy", "food", [80]),
    ("tazaj-changes-your-mood", "Tazaj", "الطازج", "الطازج يغير مزاجك", "Tazaj changes your mood", "food", [82, 81]),
    ("shawarmer-different", "Shawarmer", "شاورمر", "شاورما غير", "A different shawarma", "food", [55]),
    ("shawarmer-golden", "Shawarmer", "شاورمر", "لا تفوت الشاورما الذهبية", "Don't miss the golden shawarma", "food", [56]),
    ("jahez-delivery-flies", "Jahez", "جاهز", "توصيلنا مثل الطيارة", "Our delivery flies like a plane", "food", [44, 45]),
    ("jahez-pizza-feast", "Jahez", "جاهز", "عروض بيتزا", "Floating pizza feast", "food", [46]),
    ("hungerstation-legendary-speed", "Hungerstation", "هنقرستيشن", "سرعة خرافية", "Legendary speed", "food", [76]),
    ("gofood-at-your-door", "GoFood", "جوفود", "طلبك على الباب", "Your order at your door", "food",
     ["sources/gofood-at-your-door.png"]),
    ("takohat-forget-your-troubles", "Takohat", "تاكوهت", "الأكلة تخليك توكل أصعابك", "The meal that makes you forget your troubles", "food", [42, 43]),
    ("just-samboosa-authentic", "Just Samboosa", "جست سمبوسة", "على أصولها متعة مالها حدود", "The authentic way, boundless enjoyment", "food", [47]),
    ("just-samboosa-mindblown", "Just Samboosa", "جست سمبوسة", "سمبوسة هتجنن عقلك", "Samosa that blows your mind", "food", [86]),
    ("falafel-burak-done-right", "Falafel Burak", "فلافل بوراك", "عندنا فلافل صح", "We make falafel right", "food", [61, 62]),
    ("national-poultry-mandi", "National Poultry", "دواجن الوطنية", "مندي طيب مع دواجن الوطنية", "Tayyib mandi with National Poultry", "food", [51, 50]),
    ("al-musafir-eat-anywhere", "Al Musafir", "المسافر", "أستمتع بأكلك في أي مكان", "Enjoy your meal anywhere", "food", [35]),
    ("al-yawm-goes-with-your-day", "Al Yawm", "اليوم", "تمشي مع اليوم", "Goes with your day", "food", [36]),
    ("al-adnan-dawali", "Al Adnan", "العدنان", "دوالي", "Dawali — stuffed vine leaves", "food", [83]),
    ("burger-mish-best-in-world", "Burger Mish", "برجر مش", "أفضل برجر في العالم", "The best burger in the world", "food", [84]),
    ("the-cake-house-makes-your-day", "The Cake House", "بيت الكيك", "كيك يصنع يومك", "Cake that makes your day", "food", [85]),
    ("kayal-kunafa", "Kayal", "خيال", "كنافة فوق الخيال", "Kunafa beyond imagination", "food", [87]),
    ("kayal-al-tawool", "Kayal", "خيال", "الطول يفرق", "Length makes the difference", "food",
     ["sources/khayal-al-tawool.png"]),
    ("sultan-fish-crispy", "Sultan Al-Samak", "سلطان السمك", "سمك مقرمش", "Crispy fish", "food", [88]),
    ("ful-wazir-exceptional", "Ful Al-Wazir", "فول الوزير", "فول حقنا متميز", "Our ful is exceptional", "food", [89]),
    ("romansia-ideal-restaurant", "Al Romansia", "الرومانسية", "مطعم المثالي", "The ideal restaurant", "food", [78]),
    ("mazaaq-irresistible-burger", "Mazaaq", "مذاق", "البرجر المثالي لا يقاوم", "The perfect burger is irresistible", "food", [67, 68]),
    ("pizza-offers-beyond-imagination", "Pizza Offers", "عروض بيتزا", "بيتزا فوق الخيال", "Pizza beyond imagination", "food", [57, 58]),

    ("almarai-all-vitamins", "Almarai", "المراعي", "حليب كلو فيتامينات", "Milk, all vitamins", "fmcg", [2]),
    ("almarai-royal-hummus", "Almarai", "المراعي", "حمص ملكي", "Royal hummus", "fmcg", [26]),
    ("almarai-labneh-worries", "Almarai", "المراعي", "لبنة المراعي تنسيك همك", "Labneh that makes you forget your worries", "fmcg", [31]),
    ("almarai-labneh-heart", "Almarai", "المراعي", "لبنة يحبو قلبك", "A labneh your heart loves", "fmcg", [32]),
    ("almarai-irresistible-taste", "Almarai", "المراعي", "مذاق لا يقاوم", "An irresistible taste", "fmcg", [33]),
    ("almarai-mood-car", "Almarai", "المراعي", "تمشي مزاجك", "Moves with your mood", "fmcg", [24]),
    ("almarai-chocolate-milk", "Almarai", "المراعي", "حليب شوكولاتة", "Chocolate milk", "fmcg", [34]),
    ("al-ulali-no-other-taste", "Al Ulali", "العلالي", "طعم ولا أحلى", "A taste like no other", "fmcg", [1]),
    ("saudia-cheese-of-kings", "Saudia Cheese", "السعودية", "جبنة الملوك", "Cheese of kings", "fmcg", [20]),
    ("indomie-other-world", "Indomie", "إندومي", "عالم غير", "A whole other world", "fmcg", [19]),
    ("marami-different-chips", "Marami", "مرامي", "شبس حقنا غير", "Our chips are different", "fmcg", [70]),
    ("sadia-field-fry", "Sadia", "ساديا", "طلعة ممتعة مع ساديا", "A delightful outing with Sadia", "fmcg", [52]),
    ("country-cornflakes-protein", "Country Corn Flakes", "كونتري", "بروتين ينفع مع كورن فليكس", "Protein that works with corn flakes", "fmcg", [64]),

    ("almarai-strawberry-milk", "Almarai", "المراعي", "حليب المراعي غير", "Almarai milk is different", "drinks", [25, 69]),
    ("almarai-different-juices", "Almarai", "المراعي", "عصائر المراعي غير", "Almarai juices are different", "drinks", [28, 29]),
    ("almarai-respectable-laban", "Almarai", "المراعي", "لبن محترم", "Respectable laban", "drinks", [30]),
    ("almarai-real-watermelon", "Almarai", "المراعي", "بطيخ أصلي", "Real watermelon", "drinks", [23]),
    ("kinza-cola-splash", "Kinza", "كينزا", "كينزا كولا", "Kinza Cola", "drinks", [66]),
    ("kinza-forget-thirst", "Kinza", "كينزا", "مشروب ينسيك العطش", "A drink that makes you forget thirst", "drinks", [65]),
    ("berain-ice-water", "Berain", "بيرين", "ماء ثلج", "Ice water", "drinks", [38]),
    ("bajah-coffee-day", "Bajah", "باجة", "قهوة تمتع يومك", "Coffee that makes your day", "drinks", [37]),
    ("aseer-time-flavour", "Aseer Time", "عصير تايم", "استمتع بالنكهة", "Enjoy the flavour", "drinks", [59]),
    ("aseer-time-indulge", "Aseer Time", "عصير تايم", "تمتع", "Indulge", "drinks", [60]),

    ("jarir-best-devices", "Jarir Bookstore", "مكتبة جرير", "أفضل أجهزة عندنا", "The best devices are with us", "retail", [74, 73]),
    ("jarir-cook-in-comfort", "Jarir Bookstore", "مكتبة جرير", "اطبخ وأنت مرتاح", "Cook in comfort", "retail", [72]),
    ("jarir-safety-backpack", "Jarir Bookstore", "مكتبة جرير", "شنطة أمان لا تفوتك", "A safety backpack you can't miss", "retail", [75]),
    ("centrepoint-travel-bag", "Centrepoint", "سنتربوينت", "شنطة سفرك في أمان", "Your travel bag is safe", "retail", [54]),

    ("qiddiya-best-tourism-city", "Qiddiya", "القدية", "الأفضل مدينة سياحة", "The best city of tourism", "travel", [21, 22]),
    ("dubai-enjoy-the-vibe", "Dubai", "دبي", "أستمتع بأجواء دبي", "Enjoy the vibe of Dubai", "travel", [48]),
    ("dubai-present-meets-future", "Dubai", "دبي", "دبي حيث يلتقي الحاضر بالمستقبل", "Dubai, where the present meets the future", "travel", [49]),

    ("almarai-ramadan-kareem", "Almarai", "المراعي", "رمضان كريم", "Ramadan Kareem", "seasonal", [27]),
    ("sadia-ramadan-offers", "Sadia", "ساديا", "عروض رمضان", "Ramadan offers", "seasonal", [53]),
    ("vimto-ramadan-kareem", "Vimto", "فيمتو", "رمضان كريم", "Ramadan Kareem", "seasonal", [63]),
    ("jarir-eid-mubarak", "Jarir Bookstore", "مكتبة جرير", "عيد مبارك علينا وعليكم", "Blessed Eid to us and you", "seasonal", [71]),

    ("myroqia-series-one", "MyRoqia", "رقيتي", "سلسلة بوستات — ١", "Social series, post one", "brand", [5, 3, 4]),
    ("myroqia-series-two", "MyRoqia", "رقيتي", "سلسلة بوستات — ٢", "Social series, post two", "brand", [7, 9, 6, 8]),
    ("myroqia-series-three", "MyRoqia", "رقيتي", "سلسلة بوستات — ٣", "Social series, post three", "brand", [11, 13, 10, 12]),
    ("myroqia-story-format", "MyRoqia", "رقيتي", "تصميم ستوري", "Story-format graphic", "brand", [14, 15]),
    ("myroqia-editorial-cover", "MyRoqia", "رقيتي", "تصميم المقالات", "Editorial article cover", "brand", [16]),
    ("notion-arrab-afkarak", "Notion", "نوتشن", "رتب أفكارك", "Get your ideas in order", "brand",
     ["sources/notion-arrab-afkarak.png"]),

    ("concept-hummus", "Self-initiated", "ذاتي", "تصميم حمص", "Hummus concept ad", "concept", [17]),
    ("concept-perfume", "Self-initiated", "ذاتي", "تصميم عطر", "Perfume concept ad", "concept", [18]),
]

CATS = {
    "food": ("Restaurants & food", "مطاعم وأغذية"),
    "fmcg": ("FMCG & grocery", "سلع استهلاكية"),
    "drinks": ("Drinks & juices", "مشروبات"),
    "retail": ("Retail & lifestyle", "تجزئة وأسلوب حياة"),
    "travel": ("Tourism & places", "سياحة وأماكن"),
    "seasonal": ("Ramadan & Eid", "مواسم"),
    "brand": ("Brand & social systems", "هوية وسوشيال"),
    "concept": ("Concept & experimental", "مفاهيم تجريبية"),
}

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

works = []
for slug, ben, bar, tar, ten, cat, idxs in W:
    imgs = []
    for n in idxs:
        if isinstance(n, str):
            f, p = n, os.path.join(ROOT, n)
        else:
            f = FILES[n - 1]
            p = os.path.join(SRC, f)
        with Image.open(p) as im:
            w, h = im.size
        mt = datetime.date.fromtimestamp(os.path.getmtime(p))
        imgs.append({
            "file": f, "w": w, "h": h, "ratio": round(w / h, 4),
            "bytes": os.path.getsize(p), "year": mt.year, "date": mt.isoformat(),
            "orient": "square" if 0.95 <= w / h <= 1.05 else ("portrait" if w < h else "landscape"),
        })
    bid = BEHANCE.get(idxs[0])
    works.append({
        "id": slug, "brand_en": ben, "brand_ar": bar.replace("المراcci", "المراعي"),
        "tagline_ar": tar, "tagline_en": ten, "cat": cat,
        "images": imgs, "primary": idxs[0],
        "behance": (f"https://www.behance.net/gallery/{bid}/{BEHANCE_SLUG[bid]}" if bid else None),
        "behance_id": bid,
        "year": max(i["year"] for i in imgs),
    })

used = sorted({n for _, _, _, _, _, _, idxs in W for n in idxs if isinstance(n, int)})
alln = list(range(1, len(FILES) + 1))
missing = [n for n in alln if n not in used]
print("works:", len(works), "| source files mapped:", len(used), "of", len(alln))
print("unmapped:", [(n, FILES[n - 1]) for n in missing])
json.dump({"works": works, "cats": CATS, "source_count": len(alln)},
          open("manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
brands = sorted({w["brand_en"] for w in works})
print("brands:", len(brands))
print("by cat:", {c: sum(1 for w in works if w["cat"] == c) for c in CATS})
