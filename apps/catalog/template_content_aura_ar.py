"""Aura — Digital Studio · AR content registry.

Agency live rollout, Phase 2g3.6f, Session 49.

Voice contract (Wamda / Riyadh / Dubai startup-MSA register):
- Direct, product-oriented MSA. First/second person light.
- Startup / product lexicon: "سبرينت", "ديسكفري", "backlog",
  "onboarding", "retention", "dashboard", "funnel", "NPS".
- Stack names (Next.js, Figma, Stripe, Linear, PostHog, Segment,
  Mixpanel, GrowthBook, Datadog, Sentry, etc.) stay in Latin.
- Ship-log // comments stay Latin — they are code-style.
- Sprint chip "Sprint 07/Q2 · live" stays Latin — code indicator.
- Latin digits for all numerals (+18%, NPS +22, € 840K, 2.8M).
"""
from __future__ import annotations

from typing import Any


AURA_CONTENT_AR: dict[str, Any] = {

    "pages": [
        {"slug": "home",         "label": "الأستوديو",     "kind": "home"},
        {"slug": "studio",       "label": "من نحن",        "kind": "about"},
        {"slug": "capabilities", "label": "Capabilities",  "kind": "services"},
        {"slug": "lavori",       "label": "الأعمال",       "kind": "project_list"},
        {"slug": "sprint",       "label": "Sprint",        "kind": "process"},
        {"slug": "brief",        "label": "Brief",         "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Aura",
        "tag":         "أستوديو ديجيتال · product · growth",
        "sprint_chip": "Sprint 07/Q2 · live",
        "nav_cta":     "احجز call",
        "inquiry_page_slug": "brief",
        "phone":       "+39 02 8728 4411",
        "email":       "hello@aura.studio",
        "address":     "Via Paolo Sarpi 41 · 20154 Milano",
        "hours_compact":"Call slots · الاثنين — الخميس · 10 — 18",
        "license":     "P.IVA 12890440964 · Milano",
        "footer_intro":
            "أستوديو ديجيتال مستقل. نصمم المنتجات "
            "والمنصات وأنظمة النمو لـ scale-up "
            "وشركات التكنولوجيا. قاعدتنا في Milano، وتسليماتنا أوروبية.",
        "foot_shiplog_label":    "// ship log · last 6",
        "foot_current_sprint":   "sprint 07/Q2 · live",
        "foot_shiplog_rows": [
            ("أمس · 18:04",       "v2.14",  "Soldo — onboarding corporate جديد live"),
            ("أمس · 09:21",       "v2.13",  "Fastweb Plus — dashboard سكنية v2.3"),
            ("الاثنين · 15:30",   "v2.12",  "Lendlease — بوابة asset manager"),
            ("الجمعة · 11:12",    "v2.11",  "Casavo — retention A/B loop 003"),
            ("الخميس · 17:45",    "v2.10",  "Milkman — SDK ship tracking"),
            ("الأربعاء · 10:02",  "v2.09",  "Fiscozen — onboarding self-serve"),
        ],
        "foot_stack_marquee": [
            "Figma", "Linear", "Notion", "GitHub", "Vercel", "Stripe",
            "Segment", "PostHog", "Supabase", "Framer", "Mixpanel", "Sentry",
        ],
        "foot_studio_label":  "الأستوديو",
        "foot_stack_label":   "Stack تسليم",
        "foot_stack_rows": [
            "Design — Figma · Framer",
            "Dev — Next.js · TypeScript",
            "Data — PostHog · Segment",
            "Payments — Stripe · Checkout",
            "Infra — Vercel · Supabase",
        ],
        "foot_boot_line":
            "aura.studio · uptime 99.98 · last deploy 4 min ago · built in Milano",
    },

    # ── HOME ─────────────────────────────────────────────────────
    "home": {
        "chip": "3 فرص متاحة · Q3 2026",
        "headline": "من <em>call ديسكفري</em> إلى <em>أول KPI</em> في ستة أسابيع.",
        "intro":
            "نحن أستوديو ديجيتال يبني منتجات وأنظمة "
            "نمو لِـ scale-up إيطالية وأوروبية. "
            "سبرينت مدته أسبوعان، dashboard مشترك، "
            "تسليمات قابلة للقياس. بلا وكالة، كله منتج.",
        "primary_cta":   "احجز call",
        "primary_href":  "brief",
        "secondary_cta": "أعمال حديثة",
        "secondary_href":"lavori",

        "hero_metrics": [
            ("<em>47</em>",        "منتجاً شُحن منذ 2019"),
            ("<em>+34%</em>",      "تحويل وسطي بعد إعادة التصميم"),
            ("<em>6 أسابيع</em>",  "من sprint zero إلى أول KPI"),
        ],

        # Dashboard console tile
        "console": {
            "path":           "aura.studio/clients/casavo/live",
            "status_chip":    "LIVE · sprint 07/Q2",
            "primary_metric": "+34%",
            "primary_label":  "تحويل ما بعد إعادة التصميم · آخر 30 يوماً",
            "kpi": [
                ("<em>+18%</em>",    "Retention يوم 30"),
                ("<em>Δ 22</em>",    "NPS قبل / بعد · Casavo"),
                ("<em>€ 840K</em>",  "MRR · sprint 1 – 14"),
                ("<em>99.98%</em>",  "Uptime آخر ربع"),
            ],
            "meta_label":     "السبرينت الحالي",
            "meta_value":     "07/Q2 · week 2 of 2",
        },

        # Capabilities mini
        "capab_label":   "Capabilities",
        "capab_heading": "أربع <em>مجالات</em>، فريق واحد.",
        "capab_intro":
            "نعمل على أربعة أنواع من المشاريع — إطلاقات منتج، "
            "إعادة تصميم منصات، أنظمة نمو، وتسليم "
            "منصات B2B. يرافق كل مشروع فريق من 3-5 أشخاص "
            "مخصصين، لا account layer.",
        "capab_cards": [
            {
                "id":   "C.01",
                "title":"Product <em>launch</em>",
                "body": "من المفهوم إلى onboarding live. "
                        "مثالي لـ scale-up في Serie A ينتقلون "
                        "من MVP إلى منتج مدفوع.",
                "tags": ["Discovery", "Design system", "Next.js", "Analytics"],
            },
            {
                "id":   "C.02",
                "title":"Platform <em>redesign</em>",
                "body": "إعادة التفكير في منتجات ناضجة دون فقدان المستخدمين. "
                        "Research، A/B test، هجرة تدريجية.",
                "tags": ["UX audit", "A/B", "Incremental ship", "PostHog"],
            },
            {
                "id":   "C.03",
                "title":"Growth <em>systems</em>",
                "body": "Onboarding، retention، referral، تجارب pricing. "
                        "Quick wins خلال أول 30 يوماً، أنظمة على 90 يوماً.",
                "tags": ["Onboarding", "Retention", "Pricing", "Experiments"],
            },
            {
                "id":   "C.04",
                "title":"B2B <em>delivery</em>",
                "body": "بوابات asset manager، dashboards corporate، "
                        "backoffice داخلية. تكامل SSO + data warehouse.",
                "tags": ["Dashboards", "SSO", "Roles", "BigQuery"],
            },
        ],

        # Sprint strip
        "sprint_label":   "طريقتنا في التسليم",
        "sprint_heading": "أربعة <em>سبرينت</em>، من الـ discovery إلى الـ scale.",
        "sprint_intro":
            "كل مشروع مهيكل في سبرينت مدته أسبوعان. "
            "ترى بالضبط ما نفعله، متى سيُسلَّم، "
            "وأي مقاييس نحركها. لا مفاجآت آخر الشهر.",
        "sprints": [
            {
                "id":"S.00", "duration":"Sprint 0 · 1 أسبوع",
                "title":"<em>Signal</em>",
                "body": "Discovery مع stakeholders، المستخدمين، الـ dashboard. "
                        "التسليم: brief مشترك + backlog أولي.",
                "output": "OUT · brief + backlog",
            },
            {
                "id":"S.01", "duration":"Sprint 1 — 2 · 4 أسابيع",
                "title":"<em>Sketch</em>",
                "body": "Design system + prototypes قابلة للاختبار. "
                        "Research نوعي + أول A/B على الفرضيات الحرجة.",
                "output": "OUT · prototype + design tokens",
            },
            {
                "id":"S.02", "duration":"Sprint 3 — 5 · 6 أسابيع",
                "title":"<em>Ship</em>",
                "body": "تنفيذ staging → production. "
                        "متابعة live للمقاييس، rollback متاح بنقرة واحدة.",
                "output": "OUT · production + first KPI",
            },
            {
                "id":"S.03", "duration":"Sprint 6+ · ongoing",
                "title":"<em>Scale</em>",
                "body": "تجارب مستمرة، توسيع features، "
                        "تحسين post-launch. ship-log شريك مشترك.",
                "output": "OUT · weekly ship-log",
            },
        ],

        # Lavori cards
        "work_label":      "أعمال حديثة",
        "work_heading":    "سبعة <em>منتجات</em>، سبع <em>مقاييس</em>.",
        "work_intro":
            "لكل مشروع مقياس واضح، معلن في sprint zero "
            "ومقاس في sprint ثلاثة. إن لم يتحرك المقياس، نعمل "
            "مجاناً حتى يتحرك.",
        "work_page_slug": "lavori",
        "work_cards": [
            {
                "slug": "casavo-retention-rework",
                "id":   "W.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=900&q=80&auto=format&fit=crop",
                "title":"Retention rework في ثلاثة أشهر",
                "client":"Casavo · Proptech Milano",
                "metric_chip": "+18% retention · D30",
                "stack":["Next.js", "PostHog", "Figma"],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "W.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=80&auto=format&fit=crop",
                "title":"Dashboard سكنية v2",
                "client":"Fastweb · Telco Italia",
                "metric_chip": "NPS +22 · 6 أشهر",
                "stack":["React", "Django", "Segment"],
            },
            {
                "slug": "soldo-corporate-onboarding",
                "id":   "W.03",
                "cover":"https://images.unsplash.com/photo-1559028012-481c04fa702d?w=900&q=80&auto=format&fit=crop",
                "title":"Onboarding corporate self-serve",
                "client":"Soldo · Fintech pan-EU",
                "metric_chip": "-54% time to activate",
                "stack":["Next.js", "Stripe", "Mixpanel"],
            },
        ],

        "metric_strip": [
            ("<em>47</em>",      "منتجاً شُحن",          "منذ 2019 — وسطياً 8 / سنة"),
            ("<em>+34%</em>",    "تحويل وسطي",            "بين ما قبل وبعد إعادة التصميم"),
            ("<em>99.98%</em>",  "uptime",                "آخر ربع · status.aura.studio"),
            ("<em>6 أسابيع</em>","time to first KPI",     "من sprint zero إلى أول مقياس متحرك"),
        ],

        "cta_label":   "الـ call القادمة",
        "cta_heading": "ثلاث <em>فرص</em> مفتوحة لـ Q3 2026.",
        "cta_sub":
            "الفرصة الأولى هي call ديسكفري مدتها 30 دقيقة. إن كان "
            "المشروع يناسبنا، تصلك خلال الأيام الخمسة التالية "
            "brief قراءة + تقدير sprint zero.",
        "cta_chip":    "30 دقيقة · zero committment",
        "cta_primary": "احجز call",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "chip": "الفريق · 11 شخصاً · Milano + remote",
        "headline": "فريق من <em>أحد عشر</em>، <em>ثماني سنوات</em> من المنتجات المشحونة.",
        "standfirst":
            "Aura أستوديو لِـ product design وهندسة تأسس في "
            "Milano عام 2019. أحد عشر شخصاً — خمسة designers، أربعة "
            "engineers، اثنان product managers — موزعون بين Milano، Torino "
            "و remote. بلا account managers، بلا طبقات وسيطة: "
            "من يوقّع الـ brief هو من يشحنه.",

        "facts": [
            ("<em>11</em>",    "أشخاص",         "5 design · 4 eng · 2 PM"),
            ("<em>47</em>",    "منتجاً شُحن",    "منذ 2019 حتى اليوم"),
            ("<em>3</em>",     "مقرات",          "Milano · Torino · remote"),
            ("<em>94%</em>",   "عملاء يجددون",   "معدل retention 2024"),
        ],

        "story_label":   "حكاية الأستوديو",
        "story_heading": "كيف أجبرتنا <em>scale-up</em> على إعادة التفكير في design studio.",
        "story_paragraphs": [
            "يولد Aura عام 2019 على يد Luca Bianchi و Sofia Reggiani، "
            "product designers سابقون في Spotify و Figma. كانت الفكرة الأولى "
            "بسيطة: <em>لا نريد أن نكون وكالة، لا نريد أن نكون "
            "freelance</em>. أردنا أستوديو يعمل كفريق داخلي — "
            "بالأدوات نفسها، بالمقاييس نفسها، "
            "بالإيقاع نفسه — لكن من الخارج.",
            "كانت السنوات الثلاث الأولى سنوات تعلّم. فهمنا "
            "أن scale-up الإيطالية لم تكن بحاجة إلى <em>design</em> "
            "— كانت بحاجة إلى <em>delivery</em>. فوظّفنا "
            "engineers full-stack. فهمنا أن design "
            "review لا يكفي — نحتاج ship log. فهمنا أن القيمة "
            "ليست في الـ mockups، بل في المقاييس المتحركة.",
            "اليوم يعمل Aura مع 6-8 عملاء في العام، بسبرينت مدته "
            "أسبوعان، مع مقياس معلن في بداية كل "
            "مشروع. ينشر كل مشروع ship log داخلي يستطيع "
            "العميل قراءته في الوقت الفعلي. إن لم يتحرك المقياس، "
            "نعمل مجاناً حتى يتحرك. "
            "هي الطريقة الوحيدة التي نعرف العمل بها.",
        ],

        "team_label":   "الفريق",
        "team_heading": "من <em>يشحن</em> المشاريع.",
        "team_intro":
            "يرافق كل مشروع فريق مخصص من 3-5 أشخاص. "
            "تُشكَّل الفرق حسب نوع المشروع ولا "
            "تتغير في الطريق. من يبدأ المشروع، يشحنه.",
        "team": [
            {
                "name": "Luca Bianchi",
                "role": "شريك مؤسِّس · Head of product",
                "bio":  "سابقاً Spotify (Stoccolma · 2014-2018) و Figma "
                        "(San Francisco · 2018-2019). قاد "
                        "فريق growth design لسوق الاتحاد الأوروبي. "
                        "يتولى تعريف السبرينت.",
                "portrait": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Linear", "PostHog", "Notion"],
            },
            {
                "name": "Sofia Reggiani",
                "role": "شريكة مؤسِّسة · Head of engineering",
                "bio":  "سابقاً Spotify (Stoccolma) و Google (London). "
                        "قادت هجرة Next.js لمنصتين "
                        "pan-europee. تتولى stack التسليم.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "stack": ["Next.js", "TypeScript", "Vercel", "Supabase"],
            },
            {
                "name": "Matteo Leone",
                "role": "Principal product designer",
                "bio":  "ثماني سنوات في Satispay (Milano) قبل "
                        "الانضمام إلى Aura عام 2022. صمم ثلاثة "
                        "onboardings لِـ fintech إيطالية بأكثر من 1M مستخدم.",
                "portrait": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Framer", "Stripe Elements"],
            },
        ],

        "values_label":   "كيف نعمل",
        "values_heading": "<em>أربع قواعد</em> لا نساوم عليها.",
        "values": [
            ("V.01", "مقياس <em>معلن</em>",
             "لكل مشروع مقياس واضح محدد في sprint zero. "
             "إن لم يتحرك، نبقى حتى يتحرك."),
            ("V.02", "فريق <em>مخصص</em>",
             "من يبدأ المشروع، يشحنه. بلا account manager، "
             "بلا handoff. الـ designer الذي يصمم هو نفسه من يعمل ship."),
            ("V.03", "<em>ship-log</em> علني",
             "للعميل وصول في الوقت الفعلي إلى الـ ship-log الداخلي. "
             "يرى ما شحنّا، متى، لماذا، وما الذي فشل."),
            ("V.04", "<em>call</em> واحدة في الأسبوع",
             "اجتماع متزامن واحد في الأسبوع، مدته 30 دقيقة، "
             "بأجندة مكتوبة. الباقي async على Linear و Slack."),
        ],
    },

    # ── CAPABILITIES (services) ──────────────────────────────────
    "capabilities": {
        "chip": "4 مجالات · 3-5 أشخاص لكل مشروع",
        "headline": "أربع <em>capabilities</em>، كلها مقاسة.",
        "standfirst":
            "لكل capability منهج موثَّق، مقياس نموذجي، "
            "مدة متوقعة، وstack محدد سلفاً. ليست "
            "لائحة أسعار — بل نظام يسمح لنا أن نقول لك، في sprint zero، "
            "ما تتوقعه ومتى.",

        "capabilities": [
            {
                "id": "CAP.01 · Product launch",
                "title": "إيصال <em>منتج جديد</em> إلى أول تحويل.",
                "tagline": "نموذجي: 14 — 20 أسبوعاً · KPI · activation + first paid",
                "body":
                    "لـ scale-up التي تحققت من المشكلة (Serie Seed / A) "
                    "وتحتاج إلى بناء المنتج المدفوع. ننطلق من "
                    "sprint zero (research + backlog)، نمر عبر design "
                    "system + أول ثلاث flow حرجة، ونصل إلى production "
                    "مع onboarding قابل للقياس و pricing حي.",
                "scope_label": "// scope",
                "scope": [
                    "Sprint zero + user research",
                    "Design system (tokens + 60 components)",
                    "ثلاث flow حرجة في production",
                    "Onboarding self-serve",
                    "Pricing page live + Stripe",
                    "Analytics + funnel كامل",
                    "Rollback + feature flag",
                    "Handover docs للفريق الداخلي",
                ],
                "stack": ["Next.js 14", "TypeScript", "Figma", "Stripe", "Segment", "PostHog"],
            },
            {
                "id": "CAP.02 · Platform redesign",
                "title": "<em>إعادة تصميم</em> منتج ناضج دون فقدان المستخدمين.",
                "tagline": "نموذجي: 20 — 30 أسبوعاً · KPI · retention + NPS",
                "body":
                    "لمنصات بأكثر من 50k مستخدم نشط راكمت "
                    "دَيْن UX. ننطلق من audit كمي + نوعي، "
                    "نبني النظام الجديد بالتوازي، ونهاجر "
                    "تدريجياً عبر feature flag. لا big-bang launch.",
                "scope_label": "// scope",
                "scope": [
                    "UX audit + quant analysis",
                    "أكثر من 30 مقابلة مستخدم",
                    "هجرة تدريجية",
                    "A/B test على cohort",
                    "Design system evolution",
                    "Rollout لكل سوق",
                    "Post-launch tuning · 8 أسابيع",
                    "تدريب الفريق الداخلي",
                ],
                "stack": ["React", "Django", "PostHog", "Segment", "Split.io"],
            },
            {
                "id": "CAP.03 · Growth systems",
                "title": "<em>أنظمة نمو</em> قابلة للقياس في 30 يوماً.",
                "tagline": "نموذجي: 8 — 16 أسبوعاً · KPI · conversion + LTV",
                "body":
                    "لمنتجات في production تحتاج إلى النمو. "
                    "نعمل على onboarding، pricing، retention، referral. "
                    "Quick wins خلال أول 30 يوماً (عادة +12% على funnel). "
                    "أنظمة على 90 يوماً (تجارب جديدة مستمرة).",
                "scope_label": "// scope",
                "scope": [
                    "Audit funnel + benchmark",
                    "Experiment backlog",
                    "A/B test weekly cadence",
                    "Onboarding redesign",
                    "Pricing page A/B",
                    "Email activation series",
                    "Referral loop",
                    "Reporting dashboard",
                ],
                "stack": ["PostHog", "Segment", "Mixpanel", "Customer.io", "GrowthBook"],
            },
            {
                "id": "CAP.04 · B2B delivery",
                "title": "بوابات <em>asset manager</em> و dashboards corporate.",
                "tagline": "نموذجي: 24 — 36 أسبوعاً · KPI · task completion + time saved",
                "body":
                    "لشركات B2B (proptech، fintech، healthtech) تحتاج "
                    "إلى تسليم بوابات لعملائها enterprise. SSO، أدوار، "
                    "صلاحيات، data warehouse مدمج، exports مهيكلة. "
                    "ليست sexy، لكنها حيث يُلعب التجديد السنوي.",
                "scope_label": "// scope",
                "scope": [
                    "Discovery مع 3-5 enterprise",
                    "Design tokens corporate",
                    "SSO (SAML · Okta · Azure)",
                    "أدوار + صلاحيات granular",
                    "تكامل data warehouse",
                    "Export متعدد الصيغ",
                    "Audit log compliance",
                    "SLA 99.9% + monitoring",
                ],
                "stack": ["Next.js", "BigQuery", "Okta", "Datadog", "Sentry"],
            },
        ],

        "engagement_label":   "ثلاث طرق ارتباط",
        "engagement_heading": "من <em>المشروع المفرد</em> إلى <em>الشريك الدائم</em>.",
        "engagement_intro":
            "نختار نموذج الارتباط معاً، في sprint zero. "
            "عادة 70% من المشاريع تنطلق كـ fixed، و 30% كشراكة "
            "دائمة. نموذج الوقت والمواد نادر، "
            "نستخدمه فقط لِـ discovery أقل من 3 أسابيع.",
        "engagement_tiles": [
            {
                "id":    "E.01 · Discovery",
                "title": "<em>Discovery sprint</em>",
                "range": "2 — 3 أسابيع · fixed",
                "body":  "Sprint zero مخصص. Research، audit، backlog، "
                         "تقدير. إن تابعنا بعدها، يُحسَب ضمن المشروع.",
                "includes": [
                    "User research (5-8 مقابلات)",
                    "Audit كمي (analytics)",
                    "Backlog أولي",
                    "تقدير delivery",
                    "وثيقة مشتركة 30 صفحة",
                ],
            },
            {
                "id":    "E.02 · Fixed delivery",
                "title": "<em>Fixed delivery</em>",
                "range": "8 — 30 أسبوعاً · fixed",
                "body":  "إطلاق أو إعادة تصميم بـ scope وميزانية ثابتة. "
                         "الأكثر شيوعاً لـ scale-up في Serie A.",
                "includes": [
                    "فريق مخصص 3-5 أشخاص",
                    "Sprint من أسبوعين",
                    "Ship-log مشترك",
                    "مقياس معلن",
                    "Rollback + feature flags",
                    "Handover موثَّق",
                ],
                "featured": True,
            },
            {
                "id":    "E.03 · Partner mode",
                "title": "<em>Partner mode</em>",
                "range": "Q-by-Q · تجديد ربع سنوي",
                "body":  "ارتباط دائم لمنصات ناضجة. "
                         "نطاق أيام / ربع، roadmap مشتركة.",
                "includes": [
                    "Weekly ship cadence",
                    "مشاركة backlog العميل",
                    "Experiment مستمر",
                    "مراجعة KPI ربع سنوية",
                    "SLA دعم + on-call",
                ],
            },
        ],

        "cta_label":   "الخطوة التالية",
        "cta_heading": "لنلتق في <em>discovery</em>، 30 دقيقة.",
        "cta_primary": "احجز call",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "chip": "أرشيف المنتجات · 2019 — 2026",
        "headline": "<em>سبعة وأربعون</em> منتجاً شُحن. <em>سبعة</em> في الواجهة.",
        "standfirst":
            "لكل حالة مقياس معلن ومقاس. "
            "نعرض سبعة مشاريع علنية — الأربعون الأخرى "
            "تحت NDA (شائع في fintech و B2B). الأرشيف الكامل عند الطلب.",
        "tabs": ["الكل", "Product launch", "Redesign", "Growth", "B2B delivery"],
        "tabs_count_label": "// totali archivio",
        "tabs_count_value": "047",

        "projects": [
            {
                "slug": "casavo-retention-rework",
                "id":   "P.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=1200&q=80&auto=format&fit=crop",
                "title":"Retention rework · منصة شراء المنازل",
                "client":"Casavo",
                "discipline":"PROPTECH · REDESIGN",
                "year": "2025",
                "blurb":
                    "إعادة التفكير في كامل الـ funnel من البحث إلى التوقيع. "
                    "هجرة تدريجية عبر feature flag على 180k مستخدم. "
                    "بلا downtime، +18% retention خلال 30 يوماً.",
                "kpi": [
                    ("<em>+18%</em>",  "retention D30"),
                    ("<em>Δ+22</em>",  "NPS"),
                    ("<em>180K</em>",  "مستخدم مُهاجَر"),
                ],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "P.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80&auto=format&fit=crop",
                "title":"Dashboard سكنية v2.3",
                "client":"Fastweb",
                "discipline":"TELCO · PLATFORM",
                "year": "2024",
                "blurb":
                    "Dashboard جديدة لـ 2.8M عميل سكني. "
                    "SSO مدمج، إدارة خدمات، self-care متكامل. "
                    "خفض اتصالات call center −34% في ستة أشهر.",
                "kpi": [
                    ("<em>−34%</em>",   "اتصالات CC"),
                    ("<em>2.8M</em>",   "مستخدم"),
                    ("<em>NPS 64</em>", "post-launch"),
                ],
            },
            {
                "slug": "soldo-corporate-onboarding",
                "id":   "P.03",
                "cover":"https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1200&q=80&auto=format&fit=crop",
                "title":"Onboarding corporate self-serve",
                "client":"Soldo",
                "discipline":"FINTECH · LAUNCH",
                "year": "2025",
                "blurb":
                    "من onboarding بمساعدة (4 أيام وسطياً) إلى self-serve "
                    "(42 دقيقة). Compliance pan-EU، KYC مدمج، "
                    "multi-currency من اليوم صفر.",
                "kpi": [
                    ("<em>−54%</em>",      "TTFV"),
                    ("<em>+41%</em>",      "activation"),
                    ("<em>7 أسواق</em>",   "day one"),
                ],
            },
            {
                "slug": "milkman-ship-sdk",
                "id":   "P.04",
                "cover":"https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1200&q=80&auto=format&fit=crop",
                "title":"SDK ship tracking لتجار التجزئة",
                "client":"Milkman",
                "discipline":"LOGISTICS · B2B",
                "year": "2024",
                "blurb":
                    "SDK بـ JavaScript لتتبع التسليمات مدمج في "
                    "checkout أكثر من 40 retailer. استدعاء API واحد، "
                    "branding على جانب retailer، تحديثات real-time.",
                "kpi": [
                    ("<em>40+</em>",         "retailer"),
                    ("<em>1 استدعاء</em>",    "API"),
                    ("<em>2MB</em>",         "bundle"),
                ],
            },
            {
                "slug": "lendlease-asset-portal",
                "id":   "P.05",
                "cover":"https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
                "title":"بوابة asset manager enterprise",
                "client":"Lendlease",
                "discipline":"PROPTECH · B2B",
                "year": "2024",
                "blurb":
                    "بوابة لـ 80 asset manager إيطالي. SSO Azure، "
                    "أدوار granular، data warehouse مدمج مع "
                    "exports متعددة الصيغ. Compliance MiFID II مشمول.",
                "kpi": [
                    ("<em>80</em>",       "asset mgr"),
                    ("<em>Azure SSO</em>","deploy"),
                    ("<em>MiFID II</em>", "compliance"),
                ],
            },
            {
                "slug": "fiscozen-onboarding-self-serve",
                "id":   "P.06",
                "cover":"https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1200&q=80&auto=format&fit=crop",
                "title":"Onboarding self-serve للـ partite IVA",
                "client":"Fiscozen",
                "discipline":"FISCTECH · GROWTH",
                "year": "2024",
                "blurb":
                    "من onboarding بمساعدة محاسب إلى self-serve "
                    "كامل. خفض زمن activation و +47% "
                    "تحويل من trial إلى paid خلال أول 90 يوماً.",
                "kpi": [
                    ("<em>+47%</em>",    "trial → paid"),
                    ("<em>18 د.</em>",   "TTFV"),
                    ("<em>90 يوماً</em>", "قياس"),
                ],
            },
        ],

        "velocity_label":   "Velocity وسطي",
        "velocity_heading": "كيف <em>نشحن</em> · آخر اثني عشر شهراً.",
        "velocity_body":
            "الأرقام أدناه هي التي ننظر إليها داخلياً. "
            "مُحدَّثة شهرياً. إن كنت مهتماً بالمنهجية وراءها، "
            "نتحدث عنها برغبة في call ديسكفري.",
        "velocity_stats": [
            ("<em>8</em>",          "منتجاً شُحن · 2025"),
            ("<em>94%</em>",        "مشاريع on-time"),
            ("<em>+26%</em>",       "KPI وسطي متحرك"),
            ("<em>47 يوماً</em>",   "median time-to-ship"),
        ],
    },

    # ── SPRINT (process) ─────────────────────────────────────────
    "sprint": {
        "chip": "منهجية · 4 مراحل · telemetria live",
        "headline": "أربعة <em>سبرينت</em>، من الـ discovery إلى الـ scale.",
        "standfirst":
            "يعبر كل مشروع بأربع مراحل معلنة. "
            "مدد متوقعة، تسليمات واضحة، مقاييس علنية. "
            "يرى العميل في الوقت الفعلي أين نحن — ولماذا.",

        "sprints": [
            {
                "id": "Sprint 0 · Signal",
                "duration": "1 أسبوع · ثابت",
                "title": "<em>فهم</em> المشكلة، قبل تصميمها.",
                "tagline": "// output: brief مشترك + backlog أولي",
                "body":
                    "Sprint zero هو المرحلة الأهم والأكثر تقليلاً من شأنها. "
                    "في خمسة أيام نصغي إلى stakeholders (CEO، المنتج، "
                    "customer success)، نقابل 5-8 مستخدمين حقيقيين، نقرأ "
                    "الـ dashboard الحالية. في النهاية نقدم brief قراءة "
                    "+ backlog بالفرضيات للاختبار.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Brief مشترك · 24 صفحة",
                    "Backlog أولي · Linear",
                    "Stakeholder map",
                    "Research summary · 5-8 مقابلات",
                    "مقياس معلن + baseline",
                    "تقدير delivery (sprint count)",
                ],
            },
            {
                "id": "Sprint 1 — 2 · Sketch",
                "duration": "4 أسابيع",
                "title": "<em>نموذج أولي</em> قبل البناء.",
                "tagline": "// output: prototype قابل للاختبار + design system v0.1",
                "body":
                    "أول سبرينتَين هما prototyping سريع. "
                    "نبني في Figma + Framer أكثر ثلاث flow حرجية، "
                    "نختبرها مع مستخدمين حقيقيين، نكرر. بالتوازي "
                    "نطلق design system (tokens + 20 component أساسي). "
                    "الكود الفعلي يصل في sprint 3.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Figma prototype تفاعلي",
                    "3 جولات user testing",
                    "Design system v0.1",
                    "Code architecture",
                    "خطة A/B test",
                    "Design review للعميل",
                ],
            },
            {
                "id": "Sprint 3 — 5 · Ship",
                "duration": "6 أسابيع",
                "title": "<em>إيصال إلى production</em>، تدريجياً.",
                "tagline": "// output: production live + أول مقياس",
                "body":
                    "تنفيذ و delivery تدريجي. كل جمعة نعمل ship "
                    "لشيء في staging، وكل نهاية سبرينت في production. "
                    "Feature flag + rollback بنقرة واحدة. في نهاية sprint 5 "
                    "يجب أن يكون أول مقياس معلن قد تحرك.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Staging deploy أسبوعي",
                    "Production deploy نصف أسبوعي",
                    "Feature flags كلها نشطة",
                    "Rollback plan موثَّق",
                    "Monitoring · Datadog / Sentry",
                    "أول مقياس متحرك",
                ],
            },
            {
                "id": "Sprint 6+ · Scale",
                "duration": "ongoing · ربع سنوي",
                "title": "<em>Scale</em> · تجارب مستمرة.",
                "tagline": "// output: ship-log أسبوعي + مراجعة KPI ربع سنوية",
                "body":
                    "Post-launch ندخل في وضع scale. تجارب "
                    "أسبوعية، توسيع features، تحسين post-launch. "
                    "Ship-log مشترك علني. مراجعة ربع سنوية "
                    "للمقاييس مقابل الخطة.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Ship-log علني",
                    "A/B weekly",
                    "Feature roadmap 6 أشهر",
                    "مراجعة KPI ربع سنوية",
                    "تدريب الفريق الداخلي",
                    "Handover مستمر",
                ],
            },
        ],

        "mindset_label":   "كيف <em>نفكر</em> في المسار",
        "mindset_heading": "ثلاثة <em>مبادئ</em> delivery.",
        "mindset_cards": [
            {
                "id": "P.01",
                "title": "<em>Telemetria</em> ظاهرة",
                "body": "Ship-log علني للعميل من اليوم صفر. "
                        "ماذا شحنّا، متى، لماذا. بلا غرف مظلمة.",
            },
            {
                "id": "P.02",
                "title": "<em>Rollback</em> بنقرة واحدة",
                "body": "كل feature خلف flag. إن لم يعمل شيء "
                        "في production، نعطّله في أقل من 60 ثانية.",
            },
            {
                "id": "P.03",
                "title": "<em>Skin in the game</em>",
                "body": "إن لم يتحرك المقياس المعلن، نواصل "
                        "العمل مجاناً. فعلنا ذلك أربع مرات في ثماني سنوات.",
            },
        ],

        "stack_label":   "Stack تسليم",
        "stack_heading": "بماذا <em>نسلم</em>.",
        "stack_intro":
            "الـ stack مختار ليكون موثوقاً، سريعاً، وسهل "
            "التسليم للفريق الداخلي للعميل. بلا تكنولوجيا boutique.",
        "stack_tiles": [
            {"category": "// frontend",  "list": "<strong>Next.js 14</strong> · <span>TypeScript</span> · <strong>React</strong> · <span>Framer Motion</span>"},
            {"category": "// backend",   "list": "<strong>Node</strong> · <span>Django</span> · <strong>Supabase</strong> · <span>PostgreSQL</span>"},
            {"category": "// design",    "list": "<strong>Figma</strong> · <span>Framer</span> · <strong>Design tokens</strong> · <span>Maze</span>"},
            {"category": "// analytics", "list": "<strong>PostHog</strong> · <span>Segment</span> · <strong>Mixpanel</strong> · <span>GrowthBook</span>"},
            {"category": "// payments",  "list": "<strong>Stripe</strong> · <span>Checkout</span> · <strong>Elements</strong> · <span>Billing</span>"},
            {"category": "// infra",     "list": "<strong>Vercel</strong> · <span>Supabase</span> · <strong>Datadog</strong> · <span>Sentry</span>"},
            {"category": "// auth",      "list": "<strong>Auth0</strong> · <span>Okta SSO</span> · <strong>Azure AD</strong> · <span>Clerk</span>"},
            {"category": "// workflow",  "list": "<strong>Linear</strong> · <span>Notion</span> · <strong>Slack</strong> · <span>Loom</span>"},
        ],
    },

    # ── BRIEF (contact) ──────────────────────────────────────────
    "brief": {
        "chip": "3 فرص مفتوحة · Q3 2026",
        "headline": "احكِ لنا عن <em>المشروع</em>. نتصل بك خلال أقل من 48 ساعة.",
        "standfirst":
            "هذا ليس form. إنه brief مهيكل في 3 خطوات. "
            "كل رد تستقبله مكتوب شخصياً من Luca أو "
            "Sofia، لا من account manager. إن كان المشروع يناسبنا، "
            "الرسالة الثانية هي اقتراح call.",

        "form_heading": "// brief intake · 3 step",

        "step1": {
            "id": "STEP 01", "title": "من أنت", "sub": "فقط الحقول الضرورية.",
        },
        "step2": {
            "id": "STEP 02", "title": "المشروع", "sub": "كلما كان ملموساً أكثر، كان الرد أنفع.",
        },
        "step3": {
            "id": "STEP 03", "title": "متى", "sub": "اختر فرصة إرشادية — نؤكد لاحقاً عبر البريد.",
        },

        "labels": {
            "name":    "الاسم واللقب",
            "role":    "الدور",
            "company": "الشركة / المنتج",
            "email":   "بريد العمل",
            "scope":   "نوع المشروع",
            "brief":   "سرد موجز",
            "slot":    "الفرصة المفضلة",
        },
        "placeholders": {
            "name":    "الاسم اللقب",
            "role":    "مثال: Head of Product",
            "company": "اسم الشركة",
            "email":   "name@company.com",
            "brief":   "ماذا تبني، إلى أي نقطة وصلت (MRR، مستخدمون، round)، ما المشكلة التي تشعر بها، كيف تقيس النجاح. Brief ملموس يستقبل رداً ملموساً.",
        },
        "scope_options": [
            "Product launch · أول مرة live",
            "Platform redesign · منتج ناضج",
            "Growth systems · funnel / retention",
            "B2B delivery · بوابة / dashboard",
            "Discovery sprint · 2-3 أسابيع",
            "لست متأكداً بعد — لنتحدث",
        ],

        "slots": [
            ("mon10", "الاثنين · 10:00"),
            ("mon15", "الاثنين · 15:00"),
            ("tue10", "الثلاثاء · 10:00"),
            ("tue15", "الثلاثاء · 15:00"),
            ("wed10", "الأربعاء · 10:00"),
            ("wed15", "الأربعاء · 15:00"),
            ("thu10", "الخميس · 10:00"),
            ("thu15", "الخميس · 15:00"),
            ("async", "فقط async عبر البريد"),
        ],
        "form_submit_label": "احجز الـ call",
        "form_submit_note":  "// رد خلال 48 ساعة عمل · كل فوارق EU الزمنية",

        "async_label":   "تفضل async؟",
        "async_heading": "اكتب إلى <em>Luca</em> و <em>Sofia</em>.",
        "async_body":
            "كل بريد يصل مباشرة إلى الشريكَين المؤسِّسَين. "
            "يردان شخصياً — لا account manager، لا bot.",

        "studio_label":  "الأستوديو",

        "response_label": "// SLA استجابة",
        "response_rows": [
            ("Brief",          "< 48 ساعة"),
            ("Proposta",       "5 أيام"),
            ("Sprint zero",    "2 أسابيع"),
            ("أول مقياس",      "6 أسابيع"),
        ],

        "boot_left":  "aura.studio · hello@aura.studio · +39 02 8728 4411",
        "boot_right": "// sempre aperti al brief",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "casavo-retention-rework",
            "id":   "P.01 · PROPTECH",
            "title": "Casavo · <em>+18% retention</em> في ثلاثة أشهر.",
            "client": "Casavo · Proptech Milano",
            "discipline": "Redesign · retention",
            "duration": "14 أسبوعاً",
            "year": "2025",
            "standfirst":
                "إعادة العمل على funnel ما بعد الحجز لدى Casavo. "
                "تحسين تدريجي على 180k مستخدم، "
                "feature flag في كل مكان، بلا downtime. بعد ثلاثة أشهر: "
                "+18% retention خلال 30 يوماً، NPS +22، MRR +€ 840K.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "المستخدمون يعودون، لكن لا يحوّلون.",
            "problem_paragraphs": [
                "ضاعفت Casavo المستخدمين النشطين بين 2023 و 2024، "
                "لكن تحويل <em>الزيارة 1</em> إلى <em>حجز زيارة فعلية</em> "
                "انخفض بـ 12% — على 180k مستخدم نشط، هذا يعني ~21k "
                "حجز مفقود كل شهر.",
                "كان الفريق الداخلي قد فهم أن المشكلة في funnel "
                "ما بعد التسجيل، لكن لم تكن لديه capacity لاختبار أكثر من 10 فرضيات "
                "بشكل جدي دون إبطاء الـ roadmap الرئيسي.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Funnel ثانٍ، بالتوازي مع القديم.",
            "solution_paragraphs": [
                "بدل إعادة كتابة الـ funnel الرئيسي (مخاطرة مرتفعة جداً على "
                "180k مستخدم) بنينا <em>funnel تجريبي ثانٍ</em> "
                "خلف feature flag، متاح لـ 10% من الـ traffic. ستة أسابيع "
                "من الاختبار، سبع iterations، أربع flow مختبرة.",
                "في الـ iteration السادسة تغلّب الـ funnel الثاني على الأول بـ 18% "
                "على retention D30. هاجرنا تدريجياً باقي "
                "الـ 180k مستخدم خلال ثلاثة أسابيع — مرحلة 25%، ثم 50%، ثم 100%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "أربعة عشر أسبوعاً، <em>سبعة سبرينت</em>.",
            "timeline_intro":
                "الجدول أدناه هو التسلسل الفعلي للـ delivery — مستخرج "
                "من ship-log المشترك مع Casavo.",
            "timeline_steps": [
                {"id": "S.00", "duration": "أسبوع 1",       "title": "<em>Signal</em>",  "body": "Research + audit funnel + backlog بـ 14 فرضية."},
                {"id": "S.01", "duration": "أسبوع 2-3",     "title": "<em>Sketch</em>",  "body": "Prototypes لـ 4 flow بديلة، 8 مقابلات."},
                {"id": "S.02", "duration": "أسبوع 4-6",     "title": "<em>Ship</em>",    "body": "Funnel ثانٍ live بـ 10%، أول A/B test."},
                {"id": "S.03", "duration": "أسبوع 7-11",    "title": "<em>Iterate</em>", "body": "6 iterations أسبوعية. Cohort كل جمعة."},
                {"id": "S.04", "duration": "أسبوع 12-14",   "title": "<em>Migrate</em>", "body": "Rollout لـ 25% → 50% → 100%. بلا downtime."},
            ],

            "results_label": "// results",
            "results_heading": "أربعة <em>مقاييس متحركة</em>.",
            "results_stats": [
                ("<em>+18%</em>",     "retention D30",              "من 42% إلى 49.6% (90 يوماً rolling)"),
                ("<em>Δ +22</em>",    "NPS",                         "من 31 إلى 53 خلال 3 أشهر post-rollout"),
                ("<em>+€ 840K</em>",  "MRR تزايدي",                   "إسقاط لـ 12 شهراً"),
                ("<em>0</em>",        "downtime أثناء الـ rollout", "180k مستخدم، بلا أخطاء 5xx إضافية"),
            ],

            "quote": "في ثلاثة أشهر فهموا منتجنا أفضل من استشاريين عملوا معنا سنة كاملة. وشحنوا.",
            "quote_author": "Marianna Colombo",
            "quote_role":   "VP Product · Casavo",

            "next_label":   "// next case",
            "next_heading": "→ شاهد كل <em>الأعمال</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ احجز <em>call</em>",
        },
        {
            "slug": "fastweb-plus-dashboard",
            "id":   "P.02 · TELCO",
            "title": "Fastweb · <em>−34% اتصالات CC</em> في 6 أشهر.",
            "client": "Fastweb · Telco Italia",
            "discipline": "Platform redesign",
            "duration": "26 أسبوعاً",
            "year": "2024",
            "standfirst":
                "Dashboard سكنية جديدة لـ 2.8M عميل. "
                "إدارة خدمات، مدفوعات، auto-care، SSO. "
                "النتيجة: −34% اتصالات بالـ call center، NPS 64 post-launch، "
                "هجرة كاملة في ستة أشهر بلا downtime.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Dashboard من 2014 في عالم 2024.",
            "problem_paragraphs": [
                "بُنيت dashboard Fastweb السكنية عام 2014 "
                "وأُعيد تلبيسها ثلاث مرات دون لمس الهيكلية. النتيجة: "
                "task completion عند 41%، 2.1M اتصال بالـ call center سنوياً لعمليات "
                "كان ينبغي أن تكون self-care.",
                "الهدف: إعادة البناء دون فقدان مستخدمين، بلا downtime، "
                "وبلا big-bang launch — أُتيحت لنا 26 أسبوعاً.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Micro-frontend + هجرة تدريجية.",
            "solution_paragraphs": [
                "بنينا الـ dashboard الجديدة كـ <em>micro-frontend</em> "
                "جنب القديمة — domain واحد، SSO نفسه، backend نفسه. "
                "هُوجر المستخدمون حسب cluster جغرافي (Lombardia، "
                "Piemonte، Lazio...) على ست مراحل.",
                "كل cluster يُراقَب أسبوعَين. إن كانت NPS و task "
                "completion أفضل من القديمة، ننتقل إلى الـ cluster التالي. "
                "إن كانت أسوأ، نتراجع 24 ساعة ونصلح.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>ست مراحل</em> من rollout جغرافي.",
            "timeline_intro":
                "كل مرحلة rollout أُتيحت لها أسبوعان مراقبة قبل "
                "المرحلة التالية. الأصعب كانت الثالثة.",
            "timeline_steps": [
                {"id": "R.01", "duration": "أسبوع 10", "title": "Piemonte",    "body": "400k مستخدم. NPS +18. Go."},
                {"id": "R.02", "duration": "أسبوع 14", "title": "Lombardia",   "body": "680k مستخدم. NPS +22. Go."},
                {"id": "R.03", "duration": "أسبوع 18", "title": "Veneto",      "body": "480k مستخدم. NPS +9. Hold أسبوع."},
                {"id": "R.04", "duration": "أسبوع 22", "title": "Lazio",       "body": "520k مستخدم. NPS +21. Go."},
                {"id": "R.05", "duration": "أسبوع 26", "title": "باقي إيطاليا", "body": "720k مستخدم. NPS +19. Complete."},
            ],

            "results_label": "// results",
            "results_heading": "ستة أشهر، <em>أربعة أرقام</em>.",
            "results_stats": [
                ("<em>−34%</em>",      "اتصالات call center",   "~720k اتصال أقل / سنة"),
                ("<em>NPS 64</em>",    "post-launch",            "مقابل 32 pre-launch"),
                ("<em>2.8M</em>",      "مستخدم مُهاجَر",          "100% بلا downtime"),
                ("<em>+41% TC</em>",   "task completion",         "من 41% إلى 82%"),
            ],

            "quote": "Aura الأستوديو الوحيد الذي قدم لي خطة rollback لكل sprint. استخدمنا الـ rollback مرتين. بلا drama.",
            "quote_author": "Stefano Petri",
            "quote_role":   "Head of digital · Fastweb",

            "next_label":   "// next case",
            "next_heading": "→ شاهد كل <em>الأعمال</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ احجز <em>call</em>",
        },
        {
            "slug": "soldo-corporate-onboarding",
            "id":   "P.03 · FINTECH",
            "title": "Soldo · onboarding من <em>4 أيام</em> إلى <em>42 دقيقة</em>.",
            "client": "Soldo · Fintech pan-EU",
            "discipline": "Product launch · onboarding",
            "duration": "18 أسبوعاً",
            "year": "2025",
            "standfirst":
                "إعادة تصميم كاملة للـ onboarding corporate في Soldo. "
                "من مسار بمساعدة (4 أيام) إلى self-serve كامل "
                "(42 دقيقة) في 7 أسواق أوروبية، مع KYC، multi-currency "
                "و compliance. النتيجة: +41% activation، −54% time to value.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Onboarding يتطلب إنساناً.",
            "problem_paragraphs": [
                "كان onboarding Soldo في 2024 يتطلب 4 أيام وسطياً "
                "(2 لـ KYC، 1 لـ setup multi-currency، 1 لـ activation "
                "البطاقات). كل onboarding يستهلك 1.2 ساعة من customer success. "
                "على 2.800 onboarding/شهر، الكلفة لا تحتمل.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Onboarding موجَّه، بلا إنسان.",
            "solution_paragraphs": [
                "أعدنا تصميم كامل الـ flow كـ <em>self-serve guided</em>: "
                "يرفع العميل الوثائق مرة واحدة فقط، يجري الـ KYC في الخلفية، "
                "إعداد multi-currency مملوء سلفاً حسب سوق الإقامة.",
                "إنسان فقط عند طلب صريح (link في كل step). "
                "CSAT لم ينخفض — ارتفع بـ 22%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "تسعة <em>سبرينت</em>، سبعة أسواق.",
            "timeline_intro":
                "أول 4 سبرينت على UK (السوق الأكثر نضجاً). "
                "الخمسة الأخرى على rollout cross-market.",
            "timeline_steps": [
                {"id": "S.01", "duration": "أسبوع 1-2",  "title": "<em>Discovery</em>",        "body": "120 customer success call مُحلَّلة."},
                {"id": "S.02", "duration": "أسبوع 3-6",  "title": "<em>UK beta</em>",          "body": "Flow جديد live على UK. +28% activation."},
                {"id": "S.03", "duration": "أسبوع 7-10", "title": "<em>DE · NL · FR</em>",     "body": "3 أسواق مضافة. Fix multi-currency."},
                {"id": "S.04", "duration": "أسبوع 11-14","title": "<em>IT · ES · IE</em>",     "body": "3 أسواق مضافة. Fix لغة."},
                {"id": "S.05", "duration": "أسبوع 15-18","title": "<em>Scale</em>",            "body": "تحسين مستمر. A/B weekly."},
            ],

            "results_label": "// results",
            "results_heading": "ثلاثة <em>مقاييس core</em> متحركة.",
            "results_stats": [
                ("<em>42 د.</em>",       "time to activate",   "من 4 أيام وسطياً"),
                ("<em>+41%</em>",        "activation rate",     "trial → paid"),
                ("<em>+22%</em>",        "CSAT",                "post-onboarding"),
                ("<em>7</em>",           "أسواق",               "day one go-live"),
            ],

            "quote": "النتيجة أن فريق onboarding corporate اليوم أصغر بـ 60% لكنه يدير 3x الشركات. لم تكن Soldo لتصل إلى مستواها الحالي دون هذا الـ rework.",
            "quote_author": "Rebecca Hughes",
            "quote_role":   "VP Growth · Soldo",

            "next_label":   "// next case",
            "next_heading": "→ شاهد كل <em>الأعمال</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ احجز <em>call</em>",
        },
        {
            "slug": "milkman-ship-sdk",
            "id":   "P.04 · LOGISTICS",
            "title": "Milkman · <em>SDK tracking</em> لأكثر من 40 retailer.",
            "client": "Milkman · Logistics Italia",
            "discipline": "B2B delivery · SDK",
            "duration": "22 أسبوعاً",
            "year": "2024",
            "standfirst":
                "SDK بـ JavaScript white-label لتتبع التسليمات، "
                "مدمج في checkout أكثر من 40 retailer إيطالي. "
                "استدعاء API واحد، branding على جانب retailer، "
                "تحديثات real-time. Bundle تحت الـ 2MB gzipped.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "40 retailer، 40 تكامل custom.",
            "problem_paragraphs": [
                "كانت Milkman تدير تسليمات أكثر من 40 retailer إيطالي — "
                "Esselunga، Coop، Unieuro، Mediaworld — لكل منها "
                "تكامل custom خاص به. كل retailer جديد يتطلب 8-12 "
                "أسبوعاً من engineering.",
            ],

            "solution_label": "// solution",
            "solution_heading": "SDK واحد، استدعاء API واحد.",
            "solution_paragraphs": [
                "بنينا SDK بـ JavaScript white-label. "
                "على الـ retailer أن يفعل شيئاً واحداً: استدعاء <em>milkman.track(orderId)</em>. "
                "يدير الـ SDK الـ branding على جانب retailer (ألوان، محارف، شعار)، "
                "اللغات، التحديثات real-time عبر WebSocket.",
                "متوسط التكامل: 3 ساعات. من قبل: 8-12 أسبوعاً.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>خمسة</em> سبرينت من الـ SDK إلى الـ retailer الـ 40.",
            "timeline_intro": "أول retailer (Esselunga) في sprint 3. الـ 39 الأخرى self-serve.",
            "timeline_steps": [
                {"id": "S.01", "duration": "أسبوع 1-4",   "title": "<em>SDK core</em>",         "body": "Architecture، bundle، branding."},
                {"id": "S.02", "duration": "أسبوع 5-10",  "title": "<em>Esselunga beta</em>",   "body": "أول retailer live. 2 bug حرج."},
                {"id": "S.03", "duration": "أسبوع 11-14", "title": "<em>Unieuro · Coop</em>",   "body": "2 retailer مضافَين. بلا bug."},
                {"id": "S.04", "duration": "أسبوع 15-18", "title": "<em>Docs + portal</em>",    "body": "Self-serve onboarding."},
                {"id": "S.05", "duration": "أسبوع 19-22", "title": "<em>Scale</em>",            "body": "Retailer الـ 40 مُدمَج self-serve."},
            ],

            "results_label": "// results",
            "results_heading": "من <em>8 أسابيع</em> إلى <em>3 ساعات</em>.",
            "results_stats": [
                ("<em>40+</em>",        "retailer live",          "عند go-live الشهر السادس"),
                ("<em>3 ساعات</em>",    "time-to-integrate",      "من 8-12 أسبوعاً وسطياً"),
                ("<em>1.8 MB</em>",     "bundle gzipped",         "تحت سقف 2 MB المطلوب"),
                ("<em>0</em>",          "downtime",               "من أول sprint حتى اليوم"),
            ],

            "quote": "أتاح لنا الـ SDK فتح ثلاثة أسواق أوروبية في ستة أشهر. من قبل كان مستحيلاً.",
            "quote_author": "Antonio Perini",
            "quote_role":   "CEO · Milkman",

            "next_label":   "// next case",
            "next_heading": "→ شاهد كل <em>الأعمال</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ احجز <em>call</em>",
        },
        {
            "slug": "lendlease-asset-portal",
            "id":   "P.05 · PROPTECH",
            "title": "Lendlease · <em>بوابة enterprise</em> لـ 80 asset manager.",
            "client": "Lendlease · Proptech EU",
            "discipline": "B2B delivery",
            "duration": "30 أسبوعاً",
            "year": "2024",
            "standfirst":
                "بوابة enterprise لـ 80 asset manager إيطالي. "
                "SSO Azure، أدوار granular، data warehouse مدمج، "
                "compliance MiFID II. ليست sexy — إنها حيث يُلعب التجديد.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1600&q=80&auto=format&fit=crop",

            "problem_label":"// problem",
            "problem_heading":"بوابة enterprise بلا self-serve.",
            "problem_paragraphs":[
                "كان 80 asset manager يستخدمون بوابة من 2016 تتطلب "
                "مساعدة إنسانية لكل عملية. كل asset manager يستهلك "
                "~6 ساعات / أسبوع من customer success. Re-contracting ربع سنوي "
                "في خطر.",
            ],
            "solution_label":"// solution",
            "solution_heading":"Dashboard self-serve + export تلقائي.",
            "solution_paragraphs":[
                "أعدنا بناء البوابة كمنصة self-serve. "
                "SSO Azure، أدوار granular (analista، manager، compliance)، "
                "data warehouse مدمج مع export متعدد الصيغ "
                "(PDF، XLSX، CSV، MiFID II XML).",
            ],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>عشرة</em> سبرينت، <em>ثلاثة</em> rollout cluster.",
            "timeline_intro": "Rollout حسب cluster من asset manager (20/30/30).",
            "timeline_steps":[
                {"id":"S.01","duration":"أسبوع 1-4","title":"<em>Discovery</em>","body":"مقابلات مع 12 asset manager."},
                {"id":"S.02","duration":"أسبوع 5-14","title":"<em>SSO + أدوار</em>","body":"Azure SSO + RBAC كامل."},
                {"id":"S.03","duration":"أسبوع 15-22","title":"<em>Dashboard</em>","body":"Dashboard core + analytics."},
                {"id":"S.04","duration":"أسبوع 23-28","title":"<em>Export</em>","body":"متعدد الصيغ + MiFID II."},
                {"id":"S.05","duration":"أسبوع 29-30","title":"<em>Rollout</em>","body":"80 asset manager مُهاجَر."},
            ],
            "results_label":"// results",
            "results_heading":"<em>80</em> asset manager، <em>صفر</em> اتصال.",
            "results_stats":[
                ("<em>80</em>","asset manager مُهاجَر","100% قبل نهاية rollout"),
                ("<em>−92%</em>","اتصالات CS","6 ساعات → 28 دقيقة /أسبوع"),
                ("<em>100%</em>","ricontracting","لسنتين متتاليتين"),
                ("<em>MiFID II</em>","compliance","Audit مُجتاز من أول جولة"),
            ],
            "quote":"البوابة أصبحت السبب الرئيسي لتجديد asset managers لدينا.",
            "quote_author":"Valentina Greco",
            "quote_role":"Head of product · Lendlease IT",
            "next_label":"// next case",
            "next_heading":"→ شاهد كل <em>الأعمال</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ احجز <em>call</em>",
        },
        {
            "slug": "fiscozen-onboarding-self-serve",
            "id":   "P.06 · FISCTECH",
            "title": "Fiscozen · <em>+47%</em> من trial إلى paid.",
            "client": "Fiscozen · Fisctech Milano",
            "discipline": "Growth systems",
            "duration": "16 أسبوعاً",
            "year": "2024",
            "standfirst":
                "من onboarding بمساعدة محاسب إلى self-serve كامل "
                "للـ partite IVA. +47% تحويل trial → paid خلال 90 يوماً.",
            "meta_client_label":"// client",
            "meta_discipline_label":"// capability",
            "meta_duration_label":"// duration",
            "meta_year_label":"// delivered",
            "cover_image": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1600&q=80&auto=format&fit=crop",
            "problem_label":"// problem",
            "problem_heading":"Onboarding يتطلب محاسباً.",
            "problem_paragraphs":["كل partita IVA في trial بحاجة إلى 30 دقيقة مع محاسب للبدء. Bottleneck حرج."],
            "solution_label":"// solution",
            "solution_heading":"Guided onboarding self-serve، محاسب اختياري.",
            "solution_paragraphs":["Form موجَّه يملأ ATECO سلفاً حسب سرد المستخدم الحر، مدمج مع InfoCamere."],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>ثمانية</em> سبرينت، KPI أسبوعي.",
            "timeline_intro":"الأولوية: time-to-first-value تحت 20 دقيقة.",
            "timeline_steps":[
                {"id":"S.01","duration":"أسبوع 1-3","title":"<em>Research</em>","body":"20 مقابلة partite IVA لأول مرة."},
                {"id":"S.02","duration":"أسبوع 4-8","title":"<em>Flow v1</em>","body":"أول onboarding self-serve. 28% activation."},
                {"id":"S.03","duration":"أسبوع 9-12","title":"<em>Iterate</em>","body":"4 A/B test. 41% activation."},
                {"id":"S.04","duration":"أسبوع 13-16","title":"<em>Scale</em>","body":"Rollout 100%. 47% post-90 يوماً."},
            ],
            "results_label":"// results",
            "results_heading":"<em>أربعة</em> أشهر، <em>ثلاثة</em> مقاييس.",
            "results_stats":[
                ("<em>+47%</em>","trial → paid","من 21% إلى 31% conv. عند 90 يوماً"),
                ("<em>18 د.</em>","TTFV","من 4 ساعات مع محاسب"),
                ("<em>−38%</em>","CAC","customer acquisition cost"),
                ("<em>+2.1x</em>","volume","trial أسبوعية post-rollout"),
            ],
            "quote":"فريق Aura شحن A/B test في 16 أسبوعاً أكثر مما فعلنا في السنتين السابقتين.",
            "quote_author":"Vittorio Amato",
            "quote_role":"CEO · Fiscozen",
            "next_label":"// next case",
            "next_heading":"→ شاهد كل <em>الأعمال</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ احجز <em>call</em>",
        },
    ],
}
