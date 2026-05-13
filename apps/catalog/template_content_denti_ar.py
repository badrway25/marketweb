"""Denti+Co — Studio Dentistico · Arabic (AR · RTL) content tree.

Wave 1 Pass-2 (T46 · 2026-05-11) workflow C multilingual rollout — four
sub-agent parallel translators landing AR alongside EN/FR/ES on top of
the IT seed (`template_content_denti.py · DENTI_CONTENT_IT`).

This tree mirrors `DENTI_CONTENT_IT` with strict shape-parity: same
top-level keys, same nested keys, same tuple arities. Only the visible
strings change. Page slugs stay Italian (home/studio/visite/medici/
pubblicazioni/contatti/richiedi-visita) because the URL contract is
locale-agnostic — only the navigation `label` field is translated.

Voice anchor — `igiene` → `النظافة الفموية` (oral hygiene · the noun-em
italic). The Italian template uses `<em>igiene</em>` as a recurring
typographic motif that lands in headlines, manifesto prose, FAQ and
CTA bands; the Arabic tree carries that motif verbatim-in-translation
via `<em>النظافة الفموية</em>` in the same surface locations. Where
flow demands a shorter form (manifesto run-on, secondary mentions) we
shorten to `<em>النظافة</em>` — the editorial signature is the
em-wrapped noun, not the exact glyph count.

Tone — Modern Standard Arabic (MSA · فصحى), formal premium medical
register, Asharq Al-Awsat / BBC Arabic Health editorial gravity.
Arabic punctuation throughout: `،` comma, `؟` question mark, `؛`
semicolon. Numerals stay Latin (12, 75, 1.850 €, +39 02 7770 4488)
per the LF-2 specialist house style — Arabic-Indic digits ١٢ are
reserved for purely-Arabic prose contexts which this commerce-bearing
template is not.

Non-localizable data (verbatim from IT):
  · phone        +39 02 7770 4488
  · email        studio@denticostudio.it
  · address      Via Manzoni 18 · 20121 ميلانو
  · prices       € 95, € 220, € 1.850, etc. (Latin digits + €)
  · doctor names Dr.ssa Chiara Vespa, Dr. Riccardo Berti,
                 Dr.ssa Sofia Liccardi, Dr. Andrea Carofiglio
                 (Latin proper names · matches Causa/Cornice/Continua
                 precedent · rendered under RTL via the
                 `unicode-bidi: isolate` chrome rule)
  · press        Il Dentista Moderno, Dental Tribune, Bocca & Salute,
                 Corriere Salute, Vanity Fair Italia (original Latin)
  · photo URLs   `_CHIEF_PORTRAIT`, `_LEAD_IMAGE`, and the three
                 inline doctor portrait URLs — preserved verbatim
                 from the IT seed so the Pexels CDN cache is shared

RTL rendered chrome-level via `html[dir="rtl"]` on the specialist skin
— no template duplication. The four sub-page contracts (studio /
visite / medici / contatti / richiedi-visita) all match the IT seed
shape exactly so `template_renderer.py` resolves the locale without
needing a shape adapter.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs — preserved verbatim from the IT seed. Same Pexels
# license, same CDN cache, same dental imagery pool. See the IT seed
# for full licensing notes.
_CHIEF_PORTRAIT = (
    "https://images.pexels.com/photos/4269363/pexels-photo-4269363.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_LEAD_IMAGE = (
    "https://images.pexels.com/photos/9062525/pexels-photo-9062525.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)


DENTI_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "العيادة",              "kind": "home"},
        {"slug": "studio",          "label": "عن العيادة",            "kind": "about"},
        {"slug": "visite",          "label": "العلاجات",             "kind": "services"},
        {"slug": "medici",          "label": "أطباء الأسنان",         "kind": "team"},
        {"slug": "pubblicazioni",   "label": "المنشورات",             "kind": "blog_list"},
        {"slug": "contatti",        "label": "تواصل معنا",            "kind": "contact"},
        {"slug": "richiedi-visita", "label": "احجز جلسة نظافة",       "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "D",
        "logo_word":    "Denti+Co",
        "tag":          "عيادة أسنان مشتركة · ميلانو حي بريرا",
        "phone":        "+39 02 7770 4488",
        "email":        "studio@denticostudio.it",
        "address":      "Via Manzoni 18 · 20121 ميلانو",
        "hours_compact": "الإثنين – الجمعة · 8:30 – 19:30",
        "hours_footer_rows": [
            "السبت · 9:00 – 13:00",
            "الأحد · مغلق",
        ],
        "license":      "تسجيل OMCeO ميلانو 03 / 18742 · المدير الطبي Dr.ssa C. Vespa",
        "footer_intro":
            "عيادة أسنان مشتركة متخصصة في طب الأسنان التحفظي، "
            "والنظافة الفموية المهنية، وزراعة الأسنان. أربعة "
            "أطباء مختصين، وملف طبي واحد لكل مريض.",
    },

    "home": {
        # Hero — editorial-magazine variant: portrait-driven, different
        # silhouette from Cardio's default split-consultive.
        "hero_variant": "editorial-magazine",
        "eyebrow":  "طب الأسنان · ميلانو بريرا",
        "headline": "<em>النظافة الفموية</em> ليست تفصيلاً، بل هي الفصل الأول.",
        "intro":
            "نظافة فموية مهنية، وطب أسنان تحفظي، وزراعة، وتقويم شفاف. "
            "أربعة أطباء أسنان شركاء، وملف طبي واحد، وزيارات مراقبة "
            "نصف سنوية مشمولة ضمن الخطة السنوية.",
        "primary_cta":   "احجز جلسة نظافة",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "عن العيادة",
        "secondary_href":"studio",

        # Three-fact band (Cardio uses 3 numbers · we use 3 dental-coded)
        "facts": [
            ("12", "عاماً من العمل المشترك"),
            ("3.400", "جلسة نظافة وفحص سنوياً"),
            ("4", "أطباء أسنان مختصون داخل العيادة"),
        ],

        # Manifesto with drop-cap (specialist archetype signature)
        "manifesto_drop_cap": "ص",
        "manifesto":
            "حة الفم لا تُعالَج مرتين في السنة؛ بل تُصان كل يوم. "
            "لذلك تنطلق Denti+Co من <em>النظافة</em> — مهنيةً، "
            "قابلةً للتكرار، قابلةً للقياس — وتبني حولها طب الأسنان "
            "التحفظي وزراعة الأسنان والتقويم. أربعة أطباء مختصين، "
            "وملف طبي مشترك واحد، وتوقيع واحد على خطة العلاج. "
            "لا بيع إضافي، ولا علاج متشظٍ: <em>النظافة الفموية</em> "
            "هي الفصل الأول، وهي البوابة الوحيدة الحقيقية.",

        # Hero right sidebar (when hero_variant is split-consultive only —
        # but we kept the pulse data so the editorial-magazine pulse rail
        # also renders.)
        "hero_sidebar_top_label": "الإدارة الطبية",
        "hero_sidebar_quote":
            "«النظافة الفموية المهنية حين تُؤدّى على وجهها الصحيح "
            "تُجنّب 70 % من العلاجات الباضعة. هي عندنا ممارسة "
            "سريرية جادة، لا خدمة تجميلية.»",
        "hero_sidebar_author": "— Dr.ssa Chiara Vespa · المدير الطبي",
        "hero_sidebar_pulse": [
            ("العيادة",     "ميلانو · بريرا"),
            ("منذ",         "2013"),
            ("التخصص",      "طب أسنان مشترك"),
        ],

        # Anchor subnav (helps a dense home read like a magazine)
        "anchor_nav": [
            ("metodo",        "المنهج"),
            ("trattamenti",   "العلاجات"),
            ("percorso",      "مسار المريض"),
            ("medico",        "الإدارة الطبية"),
            ("studio",        "المقر والتواصل"),
        ],

        # Signature treatments (numbered 01-04 · the dental version of
        # Cardio's signature_visits — four core dental categories)
        "signature_visits_label":   "العلاجات والمسارات",
        "signature_visits_heading": "أربعة مسارات سريرية، <em>وملف طبي واحد.</em>",
        "signature_visits_intro":
            "أربع عائلات علاجية هي الأكثر طلباً. "
            "تجدون القائمة الكاملة في صفحة العلاجات.",
        "signature_visits": [
            ("01", "النظافة الفموية المهنية نصف السنوية",
             "إزالة الجير فوق اللثة وتحتها، وتلميع بمسحوق بيكربونات "
             "الصوديوم، ومؤشر النزف، ومسح لثوي وفق نظام PSR. "
             "مشمولة ضمن خطط المراقبة السنوية."),
            ("02", "طب الأسنان التحفظي",
             "حشوات تجميلية بالكومبوزيت الطبقي، وترميمات تجميلية، "
             "ومعالجات لبية بمحدد الذروة. عزل مطاطي إلزامي في كل "
             "تدخل تحفظي."),
            ("03", "زراعة الأسنان والترميم العظمي",
             "زراعات مفردة وتأهيلات كاملة بتحميل فوري. تخطيط مدعوم "
             "بالحاسوب وقالب جراحي مطبوع ثلاثي الأبعاد في مختبرنا "
             "الداخلي."),
            ("04", "التقويم الشفاف",
             "متقومات Invisalign وSmileLab الشفافة للبالغين، وتقويم "
             "اعتراضي للأطفال بين 8 و12 عاماً بأجهزة قابلة للنزع. "
             "متابعة شهرية مشمولة."),
        ],

        # Trattamenti tabs section (the four dental categories with
        # detailed treatment lists — uses the trattamenti_tabs DNA hook
        # the specialist skin already supports, see home.html L954+).
        "trattamenti_tabs": {
            "label":   "قائمة العلاجات",
            "heading": "ما الذي نقوم به، <em>وبأيّ معيار.</em>",
            "intro":
                "أربع فئات سريرية، لكلّ منها بروتوكول مكتوب وتكلفة "
                "معلنة. لا عرض سعر مُخصَّص للبنود الاعتيادية — فقط "
                "لخطط العلاج المُهيكَلة.",
            "tabs": [
                {
                    "id":      "igiene",
                    "label":   "النظافة",
                    "eyebrow": "النظافة الفموية المهنية",
                    "heading": "خمس وأربعون دقيقة، لا عشرون.",
                    "body":
                        "النظافة الفموية ليست موعداً اعتيادياً: هي "
                        "زيارة سريرية مدتها خمس وأربعون دقيقة تشمل "
                        "المسح اللثوي، ومؤشر النزف، والتلميع "
                        "ببيكربونات الصوديوم، والتوثيق المصور للمتابعة.",
                    "items": [
                        ("جلسة نظافة مهنية مفردة", "45 دقيقة · € 95"),
                        ("الخطة السنوية (جلستا نظافة + فحص)", "سنوية · € 220"),
                        ("تلميع ببيكربونات الصوديوم", "مشمول · مجاناً"),
                        ("سدّ الشقوق (للسن الواحد)", "10 دقائق · € 30"),
                    ],
                    "cta_label": "جميع خطط النظافة ←",
                    "cta_href":  "visite",
                },
                {
                    "id":      "conservativa",
                    "label":   "التحفظي",
                    "eyebrow": "طب الأسنان التحفظي",
                    "heading": "كومبوزيت طبقي، دائماً تحت العزل المطاطي.",
                    "body":
                        "حشوات بكومبوزيت ضوئي التصلّب، وترميمات "
                        "تجميلية، ومعالجات لبية بمحدد الذروة. عزل "
                        "مطاطي إلزامي في كل تدخل تحفظي. لا نستخدم "
                        "حشوات الأملغم منذ عام 2013.",
                    "items": [
                        ("حشوة مفردة (سطح واحد)", "45 دقيقة · € 140"),
                        ("حشوة مركّبة (2-3 أسطح)", "60 دقيقة · € 220"),
                        ("معالجة لبية أحادية الجذر", "75 دقيقة · € 280"),
                        ("معالجة لبية متعددة الجذور", "120 دقيقة · € 420"),
                    ],
                    "cta_label": "قائمة طب الأسنان التحفظي كاملةً ←",
                    "cta_href":  "visite",
                },
                {
                    "id":      "implantologia",
                    "label":   "زراعة الأسنان",
                    "eyebrow": "زراعة الأسنان والترميم العظمي",
                    "heading": "زراعات إيطالية، ضمان مدى الحياة على الجذر.",
                    "body":
                        "زراعات Sweden+Martina إيطالية المنشأ، "
                        "وتخطيط مدعوم بالحاسوب عبر التصوير المقطعي "
                        "ثلاثي الأبعاد، وقالب جراحي مطبوع ثلاثي "
                        "الأبعاد في المختبر الداخلي. التحميل الفوري "
                        "لا يُجرى إلا في حالات منتقاة بعد التقييم "
                        "السريري.",
                    "items": [
                        ("زراعة مفردة (جذر + تاج زركونيا)", "تدخل · € 1.850"),
                        ("رفع طفيف للجيب الفكي العلوي", "تدخل · € 950"),
                        ("ترميم عظمي (منطقة واحدة)", "تدخل · € 480"),
                        ("تأهيل ثابت على 4 زراعات", "خطة · حسب عرض السعر"),
                    ],
                    "cta_label": "مسارات الزراعة ←",
                    "cta_href":  "visite",
                },
                {
                    "id":      "ortodonzia",
                    "label":   "التقويم",
                    "eyebrow": "التقويم الشفاف والاعتراضي",
                    "heading": "متقومات للبالغين، تقويم اعتراضي للأطفال.",
                    "body":
                        "متقومات Invisalign وSmileLab الشفافة مع "
                        "مسح داخل الفم بجهاز iTero وخطة محاكاة "
                        "ثلاثية الأبعاد قبل الانطلاق. تقويم اعتراضي "
                        "للأطفال بين 8 و12 عاماً بأجهزة قابلة للنزع. "
                        "متابعة شهرية مشمولة في الخطة.",
                    "items": [
                        ("متقومات Invisalign – خطة كاملة", "12-18 شهراً · € 3.200"),
                        ("متقومات SmileLab – خطة كاملة", "10-14 شهراً · € 2.400"),
                        ("التقويم الاعتراضي للأطفال", "12-24 شهراً · € 1.600"),
                        ("جهاز تثبيت ليلي بعد العلاج", "دائم · € 220"),
                    ],
                    "cta_label": "بروتوكولات التقويم ←",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "الإدارة الطبية",
        "chief_heading": "توقيع واحد <em>على كل ملف طبي.</em>",
        "chief": {
            "name":  "Dr.ssa Chiara Vespa",
            "role":  "المدير الطبي · طب الأسنان التحفظي ومعالجة الجذور",
            "bio":
                "أخصائية في طب الأسنان التحفظي، تخرّجت من جامعة "
                "ميلانو واستكملت تدريبها في جامعة Loma Linda في "
                "كاليفورنيا. عضوة الجمعية الإيطالية لمعالجة الجذور "
                "(SIE)، ومحاضرة في الدورات السنوية للمدرسة "
                "اللومباردية لطب الأسنان. تتولى الإدارة الطبية "
                "للعيادة منذ عام 2013.",
            "portrait": _CHIEF_PORTRAIT,
        },

        # Patient journey — five steps in dental key (Cardio uses
        # arrival → anamnesi → ECG → diagnostica → piano scritto; we
        # use arrival → check-in → cartella+foto → trattamento → follow-up)
        "percorso": {
            "label":   "مسار المريض",
            "heading": "ما يمكن توقّعه من <em>الزيارة الأولى.</em>",
            "intro":
                "الزيارة الأولى للعيادة مُكرّسة لبناء الملف الطبي: "
                "صور، ومؤشرات، ومسح، وخطة علاج مكتوبة. لا علاج في "
                "الجلسة الأولى — إلا في الحالات الطارئة الموثّقة.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "الاستقبال والسوابق",
                    "desc": "السكرتارية، واستمارة السوابق الطبية "
                            "والسنّية، والأشعة السابقة أو الصورة "
                            "البانورامية الحديثة إن وُجدت.",
                    "duration": "10 دقائق",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "الفحص السريري الشامل",
                    "desc": "مسح لثوي، ومؤشر اللويحة، ومؤشر النزف، "
                            "وفحص موضوعي للأنسجة الرخوة والأغشية "
                            "المخاطية الفموية.",
                    "duration": "20 دقيقة",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "التصوير والمسح",
                    "desc": "مجموعة صور سريرية معيارية (8 لقطات "
                            "داخل الفم + 4 خارج الفم)، ومسح داخل "
                            "الفم بجهاز iTero للأرشيف الرقمي.",
                    "duration": "15 دقيقة",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "خطة العلاج المكتوبة",
                    "desc": "نقاش على كرسي العلاج للخطة السريرية "
                            "مع عرض سعر تفصيلي بنداً بنداً، يُسلَّم "
                            "كذلك بصيغة PDF.",
                    "duration": "15 دقيقة",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "الجدولة والمتابعة",
                    "desc": "تقويم المواعيد، واستدعاء لاحق لجلسة "
                            "النظافة الصيانية إن لزم، وقناة WhatsApp "
                            "مباشرة للحالات الطارئة.",
                    "duration": "5 دقائق",
                },
            ],
        },

        # Press strip (dental-coded outlets · NOT cardiology titles)
        "press": ["Il Dentista Moderno", "Dental Tribune", "Bocca & Salute",
                  "Corriere Salute", "Vanity Fair Italia"],
        "press_label": "نُشر في",

        # FAQ (dental-specific questions, not cardio)
        "faq": {
            "label": "الأسئلة المتكرّرة",
            "heading": "الأسئلة التي <em>يطرحها مرضانا أكثر من غيرها.</em>",
            "items": [
                ("كم مرة يحتاج المرء إلى جلسة نظافة فموية؟",
                 "للمرضى من دون مرض لثوي مُثبَت يكون التواتر نصف "
                 "سنوي. أما من يعانون من التهاب اللثة أو الالتهاب "
                 "اللثوي المتقدم أو يضعون أجهزة تقويم فيقصر التواتر "
                 "إلى ثلاثة أو أربعة أشهر. تُصمَّم الخطة بعد الزيارة "
                 "الأولى."),
                ("هل تدوم حشوات الكومبوزيت فعلاً؟",
                 "نعم، إذا رُمّمت الفجوة تحت العزل المطاطي بكومبوزيت "
                 "طبقي وضوء LED مؤهَّل. متوسط عمر حشواتنا عشر سنوات "
                 "مع زيارات مراقبة منتظمة. لا نستخدم الأملغم منذ "
                 "عام 2013."),
                ("كم تكلّف الزراعة فعلاً؟",
                 "الزراعة المفردة (جذر تيتانيوم Sweden+Martina + "
                 "تاج زركونيا) تكلّف € 1.850 شاملةً ضريبة القيمة "
                 "المضافة. لا يشمل ذلك التدخلات الترميمية التمهيدية "
                 "إن لزمت (رفع الجيب، GBR)، وتُسعَّر فقط بعد التصوير "
                 "المقطعي ثلاثي الأبعاد."),
                ("هل ينجح التقويم الشفاف فعلاً مع البالغين؟",
                 "في تسعين بالمئة من الحالات السريرية لدى البالغين، "
                 "المتقومات الشفافة (Invisalign أو SmileLab) فعّالة "
                 "بقدر التقويم الثابت التقليدي. الحالات التي ما "
                 "زالت تستدعي التقويم الثابت هي الدورانات الشديدة "
                 "للضواحك والبثوقات الواضحة، ونناقشها بصراحة عند "
                 "وضع الخطة."),
                ("هل يمكنني إحضار أبنائي إلى العيادة نفسها؟",
                 "نعم. تختص الدكتورة Liccardi بالتقويم الاعتراضي "
                 "للأطفال بين 8 و12 عاماً بأجهزة قابلة للنزع. "
                 "النظافة الفموية للأطفال مشمولة لأبناء المرضى الذين "
                 "لديهم خطة سنوية مفعَّلة."),
            ],
        },

        # Bottom CTA band
        "cta_heading":
            "كل خطة علاج هي <em>مكتوبة، ومُعلَنة، ومُشترَكة.</em>",
        "cta_primary_label":   "احجز جلسة نظافة",
        "cta_secondary_label": "تواصل مع العيادة",

        # Sede / Location — Milan Brera, different from Cardio Roma Parioli
        # and Derm Roma Veneto
        "location": {
            "label":   "مقر العيادة",
            "heading": "Via Manzoni 18، <em>ميلانو.</em>",
            "intro":
                "تشغل العيادة الطابق الرئيسي من قصر تاريخي في حي "
                "بريرا، على بُعد مئة وعشرين متراً من شارع "
                "Montenapoleone. أربع غرف علاج، وقاعة أشعة بجهاز "
                "تصوير مقطعي ثلاثي الأبعاد، ومختبر تقويم داخلي.",
            "map_image": "",
            "map_fallback_image":
                "https://images.pexels.com/photos/305567/pexels-photo-305567.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "details": [
                ("العنوان",
                 "Via Manzoni 18\n20121 ميلانو"),
                ("المترو",
                 "خط M3 محطة Montenapoleone\n3 دقائق سيراً"),
                ("موقف السيارات",
                 "كراج باتفاقية\nفي Via Bigli، على بُعد 50 متراً"),
                ("سهولة الوصول",
                 "مدخل ميسَّر مع مصعد\nحتى الطابق الرئيسي"),
            ],
            "hours_short": [
                ("الإثنين – الجمعة", "8:30 – 19:30"),
                ("السبت",            "9:00 – 13:00"),
                ("الأحد",            "مغلق"),
            ],
            "cta_label": "احصل على الاتجاهات",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) — full content, all keys the specialist
    # about.html requires (history, method_*, values_*, cta_*).
    "studio": {
        "eyebrow":   "العيادة · ميلانو بريرا",
        "headline":  "أربعة أطباء أسنان، <em>وملف طبي واحد.</em>",
        "intro":
            "Denti+Co عيادة مشتركة أُسّست في عام 2013 على يد أربعة "
            "أطباء يتشاركون الملف الطبي ذاته وبروتوكول العمل ذاته: "
            "صور قبل وبعد، عزل مطاطي دائماً، عرض سعر مكتوب يُسلَّم "
            "أيضاً بصيغة PDF، ومتابعة مجدوَلة.",
        # 5-row history timeline (year + 1-line description · 2-tuples)
        "history": [
            ("2013",
             "تأسيس العيادة المشتركة في Via Manzoni بطبيبين "
             "مختصَّين وغرفة عمل واحدة."),
            ("2016",
             "افتتاح قسم الزراعة بجهاز تصوير مقطعي ثلاثي الأبعاد "
             "Carestream CS 9600 وغرفة جراحية مخصَّصة."),
            ("2019",
             "اعتماد المسح داخل الفم بجهاز iTero وخطط التقويم "
             "المحاكاة ثلاثية الأبعاد قبل بدء العلاج."),
            ("2022",
             "افتتاح مختبر التقويم الداخلي مع طباعة ثلاثية الأبعاد "
             "للقوالب الجراحية وأجهزة التثبيت الليلية."),
            ("2025",
             "تختم العيادة العام بأربعة شركاء بدوام كامل وفريق "
             "من ست أخصائيات نظافة فموية."),
        ],
        "studio_image":
            "https://images.pexels.com/photos/4269268/pexels-photo-4269268.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "studio_image_caption": "غرفة العمل · Via Manzoni 18",
        "method_title": "منهج Denti+Co",
        "method_paragraphs": [
            "<em>النظافة الفموية</em> هي الفصل الأول لأنها أيضاً "
            "الأقدر على التكرار. تكاد لا تجد من يدخل العيادة لأول "
            "مرة وفمه في حال مرتّبة: غالبية المرضى يحتاجون إلى "
            "إعادة ترتيب الأساس قبل الحديث عن التجميل أو التقويم "
            "أو الزراعة. أربعون دقيقة من النظافة الفموية المهنية "
            "المُتقَنة تغيّر منظور عرض السعر لكل التدخلات اللاحقة.",
            "الملف الطبي واحد — هو نفسه للشركاء الأربعة — لأن "
            "المريض ليس مريض طبيب بعينه، بل مريض العيادة. حين "
            "تلاحظ أخصائية النظافة انحساراً لثوياً خلال جلسة "
            "صيانة، تُسجّله لطبيب اللثة في الوثيقة السريرية ذاتها. "
            "لا علاج متشظٍ.",
            "التكاليف مُعلَنة للبنود الاعتيادية (النظافة، طب "
            "الأسنان التحفظي، التبييض، الفحص). أما الخطط الأكثر "
            "تركيباً — الزراعة مع الترميم العظمي، والتقويم المعقّد، "
            "والتأهيلات الشاملة — فعرض سعرها مُخصَّص بعد زيارة "
            "أولى مدتها سبعون دقيقة، لكنه يُسلَّم دائماً مكتوباً "
            "وموقَّعاً في أسفله.",
        ],
        "values_label":   "قيم العيادة",
        "values_heading": "أربعة التزامات، <em>مكتوبة في الملف الطبي.</em>",
        "values": [
            ("العزل المطاطي دائماً",
             "في كل تدخل تحفظي أو لبيّ أو تطبيق كومبوزيت. "
             "من دون استثناءات."),
            ("صور قبل وبعد",
             "مجموعة صور سريرية معيارية تُسلَّم للمريض بصيغة "
             "رقمية في ختام كل خطة علاج."),
            ("عرض سعر مكتوب",
             "لا تكلفة تُناقَش شفهياً فحسب. PDF عبر البريد "
             "الإلكتروني أو يُسلَّم في العيادة قبل بدء العمل."),
            ("متابعة مجدوَلة",
             "تقويم مواعيد الصيانة يُرسَل أيضاً عبر الرسائل "
             "النصية أو WhatsApp. لا مريض يُترَك لشأنه بعد "
             "التدخل."),
        ],
        "cta_heading":
            "الخطوة الأولى تبدأ دائماً <em>بزيارة مدتها سبعون دقيقة.</em>",
        "cta_primary_label":   "تعرّف على أطباء الأسنان",
        "cta_secondary_label": "احجز الزيارة الأولى",
        "press_label": "نُشر في",
        "press": ["Il Dentista Moderno", "Dental Tribune",
                  "Bocca & Salute", "Corriere Salute"],
    },

    # ─── VISITE (services) — services.html expects `treatments`
    # as a list of 4-tuples (name, meta, desc, price) + cta_*.
    "visite": {
        "eyebrow":  "العلاجات · قائمة 2026",
        "headline": "ما الذي نقوم به، <em>وكم يكلّف، وما الذي نضمنه.</em>",
        "intro":
            "القائمة الكاملة للبنود الاعتيادية. أما خطط العلاج "
            "المُهيكَلة (الزراعة المعقّدة، والتقويم، والتأهيلات "
            "الشاملة) فتحظى دائماً بعرض سعر مُخصَّص بعد الزيارة "
            "الأولى.",
        "service_image":
            "https://images.pexels.com/photos/6502543/pexels-photo-6502543.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "service_image_caption": "غرفة العمل · المعدّات والمختبر الداخلي",
        "treatments": [
            ("جلسة نظافة فموية مهنية مفردة",
             "45 دقيقة · من دون إحالة الطبيب المعالج",
             "مسح لثوي، ومؤشر النزف، وتلميع ببيكربونات الصوديوم، "
             "وصور متابعة. تشمل تحليل عادات النظافة المنزلية مع "
             "إمكانية تجربة فرشاة صوتية.",
             "€ 95"),
            ("الخطة السنوية للصيانة",
             "سنوية · جلستا نظافة + فحص + أشعة داخل الفم",
             "جلستا نظافة نصف سنوية مجدوَلتان، وزيارة فحص مع "
             "تصوير، وأشعة داخل الفم عند الإشارة. قناة WhatsApp "
             "مباشرة للحالات الطارئة.",
             "€ 220"),
            ("حشوة تحفظية (سطح واحد)",
             "45 دقيقة · كومبوزيت طبقي تحت العزل المطاطي",
             "كومبوزيت من Tokuyama أو 3M، دائماً تحت العزل "
             "المطاطي، مع ضوء LED مؤهَّل. ضمان ثبات خمس سنوات "
             "مع زيارات مراقبة منتظمة.",
             "€ 140"),
            ("معالجة لبية أحادية الجذر",
             "75 دقيقة · محدد ذروة + إغلاق حراري",
             "معالجة لبية بمحدد الذروة Morita، وإغلاق ثلاثي "
             "الأبعاد بمادة gutta-percha الحرارية، وحشوة "
             "تاجية بالكومبوزيت. متابعة بالأشعة بعد ستة "
             "واثني عشر شهراً.",
             "€ 280"),
            ("زراعة مفردة (جذر + تاج زركونيا)",
             "تدخل + زيارتا فحص · ضمان مدى الحياة على الجذر",
             "زراعة إيطالية Sweden+Martina، ودعامة من زركونيا "
             "مستقرة، وتاج مفرد مفروز في المختبر الداخلي. "
             "التصوير المقطعي ثلاثي الأبعاد التمهيدي مشمول.",
             "€ 1.850"),
            ("متقومات Invisalign (خطة كاملة)",
             "12-18 شهراً · مسح iTero + خطة ثلاثية الأبعاد + جهاز تثبيت",
             "مسح داخل الفم بجهاز iTero، وخطة محاكاة ثلاثية "
             "الأبعاد تُسلَّم للمريض قبل بدء العلاج. متقومات "
             "تُسلَّم على مراحل. جهاز التثبيت الليلي بعد العلاج "
             "مشمول.",
             "€ 3.200"),
            ("تبييض مهني على الكرسي",
             "60 دقيقة · بيروكسيد 35 % + جل واقٍ للثة",
             "جلسة واحدة مدتها ستون دقيقة ببيروكسيد الهيدروجين "
             "35 %، وجل واقٍ للثة متصلّب ضوئياً، ومراقبة "
             "درجة حموضة اللعاب قبل العلاج وبعده.",
             "€ 380"),
            ("الزيارة الأولى (ملف طبي + خطة)",
             "70 دقيقة · سوابق + مسح iTero + خطة بصيغة PDF",
             "سوابق طبية وسنّية، وفحص موضوعي، ومسح لثوي، "
             "ومسح داخل الفم، وتصوير، وتسليم الخطة السريرية "
             "بصيغة PDF. تُحسَم التكلفة من أول علاج.",
             "€ 80"),
        ],
        "footnote_heading": "ما الذي لا تشمله القائمة",
        "footnote":
            "البنود الاعتيادية أعلاه مُعلَنة. أما خطط العلاج "
            "المُهيكَلة (التأهيلات الشاملة، والزراعة مع الترميم "
            "العظمي الموسَّع، والتقويم المصحوب بجراحة الفكين) "
            "فتحظى بعرض سعر مُخصَّص بعد الزيارة الأولى مدتها "
            "سبعون دقيقة. لا يُعطى أي عرض سعر هاتفياً أو عبر "
            "البريد الإلكتروني قبل الزيارة السريرية.",
        "cta_heading":
            "عرض السعر دائماً <em>مكتوب، وموقَّع، ومُسلَّم بصيغة PDF.</em>",
        "cta_primary_label":   "احجز الزيارة الأولى",
        "cta_secondary_label": "اكتب إلينا",
    },

    # ─── MEDICI (team) — 4 dental specialists, mix gender ───
    "medici": {
        "eyebrow":  "أطباء الأسنان · الفريق المشترك",
        "headline": "أربعة توقيعات، <em>وملف طبي واحد.</em>",
        "intro":
            "يتشارك الشركاء الأربعة الملف الطبي ذاته، ويتشاورون "
            "في الخطط المعقّدة. لكل مريض طبيب مرجعي محدَّد، غير "
            "أن نظافة الصيانة يمكن أن يقوم بها أي عضو من أعضاء "
            "الفريق.",
        "doctors": [
            {
                "name":  "Dr.ssa Chiara Vespa",
                "role":  "المدير الطبي · التحفظي ومعالجة الجذور",
                "bio":
                    "أخصائية في طب الأسنان التحفظي، تخرّجت من "
                    "جامعة ميلانو واستكملت تدريبها في جامعة Loma "
                    "Linda. عضوة الجمعية الإيطالية لمعالجة الجذور "
                    "(SIE). تتولى التنسيق السريري في العيادة منذ "
                    "عام 2013.",
                "portrait": _CHIEF_PORTRAIT,
            },
            {
                "name":  "Dr. Riccardo Berti",
                "role":  "زراعة الأسنان والترميم العظمي",
                "bio":
                    "طبيب زراعة تخرّج من كلية طب الأسنان في جامعة "
                    "نيويورك، واستكمل تدريبه في علم الإطباق "
                    "السريري في جامعة Pavia. يختص بالزراعة الموجَّهة "
                    "بالحاسوب والتأهيلات المعقّدة والترميم العظمي.",
                "portrait":
                    "https://images.pexels.com/photos/6627850/pexels-photo-6627850.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr.ssa Sofia Liccardi",
                "role":  "التقويم وطب أسنان الأطفال",
                "bio":
                    "أخصائية تقويم الأسنان والفكين، تخرّجت من "
                    "جامعة Cattolica del Sacro Cuore. حاصلة على "
                    "اعتماد Invisalign Diamond Provider. تختص "
                    "بتقويم البالغين، والتقويم الاعتراضي للأطفال، "
                    "ورعاية المرضى الصغار حتى سن السادسة عشرة.",
                "portrait":
                    "https://images.pexels.com/photos/4687404/pexels-photo-4687404.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr. Andrea Carofiglio",
                "role":  "أمراض اللثة وطب الفم",
                "bio":
                    "طبيب لثة تخرّج من جامعة Bologna، واستكمل "
                    "تدريبه في جامعة Bern. عضو الجمعية الإيطالية "
                    "لأمراض اللثة وزراعة الأسنان (SIdP). يختص "
                    "بالتهاب اللثة المزمن وطب الفم.",
                "portrait":
                    "https://images.pexels.com/photos/6529057/pexels-photo-6529057.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
        ],
        "portrait_city": "ميلانو · بريرا",
    },

    # ─── PUBBLICAZIONI (blog_list) — page metadata at this level,
    # the actual post list lives at the TOP-LEVEL `posts` key (sibling
    # to `pubblicazioni`), the same shape Cardio + Derm use.
    "pubblicazioni": {
        "eyebrow":  "المنشورات والتوعية",
        "headline": "ما الذي كتبناه، <em>ولأي قارئ.</em>",
        "intro":
            "مقالات توعوية مَنشورة في مطبوعات متخصِّصة، وإسهامات "
            "سريرية في مجلات علمية. تراجع الدكتورة Vespa شخصياً "
            "كل المحتويات قبل النشر.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Denti+Co · عيادة أسنان مشتركة · ميلانو",
        "empty_body_fallback_paragraphs": [
            "المقال قيد الإعداد التحريري. سيُتاح النص الكامل "
            "قريباً.",
            "يصف هذا النص النائب نبرة المقال: ملاحظة سريرية يكتبها "
            "الطبيب بأسلوب مباشر بعيد عن المصطلحات التقنية، "
            "موجَّهة إلى المرضى الذين يريدون معلومات موثوقة عن "
            "صحتهم الفموية.",
        ],
    },

    # Posts list — TOP-LEVEL, sibling to `pubblicazioni`. Same shape
    # the blog_list.html template expects (slug, kicker, title, date,
    # read_min, author, lede).
    "posts": [
        {
            "slug":     "igiene-professionale-perche-semestrale",
            "kicker":   "النظافة والوقاية",
            "title":    "النظافة الفموية المهنية: لماذا التواتر نصف السنوي خيار سريري",
            "date":     "12 مارس 2025",
            "read_min": 8,
            "author":   "Dr.ssa Chiara Vespa",
            "lede":
                "تدعم الأدبيات السريرية تواتراً مخصَّصاً للنظافة "
                "الفموية، غير أن قاعدة الأشهر الستة تبقى أفضل "
                "توازن بين الكلفة، والتزام المريض، والنتيجة "
                "اللثوية على المدى البعيد.",
        },
        {
            "slug":     "impianti-carico-immediato-quando",
            "kicker":   "زراعة الأسنان",
            "title":    "التحميل الفوري في الزراعة: متى يكون مُشاراً إليه فعلاً",
            "date":     "23 يناير 2025",
            "read_min": 12,
            "author":   "Dr. Riccardo Berti",
            "lede":
                "يغري التحميل الفوري باختصار زمن العلاج، غير "
                "أنه ليس الحلّ الشامل. معايير اختيار المريض "
                "مُقيِّدة، وينبغي شرحها بصراحة قبل التدخل.",
        },
        {
            "slug":     "allineatori-trasparenti-cosa-non-fanno",
            "kicker":   "التقويم",
            "title":    "المتقومات الشفافة: ثلاثة أمور لا تقوم بها",
            "date":     "5 نوفمبر 2024",
            "read_min": 6,
            "author":   "Dr.ssa Sofia Liccardi",
            "lede":
                "هي فعّالة لدى غالبية البالغين، لكنها لا تحلّ "
                "كل شيء. ثلاثة حدود سريرية صريحة ينبغي أن "
                "يعرفها كل مريض قبل بدء الخطة.",
        },
        {
            "slug":     "parodontite-non-e-solo-gengivite",
            "kicker":   "أمراض اللثة",
            "title":    "الالتهاب اللثوي المتقدم ليس مجرد «نزيف لثة»",
            "date":     "18 سبتمبر 2024",
            "read_min": 5,
            "author":   "Dr. Andrea Carofiglio",
            "lede":
                "يصيب الالتهاب اللثوي المزمن بالغاً من اثنين بعد "
                "سن الخامسة والثلاثين، لكن تشخيصه يتأخر لأن "
                "العلامات الأولى صامتة. ثلاثة مؤشرات لثوية "
                "يمكن لكل مريض أن يسأل عنها طبيبه.",
        },
    ],

    # ─── CONTATTI (contact) — contact.html expects blocks 3-tuples,
    # form_title/intro/placeholders/consent, hours 3-tuples, transport
    # 2-tuples.
    "contatti": {
        "eyebrow":  "التواصل والمقر",
        "headline": "اكتبوا إلينا، <em>ونعاود الاتصال بكم في اليوم نفسه.</em>",
        "intro":
            "لحجز الزيارة الأولى أو جلسة نظافة الصيانة يمكنكم "
            "الاتصال بنا، أو الكتابة عبر WhatsApp، أو تعبئة "
            "النموذج أدناه. نردّ خلال يوم العمل ذاته.",
        # 4 info-blocks: (label, value, sub) 3-tuples · matches the four
        # SVG icons hard-coded in contact.html (pin · phone · email · clock)
        "blocks": [
            ("المقر",
             "Via Manzoni 18\n20121 ميلانو",
             "الطابق الرئيسي · مدخل مستقل"),
            ("الهاتف",
             "+39 02 7770 4488",
             "ردّ في يوم العمل ذاته"),
            ("البريد الإلكتروني",
             "studio@denticostudio.it",
             "للطلبات غير الطارئة"),
            ("ساعات العمل",
             "الإثنين – الجمعة · 8:30 – 19:30\nالسبت · 9:00 – 13:00",
             "الأحد مغلق"),
        ],
        "form_title": "اكتبوا إلينا، ونعاود الاتصال بكم في اليوم نفسه.",
        "form_intro":
            "نموذج للاستفسارات أو لتحديد موعد الزيارة الأولى. "
            "للحالات السريرية الطارئة اتصلوا بنا مباشرة.",
        "form_placeholders": {
            "first_name": "مريم",
            "last_name":  "الحسيني",
            "email":      "maryam.alhusseini@email.com",
            "phone":      "+39 333 12 34 567",
            "subject":    "زيارة أولى / نظافة / حالة طارئة",
            "message":    "أشيروا إلى الفترة الزمنية المفضَّلة والطبيب المرجعي إن وُجد.",
        },
        "form_helpers": {},
        "form_consent":
            "أوافق على معالجة بياناتي الشخصية حصراً لغرض معاودة "
            "الاتصال من قِبَل العيادة. النظام الأوروبي العام "
            "لحماية البيانات GDPR المادة 6 · يمكن التواصل مع "
            "مسؤول حماية البيانات عبر dpo@denticostudio.it.",
        "form_submit_note":
            "ردّ خلال يوم العمل التالي.",
        "hours_heading":    "ساعات الفتح",
        # 3-tuples (day, am, pm) — matches contact.html line 175
        "hours": [
            ("الإثنين",  "8:30 – 13:00", "14:00 – 19:30"),
            ("الثلاثاء", "8:30 – 13:00", "14:00 – 19:30"),
            ("الأربعاء", "8:30 – 13:00", "14:00 – 19:30"),
            ("الخميس",   "8:30 – 13:00", "14:00 – 19:30"),
            ("الجمعة",   "8:30 – 13:00", "14:00 – 19:30"),
            ("السبت",    "9:00 – 13:00", "—"),
            ("الأحد",    "—", "مغلق"),
        ],
        "transport_heading": "كيف تصلون إلينا",
        # 2-tuples (label, text)
        "transport": [
            ("المترو",        "خط M3 محطة Montenapoleone · 3 دقائق سيراً"),
            ("الترام",        "الخط 1 · محطة Manzoni"),
            ("القطار",        "محطة Centrale · 12 دقيقة عبر M3"),
            ("موقف السيارات", "كراج Via Bigli · 50 متراً · باتفاقية"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) — needs process steps + flat
    # form_fields (form_sections is optional · the appointment.html
    # falls back to a flat field list at line 173-174 when sections
    # are absent).
    "richiedi-visita": {
        "eyebrow":  "احجز جلسة نظافة · زيارة أولى",
        "headline": "احجزوا، <em>ونعاود الاتصال بكم خلال 24 ساعة.</em>",
        "intro":
            "عبّئوا النموذج: تحدّد السكرتارية الموعد الأول خلال "
            "يوم العمل التالي، وتؤكّده كذلك عبر الرسائل النصية "
            "أو WhatsApp.",
        "process_label":   "مسار الحجز",
        "process_heading": "من النموذج إلى الموعد <em>الأول</em>، في أربع خطوات.",
        # 4 process steps (num, title, blurb) — 3-tuples
        "process": [
            ("01", "النموذج والمعاودة",
             "تتلقّى السكرتارية النموذج، وتتحقّق من اكتمال "
             "البيانات، وتعاود الاتصال بكم خلال يوم العمل "
             "التالي لتحديد الموعد."),
            ("02", "التأكيد والتذكير",
             "تصلكم رسالة تأكيد عبر الرسائل النصية أو WhatsApp "
             "تتضمن التاريخ، والساعة، والطبيب المرجعي، وعنوان "
             "العيادة، والاتجاهات."),
            ("03", "زيارة أولى مدتها 70 دقيقة",
             "سوابق، وفحص سريري شامل، ومسح iTero، وصور داخل "
             "الفم وخارجه، ومسح لثوي، وتسليم الخطة السريرية "
             "بصيغة PDF."),
            ("04", "الخطة المكتوبة",
             "نقاش الخطة على كرسي العلاج مع عرض سعر بنداً "
             "بنداً. تُحسَم تكلفة الزيارة الأولى من أول علاج "
             "في الخطة."),
        ],
        "form_title": "احجز الموعد الأول",
        "form_band_side_note":
            "ردّ خلال 24 ساعة عمل. للحالات السريرية الطارئة "
            "اتصلوا مباشرة على +39 02 7770 4488.",
        "form_band_side_note_small":
            "تُستخدَم البيانات المجمَّعة حصراً لمعاودة الاتصال بكم · GDPR المادة 6.",
        "form_fields": [
            {"name": "first_name", "label": "الاسم",
             "type": "text",       "required": True,
             "placeholder": "مريم"},
            {"name": "last_name",  "label": "اللقب",
             "type": "text",       "required": True,
             "placeholder": "الحسيني"},
            {"name": "email",      "label": "البريد الإلكتروني",
             "type": "email",      "required": True,
             "placeholder": "maryam.alhusseini@email.com"},
            {"name": "phone",      "label": "الهاتف",
             "type": "tel",        "required": True,
             "placeholder": "+39 333 12 34 567"},
            {"name": "service",    "label": "العلاج المطلوب",
             "type": "select",     "required": True,
             "options": [
                 "النظافة الفموية المهنية",
                 "الزيارة الأولى (ملف طبي + خطة)",
                 "حالة طارئة في الأسنان",
                 "زيارة زراعة",
                 "زيارة تقويم",
                 "غير ذلك",
             ]},
            {"name": "preferred",  "label": "الفترة الزمنية المفضَّلة",
             "type": "select",     "required": False,
             "options": [
                 "صباحاً (8:30 – 13:00)",
                 "بعد الظهر (14:00 – 19:30)",
                 "صباح السبت",
                 "لا فرق",
             ]},
            {"name": "notes",      "label": "ملاحظات (اختيارية)",
             "type": "textarea",   "required": False,
             "full_width": True,
             "placeholder": "أشيروا إلى أي حساسية تجاه الأدوية، أو فحوص سابقة، أو الطبيب المرجعي."},
        ],
        "submit_label": "احجز الموعد",
        "consent":
            "أوافق على معالجة البيانات الشخصية حصراً لغرض "
            "معاودة الاتصال من قِبَل العيادة. GDPR المادة 6 · "
            "يمكن التواصل مع مسؤول حماية البيانات عبر "
            "dpo@denticostudio.it.",
        "footnote":
            "تُستخدَم البيانات المجمَّعة حصراً لمعاودة الاتصال "
            "بكم في شأن الطلب. الامتثال للنظام الأوروبي GDPR "
            "المادة 6 · يمكن التواصل مع مسؤول حماية البيانات "
            "عبر dpo@denticostudio.it.",
    },
}
