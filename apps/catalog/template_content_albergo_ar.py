"""Albergo Borgo — Relais hospitality in a Tuscan UNESCO village (AR voice).

T57 · Wave 2 Pass-2 (2026-05-12) · AR MSA native-voice tree mirroring the
IT recursive shape (225 leaf paths · zero missing · zero extra).

Voice contract (AR — Modern Standard Arabic):
- Asharq al-Awsat Travel · Madame Figaro Arabia · Vogue Arabia Travel
  editorial register. Modern Standard Arabic throughout — no dialect.
  Formal hospitality voice; guest addressed in plural (احجزوا · راسلوا)
  for the editorial register.
- Voice anchor `ospitalità di borgo` → `ضيافة القرية الإيطالية`
  (ḍiyāfat al-qaryah al-īṭāliyyah). Preserved verbatim across every
  band — home headline, borgo statement_heading, soggiorno headline,
  concierge headline, site footer_intro — load-bearing in ≥ 15 surfaces.
- Latin proper names + Latin digits stay literal via inherited
  `unicode-bidi: isolate` chrome (precedent: atto T48, madou T50,
  petro T52, sapori T54). All persona, suite names, places, wines,
  producers, hotels and historical figures remain Latin script:
  Borgo San Marco · Relais & Spa, Vittoria Sernigi, Federico Bonechi,
  Tommaso Brigliadori, Anna Ricci, Caterina Sandri, Pietro Brero;
  suites La Vigna · Il Frantoio · Il Pozzo · La Cisterna · La Torre ·
  Il Cortile · La Loggia · La Cantina; Pienza · Val d'Orcia · Siena ·
  Toscana · Firenze · Borgo San Marco di Sopra · Montalcino ·
  Montepulciano · Bagno Vignoni · San Quirico d'Orcia.
- Wines stay Latin: Brunello · Vino Nobile · Chianti Classico ·
  Sangiovese · Champagne. DOCG/DOC stay Italian.
- Latin digits throughout (8, 14, 1, 12, 41) · Italian phone format
  preserved verbatim (+39 0578 748 124) · prices in € with Latin
  digits. Years stay Latin: 1612, 2009, 2014, 2019, 2026.
- Slug fields (URL identifiers) and HTML form `name` fields stay Latin
  — only `label` is Arabic. Post slugs stay Latin (suite-la-vigna).
- AR hospitality lexicon: ضيافة · قرية · منتجع · فريق · كبير الخدمة ·
  استقبال · إقامة · سبا · تذوّق · قبو النبيذ · عريشة.
"""
from __future__ import annotations

from typing import Any


# Imagery — Unsplash CC0 travel-boutique-hotel pool (mirrored from IT).
_HERO_COURTYARD = "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=1600&q=80&auto=format&fit=crop"
_SUITE_VIGNA = "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200&q=80&auto=format&fit=crop"
_SUITE_FRANTOIO = "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&q=80&auto=format&fit=crop"
_SUITE_POZZO = "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=1200&q=80&auto=format&fit=crop"
_SUITE_CISTERNA = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&q=80&auto=format&fit=crop"
_SUITE_TORRE = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&q=80&auto=format&fit=crop"
_SUITE_CORTILE = "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=1200&q=80&auto=format&fit=crop"
_SUITE_LOGGIA = "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=1200&q=80&auto=format&fit=crop"
_SUITE_CANTINA = "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1200&q=80&auto=format&fit=crop"
_BORGO_VALDORCIA = "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA = "https://images.unsplash.com/photo-1568822617270-2c1579f8dfe2?w=1200&q=80&auto=format&fit=crop"
_BORGO_MONTALCINO = "https://images.unsplash.com/photo-1517760444937-f6397edcbbcd?w=1200&q=80&auto=format&fit=crop"
_BORGO_CIPRESSI = "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1200&q=80&auto=format&fit=crop"
_BORGO_CHIANTI = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1200&q=80&auto=format&fit=crop"
_BORGO_PIENZA_PIAZZA = "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_DIRECTOR = "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_MAITRE = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CHEF = "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SOMMELIER = "https://images.unsplash.com/photo-1566753323558-f4e0952af115?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_SPA = "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=900&q=80&auto=format&fit=crop"


ALBERGO_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "القرية",        "kind": "home"},
        {"slug": "camere",     "label": "الأجنحة",       "kind": "blog_list"},
        {"slug": "borgo",      "label": "المنطقة",       "kind": "about"},
        {"slug": "brigata",    "label": "فريق الخدمة",   "kind": "team"},
        {"slug": "soggiorno",  "label": "الإقامة",       "kind": "services"},
        {"slug": "concierge",  "label": "الكونسيرج",     "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "B",
        "logo_word":      "Borgo San Marco",
        "logo_subline":   "Relais & Spa · Pienza منذ 1612",
        "tag":            "موسم 2026 · الحجوزات مفتوحة من مايو حتى أكتوبر",
        "phone":          "+39 0578 748 124",
        "phone_label":    "خطّ الكونسيرج المباشر",
        "email":          "concierge@borgosanmarco.it",
        "email_label":    "راسلوا الإدارة",
        "address":        "Borgo San Marco di Sopra · 53026 Pienza · Siena",
        "hours_compact":  "استقبال على مدار 24 ساعة · تسجيل الدخول من الساعة 14 · المغادرة قبل الساعة 11",
        "hours_footer_rows": [
            "الاستقبال مفتوح على مدار 24 ساعة مع كونسيرج في الصالة",
            "لغات الصالة: italiano · english · français · deutsch",
        ],
        "license":        "رمز CITRA 0521-053026-100201 · فئة خمس نجوم فاخرة · تسجيل Confindustria Alberghi 0428",
        "footer_intro":
            "Borgo San Marco منتجع يضمّ ثماني أجنحة مُعاد تشكيلها داخل كنيسة من "
            "القرن السابع عشر، في قريته التي تحمل الاسم نفسه، وهي بلدة جبلية تابعة "
            "لـ Pienza وتطلّ على Val d'Orcia المُدرجة ضمن قائمة UNESCO. الترميم من "
            "توقيع مكتب Castellini-Mancini عام 2009، والانتساب إلى Relais & Châteaux "
            "منذ 2014، ونجمة Michelin واحدة لمطعم Trebbio منذ 2019. ضيافة القرية "
            "الإيطالية وعدُنا: استقبال واحد يخدم ثماني غرف، وفريق خدمة في الصالة "
            "مؤلّف من أربعة عشر شخصاً، وهدوء قرية لا تزال مأهولة.",

        # Nav reservation CTA (hospitality)
        "nav_cta":         "احجزوا إقامتكم",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "احجزوا",

        # Footer labels
        "foot_studio":   "المنتجع",
        "foot_pages":    "الخريطة",
        "foot_contact":  "الكونسيرج",
        "foot_offices":  "المواقع",
        "offices_footer_rows": [
            "Borgo San Marco di Sopra · 53026 Pienza · Siena",
            "Tenuta Trebbio · قبو النبيذ وحقل الزيتون · 1,2 كم جنوباً",
        ],
        "office_rows": [
            "Borgo San Marco di Sopra 17 · 53026 Pienza · Siena",
            "هاتف +39 0578 748 124 · concierge@borgosanmarco.it",
        ],
        "dossier_label":     "أجنحة",
        "portfolio_label":   "ليالٍ / سنة",
        "territorio_label":  "القرية",
        "superficie_label":  "المساحة",
        "provenance_label":  "الإطلالة",
        "access_label":      "لغات الصالة",
        "availability_label": "الموسمية",
        "price_note":        "السعر عند الطلب · باقات موسمية",
        "nda_required_label": "خصوصية",
        "viewing_on_request": "بالحجز فقط",
        "referent_label":    "مسؤول الصالة",
        "concierge_line_label": "كونسيرج مخصّص",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "cover_location":    "Borgo San Marco di Sopra · Val d'Orcia · UNESCO",
        "cover_image_credit": "تصوير · Massimo Listri",
        "cover_image":       _HERO_COURTYARD,

        "eyebrow":           "Relais & Spa · Val d'Orcia · Pienza منذ 1612",
        "headline":          'ثماني أجنحة في قرية إيطالية من القرن السابع عشر. <em>ضيافة القرية الإيطالية</em>، موسم واحد في السنة.',
        "sub":
            "منتجع يضمّ ثماني أجنحة مُعاد تشكيلها داخل كنيسة من القرن السابع عشر "
            "تابعة لـ Borgo San Marco di Sopra، بلدة جبلية في Pienza تطلّ على "
            "Val d'Orcia. الافتتاح موسمي من مايو حتى نهاية أكتوبر · استقبال كامل "
            "· مطبخ بنجمة Michelin · سبا Aqua di Borgo داخل خزّان مياه من القرن "
            "الثامن عشر · قبو نبيذ خاص. ضيافة القرية الإيطالية بكلّ تفاصيلها.",
        "hero_wordmark":     "Borgo San Marco",
        "hero_location":     "Pienza · Siena · Toscana",
        "hero_counter_label": "أجنحة",
        "hero_counter_value": "8",
        "hero_series_label": "الموسم",
        "hero_series_title": "2026 · أبريل – أكتوبر",
        "hero_series_note":  "الافتتاح في 18 أبريل · الإغلاق في 27 أكتوبر · فريق خدمة في الصالة من 14 شخصاً",

        "primary_cta":         "احجزوا إقامتكم",
        "primary_cta_href":    "concierge",
        "secondary_cta":       "اكتشفوا الأجنحة",
        "secondary_cta_href":  "camere",

        # Hero credit cells — list[4] of tuple[2] (label, value)
        "hero_credit_cells": [
            ("الانتساب",   "Relais & Châteaux"),
            ("المطبخ",     "نجمة Michelin واحدة"),
            ("الترميم",    "Castellini-Mancini · 2009"),
            ("الافتتاح",   "موسمي · 24 أسبوعاً"),
        ],

        # Signature suite section — list[6]
        "signature_label":    "الأجنحة",
        "signature_heading":  "أجنحة القرية، واحد لكلّ غرفة من غرفها التاريخية.",
        "signature_intro":
            "ثماني أجنحة، كلٌّ منها مُعاد تشكيله من فضاء تاريخي في الكنيسة "
            "أو في قبو النبيذ المجاور من القرن الثامن عشر. ما من غرفتين "
            "متشابهتين؛ جميعها تطلّ على Val d'Orcia. ضيافة القرية الإيطالية تتجسّد في كلّ غرفة.",
        "signature": [
            {
                "slug":         "suite-la-vigna",
                "image":        _SUITE_VIGNA,
                "index":        "جناح 01",
                "title":        "La Vigna",
                "territorio":   "الجهة الغربية · الطابق الأول",
                "superficie":   "62 م² · سرير ملكي مزدوج",
                "provenance":   "إطلالة على كرم Sangiovese التاريخي",
                "availability": "متاح من مايو إلى سبتمبر",
            },
            {
                "slug":         "suite-il-frantoio",
                "image":        _SUITE_FRANTOIO,
                "index":        "جناح 02",
                "title":        "Il Frantoio",
                "territorio":   "الطابق الأرضي · الجناح الجنوبي",
                "superficie":   "78 م² · سرير مزدوج + صالون",
                "provenance":   "حجر معصرة الزيتون القديم من عام 1620 في وسط الغرفة",
                "availability": "متاح طوال الموسم",
            },
            {
                "slug":         "suite-il-pozzo",
                "image":        _SUITE_POZZO,
                "index":        "جناح 03",
                "title":        "Il Pozzo",
                "territorio":   "الفناء الداخلي · الطابق الأرضي",
                "superficie":   "54 م² · سرير مزدوج عادي",
                "provenance":   "بئر مثمّن الشكل من القرن السابع عشر في الفناء الخاص",
                "availability": "عند الطلب · للأزواج فقط",
            },
            {
                "slug":         "suite-la-cisterna",
                "image":        _SUITE_CISTERNA,
                "index":        "جناح 04",
                "title":        "La Cisterna",
                "territorio":   "الجناح الشرقي · الطابق السفلي",
                "superficie":   "88 م² · سرير ذو مظلة",
                "provenance":   "قبو خزّان مياه من القرن الثامن عشر · إضاءة طبيعية من الأعلى",
                "availability": "عند الطلب · يُنصح به لشهر العسل",
            },
            {
                "slug":         "suite-la-torre",
                "image":        _SUITE_TORRE,
                "index":        "جناح 05",
                "title":        "La Torre",
                "territorio":   "البرج الزاوي · الطابق الثاني",
                "superficie":   "70 م² · سرير مزدوج + مكتب",
                "provenance":   "إطلالة بزاوية 270 درجة على Val d'Orcia حتى Monte Amiata",
                "availability": "متاح من أبريل إلى أكتوبر",
            },
            {
                "slug":         "suite-il-cortile",
                "image":        _SUITE_CORTILE,
                "index":        "جناح 06",
                "title":        "Il Cortile",
                "territorio":   "الطابق الأرضي · الجناح الشمالي",
                "superficie":   "65 م² · سرير مزدوج + حديقة خاصة",
                "provenance":   "شرفة صغيرة خاصة تطلّ على عريشة الوستارية",
                "availability": "متاح من مايو إلى أكتوبر",
            },
        ],
        "signature_link_all":  "اطّلعوا على الأجنحة الثمانية كلّها",
        "signature_link_href": "camere",

        # Territory chip-row — list of scalar strings
        "territory_label": "المنطقة",
        "territory": [
            "Pienza · Val d'Orcia",
            "Montalcino · أقبية Brunello",
            "Montepulciano · Vino Nobile",
            "San Quirico d'Orcia · الدروب التاريخية",
            "Bagno Vignoni · حمّامات من العصور الوسطى",
            "Monte Amiata · رحلات سيراً",
            "Siena · Palio في يوليو وأغسطس",
            "Cortona · طرق الإتروسكيين",
        ],

        # Director / advisor band — single block
        "advisor_label":     "الإدارة",
        "advisor_heading":   "مديرة تعمل في الصالة. <em>اثنان وثلاثون موسماً في الفندقة</em>.",
        "advisor_intro":
            "تتولّى إدارة Borgo San Marco شخصياً Vittoria Sernigi، صاحبة فندق "
            "توسكانية من مواليد 1964، تتلمذت على يد المعلّم Casiraghi في "
            "Plaza Athénée بباريس، وعلى يد المعلّم Cipriani في Cipriani بـ Venezia. "
            "اثنان وثلاثون موسماً في الفندقة الفاخرة قبل أن تتسلّم زمام القرية "
            "في 2008، لتُجسّد ضيافة القرية الإيطالية في كلّ موسم.",
        "advisor_name":      "Vittoria Sernigi",
        "advisor_role":      "المديرة · عضو في Touring Club Italiano · سوميلييه AIS",
        "advisor_bio":
            "اثنان وثلاثون عاماً من الفندقة الدولية قبل Pienza: Plaza Athénée "
            "Parigi · Cipriani Venezia · Villa San Michele Fiesole. عضو في "
            "Touring Club Italiano منذ 1995، سوميلييه AIS منذ 2002، مدرّبة في "
            "مدرسة Siena للفندقة. حاضرة في الصالة كلّ صباح عند الإفطار، وكلّ "
            "مساء عند تسليم المفاتيح.",
        "advisor_portrait":  _PORTRAIT_DIRECTOR,
        "advisor_cta":       "راسلوا Vittoria",
        "advisor_cta_href":  "concierge",

        # Numbers band — list[4] of tuple[2] (counter, label)
        "numbers_label":    "Borgo San Marco بالأرقام",
        "numbers_heading":  "موسم واحد، استقبال كامل، فريق خدمة واحد.",
        "numbers": [
            ("8",   "أجنحة · ما من غرفتين متشابهتين"),
            ("14",  "شخصاً في فريق الخدمة في الصالة"),
            ("1",   "نجمة Michelin · مطعم Trebbio"),
            ("12",  "سنة من الانتساب إلى Relais & Châteaux"),
        ],
        "numbers_note":
            "الافتتاح الموسمي من 18 أبريل إلى 27 أكتوبر · فريق الصالة كامل "
            "حاضر في الـ 12 وردية خدمة · استقبال على مدار 24 ساعة · ضيافة القرية الإيطالية بلا انقطاع.",

        # Press band — list of scalar strings (home version)
        "press_label":   "في الصحافة",
        "press_intro":   "Borgo San Marco في الرحلات التحريرية بين 2023 و 2025",
        "press_items": [
            "Condé Nast Traveler Italia",
            "Touring Magazine",
            "Departures",
            "Monocle Travel",
            "Bell'Italia",
        ],

        # Private band — closing CTA
        "private_label":     "لضيوفكم الأعزّ",
        "private_heading":   "القرية بكاملها لعائلة واحدة. <em>حصرية لثمانية أيام</em>.",
        "private_intro":
            "يمكن حجز القرية حصرياً لعائلة واحدة أو مجموعة محدودة · ثمانية "
            "أجنحة مخصّصة، فريق خدمة متفرّغ، مطعم مغلق أمام الزوّار، وقبو نبيذ "
            "مفتوح للضيوف. الإتاحة في ثلاث نوافذ فقط في السنة · يُرجى مراسلة "
            "الإدارة قبل ستّة أشهر على الأقلّ.",
        "private_primary":      "راسلوا الإدارة",
        "private_primary_href": "concierge",
        "private_secondary":    "اكتشفوا القرية",
        "private_secondary_href": "borgo",
    },

    # ─── CAMERE (blog_list of suites) ─────────────────────────
    "camere": {
        "eyebrow":          "ثماني أجنحة · Borgo San Marco",
        "headline":         "أجنحة القرية.",
        "intro":
            "يحمل كلّ جناح اسم فضاء تاريخي من فضاءات القرية · "
            "أعاد مكتب Castellini-Mancini تصميم كلّ غرفة في 2009 "
            "مع المحافظة على المخطّط الأصلي للقرن السابع عشر · ضيافة القرية الإيطالية في كلّ تفصيل.",
        "lead_image":       _HERO_COURTYARD,
        "filter_label":     "حسب الاهتمام",
        "filter_groups": [
            {"label": "الإطلالة", "options": ["كرم العنب", "الفناء", "القرية", "Val d'Orcia", "العريشة"]},
            {"label": "الأسرّة",  "options": ["سرير ملكي مزدوج", "سرير مزدوج + صالون", "سرير ذو مظلة", "جناح بمكتب"]},
            {"label": "الموسم",   "options": ["افتتاح أبريل", "متاح من مايو إلى سبتمبر", "موسم الذروة فقط"]},
        ],
        "sort_label":       "الترتيب",
        "sort_options": [
            "حسب المساحة · من الأوسع",
            "حسب الموسمية",
            "حسب عدد الضيوف",
            "حسب الهدوء",
        ],
        "result_count":     "8 أجنحة متاحة في موسم 2026",
        "result_subtitle":  "استقبال كامل لثماني غرف · فريق خدمة في الصالة متفرّغ.",
        "footer_note_label": "الأسعار",
        "footer_note":
            "تشمل جميع الأجنحة إفطاراً في الصالة، وحرّية الوصول إلى سبا "
            "Aqua di Borgo، وتذوّقاً لثلاثة أنواع من النبيذ في قبو النبيذ "
            "بناءً على حجز مسبق. السعر الموسمي يُبلَّغ عند الطلب.",
    },

    # ─── BORGO (about · territorio del relais) ────────────────
    "borgo": {
        "eyebrow":          "Val d'Orcia · UNESCO",
        "headline":         "قرية من القرن السابع عشر لا تزال مأهولة.",
        "intro":
            "Borgo San Marco di Sopra بلدة جبلية تابعة لـ Pienza · يسكنها 41 "
            "نسمة · ساحة مركزية تعود إلى 1571 · كنيسة من 1612 (وهي اليوم "
            "المنتجع) · قبو من القرن الثامن عشر (وهو اليوم السبا). لا تزال "
            "القرية مأهولة بالعائلات السّت ذاتها منذ أربعة أجيال؛ والمنتجع "
            "أحدثها قدوماً، منذ 2009. هنا تنبت ضيافة القرية الإيطالية من جذور المكان.",

        "statement_label":   "ضيافتنا",
        "statement_heading": "ثماني أجنحة، فريق خدمة واحد، قرية بكاملها.",
        "statement_text":
            "ضيافة القرية الإيطالية تعني أنّ الاستقبال واحد لجميع الأجنحة "
            "الثمانية، وأنّ فريق الخدمة في الصالة يعرف كلّ ضيف بالاسم منذ "
            "اليوم الثاني، وأنّ القرية تبقى قرية (بسكّانها الـ 41) حتى حين "
            "تكونون ضيوفاً. لسنا منتجعاً سياحياً ضخماً. لسنا سلسلة فنادق. "
            "ولسنا فندق مدينة.",

        "territories_label":   "الجوار",
        "territories_heading": "ستّ مناطق على بُعد أقلّ من ساعة من القرية.",
        "territories_intro":
            "ينتمي جوار Val d'Orcia إلى ضيافة المنتجع: لكلّ منطقة "
            "مرجع في الصالة مخصّص لاكتشافها · نبيذ، حمّامات، دروب "
            "الإتروسكيين، رحلات في Amiata، أوبرا في Palio بـ Siena.",
        "territories": [
            {
                "image":      _BORGO_VALDORCIA,
                "name":       "Val d'Orcia",
                "region":     "Pienza · San Quirico · Bagno Vignoni",
                "history":    "تراث UNESCO منذ 2004 · مشهد طبيعي من عصر النهضة كما رسمه Lorenzetti. سرو، تلال طينية، ومزارع.",
                "architects": "صفوف السرو · دروب الإتروسكيين المنحوتة",
                "count":      "12 كم",
                "since":      "زيارة: ساعة · المرجع Federico في الصالة",
            },
            {
                "image":      _BORGO_MONTALCINO,
                "name":       "Montalcino",
                "region":     "أقبية Brunello التاريخية",
                "history":    "أقبية Brunello di Montalcino DOCG التاريخية · Biondi-Santi، Casanova di Neri، Il Poggione. تذوّقات خاصّة بحجز مسبق.",
                "architects": "كنائس من العصور الوسطى · قلاع Siena",
                "count":      "28 كم",
                "since":      "زيارة: يوم كامل · المرجع سوميلييه AIS",
            },
            {
                "image":      _BORGO_PIENZA,
                "name":       "Pienza · المدينة المثالية",
                "region":     "ساحة Pio II · الكاتدرائية · Palazzo Piccolomini",
                "history":    "المدينة المثالية لعصر النهضة، صمّمها Bernardo Rossellino لـ Pio II عام 1462. الساحة، الكاتدرائية، Palazzo Piccolomini، إطلالة على Amiata.",
                "architects": "Bernardo Rossellino · 1459-1462",
                "count":      "1,8 كم",
                "since":      "زيارة: ساعتان سيراً · الكونسيرج يرافقكم عند الطلب",
            },
            {
                "image":      _BORGO_CHIANTI,
                "name":       "Montepulciano",
                "region":     "Vino Nobile · أقبية تحت الأرض",
                "history":    "أقبية تحت الأرض منحوتة في الحجر التوفي، بعضها يعود إلى القرن الرابع عشر. تذوّق Vino Nobile di Montepulciano DOCG · أقبية Avignonesi، Salcheto، Boscarelli.",
                "architects": "Antonio da Sangallo il Vecchio · Vignola",
                "count":      "32 كم",
                "since":      "زيارة: يوم كامل · المرجع سوميلييه AIS",
            },
            {
                "image":      _BORGO_CIPRESSI,
                "name":       "Bagno Vignoni",
                "region":     "حمّامات حرّة من القرن الخامس عشر",
                "history":    "ساحة-حوض حرارية من القرن الخامس عشر، الوحيدة في العالم. مياه كبريتية بحرارة 49°م تتدفّق من الصخر، مفتوحة للجميع. عشاء في تراتوريا الساحة مع الطبّاخة Caterina.",
                "architects": "حوض طبيعي · القرن الخامس عشر",
                "count":      "8 كم",
                "since":      "زيارة: نصف يوم · مرجع الصالة Federico",
            },
            {
                "image":      _BORGO_PIENZA_PIAZZA,
                "name":       "Monte Amiata",
                "region":     "بركان خامد · غابات الزان · مزلج",
                "history":    "بركان خامد (1.738 م). غابات زان عمرها قرون، دروب CAI، مزلج في الشتاء. مهرجان الكستناء في نوفمبر في قرية Castiglione d'Orcia.",
                "architects": "دروب CAI · 4 قمم محدّدة",
                "count":      "38 كم",
                "since":      "زيارة: يوم كامل · مرشد جبلي بحجز مسبق",
            },
        ],
        "territory_card_cta":      "لنخطّط معاً · راسلوا الإدارة",
        "territory_card_cta_href": "concierge",

        "referent_label":   "مرجع الصالة",
        "referent_heading": "مرجع واحد طوال الإقامة.",
        "referent_text":
            "منذ لحظة الوصول، لكلّ ضيف مرجع واحد في الصالة — كبير الخدمة "
            "Federico Bonechi أو السوميلييه Anna Ricci بحسب الموسم. يرافق "
            "المرجع كامل الحجز: حجز المطعم، الجلسات في السبا، التذوّقات "
            "في قبو النبيذ، الرحلات في الجوار.",

        "stats_label":  "Borgo San Marco · أرقام 2025",
        # list[4] of tuple[2]
        "stats": [
            ("12",  "سنة من الانتساب إلى Relais & Châteaux"),
            ("162", "ليلة افتتاح في السنة"),
            ("8",   "أجنحة · موسم 2026"),
            ("41",  "ساكناً في القرية"),
        ],
    },

    # ─── BRIGATA (team · staff in sala) ───────────────────────
    "brigata": {
        "eyebrow":       "فريق الخدمة · 14 شخصاً في الصالة",
        "headline":      "الفريق ذاته منذ اثني عشر موسماً.",
        "intro":
            "يتألّف فريق Borgo San Marco من أربعة عشر شخصاً، عشرة منهم "
            "يعودون كلّ موسم منذ 2014. الاستقبال، الصالة، المطعم، السبا، "
            "قبو النبيذ · فريق واحد لثماني أجنحة. هذه هي ضيافة القرية الإيطالية في صورتها التطبيقية.",

        "director_label":       "الإدارة",
        "director_name":        "Vittoria Sernigi",
        "director_role":        "المديرة · المالكة منذ 2008 · سوميلييه AIS · TCI",
        "director_text":
            "تسلّمت Vittoria Sernigi إدارة Borgo San Marco عام 2008 بعد اثنين "
            "وثلاثين موسماً في الفندقة الدولية بين Parigi و Venezia و Fiesole. "
            "دبلوم من مدرسة Lausanne الدولية للفندقة (1985)، وتأهيل في إدارة "
            "الفنادق بـ Cornell. عضو في Touring Club Italiano منذ 1995، "
            "سوميلييه AIS منذ 2002.",
        "director_portrait":    _PORTRAIT_DIRECTOR,
        "director_quote":
            "ضيافة القرية الإيطالية هي الضيافة الوحيدة التي أعرفها. هي "
            "الأبطأ، والأكثر تطلّباً، والأكثر مكافأةً.",
        "director_quote_attribution": "Vittoria Sernigi · مقابلة مع Touring · 2024",

        "advisors_label":   "فريق الخدمة في الصالة",
        "advisors_heading": "أربعة مراجع، عشرة موسميون · صالة واحدة.",
        "advisors_intro":
            "يقود الصالة أربعة مراجع كبار. تمرّ قرارات الخدمة من حكمهم، "
            "لا من خوارزميات سلسلة فنادق.",
        # list[4] of dict
        "advisors": [
            {
                "portrait":    _PORTRAIT_MAITRE,
                "name":        "Federico Bonechi",
                "role":        "كبير الخدمة · المرجع الوحيد للضيوف",
                "bio":
                    "كبير الخدمة منذ 2009 · عشرة مواسم في Borgo San Marco. "
                    "خرّيج Alberghiero di Chianciano · خبرة في Castello "
                    "Banfi و Plaza Athénée. يعرف اسم كلّ ضيف منذ اليوم الثاني.",
                "territories": "الصالة · الاستقبال · الكونسيرج",
                "since":       "في الفريق منذ 2014",
                "langs":       "Italiano · English · Français",
            },
            {
                "portrait":    _PORTRAIT_CHEF,
                "name":        "Tommaso Brigliadori",
                "role":        "الشيف · مطعم Trebbio · نجمة Michelin واحدة",
                "bio":
                    "شيف مطعم Trebbio منذ 2017 · نجمة Michelin منذ 2019. "
                    "تكوّن في Albereta على يد Gualtiero Marchesi، وتأهّل لدى "
                    "Bottura في Modena. مطبخ المنطقة: pici، picci e pinoli، "
                    "خروف Zeri، فاصولياء zolfini، جبن Pienza.",
                "territories": "المطبخ · قبو النبيذ · بستان الخضار",
                "since":       "في الفريق منذ 2017",
                "langs":       "Italiano · English",
            },
            {
                "portrait":    _PORTRAIT_SOMMELIER,
                "name":        "Anna Ricci",
                "role":        "سوميلييه AIS · مسؤولة قبو النبيذ",
                "bio":
                    "سوميلييه AIS منذ 2008 · مسؤولة قبو النبيذ منذ 2015. "
                    "يضمّ القبو 4.200 ملصق بين Brunello و Vino Nobile و "
                    "Chianti Classico ومجموعة صغيرة من Champagne. تذوّقات "
                    "خاصّة في القبو للضيوف مرّتين في الأسبوع.",
                "territories": "قبو النبيذ · التذوّقات · مرافقة المطعم",
                "since":       "في الفريق منذ 2015",
                "langs":       "Italiano · English · Deutsch",
            },
            {
                "portrait":    _PORTRAIT_SPA,
                "name":        "Caterina Sandri",
                "role":        "مسؤولة سبا Aqua di Borgo",
                "bio":
                    "مسؤولة السبا منذ 2018 · دبلوم في العلاج المائي من "
                    "جامعة Siena، تكوين في إدارة السبا لدى Six Senses Toscana. "
                    "سبا Aqua di Borgo مُعاد تشكيله داخل خزّان مياه من القرن "
                    "الثامن عشر · جلسات بحجز مسبق فقط.",
                "territories": "سبا Aqua di Borgo · جلسات · مسبح تحت الأرض",
                "since":       "في الفريق منذ 2018",
                "langs":       "Italiano · English",
            },
        ],

        "partners_label":   "منتجو القرية",
        "partners_heading": "موردو المائدة التاريخيون.",
        "partners_intro":
            "تصل المواد الأوّلية لمطعم Trebbio من موردين في نطاق ثلاثين "
            "كيلومتراً حول القرية، باستثناء الزيت (من إنتاجنا) والخبز "
            "(من مخبز القرية على بعد 200 متر).",
        # list[5] of tuple[2]
        "partners": [
            ("Fattoria Trebbio",         "زيت زيتون بكر ممتاز من ملكنا · حقل زيتون تاريخي على بُعد 1,2 كم من القرية"),
            ("Caseificio Castelmuzio",   "جبن Pienza · caciotta · ricotta · 8 كم من Pienza"),
            ("Azienda agricola Falcorosso", "لحم بقر Chianina · خروف Zeri · دواجن · 12 كم"),
            ("Forno di Pienza · Lorenzini", "خبز توسكاني · schiacciate · grissini · 1,8 كم من القرية"),
            ("Erbario di Sant'Anna",     "أعشاب طبّية · شاي السبا Aqua · دير على بُعد 18 كم"),
        ],

        "press_label":   "في الصحافة · الفريق والمطبخ",
        "press_heading": "جوائز وتنويهات الفريق.",
        # list[5] of dict (magazine, issue, title, byline)
        "press_items": [
            {
                "magazine": "Guida Michelin Italia",
                "issue":    "إصدار 2019 – تأكيد 2025",
                "title":    "نجمة واحدة · مطعم Trebbio · مطبخ توسكاني من المنطقة",
                "byline":   "هيئة تحرير Michelin",
            },
            {
                "magazine": "Touring Magazine",
                "issue":    "أبريل 2024",
                "title":    "Vittoria Sernigi · بورتريه مديرة قرية",
                "byline":   "Maria Sirotti",
            },
            {
                "magazine": "Gambero Rosso",
                "issue":    "يناير 2025 · ثلاث شَوكات",
                "title":    "Trebbio di Borgo San Marco · ثلاث شَوكات مؤكَّدة",
                "byline":   "Eleonora Cozzella",
            },
            {
                "magazine": "Condé Nast Traveler Italia",
                "issue":    "مايو 2023 · Gold List",
                "title":    "Borgo San Marco · ضمن الـ 50 الأوّلين في إيطاليا",
                "byline":   "Caterina Cesari",
            },
            {
                "magazine": "Bell'Italia",
                "issue":    "سبتمبر 2024",
                "title":    "البيوت الكبرى للضيافة الـ 12 في Val d'Orcia",
                "byline":   "Giovanni Rajberti",
            },
        ],

        "numbers_label": "الفريق بالأرقام",
        # list[6] of tuple[2]
        "numbers": [
            ("14", "شخصاً في فريق الخدمة في الصالة"),
            ("10", "موسميون يعودون منذ 2014"),
            ("32", "سنة من خبرة المديرة"),
            ("4",  "لغات في الصالة (IT · EN · FR · DE)"),
            ("12", "سنة من الانتساب إلى Relais & Châteaux"),
            ("4200", "ملصقاً في قبو النبيذ · مسؤولة Anna Ricci AIS"),
        ],

        "visit_label":         "للكتابة إلى الفريق",
        "visit_heading":       "فريق واحد، صالة واحدة.",
        "visit_text":
            "للطلبات بشأن قائمة الطعام، الحساسيات، النبيذ، الرحلات أو "
            "جلسات السبا اكتبوا مباشرة إلى الفريق: نردّ خلال يوم العمل "
            "التالي. توقّع Vittoria شخصياً تأكيد الحجز.",
        "visit_primary":       "راسلوا الإدارة",
        "visit_primary_href":  "concierge",
    },

    # ─── SOGGIORNO (services · l'esperienza del soggiorno) ────
    "soggiorno": {
        "eyebrow":      "التجربة · خمسة فصول من الإقامة",
        "headline":     "خمسة فصول · من Pienza حتى العودة. ضيافة القرية الإيطالية.",
        "intro":
            "تنقسم الإقامة في Borgo San Marco إلى خمسة فصول · الوصول، "
            "الصالة، السبا، قبو النبيذ، والخروج نحو المنطقة. يتكفّل "
            "مرجع الصالة بكلّ فصل منها · ضيافة القرية الإيطالية في إيقاع متّصل.",

        "process_label":   "خمسة فصول",
        "process_heading": "كيف تجري الإقامة.",
        "process_intro":
            "سردية الإقامة واحدة، من اللحظة التي تكتبون فيها إلى الإدارة "
            "وحتى العودة إلى البيت.",
        # list[5] of dict (n, title, text, duration)
        "process": [
            {
                "n":        "01",
                "title":    "التأكيد",
                "text":
                    "ردّ شخصي من Vittoria خلال 24 ساعة من الطلب · اختيار "
                    "الجناح، نافذة الموسم، وأيّ طلبات خاصّة (قائمة الطعام، "
                    "الحساسيات، الرحلات).",
                "duration": "يوم واحد",
            },
            {
                "n":        "02",
                "title":    "الوصول",
                "text":
                    "الاستقبال من الساعة 14 · توصيل من مطار Firenze عند "
                    "الطلب · ترحيب في ساحة القرية مع نبيذ من المنطقة · "
                    "تقديم مرجع الصالة.",
                "duration": "ساعتان",
            },
            {
                "n":        "03",
                "title":    "الصالة وقبو النبيذ",
                "text":
                    "عشاء في مطعم Trebbio · قائمة طعام المنطقة من خمسة "
                    "فصول · مرافقة النبيذ يعلّق عليها السوميلييه · قبو "
                    "النبيذ مفتوح بعد العشاء لمن يرغب في إطالة السهرة.",
                "duration": "ليلة واحدة في الإقامة",
            },
            {
                "n":        "04",
                "title":    "السبا والمنطقة",
                "text":
                    "نصف يوم في سبا Aqua di Borgo (خزّان مياه من القرن "
                    "الثامن عشر) · سباحة، حمّام بخار، ساونا، تدليك مائي "
                    "في الحوض الطبيعي · جلسات بحجز مسبق · رحلة نصف يوم "
                    "في Val d'Orcia مع المرجع.",
                "duration": "نصف يوم",
            },
            {
                "n":        "05",
                "title":    "الخروج",
                "text":
                    "المغادرة قبل الساعة 11 · إفطار متأخّر حتى الساعة 10:30 "
                    "تحت عريشة الوستارية · هدية الوداع (زيت من Fattoria "
                    "Trebbio · كتيّب صغير عن القرية) · مرافقة في العودة.",
                "duration": "نصف يوم",
            },
        ],

        "testimonial_label":  "صوت الضيف",
        "testimonial_text":
            "«ثلاث إقامات في ثلاثة مواسم مختلفة، والفريق ذاته دائماً، و"
            "Federico في الاستقبال دائماً. من النادر في إيطاليا أن تجدوا "
            "فندقاً يبقى فيه الوعد المُعطى في المرّة الأولى صادقاً حتى "
            "في الزيارة الثالثة.»",
        "testimonial_author": "Giorgio Borghi · Milano · ضيف منذ 2018",

        "faq_label":    "أسئلة متكرّرة من الإدارة",
        # list[6] of dict (q, a)
        "faq_items": [
            {
                "q": "هل الفندق مفتوح طوال السنة؟",
                "a":
                    "لا. يفتح Borgo San Marco من 18 أبريل إلى 27 أكتوبر "
                    "2026 — أربعة وعشرون أسبوعاً من الموسم. يسمح الإغلاق "
                    "الشتوي بصيانة الأجنحة وراحة فريق الصالة. ما من "
                    "استثناء، حتى لعطلة رأس السنة.",
            },
            {
                "q": "هل يمكن حجز القرية بكاملها لعائلة واحدة؟",
                "a":
                    "نعم · في ثلاث نوافذ في السنة (يونيو، سبتمبر، نهاية "
                    "أكتوبر). ثماني أجنحة مخصّصة · مطعم مغلق أمام الزوّار "
                    "الخارجيين · فريق متفرّغ. يُرجى مراسلة الإدارة قبل "
                    "ستّة أشهر على الأقلّ من التاريخ المرغوب.",
            },
            {
                "q": "هل يمكن تنظيم حفلات زفاف في القرية؟",
                "a":
                    "حفلات الزفاف الحميمة فقط · بحدّ أقصى 36 ضيفاً · "
                    "المراسم المدنية في loggia الطابق النبيل · العشاء "
                    "تحت عريشة الوستارية. لا ننظّم حفلات تتجاوز 36 ضيفاً "
                    "حفاظاً على حجم القرية. يُرجى مراسلة Vittoria قبل "
                    "سنة واحدة على الأقلّ.",
            },
            {
                "q": "هل تُقبَل الكلاب الصغيرة؟",
                "a":
                    "نعم · عند الطلب · في جناحَيْ الطابق الأرضي (Il Frantoio "
                    "و Il Pozzo). رسم إضافي 30 € لليلة · إناء، فراش "
                    "وبسكويت مشمولات. مربّية حيوانات أليفة من القرية متاحة "
                    "بحجز مسبق خلال ساعات العشاء في المطعم.",
            },
            {
                "q": "هل يمكنني زيارة قبو النبيذ حتى لو لم أكن ضيفاً في المطعم؟",
                "a":
                    "نعم · قبو النبيذ مفتوح لضيوف القرية مرّتين في الأسبوع "
                    "(الثلاثاء والخميس بعد الظهر، الساعة 17–19) لتذوّق "
                    "ثلاثة أنواع من النبيذ مع Anna · الحجز إلزامي عند "
                    "الاستقبال.",
            },
            {
                "q": "هل يتوفّر الوايفاي في الأجنحة؟",
                "a":
                    "نعم · خطّ ألياف بسرعة 1 جيغابت/ثانية · متاح في الأجنحة "
                    "الثمانية جميعها، في الصالة وفي السبا. عند الطلب يمكن "
                    "تفعيل وضع digital detox: يبقى الجناح بلا اتصال طوال "
                    "الإقامة · صندوق للأجهزة عند الوصول.",
            },
        ],

        "cta_label":         "لكي تبدؤوا",
        "cta_heading":       "<em>موسم قصير</em>، فريق واحد.",
        "cta_text":
            "تفتح نوافذ موسم 2026 في 18 أبريل · الأجنحة الأكثر طلباً "
            "(La Vigna، Il Cortile، La Torre) تنفد قبل نهاية مايو. "
            "راسلوا الإدارة للحجز.",
        "cta_primary":       "احجزوا إقامتكم",
        "cta_primary_href":  "concierge",
    },

    # ─── CONCIERGE (contact · concierge dedicato) ─────────────
    "concierge": {
        "eyebrow":      "كونسيرج مخصّص · Vittoria Sernigi",
        "headline":     "راسلوا الإدارة. ضيافة القرية الإيطالية تبدأ هنا.",
        "intro":
            "لطلب الحجز، ومواعيد حصرية للقرية، والباقات الموسمية، وأيّ "
            "سؤال يخصّ الإقامة، اكتبوا مباشرة إلى الإدارة. تردّ Vittoria "
            "شخصياً خلال يوم العمل التالي.",

        "phone_label":   "الخطوط المباشرة",
        "phone_intro":
            "الاستقبال مفتوح على مدار 24 ساعة · كونسيرج مخصّص في الصالة "
            "في ورديات متواصلة · رقم مباشر للطوارئ.",
        # list[4] of tuple[2]
        "phone_rows": [
            ("الكونسيرج",   "+39 0578 748 124"),
            ("الإدارة",     "+39 0578 748 100 · Vittoria فقط"),
            ("المطعم",      "+39 0578 748 130 · حجوزات Trebbio"),
            ("السبا",       "+39 0578 748 145 · حجوزات Aqua"),
        ],

        "form_section_label": "طلب حجز",
        "form_section_intro":
            "اذكروا التواريخ المرغوبة، الجناح المفضّل (أو حصرية القرية) "
            "وأيّ طلبات خاصّة. تردّ Vittoria شخصياً بالبريد الإلكتروني "
            "بالتأكيد أو باقتراح بديل خلال 24 ساعة.",
        "form_helper_required":  "الحقول التي تحمل علامة · إلزامية",
        "form_submit_button":    "أرسلوا الطلب إلى الإدارة",
        "form_submit_note":
            "يتمّ التأكيد النهائي بدفع عربون 30% عبر تحويل مصرفي · "
            "الرصيد عند الوصول في الاستقبال.",
        # list[10] of dict (label, name, type, required, options)
        "form_fields": [
            {"label": "الاسم واللقب",            "name": "name",       "type": "text",     "required": True,  "options": []},
            {"label": "البريد الإلكتروني · ردّ مباشر", "name": "email",  "type": "email",    "required": True,  "options": []},
            {"label": "الهاتف",                  "name": "phone",      "type": "tel",      "required": False, "options": []},
            {"label": "تاريخ الوصول",            "name": "arrival",    "type": "date",     "required": True,  "options": []},
            {"label": "تاريخ المغادرة",          "name": "departure",  "type": "date",     "required": True,  "options": []},
            {"label": "عدد الضيوف",              "name": "guests",     "type": "number",   "required": True,  "options": []},
            {"label": "الجناح المفضّل",          "name": "suite",      "type": "select",   "required": False,
             "options": ["La Vigna", "Il Frantoio", "Il Pozzo", "La Cisterna", "La Torre", "Il Cortile", "حصرية القرية · 8 أجنحة", "بلا تفضيل"]},
            {"label": "الباقة",                  "name": "package",    "type": "select",   "required": False,
             "options": ["إقامة قصيرة · ليلتان", "إقامة كلاسيكية · 4 ليالٍ", "إقامة طويلة · 7 ليالٍ", "حصرية القرية · 5 ليالٍ", "زفاف حميم"]},
            {"label": "الحساسيات أو طلبات غذائية", "name": "allergies", "type": "text",     "required": False, "options": []},
            {"label": "ملاحظات للإدارة",         "name": "notes",      "type": "textarea", "required": False, "options": []},
        ],

        "offices_label":   "العناوين",
        "offices_heading": "القرية والمزارع.",
        "offices_intro":
            "يمكن الوصول إلى القرية بالسيارة من Firenze (ساعة و 45 دقيقة) "
            "أو من Roma (ساعتان و 30 دقيقة) · توصيل من مطار Firenze أو "
            "محطّة Chiusi-Chianciano عند الطلب.",
        # list[3] of dict (role, city, address, hours, email)
        "offices": [
            {
                "role":     "القرية · الاستقبال",
                "city":     "Pienza · Siena",
                "address":  "Borgo San Marco di Sopra 17 · 53026 Pienza",
                "hours":    "استقبال على مدار 24 ساعة · تسجيل الدخول 14–22 · المغادرة قبل الساعة 11",
                "email":    "concierge@borgosanmarco.it",
            },
            {
                "role":     "Fattoria Trebbio · قبو النبيذ وحقل الزيتون",
                "city":     "Pienza · Siena · 1,2 كم من القرية",
                "address":  "Strada provinciale 146 · 53026 Pienza",
                "hours":    "قبو النبيذ · الثلاثاء والخميس 17–19 · تذوّقات بحجز مسبق",
                "email":    "cantina@borgosanmarco.it",
            },
            {
                "role":     "Aqua di Borgo · السبا",
                "city":     "خزّان مياه من القرن الثامن عشر · الطابق السفلي",
                "address":  "Borgo San Marco di Sopra 17 · الطابق –1",
                "hours":    "السبا 9–13 · 15–20 · جلسات بحجز مسبق",
                "email":    "spa@borgosanmarco.it",
            },
        ],

        "press_contact_label": "الصحافة والإعلام",
        "press_contact_text":
            "للطلبات التحريرية، التغطيات الصحفية والمقابلات مع الإدارة · "
            "يُرجى مراسلة Maria Bonelli، مكتب صحافة Vittoria Sernigi، "
            "مع ذكر الوسيلة والموضوع.",
        "press_contact_email": "stampa@borgosanmarco.it",
    },

    # ─── POSTS (8 suites · the room cards consumed by camere blog_list) ─
    "posts": [
        {
            "slug":         "suite-la-vigna",
            "image":        _SUITE_VIGNA,
            "kicker":       "جناح 01",
            "title":        "La Vigna",
            "date":         "موسم 2026 · أبريل – أكتوبر",
            "author":       "Borgo San Marco",
            "read_min":     "62 م²",
            "lede":
                "الجناح المُطلّ على كرم Sangiovese التاريخي · الطابق الأول من "
                "الجناح الغربي · سرير ملكي مزدوج · سقف من العوارض الأصلية "
                "للقرن السابع عشر.",
            "footer_strap": "متاح من مايو إلى سبتمبر · إطلالة على كرم العنب",
            # list of 2-tuples (k, v)
            "meta_rows": [
                ("الطابق",        "الأول · الجناح الغربي"),
                ("الأسرّة",       "سرير ملكي مزدوج + كرسي طويل"),
                ("المساحة",       "62 م² + 8 م² شرفة صغيرة"),
                ("الإطلالة",      "كرم Sangiovese التاريخي · حقل الزيتون"),
                ("الحمّام",       "رخام travertino · دش walk-in + بانيو"),
                ("شامل",          "إفطار · سبا · تذوّق في قبو النبيذ"),
                ("الموسمية",      "متاح من مايو إلى سبتمبر"),
            ],
            # list of 2-tuples (kind, text)
            "body": [
                ("p", "La Vigna أكثر الأجنحة طلباً في البيت · إطلالة مباشرة على كرم Sangiovese التاريخي الذي يُعطي عناقيد Brunello من ملك Fattoria Trebbio. سقف من العوارض الأصلية للقرن السابع عشر، أرضية من القرميد العتيق، وأثاث مستردّ من بيوت القرية."),
                ("p", "الشرفة الصغيرة الخاصّة بمساحة 8 م² مفروشة بكنبة من الخيزران وطاولة من حجر pietra serena · مثالية لإفطار ثنائي أو لكأس Brunello المسائي (المشمول دائماً، من قبو Anna)."),
                ("h3", "الكرم التاريخي"),
                ("p", "يمتدّ كرم Fattoria Trebbio على 4,2 هكتاراً جنوب القرية، بتعريض شرقي-جنوبي-شرقي. حصاد يدوي في أكتوبر · تخمير في خزّانات صغيرة من الفولاذ · تعتيق في برميل خشب البلّوط الكبير · تعبئة في المزرعة. يحمل Brunello توقيع القرية ذاته."),
                ("ul", ["السعة · شخصان بالغان · عند الطلب مهد للرضيع", "الوايفاي · ألياف 1 جيغابت/ثانية · خطّ مباشر على شبكة القرية", "المكيّف · مستقلّ، قابل للضبط من الجناح", "خزنة · رقمية · للأشياء الثمينة", "تلفاز · 55 بوصة · قنوات دولية عند الطلب"]),
                ("p", "جناح La Vigna متاح من مايو إلى نهاية سبتمبر. لموسم 2026 يمكن حجزه حصراً ضمن باقة من ثلاث ليالٍ على الأقلّ."),
            ],
        },
        {
            "slug":         "suite-il-frantoio",
            "image":        _SUITE_FRANTOIO,
            "kicker":       "جناح 02",
            "title":        "Il Frantoio",
            "date":         "موسم 2026 · كامل الفترة",
            "author":       "Borgo San Marco",
            "read_min":     "78 م²",
            "lede":
                "الجناح الأوسع · الطابق الأرضي من الجناح الجنوبي · في وسط "
                "الغرفة حجر معصرة الزيتون القديم من 1620 محفوظ بوصفه عنصراً "
                "معمارياً.",
            "footer_strap": "متاح من أبريل إلى أكتوبر · الطابق الأرضي الجناح الجنوبي",
            "meta_rows": [
                ("الطابق",        "الأرضي · الجناح الجنوبي"),
                ("الأسرّة",       "سرير مزدوج + صالون منفصل"),
                ("المساحة",       "78 م² + 12 م² فناء"),
                ("الإطلالة",      "فناء داخلي مع حجر المعصرة من 1620"),
                ("الحمّام",       "رخام أبيض · بانيو حرّ + دش"),
                ("شامل",          "إفطار · سبا · تذوّق في قبو النبيذ + الزيت"),
                ("الموسمية",      "متاح طوال الموسم"),
            ],
            "body": [
                ("p", "Il Frantoio أكبر الأجنحة الثمانية · مساحة 78 م² زائد 12 م² من فناء خاصّ على الفناء الداخلي. حُفظ حجر معصرة الزيتون الأصلي الدائري من 1620 في وسط الغرفة بوصفه عنصراً معمارياً — غير صالح للعمل لكن سليم، من حجر pietra serena."),
                ("p", "يشمل الجناح قبواً صغيراً خاصّاً يحتوي ستّ زجاجات من Brunello لـ Fattoria Trebbio (محصول 2018-2020) وزجاجة من زيت الزيتون البكر الممتاز من حقل الزيتون التاريخي · يمكن للضيوف التذوّق كما يشاؤون، وتُحتسب الفاتورة في نهاية الإقامة فقط."),
                ("h3", "المعصرة التاريخية"),
                ("p", "كانت المعصرة الأصلية تعمل من 1620 حتى 1968، حين بدأ زيت Fattoria Trebbio يُعالَج في المعصرة المشتركة لـ Pienza. حجر معصرة الجناح أحد الحجرَيْن الأصليّيْن · الآخر معروض في متحف البيت، إلى جوار الفناء."),
                ("ul", ["السعة · شخصان بالغان + طفل على الكنبة-السرير", "الوايفاي · ألياف 1 جيغابت/ثانية", "المكيّف · مستقلّ، منطقتان غرفة/صالون", "الفناء · 12 م² مع طاولة وكراسي من الحديد المطروق", "قبو صغير خاصّ · 6 زجاجات Brunello + زجاجة زيت زيتون بكر ممتاز"]),
                ("p", "Il Frantoio متاح طوال الموسم المفتوح. حجز لليلتين على الأقلّ."),
            ],
        },
        {
            "slug":         "suite-il-pozzo",
            "image":        _SUITE_POZZO,
            "kicker":       "جناح 03",
            "title":        "Il Pozzo",
            "date":         "موسم 2026 · عند الطلب",
            "author":       "Borgo San Marco",
            "read_min":     "54 م²",
            "lede":
                "الجناح الأكثر خصوصية · الطابق الأرضي مع وصول مباشر إلى الفناء "
                "الداخلي من القرن السابع عشر · في وسط الفناء البئر المثمّن "
                "الأصلي من 1612.",
            "footer_strap": "عند الطلب · للأزواج فقط · فناء خاصّ",
            "meta_rows": [
                ("الطابق",        "الأرضي · الفناء الداخلي"),
                ("الأسرّة",       "سرير مزدوج عادي"),
                ("المساحة",       "54 م² + فناء خاصّ 28 م²"),
                ("الإطلالة",      "فناء مثمّن مع بئر من 1612"),
                ("الحمّام",       "حجر pietra serena · دش walk-in"),
                ("شامل",          "إفطار · سبا · قبو النبيذ · الفناء"),
                ("الموسمية",      "عند الطلب · للأزواج فقط · حيوانات أليفة مسموحة"),
            ],
            "body": [
                ("p", "Il Pozzo أكثر أجنحة البيت خصوصية · الوصول الوحيد من الفناء الداخلي، بلا أيّ إطلالة على خارج القرية. البئر المثمّن من 1612 لا يزال يعمل (مياه عذبة من مياه San Quirico الجوفية) ويُلقي ظلاًّ على فناء صغير بمساحة 28 م² مخصّص حصراً للجناح."),
                ("p", "يُعرض هذا الجناح للأزواج فقط · بلا أطفال · ويسمح بكلاب صغيرة دون 10 كغ عند الطلب (رسم إضافي 30 € لليلة، إناء وفراش مشمولان)."),
                ("h3", "البئر المثمّن"),
                ("p", "البئر المثمّن واحد من ثلاثة آبار في القرية · وهو الوحيد الذي لا يزال يعمل. مثمّن مثل قبّة Brunelleschi التي كان Pio II من مُعجَبيها. بُني في 1612 على يد البنّاء ذاته الذي رفع الكنيسة · توقيع منحوت داخل فوّهة البئر، غير مقروء منذ 1923 لكن موثّق في كتيّب من 1898 محفوظ في الكنيسة."),
                ("ul", ["السعة · شخصان بالغان · بلا أطفال", "كلاب صغيرة مقبولة · رسم إضافي 30 € / ليلة", "فناء خاصّ · 28 م² مع طاولة حديدية · ظلّ البئر", "الوايفاي · ألياف 1 جيغابت/ثانية", "المكيّف · مستقلّ"]),
                ("p", "Il Pozzo متاح فقط عند الطلب المباشر إلى الإدارة. إقامة دنيا ثلاث ليالٍ."),
            ],
        },
        {
            "slug":         "suite-la-cisterna",
            "image":        _SUITE_CISTERNA,
            "kicker":       "جناح 04",
            "title":        "La Cisterna",
            "date":         "موسم 2026 · عند الطلب",
            "author":       "Borgo San Marco",
            "read_min":     "88 م²",
            "lede":
                "جناح مُعاد تشكيله في قبو خزّان مياه من القرن الثامن عشر · "
                "الطابق السفلي · سرير ذو مظلة · إضاءة طبيعية من الأعلى عبر "
                "الكوّة الأصلية من 1742.",
            "footer_strap": "عند الطلب · يُنصح به لشهر العسل",
            "meta_rows": [
                ("الطابق",        "الطابق السفلي (–1) · الجناح الشرقي"),
                ("الأسرّة",       "سرير مزدوج + مظلة من الجوز"),
                ("المساحة",       "88 م² · قبو بارتفاع 4,2 م"),
                ("الإطلالة",      "كوّة سماوية · بلا إطلالة خارجية"),
                ("الحمّام",       "حجر travertino · بانيو على شكل خزّان"),
                ("شامل",          "إفطار · سبا · قبو النبيذ · تجربة ليلية"),
                ("الموسمية",      "عند الطلب · يُنصح به لشهر العسل"),
            ],
            "body": [
                ("p", "La Cisterna أكثر أجنحة القرية طلباً · مُعاد تشكيله في قبو خزّان مياه من القرن الثامن عشر، الطابق السفلي، سقف بارتفاع 4,2 أمتار. تدخل الإضاءة الطبيعية فقط من الكوّة السماوية الأصلية من 1742 · ليلاً تدخل سماء Val d'Orcia المرصّعة بالنجوم مباشرةً إلى الغرفة."),
                ("p", "كان الخزّان الأصلي يجمع مياه الأمطار من سطح الكنيسة حتى 1923، حين رُبطت القرية بشبكة المياه البلدية. حافظ ترميم Castellini-Mancini في 2009 على الانحناء الأصلي والنقش المُحاط بالجدار للمالك من القرن الثامن عشر (Giovan Pietro Buonsignori، 1742)."),
                ("h3", "السرير ذو المظلة"),
                ("p", "السرير قطعة تاريخية · مظلة من خشب الجوز المصمت من Pratomagno، حديد مطروق يدوياً من حدّاد القرية (Mario Calzini، 1971-2018، واليوم يُكمل ابن أخيه Luca الورشة). أقمشة المظلة من كتّان Bonotto. استُبدلت مصابيح الزيت بأضواء LED صغيرة بحرارة دافئة."),
                ("ul", ["السعة · شخصان بالغان · بلا أطفال", "الوايفاي · ألياف 1 جيغابت/ثانية · لا استقبال 4G في الطابق السفلي", "المكيّف · مستقلّ، حرارة ثابتة 20 °م حتى صيفاً", "البانيو · من حجر travertino · على شكل خزّان", "تجربة ليلية · بحجز مسبق فتح الكوّة مع مرصد القرية الفلكي"]),
                ("p", "La Cisterna متاح فقط بطلب مباشر · يُنصح به خاصّة لشهر العسل والذكريات السنوية. إقامة دنيا أربع ليالٍ."),
            ],
        },
        {
            "slug":         "suite-la-torre",
            "image":        _SUITE_TORRE,
            "kicker":       "جناح 05",
            "title":        "La Torre",
            "date":         "موسم 2026 · أبريل – أكتوبر",
            "author":       "Borgo San Marco",
            "read_min":     "70 م²",
            "lede":
                "جناح مُعاد تشكيله في البرج الزاوي من العصور الوسطى · الطابق "
                "الثاني · إطلالة بزاوية 270 درجة على Val d'Orcia حتى Monte "
                "Amiata · سرير مزدوج مع مكتب مجاور.",
            "footer_strap": "متاح من أبريل إلى أكتوبر · إطلالة 270 درجة",
            "meta_rows": [
                ("الطابق",        "الثاني · البرج الزاوي"),
                ("الأسرّة",       "سرير مزدوج + مكتب مع كنبة-سرير"),
                ("المساحة",       "70 م² + 6 م² مكتب"),
                ("الإطلالة",      "270° · Val d'Orcia · Monte Amiata · Pienza"),
                ("الحمّام",       "رخام أسود · دش walk-in"),
                ("شامل",          "إفطار · سبا · قبو النبيذ · منظار فلكي"),
                ("الموسمية",      "أبريل – أكتوبر · سلّم من 23 درجة"),
            ],
            "body": [
                ("p", "La Torre يشغل الطابق الثاني من البرج الزاوي للقرية من العصور الوسطى · إطلالة بزاوية 270 درجة على Val d'Orcia (جنوب-غرب)، على Pienza (شمال-غرب)، وحتى Monte Amiata (جنوب-شرق) في الأيام الصافية. ثلاث نوافذ أصلية من القرن السادس عشر بزجاج رصاصي مرمَّم."),
                ("p", "المكتب المجاور بمساحة 6 م² مفروش بمنضدة من خشب الجوز من Pratomagno ومكتبة من الكتب عن Val d'Orcia (بالإيطالية والإنكليزية) · مثالي لمن يحتاج إلى نصف يوم عمل خلال الإقامة."),
                ("h3", "المنظار الفلكي"),
                ("p", "البرج مزوّد بمنظار فلكي صغير Bresser 90 مم مثبّت على ارتفاع النافذة الغربية · مثالي لمراقبة كوكبات Val d'Orcia (تلوّث ضوئي معدوم). دليل الاستخدام في الدرج · إرشاد مسائي مع مرجع الصالة بحجز مسبق."),
                ("ul", ["السعة · شخصان بالغان + طفل على كنبة-سرير المكتب", "السلّم · 23 درجة · لا مصعد في البرج", "الوايفاي · ألياف 1 جيغابت/ثانية", "المكيّف · مروحة سقف + جهاز مستقلّ", "المنظار · Bresser 90 مم + الدليل + الإرشاد عند الطلب"]),
                ("p", "La Torre متاح من أبريل إلى أكتوبر. إقامة دنيا ليلتان."),
            ],
        },
        {
            "slug":         "suite-il-cortile",
            "image":        _SUITE_CORTILE,
            "kicker":       "جناح 06",
            "title":        "Il Cortile",
            "date":         "موسم 2026 · مايو – أكتوبر",
            "author":       "Borgo San Marco",
            "read_min":     "65 م²",
            "lede":
                "جناح بشرفة صغيرة خاصّة تطلّ على عريشة الوستارية · الطابق "
                "الأرضي من الجناح الشمالي · حديقة خاصّة بمساحة 18 م² مع "
                "طاولة وكراسي.",
            "footer_strap": "متاح من مايو إلى أكتوبر · حديقة + عريشة",
            "meta_rows": [
                ("الطابق",        "الأرضي · الجناح الشمالي"),
                ("الأسرّة",       "سرير مزدوج + كنبة-سرير"),
                ("المساحة",       "65 م² + حديقة خاصّة 18 م²"),
                ("الإطلالة",      "عريشة الوستارية · حديقة خاصّة"),
                ("الحمّام",       "رخام travertino · دش walk-in"),
                ("شامل",          "إفطار · سبا · قبو النبيذ · حديقة خاصّة"),
                ("الموسمية",      "مايو – أكتوبر · إزهار الوستارية مايو-يونيو"),
            ],
            "body": [
                ("p", "Il Cortile يتمتّع بأكثر الأبواب وصولاً مباشراً إلى عريشة الوستارية، روح القرية · زُرعت الوستارية في 1924 على يد عائلة Buonsignori، الإزهار الكامل في الأسابيع الثلاثة الأولى من مايو. حديقة خاصّة بمساحة 18 م² تحدّها جدار قصير من حجر pietra serena · مفروشة بكرسيَّيْن من الحديد المطروق وطاولة من الحجر."),
                ("p", "الإفطار تحت العريشة من تقاليد البيت · كلّ صباح من الساعة 8 إلى 10:30 يتحوّل العريش إلى ساحة إفطار صغيرة · الضيوف يجلسون على طاولات منخفضة، فريق الصالة في مرور دائم · خبز Lorenzini الساخن من مخبز القرية، مربّيات الوردة البرّية من إعداد الإدارة، أجبان Castelmuzio، فاكهة من المزارع المجاورة."),
                ("h3", "وستارية 1924"),
                ("p", "زُرعت الوستارية في 1924 على يد Caterina Buonsignori (1902-1989، آخر سلالة عائلة القرية الأصلية) هديةَ عرس لابنتها Anna. منذ ذلك الحين نمت حتى غطّت العريشة بكاملها. يدوم الإزهار الكامل ثلاثة أسابيع · من العقد الأول من مايو حتى 25 مايو تقريباً."),
                ("ul", ["السعة · شخصان بالغان + طفل على كنبة-السرير", "حديقة خاصّة · 18 م² · جدار من حجر pietra serena · مفروشة", "الوايفاي · ألياف 1 جيغابت/ثانية", "المكيّف · مستقلّ", "الإفطار · يُقدَّم تحت عريشة الوستارية من الساعة 8 إلى 10:30"]),
                ("p", "Il Cortile متاح من مايو إلى أكتوبر. لمشاهدة الوستارية في زهرتها يُحجز في النصف الأول من مايو."),
            ],
        },
        {
            "slug":         "suite-la-loggia",
            "image":        _SUITE_LOGGIA,
            "kicker":       "جناح 07",
            "title":        "La Loggia",
            "date":         "موسم 2026 · أبريل – أكتوبر",
            "author":       "Borgo San Marco",
            "read_min":     "82 م²",
            "lede":
                "جناح الطابق النبيل · loggia من عصر النهضة تطلّ على Pienza · "
                "سقف ذو صناديق مزخرفة من 1671 · سرير ملكي مزدوج + مكتب + "
                "حمّام رئيسي.",
            "footer_strap": "متاح من أبريل إلى أكتوبر · الطابق النبيل",
            "meta_rows": [
                ("الطابق",        "الأول النبيل · الجناح الغربي"),
                ("الأسرّة",       "سرير ملكي مزدوج + مكتب"),
                ("المساحة",       "82 م² + loggia 14 م²"),
                ("الإطلالة",      "Pienza · الكاتدرائية · Palazzo Piccolomini"),
                ("الحمّام",       "رخام travertino + statuario · بانيو + دش منفصل"),
                ("شامل",          "إفطار · سبا · قبو النبيذ · عشاء خاصّ في loggia عند الطلب"),
                ("الموسمية",      "أبريل – أكتوبر · مراسم مدنية ممكنة في loggia"),
            ],
            "body": [
                ("p", "La Loggia جناح الطابق النبيل · 82 م² زائد loggia من عصر النهضة بمساحة 14 م² تطلّ على Pienza · يُرى منها كاتدرائية Bernardo Rossellino من 1462 و Palazzo Piccolomini. رُمِّم السقف ذو الصناديق المزخرفة من 1671 في 2009 على يد Mauro Pellegrini، مرمِّم من Siena."),
                ("p", "loggia هي مكان المراسم المدنية لحفلات الزفاف الحميمة في القرية (بحدّ أقصى 36 ضيفاً). عند الطلب يمكن تنظيم عشاء خاصّ في loggia لضيوف الجناح · خدمة الشيف Tommaso · السعر عند الطلب."),
                ("h3", "السقف ذو الصناديق من 1671"),
                ("p", "كلّف Pietro Buonsignori السقف في 1671 الرسّامَ Domenico Manetti من Siena (1609-1683). ثلاثون صندوقاً مزخرفاً بالتمبرا: مشاهد من Val d'Orcia، رموز شعار العائلة، ملائكة قاطفة للعنب. أعاد ترميم 2009 الألوان الأصلية؛ تأكّد تذهيب الزخارف في المختبر."),
                ("ul", ["السعة · شخصان بالغان + طفل على كنبة-سرير المكتب", "loggia · 14 م² تطلّ على Pienza · مفروشة · عشاء خاصّ عند الطلب", "الوايفاي · ألياف 1 جيغابت/ثانية", "المكيّف · منطقتان", "مراسم مدنية · في loggia · بحدّ أقصى 36 ضيفاً · عند الطلب"]),
                ("p", "La Loggia متاح من أبريل إلى أكتوبر. إقامة دنيا ليلتان، وثلاث ليالٍ في نافذة المراسم المدنية."),
            ],
        },
        {
            "slug":         "suite-la-cantina",
            "image":        _SUITE_CANTINA,
            "kicker":       "جناح 08",
            "title":        "La Cantina",
            "date":         "موسم 2026 · عند الطلب",
            "author":       "Borgo San Marco",
            "read_min":     "92 م²",
            "lede":
                "جناح مُعاد تشكيله في قبو النبيذ القديم من القرن الثامن عشر "
                "(قبو النبيذ التشغيلي اليوم في Fattoria Trebbio) · الطابق "
                "السفلي · سرير مزدوج + منطقة جلوس + قبو خاصّ بـ 12 ملصقاً.",
            "footer_strap": "عند الطلب · مثالي لمحبّي النبيذ",
            "meta_rows": [
                ("الطابق",        "الطابق السفلي (–1) · الجناح الجنوبي"),
                ("الأسرّة",       "سرير ملكي مزدوج + منطقة جلوس"),
                ("المساحة",       "92 م² · قبو بارتفاع 3,8 م"),
                ("الإطلالة",      "قبو خاصّ زجاجي · بلا إطلالة خارجية"),
                ("الحمّام",       "حجر travertino · دش walk-in بانورامي على القبو"),
                ("شامل",          "إفطار · سبا · 12 ملصقاً في القبو الخاصّ · تذوّق مُوجَّه"),
                ("الموسمية",      "عند الطلب · مثالي في الخريف"),
            ],
            "body": [
                ("p", "La Cantina مُعاد تشكيله في قبو النبيذ القديم للقرية · الطابق السفلي، قبو بارتفاع 3,8 أمتار · كان قبواً تشغيلياً حتى 2007، حين انتقل نبيذ Fattoria Trebbio إلى القبو الحديث على بعد 1,2 كم. يحتفظ الجناح بقبو خاصّ زجاجي، يُملأ كلّ موسم بـ 12 ملصقاً من البيت تختارها السوميلييه Anna."),
                ("p", "القبو الخاصّ مشمول في الإقامة · الزجاجات الـ 12 في تصرّف الضيوف للتذوّق غير المحدود طوال الإقامة. التذوّق المُوجَّه مع Anna مقرَّر ليلةً في الإقامة (مشمول في السعر) · تذوّقات إضافية عند الطلب."),
                ("h3", "الـ 12 ملصقاً للموسم"),
                ("p", "يتغيّر تركيب القبو كلّ موسم. اختيار 2026 (بإشراف Anna Ricci): 4 Brunello (Fattoria Trebbio 2018، Biondi-Santi 2016، Casanova di Neri 2017، Il Poggione 2018) · 3 Vino Nobile (Avignonesi 2019، Salcheto 2020، Boscarelli 2018) · 2 Chianti Classico (Castello di Ama 2019، Felsina 2018) · 3 أنبذة تجريبية من جنوب Toscana (Petricci 2020، Gualdo del Re 2021، Salvo 2019)."),
                ("ul", ["السعة · شخصان بالغان · بلا أطفال", "القبو · 12 ملصقاً · اختيار Anna Ricci AIS · يتغيّر كلّ موسم", "تذوّق مُوجَّه · ليلة في الإقامة (مشمول)", "الوايفاي · ألياف 1 جيغابت/ثانية · لا استقبال 4G", "المكيّف · مستقلّ، حرارة ثابتة 18 °م"]),
                ("p", "La Cantina متاح عند الطلب · مثالي في الموسم الخريفي بعد الحصاد. إقامة دنيا أربع ليالٍ."),
            ],
        },
    ],
}
