"""Brace — Brace Street Lab (street-modern archetype) — AR content tree.

Phase 2g3.6 — Restaurant live-completion (Session 48, 2026-04-15).

Voice contract (AR — Arabic urban street-food register):
- Pan-MENA modern lifestyle voice in the register of Wamda lifestyle,
  Vice Arabia food sections, Asharq Business Lifestyle (street-food).
  Native Modern Standard Arabic, urban, fast-casual, second-person
  imperative. Short rolling sentences. NEVER warm Brownbook drift,
  NEVER classical literary register.
- Arabic vocabulary signals: نار · شواء · طابور · بار · مقلي · حيّ ·
  توصيل · سريع · حار · ليلي · على الطاير. Fast, urban, direct.
- Latin verbatim (NEVER transliterated): brand "Brace Street Lab",
  city "Bologna", street "Via Indipendenza 42", dish names
  (Margherita, Marinara, Mortadella, Tortellini), delivery brand
  names (GLOVO, DELIVEROO, JUST EAT, UBER EATS), social handles
  (@brace.lab, @brace.bologna), proper crew names (Dario Riva,
  Amina Beretta, Luka Hoxha, Sofia Martini, Tito Brama), supplier
  names (Macelleria Sarti, Forno Beretta, Ortofrutta Tosi), magazine
  names (Zero Magazine), prices (€ 9.50), phone (051 234 5566),
  hours (12:00 – 24:00). Western Arabic digits (0-9).
- Arabic punctuation (، ؛ ؟) for natural flow. HTML <em>…</em>
  preserved verbatim for RTL renderer.

Differentiation contract vs Sapore AR (trattoria-warm archetype):
- Brace AR = Wamda urban-imperative street-food register.
- Sapore AR = warm Roman trattoria cultural-publishing register.
- Vocabularies MUST NOT overlap. Brace: نار · بار · طابور · حيّ · ليلي.
  AVOIDED Sapore vocabulary: عائلة · جدّة · مائدة · تقاليد · ضيف.

Differentiation contract vs Gusto AR (fine-dining archetype):
- Brace AR = imperative urban street-food register, you (أنت), short.
- Gusto AR = formal Michelin-editorial sommelier register, plural
  formal (نحن/حضراتكم), long flowing sentences, tasting-menu poetry.
- Vocabularies MUST NOT overlap. Brace: على الطاير · ادفع · طابور.
  AVOIDED Gusto vocabulary: تذوّق · ساقي النبيذ · نجمة · حجز خاص.
"""
from __future__ import annotations

from typing import Any


BRACE_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "الرئيسية", "kind": "home"},
        {"slug": "menu",     "label": "القائمة",  "kind": "menu"},
        {"slug": "lab",      "label": "المختبر",  "kind": "about"},
        {"slug": "moments",  "label": "لحظات",    "kind": "gallery"},
        {"slug": "ordina",   "label": "اطلب",     "kind": "order"},
        {"slug": "contatti", "label": "موقعنا",   "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "B",
        "logo_word":    "BRACE STREET LAB",
        "tag":          "Bologna · Via Indipendenza 42 · 12:00 → 24:00",
        "phone":        "051 234 5566",
        "phone_tel":    "+390512345566",
        "phone_display": "051 234 5566",
        "whatsapp":     "051 234 5566",
        "whatsapp_link": "https://wa.me/390512345566",
        "email":        "ordini@bracestreetlab.it",
        "address":      "Via Indipendenza 42 · 40121 Bologna",
        "hours_compact": "كل يوم · 12:00 – 24:00 · الجمعة/السبت حتى 01:30",
        "hours_footer_rows": [
            "الإثنين – الخميس · 12:00 – 24:00",
            "الجمعة – السبت · 12:00 – 01:30",
            "الأحد · 12:00 – 24:00",
        ],
        "license":      "P.IVA 04127880371 · CCIAA Bologna REA 358912",
        "footer_intro":
            "مختبر طعام شارع في Bologna. سماشبرغر لحم Scottona من Piemonte، "
            "مقليّات تخرج من الزيت لحظتها، بيتزا بالقطعة من فرن الحطب. "
            "تطلب على البار، تستلم بالرقم، تأكل على الطاير. مفتوح حتى وقت متأخر، "
            "كل يوم، حتى الأحد.",
        "nav_cta":      "اطلب الآن",
        "nav_cta_href": "ordina",
        "nav_phone_cta": "051 234 5566",
        "star_line":    "STREET FOOD LAB · BOLOGNA",
        "copyright":    "© 2026 Brace Street Lab · رقم ضريبي 04127880371",

        # Mirror the fine-dining/_base.html footer keys used by the chrome
        "footer_hours_1": "الإثنين – الخميس · 12:00 – 24:00",
        "footer_hours_2": "الجمعة – السبت · 12:00 – 01:30",

        # Social
        "instagram_handle": "@brace.lab",
        "instagram_link":   "https://instagram.com/brace.lab",
        "tiktok_handle":    "@brace.bologna",
        "tiktok_link":      "https://tiktok.com/@brace.bologna",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "STREET FOOD LAB · BOLOGNA",
        "headline": 'مشويّ على <em>نار حيّة.</em>',
        "intro":
            "سماشبرغر لحم Scottona من Piemonte، مقليّات ضدّ التيّار، بيتزا بالقطعة "
            "من فرن الحطب. تطلب على البار، تستلم بالرقم، تأكل على الطاير.",
        "primary_cta":   "اطلب الآن",
        "primary_href":  "ordina",
        "secondary_cta": "القائمة",
        "secondary_href": "menu",

        # Hero product cutout
        "hero_image":       "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=1400&q=80&auto=format&fit=crop",
        "hero_alt":         "DOPPIO BRACE smashburger close-up",
        "hero_badge_price": "€ 9.50",
        "hero_badge_label": "DOPPIO BRACE",
        "hero_badge_tag":   "الأعلى طلباً",

        # Real-time queue counter strip
        "counter_label": "طابور البار",
        "counter_value": "≈ 4 دقائق",
        "counter_kitchen_label": "المطبخ مفتوح",
        "counter_kitchen_value": "حتى 24:00",
        "counter_last_label":    "آخر طلب",
        "counter_last_value":    "23:30",

        # Stat band — 4 numbers
        "stats_label": "أرقام المختبر",
        "stats": [
            ("12.000",  "برغر شهرياً"),
            ("4.9 ★",   "من 1.380 تقييم"),
            ("100%",    "Scottona من Piemonte"),
            ("420°C",   "فرن حطب"),
        ],

        # Menu strip — 6 product-grid items on home (teaser of full menu)
        "menu_strip_label":   "من البار الليلة",
        "menu_strip_heading": 'قائمة <em>على الطاير.</em>',
        "menu_strip_intro":
            "ستّ قطع تخرج ساخنة من الباس كلّ خمس عشرة دقيقة. "
            "أشِر، اختر، ادفع على البار، نناديك بالرقم.",
        "menu_strip_cta":      "كل القائمة",
        "menu_strip_cta_href": "menu",
        "menu_strip_items": [
            {
                "name":  "DOPPIO BRACE",
                "desc":  "Scottona مزدوجة، شيدر مذوّب، صلصة Brace",
                "price": "€ 9.50",
                "tag":   "الأعلى طلباً",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SMASH CLASSICO",
                "desc":  "Scottona مفردة، شيدر، بصل مكرمل",
                "price": "€ 7.50",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRITTO MISTO",
                "desc":  "بطاطس، Jalapeño مقلي، باكالا مقلي",
                "price": "€ 6.00",
                "tag":   "حار",
                "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "PIZZA ROSSA",
                "desc":  "طماطم San Marzano DOP، فيور دي لاتي، ريحان",
                "price": "€ 4.50",
                "tag":   "نباتي",
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "FRIES BRACE",
                "desc":  "بطاطس مقلية مرّتين، ملح خشن، صلصة Brace",
                "price": "€ 4.50",
                "tag":   "",
                "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":  "SODA BRACE",
                "desc":  "ليموناضة بيتيّة بالريحان الطازج",
                "price": "€ 3.00",
                "tag":   "جديد",
                "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Delivery partners marquee strip
        "delivery_label":    "اطلب من حيث تريد",
        "delivery_subtitle": "توصيل في 30 دقيقة · وسط Bologna",
        "delivery_partners": [
            ("GLOVO",     "30 دقيقة", "الحدّ الأدنى € 12"),
            ("DELIVEROO", "25 دقيقة", "الحدّ الأدنى € 10"),
            ("JUST EAT",  "35 دقيقة", "الحدّ الأدنى € 15"),
            ("UBER EATS", "30 دقيقة", "الحدّ الأدنى € 12"),
        ],

        # Lab manifesto — 3 short bold paragraphs
        "manifesto_label":   "المختبر",
        "manifesto_heading": 'لماذا النار. <em>لماذا السرعة.</em>',
        "manifesto_paragraphs": [
            "Brace مختبر. لا ورق جدران، لا مفارش طاولات. "
            "حديد ونار وخمسة أشخاص يعملون أمامك مئة وثمانين ثانية لكل طبق.",

            "نشتغل فقط على Scottona من Piemonte، نطحنها صباحاً بالمطحنة فوق البار. "
            "كل بطاطس تُقطَّع باليد عند العاشرة. كل صلصة تُحضَّر داخل المختبر، لا تُشترى أبداً.",

            "تعال متى شئت. مفتوحون من الثانية عشرة حتى منتصف الليل، كل يوم، حتى الأحد. "
            "السبت نشدّ حتى الواحدة والنصف. المطبخ لا يقفل قبل آخر داخل.",
        ],
        "manifesto_cta":      "اكتشف المختبر",
        "manifesto_cta_href": "lab",

        # Crew band — 3 people (chef, griller, founder)
        "crew_label":   "الفريق",
        "crew_heading": 'خمسة على البار. <em>فريق واحد.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "المؤسّس وعلى الشواية",
                "quote":  "«سماش جيّد يعني حديد ساخن، Scottona باردة، تسعون ثانية وكفى.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "صانعة البيتزا · فرن الحطب",
                "quote":  "«الفرن يطلب انتباهاً كل دقيقتين. لذلك لا أنظر إلى الهاتف.»",
                "portrait": "https://images.unsplash.com/photo-1554727242-741c14fa561c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "المقليّات والصلصات",
                "quote":  "«المايونيز على النار توقيعي. لا سرّ، فقط صبر.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Urban photo strip — 3 atmosphere shots
        "atmo_label":   "الجوّ",
        "atmo_heading": 'بار. نيون. <em>طابور.</em>',
        "atmo_strip": [
            {
                "image": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=900&q=80&auto=format&fit=crop",
                "cap":   "طابور على البار · ليلة سبت 19:40",
            },
            {
                "image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "cap":   "Late-night DJ set · آخر جمعة من كل شهر",
            },
            {
                "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "cap":   "فرن الحطب مشتعل من 11:00 حتى الإغلاق",
            },
        ],

        # Final CTA band — late-night order push
        "final_label":   "جاهز للطلب؟",
        "final_heading": 'آخر طلب <em>الساعة 23:30.</em>',
        "final_intro":
            "ثلاث طرق لتوصلك. تعال إلى البار. اتصل للتيك أواي. "
            "اطلب من شركاء التوصيل. لا تتأخّر.",
        "final_primary_cta":   "اطلب الآن",
        "final_primary_href":  "ordina",
        "final_phone_cta":     "اتصل 051 234 5566",
        "final_phone_href":    "+390512345566",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "القائمة · من البار",
        "headline": 'كل ما <em>يُشوى عندنا.</em>',
        "intro":
            "خمسة أقسام، اثنتان وعشرون قطعة، أسعار البار. أشِر بإصبعك، "
            "ادفع، نناديك بالرقم. لا رسوم خدمة، لا غطاء طاولة.",

        "sections": [
            {
                "id":    "burger",
                "label": "01",
                "title": "BURGER",
                "desc":  "Scottona من Piemonte · مطحونة صباحاً · خبز بريوش بقمح محروق",
                "items": [
                    {
                        "name":  "DOPPIO BRACE",
                        "desc":  "Scottona مزدوجة، شيدر مذوّب، صلصة Brace، بصل نيء",
                        "price": "€ 9.50",
                        "tag":   "الأعلى طلباً",
                        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "SMASH CLASSICO",
                        "desc":  "Scottona مفردة، شيدر، بصل مكرمل، صلصة البيت",
                        "price": "€ 7.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VEGGIE PATTY",
                        "desc":  "قرصة عدس وشمندر، حمّص بالليمون، جرجير",
                        "price": "€ 8.00",
                        "tag":   "نباتي",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BRACE PICCANTE",
                        "desc":  "Scottona، Jalapeño مقلي، شيدر حار، Sriracha Brace",
                        "price": "€ 9.00",
                        "tag":   "حار",
                        "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "fritti",
                "label": "02",
                "title": "FRITTI",
                "desc":  "بطاطس مقطّعة باليد عند 10:00 · قلي مزدوج · ملح Cervia",
                "items": [
                    {
                        "name":  "FRIES BRACE",
                        "desc":  "بطاطس قلي مزدوج، ملح خشن، صلصة Brace في كوب",
                        "price": "€ 4.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "FRITTO MISTO",
                        "desc":  "بطاطس، Jalapeño مغموس، باكالا مقلي، حلقات بصل",
                        "price": "€ 6.00",
                        "tag":   "حار",
                        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "JALAPEÑO POPPER",
                        "desc":  "Jalapeño محشوّ شيدر، مغموس، مقلي، صلصة لايم",
                        "price": "€ 5.50",
                        "tag":   "نباتي",
                        "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ONION RINGS",
                        "desc":  "حلقات بصل أحمر من Tropea بالتمبورا، BBQ البيت",
                        "price": "€ 5.00",
                        "tag":   "نباتي",
                        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "pizza",
                "label": "03",
                "title": "PIZZA AL TAGLIO",
                "desc":  "عجين 72 ساعة · فرن حطب 420°C · ستّون ثانية طهي",
                "items": [
                    {
                        "name":  "PIZZA ROSSA",
                        "desc":  "طماطم San Marzano DOP، فيور دي لاتي، ريحان",
                        "price": "€ 4.50",
                        "tag":   "نباتي",
                        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIANCA AL TARTUFO",
                        "desc":  "فيور دي لاتي، شرائح كمأة سوداء صيفية، زيت زيتون بكر",
                        "price": "€ 6.50",
                        "tag":   "الأعلى طلباً",
                        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "DIAVOLA NEW",
                        "desc":  "طماطم، فيور دي لاتي، سلامي حار كالابري، عسل",
                        "price": "€ 5.50",
                        "tag":   "حار",
                        "image": "https://images.unsplash.com/photo-1593504049359-74330189a345?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "MORTADELLA & PISTACCHIO",
                        "desc":  "فيور دي لاتي، Mortadella di Bologna IGP، فستق Bronte",
                        "price": "€ 6.00",
                        "tag":   "جديد",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "drink",
                "label": "04",
                "title": "SODA & BEVANDE",
                "desc":  "صودا البيت معصورة على البار · بيرات Bologna على الصنبور · نبيذ بالكأس",
                "items": [
                    {
                        "name":  "SODA BRACE",
                        "desc":  "ليموناضة بيتيّة بالريحان الطازج وزنجبيل",
                        "price": "€ 3.00",
                        "tag":   "جديد",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "ICED TEA HOUSE",
                        "desc":  "شاي مثلّج Earl Grey بعسل الكستناء وقشر ليمون",
                        "price": "€ 3.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "BIRRA SPINA",
                        "desc":  "Lager من مصنع Sant'Orsola في Bologna · 0,33 لتر",
                        "price": "€ 4.50",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "VINO AL CALICE",
                        "desc":  "Sangiovese di Romagna DOC · Cantina Ronchi di Solarolo",
                        "price": "€ 5.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
            {
                "id":    "dolci",
                "label": "05",
                "title": "DOLCI",
                "desc":  "تُصنع داخل المختبر · حصص صغيرة، تؤكل على الطاير",
                "items": [
                    {
                        "name":  "BRACE COOKIE",
                        "desc":  "كوكي كاكاو بقلب Nutella ساخن لا يزال",
                        "price": "€ 3.50",
                        "tag":   "الأعلى طلباً",
                        "image": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "GELATO ARTIGIANALE",
                        "desc":  "فيور دي بانا أو فستق · من Gelateria Stefino",
                        "price": "€ 3.00",
                        "tag":   "نباتي",
                        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80&auto=format&fit=crop",
                    },
                    {
                        "name":  "TIRAMISÙ AL VOLO",
                        "desc":  "في كوب، Mascarpone طازج، Savoiardi، قهوة Bologna",
                        "price": "€ 4.00",
                        "tag":   "",
                        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&q=80&auto=format&fit=crop",
                    },
                ],
            },
        ],

        # Allergen line at bottom
        "allergen_label": "مسبّبات الحساسية",
        "allergen_text":
            "تُطبخ كل الأطباق في بيئة تحتوي على غلوتين، ألبان، بيض، صويا، مكسّرات. "
            "للحساسية الشديدة كلّم البار قبل الطلب. القائمة الكاملة لمسبّبات الحساسية "
            "متوفّرة على البار.",

        # Producer band — 3 producer names with city
        "producers_label":   "الموردون",
        "producers_heading": 'من أين تأتي <em>كل قطعة.</em>',
        "producers_intro":
            "نعمل مع ثلاثة موردين تاريخيين من المدينة. كل منتج موقّع، "
            "متتبَّع، يصلنا في دفعات أسبوعية صغيرة.",
        "producers": [
            {
                "name":   "MACELLERIA SARTI",
                "city":   "BOLOGNA · VIA PETRONI",
                "role":   "Scottona من Piemonte، تُطحن طازجة كل صباح عند السابعة.",
            },
            {
                "name":   "FORNO BERETTA",
                "city":   "MODENA · CASTELFRANCO",
                "role":   "خبز بريوش بقمح محروق وعجين بيتزا 72 ساعة.",
            },
            {
                "name":   "ORTOFRUTTA TOSI",
                "city":   "BOLOGNA · MERCATO ALBANI",
                "role":   "بطاطس، بصل أحمر من Tropea، Jalapeño مزروع في صوبة.",
            },
        ],

        # Final CTA
        "final_label":         "اطلب فوراً",
        "final_heading":       'أشِر. <em>ادفع. استلم.</em>',
        "final_primary_cta":   "اطلب الآن",
        "final_primary_href":  "ordina",
        "final_secondary_cta": "موقعنا",
        "final_secondary_href": "contatti",
    },

    # ─── LAB (about) ─────────────────────────────────────────────
    "lab": {
        "eyebrow":  "المختبر",
        "headline": 'لماذا النار. <em>لماذا السرعة.</em>',
        "intro":
            "Brace مختبر مفتوح كل يوم من الثانية عشرة حتى منتصف الليل. "
            "خمسة أشخاص، بار، فرنان. لا أكثر، لا أقل.",

        # Big atmosphere photo
        "hero_image":   "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "البار مفتوح · فرن حطب على 420°C · كل خدمة تبدأ هنا",

        # Manifesto — 4 short bold paragraphs
        "manifesto_label":   "المانيفستو",
        "manifesto_paragraphs": [
            {
                "title": "01 العجين",
                "text":  "خميرة أمّ تُجدَّد كل اثنتي عشرة ساعة. دقيق Tipo 1 مطحون "
                         "بالحجر من Forno Beretta في Castelfranco. اثنتان وسبعون ساعة "
                         "تخمير بطيء في الخزانة، لا أقل. البيتزا تُحَسّ بالأصابع قبل الفم.",
            },
            {
                "title": "02 النار",
                "text":  "فرن الحطب يحرق فقط بلوط Cimino، لا غيره. يصل إلى 420°C "
                         "في خمس وثلاثين دقيقة. صفيحة الشواية تصل إلى 280°C: "
                         "Scottona من Piemonte توضع، تُكبَس بالحديد، تسعون ثانية لكل وجه.",
            },
            {
                "title": "03 المادة",
                "text":  "فقط Scottona من Piemonte من Macelleria Sarti، تُطحن فوق البار "
                         "كل صباح عند السابعة. بطاطس Tosi تُقطَّع باليد عند العاشرة. "
                         "طماطم San Marzano DOP من Agro Sarnese. كل شيء موقّع، كل شيء متتبَّع.",
            },
            {
                "title": "04 السرعة",
                "text":  "ثلاث دقائق من البار إلى الباس. أربع عشرة ثانية لقلب السماش. "
                         "ستّون ثانية للبيتزا. مئة وثمانون ثانية كاملة للخدمة. "
                         "سرعة نعم، لكن مصنوع كما يجب.",
            },
        ],

        # Process strip — 3-step
        "process_label":   "العملية",
        "process_heading": "ثلاث حركات. <em>لا غير.</em>",
        "process": [
            {
                "num":   "01",
                "title": "العجين",
                "desc":  "كل ليلة عند 23:00، تخمير 72 ساعة في خزانة 4°C",
            },
            {
                "num":   "02",
                "title": "النار",
                "desc":  "الفرن مشتعل عند 11:00، الصفيحة على 280°C من 12:00",
            },
            {
                "num":   "03",
                "title": "الخدمة",
                "desc":  "ثلاث دقائق من البار إلى الباس، نناديك بالرقم",
            },
        ],

        # Crew band — 4 people
        "crew_label":   "الفريق كاملاً",
        "crew_heading": 'خمسة على البار. <em>فريق واحد.</em>',
        "crew": [
            {
                "name":   "DARIO RIVA",
                "role":   "المؤسّس وعلى الشواية",
                "quote":  "«سماش جيّد يعني حديد ساخن، Scottona باردة، تسعون ثانية وكفى.»",
                "portrait": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "AMINA BERETTA",
                "role":   "صانعة البيتزا · فرن الحطب",
                "quote":  "«الفرن يطلب انتباهاً كل دقيقتين. لذلك لا أنظر إلى الهاتف.»",
                "portrait": "https://images.unsplash.com/photo-1554727242-741c14fa561c?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "LUKA HOXHA",
                "role":   "المقليّات والصلصات",
                "quote":  "«المايونيز على النار توقيعي. لا سرّ، فقط صبر.»",
                "portrait": "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "SOFIA MARTINI",
                "role":   "البار والورديات",
                "quote":  "«أناديك باسمك إذا أتيت مرّتين من قبل. هذه قاعدة البيت.»",
                "portrait": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Values grid — 4 cards
        "values_label":   "القيم",
        "values_heading": 'أربعة بنود <em>غير قابلة للتفاوض.</em>',
        "values": [
            {"title": "الوقت",        "tag": "صفر انتظار",     "desc": "ثلاث دقائق من البار إلى الباس، دائماً"},
            {"title": "الحرارة",      "tag": "420°C / 280°C",  "desc": "فرن وصفيحة تحت السيطرة على المرأى، لا أقل"},
            {"title": "الجودة",       "tag": "100% Piemonte",  "desc": "Scottona موقّعة، متتبَّعة، مطحونة صباحاً"},
            {"title": "الطاقة",       "tag": "كل يوم",          "desc": "مفتوحون من 12 حتى منتصف الليل، حتى الأحد"},
        ],

        # Kitchen energy band
        "kitchen_label":   "الورقة التقنية",
        "kitchen_heading": 'أرقام <em>المطبخ.</em>',
        "kitchen_specs": [
            ("210°C", "صفيحة السماش"),
            ("420°C", "فرن الحطب"),
            ("14 ث", "قلبة السماش"),
            ("90 ث", "طهي البيتزا"),
            ("3 د", "البار إلى الباس"),
            ("72 س", "تخمير"),
        ],

        # Final CTA
        "final_label":   "تعال شاهده",
        "final_heading": 'المختبر <em>مفتوح دائماً.</em>',
        "final_intro":
            "مفتوحون من الثانية عشرة حتى منتصف الليل، كل يوم. تعال متى شئت، "
            "أشِر بإصبعك، ادفع على البار. لا حجوزات، لا غطاء طاولة.",
        "final_primary_cta":   "القائمة",
        "final_primary_href":  "menu",
        "final_secondary_cta": "موقعنا",
        "final_secondary_href": "contatti",
    },

    # ─── MOMENTS (gallery) ───────────────────────────────────────
    "moments": {
        "eyebrow":  "MOMENTS · يوميّات الشارع",
        "headline": 'كل ليلة <em>لحظة.</em>',
        "intro":
            "اليوميّات المصوّرة لـ Brace. طابور البار، Late-night DJ، "
            "زيت يقفز، فريق على العمل. كل صورة من هنا، عندنا.",

        # Category pills
        "categories_label": "تصفية",
        "categories_all_label": "الكل",
        "categories": [
            "DJ NIGHTS",
            "طابور البار",
            "ليلي",
            "لحظات قلي",
            "الفريق",
            "الافتتاح",
        ],

        # 6-image grid
        "grid": [
            {
                "image":    "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-001",
                "cap":      "طابور البار · سبت 23:14 · ثمانون شخصاً في Via Indipendenza",
                "tag":      "طابور البار",
            },
            {
                "image":    "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-002",
                "cap":      "DJ Tito Brama · last friday set · فينيل فقط حتى 02:00",
                "tag":      "DJ NIGHTS",
            },
            {
                "image":    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-003",
                "cap":      "فرن الحطب · 420°C · الساعة الحادية عشرة من الخدمة",
                "tag":      "ليلي",
            },
            {
                "image":    "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-004",
                "cap":      "بطاطس قلي مزدوج · ملح Cervia · جاهزة في ثلاثمئة ثانية",
                "tag":      "لحظات قلي",
            },
            {
                "image":    "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-005",
                "cap":      "Luka على الباس · جمعة 20:34 · سابع غطاء في الليلة",
                "tag":      "الفريق",
            },
            {
                "image":    "https://images.unsplash.com/photo-1567521464027-f127ff144326?w=900&q=80&auto=format&fit=crop",
                "filename": "MO-006",
                "cap":      "الافتتاح · 13 مارس 2024 · أوّل دخول إلى البار عند 12:01",
                "tag":      "الافتتاح",
            },
        ],

        # Featured shot with quote overlay
        "featured_image": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1600&q=80&auto=format&fit=crop",
        "featured_quote": "«Brace هو المكان الذي تذهب إليه إذا أردت أن تأكل جيّداً وبسرعة، ولا أحد يسألك عن مهنتك.»",
        "featured_author": "ZERO MAGAZINE · BOLOGNA · مارس 2025",
        "featured_filename": "MO-FEAT-002",

        # End CTA
        "final_label":     "شاهد كل الباقي",
        "final_heading":   'تابعنا <em>على السوشيال.</em>',
        "final_intro":
            "كل يوم قصّة جديدة، كل جمعة Drop الأسبوع. "
            "على Instagram تجد اليوميّات، على TikTok كيف نشتغل خلف البار.",
        "final_instagram_cta": "INSTAGRAM @brace.lab",
        "final_tiktok_cta":    "TIKTOK @brace.bologna",
    },

    # ─── ORDINA ──────────────────────────────────────────────────
    "ordina": {
        "eyebrow":  "اطلب على الطاير",
        "headline": 'ثلاث طرق. <em>طبق واحد.</em>',
        "intro":
            "تعال إلى البار، اتصل للتيك أواي، اطلب من شركاء التوصيل. "
            "نناديك بالرقم حين يكون جاهزاً، لا قبلها أبداً.",

        # Counter-status band
        "counter_status_label":  "حالة البار",
        "counter_queue_label":   "طابور البار",
        "counter_queue_value":   "≈ 4 دقائق",
        "counter_kitchen_label": "المطبخ مفتوح",
        "counter_kitchen_value": "حتى 24:00",
        "counter_last_label":    "آخر طلب",
        "counter_last_value":    "23:30",

        # 3-route grid — counter / takeaway / delivery
        "routes_label":   "ثلاثة مسارات",
        "routes_heading": 'اختر <em>كيف تطلب.</em>',
        "routes": [
            {
                "id":      "01",
                "title":   "على البار",
                "subtitle": "تعال وأشِر",
                "desc":
                    "Via Indipendenza 42, Bologna. أشِر بإصبعك على القائمة، ادفع على "
                    "البار، نناديك بالرقم حين يكون جاهزاً. لا حجوزات، لا غطاء، لا "
                    "رسوم خدمة. ثلاث دقائق من الباس إلى الطبق.",
                "lines": [
                    ("العنوان",     "Via Indipendenza 42, Bologna"),
                    ("طابور تقريبي", "≈ 4 دقائق"),
                    ("الأوقات",      "12:00 – 24:00 · كل يوم"),
                ],
                "cta_label": "افتح الخريطة",
                "cta_href":  "https://www.openstreetmap.org/?mlat=44.4949&mlon=11.3426#map=17/44.4949/11.3426",
                "cta_kind":  "external",
            },
            {
                "id":      "02",
                "title":   "TAKEAWAY",
                "subtitle": "اتصل واستلم",
                "desc":
                    "اتصل بالبار، قل لنا ماذا تريد، نعطيك وقت استلام. "
                    "جاهز في اثنتي عشرة دقيقة، دائماً. تدفع عند الاستلام، نقداً أو "
                    "بالبطاقة. WhatsApp إن فضّلت الكتابة.",
                "lines": [
                    ("الهاتف",    "051 234 5566"),
                    ("WhatsApp",  "اكتب إلى 051 234 5566"),
                    ("جاهز خلال", "12 دقيقة"),
                ],
                "cta_label": "اتصل الآن",
                "cta_href":  "+390512345566",
                "cta_kind":  "tel",
            },
            {
                "id":      "03",
                "title":   "DELIVERY",
                "subtitle": "توصيل إلى البيت",
                "desc":
                    "أربعة شركاء توصيل، كلّهم في وسط Bologna. الحدّ الأدنى للطلب "
                    "عشرة يورو، توصيل في ثلاثين دقيقة، مجّاني فوق العشرين يورو. "
                    "افتح تطبيق الشريك الذي تستخدمه أكثر.",
                "lines": [
                    ("الشركاء",          "GLOVO · DELIVEROO · JUST EAT · UBER EATS"),
                    ("المنطقة",          "وسط Bologna · نطاق 4 كم"),
                    ("الحدّ الأدنى للطلب", "€ 10"),
                ],
                "cta_label": "شاهد الشركاء",
                "cta_href":  "#partners",
                "cta_kind":  "anchor",
            },
        ],

        # Delivery partners detail
        "partners_label":   "شركاء التوصيل",
        "partners_heading": 'توصيل في <em>30 دقيقة.</em>',
        "partners": [
            {"name": "GLOVO",     "eta": "30 دقيقة", "min": "الحدّ الأدنى € 12", "zone": "وسط Bologna · 4 كم"},
            {"name": "DELIVEROO", "eta": "25 دقيقة", "min": "الحدّ الأدنى € 10", "zone": "وسط Bologna · 3 كم"},
            {"name": "JUST EAT",  "eta": "35 دقيقة", "min": "الحدّ الأدنى € 15", "zone": "Bologna · 6 كم"},
            {"name": "UBER EATS", "eta": "30 دقيقة", "min": "الحدّ الأدنى € 12", "zone": "وسط Bologna · 5 كم"},
        ],

        # Late-night opening hours table
        "hours_label":   "متى نحن مفتوحون",
        "hours_heading": 'حتى يوم <em>الأحد.</em>',
        "hours_rows": [
            ("الإثنين", "12:00 – 24:00"),
            ("الثلاثاء", "12:00 – 24:00"),
            ("الأربعاء", "12:00 – 24:00"),
            ("الخميس",   "12:00 – 24:00"),
            ("الجمعة",   "12:00 – 01:30"),
            ("السبت",    "12:00 – 01:30"),
            ("الأحد",    "12:00 – 24:00"),
        ],
        "hours_note":
            "آخر طلب دائماً قبل الإغلاق بثلاثين دقيقة. المطبخ يقفل مبكّراً فقط إذا "
            "نفد عجين البيتزا، أبداً قبل منتصف الليل.",

        # Allergen note
        "allergen_label": "مسبّبات الحساسية",
        "allergen_text":
            "تُطبخ كل الأطباق في بيئة تحتوي على غلوتين، ألبان، بيض، صويا، مكسّرات. "
            "للحساسية الشديدة كلّم البار قبل الطلب أو اكتب لنا على WhatsApp.",

        # Big phone CTA band
        "phone_label":   "جاهزون الآن",
        "phone_heading": 'اتصل بنا <em>على البار.</em>',
        "phone_intro":
            "نردّ في ثلاث رنّات، حتى أثناء الخدمة. إذا لم نردّ، "
            "فنحن نقلب سماش. أعد المحاولة بعد ثلاثين ثانية.",
        "phone_cta_label": "اتصل 051 234 5566",
        "phone_cta_href":  "+390512345566",

        # FAQ accordion — 4 questions
        "faq_label":   "الأسئلة الشائعة",
        "faq_heading": 'أمور <em>يسألوننا عنها كثيراً.</em>',
        "faq": [
            {
                "q": "هل لديكم خيارات GLUTEN FREE؟",
                "a": "خبز بريوش Gluten Free عند الطلب، نطلب منك ثلاثين دقيقة "
                     "إضافية انتظار. أعلِم البار قبل الطلب. البطاطس واللحم "
                     "والصلصات بطبيعتها Gluten Free، لكنها تُطبخ في البيئة "
                     "نفسها — للحساسية الشديدة كلّم البار.",
            },
            {
                "q": "هل تأخذون حجوزات للمجموعات؟",
                "a": "لا طاولات محجوزة، لا حجوزات. للمجموعات فوق اثني عشر شخصاً "
                     "اكتب لنا على WhatsApp قبل يومين: نقول لك إن كنّا نقدر أن "
                     "ننظّم وقتاً أقل ازدحاماً (عادةً ثلاثاء/أربعاء عند 19:00).",
            },
            {
                "q": "هل لديكم خيارات نباتية وفيغان؟",
                "a": "نعم، دائماً ثلاثة خيارات نباتية: Veggie patty عدس، Pizza rossa، "
                     "Fries Brace. الخيارات الفيغان (دون ألبان) تتبدّل كل أسبوع — "
                     "اسأل البار ماذا يوجد اليوم.",
            },
            {
                "q": "هل تقدّمون كاترينغ أو فعاليات خاصة؟",
                "a": "نعم، من عشرين إلى ستّين شخصاً. Smashburger، Pizza al taglio، "
                     "مقليّات، صودا البيت. فرن متنقّل للفعاليات في Bologna والإقليم. "
                     "اكتب إلى eventi@bracestreetlab.it بالتاريخ والمكان وعدد الأشخاص — "
                     "نردّ خلال 24 ساعة بعرض سعر.",
            },
        ],
    },

    # ─── CONTATTI ────────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "موقعنا · BOLOGNA",
        "headline": 'Via Indipendenza <em>42.</em>',
        "intro":
            "وسط Bologna، خطوتان من Due Torri. مفتوحون كل يوم، حتى الأحد، "
            "حتى وقت متأخّر من الليل. تعال مشياً إن استطعت.",

        # Address card
        "address_label": "العنوان",
        "address_value": "Via Indipendenza 42 · 40121 Bologna",
        "address_note":  "بين Piazza Maggiore والمحطّة · منطقة مشاة",

        # Map iframe
        "map_lat":   "44.4949",
        "map_lon":   "11.3426",
        "map_zoom":  "16",
        "map_label": "خريطة OpenStreetMap · Via Indipendenza 42, Bologna",

        # Contact channels grid
        "channels_label": "كلّم البار",
        "channels": [
            {
                "icon":  "phone",
                "label": "الهاتف",
                "value": "051 234 5566",
                "note":  "نردّ في ثلاث رنّات، حتى أثناء الخدمة",
                "href":  "+390512345566",
                "kind":  "tel",
            },
            {
                "icon":  "whatsapp",
                "label": "WHATSAPP",
                "value": "051 234 5566",
                "note":  "اكتب إن فضّلت، نردّ خلال 30 دقيقة",
                "href":  "https://wa.me/390512345566",
                "kind":  "external",
            },
            {
                "icon":  "email",
                "label": "EMAIL",
                "value": "ordini@bracestreetlab.it",
                "note":  "للكاترينغ والفعاليات والموردين",
                "href":  "ordini@bracestreetlab.it",
                "kind":  "mail",
            },
        ],

        # Hours grid (compact)
        "hours_label": "ساعات العمل",
        "hours_rows": [
            ("الإثنين – الخميس", "12:00 – 24:00"),
            ("الجمعة – السبت",   "12:00 – 01:30"),
            ("الأحد",             "12:00 – 24:00"),
        ],
        "hours_note": "آخر طلب قبل الإغلاق بثلاثين دقيقة · المطبخ شغّال دائماً",

        # Transport note
        "transport_label": "كيف تصل",
        "transport_rows": [
            ("BUS",       "الخطوط 11، 14، 27 · موقف Indipendenza"),
            ("القطار",    "Stazione Centrale · 8 دقائق مشياً"),
            ("موقف سيارات", "Riva di Reno · 4 دقائق مشياً"),
            ("دراجة",      "موقف دراجات في Via dell'Indipendenza"),
        ],

        # Jobs band
        "jobs_label":    "اشتغل معنا",
        "jobs_heading":  'نبحث عن <em>خمسة أشخاص.</em>',
        "jobs_intro":
            "Brace يكبر. نفتح مختبراً ثانياً في Modena قبل صيف 2026. "
            "نحتاج إلى أشخاص حقيقيّين، لا سِيَر ذاتية مثاليّة.",
        "jobs": [
            {"role": "GRILLER",        "type": "دوام كامل",  "city": "BOLOGNA"},
            {"role": "صانع البيتزا",   "type": "دوام جزئي",  "city": "BOLOGNA"},
            {"role": "RUNNER وعلى البار", "type": "نهاية الأسبوع", "city": "BOLOGNA"},
        ],
        "jobs_cta_label": "أرسل رسالة",
        "jobs_cta_href":  "lavoro@bracestreetlab.it",

        # Social block
        "social_label": "تابعنا",
        "social": [
            {"platform": "INSTAGRAM", "handle": "@brace.lab",      "href": "https://instagram.com/brace.lab"},
            {"platform": "TIKTOK",    "handle": "@brace.bologna",  "href": "https://tiktok.com/@brace.bologna"},
        ],

        # Mini reservation/inquiry form
        "form_label":   "اكتب لنا",
        "form_heading": 'سطران <em>يكفيان.</em>',
        "form_intro":
            "للكاترينغ، للمجموعات فوق اثني عشر شخصاً، للموردين. للطلبات "
            "اكتب لنا على WhatsApp، أسرع.",
        "form_field_name":     "الاسم",
        "form_field_email":    "البريد الإلكتروني",
        "form_field_phone":    "الهاتف",
        "form_field_message":  "ماذا تحتاج",
        "form_field_message_placeholder": "كاترينغ، فعالية، توريد، غير ذلك…",
        "form_submit_label":   "أرسل",
        "form_submit_note":
            "عرض توضيحي · لن تُرسَل أي بيانات. للطلب الفعلي، "
            "اتصل 051 234 5566 أو اكتب على WhatsApp.",
    },

    # No blog on Brace
    "posts": [],
}
