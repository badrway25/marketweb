"""Aura — Digital Studio · EN content registry.

Agency live rollout, Phase 2g3.6f, Session 49.

Voice contract (TechCrunch / Linear / Figma / Intercom register):
- Second-person / imperative-light ("book a call", "let's talk", "see it live").
- Growth-tech lexicon: "sprint", "discovery", "backlog", "telemetry",
  "product-market fit", "dashboard", "funnel", "onboarding", "NPS".
  Never curatorial / editorial vocabulary (that is Vertex).
- Clients are tech / SaaS / product / scale-up — Italian fintechs,
  European platforms, B2B, early-stage post-Series A.
- Numbers explicit and measurable. "+34%", "6 wks", "Δ NPS +22",
  "MRR €840K". Never "with care" — the voice is direct, measured.
- Mono is used for: sprint IDs, status, KPI, timestamps, stack logos.
"""
from __future__ import annotations

from typing import Any


AURA_CONTENT_EN: dict[str, Any] = {

    "pages": [
        {"slug": "home",         "label": "Studio",        "kind": "home"},
        {"slug": "studio",       "label": "About",         "kind": "about"},
        {"slug": "capabilities", "label": "Capabilities",  "kind": "services"},
        {"slug": "lavori",       "label": "Work",          "kind": "project_list"},
        {"slug": "sprint",       "label": "Sprint",        "kind": "process"},
        {"slug": "brief",        "label": "Brief",         "kind": "contact"},
    ],

    # ── Site chrome ──────────────────────────────────────────────
    "site": {
        "logo_word":   "Aura",
        "tag":         "Digital · product · growth studio",
        "sprint_chip": "Sprint 07/Q2 · live",
        "nav_cta":     "Book a call",
        "inquiry_page_slug": "brief",
        "phone":       "+39 02 8728 4411",
        "email":       "hello@aura.studio",
        "address":     "Via Paolo Sarpi 41 · 20154 Milano",
        "hours_compact":"Call slots · Mon — Thu · 10 — 18",
        "license":     "P.IVA 12890440964 · Milano",
        "footer_intro":
            "Independent digital studio. We design products, "
            "platforms and growth systems for scale-ups and "
            "tech companies. Based in Milano, European delivery.",
        "foot_shiplog_label":    "// ship log · last 6",
        "foot_current_sprint":   "sprint 07/Q2 · live",
        "foot_shiplog_rows": [
            ("yesterday · 18:04", "v2.14",  "Soldo — new corporate onboarding live"),
            ("yesterday · 09:21", "v2.13",  "Fastweb Plus — residential dashboard v2.3"),
            ("mon · 15:30",       "v2.12",  "Lendlease — asset manager portal"),
            ("fri · 11:12",       "v2.11",  "Casavo — retention A/B loop 003"),
            ("thu · 17:45",       "v2.10",  "Milkman — ship tracking SDK"),
            ("wed · 10:02",       "v2.09",  "Fiscozen — self-serve onboarding"),
        ],
        "foot_stack_marquee": [
            "Figma", "Linear", "Notion", "GitHub", "Vercel", "Stripe",
            "Segment", "PostHog", "Supabase", "Framer", "Mixpanel", "Sentry",
        ],
        "foot_studio_label":  "Studio",
        "foot_stack_label":   "Delivery stack",
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
        "chip": "3 slots open · Q3 2026",
        "headline": "From the <em>discovery call</em> to the <em>first KPI</em> in six weeks.",
        "intro":
            "We are a digital studio building products and "
            "growth systems for Italian and European scale-ups. "
            "Two-week sprints, shared dashboard, "
            "measurable delivery. Zero agency, all product.",
        "primary_cta":   "Book a call",
        "primary_href":  "brief",
        "secondary_cta": "Recent work",
        "secondary_href":"lavori",

        "hero_metrics": [
            ("<em>47</em>",    "products shipped since 2019"),
            ("<em>+34%</em>",  "median post-rework conversion"),
            ("<em>6 wks</em>", "from sprint zero to first KPI"),
        ],

        # Dashboard console tile
        "console": {
            "path":           "aura.studio/clients/casavo/live",
            "status_chip":    "LIVE · sprint 07/Q2",
            "primary_metric": "+34%",
            "primary_label":  "Post-rework conversion · last 30 days",
            "kpi": [
                ("<em>+18%</em>",    "Day-30 retention"),
                ("<em>Δ 22</em>",    "NPS pre / post · Casavo"),
                ("<em>€ 840K</em>",  "MRR · sprint 1 – 14"),
                ("<em>99.98%</em>",  "Uptime last quarter"),
            ],
            "meta_label":     "Current sprint",
            "meta_value":     "07/Q2 · week 2 of 2",
        },

        # Capabilities mini
        "capab_label":   "Capabilities",
        "capab_heading": "Four <em>areas</em>, one team.",
        "capab_intro":
            "We work on four kinds of project — product launches, "
            "platform redesigns, growth systems and B2B platform "
            "delivery. Every project runs through a dedicated team "
            "of 3-5 people, never an account layer.",
        "capab_cards": [
            {
                "id":   "C.01",
                "title":"Product <em>launch</em>",
                "body": "From concept to live onboarding. "
                        "Ideal for post-Series-A scale-ups that need to "
                        "move from MVP to paying product.",
                "tags": ["Discovery", "Design system", "Next.js", "Analytics"],
            },
            {
                "id":   "C.02",
                "title":"Platform <em>redesign</em>",
                "body": "Rethink mature products without losing users. "
                        "Research, A/B testing, progressive migration.",
                "tags": ["UX audit", "A/B", "Incremental ship", "PostHog"],
            },
            {
                "id":   "C.03",
                "title":"Growth <em>systems</em>",
                "body": "Onboarding, retention, referral, pricing experiments. "
                        "Quick wins in the first 30 days, systems in 90.",
                "tags": ["Onboarding", "Retention", "Pricing", "Experiments"],
            },
            {
                "id":   "C.04",
                "title":"B2B <em>delivery</em>",
                "body": "Asset-manager portals, corporate dashboards, "
                        "internal back-offices. SSO + data-warehouse integration.",
                "tags": ["Dashboards", "SSO", "Roles", "BigQuery"],
            },
        ],

        # Sprint strip
        "sprint_label":   "The way we ship",
        "sprint_heading": "Four <em>sprints</em>, from discovery to scale.",
        "sprint_intro":
            "Every project is structured in two-week sprints. "
            "You see exactly what we're doing, when it will ship, "
            "and which metrics we're moving. No end-of-month surprises.",
        "sprints": [
            {
                "id":"S.00", "duration":"Sprint 0 · 1 week",
                "title":"<em>Signal</em>",
                "body": "Discovery with stakeholders, users, dashboards. "
                        "Out: shared brief + initial backlog.",
                "output": "OUT · brief + backlog",
            },
            {
                "id":"S.01", "duration":"Sprint 1 — 2 · 4 wks",
                "title":"<em>Sketch</em>",
                "body": "Design system + testable prototypes. "
                        "Qualitative research + first A/Bs on the critical hypotheses.",
                "output": "OUT · prototype + design tokens",
            },
            {
                "id":"S.02", "duration":"Sprint 3 — 5 · 6 wks",
                "title":"<em>Ship</em>",
                "body": "Staging → production rollout. "
                        "Live metric monitoring, rollback available at 1 click.",
                "output": "OUT · production + first KPI",
            },
            {
                "id":"S.03", "duration":"Sprint 6+ · ongoing",
                "title":"<em>Scale</em>",
                "body": "Continuous experiments, feature expansion, "
                        "post-launch optimisation. Shared ship-log as partner.",
                "output": "OUT · weekly ship-log",
            },
        ],

        # Lavori cards
        "work_label":      "Recent work",
        "work_heading":    "Seven <em>products</em>, seven <em>metrics</em>.",
        "work_intro":
            "Every project has one clear metric, declared in sprint zero "
            "and measured by sprint three. If the metric doesn't move, "
            "we work for free until it does.",
        "work_page_slug": "lavori",
        "work_cards": [
            {
                "slug": "casavo-retention-rework",
                "id":   "W.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=900&q=80&auto=format&fit=crop",
                "title":"Three-month retention rework",
                "client":"Casavo · Proptech Milano",
                "metric_chip": "+18% retention · D30",
                "stack":["Next.js", "PostHog", "Figma"],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "W.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=900&q=80&auto=format&fit=crop",
                "title":"Residential dashboard v2",
                "client":"Fastweb · Telco Italy",
                "metric_chip": "NPS +22 · 6 months",
                "stack":["React", "Django", "Segment"],
            },
            {
                "slug": "soldo-corporate-onboarding",
                "id":   "W.03",
                "cover":"https://images.unsplash.com/photo-1559028012-481c04fa702d?w=900&q=80&auto=format&fit=crop",
                "title":"Self-serve corporate onboarding",
                "client":"Soldo · Fintech pan-EU",
                "metric_chip": "-54% time to activate",
                "stack":["Next.js", "Stripe", "Mixpanel"],
            },
        ],

        "metric_strip": [
            ("<em>47</em>",     "products shipped",  "since 2019 — avg 8 / year"),
            ("<em>+34%</em>",   "median conversion", "between pre- and post-rework"),
            ("<em>99.98%</em>", "uptime",            "last quarter · status.aura.studio"),
            ("<em>6 wks</em>",  "time to first KPI", "from sprint zero to first metric moved"),
        ],

        "cta_label":   "Next call",
        "cta_heading": "Three <em>slots</em> open for Q3 2026.",
        "cta_sub":
            "The first slot is a 30-minute discovery call. If the "
            "project is right for us, within 5 days you receive a "
            "reading brief + sprint-zero estimate.",
        "cta_chip":    "30 min · zero commitment",
        "cta_primary": "Book a call",
    },

    # ── STUDIO (about) ───────────────────────────────────────────
    "studio": {
        "chip": "Team · 11 people · Milano + remote",
        "headline": "A team of <em>eleven</em>, <em>eight years</em> of products shipped.",
        "standfirst":
            "Aura is a product-design and engineering studio founded in "
            "Milano in 2019. Eleven people — five designers, four "
            "engineers, two product managers — spread between Milano, Torino "
            "and remote. Zero account managers, zero intermediate layers: "
            "whoever signs the brief is whoever ships it.",

        "facts": [
            ("<em>11</em>",   "people",              "5 design · 4 eng · 2 PM"),
            ("<em>47</em>",   "products shipped",    "From 2019 to today"),
            ("<em>3</em>",    "locations",           "Milano · Torino · remote"),
            ("<em>94%</em>",  "clients renew",       "2024 retention rate"),
        ],

        "story_label":   "History of the studio",
        "story_heading": "How <em>scale-ups</em> forced us to rethink the design studio.",
        "story_paragraphs": [
            "Aura was founded in 2019 by Luca Bianchi and Sofia Reggiani, "
            "former product designers at Spotify and Figma. The opening idea was "
            "simple: <em>we don't want to be an agency, we don't want to "
            "be freelancers</em>. We wanted a studio that worked "
            "like an in-house team — with the same tools, the same "
            "metrics, the same cadence — but from the outside.",
            "The first three years were about learning. We understood "
            "that Italian scale-ups didn't need <em>design</em> "
            "— they needed <em>delivery</em>. So we hired "
            "full-stack engineers. We understood that design reviews "
            "weren't enough — you needed the ship log. We understood that value "
            "wasn't in mockups, but in metrics moved.",
            "Today Aura works with 6-8 clients a year, in two-week "
            "sprints, with one metric declared at the start of each "
            "project. Each project publishes an internal ship log that the "
            "client can read in real time. If the metric doesn't "
            "move, we work for free until it does. "
            "It's the only way we know how to work.",
        ],

        "team_label":   "The team",
        "team_heading": "Who <em>ships</em> the work.",
        "team_intro":
            "Every project is carried by a dedicated team of 3-5 people. "
            "Teams are composed by project type and don't "
            "change mid-flight. Whoever starts the project ships it.",
        "team": [
            {
                "name": "Luca Bianchi",
                "role": "Co-founder · Head of product",
                "bio":  "Ex-Spotify (Stockholm · 2014-2018) and Figma "
                        "(San Francisco · 2018-2019). Led the "
                        "growth-design team for the EU market. "
                        "Owns the sprint definition.",
                "portrait": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Linear", "PostHog", "Notion"],
            },
            {
                "name": "Sofia Reggiani",
                "role": "Co-founder · Head of engineering",
                "bio":  "Ex-Spotify (Stockholm) and Google (London). "
                        "Led the Next.js migration of two pan-European "
                        "platforms. Owns the delivery stack.",
                "portrait": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=900&q=80&auto=format&fit=crop",
                "stack": ["Next.js", "TypeScript", "Vercel", "Supabase"],
            },
            {
                "name": "Matteo Leone",
                "role": "Principal product designer",
                "bio":  "Eight years at Satispay (Milano) before "
                        "joining Aura in 2022. Designed three "
                        "onboardings for Italian fintechs with >1M users.",
                "portrait": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=900&q=80&auto=format&fit=crop",
                "stack": ["Figma", "Framer", "Stripe Elements"],
            },
        ],

        "values_label":   "How we work",
        "values_heading": "<em>Four rules</em> we don't negotiate.",
        "values": [
            ("V.01", "One <em>metric</em> declared",
             "Every project has a clear metric defined in sprint zero. "
             "If it doesn't move, we stay until it does."),
            ("V.02", "One <em>dedicated</em> team",
             "Whoever starts the project ships it. Zero account managers, "
             "zero handoffs. The designer who designs is the one who ships."),
            ("V.03", "A <em>public</em> ship-log",
             "The client has real-time access to the internal ship-log. "
             "They see what we've shipped, when, why, and what failed."),
            ("V.04", "One <em>call</em> a week",
             "One synchronous 30-minute meeting per week, "
             "with a written agenda. The rest is async on Linear and Slack."),
        ],
    },

    # ── CAPABILITIES (services) ──────────────────────────────────
    "capabilities": {
        "chip": "4 areas · 3-5 people per project",
        "headline": "Four <em>capabilities</em>, all measured.",
        "standfirst":
            "Every capability has a documented method, a typical metric, "
            "a predictable duration and a predefined stack. It isn't a "
            "rate card — it's a system that lets us tell you, in sprint zero, "
            "what to expect and when.",

        "capabilities": [
            {
                "id": "CAP.01 · Product launch",
                "title": "Taking <em>a new product</em> to first conversion.",
                "tagline": "Typical: 14 — 20 wks · KPI · activation + first paid",
                "body":
                    "For scale-ups that have validated the problem (Seed / Series A) "
                    "and need to build the paying product. We start from "
                    "sprint zero (research + backlog), move through the design "
                    "system + the first three critical flows, and take to "
                    "production with measurable onboarding and live pricing.",
                "scope_label": "// scope",
                "scope": [
                    "Sprint zero + user research",
                    "Design system (tokens + 60 components)",
                    "Three critical flows in production",
                    "Self-serve onboarding",
                    "Pricing page live + Stripe",
                    "Analytics + full funnel",
                    "Rollback + feature flags",
                    "Handover docs to internal team",
                ],
                "stack": ["Next.js 14", "TypeScript", "Figma", "Stripe", "Segment", "PostHog"],
            },
            {
                "id": "CAP.02 · Platform redesign",
                "title": "<em>Redesigning</em> a mature product without losing users.",
                "tagline": "Typical: 20 — 30 wks · KPI · retention + NPS",
                "body":
                    "For platforms with > 50k active users that have accumulated "
                    "UX debt. We start from a quantitative + qualitative audit, "
                    "build the new system in parallel, migrate "
                    "progressively via feature flags. No big-bang launch.",
                "scope_label": "// scope",
                "scope": [
                    "UX audit + quant analysis",
                    "30+ user interviews",
                    "Progressive migration",
                    "A/B testing on cohort",
                    "Design system evolution",
                    "Market-by-market rollout",
                    "Post-launch tuning · 8 wks",
                    "Internal team training",
                ],
                "stack": ["React", "Django", "PostHog", "Segment", "Split.io"],
            },
            {
                "id": "CAP.03 · Growth systems",
                "title": "<em>Growth systems</em> measurable in 30 days.",
                "tagline": "Typical: 8 — 16 wks · KPI · conversion + LTV",
                "body":
                    "For products already in production that need to grow. "
                    "We work on onboarding, pricing, retention, referral. "
                    "Quick wins in the first 30 days (usually +12% on a funnel). "
                    "90-day systems (ongoing new experiments).",
                "scope_label": "// scope",
                "scope": [
                    "Funnel audit + benchmark",
                    "Experiment backlog",
                    "Weekly A/B cadence",
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
                "title": "<em>Asset-manager</em> portals and corporate dashboards.",
                "tagline": "Typical: 24 — 36 wks · KPI · task completion + time saved",
                "body":
                    "For B2B companies (proptech, fintech, healthtech) that need to "
                    "deliver portals to their enterprise clients. SSO, roles, "
                    "permissions, integrated data warehouse, structured exports. "
                    "Not sexy, but it's where annual renewals are won.",
                "scope_label": "// scope",
                "scope": [
                    "Discovery with 3-5 enterprise users",
                    "Corporate design tokens",
                    "SSO (SAML · Okta · Azure)",
                    "Granular roles + permissions",
                    "Data warehouse integration",
                    "Multi-format export",
                    "Compliance audit log",
                    "99.9% SLA + monitoring",
                ],
                "stack": ["Next.js", "BigQuery", "Okta", "Datadog", "Sentry"],
            },
        ],

        "engagement_label":   "Three engagement modes",
        "engagement_heading": "From the <em>single project</em> to the <em>continuous partner</em>.",
        "engagement_intro":
            "We pick the engagement model together, in sprint zero. "
            "Usually 70% of projects start as fixed-scope, 30% as ongoing "
            "partnerships. Time & materials is rare — we only use it "
            "for discovery shorter than 3 weeks.",
        "engagement_tiles": [
            {
                "id":    "E.01 · Discovery",
                "title": "<em>Discovery sprint</em>",
                "range": "2 — 3 weeks · fixed",
                "body":  "Dedicated sprint zero. Research, audit, backlog, "
                         "estimate. If we then proceed, it gets scaled up.",
                "includes": [
                    "User research (5-8 interviews)",
                    "Quantitative audit (analytics)",
                    "Initial backlog",
                    "Delivery estimate",
                    "Shared 30-page document",
                ],
            },
            {
                "id":    "E.02 · Fixed delivery",
                "title": "<em>Fixed delivery</em>",
                "range": "8 — 30 weeks · fixed",
                "body":  "Launch or redesign with fixed scope and budget. "
                         "The most common mode for post-Series-A scale-ups.",
                "includes": [
                    "Dedicated team of 3-5",
                    "Two-week sprints",
                    "Shared ship-log",
                    "Declared metric",
                    "Rollback + feature flags",
                    "Documented handover",
                ],
                "featured": True,
            },
            {
                "id":    "E.03 · Partner mode",
                "title": "<em>Partner mode</em>",
                "range": "Q-by-Q · quarterly renewal",
                "body":  "Ongoing engagement for mature platforms. "
                         "Days-per-quarter band, shared roadmap.",
                "includes": [
                    "Weekly ship cadence",
                    "Shared client backlog",
                    "Ongoing experiments",
                    "Quarterly KPI review",
                    "SLA support + on-call",
                ],
            },
        ],

        "cta_label":   "Next step",
        "cta_heading": "Let's meet for <em>discovery</em>, 30 minutes.",
        "cta_primary": "Book a call",
    },

    # ── LAVORI (project_list) ────────────────────────────────────
    "lavori": {
        "chip": "Product archive · 2019 — 2026",
        "headline": "<em>Forty-seven</em> products shipped. <em>Seven</em> on show.",
        "standfirst":
            "Every case has a declared, measured metric. "
            "We show seven public projects — the other forty are "
            "under NDA (common in fintech and B2B). Full archive on request.",
        "tabs": ["All", "Product launch", "Redesign", "Growth", "B2B delivery"],
        "tabs_count_label": "// archive total",
        "tabs_count_value": "047",

        "projects": [
            {
                "slug": "casavo-retention-rework",
                "id":   "P.01",
                "cover":"https://images.unsplash.com/photo-1551434678-e076c223a692?w=1200&q=80&auto=format&fit=crop",
                "title":"Retention rework · home-buying platform",
                "client":"Casavo",
                "discipline":"PROPTECH · REDESIGN",
                "year": "2025",
                "blurb":
                    "Rethought the entire funnel from search to signature. "
                    "Progressive migration via feature flag across 180k users. "
                    "Zero downtime, +18% retention at 30 days.",
                "kpi": [
                    ("<em>+18%</em>",  "D30 retention"),
                    ("<em>Δ+22</em>",  "NPS"),
                    ("<em>180K</em>",  "users migrated"),
                ],
            },
            {
                "slug": "fastweb-plus-dashboard",
                "id":   "P.02",
                "cover":"https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80&auto=format&fit=crop",
                "title":"Residential dashboard v2.3",
                "client":"Fastweb",
                "discipline":"TELCO · PLATFORM",
                "year": "2024",
                "blurb":
                    "A new dashboard for 2.8M residential customers. "
                    "Integrated SSO, service management, full self-care. "
                    "Call-centre volume down −34% in six months.",
                "kpi": [
                    ("<em>−34%</em>",   "CC calls"),
                    ("<em>2.8M</em>",   "users"),
                    ("<em>NPS 64</em>", "post-launch"),
                ],
            },
            {
                "slug": "soldo-corporate-onboarding",
                "id":   "P.03",
                "cover":"https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1200&q=80&auto=format&fit=crop",
                "title":"Self-serve corporate onboarding",
                "client":"Soldo",
                "discipline":"FINTECH · LAUNCH",
                "year": "2025",
                "blurb":
                    "From assisted onboarding (4 day median) to self-serve "
                    "(42 minutes). Pan-EU compliance, integrated KYC, "
                    "multi-currency day zero.",
                "kpi": [
                    ("<em>−54%</em>",      "TTFV"),
                    ("<em>+41%</em>",      "activation"),
                    ("<em>7 markets</em>", "day one"),
                ],
            },
            {
                "slug": "milkman-ship-sdk",
                "id":   "P.04",
                "cover":"https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1200&q=80&auto=format&fit=crop",
                "title":"Ship-tracking SDK for retailers",
                "client":"Milkman",
                "discipline":"LOGISTICS · B2B",
                "year": "2024",
                "blurb":
                    "A JavaScript SDK for delivery tracking integrated into "
                    "the checkout of 40+ retailers. One API call, "
                    "retailer-side branding, real-time updates.",
                "kpi": [
                    ("<em>40+</em>",    "retailers"),
                    ("<em>1 call</em>", "API"),
                    ("<em>2MB</em>",    "bundle"),
                ],
            },
            {
                "slug": "lendlease-asset-portal",
                "id":   "P.05",
                "cover":"https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
                "title":"Enterprise asset-manager portal",
                "client":"Lendlease",
                "discipline":"PROPTECH · B2B",
                "year": "2024",
                "blurb":
                    "A portal for 80 Italian asset managers. Azure SSO, "
                    "granular roles, integrated data warehouse with "
                    "multi-format export. MiFID II compliance included.",
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
                "title":"Self-serve onboarding for sole traders",
                "client":"Fiscozen",
                "discipline":"FISCTECH · GROWTH",
                "year": "2024",
                "blurb":
                    "From accountant-assisted to fully self-serve "
                    "onboarding. Shorter activation times and +47% "
                    "conversion from trial to paid in the first 90 days.",
                "kpi": [
                    ("<em>+47%</em>",   "trial → paid"),
                    ("<em>18 min</em>", "TTFV"),
                    ("<em>90 days</em>","measurement"),
                ],
            },
        ],

        "velocity_label":   "Median velocity",
        "velocity_heading": "How we <em>ship</em> · last twelve months.",
        "velocity_body":
            "The numbers below are the ones we watch internally. "
            "Updated monthly. If you're interested in the methodology behind them, "
            "we're happy to talk through it on a discovery call.",
        "velocity_stats": [
            ("<em>8</em>",      "products shipped · 2025"),
            ("<em>94%</em>",    "projects on-time"),
            ("<em>+26%</em>",   "median KPI moved"),
            ("<em>47 days</em>","median time-to-ship"),
        ],
    },

    # ── SPRINT (process) ─────────────────────────────────────────
    "sprint": {
        "chip": "Methodology · 4 phases · live telemetry",
        "headline": "Four <em>sprints</em>, from discovery to scale.",
        "standfirst":
            "Every project moves through four declared phases. "
            "Predictable durations, clear deliverables, public metrics. "
            "The client sees in real time where we are — and why.",

        "sprints": [
            {
                "id": "Sprint 0 · Signal",
                "duration": "1 week · fixed",
                "title": "<em>Understand</em> the problem before designing it.",
                "tagline": "// output: shared brief + initial backlog",
                "body":
                    "Sprint zero is the most important and most under-rated phase. "
                    "In five days we listen to the stakeholders (CEO, product, "
                    "customer success), interview 5-8 real users, read "
                    "the current dashboard. At the end we present a reading "
                    "brief + backlog of hypotheses to test.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Shared brief · 24 pages",
                    "Initial backlog · Linear",
                    "Stakeholder map",
                    "Research summary · 5-8 interviews",
                    "Declared metric + baseline",
                    "Delivery estimate (sprint count)",
                ],
            },
            {
                "id": "Sprint 1 — 2 · Sketch",
                "duration": "4 weeks",
                "title": "<em>Prototype</em> before building.",
                "tagline": "// output: testable prototype + design system v0.1",
                "body":
                    "The first two sprints are rapid prototyping. "
                    "We build the three most critical flows in Figma + Framer, "
                    "test them with real users, iterate. In parallel "
                    "we kick off the design system (tokens + 20 base components). "
                    "Real code lands in sprint 3.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Interactive Figma prototype",
                    "3 rounds of user testing",
                    "Design system v0.1",
                    "Code architecture",
                    "A/B testing plan",
                    "Design review with the client",
                ],
            },
            {
                "id": "Sprint 3 — 5 · Ship",
                "duration": "6 weeks",
                "title": "<em>To production</em>, incremental.",
                "tagline": "// output: production live + first metric",
                "body":
                    "Implementation and incremental delivery. Every Friday we ship "
                    "something to staging, every sprint end to production. "
                    "Feature flags + 1-click rollback. By the end of sprint 5 "
                    "the first declared metric must have moved.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Weekly staging deploy",
                    "Bi-weekly production deploy",
                    "All feature flags active",
                    "Rollback plan documented",
                    "Monitoring · Datadog / Sentry",
                    "First metric moved",
                ],
            },
            {
                "id": "Sprint 6+ · Scale",
                "duration": "ongoing · quarterly",
                "title": "<em>Scale</em> · continuous experiments.",
                "tagline": "// output: weekly ship-log + quarterly KPI review",
                "body":
                    "Post-launch we switch into scale mode. Weekly "
                    "experiments, feature expansion, post-launch optimisation. "
                    "Public shared ship-log. Quarterly review of the "
                    "metrics against plan.",
                "deliverables_label": "// deliverables",
                "deliverables": [
                    "Public ship-log",
                    "Weekly A/B",
                    "6-month feature roadmap",
                    "Quarterly KPI review",
                    "Internal team training",
                    "Continuous handover",
                ],
            },
        ],

        "mindset_label":   "How we <em>think</em> about the process",
        "mindset_heading": "Three <em>delivery principles</em>.",
        "mindset_cards": [
            {
                "id": "P.01",
                "title": "Visible <em>telemetry</em>",
                "body": "The ship-log is public to the client from day zero. "
                        "What we shipped, when, why. Zero dark rooms.",
            },
            {
                "id": "P.02",
                "title": "<em>Rollback</em> at 1 click",
                "body": "Every feature sits behind a flag. If something isn't "
                        "working in production, we turn it off in under 60 seconds.",
            },
            {
                "id": "P.03",
                "title": "<em>Skin in the game</em>",
                "body": "If the declared metric doesn't move, we keep "
                        "working for free. We've done it four times in eight years.",
            },
        ],

        "stack_label":   "Delivery stack",
        "stack_heading": "What we <em>ship with</em>.",
        "stack_intro":
            "The stack is picked to be reliable, fast, and easy "
            "to hand over to the client's internal team. Zero boutique tech.",
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
        "chip": "3 slots open · Q3 2026",
        "headline": "Tell us about the <em>project</em>. We call you back in under 48h.",
        "standfirst":
            "This isn't a form. It's a brief structured in 3 steps. "
            "Every reply you receive is written personally by Luca or "
            "Sofia, not by an account manager. If the project is right for us, "
            "the second message is already a call proposal.",

        "form_heading": "// brief intake · 3 step",

        "step1": {
            "id": "STEP 01", "title": "Who you are", "sub": "Only the strictly necessary fields.",
        },
        "step2": {
            "id": "STEP 02", "title": "The project", "sub": "The more concrete, the more useful the reply.",
        },
        "step3": {
            "id": "STEP 03", "title": "When", "sub": "Pick an indicative slot — we'll confirm by email.",
        },

        "labels": {
            "name":    "Name and surname",
            "role":    "Role",
            "company": "Company / product",
            "email":   "Work email",
            "scope":   "Type of project",
            "brief":   "Short narrative",
            "slot":    "Preferred slot",
        },
        "placeholders": {
            "name":    "First Last",
            "role":    "e.g. Head of Product",
            "company": "Company name",
            "email":   "name@company.com",
            "brief":   "What you're building, where you are (MRR, users, round), what problem you're feeling, how you measure success. A concrete brief gets a concrete reply.",
        },
        "scope_options": [
            "Product launch · first time live",
            "Platform redesign · mature product",
            "Growth systems · funnel / retention",
            "B2B delivery · portal / dashboard",
            "Discovery sprint · 2-3 weeks",
            "Not sure yet — let's talk",
        ],

        "slots": [
            ("mon10", "Mon · 10:00"),
            ("mon15", "Mon · 15:00"),
            ("tue10", "Tue · 10:00"),
            ("tue15", "Tue · 15:00"),
            ("wed10", "Wed · 10:00"),
            ("wed15", "Wed · 15:00"),
            ("thu10", "Thu · 10:00"),
            ("thu15", "Thu · 15:00"),
            ("async", "Async via email only"),
        ],
        "form_submit_label": "Book the call",
        "form_submit_note":  "// reply within 48 working hours · all EU time zones",

        "async_label":   "Prefer async?",
        "async_heading": "Write to <em>Luca</em> and <em>Sofia</em>.",
        "async_body":
            "Every email lands directly with the two co-founders. "
            "They reply themselves — not an account manager, not a bot.",

        "studio_label":  "The studio",

        "response_label": "// response SLA",
        "response_rows": [
            ("Brief",         "< 48h"),
            ("Proposal",      "5 days"),
            ("Sprint zero",   "2 weeks"),
            ("First metric",  "6 weeks"),
        ],

        "boot_left":  "aura.studio · hello@aura.studio · +39 02 8728 4411",
        "boot_right": "// always open to a brief",
    },

    # ── POSTS (project_detail) ───────────────────────────────────
    "posts": [
        {
            "slug": "casavo-retention-rework",
            "id":   "P.01 · PROPTECH",
            "title": "Casavo · <em>+18% retention</em> in three months.",
            "client": "Casavo · Proptech Milano",
            "discipline": "Redesign · retention",
            "duration": "14 weeks",
            "year": "2025",
            "standfirst":
                "The rework of Casavo's post-booking funnel. "
                "An incremental optimisation across 180k users, "
                "feature flags everywhere, zero downtime. Three months later: "
                "+18% D30 retention, NPS +22, MRR +€840K.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "Users came back, but didn't convert.",
            "problem_paragraphs": [
                "Casavo had doubled active users between 2023 and 2024, "
                "but conversion from <em>visit 1</em> to <em>real viewing booking</em> "
                "had dropped 12% — across 180k active users, that meant ~21k "
                "bookings lost every month.",
                "The internal team had understood that the problem was in the "
                "post-signup funnel, but didn't have capacity to test 10+ hypotheses "
                "seriously without slowing the main roadmap.",
            ],

            "solution_label": "// solution",
            "solution_heading": "A second funnel, in parallel with the old.",
            "solution_paragraphs": [
                "Rather than rewriting the main funnel (too high a risk across "
                "180k users) we built a <em>second experimental funnel</em> "
                "behind a feature flag, available to 10% of traffic. Six weeks "
                "of testing, seven iterations, four flows tested.",
                "By the sixth iteration the second funnel beat the first by 18% "
                "on D30 retention. We progressively migrated the rest of the "
                "180k users across three weeks — 25% phase, then 50%, then 100%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Fourteen weeks, <em>seven sprints</em>.",
            "timeline_intro":
                "The timeline below is the real delivery chronology — pulled "
                "from the ship-log shared with Casavo.",
            "timeline_steps": [
                {"id": "S.00", "duration": "wk 1",     "title": "<em>Signal</em>",  "body": "Research + funnel audit + backlog of 14 hypotheses."},
                {"id": "S.01", "duration": "wk 2-3",   "title": "<em>Sketch</em>",  "body": "Prototypes of 4 alternative flows, 8 interviews."},
                {"id": "S.02", "duration": "wk 4-6",   "title": "<em>Ship</em>",    "body": "Second funnel live at 10%, first A/B test."},
                {"id": "S.03", "duration": "wk 7-11",  "title": "<em>Iterate</em>", "body": "6 weekly iterations. Cohort every Friday."},
                {"id": "S.04", "duration": "wk 12-14", "title": "<em>Migrate</em>", "body": "Rollout 25% → 50% → 100%. Zero downtime."},
            ],

            "results_label": "// results",
            "results_heading": "Four <em>metrics moved</em>.",
            "results_stats": [
                ("<em>+18%</em>",    "D30 retention",           "from 42% to 49.6% (90-day rolling)"),
                ("<em>Δ +22</em>",   "NPS",                     "from 31 to 53 in the 3 months post-rollout"),
                ("<em>+€ 840K</em>", "incremental MRR",          "12-month projection"),
                ("<em>0</em>",       "downtime during rollout",  "180k users, zero extra 5xx errors"),
            ],

            "quote": "In three months they understood our product better than consultants who had worked on it for a year. And they shipped.",
            "quote_author": "Marianna Colombo",
            "quote_role":   "VP Product · Casavo",

            "next_label":   "// next case",
            "next_heading": "→ see all <em>work</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ book a <em>call</em>",
        },
        {
            "slug": "fastweb-plus-dashboard",
            "id":   "P.02 · TELCO",
            "title": "Fastweb · <em>−34% CC calls</em> in 6 months.",
            "client": "Fastweb · Telco Italy",
            "discipline": "Platform redesign",
            "duration": "26 weeks",
            "year": "2024",
            "standfirst":
                "A new residential dashboard for 2.8M customers. "
                "Service management, payments, auto-care, SSO. "
                "Outcome: −34% call-centre calls, NPS 64 post-launch, "
                "full migration in six months with zero downtime.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "A 2014 dashboard in a 2024 world.",
            "problem_paragraphs": [
                "Fastweb's residential dashboard had been built in 2014 "
                "and re-skinned three times without touching the structure. Result: "
                "task completion at 41%, 2.1M call-centre calls a year for "
                "operations that should have been self-care.",
                "The goal: rebuild without losing users, without downtime, "
                "and without a big-bang launch — we had 26 weeks.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Micro-frontend + progressive migration.",
            "solution_paragraphs": [
                "We built the new dashboard as a <em>micro-frontend</em> "
                "alongside the old one — same domain, same SSO, same backend. "
                "Users were migrated by geographic cluster (Lombardia, "
                "Piemonte, Lazio...) in six phases.",
                "Each cluster was monitored for 2 weeks. If NPS and task "
                "completion were better than the old, we moved to the next cluster. "
                "If worse, we rolled back 24 hours and fixed.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Six phases</em> of geographic rollout.",
            "timeline_intro":
                "Each rollout phase had 2 weeks of monitoring before "
                "the next. The hardest was the third.",
            "timeline_steps": [
                {"id": "R.01", "duration": "Week 10", "title": "Piemonte",     "body": "400k users. NPS +18. Go."},
                {"id": "R.02", "duration": "Week 14", "title": "Lombardia",    "body": "680k users. NPS +22. Go."},
                {"id": "R.03", "duration": "Week 18", "title": "Veneto",       "body": "480k users. NPS +9. Hold 1 wk."},
                {"id": "R.04", "duration": "Week 22", "title": "Lazio",        "body": "520k users. NPS +21. Go."},
                {"id": "R.05", "duration": "Week 26", "title": "Rest of Italy","body": "720k users. NPS +19. Complete."},
            ],

            "results_label": "// results",
            "results_heading": "Six months, <em>four numbers</em>.",
            "results_stats": [
                ("<em>−34%</em>",    "call-centre calls", "~720k fewer calls / year"),
                ("<em>NPS 64</em>",  "post-launch",        "vs 32 pre-launch"),
                ("<em>2.8M</em>",    "users migrated",     "100% zero downtime"),
                ("<em>+41% TC</em>", "task completion",    "from 41% to 82%"),
            ],

            "quote": "Aura is the only studio that handed me a rollback plan for every single sprint. We used the rollback twice. Zero drama.",
            "quote_author": "Stefano Petri",
            "quote_role":   "Head of digital · Fastweb",

            "next_label":   "// next case",
            "next_heading": "→ see all <em>work</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ book a <em>call</em>",
        },
        {
            "slug": "soldo-corporate-onboarding",
            "id":   "P.03 · FINTECH",
            "title": "Soldo · onboarding from <em>4 days</em> to <em>42 minutes</em>.",
            "client": "Soldo · Fintech pan-EU",
            "discipline": "Product launch · onboarding",
            "duration": "18 weeks",
            "year": "2025",
            "standfirst":
                "A full redesign of Soldo's corporate onboarding. "
                "From an assisted process (4 days) to fully self-serve "
                "(42 minutes) across 7 European markets, with KYC, multi-currency "
                "and compliance. Result: +41% activation, −54% time to value.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1559028012-481c04fa702d?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "An onboarding that needed a human.",
            "problem_paragraphs": [
                "Soldo's 2024 onboarding took 4 days median "
                "(2 for KYC, 1 for multi-currency setup, 1 for card "
                "activation). Each onboarding consumed 1.2 hours of customer success. "
                "Across 2,800 onboardings/month, the cost was unsustainable.",
            ],

            "solution_label": "// solution",
            "solution_heading": "Guided onboarding, zero human.",
            "solution_paragraphs": [
                "We redesigned the entire flow as <em>self-serve guided</em>: "
                "the client uploads documents once, KYC runs in the background, "
                "multi-currency config is pre-filled against the market of residence.",
                "Human only on explicit request (link in every step). "
                "CSAT didn't drop — it rose 22%.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "Nine <em>sprints</em>, seven markets.",
            "timeline_intro":
                "First 4 sprints on UK (most mature market). "
                "The other 5 on cross-market rollout.",
            "timeline_steps": [
                {"id": "S.01", "duration": "wk 1-2",   "title": "<em>Discovery</em>",    "body": "120 customer success calls analysed."},
                {"id": "S.02", "duration": "wk 3-6",   "title": "<em>UK beta</em>",       "body": "New flow live on UK. +28% activation."},
                {"id": "S.03", "duration": "wk 7-10",  "title": "<em>DE · NL · FR</em>",  "body": "3 markets added. Multi-currency fix."},
                {"id": "S.04", "duration": "wk 11-14", "title": "<em>IT · ES · IE</em>",  "body": "3 markets added. Language fix."},
                {"id": "S.05", "duration": "wk 15-18", "title": "<em>Scale</em>",         "body": "Continuous optimisation. Weekly A/B."},
            ],

            "results_label": "// results",
            "results_heading": "Three core <em>metrics</em> moved.",
            "results_stats": [
                ("<em>42 min</em>", "time to activate",  "from 4 day median"),
                ("<em>+41%</em>",   "activation rate",    "trial → paid"),
                ("<em>+22%</em>",   "CSAT",               "post-onboarding"),
                ("<em>7</em>",      "markets",            "day one go-live"),
            ],

            "quote": "The outcome is that our corporate onboarding team today is 60% smaller but handles 3x the companies. Soldo wouldn't be at today's level without this rework.",
            "quote_author": "Rebecca Hughes",
            "quote_role":   "VP Growth · Soldo",

            "next_label":   "// next case",
            "next_heading": "→ see all <em>work</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ book a <em>call</em>",
        },
        {
            "slug": "milkman-ship-sdk",
            "id":   "P.04 · LOGISTICS",
            "title": "Milkman · <em>tracking SDK</em> for 40+ retailers.",
            "client": "Milkman · Logistics Italy",
            "discipline": "B2B delivery · SDK",
            "duration": "22 weeks",
            "year": "2024",
            "standfirst":
                "A white-label JavaScript SDK for delivery tracking, "
                "integrated into the checkout of 40+ Italian retailers. "
                "One API call, retailer-side branding, "
                "real-time updates. Bundle under 2MB gzipped.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1600&q=80&auto=format&fit=crop",

            "problem_label": "// problem",
            "problem_heading": "40 retailers, 40 custom integrations.",
            "problem_paragraphs": [
                "Milkman handled deliveries for more than 40 Italian retailers — "
                "Esselunga, Coop, Unieuro, Mediaworld — each with their own "
                "custom integration. Each new retailer took 8-12 "
                "weeks of engineering.",
            ],

            "solution_label": "// solution",
            "solution_heading": "One SDK, one API call.",
            "solution_paragraphs": [
                "We built a white-label JavaScript SDK. "
                "A retailer has to do just one thing: call <em>milkman.track(orderId)</em>. "
                "The SDK handles retailer-side branding (colours, fonts, logo), "
                "languages, real-time updates via WebSocket.",
                "Median integration: 3 hours. Before: 8-12 weeks.",
            ],

            "timeline_label": "// timeline",
            "timeline_heading": "<em>Five</em> sprints from SDK to the 40th retailer.",
            "timeline_intro": "First retailer (Esselunga) in sprint 3. The other 39 self-serve.",
            "timeline_steps": [
                {"id": "S.01", "duration": "wk 1-4",   "title": "<em>SDK core</em>",       "body": "Architecture, bundle, branding."},
                {"id": "S.02", "duration": "wk 5-10",  "title": "<em>Esselunga beta</em>", "body": "First retailer live. 2 critical bugs."},
                {"id": "S.03", "duration": "wk 11-14", "title": "<em>Unieuro · Coop</em>", "body": "2 retailers added. Zero bugs."},
                {"id": "S.04", "duration": "wk 15-18", "title": "<em>Docs + portal</em>",  "body": "Self-serve onboarding."},
                {"id": "S.05", "duration": "wk 19-22", "title": "<em>Scale</em>",          "body": "40th retailer integrated self-serve."},
            ],

            "results_label": "// results",
            "results_heading": "From <em>8 weeks</em> to <em>3 hours</em>.",
            "results_stats": [
                ("<em>40+</em>",    "retailers live",      "At sixth-month go-live"),
                ("<em>3 hrs</em>",  "time-to-integrate",   "From 8-12 week median"),
                ("<em>1.8 MB</em>", "bundle gzipped",      "Under the required 2 MB ceiling"),
                ("<em>0</em>",      "downtime",            "From first sprint to today"),
            ],

            "quote": "The SDK let us open three European markets in six months. Before, it would have been impossible.",
            "quote_author": "Antonio Perini",
            "quote_role":   "CEO · Milkman",

            "next_label":   "// next case",
            "next_heading": "→ see all <em>work</em>",
            "cta_label":    "// start a project",
            "cta_heading":  "→ book a <em>call</em>",
        },
        {
            "slug": "lendlease-asset-portal",
            "id":   "P.05 · PROPTECH",
            "title": "Lendlease · <em>enterprise portal</em> for 80 asset managers.",
            "client": "Lendlease · Proptech EU",
            "discipline": "B2B delivery",
            "duration": "30 weeks",
            "year": "2024",
            "standfirst":
                "An enterprise portal for 80 Italian asset managers. "
                "Azure SSO, granular roles, integrated data warehouse, "
                "MiFID II compliance. It isn't sexy — it's where renewal is won.",
            "meta_client_label":     "// client",
            "meta_discipline_label": "// capability",
            "meta_duration_label":   "// duration",
            "meta_year_label":       "// delivered",
            "cover_image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1600&q=80&auto=format&fit=crop",

            "problem_label":"// problem",
            "problem_heading":"An enterprise portal with zero self-serve.",
            "problem_paragraphs":[
                "80 asset managers were using a 2016 portal that needed "
                "human assistance for every action. Each asset manager consumed "
                "~6 hours / week of customer success. Quarterly re-contracting "
                "at risk.",
            ],
            "solution_label":"// solution",
            "solution_heading":"Self-serve dashboard + automated export.",
            "solution_paragraphs":[
                "We rebuilt the portal as a self-serve platform. "
                "Azure SSO, granular roles (analyst, manager, compliance), "
                "integrated data warehouse with multi-format export "
                "(PDF, XLSX, CSV, MiFID II XML).",
            ],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Ten</em> sprints, <em>three</em> rollout clusters.",
            "timeline_intro": "Rollout by asset-manager cluster (20/30/30).",
            "timeline_steps":[
                {"id":"S.01","duration":"wk 1-4",  "title":"<em>Discovery</em>",   "body":"Interviews with 12 asset managers."},
                {"id":"S.02","duration":"wk 5-14", "title":"<em>SSO + roles</em>", "body":"Azure SSO + full RBAC."},
                {"id":"S.03","duration":"wk 15-22","title":"<em>Dashboard</em>",   "body":"Core dashboard + analytics."},
                {"id":"S.04","duration":"wk 23-28","title":"<em>Export</em>",      "body":"Multi-format + MiFID II."},
                {"id":"S.05","duration":"wk 29-30","title":"<em>Rollout</em>",     "body":"80 asset managers migrated."},
            ],
            "results_label":"// results",
            "results_heading":"<em>80</em> asset managers, <em>zero</em> calls.",
            "results_stats":[
                ("<em>80</em>",       "asset managers migrated","100% by end of rollout"),
                ("<em>−92%</em>",     "CS calls",               "6 hrs → 28 min /wk"),
                ("<em>100%</em>",     "re-contracting",         "Two years running"),
                ("<em>MiFID II</em>", "compliance",             "Audit passed first time"),
            ],
            "quote":"The portal has become the main reason our asset managers renew.",
            "quote_author":"Valentina Greco",
            "quote_role":"Head of product · Lendlease IT",
            "next_label":"// next case",
            "next_heading":"→ see all <em>work</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ book a <em>call</em>",
        },
        {
            "slug": "fiscozen-onboarding-self-serve",
            "id":   "P.06 · FISCTECH",
            "title": "Fiscozen · <em>+47%</em> from trial to paid.",
            "client": "Fiscozen · Fisctech Milano",
            "discipline": "Growth systems",
            "duration": "16 weeks",
            "year": "2024",
            "standfirst":
                "From accountant-assisted to fully self-serve onboarding "
                "for Italian sole traders. +47% conversion trial → paid in 90 days.",
            "meta_client_label":"// client",
            "meta_discipline_label":"// capability",
            "meta_duration_label":"// duration",
            "meta_year_label":"// delivered",
            "cover_image": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1600&q=80&auto=format&fit=crop",
            "problem_label":"// problem",
            "problem_heading":"An onboarding that needed an accountant.",
            "problem_paragraphs":["Every trial VAT holder needed 30 min with an accountant to get started. A critical bottleneck."],
            "solution_label":"// solution",
            "solution_heading":"Guided self-serve onboarding, accountant optional.",
            "solution_paragraphs":["Guided form that pre-fills ATECO codes from the user's free-form description, integrated with InfoCamere."],
            "timeline_label":"// timeline",
            "timeline_heading":"<em>Eight</em> sprints, weekly KPI.",
            "timeline_intro":"Priority: time-to-first-value under 20 minutes.",
            "timeline_steps":[
                {"id":"S.01","duration":"wk 1-3",  "title":"<em>Research</em>","body":"20 first-time sole-trader interviews."},
                {"id":"S.02","duration":"wk 4-8",  "title":"<em>Flow v1</em>", "body":"First self-serve onboarding. 28% activation."},
                {"id":"S.03","duration":"wk 9-12", "title":"<em>Iterate</em>", "body":"4 A/B tests. 41% activation."},
                {"id":"S.04","duration":"wk 13-16","title":"<em>Scale</em>",   "body":"100% rollout. 47% post-90 days."},
            ],
            "results_label":"// results",
            "results_heading":"<em>Four</em> months, <em>three</em> metrics.",
            "results_stats":[
                ("<em>+47%</em>",   "trial → paid","from 21% to 31% conv. at 90 days"),
                ("<em>18 min</em>", "TTFV",        "from 4 hours with an accountant"),
                ("<em>−38%</em>",   "CAC",         "customer acquisition cost"),
                ("<em>+2.1x</em>",  "volume",      "weekly trials post-rollout"),
            ],
            "quote":"The Aura team shipped more A/B tests in 16 weeks than we had in the previous 2 years.",
            "quote_author":"Vittorio Amato",
            "quote_role":"CEO · Fiscozen",
            "next_label":"// next case",
            "next_heading":"→ see all <em>work</em>",
            "cta_label":"// start a project",
            "cta_heading":"→ book a <em>call</em>",
        },
    ],
}
