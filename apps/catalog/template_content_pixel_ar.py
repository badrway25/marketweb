"""Pixel — Portfolio Fotografico · Arabic content tree.

Mirrors the shape of ``PIXEL_CONTENT_IT`` exactly — same keys, nesting and
list shapes. Authored Session 39 for the Pixel live i18n rollout of the
cinematic-photographer archetype. Formal MSA (الفصحى الحديثة) editorial register,
proper names in Latin script, Latin digits for technical data.
"""
from __future__ import annotations

from typing import Any


PIXEL_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "الفهرس",        "kind": "home"},
        {"slug": "serie",         "label": "السلاسل",       "kind": "series_list"},
        {"slug": "biografia",     "label": "السيرة",        "kind": "about"},
        {"slug": "pubblicazioni", "label": "النشرات",       "kind": "publications"},
        {"slug": "contatti",      "label": "تواصل",         "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "P",
        "logo_word":      "Pixel — Lorenzo Bianchi",
        "logo_short":     "PXL",
        "tag":            "مصوِّر مؤلِّف · Milano · Trieste",
        "phone":          "+39 348 211 7720",
        "email":          "studio@lorenzobianchi.photo",
        "address":        "Via Tadino 18 · 20124 Milano",
        "hours_compact":  "متاح للتكليفات · 2026 — 27",
        "license":        "تسجيل Tau · نقابة المصوّرين المحترفين رقم 4421/2014",
        "footer_intro":
            "مصوِّر مؤلِّف مستقل. ريبورتاج طويل النَفَس، "
            "وبورتريه تحريري، وتكليفات علامة لدور النشر "
            "والغاليريهات ودور الأزياء. ممثَّل من قِبَل "
            "Galleria Carla Sozzani في مجال الطباعة الفنية.",
        # Primary nav bracket CTA (right-side) — lifted Session 39 per D-047
        "nav_cta":       "افتح محادثة",
        "foot_studio":   "الاستوديو",
        "foot_pages":    "الفهرس",
        "foot_contact":  "تواصل",
        "foot_kit":      "المعدّات",
        # EXIF-style footer cells
        "exif_footer": [
            ("المقر",        "Milano · Trieste"),
            ("الإتاحة",      "تكليفات 2026 — 27"),
            ("التمثيل",      "Galleria Carla Sozzani · Milano"),
            ("الطباعة",      "Atelier Druckwerkstatt · Berlin"),
        ],
        # Footer kit column rows (per-tenant — never inline in skin per D-047)
        "kit_footer_rows": [
            "Mamiya 7II · Sony α7R V",
            "Kodak Portra 400",
            "طباعة · Druckwerkstatt Berlin",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Series counter chip (top-left of hero)
        "series_counter_label": "السلسلة الراهنة",
        "series_counter_value": "07 / 24",

        # Status pulse on nav (right side)
        "status_pulse": "متاح · 2026 — 27",

        # Eyebrow + headline
        "eyebrow":   "التصوير الفوتوغرافي المؤلِّف · 2014 — 2026",
        # All-caps cinematic hero per archetype
        "headline":  "مراقبة ما يبقى <em>حين تتبدّل الإضاءة</em>",
        "subhead":
            "ريبورتاج طويل النَفَس، وبورتريه تحريري، "
            "وتكليفات علامة. أعمل على فيلم متوسط المقاس "
            "وعلى رقمي ثنائي الحسّاس — لمشاريع تطلب "
            "عشرة أيام أو ثلاث سنوات من الوقت.",
        "primary_cta":   "افتح السلسلة الكاملة",
        "primary_href":  "serie",
        "secondary_cta": "إتاحة 2026",
        "secondary_href":"contatti",

        # Hero image — fullbleed dominant
        "hero_image":
            "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
        "hero_image_alt":
            "مشهد من ميناء Trieste عند الساعة 6:14 فجراً · "
            "نوفمبر 2025 · فيلم Kodak Portra 400",

        # EXIF credit cells under hero (4-cell mono bar)
        "hero_credit_cells": [
            ("الكاميرا",   "Mamiya 7II"),
            ("الفيلم",     "Kodak Portra 400"),
            ("المكان",     "Porto Vecchio · Trieste"),
            ("التاريخ",    "نوفمبر 2025"),
        ],

        # Featured series (filmstrip on home — 4 series)
        "filmstrip_label":   "أعمال حديثة",
        "filmstrip_heading": "أربع سلاسل · 2024 — 2026",
        "filmstrip_intro":
            "أربعة أعمال طويلة النَفَس أُغلقت في العامَين الأخيرَين. "
            "تتاح السلاسل الكاملة في قسم «السلاسل» — "
            "تتضمّن كلّ سلسلة بين عشرين وأربعين صورة.",
        # Each: (num, title, discipline, year, slug-for-link)
        "filmstrip": [
            ("07", "Porto Vecchio · Trieste",
             "ريبورتاج طويل النَفَس", "2024 — 2026",
             "porto-vecchio-trieste"),
            ("06", "Atelier Velluti & Co.",
             "تكليف تحريري", "2025",
             "atelier-velluti"),
            ("05", "بيوت الحجر",
             "ريبورتاج معماري", "2023 — 2024",
             "case-di-pietra-puglia"),
            ("04", "بورتريهات نهر Po",
             "بورتريه مؤلِّف", "2023",
             "ritratti-del-po"),
        ],

        # Reel — REMOVED per D-068 (Session 36).
        # A short-film claim without a real signed MP4 shipped as a placeholder
        # contradicts the cinematic-photographer identity; the "Play · 3:12" +
        # "Reel · 1080p · 24 fps" meta also trespassed into codec-theatre.
        # Lorenzo's identity is stills — the filmstrip + EXIF cells + series
        # index already carry the cinematic voice. When a genuine Carso reel
        # exists, this block can return with a real `src` and meta pruned of
        # pseudo-technical cues.

        # About excerpt — 3 sentences (full bio on /biografia)
        "about_label":   "ملاحظات سِيَريّة",
        "about_heading": "LORENZO BIANCHI",
        "about_excerpt":
            "وُلدت في Trieste عام 1986، وأعيش بين Milano "
            "وهضبة Carso. بدأت بتصوير أسواق Sarajevo "
            "عام 2009، ولم أغيّر اختصاصي منذ ذلك الحين — "
            "غيّرت الزمن والإضاءة والمقاس فقط. أعمل على "
            "فيلم Kodak Portra 400 متوسط المقاس للمشاريع "
            "الشخصية، وعلى رقمي Sony ثنائي الحسّاس للتكليفات.",
        "about_cta":     "اقرأ السيرة",
        "about_cta_href":"biografia",

        # Recent publications strip (3 selected)
        "publications_label":   "نُشر أخيراً",
        "publications_heading": "الصحافة والنشر · 2025",
        "publications": [
            ("FOAM Magazine رقم 64",
             "بورتفوليو من ثماني صفحات عن سلسلة «Porto Vecchio»",
             "نوفمبر 2025"),
            ("Internazionale رقم 1612",
             "ريبورتاج مصوَّر عن بيوت الحجر في Salento",
             "سبتمبر 2025"),
            ("Domus رقم 1102",
             "تكليف تحريري للعدد المونوغرافي Carlo Scarpa",
             "أبريل 2025"),
        ],

        # Final CTA band — commission inquiry
        "cta_label":   "تكليفات · إتاحة 2026 — 2027",
        "cta_heading": "[ افتح محادثة ]",
        "cta_intro":
            "أنا متاح لتكليفات تحريرية، ولبورتريه مؤلِّف، "
            "ولمشاريع طويلة الأمد حتى سبتمبر 2027. "
            "تكليفات العلامات تُدرَس حالة بحالة — "
            "أُفضِّل التفويضات ذات الأمد الطويل.",
        "cta_primary":      "اكتب مقترحاً",
        "cta_primary_href": "contatti",
        "cta_secondary":    "اذهب إلى التمثيل",
        "cta_secondary_href":"biografia",
    },

    # ─── SERIE (series_list) ────────────────────────────────────
    "serie": {
        "series_counter_label": "الأرشيف",
        "series_counter_value": "24 سلسلة",
        "status_pulse":         "متاح · 2026 — 27",

        "eyebrow":   "أرشيف السلاسل · 2009 — 2026",
        "headline":  "أربع وعشرون سلسلة، <em>اختصاص واحد</em>",
        "subhead":
            "الأرشيف الكامل للسلاسل الموقَّعة. ريبورتاج "
            "طويل النَفَس، وبورتريه مؤلِّف، وتكليفات تحريرية. "
            "المختارات المعروضة تغطّي الأعمال الأحدث — "
            "أمّا السلاسل التاريخية (2009 — 2018) فمتاحة "
            "عند الطلب للدراسة أو النشر.",

        # Discipline filter pills
        "filter_label": "الاختصاصات",
        "filters": [
            "الكلّ",
            "ريبورتاج طويل النَفَس",
            "بورتريه مؤلِّف",
            "تكليف تحريري",
            "ريبورتاج معماري",
        ],

        # Index intro band
        "index_label": "مختارات 2018 — 2026",
        "index_intro":
            "انقر على الغلاف لفتح السلسلة الكاملة. "
            "تتضمّن كلّ سلسلة بين عشرين وأربعين صورة، "
            "مع أداة نقدية وبيانات EXIF لكلّ لقطة.",

        # CTA before footer
        "cta_label":   "أتبحثون عن شيء بعينه؟",
        "cta_heading": "[ أرشيف محفوظ · صحافة واستوديو ]",
        "cta_intro":
            "للوصول إلى الأرشيف التاريخي (2009 — 2018)، "
            "أو لطلبات الطباعة الفنية، أو لتكليف عمل جديد: "
            "افتحوا محادثة تمهيدية.",
        "cta_primary":      "اكتب إلى المصوِّر",
        "cta_primary_href": "contatti",

        # Chrome labels shared by serie card + series_detail page.
        # Lifted Session 39 (D-047 lift) — same labels across every post,
        # so they live on the parent serie block rather than on each post.
        "card_arrow_label":        "افتح السلسلة",
        "post_discipline_label":   "الاختصاص",
        "post_period_label":       "المدّة",
        "post_location_label":     "المكان",
        "post_frames_label":       "الصور",
        "post_gallery_label":      "الغاليري",
        "post_edition_label":      "الإصدار",
    },

    # ─── BIOGRAFIA (about) ──────────────────────────────────────
    "biografia": {
        "series_counter_label": "ملاحظات سِيَريّة",
        "series_counter_value": "1986 — 2026",
        "status_pulse":         "المقر · Milano + Trieste",

        "eyebrow":   "ملاحظات سِيَريّة · 1986 — 2026",
        "headline":  "LORENZO BIANCHI <em>مصوِّر مؤلِّف</em>",
        "subhead":
            "وُلدت في Trieste عام 1986، وأعيش بين Milano "
            "وهضبة Carso. بدأت بتصوير أسواق Sarajevo "
            "عام 2009 — مقالة لصالح Granta لم تُنشر قطّ. "
            "ومنذ ذلك الحين لم أغيّر اختصاصي، بل غيّرت "
            "الزمن والإضاءة والمقاس فقط.",

        # Bio statement — 5 paragraphs
        "statement_label":   "بيان",
        "statement_heading": "لماذا أصوِّر",
        "statement_paragraphs": [
            "أصوِّر لأبقى طويلاً في المكان. التصوير هو "
            "الاختصاص الوحيد الذي يُلزمني بالعودة. "
            "السلسلة، في فهمي، عشر رحلات أو عشرون على "
            "امتداد أشهر إلى النقطة ذاتها، حتى يتبدّل "
            "شيء بما يكفي ليستحقّ لقطة.",
            "أعمل على فيلم متوسط المقاس — Mamiya 7II، "
            "وعدستان، وKodak Portra 400. البطء الميكانيكي "
            "انضباط لا تفنُّن. أُحمِّض وأطبع بنفسي، "
            "في مطبخ حُوِّل إلى غرفة مظلمة للسحوبات "
            "الصغيرة، وعند Druckwerkstatt Berlin للطباعة الفنية.",
            "في التكليفات التحريرية أستعمل نظاماً رقمياً "
            "من Sony Alpha ثنائي الحسّاس — سرعة التسليم "
            "التي تشترطها غرفة التحرير لا تتصالح مع زمن "
            "الفيلم. غير أنّ طريقة النظر تبقى كما هي، "
            "والرقمي ليس إلّا عربة أخرى.",
            "أنا ممثَّل منذ عام 2018 من قِبَل Galleria "
            "Carla Sozzani في Milano للطباعة الفنية "
            "والسوق الثانوية. أمّا تكليفات التحرير "
            "والعلامات فأعمل فيها مباشرةً، دون وكيل — "
            "الوكيل يعني مصفاةً بين المصوِّر والمُكلِّف، "
            "وأفقد بها المحادثات التي تهمّني أكثر.",
            "أُدرِّس التصوير الوثائقي في CFP Bauer بـMilano "
            "منذ عام 2019 — يوماً واحداً في الأسبوع، "
            "لطلبة السنة الثانية. هذا هو الالتزام الثابت "
            "الوحيد في تقويم الاستوديو. كلّ ما عداه "
            "مُختار بحسب المشروع.",
        ],

        # Camera kit — what we shoot with.
        # Availability label + value lifted Session 39 (D-047).
        "kit_label":                "معدّات العمل",
        "kit_heading":              "أربعة أنظمة، خيار واحد لكلّ مشروع",
        "kit_availability_label":   "متاح",
        "kit_availability_value":   "بالتكليف",
        "kit": [
            ("01", "Mamiya 7II",
             "كاميرا تلميترية متوسطة المقاس 6 × 7 سم، وعدستان (80mm و43mm). "
             "للأعمال الشخصية على فيلم — ريبورتاج طويل النَفَس "
             "وبورتريه مؤلِّف.",
             "فيلم الاستوديو", "Kodak Portra 400 + Tri-X 400"),
            ("02", "Sony α7R V + α7S III",
             "حسّاس مزدوج (دقّة عالية + حساسية). "
             "للتكليفات التحريرية وللأعمال التي تستوجب "
             "تسليماً خلال 72 ساعة.",
             "العدسات", "GM 24/35/85 + Voigtländer 50/1.5"),
            ("03", "Linhof Master Technika 4 × 5",
             "كاميرا منضدية للطباعة الفنية والبورتريه في الاستوديو. "
             "محفوظة لثماني إلى عشر لقطات في السنة للغاليري.",
             "لوحة", "Ilford FP4+ · Foma Retropan 320"),
            ("04", "غرفة مظلمة · مطبخ Milano",
             "تحميض وطباعة للسحوبات الصغيرة (حتى 18 × 24 سم). "
             "السحوبات الفنية تُطبع لدى Druckwerkstatt Berlin "
             "بالتعاون مع Anna Wedekind.",
             "ورق الاستوديو", "Ilford Multigrade FB Classic"),
        ],

        # Exhibitions + publications timeline (selected — full list /pubblicazioni)
        "timeline_label":   "معارض ونشرات · مختارات",
        "timeline_heading": "اثنتا عشرة محطّة، خمسة عشر عاماً",
        "timeline": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "معرض جماعي · سلسلة «Porto Vecchio»"),
            ("2025", "FOAM Magazine رقم 64",
             "بورتفوليو من ثماني صفحات عن سلسلة «Porto Vecchio»"),
            ("2024", "Triennale Milano · «جغرافية أرض»",
             "معرض فردي · سلسلة «بيوت الحجر»"),
            ("2024", "World Press Photo Story of the Year · Finalist",
             "فئة المشاريع طويلة الأمد، سلسلة «بيوت الحجر»"),
            ("2023", "Internazionale Festival Ferrara",
             "معرض جماعي · سلسلة «بورتريهات نهر Po»"),
            ("2022", "Photo London · جناح Galleria Carla Sozzani",
             "طبعات فنية · مختارات 2018 — 2022"),
            ("2021", "Magnum Foundation Grant · في القائمة القصيرة",
             "فئة المصوّر الصاعد"),
            ("2020", "MAXXI Roma · «يوميّات الإغلاق»",
             "معرض جماعي · مساهمة شخصية بـ12 طبعة"),
            ("2019", "GUP Magazine رقم 60 · غلاف",
             "مقالة مصوَّرة عن أرشيف أسواق Sarajevo"),
            ("2018", "FOAM Talent · Amsterdam · مختارات",
             "سلسلة «قطارات الليل»"),
            ("2016", "Premio Marco Pesaresi · في القائمة القصيرة",
             "ريبورتاج إيطالي · «العبور»"),
            ("2009", "Granta Magazine · مقالة مكلَّف بها (لم تُنشر)",
             "أسواق Sarajevo · بداية احترافية"),
        ],

        # Final CTA — commissions
        "cta_heading":      "[ تكليفات 2026 — 2027 ]",
        "cta_intro":
            "يقبل الاستوديو ستّ إلى ثماني تكليفات في السنة، "
            "تُختار بحسب الوقت المتاح وبحسب الانسجام مع "
            "الاختصاص. المقترحات التحريرية ومقترحات العلامات "
            "تُدرَس حالة بحالة — أُفضِّل التفويضات ذات الأمد الطويل.",
        "cta_primary":      "افتح محادثة",
        "cta_primary_href": "contatti",
    },

    # ─── PUBBLICAZIONI (publications) ───────────────────────────
    "pubblicazioni": {
        "series_counter_label": "أرشيف الصحافة",
        "series_counter_value": "47 نشرة",
        "status_pulse":         "محدَّث · يناير 2026",

        "eyebrow":   "نشرات ومعارض · 2009 — 2026",
        "headline":  "سبع وأربعون نشرة، <em>خمسة عشر عاماً</em>",
        "subhead":
            "الأرشيف الكامل للمنشورات المطبوعة، والمعارض "
            "الفردية والجماعية، والجوائز والإقامات. القائمة "
            "محدَّثة حتى يناير 2026 — تصدر إصدارات إضافية "
            "خلال السنة.",

        # Press band — magazine + book covers
        "press_label":   "صحافة ونشر · أبرز الإصدارات",
        "press_heading": "مجلّات ومجلّدات مونوغرافية",
        "press": [
            {
                "year":    "2025",
                "outlet":  "FOAM Magazine رقم 64",
                "type":    "بورتفوليو تحريري",
                "subject": "سلسلة «Porto Vecchio · Trieste»",
                "format":  "8 صفحات · طباعة أوفست · Amsterdam",
            },
            {
                "year":    "2025",
                "outlet":  "Internazionale رقم 1612",
                "type":    "ريبورتاج مصوَّر",
                "subject": "سلسلة «بيوت الحجر · Salento»",
                "format":  "12 صفحة · طباعة روتوغرافور · Roma",
            },
            {
                "year":    "2025",
                "outlet":  "Domus رقم 1102",
                "type":    "تكليف تحريري",
                "subject": "العدد المونوغرافي Carlo Scarpa",
                "format":  "16 صفحة · طباعة أوفست · Milano",
            },
            {
                "year":    "2024",
                "outlet":  "بيوت الحجر (مجلد مونوغرافي)",
                "type":    "مجلّد مونوغرافي",
                "subject": "ريبورتاج معماري · Salento 2023 — 24",
                "format":  "دار Quodlibet · 168 صفحة · 24 × 28 سم",
            },
            {
                "year":    "2024",
                "outlet":  "GUP Magazine رقم 73",
                "type":    "مقالة نقدية",
                "subject": "حوار مع Sarah Kelly حول الأزمنة الطويلة",
                "format":  "10 صفحات · طباعة أوفست · Amsterdam",
            },
            {
                "year":    "2023",
                "outlet":  "Vogue Italia · قسم Photography",
                "type":    "بورتريه تحريري",
                "subject": "بورتريهات نهر Po · سلسلة مختارة",
                "format":  "6 صفحات · طباعة أوفست · Milano",
            },
            {
                "year":    "2022",
                "outlet":  "Aperture رقم 248",
                "type":    "مقالة مصوَّرة",
                "subject": "تأمّل في الفيلم في الزمن الرقمي",
                "format":  "8 صفحات · طباعة أوفست · New York",
            },
            {
                "year":    "2019",
                "outlet":  "GUP Magazine رقم 60 · غلاف",
                "type":    "غلاف + مقالة مصوَّرة",
                "subject": "أرشيف أسواق Sarajevo 2009",
                "format":  "غلاف + 14 صفحة · طباعة أوفست · Amsterdam",
            },
        ],

        # Exhibitions
        "exhibitions_label":   "معارض · فردية وجماعية",
        "exhibitions_heading": "اثنا عشر معرضاً، خمسة عشر عاماً",
        "exhibitions": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "جماعي · 18 مصوِّراً دولياً",
             "مارس — مايو 2026"),
            ("2024", "Triennale Milano · «جغرافية أرض»",
             "فردي · سلسلة «بيوت الحجر» · 38 طبعة",
             "سبتمبر — ديسمبر 2024"),
            ("2023", "Internazionale Festival Ferrara",
             "جماعي · قسم المشاريع طويلة الأمد",
             "أكتوبر 2023"),
            ("2022", "Photo London · جناح Galleria Carla Sozzani",
             "سوق فنية · 14 طبعة معروضة للبيع",
             "مايو 2022"),
            ("2020", "MAXXI Roma · «يوميّات الإغلاق»",
             "جماعي · 12 طبعة من المساهمة الشخصية",
             "سبتمبر — نوفمبر 2020"),
            ("2018", "FOAM Talent · Amsterdam · سلسلة مختارة",
             "جماعي · سلسلة «قطارات الليل» · 16 طبعة",
             "أبريل — يونيو 2018"),
        ],

        # Awards & residencies
        "awards_label":   "جوائز وإقامات",
        "awards_heading": "تكريمات",
        "awards": [
            ("2024", "World Press Photo · Finalist · المشاريع طويلة الأمد",
             "سلسلة «بيوت الحجر»"),
            ("2023", "Magnum Foundation · Photography & Social Justice · مختار",
             "برنامج إرشاد · 6 أشهر في New York"),
            ("2021", "Magnum Foundation Grant · في القائمة القصيرة للمصوّرين الصاعدين",
             "منحة للعمل الشخصي"),
            ("2020", "Premio Voglino · في القائمة القصيرة",
             "فئة الريبورتاج الإيطالي"),
            ("2016", "Premio Marco Pesaresi · في القائمة القصيرة",
             "ريبورتاج إيطالي · «العبور»"),
            ("2014", "Premio Angelo Frontoni · مختار",
             "فئة التصوير الوثائقي"),
        ],

        # Final CTA — speaking + workshops
        "cta_heading":      "[ محاضرات · ورش · ندوات ]",
        "cta_intro":
            "لطلبات التدخّل الأكاديمي (مهرجانات، مدارس، "
            "جامعات)، أو ورش على فيلم متوسط المقاس، أو "
            "محاضرات تحريرية: افتحوا محادثة. تُحدَّد الإتاحة "
            "في التقويم قبل ثلاثة أشهر على الأقلّ.",
        "cta_primary":      "افتح محادثة",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "series_counter_label": "الإتاحة",
        "series_counter_value": "2026 — 27",
        "status_pulse":         "مفتوح للتكليفات",

        "eyebrow":   "محادثة تمهيدية · دون وسطاء",
        "headline":  "[ افتح محادثة ] <em>مباشرة</em>",
        "subhead":
            "تُناقَش التكليفات مباشرةً مع المصوِّر، دون وكيل. "
            "للمقترحات التحريرية، أو مقترحات العلامات، أو "
            "الطباعة الفنية (تمثيل Galleria Carla Sozzani · "
            "Milano): اكتبوا مقترحاً. أُجيب خلال اثنتين "
            "وسبعين ساعة عمل.",

        # Studio info side card (dark style)
        "studio_label":   "الاستوديو التشغيلي",
        "studio_address": "Via Tadino 18 · 20124 Milano",
        "studio_area":    "Porta Venezia · مدخل جانبي · جرس «Bianchi»",
        "studio_metro":   "مترو MM1 / MM3 Loreto · 4 دقائق سيراً",
        "studio_hours":   "متاح بموعد مسبق · ليس على حين غِرّة",
        "studio_row_address_label":  "العنوان",
        "studio_row_entrance_label": "المدخل",
        "studio_row_metro_label":    "المترو",
        "studio_row_hours_label":    "متاح",

        # Form fields
        "form_label":   "مقترح تكليف",
        "form_heading": "[ املأ المقترح ]",
        "form_intro":
            "مقترح التكليف وصف مُنظَّم للمشروع الفوتوغرافي. "
            "ليس موجزاً تسويقياً — بل محادثة تمهيدية "
            "للنظر في مدى تطابق اختصاص العمل مع اختصاصي.",
        "form_fields": [
            {"name": "name",      "label": "الاسم",          "type": "text",     "required": True,  "placeholder": "مثلاً Lorenzo",
             "helper": "الاسم فقط، شكراً."},
            {"name": "surname",   "label": "اللقب",          "type": "text",     "required": True,  "placeholder": "مثلاً Bianchi",
             "helper": "كما يَرِد في التوقيع."},
            {"name": "organization", "label": "الجهة",       "type": "text", "required": False, "placeholder": "مثلاً FOAM Magazine",
             "helper": "إن كان التكليف تحريرياً أو لصالح علامة."},
            {"name": "email",     "label": "البريد الإلكتروني",    "type": "email",    "required": True,  "placeholder": "lorenzo@foam.org",
             "helper": "بريد مباشر · الردّ خلال 72 ساعة عمل."},
            {"name": "phone",     "label": "الهاتف",         "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "فقط إن كنتم تفضّلون المعاودة هاتفياً."},
            {"name": "discipline", "label": "اختصاص التكليف", "type": "select", "required": True,
             "options": [
                 "يُحدَّد في المحادثة",
                 "ريبورتاج طويل النَفَس",
                 "بورتريه تحريري",
                 "تكليف علامة",
                 "ريبورتاج معماري",
                 "طباعة فنية (Galleria Sozzani)",
                 "ورشة / محاضرة",
             ],
             "helper": "اختاروا «يُحدَّد» إن كان المجال لم يتّضح بعد."},
            {"name": "timeline",  "label": "زمن التنفيذ", "type": "select", "required": True,
             "options": [
                 "خلال شهر (تسليم سريع)",
                 "ثلاثة — ستّة أشهر (تكليف تحريري)",
                 "ستّة — ثمانية عشر شهراً (عمل طويل النَفَس)",
                 "استكشافي · دون موعد نهائي",
             ],
             "helper": "أزمنة التسليم تُحدِّد المقاس (رقمي أو فيلم)."},
            {"name": "location",  "label": "مكان التصوير", "type": "text", "required": False,
             "placeholder": "مثلاً Salento · Trieste · Sarajevo",
             "helper": "ذكر المدينة / المنطقة / البلد · يلزم لتقدير الرحلات."},
            {"name": "story",     "label": "الحكاية التي ترغبون في روايتها", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "بحدّ أقصى 1000 حرف. وصف للموضوع، ولأسباب "
                            "المشروع، وللمنفذ المرتقب للنشر. لا موجز تسويقياً "
                            "— ما يهمّ هنا هو المحتوى، لا مخرجات التسليم.",
             "helper": "إن لم تعرفوا من أين تبدؤون، اكتبوا ما استوقفكم."},
        ],

        "form_sections": [
            {"num": "01", "title": "المرجع",
             "meta": "الشخص الذي سيتابع التكليف من جهة المُكلِّف.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "النشر",
             "meta": "لفهم السياق التحريري أو سياق العلامة.",
             "fields": ["organization"]},
            {"num": "03", "title": "إطار التكليف",
             "meta": "أزمنة التسليم تُحدِّد مقاس الالتقاط — فيلم أو رقمي.",
             "fields": ["discipline", "timeline", "location", "story"]},
            {"num": "04", "title": "مراجع (اختيارية)",
             "meta": "موجز تحريري، أو خطّة عدد، أو صور مرجعية. قد تُمهّد للمحادثة.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "مراجع تمهيدية",
            "helper":   "موجز تحريري، أو خطّة عدد، أو صور مرجعية. "
                        "PDF / DOCX / JPG / PNG · بحدّ أقصى 25 ميغابايت إجمالاً.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "اسحبوا المستندات هنا أو",
            "link":     "تصفّحوا من الأرشيف",
            "meta":     "PDF / DOCX / JPG · بحدّ أقصى 25 ميغابايت",
        },

        "form_submit_label": "[ أرسل المقترح ]",
        "form_submit_note":
            "الردّ مباشرةً من المصوِّر خلال 72 ساعة عمل. "
            "لا وكيل، ولا أتمتة للاستفسارات.",
        "form_consent":
            "أوافق على معالجة البيانات الشخصية وفق اللائحة "
            "الأوروبية 679/2016. تُقرَأ طلبات التكليف وتُحفَظ "
            "من قِبَل المصوِّر وحده. أمّا الطباعة الفنية "
            "(السوق الثانوية) فالتمثيل فيها حصرياً لـGalleria "
            "Carla Sozzani.",

        # Sidebar — channels (EXIF style)
        "channels_label": "قنوات مباشرة",
        "channels": [
            ("الاستوديو",       "studio@lorenzobianchi.photo",      "الردّ خلال 72 ساعة"),
            ("الجوّال",          "+39 348 211 7720",                 "الاثنين – الجمعة · 10:00 – 19:00"),
            ("الطباعة الفنية",  "Galleria Carla Sozzani · Milano",   "Corso Como 10 · +39 02 6555 2223"),
            ("التدريس",         "CFP Bauer · Milano",                "وثائقي · السنة الثانية · الخميس"),
        ],

        "footnote":
            "في ما يخصّ الطباعة الفنية — البيع في السوق "
            "الثانوية، والإصدارات المحدودة، ومعارض الغاليري — "
            "التمثيل الحصري لـGalleria Carla Sozzani في Milano "
            "منذ عام 2018. تُوجَّه طلبات الطباعة التجارية "
            "مباشرةً إلى الغاليري.",
    },

    # ─── POSTS — drives /serie/<slug>/ series_detail ────────────
    "posts": [
        {
            "slug":        "porto-vecchio-trieste",
            "title":       "Porto Vecchio · Trieste",
            "category":    "ريبورتاج طويل النَفَس",
            "discipline":  "ريبورتاج طويل النَفَس",
            "year":        "2024 — 2026",
            "duration":    "24 شهراً · 18 رحلة",
            "location":    "Porto Vecchio · Trieste · إيطاليا",
            "frame_count": "47 صورة",
            "edition":     "إصدار محدود · 12 + 2 AP لكلّ طبعة",
            "print_meta": [
                ("السحب",        "12 + 2 AP لكلّ صورة"),
                ("الطباعة",       "Druckwerkstatt Berlin"),
                ("الورق",         "Hahnemühle Photo Rag Baryta 315 g/m²"),
                ("التمثيل",       "Galleria Carla Sozzani · Milano"),
            ],
            "lead":
                "أربعة وعشرون شهراً في ميناء Trieste الآيل "
                "إلى التفكيك — مساحة من ستّة وستّين هكتاراً "
                "بين بحر الأدرياتيك والمدينة، في انتقال بين "
                "الأثر الصناعي الهابسبورغي ومصير عمراني "
                "لم يُحسَم بعد. سبع وأربعون صورة على فيلم "
                "Kodak Portra 400 متوسط المقاس.",
            "cover_image":
                "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("الكاميرا",      "Mamiya 7II · 80mm + 43mm"),
                ("الفيلم",        "Kodak Portra 400 متوسط المقاس"),
                ("المدّة",        "نوفمبر 2024 — يناير 2026"),
                ("الطباعة",       "Druckwerkstatt Berlin · 30 × 40 سم"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=1600&q=85&auto=format&fit=crop",
                 "صورة 03",
                 "Porto Vecchio عند الفجر · حوض San Marco · نوفمبر 2024"),
                ("https://images.unsplash.com/photo-1505820013142-f86a3439c5b2?w=1600&q=85&auto=format&fit=crop",
                 "صورة 11",
                 "مخازن مهجورة · فبراير 2025 · 6:14 فجراً"),
                ("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600&q=85&auto=format&fit=crop",
                 "صورة 18",
                 "مشهد من الحوض المائي · ربيع 2025"),
                ("https://images.unsplash.com/photo-1499346030926-9a72daac6c63?w=1600&q=85&auto=format&fit=crop",
                 "صورة 24",
                 "حوض بناء سفن مُعطَّل · صيف 2025"),
                ("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=85&auto=format&fit=crop",
                 "صورة 31",
                 "خطّ الماء · أكتوبر 2025 · ضوء جانبي"),
                ("https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=1600&q=85&auto=format&fit=crop",
                 "صورة 39",
                 "مشهد أخير · يناير 2026 · آخر رحلة"),
            ],
            "sections": [
                {
                    "label": "السلسلة",
                    "heading": "ستّة وستّون هكتاراً، أربعة وعشرون شهراً",
                    "body":
                        "ميناء Porto Vecchio في Trieste مساحة "
                        "من ستّة وستّين هكتاراً على بحر "
                        "الأدرياتيك، مُعطَّلة منذ 1991 "
                        "وبانتظار مُخطَّط عمراني نهائي. "
                        "تتابع السلسلة حالته المُعلَّقة بين "
                        "نوفمبر 2024 ويناير 2026 — "
                        "ثماني عشرة رحلة، وثلاثة مواسم كاملة، "
                        "وإضاءة واحدة من الصباح الباكر. نُشر "
                        "العمل في FOAM Magazine رقم 64 "
                        "(نوفمبر 2025) وهو معروض في FOAM "
                        "Talent Lounge في Amsterdam منذ مارس 2026.",
                },
                {
                    "label": "المنهج",
                    "heading": "فيلم، فجر، عودة",
                    "body":
                        "صوَّرت دائماً بـMamiya 7II وفيلم "
                        "Kodak Portra 400 متوسط المقاس — "
                        "بعدستَين، 80 و43 ملم. نُفِّذ "
                        "العمل كلّه بين الساعة 5:30 و7:00 "
                        "فجراً، قبل وصول موظّفي الحراسة. "
                        "إضاءة Trieste في هذا النطاق الزمني "
                        "مميّزة — رياح البُورا الليلية "
                        "تُنقّي الهواء، وسطح الحوض يصبح "
                        "مرآة، والشمس لم تُشرق بعد فوق Carso.",
                },
                {
                    "label": "الإصدار",
                    "heading": "طباعة فنية · اثنتا عشرة نسخة",
                    "body":
                        "يضمّ الإصدار الفنّي اثنتَي عشرة طبعة "
                        "+ طبعتَي artist proof لكلّ صورة، "
                        "مطبوعة على ورق Hahnemühle Photo "
                        "Rag Baryta 315 g/m² لدى "
                        "Druckwerkstatt Berlin بالتعاون مع "
                        "Anna Wedekind. مقاس الطباعة "
                        "30 × 40 سم. التوزيع الفنّي "
                        "حصري لـGalleria Carla Sozzani في Milano.",
                },
            ],
            "next_label": "السلسلة التالية",
        },
        {
            "slug":        "case-di-pietra-puglia",
            "title":       "بيوت الحجر · Salento",
            "category":    "ريبورتاج معماري",
            "discipline":  "ريبورتاج معماري",
            "year":        "2023 — 2024",
            "duration":    "16 شهراً · 9 رحلات",
            "location":    "Salento · Puglia · إيطاليا",
            "frame_count": "62 صورة",
            "edition":     "إصدار مونوغرافي · Quodlibet · 168 صفحة",
            "print_meta": [
                ("السحب",        "1.500 نسخة · الطبعة الأولى نافدة"),
                ("الطباعة",       "Quodlibet · Macerata"),
                ("الورق",         "Munken Pure 130 g/m² · غير مطلي"),
                ("التمثيل",       "Galleria Carla Sozzani · Milano"),
            ],
            "lead":
                "ستّة عشر شهراً في مزارع الحجر الجاف في "
                "Salento الجنوبي — أربعون مبنى، دون أيّ "
                "تدخّل معاصر. ريبورتاج معماري وثائقي، "
                "نُشر في مجلّد مونوغرافي لدى Quodlibet "
                "(نوفمبر 2024) وفي Internazionale رقم 1612 "
                "(سبتمبر 2025).",
            "cover_image":
                "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("الكاميرا",      "Mamiya 7II + Sony α7R V"),
                ("الفيلم",        "Kodak Portra 400 + رقمي ثنائي"),
                ("المدّة",        "مارس 2023 — يوليو 2024"),
                ("الطباعة",       "مجلّد Quodlibet · 24 × 28 سم · 168 صفحة"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1543248939-4296e1fea89b?w=1600&q=85&auto=format&fit=crop",
                 "صورة 04",
                 "Masseria San Giovanni · Otranto · ربيع 2023"),
                ("https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=1600&q=85&auto=format&fit=crop",
                 "صورة 12",
                 "Trullo dei Cento Giganti · Locorotondo · صيف 2023"),
                ("https://images.unsplash.com/photo-1512100356356-de1b84283e18?w=1600&q=85&auto=format&fit=crop",
                 "صورة 22",
                 "Masseria Pulicchia · Galatina · خريف 2023"),
                ("https://images.unsplash.com/photo-1518131672697-613becd4fab5?w=1600&q=85&auto=format&fit=crop",
                 "صورة 31",
                 "Lamia داخلية · Sannicola · يناير 2024"),
                ("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=85&auto=format&fit=crop",
                 "صورة 41",
                 "مشهد الجدار الجاف · Specchia · مارس 2024"),
                ("https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1600&q=85&auto=format&fit=crop",
                 "صورة 53",
                 "فناء داخلي · Tricase · يوليو 2024"),
            ],
            "sections": [
                {
                    "label": "السلسلة",
                    "heading": "أربعون مبنى، ستّة عشر شهراً",
                    "body":
                        "يوثِّق الريبورتاج أربعين مبنى من "
                        "حجر جافّ في Salento الجنوبي — "
                        "مزارع، ولاميات، وتروللي صغيرة، "
                        "وبيوت رعي. كانت الفكرة توثيقها "
                        "قبل أيّ ترميم محتمل أو هدم، "
                        "بالتعاون مع Centro Studi Salentini "
                        "في Lecce. ستّة عشر شهراً من العمل، "
                        "وتسع رحلات، واثنتان وستّون صورة مختارة.",
                },
                {
                    "label": "المنهج",
                    "heading": "مقاس مزدوج للتوثيق",
                    "body":
                        "خلافاً للأعمال الشخصية، اشتغلت "
                        "هنا بمقاس مزدوج — Mamiya 7II "
                        "للخارج على فيلم، وSony α7R V "
                        "للداخل رقمياً (للتوثيق المعماري "
                        "الدقيق). يتعايش المقاسان في مجلّد "
                        "Quodlibet دون تمييز تحريري ظاهر — "
                        "الفيلم والرقمي، حين يُعالَجان في "
                        "الطباعة، يصيران متعذِّرَي التمييز "
                        "على 24 × 28 سم.",
                },
                {
                    "label": "المجلّد",
                    "heading": "مئة وثمان وستّون صفحة، Quodlibet",
                    "body":
                        "صدر المجلّد المونوغرافي «بيوت الحجر» "
                        "عن Quodlibet (نوفمبر 2024) "
                        "مع مقالة نقدية بقلم Salvatore Settis. "
                        "مئة وثمان وستّون صفحة، بمقاس "
                        "24 × 28 سم، وتجليد خياطي، "
                        "وورق Munken Pure غير المطلي بوزن "
                        "130 g/m². سحب 1.500 نسخة، "
                        "والطبعة الأولى نفدت في ثلاثة أشهر. "
                        "اختير العمل في القائمة القصيرة "
                        "لجائزة World Press Photo 2024 "
                        "في فئة المشاريع طويلة الأمد.",
                },
            ],
            "next_label": "السلسلة التالية",
        },
        {
            "slug":        "ritratti-del-po",
            "title":       "بورتريهات نهر Po",
            "category":    "بورتريه مؤلِّف",
            "discipline":  "بورتريه مؤلِّف",
            "year":        "2023",
            "duration":    "8 أشهر · 7 رحلات",
            "location":    "دلتا Po · Veneto · إيطاليا",
            "frame_count": "28 صورة",
            "edition":     "نُشر · Vogue Italia photography",
            "print_meta": [
                ("السحب",        "8 + 2 AP لكلّ طبعة مختارة"),
                ("الطباعة",       "سحوبات شخصية · مطبخ Milano"),
                ("الورق",         "Ilford Multigrade FB Classic"),
                ("التمثيل",       "Galleria Carla Sozzani · Milano"),
            ],
            "lead":
                "ثمانية وعشرون بورتريهاً لصيّادي السمك، "
                "وصيّادات المحار، وسائقي الصنادل في دلتا "
                "Po بـVeneto. ثمانية أشهر من العمل بين "
                "ربيع وخريف 2023، نُشرت في قسم Photography "
                "من Vogue Italia (ديسمبر 2023) وعُرضت في "
                "المهرجان الدولي في Ferrara (أكتوبر 2023).",
            "cover_image":
                "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("الكاميرا",      "Mamiya 7II · 80mm"),
                ("الفيلم",        "Kodak Portra 400 متوسط المقاس"),
                ("المدّة",        "أبريل — نوفمبر 2023"),
                ("الطباعة",       "سحوبات شخصية · مطبخ Milano"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=1600&q=85&auto=format&fit=crop",
                 "صورة 01",
                 "Aldo · صيّاد · Pila · مايو 2023"),
                ("https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=1600&q=85&auto=format&fit=crop",
                 "صورة 06",
                 "Maria · صيّادة محار · Goro · يونيو 2023"),
                ("https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=1600&q=85&auto=format&fit=crop",
                 "صورة 12",
                 "Carlo وGiuseppe · أخوان صيّادان · يوليو 2023"),
                ("https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=1600&q=85&auto=format&fit=crop",
                 "صورة 17",
                 "Anna · صاحبة مطعم · سبتمبر 2023"),
                ("https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=1600&q=85&auto=format&fit=crop",
                 "صورة 22",
                 "Luca · سائق صندل · أكتوبر 2023"),
                ("https://images.unsplash.com/photo-1521252659862-eec69941b071?w=1600&q=85&auto=format&fit=crop",
                 "صورة 28",
                 "بورتريه أخير · نوفمبر 2023 · الضوء الأخير"),
            ],
            "sections": [
                {
                    "label": "السلسلة",
                    "heading": "ثمانية وعشرون شخصاً، ثمانية أشهر",
                    "body":
                        "سلسلة من ثمانية وعشرين بورتريهاً "
                        "لمن يعيش دلتا Po في Veneto مكاناً "
                        "للعمل — صيّادون، وصيّادات محار، "
                        "وأصحاب مطاعم، وسائقو صنادل. "
                        "ثمانية أشهر من العمل بين أبريل "
                        "ونوفمبر 2023، وسبع رحلات في "
                        "المقاطعتَين (Rovigo + Ferrara). "
                        "يسبق كلّ بورتريه يومٌ واحد على "
                        "الأقلّ أُمضيه مع الشخص — لا "
                        "جلسات «عابرة» أبداً.",
                },
                {
                    "label": "المنهج",
                    "heading": "كاميرا واحدة، إضاءة واحدة",
                    "body":
                        "نُفِّذت البورتريهات كلّها بـMamiya "
                        "7II وعدسة ثمانين ملم، في ضوء "
                        "طبيعي متاح — دون فلاش، ودون "
                        "لوحات عاكسة. الفيلم دائماً Kodak "
                        "Portra 400، مُحمَّض في البيت. "
                        "اختيار عدسة واحدة (بدل حقيبة من "
                        "ثلاث أو أربع) انضباطٌ شكلي — "
                        "يُلزم بالحركة في علاقة الشخص، "
                        "لا بإدارة حلقة العدسة.",
                },
                {
                    "label": "النشر",
                    "heading": "Vogue Italia · مهرجان Ferrara",
                    "body":
                        "نُشرت السلسلة في قسم Photography "
                        "من Vogue Italia (ديسمبر 2023، "
                        "ستّ صفحات) وعُرضت في معرض جماعي "
                        "بالمهرجان الدولي في Ferrara "
                        "(أكتوبر 2023، اثنتا عشرة طبعة "
                        "مختارة). دخلت طبعة واحدة "
                        "المجموعة الدائمة لـMAXXI في Roma.",
                },
            ],
            "next_label": "السلسلة التالية",
        },
    ],
}
