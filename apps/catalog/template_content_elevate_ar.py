"""Elevate — Startup SaaS Landing Kit · Arabic content tree.

Mirrors the shape of ``ELEVATE_CONTENT_IT`` exactly — same keys, same tuple
and list nesting, same field counts. Authored Session 41 for the Elevate
live i18n rollout of the startup-saas-landing archetype. Modern Standard
Arabic (الفصحى الحديثة) in a startup / growth-tech register — direct,
technical, candid. Latin script preserved for product names, tool names,
versions and proper names per the modern MENA tech-press convention
(Wamda, Hsoub, Microsoft Arabic docs). Western digits throughout.
"""
from __future__ import annotations

from typing import Any


ELEVATE_CONTENT_AR: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "الرئيسية",   "kind": "home"},
        {"slug": "prodotto",   "label": "المنتج",     "kind": "product"},
        {"slug": "prezzi",     "label": "الأسعار",    "kind": "pricing"},
        {"slug": "demo",       "label": "عرض توضيحي", "kind": "demo"},
        {"slug": "contatti",   "label": "تواصل",      "kind": "contact"},
    ],

    # Site-wide chrome
    "site": {
        "logo_initial": "E",
        "logo_word":    "Elevate",
        "tag":          "أداة تركّز على التحويل · للمؤسسين الذين يطلقون",
        "nav_cta":      "ابدأ مجاناً",
        "phone":        "hello@elevatekit.io",
        "email":        "hello@elevatekit.io",
        "address":      "Talent Garden Calabiana · ميلانو",
        "hours_compact":"غير متزامن أولاً · Slack 9-19 CET",
        "hours_footer_rows": [
            "عرض توضيحي عند الطلب · كل ثلاثاء 17:00 CET",
            "ساعات مكتب المؤسس · الجمعة 11:00 CET",
        ],
        "license":      "",
        "footer_intro":
            "Elevate هو GTM kit الذي ينقل شركتك الناشئة من قائمة "
            "الانتظار إلى أول MRR في أربعة عشر يوماً. Built for founders, "
            "by founders. نشحنه من ميلانو، تنشره أنت في أي مكان.",
        "foot_studio":   "المنتج",
        "foot_pages":    "الصفحات",
        "foot_contact":  "تواصل معنا",
        "foot_offices":  "سجل الإطلاقات",
        "shiplog_footer_rows": [
            "v2.9 · الجمعة · أداة بناء Hero بالسحب والإفلات",
            "v2.8 · أمس · مكتبة شهادات عملاء مميزة",
            "v2.7 · الثلاثاء · اختبار A/B مدمج عبر GrowthBook",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "banner_label":   "Series A · الربع الثاني 2026",
        "banner_text":    "نُغلق أول خمسين مقعد وصول مبكر",
        "banner_href":    "demo",

        "eyebrow":     "GTM kit تحويلي أولاً · لشركات SaaS والشركات الناشئة في مراحلها المبكرة",
        "headline":    "من <em>قائمة الانتظار</em> إلى أول <em>MRR</em> في أربعة عشر يوماً.",
        "intro":
            "Elevate هو kit الصفحات والأسعار والـ onboarding الذي "
            "يحوّل أول الزوّار إلى مستخدمين يدفعون. اختبار A/B مدمج، "
            "Stripe checkout بنقرة واحدة، copy kit عربي وإيطالي، "
            "نشر على Vercel في ثلاثين ثانية.",
        "primary_cta":   "ابدأ مجاناً · 14 يوماً",
        "primary_href":  "demo",
        "secondary_cta": "شاهد العرض التوضيحي · دقيقتان",
        "secondary_href":"prodotto",

        "trust_label":   "اعتمدته أكثر من 240 شركة ناشئة في مراحلها المبكرة",
        "trust_logos":   ["FLUX", "NOVA/", "QUANTA", "HELIX", "RIFT.", "CASP", "ARC", "LOOM"],

        # Product mockup card
        "mockup": {
            "chrome_label":     "elevate.app / dashboard / onboarding-flow",
            "chrome_dots":      ["●", "●", "●"],
            "badge":            "Live A/B",
            "metric_primary":   "↑ 38%",
            "metric_label":     "تحويل CTA الرئيسي",
            "metric_desc":      "مقابل المتغيّر B (control)",
            "secondary_metric": "+ € 12.4K",
            "secondary_label":  "MRR · آخر 30 يوماً",
            "secondary_desc":   "تحويل التجربة إلى اشتراك مدفوع: 22%",
            "feature_label":    "خطة Launch · 29 € / شهرياً",
            "perks":            ["الاستضافة + CDN مضمّنان", "نشر CLI · بدون أي إعداد", "دعم مباشر عبر Slack"],
        },

        # Feature pills under the hero
        "feature_pills":  ["Stripe + Linear", "اختبار A/B مدمج", "Edge analytics", "Copy kit عربي", "نشر في 30 ثانية"],

        # Capabilities — 6 cards in a 3x2 grid
        "features_label":   "ما الذي بداخله",
        "features_heading": "ستة وحدات، <em>تثبيت واحد فقط</em>.",
        "features_intro":
            "كل ما تحتاجه للانطلاق والبدء في تحقيق الدخل — مدمج "
            "مسبقاً، مختبر مسبقاً، موثّق مسبقاً.",
        "features": [
            {
                "icon": "→",
                "title": "أداة بناء Hero بالسحب والإفلات",
                "desc":
                    "عشرة تخطيطات Hero مختبرة على 1.200 شركة ناشئة. "
                    "اختبار A/B بين المتغيّرات دون كتابة سطر واحد من الكود.",
            },
            {
                "icon": "$",
                "title": "جدول الأسعار و Stripe",
                "desc":
                    "ثلاث خطط قابلة للتخصيص، تحويل checkout بنقرة واحدة، "
                    "إدارة الاشتراكات جاهزة من الصندوق. Webhook من Stripe "
                    "موصول مسبقاً بـ Linear و Slack.",
            },
            {
                "icon": "▲",
                "title": "Edge analytics",
                "desc":
                    "Web vitals، قمع التحويل، تتبع الإسناد متعدد النقاط — "
                    "تُجمع على طرف الشبكة، صفر أثر على TTI. خصوصية أولاً، "
                    "بلا cookies، متوافق مع GDPR.",
            },
            {
                "icon": "✱",
                "title": "تدفق الـ Onboarding",
                "desc":
                    "قائمة مهام موجَّهة متعدّدة الخطوات، شريط تقدّم، "
                    "مشغّلات بريد إلكتروني عند الإنجاز. متوسّط time-to-value "
                    "4 دقائق مقابل معيار القطاع البالغ 18 دقيقة.",
            },
            {
                "icon": "◐",
                "title": "Copy kit متعدد اللغات",
                "desc":
                    "ستون كتلة نصية مختبَرة على أسواق IT/EN/FR/AR — "
                    "headline و sub و CTA و microcopy للـ onboarding و error states. "
                    "جاهزة للتعديل مباشرة عبر Markdown.",
            },
            {
                "icon": "↗",
                "title": "نشر CLI",
                "desc":
                    "elevate deploy → Vercel / Netlify / Cloudflare في "
                    "ثلاثين ثانية. معاينات تلقائية للفروع، استعادة بأمر "
                    "واحد، متغيّرات البيئة متزامنة تلقائياً.",
            },
        ],

        # Live product walkthrough invitation
        "product_demo_card": {
            "label":      "شاهد Elevate على الهواء مباشرة",
            "heading":    "خمس عشرة دقيقة مع من بناه.",
            "intro":
                "بدلاً من فيديو مسجَّل: نحجز لك جولة قصيرة على المشروع "
                "الحقيقي — محرّر السحب والإفلات، معالج الأسعار، ربط "
                "Stripe و Linear، النشر على Vercel. أسئلة حقيقية، مشروع "
                "حقيقي، دون أي رسائل متابعة.",
            "poster":     "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1800&q=80&auto=format&fit=crop",
            "primary_cta":    "احجز الجولة",
            "primary_href":   "demo",
            "secondary_cta":  "استكشف المنتج",
            "secondary_href": "prodotto",
            "caption":        "جولة 1-1 · تقويم مباشر",
        },

        # Metric strip on dark band
        "metric_label":   "أرقام الـ kit في الإنتاج",
        "metric_heading": "الستاك الذي يطلق",
        "metric_strip": [
            ("3.1 ×",  "متوسط تحويل الصفحة"),
            ("14 يوماً","من النشر إلى أول مستخدم يدفع"),
            ("99.98%", "تشغيل البنية التحتية"),
            ("4 دقائق","الوسيط لـ time-to-value"),
        ],

        # Integrations row
        "integrations_label":   "تكاملات جاهزة من الصندوق",
        "integrations_heading": "موصولة مسبقاً بالستاك الذي تستخدمه",
        "integrations": [
            ("Stripe",     "Subscription · Checkout · Tax"),
            ("Linear",     "Issue tracking · changelog تلقائي"),
            ("Slack",      "إشعارات · تنبيهات MRR"),
            ("Vercel",     "نشر · معاينة · استعادة"),
            ("PostHog",    "قمع · session replay"),
            ("GrowthBook", "اختبار A/B · feature flags"),
            ("Loops",      "رسائل المعاملات"),
            ("Cal.com",    "حجز عروض توضيحية تلقائي"),
        ],

        # Pricing teaser
        "pricing_teaser_label":   "أسعار شفّافة",
        "pricing_teaser_heading": "ثلاث خطط، بدون أي رسوم إعداد.",
        "pricing_teaser_intro":
            "إلغاء بنقرة واحدة، فوترة شهرية أو سنوية، تجربة مجانية "
            "لأربعة عشر يوماً دون بطاقة ائتمان.",
        "pricing_teaser": [
            {"name": "Launch",  "price": "29 €",  "period": "/ شهرياً", "tag": "للمؤسسين المنفردين",
             "highlight": False, "perks": ["جميع الوحدات", "استضافة + CDN", "بريد Slack"]},
            {"name": "Scale",   "price": "79 €",  "period": "/ شهرياً", "tag": "الأكثر اختياراً",
             "highlight": True, "perks": ["كل ما في Launch +", "A/B متقدّم", "5 مشاريع"]},
            {"name": "Studio",  "price": "199 €", "period": "/ شهرياً", "tag": "للاستوديوهات والوكالات",
             "highlight": False, "perks": ["كل ما في Scale +", "مشاريع غير محدودة", "White-label"]},
        ],
        "pricing_teaser_cta":      "قارن الخطط بالتفصيل",
        "pricing_teaser_cta_href": "prezzi",

        # Founder proof
        "founders_label":   "مؤسسون أطلقوا مع Elevate",
        "founders_heading": "الكلمة لمن <em>يطلق فعلاً</em>.",
        "founders": [
            {
                "name":  "Anna Vecchietti",
                "role":  "Founder · Quanta Analytics",
                "quote":
                    "جرّبت ثلاث boilerplate واثنين من منصّات no-code. "
                    "مع Elevate انطلقت في عطلتَي أسبوع، وأول MRR جاء "
                    "بعد سبعة عشر يوماً من النشر. الفارق هو copy kit — "
                    "لا حاجة لإعادة كتابة كل headline من الصفر.",
                "metric_primary": "+ € 4.2K",
                "metric_label":   "MRR خلال أول 60 يوماً",
            },
            {
                "name":  "Davide Zonca",
                "role":  "CTO · Helix Workflows",
                "quote":
                    "الستاك الذي احتجته دون سبعة أيام من الإعداد. "
                    "Stripe و GrowthBook و Linear موصولة مسبقاً يعني "
                    "أننا أمضينا الشهر الأول في الحديث مع المستخدمين، "
                    "لا في إعداد webhook.",
                "metric_primary": "× 3.4",
                "metric_label":   "التحويل مقارنة بالصفحة السابقة",
            },
        ],

        # Ship log
        "shiplog_label":   "سجل الإطلاقات الحي",
        "shiplog_heading": "ما أطلقناه مؤخراً",
        "shiplog_intro":
            "Elevate في continuous deploy. كل ميزة تُطلق تظهر هنا في "
            "الوقت الفعلي — لا خرائط طريق نظرية، لا مواسم منتج. ما "
            "تراه اليوم هو ما ستستخدمه غداً.",
        "shiplog": [
            {"version": "v2.9", "date": "الجمعة",  "title": "أداة بناء Hero بالسحب والإفلات",
             "desc": "عشرة تخطيطات مختبرة، اختبار A/B بين المتغيّرات، معاينة مباشرة."},
            {"version": "v2.8", "date": "أمس",     "title": "مكتبة شهادات عملاء مميزة",
             "desc": "أربعة تخطيطات (carousel و masonry و single-feature و video-first) مع حركات reveal."},
            {"version": "v2.7", "date": "الثلاثاء", "title": "اختبار A/B مدمج عبر GrowthBook",
             "desc": "معالج إعداد تجربة في 4 خطوات، hypothesis tracker، دلالة إحصائية تلقائية."},
            {"version": "v2.6", "date": "الإثنين", "title": "Stripe Checkout بنقرة واحدة",
             "desc": "مُكيّفات لأكبر 4 مزوّدي دفع أوروبيين، إدارة ضريبة VAT تلقائية."},
            {"version": "v2.5", "date": "الأسبوع الماضي", "title": "Edge analytics بخصوصية أولاً",
             "desc": "تتبّع بلا cookies، أقل من 4KB على TTI، لوحة قمع مضمّنة."},
        ],
        "shiplog_cta":      "اشترك في سجل الإطلاقات عبر Slack",
        "shiplog_cta_href": "demo",
        "shiplog_release_label": "الإصدار القادم",
        "shiplog_release_value": "v3.0 · أول إثنين من الشهر",
        "shiplog_release_chip":  "RC حي",

        # Final CTA band before footer
        "cta_label":     "ابدأ الآن",
        "cta_heading":   "أربعة عشر يوماً مجاناً. أربعون دقيقة للانطلاق.",
        "cta_intro":
            "بدون بطاقة ائتمان لتفعيل التجربة. Slack مباشر مع الفريق "
            "المؤسس. إن لم تُطلق خلال أسبوعين، نُعيد لك المبلغ. "
            "وعد مكتوب.",
        "cta_primary":   "فعّل التجربة المجانية",
        "cta_primary_href": "demo",
        "cta_secondary": "اطّلع على الخطة الكاملة",
        "cta_secondary_href": "prezzi",
    },

    # ─── PRODOTTO (product tour) ────────────────────────────────
    "prodotto": {
        "eyebrow":   "جولة المنتج · v2.9 (أبريل 2026)",
        "headline":  "كل ما <em>عليك إطلاقه</em> لتنطلق.",
        "intro":
            "ستة وحدات أساسية + اثنتا عشرة تكاملاً جاهزاً من الصندوق. "
            "لا plugin لإعدادها، لا boilerplate لعمل fork عليه، لا "
            "Twitter thread لاتباعه لفعل ما ينبغي أن يكون بديهياً. "
            "افتح، عدّل، انشر.",

        # Product modules — expanded from home
        "modules_label":   "الوحدات الأساسية",
        "modules_heading": "ستة أجزاء، تثبيت واحد",
        "modules": [
            {
                "num":   "01",
                "title": "أداة بناء Hero بالسحب والإفلات",
                "blurb":
                    "عشرة تخطيطات Hero مختبرة على 1.200 شركة ناشئة في "
                    "مراحلها المبكرة. يأتي كل تخطيط مع ثلاث متغيّرات "
                    "نصية (B2B و B2C و dev-tool) ومع اختبار A/B مدمج.",
                "highlights": [
                    "10 تخطيطات · 30 متغيّراً نصياً",
                    "A/B بين المتغيّرات دون كود",
                    "Headline و sub و CTA و شارة اجتماعية كلها قابلة للتعديل",
                    "تحسين منفصل للموبايل والديسكتوب",
                ],
            },
            {
                "num":   "02",
                "title": "جدول الأسعار و Stripe Checkout",
                "blurb":
                    "ثلاث خطط قابلة للتخصيص مع إبراز تلقائي للخطة "
                    "الوسطى. إدارة اشتراكات Stripe، checkout بنقرة "
                    "واحدة على الموبايل، إدارة VAT الأوروبية تلقائياً.",
                "highlights": [
                    "1 أو 2 أو 3 أو 4 خطط · إبراز حسب الاختيار",
                    "تبديل شهري / سنوي مضمّن",
                    "Stripe Tax في 38 دولة أوروبية",
                    "Webhook من Stripe إلى Slack موصول مسبقاً",
                ],
            },
            {
                "num":   "03",
                "title": "Edge analytics بخصوصية أولاً",
                "blurb":
                    "Web vitals، قمع متعدّد الخطوات، إسناد متعدّد "
                    "النقاط — كلها تُجمع على طرف الشبكة عبر "
                    "Cloudflare Worker. بلا cookies، متوافق مع GDPR، "
                    "أقل من 4KB على TTI.",
                "highlights": [
                    "بلا cookies · GDPR · ePrivacy نظيف",
                    "Web Vitals · LCP · FID · CLS في لوحة التحكم",
                    "قمع تحويل بصري",
                    "موصل PostHog اختياري",
                ],
            },
            {
                "num":   "04",
                "title": "تدفق onboarding موجَّه",
                "blurb":
                    "قائمة مهام متعدّدة الخطوات مع شريط تقدّم، "
                    "احتفال بالإنجازات، مشغّلات بريد تلقائية. "
                    "وسيط time-to-value 4 دقائق مقابل معيار القطاع "
                    "البالغ 18 دقيقة.",
                "highlights": [
                    "قائمة مهام قابلة للتخصيص بالسحب والإفلات",
                    "مشغّلات بريد عبر Loops · Resend · Postmark",
                    "Achievement badge مضمّن",
                    "إعادة تفاعل تلقائية بعد 48 ساعة",
                ],
            },
            {
                "num":   "05",
                "title": "Copy kit متعدد اللغات (IT + EN + FR + AR)",
                "blurb":
                    "ستون كتلة نصية تحريرية مختبرة على أسواق "
                    "IT/EN/FR/AR. Headline و sub و CTA و microcopy "
                    "للـ onboarding و error states و empty states.",
                "highlights": [
                    "60 كتلة · IT + EN + FR + AR",
                    "نبرة الصوت قابلة للتخصيص",
                    "تحرير Markdown مباشر",
                    "مكتبة snippet مع بحث دلالي",
                ],
            },
            {
                "num":   "06",
                "title": "نشر CLI · ثلاثون ثانية",
                "blurb":
                    "elevate deploy. ثلاثون ثانية لأول نشر حي، "
                    "معاينات تلقائية للفروع على PR، استعادة بأمر "
                    "واحد، متغيّرات البيئة متزامنة بين dev / staging / prod.",
                "highlights": [
                    "Vercel · Netlify · Cloudflare adapter",
                    "معاينات تلقائية للفروع على PR",
                    "استعادة فورية · صفر downtime",
                    "مزامنة env-var · dev / staging / prod",
                ],
            },
        ],

        # Integrations grid — bigger
        "integrations_label":   "تكاملات جاهزة من الصندوق",
        "integrations_heading": "الستاك الذي تحتاجه، موصول مسبقاً.",
        "integrations_intro":
            "اثنتا عشرة تكاملاً أصلياً، صفر plugin للتثبيت. تلك "
            "التي لا تراها هنا نضيفها إن طلبتها على Slack.",
        "integrations_full": [
            {"name": "Stripe",     "category": "المدفوعات",   "desc": "Subscription · Checkout · Tax · Connect"},
            {"name": "Linear",     "category": "التتبّع",     "desc": "Issue · Cycles · changelog منشور تلقائياً"},
            {"name": "Slack",      "category": "التواصل",     "desc": "إشعارات · تنبيهات MRR · ملخّص يومي"},
            {"name": "Vercel",     "category": "النشر",        "desc": "نشر إنتاج · فروع معاينة · استعادة"},
            {"name": "Netlify",    "category": "النشر",        "desc": "Edge functions · build hooks · مزامنة analytics"},
            {"name": "Cloudflare", "category": "النشر",        "desc": "Workers · KV · D1 · R2 storage"},
            {"name": "PostHog",    "category": "التحليلات",   "desc": "قمع · session replay · feature flag"},
            {"name": "GrowthBook", "category": "التجارب",     "desc": "اختبار A/B · hypothesis tracker · stat-sig تلقائي"},
            {"name": "Loops",      "category": "البريد",       "desc": "معاملات · تسلسلات onboarding"},
            {"name": "Resend",     "category": "البريد",       "desc": "معاملات · React Email templates"},
            {"name": "Cal.com",    "category": "الحجوزات",    "desc": "حجز عروض · routing · webhook"},
            {"name": "Plain",      "category": "الدعم",        "desc": "صندوق دعم · CRM مع فرز بالذكاء الاصطناعي"},
        ],

        # Architecture
        "stack_label":   "البنية",
        "stack_heading": "ماذا يعمل أين (ولماذا)",
        "stack_intro":
            "شفافية تقنية — لا سحر، لا lock-in مخفي. الستاك موثّق "
            "علناً، والكود بكامله قابل للتصدير بنقرة واحدة إن قرّرت "
            "الرحيل.",
        "stack": [
            ("Frontend",    "Next.js 15 · React 19 · App Router · Server Actions"),
            ("Edge",        "Cloudflare Workers + KV للـ analytics و A/B"),
            ("قاعدة البيانات", "PostgreSQL · Prisma · Neon serverless"),
            ("المصادقة",      "Clerk · OAuth · passkey · magic link"),
            ("المدفوعات",     "Stripe Subscriptions + Stripe Tax + Stripe Connect"),
            ("البريد",        "Loops أو Resend حسب الاختيار · React Email templates"),
            ("التحليلات",     "PostHog اختياري · edge analytics أصلي"),
            ("التجارب",       "GrowthBook · self-hosted أو cloud"),
        ],

        "cta_heading":   "جاهز لرؤيته في العمل؟",
        "cta_intro":
            "عرض توضيحي مباشر مع أحد أعضاء الفريق المؤسس كل ثلاثاء "
            "الساعة 17:00 CET. نصف ساعة مكالمة، screen-share، "
            "الأسئلة التقنية مرحّب بها.",
        "cta_primary":   "احجز عرضاً توضيحياً",
        "cta_primary_href": "demo",
        "cta_secondary": "اطّلع على الخطط",
        "cta_secondary_href": "prezzi",
    },

    # ─── PREZZI (pricing) ───────────────────────────────────────
    "prezzi": {
        "eyebrow":  "أسعار شفّافة · 2026",
        "headline": "إلغاء بنقرة واحدة. <em>دائماً</em>.",
        "intro":
            "ثلاث خطط، بدون رسوم إعداد، فوترة شهرية أو سنوية (شهرا "
            "هدية على الفوترة السنوية). أربعة عشر يوماً تجربة مجانية، "
            "دون بطاقة ائتمان.",

        # Highlight badge label
        "highlight_badge": "الأكثر اختياراً",
        "annual_prefix":   "أو",

        # Toggle row UI cue
        "billing_toggle_label": "الفوترة",
        "billing_toggle_options": [
            ("monthly", "شهرية"),
            ("annual",  "سنوية · –17%"),
        ],

        # Three pricing tiers
        "tiers": [
            {
                "name":     "Launch",
                "tag":      "للمؤسسين المنفردين",
                "price":    "29 €",
                "annual":   "24 €",
                "period":   "/ شهرياً",
                "annual_period": "/ شهرياً · بفوترة سنوية",
                "highlight": False,
                "blurb":
                    "كل ما يلزم للانطلاق بمنتج واحد فقط. مصمَّمة للمؤسس "
                    "المنفرد أو لأول أسبوع في الفريق المؤسس.",
                "cta":         "ابدأ مجاناً",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "جميع الوحدات الأساسية الست"),
                    ("✓", "استضافة + CDN عالمي مضمّنان"),
                    ("✓", "نشر CLI · معاينات تلقائية للفروع"),
                    ("✓", "Edge analytics + قمع أساسي"),
                    ("✓", "1 مشروع · 1 نطاق مخصّص"),
                    ("✓", "Slack مباشر مع الفريق المؤسس"),
                    ("○", "اختبار A/B أساسي (يدوي)"),
                    ("○", "1 copy kit (IT أو EN أو FR أو AR)"),
                ],
            },
            {
                "name":     "Scale",
                "tag":      "الأكثر اختياراً · للشركات الناشئة بعد PMF",
                "price":    "79 €",
                "annual":   "65 €",
                "period":   "/ شهرياً",
                "annual_period": "/ شهرياً · بفوترة سنوية",
                "highlight": True,
                "blurb":
                    "الخطة للفريق المؤسس الذي وجد product/market fit "
                    "ويتوسّع. تضيف A/B متقدّماً، ومشاريع متعدّدة، "
                    "وonboarding بلمسة شخصية.",
                "cta":         "ابدأ مجاناً",
                "cta_href":    "demo",
                "perks": [
                    ("✓", "كل ما في Launch +"),
                    ("✓", "اختبار A/B متقدّم (GrowthBook مدمج)"),
                    ("✓", "5 مشاريع · نطاقات مخصّصة غير محدودة"),
                    ("✓", "موصل PostHog + session replay"),
                    ("✓", "Stripe Tax + Stripe Connect"),
                    ("✓", "جميع copy kits الأربعة (IT + EN + FR + AR)"),
                    ("✓", "Onboarding 1-1 مع الفريق المؤسس (60 دقيقة)"),
                    ("✓", "قناة Slack مخصّصة · SLA 4 ساعات"),
                ],
            },
            {
                "name":     "Studio",
                "tag":      "للاستوديوهات والوكالات وبنّائي المشاريع",
                "price":    "199 €",
                "annual":   "165 €",
                "period":   "/ شهرياً",
                "annual_period": "/ شهرياً · بفوترة سنوية",
                "highlight": False,
                "blurb":
                    "للوكالات والاستوديوهات الإبداعية وبنّائي المشاريع "
                    "الذين يطلقون عدّة صفحات لعملاء مختلفين. مشاريع "
                    "غير محدودة و white-label كامل.",
                "cta":         "تواصل معنا",
                "cta_href":    "contatti",
                "perks": [
                    ("✓", "كل ما في Scale +"),
                    ("✓", "مشاريع غير محدودة · branding بـ white-label"),
                    ("✓", "حساب فرعي لكل عميل"),
                    ("✓", "API كاملة · webhook مخصّص"),
                    ("✓", "SLA ساعة واحدة · دعم هاتفي"),
                    ("✓", "مدير حساب مخصّص"),
                    ("✓", "مراجعة ربع سنوية مع الفريق المؤسس"),
                    ("✓", "Audit trail · توافق SOC 2"),
                ],
            },
        ],

        # Comparison
        "comparison_label":   "ما ليس موجوداً (ولماذا)",
        "comparison_heading": "الشفافية التي يتجنّبها الآخرون",
        "comparison": [
            ("رسوم الإعداد",
             "أبداً. لا على Launch ولا على Scale ولا على Studio. إن وجدت "
             "boilerplate منافساً لا يطلب منك رسوم إعداد + يعطيك الستاك "
             "موصولاً مسبقاً، أخبرنا ونعيد لك قيمة الشهر الأول."),
            ("Lock-in للكود",
             "أبداً. كل كودك قابل للتصدير عبر CLI بأمر واحد. إن قرّرت "
             "مغادرة Elevate، ننقل لك النشر إلى Vercel خاص بك مجاناً "
             "خلال 24 ساعة."),
            ("رسوم خفيّة",
             "أبداً. ما تقرأه هو ما تدفعه. ضريبة VAT الأوروبية تُحسب "
             "تلقائياً وتُعرض في checkout — لا مفاجآت في الفاتورة."),
            ("حدّ على المعاملات",
             "أبداً. Stripe Connect بلا سقف للمعاملات أو الحجم. ببيع "
             "10 اشتراكات أو 10.000 — السعر ذاته."),
        ],

        # FAQ accordion
        "faq_label":   "الأسئلة الشائعة",
        "faq_heading": "ما يسألوننا عنه أكثر",
        "faq": [
            ("هل يمكنني التجربة قبل الدفع؟",
             "نعم، أربعة عشر يوماً من التجربة الكاملة دون بطاقة ائتمان. "
             "تحصل على الوصول إلى جميع وحدات خطة Scale خلال التجربة — "
             "إن قرّرت البقاء، اختر الخطة التي تناسبك. وإن لم تقرّر، "
             "تنتهي التجربة تلقائياً، بلا أي خصم تلقائي."),
            ("ماذا يحدث إن ألغيت؟",
             "تُلغي من لوحة التحكم بنقرة واحدة في أي وقت. يبقى نشرك "
             "حياً حتى نهاية الفترة المدفوعة. نُصدّر لك الكود عبر CLI "
             "ونساعدك على الهجرة إلى Vercel/Netlify خاص بك إن أردت "
             "متابعة العمل باستقلالية."),
            ("هل لديكم خصم للشركات الناشئة؟",
             "نعم، 50% على الأشهر الستة الأولى للشركات الناشئة في "
             "مرحلة pre-seed (تمويل < 500 ألف يورو) و 30% على السنة "
             "الأولى للشركات في مرحلة post-seed. اكتب إلى "
             "hello@elevatekit.io مع pitch deck لتفعيل العرض."),
            ("هل يتكامل مع ستاكنا الحالي؟",
             "على الأرجح نعم. تغطي التكاملات الأصلية الاثنتا عشرة 90% "
             "من الستاك الذي نراه، وتسمح لك REST API + webhook "
             "المخصّص بوصل ما ينقص. إن احتجت تكاملاً غير موجود، "
             "اكتب لنا على Slack — نطلقه عادة خلال أسبوعين."),
            ("هل يمكنني الاستضافة على بنيتي الخاصة؟",
             "على خطة Studio، نعم — نعطيك Docker container و schema "
             "Postgres لاستضافتهما حيث تفضّل. على خطتَي Launch و "
             "Scale، الاستضافة مضمّنة وجزء من قيمة الـ kit."),
            ("هل الفواتير من إيطاليا؟",
             "نعم، نفوتر من ميلانو باليورو برقم VAT إيطالي، وفوترة "
             "إلكترونية SDI مضمّنة. للعملاء الأوروبيين من خارج إيطاليا، "
             "الفاتورة بنظام reverse-charge VAT."),
        ],

        "cta_heading":   "جاهز للبدء؟",
        "cta_intro":
            "أربعة عشر يوماً مجاناً. بلا بطاقة ائتمان. أربعون دقيقة "
            "للانطلاق بأول نشر لك.",
        "cta_primary":   "فعّل التجربة المجانية",
        "cta_primary_href": "demo",
        "cta_secondary": "أسئلة؟ اكتب لنا",
        "cta_secondary_href": "contatti",
    },

    # ─── DEMO (lead form) ───────────────────────────────────────
    "demo": {
        "eyebrow":  "عرض توضيحي مباشر · الثلاثاء 17:00 CET",
        "headline": "نصف ساعة مع <em>عضو من الفريق المؤسس</em>.",
        "intro":
            "عرض توضيحي مباشر كل ثلاثاء الساعة 17:00 CET. ثلاثون "
            "دقيقة screen-share — نعرض كيف تُهيّأ طبقة أسعار، وكيف "
            "يُطلق اختبار A/B، وكيف يُنفَّذ أول نشر. الأسئلة التقنية "
            "مرحّب بها، ولا حاجة لـ pitch deck.",

        # Form
        "form_label":   "احجز موعداً",
        "form_heading": "املأ النموذج ونؤكّد لك خلال ساعة",
        "form_intro":
            "موعد الثلاثاء القادم هو الذي ستحصل عليه افتراضياً. إن "
            "فضّلت موعداً مخصّصاً، اختر «موعد مخصّص» ونراسلك لتحديده. "
            "تعمل بشكل غير متزامن فقط؟ لا بأس، اطّلع على الخيار أدناه.",
        "form_fields": [
            {"name": "name",     "label": "الاسم",       "type": "text",  "required": True,  "placeholder": "مثال: Anna",
             "helper": "لنسلّم عليك خلال العرض التوضيحي."},
            {"name": "email",    "label": "البريد الإلكتروني", "type": "email", "required": True,  "placeholder": "anna@startup.io",
             "helper": "دعوة التقويم + Loom تصل إلى هنا."},
            {"name": "company",  "label": "الشركة الناشئة", "type": "text",  "required": True,  "placeholder": "مثال: Quanta Analytics",
             "helper": "الاسم الذي تستخدمه للـ commit والفوترة."},
            {"name": "role",     "label": "الدور",       "type": "select","required": True,
             "options": ["مؤسس منفرد", "Co-founder · CEO", "Co-founder · CTO", "Co-founder · آخر", "موظف 1-5", "آخر"],
             "helper": "إن كنت بمفردك، «مؤسس منفرد» هو الخيار المناسب."},
            {"name": "stage",    "label": "المرحلة",     "type": "select","required": True,
             "options": ["ما قبل الفكرة / نستكشف", "ما قبل الإطلاق / قائمة انتظار", "ما بعد الإطلاق / نبحث عن PMF", "ما بعد PMF / نتوسّع"],
             "helper": "يتكيّف العرض التوضيحي: ما قبل الإطلاق يرى الـ onboarding + قائمة الانتظار، ما بعد PMF يرى طبقات الأسعار + A/B."},
            {"name": "slot",     "label": "الموعد المفضّل", "type": "select","required": True,
             "options": ["الثلاثاء القادم 17:00 CET", "موعد مخصّص (سنراسلك)", "غير متزامن — أريد Loom مسجّلاً"],
             "helper": "الخيار غير المتزامن = تستلم Loom مدّته 12 دقيقة على البريد فوراً."},
            {"name": "stack",    "label": "الستاك الحالي",
             "type": "text", "required": False,
             "placeholder": "مثال: Next.js + Vercel + Stripe",
             "helper": "اختياري. نوجّه الحديث مباشرة إلى نقاط التكامل المناسبة."},
            {"name": "context",  "label": "ما الذي تحتاج إلى معرفته؟", "type": "textarea",
             "required": False, "full_width": True,
             "placeholder": "أسئلة محدّدة، كتل تريد رؤيتها في العرض، شكوك تقنية... (اختياري)",
             "helper": "يكفي سطران. أي شكّ تقني نعالجه بصراحة."},
        ],

        "form_sections": [
            {"num": "01", "title": "من أنت",
             "meta": "لا BDR، لا sequence — يُجيبك عضو من الفريق المؤسس.",
             "fields": ["name", "email", "company"]},
            {"num": "02", "title": "السياق",
             "meta": "لتكييف العرض التوضيحي مع مرحلتك وستاكك.",
             "fields": ["role", "stage", "stack"]},
            {"num": "03", "title": "تفضيلات العرض التوضيحي",
             "meta": "مباشر كل ثلاثاء الساعة 17:00 CET، أو غير متزامن عبر Loom.",
             "fields": ["slot", "context"]},
            {"num": "04", "title": "المواد (اختيارية)",
             "meta": "Loom خاص بك، أو لقطات شاشة للمنتج، أو metrics snapshot "
                     "تسمح لنا بالحضور مستعدّين.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "demo_allegati",
            "label":    "مواد سياقية",
            "helper":   "PDF · PNG · JPG · MP4 · MOV · 3 ملفات كحد أقصى، 25 ميغابايت إجمالاً. "
                        "مفيدة لمن يريد أن نُلقي نظرة على المنتج أو قمع التحويل الحالي.",
            "accept":   ".pdf,.png,.jpg,.jpeg,.mp4,.mov",
            "multiple": True,
            "primary":  "اسحب هنا deck أو لقطة شاشة أو Loom أو",
            "link":     "تصفّح من المجلد",
            "meta":     "PDF / PNG / JPG / MP4 · 25 ميغابايت كحد أقصى",
        },

        "form_submit_label": "احجز العرض التوضيحي",
        "form_submit_note":
            "تأكيد خلال ساعة في أوقات المكتب (9-19 CET) · بلا نشرة "
            "بريدية، بلا sequence تلقائي.",
        "form_consent":
            "بتسجيلك توافق على استلام دعوة التقويم ورسالة تذكير قبل "
            "24 ساعة. بلا نشرة بريدية، بلا sequence تلقائي. معالجة "
            "البيانات وفق اللائحة الأوروبية 679/2016.",

        # Async option block
        "async_label":   "تفضّل العمل بشكل غير متزامن؟",
        "async_heading": "Loom مسجّل مدّته 12 دقيقة",
        "async_intro":
            "إن لم تتمكّن من حضور العرض التوضيحي المباشر، سجّلنا لك "
            "Loom مدّته اثنتا عشرة دقيقة يعرض الإعداد الكامل من "
            "البداية إلى النهاية. ستستلمه على البريد خلال ساعة من "
            "الطلب.",
        "async_cta":     "استلم Loom عبر البريد",
        "async_cta_href": "demo",

        # Trust strip
        "trust_label":   "ماذا تتوقّع من العرض التوضيحي",
        "trust_items": [
            ("01", "نصف ساعة screen-share",
             "لا شرائح. نفتح التطبيق، نُهيّأ طبقة أسعار، نطلق اختبار A/B، ننشر."),
            ("02", "الأسئلة التقنية مرحّب بها",
             "Latency على الـ edge، schema Postgres، webhook Stripe — أي "
             "سؤال حول التنفيذ نعالجه بصراحة."),
            ("03", "لا ضغط للإغلاق",
             "لا نُغلق صفقة خلال المكالمة. إن احتجت، نمنحك وصولاً إلى "
             "التجربة فوراً؛ وإلا نعود للحديث بعد أسبوع."),
        ],

        "footnote":
            "يقود العروض التوضيحية أحد المؤسّسين الثلاثة لـ Elevate "
            "(لا BDR خارجيون). إن لم تناسبك نافذة الساعة 17:00 من يوم "
            "الثلاثاء حسب توقيتك، نقترح عليك موعداً بديلاً عبر البريد "
            "خلال 24 ساعة.",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "تواصل معنا · غير متزامن أولاً",
        "headline": "Slack، بريد، أو عرض مباشر. <em>أنت تختار</em>.",
        "intro":
            "«غير متزامن أولاً» يعني أننا نردّ خلال ساعة في أوقات "
            "المكتب (9-19 CET) وأن القرارات تُتّخذ كتابياً. إن فضّلت "
            "مكالمة، يكفي حجزها — مضمّنة في جميع الخطط، بلا أي رسوم "
            "إضافية.",

        # Channels grid
        "channels_label":   "أربع قنوات، شخص واحد يردّ عليك",
        "channels": [
            {
                "icon":  "✉",
                "title": "البريد الإلكتروني",
                "value": "hello@elevatekit.io",
                "desc":  "الفريق المؤسس يقرأ كل شيء. ردّ خلال ساعة في أوقات المكتب.",
                "cta":   "اكتب الآن",
            },
            {
                "icon":  "#",
                "title": "مجتمع Slack",
                "value": "elevate-founders.slack.com",
                "desc":  "قناة لمن فعّل التجربة أو خطة. أكثر من 220 مؤسّساً بالداخل.",
                "cta":   "اطلب الدعوة",
            },
            {
                "icon":  "▶",
                "title": "عرض توضيحي مباشر",
                "value": "الثلاثاء 17:00 CET",
                "desc":  "ثلاثون دقيقة screen-share مع عضو من الفريق المؤسس. خيار غير متزامن متاح.",
                "cta":   "احجز الموعد",
            },
            {
                "icon":  "✱",
                "title": "ساعات مكتب المؤسس",
                "value": "الجمعة 11:00 CET",
                "desc":  "مكالمة أسبوعية مفتوحة لخطّتَي Scale و Studio. أسئلة عامة، إجابات مفتوحة.",
                "cta":   "اشترك في التقويم",
            },
        ],

        # Founders block
        "team_label":   "الفريق المؤسس",
        "team_heading": "الأشخاص الذين يقرؤون رسائلك",
        "team_intro":
            "حين تكتب إلى hello@elevatekit.io، يردّ عليك أحد هؤلاء "
            "الثلاثة — لا BDR خارجي، لا copilot بالذكاء الاصطناعي. "
            "في الأسفل، بريداتهم المباشرة لطلبات محدّدة.",
        "team": [
            {
                "name":  "Riccardo Camillini",
                "role":  "Co-founder · Product",
                "email": "riccardo@elevatekit.io",
                "tag":   "أسئلة المنتج · خارطة الطريق",
                "bio":
                    "ثلاث exit سابقة كـ technical founder، آخرها إلى "
                    "صندوق SaaS B2B أوروبي. يتولّى product strategy "
                    "وخارطة الطريق وقرارات البنية.",
            },
            {
                "name":  "Beatrice Lavia",
                "role":  "Co-founder · Engineering",
                "email": "beatrice@elevatekit.io",
                "tag":   "أسئلة تقنية · الستاك · API",
                "bio":
                    "ثماني سنوات كمهندسة senior في Vercel و Linear. "
                    "صمّمت edge analytics وجميع مكيّفات النشر. "
                    "تُجيب على أي سؤال تنفيذي.",
            },
            {
                "name":  "Tommaso Adami",
                "role":  "Co-founder · Growth",
                "email": "tommaso@elevatekit.io",
                "tag":   "Onboarding · الأسعار · الشراكات",
                "bio":
                    "Ex growth lead في scale-up fintech أوروبية. "
                    "يتولّى onboarding وpricing strategy وخصومات "
                    "الشركات الناشئة في مرحلة pre-seed وشراكات المسرّعات.",
            },
        ],

        # Office meta-row labels
        "office_address_label":   "المكتب",
        "office_transport_label": "المواصلات",
        "office_model_label":     "النموذج",

        # Studio info
        "office_label":   "مكتب غير متزامن أولاً",
        "office_heading": "أين نحن (حتى لو ستجدنا على الإنترنت)",
        "office_intro":
            "المكتب الفعلي في Talent Garden Calabiana في ميلانو، "
            "لكن الفريق موزَّع (ميلانو، برلين، لشبونة، كراكوف). "
            "«غير متزامن أولاً» يعني أن الاجتماعات الداخلية مُختصَرة "
            "للحدّ الأدنى، وأن معظم القرارات تُتّخذ على Linear في pull request.",
        "office": {
            "address":     "Talent Garden Calabiana · Via Calabiana 6 · 20139 Milano",
            "transport":   "M3 Lodi · 8 دقائق مشياً · موقف داخلي متاح",
            "hours":       "غير متزامن أولاً · المؤسسون في المكتب الثلاثاء والخميس",
            "schedule": [
                ("Slack",          "الإثنين – الجمعة · 9:00 – 19:00 CET"),
                ("البريد",          "ردّ خلال ساعة في أوقات المكتب · خلال 24 ساعة خارج الأوقات"),
                ("عرض عند الطلب",  "الثلاثاء 17:00 CET · غير متزامن عبر Loom في أي وقت"),
                ("ساعات المكتب",   "الجمعة 11:00 CET · لخطّتَي Scale و Studio"),
            ],
        },

        "footnote":
            "Elevate فريق من ستة أشخاص — ثلاثة مؤسسين + ثلاثة "
            "مهندسين. سنردّ شخصياً على بريدك. إن لم تسمع منا خلال "
            "24 ساعة، فلم يضع طلبك: اكتب على Slack وسيُفعَّل لك "
            "تذكير. وعدٌ، لا يمرّ طلب دون استماع.",
    },
}
