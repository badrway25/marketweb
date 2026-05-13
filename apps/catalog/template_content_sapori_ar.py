"""Sapori di Langa — Enoteca dei Vignaioli (artisan-workshop archetype) · AR.

Wave 1 Pass-10 close-out (T54 · 2026-05-12). AR translation tree for the
first reuse of the `artisan-workshop` skin after Bottega.

Voice contract (AR · Modern Standard Arabic, MSA):
- Asharq al-Awsat / Al-Hayat Lifestyle / Wine Society MSA editorial
  register · sommelier-pacato · terroir-curatorial.
- MSA throughout — no Egyptian/Levantine/Gulf colloquialisms. The
  register a Lebanese or Tunisian wine merchant would use in catalog
  copy: matter-of-fact, refined, no apologetics on the subject of wine.
- Voice anchor: «كَرَّام مستقل» (read: karrām mustaqill). Plural:
  «كَرَّامون مستقلّون» / accusative «كَرَّاماً مستقلاًّ». Used as the canonical
  thread across hero, atelier, makers, journal, contatti — ≥ 25 surfaces.
- Headline: `Vini di <em>vignaiolo indipendente</em> dalle Langhe del Barolo.`
  → `خمور <em>كَرَّام مستقل</em> من تلال لانغي باربولو.` (HTML <em> kept).

RTL chrome & Latin-name preservation (CRITICAL · precedent atto T48 /
madou T50 / petro T52):
- All Latin proper names + Latin digits stay LITERAL Latin script, wrapped
  by the existing CSS `unicode-bidi: isolate` chrome the artisan-workshop
  skin inherits. No transliteration.
- Brand «Sapori di Langa · Enoteca dei Vignaioli» kept Latin (glossed
  once as «حانوت الكَرَّامين في ألبا»).
- Persona names Latin: Pietro Brero, Federica Brero.
- Producers + cantine Latin: Carlo Brezza, Maria Vajra, Luigi Boasso,
  Anna Brovia · Brezza & Figli, Vajra, Boasso, Brovia.
- Places Latin: Alba, Langhe, Roero, Monferrato, Barolo, Cannubi,
  Bricco delle Viole, Gabutti, Villero, Bricco Sarmassa, Cannubi
  Muscatel, Domaine Romanée-Conti.
- Wine names Latin: Barolo, Barbera, Dolcetto, Nebbiolo, Verduno
  Pelaverga, Barbaresco, Rabajà.
- PDO/DOC names stay literal IT: Olio EVO, Castelmagno DOP, Nocciola
  Tonda Gentile, Tartufo Bianco.
- Press Latin: Slow Wine, Gambero Rosso Vini, Vitae AIS, I Vini di
  Veronelli, Doctor Wine.
- Latin digits (0-9) throughout — prices «€ 58», years «2019», phone
  «+39 0173 364 990». NOT Eastern Arabic-Indic digits.
- `slug` fields stay Latin (URL identifiers · home, shop, product,
  atelier, journal, contatti). Form input `name` fields stay Latin.

Shape parity contract: exactly 179 leaf paths, mirroring IT 1:1.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from X.3 curator pack `wine-food-boutique.md`. All
# Pexels CC0 · commercial-safe.  Re-declared verbatim from IT.
_VIGNAIOLO_PORTRAIT_PIETRO = (
    "https://images.pexels.com/photos/8472892/pexels-photo-8472892.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_CARLO = (
    "https://images.pexels.com/photos/8472933/pexels-photo-8472933.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_MARIA = (
    "https://images.pexels.com/photos/8472896/pexels-photo-8472896.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_LUIGI = (
    "https://images.pexels.com/photos/5946081/pexels-photo-5946081.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_FOUNDER_PORTRAIT = (
    "https://images.pexels.com/photos/8472944/pexels-photo-8472944.jpeg"
    "?auto=compress&cs=tinysrgb&w=800&h=1000&fit=crop"
)
_BOTTLE_BAROLO = (
    "https://images.pexels.com/photos/1407847/pexels-photo-1407847.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_BARBERA = (
    "https://images.pexels.com/photos/1123260/pexels-photo-1123260.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_OLIO = (
    "https://images.pexels.com/photos/33783/olive-oil-salad-dressing-cooking-olive.jpg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_FORMAGGIO = (
    "https://images.pexels.com/photos/821365/pexels-photo-821365.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)


SAPORI_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "الحانوت",        "kind": "home"},
        {"slug": "shop",     "label": "الكتالوج",       "kind": "shop"},
        {"slug": "product",  "label": "القنينة",        "kind": "product"},
        {"slug": "atelier",  "label": "الكَرَّامون",       "kind": "about"},
        {"slug": "journal",  "label": "الدفتر",         "kind": "journal"},
        {"slug": "contatti", "label": "زيارة وطلبات",   "kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Sapori di Langa",
        "tag":          "حانوت الكَرَّامين · Alba · منذ 1992",
        "phone":        "+39 0173 364 990",
        "whatsapp":     "0173 364 990",
        "whatsapp_link": "https://wa.me/390173364990",
        "email":        "enoteca@saporidilanga.it",
        "address":      "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "hours_compact": "الثلاثاء – السبت · 9:30 – 19:30 · الأحد 10 – 13",
        "hours_footer_rows": [
            "الأحد · 10:00 – 13:00 (صباحاً فقط)",
            "الإثنين · مغلق",
            "موسم Fiera del Tartufo · دوام متواصل تشرين الأول – تشرين الثاني",
        ],
        "license":      "P.IVA 02814730042 · CCIAA Cuneo REA 263118",
        "footer_intro":
            "حانوت خمور في Alba، أسّسه Pietro Brero عام 1992. اثنان وثلاثون "
            "كَرَّاماً مستقلاًّ من تلال Langhe وRoero وMonferrato، لكلٍّ منهم رقم "
            "إصداره الخاص، وتوقيعه بخط اليد في ذيل كل قنينة، وقطعته الكَرْمية "
            "المعتّقة في نقاء تام. شحن مبرَّد خلال 48 ساعة في كافة أنحاء إيطاليا.",
        "nav_cta":      "اطلب صندوق الكَرَّام",
        "nav_cta_kind": "case-order",

        "foot_studio":   "الحانوت",
        "foot_pages":    "خريطة الموقع",
        "foot_contact":  "الطلبات والزيارات",
        "foot_stockists":"مطاعم تختار كَرَّامينا المستقلّين",
        "stockists_rows": [
            "Piazza Duomo · Alba · ثلاث نجوم Michelin",
            "La Ciau del Tornavento · Treiso",
            "Locanda del Pilone · Madonna di Como",
            "Antica Corona Reale · Cervere",
        ],

        "currency_symbol":  "€",
        "shop_filter_label": "التصفية",
        "shop_count_unit":   "قنينة",
        "edition_label":     "الإصدار",
        "made_in_label":     "تخمّر في",
        "artisan_label":     "كَرَّام مستقل",
        "material_label":    "العنب",
        "shipping_label":    "الشحن",
        "shipping_value":    "مبرَّد خلال 48 ساعة · ستّ قناني للصندوق",
        "guarantee_label":   "الضمان",
        "guarantee_value":   "استبدال مجاني لأي قنينة معيبة",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "موسم 2023 · اثنان وثلاثون كَرَّاماً مستقلاًّ في الحانوت",
        "headline": "خمور <em>كَرَّام مستقل</em> من تلال Langhe del Barolo.",
        "intro":
            "نزور الكُروم مرّتين كل عام: مرّةً في القطاف ومرّةً لتذوّق المواسم "
            "في البراميل. من كل قبو نعرف الكَرَّام المستقل باسمه، والقطعة الكَرْمية "
            "المعتّقة، ورقم الإصدار في القنينة. لا تصل إلينا خمرة واحدة من "
            "كتالوج جملة · كل قنينة بتوقيع كَرَّام مستقل.",
        "primary_cta":   "اطلب صندوق الكَرَّام",
        "primary_href":  "shop",
        "secondary_cta": "زُر الحانوت",
        "secondary_href":"contatti",

        # Stamp-aside data
        "stamp_label":  "قاعدتنا",
        "stamp_heading":"رحلتان، <em>قنينة واحدة.</em>",
        "stamp_rows": [
            ("كَرَّامون مستقلّون",   "32 قبواً"),
            ("التسميات",     "180 في الكَرْت"),
            ("القطاف",       "يدوي دائماً"),
            ("الصندوق",      "6 قناني"),
        ],
        "stamp_footer": "إصدار مرقَّم · شحن مبرَّد",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "الحانوت",

        # Latest-arrived band — 4 bottles
        "latest_label":   "أحدث الدفعات في الكَرْت",
        "latest_heading": "آخر المواسم <em>من Langhe.</em>",
        "latest_link_label": "الكتالوج بكامله",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "موسم 2019",
                "edition":  "إصدار 23 / 280",
                "name":     "Barolo Cannubi",
                "meta":     "Nebbiolo 100% · Barolo · La Morra",
                "price":    "€ 58",
                "tag":      "موسم",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "موسم 2021",
                "edition":  "إصدار 87 / 1.200",
                "name":     "Barbera d'Alba Superiore",
                "meta":     "Barbera 100% · Roero",
                "price":    "€ 22",
                "tag":      "يومية",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "حصاد 2024",
                "edition":  "إصدار 12 / 380",
                "name":     "Olio EVO Langhe DOP",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "€ 28",
                "tag":      "موسمي",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "تعتيق 18 شهراً",
                "edition":  "قالب 04 / 22",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "حليب بقري · Castelmagno CN",
                "price":    "€ 36",
                "tag":      "موسم",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        # Vignaioli band — 4 named vintners
        "makers_label":   "أيادٍ تصنع الخمرة",
        "makers_heading": "اثنان وثلاثون كَرَّاماً مستقلاًّ، <em>كَرْتٌ واحد.</em>",
        "makers_intro":
            "لا نتعامل إلاّ مع كَرَّامين مستقلّين — أي كَرَّام مستقل يخمّر عنبه على قطعته "
            "بنفسه ويوقّع بيده كل إصدار يدخل الكَرْت. كل قبو يزوره Pietro "
            "ثلاث مرّات على الأقل قبل أن يدخل الكتالوج.",
        "makers": [
            {
                "name":   "Carlo Brezza",
                "craft":  "كَرَّام مستقل · Cannubi التاريخية",
                "place":  "Barolo (CN)",
                "since":  "كَرْم منذ 1885 · عائلة Brezza منذ 1885",
                "quote":  "«لا يُصنع الـ Barolo بالعَجَل. يُصنع بالصمت: "
                          "عامان في البرميل الكبير، والأذن منتصبة لسماع "
                          "هل البرميل يغنّي أم ينوح.»",
                "portrait": _VIGNAIOLO_PORTRAIT_CARLO,
            },
            {
                "name":   "Maria Vajra",
                "craft":  "كَرَّامة مستقلّة · Bricco delle Viole",
                "place":  "Vergne · Barolo (CN)",
                "since":  "قبو عائلي منذ 1972",
                "quote":  "«لا نخمّر إلاّ ما نراه ينمو بأعيننا. إن لم تعطِ "
                          "قطعةٌ ما يجب، فلا نعبّئ موسمها. كَرْت الكَرَّامين "
                          "يُكتب أيضاً بما لا نضعه فيه.»",
                "portrait": _VIGNAIOLO_PORTRAIT_MARIA,
            },
            {
                "name":   "Luigi Boasso",
                "craft":  "كَرَّام مستقل · Gabutti Roccaforte",
                "place":  "Serralunga d'Alba (CN)",
                "since":  "أربعة أجيال في الكَرْم",
                "quote":  "«الـ Nebbiolo عنبٌ مخاتل. يصير ما تحكيه له "
                          "التربة. لذلك لا أعمل قطعاً أُخَر: تعلُّم تربةٍ "
                          "واحدةٍ يتطلّب ثلاثين عاماً.»",
                "portrait": _VIGNAIOLO_PORTRAIT_LUIGI,
            },
            {
                "name":   "Anna Brovia",
                "craft":  "كَرَّامة مستقلّة · Villero & Rocche dei Brovia",
                "place":  "Castiglione Falletto (CN)",
                "since":  "قبو Brovia منذ 1863",
                "quote":  "«لا نُسابق ولا نُجمّع نقاطاً. نصنع Barolo كما "
                          "صُنع دائماً في Castiglione Falletto: طويلاً، "
                          "صارماً، بلا زخارف. من ينشد السهل، فليبحث في "
                          "مكان آخر.»",
                "portrait": _VIGNAIOLO_PORTRAIT_PIETRO,
            },
        ],

        # Provenance — terroir + filiera
        "provenance_label":   "من أين تأتي",
        "provenance_heading": "خمسة وستّون كيلومتراً، <em>ثلاث تسميات.</em>",
        "provenance_intro":
            "كل تسميات الكَرْت تأتي من دائرة نصف قطرها خمسة وستّون كيلومتراً "
            "حول Alba. ثلاث تسميات أساسية — Langhe وRoero وMonferrato — "
            "وشبكةٌ من كَرَّامين مستقلّين اختار كل كَرَّام مستقل منهم رفيقَه بنفسه.",
        "provenance_items": [
            {
                "icon": "vine",
                "title": "Langhe DOCG",
                "desc":  "Barolo وBarbaresco وDolcetto · أحد عشر بلدةً "
                         "للإنتاج · ترابٌ كلسي مارني · ارتفاعٌ بين "
                         "200 و400 م فوق سطح البحر.",
                "place": "Alba · La Morra · Barolo · Castiglione",
            },
            {
                "icon": "hills",
                "title": "Roero DOCG",
                "desc":  "Nebbiolo Roero وArneis وFavorita · ما وراء نهر "
                         "Tanaro · ترابٌ رملي · خمور أرشق وأعطر · ارتفاعٌ "
                         "بين 280 و380 م فوق سطح البحر.",
                "place": "Canale · Vezza · Santo Stefano Roero",
            },
            {
                "icon": "cheese",
                "title": "Monferrato Casalese",
                "desc":  "Barbera Superiore وGrignolino وRuchè · سفوحٌ "
                         "تلّية · ترابٌ كلسي طيني · خمور يومية ذات طابع.",
                "place": "Casale · Vignale · Rosignano",
            },
            {
                "icon": "olive",
                "title": "ساحل ليغوريا (50 كم)",
                "desc":  "Olio EVO Taggiasco DOP · ملح Trapani بالفحم "
                         "النباتي · مَكْرَلة بالزيت من La Spezia. موَرِّدون "
                         "تاريخيون للحانوت.",
                "place": "Imperia · La Spezia · Trapani",
            },
        ],

        # Care — wine handling guarantees
        "care_label":   "كيف تصل، كيف تُحفَظ",
        "care_heading": "أربعة وعود في الصندوق.",
        "care_items": [
            ("شحن مبرَّد",
             "صندوق من ستّ قناني يُشحن في علبة عازلة مع "
             "gel pack بحرارة 14°C. تسليم خلال 48 ساعة في "
             "كل إيطاليا · 4 أيام في أوروبا الغربية."),
            ("إصدار مرقَّم في الذيل",
             "كل قنينة تحمل بخط اليد رقم الإصدار وموسم الخمرة "
             "وتوقيع الكَرَّام المستقل. لا ملصقات طباعية صناعية."),
            ("استبدال القنينة المعيبة",
             "TCA، تأكسد، كسر في الترانزيت · نستبدلها مجاناً خلال "
             "ثلاثة أشهر من التسليم · يكفي إثباتٌ مصوَّر للسدّادة "
             "أو لمستوى السائل."),
            ("نصائح خبير النبيذ",
             "يتّصل بك Pietro أو Federica خلال 24 ساعة إن لزمك "
             "اقتراحٌ لعشاءٍ ما، أو تذوّقٌ رأسي لعيد ميلاد، أو "
             "صندوقٌ لإهداء مؤسسي."),
        ],

        # Press band — Italian wine press
        "press_label": "كُتب عنّا في",
        "press_items": ["Slow Wine", "Gambero Rosso Vini", "Vitae AIS",
                        "I Vini di Veronelli", "Doctor Wine"],

        # Journal teaser
        "journal_teaser_label":   "ملاحظات من الدفتر",
        "journal_teaser_heading": "كيف بنينا كَرْت <em>كَرَّام مستقل بعد آخر · خريف 2026.</em>",
        "journal_teaser_link":    "اقرأ الدفتر",
        "journal_teaser_href":    "journal",

        # CTA section
        "cta_label":     "اطلب · زُر · راسلنا",
        "cta_heading":   "صندوقٌ من ستّ قناني، <em>اختاره Pietro.</em>",
        "cta_intro":
            "تتبدّل الصناديق المختارة كل شهر بحسب قبور الكَرَّامين المستقلّين "
            "القادمة. خمورٌ ليومياتك، أو خمور للتعتيق، أو تشكيلات مختلطة "
            "مع زيت زيتون وأجبان. الدفع عند الاستلام، والشحن مبرَّد خلال "
            "48 ساعة، وتوقيع كَرَّام مستقل على كل قنينة.",
        "cta_primary":      "اطلب صندوق الشهر",
        "cta_primary_href": "shop",
        "cta_secondary":    "تعالَ إلى الحانوت",
    },

    # ─── SHOP (catalog) ─────────────────────────────────────────
    "shop": {
        "eyebrow":  "كَرْت الحانوت · موسم 2023-2024",
        "headline": "مئةٌ وثمانون تسمية، <em>توقيعٌ واحد.</em>",
        "intro":
            "كَرْت الخمور وزيوت الزيتون والأجبان والمصبَّرات. كل تسمياتنا "
            "تأتي من كَرَّامين مستقلّين زرناهم شخصياً. عند كل خمرة نُشير "
            "إلى الموسم ورقم الإصدار وسنة العنب واسم الكَرَّام المستقل الموقِّع.",

        "filter_section_label": "التصفية",
        "filter_groups": [
            {
                "label": "التسمية",
                "options": ["Barolo DOCG", "Barbaresco DOCG", "Roero DOCG",
                            "Langhe DOC", "Monferrato DOC", "Asti DOCG",
                            "Vino da Tavola"],
            },
            {
                "label": "العنب",
                "options": ["Nebbiolo", "Barbera", "Dolcetto", "Arneis",
                            "Favorita", "Grignolino"],
            },
            {
                "label": "النوع",
                "options": ["خمور حمراء", "خمور بيضاء", "خمور حلوة",
                            "خمور فوّارة", "زيوت وتوابل", "أجبان",
                            "مصبَّرات ومقدَّدات"],
            },
        ],

        "sort_label": "الترتيب حسب",
        "sort_options": ["الأحدث", "كَرَّام مستقل", "الموسم", "السعر"],

        "result_count": "180 قنينة",
        "result_subtitle": "آخر تحديث الثلاثاء 8 تشرين الأول 2026",

        # Sample products — 8 cards
        "products": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "01",
                "edition":  "موسم 2019 · إصدار 23",
                "name":     "Barolo Cannubi · Brezza",
                "meta":     "Nebbiolo · Barolo · La Morra",
                "price":    "€ 58",
                "tag":      "موسم",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbaresco-rabaja-2018",
                "n":        "02",
                "edition":  "موسم 2018 · إصدار 11",
                "name":     "Barbaresco Rabajà · Cortese",
                "meta":     "Nebbiolo · Barbaresco · Treiso",
                "price":    "€ 64",
                "tag":      "تذوّق رأسي",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "03",
                "edition":  "موسم 2021 · إصدار 87",
                "name":     "Barbera d'Alba Superiore · Vajra",
                "meta":     "Barbera · Roero · Canale",
                "price":    "€ 22",
                "tag":      "يومية",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "dolcetto-diano-2022",
                "n":        "04",
                "edition":  "موسم 2022 · إصدار 42",
                "name":     "Dolcetto di Diano d'Alba · Boasso",
                "meta":     "Dolcetto · Diano d'Alba",
                "price":    "€ 16",
                "tag":      "مائدة",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "arneis-roero-2023",
                "n":        "05",
                "edition":  "موسم 2023 · إصدار 56",
                "name":     "Roero Arneis · Brovia",
                "meta":     "Arneis · Vezza d'Alba",
                "price":    "€ 18",
                "tag":      "أبيض",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "06",
                "edition":  "حصاد 2024 · إصدار 12",
                "name":     "Olio EVO Langhe DOP · Frantoio Anfossi",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "€ 28",
                "tag":      "موسمي",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "07",
                "edition":  "تعتيق 18 شهراً · قالب 04",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "حليب بقرة piemontese",
                "price":    "€ 36",
                "tag":      "جبن",
                "image":    _BOTTLE_FORMAGGIO,
            },
            {
                "id":       "salame-cuneo",
                "n":        "08",
                "edition":  "تعتيق 4 أشهر · إصدار 08",
                "name":     "Salame Cuneo · Macelleria Cesare",
                "meta":     "خنزير Cuneo · فلفل أسود · خمرة في العجين",
                "price":    "€ 24",
                "tag":      "مقدَّدات",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        "featured_product_id": "barolo-cannubi-2019",

        "footer_note_label": "الشحن والاستلام",
        "footer_note":
            "شحن مبرَّد خلال 48 ساعة في إيطاليا · الحدّ الأدنى ستّ قناني في "
            "الصندوق · رسم الشحن € 12 (مجاناً فوق € 200). استلامٌ من "
            "الحانوت بلا حجز مسبق. للطلبات فوق اثنتي عشرة قنينة، التواصل "
            "مباشرةً معنا.",
    },

    # ─── PRODUCT ────────────────────────────────────────────────
    "product": {
        "id":       "barolo-cannubi-2019",
        "n":        "01",
        "edition":  "موسم 2019",
        "edition_note": "إصدار 23 / 280 · عُبِّئ في كانون الأول 2022",
        "name":     "Barolo Cannubi · Brezza",
        "subtitle": "Nebbiolo 100% · مخمَّر على تلّة Cannubi التاريخية",
        "price":    "€ 58",
        "vat_note": "متضمّن الضريبة · الحدّ الأدنى ستّ قناني في الصندوق",
        "intro":
            "Barolo من قبو Brezza، قطعة Cannubi التاريخية (أقدم تلال بلدة "
            "Barolo، وثائق القطاف موثَّقة منذ 1752). قطاف يدوي، تخمّر "
            "في خزانات فولاذية، تعتيق في برميل كبير من خشب بلوط Slavonia "
            "لثلاثين شهراً، ثم اثنا عشر شهراً أخرى في القنينة قبل الإصدار.",

        "gallery": [
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
        ],

        "info_label": "البطاقة الفنية",
        "info_rows": [
            ("كَرَّام مستقل",    "Carlo Brezza · Brezza & Figli"),
            ("التسمية",         "Barolo DOCG"),
            ("العنب",           "Nebbiolo 100%"),
            ("البلدة",          "Barolo (CN)"),
            ("القطعة",          "Cannubi التاريخية"),
            ("الارتفاع",        "260 م فوق سطح البحر · مَيْلٌ نحو الجنوب الشرقي"),
            ("القطاف",          "يدوي · الأسبوع الثاني من تشرين الأول 2019"),
            ("التعتيق",         "30 شهراً برميل كبير + 12 قنينة"),
            ("الكحول",          "14,5% vol"),
            ("الكبريتيات",      "< 80 mg/l · كَرْمٌ بيولوجي معتمَد"),
        ],

        "size_label": "الأحجام المتاحة",
        "size_intro": "متاح في قنينة مفردة وMagnum وصندوق أفقي 2019 وصندوق تذوّق رأسي 2015 – 2019.",
        "size_options": ["750 ml", "1,5 L Magnum", "صندوق 6 · 2019", "صندوق 6 · رأسي"],
        "size_chart_link": "كل الأحجام والتذوّقات الرأسية",
        "size_chart_href": "shop",

        "artisan_label":   "كَرَّام مستقل",
        "artisan_name":    "Carlo Brezza",
        "artisan_role":    "الجيل الرابع · Brezza & Figli منذ 1885",
        "artisan_bio":
            "قبو عائلي أسّسه جدّ Carlo الكبير عام 1885، ثم تتابع توارثُه "
            "في خطٍّ مباشر من أبٍ إلى ابن. دخل Carlo إلى الكَرْم عام 1997 "
            "بعد دراسته للخمَّاريات في Alba، وثلاثة مواسم قطاف في "
            "Domaine Romanée-Conti. لا يخمّر إلاّ القطع المملوكة للعائلة "
            "(Cannubi التاريخية، Bricco Sarmassa، Cannubi Muscatel) — "
            "لا عنب يُشترى من الخارج.",
        "artisan_portrait": _VIGNAIOLO_PORTRAIT_CARLO,

        "buy_primary":   "أضِف إلى الصندوق",
        "buy_secondary": "احجز في الحانوت",
        "buy_note":
            "الطلبات فوق 12 قنينة · يُرجى التواصل مع القبو مباشرةً. "
            "يُتحقَّق من التوفّر لحظة الطلب.",

        "care_label": "الحفظ",
        "care_intro":
            "Barolo قابل للتعتيق · يحتاج حفظاً متيقّظاً ليبلغ كامل طاقاته.",
        "care_items": [
            ("الحرارة",     "12-14°C ثابتة · بلا تذبذب"),
            ("الوضعية",     "أفقياً · السدّادة دائماً ملامِسةً للخمرة"),
            ("الرطوبة",     "70% على الأقل · جوٌّ معتم"),
            ("الفتح",       "يُفتح قبل 2-3 ساعات · يُنصح بالـ decantazione"),
            ("ذروة النضج", "جاهز للشرب 2025-2040 · ذروة الكمال 2028-2035"),
        ],

        "provenance_label":   "من Cannubi إلى الكأس",
        "provenance_heading": "أربع محطّات موثَّقة.",
        "provenance_steps": [
            ("01", "القطاف",     "قطاف يدوي في صناديق 18 كغ · Cannubi على 260 م فوق سطح البحر · الأسبوع الثاني من تشرين الأول 2019"),
            ("02", "التعتيق",    "برميل كبير من خشب بلوط Slavonia · 30 شهراً · لا براميل برّيك · قبو Brezza في Barolo"),
            ("03", "التعبئة",    "كانون الأول 2022 · بلا فلترة · بلا تصفية · إصدار 23 من 280"),
            ("04", "الشحن",      "صندوق خشبي مختوم · علبة عازلة مع gel pack بحرارة 14°C · 48 ساعة في إيطاليا"),
        ],

        "related_label":   "تذوّقات رأسية ومرافقات",
        "related_intro":
            "إصدارات من القبو نفسه لمواسم سابقة، وخمور أخرى يُوصي بها "
            "Pietro مرافقةً للمقارنة.",
        "related_items": [
            {"id":"barolo-cannubi-2018",   "n":"رقم 088","name":"Barolo Cannubi · 2018",   "meta":"موسم بارد · Brezza",            "price":"€ 62","image":_BOTTLE_BAROLO},
            {"id":"barolo-cannubi-2017",   "n":"رقم 074","name":"Barolo Cannubi · 2017",   "meta":"موسم حارّ · Brezza",            "price":"€ 68","image":_BOTTLE_BAROLO},
            {"id":"barbaresco-rabaja-2018","n":"رقم 142","name":"Barbaresco Rabajà · 2018","meta":"مقارنة ترّوارية",                "price":"€ 64","image":_BOTTLE_BAROLO},
            {"id":"barbera-vajra",         "n":"رقم 211","name":"Barbera Superiore · 2021","meta":"يومية على المائدة · Vajra",      "price":"€ 22","image":_BOTTLE_BARBERA},
        ],
    },

    # ─── ATELIER (about · "كَرَّامون مستقلّون") ────────────────
    "atelier": {
        "eyebrow":  "الحانوت",
        "headline": "Sapori di Langa: <em>اثنان وثلاثون كَرَّاماً مستقلاًّ، يافطةٌ واحدة.</em>",
        "intro":
            "Sapori di Langa حانوتُ خمورٍ مستقلٌّ أُسِّس في Alba عام 1992. "
            "لا نعمل إلاّ مع كل كَرَّام مستقل يخمّر عنبه بنفسه · لا تعاونيّات · "
            "لا خمور صناعية · لا تسميات صُنعت على الورق. لكي يدخل قبوٌ ما "
            "إلى الكَرْت، يزوره Pietro ثلاث مرّات على الأقل.",

        "mission_label":   "رسالتنا",
        "mission_heading": "أن نوفّي كَرَّاماً مستقلاًّ حقَّه.",
        "mission_text":
            "وُجد الحانوت لسببٍ واحد: أن نُعيد إلى كل كَرَّام مستقل السعر "
            "الذي يستحقّه عمله. هامشٌ متّفقٌ عليه بشفافية، عقودٌ سنوية "
            "موقَّعة باليد، وعربون على العنب في الكَرْم إن لزم. لا نبيع "
            "«تخفيضات»: من يصنع Nebbiolo بكحول 14% لا يستطيع أن يُخفِّض "
            "شيئاً.",

        "process_label":   "كيف نختار التسميات",
        "process_heading": "ثلاث زيارات، كَرْتٌ واحد.",
        "process_steps": [
            {"num": "01", "title": "الزيارة الأولى · الربيع",
             "desc": "يذهب Pietro إلى الكَرْم في آذار أو نيسان، ينظر إلى "
                     "التشذيب، ويتذوّق آخر المواسم من البراميل، ويُسائل "
                     "الكَرَّام المستقل عن صيف العام الفائت."},
            {"num": "02", "title": "الزيارة الثانية · القطاف",
             "desc": "أيلول-تشرين الأول · حضورٌ في يوم قطاف · ثلاث صناديق "
                     "تُفتح على الأقل. ننظر إلى من يقطف في الكَرْم، وبأيّ "
                     "عناية يفعل ذلك."},
            {"num": "03", "title": "الزيارة الثالثة · تذوّق في القبو",
             "desc": "الشتاء التالي · تذوّقٌ تقني للبراميل مع الكَرَّام المستقل. "
                     "إن كانت الأرقام منطقية والخمرة تقول الحقيقة، يُوقَّع "
                     "العقد السنوي."},
            {"num": "04", "title": "الدخول إلى الكَرْت",
             "desc": "أول إصدار يدخل الكَرْت بعد الزيارة الرابعة فقط (خروجٌ "
                     "من البراميل، قنينةٌ في اليد). لا تدخل خمرة الكَرْت قبل "
                     "أن يتذوّقها Pietro في ثلاثة مواسم مختلفة."},
        ],

        "founder_label":   "المؤسِّس",
        "founder_heading": "Pietro Brero.",
        "founder_text":
            "وُلد Pietro في Alba عام 1958. نشأ في trattoria العائلة، وعمل "
            "خبيرَ نبيذٍ (sommelier) في Combal.Zero مع Davide Scabin من "
            "1985 إلى 1991، حين كان Combal لا يزال في Almese. افتتح "
            "Sapori di Langa عام 1992 في via Vittorio Emanuele بثلاثة "
            "قبوٍ في الكَرْت. اليوم اثنان وثلاثون. مُنح وسام فرسان الكَمأة "
            "وخمور Alba (Cavalier dell'Ordine dei Cavalieri del Tartufo "
            "e dei Vini di Alba) عام 2014.",
        "founder_portrait": _FOUNDER_PORTRAIT,
        "founder_caption": "Pietro Brero · Cavalier dell'Ordine dei Cavalieri del Tartufo e dei Vini di Alba",

        "numbers_label":   "الحانوت بالأرقام",
        "numbers_items": [
            ("32",     "كَرَّاماً مستقلاًّ في الكَرْت · كل كَرَّام مستقل بتوقيعه"),
            ("180",    "تسميةً في الكتالوج السنوي"),
            ("1992",   "سنة الافتتاح"),
            ("65 كم", "أقصى نصف قطر اختيار من Langhe"),
        ],

        "visit_label":   "زُر الحانوت",
        "visit_heading": "Via Vittorio Emanuele 38, <em>Alba.</em>",
        "visit_text":
            "خمس دقائق من Stazione di Alba · عشر دقائق من الكاتدرائية. "
            "تذوّقٌ موجَّه بموعد مسبق عصر الخميس · خمس خمور مع طبق "
            "Castelmagno وSalame Cuneo، 35 € للشخص. لا حاجة لموعد للشراء "
            "في أوقات الفتح.",
        "visit_primary":      "احجز تذوّقاً",
        "visit_primary_href": "contatti",
        "visit_secondary":    "الخريطة والأوقات",
    },

    # ─── JOURNAL ───────────────────────────────────────────────
    "journal": {
        "eyebrow":  "دفتر الحانوت",
        "headline": "ملاحظاتُ قبوٍ، <em>ملاحظاتُ قطاف.</em>",
        "intro":
            "ملاحظاتٌ موجزة من Pietro وFederica حول العمل في القبو، "
            "والمواسم الجارية، والقناني التي تُفتح في الأمسيات للزبائن "
            "الأكثر فضولاً. قراءةٌ محجوزة للقرّاء.",
        "list_label": "أبواب دفتر الكَرَّام المستقل",
        "entries": [
            {
                "slug":    "vendemmia-2024-langhe",
                "kicker":  "قطاف 2024",
                "title":   "قطاف 2024 في Langhe · ما خرج من البراميل",
                "date":    "10 تشرين الأول 2026",
                "read_min": 6,
                "author":  "Pietro Brero",
                "lede":
                    "تطلَّب قطاف 2024 صبراً. حرارة آب أبطأت النضج، "
                    "وأيلول أعاد الأمور إلى مسارها. ها هو ما يدخل "
                    "الكَرْت ابتداءً من تشرين الثاني.",
            },
            {
                "slug":    "barolo-2019-degustazione",
                "kicker":  "موسم في الكَرْت",
                "title":   "لماذا يستحقّ Barolo 2019 ست سنوات من الانتظار",
                "date":    "28 أيلول 2026",
                "read_min": 5,
                "author":  "Pietro Brero",
                "lede":
                    "خرج موسم 2019 في آب بعد ثلاثين عاماً من Barolo في "
                    "القبو. هذه أسباب استحقاقه عامين في البرميل الكبير "
                    "وستّ سنوات حدّاً أدنى قبل فتحه.",
            },
            {
                "slug":    "olio-evo-langhe-2024",
                "kicker":  "زيت البيت",
                "title":   "Olio EVO Langhe 2024 · حصادٌ يُذكر",
                "date":    "15 أيلول 2026",
                "read_min": 4,
                "author":  "Federica Bertola",
                "lede":
                    "أنهى Frantoio Anfossi حصاد 2024 في الخامس من أيلول. "
                    "خمسة هكتولترات في الكَرْت ابتداءً من تشرين الأول، "
                    "إصدار 12. هذا طعمُه.",
            },
        ],

        "footer_note_label": "اِستقبل الدفتر بالبريد",
        "footer_note":
            "أربعة إلى خمسة أعداد في العام، لا أكثر. لا يستقبله إلاّ من "
            "طلبه صراحةً في الحانوت أو على نموذج التواصل.",
    },

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "زيارة وطلبات",
        "headline": "اتّصالٌ واحد، <em>صندوقٌ واحد.</em>",
        "intro":
            "لطلب صندوقٍ أو حجز تذوّقٍ موجَّه، أبسط الطرق اتّصالٌ هاتفي "
            "بالحانوت في أوقات الفتح. أو استعمال النموذج أدناه · جوابنا "
            "خلال 24 ساعة في أوقات العمل.",

        "form_section_label": "راسلنا",
        "form_section_intro":
            "للطلبات الخاصة (تذوّقات رأسية، Magnum، صناديق مؤسسية)، "
            "أشِر إلى اسم الكَرَّام المستقل أو الموسم المرغوب. للتذوّقات الموجَّهة، "
            "أشِر إلى التاريخ وعدد المشاركين.",
        "form_helper_required": "الحقول المعلَّمة إلزامية.",
        "form_submit_button":   "أرسِل الطلب",
        "form_submit_note":     "تستقبل تأكيداً بالبريد خلال 24 ساعة في أوقات الفتح.",

        "form_fields": [
            {"name": "name",     "label": "الاسم واللقب",   "type": "text",     "required": True},
            {"name": "email",    "label": "البريد",          "type": "email",    "required": True},
            {"name": "phone",    "label": "الهاتف",          "type": "tel",      "required": False},
            {"name": "subject",  "label": "الموضوع",         "type": "select",
             "options": ["طلب صندوق كَرَّام مستقل", "تذوّق موجَّه", "تذوّق رأسي أو Magnum",
                         "صندوق مؤسسي أو هدية", "غير ذلك"],     "required": True},
            {"name": "message",  "label": "الرسالة",         "type": "textarea", "required": True,
             "placeholder": "مثال: «صندوق من ستّ قناني Barolo موسم 2019» أو "
                             "«تذوّق لأربعة أشخاص الخميس 18 تشرين الأول»."},
        ],

        "card_label":          "الحانوت",
        "card_address_label":  "العنوان",
        "card_address_value":  "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "card_phone_label":    "الهاتف",
        "card_phone_value":    "+39 0173 364 990",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "0173 364 990",
        "card_email_label":    "البريد",
        "card_email_value":    "enoteca@saporidilanga.it",
        "card_hours_label":    "الأوقات",
        "card_hours_rows": [
            "الثلاثاء – السبت · 9:30 – 19:30 دوام متواصل",
            "الأحد · 10:00 – 13:00 صباحاً فقط",
            "الإثنين · مغلق · تذوّقات خاصة بموعد مسبق",
            "موسم Fiera del Tartufo · ت1 – ت2 · 9 – 21 دوام متواصل",
        ],
        "card_directions_label": "كيف تصل",
        "card_directions_text":
            "خمس دقائق سيراً من Stazione di Alba (قطار إقليمي مباشر من "
            "Torino · 1 ساعة و10 دقائق). عشر دقائق من كاتدرائية San "
            "Lorenzo. موقفٌ مجاني في Piazza Risorgimento، على بُعد 200 "
            "متر من الحانوت.",

        "faq_label": "أسئلة متكرّرة",
        "faq_items": [
            ("كم تكلفة الشحن؟",
             "شحن مبرَّد خلال 48 ساعة: € 12 في إيطاليا "
             "(مجاناً فوق € 200)، € 24 في أوروبا الغربية. "
             "الحدّ الأدنى ستّ قناني للصندوق."),
            ("هل يمكنني طلب قنينة واحدة فقط؟",
             "لا، الحدّ الأدنى ستّ قناني في الصندوق. التشكيلة "
             "حرّة بين الخمور وزيت الزيتون والأجبان والمقدَّدات. "
             "قيمة الصندوق الأدنى تقريباً € 90-100."),
            ("هل لديكم خمور بيولوجية أو طبيعية؟",
             "نعم. نحو 70% من كَرَّامينا المستقلّين في الكَرْت يعملون "
             "بزراعة بيولوجية معتمَدة، و20% بزراعة بيوديناميكية "
             "معتمَدة Demeter. الباقي يتّبع بروتوكولات بأقلّ "
             "تدخّل لكن بلا شهادة."),
            ("هل تشحنون خارج إيطاليا؟",
             "أوروبا الغربية نعم (فرنسا، ألمانيا، بلجيكا، هولندا، "
             "لوكسمبورغ، النمسا). باقي العالم بعرض سعر فقط "
             "(USA · UK · Svizzera · Giappone)."),
            ("هل يمكن زيارة الحانوت دون حجز؟",
             "نعم، في أوقات الفتح. أمّا التذوّق الموجَّه عصر الخميس "
             "فيستلزم حجزاً مسبقاً قبل 48 ساعة على الأقل."),
        ],
    },
}
