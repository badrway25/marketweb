"""Luxe — Fashion Store (fashion-editorial archetype) — Arabic content tree.

Phase 2g3.5 / Session 41 — eCommerce live i18n rollout.

Voice contract (ar):
- Modern Standard Arabic (الفصحى المعاصرة) in the register of Vogue Arabia
  editorial, Marie Claire Arabia fashion features, Asharq al-Awsat fashion
  section, Brownbook luxury profiles. Formal maison cadence, italic-thinking
  editorial prose, never colloquial, never warm-conversational.
- Maison-luxury vocabulary: مايسون · مجموعة · إطلالة · كبسولة · أتيلييه ·
  لوكبوك · زيارة خاصة · بموعد مسبق · قائمة الانتظار · مكتب العناية
  بالعميلات. AVOID artisan register (ورشة/حِرَفي/يدوي/إصدار محدود) — that
  belongs to Bottega.
- Italic `<em>` tags preserved verbatim inside translated headlines.

Latin-isolation policy (mandatory — mirrors MENA luxury press convention):
- ALL proper names, place names, brand names, magazine titles, designer
  names, season codes (SS26, Drop 02, Look 11, Issue 12), prices (€ 2.480),
  phone numbers (+39 02 7600 1492), emails, addresses, and year markers
  (2014, 2026) remain in Latin script with Western digits.
- Page slugs stay Italian (URL-canonical); only `label` fields become Arabic.
- Arabic punctuation: ، ؛ ؟ « » used throughout; Western digits in Arabic
  body prose where numerals are meaningful counts (12, 45, 9, 3).

Differentiation contract vs Bottega AR (D-054):
- Luxe AR = formal maison luxury register, editorial, appointment-driven.
- Bottega AR = warm cultural-publishing register, narrative, hand-led.
- Vocabularies MUST NOT overlap on the artisan axis.
"""
from __future__ import annotations

from typing import Any


LUXE_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "المايسون",      "kind": "home"},
        {"slug": "collezione", "label": "المجموعة",      "kind": "collection"},
        {"slug": "product",    "label": "الإطلالة",       "kind": "product"},
        {"slug": "maison",     "label": "الأتيلييه",     "kind": "about"},
        {"slug": "lookbook",   "label": "اللوكبوك",      "kind": "lookbook"},
        {"slug": "contatti",   "label": "خاص",           "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "L",
        "logo_word":    "Maison Luxe",
        "logo_subline": "Milano · Paris · Tokyo",
        "tag":          "Atelier · Spring–Summer 2026",
        "phone":        "+39 02 7600 1492",
        "private_phone_label": "مكتب العناية بالعميلات",
        "email":        "private@maisonluxe.com",
        "private_email_label": "كونسيرج العميلات",
        "address":      "Via Senato 28 · 20121 Milano",
        "showroom_paris": "9 rue du Mail · 75002 Paris",
        "showroom_tokyo": "1-1-7 Aoyama · Minato-ku · Tokyo",
        "hours_compact": "الثلاثاء – السبت · 11:00 – 19:00 · بموعد مسبق",
        "hours_footer_rows": [
            "الأحد · استقبال خاص",
            "الاثنين · مُغلق",
        ],
        "license":      "Maison Luxe Srl · P.IVA 11489720152 · CCIAA Milano REA 2589441",
        "footer_intro":
            "مايسون تأسّست في Milano عام 2014 على يد Giulia Maison، مع أتيلييه في Paris "
            "وصالون في Tokyo. قِطَعٌ تُرسم وتُخاط بين Milano وParis، في سلاسل محدودة العدد، "
            "ولا تُقدَّم إلا لقائمة الانتظار. الإطلاق كلّ ستّة أشهر بخمس وأربعين قطعة "
            "وتسع صيحات موقَّعة.",

        # Nav reservation CTA (private viewing)
        "nav_cta":      "اطلبي زيارة خاصة",
        "nav_cta_kind": "appointment",

        # Marketplace footer chrome labels
        "foot_studio":   "عن المايسون",
        "foot_pages":    "الأقسام",
        "foot_contact":  "مكتب العناية بالعميلات",
        "foot_offices":  "الأتيلييه والصالون",
        "office_rows": [
            "Milano · Via Senato 28",
            "Paris · 9 rue du Mail",
            "Tokyo · 1-1-7 Aoyama",
        ],

        # Cross-page meta-strip labels (D-047)
        "currency_symbol":  "€",
        "collection_label": "المجموعة",
        "drop_label":       "Drop",
        "season_label":     "الموسم",
        "shipping_label":   "تسليم خاص",
        "shipping_value":   "خدمة توصيل المايسون Milano · 24 ساعة داخل إيطاليا · 72 ساعة في أوروبا",
        "viewing_label":    "زيارة خاصة",
        "viewing_value":    "بموعد مسبق حصرياً · كونسيرج مخصَّص",
        "waitlist_label":   "قائمة الانتظار",
        "rsvp_label":       "RSVP",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "issue":    "Issue 12 · Spring '26",
        "issue_label": "Issue",
        "cover_styling_label": "التنسيق",
        "cover_styling_name":  "Carla Sozzani",
        "cover_label":         "الغلاف",
        "cover_subject":       "La Muse en Velours",
        "cover_image":
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1600&q=80&auto=format&fit=crop",

        "eyebrow":  "اللوكبوك · Spring–Summer 2026",
        "headline": "الجسد الجديد <em>للِّباس.</em>",
        "headline_credit_line": "خمسون قطعة · تسعون لمسة خياطة",
        "intro":
            "مجموعة واحدة، نُسِجَت بين Como وPrato، وصُوِّرت في Grand Hôtel Villa d'Este. "
            "إطلاقات شهرية، مخصَّصة حصرياً لمن هنّ على قائمة الانتظار. لا تبيع المايسون "
            "القطعة الواحدة مرّتين أبداً.",

        "primary_cta":   "ادخلي إلى اللوكبوك",
        "primary_href":  "lookbook",
        "secondary_label":   "الإدارة الإبداعية",
        "secondary_name":    "Giulia Maison",

        # Editorial tile strip — 4 silhouettes pinned below hero
        "edition_label":   "إصدار مقصور",
        "edition_subline": "أربع قطع مختارة",
        "tiles": [
            {
                "id":       "rack-atelier",
                "tag":      "جديد",
                "name":     "Rack Atelier",
                "price":    "€ 2.480",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "tag":      "كبسولة",
                "name":     "Bomber Siena",
                "price":    "€ 1.290",
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pelletteria-isola",
                "tag":      "أتيلييه",
                "name":     "Borsa Isola",
                "price":    "€ 860",
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "tag":      "أرشيف",
                "name":     "Sessione Vogue",
                "price":    "€ 1.940",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Manifesto / maison statement
        "manifesto_label":   "بيان المايسون",
        "manifesto_heading": "خمس وأربعون قطعة <em>في الموسم، لا واحدة أكثر.</em>",
        "manifesto_text":
            "نرسم المجموعة مرّتين في العام، في أتيلييه يمتدّ على مائة وأربعين متراً مربّعاً بين "
            "Brera وSentier. تُقَصّ كلّ قطعة باليد، وتُخاط على مقاس العميلة، وتوقِّعها من صنعتها. "
            "لا منافذ تنصيف، ولا تخفيضات، ولا علامات معادة البيع. لا شيء سوى ما خرج من "
            "المايسون.",

        # Atelier numbers — KPI strip
        "atelier_numbers_label":   "الأتيلييه بالأرقام",
        "atelier_numbers": [
            ("12",     "عاماً من عمر المايسون"),
            ("45",     "قطعة في الموسم"),
            ("9",      "صيحات موقَّعة"),
            ("3",      "أتيلييه حول العالم"),
        ],

        # Lookbook teaser — editorial 3-tile
        "lookbook_teaser_label":   "اللوكبوك الحالي",
        "lookbook_teaser_heading": "ثماني عشرة صورة، <em>ضوءٌ واحد.</em>",
        "lookbook_teaser_intro":
            "صُوِّر في Grand Hôtel Villa d'Este على بحيرة Como، بضوء النهار الطبيعي في شهر "
            "مارس. التنسيق بإشراف Carla Sozzani، والتصوير لـLetizia Carrera، والإدارة "
            "الفنية من المايسون.",
        "lookbook_teaser_link": "تصفّحي اللوكبوك",
        "lookbook_teaser_href": "lookbook",
        "lookbook_teaser_tiles": [
            {
                "title":   "Look 03 · Cady doppio strato",
                "credit":  "التنسيق · Carla Sozzani",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 09 · Lana cardata di Biella",
                "credit":  "تصوير · Letizia Carrera",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "title":   "Look 14 · Crêpe di seta Como",
                "credit":  "أتيلييه · Sentier Paris",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        # Press / editorial mentions strip
        "press_label":   "المختارات الصحفية",
        "press_intro":   "استعراض في",
        "press_items":   ["Vogue Italia", "The Gentlewoman", "AnOther Magazine", "Le Monde D'Hermès", "Wallpaper*"],

        # Seasonal drop card
        "drop_label":    "الإطلاق القادم",
        "drop_heading":  "SS26 · Capsula 04 — <em>ضوءُ Como.</em>",
        "drop_subhead":  "افتتاح قائمة الانتظار · الجمعة 24 أبريل، الساعة 11:00 بتوقيت CET",
        "drop_metadata": [
            ("القِطع",      "9 صيحات"),
            ("الخامة",      "Crêpe di seta · cady · alpaca"),
            ("الحصرية",     "12 نسخة لكلّ صيحة"),
            ("الافتتاح",    "قائمة الانتظار · الجمعة 24 أبريل"),
        ],
        "drop_cta":      "سجِّلي في القائمة",
        "drop_cta_href": "contatti",

        # Private viewing CTA band
        "private_label":   "زيارة خاصة",
        "private_heading": "ثلاثة صالونات، <em>غرفةٌ فارغة من أجلكِ وحدكِ.</em>",
        "private_intro":
            "أبواب مايسون Milano وParis وTokyo لا تُفتح إلا بموعد مسبق. يحجز مكتب العناية "
            "بالعميلات ساعةً كاملةً من الصالون، يُعدّ لكِ القِطَع المنتقاة وفق ملفّكِ الشخصي، "
            "ويُنسِّق جلسة القياس مع الخيّاطة. خدمة مجّانية · كونسيرج مخصَّص.",
        "private_primary":     "اطلبي زيارة خاصة",
        "private_primary_href":"contatti",
        "private_secondary":   "تعرّفي على الأتيلييه",
        "private_secondary_href":"maison",
    },

    # ─── COLLEZIONE (shop list) ───────────────────────────────
    "collezione": {
        "season_chip":  "Spring–Summer 2026",
        "eyebrow":      "المجموعة الكاملة · drop 04 · capsule 01–04",
        "headline":     "خمس وأربعون قطعة، <em>تسع صيحات موقَّعة.</em>",
        "intro":
            "مجموعة Spring–Summer 2026 كاملةً، منظَّمة حسب الصيحة. كلّ قطعة متاحة حصرياً "
            "عبر قائمة الانتظار: من التأكيد إلى التسليم، أربعة إلى ستّة أسابيع.",

        "filter_label":  "تصفية",
        "filter_groups": [
            {
                "label": "الصيحة",
                "options": ["بدلة انسيابية", "Robe-manteau", "بنطلون wide", "تريكو تحريري", "جلديات الأتيلييه"],
            },
            {
                "label": "الخامة",
                "options": ["Cashmere alpaca", "Cady طبقتان", "Crêpe di seta Como", "صوف مُمشَّط Biella", "جلد Firenze"],
            },
            {
                "label": "التوافر",
                "options": ["في الصالون", "قائمة الانتظار مفتوحة", "نفدت الكمية · بالحجز"],
            },
        ],
        "sort_label":    "ترتيب",
        "sort_options":  ["حسب الصيحة", "حسب Drop", "السعر تصاعدياً", "الأحدث"],

        "result_count":     "45 قطعة في المجموعة",
        "result_subtitle":  "تُحدَّث مطلع كلّ شهر، عقب الإطلاق",

        "products": [
            {
                "id":       "robe-manteau-grigio-perla",
                "n":        "Look 03",
                "name":     "Robe-manteau Grigio Perla",
                "meta":     "Cashmere alpaca مزدوج · Maglificio Lanifer Biella",
                "drop":     "Drop 01 · Spring 26",
                "price":    "€ 2.840",
                "tag":      "قائمة الانتظار",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tailleur-cady-bianco",
                "n":        "Look 07",
                "name":     "Tailleur Cady Bianco",
                "meta":     "Cady طبقتان · Setificio Tessitura Como",
                "drop":     "Drop 02 · Spring 26",
                "price":    "€ 3.420",
                "tag":      "في الصالون",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier-nero",
                "n":        "Look 11",
                "name":     "Rack Atelier Nero",
                "meta":     "جلد nappa من Firenze · خياطة sellier",
                "drop":     "Drop 02 · Spring 26",
                "price":    "€ 2.480",
                "tag":      "قائمة الانتظار",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "bomber-siena",
                "n":        "Look 14",
                "name":     "Bomber Siena",
                "meta":     "Cady مصبوغ في Siena · تطريز Atelier Sentier",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€ 1.290",
                "tag":      "كبسولة",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "pantalone-wide-crepe",
                "n":        "Look 16",
                "name":     "Pantalone Wide Crêpe",
                "meta":     "Crêpe di seta Como · حزام sellier",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€ 1.180",
                "tag":      "قائمة الانتظار",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-isola",
                "n":        "Look 18",
                "name":     "Borsa Isola",
                "meta":     "جلد Atelier Firenze · pochette نهارية",
                "drop":     "Drop 03 · Summer 26",
                "price":    "€ 860",
                "tag":      "أتيلييه",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "abito-sera-organza",
                "n":        "Look 22",
                "name":     "Abito Sera Organza",
                "meta":     "Organza منسوج Como · تطريز Lesage",
                "drop":     "Drop 04 · Summer 26",
                "price":    "€ 4.690",
                "tag":      "نفدت الكمية · بالحجز",
                "available":False,
                "image":    "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "maglia-cashmere-corta",
                "n":        "Look 24",
                "name":     "Maglia Cashmere Corta",
                "meta":     "Cashmere 12 خيطاً · Maglificio Lanifer Biella",
                "drop":     "Drop 04 · Summer 26",
                "price":    "€ 1.420",
                "tag":      "قائمة الانتظار",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Sessione Vogue",
                "meta":     "معطف أرشيف · إعادة إصدار drop 2024",
                "drop":     "أرشيف · 2024",
                "price":    "€ 1.940",
                "tag":      "أرشيف",
                "available":True,
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],

        "featured_product_id": "rack-atelier-nero",

        "footer_note_label": "Drop 04 في الافتتاح",
        "footer_note":
            "تُفتح تسجيلات Drop 04 — كبسولة ضوء Como — يوم الجمعة 24 أبريل الساعة 11:00 "
            "بتوقيت CET. تحظى العميلات المسجَّلات سلفاً في قائمة الانتظار بالأولوية المطلقة "
            "على جميع الصيحات. للانضمام إلى القائمة: الكتابة مباشرةً إلى مكتب العناية بالعميلات.",
    },

    # ─── PRODUCT DETAIL ───────────────────────────────────────
    "product": {
        "id":       "rack-atelier-nero",
        "n":        "Look 11 · Drop 02",
        "name":     "Rack Atelier Nero",
        "subtitle": "جلد nappa من Firenze · خياطة sellier · حافة ذهبية",
        "price":    "€ 2.480",
        "vat_note": "ضريبة القيمة المضافة مُدرجة · توصيل المايسون · 24 ساعة داخل إيطاليا",
        "tag":      "قائمة الانتظار · Drop 02 SS26",
        "intro":
            "حقيبة نهار-سهرة من جلد nappa من Firenze، مخيطة باليد في أتيلييه Sentier بخياطة "
            "sellier ذهبية على ثلاث جهات. الحافة مصقولة بشمع النحل، والقاع مُعزَّز بجلد "
            "Vacchetta. صُمِّمت على قوام المديرة الإبداعية، وأُنتجت بإثنتَي عشرة نسخة مُرقَّمة، "
            "ويوقِّعها من قاعها الأتيلييه الذي صَنَعَها.",

        "gallery": [
            "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1591561954557-26941169b49e?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1400&q=80&auto=format&fit=crop",
        ],

        # Editorial caption strip below gallery
        "gallery_caption_styling":  "التنسيق · Carla Sozzani",
        "gallery_caption_photo":    "تصوير · Letizia Carrera",
        "gallery_caption_location": "Grand Hôtel Villa d'Este · مارس 2026",

        # Right-side info panel — italic captioned
        "info_label":  "تفاصيل الأتيلييه",
        "info_rows": [
            ("الأتيلييه",     "Sentier · Paris"),
            ("الخامة",        "Nappa من Firenze · دباغة نباتية"),
            ("الخياطة",       "Sellier ذهبية على ثلاث جهات · خيط مُشمَّع"),
            ("الحافة",        "شمع النحل · تلميع يدوي"),
            ("القاع",         "Vacchetta مُعزَّز · قواعد نحاسية"),
            ("الحِلى",         "نحاس مطليّ بالذهب عيار 24K"),
            ("المقاسات",      "32 × 24 × 12 سم · حِزام الكتف 105 سم"),
            ("التنفيذ",       "21 ساعة أتيلييه للقطعة الواحدة"),
        ],

        # Sizing / variant card (silhouette comes in 2 dimensions + 3 tonalities)
        "size_label":    "المقاس",
        "size_options":  ["Day · 32 × 24", "Evening · 25 × 18"],
        "color_label":   "اللون",
        "color_options": ["أسود الليل", "Bordeaux Como", "عاجي كريمي"],

        # Edition note
        "edition_label": "الإصدار",
        "edition_value": "12 نسخة مُرقَّمة · النسخة n° 03/12 متاحة",
        "edition_note":
            "كلّ نسخة تحمل وسماً بارداً على وجهها الداخلي يتضمّن الرقم التسلسلي، "
            "واسم الخيّاط الرئيس، وتاريخ التسليم من الأتيلييه.",

        # Atelier signature
        "atelier_label":   "بتوقيع الأتيلييه",
        "atelier_name":    "Atelier Sentier · Paris",
        "atelier_founded": "افتُتح عام 2017",
        "atelier_text":
            "أتيلييه للجلديات تديره المايسون مباشرةً، في rue du Mail. ستّة سيليه تدرّبوا في "
            "مدارس Hermès وGoyard، وقاطعة واحدة، ومسؤولة عن الشمع. يعملون حصرياً لصالح "
            "Maison Luxe — لا طرف ثالث، ولا إنتاج تحت علامة بيضاء.",
        "atelier_portrait":
            "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=600&q=80&auto=format&fit=crop",

        # Buy band — private request style
        "buy_primary":   "اطلبيها من المايسون",
        "buy_primary_href":  "contatti",
        "buy_secondary": "أضيفيها إلى قائمة الانتظار",
        "buy_note":
            "الشراء بموعد مسبق أو بطلب مباشر إلى مكتب العناية بالعميلات. عربون قدره ثلاثون "
            "بالمئة عند التأكيد. التسليم خلال 4–6 أسابيع من الطلب، عبر خدمة المايسون Milano "
            "في علبة موقَّعة.",

        # Care section (italic editorial style)
        "care_label":   "العناية بالقطعة",
        "care_intro":
            "جلد nappa من Firenze جلدٌ حيّ: يأخذ شكل من يحمله، ويلين في الأشهر الأولى دون "
            "أن يفقد بنيته. مُعالَج في الأتيلييه بشمع النحل المحايد، ولا يحتاج إلى صيانة "
            "في أوّل عامَين من الاستخدام اليومي.",
        "care_items": [
            ("التنظيف",      "قطعة قماش ناعمة مبلّلة قليلاً. لا مواد كيميائية أبداً."),
            ("الترطيب",      "شمع نحل المايسون كلّ اثني عشر شهراً. العلبة الملحقة مجهَّزة."),
            ("التخزين",      "كيس قطني عضوي، لا بلاستيك أبداً. ولا أشعة شمس مباشرة."),
            ("المطر",        "تجفيف طبيعي في الظلّ. ثمّ تمريرة واحدة من الشمع."),
        ],

        # Atelier provenance
        "provenance_label":   "المنشأ",
        "provenance_heading": "أربع محطّات، <em>أربعة توقيعات.</em>",
        "provenance_steps": [
            ("01", "الدباغة",            "Conceria della Madonna · Firenze · دباغة نباتية 45 يوماً"),
            ("02", "القصّ",              "Atelier Sentier · Paris · قصٌّ باليد الحرّة"),
            ("03", "خياطة Sellier",     "Atelier Sentier · Paris · 21 ساعة للقطعة"),
            ("04", "التغليف",            "Maison Milano · علبة وشريط موقَّعان"),
        ],

        # Related — three other atelier pieces
        "related_label":   "من الأتيلييه نفسه",
        "related_intro":   "جلديات بتوقيع Sentier · Paris.",
        "related_items": [
            {
                "id":      "borsa-isola",
                "n":       "Look 18",
                "name":    "Borsa Isola",
                "meta":    "Pochette نهارية · Atelier Sentier",
                "price":   "€ 860",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "rack-atelier",
                "n":        "Look 09",
                "name":     "Rack Atelier Crema",
                "meta":     "حقيبة نهار · Atelier Sentier",
                "price":    "€ 2.480",
                "image":    "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=1000&q=80&auto=format&fit=crop",
            },
            {
                "id":       "sessione-vogue",
                "n":        "Look 26",
                "name":     "Cappotto Sessione Vogue",
                "meta":     "معطف أرشيف · drop 2024",
                "price":    "€ 1.940",
                "image":    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── MAISON (about) ───────────────────────────────────────
    "maison": {
        "eyebrow":  "عن المايسون",
        "headline": "ثلاث مدن، <em>توقيعٌ واحد.</em>",
        "intro":
            "تأسّست Maison Luxe في Milano عام 2014 على يد Giulia Maison، بعد ثماني سنوات "
            "بين Hermès وBottega Veneta. تصمّم اليوم مجموعتَين في العام، في أتيلييه بين "
            "Brera وSentier، ولا تستقبل إلا بموعد مسبق في مايسون Milano وParis وTokyo. "
            "خمس وأربعون قطعة في الموسم، لا واحدة أكثر.",

        # Maison statement panel
        "statement_label":   "البيان",
        "statement_heading": "خمس وأربعون قطعة <em>في الموسم.</em>",
        "statement_text":
            "العدد قرارٌ تحريريٌّ لا قيد. يجب أن تُرسم كلّ قطعة من قِبَل المديرة الإبداعية، "
            "وتُقَصّ في الأتيلييه، وتُخيطها خيّاطة توقِّعها، وتُصوَّر للوكبوك، وتُتابَع شخصياً حتى "
            "التسليم. خمس وأربعون هو أقصى عدد يسمح لنا بإنجاز كلّ ذلك على أفضل وجه.",

        # Atelier cards — 3 cities
        "ateliers_label":   "الأتيلييه الثلاثة",
        "ateliers_heading": "Milano، Paris، <em>Tokyo.</em>",
        "ateliers_intro":
            "ثلاث دور، مايسون واحدة. Milano ترسم وتُدير. Paris تخيط وتطرّز. Tokyo تستقبل "
            "العميلة الآسيوية في صالون خاص في Aoyama.",
        "ateliers": [
            {
                "city":   "Milano",
                "place":  "Via Senato 28 · Brera",
                "role":   "أتيلييه إبداعي · إدارة · خياطة",
                "since":  "افتُتح عام 2014",
                "head":   "Giulia Maison · المديرة الإبداعية",
                "team":   "ستّ خيّاطات · قاطعتان · مسؤولة العناية بالعميلات",
                "image":  "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Paris",
                "place":  "9 rue du Mail · Sentier",
                "role":   "أتيلييه جلديات · خياطة sellier",
                "since":  "افتُتح عام 2017",
                "head":   "Jean-Luc Berthier · maître sellier",
                "team":   "ستّة سيليه · قاطعة · مسؤولة الشمع",
                "image":  "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=900&q=80&auto=format&fit=crop",
            },
            {
                "city":   "Tokyo",
                "place":  "1-1-7 Aoyama · Minato-ku",
                "role":   "صالون خاص · استقبال العميلات",
                "since":  "افتُتح عام 2021",
                "head":   "Yumi Tanaka · كونسيرج",
                "team":   "ثلاث كونسيرج · خيّاطة متنقّلة",
                "image":  "https://images.unsplash.com/photo-1559563458-527698bf5295?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Direction credit
        "direction_label":   "الإدارة الإبداعية",
        "direction_name":    "Giulia Maison",
        "direction_role":    "المديرة الإبداعية · المؤسِّسة",
        "direction_text":
            "درست Giulia Maison في Central Saint Martins في London، وعملت ثماني سنوات "
            "بين Hermès وBottega Veneta قبل أن تؤسِّس المايسون عام 2014. كتابتها إيطالية، "
            "من Brera، لكنّ يدها تقصّ بالفرنسية. المايسون هي استوديوها.",
        "direction_portrait":
            "https://images.unsplash.com/photo-1624206112918-f140f087f9b5?w=600&q=80&auto=format&fit=crop",
        "direction_quote":
            "«العدد قرار لا نتيجة. خمس وأربعون قطعة في الموسم هو الرقم الذي يتيح لنا "
            "أن ننظر في وجه كلّ عميلة.»",
        "direction_quote_attribution": "Giulia Maison · The Gentlewoman, 2025",

        # Press / editorial mentions
        "press_label":   "المختارات الصحفية",
        "press_heading": "حضورٌ صحفيٌّ <em>حديث.</em>",
        "press_items": [
            {
                "magazine": "Vogue Italia",
                "issue":    "أبريل 2026",
                "title":    "الصمت الجديد للترف الإيطالي",
                "byline":   "تحقيق · Sara Maino",
            },
            {
                "magazine": "The Gentlewoman",
                "issue":    "Spring 2025",
                "title":    "Forty-five pieces. Never one more.",
                "byline":   "بورتريه · Penny Martin",
            },
            {
                "magazine": "AnOther Magazine",
                "issue":    "AW25",
                "title":    "L'atelier de Sentier",
                "byline":   "صور · Mark Borthwick",
            },
            {
                "magazine": "Le Monde D'Hermès",
                "issue":    "Numero 84",
                "title":    "Filiation italienne",
                "byline":   "نصّ · Stefano Tonchi",
            },
            {
                "magazine": "Wallpaper*",
                "issue":    "مارس 2025",
                "title":    "Une maison bien cachée",
                "byline":   "زيارة أتيلييه · Tony Chambers",
            },
        ],

        # Numbers
        "numbers_label":   "أرقام المايسون",
        "numbers_items": [
            ("12",    "عاماً على التأسيس"),
            ("3",     "أتيلييه حول العالم"),
            ("45",    "قطعة في الموسم"),
            ("9",     "صيحات في الإطلاق"),
        ],

        # Visit card — 3 cities
        "visit_label":   "زوري المايسون",
        "visit_heading": "ثلاث دور، <em>ثلاثة صالونات خاصة.</em>",
        "visit_text":
            "أبواب مايسون Milano وParis وTokyo لا تُفتح إلا بموعد مسبق. يحجز مكتب العناية "
            "بالعميلات غرفةً، ويُعدّ القِطَع المنتقاة وفق ملفّكِ الشخصي، ويُنسِّق جلسة القياس "
            "مع الخيّاطة. خدمة مجّانية، خاصّة تماماً.",
        "visit_primary":   "اطلبي موعداً",
        "visit_primary_href": "contatti",
    },

    # ─── LOOKBOOK ─────────────────────────────────────────────
    "lookbook": {
        "issue":     "Spring–Summer 2026",
        "issue_label":"Issue",
        "issue_n":   "Issue 12",
        "eyebrow":   "اللوكبوك · Issue 12",
        "headline":  "ضوءُ <em>Como، في مارس.</em>",
        "intro":
            "ثماني عشرة صورة التُقطت خلال ثلاثة أيام من مارس في Grand Hôtel Villa d'Este، "
            "على بحيرة Como. التنسيق بإشراف Carla Sozzani، والتصوير لـLetizia Carrera، "
            "وتصميم المشهد لـSebastiano Pellion di Persano. كان ضوء الصباح الطبيعي هو "
            "أداة الإضاءة الوحيدة.",

        # Credits panel
        "credits_label":   "Credits",
        "credits_rows": [
            ("الإدارة الإبداعية", "Giulia Maison · Maison Luxe Milano"),
            ("التنسيق",           "Carla Sozzani"),
            ("التصوير",           "Letizia Carrera"),
            ("تصميم المشهد",      "Sebastiano Pellion di Persano"),
            ("الشعر والمكياج",    "Lina Hammar · Art + Commerce"),
            ("عارضة الأزياء",     "Sara Grace Wallerstedt · IMG Models"),
            ("الموقع",            "Grand Hôtel Villa d'Este · Cernobbio"),
            ("الطباعة",           "سحب تماثلي · Studio Riffraff Milano"),
        ],

        # Editorial grid — 6 looks
        "looks_label":   "الإطلالات الثمانَ عشرة",
        "looks_intro":   "ستّ منتقاة للصحافة، واثنتا عشرة في المكتبة الخاصة.",
        "looks": [
            {
                "n":       "Look 03",
                "title":   "Cady doppio strato",
                "outfit":  "Robe-manteau cady طبقتان · حذاء جلدي من Sentier",
                "credit":  "التنسيق · وشاح من أرشيف 2018",
                "image":   "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 07",
                "title":   "Tailleur Cady Bianco",
                "outfit":  "جاكيت + بنطلون wide · حذاء Atelier Sentier · pochette Isola",
                "credit":  "المشهد · حديقة الكاميليا",
                "image":   "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 09",
                "title":   "Lana cardata di Biella",
                "outfit":  "معطف ممشَّط · بنطلون crêpe · بوط sellier",
                "credit":  "معطف Maglificio Lanifer",
                "image":   "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 11",
                "title":   "Rack Atelier Nero",
                "outfit":  "تريكو cashmere قصير · بنطلون crêpe · حقيبة Atelier",
                "credit":  "حقيبة Atelier Sentier · 21 ساعة تنفيذ",
                "image":   "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 14",
                "title":   "Crêpe di seta Como",
                "outfit":  "Bomber Siena · بنطلون wide crêpe · صندل مربوط",
                "credit":  "نسيج Setificio Tessitura Como",
                "image":   "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1200&q=80&auto=format&fit=crop",
            },
            {
                "n":       "Look 18",
                "title":   "Borsa Isola · نهاراً",
                "outfit":  "تريكو ممشَّط · jeans أتيلييه · حقيبة Isola",
                "credit":  "حقيبة Atelier Sentier · جلد Madonna",
                "image":   "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1200&q=80&auto=format&fit=crop",
            },
        ],

        # Editorial pull-quote
        "pullquote":
            "«Como في مارس غرفةٌ موصدة. خرجت منها المايسون بثماني عشرة صورة تجعلها "
            "قابلةً للقراءة.»",
        "pullquote_attribution": "Carla Sozzani · منسِّقة اللوكبوك",

        # Notes from set
        "notes_label":   "ملاحظات من المشهد",
        "notes_intro":
            "ثلاثة أيام من مارس، شمسٌ محجوبة بغيم رقيق، وريحٌ من الشمال الشرقي. وقفت عارضة "
            "الأزياء دون انقطاع من السابعة حتى الحادية عشرة، في ضوء قدوم الصباح. جاكيت "
            "cady من Look 03 تطلَّب ساعتَين من الكيّ كلّ صباح ليستعيد ثنيّاته.",
        "notes_items": [
            {
                "label": "اليوم 01 · صالون الكاميليا",
                "text":  "سبع إطلالات في خمس ساعات من الضوء. تبديل الملابس بين لقطة "
                         "وأخرى في غرفة مجاورة. الغداء عند الثالثة عصراً.",
            },
            {
                "label": "اليوم 02 · شرفة البحيرة",
                "text":  "ستّ إطلالات في ضوء الصباح الأمامي. أمطار خفيفة بين الحادية "
                         "عشرة والظهيرة: أُرجئت اللقطة إلى بعد الظهر.",
            },
            {
                "label": "اليوم 03 · الصالون الخاص",
                "text":  "خمس إطلالات في ضوء الشموع والنافذة. الصور الثلاث الأخيرة "
                         "طلبتها المديرة الإبداعية لاستفتاح الاقتباس الافتتاحي.",
            },
        ],

        # Buy from lookbook CTA
        "shop_label":   "اشتري من اللوكبوك",
        "shop_heading": "كلّ إطلالة تقود <em>إلى قطعة في المجموعة.</em>",
        "shop_intro":
            "الإطلالات الثمانَ عشرة قابلة للتصفّح من المجموعة الكاملة. لطلب قطعة، يُرجى "
            "الكتابة إلى مكتب العناية بالعميلات — تُفتح قائمة الانتظار يوم الجمعة 24 أبريل.",
        "shop_primary":     "إلى المجموعة",
        "shop_primary_href":"collezione",
        "shop_secondary":   "سجِّلي في قائمة الانتظار",
        "shop_secondary_href":"contatti",
    },

    # ─── CONTATTI (private appointment form) ──────────────────
    "contatti": {
        "eyebrow":  "مكتب العناية بالعميلات · خاص",
        "headline": "بموعد <em>مسبق حصرياً.</em>",
        "intro":
            "تستقبل المايسون حصرياً بموعد مسبق، في ثلاثة صالونات خاصة في Milano وParis "
            "وTokyo. يُجهِّز مكتب العناية بالعميلات القِطَع المنتقاة وفق ملفّكِ قبل وصولكِ، "
            "ويحجز لكِ الخيّاطة لجلسة القياس. خدمة خاصّة، مجّانية، بطلب مباشر.",

        # Form intro
        "form_section_label":  "طلب خاص",
        "form_section_intro":
            "يُرجى استكمال البطاقة بتفاصيل موعدكِ أو طلبكِ. يردّ مكتب العناية بالعميلات "
            "خلال يوم العمل التالي. لقائمة انتظار Drop 04 — الافتتاح في 24 أبريل — "
            "اختاري الخيار المخصَّص.",

        "form_helper_required":  "الحقول المُعلَّمة إلزامية",
        "form_submit_button":    "أرسلي الطلب الخاص",
        "form_submit_note":
            "بياناتكِ تُعالَج حصرياً من قِبَل مكتب العناية بالعميلات. لا نشرة إخبارية، "
            "ولا اتصالات تجارية.",

        "form_fields": [
            {"name":"titolo",    "label":"اللقب",     "type":"select", "required":True,
             "options":["السيدة","السيد","Mx","Studio·Atelier","صحافة · Press"]},
            {"name":"nome",      "label":"الاسم الكامل", "type":"text", "placeholder":"مثال: السيدة Eleonora Cattaneo", "required":True},
            {"name":"email",     "label":"البريد الإلكتروني", "type":"email", "placeholder":"e.cattaneo@esempio.it",      "required":True},
            {"name":"telefono",  "label":"الهاتف",       "type":"tel",   "placeholder":"+39 …",                      "required":False},
            {"name":"city",      "label":"المايسون المعنيّة", "type":"select", "required":True,
             "options":["Milano · Via Senato","Paris · Sentier","Tokyo · Aoyama","لا فارق"]},
            {"name":"servizio",  "label":"الخدمة المطلوبة", "type":"select", "required":True,
             "options":["زيارة خاصة","قائمة انتظار Drop 04","قطعة على المقاس","إعادة إصدار من الأرشيف","صحافة · Press"]},
            {"name":"capo",      "label":"الإطلالة أو القطعة (اختياري)", "type":"text", "placeholder":"مثال: Look 11 · Rack Atelier Nero", "required":False},
            {"name":"messaggio", "label":"ملاحظات لمكتب العناية بالعميلات", "type":"textarea", "placeholder":"يُرجى تحديد التاريخ المفضَّل، والمقاسات، والملف الشخصي.", "required":True, "rows":5},
        ],

        # Right-side card — three maison addresses
        "card_label":   "المايسون الثلاث",
        "maison_cards": [
            {
                "city":    "Milano",
                "address": "Via Senato 28 · 20121 Milano",
                "phone":   "+39 02 7600 1492",
                "email":   "milano@maisonluxe.com",
                "hours":   "الثلاثاء – السبت · 11:00 – 19:00 · بموعد مسبق حصرياً",
            },
            {
                "city":    "Paris",
                "address": "9 rue du Mail · 75002 Paris",
                "phone":   "+33 1 4296 4720",
                "email":   "paris@maisonluxe.com",
                "hours":   "الثلاثاء – الجمعة · 11:00 – 19:00 · بموعد مسبق حصرياً",
            },
            {
                "city":    "Tokyo",
                "address": "1-1-7 Aoyama · Minato-ku · Tokyo 107-0062",
                "phone":   "+81 3 6450 5018",
                "email":   "tokyo@maisonluxe.com",
                "hours":   "الأربعاء – السبت · 12:00 – 20:00 · بموعد مسبق حصرياً",
            },
        ],

        # FAQ accordion (private viewing oriented)
        "faq_label":   "أسئلة متكرّرة",
        "faq_items": [
            {
                "q": "قبل كم من الوقت تُحجز الزيارة الخاصة؟",
                "a": "أسبوعٌ واحد على الأقلّ لـMilano وParis؛ أسبوعان لـTokyo. "
                     "للطلبات العاجلة، يُرجى الكتابة مباشرةً إلى مكتب العناية بالعميلات.",
            },
            {
                "q": "هل تُدفع رسوم على خدمة الزيارة الخاصة؟",
                "a": "لا، الخدمة مجّانية وخاصّة. وتشمل تجهيز القِطَع، وحضور الخيّاطة في "
                     "الصالون، والقهوة والشمبانيا، وخريطة مخصَّصة للمجموعة.",
            },
            {
                "q": "هل يمكن طلب قطعة على المقاس؟",
                "a": "نعم، استناداً إلى الصيحات القائمة. مدّة التسليم: من ثمانية إلى "
                     "اثني عشر أسبوعاً. عربون قدره خمسون بالمئة عند تأكيد التصميم.",
            },
            {
                "q": "كيف تعمل قائمة الانتظار؟",
                "a": "تحظى المسجَّلات في القائمة بالأولوية المطلقة على جميع الإطلاقات. "
                     "لا تستوجب القائمة أيّ التزامٍ بالشراء. التسجيل مجّاني، بطلب "
                     "مباشر.",
            },
        ],
    },
}
