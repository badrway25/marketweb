"""Sapore — Trattoria Da Nonna Rosa (trattoria-warm archetype) — AR content tree.

Phase 2g3.6 — Restaurant live-completion (Session 48, 2026-04-15).

Voice contract (AR — Arabic cultural-publishing register):
- Native MSA in the register of Brownbook / Saudi Gazette Lifestyle /
  Annahar culture pages reviewing a Roman family trattoria. Warm,
  observant, second-person inclusive, literate but intimate — never
  marketing-speak, never colloquial.
- Arabic vocabulary signals: تراتوريا · جدّة · بيت · فرن حطب · عجين ·
  مائدة طويلة · كأس · حكاية · حيّ · دفء · رائحة الخبز · يد الجدّة.
- Latin verbatim (NEVER transliterated): Trattoria Da Nonna Rosa,
  Rosa Trezzi, Marco Trezzi, Giulia Trezzi, Trastevere, Roma,
  Via dei Salumi, Lazio, Amatrice, Cacio e pepe, Carbonara,
  Bucatini all'amatriciana, Coda alla vaccinara, Tonnarelli,
  Margherita verace, Cesanese del Lazio, Olevano Romano, Agerola,
  Sarnelli, Molino Paolo Mariani, Proietti Riccardi, Pienza,
  Pondichéry, Ribelà, Sorrentina, Parisi, Viterbese, Cimino,
  Vitorchiano, Senatore Cappelli, Gambero Rosso, Corriere della Sera,
  Puntarella Rossa, Beppe, Josep Maria, Barcellona, Peppe Guida,
  Vico Equense, Gennaro Esposito, Testaccio, Porta Portese, Valentini,
  Sabina DOP, Piennolo, Amalfi, HACCP, OpenStreetMap, WhatsApp,
  SMS, Piazza Trilussa, Circo Massimo, Piazza dei Mercanti,
  lungotevere Ripa, Piazza Navona, Campo de' Fiori, Ponte Sisto,
  Piazza in Piscinula, Prato, Norcia, Andria, Diamante, Sarmento,
  Barchi, Marche, Campania, Toscana, Usigliano di Lari, Monte Savello,
  Belli, Sonnino, "Roma nun fa' la stupida stasera". Prices stay
  Latin with Western digits (€ 12.00). Phone numbers Latin.
  Hours Latin (12:30 – 15:00). Days translate to AR (الإثنين · الثلاثاء).
- Arabic punctuation (، ؛ ؟) and «…» quotes. HTML <em>…</em> preserved
  verbatim for RTL italic renderer. Western digits (0-9) throughout,
  per MENA business-press convention.

Differentiation contract vs Brace AR (D-054 enforcement):
- Brace AR is Bologna street-food register with neon-yellow brutalist
  energy (order-now flows, QR menus, delivery strip). Sapore AR is
  intimate Roman family-trattoria food-writer reportage, warm cream
  paper register (reservations, phone + WhatsApp, hand-lettered
  chalkboard). Vocabularies MUST NOT overlap.

Differentiation contract vs Gusto AR (D-054 enforcement):
- Gusto AR is formal MSA Michelin editorial-chef register (شيف، مسرح،
  فصول، مرافقة نبيذ، قاعة واحدة لأربعة عشر ضيفًا). Sapore AR is
  warm family-trattoria register (جدّة، بيت، فرن حطب، مائدة طويلة،
  ثلاثة أجيال في المطبخ). Vocabularies MUST NOT overlap.
"""
from __future__ import annotations

from typing import Any


SAPORE_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "الرئيسية",                "kind": "home"},
        {"slug": "menu",     "label": "القائمة",                 "kind": "menu"},
        {"slug": "storia",   "label": "حكايتنا",                 "kind": "about"},
        {"slug": "forno",    "label": "الفرن وجوارحُه",          "kind": "signature"},
        {"slug": "eventi",   "label": "الموائد والمناسبات",      "kind": "events"},
        {"slug": "contatti", "label": "اعثر علينا واحجز",        "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "R",
        "logo_word":    "Trattoria Da Nonna Rosa",
        "tag":          "تراتوريا عائلية · حيّ Trastevere · منذ 1987",
        "phone":        "06 581 4488",
        "phone_tel":    "+390658144880",
        "whatsapp":     "06 581 4488",
        "whatsapp_link": "https://wa.me/390658144880",
        "email":        "ciao@trattoriadanonnarosa.it",
        "address":      "Via dei Salumi 16/a · 00153 Roma · Trastevere",
        "hours_compact": "الثلاثاء – السبت · 12:30 – 15:00 · 19:00 – 23:30",
        "hours_footer_rows": [
            "الأحد · الغداء فقط · 12:30 – 15:00",
            "الإثنين · يوم الراحة الأسبوعي",
        ],
        "license":      "P.IVA 07634211006 · CCIAA Roma REA 1138992",
        "footer_intro":
            "تراتوريا عائلية افتتحتها Rosa Trezzi عام 1987. عجينٌ يُمَدّ بالنشّابة "
            "كلَّ صباح، وبيتزا تخرج من فرن الحطب مع مغيب الشمس، وكأسٌ من نبيذ "
            "البيت نُقدّمه هديّةً لمن عاد إلينا مرّتين. ستّون مقعدًا، قاعتان، "
            "وثلاثة أجيال من العائلة في المطبخ.",
        "nav_cta":      "احجز طاولة",
        "nav_cta_href": "contatti",
        "nav_phone_cta": "اتصل بنا: 06 581 4488",
        "star_line":    "تراتوريا عائلية · منذ 1987",
        "copyright":    "© 2026 Trattoria Da Nonna Rosa · الرقم الضريبي 07634211006",

        # Mirror the fine-dining _base.html footer keys used by the chrome
        "footer_hours_1": "الثلاثاء – السبت · غداء وعشاء",
        "footer_hours_2": "الأحد · الغداء فقط",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "تراتوريا عائلية · حيّ Trastevere · منذ 1987",
        "headline": "عند Nonna Rosa، <em>كأنّكَ في بيتك.</em>",
        "intro":
            "عجينٌ يُمَدّ بالنشّابة كلَّ صباح، وبيتزا من فرن الحطب مع المساء، "
            "وكأسٌ من نبيذ البيت نقدّمه هديّةً لمن عاد إلينا مرّتين. ستّون مقعدًا، "
            "قاعتان، وثلاثة أجيال من العائلة في المطبخ ذاته منذ أربعين عامًا.",
        "primary_cta":   "احجز طاولة",
        "primary_href":  "contatti",
        "secondary_cta": "راسلنا على WhatsApp",
        "secondary_href_is_whatsapp": True,

        # Hero photo-frame
        "hero_image":   "https://images.unsplash.com/photo-1481931098730-318b6f776db0?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Cacio e pepe يوم الثلاثاء · Tonnarelli يُمَدّ بالنشّابة",
        "hero_stamp":   "منذ 1987",

        # Facts band — 3 numbers/claims
        "facts": [
            ("1987",   "العام الذي فتحت فيه Rosa مطبخها"),
            ("60",     "مقعدًا في قاعتين · لا حجوزات بعد الثامنة مساءً"),
            ("3",      "أجيال من العائلة في المطبخ"),
        ],

        # Chalkboard — 5 daily specials lun → ven
        "chalkboard_label":   "لوحُ الطباشير في هذا الأسبوع",
        "chalkboard_heading": "طبقُ اليوم، <em>مكتوبٌ باليد.</em>",
        "chalkboard_intro":
            "كلَّ صباح تكتب Nonna Rosa لوحَ الطباشير بخطّها، فتقرّر أمام "
            "الباب ما الذي سنطبخه اليوم. هكذا يدور الأسبوع عندنا.",
        "chalkboard_buongiorno": "هنيئًا مريئًا!",
        "chalkboard_days": [
            ("الإثنين",  "Cacio e pepe",              "Tonnarelli مَمدود باليد",                        "€ 10.00"),
            ("الثلاثاء", "Bucatini all'amatriciana",  "Guanciale من Amatrice بتوقيع Sarnelli",          "€ 11.00"),
            ("الأربعاء", "Coda alla vaccinara",       "وصفة Nonna Rosa كما كانت عام 1987",             "€ 14.00"),
            ("الخميس",   "Gnocchi al sugo d'arrosto", "يُصنَع في الصباح من البطاطا البلديّة المعتّقة",   "€ 11.00"),
            ("الجمعة",   "Baccalà in pastella",       "طماطم كرزيّة مُربّاة وخرشوف روماني",              "€ 13.00"),
        ],

        # Family strip — 3 portraits with personal blurbs
        "family_label":   "العائلة في المطبخ",
        "family_heading": "ثلاثة أجيال، <em>مائدة واحدة.</em>",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "عجينة طازجة منذ 1987",
                "blurb":
                    "افتتحت Nonna Rosa التراتوريا في الثالث من سبتمبر 1987 بحلمٍ "
                    "وبنشّابتَين. بلغت اليوم الثانية والثمانين ومازالت تمدّ العجين "
                    "كلَّ صباح منذ السابعة. قاعدتها بسيطة: «العجينة الجيّدة تعرفها "
                    "تحت يديك، ولستَ بحاجةٍ إلى ميزان».",
                "portrait": "https://images.pexels.com/photos/2050990/pexels-photo-2050990.jpeg?auto=compress&cs=tinysrgb&w=600&h=750&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "صانع البيتزا · فرن الحطب منذ 2003",
                "blurb":
                    "ابنُ Rosa، نشأ بين الدقيق والطوب. يُشعل الفرن كلَّ عصرٍ عند "
                    "الرابعة — خشب بلّوط من Cimino، لا غير — ويُبقيه حيًّا حتّى "
                    "منتصف الليل. تعلّم Margherita verace على يد Peppe Guida في "
                    "Vico Equense عام 2008.",
                "portrait": "https://images.unsplash.com/photo-1607631568010-a87245c0daf8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "القاعة وحلويات البيت",
                "blurb":
                    "حفيدة Rosa، في الثلاثين من عمرها، تتولّى القاعة والحلويات. "
                    "تيراميسو بمَسكَربوني Sarnelli، فطيرة الكرز الحامض في موسمه، "
                    "و«maritozzi» بالقشطة صباح السبت فقط. تستقبلكم بابتسامةٍ "
                    "وإبريقٍ من الماء الفوّار.",
                "portrait": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Forno teaser band
        "forno_label":   "فرن الحطب",
        "forno_heading": "يُشعَل كلَّ عصرٍ عند <em>الرابعة تمامًا.</em>",
        "forno_text":
            "قُبّة فرن Marco مبنيّة من طوب Viterbese، شيّدها بيد الحِرفيّ Gennaro "
            "Esposito عام 2003. لا يحترق فيها إلّا خشب بلّوط Cimino، وترتفع "
            "حرارتها إلى 420 درجة، فتُنضج البيتزا في ستّين ثانية. من الثلاثاء إلى "
            "السبت، مساءً فقط، حين تخلو القاعة الأولى من ضيوف الغداء.",
        "forno_image":    "https://images.unsplash.com/photo-1593504049359-74330189a345?w=1200&q=80&auto=format&fit=crop",
        "forno_caption":  "Margherita verace · 420 درجة · ستّون ثانية",
        "forno_cta":      "تعرَّف على البيتزا والمعكرونة",
        "forno_cta_href": "forno",

        # Reviews band — 2–3 quotes
        "reviews_label": "كُتِبَ عنّا",
        "reviews": [
            {
                "quote":  "شعرتُ أنّني في مطبخ الجدّة التي لم تكن لي.",
                "author": "Gambero Rosso · Tre Spicchi 2024",
            },
            {
                "quote":  "من آخر التراتوريّات الأصيلة في Trastevere. سِرْ إليها على قدمَيك في المساء، واطلب طبق الـ Coda.",
                "author": "Corriere della Sera · Cook",
            },
            {
                "quote":  "Carbonara Rosa تُسكت الجميع، حتّى أهل Testaccio.",
                "author": "Puntarella Rossa · 2025",
            },
        ],

        # Hours strip — 3 rows under reviews
        "hours_label":  "متى نفتح",
        "hours_rows": [
            ("الثلاثاء – السبت", "12:30 – 15:00", "الغداء"),
            ("الثلاثاء – السبت", "19:00 – 23:30", "العشاء · فرن الحطب"),
            ("الأحد",            "12:30 – 15:00", "الغداء فقط · الإغلاق عند 16:00"),
        ],
        "hours_note": "الإثنين يوم الراحة الأسبوعي · مفتوحون في كلّ الأعياد الرسميّة عدا عيد الميلاد",

        # Tavolata band — group experience teaser
        "tavolata_label":   "المائدة الطويلة",
        "tavolata_heading": "اثنا عشر صديقًا، <em>طاولة واحدة.</em>",
        "tavolata_text":
            "مائدتُنا الطويلة ذات الاثني عشر مقعدًا تقع في قاعة المدفأة. قائمة "
            "ثابتة باثنَين وثلاثين يورو، تشمل نبيذ البيت، وتُختَم بحلويات Giulia. "
            "لأعياد الميلاد، وحفلات التناول الأوّل، وسهرات الدراسة القديمة، أو "
            "لمجرّد أنّ اليوم صالحٌ للاجتماع حول طاولة.",
        "tavolata_cta":      "نظِّم مائدةً طويلة",
        "tavolata_cta_href": "eventi",
        "tavolata_image":    "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=1200&q=80&auto=format&fit=crop",

        # Final CTA band
        "cta_label":    "تعالَوا إلينا",
        "cta_heading":  "Via dei Salumi رقم ستّة عشر، <em>اضغط الجرس بقوّة.</em>",
        "cta_intro":
            "نقع في Via dei Salumi، على بُعد خطوات من ضفّة Tevere. البابُ من "
            "خشبٍ أخضر، والجرس عالي الصوت: لا تتردّدوا، اضغطوا بقوّة. ستجدون "
            "كأسًا باردةً من Cesanese في انتظاركم، وشريحة بيتزا حمراء خرجت "
            "لتوّها من الفرن.",
        "cta_primary":      "احجز طاولة",
        "cta_primary_href": "contatti",
        "cta_secondary":    "اكتب لنا على WhatsApp",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "القائمة · موسم خريف 2026",
        "headline": "عجينٌ مَمدود باليد، بيتزا من فرن الحطب، <em>وحلويات البيت.</em>",
        "intro":
            "لا تتبدّل القائمة كثيرًا، لأنّ أطباق البيت هي هذه: Cacio e pepe، "
            "Amatriciana، Carbonara، Coda، Saltimbocca. أمّا البيتزا فتدور مع "
            "الفصل. وما عدا ذلك تقرّره Nonna Rosa أمام الباب في الصباح.",

        "wine_house_label":   "نبيذ البيت",
        "wine_house_heading": "Cesanese del Lazio، <em>من البرميل، € 18.00 للّتر.</em>",
        "wine_house_text":
            "يأتي نبيذُ البيت من Olevano Romano، من قبو Proietti Riccardi الذي "
            "يعصرُه منذ أربعين عامًا. نُقدّمه في إبريقٍ لترًا أو نصفًا أو رُبعًا. "
            "أمّا الأبيض فهو Malvasia Puntinata من تلال الـ Castelli، من قبو "
            "Ribelà، ويُقدَّم كذلك من البرميل.",

        "allergen_note":
            "الأطباق التي تحمل العلامة (G) تحتوي على الغلوتين، و(L) على الحليب، "
            "و(P) على الأسماك. إن كان لديك حساسيّة خاصّة، اسأل أمام الباب قبل "
            "الطلب: Rosa تلقّت دورة HACCP عام 2019 وتعرف كلّ ما يلزم.",

        "sections": [
            {
                "label": "مُقبّلات البيت",
                "heading": "من البستان ومن وراء الباب",
                "dishes": [
                    ("Bruschetta al pomodoro",       "طماطم Piennolo، ريحان، زيت زيتون Sabina DOP",      "€ 7.00"),
                    ("Carciofo alla giudia",         "خرشوف روماني، مقليّ مرّتين، ليمون Amalfi",          "€ 9.00"),
                    ("Suppli classico",              "أرز، موتزاريلّا ذائبة، صلصة لحم البيت",            "€ 4.00"),
                    ("Fiori di zucca fritti",        "محشوّة بالموتزاريلّا والأنشوجة، عجينٌ خفيف",         "€ 8.00"),
                    ("Puntarelle alla romana",       "أنشوجة بحر Cantabrico، ثوم، خلّ أحمر",             "€ 8.00"),
                    ("Tagliere di salumi & formaggi","Guanciale من Amatrice، Pecorino من Pienza، زيتون", "€ 14.00"),
                    ("Polpette di Nonna Rosa",       "صلصة طماطم، خبز البيت إلى جانبها",                "€ 10.00"),
                ],
            },
            {
                "label": "المعكرونة الممدودة بالنشّابة",
                "heading": "من نشّابة الصباح",
                "dishes": [
                    ("Cacio e pepe",                 "Tonnarelli مَمدود باليد، Pecorino من Pienza",       "€ 12.00"),
                    ("Carbonara classica",           "Guanciale من Amatrice، Pecorino romano، خمسة صفارات بيض", "€ 13.00"),
                    ("Bucatini all'amatriciana",     "Guanciale، طماطم San Marzano، Pecorino",            "€ 12.00"),
                    ("Gnocchi al sugo d'arrosto",    "يُصنَع في الصباح، صلصة خميس Rosa",                  "€ 11.00"),
                    ("Fettuccine alla papalina",     "لحم خنزير مُقدَّد، بازلّاء طازجة، بيض، Parmigiano",   "€ 13.00"),
                    ("Rigatoni con la pajata",       "أمعاء العجل الرضيع، صلصة طماطم",                   "€ 15.00"),
                    ("Tonnarelli al cacio e tartufo","كمأة سوداء من Norcia، Pecorino، فلفل",               "€ 18.00"),
                ],
            },
            {
                "label": "بيتزا من فرن الحطب",
                "heading": "مساءً فقط · الثلاثاء ← السبت",
                "dishes": [
                    ("Margherita verace",            "طماطم San Marzano، fiordilatte، ريحان",             "€ 9.00"),
                    ("Capricciosa di Nonna Rosa",    "خرشوف، فطر، لحم خنزير مطبوخ، بيضة",                 "€ 12.00"),
                    ("Diavola al guanciale",         "طماطم، fiordilatte، سلامي حارّ، Guanciale",         "€ 11.00"),
                    ("Bianca al cacio e pepe",       "fiordilatte، Pecorino، فلفل أسود من Pondichéry",    "€ 10.00"),
                    ("Nonna Rosa (التوقيع)",         "Stracciatella من Andria، طماطم كرزيّة نصف مُجفّفة، ريحان", "€ 13.00"),
                    ("Zucca e salsiccia",            "كريمة يقطين، نقانق من Norcia، إكليل الجبل",         "€ 12.00"),
                ],
            },
            {
                "label": "أطباقٌ رئيسيّة من وراء الباب",
                "heading": "من مطبخ يوم الأحد",
                "dishes": [
                    ("Saltimbocca alla romana",      "لحم عجل، لحم خنزير مُقدَّد، مريميّة، نبيذ أبيض",   "€ 16.00"),
                    ("Coda alla vaccinara",          "ذَيل بقر، كرفس، كاكاو، صنوبر، زبيب",                 "€ 17.00"),
                    ("Abbacchio a scottadito",       "ضلوع حَمَل، إكليل الجبل، ليمون",                    "€ 19.00"),
                    ("Trippa alla romana",           "كرشة، صلصة طماطم، نعناع بلدي، Pecorino",            "€ 14.00"),
                    ("Baccalà in pastella",          "قَدّ مُنَعَّم، عجينٌ خفيف، طماطم كرزيّة",             "€ 14.00"),
                ],
            },
            {
                "label": "حلويات البيت",
                "heading": "يدا Giulia",
                "dishes": [
                    ("Tiramisù di Giulia",           "Mascarpone من Sarnelli، بسكويت سافوياردي، قهوة المَوكا", "€ 6.00"),
                    ("Panna cotta alla vaniglia",    "مع كرز Nonna Rosa الحامض",                            "€ 5.00"),
                    ("Crostata di visciole",         "عجينة الفطيرة البلديّة، كرز حامض من قَطْف 2025",      "€ 6.00"),
                    ("Maritozzo con la panna",       "صباح السبت فقط · قشطة طازجة من Valentini",             "€ 4.00"),
                    ("Gelato del nonno",             "ثلاثة نكهات · زهرة حليب، بندق، شوكولاتة",              "€ 5.00"),
                ],
            },
        ],
    },

    # ─── STORIA (about) ──────────────────────────────────────────
    "storia": {
        "eyebrow":  "الحكاية · منذ 1987",
        "headline": "أربعون عامًا من العجين الممدود <em>بالنشّابة.</em>",
        "intro":
            "تفتح Trattoria Da Nonna Rosa أبوابها في الثالث من سبتمبر 1987، في "
            "غرفتين من Via dei Salumi ورثَتهما Rosa Trezzi عن أمّها. بعد أربعين "
            "عامًا، ما زلنا هنا، في المطبخ ذاته، مع فرنٍ جديد وثلاثة أجيال من "
            "العائلة يتناوبون أمام الباب.",

        "story": [
            "وُلدت Rosa Trezzi في Roma عام 1944، ابنةً لصاحب حانةٍ في حيّ "
            "Testaccio. ترعرعت بين القدور والنشّابات وضوضاء سوق Porta Portese. "
            "تزوّجت في الخامسة عشرة من Marino الذي كان خبّازًا، وافتتحا معًا "
            "حانةً أولى في Via dei Foraggi. دامت ستّ سنوات، حتّى عام 1987، حين "
            "ورثَ والدُ Marino غرفتين في Via dei Salumi بحيّ Trastevere.",

            "في الثالث من سبتمبر 1987 تفتح التراتوريا في الرقم ستّة عشر، باثني "
            "عشر مقعدًا، وفرنٍ يعمل بالغاز، وثلّاجةٍ جداريّة. قائمة الليلة الأولى "
            "كتبتها Rosa بالقلم على ورقةٍ زيتيّة: Cacio e pepe، Amatriciana، "
            "Coda alla vaccinara، وتيراميسو بمَسكَربوني الحلّاب في الحيّ. كلفة "
            "العشاء الإجماليّة: أربعةُ آلاف ليرة.",

            "في عام 2003 يتسلّم الابن Marco القاعة الثانية — ورشة نجّارٍ أغلقت "
            "أبوابها — ويُشيّد فرنَ الحطب مع صانع البيتزا Gennaro Esposito، الذي "
            "كان قد حلَّ ضيفًا على Roma في عرسٍ من الأعراس. منذ ذلك الصيف دخلت "
            "البيتزا إلى القائمة، مساءً فقط، أيّام الثلاثاء والسبت. ثمّ في كلّ "
            "الأمسيات منذ 2005.",

            "في عام 2024 تعود Giulia، حفيدة Rosa، من Barcellona حيث كانت تعمل "
            "في معجنات، لتتسلّم القاعة والحلويات. تضمّ التراتوريا اليوم ستّين "
            "مقعدًا، وثلاثة أجيال، وفرنَ حطب، ونادلًا قديمًا — Beppe، منذ 1996 — "
            "واللافتةَ ذاتها على الباب: من عاد إلينا مرّتَين، فكأسُ نبيذ البيت "
            "هديّةٌ له.",
        ],

        # Timeline — 3 steps
        "timeline_label":   "ثلاثة تواريخ",
        "timeline": [
            {
                "year":  "1987",
                "title": "تفتح Rosa الباب في الرقم ستّة عشر",
                "desc":  "الثالث من سبتمبر، اثنا عشر مقعدًا، أربعةُ آلاف ليرة للشخص. القائمة الأولى مكتوبةٌ بالقلم على ورقةٍ زيتيّة.",
            },
            {
                "year":  "2003",
                "title": "يصل فرن الحطب",
                "desc":  "يتسلّم Marco القاعة الثانية ويبني الفرن مع Gennaro Esposito. Margherita الأولى: الثاني والعشرون من يونيو.",
            },
            {
                "year":  "2024",
                "title": "تعود Giulia إلى البيت",
                "desc":  "تعود Giulia من Barcellona وتتسلّم القاعة. أوّل maritozzo سبتٍ: السادس والعشرون من أكتوبر.",
            },
        ],

        # Family portraits (reused shape from home but with longer blurbs)
        "family_label":   "الأيادي التي تخدمكم",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "المؤسِّسة · عجينة طازجة منذ 1987",
                "blurb":
                    "اثنتان وثمانون عامًا، حفيدٌ لكلّ إصبع من يدها، ونشّابةٌ تعرفها "
                    "عن ظهر قلب. تمدّ العجين كلَّ صباح من السابعة إلى العاشرة، ثمّ "
                    "تنصرف إلى كتابة لوح اليوم. وحدَها تصنع الـ Carbonara: "
                    "طقسٌ تغار عليه ولا تُفرّط فيه.",
                "portrait": "https://images.pexels.com/photos/2050990/pexels-photo-2050990.jpeg?auto=compress&cs=tinysrgb&w=600&h=750&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "صانع البيتزا · فرن الحطب منذ 2003",
                "blurb":
                    "ترعرع في التراتوريا، عمل نجّارًا ثلاث سنوات، ثمّ صار صانعَ "
                    "بيتزا اثنَتَين وعشرين سنة. يُشعل الفرن عند الرابعة، ويطقطق "
                    "بلّوطَ Cimino، ويعجن يدويًّا بخميرةٍ حيّةٍ منذ 2008. يُدخل "
                    "Margherita إلى الفرن مُغمضَ العينين في ستّين ثانية.",
                "portrait": "https://images.unsplash.com/photo-1607631568010-a87245c0daf8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "القاعة والحلويات · منذ 2024",
                "blurb":
                    "سنتان عند Josep Maria في معجنات Barcellona، ثمّ العودة. "
                    "تتولّى القاعة مع النادل Beppe، وتُحضّر حلويات اليوم، وتختار "
                    "قائمة النبيذ. تصنع أفضل maritozzo غرب نهر Tevere، لكن "
                    "صباح السبت فقط.",
                "portrait": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Valori grid — 4 cards
        "values_label":   "قواعد البيت",
        "values_heading": "أربعةُ أشياء <em>لا تتبدّل.</em>",
        "values": [
            {
                "title": "عجن المعكرونة",
                "desc":
                    "دقيقٌ من Molino Paolo Mariani، ماءٌ من Roma، صفار بيضٍ من "
                    "Paolo Parisi. تُمَدّ بالنشّابة كلَّ صباح من السابعة. لا "
                    "تجفيف، لا تجميد، لا من صباح الأمس.",
            },
            {
                "title": "فرن الحطب",
                "desc":
                    "خشب بلّوط Cimino وحده، يُقطَع في Vitorchiano. يُشعَل كلَّ "
                    "عصرٍ عند الرابعة تمامًا. إن لم يبلغ الفرن 420 درجة تلك "
                    "الليلة، فلا بيتزا — هكذا اتّفقنا.",
            },
            {
                "title": "نبيذ البيت",
                "desc":
                    "Cesanese من Olevano Romano بتوقيع Proietti Riccardi، "
                    "وMalvasia dei Castelli بتوقيع Cantina Ribelà. من البرميل، "
                    "في إبريق. ثمانيةَ عشَرَ يورو للّتر، الرقم ذاته منذ 2019.",
            },
            {
                "title": "قاعدة الكأس",
                "desc":
                    "من عاد إلينا مرّتين، فكأس نبيذ البيت هديّةٌ له. مكتوبةٌ على "
                    "اللوح منذ اليوم الأوّل، لم نُبدِّلها يومًا. حتّى إن تعرّفنا "
                    "عليك، اطلبها مِنّا على كلّ حال.",
            },
        ],

        "photo_image":   "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1600&q=80&auto=format&fit=crop",
        "photo_caption": "قاعة المدفأة · عشاء السبت · نوفمبر 2025",
    },

    # ─── FORNO (signature · pizza & pasta) ────────────────────────
    "forno": {
        "eyebrow":  "البيتزا والمعكرونة · تواقيع البيت",
        "headline": "أربعُ بيتزات وأربعُ معكرونات <em>مكتوبةٌ باليد.</em>",
        "intro":
            "تواقيعُنا ثمانية — أربعٌ من الفرن، وأربعٌ من النشّابة. لا تتبدّل، "
            "ولا تُضاف إليها طبقاتٌ، ولا تدور مع الموسم. إنّها الأطباق التي "
            "أقرّتها Nonna Rosa عام 1987، وتُراهن عليها العائلة منذ أربعين "
            "عامًا.",

        # Pizza section
        "pizza_label":   "من فرن الحطب",
        "pizza_heading": "أربعُ بيتزات <em>بتوقيع البيت.</em>",
        "pizza_intro":
            "فرن Marco لا يحترق فيه إلّا بلّوط Cimino، يبلغ 420 درجة، ويُنضج "
            "البيتزا في ستّين ثانية. عجينٌ يختمر على مدى 24 ساعة بخميرة حيّة "
            "منذ 2008. طماطم San Marzano DOP، وfiordilatte Agerola من "
            "Caseificio Sorrentina.",
        "pizza_signatures": [
            {
                "n":     "I",
                "name":  "Margherita verace",
                "desc":  "طماطم San Marzano DOP، fiordilatte من Agerola، ريحان جنوي DOP، زيت زيتون Sabina على البارد.",
                "price": "€ 9.00",
            },
            {
                "n":     "II",
                "name":  "Capricciosa di Nonna Rosa",
                "desc":  "خرشوف روماني مقلوب، فطر champignon، لحم خنزير مطبوخ من Prato، بيضةٌ عضويّة من Parisi في الوسط.",
                "price": "€ 12.00",
            },
            {
                "n":     "III",
                "name":  "Diavola al guanciale",
                "desc":  "طماطم، fiordilatte، سلامي حارّ من Amatrice، Guanciale من Sarnelli، فلفل حارّ من Diamante.",
                "price": "€ 11.00",
            },
            {
                "n":     "IV",
                "name":  "Nonna Rosa (توقيع البيت)",
                "desc":  "Stracciatella من Andria باردةً، طماطم كرزيّة نصف مُجفّفة، ريحان، زيت Sabina، قشرة ليمون Amalfi.",
                "price": "€ 13.00",
            },
        ],

        # Pasta section
        "pasta_label":   "من النشّابة",
        "pasta_heading": "أربعُ معكرونات <em>مَمدودةٌ باليد منذ السابعة.</em>",
        "pasta_intro":
            "عجينٌ يُمَدّ بالنشّابة كلَّ صباح من السابعة إلى العاشرة. دقيقٌ من "
            "Molino Paolo Mariani، ماءٌ من Roma، صفار بيضٍ من Paolo Parisi. "
            "لا تجفيف، لا تجميد، لا من صباح الأمس.",
        "pasta_signatures": [
            {
                "n":     "I",
                "name":  "Cacio e pepe",
                "desc":  "Tonnarelli مَمدود باليد، Pecorino من Pienza DOP، فلفل أسود من Pondichéry مطحونٌ لحظةَ التقديم.",
                "price": "€ 12.00",
            },
            {
                "n":     "II",
                "name":  "Carbonara classica",
                "desc":  "سباغيتّي، Guanciale من Amatrice، Pecorino romano، خمسة صفارات بيض من Parisi، فلفل أسود. لا قشطة، أبدًا.",
                "price": "€ 13.00",
            },
            {
                "n":     "III",
                "name":  "Bucatini all'amatriciana",
                "desc":  "Bucatini من المطحنة، Guanciale من Amatrice مُقَرمَش، San Marzano، Pecorino romano مبشورٌ في الطبق.",
                "price": "€ 12.00",
            },
            {
                "n":     "IV",
                "name":  "Fettuccine alla papalina",
                "desc":  "Fettuccine، لحم خنزير مُقدَّد San Daniele، بازلّاء طازجة، بيض، Parmigiano reggiano بعمر 36 شهرًا.",
                "price": "€ 13.00",
            },
        ],

        # Forno story
        "forno_story_label":   "فرن الحطب",
        "forno_story_heading": "أربعمئة وعشرون درجة، <em>ستّون ثانية.</em>",
        "forno_story_text_1":
            "قُبّة فرن Marco شيّدها يدويًّا عام 2003 صانع البيتزا Gennaro "
            "Esposito، طوبةً فطوبة، من طينٍ حراريٍّ جُلب من Viterbo. يبلغ قُطرها "
            "مترَين وعشرة سنتيمترات، وتطبخ ستّ بيتزات في آنٍ واحد، وتصل إلى "
            "420 درجة مع سلّةٍ من بلّوط Cimino المقطوع في Vitorchiano.",
        "forno_story_text_2":
            "يُشعَل كلَّ عصرٍ عند الرابعة تمامًا. إن لم يبلغ الحرارة المطلوبة "
            "بحلول السادسة، فلا بيتزا تلك الليلة — حدث ذلك ثلاث مرّات في اثنَتَين "
            "وعشرين سنة، آخرها في فبراير 2024 حين ضربت العاصفة الثلجيّة، "
            "فصنعنا كلُّنا معكرونةً تلك الليلة.",
        "forno_story_image":
            "https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?w=1600&q=80&auto=format&fit=crop",
        "forno_story_caption": "بلّوط Cimino · الفرن عند 420 درجة · يوليو 2025",

        # Ingredients/producers band
        "producers_label":   "خمسُ أيادٍ توقِّع",
        "producers_heading": "من أين يأتي، <em>ومن أيّ يد.</em>",
        "producers": [
            {
                "name":       "Sarnelli Guanciale",
                "place":      "Amatrice · Lazio",
                "ingredient": "Guanciale من خنزيرٍ أسود في Caserta · تعتيقٌ 90 يومًا",
            },
            {
                "name":       "Molino Paolo Mariani",
                "place":      "Barchi · Marche",
                "ingredient": "دقيق من نوع 0 و00 · قمح Senatore Cappelli · مطحونٌ على الحجر",
            },
            {
                "name":       "Proietti Riccardi",
                "place":      "Olevano Romano · Lazio",
                "ingredient": "Cesanese del Lazio من البرميل · كرومٌ على شكل شُجَيرات · قَطْف 2024",
            },
            {
                "name":       "Caseificio Sorrentina",
                "place":      "Agerola · Campania",
                "ingredient": "fiordilatte من جاموس Campania · توصيلٌ يوميّ",
            },
            {
                "name":       "Paolo Parisi",
                "place":      "Usigliano di Lari · Toscana",
                "ingredient": "بيضٌ من دجاجٍ يتغذّى على حليب الماعز · صفارٌ برتقاليّ",
            },
        ],

        # Dough photo
        "dough_image":   "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=1600&q=80&auto=format&fit=crop",
        "dough_caption": "عجينٌ يختمر 24 ساعة · خميرةٌ حيّةٌ منذ 2008",
    },

    # ─── EVENTI (events & tavolate) ──────────────────────────────
    "eventi": {
        "eyebrow":  "الموائد والمناسبات · مجموعاتٌ من اثنَي عشرَ إلى ستّين ضيفًا",
        "headline": "مائدةٌ طويلة، <em>الجميعُ جلوسًا جنبًا إلى جنب.</em>",
        "intro":
            "تفتح قاعة المدفأة أبوابها للموائد الطويلة من اثني عشر مقعدًا فأكثر. "
            "قائمةٌ ثابتة، نبيذ البيت ضمن السعر، وحلويات Giulia في الختام. "
            "لأعياد الميلاد، والتناوُل الأوّل، وسهرات الدراسة القديمة، وحفلات "
            "التوديع، والسهرات المهنيّة — أو لمجرّد أنّ الاجتماع حول طاولة يُفرِح.",

        # 3 group experiences
        "experiences_label":   "ثلاث صِيَغ",
        "meta_menu_label":     "القائمة",
        "meta_wine_label":     "النبيذ",
        "experiences": [
            {
                "n":       "01",
                "title":   "المائدة الطويلة",
                "persons": "من 12 إلى 20 ضيفًا",
                "menu":    "مقبّلات مشكّلة، طبقان أوّلان على الاختيار، طبق رئيسيّ، حلويات · € 32.00",
                "wine":    "Cesanese البيت وماء ضمن السعر",
                "desc":
                    "الصيغة العريقة: طاولة طويلة في قاعة المدفأة، أطباقٌ تُقسَم، "
                    "وأوقاتٌ على مهلها. صيغةٌ مثاليّة لأعياد الميلاد، وسهرات "
                    "الدراسة، وحفلات التوديع. يُحجَز قبل أربعة أيّام.",
            },
            {
                "n":       "02",
                "title":   "التناوُل الأوّل والعِماد",
                "persons": "من 20 إلى 40 ضيفًا",
                "menu":    "بوفيه مقبّلات، طبقان أوّلان، طبقان رئيسيّان، كعكة · € 48.00",
                "wine":    "Cesanese + Malvasia + مشروبات ضمن السعر · الفوّار على جنب",
                "desc":
                    "القاعتان مفتوحتان على المقاس، الأطفالُ أهلًا بهم، وكعكةُ "
                    "Giulia ضمن القائمة (اختر من ثلاث: ريكوتّا وكرز حامض، "
                    "شوكولاتة وكمّثرى، millefoglie بالفانيليا). يُحجَز قبل أسبوعَين.",
            },
            {
                "n":       "03",
                "title":   "سهرة مؤسّسة",
                "persons": "من 25 إلى 60 ضيفًا",
                "menu":    "قائمة تذوُّق من خمسة أطباق · € 62.00",
                "wine":    "مرافقة نبيذٍ من سوميلييه البيت · أربع كؤوس",
                "desc":
                    "تخصيصُ التراتوريا بالكامل لسهرةٍ وسط الأسبوع (ثلاثاء–خميس). "
                    "قائمةٌ بثلاث لغات إن لزم، جهازُ عرض للعروض التقديميّة، "
                    "Wi-Fi حرّ. يُحجَز قبل شهرٍ كامل.",
            },
        ],

        # Birthday/celebration block
        "birthday_label":   "أعياد الميلاد والذكريات",
        "birthday_heading": "كعكةُ Giulia، وشموعٌ، <em>ونَخبٌ مع Nonna Rosa.</em>",
        "birthday_text":
            "لكلّ عيد ميلاد تُحضّر Giulia كعكةً على المقاس (أخبِرنا بالنكهة "
            "المفضّلة قبل يومَين). نحملها بشموعها المُشعَلة، وتخرج Nonna Rosa "
            "من المطبخ لترفع النَخب معكم، وإن حالفكم الحظّ ستُغنّي لكم مقطعًا "
            "من «Roma nun fa' la stupida stasera» — لكنّها لا تفعل ذلك معنا "
            "أبدًا، إلّا إن طلبتَها منها بنفسك.",
        "birthday_image":   "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=1200&q=80&auto=format&fit=crop",
        "birthday_caption": "كعكةُ ريكوتّا وكرز حامض · عيد ميلاد Beppe الستّين",

        # Contact card specific to events
        "contact_label":    "لتنظيم مائدةٍ طويلة",
        "contact_heading":  "تكلَّم مباشرةً <em>مع Giulia.</em>",
        "contact_text":
            "الموائد والمناسبات تديرها Giulia بنفسها. اتّصل بها بين العاشرة "
            "والثانية عشرة صباحًا (هي الساعة التي لا تكون فيها بعدُ في القاعة)، "
            "أو اكتب إليها على WhatsApp: تُجيبك قبل نهاية النهار. وإن كان "
            "البريد الإلكتروني أيسرَ لك، فهو كذلك مناسب.",
        "contact_phone":    "06 581 4488",
        "contact_whatsapp": "06 581 4488",
        "contact_email":    "eventi@trattoriadanonnarosa.it",
        "contact_cta":      "اكتب إلى Giulia",
        "contact_cta_href": "contatti",
    },

    # ─── CONTATTI (reservations + find us) ────────────────────────
    "contatti": {
        "eyebrow":  "اعثر علينا واحجز · Via dei Salumi 16/a",
        "headline": "احجز طاولةً، <em>أو تعالَ من دون موعد.</em>",
        "intro":
            "نقع في Via dei Salumi بحيّ Trastevere، على بُعد خمس دقائق سيرًا "
            "من ضفّة Tevere. إن كنتم اثنَين أو ثلاثة فلا حاجة إلى الحجز: "
            "ادخلوا، وستجدون طاولة. من أربعةٍ فأكثر، الأفضلُ مكالمةٌ في "
            "اليوم السابق. للمجموعات فوق الاثني عشر، اذهبوا إلى صفحة الموائد.",

        # Address card
        "address_label":   "أين نحن",
        "address_heading": "Via dei Salumi 16/a",
        "address_text":
            "في حيّ Trastevere، بين Piazza dei Mercanti وضفّة Tevere في "
            "lungotevere Ripa. البابُ من خشبٍ أخضر، والجرسُ عالي الصوت. "
            "مترو خطّ B محطّة Circo Massimo (عشر دقائق سيرًا)، ترام رقم 8 "
            "محطّة Belli (أربع دقائق)، باص H محطّة Sonnino.",
        "address_city":    "00153 Roma · Trastevere",

        # Hours table — 4 rows
        "hours_label":   "أوقات الفتح",
        "hours_heading": "غداءٌ وعشاء، <em>الإثنين يوم الراحة.</em>",
        "hours_table": [
            ("الثلاثاء – السبت", "12:30 – 15:00",   "الغداء"),
            ("الثلاثاء – السبت", "19:00 – 23:30",   "العشاء · فرن الحطب مُشعَل"),
            ("الأحد",            "12:30 – 15:00",   "الغداء فقط · الإغلاق عند 16:00"),
            ("الإثنين",          "مغلق",            "يوم الراحة الأسبوعي"),
        ],

        # Phone/WhatsApp/email card
        "contact_label":     "تحدَّث إلينا",
        "contact_heading":   "ثلاثُ طرق، <em>كلُّها تصلح.</em>",
        "contact_phone_label":    "اتّصل أمام الباب",
        "contact_phone_value":    "06 581 4488",
        "contact_phone_hours":    "تجيب Giulia من العاشرة إلى الحادية عشرة ليلًا",
        "contact_whatsapp_label": "اكتب على WhatsApp",
        "contact_whatsapp_value": "06 581 4488",
        "contact_whatsapp_hours": "نردّ عليك خلال ساعةٍ واحدة",
        "contact_email_label":    "اكتب لنا بريدًا إلكترونيًّا",
        "contact_email_value":    "ciao@trattoriadanonnarosa.it",
        "contact_email_hours":    "نجيبك قبل نهاية اليوم التالي",

        # Reservation form
        "form_label":    "احجز عبر الموقع",
        "form_heading":  "احجز طاولةً، <em>نكتبك على اللوح.</em>",
        "form_intro":
            "املأ النموذج في الأسفل. ستصلك رسالةُ تأكيدٍ عبر الرسائل القصيرة "
            "أو WhatsApp خلال ساعتَين (نحن في المطبخ، غير أنّنا نُطالع "
            "الهواتف). للمجموعات فوق الاثني عشر، اكتبوا إلينا مباشرةً على "
            "WhatsApp.",

        "form_sections": [
            {
                "num":   "01",
                "title": "مَن أنت",
                "meta":  "لنؤكّد لك الطاولة",
                "fields": ["name", "email", "phone"],
            },
            {
                "num":   "02",
                "title": "متى تأتي",
                "meta":  "التاريخ والساعة وعدد الضيوف",
                "fields": ["date", "time", "people"],
            },
            {
                "num":   "03",
                "title": "ملاحظات",
                "meta":  "المناسبة، الحساسيّات، التفضيلات",
                "fields": ["occasion", "notes"],
            },
        ],

        "form_fields": [
            {
                "name":     "name",
                "label":    "الاسم الكامل",
                "type":     "text",
                "placeholder": "كيف ننادي عليك إلى الطاولة",
                "required": True,
                "helper":   "نكتبه على لوح الحجوزات.",
            },
            {
                "name":     "email",
                "label":    "البريد الإلكتروني",
                "type":     "email",
                "placeholder": "nome@esempio.it",
                "required": True,
                "helper":   "نرسل التأكيد على هذا العنوان.",
            },
            {
                "name":     "phone",
                "label":    "الهاتف أو WhatsApp",
                "type":     "tel",
                "placeholder": "+39 333 123 45 67",
                "required": True,
                "helper":   "لا نتّصل بك هنا إلّا في حال طارئ.",
            },
            {
                "name":     "date",
                "label":    "التاريخ",
                "type":     "date",
                "placeholder": "يوم/شهر/سنة",
                "required": True,
                "helper":   "مغلقون يوم الإثنين.",
            },
            {
                "name":     "time",
                "label":    "الساعة",
                "type":     "time",
                "placeholder": "مثلاً 20:30",
                "required": True,
                "helper":   "الغداء 12:30 – 14:30 · العشاء 19:00 – 22:30.",
            },
            {
                "name":     "people",
                "label":    "كم عددُكم",
                "type":     "number",
                "placeholder": "عدد المقاعد",
                "required": True,
                "helper":   "فوق الاثني عشر، اكتبوا مباشرةً على WhatsApp.",
            },
            {
                "name":     "occasion",
                "label":    "المناسبة",
                "type":     "select",
                "placeholder": "",
                "required": False,
                "full_width": True,
                "helper":   "إن كان عيد ميلاد، نُحضّر كعكةَ Giulia.",
            },
            {
                "name":     "notes",
                "label":    "ملاحظاتٌ للمطبخ",
                "type":     "textarea",
                "placeholder": "الحساسيّات، الأطباق المفضّلة، الطلبات الخاصّة…",
                "required": False,
                "full_width": True,
                "helper":   "Rosa أتمّت دورة HACCP عام 2019: قل لنا بصراحة ويكفي.",
            },
        ],

        "occasion_options": [
            "عشاءٌ اعتيادي",
            "عيد ميلاد",
            "ذكرى سنويّة",
            "عشاء عمل",
            "زيارةٌ أولى إلينا",
            "مائدةٌ طويلة (+12)",
            "أخرى",
        ],

        "consent":
            "أوافق على معالجة بياناتي لإدارة الحجز "
            "(لا نشرة إخباريّة، لا إعلانات، أبدًا).",
        "form_submit":      "احجز الطاولة",
        "form_submit_note": "نؤكّد الحجز خلال ساعتين، عبر الرسائل القصيرة أو WhatsApp.",

        # Map
        "map_label":    "على الخارطة",
        "map_heading":  "Via dei Salumi 16/a · Trastevere",
        "map_embed":
            "https://www.openstreetmap.org/export/embed.html"
            "?bbox=12.4660%2C41.8880%2C12.4720%2C41.8910"
            "&layer=mapnik&marker=41.8893%2C12.4690",
        "map_link":     "افتح على OpenStreetMap",
        "map_link_href":"https://www.openstreetmap.org/?mlat=41.8893&mlon=12.4690#map=17/41.8893/12.4690",

        # Getting-here notes
        "transport_label":   "كيف تصل إلينا",
        "transport_heading": "ثلاث طرق، <em>كلُّها سيرًا من قلب المدينة.</em>",
        "transport": [
            {
                "mode":  "المترو",
                "line":  "B · محطّة Circo Massimo",
                "note":  "عشر دقائق سيرًا على امتداد via di Monte Savello وlungotevere Ripa.",
            },
            {
                "mode":  "الترام",
                "line":  "8 · محطّة Belli",
                "note":  "أربع دقائق سيرًا، عبر Piazza Trilussa نحو Via dei Salumi.",
            },
            {
                "mode":  "الحافلة",
                "line":  "H · محطّة Sonnino",
                "note":  "ستّ دقائق سيرًا، مرورًا بـ Piazza in Piscinula.",
            },
            {
                "mode":  "سيرًا من المركز",
                "line":  "Ponte Sisto · خمسَ عشرةَ دقيقة",
                "note":  "من Piazza Navona، عبورًا بـ Campo de' Fiori ثمّ جسر Sisto.",
            },
        ],
    },

    # No blog
    "posts": [],
}
