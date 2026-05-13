"""Podere Le Querce — Tuscan family agriturismo (artisan-workshop · AR MSA).

T60 · Wave 2 Pass-4 (2026-05-13) · close-out AR translation of the
podere-agriturismo template. Mirrors PODERE_CONTENT_IT shape exactly:
218 leaf paths, zero missing, zero extra, all iterator shapes
preserved (dicts vs tuples vs scalars per artisan-workshop shape
contract).

Voice contract (AR Modern Standard Arabic):
- Editorial-rural register in MSA · Asharq al-Awsat Travel · Madame
  Figaro Arabia (Voyages) · Al-Hayat Lifestyle (Travel) editorial.
  Familiar premium warmth, plural address (أنتم) across contact band.
- Voice anchor `ospitalità contadina` → `ضيافة المزرعة العائلية`
  (ḍiyāfat al-mazraʿah al-ʿāʾiliyyah · "family-farm hospitality").
  Verbatim across every band where IT uses "ospitalità contadina"
  · headline, famiglia statement_heading, soggiorno intro, soggiorno
  faq, site footer_intro · used ≥ 15 surfaces.
- Vocabolario AR: بوديري · ضيافة المزرعة · عائلة فلاحية · موسم العنب ·
  موسم الزيتون · بستان الزيتون · كرم العنب · بستان الخضراوات · إسطبل ·
  قبو · مطبخ · ضيافة · مائدة طويلة. لا: منتجع · كل شيء مشمول · سبا
  خمس نجوم · حجز إلكتروني فوري.
- Concrete detail kept verbatim: Greve in Chianti · Chianti Classico
  DOCG · Cinta Senese · موسم الزيتون نوفمبر · موسم العنب سبتمبر ·
  Antinori (الملاك التاريخيون · 1934 عقد البيع للأجداد Pasquinelli) ·
  Famiglia Pasquinelli (Maria مواليد 1962 المرأة الكبيرة · Carlo
  الزوج · Giovanni 35 الطباخ · Anna 32 البستان والضيافة) · 8 منتجات
  من البوديري تُباع في La Dispensa.

RTL chrome + Latin-name preservation contract (CRITICAL):
- Brand: Podere Le Querce · Agriturismo di Famiglia (Latin).
- Family + producers + places + wines + DOCG/DOP terms stay literal
  Latin via existing `unicode-bidi: isolate` chrome.
- Latin digits throughout · prices € 28 · years 1934 · phone
  +39 055 853 261 · NO Eastern Arabic-Indic numerals.
- Slug fields (URL identifiers) stay Latin: home · dispensa ·
  prodotto · famiglia · diario · soggiorno. Only `label` is Arabic.
- Form `name` fields (HTML input names) stay Latin: name · email ·
  phone · arrival · departure · guests · notes. Only `label` is AR.

Differentiation from Bottega-AR / Sapori-AR (D-054 enforcement):
- Bottega-AR: artisan-workshop typographic warmth · "صناعة يدوية".
- Sapori-AR: artisan-workshop terroir-curatorial · "كرّام مستقل".
- Podere-AR: artisan-workshop rural-hospitality · "ضيافة المزرعة
  العائلية" voice anchor · stay-and-take-home CTA (صندوق البوديري
  يصل إلى المنزل بعد الإقامة). Macro tone: عائلة تستضيف عائلة.

Contract compliance — factory/standards/artisan-workshop-shape-
contract.md (T58). All iterator shapes verified at write time ·
products list[8] dict[11] · provenance_steps list[4] 3-tuples ·
size_options list[4] scalars · process_steps list[4] dict[5] ·
faq_items list[5] dict[2] · stamp_rows / care_items / info_rows /
numbers_items tuples · press_items / card_hours_rows / stockists
scalars. Zero silent drift.
"""
from __future__ import annotations

from typing import Any


# Interim Unsplash CC0 imagery pool · travel-agriturismo signal.
# Same URLs as IT — pool re-declared verbatim per template contract.
_PODERE_HERO = "https://images.unsplash.com/photo-1602941525521-46f6f1ab39ce?w=1600&q=80&auto=format&fit=crop"
_OLIVETO = "https://images.unsplash.com/photo-1567416661576-d8b6e92e63d2?w=1200&q=80&auto=format&fit=crop"
_VIGNA_CHIANTI = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_TAVOLATA = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200&q=80&auto=format&fit=crop"
_CUCINA_CONTADINA = "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=1200&q=80&auto=format&fit=crop"
_FAMIGLIA_PORTRAIT = "https://images.unsplash.com/photo-1573497019418-b400bb3ab074?w=1200&q=80&auto=format&fit=crop"
_OLIO_BOTTLE = "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=1200&q=80&auto=format&fit=crop"
_VINO_BOTTLE = "https://images.unsplash.com/photo-1474722883778-792e7990302f?w=1200&q=80&auto=format&fit=crop"
_VINSANTO = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_MIELE = "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=1200&q=80&auto=format&fit=crop"
_MARMELLATA = "https://images.unsplash.com/photo-1535990379313-50d1f6fc0c4f?w=1200&q=80&auto=format&fit=crop"
_PECORINO = "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=1200&q=80&auto=format&fit=crop"
_SALAME = "https://images.unsplash.com/photo-1599379892470-bbe1eb01ea75?w=1200&q=80&auto=format&fit=crop"
_CANTUCCI = "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_MARIA = "https://images.unsplash.com/photo-1559963110-71b394e7494d?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CARLO = "https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_GIOVANNI = "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_ANNA = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_PRODUCER = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"


PODERE_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "البوديري",            "kind": "home"},
        {"slug": "dispensa",  "label": "La Dispensa",         "kind": "shop"},
        {"slug": "prodotto",  "label": "المنتج",              "kind": "product"},
        {"slug": "famiglia",  "label": "العائلة",             "kind": "about"},
        {"slug": "diario",    "label": "يوميات الريف",         "kind": "journal"},
        {"slug": "soggiorno", "label": "الإقامة",             "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":    "Q",
        "logo_word":       "Podere Le Querce",
        "tag":             "ضيافة المزرعة العائلية · Greve in Chianti · منذ 1934",
        "phone":           "+39 055 853 261",
        "whatsapp":        "+39 339 458 1126",
        "whatsapp_link":   "https://wa.me/393394581126",
        "email":           "famiglia@podereleQuerce.it",
        "address":         "Località Le Querce 14 · 50022 Greve in Chianti · Firenze",
        "hours_compact":   "مفتوح طوال السنة · المطبخ بحجز مسبق 12:30 و19:30",
        "hours_footer_rows": [
            "استقبال الضيوف 8-22 · Maria في المطبخ منذ السابعة صباحاً",
            "La Dispensa مفتوحة كل يوم 9-19 · الأحد مغلقة",
        ],
        "license":         "رمز CITRA 048-029-001 · سجل CCIAA Firenze 354210 · Az. Agricola Pasquinelli S.S.",
        "footer_intro":
            "Podere Le Querce هو بوديري عائلي للزراعة في Greve in Chianti · "
            "13 هكتاراً من الأرض تضم بستان زيتون تاريخياً، وكرم Sangiovese، "
            "وبستان خضراوات، وإسطبل Cinta Senese، وقبواً للنبيذ، وأربع "
            "غرف ضيافة ريفية. نصنع كل شيء في البيت: زيتاً ونبيذاً وعسلاً "
            "وسلامي ومعكرونة وكانتوتشي. عائلة Pasquinelli تعيش هنا منذ "
            "1934. حين تأتون ضيوفاً، تأكلون على مائدتنا. هذه ضيافة "
            "المزرعة العائلية كما عهدتموها.",

        # Nav CTA — agriturismo-flavoured
        "nav_cta":         "احجزوا إقامتكم",
        "nav_cta_kind":    "appointment",

        # Footer labels
        "foot_studio":     "البوديري",
        "foot_pages":      "الخارطة",
        "foot_contact":    "الإقامة",
        "foot_stockists":  "أين تجدوننا",
        "stockists_rows": [
            "Mercato della Terra · Greve in Chianti · صباح الأحد",
            "Slow Food Firenze · طاولة شهرية",
            "شحن إلى المنزل · إيطاليا 24-48 ساعة · أوروبا 4-6 أيام",
            "La Dispensa في البوديري · مفتوحة للجمهور كل يوم 9-19",
        ],

        # Currency + product labels (used on shop cards + product page)
        "currency_symbol":   "€",
        "shop_filter_label": "تصفية La Dispensa",
        "shop_count_unit":   "منتجات من البوديري",
        "edition_label":     "السنة",
        "made_in_label":     "صُنع في",
        "artisan_label":     "بيد",
        "material_label":    "المادة الأولية",
        "shipping_label":    "الشحن",
        "shipping_value":    "24-48 ساعة داخل إيطاليا · شحن مبرّد صيفاً",
        "guarantee_label":   "ضمان البوديري",
        "guarantee_value":   "نستبدل مجاناً كل قنينة مكسورة أو معيبة · خلال 30 يوماً",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "ضيافة المزرعة · Greve in Chianti · منذ 1934",
        "headline": "أربعة أجيال في مزرعة عائلية بالتوسكانا. <em>ضيافة المزرعة العائلية</em>، طوال السنة.",
        "intro":
            "Podere Le Querce هو بيت عائلة Pasquinelli منذ 1934، حين "
            "اشتراه الجدّان الكبيران Mario وAnnetta من عائلة Antinori "
            "بعقد بيع لا يزال محفوظاً في البلدية. اليوم هو ضيافة مزرعة "
            "بأربع غرف، ومطبخ عائلي مع مائدة طويلة بحجز مسبق، و"
            "La Dispensa الفلاحية بمنتجاتنا الثمانية. ضيافة المزرعة "
            "العائلية كما عرفها أبناء البوديري منذ أربعة أجيال.",

        "primary_cta":          "احجزوا إقامتكم",
        "primary_href":         "soggiorno",
        "secondary_cta":        "زوروا La Dispensa",
        "secondary_href":       "dispensa",

        # Stamp panel — list[4] of tuple[2]
        "stamp_label":   "البوديري في أربعة أسطر",
        "stamp_heading": "أربعة أجيال · مائدة واحدة طويلة.",
        "stamp_rows": [
            ("السنة",              "1934 · عقد البيع Antinori ← Pasquinelli"),
            ("العائلة",            "Maria + Carlo + Giovanni + Anna · 4 على القيادة"),
            ("الهكتارات",          "13 هكتاراً · زيتون + كرم + بستان + إسطبل"),
            ("الغرف",              "4 غرف · ضيافة ريفية مفتوحة طوال السنة"),
        ],
        "stamp_footer":      "Mercato della Terra Greve · Slow Food Firenze · شحن إلى المنزل في إيطاليا 24-48 ساعة",
        "stamp_corner_index": "الموسم",
        "stamp_corner_word":  "2026",

        # Latest items — list[4] of dict[8 keys=edition,id,image,meta,n,name,price,tag]
        "latest_label":       "في La Dispensa",
        "latest_heading":     "ثمانية منتجات من البوديري، دائماً متوفرة.",
        "latest_link_label":  "كل المنتجات",
        "latest_link_href":   "dispensa",
        "latest_items": [
            {
                "id":      "olio-evo-podere-2025",
                "n":       "N° 01",
                "image":   _OLIO_BOTTLE,
                "edition": "موسم 2025",
                "name":    "زيت الزيتون البكر الممتاز من البوديري",
                "meta":    "Moraiolo + Frantoio + Leccino · 2400 شجرة",
                "price":   "€ 28 / 500 مل",
                "tag":     "جديد · موسم نوفمبر",
            },
            {
                "id":      "chianti-classico-2022",
                "n":       "N° 02",
                "image":   _VINO_BOTTLE,
                "edition": "موسم العنب 2022",
                "name":    "Chianti Classico DOCG",
                "meta":    "Sangiovese 95% · 1,8 هكتار من الكرم",
                "price":   "€ 22 / قنينة",
                "tag":     "من قبو البوديري",
            },
            {
                "id":      "miele-millefiori",
                "n":       "N° 04",
                "image":   _MIELE,
                "edition": "استخراج يوليو 2025",
                "name":    "عسل أزهار متعددة",
                "meta":    "12 خلية · غابة الكستناء",
                "price":   "€ 14 / 250 غ",
                "tag":     "مئة بالمئة من البوديري",
            },
            {
                "id":      "salame-cinta-senese",
                "n":       "N° 07",
                "image":   _SALAME,
                "edition": "تعتيق 9 أشهر",
                "name":    "سلامي Cinta Senese",
                "meta":    "خنازير سوداء تربّى نصف طليقة",
                "price":   "€ 38 / قطعة كاملة",
                "tag":     "8 رؤوس في الإسطبل",
            },
        ],

        # Makers — list[4] of dict[6 keys=craft,name,place,portrait,quote,since]
        "makers_label":   "منتجو المنطقة",
        "makers_heading": "أربع أيدٍ تُكمل مائدتنا.",
        "makers_intro":
            "منتجات البوديري لا تكفي لمائدة كل الضيوف · منذ أربعة أجيال "
            "تعتمد عائلة Pasquinelli على المنتجين أنفسهم في المنطقة. "
            "كلّهم على بُعد أقل من ثلاثين كيلومتراً.",
        "makers": [
            {
                "craft":    "راعٍ · pecorino من الحليب الخام",
                "name":     "Andrea Falleri",
                "place":    "Lamole · 4 كم من البوديري",
                "since":    "زبون العائلة منذ 1987",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "آل Pasquinelli يأخذون مني pecorino Lamole منذ "
                    "أن كنت شاباً. جدّي كان يعطيه لوالدهم، وأنا الآن "
                    "أعطيه لـMaria. هكذا تتوارث الأشياء هنا.",
            },
            {
                "craft":    "طحّان · قمح صلب من Maremma",
                "name":     "Famiglia Bartoletti",
                "place":    "Roccastrada · 28 كم من البوديري",
                "since":    "مطحنة العائلة منذ 1820",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "نطحن قمح Senatore Cappelli الصلب على الحجر · "
                    "تصنع منه Maria معكرونة المائدة الطويلة يوم الأحد. "
                    "نكهة الدقيق العتيق هي نكهة معكرونتها.",
            },
            {
                "craft":    "نورتشينو · سلامي Cinta Senese",
                "name":     "Davide Pieri",
                "place":    "Castelfiorentino · 22 كم من البوديري",
                "since":    "حانوت سلامي عائلي منذ 1958",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "والد Maria علّمني تقطيع الخنزير على الأصول عام 1972. "
                    "الآن وقد صارت Maria تربّي Cinta Senese في البوديري، "
                    "أنا من يصنع لها السلامي.",
            },
            {
                "craft":    "دير · مربّى السفرجل",
                "name":     "Suore di San Vivaldo",
                "place":    "Montaione · 18 كم من البوديري",
                "since":    "دير عامل منذ القرن الخامس عشر",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "راهبات الدير يصنعن مربّى السفرجل كما كنّ "
                    "يصنعنه في القرن الخامس عشر · خمس ساعات طهو "
                    "على نار هادئة. Maria تضعه على المائدة مع pecorino.",
            },
        ],

        # Provenance items — list[4] of dict[4 keys=icon,title,desc,place]
        "provenance_label":   "البوديري",
        "provenance_heading": "ثلاثة عشر هكتاراً، أربعة محاصيل.",
        "provenance_intro":
            "البوديري يضم 13 هكتاراً تزرعها عائلة Pasquinelli مباشرة. "
            "أربعة محاصيل تاريخية · زيتون وكرم وبستان وإسطبل · لا تزال "
            "تُدار بالإيقاع الذي تعلّمته Maria من والدها.",
        "provenance_items": [
            {
                "icon":  "🌿",
                "title": "بستان الزيتون التاريخي",
                "desc":  "2400 شجرة Moraiolo وFrantoio وLeccino · بعض الأشجار يزيد عمرها على 200 سنة · قطاف باليد في نوفمبر · عصر بارد خلال 8 ساعات.",
                "place": "8 هكتارات على الجانب الجنوبي الشرقي للبوديري",
            },
            {
                "icon":  "🍇",
                "title": "كرم Sangiovese",
                "desc":  "1,8 هكتار من Sangiovese (95%) مع حصص صغيرة من Canaiolo وColorino · قطاف يدوي في أواخر سبتمبر · تخمير في قبو العائلة · تعبئة في القناني حتى مايو.",
                "place": "1,8 هكتار على الجانب الغربي · 380 م فوق سطح البحر",
            },
            {
                "icon":  "🥕",
                "title": "بستان المطبخ",
                "desc":  "1 هكتار من البستان الموسمي · طماطم San Marzano، فاصولياء zolfini، زعفران، أعشاب طبية · لا منتجات مشتراة لمائدة Maria باستثناء الليمون في الشتاء.",
                "place": "1 هكتار بجانب البيت الريفي",
            },
            {
                "icon":  "🐖",
                "title": "إسطبل Cinta Senese",
                "desc":  "8 رؤوس من Cinta Senese (الخنزير الأسود) تربّى نصف طليقة · تتغذى على بلوط غابة البوديري وعلى الحنطة من البستان · ذبح محلي مرتين في السنة.",
                "place": "2,2 هكتار من الغابة مع إسطبل مغطى",
            },
        ],

        # Care items — list[4] of tuple[2] · the four ospitalità promises
        "care_label":   "أربعة وعود من البيت",
        "care_heading": "ضيافة المزرعة العائلية: قواعد قليلة، تُحترم دائماً.",
        "care_items": [
            ("المائدة الطويلة دائماً مع Maria",
             "كلّ عشاء تُحضّره Maria وتضعه على المائدة بنفسها. حين "
             "تجلس معكم، يكون لأنها انتهت من الخدمة — لا لتسليتكم."),
            ("لا تسجيل دخول آلي",
             "Carlo أو Giovanni يستقبلكم عند البوابة ويرافقكم إلى "
             "الغرفة. المفتاح مفتاح حقيقي، من حديد، يحمل اسم الغرفة. "
             "لا بطاقات ممغنطة."),
            ("الفطور حتى الـ10:30",
             "خبز Lorenzini الساخن من فرن البوديري · مربّيات راهبات "
             "San Vivaldo · عسل الخلية · بيض الدجاج · قهوة من خلطة "
             "البوديري التاريخية."),
            ("شحن إلى المنزل بعد الإقامة",
             "عند المغادرة، تحضّر لكم La Dispensa صندوقاً من ستة "
             "منتجات من البوديري حسب اختياركم. نشحنه إلى المنزل خلال "
             "أسبوع · أجرة الشحن وحدها على حسابكم."),
        ],

        # Press strip — list[5] of scalar str (NOT dicts per contract)
        "press_label":   "صحافة البوديري",
        "press_items": [
            "Slow Food Firenze",
            "Bell'Italia · Toscana rurale",
            "Touring Club Italiano",
            "Gambero Rosso · Agriturismi 2025",
            "Vie del Gusto · Chianti Classico",
        ],

        # Journal teaser
        "journal_teaser_label":   "من يوميات الريف · ضيافة المزرعة",
        "journal_teaser_heading": "ثلاثة أصوات من Greve in Chianti.",
        "journal_teaser_link":    "اقرأوا اليوميات",
        "journal_teaser_href":    "diario",

        # Final CTA
        "cta_label":          "لحجز المائدة الطويلة · ضيافة المزرعة العائلية",
        "cta_heading":        "<em>أربع غرف</em>، مائدة واحدة، عائلة واحدة.",
        "cta_intro":
            "غرف البوديري الأربع تُحجز مباشرةً مع Maria عبر WhatsApp "
            "أو الهاتف. مائدة العشاء الطويلة تُحجز عند الوصول · نطبخ "
            "بحسب عددكم.",
        "cta_primary":        "راسلوا Maria عبر WhatsApp",
        "cta_primary_href":   "soggiorno",
        "cta_secondary":      "هاتف مباشر إلى المطبخ",
    },

    # ─── DISPENSA (shop · 8 farm products) ─────────────────────
    "dispensa": {
        "eyebrow":             "La Dispensa الفلاحية · ضيافة المزرعة العائلية",
        "headline":            "ثمانية منتجات من البوديري · شحن إلى المنزل في إيطاليا 24-48 ساعة.",
        "intro":
            "La Dispensa هي الامتداد الطبيعي لمطبخ Maria: المنتجات "
            "التي تأكلونها على المائدة حين تكونون ضيوفاً، تجدونها هنا "
            "لتأخذوها معكم إلى البيت. شحن مبرّد صيفاً، في صندوق خشبي "
            "يحمل ختم البوديري.",
        "filter_section_label": "تصفية La Dispensa",
        "filter_groups": [
            {
                "label":   "الإنتاج",
                "options": ["زيت زيتون بكر ممتاز", "نبيذ", "محفوظات", "سلامي", "معكرونة · خبز · حلويات"],
            },
            {
                "label":   "الموسم",
                "options": ["موسم 2025", "موسم العنب 2022-2024", "استخراج يوليو", "تعتيق طويل", "متوفر دائماً"],
            },
            {
                "label":   "صندوق خشبي",
                "options": ["صندوق من 6 منتجات · اختيار حر", "صندوق زيت + نبيذ", "صندوق الفطور (عسل + مربّى + كانتوتشي)", "صندوق السلامي"],
            },
        ],
        "sort_label":      "ترتيب",
        "sort_options": [
            "حسب الإنتاج",
            "حسب الموسم",
            "حسب التعتيق",
            "حسب التوفر",
        ],
        "result_count":    "8 منتجات من البوديري في La Dispensa",
        "result_subtitle": "ستة بختم البوديري + اثنان من منتجي المنطقة · شحن إلى المنزل في إيطاليا 24-48 ساعة.",
        "featured_product_id": "olio-evo-podere-2025",

        # 8 products — full dict shape (11 keys per contract)
        "products": [
            {
                "id":         "olio-evo-podere-2025",
                "n":          "N° 01",
                "image":      _OLIO_BOTTLE,
                "edition":    "موسم 2025",
                "name":       "زيت الزيتون البكر الممتاز من البوديري",
                "meta":       "Moraiolo 60% + Frantoio 25% + Leccino 15% · عصر بارد خلال 8 ساعات من القطاف",
                "place":      "Greve in Chianti",
                "artisan":    "Maria + Carlo Pasquinelli",
                "price":      "€ 28 / 500 مل",
                "tag":        "موسم نوفمبر",
                "available":  True,
            },
            {
                "id":         "chianti-classico-2022",
                "n":          "N° 02",
                "image":      _VINO_BOTTLE,
                "edition":    "موسم العنب 2022",
                "name":       "Chianti Classico DOCG",
                "meta":       "Sangiovese 95% · Canaiolo 4% · Colorino 1% · برميل كبير + 6 أشهر في القنينة",
                "place":      "كرم البوديري · 1,8 هكتار · 380 م فوق سطح البحر",
                "artisan":    "Giovanni Pasquinelli · عالم الخمور في البوديري",
                "price":      "€ 22 / 750 مل",
                "tag":        "من قبو البوديري",
                "available":  True,
            },
            {
                "id":         "vin-santo-2018",
                "n":          "N° 03",
                "image":      _VINSANTO,
                "edition":    "سنة 2018 · تعتيق 7 سنوات",
                "name":       "Vin Santo del Chianti",
                "meta":       "Malvasia bianca + Trebbiano · تجفيف 4 أشهر · براميل صغيرة من البلوط سعة 50 لتراً",
                "place":      "علّية البوديري · براميل تاريخية",
                "artisan":    "Carlo Pasquinelli · مسؤول القبو",
                "price":      "€ 32 / 375 مل",
                "tag":        "نصف قنينة",
                "available":  True,
            },
            {
                "id":         "miele-millefiori",
                "n":          "N° 04",
                "image":      _MIELE,
                "edition":    "استخراج يوليو 2025",
                "name":       "عسل أزهار متعددة",
                "meta":       "12 خلية على غابة الكستناء · جمع يوليو · لا معالجات كيميائية · لا تغذية شتوية",
                "place":      "غابة البوديري",
                "artisan":    "Anna Pasquinelli · النحّالة",
                "price":      "€ 14 / 250 غ",
                "tag":        "مئة بالمئة من البوديري",
                "available":  True,
            },
            {
                "id":         "marmellata-susine",
                "n":          "N° 05",
                "image":      _MARMELLATA,
                "edition":    "دفعة أغسطس 2025",
                "name":       "مربّى الخوخ الأصفر",
                "meta":       "خوخ claudia الأصفر · سكر 38% · لا بكتين مضاف · طهو على نار هادئة 4 ساعات",
                "place":      "بستان البوديري · 3 أشجار تاريخية",
                "artisan":    "Maria Pasquinelli · المطبخ",
                "price":      "€ 9 / 280 غ",
                "tag":        "دفعة صغيرة",
                "available":  True,
            },
            {
                "id":         "pecorino-toscano-dop",
                "n":          "N° 06",
                "image":      _PECORINO,
                "edition":    "تعتيق 6 أشهر",
                "name":       "Pecorino Toscano DOP",
                "meta":       "حليب نعاج خام · مَنفحة طبيعية · معتّق في كهف · مدهون بزيت زيتون البوديري",
                "place":      "Lamole · 4 كم من البوديري",
                "artisan":    "Andrea Falleri · الراعي",
                "price":      "€ 24 / قالب صغير 600 غ",
                "tag":        "بيد Andrea",
                "available":  True,
            },
            {
                "id":         "salame-cinta-senese",
                "n":          "N° 07",
                "image":      _SALAME,
                "edition":    "تعتيق 9 أشهر",
                "name":       "سلامي Cinta Senese",
                "meta":       "خنازير Cinta Senese من البوديري · تربية نصف طليقة · ذبح محلي · تعتيق في قبو حجري",
                "place":      "إسطبل البوديري + حانوت Pieri في Castelfiorentino",
                "artisan":    "Davide Pieri · النورتشينو",
                "price":      "€ 38 / قطعة كاملة 700 غ",
                "tag":        "8 رؤوس في الإسطبل",
                "available":  True,
            },
            {
                "id":         "cantucci-mandorle",
                "n":          "N° 08",
                "image":      _CANTUCCI,
                "edition":    "خبز أسبوعي",
                "name":       "كانتوتشي اللوز",
                "meta":       "لوز بقشره · بيض البوديري · سكر قصب · وصفة الجدة Annetta من 1948",
                "place":      "فرن البوديري · مطبخ Maria",
                "artisan":    "Maria Pasquinelli · المطبخ",
                "price":      "€ 12 / كيس 250 غ",
                "tag":        "وصفة الجدة Annetta",
                "available":  True,
            },
        ],

        "footer_note_label": "الشحن والصندوق",
        "footer_note":
            "كل المنتجات تُشحن في صندوق خشبي يحمل ختم البوديري · "
            "الطلبات فوق € 80 شحن مجاني داخل إيطاليا · وإلا € 12 "
            "ثابتة. الصندوق يعود إلينا حسب رغبتكم · أو يبقى عندكم "
            "كقطعة مطبخ.",
    },

    # ─── PRODOTTO (product page · featured = Olio EVO 2025) ───
    "prodotto": {
        "id":           "olio-evo-podere-2025",
        "n":            "N° 01",
        "edition":      "موسم نوفمبر 2025",
        "edition_note": "سنة 2025 محدودة بـ1800 قنينة · دفعة 23/01",
        "name":         "زيت الزيتون البكر الممتاز من البوديري",
        "subtitle":     "Moraiolo + Frantoio + Leccino · عصر بارد خلال 8 ساعات",
        "price":        "€ 28 / قنينة 500 مل",
        "vat_note":     "تشمل ضريبة القيمة المضافة · شحن 24-48 ساعة داخل إيطاليا",
        "intro":
            "زيت Podere Le Querce هو المنتج التاريخي للبيت · عائلة "
            "Pasquinelli كانت دائماً تبيع زيت الزيتون البكر الممتاز "
            "مباشرةً منذ الجدّين الكبيرين Mario وAnnetta. موسم 2025 "
            "قطف باليد عبر عشرة أشخاص (العائلة وأربعة موسميين) بين "
            "السادس والتاسع عشر من نوفمبر · عصر بارد خلال ثماني ساعات.",

        # Gallery — list of scalar URL strings
        "gallery": [
            _OLIO_BOTTLE,
            _OLIVETO,
            _CUCINA_CONTADINA,
        ],

        "info_label": "البطاقة الفنية",
        # info_rows — list[10] of tuple[2]
        "info_rows": [
            ("الأصناف",         "Moraiolo 60% · Frantoio 25% · Leccino 15%"),
            ("القطاف",          "يدوي · 6-19 نوفمبر 2025"),
            ("العصر",           "بارد · خلال 8 ساعات · 27 °م كحدّ أقصى"),
            ("الحموضة",         "0,18% · دون عتبة التفوق"),
            ("البوليفينولات",   "412 مغ/كغ · قيمة عالية"),
            ("القنينة",         "زجاج داكن 500 مل · غطاء معدني لولبي"),
            ("الدفعة",          "23/01 من أصل 36 · ملصق مرقّم باليد"),
            ("الحفظ",           "مكان بارد · بعيداً عن الضوء · خلال 18 شهراً"),
            ("الجوائز",         "Slow Food Presidio · Gambero Rosso ورقتان 2025"),
            ("التوفر",          "1800 قنينة · متوفرة حتى نفاد الكمية"),
        ],

        "size_label":      "الأحجام المتوفرة",
        "size_intro":      "قنينة منفردة 500 مل، صندوق من 6 قناني بخصم 12%، أو علبة معدنية 3 لترات لمن يطبخ كثيراً.",
        # size_options — list[4] of SCALAR strings (per contract · NOT tuples)
        "size_options": [
            "قنينة 500 مل",
            "صندوق من 6 قناني · 500 مل",
            "علبة معدنية 3 لترات",
            "كيس هدية · قنينتان + كانتوتشي",
        ],
        "size_chart_link":   "كل تشكيلات La Dispensa",
        "size_chart_href":   "dispensa",

        "artisan_label":     "بيد",
        "artisan_name":      "Maria + Carlo Pasquinelli",
        "artisan_role":      "الجيل الرابع · في البوديري منذ 1985",
        "artisan_bio":
            "Maria Pasquinelli (مواليد 1962) وCarlo Pasquinelli (مواليد "
            "1960) تسلّما إدارة البوديري عام 1985 بعد وفاة Mario، والد "
            "Maria. منذ ذلك الحين يعتنيان ببستان الزيتون معاً · Carlo "
            "يقود القطاف باليد، Maria تشرف على العصر في معصرة Chianti "
            "التعاونية. العائلة لم تستعمل المبيدات في بستان الزيتون "
            "قطّ.",
        "artisan_portrait":  _PORTRAIT_MARIA,

        "buy_primary":       "أضِف إلى الصندوق",
        "buy_secondary":     "راسلوا Maria عبر WhatsApp",
        "buy_note":
            "للطلبات التي تتجاوز 12 قنينة، اكتبوا مباشرةً للعائلة · "
            "نحضّر لكم صندوقاً خاصاً ونحسب لكم الخصم. الدفع عند "
            "الاستلام في إيطاليا، وبتحويل مصرفي لأوروبا.",

        "care_label":  "الحفظ والاستعمال",
        "care_intro":
            "زيت البوديري زيت يُستهلك نيّئاً · على الخبز الساخن، الفاصولياء، "
            "الـribollita، والـbruschetta. لا يُنصح به للقلي.",
        # care_items — list[5] of tuple[2]
        "care_items": [
            ("الحرارة",       "احفظوه بين 14-18 °م · لا في الثلاجة · لا في مطبخ ساخن"),
            ("الضوء",         "قنينة زجاج داكن · احموه مع ذلك من الضوء المباشر"),
            ("الاستهلاك",     "بعد فتحه · أنهوه خلال 4 أشهر · بعدها يخفّ النكهة"),
            ("الطعم",         "أخضر، مرّ وحارق في توازن · فاكهي متوسط الشدة"),
            ("المرافقة",      "فاصولياء zolfini · خبز بلا ملح · ribollita · bruschetta توسكانية"),
        ],

        "provenance_label":   "من بستان الزيتون إلى القنينة",
        "provenance_heading": "أربع خطوات باليد.",
        # provenance_steps — list[4] of 3-TUPLE (n, t, p) per contract
        "provenance_steps": [
            ("01", "قطاف يدوي",            "من السادس إلى التاسع عشر من نوفمبر 2025 · 10 أشخاص · 6 أسابيع من القطاف باليد · صناديق بلاستيكية مثقّبة"),
            ("02", "النقل إلى المعصرة",    "اليوم نفسه · خلال 8 ساعات · 12 كم إلى معصرة Chianti التعاونية"),
            ("03", "العصر البارد",         "27 °م كحدّ أقصى · استخلاص ميكانيكي · لا ماء مضاف · لا حرارة"),
            ("04", "التعبئة في القناني",   "مارس 2026 · في البوديري · قنينة زجاج داكن 500 مل · دفعة مرقّمة باليد"),
        ],

        "related_label": "منتجات أخرى من البوديري",
        "related_intro": "منتجات الموسم نفسه التي تُكمل الصندوق.",
        # related_items — list[4] of dict[5 keys=image,n,name,meta,price]
        "related_items": [
            {
                "id":    "chianti-classico-2022",
                "n":     "N° 02",
                "image": _VINO_BOTTLE,
                "name":  "Chianti Classico DOCG · 2022",
                "meta":  "نبيذ من السنة التاريخية نفسها · مثالي مع صندوق الزيت",
                "price": "€ 22",
            },
            {
                "id":    "miele-millefiori",
                "n":     "N° 04",
                "image": _MIELE,
                "name":  "عسل أزهار متعددة",
                "meta":  "12 خلية · غابة الكستناء · استخراج يوليو",
                "price": "€ 14",
            },
            {
                "id":    "marmellata-susine",
                "n":     "N° 05",
                "image": _MARMELLATA,
                "name":  "مربّى الخوخ الأصفر",
                "meta":  "خوخ claudia · دفعة أغسطس · طهو هادئ 4 ساعات",
                "price": "€ 9",
            },
            {
                "id":    "cantucci-mandorle",
                "n":     "N° 08",
                "image": _CANTUCCI,
                "name":  "كانتوتشي اللوز",
                "meta":  "وصفة الجدة Annetta · فرن أسبوعي في البوديري",
                "price": "€ 12",
            },
        ],
    },

    # ─── FAMIGLIA (about · La famiglia Pasquinelli) ───────────
    "famiglia": {
        "eyebrow":  "عائلة Pasquinelli · ضيافة المزرعة العائلية",
        "headline": "أربعة أجيال في Le Querce.",
        "intro":
            "بوديري Le Querce هو بيت عائلة Pasquinelli منذ نوفمبر "
            "1934. الجدّان الكبيران Mario وAnnetta اشترياه من عائلة "
            "Antinori بعقد بيع لا يزال محفوظاً في البلدية. منذ ذلك "
            "الحين تعاقبت أربعة أجيال على البوديري · اليوم على القيادة "
            "Maria وCarlo مع ابنيهما Giovanni وAnna.",

        "mission_label":   "رسالتنا",
        "mission_heading": "ضيافة المزرعة العائلية كما تتخيلونها.",
        "mission_text":
            "نطبخ لضيوفنا المطبخ نفسه الذي نطبخه لأنفسنا · لا قائمة "
            "طعام كالمطاعم، لا عربة جبن، لا متخصص نبيذ. هناك Maria "
            "تحمل إلى المائدة الـribollita التي طبختها هذا الصباح، "
            "وGiovanni يفتح النبيذ الذي عبّأه في الربيع، وAnna تقطع "
            "الخبز الذي خبزته عند الفجر.",

        "process_label":   "روزنامة العائلة",
        "process_heading": "أربعة فصول، أربعة أوقات للبوديري.",
        # process_steps — list[4] of DICT[5 keys=n,title,place,desc,duration]
        # CANONICAL shape (NOT Sapori's broken {num/title/desc})
        "process_steps": [
            {
                "n":        "01",
                "title":    "الربيع · التطعيم والإزهار",
                "place":    "بستان الزيتون + الكرم + البستان",
                "desc":
                    "مارس-مايو · تطعيم العنب، تقليم بستان الزيتون، "
                    "زرع البستان · الغرف الأربع تُعاد إلى الخدمة بعد "
                    "الإغلاق الفني في يناير. مائدة عيد الفصح الطويلة "
                    "مع خروف من Zeri.",
                "duration": "ثلاثة أشهر · مارس-مايو",
            },
            {
                "n":        "02",
                "title":    "الصيف · القطاف والضيافة الكاملة",
                "place":    "البوديري كلّه",
                "desc":
                    "يونيو-أغسطس · ذروة موسم الضيافة · مائدة طويلة "
                    "يومية تضم 12-16 ضيفاً · جمع العسل · حصاد القمح · "
                    "تحضير محفوظات الصيف (طماطم، خوخ، توت، تين).",
                "duration": "ثلاثة أشهر · يونيو-أغسطس",
            },
            {
                "n":        "03",
                "title":    "سبتمبر · موسم العنب",
                "place":    "الكرم + القبو",
                "desc":
                    "سبتمبر · قطاف Sangiovese يدوياً · ثمانية عشر "
                    "يوماً من العمل المتواصل في الكرم · القبو مغلق "
                    "أمام الجمهور خلال الأسبوعين اللذين يتم فيهما "
                    "التخمير · مائدة طويلة لإغلاق موسم العنب مع كل "
                    "العائلة والعمّال.",
                "duration": "شهر واحد · سبتمبر",
            },
            {
                "n":        "04",
                "title":    "الخريف-الشتاء · الزيت والخنزير",
                "place":    "بستان الزيتون + الإسطبل + المطبخ",
                "desc":
                    "نوفمبر · قطاف الزيتون (ستة أسابيع) · ديسمبر "
                    "ذبح Cinta Senese · يناير إنتاج السلامي مع "
                    "النورتشينو Pieri · فبراير إغلاق فني للبوديري · "
                    "مارس إعادة الفتح.",
                "duration": "خمسة أشهر · نوفمبر-مارس",
            },
        ],

        "founder_label":    "كبيرة العائلة",
        "founder_heading":  "Maria Pasquinelli · في البوديري منذ 1985.",
        "founder_text":
            "Maria Pasquinelli (مواليد 1962) هي الجيل الثالث للبوديري "
            "· ابنة Giovanni وMaddalena Pasquinelli، حفيدة الجدّين "
            "الكبيرين Mario وAnnetta اللذين اشتريا البوديري من "
            "Antinori. تسلّمت إدارة الضيعة عام 1985 بعد وفاة والدها · "
            "متزوجة من Carlo (من بوديري مجاور) منذ 1987 · وأمّ "
            "لـGiovanni (1990) وAnna (1993) اللذين يعملان في البوديري "
            "بدوام كامل منذ 2015. في المطبخ منذ السابعة صباحاً، حتى "
            "المائدة الطويلة مساءً مع الضيوف.",
        "founder_portrait":  _PORTRAIT_MARIA,
        "founder_caption":   "Maria Pasquinelli على مائدة الأحد الطويلة · صورة Paolo Codeluppi · صيف 2024",

        "numbers_label": "البوديري بالأرقام",
        # numbers_items — list[4] of tuple[2]
        "numbers_items": [
            ("92",  "سنة من حضور عائلة Pasquinelli في البوديري · منذ 1934"),
            ("13",  "هكتاراً تزرعها العائلة مباشرةً · زيتون + كرم + بستان + غابة"),
            ("4",   "غرف ضيافة · كل العائلة في المطبخ"),
            ("8",   "منتجات في La Dispensa · ستة بختم البوديري + اثنان من منتجي المنطقة"),
        ],

        "visit_label":          "لزيارة البوديري",
        "visit_heading":        "ضيافة المزرعة العائلية · مائدة طويلة بحجز مسبق أو زيارة برفقة مرشد.",
        "visit_text":
            "زيارات مرفقة للبوديري بحجز مسبق · ثلاثاء وخميس بعد الظهر "
            "(الساعة 16) للضيوف من خارج النزلاء. مائدة العشاء الطويلة "
            "(12-16 شخصاً) بحجز قبل 48 ساعة على الأقل. الغرف الأربع "
            "تُحجز مباشرةً مع Maria.",
        "visit_primary":         "احجزوا المائدة الطويلة",
        "visit_primary_href":    "soggiorno",
        "visit_secondary":       "WhatsApp مباشر إلى Maria",
    },

    # ─── DIARIO (journal · 3 entries) ─────────────────────────
    "diario": {
        "eyebrow":     "يوميات الريف",
        "headline":    "ثلاثة أصوات من Greve in Chianti.",
        "intro":
            "يوميات البوديري تجمع أصوات العائلة · Maria تكتب مرة في "
            "الشهر منذ يناير 2018 · Giovanni وAnna يضيفان ملاحظات "
            "الموسم. ملاحظات عمل · لا حكايات للسياح.",
        "list_label":  "ثلاث ملاحظات حديثة",
        # entries — list[3] of dict[5 keys=n,title,place,excerpt,minutes]
        "entries": [
            {
                "n":       "001",
                "title":   "موسم العنب 2025 · يوم المطر",
                "place":   "الكرم · 14 سبتمبر 2025",
                "excerpt":
                    "المطر وصل بعد ظهر اليوم العاشر · عملنا رغم "
                    "ذلك · ثلاثة صفوف فقط بقيت. Giovanni جلب الحوض "
                    "الكبير تحت العريشة · Maria فتحت المطبخ · في "
                    "العاشرة مساءً كنّا كلّنا في الداخل مع حساء "
                    "الكرنب الأسود.",
                "minutes": "4 دقائق قراءة",
            },
            {
                "n":       "002",
                "title":   "قطاف الزيتون 2025 · الأشجار الأقدم",
                "place":   "بستان الزيتون · 12 نوفمبر 2025",
                "excerpt":
                    "أشجار ما فوق المئتي سنة أعطت هذه السنة أقل "
                    "بكثير · حرّ أغسطس أرهقها. Carlo يقول إن الشجرة "
                    "رقم 47 (الأقدم، ما فوق 350 سنة وفق دفتر 1923) "
                    "أعطت 4 كغ فقط هذا العام مقابل 28 كغ السنة "
                    "الماضية. سنواصل العناية بها.",
                "minutes": "3 دقائق قراءة",
            },
            {
                "n":       "003",
                "title":   "Anna تبدأ تربية النحل · أول ثلاث خلايا",
                "place":   "غابة البوديري · 22 أبريل 2025",
                "excerpt":
                    "Anna جلبت إلى البيت أول ثلاث خلايا من دورة "
                    "تربية النحل في Vinci. وضعتها في غابة البوديري، "
                    "حيث ثمة فسحة من أشجار الكستناء. Maria تقول إن "
                    "والدها أبقى النحل حتى 1972 · ثم لم يعد أحد. "
                    "لنرَ هل تمضي الشتاء.",
                "minutes": "5 دقائق قراءة",
            },
        ],
        "footer_note_label": "لاستلام اليوميات",
        "footer_note":
            "اليوميات لا تصدر بنشرة آلية · إن أردتم استلامها اكتبوا "
            "إلى Maria. نرسل نسخة ورقية مطبوعة في نهاية السنة "
            "للضيوف الذين يطلبونها.",
    },

    # ─── SOGGIORNO (contact · prenota la tavolata) ────────────
    "soggiorno": {
        "eyebrow":  "الإقامة · حجز مباشر · ضيافة المزرعة العائلية",
        "headline": "أربع غرف، مائدة واحدة طويلة.",
        "intro":
            "غرف البوديري الأربع تُحجز مباشرةً مع عائلة Pasquinelli · "
            "لا منصة خارجية، لا عمولات وسيطة. هذه ضيافة المزرعة "
            "العائلية. اكتبوا إلى Maria · تجيب بنفسها خلال اليوم، "
            "غالباً بين فواصل المطبخ.",

        "form_section_label":   "طلب إقامة",
        "form_section_intro":
            "اذكروا التواريخ المرغوبة، وعدد الضيوف، وأي طلب خاص · "
            "حساسيات، عدم تحمّل، أطفال، حيوانات. Maria تجيب من "
            "المطبخ خلال 24 ساعة.",
        "form_helper_required": "الحقول التي تحمل · إلزامية",
        "form_submit_button":   "أرسلوا إلى Maria",
        "form_submit_note":
            "التأكيد النهائي عبر عربون 30% بتحويل مصرفي · باقي "
            "المبلغ عند الوصول إلى استقبال البوديري.",

        # form_fields — list[~7] of dict[5 keys=label,name,type,required,placeholder]
        "form_fields": [
            {
                "label":       "الاسم والكنية",
                "name":        "name",
                "type":        "text",
                "required":    True,
                "placeholder": "كيف تقدّمون أنفسكم · Maria ستناديكم باسمكم",
            },
            {
                "label":       "البريد الإلكتروني المباشر",
                "name":        "email",
                "type":        "email",
                "required":    True,
                "placeholder": "Maria تردّ من famiglia@podereleQuerce.it",
            },
            {
                "label":       "WhatsApp · أو الهاتف",
                "name":        "phone",
                "type":        "tel",
                "required":    False,
                "placeholder": "+39 339 458 1126 · Maria تردّ أيضاً عبر WhatsApp",
            },
            {
                "label":       "تاريخ الوصول",
                "name":        "arrival",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "تاريخ المغادرة",
                "name":        "departure",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "عدد الضيوف",
                "name":        "guests",
                "type":        "number",
                "required":    True,
                "placeholder": "كبار + أطفال",
            },
            {
                "label":       "حساسيات، عدم تحمّل، حيوانات",
                "name":        "notes",
                "type":        "textarea",
                "required":    False,
                "placeholder": "Maria تكيّف المطبخ · اذكروا ذلك هنا",
                "rows":        5,
            },
        ],

        # Contact card
        "card_label":            "للأجوبة السريعة",
        "card_address_label":    "أين نحن",
        "card_address_value":    "Località Le Querce 14 · 50022 Greve in Chianti · Firenze",
        "card_phone_label":      "المطبخ · Maria",
        "card_phone_value":      "+39 055 853 261",
        "card_whatsapp_label":   "WhatsApp المباشر",
        "card_whatsapp_value":   "+39 339 458 1126 · Maria",
        "card_email_label":      "البريد الإلكتروني",
        "card_email_value":      "famiglia@podereleQuerce.it",
        "card_hours_label":      "الأوقات",
        # card_hours_rows — list of SCALAR strings (per contract · NOT tuples)
        "card_hours_rows": [
            "المطبخ مفتوح طوال السنة · غداء 12:30 · عشاء 19:30",
            "استقبال الضيوف 8-22 · Maria في المطبخ منذ السابعة صباحاً",
            "La Dispensa 9-19 · الأحد مغلقة (سوق Greve)",
            "إغلاق فنّي · 1-28 فبراير",
        ],
        "card_directions_label": "كيف تصلون إلينا",
        "card_directions_text":
            "من Firenze 28 كم · مخرج طريق A1 السريع Firenze Sud · "
            "اتبعوا Chiantigiana · بعد 12 كم من Greve in Chianti "
            "انعطفوا يميناً نحو Lamole · 1,4 كم من المفترق. بوابة "
            "خشبية مكتوب عليها «Podere Le Querce» باليد · اقرعوا "
            "الجرس.",

        "faq_label": "أسئلة من المطبخ",
        # faq_items — list[5] of DICT[2 keys=q,a]
        # CANONICAL shape (NOT Sapori's broken 2-tuples)
        "faq_items": [
            {
                "q": "هل ندفع المائدة الطويلة حتى لو كنّا ضيوف الغرف؟",
                "a":
                    "نعم · المطبخ والضيافة شيئان مختلفان · الغرف "
                    "تُدفع للإقامة الليلية، والمائدة الطويلة تُدفع "
                    "على حدة · 35 € للشخص للعشاء، 28 € للغداء (نبيذ "
                    "البوديري مشمول). أما الفطور فمشمول في سعر الغرفة.",
            },
            {
                "q": "هل يُقبل الأطفال والحيوانات؟",
                "a":
                    "الأطفال أهلاً وسهلاً · لدينا أسرّة للصغار، وكراسٍ "
                    "مرتفعة للأكبر · Anna كثيراً ما تأخذهم إلى الإسطبل "
                    "لرؤية Cinta Senese. هذه ضيافة المزرعة العائلية. "
                    "الكلاب الصغيرة مسموح بها في الغرف الأرضية "
                    "(زيادة 15 € لليلة) · الكبيرة في الفناء والغابة، "
                    "لكن لا في الغرفة ولا في المطبخ.",
            },
            {
                "q": "هل يمكن زيارة البوديري دون مبيت؟",
                "a":
                    "نعم · ثلاثاء وخميس بعد الظهر (الساعة 16، مدتها 90 "
                    "دقيقة، بحجز قبل 24 ساعة على الأقل) Carlo يأخذ "
                    "الزوّار إلى بستان الزيتون والقبو · 20 € للشخص · "
                    "تذوّق زيت + نبيذ + عسل مشمول. ومن دون حجز تبقى "
                    "La Dispensa مفتوحة كل يوم 9-19.",
            },
            {
                "q": "هل يمكن حجز البوديري بأكمله للأعراس أو الفعاليات؟",
                "a":
                    "نعم، للأعراس الحميمة · بحدّ أقصى 36 ضيفاً · "
                    "مراسم مدنية في الحديقة تحت عريشة الويستيريا · "
                    "مائدة طويلة تحت الحظيرة المرمّمة · اكتبوا إلى "
                    "Maria قبل ثمانية أشهر من التاريخ على الأقل. لا "
                    "ننظّم أعراساً تتجاوز 36 ضيفاً ولا فعاليات شركاتية.",
            },
            {
                "q": "هل يمكن شراء المنتجات دون المجيء إلى البوديري؟",
                "a":
                    "نعم · La Dispensa تشحن إلى كل إيطاليا (24-48 "
                    "ساعة، شحن مجاني فوق € 80) وإلى أوروبا (4-6 "
                    "أيام). صندوق خشبي مختوم بختم البوديري · يعود "
                    "إلينا حسب رغبتكم · للطلبات فوق 12 قنينة اكتبوا "
                    "مباشرةً إلى Maria للحصول على خصم.",
            },
        ],
    },
}
