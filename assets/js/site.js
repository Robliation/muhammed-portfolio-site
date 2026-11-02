/* M Designer — site logic: bilingual rendering, filtering, proof lightbox */
(function () {
  "use strict";
  var D = window.MD_DATA;
  if (!D) return;

  /* ------------------------------------------------------------------ copy */
  var T = {
    ar: {
      title: "محمد — مصمم جرافيك | بورتفوليو تصاميم إعلانية",
      desc: "بورتفوليو محمد، مصمم جرافيك في مكة المكرمة. 68 تصميمًا إعلانيًا لـ38 علامة في المطاعم والأغذية والمشروبات والتجزئة والسياحة.",
      "nav.work": "الأعمال", "nav.about": "نبذة", "nav.brands": "العلامات",
      "nav.path": "المسار", "nav.cv": "السيرة", "nav.contact": "تواصل",
      "hero.eyebrow": "مصمم جرافيك · مكة المكرمة، السعودية",
      "hero.line1": "تصميم إعلانات",
      "hero.line2": "توقف <em>التمرير</em>",
      "hero.lede": "أشتغل على الإعلان الموجّه للسوشيال ميديا: جملة عربية قوية، منتج يبدو شهياً، وتكوين يُقرأ في الثانية الأولى. كل حملة أجهّزها بالمقاسات المربعة والطولية والعرضية.",
      "hero.cta1": "شاهد الأعمال", "hero.cta2": "حمّل السيرة", "hero.cta3": "تواصل",
      "fact.works": "تصميم", "fact.brands": "علامة", "fact.fields": "مجال", "fact.formats": "مقاسات",
      "board.tag": "أحدث الأعمال", "board.meta": "4 من أصل",
      "ticker.label": "علامات في الأعمال",
      "work.n": "الأعمال",
      "work.h": "كل التصاميم في مكان واحد",
      "work.lede": "تصفّى حسب المجال أو ابحث باسم العلامة. اضغط أي تصميم لفتحه بالحجم الكامل مع بياناته.",
      "work.all": "الكل", "work.search": "ابحث باسم العلامة أو النص…",
      "work.showing": "يعرض", "work.of": "من",
      "work.spec": "الأعمال المنشورة هنا مفاهيمية (Spec) لعلامات قائمة، أُنتجت كتدريب على السوق السعودي ما لم يُذكر عكس ذلك.",
      "work.empty.t": "ما فيه نتيجة",
      "work.empty.d": "جرّب اسم علامة ثاني أو أزل الفلاتر.",
      "work.reset": "أظهر كل الأعمال",
      "about.n": "نبذة",
      "about.h": "مين محمد؟",
      "about.p1": "أنا <strong>محمد</strong>، مصمم جرافيك في <strong>مكة المكرمة</strong>. تخصصي هو الإعلان الرقمي بالعربي — البوست اللي يوقف الشخص وهو يمرر، ويخليه يحس بالطعم قبل ما يقرأ النص.",
      "about.p2": "بدأت من الهوية الشخصية والأنظمة البصرية لمحتوى ديني، ووصلت اليوم إلى إعلانات العلامات الكبيرة في السعودية: ألبان، مطاعم، مشروبات، تجزئة، وسياحة. أشتغل أساساً على <strong>Adobe Photoshop</strong> و<strong>Illustrator</strong>، وأستخدم أدوات توليد الصور بالذكاء الاصطناعي لبناء صور خام سريعة، ثم أعالجها يدوياً حتى تصير قابلة للنشر.",
      "about.pull": "التصميم الجيد على السوشيال يُفهم في ثانية — ولا يشرح نفسه.",
      "about.skills": "المهارات", "about.tools": "الأدوات", "about.fields": "المجالات الإبداعية",
      "about.spec.role": "المسمى", "about.spec.role.v": "مصمم جرافيك — إعلان السوشيال ميديا",
      "about.spec.loc": "الموقع", "about.spec.loc.v": "مكة المكرمة، السعودية",
      "about.spec.exp": "الخبرة", "about.spec.exp.v": "سنتان في تصميم منشورات السوشيال ميديا",
      "about.spec.lang": "اللغات", "about.spec.lang.v": "العربية (لغة أم) · الإنجليزية",
      "about.spec.avail": "متاح لـ", "about.spec.avail.v": "وظيفة بدوام كامل · مشاريع freelance",
      "brands.n": "العلامات",
      "brands.h": "العلامات في الأعمال",
      "brands.lede": "38 علامة، مرتبة حسب المجال، مع عدد التصاميم لكل واحدة.",
      "path.n": "المسار",
      "path.h": "من الهوية الشخصية إلى إعلان البراند",
      "path.1.t": "البداية — أنظمة هوية ومحتوى",
      "path.1.y": "2024",
      "path.1.d": "سلسلة بوستات ومقالات لهوية شخصية دينية (موقع رقيتي): إطار زخرفي إسلامي، نسخ بالمربع والطولي والعرضي، وتجارب على الخط العربي.",
      "path.2.t": "بيهاينس — النشر اليومي",
      "path.2.y": "فبراير 2025",
      "path.2.d": "انضممت إلى بيهاينس في فبراير 2025 وبدأت أنشر الأعمال بانتظام، وبنيت أسلوب الإعلان العربي المربع/الطولي/العرضي.",
      "path.3.t": "إعلانات العلامات السعودية",
      "path.3.y": "2025",
      "path.3.d": "أكثر من 60 إعلاناً للمراعي والبيك والطازج وجاهز وجرير وكينزا والقدية ودبي وغيرها، من فبراير إلى مايو 2025.",
      "path.4.t": "اليوم",
      "path.4.y": "2026",
      "path.4.d": "أوسّع الأعمال على علامات جديدة وأجهّز كل حملة بكل المقاسات. متاح لفرصة بدوام كامل أو مشاريع مستقلة.",
      "contact.n": "تواصل",
      "contact.h": "تحتاج مصمم لحملتك الجاية؟",
      "contact.p": "أرسل تفاصيل المشروع أو الوظيفة، وأرد عليك خلال يوم عمل. تقدر تشوف الأعمال كاملة على بيهاينس أو تفتح صفحة السيرة المختصرة.",
      "contact.be": "راسلني على بيهاينس", "contact.gh": "GitHub", "contact.cv": "حمّل السيرة",
      "contact.avail": "متاح لاستلام عمل جديد",
      "foot.tag": "تصميم إعلانات بالعربي · مكة المكرمة",
      "foot.rights": "جميع التصاميم ملك محمد — 2024 إلى 2026.",
      "lb.prev": "التصميم السابق", "lb.next": "التصميم التالي", "lb.close": "إغلاق",
      "lb.cat": "المجال", "lb.year": "السنة", "lb.size": "المقاس الأصلي", "lb.fmt": "المقاسات",
      "lb.be": "مشاهده على بيهاينس", "lb.alt": "نسخ أخرى من نفس التصميم",
      "lb.of": "تصميم",
      "alt.img": "تصميم إعلاني لعلامة",
      "cv.h": "السيرة المختصرة",
      "lang.btn": "EN",
    },
    en: {
      title: "Muhammed — Graphic Designer | Advertising Design Portfolio",
      desc: "Portfolio of Muhammed, a graphic designer in Mecca, Saudi Arabia. 68 advertising designs across 38 brands in food, dairy, drinks, retail and tourism.",
      "nav.work": "Work", "nav.about": "About", "nav.brands": "Brands",
      "nav.path": "Path", "nav.cv": "Résumé", "nav.contact": "Contact",
      "hero.eyebrow": "Graphic designer · Mecca, Saudi Arabia",
      "hero.line1": "Ad design that",
      "hero.line2": "<em>stops the scroll</em>",
      "hero.lede": "I make social-first advertising: a hard-hitting Arabic line, a product that looks appetising, and a composition that reads in the first second. Every campaign ships square, portrait and landscape.",
      "hero.cta1": "View work", "hero.cta2": "Download résumé", "hero.cta3": "Get in touch",
      "fact.works": "designs", "fact.brands": "brands", "fact.fields": "sectors", "fact.formats": "formats",
      "board.tag": "Latest proofs", "board.meta": "4 of",
      "ticker.label": "Brands in the work",
      "work.n": "The work",
      "work.h": "Every design in one place",
      "work.lede": "Filter by sector or search a brand. Open any design to see it full size with its specs.",
      "work.all": "All", "work.search": "Search a brand or line…",
      "work.showing": "Showing", "work.of": "of",
      "work.spec": "Unless stated otherwise, these are concept (spec) advertisements for existing brands, produced as training for the Saudi market.",
      "work.empty.t": "Nothing matches",
      "work.empty.d": "Try another brand, or clear the filters.",
      "work.reset": "Show all work",
      "about.n": "About",
      "about.h": "Who is Muhammed?",
      "about.p1": "I'm <strong>Muhammed</strong>, a graphic designer based in <strong>Mecca</strong>. My specialty is Arabic digital advertising — the post that stops someone mid-scroll and makes them taste the product before reading a word.",
      "about.p2": "I started with identity systems for faith-based content and arrived at advertising for major Saudi brands: dairy, restaurants, drinks, retail and tourism. I work primarily in <strong>Adobe Photoshop</strong> and <strong>Illustrator</strong>, and use AI image generation to build raw stock imagery fast, then retouch it by hand until it is publishable.",
      "about.pull": "Good social design is understood in one second — and never has to explain itself.",
      "about.skills": "Capabilities", "about.tools": "Tools", "about.fields": "Creative fields",
      "about.spec.role": "Role", "about.spec.role.v": "Graphic designer — social advertising",
      "about.spec.loc": "Based in", "about.spec.loc.v": "Mecca, Saudi Arabia",
      "about.spec.exp": "Experience", "about.spec.exp.v": "2 years designing social media campaigns",
      "about.spec.lang": "Languages", "about.spec.lang.v": "Arabic (native) · English",
      "about.spec.avail": "Open to", "about.spec.avail.v": "Full-time role · freelance projects",
      "brands.n": "Brands",
      "brands.h": "Brands in the work",
      "brands.lede": "38 brands, grouped by sector, with the number of designs for each.",
      "path.n": "Path",
      "path.h": "From identity systems to brand advertising",
      "path.1.t": "Start — identity and content systems",
      "path.1.y": "2024",
      "path.1.d": "A post series and editorial covers for a personal faith brand (MyRoqia): an Islamic decorative frame, square/portrait/landscape versions, and Arabic type experiments.",
      "path.2.t": "Behance — publishing daily",
      "path.2.y": "Feb 2025",
      "path.2.d": "Joined Behance in February 2025, started publishing consistently, and built the square/portrait/landscape Arabic ad format.",
      "path.3.t": "Saudi brand advertising",
      "path.3.y": "2025",
      "path.3.d": "Over 60 ads for Almarai, Al Baik, Tazaj, Jahez, Jarir, Kinza, Qiddiya and Dubai, from February to May 2025.",
      "path.4.t": "Now",
      "path.4.y": "2026",
      "path.4.d": "Adding new brands and shipping every campaign in all formats. Available for a full-time role or freelance projects.",
      "contact.n": "Contact",
      "contact.h": "Need a designer for the next campaign?",
      "contact.p": "Send the brief or the job description and you'll get a reply within one working day. Full work is on Behance, and the résumé is available as a printable page.",
      "contact.be": "Message me on Behance", "contact.gh": "GitHub", "contact.cv": "Résumé",
      "contact.avail": "Available for new work",
      "foot.tag": "Arabic ad design · Mecca, Saudi Arabia",
      "foot.rights": "All designs copyright Muhammed — 2024 to 2026.",
      "lb.prev": "Previous design", "lb.next": "Next design", "lb.close": "Close",
      "lb.cat": "Sector", "lb.year": "Year", "lb.size": "Original size", "lb.fmt": "Formats",
      "lb.be": "View on Behance", "lb.alt": "Other formats of this design",
      "lb.of": "design",
      "alt.img": "Advertising design",
      "cv.h": "Résumé",
      "lang.btn": "عربي",
    },
  };

  var SKILLS = {
    ar: ["تصميم إعلانات السوشيال", "التايبوغرافي العربي", "تكوين ودمج المنتجات والأطعمة", "هوية بصرية وأنظمة سوشيال", "مقاسات متعددة لكل حملة", "صور خام بالذكاء الاصطناعي", "معالجة ورفع جودة الصور"],
    en: ["Social ad design", "Arabic typography", "Product & food compositing", "Visual identity & social systems", "Multi-format campaign delivery", "AI-assisted stock imagery", "Retouching & upscaling"],
  };
  var TOOLS = ["Adobe Photoshop", "Adobe Illustrator", "ImageFX", "Whisk AI", "UpScayl"];
  var FIELDS = { ar: ["التصميم الجرافيكي", "الإعلان", "التصوير"], en: ["Graphic design", "Advertising", "Photography"] };

  var BE = "https://www.behance.net/M_Designer_Original";
  var GH = "https://github.com/Robliation";

  var ORIENT = {
    ar: { square: "مربع", portrait: "طولي", landscape: "عرضي" },
    en: { square: "square", portrait: "portrait", landscape: "landscape" },
  };
  function orient(o) { return (ORIENT[lang] && ORIENT[lang][o]) || o; }

  /* ------------------------------------------------------------------ state */
  var lang = "ar";
  try { lang = localStorage.getItem("md.lang") === "en" ? "en" : "ar"; } catch (e) {}
  try {
    var q = new URLSearchParams(location.search).get("lang");
    if (q === "en" || q === "ar") lang = q;
  } catch (e) {}
  var cat = "all";
  var query = "";
  var lastFocus = null;
  var openList = [];
  var openIdx = 0;

  function t(k) { return (T[lang] && T[lang][k]) || T.en[k] || k; }
  function num(n) { return String(n); }
  function el(s) { var d = document.createElement("div"); d.innerHTML = s; return d; }

  /* ------------------------------------------------------------------ render */
  function pic(stem, w, h, alt, lazy, cls) {
    return '<picture><source type="image/webp" srcset="' + stem + '.webp">' +
      '<img src="' + stem + '.jpg" width="' + w + '" height="' + h + '" alt="' + alt + '"' +
      (lazy ? ' loading="lazy" decoding="async"' : ' decoding="async"') +
      (cls ? ' class="' + cls + '"' : "") + "></picture>";
  }

  /* the lightbox sizes its image against the stage, so it uses a bare img, not picture */
  var WEBP = false;
  try { WEBP = document.createElement("canvas").toDataURL("image/webp").indexOf("data:image/webp") === 0; } catch (e) {}
  function stagePic(stem, w, h, alt) {
    return '<img src="' + stem + (WEBP ? ".webp" : ".jpg") + '" width="' + w + '" height="' + h +
      '" alt="' + alt + '" decoding="async">';
  }

  function heroBoard() {
    var picks = ["albaik-crispy-chicken", "almarai-real-watermelon", "kinza-cola-splash", "tazaj-city-of-crispy"];
    var host = document.getElementById("board");
    var out = "";
    picks.forEach(function (id) {
      var w = byId(id); if (!w) return;
      var im = w.imgs[0];
      out += '<a class="tile" href="#work/' + id + '" aria-label="' + esc(w.brand[lang]) + " — " + esc(w.tag[lang]) + '">' +
        pic("assets/img/" + im.stem + "-thumb", im.tw, im.th, altFor(w), true) + "</a>";
    });
    host.innerHTML = out + '<div class="board-meta"><span>' + t("board.meta") + " <b>" + num(D.meta.totalWorks) + "</b> " +
      esc(t("fact.works")) + "</span><span><b>" + num(D.meta.brands) + "</b> " + esc(t("fact.brands")) + "</span></div>";
  }

  function ticker() {
    var counts = brandCounts();
    var names = counts.map(function (c) { return c[lang === "ar" ? "ar" : "en"]; });
    var one = names.map(function (n) { return '<span class="ticker-item">' + esc(n) + "</span>"; }).join("");
    document.getElementById("ticker-track").innerHTML = one + one;
  }

  function brandCounts() {
    var m = {};
    D.works.forEach(function (w) {
      var k = w.brand.en;
      if (!m[k]) m[k] = { en: w.brand.en, ar: w.brand.ar, n: 0, cat: w.cat };
      m[k].n++;
    });
    return Object.keys(m).map(function (k) { return m[k]; })
      .sort(function (a, b) { return b.n - a.n || a.en.localeCompare(b.en); });
  }

  function filtered() {
    var q = query.trim().toLowerCase();
    return D.works.filter(function (w) {
      if (cat !== "all" && w.cat !== cat) return false;
      if (!q) return true;
      return (w.brand.ar + " " + w.brand.en + " " + w.tag.ar + " " + w.tag.en).toLowerCase().indexOf(q) > -1;
    });
  }

  function grid() {
    var list = filtered();
    openList = list.map(function (w) { return w.id; });
    var host = document.getElementById("works");
    if (!list.length) {
      host.innerHTML = '<div class="empty-state"><b>' + esc(t("work.empty.t")) + "</b>" + esc(t("work.empty.d")) +
        '<div style="margin-top:16px"><button class="chip" id="reset-filters">' + esc(t("work.reset")) + "</button></div></div>";
      document.getElementById("reset-filters").addEventListener("click", function () {
        cat = "all"; query = ""; document.getElementById("search").value = "";
        renderChips(); grid();
      });
    } else {
      host.innerHTML = list.map(function (w, i) {
        var im = w.imgs[0];
        return '<a class="work-card rv" href="#work/' + w.id + '" data-id="' + w.id + '" style="transition-delay:' +
          Math.min(i % 8, 7) * 35 + 'ms" aria-label="' + esc(t("lb.of")) + ": " + esc(w.brand[lang]) + " — " + esc(w.tag[lang]) + '">' +
          (w.behance ? '<span class="badge-be">Behance</span>' : "") +
          '<span class="crop"><i></i><i></i><i></i><i></i></span>' +
          pic("assets/img/" + im.stem + "-thumb", im.tw, im.th, altFor(w), true) +
          '<span class="work-cap"><span class="b">' + esc(w.brand[lang]) + "</span>" +
          '<span class="g">' + esc(w.tag[lang]) + "</span>" +
          '<span class="m">' + esc(t("lb.cat")) + " · " + esc(D.cats[w.cat][lang]) + " · " + num(w.year) + "</span></span></a>";
      }).join("");
      observeReveals(host);
    }
    document.getElementById("count").textContent =
      t("work.showing") + " " + num(list.length) + " " + t("work.of") + " " + num(D.works.length) + " " + t("fact.works");
    document.getElementById("grid-live").textContent = num(list.length) + " " + t("fact.works");
  }

  function renderChips() {
    var host = document.getElementById("chips");
    var counts = {};
    D.works.forEach(function (w) { counts[w.cat] = (counts[w.cat] || 0) + 1; });
    var out = '<button class="chip" data-cat="all" aria-pressed="' + (cat === "all") + '">' + esc(t("work.all")) +
      '<span class="c">' + num(D.works.length) + "</span></button>";
    Object.keys(D.cats).forEach(function (k) {
      if (!counts[k]) return;
      out += '<button class="chip" data-cat="' + k + '" aria-pressed="' + (cat === k) + '">' + esc(D.cats[k][lang]) +
        '<span class="c">' + num(counts[k]) + "</span></button>";
    });
    host.innerHTML = out;
  }

  function brandIndex() {
    var counts = brandCounts();
    document.getElementById("brand-index").innerHTML = counts.map(function (c) {
      return '<div class="index-cell"><span class="nm">' + esc(c[lang]) + '</span><span class="ct">' + num(c.n) + "</span></div>";
    }).join("");
  }

  function facts() {
    var fmts = 3;
    var rows = [[D.meta.totalWorks, "fact.works"], [D.meta.brands, "fact.brands"],
      [Object.keys(D.cats).length, "fact.fields"], [fmts, "fact.formats"]];
    document.getElementById("facts").innerHTML = rows.map(function (r) {
      return '<div class="fact"><div class="n">' + num(r[0]) + '</div><div class="l">' + esc(t(r[1])) + "</div></div>";
    }).join("");
  }

  function about() {
    document.getElementById("skills").innerHTML = SKILLS[lang].map(function (s) {
      return '<span class="tag' + (s === SKILLS[lang][0] || s === SKILLS[lang][1] ? " hot" : "") + '">' + esc(s) + "</span>";
    }).join("");
    document.getElementById("tools").innerHTML = TOOLS.map(function (s) { return '<span class="tag">' + esc(s) + "</span>"; }).join("");
    document.getElementById("fields").innerHTML = FIELDS[lang].map(function (s) { return '<span class="tag">' + esc(s) + "</span>"; }).join("");
  }


  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function altFor(w) {
    return w.brand[lang] + " — " + w.tag[lang] + (lang === "ar" ? " (تصميم إعلاني)" : " (advertising design)");
  }
  function byId(id) { for (var i = 0; i < D.works.length; i++) if (D.works[i].id === id) return D.works[i]; return null; }

  /* ------------------------------------------------------------------ i18n */
  function applyLang() {
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n]"), function (n) {
      var v = t(n.getAttribute("data-i18n"));
      if (n.hasAttribute("data-html")) n.innerHTML = v; else n.textContent = v;
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-aria]"), function (n) {
      n.setAttribute("aria-label", t(n.getAttribute("data-i18n-aria")));
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-ph]"), function (n) {
      n.setAttribute("placeholder", t(n.getAttribute("data-i18n-ph")));
    });
    document.title = t("title");
    var md = document.querySelector('meta[name="description"]'); if (md) md.setAttribute("content", t("desc"));
    var og = document.querySelector('meta[property="og:title"]'); if (og) og.setAttribute("content", t("title"));
    var ogd = document.querySelector('meta[property="og:description"]'); if (ogd) ogd.setAttribute("content", t("desc"));
    document.getElementById("lang-btn").textContent = t("lang.btn");
    document.getElementById("brand-txt").textContent = lang === "ar" ? "محمد" : "M DESIGNER";
    heroBoard(); ticker(); facts(); about(); brandIndex(); renderChips(); grid();
    try { localStorage.setItem("md.lang", lang); } catch (e) {}
  }

  /* ------------------------------------------------------------------ lightbox */
  function openProof(id, imgIx) {
    var w = byId(id); if (!w) return;
    var list = filtered();
    openList = list.map(function (x) { return x.id; });
    openIdx = Math.max(0, openList.indexOf(id));
    var dl = document.getElementById("proof");
    lastFocus = document.activeElement;
    paintProof(w, imgIx || 0);
    if (typeof dl.showModal === "function") dl.showModal(); else dl.setAttribute("open", "");
    document.body.style.overflow = "hidden";
    document.getElementById("proof-close").focus();
  }

  function paintProof(w, ix) {
    var im = w.imgs[ix] || w.imgs[0];
    var stage = document.getElementById("proof-img");
    stage.innerHTML = stagePic("assets/img/" + im.stem, im.fw, im.fh, altFor(w));
    document.getElementById("proof-brand").textContent = w.brand[lang];
    document.getElementById("proof-tag").textContent = w.tag[lang];
    document.getElementById("proof-cat").textContent = D.cats[w.cat][lang];
    document.getElementById("proof-year").textContent = num(w.year);
    document.getElementById("proof-size").textContent = im.orig;
    document.getElementById("proof-fmt").textContent = w.imgs.map(function (x) { return orient(x.orient); }).join(" · ");
    document.getElementById("proof-idx").textContent =
      num(openList.indexOf(w.id) + 1) + (lang === "ar" ? " من " : " / ") + num(openList.length);
    var be = document.getElementById("proof-be");
    if (w.behance) { be.href = w.behance; be.hidden = false; } else { be.hidden = true; }
    var alts = document.getElementById("proof-alts");
    if (w.imgs.length > 1) {
      alts.innerHTML = '<span class="mono-label">' + esc(t("lb.alt")) + "</span>" + w.imgs.map(function (x, i) {
        return '<button class="alt-thumb" data-ix="' + i + '" aria-current="' + (i === ix) + '" aria-label="' +
          esc(orient(x.orient)) + '">' + pic("assets/img/" + x.stem + "-thumb", x.tw, x.th, w.brand[lang] + " " + orient(x.orient), true) + "</button>";
      }).join("");
      alts.hidden = false;
    } else { alts.hidden = true; alts.innerHTML = ""; }
    document.getElementById("proof-root").dataset.id = w.id;
    document.getElementById("proof-root").dataset.ix = ix;
  }

  function step(d) {
    if (!openList.length) return;
    openIdx = (openIdx + d + openList.length) % openList.length;
    var w = byId(openList[openIdx]);
    if (w) { paintProof(w, 0); history.replaceState(null, "", "#work/" + w.id); }
  }
  function closeProof() {
    var dl = document.getElementById("proof");
    if (typeof dl.close === "function") dl.close(); else dl.removeAttribute("open");
    document.body.style.overflow = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus();
    if (location.hash.indexOf("#work/") === 0) history.replaceState(null, "", location.pathname + location.search);
  }

  /* ------------------------------------------------------------------ reveal */
  var io;
  function observeReveals(root) {
    if (!("IntersectionObserver" in window)) {
      Array.prototype.forEach.call((root || document).querySelectorAll(".rv"), function (n) { n.classList.add("in"); });
      return;
    }
    if (!io) io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "60px 0px", threshold: 0.05 });
    Array.prototype.forEach.call((root || document).querySelectorAll(".rv:not(.in)"), function (n) { io.observe(n); });
  }

  /* ------------------------------------------------------------------ wire */
  function boot() {
    document.getElementById("be-link").href = BE;
    document.getElementById("gh-link").href = GH;
    document.getElementById("foot-be").href = BE;
    document.getElementById("foot-gh").href = GH;

    applyLang();

    document.getElementById("lang-btn").addEventListener("click", function () {
      lang = lang === "ar" ? "en" : "ar"; applyLang();
    });
    document.getElementById("chips").addEventListener("click", function (e) {
      var b = e.target.closest("[data-cat]"); if (!b) return;
      cat = b.getAttribute("data-cat"); renderChips(); grid();
    });
    var s = document.getElementById("search");
    s.addEventListener("input", function () { query = s.value; grid(); });

    document.getElementById("works").addEventListener("click", function (e) {
      var a = e.target.closest(".work-card"); if (!a) return;
      e.preventDefault(); openProof(a.dataset.id, 0);
    });
    document.getElementById("board").addEventListener("click", function (e) {
      var a = e.target.closest(".tile"); if (!a) return;
      e.preventDefault(); openProof(a.getAttribute("href").split("/").pop(), 0);
    });

    document.getElementById("proof-close").addEventListener("click", closeProof);
    document.getElementById("proof-prev").addEventListener("click", function () { step(-1); });
    document.getElementById("proof-next").addEventListener("click", function () { step(1); });
    document.getElementById("proof-alts").addEventListener("click", function (e) {
      var b = e.target.closest("[data-ix]"); if (!b) return;
      var w = byId(document.getElementById("proof-root").dataset.id);
      if (w) paintProof(w, +b.dataset.ix);
    });
    document.getElementById("proof").addEventListener("click", function (e) {
      if (e.target === this || e.target.id === "proof-img") closeProof();
    });
    document.getElementById("proof").addEventListener("keydown", function (e) {
      var rtl = lang === "ar";
      if (e.key === "ArrowRight") { e.preventDefault(); step(rtl ? -1 : 1); }
      if (e.key === "ArrowLeft") { e.preventDefault(); step(rtl ? 1 : -1); }
      if (e.key === "Home") { e.preventDefault(); openIdx = -1; step(1); }
      if (e.key === "End") { e.preventDefault(); openIdx = openList.length - 2; step(1); }
      if (e.key === "Escape") { e.preventDefault(); closeProof(); }
    });

    observeReveals(document);
    requestAnimationFrame(function () { document.body.classList.add("loaded"); });
    setTimeout(function () { document.body.classList.add("loaded"); }, 500);

    if (location.hash.indexOf("#work/") === 0) {
      var id = location.hash.slice(6);
      if (byId(id)) setTimeout(function () { openProof(id, 0); }, 260);
    }
    window.addEventListener("hashchange", function () {
      if (location.hash.indexOf("#work/") === 0) {
        var id = location.hash.slice(6);
        if (byId(id)) openProof(id, 0);
      }
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
