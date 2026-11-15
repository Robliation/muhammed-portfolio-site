# -*- coding: utf-8 -*-
"""Canonical work list: 89 source files -> unique designs (orientation pairs merged)."""
import os, json, datetime
from PIL import Image

SRC = r"C:\Users\M Deisgner\Pictures\Pictures Photoshop\Designs"
FILES = sorted(f for f in os.listdir(SRC) if f.lower().endswith((".jpg", ".jpeg", ".png")))

BEHANCE = {
    82: 225611763,
    84: 229800805,
    38: 221799605,
    34: 222872961,
    35: 221496423,
    21: 221449035,
    28: 221261353,
    33: 229800671,
    71: 225431617,
    40: 221889365,
    77: 221360445,
    76: 222550607,
}
BEHANCE_SLUG = {
    225611763: "Design-about-ALBAIK",
    229800805: "-(-)",
    221799605: "-(-)",
    222872961: "-(-)",
    221496423: "-(-)",
    221449035: "-(-)",
    221261353: "-(-)",
    229800671: "-(-)",
    225431617: "Kinza-cola-Design",
    221889365: "-(-)",
    221360445: "-(-)",
    222550607: "-(-)",
}

# (slug, brand_en, brand_ar, tagline_ar, tagline_en, category, sources)
# A source is either a 1-based index into FILES or, for artwork the owner handed
# over as a finished file rather than dropping into the Designs library, a
# workspace-relative path. A path carrying a slash is read that way by optimize.py.
W = [
    ("albaik-crispy-chicken", "Al Baik", "البيك", "دجاج Crispy", "Crispy chicken, square", "food", [42]),
    ("albaik-best-with-us", "Al Baik", "البيك", "الأفضل لك عندنا", "The best for you is with us", "food", [44, 43]),
    ("albaik-love-of-the-years", "Al Baik", "البيك", "البيك حب السنين", "Al Baik, the love of the years", "food", [82]),
    ("tazaj-crazy-taste", "Tazaj", "الطازج", "طعم بجنن", "A crazy-good taste", "food", [84]),
    ("tazaj-city-of-crispy", "Tazaj", "الطازج", "TAZAJ", "TAZAJ — city of crispy", "food", [85]),
    ("tazaj-changes-your-mood", "Tazaj", "الطازج", "الطازج يغير مزاجك", "Tazaj changes your mood", "food", [87, 86]),
    ("shawarmer-different", "Shawarmer", "شاورمر", "شاورما غير", "A different shawarma", "food", [59]),
    ("shawarmer-golden", "Shawarmer", "شاورمر", "لا تفوت الشاورما الذهبية", "Don't miss the golden shawarma", "food", [60]),
    ("jahez-delivery-flies", "Jahez", "جاهز", "توصيلنا مثل الطيارة", "Our delivery flies like a plane", "food", [47, 48]),
    ("jahez-pizza-feast", "Jahez", "جاهز", "عروض بيتزا", "Floating pizza feast", "food", [49]),
    ("hungerstation-legendary-speed", "Hungerstation", "هنقرستيشن", "سرعة خرافية", "Legendary speed", "food", [81]),
    ("gofood-at-your-door", "GoFood", "جوفود", "طلبك على الباب", "Your order at your door", "food", ["sources/gofood-at-your-door.png"]),
    ("takohat-forget-your-troubles", "Takohat", "تاكوهت", "الأكلة تخليك توكل أصعابك", "The meal that makes you forget your troubles", "food", [45, 46]),
    ("just-samboosa-authentic", "Just Samboosa", "جست سمبوسة", "على أصولها متعة مالها حدود", "The authentic way, boundless enjoyment", "food", [50]),
    ("just-samboosa-mindblown", "Just Samboosa", "جست سمبوسة", "سمبوسة هتجنن عقلك", "Samosa that blows your mind", "food", [91]),
    ("falafel-burak-done-right", "Falafel Burak", "فلافل بوراك", "عندنا فلافل صح", "We make falafel right", "food", [66, 67]),
    ("national-poultry-mandi", "National Poultry", "دواجن الوطنية", "مندي طيب مع دواجن الوطنية", "Tayyib mandi with National Poultry", "food", [55, 54]),
    ("al-musafir-eat-anywhere", "Al Musafir", "المسافر", "أستمتع بأكلك في أي مكان", "Enjoy your meal anywhere", "food", [38]),
    ("al-yawm-goes-with-your-day", "Al Yawm", "اليوم", "تمشي مع اليوم", "Goes with your day", "food", [39]),
    ("al-adnan-dawali", "Al Adnan", "العدنان", "دوالي", "Dawali — stuffed vine leaves", "food", [88]),
    ("burger-mish-best-in-world", "Burger Mish", "برجر مش", "أفضل برجر في العالم", "The best burger in the world", "food", [89]),
    ("the-cake-house-makes-your-day", "The Cake House", "بيت الكيك", "كيك يصنع يومك", "Cake that makes your day", "food", [90]),
    ("kayal-kunafa", "Kayal", "خيال", "كنافة فوق الخيال", "Kunafa beyond imagination", "food", [92]),
    ("kayal-al-tawool", "Kayal", "خيال", "الطول يفرق", "Length makes the difference", "food", ["sources/khayal-al-tawool.png"]),
    ("sultan-fish-crispy", "Sultan Al-Samak", "سلطان السمك", "سمك مقرمش", "Crispy fish", "food", [93]),
    ("ful-wazir-exceptional", "Ful Al-Wazir", "فول الوزير", "فول حقنا متميز", "Our ful is exceptional", "food", [94]),
    ("romansia-ideal-restaurant", "Al Romansia", "الرومانسية", "مطعم المثالي", "The ideal restaurant", "food", [83]),
    ("mazaaq-irresistible-burger", "Mazaaq", "مذاق", "البرجر المثالي لا يقاوم", "The perfect burger is irresistible", "food", [72, 73]),
    ("pizza-offers-beyond-imagination", "Pizza Offers", "عروض بيتزا", "بيتزا فوق الخيال", "Pizza beyond imagination", "food", [61, 62]),
    ("almarai-all-vitamins", "Almarai", "المراعي", "حليب كلو فيتامينات", "Milk, all vitamins", "fmcg", [2]),
    ("almarai-royal-hummus", "Almarai", "المراعي", "حمص ملكي", "Royal hummus", "fmcg", [29]),
    ("almarai-labneh-worries", "Almarai", "المراعي", "لبنة المراعي تنسيك همك", "Labneh that makes you forget your worries", "fmcg", [34]),
    ("almarai-labneh-heart", "Almarai", "المراعي", "لبنة يحبو قلبك", "A labneh your heart loves", "fmcg", [35]),
    ("almarai-irresistible-taste", "Almarai", "المراعي", "مذاق لا يقاوم", "An irresistible taste", "fmcg", [36]),
    ("almarai-mood-car", "Almarai", "المراعي", "تمشي مزاجك", "Moves with your mood", "fmcg", [27]),
    ("almarai-chocolate-milk", "Almarai", "المراعي", "حليب شوكولاتة", "Chocolate milk", "fmcg", [37]),
    ("al-ulali-no-other-taste", "Al Ulali", "العلالي", "طعم ولا أحلى", "A taste like no other", "fmcg", [1]),
    ("al-ulali-for-the-ones-who-matter", "Al Ulali", "العلالي", "لأنها للغالي", "For the ones who matter", "fmcg", ["sources/al-ulali-for-the-ones-who-matter.png"]),
    ("saudia-cheese-of-kings", "Saudia Cheese", "السعودية", "جبنة الملوك", "Cheese of kings", "fmcg", [22]),
    ("indomie-other-world", "Indomie", "إندومي", "عالم غير", "A whole other world", "fmcg", [21]),
    ("marami-different-chips", "Marami", "مرامي", "شبس حقنا غير", "Our chips are different", "fmcg", [75]),
    ("sadia-field-fry", "Sadia", "ساديا", "طلعة ممتعة مع ساديا", "A delightful outing with Sadia", "fmcg", [56]),
    ("country-cornflakes-protein", "Country Corn Flakes", "كونتري", "بروتين ينفع مع كورن فليكس", "Protein that works with corn flakes", "fmcg", [69]),
    ("almarai-strawberry-milk", "Almarai", "المراعي", "حليب المراعي غير", "Almarai milk is different", "drinks", [28, 74]),
    ("almarai-different-juices", "Almarai", "المراعي", "عصائر المراعي غير", "Almarai juices are different", "drinks", [31, 32]),
    ("almarai-respectable-laban", "Almarai", "المراعي", "لبن محترم", "Respectable laban", "drinks", [33]),
    ("almarai-real-watermelon", "Almarai", "المراعي", "بطيخ أصلي", "Real watermelon", "drinks", [26]),
    ("kinza-cola-splash", "Kinza", "كينزا", "كينزا كولا", "Kinza Cola", "drinks", [71]),
    ("kinza-forget-thirst", "Kinza", "كينزا", "مشروب ينسيك العطش", "A drink that makes you forget thirst", "drinks", [70]),
    ("berain-ice-water", "Berain", "بيرين", "ماء ثلج", "Ice water", "drinks", [41]),
    ("bajah-coffee-day", "Bajah", "باجة", "قهوة تمتع يومك", "Coffee that makes your day", "drinks", [40]),
    ("aseer-time-flavour", "Aseer Time", "عصير تايم", "استمتع بالنكهة", "Enjoy the flavour", "drinks", [63]),
    ("aseer-time-indulge", "Aseer Time", "عصير تايم", "تمتع", "Indulge", "drinks", [65]),
    ("aseer-time-real-refresh", "Aseer Time", "عصير تايم", "الانتعاش الحقيقي يسرسح على قلبك", "The real refreshment that swooshes your heart", "drinks", [64]),
    ("jarir-best-devices", "Jarir Bookstore", "مكتبة جرير", "أفضل أجهزة عندنا", "The best devices are with us", "retail", [79, 78]),
    ("jarir-cook-in-comfort", "Jarir Bookstore", "مكتبة جرير", "اطبخ وأنت مرتاح", "Cook in comfort", "retail", [77]),
    ("jarir-safety-backpack", "Jarir Bookstore", "مكتبة جرير", "شنطة أمان لا تفوتك", "A safety backpack you can't miss", "retail", [80]),
    ("centrepoint-travel-bag", "Centrepoint", "سنتربوينت", "شنطة سفرك في أمان", "Your travel bag is safe", "retail", [58]),
    ("qiddiya-best-tourism-city", "Qiddiya", "القدية", "الأفضل مدينة سياحة", "The best city of tourism", "travel", [24, 25]),
    ("dubai-enjoy-the-vibe", "Dubai", "دبي", "أستمتع بأجواء دبي", "Enjoy the vibe of Dubai", "travel", [52]),
    ("dubai-present-meets-future", "Dubai", "دبي", "دبي حيث يلتقي الحاضر بالمستقبل", "Dubai, where the present meets the future", "travel", [53]),
    ("almarai-ramadan-kareem", "Almarai", "المراعي", "رمضان كريم", "Ramadan Kareem", "seasonal", [30]),
    ("sadia-ramadan-offers", "Sadia", "ساديا", "عروض رمضان", "Ramadan offers", "seasonal", [57]),
    ("vimto-ramadan-kareem", "Vimto", "فيمتو", "رمضان كريم", "Ramadan Kareem", "seasonal", [68]),
    ("jarir-eid-mubarak", "Jarir Bookstore", "مكتبة جرير", "عيد مبارك علينا وعليكم", "Blessed Eid to us and you", "seasonal", [76]),
    ("myroqia-series-one", "MyRoqia", "رقيتي", "سلسلة بوستات — ١", "Social series, post one", "brand", [6, 4, 5]),
    ("myroqia-series-two", "MyRoqia", "رقيتي", "سلسلة بوستات — ٢", "Social series, post two", "brand", [8, 10, 7, 9]),
    ("myroqia-series-three", "MyRoqia", "رقيتي", "سلسلة بوستات — ٣", "Social series, post three", "brand", [12, 14, 11, 13]),
    ("myroqia-story-format", "MyRoqia", "رقيتي", "تصميم ستوري", "Story-format graphic", "brand", [15, 16]),
    ("myroqia-editorial-cover", "MyRoqia", "رقيتي", "تصميم المقالات", "Editorial article cover", "brand", [17]),
    ("notion-arrab-afkarak", "Notion", "نوتشن", "رتب أفكارك", "Get your ideas in order", "brand", ["sources/notion-arrab-afkarak.png"]),
    ("concept-hummus", "Self-initiated", "ذاتي", "تصميم حمص", "Hummus concept ad", "concept", [18]),
    ("concept-perfume", "Self-initiated", "ذاتي", "تصميم عطر", "Perfume concept ad", "concept", [19]),
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
