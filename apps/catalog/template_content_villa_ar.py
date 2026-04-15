"""Phase 2g3.7 · Session 53 · Villa — AR native-voice tree. Editorial-concierge private-advisory voice."""
from __future__ import annotations

from typing import Any


VILLA_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "المنازل",      "kind": "home"},
        {"slug": "collezione", "label": "المجموعة",     "kind": "blog_list"},
        {"slug": "territorio", "label": "الأقاليم",     "kind": "about"},
        {"slug": "studio",     "label": "المكتب",       "kind": "team"},
        {"slug": "esperienza", "label": "التجربة",      "kind": "services"},
        {"slug": "concierge",  "label": "الكونسيرج",    "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":   "V",
        "logo_word":      "Villa Prestige",
        "logo_subline":   "استشارات خاصة · منذ عام 1998",
        "tag":            "مجموعة ربيع 2026 · المحفظة رقم 03",
        "phone":          "concierge@villaprestige.it",
        "phone_label":    "خط الكونسيرج السري",
        "email":          "concierge@villaprestige.it",
        "email_label":    "كونسيرج خاص",
        "address":        "Via Montenapoleone 17 · 20121 ميلانو",
        "hours_compact":  "المعاينة بموعد فقط · الإثنين–الجمعة 10–19 · السبت عند الطلب",
        "hours_footer_rows": [
            "استقبال في مكاتبنا · كونسيرج خاص",
            "اللغات: الإيطالية · English · Français",
        ],
        "license":        "قيد RIEA ميلانو رقم 2841 · الرقم الضريبي IT07324110984 · سجل المستشارين الخاصين",
        "footer_intro":
            "Villa Prestige — مكتب استشارات خاصة للمنازل المميزة في إيطاليا والريفيرا الفرنسية. "
            "محفظة ضيّقة، مُخاطَب واحد، كتمان مطلق. نختار المنازل التاريخية والمعاصرة حصراً لعملاء "
            "من الأُسر الخاصة ومكاتب الإدارة الأسرية، بعد تقييم على مستويَين: البصمة المعمارية "
            "وتماسك الإقليم.",

        # Nav reservation CTA (private viewing)
        "nav_cta":         "طلب معاينة خاصة",
        "nav_cta_kind":    "appointment",
        "nav_cta_short":   "طلب معاينة",

        # Footer labels
        "foot_studio":   "المكتب",
        "foot_pages":    "خريطة الموقع",
        "foot_contact":  "الكونسيرج",
        "foot_offices":  "المقرّات",
        "offices_footer_rows": [
            "ميلانو · Montenapoleone 17",
            "Portofino · مكتب الكونسيرج",
            "Saint-Tropez · بموعد",
        ],
        "office_rows": [
            "ميلانو · Montenapoleone 17",
            "Portofino · مكتب الكونسيرج",
            "Saint-Tropez · بموعد",
        ],

        # Cross-page editorial meta-strip labels (D-047)
        "dossier_label":        "الملف",
        "portfolio_label":      "المحفظة",
        "territorio_label":     "الإقليم",
        "superficie_label":     "المساحة",
        "provenance_label":     "البصمة",
        "access_label":         "المدخل",
        "availability_label":   "الإتاحة",
        "price_note":           "السعر عند الطلب",
        "nda_required_label":   "اتفاقية عدم إفشاء مطلوبة قبل تسليم الملف",
        "viewing_on_request":   "متاحة بموعد فقط",
        "referent_label":       "مُخاطَب واحد",
        "concierge_line_label": "خط الكونسيرج",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # Fullbleed editorial cover
        "cover_location": "بورتوفينو · لِيغوريا Portofino, Liguria",
        "cover_image_credit": "مجموعة الربيع · الملف 03 / 18",
        "cover_image":
            "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=2200&h=1400&fit=crop",

        # Eyebrow + serif drama
        "eyebrow":          "Villa Prestige · استشارات خاصة · إيطاليا والريفيرا الفرنسية",
        "headline":         "منازل <em>ذات توقيع</em>، لمن يُحسن قراءتها.",
        "sub":
            "محفظة ضيّقة من المنازل الخاصة — تاريخية ومعاصرة — تُقدَّم بموعد فقط. معاينات سرية، "
            "ملف تحريري مُكرَّس، مفاوضة هادئة: من اللقاء الأول إلى التوقيع أمام الموثّق، مُخاطَب واحد.",

        # Hero wordmark + counter chip (from DNA)
        "hero_wordmark":        "Villa Prestige",
        "hero_location":        "بورتوفينو · مجموعة ربيع 2026",
        "hero_counter_label":   "المنزل الحاضر",
        "hero_counter_value":   "رقم 03 / 18",
        "hero_series_label":    "في الواجهة",
        "hero_series_title":    "« Villa Aurelia » · بورتوفينو",
        "hero_series_note":
            "منزل تاريخي من عام 1922، حديقة من ثلاثة هكتارات مطلّة على الخليج. أربعمائة متر مربع، "
            "مكتبة ذات توقيع، مسبح لا نهائي مطلّ على جزيرة بالماريا.",
        "primary_cta":          "طلب معاينة خاصة",
        "primary_cta_href":     "concierge",
        "secondary_cta":        "مجموعة الربيع",
        "secondary_cta_href":   "collezione",

        # Editorial credit cells — fullbleed hero bottom strip
        "hero_credit_cells": [
            ("المجموعة", "رقم 03 / 18"),
            ("الإقليم",  "بورتوفينو · لِيغوريا"),
            ("المساحة",  "400 م² · حديقة 30.000 م²"),
            ("المدخل",   "بموعد فقط"),
        ],

        # Signature properties strip — 4 dossier cards (2-up editorial grid)
        "signature_label":   "مجموعة الربيع",
        "signature_heading": "منازل <em>مختارة</em> لهذا الموسم.",
        "signature_intro":
            "كل عقار لا يُقدَّم إلا بعد تقييم على مستويَين — البصمة المعمارية وتماسك الإقليم. "
            "القائمة الكاملة مُتاحة عند الطلب، في صيغة ملف تحريري موقّع من المُخاطَب المُكرَّس.",
        "signature": [
            {
                "index":       "01",
                "title":       "Villa Aurelia",
                "territorio":  "بورتوفينو · لِيغوريا",
                "superficie":  "400 م² · حديقة 30.000 م²",
                "provenance":  "عشرينيات القرن العشرين · توقيع بياتشينتيني",
                "availability":"ثلاثة أيام متاحة",
                "slug":        "villa-aurelia-portofino",
                "image":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "02",
                "title":       "Castello di Monterò",
                "territorio":  "Chianti Classico · توسكانا",
                "superficie":  "1.200 م² · 18 هكتاراً",
                "provenance":  "القرن الثاني عشر · ترميم 2014",
                "availability":"حصرية",
                "slug":        "castello-di-montero-chianti",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "03",
                "title":       "Penthouse Quadronno",
                "territorio":  "ميلانو · Magenta",
                "superficie":  "380 م² · شرفة 180 م²",
                "provenance":  "شقة علوية فريدة · مطلّة على الدومو",
                "availability":"بموعد",
                "slug":        "penthouse-quadronno-milano",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "index":       "04",
                "title":       "Mas de la Mer",
                "territorio":  "Saint-Tropez · الريفيرا الفرنسية",
                "superficie":  "550 م² · كرم خاص",
                "provenance":  "القرن الثامن عشر · موثّق",
                "availability":"جديد",
                "slug":        "mas-de-la-mer-saint-tropez",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "signature_link_all":  "عرض المجموعة الكاملة  ←",
        "signature_link_href": "collezione",

        # Territory ribbon — continental destinations
        "territory_label":  "الأقاليم المرجعية",
        "territory":        ["PORTOFINO", "CHIANTI CLASSICO", "COSTA SMERALDA", "LAGO DI COMO", "SAINT-TROPEZ", "CAPRI", "VAL D'ORCIA"],

        # Private advisor block
        "advisor_label":    "المستشار الخاص",
        "advisor_heading":  "<em>مُخاطَب</em> واحد، من الملف الأول إلى توقيع الموثّق.",
        "advisor_intro":
            "يُتابَع كل عميل خاص شخصياً من قِبَل مستشاره، من تسليم الملف التحريري الأول إلى "
            "التوقيع أمام الموثّق. لا يتجاوز عدد التوكيلات الفاعلة ثمانية لكل مستشار، ضماناً "
            "لحضور فعلي وكتمان تام.",
        "advisor_name":     "Alessandra Visconti di Modrone",
        "advisor_role":     "مديرة العملاء الخاصين · منذ 2011",
        "advisor_bio":
            "خمس عشرة سنة بين Savills وKnight Frank وSotheby's International Realty "
            "(لندن · ميلانو · بورتوفينو). أشرفت شخصياً على أكثر من ثمانين صفقة خاصة في "
            "إيطاليا والريفيرا الفرنسية لأُسر أوروبية وأميركية وآسيوية. ترافق كل عميل منها "
            "من اللقاء السري الأول حتى التوقيع أمام الموثّق.",
        "advisor_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
        "advisor_cta":      "طلب محادثة أولى",
        "advisor_cta_href": "concierge",

        # Editorial storytelling — the maison's numbers (discreet stats — counters OK)
        "numbers_label":    "المكتب بالأرقام",
        "numbers_heading":  "محفظة <em>ضيّقة</em>، حضور كامل.",
        "numbers": [
            ("26",   "عاماً من الاستشارات الخاصة"),
            ("42",   "منزلاً في المحفظة"),
            ("9",    "مستشارين خاصين مُكرَّسين"),
            ("150",  "مكتب إدارة أسرية مرافَقاً"),
        ],
        "numbers_note":
            "لا تتجاوز التوكيلات خمسين في آنٍ واحد. كل ملف يمرّ بمكتب الإدارة قبل الدخول في المجموعة.",

        # Press ribbon
        "press_label":    "تحريرياً",
        "press_intro":    "ظهر في",
        "press_items":    [
            "Financial Times · How to Spend It",
            "Monocle",
            "Robb Report",
            "Corriere Living",
            "AD Italia",
        ],

        # Editorial storytelling panel — closing private-viewing band
        "private_label":    "معاينة خاصة",
        "private_heading":  "ساعة في قاعة محجوزة، <em>والملف بين يديك.</em>",
        "private_intro":
            "يتمّ اللقاء في مكاتبنا بموعد، وبحضور المُخاطَب المُكرَّس. نُعدّ مسبقاً الملفات "
            "التحريرية للمنازل الملائمة لصورة العميل، ونحجز قاعة تُعرض فيها المَشاهد على "
            "شاشة كبيرة. الخدمة بلا مقابل، وسرية تماماً.",
        "private_primary":       "طلب معاينة خاصة",
        "private_primary_href":  "concierge",
        "private_secondary":     "اكتشاف التجربة",
        "private_secondary_href":"esperienza",
    },

    # ─── COLLEZIONE — signature properties list (blog_list) ───
    "collezione": {
        "eyebrow":   "مجموعة ربيع 2026 · الملفات من 01 إلى 14",
        "headline":  "أربعة عشر <em>منزلاً ذا توقيع</em>، في انتظار مُخاطِبها.",
        "intro":
            "المجموعة مفتوحة حصراً للعملاء الموقّعين على اتفاقية عدم إفشاء. يتضمن كل ملف "
            "بصمة معمارية موثّقة، ومخططاً تحريرياً، والإقليم، ونبذة تاريخية موجزة عن المنزل. "
            "تُبلَّغ الأسعار مباشرةً من المُخاطَب بعد اللقاء السري الأول.",

        # Lead post / hero dossier
        "lead_image":
            "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=1600&h=1000&fit=crop",

        # Filters by territorio / provenance / availability
        "filter_label":  "التصفية",
        "filter_groups": [
            {
                "label":   "الإقليم",
                "options": ["الكلّ", "بورتوفينو", "Chianti Classico", "ميلانو", "الريفيرا الفرنسية", "كابري", "Lago di Como", "Val d'Orcia"],
            },
            {
                "label":   "البصمة",
                "options": ["الكلّ", "القرنان السابع عشر–الثامن عشر", "مطلع القرن العشرين · توقيع معماري", "معاصر · ترميم حديث", "شقة علوية فريدة"],
            },
            {
                "label":   "الإتاحة",
                "options": ["مفتوحة", "جديد", "حصرية", "بموعد فقط"],
            },
        ],
        "sort_label":    "ترتيب حسب",
        "sort_options":  ["الإقليم", "البصمة", "الأحدث", "الحصريات"],

        "result_count":    "14 ملفاً في مجموعة الربيع",
        "result_subtitle": "يُحدَّث كل أول خميس من الشهر",

        "footer_note_label": "الدخول في المجموعة",
        "footer_note":
            "تُفتح مجموعة صيف 2026 يوم الخميس 28 أيار. للعملاء الموقّعين على اتفاقية عدم إفشاء "
            "أولوية مطلقة على كل ملف جديد. للانضمام إلى القائمة السرية، يُرجى الكتابة مباشرةً "
            "إلى كونسيرج الدار.",
    },

    # ─── TERRITORIO (about) — editorial territorio cards ──────
    "territorio": {
        "eyebrow":   "الأقاليم المرجعية · سبع جغرافيات خاصة",
        "headline":  "<em>المَشهد</em> هو التوقيع الأول لأيّ منزل.",
        "intro":
            "نعمل حصراً في سبعة أقاليم إيطالية وفرنسية. لكلٍّ منها مُخاطَب مقيم، وأرشيف تحريري "
            "مُكرَّس، وشبكة من المعماريين الموثوقين. لا نشتغل خارج هذه الجغرافيات — وبذلك نضمن "
            "معرفة حقيقية بالبيوت، وبالجيران، وبالرياح السائدة.",

        # Editorial statement
        "statement_label":   "بيان",
        "statement_heading": "سبعة أقاليم، <em>سبعة أرشيفات خاصة.</em>",
        "statement_text":
            "يُتابِع كل إقليم مُخاطَبٌ مقيم فيه منذ عشر سنوات على الأقل. نعرف المنازل قبل أن "
            "تدخل السوق — وكثيراً ما تابعناها عبر أجيال من الملاك. يضمّ أرشيفنا السجلات "
            "العقارية التاريخية، والدراسات المَشهدية، وعلاقات مع البلديات ودواوين حماية "
            "التراث المعنية.",

        # 6 territorio cards — history, provenance, architects, property count
        "territories_label":   "الأقاليم السبعة",
        "territories_heading": "جغرافيات <em>المجموعة.</em>",
        "territories_intro":
            "من شبه جزيرة بورتوفينو إلى كروم Saint-Tropez، ومن تلال Chianti إلى ساحل "
            "Costa Smeralda. لكل إقليم موسم دخوله، وعموده المعماري، وسجلّه من الأُسر.",
        "territories": [
            {
                "name":      "بورتوفينو Portofino",
                "region":    "لِيغوريا · خليج التِيغولو",
                "history":   "شبه جزيرة ارتادتها الأُسر الميلانية منذ ما بعد الحرب الثانية. بيوت ساحلية مطلّة على الماء، شُرفات فوق خليج San Fruttuoso، حدائق مغلقة من الجهنمية وأشجار زيتون معمّرة. ضوء أواخر الربيع هو خير شاهد.",
                "architects":"Gio Ponti · Gae Aulenti · Umberto Riva · ترميمات حديثة بتوقيع A. Citterio",
                "count":     "9 منازل في المجموعة",
                "since":     "مُخاطَب مقيم منذ 2008",
                "image":
                    "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Chianti Classico",
                "region":    "توسكانا · Gaiole – Radda – Castellina",
                "history":   "عمود Chianti بين سيينا وفلورنسا، غنيٌّ بالقلاع القروسطية والكنائس القروية المُرمَّمة. منازل مسكونة بكروم منتجة، وبساتين زيتون معمّرة، وأقبية تحت الأرض. يُعلي الإقليم شأن الترميم المحافظ تحت إشراف ديوان حماية التراث في فلورنسا.",
                "architects":"ترميمات Tobia Scarpa · Massimo Carmassi · مكتب ACPV",
                "count":     "7 منازل في المجموعة",
                "since":     "مُخاطَب مقيم منذ 2011",
                "image":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Costa Smeralda",
                "region":    "سردينيا · Porto Cervo – Porto Rotondo",
                "history":   "ساحل رسمه في ستينيات القرن الماضي الأمير كريم آغا خان. فيلات صممها Jacques Couëlle وLuigi Vietti، بالغرانيت المحلي وسقوف العَرْعَر. شُرفات حجرية فوق البحر، وخلجان خاصة لا يُبلَغ إليها إلا مشياً أو بقارب صغير.",
                "architects":"Jacques Couëlle · Luigi Vietti · Savin Couëlle · ترميمات حديثة بتوقيع A. Citterio",
                "count":     "5 منازل في المجموعة",
                "since":     "مُخاطَب مقيم منذ 2014",
                "image":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Lago di Como",
                "region":    "لومبارديا · Cernobbio – Tremezzo – Bellagio",
                "history":   "فيلات البحيرة التاريخية، من Villa d'Este إلى Villa Balbianello. حدائق نباتية نُحتت في القرن الثامن عشر، ومراسٍ خاصة، ومشارف من الياسمين. عقارات مُقيَّدة في الغالب، وتَجري ترميماتها بالتنسيق مع ديوان حماية التراث في ميلانو.",
                "architects":"فيلات تاريخية · Pelagio Palagi · ترميمات Lissoni Casal Ribeiro",
                "count":     "6 منازل في المجموعة",
                "since":     "مُخاطَب مقيم منذ 2010",
                "image":
                    "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Saint-Tropez",
                "region":    "الريفيرا الفرنسية · Var · Pampelonne",
                "history":   "Var الداخلي، تلال بين Ramatuelle وGassin. ماس بروفنسية أصيلة من القرنين السابع عشر والثامن عشر، بعضها يضمّ كرماً منتجاً بتسمية AOP Côtes de Provence. بيوت على مسافة مُتحفِّظة من البحر، نصف ساعة من ميناء Saint-Tropez.",
                "architects":"François Catroux · Jacques Grange · Studio KO · ترميمات تقليدية",
                "count":     "4 منازل في المجموعة",
                "since":     "مكتب كونسيرج منذ 2016",
                "image":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
            {
                "name":      "Capri & Val d'Orcia",
                "region":    "كابري · جنوب توسكانا · Pienza – Montalcino",
                "history":   "إقليمان تَوأَمان في الندرة وحُسن الحفظ الأسري. في كابري، بيوت مُدرَّجة في اتجاه الفاراليوني، تُتوارث عبر ثلاثة أجيال. في Val d'Orcia، ضِياع زراعية بكنيسة قروية رومانية وكرم من Brunello، عقارات تراث UNESCO تحت حماية صارمة.",
                "architects":"كابري · Francesco Venezia · التقليد الكابري المحلي؛ Val d'Orcia · Matteo Nunziati · Studio Perruccio",
                "count":     "5 منازل في المجموعة",
                "since":     "مُخاطَبون مقيمون منذ 2013",
                "image":
                    "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",
            },
        ],
        "territory_card_cta": "طلب ملف الإقليم  ←",
        "territory_card_cta_href": "concierge",

        # Closing — the referent promise
        "referent_label":   "المُخاطَب المقيم",
        "referent_heading": "نعرف البيوت <em>قبل</em> أن تدخل السوق.",
        "referent_text":
            "ليس المُخاطَب المقيم مستشاراً عند الطلب: بل هو شخص يعيش الإقليم منذ عشر سنوات "
            "على الأقل، يتحدّث اللسان المحلي، ويعرف دواوين حماية التراث والأُسر العريقة. "
            "كثير من منازل المجموعة يأتينا بكلمة صديق مشترك، لا من السوق — هكذا كانت "
            "تَنتقل هذه العقارات دوماً، بين أشخاص يثق بعضهم ببعض.",

        # Discreet stats — territories in numbers
        "stats_label":      "الأقاليم بالأرقام",
        "stats": [
            ("7",   "أقاليم مرجعية"),
            ("36",  "منزلاً تاريخياً في الأرشيف"),
            ("18",  "معمارياً ذا توقيع شريكاً"),
            ("26",  "عاماً من الحضور المتواصل"),
        ],
    },

    # ─── STUDIO (team) — private advisors ─────────────────────
    "studio": {
        "eyebrow":  "المكتب · تسعة مستشارين خاصين · ميلانو بورتوفينو Saint-Tropez",
        "headline": "تسعة مستشارين، <em>لا يتجاوز كلٌّ منهم ثمانية توكيلات.</em>",
        "intro":
            "المكتب دار من المستشارين الخاصين: كلّ منّا له جذور مهنية في الدور الدولية "
            "الكبرى — Sotheby's International Realty وKnight Frank وSavills وChristie's "
            "Real Estate — ويعمل اليوم باستقلال تام، بمحفظة ضيّقة. لا نرفع راية دار، "
            "بل ملفات فقط. ولا نبيع شيئاً تحت ضغط.",

        # Director hero card — Alessandra Visconti
        "director_label":   "الإدارة",
        "director_name":    "Alessandra Visconti di Modrone",
        "director_role":    "مديرة العملاء الخاصين · مؤسِّسة · منذ 1998",
        "director_text":
            "أسَّست Villa Prestige في ميلانو عام 1998، بعد ثماني سنوات في Sotheby's "
            "International Realty لندن. أشرفت شخصياً على أكثر من ثمانين صفقة خاصة في "
            "إيطاليا والريفيرا الفرنسية — من Villa Aurelia في بورتوفينو إلى Castello di "
            "Monterò في Chianti — لأُسر أوروبية وأميركية وآسيوية ومن الشرق الأوسط. تُوقِّع "
            "في Monocle وCorriere Living عموداً سنوياً عن سوق المنازل التاريخية.",
        "director_portrait":
            "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=800&h=1100&fit=crop",
        "director_quote":
            "«لا نختار المنازل لِسِعرها. نختار المنازل التي تَبقى في ذاكرتنا بعد زيارة واحدة. "
            "ثمانون في المئة من العقارات التي تَردنا تُستَبعد قبل الدخول في المجموعة.»",
        "director_quote_attribution": "Alessandra Visconti di Modrone · Monocle · آذار 2025",

        # 4 private advisors
        "advisors_label":   "المستشارون الخاصون",
        "advisors_heading": "<em>مُخاطَب واحد</em>، من الملف الأول إلى توقيع الموثّق.",
        "advisors_intro":
            "يُرافَق كل عميل شخصياً من قِبَل مستشار يُعيَّن في بداية التوكيل. لا وسيط أبداً، "
            "ولا انتقالاً للمرافقة. وإن رغب العميل في رأي ثانٍ، أتاح المكتب مستشاراً ثانياً "
            "بصفة استشارية، دائماً تحت سقف الكتمان نفسه.",
        "advisors": [
            {
                "name":      "Francesco Medici di Porrena",
                "role":      "مستشار أول · إقليم Chianti وVal d'Orcia",
                "bio":
                    "اثنتا عشرة سنة في Knight Frank فلورنسا، متخصص في الترميم المحافظ "
                    "للمنازل التاريخية في Chianti Classico. إجازة في العمارة من فلورنسا، "
                    "وماجستير من Bartlett في لندن. يُشرف شخصياً على كل المفاوضات في توسكانا "
                    "الجنوبية.",
                "territories":"Chianti Classico · Val d'Orcia · فلورنسا",
                "since":     "في المكتب منذ 2014",
                "portrait":
                    "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "الإيطالية · English · Français",
            },
            {
                "name":      "Élodie Charbonneau",
                "role":      "مستشارة أولى · إقليم الريفيرا الفرنسية وكابري",
                "bio":
                    "عشر سنوات في Savills باريس وChristie's Real Estate Monte-Carlo. "
                    "مُنسِّقة بيوع خاصة لهواة جمع فرنسيين وأميركيين في الريفيرا الفرنسية. "
                    "متخصصة في الماس البروفنسية الأصيلة والفيلات ذات التوقيع. مسؤولة مكتب "
                    "الكونسيرج في Saint-Tropez.",
                "territories":"Saint-Tropez · موناكو · كابري",
                "since":     "في المكتب منذ 2016",
                "portrait":
                    "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "Français · English · الإيطالية",
            },
            {
                "name":      "Arianna Testa Piccolomini",
                "role":      "مستشارة أولى · إقليم بورتوفينو وLago di Como",
                "bio":
                    "ثماني سنوات في Sotheby's International Realty ميلانو، ثم مستشارة "
                    "مستقلة لمكتبَي إدارة أسرية في Brescia وPiemonte. مقيمة في بورتوفينو "
                    "منذ عشر سنوات، تعرف شخصياً الأُسر العريقة في شبه الجزيرة. لغات العمل: "
                    "الإيطالية والإنكليزية والألمانية.",
                "territories":"بورتوفينو · Lago di Como · ميلانو",
                "since":     "في المكتب منذ 2017",
                "portrait":
                    "https://images.pexels.com/photos/1438834/pexels-photo-1438834.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "الإيطالية · English · Deutsch",
            },
            {
                "name":      "Omar Khoury",
                "role":      "مستشار عملاء خاصين · العملاء الآسيويون وعملاء الشرق الأوسط",
                "bio":
                    "تسع سنوات بين Knight Frank دبي وChristie's Hong Kong. متخصص في "
                    "استقبال العملاء الخاصين من هونغ كونغ وسنغافورة والدوحة والرياض ودبي. "
                    "يُنسِّق الترجمات والتوثيقات الدولية لدى الموثّقين. مقيم بين ميلانو "
                    "وبورتوفينو.",
                "territories":"عملاء آسيويون · الإمارات · الخليج العربي",
                "since":     "في المكتب منذ 2019",
                "portrait":
                    "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
                "langs":     "العربية · English · Français · 中文 (مبادئ)",
            },
        ],

        # Legal / fiscal partner ribbon
        "partners_label":   "شركاء مؤسَّساتيون",
        "partners_heading": "شركاء المكتب <em>القانونيون والجبائيون.</em>",
        "partners_intro":
            "لا تُحرِّر Villa Prestige العقود. تُرافَق كل مفاوضة بشركاء مؤسَّساتيين منتخبين "
            "— مكاتب توثيق، ومحامون دوليون، ومستشارون جبائيون في الثروات — يعملون تحت "
            "سقف الكتمان نفسه. يُوقِّع العميل معهم توكيلاً مباشراً، مستقلاً عن توكيلنا، "
            "بأتعاب شفافة.",
        "partners": [
            ("Studio Notarile Baldi-Corsini",     "ميلانو · موثّق الأُسر اللومباردية"),
            ("Gattai Minoli Agostinelli",         "ميلانو · القانون العقاري الدولي"),
            ("Chiomenti",                          "ميلانو · الجباية العائلية لمكاتب الإدارة الأسرية"),
            ("Ughi e Nunziante",                   "روما · التراث والممتلكات الثقافية"),
            ("Cabinet Bredin Prat",                "باريس · معاملات الريفيرا الفرنسية"),
        ],

        # Press / editorial mentions
        "press_label":   "تحريرياً",
        "press_heading": "الأصداء الأخيرة <em>للمكتب.</em>",
        "press_items": [
            {
                "magazine": "Financial Times · How to Spend It",
                "issue":    "ربيع 2026",
                "title":    "The quiet sellers of the Italian coast",
                "byline":   "ملامح · بقلم Bill Prince",
            },
            {
                "magazine": "Monocle",
                "issue":    "العدد 181",
                "title":    "The Chianti Classico revival",
                "byline":   "ريبورتاج · بقلم Josh Fehnert",
            },
            {
                "magazine": "Robb Report",
                "issue":    "نيسان 2025",
                "title":    "Nine villas, one director",
                "byline":   "ملامح · بقلم Laurie Kahle",
            },
            {
                "magazine": "Corriere Living",
                "issue":    "كانون الثاني 2026",
                "title":    "سوق المنازل التاريخية، كما يُرى من ميلانو",
                "byline":   "عمود سنوي · بتوقيع Alessandra Visconti di Modrone",
            },
            {
                "magazine": "AD Italia",
                "issue":    "تشرين الثاني 2025",
                "title":    "Villa Aurelia · عودة أيقونة من بورتوفينو",
                "byline":   "تصوير · Gianluca Ruotolo",
            },
        ],

        # Studio in numbers
        "numbers_label":   "المكتب بالأرقام",
        "numbers": [
            ("26",   "عاماً على التأسيس"),
            ("9",    "مستشارين خاصين مُكرَّسين"),
            ("42",   "منزلاً في المجموعة"),
            ("7",    "أقاليم مرجعية"),
            ("150",  "مكتب إدارة أسرية مرافَقاً"),
            ("91",   "صفقة خاصة منذ 2015"),
        ],

        # Closing visit CTA
        "visit_label":     "لقاء في مكاتبنا",
        "visit_heading":   "<em>محادثة سرية</em> أولى في مكتبَي ميلانو أو بورتوفينو.",
        "visit_text":
            "نستقبل حصراً بموعد، في مكتبَي ميلانو وبورتوفينو، أو في مكتب الكونسيرج في "
            "Saint-Tropez. اللقاء الأول محادثة سرية — لا يرتب أي توكيل — يُحدَّد خلالها "
            "ملمح العميل، وتُوقَّع اتفاقية عدم الإفشاء التي تفتح الوصول إلى الملفات.",
        "visit_primary":      "طلب المحادثة الأولى",
        "visit_primary_href": "concierge",
    },

    # ─── ESPERIENZA (services) — private-viewing process ─────
    "esperienza": {
        "eyebrow":  "التجربة · خمس مراحل في الكتمان",
        "headline": "من <em>الملف</em> الأول إلى توقيع الموثّق.",
        "intro":
            "نُرافق العميل عبر خمس مراحل، كلٌّ منها سرية وموثّقة. يَمتدّ المسار في المتوسط "
            "أربعة أشهر للعقارات الجاهزة للتوقيع، ويَصل إلى اثني عشر للمنازل التاريخية "
            "الخاضعة لقيود حماية المَشهد. لا مرحلة إلزامية — يَحقّ للعميل فسخ التوكيل في "
            "أي وقت دون غرامة.",

        # 5-step private-viewing process
        "process_label":   "المسار",
        "process_heading": "خمس مراحل، <em>مُخاطَب واحد.</em>",
        "process_intro":
            "كل مرحلة يتابعها شخصياً المستشار المُعيَّن في بداية التوكيل. يَحقّ للعميل في "
            "أي وقت أن يطلب التخاطب مع الإدارة — تُجيب Alessandra Visconti di Modrone "
            "شخصياً خلال يوم عمل.",
        "process": [
            {
                "n":        "01",
                "title":    "طلب الملف",
                "duration": "الرد خلال 48 ساعة عمل",
                "text":
                    "يَكتب العميل إلى الكونسيرج واصفاً ملمح المنزل المُبتغى — الإقليم "
                    "والبصمة والمساحة وموسم الاستخدام. يُجيب مستشار الإقليم خلال يومَي "
                    "عمل بموجز أول للمجموعة الملائمة، ومُقترح لقاء أولي.",
            },
            {
                "n":        "02",
                "title":    "اتفاقية عدم إفشاء",
                "duration": "يُوقَّع في المكتب أو عن بُعد",
                "text":
                    "قبل تسليم الملفات الكاملة، يُوقِّع العميل والمكتب اتفاقية عدم إفشاء "
                    "متبادلة تُلزم الطرفَين بكتمان تامّ حول العقارات والأُسر البائعة "
                    "والشروط المالية. الاتفاقية معيارية، ولا تمنع الاستعانة بمستشار "
                    "جبائي ثانٍ.",
            },
            {
                "n":        "03",
                "title":    "مكالمة مرئية تحريرية",
                "duration": "نصف يوم · مع المستشار",
                "text":
                    "لقاء أول عبر الفيديو — أو في المكتب إن فضَّل العميل — نستعرض خلاله "
                    "معاً ثلاثة أو أربعة ملفات تحريرية، بالمخططات وتاريخ المنزل وصور "
                    "محدَّثة وتقرير مَشهدي. يَختار العميل المنزلَين للزيارة الحضورية.",
            },
            {
                "n":        "04",
                "title":    "معاينة خاصة حضورية",
                "duration": "يوم إلى يومَين في الإقليم",
                "text":
                    "نُرافق العميل شخصياً إلى العقار، بحضور المُخاطَب المقيم، وحضور "
                    "الأسرة البائعة إن شاءت ذلك. المعاينة بلا ضغط تجاري: تستغرق ما يلزم "
                    "من وقت، وتشمل غداءً في الجوار، ويُمكن تكرارها مرة ثانية في موسم مختلف.",
            },
            {
                "n":        "05",
                "title":    "التفاوض والتوقيع",
                "duration": "من 45 يوماً إلى 6 أشهر",
                "text":
                    "يُحرّر المكتب عرض الشراء بالاتفاق مع العميل ويُقدّمه مباشرةً إلى "
                    "الأسرة البائعة. يُعدّ الشركاء الموثّقون العقد الابتدائي والعقد "
                    "النهائي. يُرافق المستشارُ العميلَ شخصياً إلى التوقيع، ويبقى تحت "
                    "تصرّفه ستة أشهر بعدها، لأيّ إجراء بعد التسليم.",
            },
        ],

        # Testimonial slot (single, editorial, discreet)
        "testimonial_label":   "شهادة",
        "testimonial_text":
            "«نُصحت بالمكتب من شريك سابق لي في لندن. طلبت محادثة أولى في ميلانو، وفي ستة "
            "أشهر اقتنَت أسرتنا فيلا في Costa Smeralda، دون أن تخرج المفاوضة يوماً عن "
            "دائرة الأشخاص الثلاثة المَعنيين. المُخاطَبة بقيت نفسها — تَعرف اليوم أبنائي "
            "أيضاً.»",
        "testimonial_author":  "مكتب إدارة أسرية لومباردي · اقتناء 2024 · Porto Cervo",

        # FAQ accordion
        "faq_label":   "أسئلة متكررة",
        "faq_items": [
            {
                "q": "كم يَستغرق المسار في المتوسط حتى التوقيع؟",
                "a": "من أربعة إلى اثني عشر شهراً، حسب تعقيد العقار. تُغلَق المنازل الجاهزة "
                     "للتوقيع في خمسة وأربعين يوماً؛ أما التاريخية منها، الخاضعة لحماية "
                     "المَشهد أو للتقسيم العقاري، فتتطلّب آجالاً أطول لتحقيقات ديوان "
                     "حماية التراث.",
            },
            {
                "q": "ما هي لغات عمل المكتب؟",
                "a": "الإيطالية والإنكليزية والفرنسية في كل مفاوضة. الألمانية لإقليم Lago "
                     "di Como، والعربية والصينية بمستوى أساسي لعملاء الشرق الأوسط وآسيا. "
                     "الترجمات المحلَّفة لكل الوثائق التوثيقية مشمولة بالتوكيل.",
            },
            {
                "q": "كيف تُحتسب أتعاب المكتب؟",
                "a": "دوماً كنسبة مئوية من السعر النهائي للاقتناء، مُبيَّنة بشفافية في "
                     "التوكيل الابتدائي. لا مبالغ ثابتة على العميل خلال مراحل الدراسة — "
                     "فقط عند التوقيع الفعلي أمام الموثّق.",
            },
            {
                "q": "هل يُمثِّل المكتب البائعين أيضاً؟",
                "a": "نعم، لكن ليس في آنٍ واحد على المنزل ذاته. كل توكيل حصري لأحد "
                     "الطرفَين، ضماناً لشفافية قصوى في المفاوضة. يَعلم العميل دوماً لأيّ "
                     "طرف نعمل.",
            },
            {
                "q": "هل يُمكن معاينة منزل أكثر من مرة؟",
                "a": "نعم، عند الطلب. نُرافق العميل بلا مقابل إلى زيارة ثانية في موسم "
                     "مختلف — كثير من العقارات الساحلية تُعايَن مرة في الصيف ومرة في "
                     "الشتاء قبل القرار.",
            },
            {
                "q": "كيف تحمون سرية المفاوضة؟",
                "a": "تُفتَح كل مفاوضة باتفاقية عدم إفشاء متبادلة، تُوقَّع في المكتب أو "
                     "عن بُعد، وتُلزم المكتب والعميل والأسرة البائعة. لا ملفّ متاح "
                     "بصيغة رقمية مفتوحة — كل الوثائق تُسلَّم عبر منصة محمية أو ورقياً.",
            },
        ],

        # Closing CTA
        "cta_label":      "محادثة أولى",
        "cta_heading":    "<em>المحادثة الأولى</em> دوماً بلا مقابل وسرية.",
        "cta_text":
            "لا توكيل مُستحَقّ بعد اللقاء الأول. يتلقّى العميل موجزاً أولاً للمجموعة "
            "الملائمة، ومقترح مستشار مُكرَّس، وتاريخاً استرشادياً للمعاينة الخاصة الأولى. "
            "وإن لم يكن الملمح ملائماً، شكرناه وانصرفنا — دون لواحق.",
        "cta_primary":      "طلب المحادثة الأولى",
        "cta_primary_href": "concierge",
    },

    # ─── CONCIERGE (contact) — private-viewing request ───────
    "concierge": {
        "eyebrow":  "كونسيرج خاص · بموعد",
        "headline": "بموعد <em>فقط</em>.",
        "intro":
            "نستقبل حصراً بموعد، في مكتبَي ميلانو وبورتوفينو، وفي مكتب الكونسيرج في "
            "Saint-Tropez. يقرأ الكونسيرج كل طلب شخصياً ويُجيب خلال يوم العمل التالي. "
            "للطلبات باللغة العربية أو الصينية أو الألمانية، يُوقَّع الرد مباشرةً من "
            "المستشار المُكرَّس لإقليم الاختصاص.",

        # Dedicated phone line by territorio
        "phone_label":    "خط الكونسيرج بحسب الإقليم",
        "phone_intro":
            "لكل إقليم خطّ مُكرَّس، مفتوح فقط للعملاء الموقّعين على اتفاقية عدم إفشاء أو "
            "المُزكَّين من مُرجِّع. للتواصل الأول، يُفضَّل دائماً الكتابة إلى الكونسيرج "
            "بالبريد الإلكتروني — الرد أسرع وأكثر توثيقاً.",
        "phone_rows": [
            ("ميلانو · الإدارة",                "concierge@villaprestige.it"),
            ("بورتوفينو · مكتب الكونسيرج",      "portofino@villaprestige.it"),
            ("Saint-Tropez · مكتب الكونسيرج",   "saint-tropez@villaprestige.it"),
            ("عملاء آسيويون · Omar Khoury",     "asia@villaprestige.it"),
        ],

        # Form section (private-viewing request with NDA consent)
        "form_section_label":  "طلب معاينة خاصة",
        "form_section_intro":
            "يُرجى تعبئة الحقول اللازمة بأناة. يُجيب الكونسيرج خلال يوم العمل التالي، "
            "بالإيطالية أو الإنكليزية أو الفرنسية. للطلبات بلغات أخرى، يُرجى الإشارة "
            "إلى اللغة المُفضَّلة في حقل الملاحظات.",

        "form_helper_required":  "الحقول المُعلَّمة إلزامية",
        "form_submit_button":    "إرسال طلب سري",
        "form_submit_note":
            "يُقرأ طلبك شخصياً من كونسيرج الإدارة. لا نشرة بريدية ولا اتصالات تجارية. "
            "تُمحى البيانات خلال تسعين يوماً إن لم يكن الملمح ملائماً للمجموعة.",

        "form_fields": [
            {"name":"titolo",    "label":"اللقب", "type":"select", "required":True,
             "options":["السيدة","السيد","مكتب · إدارة أسرية","صحافة · تحرير"]},
            {"name":"nome",      "label":"الاسم الكامل", "type":"text",
             "placeholder":"مثال: السيدة Eleonora Visconti", "required":True},
            {"name":"email",     "label":"بريد إلكتروني سري", "type":"email",
             "placeholder":"e.visconti@example.com", "required":True},
            {"name":"telefono",  "label":"الهاتف (اختياري)", "type":"tel",
             "placeholder":"+971 …", "required":False},
            {"name":"sede",      "label":"المكتب المُفضَّل", "type":"select", "required":True,
             "options":["ميلانو · Montenapoleone","بورتوفينو · الكونسيرج","Saint-Tropez · الكونسيرج","مكالمة مرئية تمهيدية","لا أفضّل مكتباً بعينه"]},
            {"name":"territorio","label":"الإقليم المهتم به", "type":"select", "required":True,
             "options":["بورتوفينو · لِيغوريا","Chianti Classico · توسكانا","Costa Smeralda · سردينيا","Lago di Como · لومبارديا","Saint-Tropez · الريفيرا الفرنسية","كابري · كامبانيا","Val d'Orcia · توسكانا","إقليمان أو أكثر"]},
            {"name":"profilo",   "label":"ملمح المنزل", "type":"select", "required":True,
             "options":["منزل تاريخي بحديقة","شقة علوية أو بنتهاوس حَضَري","فيلا معاصرة ذات توقيع","ضيعة زراعية بكرم","عقار ساحلي","لا ملمح محدَّد مسبقاً"]},
            {"name":"date",      "label":"تواريخ مُفضَّلة", "type":"text",
             "placeholder":"مثال: الأسبوع الثاني من أيار · أو في بداية الموسم", "required":False},
            {"name":"note",      "label":"ملاحظات للكونسيرج", "type":"textarea",
             "placeholder":"يُرجى الإشارة إلى تفضيل اللغة، والمُرجِّع الذي يُقدِّمك، وإتاحات الأسرة.", "required":True, "rows":5},
            {"name":"nda",       "label":"أوافق على توقيع اتفاقية عدم إفشاء متبادلة قبل تسليم الملفات التحريرية", "type":"checkbox", "required":True},
        ],

        # Office cards — three concierge offices
        "offices_label":   "المقرّات",
        "offices_heading": "ثلاثة مقرّات، <em>ثلاث قاعات محجوزة.</em>",
        "offices_intro":
            "كل مقرّ لا يستقبل إلا بموعد، في قاعة محجوزة بأرشيف تحريري محلي. مكتب "
            "ميلانو هو الإدارة العامة؛ أما بورتوفينو وSaint-Tropez فيتولّاهما في "
            "الموسم المُخاطَبان المقيمان.",
        "offices": [
            {
                "city":    "ميلانو",
                "address": "Via Montenapoleone 17 · 20121 ميلانو",
                "hours":   "الإثنين – الجمعة · 10:00 – 19:00 · بموعد فقط",
                "email":   "concierge@villaprestige.it",
                "role":    "الإدارة · الأرشيف المركزي · لقاءات في المكتب",
            },
            {
                "city":    "بورتوفينو",
                "address": "Via Roma 28 · 16034 Portofino GE",
                "hours":   "نيسان – تشرين الأول · معاينة بموعد · تشرين الثاني – آذار عند الطلب",
                "email":   "portofino@villaprestige.it",
                "role":    "مكتب الكونسيرج · مُخاطَب مقيم · لِيغوريا",
            },
            {
                "city":    "Saint-Tropez",
                "address": "Place de la Garonne 6 · 83990 Saint-Tropez",
                "hours":   "أيار – أيلول · معاينة بموعد · تشرين الأول – نيسان عند الطلب",
                "email":   "saint-tropez@villaprestige.it",
                "role":    "مكتب الكونسيرج · مُخاطَب مقيم · الريفيرا الفرنسية",
            },
        ],

        # Press contact ribbon
        "press_contact_label":   "تواصل صحافي",
        "press_contact_text":
            "للطلبات التحريرية وطلبات الصحافة المتخصصة، يُرجى الكتابة مباشرةً إلى "
            "الإدارة: stampa@villaprestige.it. تُنسَّق البيانات الصحفية والمِلفات "
            "المصوَّرة والمقابلات شخصياً من قِبَل المديرة. نُجيب الصحافة الدولية خلال "
            "يوم عمل، بالإيطالية أو الإنكليزية أو الفرنسية.",
        "press_contact_email":   "stampa@villaprestige.it",
    },

    # ─── BLOG POSTS (used by collezione blog_list + blog_detail) ──
    # These render the signature properties as editorial dossiers.
    "posts": [
        {
            "slug":     "villa-aurelia-portofino",
            "kicker":   "بورتوفينو · لِيغوريا · عشرينيات القرن العشرين",
            "title":    "Villa Aurelia — منزل تاريخي من عام 1922 على شبه الجزيرة",
            "lede":
                "أربعمائة متر مربع مطلّة على خليج التِيغولو، حديقة من ثلاثة هكتارات، مكتبة "
                "ذات توقيع، ومسبح لا نهائي معلَّق فوق جزيرة بالماريا.",
            "date":     "12 نيسان 2026",
            "read_min": "7",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 03 / 18 · ربيع 2026"),
                ("الإقليم",   "بورتوفينو · لِيغوريا · خليج التِيغولو"),
                ("المساحة",   "400 م² داخلية · حديقة 30.000 م² · 7 غرف نوم"),
                ("البصمة",    "1922 · توقيع Marcello Piacentini · ترميم A. Citterio 2014"),
                ("الإتاحة",   "ثلاثة أيام في الشهر · بموعد"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "يَفتح المنزل بوابته المركبة على صعود مُظلَّل ببلوط سنديان معمَّر، ولا "
                 "يَنكشف إلا بعد ثلاثمائة متر، مطلّاً على خليج التِيغولو من ارتفاع ستين "
                 "متراً. المُسقَط على شكل حَدوَة خيل، بجسم مركزي من 1922 وجناحَين أُضيفا "
                 "عام 1938 بتوقيع Marcello Piacentini ذاته. تدخُّل 2014 — بإدارة "
                 "Antonio Citterio ومع المعماري المَشهدي Paolo Pejrone للحديقة — أبقى "
                 "على كل الجداريات الأصلية في القاعة المركزية، ورَدّ الأصل لإطارات "
                 "النوافذ الخشبية المصمَّتة، واستحدث المسبح اللانهائي الذي بات اليوم من "
                 "الصور الأيقونية لشبه الجزيرة."),
                ("h2", "الحديقة · ثلاثة هكتارات من السنديان والزيتون والكاميليا"),
                ("p",
                 "الحديقة، التي صممها أصلاً الكونت Ricci عام 1924 وراجعها Paolo "
                 "Pejrone في 2014، تُواكب بين بلوط سنديان معمَّر، وبساتين زيتون منتجة، "
                 "ومجموعة من اثنتَين وثلاثين سُلالة من الكاميليا. للمنزل درج خاص "
                 "يَنحدر مباشرةً إلى البحر، بمَرسى لقوارب يَصل طولها إلى ثمانية أمتار. "
                 "الحديقة مكتفية ذاتياً في الرَي بفضل صهريج لجمع مياه الأمطار رُمِّم "
                 "عام 2018."),
                ("h2", "الداخل · مكتبة ذات توقيع وقاعة استقبال"),
                ("p",
                 "في الطابق النبيل تَتمفصَل القاعة المركزية على 140 متراً مربعاً، "
                 "بجداريات أصلية من مدرسة لِيغوريا، وغرفة طعام مطلّة على البحر، "
                 "والمكتبة ذات التوقيع، بألواح جوز نُحتت عام 1938. في الطابق الأول، "
                 "يَشغل الجناح الرئيسي الشرقي بأكمله مع حمّام خاص من رخام كارارا "
                 "وشُرفة مطلّة على جزيرة بالماريا. ست غرف أخرى تتوزَّع بين الطابقَين "
                 "الأول والثاني، لكلٍّ منها حمّامها."),
                ("blockquote",
                 "«فيلا بورتوفينو ليست عقاراً: إنها إيماءة تحفُّظ تَتوارَث بين أُسر "
                 "يثق بعضها ببعض. دورنا لا يعدو صون المُرور.»"),
                ("h2", "البصمة · يد Piacentini، وترميم Citterio"),
                ("p",
                 "كُلِّف بها عام 1921 المعماريُّ Marcello Piacentini من الأسرة "
                 "الجنوية Acquarone — وكان قد وقَّع تدخُّلات عدة على الواجهة البحرية "
                 "لفياريدجو — واكتَمَلت Villa Aurelia عام 1922، وظلَّت في الأسرة "
                 "ذاتها ثلاثة أجيال. انتَقَلت عام 2007 إلى أسرة ميلانية ثانية، التي "
                 "كلَّفت عام 2014 Antonio Citterio بالترميم المحافظ، وPaolo Pejrone "
                 "بالحديقة. نُشر التدخُّل في AD Italia وElle Decor وCorriere Living."),
                ("ol", [
                    "المدخل: طريق خاص ببوابة مركبة، وإشراف مَشهدي من ديوان حماية التراث في جنوة.",
                    "الحديقة: ثلاثة هكتارات · درج خاص إلى البحر · مَرسى لقوارب حتى ثمانية أمتار.",
                    "المساحة الداخلية: أربعمائة متر مربع · سبع غرف نوم · حمّامات من رخام كارارا.",
                    "التجهيزات: تدفئة جيوحرارية · لوحات كهروضوئية قليلة الأثر البصري · صهريج مياه الأمطار.",
                    "السعر: عند الطلب إلى المُخاطَب · اتفاقية عدم إفشاء مطلوبة قبل الملف الكامل.",
                ]),
                ("p",
                 "الإتاحة لا تتجاوز ثلاثة أيام في الشهر للمعاينات الخاصة، بحضور الأسرة "
                 "المالكة. المستشارة المُكرَّسة للإقليم — Arianna Testa Piccolomini، "
                 "المقيمة في بورتوفينو منذ عشر سنوات — تُرافق العميل شخصياً من أول "
                 "مكالمة مرئية إلى التوقيع أمام الموثّق."),
            ],
            "footer_strap": "Villa Prestige · بورتوفينو · الملف رقم 03 / 18",
        },
        {
            "slug":     "castello-di-montero-chianti",
            "kicker":   "Chianti Classico · توسكانا · القرن الثاني عشر",
            "title":    "Castello di Monterò — قلعة قروسطية بكرم منتج",
            "lede":
                "ألف ومائتا متر مربع على ثمانية عشر هكتاراً، كرم من Chianti Classico في "
                "إدارة حيوية دينامية، قبو تحت الأرض، وكنيسة مُكرَّسة من عام 1432.",
            "date":     "5 نيسان 2026",
            "read_min": "9",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 07 / 18 · ربيع 2026"),
                ("الإقليم",   "Chianti Classico · توسكانا · Gaiole in Chianti"),
                ("المساحة",   "1.200 م² داخلية · 18 هكتاراً · 7 هكتارات كرم"),
                ("البصمة",    "القرن الثاني عشر · ترميم محافظ Tobia Scarpa 2014"),
                ("الإتاحة",   "حصرية · توكيل واحد فاعل"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "تَقف القلعة على جبل بارتفاع 520 متراً بين Gaiole in Chianti وRadda، "
                 "مطلّةً جنوباً على وادي الأربيا، وشمالاً على تلال San Polo. الجسم "
                 "المركزي، ببرج مراقبة من عام 1185، بقي في معظمه على حاله منذ "
                 "التشييد الأول؛ وترميم 2014، بإدارة Tobia Scarpa وبإشراف ديوان "
                 "حماية التراث في فلورنسا، جعل الألف ومائتَي متر مربع الداخلية "
                 "صالحة للسكن دون المساس بحجر واحد من الغلاف القروسطي."),
                ("h2", "الضَيعة · ثمانية عشر هكتاراً، كرم في إدارة حيوية دينامية"),
                ("p",
                 "يَمتدّ العقار على ثمانية عشر هكتاراً، سبعة منها مخصَّصة لكرم "
                 "Chianti Classico DOCG، في إدارة حيوية دينامية موثَّقة منذ 2016. "
                 "الإنتاج السنوي نحو خمس عشرة ألف قارورة، تُوزَّع حصراً بتخصيص "
                 "خاص — لا في السوق. القبو تحت الأرض، المحفور أسفل الجسم المركزي، "
                 "يَضمّ ثلاثين برميلاً ومجموعة تاريخية من ألفَي قارورة."),
                ("h2", "الجسم المركزي · قاعة الأسلحة وكنيسة 1432"),
                ("p",
                 "في الطابق الأرضي تَتمفصَل قاعة الأسلحة على 180 متراً مربعاً، "
                 "والكنيسة الخاصة المُكرَّسة عام 1432 (ما زالت مُستخدَمة سنوياً "
                 "في 24 حزيران، عيد الشفيع)، والمطبخ التاريخي بفرن حطبه الأصلي. "
                 "يَحتضن الطابق الأول المكتبة العائلية بثلاثة آلاف مُجلَّد، "
                 "وخمس غرف نوم رئيسية، وصالتَين. في الطابق الثاني، حُوِّل برج "
                 "المراقبة إلى مكتب خاص مُطلٍّ على الوادي بزاوية ثلاثمائة وستين درجة."),
                ("blockquote",
                 "«القلعة ليست للبيع لأن الأسرة بحاجة إلى مال. هي للبيع لأن الجيل "
                 "القادم يَسكن بين لندن وشنغهاي، ونشعر بالحاجة إلى تسليمها لمن "
                 "سيَعرف كيف يَحمل أَمانتها.»"),
                ("h2", "البصمة · سبعة قرون وأسرتان"),
                ("p",
                 "موثَّقة منذ عام 1185 في سجلات موثّقي سيينا، كانت القلعة أربعمائة "
                 "سنة مَعقِلاً لأسرة Ricasoli، ثم لأسرة Pannocchieschi منذ 1570، "
                 "وأخيراً للأسرة الحالية Medici di Porrena منذ 1812. قرار إسناد "
                 "التوكيل إلى Villa Prestige ينبع من علاقة شخصية تَمتدّ ثلاثين "
                 "عاماً بين الأسرة والمستشار الأول Francesco Medici di Porrena — "
                 "نسيب الأسرة نفسها ومستشار المكتب لـChianti Classico."),
                ("ol", [
                    "المدخل: طريق ترابية خاصة بطول كيلومتر · حماية مَشهدية UNESCO قيد التقييم.",
                    "الحديقة والكرم: ثمانية عشر هكتاراً · سبعة في Chianti Classico حيوي دينامي · بستان زيتون بألفَي شجرة معمَّرة.",
                    "المساحة الداخلية: ألف ومائتا متر مربع · عشر غرف نوم · كنيسة مُكرَّسة 1432.",
                    "القبو: تحت الأرض أسفل الجسم المركزي · ثلاثون برميلاً · مجموعة تاريخية ألفا قارورة.",
                    "التجهيزات: تدفئة بالكتلة الحيوية · لوحات كهروضوئية قليلة الأثر · ماء نبع خاص.",
                    "السعر: عند الطلب إلى المُخاطَب · حصرية تامة حتى خريف 2026.",
                ]),
                ("p",
                 "الإتاحة لا تتجاوز يوماً واحداً في الشهر للمعاينات الخاصة، "
                 "مباشرةً مع الأسرة والمستشار. يستلزم مسار الاقتناء ستة أشهر على "
                 "الأقل لتحقيقات ديوان حماية التراث في فلورنسا وإقليم توسكانا. "
                 "نقل التوكيل الزراعي للكرم يُنسَّق مع اتحاد Chianti Classico."),
            ],
            "footer_strap": "Villa Prestige · Chianti Classico · الملف رقم 07 / 18",
        },
        {
            "slug":     "penthouse-quadronno-milano",
            "kicker":   "ميلانو · Magenta · شقة علوية فريدة",
            "title":    "Penthouse Quadronno — شقة علوية من 1957 مطلّة على الدومو",
            "lede":
                "ثلاثمائة وثمانون متراً مربعاً في الطابق السادس من via Quadronno، شُرفة "
                "من 180 م²، إطلالة مباشرة على الدومو، وتصميم داخلي بتوقيع Vico "
                "Magistretti عام 1958.",
            "date":     "28 آذار 2026",
            "read_min": "6",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 11 / 18 · ربيع 2026"),
                ("الإقليم",   "ميلانو · Magenta · via Quadronno"),
                ("المساحة",   "380 م² داخلية · شُرفة 180 م² · 4 غرف نوم"),
                ("البصمة",    "1957 · توقيع Luigi Caccia Dominioni · التصميم الداخلي Vico Magistretti 1958"),
                ("الإتاحة",   "بموعد"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "تَشغل الشقة العلوية كامل الطابق السادس من قصر Quadronno، المُقام "
                 "عام 1957 على تصميم Luigi Caccia Dominioni، لصالح مالك خاص من "
                 "البرجوازية الصناعية الميلانية. اكتَمَل التصميم الداخلي بعد عشرة "
                 "أشهر على يد Vico Magistretti، وكان حينها في الثالثة والثلاثين، "
                 "بعمل حرفي دقيق على الأخشاب والرخام والمقابض، ما زال حتى اليوم "
                 "على سلامته الأصلية."),
                ("h2", "المُسقَط · ثلاثمائة وثمانون متراً مربعاً مُتمفصِلة"),
                ("p",
                 "المدخل يَفتح على رواق طوله ثمانية عشر متراً يُوزِّع جناحَي الشقة — "
                 "منطقة النهار جنوباً شرقاً، ومنطقة الليل شمالاً غرباً. الصالة "
                 "الرئيسية على مائة وعشرة أمتار مربعة تُطلّ مباشرةً على الدومو "
                 "عبر زجاج من تصميم Jacopo Foggini رُكِّب عام 2018. غرفة الطعام "
                 "والمطبخ الاحترافي والمخزن تُكمِل جناح النهار. أربع غرف نوم، "
                 "كل واحدة بحمّامها الخاص من رخام كارارا الأصلي لعام 1957، تُؤلّف "
                 "جناح الليل."),
                ("h2", "الشُرفة · مائة وثمانون متراً مربعاً مُحيطية"),
                ("p",
                 "الشُرفة المُحيطية، بمائة وثمانين متراً مربعاً في مُجمَلها، "
                 "تُقدّم إطلالة بزاوية ثلاثمائة وستين درجة على المدينة: الدومو "
                 "شرقاً، وقلعة Sforzesco شمالاً، وملعب San Siro في الأفق الغربي. "
                 "تَدخُّل Patricia Urquiola المَشهدي عام 2019 أضاف حوض استرخاء "
                 "مُغطّى، وعريشة من الطوب، ومجموعة من خمس عشرة سُلالة من الأعشاب "
                 "العطرية المتوسّطية."),
                ("blockquote",
                 "«الـQuadronno ليس شقة علوية: إنه متحف صغير للبيت الميلاني في "
                 "خمسينيات القرن الماضي. كل تفصيل من Magistretti بَقي في موضعه.»"),
                ("h2", "البصمة · Caccia Dominioni وMagistretti وUrquiola"),
                ("p",
                 "كُلِّف بها عام 1956 Luigi Caccia Dominioni من أسرة Brambilla، "
                 "واكتَمَلت عام 1957. سُلِّم التصميم الداخلي لـVico Magistretti عام "
                 "1958، ولم يَطرأ عليه تغيير جوهري لستين عاماً. عام 2018، كلَّفت "
                 "الأسرة المالكة الثانية Jacopo Foggini بالزجاج الأمامي؛ وعام 2019، "
                 "وقَّعت Patricia Urquiola التدخُّل المَشهدي على الشُرفة. جميع "
                 "التدخُّلات وُثِّقت في Domus وInterni وCorriere Living."),
                ("ol", [
                    "المدخل: بوابة قصر رفيع الشأن · مصعد خدمة مُكرَّس.",
                    "المساحة الداخلية: ثلاثمائة وثمانون متراً مربعاً · أربع غرف نوم · حمّامات بالرخام الأصلي 1957.",
                    "الشُرفة: مائة وثمانون متراً مربعاً · حوض استرخاء مُغطّى · عريشة من الطوب Urquiola 2019.",
                    "الإطلالة: مباشرة على دومو ميلانو · بانوراما ثلاثمائة وستين درجة.",
                    "التجهيزات: تدفئة مستقلة · تكييف مستقل جناحاً جناحاً.",
                    "السعر: عند الطلب إلى المُخاطَب · اتفاقية عدم إفشاء مطلوبة قبل الملف الكامل.",
                ]),
                ("p",
                 "الإتاحة مفتوحة بموعد. متوسط مسار الاقتناء خمسة وأربعون يوماً من "
                 "اتفاقية عدم الإفشاء إلى التوقيع، بفضل وثائق السجلّ العقاري "
                 "الكاملة والمُحدَّثة. الأسرة البائعة مستعدة للقاء مباشر قبل التوقيع."),
            ],
            "footer_strap": "Villa Prestige · ميلانو · الملف رقم 11 / 18",
        },
        {
            "slug":     "mas-de-la-mer-saint-tropez",
            "kicker":   "Saint-Tropez · الريفيرا الفرنسية · القرن الثامن عشر",
            "title":    "Mas de la Mer — ماس بروفنسي من 1754 بكرم AOP",
            "lede":
                "خمسمائة وخمسون متراً مربعاً على تلال Ramatuelle، كرم خاص بتسمية Côtes "
                "de Provence AOP، تشييد أصلي من 1754 رُمِّم عام 2017.",
            "date":     "20 آذار 2026",
            "read_min": "8",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 14 / 18 · ربيع 2026"),
                ("الإقليم",   "Saint-Tropez · الريفيرا الفرنسية · Ramatuelle"),
                ("المساحة",   "550 م² داخلية · 6 هكتارات · كرم 2,5 هكتاراً"),
                ("البصمة",    "1754 · ماس بروفنسي أصلي · ترميم François Catroux 2017"),
                ("الإتاحة",   "جديد · دخل المجموعة لتوّه"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "يَنهض الماس على تلال Ramatuelle الداخلية، على بُعد اثنَي عشر "
                 "كيلومتراً من ميناء Saint-Tropez، في صمت لا يَعرفه إلا Var الداخلي. "
                 "التشييد الأصلي من 1754، في ملكية الأسرة ذاتها من تقاليد الكَرم "
                 "حتى عام 1948. اقتَنَته أسرة باريسية عام 1985، ورُمِّم عام 2017 "
                 "على يد François Catroux — آخر عمل خاص للمعماري الفرنسي قبل "
                 "رحيله — بهدف استعادة بساطة الداخل الأصلية، بعد خمسين سنة من "
                 "تدخُّلات مُتفاوتة."),
                ("h2", "الكرم · هكتاران ونصف من Côtes de Provence AOP"),
                ("p",
                 "يَضمّ العقار هكتارَين ونصف من كرم في إنتاج AOP Côtes de Provence، "
                 "بعمليات تخمير مُسنَدة إلى Domaine Ott لحصة الروزيه وإلى Domaine "
                 "Tempier لحصة الأحمر. الإنتاج السنوي نحو سبعة آلاف قارورة، "
                 "تُوزَّع حصراً على الأسرة المالكة وضيوفها. قبو التحويل يَقَع "
                 "مباشرةً أسفل الماس، في مقرٍّ نصف تحت الأرض من عام 1802."),
                ("h2", "الداخل · صالة بارتفاع مزدوج وغرفة نوم رئيسية"),
                ("p",
                 "يَتمفصَل الطابق الأرضي حول صالة بارتفاع مزدوج مساحتها مائة "
                 "وعشرون متراً مربعاً، بمدفأة زاوية من الحجر الأصلي وعوارض بلوط "
                 "ظاهرة. المطبخ مُقبَّب، مرصَّع ببلاط Salernes الطيني. في الطابق "
                 "الأول، تَشغل غرفة النوم الرئيسية كامل الجناح الجنوبي، بحمّام "
                 "خاص من رخام Caunes-Minervois؛ ثلاث غرف مزدوجة أخرى، لكلٍّ "
                 "منها حمّامها، تُكمِل الطابق. مُلحَق الحارس يَحتضن شقة لحارس "
                 "أو ضيوف."),
                ("blockquote",
                 "«أعاد François Catroux إلى الماس البطءَ الذي عرفه Var الداخلي "
                 "منذ الأزل. هو آخر أعماله الخاصة، وتَشعُر بذلك.»"),
                ("h2", "البصمة · من الكَرم إلى الأسرة الباريسية"),
                ("p",
                 "بناه عام 1754 آل Bertrand، وامتَلَكوه ستة أجيال يُزَرِعُون الكرم "
                 "ويُنتجون زيت الزيتون، قبل أن يَنتقل إلى أسرة Armand الباريسية "
                 "عام 1948. رُمِّم أول مرة عام 1985 على يد Madeleine Castaing "
                 "بأسلوب غني مُزخرَف، ثم أُعيد إلى رصانته الأصلية عام 2017 بترميم "
                 "François Catroux. نُشر العمل في Architectural Digest France "
                 "وفي Le Monde d'Hermès."),
                ("ol", [
                    "المدخل: طريق ترابية خاصة بطول مائتَي متر · بوابة حديدية أصلية من 1754.",
                    "الحديقة: ستة هكتارات · كرم AOP هكتاران ونصف · بستان زيتون معمَّر · حوض طبيعي من الحجر.",
                    "المساحة الداخلية: خمسمائة وخمسون متراً مربعاً · أربع غرف نوم · مُلحَق الحارس.",
                    "الكرم: Côtes de Provence AOP · تخمير Domaine Ott وTempier · إنتاج سبعة آلاف قارورة.",
                    "التجهيزات: تدفئة بالكريات · تكييف لطيف · ماء نبع خاص.",
                    "السعر: عند الطلب إلى المُخاطَب · اتفاقية عدم إفشاء مطلوبة قبل الملف الكامل.",
                ]),
                ("p",
                 "تُفتَح الإتاحة بموعد اعتباراً من موسم المعاينات المقبل — منتصف "
                 "أيار. يُحال التوكيل الزراعي للكرم سويةً مع التوقيع العقاري؛ "
                 "أما النقل اللاحق للتسمية AOP فيُنسَّق مع Domaine Ott. متوسط "
                 "مسار الاقتناء أربعة أشهر من اتفاقية عدم الإفشاء إلى التوقيع "
                 "أمام الموثّق الفرنسي."),
            ],
            "footer_strap": "Villa Prestige · Saint-Tropez · الملف رقم 14 / 18",
        },
        # Four shorter dossiers to round out the collezione list
        {
            "slug":     "villa-lario-tremezzo",
            "kicker":   "Lago di Como · Tremezzo · القرن التاسع عشر",
            "title":    "Villa Lario — منزل على البحيرة من 1862 بمَرسى خاص",
            "lede":
                "أربعمائة وخمسون متراً مربعاً على مستوى البحيرة، حديقة هكتارَين ونصف، "
                "ومَرسى خاص لقوارب حتى خمسة عشر متراً.",
            "date":     "15 آذار 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 04 / 18 · ربيع 2026"),
                ("الإقليم",   "Lago di Como · Tremezzo"),
                ("المساحة",   "450 م² داخلية · حديقة 25.000 م² · مَرسى خاص"),
                ("البصمة",    "1862 · فيلا من القرن التاسع عشر · ترميم Lissoni 2020"),
                ("الإتاحة",   "بموعد"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "تَقف Villa Lario على مستوى Lago di Como، على مسافة خمس دقائق من "
                 "ساحة Tremezzo الصغيرة، وعشر دقائق بالقارب السريع من Villa "
                 "d'Este. التشييد الأصلي من 1862، لأسرة ميلانية من البرجوازية "
                 "الصناعية اللومباردية. الترميم المحافظ لعام 2020، بإدارة مكتب "
                 "Lissoni Casal Ribeiro، أبقى على سلامة الزخارف من القرن التاسع "
                 "عشر في الصالة الرئيسية، والألواح الخشبية الأصلية، والدرج "
                 "الداخلي من رخام Candoglia."),
                ("h2", "الحديقة والمَرسى · مَدخل خاص إلى البحيرة"),
                ("p",
                 "تَمتدّ الحديقة على هكتارَين ونصف تَنحدر نحو البحيرة، بحديقة "
                 "إيطالية أصلية من 1875، وبركة أسماك، ورَواق من الياسمين "
                 "المُعمَّر. المَرسى الخاص، الأصلي من 1870 والمُرمَّم عام 2020، "
                 "يَحتضن قوارب يَصل طولها إلى خمسة عشر متراً، ومزوَّد برافعة "
                 "كهربائية للإخراج الشتوي. يَنحدر درج حجري مباشرةً من الصالة "
                 "الرئيسية إلى مِشرفة البحيرة."),
                ("ol", [
                    "المدخل: طريق عام · بوابة خاصة ببوّاب.",
                    "الحديقة: هكتاران ونصف · حديقة إيطالية · مَرسى خاص.",
                    "المساحة الداخلية: أربعمائة وخمسون متراً مربعاً · خمس غرف نوم · مكتبة.",
                    "السعر: عند الطلب إلى المُخاطَب · اتفاقية عدم إفشاء مطلوبة قبل الملف.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Lago di Como · الملف رقم 04 / 18",
        },
        {
            "slug":     "casa-delle-torri-porto-cervo",
            "kicker":   "Costa Smeralda · Porto Cervo · سبعينيات القرن الماضي",
            "title":    "Casa delle Torri — فيلا من توقيع Jacques Couëlle عام 1972",
            "lede":
                "ستمائة وعشرون متراً مربعاً على شبه جزيرة خاصة، تصميم أصلي من Jacques "
                "Couëlle، وشُرفات فوق البحر مع مَدخل مباشر إلى خليج خاص.",
            "date":     "8 آذار 2026",
            "read_min": "6",
            "author":   "Élodie Charbonneau",
            "image":
                "https://images.pexels.com/photos/2351649/pexels-photo-2351649.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 08 / 18 · ربيع 2026"),
                ("الإقليم",   "Costa Smeralda · Porto Cervo"),
                ("المساحة",   "620 م² داخلية · شبه جزيرة خاصة · خليج"),
                ("البصمة",    "1972 · توقيع Jacques Couëlle · ترميم A. Citterio 2018"),
                ("الإتاحة",   "بموعد"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "صمَّمها عام 1972 Jacques Couëlle لأسرة بلجيكية، وCasa delle "
                 "Torri من الفيلات النادرة الباقية بكامل روحها من التصميم "
                 "العضوي في Smeralda. ترميم 2018 بإدارة Antonio Citterio أبقى "
                 "على السلامة التامة للغلاف من الغرانيت المحلي والسقوف من "
                 "العَرْعَر، واستحدَث تجهيزات خفية ومطبخاً معاصراً في الملحق."),
                ("ol", [
                    "المدخل: طريق الاتحاد الخاص · بوّابة Porto Cervo.",
                    "الشُرفات: ثلاثة مستويات فوق البحر · خليج خاص يُبلَغ إليه مشياً.",
                    "المساحة: ستمائة وعشرون متراً مربعاً · ست غرف نوم · مُلحَق للعاملين.",
                    "السعر: عند الطلب إلى المُخاطَب.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Costa Smeralda · الملف رقم 08 / 18",
        },
        {
            "slug":     "casa-canapa-capri",
            "kicker":   "كابري · Anacapri · ثلاثينيات القرن الماضي",
            "title":    "Casa Canapa — فيلا كابرية مطلّة على الفاراليوني",
            "lede":
                "مائتان وعشرون متراً مربعاً على ثلاثة مستويات، شُرفات متتالية نحو "
                "الفاراليوني، حديقة ليمون معمَّر، ومَدخل مشاة من مركز Anacapri.",
            "date":     "1 آذار 2026",
            "read_min": "5",
            "author":   "Arianna Testa Piccolomini",
            "image":
                "https://images.pexels.com/photos/2079249/pexels-photo-2079249.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 15 / 18 · ربيع 2026"),
                ("الإقليم",   "كابري · Anacapri"),
                ("المساحة",   "220 م² داخلية · 3 شُرفات · حديقة 800 م²"),
                ("البصمة",    "1934 · فيلا كابرية أصلية · ثلاثة أجيال في الأسرة ذاتها"),
                ("الإتاحة",   "بموعد"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "Casa Canapa فيلا كابرية أصيلة من 1934، تَتوارثها ثلاثة أجيال في "
                 "الأسرة النابولية ذاتها. التصميم الأصلي من التقليد الكابري — "
                 "قبب وأنصاف قبب ودرجات خارجية من المايوليكا — ولم يَطرأ عليه "
                 "تدخُّل جوهري. الصيانة الاعتيادية، المُسنَدة إلى حرفيي كابري "
                 "المعهودين، صانَت الطابع الجزري للبيت على حاله."),
                ("ol", [
                    "المدخل: مشاة فقط · خمس دقائق سيراً من ساحة Anacapri الصغيرة.",
                    "الشُرفات: ثلاثة مستويات متتالية · إطلالة على فاراليوني كابري.",
                    "المساحة: مائتان وعشرون متراً مربعاً · أربع غرف نوم.",
                    "السعر: عند الطلب إلى المُخاطَب.",
                ]),
            ],
            "footer_strap": "Villa Prestige · كابري · الملف رقم 15 / 18",
        },
        {
            "slug":     "pieve-di-santorso-val-dorcia",
            "kicker":   "Val d'Orcia · Montalcino · القرن الثاني عشر",
            "title":    "Pieve di Sant'Orso — ضيعة UNESCO بكرم من Brunello",
            "lede":
                "ثمانمائة متر مربع بين كنيسة قروية رومانية ومسكن ريفي، اثنان وعشرون "
                "هكتاراً من تراث UNESCO، وكرم من Brunello di Montalcino DOCG في الإنتاج.",
            "date":     "22 شباط 2026",
            "read_min": "7",
            "author":   "Francesco Medici di Porrena",
            "image":
                "https://images.pexels.com/photos/2029694/pexels-photo-2029694.jpeg?auto=compress&cs=tinysrgb&w=1800&h=1100&fit=crop",
            "meta_rows": [
                ("المجموعة",  "رقم 17 / 18 · ربيع 2026"),
                ("الإقليم",   "Val d'Orcia · Montalcino"),
                ("المساحة",   "800 م² داخلية · 22 هكتاراً UNESCO · كرم 4 هكتارات"),
                ("البصمة",    "القرن الثاني عشر · كنيسة قروية رومانية · ترميم Matteo Nunziati 2019"),
                ("الإتاحة",   "حصرية"),
                ("السعر",     "عند الطلب إلى المُخاطَب"),
            ],
            "body": [
                ("p",
                 "تَمتدّ ضيعة Sant'Orso على اثنَين وعشرين هكتاراً من تراث UNESCO "
                 "في Val d'Orcia، بين Montalcino وSan Quirico d'Orcia. يَضمّ "
                 "النواة التاريخية الكنيسة القروية الرومانية من 1182 — ما زالت "
                 "مُكرَّسة، تُستخدَم مرة في السنة — والمسكن الريفي الأصلي من "
                 "1620، المُرمَّم عام 2019 على يد Matteo Nunziati. يَشغل كرم "
                 "Brunello di Montalcino DOCG أربعة هكتارات، في إدارة عضوية "
                 "موثَّقة، بتخمير مُسنَد إلى الضَيعة المجاورة."),
                ("ol", [
                    "المدخل: طريق بلدية ترابية بطول كيلومترَين · حماية UNESCO.",
                    "الضَيعة: اثنان وعشرون هكتاراً · كرم أربعة هكتارات · بستان زيتون من ثمانمائة شجرة.",
                    "المساحة الداخلية: ثمانمائة متر مربع · كنيسة قروية رومانية · ست غرف نوم.",
                    "السعر: عند الطلب إلى المُخاطَب · حصرية تامة.",
                ]),
            ],
            "footer_strap": "Villa Prestige · Val d'Orcia · الملف رقم 17 / 18",
        },
    ],
}


# D-047 · all chrome labels flow from site/page_data above — no string
# should ever be hardcoded in the skin or preview composition HTML.
