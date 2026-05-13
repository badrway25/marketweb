"""Content tree · `madou-pasticceria` · T50 multilingual rollout (AR · RTL).

Modern Standard Arabic (MSA · فصحى) translation of `MADOU_CONTENT_IT`.
Built for the marketweb T50 multilingual pass (IT → EN/FR/ES/AR · AAA
walk · public flip). Shape parity contract enforced against
`template_content_madou.py`:

  * Same top-level keys, same nested keys at every depth.
  * Same list lengths (5 lievitati signature courses, 8 menu courses,
    4 produttori, 4 atmosphere images, 4 riconoscimenti, etc.).
  * Same tuple positions for tuple-typed values.
  * Same `pages[].slug` values (labels translated to Arabic, slugs
    preserved as IT for routing parity).
  * Same `posts[].slug` values, same `page kind`.

Voice anchor — `تخمير بطيء` (slow proofing · MSA premium artisanal
register · Asharq Al-Awsat gastronomic gravity · Cookpad MENA
pastry-craft idiom) carries the IT `lievitazione lenta` load-bearing
promise across the same surfaces (hero H1 with `<em>` italic emphasis,
manifesto, cta_heading, forno headline/values, pasticceria intro,
ordina, produttori + signature courses copy). Variant `الخميرة الأم`
(mother starter) and `العجن البطيء` (slow kneading) appear as
synonym anchors where useful.

RTL house-style (mirrors `template_content_atto_ar.py` T48
precedent · the chrome handles bidi via `unicode-bidi: isolate`):

- Latin proper names preserved verbatim in Latin script
  (Torino, Borgo Po, Via Sant'Ottavio 36, Pierre Marchais, Famiglia
  Brero, Olivier Domori, Anna Negroni, Carla Madou, Tommaso Rinaldi,
  Iginio Massari, Pierre Hermé, Cristian Beduschi, Cuneo IGP, Val
  Susa, Isigny-sur-Mer, Madagascar Sambirano, Mortara, Domori
  Criollo, Marrone IGP, Nocciola Piemonte IGP, Gambero Rosso
  Pasticcerie, AMPI, Coppa del Mondo Pasticceria, Identità di
  Pasticceria, Dissapore, Cook Corriere, Vogue Cibo, Erbaluce
  passito Cieck, Caffè Vergnano, Damman, Inalpi, Caffè Al Bicerin).
- Brand name `Madou · Pasticceria Atelier` preserved verbatim
  (NOT transliterated to Arabic).
- Pastry product names in Latin/French script preserved
  (Croissant viennoise, Maritozzo, Millefoglie, Bignè, Saint
  Honoré, Mont-Blanc, Tarte au chocolat, Macarons, Pasta sfoglia,
  Bicerin, panettone, colomba, kouign-amann, brioche col tuppo).
- Latin (Western Arabic) digits preserved per atto_ar precedent
  (2011, 12, 64, 5:30, 7:30, 19:30, 75 €, € 18). Eastern
  Arabic-Indic digits are NOT used.
- Times rendered with Latin digits and ` – ` en-dash separator.
- Arabic punctuation `،` `؟` `؛` used in running prose.
- Carla Madou referred to as `الباستيشيرا` / `صانعة المعجنات`
  (feminine, MSA).
"""

from typing import Any


MADOU_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",         "label": "الرئيسية",       "kind": "home"},
        {"slug": "forno",        "label": "الفرن",          "kind": "about"},
        {"slug": "pasticceria",  "label": "المعجنات",       "kind": "menu"},
        {"slug": "vetrina",      "label": "الواجهة",        "kind": "gallery"},
        {"slug": "diario",       "label": "اليوميات",       "kind": "blog_list"},
        {"slug": "ordina",       "label": "الطلبات",        "kind": "reservations"},
    ],

    "site": {
        "logo_initial":  "MD",
        "logo_word":     "Madou",
        "tag":           "Pasticceria Atelier · Torino Borgo Po · منذ 2011",
        "phone":         "+39 011 8195 770",
        "email":         "atelier@madou-pasticceria.it",
        "address":       "Via Sant'Ottavio 36 · 10124 Torino",
        "hours_compact": "الثلاثاء – السبت · 7:30 – 19:30 · الأحد 7:30 – 13:00",
        "star_line":     "★ Tre Torte · Gambero Rosso · 2023 · 2024 · 2025",
        "footer_intro":
            "خمسة عشر عاماً من التخمير البطيء. صالة عملٍ مكشوفة، "
            "وواجهةٌ من العجين النيّء، وفرنان بأرضيةٍ حراريةٍ صامدة. "
            "لا عجائن صناعية مسبَّقة، ولا مجمَّدات، ولا استعجال.",
        "footer_hours_1": "الثلاثاء – السبت · 7:30 – 19:30",
        "footer_hours_2": "الأحد · 7:30 – 13:00 · الإثنين · إغلاق",
        "copyright": "© 2026 Madou Atelier S.r.l. · الرقم الضريبي 11237680016",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # T49: hero plate URL threaded into the fine-dining template via
        # page_data so Madou swaps Gusto's plated-dish hero for the
        # pasticceria vetrina without forking home.html. URL from X.3
        # curator pack `bakery-pasticceria.md` (Pexels CC0-compatible).
        "hero_plate_url":
            "https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600",
        "eyebrow":  "Pasticceria Atelier · Torino Borgo Po · منذ 2011",
        "headline": "اثنتا عشرة ساعةً من <em>التخمير البطيء،</em> عجينٌ ورقيٌّ يَدَعُكَ تَسمعُه.",
        "intro":
            "عجائن ورقية مُرقَّقة على البارد، تخميرٌ طبيعيٌّ بالعجين الأم "
            "يُجدَّد كل اثنتي عشرة ساعة، وكريماتٌ تُخفَق بحسب الطلب. "
            "الواجهة تتغيّر يومياً وفقَ ما خرج من الفرن في فجر النهار.",
        "primary_cta":   "اطلب عجين السبت مسبقاً",
        "primary_href":  "ordina",
        "secondary_cta": "الباستيشيرا",
        "secondary_href":"forno",

        # Repurposed labels (Gusto's "chef" → Madou's "pasticciera")
        "chef_label":    "الباستيشيرا",
        "star_tag":      "★ Tre Torte · Gambero Rosso 2025",
        "photo_label":   "التصوير",
        "cuisine_label": "صانعة المعجنات",

        "facts": [
            ("12 h",  "تخمير أدنى · pasta sfoglia"),
            ("3",     "خمائر أمٍّ حيّة في الأتيليه · منذ 2011"),
            ("0",     "عجائن صناعية مسبَّقة · 0 مجمَّدات · 0 خلطات جاهزة"),
        ],

        "manifesto_drop_cap": "ع",
        "manifesto":
            "ندما تدخل صفيحةُ عجينٍ ورقيٍّ إلى الفرن، يتوقف العمل في "
            "Madou أربع دقائق ويُصغي الجميع. صوتُ العجين وهو ينتفخ — "
            "فقاعاتُ الهواء تتحرر بين 64 طبقةً من العجين المُرقَّق — هو "
            "المؤشرُ الأول إن كانت تلك الدفعة ستُباع صباح السبت أم "
            "ستذهب إلى الفرقة. لا ساعةَ توقيت، ولا ميزانَ حرارة: "
            "الأذنُ وحدها.",

        # Pasticceria signature — 5 "lievitati" (vs Gusto 5 "atti")
        "signature_courses": [
            ("I",    "Croissant viennoise",         "12 ساعةً من التخمير البطيء · 64 طبقة · زبدة نورماندية من Isigny", "قهوة Etiopia Sidamo أحادية المنشأ"),
            ("II",   "Maritozzo con la panna",      "تخمير طبيعي 24 ساعة · قشدة طازجة تُخفَق بحسب الطلب",            "شوكولاتة ساخنة Madagascar 72%"),
            ("III",  "Millefoglie alla nocciola",   "ثلاث طبقات من العجين الورقي المُكرمَل · كريم شانتيي بالبندق IGP",   "Bicerin تقليدي تورينيّ"),
            ("IV",   "Bignè al cioccolato Domori",  "عجين شو من البيت · غاناش داكن Criollo 80%",                       "شاي أسود Darjeeling First Flush"),
            ("V",    "Saint Honoré ai marroni",     "موسميٌّ خريفي · كستناء Cuneo IGP · كريم mousseline",              "نبيذ حلو Erbaluce passito"),
        ],

        # Persona — pasticciera Carla Madou
        "chef": {
            "name":  "Carla Madou",
            "role":  "باستيشيرا الأتيليه · من مواليد 1979",
            "bio":
                "تورينيةُ المولد، من مواليد 1979. تتلمذت أربع سنوات لدى "
                "Iginio Massari في Brescia، ثم سنتين لدى Pierre Hermé "
                "في باريس، وأخيراً سنتين لدى Cristian Beduschi في "
                "جنيف. افتتحت Madou عام 2011 في مطبعةٍ سابقةٍ بحي "
                "Borgo Po، بحدسٍ واحد: ألا تعمل إلا بخمائر أمٍّ حيّة، "
                "تُجدَّد كل اثنتي عشرة ساعة.",
        },

        "courses_label": "خمسةُ معجناتٍ مخمَّرة هذا الأسبوع · أكتوبر '26",
        "courses_footline": "واجهةٌ حيّة — ما ترونه قد خرج من الفرن هذا الصباح",
        "courses_full_cta": "كل المعجنات",
        "chef_link_filosofia": "الفرنُ واليدان",
        "chef_link_diario": "يوميات الطحين",

        "press_label": "نُشِر عنّا في",
        "press": ["GAMBERO ROSSO PASTICCERIE", "DISSAPORE", "COOK CORRIERE",
                  "IDENTITÀ DI PASTICCERIA", "VOGUE CIBO"],

        # Ingredients/sourcing editorial band — pasticceria-specific
        "ingredienti": {
            "label":   "المواد الأولية",
            "heading": "ستةَ عشرَ مورِّداً، <em>كلٌّ منهم بالاسم.</em>",
            "text":
                "سلسلةُ توريد Madou قصيرةٌ، يمكن تتبُّعها سطراً بسطر. "
                "الزبدةُ تَرِدُ من مزرعة ألبانٍ نورماندية في Isigny-sur-Mer · "
                "البيضُ من مزرعةٍ على بُعدِ ستين كيلومتراً من Torino · "
                "أنواعُ الطحين من طاحونةٍ حجريةٍ في Val Susa · الكاكاو "
                "من ثلاث مزارع أحادية المنشأ (Madagascar، Venezuela، "
                "República Dominicana) اختيرت في الحقل سنة 2019.",
            "image":
                "https://images.pexels.com/photos/28183472/pexels-photo-28183472.jpeg"
                "?auto=compress&cs=tinysrgb&w=1000",
            "image_caption":
                "العجين المُرقَّق على الرخام المُبرَّد · مناوبةُ الخامسةِ والنصف فجراً",
        },

        # Atmosphere teaser — pasticceria-specific imagery
        "atmosphere_teaser": {
            "label": "الواجهة الحيّة",
            "images": [
                ("https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "واجهة صباح السبت"),
                ("https://images.pexels.com/photos/16140003/pexels-photo-16140003.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "زينةٌ يدوية · كعكةٌ بحسب الطلب"),
                ("https://images.pexels.com/photos/30853716/pexels-photo-30853716.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Croissant viennoise حديثة الخروج من الفرن"),
                ("https://images.pexels.com/photos/31000323/pexels-photo-31000323.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Macarons موسمية · أكتوبر '26"),
            ],
            "link_label": "ادخل إلى الواجهة",
            "link_href":  "vetrina",
        },

        # Awards/recognition — pastry awards (not Michelin)
        "riconoscimenti": {
            "label": "التكريمات",
            "items": [
                ("★★★",  "Tre Torte · Gambero Rosso",     "جائزة سنوية · 2023 · 2024 · 2025"),
                ("AMPI", "Accademia Maestri Pasticceri",  "عضوٌ منذ 2017 · فرع Brescia"),
                ("CMP",  "Coppa del Mondo Pasticceria",   "منتخب إيطاليا · بديل 2022 · المركز الرابع في Lyon"),
                ("DIS",  "Dissapore · 50 Pasticcerie",    "المركز الأول في Piemonte 2024 · ضمن أفضل 5 في إيطاليا 2025"),
            ],
        },

        # CTA section
        "cta_heading": "لا شيء سوى التخميرِ البطيء، <em>لا شيء سوى ما يخرج من الفرن صباحاً.</em>",
        "cta_primary":  "اطلب عجين السبت مسبقاً",
        "cta_secondary": "اكتشف كل المعجنات",

        # Seasonal highlight card — pasticceria seasonal
        "stagione": {
            "label":     "في الواجهة الآن",
            "title":     "معجنات خريف '26",
            "subtitle":  "كستناء، كاكي، شوكولاتة أحادية المنشأ · ابتداءً من 6 أكتوبر",
            "text":
                "تُفتَتح قائمةُ الخريف في 6 أكتوبر بـ Saint Honoré "
                "بكستناء Cuneo IGP، وميل-فوي بالكاكي القابض من "
                "Bel Paese، وَMont-Blanc 2026 في صيغته الفرديّة. "
                "تبقى كلُّ معجنات الخريف في الواجهة حتى 30 نوفمبر، "
                "ثم تبدأ قائمةُ عيد الميلاد.",
            "cta_label": "اكتشف كامل قائمة الخريف ←",
            "cta_href":  "pasticceria",
        },

        # Producer showcase — pastry supply chain (vs Gusto wine producers)
        "produttori": {
            "label":   "المورِّدون",
            "heading": "ستَّ عشرةَ يداً، <em>واجهةٌ واحدة.</em>",
            "intro":
                "لكل مادةٍ أوّليةٍ لدى Madou مورِّدٌ باسمٍ وعنوانٍ ورقمِ "
                "هاتف. الزبدة، الحليب، البيض، الطحين، الكاكاو، الفاكهة، "
                "العسل — لا شيء يَرِدُ من كتالوج. كلُّ المورِّدين زارتهم "
                "Carla شخصياً مرةً واحدةً على الأقل.",
            "items": [
                {
                    "portrait":
                        "https://images.pexels.com/photos/8477754/pexels-photo-8477754.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Pierre Marchais",
                    "role": "زبدة نورماندية AOP",
                    "area": "Isigny-sur-Mer · Normandie",
                    "blurb":
                        "زبدةُ Isigny AOP تَرِدُ كلَّ أربعاء بشحنةٍ مُبرَّدةٍ "
                        "عند 4°C. مزرعةُ ألبانٍ عائليةٌ منذ 1932، "
                        "أربعُ بقراتٍ نورماندية لكل هكتار.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/8188937/pexels-photo-8188937.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Famiglia Brero",
                    "role": "طاحونة حجرية في Val Susa",
                    "area": "Bussoleno · Piemonte",
                    "blurb":
                        "طحنٌ بالحجر في ثلاث تمريرات · قمحٌ طريّ "
                        "Bologna محلّيٌّ بالكامل · لا تكرير. ثلاثةُ "
                        "أنواع طحين، نوعٌ شهرياً حصرياً للأتيليه.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/11869895/pexels-photo-11869895.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Olivier Domori",
                    "role": "كاكاو أحادي المنشأ",
                    "area": "Sambirano · Madagascar",
                    "blurb":
                        "ثلاثُ مزارع اختارتها Carla في الحقل سنة "
                        "2019. كاكاو Criollo Trinitario بنسبة 80%، "
                        "محمَّصٌ على البارد في إيطاليا · تتبُّع كلِّ "
                        "دفعةٍ بالرقم.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/29198586/pexels-photo-29198586.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Anna Negroni",
                    "role": "فاكهة موسمية · Cuneo",
                    "area": "Lagnasco · Piemonte",
                    "blurb":
                        "خوخُ Cuneo IGP في يونيو · كستناء IGP في "
                        "أكتوبر · كاكي قابض في نوفمبر. ثمانيةُ "
                        "هكتارات، قطفٌ يدوي، لا غرف تبريد.",
                },
            ],
        },

        # Repurposed `private_dining` → `eventi su misura` / cake design
        "private_dining": {
            "label":   "مناسبات بحسب الطلب",
            "heading": "تصميمُ الكعك و<em>الطلبيّات الخاصة.</em>",
            "intro":
                "يَقبلُ Madou طلبيّات الكعك الاحتفاليّ وكعكِ الأعراس "
                "والإنتاجات الخاصة الصغيرة للمناسبات. ثلاثُ مداخل، "
                "لكلٍّ منها مدةُ تحضيرٍ وأسعارٌ مختلفة.",
            "experiences": [
                {
                    "icon": "fork",
                    "title": "كعكة بحسب الطلب",
                    "meta":  "حدٌّ أدنى 8 حصص · ابتداءً من € 18 / حصة",
                    "desc":
                        "تصميمٌ خاصٌّ يُبنى على ثلاثة لقاءاتٍ تمهيديةٍ "
                        "مع Carla. مدةُ التحضير: أسبوعان كحدٍّ أدنى. "
                        "نُزخرف باليد فقط — لا قوالب صناعية.",
                },
                {
                    "icon": "door",
                    "title": "كعكة عرس",
                    "meta":  "ابتداءً من 40 حصة · من € 22 / حصة",
                    "desc":
                        "أربعةُ أشهرٍ من العمل المشترك مع الثنائي. "
                        "ثلاثُ تجارب تذوُّقٍ ضمن الخدمة. الاستلامُ في "
                        "الأتيليه أو توصيلٌ مُبرَّدٌ على عاتق Madou في "
                        "وسط Piemonte.",
                },
                {
                    "icon": "wine",
                    "title": "بوفيه خاص",
                    "meta":  "20 – 60 ضيفاً · من € 38 / ضيف",
                    "desc":
                        "معجنات mignon فقط · 8 مرجعيات، 150 قطعةً "
                        "كحدٍّ أدنى. الخَبْزُ يومَ المناسبة، وتوصيلٌ "
                        "مُبرَّد. ما بعد ظهر السبت نُبقيه حُرّاً.",
                },
            ],
            "cta_label": "اكتب إلى الباستيشيرا",
            "cta_href":  "ordina",
        },

        # Repurposed `wine_program` → `lieviti madre` collection
        "wine_program": {
            "label":   "أرشيف الخمائر",
            "heading": "ثلاثُ خمائر أمٍّ حيّة، <em>وَمعجناتٌ واحدة.</em>",
            "intro":
                "يحفظ الأتيليه ثلاثَ خمائر أمٍّ نشطة، لكلِّ واحدةٍ منها "
                "بصمتُها في الحموضة وإنتاجِيَّتها. كلُّ مُخمَّرٍ من Madou "
                "مُقترنٌ بالأمِّ التي تخصُّه — لا خميرة بيرة، ولا "
                "محسِّنات.",
            "sommelier": {
                "name": "Tommaso Rinaldi",
                "role": "معلِّمُ التخمير · مسؤولُ العجين الأم",
                "bio":
                    "تتلمذَ لدى Carla منذ 2014، ومسؤولٌ عن تجديد "
                    "الخمائر الأمِّ الثلاث منذ 2018. يُجدِّدُ كلَّ "
                    "اثنتي عشرة ساعة، عند 5:30 و17:30. يحفظ ذاكرة "
                    "الطحين لكلِّ دفعة.",
            },
            "pairings": [
                ("01", "الأم M-1 · العجين الورقي المُرقَّق",
                 "خميرةٌ نشطةٌ منذ 2011 · حموضةٌ لاكتيكيةٌ مهيمنة · "
                 "pH 4.2 · ثنياتٌ سريعة، راحةٌ طويلة. تُستعمل لـ "
                 "Croissant، kouign-amann، brioche col tuppo.",
                 "12 – 16 ساعة"),
                ("02", "الأم M-2 · panettoni والمخمَّرات العالية",
                 "أمٌّ وُلدت سنة 2014 من تجديدٍ ثلاثي. حموضةٌ مختلطة "
                 "أسيتيكية-لاكتيكية، pH 4.5 · نموٌّ عموديٌّ قوي. "
                 "panettone و colomba و veneziana فقط.",
                 "36 – 48 ساعة"),
                ("03", "الأم M-3 · pan brioche والمُرقَّقات الحلوة",
                 "أمٌّ تُجدَّد بعسلِ الكستناء · حموضةٌ مُهذَّبة، pH 4.7 · "
                 "عبيرُ البندق المحمَّص. Maritozzi، brioche مدوَّرة، "
                 "ضفيرةُ الشوكولاتة.",
                 "8 – 12 ساعة"),
            ],
            "cellar_facts": [
                ("3",    "خمائر أمٍّ حيّة"),
                ("12h",  "تواتر تجديدٍ ثابت"),
                ("2011", "سنةُ الأمِّ الأولى · M-1"),
            ],
        },
    },

    # ─── FORNO (about) — Gusto's "filosofia" page ────────────
    "forno": {
        "eyebrow":  "الفرن",
        "headline": "خمسةَ عشرَ عاماً من العمل عند الفرن، <em>ووعدُ تخميرٍ بطيءٍ واحد.</em>",
        "intro":
            "وُلدَ Madou سنة 2011 في مطبعةٍ سابقةٍ بحي Borgo Po، "
            "في Torino. الأتيليه فيه صالةُ عملٍ مكشوفةٌ على الشارع، "
            "وفرنان بأرضيةٍ حراريةٍ صامدة. الوعدُ هو نفسُه دائماً: "
            "صفرُ عجائنَ مسبَّقة، صفرُ مجمَّدات، صفرُ خلطاتٍ صناعية. "
            "لا شيء سوى التخميرِ البطيء، ولا شيء سوى موادَّ أوَّليةٍ "
            "متتبَّعة.",

        "history": [
            ("2011",
             "افتتحت Carla Madou الأتيليه في Via Sant'Ottavio بعد "
             "ثماني سنواتٍ بين Brescia (Massari) وَParis (Hermé) "
             "وَGenève (Beduschi). أربعةُ مقاعدَ على الكاونتر، "
             "مرجعيّتان من المعجنات، أمٌّ واحدة — M-1، أُسِّستْ "
             "بطحينِ طاحونة Brero."),
            ("2014",
             "ينضمُّ Tommaso Rinaldi متدرباً، ويصبحُ خلال ثلاث سنواتٍ "
             "مسؤولاً عن الخمائر الأم. تُولَدُ M-2، أمُّ panettone، "
             "من تجديدٍ ثلاثيٍّ لـ M-1."),
            ("2017",
             "تُقبَلُ Carla في الأكاديمية الإيطالية لمعلِّمي المعجنات "
             "(AMPI)، لتكون ثانيةَ امرأةٍ بييمونتية تنضمُّ إليها بعد "
             "Sonia Balacchi."),
            ("2021",
             "ينتقلُ الأتيليه إلى Via Sant'Ottavio 36، المطبعةُ "
             "السابقةُ المُرمَّمةُ بالكامل. ثلاثةُ أفران، مُرقِّقان، "
             "وواجهةٌ خطّيةٌ بطول خمسةَ عشرَ متراً مفتوحةٌ على "
             "الشارع."),
            ("2023",
             "يمنحُ Gambero Rosso الـ Tre Torte (أعلى تكريمٍ في "
             "المعجنات) ويُعيدُ تأكيده عامي 2024 و2025. يصبح Madou "
             "محطةً ثابتةً ضمن دائرة المعجنات الإيطالية المؤلِّفة."),
        ],

        "filosofia_image":
            "https://images.pexels.com/photos/30918889/pexels-photo-30918889.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400",
        "filosofia_image_caption": "المختبر · Carla Madou عند المُرقِّق",

        "method_title": "المنهج",
        "method_paragraphs": [
            "تنطلق كلُّ معجنات Madou من تجديد الأم. عند 5:30 فجراً "
            "يُجدِّد Tommaso الخمائر الأمَّ الثلاث ويفرز الكميّات "
            "اللازمة لعجائن النهار · وعند 17:30 يُجدِّد مرةً أخرى "
            "لعجائن الليل. هو جدولٌ ثابت، لا يتأثر بعيد الميلاد ولا "
            "بعيد الفصح ولا بعطلة Ferragosto.",
            "تُحضَّر العجائن الورقيةُ المُرقَّقةُ في المساء السابق "
            "وتستريحُ في غرفةٍ باردةٍ عند 4°C لاثنتي عشرة ساعةً "
            "كحدٍّ أدنى، وستَّ عشرةَ ساعةً لدفعات السبت. تُضربُ "
            "الزبدةُ على البارد · يُضافُ ملحُ Mothia على شكلِ "
            "رقائق · الثنياتُ أربعٌ دائماً، لا ثلاث · وتُنتجُ دورةُ "
            "الترقيق النهائيةُ 64 طبقةً من العجين تظهرُ عند القطع.",
            "تُحضَّرُ الكريماتُ أمامَ الزبون، وتُخفَقُ بحسبِ الطلب. "
            "لا تخرجُ أيُّ معجَّناتٍ من Madou من الكاونتر بكريمٍ "
            "حُضِّرَ قبل ساعتين · يُقطَّعُ العجينُ الهشُّ باليد · "
            "وتُستحلَبُ الغاناشاتُ بالمضربِ في التمريرة التالية. "
            "العمل بحسب الطلب هو السبب الذي من أجله لا نبيع تصميم "
            "كعكٍ من دون إشعارٍ مسبق.",
        ],

        "values_label": "ما نضمنُه",
        "values_heading": "أربعةُ وعودٍ <em>غيرِ قابلةٍ للتفاوض</em>.",
        "values": [
            ("الزمن",       "اثنتا عشرة ساعةً من التخمير البطيء كحدٍّ أدنى · ستَّ عشرةَ يوم السبت."),
            ("سلسلة التوريد", "ستةَ عشرَ مورِّداً، كلٌّ منهم زِيرَ شخصياً مرةً على الأقل."),
            ("الشفافية",    "لا خلطات جاهزة، ولا محسِّنات، ولا مجمَّدات."),
            ("اليد",       "زينةٌ يدوية · كريماتٌ تُخفَقُ بحسب الطلب · لا قوالبَ صناعية."),
        ],

        "cta_heading": "أتُريدُ أن ترى <em>معجنات الأسبوع الجاري؟</em>",
        "cta_menu": "خمسةُ معجناتٍ مخمَّرة لأكتوبر '26",
        "cta_prenota": "اطلب عجين السبت مسبقاً",
    },

    # ─── PASTICCERIA (menu) — Gusto's "menu" page ────────────
    "pasticceria": {
        "eyebrow":  "قائمةُ الأسبوع",
        "headline": "واجهةٌ حيّة — <em>خريف '26</em>",
        "intro":
            "تتبدَّلُ معجنات Madou كلَّ أسبوعٍ وفقَ فرنِ ليلةِ الإثنين. "
            "ما يلي هو القائمةُ السارية من 6 إلى 12 أكتوبر 2026 · "
            "الواجهةُ مفتوحةٌ من الثلاثاء إلى السبت، وصبيحةَ الأحد فقط، "
            "والإثنينُ إغلاق.",
        "courses_label": "خمسةُ معجناتٍ مخمَّرة · أكتوبر '26",

        "courses": [
            ("I",     "Croissant viennoise",
             "Pasta sfoglia مُخمَّرة 12 ساعة · زبدة نورماندية AOP "
             "من Isigny · 64 طبقةً تظهرُ عند القطع · طلاءُ صفارٍ من "
             "البيض الكامل · سُكَّر ناعمٌ من Mothia يُرشُّ عند الخروج "
             "من الفرن.",
             "قهوة Etiopia Sidamo أحادية المنشأ · Caffè Vergnano لـ Madou"),
            ("II",    "Maritozzo con la panna",
             "عجين brioche مُخمَّر 24 ساعة بـ M-3 · قشدةٌ طازجةٌ من "
             "مزرعة Inalpi تُخفَقُ بحسب الطلب · فانيليا Tahitian "
             "كاملة من Madagascar · تاجٌ من سُكَّر الغزل.",
             "شوكولاتة ساخنة Madagascar Domori 72%"),
            ("III",   "Millefoglie alla nocciola",
             "ثلاث طبقات من pasta sfoglia المُكرمَل · كريم شانتيي "
             "بالبندق Nocciola Piemonte IGP من طاحونة Brero · جريش "
             "بندقٍ محمَّصٍ على الأرضية الحرارية.",
             "Bicerin تقليديٌّ تورينيّ · وصفة Caffè Al Bicerin التاريخية"),
            ("IV",    "Bignè al cioccolato Domori",
             "عجين شو من البيت · غاناش داكن بكاكاو Criollo Domori "
             "80% · تلميعٌ بشراب الغلوكوز · تشطيبٌ بالحقن · سُكَّر "
             "ناعم حسب الرغبة.",
             "شاي أسود Darjeeling First Flush · مجموعة Damman 2026"),
            ("V",     "Saint Honoré ai marroni",
             "الخريفُ حصراً · bignè مَحْشُوّةٌ بكريم mousseline "
             "بالكستناء · كستناء Cuneo IGP من حقل Anna Negroni · "
             "قاعدةٌ من pasta sfoglia · تاجٌ ذهبيٌّ من سُكَّر الغزل.",
             "Erbaluce di Caluso passito · مجموعة Cieck · 50 cl بالكأس"),
            ("VI",    "Mont-Blanc 2026",
             "شَعيريّاتُ كستناء IGP من Mortara · كريم شانتيي "
             "بالفانيليا · قلبٌ من المرنغ الفرنسي مَخْبُوزٌ عند 90°C "
             "أربع ساعات · تشطيبٌ يدوي.",
             "قهوة تركية بالهيل الأخضر · تُقدَّم في إبريق نُحاس"),
            ("VII",   "Tarte au chocolat Sambirano",
             "عجينٌ هشٌّ بالكاكاو 22% · غاناش داكن Madagascar "
             "Sambirano 72% · رقائق ملح Mothia · تشطيبٌ بزيت زيتون "
             "بكر من Taggia.",
             "—"),
            ("VIII",  "Macarons موسمية",
             "ستةُ Macarons موسمية · زعفرانُ Abruzzo، توتُ Roero، "
             "كستناءُ Cuneo، شوكولاتةُ Sambirano، فانيليا Tahitian، "
             "زيتونُ Taggia · خَبْزٌ عند 165°C لمدة 12 دقيقة.",
             "شاي أبيض Pai Mu Tan · مجموعة Damman"),
        ],

        # Wine_program → repurposed as caffè & tisaneria
        "wine_intro_title": "ركن القهوة والشاي",
        "wine_intro":
            "يَقترنُ في Madou كلُّ مُخمَّرٍ بقهوةٍ أحادية المنشأ مُحمَّصةٍ "
            "في Torino لدى Vergnano أو شايٍ مختارٍ من Damman. قائمةُ "
            "الشاي والقهوة كاملة، والاقتراناتُ بتقدير الكاونتر — "
            "اسألوا Tommaso عند المرور إلى المحاسبة.",

        "wine_highlights": [
            ("قهوة أحادية المنشأ",  "8 مناشئ · Etiopia، Brasile، Colombia، Guatemala، Vietnam، Sambirano"),
            ("شاي أسود وأخضر",     "22 اختياراً من Damman · Darjeeling، Ceylon، Sencha، Genmaicha"),
            ("شوكولاتات ساخنة",    "6 مناشئ · Madagascar، Venezuela، Ecuador، Dominicana، Tanzania، Ghana"),
            ("مشروبات تقليدية",    "Bicerin · vin brulé بالقرفة · ponce بالمندرين · zabaione"),
        ],

        "footer":
            "الواجهةُ مفتوحةٌ من الثلاثاء إلى السبت · يُنصَحُ بالحجزِ "
            "المسبق لعجين السبت ابتداءً من الأربعاء. عجينُ السبت "
            "ينفدُ عادةً قبل الساعة 11:00. للطلبيّات التي تتجاوز 12 "
            "قطعة، يُرجى الكتابةُ إلى atelier@madou-pasticceria.it قبل "
            "48 ساعةً على الأقل.",
    },

    # ─── VETRINA (gallery) — Gusto's "atmosfera" ─────────────
    "vetrina": {
        "eyebrow":  "الواجهة",
        "headline": "خمسةَ عشرَ متراً من الواجهة، <em>واجهةٌ واحدة.</em>",
        "intro":
            "يشغلُ Madou مطبعةً سابقةً في Via Sant'Ottavio · الواجهةُ "
            "مفتوحةٌ على الشارع بطول خمسةَ عشرَ متراً خطّياً، وتُريك "
            "كامل المختبر. لا جدارَ بين الفرنِ ورصيفِ Borgo Po.",

        "rooms": [
            ("الواجهة على الشارع",
             "خمسةَ عشرَ متراً من الواجهة على امتداد Via Sant'Ottavio · "
             "عرضٌ بمستويين · تبريدٌ عند +4°C للكريمات · خِزانةٌ "
             "جافةٌ عند +18°C للمخمَّرات."),
            ("صالة العمل المكشوفة",
             "الأتيليه الحقيقي — أربعُ منصّات: الترقيق، المخمَّرات، "
             "الكريمات، الزخرفة. تُرى كلُّ المعجنات بالزمن الحقيقي "
             "من الواجهة · لا مطبخ خفيّ."),
            ("صالة التذوق",
             "ثمانيةُ مقاعدَ على الكاونتر، قُبالةَ المُرقِّق. مفتوحةٌ "
             "حصراً لجلسات التذوق المُوجَّهة بعدَ ظهر الخميس · ثلاثُ "
             "ساعاتٍ مع Carla، ستةُ مخمَّرات، ثلاثُ قهواتٍ أحادية "
             "المنشأ."),
            ("فناءُ المطبعة السابقة",
             "من مايو إلى سبتمبر، أربعُ طاولاتٍ في الهواء الطلق تحت "
             "شجرة الويستيريا في المطبعة السابقة. تُفتَحُ للفطور فقط · "
             "قائمةٌ ثابتةٌ للإثنين، Croissant + Bicerin."),
        ],

        "captions": [
            "واجهةُ صباح السبت · عَرضُ الساعة 7:30.",
            "زينةٌ يدوية · كعكةُ عرسٍ خريف '26.",
            "Croissant viennoise حديثةُ الخروج من الفرن عند 6:00.",
            "Macarons أكتوبر '26 · ستةُ نكهاتٍ موسمية.",
            "Carla Madou عند المُرقِّق · pasta sfoglia الخامسةِ والنصف فجراً.",
            "الكاونتر عند مرورِ أوَّلِ زبون · الثلاثاء 7:30.",
        ],

        "cta_quote": "«لا جدارَ بين الفرنِ ورصيفِ Borgo Po.»",
        "cta_desc": "الواجهةُ مفتوحةٌ الثلاثاء – السبت · 7:30 – 19:30 · الأحد 7:30 – 13:00 · الإثنين إغلاق.",
        "cta_primary": "اطلب عجين السبت مسبقاً",
        "cta_secondary": "اطَّلِع على كل المعجنات",
    },

    # ─── DIARIO (blog list / detail) ──────────────────────────
    "diario": {
        "eyebrow":  "يوميات الطحين",
        "headline": "ملاحظاتٌ من الفرن، <em>ومن الخميرة،</em> ومن المختبر.",
        "intro":
            "ملاحظاتٌ مختصرةٌ من Carla Madou وَTommaso Rinaldi عن "
            "التخميرات الجارية، وعن المواد الأوليّة الموسمية، وعن "
            "أجمل المعجنات، وعمّا لا يَسير على ما يُرام في المعجنات "
            "من أسبوعٍ لآخر.",
        "read_article": "اقرأ المقال",
        "min_label": "د",
        "min_read_label": "د قراءة",
        "crumb_label": "اليوميات",
        "back_link": "← العودة إلى كلِّ اليوميات",
        "footer_label": "Madou Pasticceria Atelier · يوميات الطحين",
        "empty_body": [
            "المقالُ قيدَ الإعداد التحريري. سيكون النشر الكاملُ متاحاً "
            "قريباً، بقلمِ الباستيشيرا شخصياً أو معلِّمِ التخمير.",
            "هذا الموضِع يصف صوتَ يوميّات الطحين: ملاحظاتٌ قصيرةٌ "
            "من العمل، تأمُّلاتٌ في الخمائر الأم، حكاياتُ تخميرات "
            "ذهبت إلى غير ما يجب. لا تتجاوز ألفي كلمة أبداً، ولا "
            "تَقِلُّ عن خمسمئة كلمة.",
        ],
    },

    "posts": [
        {
            "slug":     "vetrina-autunno-26",
            "kicker":   "الواجهة الجارية",
            "title":    "خمسُ أفكارٍ خلفَ واجهة خريف '26",
            "date":     "6 أكتوبر 2026",
            "read_min": 5,
            "author":   "Carla Madou",
            "lede":
                "دخلت القائمةُ الجديدةُ إلى الواجهة ليلةَ أمس. خمسةُ "
                "مخمَّرات، إعادتانِ لكلاسيكيّاتٍ من المعجنات التورينية، "
                "وقطعةُ pasta sfoglia طارَدتها ثلاث سنوات.",
            "body": [
                ("p", "بناءُ واجهةٍ خريفيةٍ مسألةُ توقيتاتِ تخميرٍ أكثرَ "
                      "منها مسألةَ وصفات. تنخفضُ حرارةُ الغرفة، "
                      "وتُبطئُ الخمائر · وتستجيبُ الأمَّهاتُ ببطء. "
                      "لقائمة خريف '26 عملنا أسبوعين كاملين على "
                      "أزمنة استراحة Saint Honoré بالكستناء وحده."),
                ("h2", "الأفكارُ الخمسُ الجديدة"),
                ("p", "المُخمَّرُ الأول، Saint Honoré بكستناء Cuneo، "
                      "هو إعادةُ قراءةٍ لكلاسيكي Saint Honoré الفرنسي "
                      "مبنيٌّ على ثلاث موادَّ أوَّليةٍ بييمونتية: كستناءُ "
                      "Cuneo IGP من حقل Anna Negroni، وقشدةٌ "
                      "طازجةٌ من مزرعة Inalpi، وَpasta sfoglia "
                      "بالزبدة النورماندية. كان في نَفْسي منذ 2022، "
                      "حين مَرَرتُ بـ Lyon وَتذوقتُ نسخةَ Cyril "
                      "Lignac · غير أنني أردتُ نسخةً تورينيةً، لا "
                      "باريسية."),
                ("h2", "إعادةُ القراءات"),
                ("p", "Mont-Blanc 2026 وَMaritozzo con la panna "
                      "حلوَيانِ أعملُ عليهما منذ سبع سنوات · لا "
                      "يُولَدُ أحدُهما في أكتوبر، غير أنه في أكتوبر "
                      "تَدخلُ موادُّهما الأوليّةُ في أفضل أحوالها: "
                      "كستناء Mortara للأول، والقشدةُ الخريفيةُ "
                      "للثاني. أما Maritozzo بشكلٍ خاص، فقد بدَّلتُه "
                      "سبعَ مرات في اثني عشر شهراً. الآن صار "
                      "كما يجب."),
                ("h2", "قطعة pasta sfoglia"),
                ("p", "Croissant viennoise هي القطعةُ التي أفخرُ "
                      "بها أكثرَ في هذه القائمة. هي pasta sfoglia "
                      "مُخمَّرةٌ 12 ساعةً في غرفةٍ عند +4°C، بزبدةِ "
                      "Isigny AOP مَضْرُوبةٍ على البارد وطحينِ "
                      "طاحونة Brero. أربعٌ وستون طبقةً تظهرُ عند "
                      "القطع، فقاعةُ هواءٍ في كلِّ 0.4 ميليمترٍ من "
                      "العجين. هي المُخمَّرُ الذي وصلتُ إليه بعد "
                      "ثماني سنواتٍ من المحاولات، والسببُ الوحيد "
                      "لوجودي هنا."),
                ("h2", "ما يخرجُ يوم السبت"),
                ("p", "في السبت يُنتجُ Madou 220 قطعةً من "
                      "Croissant viennoise تنفدُ عادةً قبل الساعة "
                      "11:00. لذلك يُنصَحُ كثيراً بالحجز المسبق "
                      "ابتداءً من الخميس — لا سيّما من أكتوبر، حين "
                      "يَعودُ الطلبُ إلى الارتفاع مع البَرْدِ الأول."),
            ],
        },
        {
            "slug":     "lievito-madre-m2",
            "kicker":   "الخميرة الأم",
            "title":    "لماذا انتظرنا سبع سنواتٍ قبل صنع panettone",
            "date":     "28 سبتمبر 2026",
            "read_min": 6,
            "author":   "Tommaso Rinaldi",
            "lede":
                "لم تضع Madou panettone على القائمة إلا في 2018، "
                "أي بعد سبع سنواتٍ من الافتتاح. السببُ واحد: الأمُّ "
                "M-2 لم تكن جاهزة. وفي ما يلي السبب.",
            "body": [
                ("p", "يستدعي panettone أمَّ أمٍّ · يصنعُ كثيرٌ من "
                      "الباستيشيريّين أمَّهم حين يفتتحون المعجنات، "
                      "غيرَ أن panettone الراقي يحتاجُ أمّاً عَملت "
                      "ثلاث سنواتٍ على الأقل، وَطوَّرت ملمحَها "
                      "الأسيتيكي، وَوَجَدت توازنَها. أمُّ Madou M-1 "
                      "— المؤسَّسةُ سنة 2011 — كانت أمّاً لاكتيكية، "
                      "مثاليةً للعجين الورقي ولكنها غيرُ ضاريةٍ "
                      "بما يكفي لـ panettone."),
                ("h2", "كيف تُولَدُ M-2"),
                ("p", "في 2014 أَخَذتُ قطعةً وزنُها 200 غرامٍ من "
                      "M-1 وَجدَّدتُها بثلاثيٍّ لأربعين يوماً · كلَّ "
                      "اثنتي عشرة ساعةً، دائماً. هكذا «تُحرَّفُ» الأمُّ "
                      "اللاكتيكيةُ نحو ملمحٍ مختلط · هي عمليةٌ "
                      "تعلَّمتُها من Achille Zoia. بعد الأربعين "
                      "يوماً، صارت الأمُّ أسيتيكيةً بما يكفي لـ "
                      "panettone، لكنها كانت بعد فتيّةً جداً."),
                ("h2", "أربع سنواتِ انتظار"),
                ("p", "من 2014 إلى 2018 جدَّدتُ M-2 كلَّ اثنتي "
                      "عشرة ساعةً من دون أن أتخلَّفَ ولو مرةً · "
                      "لا في عيد الميلاد، ولا في أغسطس. كانت "
                      "Carla تُسمِّيها «أمَّ المستقبل» لأننا لم "
                      "نستعملْها أبداً. في نوفمبر 2018، عند المحاولة "
                      "السابعة، خرج panettone كما يجبُ أن يخرج. "
                      "منذ ذلك الحين تُنتجُ M-2 panettone وَcolomba "
                      "وَveneziana حصراً، لا شيءَ آخر."),
            ],
        },
    ],

    # ─── ORDINA (reservations) — Gusto's "prenota" ────────────
    "ordina": {
        "eyebrow":      "الطلبيّات والطلبات الخاصة",
        "headline":     "اطلب عجين السبت مسبقاً.",
        "intro":
            "تنفدُ واجهةُ السبت عادةً قبل الساعة 11:00. ولضمان "
            "الحصول على المخمَّرات، يُستحسَنُ الطلبُ المسبقُ ابتداءً "
            "من الأربعاء · الاستلامُ من الكاونتر من 7:30 حتى 13:00. "
            "أما طلبيّاتُ الكعك الخاص وكعك الأعراس، فيُرجى الكتابةُ "
            "إلى atelier@madou-pasticceria.it قبل أسبوعين على الأقل.",
        "primary_label":   "ما الذي تودُّ طلبه مسبقاً؟",
        "primary_placeholder": "السبت 18 أكتوبر · 12 Croissant viennoise + 4 Maritozzi · استلامٌ عند 9:30",
        "name_label":      "الاسم الكامل",
        "phone_label":     "الهاتف",
        "email_label":     "البريد الإلكتروني",
        "submit_label":    "إرسال الطلب المسبق",
        "submit_note":     "ستتلقّى تأكيداً من الكاونتر خلال 24 ساعة. يُدفَع الطلبُ المسبق عند الاستلام.",

        "contact_block": {
            "address_label": "الأتيليه",
            "address":       "Via Sant'Ottavio 36 · 10124 Torino · Borgo Po",
            "phone_label":   "الكاونتر",
            "phone":         "+39 011 8195 770",
            "email_label":   "البريد الإلكتروني",
            "email":         "atelier@madou-pasticceria.it",
            "hours_label":   "أوقات الدوام",
            "hours_list": [
                "الثلاثاء – السبت · 7:30 – 19:30",
                "الأحد · 7:30 – 13:00",
                "الإثنين · إغلاق",
            ],
        },

        "policy_label": "ملاحظات الطلب المسبق",
        "policy_paragraphs": [
            "يُغلَقُ الطلبُ المسبقُ ليوم السبت يومَ الجمعة عند الساعة 18:00. "
            "بعد تلك الساعة، لا نقبلُ إلا إذا أتاح ذلك إنتاجُ اليوم.",
            "للطلبيّات التي تتجاوز 12 قطعة، يُرجى التواصلُ مع الكاونتر "
            "مباشرة. تتطلَّبُ كعكاتُ الأعراس أسبوعين كحدٍّ أدنى من "
            "الإشعار · أما تصميمُ الكعك، فثلاثة أسابيع.",
            "تَتبعُ المواد الأوليّةُ المُتتبَّعة (زبدة Isigny، كاكاو "
            "Sambirano، كستناء IGP، بندق IGP) الرزنامةَ الموسمية. "
            "في حال نفاد المخزون، نقترحُ بديلاً منسجماً.",
        ],

        "small_print":
            "Madou Atelier S.r.l. · الرقم الضريبي 11237680016 · "
            "Via Sant'Ottavio 36، 10124 Torino · Pasticceria Atelier "
            "منذ 2011.",
    },
}
