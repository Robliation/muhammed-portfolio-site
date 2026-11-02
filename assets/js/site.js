/* Muhammad Al-Masri — bilingual portfolio: logos, filtering, proof lightbox, scroll motion */
(function () {
  "use strict";
  var D = window.MD_DATA;
  if (!D) return;
  var LOGOS = window.MD_BRANDS || {};

  /* Brands that are not clients, so they stay out of the "designed for" wall. */
  var NOT_A_CLIENT = { "Self-initiated": 1 };

  /* ------------------------------------------------------------------ copy */
  var T = {
    ar: {
      title: "محمد المصري — مصمم جرافيك وإعلانات السوشيال ميديا في مكة المكرمة | بورتفوليو 2026",
      desc: "بورتفوليو محمد المصري، مصمم جرافيك في مكة المكرمة متخصص في تصميم إعلانات السوشيال ميديا بالعربي: 63 تصميمًا إعلانيًا لأكثر من 35 علامة تجارية في المطاعم والأغذية والمشروبات والتجزئة والسياحة. متاح للتوظيف.",
      "nav.work": "الأعمال", "nav.craft": "الحرفة", "nav.tools": "الأدوات", "nav.about": "نبذة",
      "nav.brands": "العلامات", "nav.path": "المسار", "nav.cv": "السيرة", "nav.contact": "تواصل",
      "hero.eyebrow": "محمد المصري · مصمم جرافيك وإعلانات السوشيال ميديا · مكة المكرمة، السعودية",
      "hero.line1": "تصميم إعلانات",
      "hero.line2": "توقف <em>التمرير</em>",
      "hero.lede": "أصمّم إعلانات سوشيال ميديا بالعربي للعلامات التجارية في السعودية: جملة عربية تُقرأ في ثانية، منتج يبدو شهياً، وتكوين يحمل الفكرة كاملة. 63 تصميمًا إعلانيًا لأكثر من 35 علامة في المطاعم والأغذية والمشروبات والتجزئة والسياحة، مُسلَّمة بالمقاسات المربعة والطولية والعرضية لكل حملة.",
      "hero.cta1": "شاهد الأعمال", "hero.cta2": "حمّل السيرة", "hero.cta3": "راسلني بالبريد",
      "fact.works": "تصميم", "fact.brands": "علامة تجارية", "fact.fields": "مجال", "fact.formats": "مقاسات",
      "board.tag": "أحدث الأعمال", "board.meta": "4 من أصل",
      "strip.label": "أكثر من 35+ علامة تجارية صممت لها",
      "strip.sub": "شعارات العلامات المعروضة هنا ملك أصحابها وتُعرض للتعريف بأعمال التصميم.",
      "work.n": "الأعمال", "work.h": "كل التصاميم في مكان واحد",
      "work.lede": "تصفّى حسب المجال أو ابحث باسم العلامة التجارية. كل تصميم يفتح كبروفة كاملة الحجم مع مقاسه الأصلي وكل نسخ الحملة.",
      "work.search": "ابحث باسم العلامة أو النص…", "work.all": "الكل",
      "work.showing": "عرض", "work.of": "من", "work.reset": "إعادة التصفية",
      "work.empty.t": "ما فيه نتيجة", "work.empty.d": "جرّب اسم علامة آخر أو مجال مختلف.",
      "craft.n": "الحرفة", "craft.h": "ما الذي يفصل إعلانًا يعمل عن إعلان جميل فقط",
      "craft.lede": "ثلاث حِرف أطبّقها في كل مشروع تصميم جرافيك: تركيب الطعام، التايبوغرافي العربي، والحملات الموسمية.",
      "craft.1.t": "تركيب المنتجات والطعام",
      "craft.1.d": "المنتج هو البطل. أشتغل على القصّ الدقيق، والرمي والانعكاس، وإضاءة تجعل الطعم يُحس قبل أن يُقرأ النص — ثم أوحّد لون المنتج مع خلفية الإعلان حتى لا يظهر كمقطوع ملصق. أغلب أعمالي في إعلانات المطاعم والأغذية مبنية على هذه المرحلة وحدها.",
      "craft.2.t": "التايبوغرافي العربي",
      "craft.2.d": "الجملة العربية لها وزن ومزاج ومسافة. أوزّع النص على الكادر بحيث تُقرأ الكلمة الأولى قبل الصورة، وأوازن بين حجم الخط ووزنه وحرّكته، وأبقي المساحة السلبية تخدم الجملة بدل ما تزاحمها. هذا هو الفرق بين بوست يُفهم في ثانية وبوست يحتاج شرح.",
      "craft.3.t": "المواسم والحملات",
      "craft.3.d": "رمضان والأعياد ومواسم العروض هي أعلى الشراء على السوشيال ميديا في السعودية. أصمّم لكل موسم بلغته البصرية — زخرفة وهلال وذهبي في رمضان، وفرح وألوان في العيد — وأسلّم الحملة كاملة بالمقاسات المربعة والطولية والعرضية جاهزة للنشر.",
      "craft.view": "شاهد أعمال هذا المجال",
      "tools.n": "الأدوات", "tools.h": "أعمل على الأدوات التي يعرفها فريق التسويق",
      "tools.lede": "من الفكرة إلى التسليم النهائي: تصميم ثابت، هوية، مونتاج فيديو، وصور خام بالذكاء الاصطناعي أُعالجها يدويًا قبل النشر.",
      "tools.ps.y": "3+ سنوات", "tools.ps.d": "الاعتماد الأساسي: تركيب المنتجات والطعام، تصحيح وتوحيد الألوان، تنقية الصور، وتجهيز الطباعة والنشر بكل المقاسات.",
      "tools.ai.y": "2+ سنتان", "tools.ai.d": "الشعارات والأنظمة المتجهية، إطار البوست الموحّد، الأيقونات، وتخطيط الإعلانات التي تحتاج دقة في الحواف والتكرار.",
      "tools.capcut.y": "2+ سنتان", "tools.capcut.d": "تعديل ومونتاج الفيديو الإعلاني بشكل احترافي: قصّ عمودي للسوشيال، توقيت على الموسيقى، نصوص متحركة، وتجهيز الريلز والستوري.",
      "tools.gemini.y": "سنتان", "tools.gemini.d": "إنتاج الصور الخام بالذكاء الاصطناعي عبر نماذج Google — Nano Banana 2 وNano Banana Pro — ثم معالجتها يدويًا في Photoshop حتى تكون قابلة للنشر على حساب العلامة.",
      "about.n": "نبذة", "about.h": "مين محمد المصري؟",
      "about.p1": "أنا <strong>محمد المصري</strong>، مصمم جرافيك في <strong>مكة المكرمة</strong>. تخصصي هو <strong>تصميم إعلانات السوشيال ميديا بالعربي</strong> — البوست اللي يوقف الشخص وهو يمرر، ويخليه يحس بالطعم قبل ما يقرأ النص. أشتغل مع العلامات التجارية في السعودية على منشورات السوشيال ميديا الثابتة والمتحركة، بنرات الحملات، ومحتوى المواسم.",
      "about.p2": "بدأت المسار سنة 2021 بتعلّم <strong>Adobe Photoshop</strong> و<strong>Adobe Illustrator</strong> بشكل ممنهج، ووصلت اليوم إلى إعلانات العلامات الكبيرة: ألبان، مطاعم، مشروبات، تجزئة، وسياحة. أعمل على Photoshop بأكثر من 3 سنوات ممارسة احترافية، وIllustrator بأكثر من سنتين، وأجهّز مونتاج الفيديو الإعلاني بـ<strong>CapCut</strong>.",
      "about.p3": "من سنتين أستخدم أدوات الذكاء الاصطناعي التوليدية من Google — <strong>Nano Banana 2</strong> و<strong>Nano Banana Pro</strong> — لإنتاج الصور الخام بسرعة، ثم أعالجها يدويًا في Photoshop: تصحيح الإضاءة، دمج المنتج الحقيقي، تنقية الحواف، ورفع الجودة حتى تصير الصورة قابلة للنشر على حساب العلامة.",
      "about.pull": "التصميم الجيد على السوشيال يُفهم في ثانية — ولا يشرح نفسه.",
      "about.skills": "المهارات", "about.fields": "المجالات الإبداعية",
      "about.spec.name": "الاسم", "about.spec.name.v": "محمد المصري · Muhammad Al-Masri",
      "about.spec.role": "المسمى", "about.spec.role.v": "مصمم جرافيك & إعلانات السوشيال ميديا",
      "about.spec.loc": "الموقع", "about.spec.loc.v": "مكة المكرمة، السعودية",
      "about.spec.exp": "الخبرة", "about.spec.exp.v": "مسار 5 سنوات · 3+ سنوات Photoshop · 2+ سنوات Illustrator وCapCut",
      "about.spec.mail": "البريد", "about.spec.lang": "اللغات", "about.spec.lang.v": "العربية (لغة أم) · الإنجليزية",
      "about.spec.avail": "متاح لـ", "about.spec.avail.v": "وظيفة بدوام كامل · مشاريع freelance · عمل عن بعد",
      "brands.n": "العلامات", "brands.h": "العلامات التجارية في الأعمال",
      "brands.lede": "أكثر من 35 علامة تجارية في السعودية والخليج صممت لها إعلانات، مرتبة حسب المجال مع عدد التصاميم لكل علامة. اضغط أي بطاقة لعرض أعمالها فقط.",
      "brands.note": "العلامات وشعاراتها ملك أصحابها، وتُعرض هنا للتعريف بأعمال التصميم فقط.",
      "brands.count": "تصميم", "brands.view": "شاهد أعمالها",
      "path.n": "المسار", "path.h": "من الهوية الشخصية إلى إعلان البراند",
      "path.lede": "خمس سنوات من 2021 إلى 2026: تعلّم ممنهج، ثم تطبيق على السوق، ثم بناء أسلوب إعلاني عربي واضح.",
      "path.1.y": "2021", "path.1.t": "البداية — تعلّم أساسيات Photoshop",
      "path.1.d": "بدأت Adobe Photoshop من الصفر: الطبقات، التحديد والقصّ، تصحيح الألوان، ودمج الصور. أول الأعمال كانت تجارب شخصية وتدريب طويل على تجهيز الصور وتنظيف حوافها.",
      "path.2.y": "2022", "path.2.t": "Photoshop بعمق — وأول هوية بصرية",
      "path.2.d": "انتقلت من الاستخدام إلى الإتقان: تركيب منتجات الطعام، ظلال وإضاءة مقنعة، وبناء أول هوية بصرية كاملة. في نفس السنة بدأت تعلّم Adobe Illustrator: المتجهات، الشعارات، والتخطيط الشبكي.",
      "path.3.y": "2023", "path.3.t": "أنظمة محتوى وسوشيال بالعربي",
      "path.3.d": "بنيت أنظمة بوستات ومقالات لهوية شخصية: إطار زخرفي موحّد، نسخ مربعة وطولية وعرضية لكل محتوى، وتجارب جدية على التايبوغرافي العربي والخط.",
      "path.4.y": "2024", "path.4.t": "احتراف Illustrator + مونتاج الفيديو بـCapCut",
      "path.4.d": "رسّخت Adobe Illustrator على الشعارات والأنظمة المتجهية، وأضفت مهارة جديدة: تعديل ومونتاج الفيديو الإعلاني عبر CapCut — قصّ عمودي، توقيت على الموسيقى، ونصوص متحركة للريلز والستوري.",
      "path.5.y": "2025", "path.5.t": "إعلانات العلامات السعودية والنشر على بيهاينس",
      "path.5.d": "انضممت إلى بيهاينس في فبراير 2025 وبدأت النشر المنتظم. أكثر من 60 إعلانًا للمراعي والبيك والطازج وجاهز وجرير وكينزا والقدية ودبي وغيرها، وفيها اكتمل أسلوب الإعلان العربي المربع والطولي والعرضي.",
      "path.6.y": "2026", "path.6.t": "الذكاء الاصطناعي التوليدي — واليوم",
      "path.6.d": "من سنتين أعمل على أدوات الذكاء الاصطناعي من Google — Nano Banana 2 وNano Banana Pro — لإنتاج الصور الخام ثم معالجتها يدويًا. أوسّع الأعمال على علامات جديدة وأسلّم كل حملة بكل المقاسات. متاح لوظيفة بدوام كامل أو مشاريع مستقلة أو عمل عن بعد.",
      "faq.n": "أسئلة", "faq.h": "أسئلة يسألها الأرباب والوكالات",
      "faq.q1": "من هو محمد المصري؟",
      "faq.a1": "مصمم جرافيك في مكة المكرمة، متخصص في تصميم إعلانات السوشيال ميديا بالعربي. قدّم 63 تصميمًا إعلانيًا لأكثر من 35 علامة تجارية سعودية في المطاعم والأغذية والمشروبات والتجزئة والسياحة.",
      "faq.q2": "ما البرامج التي يعمل عليها؟",
      "faq.a2": "Adobe Photoshop لأكثر من 3 سنوات، وAdobe Illustrator لأكثر من سنتين، وCapCut لتعديل ومونتاج الفيديو لأكثر من سنتين، إضافة إلى أدوات الذكاء الاصطناعي التوليدية من Google مثل Nano Banana 2 وNano Banana Pro.",
      "faq.q3": "هل يقبل عملًا عن بعد أو مشاريع مستقلة؟",
      "faq.a3": "نعم. متاح لوظيفة مصمم جرافيك بدوام كامل داخل السعودية أو عن بعد، وكذلك لمشاريع تصميم إعلانات السوشيال ميديا بالقطعة. التواصل عبر muhammedwork7623@gmail.com.",
      "faq.q4": "ما تخصصه الدقيق في التصميم الإعلاني؟",
      "faq.a4": "الإعلان الرقمي بالعربي للعلامات التجارية: بوست يوقف التمرير في ثانية، جملة عربية مقروءة بقوة، ومنتج طعام يبدو شهيًا داخل الكادر — مع تسليم كل حملة بالمقاسات المربعة والطولية والعرضية.",
      "faq.q5": "كم سنة خبرة لديه؟",
      "faq.a5": "بدأ تعلّم Photoshop وIllustrator عام 2021، أي خمس سنوات في المسار؛ منها أكثر من 3 سنوات ممارسة احترافية على Photoshop، وأكثر من سنتين على Illustrator ومونتاج الفيديو بـCapCut، وسنتين على أدوات الذكاء الاصطناعي التوليدية.",
      "faq.q6": "كيف يمكن للشركة توظيفه أو التعاقد معه؟",
      "faq.a6": "بريد واحد يكفي: muhammedwork7623@gmail.com مع وصف المشروع أو الوصف الوظيفي. الرد خلال يوم عمل، ومع البريد رابط هذا البورتفوليو وصفحة السيرة القابلة للتصدير PDF بصيغة ATS.",
      "contact.n": "تواصل", "contact.h": "تحتاج مصمم لحملتك الجاية؟",
      "contact.p": "أرسل تفاصيل المشروع أو الوصف الوظيفي على بريدي، وأرد عليك خلال يوم عمل. تقدر تشوف الأعمال كاملة على بيهاينس أو تفتح صفحة السيرة القابلة للتصدير PDF.",
      "contact.mail": "راسلني بالبريد", "contact.be": "Behance", "contact.cv": "حمّل السيرة",
      "contact.avail": "متاح لاستلام عمل جديد",
      "foot.tag": "تصميم إعلانات بالعربي · مكة المكرمة", "foot.elsewhere": "في مكان آخر",
      "foot.rights": "جميع التصاميم ملك محمد المصري.",
      "lb.close": "إغلاق", "lb.prev": "السابق", "lb.next": "التالي", "lb.of": "عمل",
      "lb.cat": "المجال", "lb.year": "السنة", "lb.size": "المقاس الأصلي", "lb.fmt": "المقاسات",
      "lb.be": "مشاهده على بيهاينس", "lb.alt": "بقية مقاسات هذا التصميم",
      "lang.btn": "EN",
    },
    en: {
      title: "Muhammad Al-Masri — Graphic Designer & Social Advertising, Mecca, Saudi Arabia",
      desc: "Portfolio of Muhammad Al-Masri, a graphic designer in Mecca, Saudi Arabia, specialising in Arabic social media advertising design: 63 ad designs for 35+ brands in food, dairy, drinks, retail and tourism. Photoshop, Illustrator, CapCut and generative AI. Available for hire.",
      "nav.work": "Work", "nav.craft": "Craft", "nav.tools": "Tools", "nav.about": "About",
      "nav.brands": "Brands", "nav.path": "Path", "nav.cv": "Résumé", "nav.contact": "Contact",
      "hero.eyebrow": "Muhammad Al-Masri · Graphic Designer & Social Advertising · Mecca, Saudi Arabia",
      "hero.line1": "Ads that",
      "hero.line2": "<em>stops the scroll</em>",
      "hero.lede": "I design Arabic social media advertising for brands across Saudi Arabia: a line that reads in one second, a product that looks appetising, and a composition that carries the whole idea. 63 advertising designs for 35+ brands in food, dairy, drinks, retail and tourism — every campaign shipped square, portrait and landscape.",
      "hero.cta1": "See the work", "hero.cta2": "Download résumé", "hero.cta3": "Email me",
      "fact.works": "designs", "fact.brands": "brands", "fact.fields": "sectors", "fact.formats": "formats",
      "board.tag": "Latest work", "board.meta": "4 of",
      "strip.label": "Designed for 35+ brands",
      "strip.sub": "Client logos shown here belong to their owners and appear only to identify the design work.",
      "work.n": "Work", "work.h": "Every design in one place",
      "work.lede": "Filter by sector or search a brand name. Each design opens as a full-size proof with its original pixel size and every format in the campaign.",
      "work.search": "Search a brand or headline…", "work.all": "All",
      "work.showing": "Showing", "work.of": "of", "work.reset": "Reset filters",
      "work.empty.t": "Nothing matches", "work.empty.d": "Try another brand or sector.",
      "craft.n": "Craft", "craft.h": "What separates an ad that works from an ad that only looks nice",
      "craft.lede": "Three crafts I apply to every design: food compositing, Arabic typography, and seasonal campaigns.",
      "craft.1.t": "Product & food compositing",
      "craft.1.d": "The product is the hero. I work on clean cut-outs, believable shadow and reflection, and lighting that makes the taste land before the copy is read — then I match the product colour into the ad background so it never reads as a pasted cut-out. Most of my restaurant and food advertising is won or lost at this stage.",
      "craft.2.t": "Arabic typography",
      "craft.2.d": "An Arabic line has weight, mood and spacing. I set the text in the frame so the first word lands before the image does, balancing size, weight and movement against each other, and letting negative space serve the line instead of competing with it. That is the difference between a post that reads in a second and one that needs explaining.",
      "craft.3.t": "Seasons & campaigns",
      "craft.3.d": "Ramadan, Eid and offer seasons drive the highest social purchase intent in Saudi Arabia. I design each season in its own visual language — ornament, crescent and gold for Ramadan, joy and colour for Eid — and deliver the campaign square, portrait and landscape, ready to publish.",
      "craft.view": "See work in this area",
      "tools.n": "Tools", "tools.h": "The tools a marketing team already recognises",
      "tools.lede": "From idea to final delivery: static design, identity systems, video editing, and AI-generated raw imagery I retouch by hand before it ships.",
      "tools.ps.y": "3+ years", "tools.ps.d": "My main workspace: product and food compositing, colour correction and matching, image cleanup, and print- and web-ready output in every size.",
      "tools.ai.y": "2+ years", "tools.ai.d": "Vector marks and systems, the unified post frame, iconography, and any layout that needs exact edges and repeatable geometry.",
      "tools.capcut.y": "2+ years", "tools.capcut.d": "Professional video editing and montage for advertising: vertical cuts for social, timing to music, animated type, and reels and stories delivery.",
      "tools.gemini.y": "2 years", "tools.gemini.d": "Raw image generation with Google's models — Nano Banana 2 and Nano Banana Pro — then hand-retouched in Photoshop until the frame is publishable on a brand account.",
      "about.n": "About", "about.h": "Who is Muhammad Al-Masri?",
      "about.p1": "I am <strong>Muhammad Al-Masri</strong>, a graphic designer based in <strong>Mecca, Saudi Arabia</strong>. My specialty is <strong>Arabic social media advertising design</strong> — the post that stops someone mid-scroll and makes them taste the product before reading a word. I work with Saudi brands on static and motion posts, campaign banners and seasonal content.",
      "about.p2": "The path started in 2021 with systematic learning of <strong>Adobe Photoshop</strong> and <strong>Adobe Illustrator</strong>, and today reaches the big brand accounts: dairy, restaurants, beverages, retail and tourism. That is 3+ years of professional Photoshop practice, 2+ years in Illustrator, and advertising video edited in <strong>CapCut</strong>.",
      "about.p3": "For two years I have used Google's generative image tools — <strong>Nano Banana 2</strong> and <strong>Nano Banana Pro</strong> — to produce raw imagery fast, then retouch it by hand in Photoshop: fixing light, compositing the real product, cleaning edges and raising quality until the image is fit to publish on the brand's own account.",
      "about.pull": "Good social design is understood in a second — it never has to explain itself.",
      "about.skills": "Capabilities", "about.fields": "Creative fields",
      "about.spec.name": "Name", "about.spec.name.v": "Muhammad Al-Masri · محمد المصري",
      "about.spec.role": "Role", "about.spec.role.v": "Graphic Designer & Social Advertising",
      "about.spec.loc": "Location", "about.spec.loc.v": "Mecca, Saudi Arabia",
      "about.spec.exp": "Experience", "about.spec.exp.v": "5-year path · 3+ years Photoshop · 2+ years Illustrator and CapCut",
      "about.spec.mail": "Email", "about.spec.lang": "Languages", "about.spec.lang.v": "Arabic (native) · English",
      "about.spec.avail": "Available for", "about.spec.avail.v": "Full-time role · freelance projects · remote work",
      "brands.n": "Brands", "brands.h": "The brands in the work",
      "brands.lede": "Advertising designed for 35+ brands across Saudi Arabia and the Gulf, grouped by sector with the number of designs each one has. Tap any card to show only its work.",
      "brands.note": "All brands and their logos are the property of their owners and are shown here only to identify the design work.",
      "brands.count": "designs", "brands.view": "See their work",
      "path.n": "Path", "path.h": "From a personal identity to brand advertising",
      "path.lede": "Five years from 2021 to 2026: systematic learning, then real market application, then a clear Arabic advertising style.",
      "path.1.y": "2021", "path.1.t": "Start — Photoshop fundamentals",
      "path.1.d": "Adobe Photoshop from zero: layers, selection and cut-outs, colour correction, and compositing. The first output was personal experiments and long practice preparing and cleaning images.",
      "path.2.y": "2022", "path.2.t": "Photoshop in depth — first visual identity",
      "path.2.d": "Moved from using Photoshop to mastering it: food compositing, believable shadow and light, and the first complete visual identity. Adobe Illustrator started the same year — vectors, marks and grid systems.",
      "path.3.y": "2023", "path.3.t": "Arabic content and social systems",
      "path.3.d": "Built post and article systems for a personal brand: one decorative frame, square, portrait and landscape variants for every piece, and serious work on Arabic typography.",
      "path.4.y": "2024", "path.4.t": "Illustrator to a professional level + CapCut video",
      "path.4.d": "Consolidated Adobe Illustrator for marks and vector systems, and added a new skill: professional advertising video editing and montage in CapCut — vertical cuts, timing to music and animated type for reels and stories.",
      "path.5.y": "2025", "path.5.t": "Saudi brand advertising and publishing on Behance",
      "path.5.d": "Joined Behance in February 2025 and published consistently. Over 60 ads for Almarai, Al Baik, Tazaj, Jahez, Jarir, Kinza, Qiddiya and Dubai — and the square/portrait/landscape Arabic ad format became a system.",
      "path.6.y": "2026", "path.6.t": "Generative AI — and today",
      "path.6.d": "Two years working with Google's AI image models — Nano Banana 2 and Nano Banana Pro — for raw imagery, then hand-retouched. Expanding to new brands and shipping every campaign in all formats. Open to a full-time role, freelance projects or remote work.",
      "faq.n": "FAQ", "faq.h": "Questions employers and agencies ask",
      "faq.q1": "Who is Muhammad Al-Masri?",
      "faq.a1": "A graphic designer in Mecca, Saudi Arabia, specialising in Arabic social media advertising design. 63 advertising designs delivered for more than 35 Saudi brands across restaurants, food, beverages, retail and tourism.",
      "faq.q2": "Which software does he work in?",
      "faq.a2": "Adobe Photoshop for 3+ years, Adobe Illustrator for 2+ years, and CapCut for professional video editing and montage for 2+ years — plus Google's generative image tools, Nano Banana 2 and Nano Banana Pro, for raw imagery that is then retouched by hand.",
      "faq.q3": "Does he take remote work or freelance projects?",
      "faq.a3": "Yes. Open to a full-time graphic design role in Saudi Arabia or remotely, and to piece-work on social advertising. Contact via muhammedwork7623@gmail.com.",
      "faq.q4": "What exactly is his advertising specialty?",
      "faq.a4": "Arabic digital advertising for brands: a post that stops the scroll in one second, an Arabic line with real typographic weight, and a food product that looks appetising in frame — delivered square, portrait and landscape.",
      "faq.q5": "How many years of experience?",
      "faq.a5": "The path began in 2021, so five years overall: 3+ years of professional Photoshop practice, 2+ years of Illustrator and CapCut video editing, and 2 years with generative AI image tools.",
      "faq.q6": "How does a company hire or brief him?",
      "faq.a6": "One email is enough: muhammedwork7623@gmail.com with the project brief or the job description. A reply within one working day, with this portfolio and a résumé page that exports to an ATS-readable PDF.",
      "contact.n": "Contact", "contact.h": "Need a designer for your next campaign?",
      "contact.p": "Send the brief or the job description to my email and you'll get a reply within one working day. The full work is on Behance, and the résumé exports as a printable PDF.",
      "contact.mail": "Email me", "contact.be": "Behance", "contact.cv": "Download résumé",
      "contact.avail": "Available for new work",
      "foot.tag": "Arabic advertising design · Mecca", "foot.elsewhere": "Elsewhere",
      "foot.rights": "All designs belong to Muhammad Al-Masri.",
      "lb.close": "Close", "lb.prev": "Previous", "lb.next": "Next", "lb.of": "work",
      "lb.cat": "Sector", "lb.year": "Year", "lb.size": "Original size", "lb.fmt": "Formats",
      "lb.be": "View on Behance", "lb.alt": "Other formats of this design",
      "lang.btn": "ع",
    },
  };

  var SKILLS = {
    ar: ["تصميم إعلانات السوشيال ميديا", "التايبوغرافي العربي", "تركيب ودمج المنتجات والأطعمة", "هوية بصرية وأنظمة سوشيال", "مونتاج الفيديو الإعلاني بـCapCut", "مقاسات متعددة لكل حملة", "صور خام بالذكاء الاصطناعي", "معالجة ورفع جودة الصور", "تصميم بنرات الحملات", "إعلانات رمضان والأعياد"],
    en: ["Social media ad design", "Arabic typography", "Product & food compositing", "Visual identity & social systems", "Advertising video editing (CapCut)", "Multi-format campaign delivery", "AI-assisted raw imagery", "Retouching & upscaling", "Campaign banner design", "Ramadan & Eid advertising"],
  };
  var FIELDS = {
    ar: ["التصميم الجرافيكي", "الإعلان الرقمي", "إعلانات المطاعم والأغذية", "هوية بصرية", "مونتاج فيديو", "التصوير"],
    en: ["Graphic design", "Digital advertising", "Food & restaurant advertising", "Visual identity", "Video editing", "Photography"],
  };

  var BE = "https://www.behance.net/M_Designer_Original";

  var TOOLS = [
    { key: "ps", badge: "ps", name: "Adobe Photoshop" },
    { key: "ai", badge: "ai", name: "Adobe Illustrator" },
    { key: "capcut", badge: "capcut", name: "CapCut" },
    { key: "gemini", badge: "gemini", name: "Nano Banana 2 · Nano Banana Pro" },
  ];

  var CRAFT = [
    { key: 1, cat: "food", ids: ["albaik-crispy-chicken", "tazaj-city-of-crispy", "sultan-fish-crispy", "national-poultry-mandi"] },
    { key: 2, cat: "fmcg", ids: ["almarai-royal-hummus", "burger-mish-best-in-world", "ful-wazir-exceptional", "just-samboosa-authentic"] },
    { key: 3, cat: "seasonal", ids: ["almarai-ramadan-kareem", "sadia-ramadan-offers", "vimto-ramadan-kareem", "jarir-eid-mubarak"] },
  ];

  var PATH_YEARS = [1, 2, 3, 4, 5, 6];
  var FAQ_Q = [1, 2, 3, 4, 5, 6];

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

  /* ------------------------------------------------------------------ brand marks */
  /* Official logo when we have one; otherwise a set typographic tile — never a blurry accept. */
  function logoImg(B, localName, cls) {
    var d = (B.w && B.h) ? ' width="' + num(B.w) + '" height="' + num(B.h) + '"' : "";
    return '<img class="logo-img' + (cls ? " " + cls : "") + '" src="assets/brands/' + B.file + '"' + d +
      ' alt="' + esc(localName) + '" loading="lazy" decoding="async">';
  }
  function mark(name, localName, cls) {
    var B = LOGOS[name];
    if (B && B.file) return logoImg(B, localName || name, cls);
    return '<span class="logo-wm' + (cls ? " " + cls : "") + '" aria-hidden="true">' + esc(localName || name) + "</span>";
  }

  /* In the brand cards the name is already printed beside the tile, so a missing logo
     shows a lettermark instead of repeating the same word twice. */
  function lettermark(name, localName) {
    var B = LOGOS[name];
    if (B && B.file) return logoImg(B, localName || name, "");
    return '<span class="logo-mono" aria-hidden="true">' + esc(String(localName || name).trim().charAt(0)) + "</span>";
  }

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
      out += '<a class="tile" href="#work/' + w.id + '" aria-label="' + esc(w.brand[lang]) + " — " + esc(w.tag[lang]) + '">' +
        pic("assets/img/" + im.stem + "-thumb", im.tw, im.th, altFor(w), false) + "</a>";
    });
    host.innerHTML = out + '<div class="board-meta"><span>' + t("board.meta") + " <b>" + num(D.meta.totalWorks) + "</b> " +
      esc(t("fact.works")) + "</span><span><b>" + num(clientBrandCount()) + "</b> " + esc(t("fact.brands")) + "</span></div>";
  }

  function clientBrandCount() {
    return brandCounts().filter(function (c) { return !NOT_A_CLIENT[c.en]; }).length;
  }

  function ticker() {
    var counts = brandCounts().filter(function (c) { return !NOT_A_CLIENT[c.en]; });
    var one = counts.map(function (c) {
      return '<span class="ticker-item"><span class="logo-slot">' + mark(c.en, c[lang]) + "</span></span>";
    }).join("");
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

  /* Brand wall: one card per client, logo first, grouped by sector. */
  function brandIndex() {
    var counts = brandCounts().filter(function (c) { return !NOT_A_CLIENT[c.en]; });
    var groups = {}, order = [];
    counts.forEach(function (c) {
      var g = D.cats[c.cat][lang];
      if (!groups[g]) { groups[g] = []; order.push(g); }
      groups[g].push(c);
    });
    document.getElementById("brand-index").innerHTML = order.map(function (g) {
      return '<div class="brand-group rv"><h3 class="brand-group-h">' + esc(g) + "</h3><div class=\"brand-group-in\">" +
        groups[g].map(function (c) {
          return '<button class="brand-card" type="button" data-brand="' + esc(c.en) + '">' +
            '<span class="brand-logo">' + lettermark(c.en, c[lang]) + "</span>" +
            '<span class="brand-meta"><span class="brand-nm">' + esc(c[lang]) + "</span>" +
            '<span class="brand-ct">' + num(c.n) + " " + esc(t("brands.count")) + "</span></span>" +
            '<span class="brand-go" aria-hidden="true">→</span></button>';
        }).join("") + "</div></div>";
    }).join("");
    observeReveals(document.getElementById("brand-index"));
  }

  function craftRows() {
    document.getElementById("craft-rows").innerHTML = CRAFT.map(function (c, i) {
      var works = c.ids.map(byId).filter(Boolean);
      var imgs = works.map(function (w) {
        var im = w.imgs[0];
        return '<a class="craft-shot" href="#work/' + w.id + '" aria-label="' + esc(w.brand[lang]) + " — " + esc(w.tag[lang]) + '">' +
          pic("assets/img/" + im.stem + "-thumb", im.tw, im.th, altFor(w), true) +
          '<span class="craft-shot-cap">' + esc(w.brand[lang]) + "</span></a>";
      }).join("");
      return '<article class="craft-row rv' + (i % 2 ? " flip" : "") + '">' +
        '<div class="craft-txt"><span class="craft-ix">' + num(i + 1) + " / " + num(CRAFT.length) + "</span>" +
        "<h3>" + esc(t("craft." + c.key + ".t")) + "</h3><p>" + esc(t("craft." + c.key + ".d")) + "</p>" +
        '<button class="link-btn" type="button" data-craft-cat="' + c.cat + '">' + esc(t("craft.view")) + " →</button></div>" +
        '<div class="craft-shots">' + imgs + "</div></article>";
    }).join("");
    observeReveals(document.getElementById("craft-rows"));
  }

  function toolGrid() {
    document.getElementById("tool-grid").innerHTML = TOOLS.map(function (x) {
      return '<article class="tool-card rv">' + badge(x.badge) +
        '<div class="tool-body"><div class="tool-top"><h3>' + esc(x.name) + "</h3>" +
        '<span class="tool-yrs">' + esc(t("tools." + x.key + ".y")) + "</span></div>" +
        "<p>" + esc(t("tools." + x.key + ".d")) + "</p></div></article>";
    }).join("");
    observeReveals(document.getElementById("tool-grid"));
  }

  /* Adobe's own app-icon convention is a two-tone rounded square with the short mark,
     so Ps/Ai are set in type at the official colours; CapCut and Gemini use their real marks. */
  function badge(kind) {
    if (kind === "ps") return '<span class="app-badge ab-ps" aria-hidden="true">Ps</span>';
    if (kind === "ai") return '<span class="app-badge ab-ai" aria-hidden="true">Ai</span>';
    if (kind === "capcut") return '<span class="app-badge ab-plain"><img src="assets/tools/capcut.svg" alt="" width="24" height="24" loading="lazy"></span>';
    return '<span class="app-badge ab-plain"><img src="assets/tools/gemini.svg" alt="" width="24" height="24" loading="lazy"></span>';
  }

  function timeline() {
    document.getElementById("timeline").innerHTML = PATH_YEARS.map(function (n) {
      return '<div class="tl-row rv"><span class="yr">' + esc(t("path." + n + ".y")) + "</span>" +
        '<div class="bd"><p class="t">' + esc(t("path." + n + ".t")) + "</p>" +
        '<p class="d">' + esc(t("path." + n + ".d")) + "</p></div></div>";
    }).join("");
    observeReveals(document.getElementById("timeline"));
  }

  function faq() {
    document.getElementById("faq-list").innerHTML = FAQ_Q.map(function (n) {
      return '<details class="faq-item rv"' + (n === 1 ? " open" : "") + "><summary>" + esc(t("faq.q" + n)) + "</summary>" +
        "<p>" + esc(t("faq.a" + n)) + "</p></details>";
    }).join("");
    observeReveals(document.getElementById("faq-list"));
  }

  function facts() {
    var fmts = 3;
    var rows = [[D.meta.totalWorks, "fact.works"], [clientBrandCount(), "fact.brands"],
      [Object.keys(D.cats).length, "fact.fields"], [fmts, "fact.formats"]];
    document.getElementById("facts").innerHTML = rows.map(function (r) {
      return '<div class="fact"><div class="n">' + num(r[0]) + '</div><div class="l">' + esc(t(r[1])) + "</div></div>";
    }).join("");
  }

  function about() {
    document.getElementById("skills").innerHTML = SKILLS[lang].map(function (s) {
      return '<span class="tag' + (s === SKILLS[lang][0] || s === SKILLS[lang][1] ? " hot" : "") + '">' + esc(s) + "</span>";
    }).join("");
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
    document.getElementById("brand-txt").textContent = lang === "ar" ? "محمد المصري" : "Muhammad Al-Masri";
    heroBoard(); ticker(); facts(); about(); brandIndex(); craftRows(); toolGrid(); timeline(); faq();
    renderChips(); grid();
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
    }, { rootMargin: "80px 0px", threshold: 0.04 });
    Array.prototype.forEach.call((root || document).querySelectorAll(".rv:not(.in)"), function (n) { io.observe(n); });
  }

  /* ------------------------------------------------------------------ scroll motion
     Transform and opacity only, one rAF pass, and never on reduced-motion or touch. */
  function scrollMotion() {
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var hero = document.querySelector(".hero-grid");
    var board = document.querySelector(".board");
    var strip = document.querySelector(".strip");
    if (reduce || !hero || !board) return;

    var ticking = false;
    function paint() {
      ticking = false;
      var vh = window.innerHeight || 1;
      var y = window.pageYOffset || document.documentElement.scrollTop || 0;
      var p = Math.min(1, Math.max(0, y / (vh * 0.9)));
      board.style.transform = "translate3d(0," + (p * -34).toFixed(2) + "px,0) scale(" + (1 - p * 0.035).toFixed(4) + ")";
      var hc = document.querySelector(".hero-col");
      if (hc) hc.style.transform = "translate3d(0," + (p * 18).toFixed(2) + "px,0)";
      if (strip) {
        var r = strip.getBoundingClientRect();
        var q = 1 - Math.min(1, Math.max(0, (r.bottom - vh * 0.25) / (vh * 0.55)));
        strip.style.opacity = (1 - q * 0.55).toFixed(3);
      }
    }
    function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    paint();
  }

  /* ------------------------------------------------------------------ wire */
  function boot() {
    document.getElementById("be-link").href = BE;
    document.getElementById("foot-be").href = BE;

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

    /* brand card -> filter the grid to that brand and move to the work section */
    document.getElementById("brand-index").addEventListener("click", function (e) {
      var b = e.target.closest("[data-brand]"); if (!b) return;
      cat = "all"; query = b.getAttribute("data-brand"); s.value = query;
      renderChips(); grid();
      document.getElementById("work").scrollIntoView({ behavior: "smooth", block: "start" });
    });

    document.getElementById("craft-rows").addEventListener("click", function (e) {
      var a = e.target.closest(".craft-shot");
      if (a) { e.preventDefault(); openProof(a.getAttribute("href").split("/").pop(), 0); return; }
      var b = e.target.closest("[data-craft-cat]");
      if (b) {
        cat = b.getAttribute("data-craft-cat"); query = ""; s.value = "";
        renderChips(); grid();
        document.getElementById("work").scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });

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

    Array.prototype.forEach.call(document.querySelectorAll(".sec-head"), function (n) { n.classList.add("rv"); });
    observeReveals(document);
    scrollMotion();
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
