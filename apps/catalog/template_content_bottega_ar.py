"""Bottega — Shop Artigianale (artisan-workshop archetype) — AR content tree.

Phase 2g3.5 — eCommerce live rollout (Session 41, 2026-04-14).

Voice contract (AR — Arabic editorial cultural register):
- Pan-MENA cultural-publishing voice in the register of Brownbook,
  Bait Al-Hikma و Sharjah Art Foundation publications. Native Modern
  Standard Arabic, classical syntax, warm artisan tone. NEVER
  marketing-speak, NEVER Egyptian colloquialism.
- Arabic vocabulary signals: ورشة · حِرَفي · يدوي · إصدار محدود ·
  كل قطعة موقعة · صَنَعَ · دبغ · خرط · نسج · طبخ بطيء. Warm, tactile,
  workshop-first.
- Latin verbatim (NEVER transliterated): artisan names (Severino Falchi,
  Caterina Lippi, Bruno Ricci, Adele Pignatelli, Martino Boncompagni,
  Anna Boncompagni), brand "La Bottega di Martino", city names (Santa
  Croce sull'Arno, Montelupo Fiorentino, Prato, Greve in Chianti,
  Firenze, Toscana, Pratovecchio), magazine names (Vogue Italia,
  Domus, La Repubblica, Apartamento, Cereal Magazine), edition numbers
  (N° 042, 3 / 8), prices (€ 420), phone (+39 055 234 11 90), years
  (1968, 1989), WhatsApp. Western Arabic digits (0-9), NOT Eastern
  (٠١٢٣٤٥٦٧٨٩). This is the MENA business-press convention.
- Arabic punctuation (، ؛ ؟) for natural flow. HTML <em>…</em>
  preserved verbatim for RTL italic renderer.

Differentiation contract vs Luxe AR (D-054 enforcement):
- Bottega AR is warm cultural-publishing register (think Brownbook,
  Bait Al-Hikma, Sharjah Art Foundation). Luxe AR is formal
  MSA boardroom Vogue-grade register (mayison, couture, private
  viewings). Vocabularies MUST NOT overlap.
- Bottega vocabulary: ورشة · حِرَفي · قطعة فريدة · إصدار محدود ·
  جلد مدبوغ نباتياً · مخروط · منسوج · توقيع باليد.
- AVOIDED Luxe vocabulary: مايسون · مجموعة · خاص جداً · لِستة الانتظار ·
  عرض خاص · سجادة حمراء · كوتير.
"""
from __future__ import annotations

from typing import Any


BOTTEGA_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "الورشة",   "kind": "home"},
        {"slug": "shop",     "label": "الكتالوج", "kind": "shop"},
        {"slug": "product",  "label": "القطعة",   "kind": "product"},
        {"slug": "atelier",  "label": "الورشة",   "kind": "about"},
        {"slug": "journal",  "label": "الدفتر",   "kind": "journal"},
        {"slug": "contatti", "label": "التواصل",  "kind": "contact"},
    ],

    # Site-wide chrome (consumed by _base.html nav + footer).
    "site": {
        "logo_initial": "M",
        "logo_word":    "La Bottega di Martino",
        "tag":          "Firenze · منذ 1968 · صُنِعَ باليد",
        "phone":        "+39 055 234 11 90",
        "whatsapp":     "055 234 11 90",
        "whatsapp_link": "https://wa.me/390552341190",
        "email":        "bottega@bottegadimartino.it",
        "address":      "Via dei Serragli 47/r · 50124 Firenze",
        "hours_compact": "الثلاثاء – السبت · 10:00 – 19:30",
        "hours_footer_rows": [
            "الأحد · بموعد مسبق فقط",
            "الإثنين · مغلق",
        ],
        "license":      "P.IVA 04891240484 · CCIAA Firenze REA 502118",
        "footer_intro":
            "ورشة حِرَفية أسّسها Martino Boncompagni عام 1968. "
            "جلد وخزف ومنسوجات تُصنع يدوياً في Toscana، ضمن إصدارات صغيرة لا تتكرّر. "
            "الشحن خلال 48 ساعة داخل إيطاليا، ويومان إضافيّان في باقي أوروبا.",
        # Nav CTA — primary action button next to nav links
        "nav_cta":      "زُر الورشة",
        "nav_cta_kind": "appointment",  # links to /contatti/

        # Marketplace footer chrome labels
        "foot_studio":   "الورشة",
        "foot_pages":    "خريطة الموقع",
        "foot_contact":  "الورشة والطلبات",
        "foot_stockists":"نقاط بيع مختارة",
        "stockists_rows": [
            "10 Corso Como · Milano",
            "Eataly Lingotto · Torino",
            "Spazio B**K · Milano",
            "Atelier Pitti · Firenze",
        ],

        # Cross-page meta-strip labels (D-047 lifts on shop/product/atelier)
        "currency_symbol":  "€",
        "shop_filter_label": "التصفية",
        "shop_count_unit":   "قطعة",
        "edition_label":     "الإصدار",
        "made_in_label":     "صُنِعَ في",
        "artisan_label":     "بتوقيع",
        "material_label":    "الخامة",
        "shipping_label":    "الشحن",
        "shipping_value":    "48 ساعة داخل إيطاليا · 4 أيام في أوروبا",
        "guarantee_label":   "الضمان",
        "guarantee_value":   "إصلاح مجاني لمدّة سنتين",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "كتالوج الخريف · الإصدار 47",
        "headline": "قطع فريدة تُخاط وتُخرَط وتُنسَج <em>في الورشة.</em>",
        "intro":
            "جلد مدبوغ نباتياً في Santa Croce sull'Arno، وخزف مخروط في Montelupo Fiorentino، "
            "وكتّان منسوج في Prato. كلّ قطعة تحمل توقيع الحِرَفي الذي صنعها، "
            "ورقماً تسلسلياً لا يتكرّر أبداً.",
        "primary_cta":   "زُر الورشة",
        "primary_href":  "contatti",
        "secondary_cta": "تصفّح الكتالوج",
        "secondary_href":"shop",

        # Stamp-aside data — the rubber-stamped right column of the hero
        "stamp_label":  "قاعدتنا",
        "stamp_heading":"ثلاث أيدٍ، <em>قطعة واحدة.</em>",
        "stamp_rows": [
            ("الحِرَفيّون",  "12 ورشة"),
            ("الخامات",     "إيطاليّة 100%"),
            ("الإصدار",     "لا يتجاوز 50 قطعة"),
            ("الشحن",       "خلال 48 ساعة"),
        ],
        "stamp_footer": "مكتوب باليد · مُغلَّف داخل الورشة",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "الورشة",

        # Latest-arrived band — 4 product cards
        "latest_label":   "آخر ما وصل",
        "latest_heading": "لتوّها خرجت <em>من طاولة العمل.</em>",
        "latest_link_label": "الكتالوج كامِلاً",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "سترة Terra",
                "meta":     "جلد مدبوغ نباتياً · Santa Croce",
                "price":    "€ 420",
                "tag":      "قطعة فريدة",
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "قميص من الكتّان",
                "meta":     "كتّان خام · Prato",
                "price":    "€ 95",
                "tag":      "صُنِعَ يدوياً",
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "طقم المطبخ",
                "meta":     "خزف مطلي · Montelupo",
                "price":    "€ 148",
                "tag":      "إصدار محدود",
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "مُحَضَّرات السوق",
                "meta":     "طماطم كرزيّة · Chianti",
                "price":    "€ 18",
                "tag":      "موسميّ",
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Makers band — 4 artisans with portrait
        "makers_label":   "أيادٍ توقّع",
        "makers_heading": "اثنتا عشرة ورشة، <em>لافتة واحدة.</em>",
        "makers_intro":
            "لا نتعامل إلّا مع حِرَفيّين نعرفهم بأسمائهم. "
            "كلّ قطعة تخرج من تحت لافتتنا تحمل توقيعهم، "
            "لأنّ من صنعها يستحقّ أن يضع وجهه إلى جانبها.",
        "makers": [
            {
                "name":   "Severino Falchi",
                "craft":  "أستاذ الدباغة",
                "place":  "Santa Croce sull'Arno",
                "since":  "في الورشة منذ 1989",
                "quote":  "«الجلد الجيّد تعرفه من رائحته. إذا فاحت منه الكيمياء، فلم نَدبُغه نحن.»",
                "portrait": "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Caterina Lippi",
                "craft":  "خرّاطة خزف",
                "place":  "Montelupo Fiorentino",
                "since":  "فتحت الورشة عام 2003",
                "quote":  "«كلّ قطعة تعود إلى الفرن ثلاث مرّات. وإن لم تُغنِّ في الثالثة، كسّرتها.»",
                "portrait": "https://images.unsplash.com/photo-1604881991720-f91add269bed?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Bruno Ricci",
                "craft":  "نسّاج كتّان",
                "place":  "Prato · Via del Telaio",
                "since":  "على النول اليدويّ منذ 1976",
                "quote":  "«الكتّان الخام نبتة. يُعامَل كالخبز: بهدوء وبجوع.»",
                "portrait": "https://images.unsplash.com/photo-1521119989659-a83eee488004?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Adele Pignatelli",
                "craft":  "مُحضِّرة مُربّيات Chianti",
                "place":  "Greve in Chianti",
                "since":  "ثلاثة أجيال من المرطبانات",
                "quote":  "«المربّى يُصنَع حين تشاء الثمرة. لا حين يقرّر الرزنامة.»",
                "portrait": "https://images.unsplash.com/photo-1607743386760-88ac62b89b8a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Provenance trio — 3 cards on materials & places
        "provenance_label":   "المنشأ",
        "provenance_heading": "ثلاثة مواطن، <em>ثلاث خامات.</em>",
        "provenance_intro":
            "لا شيء يأتي من أبعد من مئتي كيلومتر. المادّة الأوّلى هي التوقيع الأوّل "
            "للحِرَفي: إن استطاع أن يخبرك من أين جاء بها، فقد أخبرك كيف عمل عليها.",
        "provenance_items": [
            {
                "icon":  "01",
                "title": "جلد Valdarno",
                "desc":  "مدبوغ نباتياً بلحاء الكستناء والميموزا. "
                         "أربعون يوماً في الأحواض، دون كروم ودون اختصارات. "
                         "مورِّد وحيد: Conceria Falchi في Santa Croce sull'Arno.",
                "place": "Santa Croce sull'Arno · 38 كم عن Firenze",
            },
            {
                "icon":  "02",
                "title": "طين Montelupo",
                "desc":  "طين أحمر محلّي، يُطلى على البارد بأكاسيد طبيعيّة. "
                         "ثلاث طبخات عند 980° في فرن الحطب. خَرط حُرّ باليد.",
                "place": "Montelupo Fiorentino · 22 كم عن Firenze",
            },
            {
                "icon":  "03",
                "title": "كتّان Prato",
                "desc":  "كتّان خام غير مبيَّض، يُنسَج على نول آليّ من الخمسينيّات. "
                         "لُحمة واسعة وسَداة ضيّقة. كلّ لفّة لها وزن مختلف.",
                "place": "Prato · 24 كم عن Firenze",
            },
        ],

        # Care / guarantee strip
        "care_label":   "الضمانات والعناية",
        "care_heading": "يُصلَح في الورشة، <em>إلى الأبد.</em>",
        "care_items": [
            ("إصلاح مجاني لمدّة سنتين",
             "مِقبض مفكوك، طلاء متكسِّر، تطريز مُرتخٍ: نُصلحها نحن، داخل الورشة."),
            ("الإرجاع مقبول خلال سبعة أيّام",
             "إن لم تُقنعك القطعة، أعدناها إلى الورشة دون رسوم ودون أسئلة."),
            ("الشحن خلال 48 ساعة",
             "نشحن من Firenze في اليوم التالي للطلب، داخل علبة ورق سميك وخيط قنّب."),
            ("دفع آمن",
             "بطاقة أو حوالة مصرفيّة. لا اشتراكات ولا حسابات ولا ملفّات تعقّب إعلاني."),
        ],

        # Press / stockists strip
        "press_label":   "كُتِبَ عنّا",
        "press_items":   ["Vogue Italia", "Domus", "La Repubblica", "Apartamento", "Cereal Magazine"],

        "journal_teaser_label":   "من الدفتر",
        "journal_teaser_heading": "ملاحظات عمل، <em>مكتوبة باليد.</em>",
        "journal_teaser_link":    "افتح الدفتر",
        "journal_teaser_href":    "journal",

        # Final CTA band
        "cta_label":   "زُر الورشة",
        "cta_heading": "تعالَ إلينا في Firenze، <em>ونُعِدّ لك قهوة.</em>",
        "cta_intro":
            "الورشة في Via dei Serragli، على بُعد خطوات من Pitti. مفتوحة من الثلاثاء إلى "
            "السبت، من العاشرة صباحاً حتّى السابعة والنصف مساءً. نُريك كيف يُدبَغ الجلد، "
            "وكيف يُخرَط الصحن، وإن شئتَ قدّمناك إلى الحِرَفيّين شخصيّاً.",
        "cta_primary":   "احجز زيارة",
        "cta_primary_href": "contatti",
        "cta_secondary": "اكتب لنا على WhatsApp",
        # cta_secondary_href is rendered as site.whatsapp_link
    },

    # ─── SHOP ─────────────────────────────────────────────────
    "shop": {
        "eyebrow":  "الكتالوج · الإصدار 47",
        "headline": "طاولة العمل <em>كاملةً،</em> مفتوحة.",
        "intro":
            "سبع وأربعون قطعة فريدة، واثنا عشر حِرَفيّاً، وثلاثة مواطن. "
            "كلّ رقم تسلسليّ منذ 1968 ولا يتكرّر أبداً. صَفِّ الكتالوج حسب "
            "الخامة، أو الحِرَفي، أو التوفّر.",

        "filter_section_label": "صَفِّ حسب",
        "filter_groups": [
            {
                "label": "الخامة",
                "options": ["جلد", "خزف", "كتّان ومنسوجات", "مُحَضَّرات", "ورق وتجليد"],
            },
            {
                "label": "الحِرَفي",
                "options": ["Severino Falchi", "Caterina Lippi", "Bruno Ricci", "Adele Pignatelli", "الجميع"],
            },
            {
                "label": "التوفّر",
                "options": ["في الورشة", "بطلب مسبق", "إصدار نَفِد"],
            },
        ],

        "sort_label": "رتِّب حسب",
        "sort_options": ["آخر ما وصل", "الرقم التسلسليّ", "السعر تصاعديّاً", "السعر تنازليّاً"],

        "result_count":    "47 قطعة حاليّاً في الكتالوج",
        "result_subtitle": "يُحدَّث صباح الإثنين، قبل افتتاح الورشة",

        "products": [
            {
                "id":       "giubbotto-terra",
                "n":        "N° 042",
                "edition":  "3 / 8",
                "name":     "سترة Terra",
                "meta":     "جلد مدبوغ نباتياً ومصبوغ باليد",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 420",
                "tag":      "قطعة فريدة",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "borsa-cartolina",
                "n":        "N° 056",
                "edition":  "2 / 12",
                "name":     "حقيبة Cartolina",
                "meta":     "جلد طبيعيّ وخياطة سَرج",
                "place":    "Santa Croce sull'Arno",
                "artisan":  "Severino Falchi",
                "price":    "€ 280",
                "tag":      "قطعة فريدة",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "camicia-lino",
                "n":        "N° 108",
                "edition":  "1 / 6",
                "name":     "قميص من الكتّان",
                "meta":     "كتّان خام غير مبيَّض",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 95",
                "tag":      "صُنِعَ يدوياً",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tovaglia-armaiolo",
                "n":        "N° 134",
                "edition":  "5 / 30",
                "name":     "مفرش Armaiolo",
                "meta":     "كتّان وقطن · لُحمة واسعة",
                "place":    "Prato",
                "artisan":  "Bruno Ricci",
                "price":    "€ 165",
                "tag":      "إصدار محدود",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "ceramica-cucina",
                "n":        "N° 213",
                "edition":  "7 / 24",
                "name":     "طقم المطبخ",
                "meta":     "خزف مطليّ على البارد",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 148",
                "tag":      "إصدار محدود",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "tazze-tornite",
                "n":        "N° 219",
                "edition":  "11 / 24",
                "name":     "أكواب مخروطة",
                "meta":     "طين أحمر محلّي · طَبخ بالحطب",
                "place":    "Montelupo Fiorentino",
                "artisan":  "Caterina Lippi",
                "price":    "€ 78",
                "tag":      "إصدار محدود",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "vassoio-noce",
                "n":        "N° 251",
                "edition":  "نَفِد",
                "name":     "صينيّة من خشب الجوز",
                "meta":     "جوز صُلب · تشطيب بالزيت",
                "place":    "Pratovecchio",
                "artisan":  "Severino Falchi",
                "price":    "€ 210",
                "tag":      "قائمة الانتظار",
                "available": False,
                "image":    "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "conserve-chianti",
                "n":        "N° 317",
                "edition":  "12 / 60",
                "name":     "مُحَضَّرات السوق",
                "meta":     "طماطم قلب الثور + زيت زيتون بِكر ممتاز",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 18",
                "tag":      "موسميّ",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":       "marmellata-fichi",
                "n":        "N° 322",
                "edition":  "21 / 80",
                "name":     "مربّى التين",
                "meta":     "تين أسود من سبتمبر · طَبخ بطيء",
                "place":    "Greve in Chianti",
                "artisan":  "Adele Pignatelli",
                "price":    "€ 14",
                "tag":      "موسميّ",
                "available": True,
                "image":    "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=900&q=80&auto=format&fit=crop",
            },
        ],

        # Featured product detail link — used by smoke and "see more"
        "featured_product_id": "giubbotto-terra",

        "footer_note_label": "الورشة",
        "footer_note":
            "لا خوارزميّات ولا توصيات: الكتالوج مرتَّب كما على رفوف الورشة تماماً. "
            "إن كنت تبحث عن قطعة بعينها، اكتب لنا على WhatsApp — نُجيبك نحن، "
            "شخصاً واحداً في كلّ مرّة.",
    },

    # ─── PRODUCT (detail) ─────────────────────────────────────
    "product": {
        # Hero (uses featured_product_id from shop)
        "id":       "giubbotto-terra",
        "n":        "N° 042",
        "edition":  "3 / 8",
        "edition_note": "إصدار من ثماني قطع · بقيت ثلاث",
        "name":     "سترة Terra",
        "subtitle": "جلد مدبوغ نباتياً · خياطة سَرج · صبغ يدويّ",
        "price":    "€ 420",
        "vat_note": "شامل الضريبة · الشحن خلال 48 ساعة داخل إيطاليا",
        "intro":
            "سترة قصيرة من جلد Valdarno، مدبوغة نباتياً طوال أربعين يوماً "
            "بلحاء الكستناء والميموزا. تُصبَغ باليد بقطعة من الكتّان مُشبَعة "
            "بصِبغة طبيعيّة من تراب Siena: كلّ قطعة تأخذ اللون على نحو مختلف قليلاً، "
            "ولا اثنتان تتطابقان.",

        "gallery": [
            "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=1200&q=80&auto=format&fit=crop",
        ],

        # Right-side info aside (the rubber-stamped data block)
        "info_label":  "المواصفات",
        "info_rows": [
            ("الخامة",      "جلد Valdarno · دباغة نباتيّة"),
            ("السُّمك",      "1,8 مم منتظم"),
            ("الصبغة",      "تراب Siena · صِبغة طبيعيّة"),
            ("الخياطة",     "غُرزة السَّرج، خيط مشمَّع"),
            ("البطانة",     "كتّان خام غير مبيَّض"),
            ("الأزرار",     "قرن ثَور · منشؤه Toscana"),
            ("الوزن",       "780 غ (مقاس M)"),
            ("مدّة الصنع",  "11 يوماً في الورشة"),
        ],

        # Sizing card
        "size_label":    "المقاسات المتوفّرة",
        "size_intro":    "الخياطة حسب القياس ممكنة خلال ثلاثة أسابيع. اكتب لنا على WhatsApp.",
        "size_options":  ["S", "M", "L", "XL", "حسب القياس"],
        "size_chart_link": "اطّلع على دليل المقاسات",
        "size_chart_href": "atelier",

        # Made by
        "artisan_label": "بتوقيع",
        "artisan_name":  "Severino Falchi",
        "artisan_role":  "أستاذ الدباغة · في الورشة منذ 1989",
        "artisan_bio":
            "يدبغ Severino الجلد في حوضه منذ 1989. يعمل مع ابنَيه وحفيد، "
            "ويصبغ كلّ جلدة بيده. شعاره في المدبغة: «الهُوَينى أفضل».",
        "artisan_portrait":
            "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=400&q=80&auto=format&fit=crop",

        # Buy band
        "buy_primary":   "أضف إلى السلّة",
        "buy_secondary": "اكتب لنا على WhatsApp",
        "buy_note":
            "بطاقة أو حوالة مصرفيّة أو دفع عند التسليم إن استلمتَها من الورشة. "
            "نشحن خلال 48 ساعة، داخل علبة ورق سميك وخيط قنّب.",

        # Care
        "care_label":   "العناية بالقطعة",
        "care_intro":
            "الجلد المدبوغ نباتياً قليل المطالب، طويل العمر. عالجناه في المدبغة "
            "بزيت بذر الكتّان الخام. في الأشهر الأولى سيتغيّر اللون قليلاً، فيفتَحّ "
            "عند الطيّات — وهذا طبيعيّ ومقصود.",
        "care_items": [
            ("التنظيف",    "قطعة قماش جافّة. لا مواد منظّفة، ولا كحول."),
            ("الترطيب",    "زيت بذر الكتّان أو كريم محايد مرّةً في السنة."),
            ("الإصلاح",    "نقوم به مجّاناً في الورشة لمدّة سنتين."),
            ("المطر",      "يُجفَّف بعيداً عن مصادر الحرارة. لا مُجفِّف شعر."),
        ],

        # Provenance map
        "provenance_label":   "المنشأ",
        "provenance_heading": "ثلاث محطّات، <em>أربعون كيلومتراً.</em>",
        "provenance_steps": [
            ("01", "المدبغة",    "Conceria Falchi · Santa Croce sull'Arno · 38 كم"),
            ("02", "الصباغة",    "Bottega di Martino · Firenze · 0 كم"),
            ("03", "الخياطة",    "Bottega di Martino · Firenze · 0 كم"),
            ("04", "التغليف",    "ورق خبز من Greve in Chianti · 32 كم"),
        ],

        # Related products band
        "related_label":   "من اليد نفسها أيضاً",
        "related_intro":   "قطع وُلدت في الورشة ذاتها، بالتوقيع نفسه.",
        "related_items": [
            {
                "id":      "borsa-cartolina",
                "n":       "N° 056",
                "name":    "حقيبة Cartolina",
                "meta":    "جلد طبيعيّ · Severino Falchi",
                "price":   "€ 280",
                "image":   "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "vassoio-noce",
                "n":       "N° 251",
                "name":    "صينيّة من خشب الجوز",
                "meta":    "جوز صُلب · Severino Falchi",
                "price":   "€ 210",
                "image":   "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=900&q=80&auto=format&fit=crop",
            },
            {
                "id":      "ceramica-cucina",
                "n":       "N° 213",
                "name":    "طقم المطبخ",
                "meta":    "خزف مطليّ · Caterina Lippi",
                "price":   "€ 148",
                "image":   "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=900&q=80&auto=format&fit=crop",
            },
        ],
    },

    # ─── ATELIER (about) ──────────────────────────────────────
    "atelier": {
        "eyebrow":  "الورشة في Via dei Serragli",
        "headline": "ورشة <em>داخل ورشة.</em>",
        "intro":
            "افتُتحت عام 1968 على يد Martino Boncompagni، وهي اليوم فضاء من مئة وعشرة أمتار مربّعة "
            "في Via dei Serragli، حيث يُحضِر اثنا عشر حِرَفيّاً توسكانيّاً قطعهم ثلاث مرّات في "
            "الأسبوع. لا مستودع مركزيّاً، ولا سلسلة — كلّ ما تراه في الواجهة صُنِعَ "
            "على بُعد أقلّ من مئتي كيلومتر من هنا.",

        # Mission stamp panel
        "mission_label":   "قاعدة الورشة",
        "mission_heading": "ثلاث أيدٍ، قطعة واحدة. <em>دائماً.</em>",
        "mission_text":
            "كلّ قطعة تمرّ بين ثلاث أيدٍ: اليد التي تُعالج الخامة، واليد التي تُنهيها، "
            "واليد التي تتحقّق من أنّ الرقم التسلسليّ مكتوب بالقلم قبل الشحن. "
            "لا آلة تحلّ محلّ التوقيع الأخير. إن لم نستطع تمرير قطعة بين ثلاث أيدٍ، "
            "لا نصنعها.",

        # Process timeline — 5 steps
        "process_label":   "الدرب",
        "process_heading": "من الخامة الأوّلى <em>إلى خيط القنّب.</em>",
        "process_steps": [
            {
                "n":    "01",
                "title":"نذهب لجلب الخامة",
                "place":"Valdarno · Mugello · Chianti",
                "desc": "جلد من مدابغ Valdarno، وطين أحمر من Montelupo، "
                        "وكتّان من أنوال Prato. نذهب شخصيّاً، ولا نعتمد على شركات النقل.",
                "duration": "أسبوع واحد كلّ شهر",
            },
            {
                "n":    "02",
                "title":"ندع الخامة ترتاح",
                "place":"الورشة · الغرفة الخلفيّة",
                "desc": "يبقى الجلد في الحوض أربعين يوماً. يجفّ الطين ببطء في الهواء. "
                        "ينتظر الكتّان حتّى يتبدّل الطقس. لا دورات مُعجَّلة.",
                "duration": "من أسبوعين إلى ثلاثة أشهر",
            },
            {
                "n":    "03",
                "title":"نعمل باليد",
                "place":"طاولة العمل · النافذة المطلّة على الحديقة",
                "desc": "تتشكّل القطعة تحت أيدي الحِرَفي الرئيسيّ. "
                        "خياطة سَرج، وخَرط حرّ، ونَول آليّ من الخمسينيّات.",
                "duration": "من أربعة إلى اثني عشر يوماً",
            },
            {
                "n":    "04",
                "title":"نُنهي التشطيب",
                "place":"الورشة · طاولة Anna",
                "desc": "تفحص Anna، وتصقل، وتصبغ. وتضيف الرقم التسلسليّ. "
                        "إن لم تَعبُر القطعة فحصَها، تعود إلى الطاولة الرئيسيّة.",
                "duration": "نصف يوم لكلّ قطعة",
            },
            {
                "n":    "05",
                "title":"نُغلِّف",
                "place":"الورشة · طاولة التغليف",
                "desc": "ورق خبز من Greve، وخيط قنّب، وبطاقة مكتوبة باليد "
                        "باسم من صنع القطعة. نشحن من Firenze خلال 48 ساعة.",
                "duration": "اليوم ذاته للشحن",
            },
        ],

        # Founder
        "founder_label":   "مَن نحن",
        "founder_heading": "Martino و Anna، <em>واثنتا عشرة ورشة.</em>",
        "founder_text":
            "افتتح Martino الورشة عام 68 بطاولة من ثلاثة أمتار وبالة من الجلد. يُدير الورشة اليوم "
            "مع حفيدته Anna — هو يُلازم الطاولة أكثر، وهي ترعى من يدخل، ومن يتّصل، ومن "
            "يكتب. يحافظان معاً على العلاقة مع الحِرَفيّين الاثني عشر. دون أن يتحوّلا إلى "
            "شركة يوماً.",
        "founder_portrait":
            "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=600&q=80&auto=format&fit=crop",
        "founder_caption":
            "Martino Boncompagni و Anna Boncompagni · الورشة في Via dei Serragli، Firenze",

        # Numbers stamp
        "numbers_label":   "أرقام الورشة",
        "numbers_items": [
            ("57",     "عاماً من الانفتاح المتواصل"),
            ("12",     "حِرَفيّاً يوقّعون معنا"),
            ("47ª",    "الإصدار السابع والأربعون من الكتالوج"),
            ("0",      "آلة صناعيّة"),
        ],

        # Visit card
        "visit_label":   "تعالَ إلينا",
        "visit_heading": "Via dei Serragli 47/r، <em>على بُعد خطوات من Pitti.</em>",
        "visit_text":
            "الورشة مفتوحة من الثلاثاء إلى السبت، من العاشرة صباحاً حتّى السابعة والنصف مساءً. الأحد "
            "بموعد مسبق فقط. إن جئتَ عصر الخميس، عادةً ما يكون أحد الحِرَفيّين في الورشة لتسليم "
            "قطعه. القهوة وسجلّ الضيوف جاهزان.",
        "visit_primary":   "احجز زيارة",
        "visit_primary_href": "contatti",
        "visit_secondary": "اكتب لنا على WhatsApp",
    },

    # ─── JOURNAL ──────────────────────────────────────────────
    "journal": {
        "eyebrow":  "دفتر الورشة",
        "headline": "ملاحظات عمل، <em>مكتوبة بالقلم.</em>",
        "intro":
            "صفحة واحدة في الشهر، تكتبها Anna في بعد الظهيرة الهادئ. تتحدّث عن "
            "من جاء لزيارتنا، عن خامة جديدة وصلت، عن قطعة استغرقت ضعف الوقت المعتاد. "
            "ليس مدوّنة: هو يوميّات الورشة.",

        "list_label":  "ملاحظات حديثة",
        "entries": [
            {
                "n":      "47",
                "title":  "خريف من الصِبغات الطبيعيّة",
                "place":  "الورشة · 12 مارس 2026",
                "excerpt":
                    "عاد Severino من المدبغة بستّ جلدات مصبوغة بلحاء الكستناء وحده. "
                    "هي أصلاً صِبغة الدفعة المقبلة من سترة Terra.",
                "minutes":"3 دقائق قراءة",
            },
            {
                "n":      "46",
                "title":  "Caterina والفرن الذي يُغنّي",
                "place":  "Montelupo · 22 فبراير 2026",
                "excerpt":
                    "أعادت Caterina بناء فرن الحطب في ورشتها. كانت الطبخة الأولى "
                    "ستّ قطع، وكلّها غنّت عند التبريد. بِشارة طيّبة.",
                "minutes":"4 دقائق قراءة",
            },
            {
                "n":      "45",
                "title":  "نَول Bruno يعود إلى الطَّرْق",
                "place":  "Prato · 31 يناير 2026",
                "excerpt":
                    "ظلّ متوقّفاً شهرين لتبديل المُشط. استأنف Bruno النسج يوم الإثنين. "
                    "كانت أوّل قطعة مفرشاً من الكتّان بلون الرمال.",
                "minutes":"5 دقائق قراءة",
            },
            {
                "n":      "44",
                "title":  "Adele في سوق Greve",
                "place":  "Chianti · 14 ديسمبر 2025",
                "excerpt":
                    "ذهبت Adele إلى سوق ديسمبر لجلب التين المتأخّر. مربّيات يناير "
                    "كلّها من هذا المحصول.",
                "minutes":"3 دقائق قراءة",
            },
            {
                "n":      "43",
                "title":  "يوم في المدبغة",
                "place":  "Santa Croce · 8 نوفمبر 2025",
                "excerpt":
                    "قضت Anna يوماً كاملاً عند Severino. رأت كيف تدخل الجلدة إلى الحوض، "
                    "وتُقلَّب كلّ أربعة أيّام، وبعد أربعين يوماً تخرج مختلفة.",
                "minutes":"6 دقائق قراءة",
            },
            {
                "n":      "42",
                "title":  "مُحَضَّرات وكُتب وأيادٍ جديدة",
                "place":  "Firenze · 19 أكتوبر 2025",
                "excerpt":
                    "منذ أكتوبر يعمل حِرَفيّان جديدان للورشة: مُجلِّد كتب من Pistoia "
                    "وصانعة ورق من San Frediano. إصدارات قادمة في الربيع.",
                "minutes":"4 دقائق قراءة",
            },
        ],

        "footer_note_label": "الدفتر",
        "footer_note":
            "الصفحات القديمة تبقى، لا نُحدِّثها. إن أحببتَ أن يصلك الدفتر "
            "بالبريد، اكتب لنا رسالة — نُرسله إليك مطبوعاً مرّتين في السنة.",
    },

    # ─── CONTATTI (form) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "تعالَ إلينا",
        "headline": "اكتب أو اتّصل، <em>أو مُرّ بنا.</em>",
        "intro":
            "الورشة في Via dei Serragli، على بُعد خطوات من Pitti. مفتوحة من الثلاثاء إلى "
            "السبت، من العاشرة صباحاً حتّى السابعة والنصف مساءً. إن أردتَ أن تعرف ما إذا كانت قطعة "
            "لا تزال في الواجهة، اكتب لنا على WhatsApp — نُجيبك خلال ساعة.",

        # Two-column layout: left form, right contact card
        "form_section_label": "اكتب لنا سطرَين",
        "form_section_intro":
            "يكفي الاسم ووسيلة الاتّصال وما تبحث عنه. تردّ Anna خلال يوم العمل التالي. "
            "إن كنت تطلب قطعة حسب القياس، فاكتبها هنا: "
            "نُعيد إليك رسماً بالمواعيد والأسعار خلال ثلاثة أيّام.",

        # Form helper
        "form_helper_required":  "الحقول ذات العلامة النجميّة إلزاميّة",
        "form_submit_button":    "أرسل الطلب",
        "form_submit_note":      "لا نشرة بريديّة. نستخدم سطورك للردّ عليك فقط.",

        "form_fields": [
            {"name": "nome",          "label": "الاسم واللقب",          "type": "text",     "placeholder": "مثلاً: Maria Rossi", "required": True},
            {"name": "email",         "label": "البريد الإلكترونيّ",    "type": "email",    "placeholder": "maria@esempio.it", "required": True},
            {"name": "telefono",      "label": "هاتف أو WhatsApp",      "type": "tel",      "placeholder": "اختياريّ · +39 …", "required": False},
            {"name": "interesse",     "label": "ما يُهمّك",             "type": "select",   "required": True,
             "options": ["قطعة من الكتالوج", "طلب حسب القياس", "زيارة إلى الورشة", "تعاون", "صحافة وإعلام"]},
            {"name": "pezzo",         "label": "القطعة أو رقمها (اختياريّ)", "type": "text", "placeholder": "مثلاً: N° 042 · سترة Terra", "required": False},
            {"name": "messaggio",     "label": "طلبك",                  "type": "textarea", "placeholder": "أخبِرنا عمّا تبحث عنه، حتّى سطران يكفيان.", "required": True, "rows": 5},
        ],

        # Right-side card
        "card_label":   "Bottega di Martino",
        "card_address_label":  "العنوان",
        "card_address_value":  "Via dei Serragli 47/r · 50124 Firenze",
        "card_phone_label":    "الهاتف",
        "card_phone_value":    "+39 055 234 11 90",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "055 234 11 90",
        "card_email_label":    "البريد الإلكترونيّ",
        "card_email_value":    "bottega@bottegadimartino.it",
        "card_hours_label":    "ساعات العمل",
        "card_hours_rows": [
            "الثلاثاء – السبت · 10:00 – 19:30",
            "الأحد · بموعد مسبق فقط",
            "الإثنين · مغلق",
        ],
        "card_directions_label": "كيف تصل",
        "card_directions_text":
            "ثلاث دقائق مشياً من Palazzo Pitti. حافلة 11، محطّة Serragli. "
            "من محطّة SMN: خمس عشرة دقيقة مشياً عبر الوسط.",

        # FAQ accordion
        "faq_label":   "أسئلة متكرِّرة",
        "faq_items": [
            {
                "q": "هل تشحنون إلى الخارج؟",
                "a": "نعم، إلى كلّ أنحاء أوروبا خلال أربعة أيّام عمل. "
                     "للولايات المتّحدة واليابان، اكتب لنا أوّلاً — نُؤكّد المواعيد حالةً بحالة.",
            },
            {
                "q": "هل يمكنني رؤية القطعة قبل شرائها؟",
                "a": "بالتأكيد. احتفظ بها جانباً باتّصال هاتفيّ بالورشة، وحين تمرّ "
                     "نُريك إيّاها دون أيّ التزام. إن لم تُقنعك، فلا ضغط إطلاقاً.",
            },
            {
                "q": "هل تصنعون قطعاً حسب القياس؟",
                "a": "نعم، في الجلد والخزف والنسيج. المواعيد: من ثلاثة إلى ثمانية أسابيع "
                     "حسب القطعة. عربون بثلاثين في المئة عند تأكيد الرسم.",
            },
            {
                "q": "ماذا يحدث إن تعطّلت القطعة؟",
                "a": "لمدّة سنتين نُصلحها في الورشة دون رسوم. بعد ذلك، نطبّق تكلفة رمزيّة "
                     "— أقلّ من ثلاثين يورو في الغالب.",
            },
        ],
    },
}
