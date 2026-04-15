"""Phase 2g3.7 · Session 53 · Juris — EN native-voice tree. Advisory-modern tech boutique voice."""
from __future__ import annotations

from typing import Any


JURIS_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Home",        "kind": "home"},
        {"slug": "approccio",  "label": "Approach",    "kind": "about"},
        {"slug": "servizi",    "label": "Services",    "kind": "services"},
        {"slug": "settori",    "label": "Sectors",     "kind": "team"},
        {"slug": "insights",   "label": "Insights",    "kind": "blog_list"},
        {"slug": "contatti",   "label": "Contact",     "kind": "contact"},
    ],

    # Site-wide chrome
    "site": {
        "logo_initial": "M",
        "logo_word":    "Martini & Partners",
        "tag":          "Legal advisory · since 2018",
        "phone":        "hello@martinipartners.legal",
        "email":        "hello@martinipartners.legal",
        "address":      "Via Solferino 40 · 20121 Milan",
        "hours_compact":"Strategy call · Mon – Fri · 09:00 – 19:00",
        "hours_footer_rows": [
            "Video call from our dashboard",
            "Reply within 2 business hours",
        ],
        "license":      "Milan Bar no. MI18224 · VAT IT10123540967",
        "nav_cta":      "Book a strategy call",
        "footer_intro":
            "Martini & Partners is the firm that brings law, technology and "
            "strategy together for startups, SMEs and founders. Clear fees, "
            "defined timelines, a shared dashboard.",
        "foot_studio":  "The firm",
        "foot_pages":   "Pages",
        "foot_contact": "Contact",
        "foot_offices": "Offices",
        "offices_footer_rows": [
            "Milan · via Solferino 40",
            "Turin · via Roma 324",
            "Bologna · via Indipendenza 18",
        ],
        "post_date_label":    "Published",
        "post_reading_label": "Read time",
        "post_author_label":  "By",
        "post_topic_label":   "Practice",
        "post_back_label":    "All insights",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Martini & Partners · Milan · Turin · Bologna",
        "headline":    "The law, <em>on your side.</em>",
        "intro":
            "We partner with startups, SMEs and founders on the legal "
            "decisions that move the business — with clear timelines, "
            "transparent fees, and a shared dashboard where you track "
            "every step of your matter.",
        "primary_cta":    "Book a strategy call",
        "primary_href":   "contatti",
        "secondary_cta":  "How we work",
        "secondary_href": "approccio",

        "sprint_chip":     "Strategy call · Next slot · April 17",
        "sprint_chip_cta": "Book →",

        "sectors_label":   "Sectors",
        "sectors_heading": "Six practices, one <em>method</em>.",
        "sectors_intro":
            "Every practice is led by a partner + legal-ops pair. The first "
            "partner you speak to is the one who signs the engagement — "
            "no handoffs, no BDRs, no pitch decks.",
        "sectors": [
            ("01", "Startup & Tech",
             "Fundraising, cap table, IP, GDPR and AI Act compliance for digital companies."),
            ("02", "SMEs & Family businesses",
             "Generational transitions, governance, shareholder agreements and mid-market M&A."),
            ("03", "Employment & HR",
             "Contracts, dismissals, benefits, stock options and cross-border remote work."),
            ("04", "B2B contracts",
             "SaaS, licensing, partnerships, vendor due diligence and English-language MSAs."),
            ("05", "Dispute resolution",
             "Mediation, arbitration, ADR and strategic litigation."),
            ("06", "Privacy & AI",
             "GDPR, AI Act, data mapping, DPIA and policy for data-driven companies."),
        ],

        "process_label":   "How we work",
        "process_heading": "From brief to <em>first filing</em> in two weeks.",
        "process_intro":
            "We don't sell hours — we sell outcomes. The method is the same "
            "for every client, from the seed-stage startup closing its first "
            "round to the SME on its fourth engagement. Three steps, zero mystery.",
        "process": [
            ("S.01", "Discovery call",
             "30 minutes over video · we scope the problem, we don't pitch the service."),
            ("S.02", "Clear quote",
             "Timeline, phases, fixed or capped fee — all written, no surprises."),
            ("S.03", "Live dashboard",
             "Real-time view of filings, deadlines, documents and hours logged."),
        ],

        "metric_label":    "By the numbers",
        "metric_heading":  "Eight years on the ground, three cities, a hundred engagements a year.",
        "metric_strip": [
            ("180+", "companies advised"),
            ("14",   "days · median to first filing"),
            ("4.9",  "★ client satisfaction"),
            ("0",    "€ setup fee, always"),
        ],

        "trust_label": "We have advised in the last twelve months",
        "trust_logos": [
            "A MILAN FINTECH · SEED ROUND",
            "A VENETO FAMILY GROUP · GENERATIONAL TRANSITION",
            "A TURIN B2B SAAS · SERIES A",
            "A BOLOGNA SME · CROSS-BORDER M&A",
            "A ROME MARKETPLACE · AI POLICY",
            "A FLORENCE SCALE-UP · STOCK OPTIONS",
        ],

        "insights_label":   "Insights · this week",
        "insights_heading": "What we're reading <em>at the firm</em>.",
        "insights_intro":
            "The notes we write when a rule changes. Our clients read them "
            "with their morning coffee — no newsletter, no lead magnet, no drip "
            "sequence.",
        "insights_link":    "All insights →",
        "insights_link_href":"insights",
        "insights": [
            ("17 Apr", "AI Act: what changes for Italian SMEs",          "ai-act-pmi-italiane"),
            ("14 Apr", "Stock options 2026: new tax regime",             "stock-option-2026"),
            ("11 Apr", "Remote work across borders: three scenarios",    "smart-working-confine"),
        ],

        "cta_label":     "Ready to talk?",
        "cta_heading":   "Thirty minutes, over video, no obligation.",
        "cta_intro":
            "Your first call is with a partner, not a BDR. If the matter "
            "isn't in our practice area, we'll point you to the right firm — "
            "whether you ever work with us or not.",
        "cta_primary":      "Book a strategy call",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Read our method",
        "cta_secondary_href":"approccio",
    },

    # ─── APPROCCIO (about) ──────────────────────────────────────
    "approccio": {
        "eyebrow":  "Our method · 2018 — 2026",
        "headline": "We don't sell hours, <em>we sell outcomes.</em>",
        "intro":
            "We founded the firm in 2018 out of real frustration — two "
            "partners who had spent ten years inside Milan's international "
            "business-law firms and couldn't stand the hourly-billing model, "
            "the parked junior associates, and the 1990s-vintage legal "
            "dashboards any longer. We opened Martini & Partners to do it differently.",

        "manifesto_label":   "Manifesto",
        "manifesto_heading": "Four principles, <em>non-negotiable</em>.",
        "manifesto_intro":
            "We write them on page one of the engagement letter. They're not "
            "slogans, they're operating rules — break any of these four and "
            "we won't work with you (or you won't work with us).",
        "manifesto": [
            ("01", "The problem first, the fee later",
             "The discovery call is free. We write the quote only after we "
             "understand whether the problem is ours to solve and whether the "
             "solution is worth the fee. If it's not our field, we point you "
             "to the right firm — with no referral fee."),
            ("02", "Written fees, never hourly",
             "Every engagement has either a fixed fee or a hard cap. We only "
             "use hourly billing for unplannable emergencies — and we always "
             "flag it before we start. No surprise line items, no vague "
             "\"matter management\" entries."),
            ("03", "One partner, from the first filing to the last",
             "The partner you meet in discovery is the one who signs the "
             "final filing. The team rotates by specialization, never by "
             "seniority — you'll never find a junior associate you've never "
             "met working on your file without your prior approval."),
            ("04", "Shared dashboard, always",
             "Every client gets a dedicated workspace with matter status, "
             "documents, filed pleadings, hours logged, and the deadline "
             "timeline. We don't email PDFs — everything flows through the "
             "dashboard, always current, always exportable."),
        ],

        "story_label":   "The story",
        "story_heading": "Eight years, three cities, one method.",
        "story": [
            ("2018", "Founding in Milan",
             "Giorgia Martini (ex-DLA Piper) and Davide Romano (ex-Bird & Bird) "
             "open the firm on via Solferino with three engagements already "
             "signed from clients of their previous practices."),
            ("2020", "First internal dashboard",
             "We build the first version of the client dashboard with a "
             "product manager ex-Zalando. The idea of making it the "
             "signature of the Martini & Partners method is born here."),
            ("2022", "Turin desk opens",
             "We open the second office in Turin to stay close to scale-up "
             "engagements in Piedmont — today half of the firm's startup "
             "matters flow through that desk."),
            ("2024", "Bologna desk opens",
             "The third desk in Bologna covers the Emilia-Romagna corridor "
             "with a focus on family SMEs and mid-market M&A. In 2025 our "
             "first AI Act matters come out of this desk too."),
            ("2026", "Right-sized for the work",
             "Today we're eight lawyers and two legal ops. We have no plan "
             "to grow beyond — we'd rather pick our engagements than open "
             "a fourth office."),
        ],

        "dashboard_label":   "The client dashboard",
        "dashboard_heading": "Track your matter like you <em>track a deploy</em>.",
        "dashboard_intro":
            "Every client gets an encrypted workspace with their matters, "
            "documents, deadlines and the hours actually worked. Modeled on "
            "Linear more than on any legal portal — because we work for "
            "people who use Linear in their own job.",
        "dashboard_features": [
            ("Matter status",           "Every file has a kanban with status · owner · next deadline."),
            ("Versioned documents",     "Filed pleadings, drafts, exhibits — with history and inline comments."),
            ("Hours logged, in the open", "The hours of every partner and legal ops, updated every Friday evening."),
            ("Calendar deadlines",      "Every deadline is an event · sync it with your Google Calendar."),
            ("Finance export",          "One click for invoice + expense export for your accountant."),
            ("Shared access",           "Invite the CFO, the CEO, the accountant — with granular permissions."),
        ],
        "dashboard_mock": {
            "url":         "martini-partners.dashboard",
            "sidebar":     ["Matters", "Filings", "Hours", "Deadlines", "Team"],
            "sidebar_active_index": 0,
            "columns": [
                {"label": "Discovery",
                 "cards": [
                     {"title": "Fintech · seed",      "accent": False},
                     {"title": "SME · transition",    "accent": False},
                 ]},
                {"label": "Live",
                 "cards": [
                     {"title": "Scale-up · Series A", "accent": True},
                     {"title": "SaaS · MSA",          "accent": False},
                     {"title": "M&A · due diligence", "accent": False},
                 ]},
                {"label": "Closing",
                 "cards": [
                     {"title": "HR · stock options",  "accent": False},
                 ]},
            ],
        },

        "founders_label":   "Founders",
        "founders_heading": "Two lawyers, <em>one shared idea</em>.",
        "founders": [
            {
                "name":  "Avv. Giorgia Martini",
                "role":  "Managing partner · Startup & Tech",
                "bio":
                    "Twelve years at DLA Piper Milan, corporate department. "
                    "Closed two Series A rounds with Italian funds and one "
                    "cross-border round with Orange Ventures. Leads the "
                    "startup practice and the Milan desk.",
                "credentials": [
                    "Bocconi (Law '10)",
                    "LL.M. NYU '13",
                    "Member · Italian Tech Alliance",
                ],
            },
            {
                "name":  "Avv. Davide Romano",
                "role":  "Co-founder · B2B contracts",
                "bio":
                    "Ten years at Bird & Bird, tech & comms department. "
                    "Specialized in SaaS licensing, cross-border MSAs and "
                    "marketplace-platform contracts. Leads the Turin desk "
                    "and the AI Act practice.",
                "credentials": [
                    "Sapienza (Law '11)",
                    "LL.M. Fordham '14",
                    "Contributor · AIGA",
                ],
            },
        ],

        "offices_label": "The offices",
        "offices": [
            ("Milan",    "Via Solferino 40 · 20121 · Brera",          "Headquarters · every practice area"),
            ("Turin",    "Via Roma 324 · 10123 · Centro",             "Scale-up desk + Piedmont corridor"),
            ("Bologna",  "Via Indipendenza 18 · 40121 · Centro",      "SME desk + Emilia-Romagna corridor"),
        ],

        "cta_heading": "Want to see the dashboard live?",
        "cta_intro":
            "The discovery call includes a walkthrough of the client "
            "workspace. We'll show you what it looks like, what you can see, "
            "what you can export, and how we integrate with your stack "
            "(Notion, Slack, Google Workspace).",
        "cta_primary":      "Book the discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── SERVIZI (services) ─────────────────────────────────────
    "servizi": {
        "eyebrow":  "Services · 2026",
        "headline": "Seven offerings, <em>committed timelines</em>, stated prices.",
        "intro":
            "The seven service lines of the firm. Every offering has a "
            "written scope, an indicative timeline, and either a fixed or "
            "capped fee. No generic hourly rate card, no \"let's figure it "
            "out on the call\".",

        "svc_duration_label": "Duration",
        "svc_price_label":    "Price",
        "svc_deliverables_label": "What we deliver",
        "svc_engagement_label":   "Engagement",

        "services": [
            {
                "num":   "01",
                "title": "Startup Legal Sprint",
                "blurb":
                    "The entire legal setup for a startup closing its seed round "
                    "in three weeks — bylaws, shareholder agreement, term sheet, "
                    "investor onboarding and a clean cap table.",
                "deliverables": [
                    "Tailored bylaws and shareholder agreement",
                    "Term sheet and SAFE/convertible note review",
                    "Cap table maintained on Ledgy or Capdesk",
                    "Onboarding of first investors over video call",
                ],
                "duration":   "3 weeks",
                "price":      "€ 6,500 all-in",
                "engagement": "Fixed · 60% on kickoff · 40% on round closing",
                "tier":       "Seed-ready",
            },
            {
                "num":   "02",
                "title": "M&A Advisory · SMEs",
                "blurb":
                    "We advise family SMEs on strategic transactions — equity "
                    "sales, minority-fund entries, cross-border Italy-DACH M&A. "
                    "Vendor-side or buyer-side, never both in the same deal.",
                "deliverables": [
                    "Legal and tax due diligence",
                    "Valuation and SPA draft",
                    "Negotiation and closing support",
                    "Post-closing · 100-day integration",
                ],
                "duration":   "12 – 24 weeks depending on scope",
                "price":      "€ 45,000 base + 0.8% success fee",
                "engagement": "Mixed · fixed base + success fee at closing",
                "tier":       "Mid-market",
            },
            {
                "num":   "03",
                "title": "Contract-as-a-Service · B2B",
                "blurb":
                    "For SaaS and scale-ups signing MSAs every week — a "
                    "dedicated team runs drafting, negotiation and contract "
                    "archive. One Slack channel, 48-hour SLA, monthly retainer.",
                "deliverables": [
                    "Tailored MSA / DPA / SOW templates",
                    "Redline negotiation with counterparties",
                    "Contract archive on Notion or Juro",
                    "Monthly report with time and volume KPIs",
                ],
                "duration":   "Monthly retainer · 6-month minimum",
                "price":      "From € 3,200 / month",
                "engagement": "Recurring · Slack channel + dashboard",
                "tier":       "Scale-ready",
            },
            {
                "num":   "04",
                "title": "Privacy & AI Act Readiness",
                "blurb":
                    "Full GDPR audit + AI Act risk mapping for data-driven "
                    "companies. DPIA, records of processing, internal policies, "
                    "team training, and a readiness report for the board or investors.",
                "deliverables": [
                    "GDPR audit + updated records of processing",
                    "AI Act gap analysis and risk-class mapping",
                    "DPIA on critical processes (max 4)",
                    "Two-hour training for the operating team",
                ],
                "duration":   "6 weeks",
                "price":      "€ 12,500 all-in",
                "engagement": "Fixed · 50% on kickoff · 50% on report delivery",
                "tier":       "Compliance",
            },
            {
                "num":   "05",
                "title": "Stock Options & Benefits",
                "blurb":
                    "Design and implementation of stock-option plans for "
                    "startups and scale-ups — including the 2026 tax treatment "
                    "and employment-law profile for Italian and cross-border contracts.",
                "deliverables": [
                    "Custom-designed SO/SAR plan",
                    "Internal rules + employee onboarding",
                    "Documented 2026 tax treatment",
                    "Lock-up and tag-along agreements with funds",
                ],
                "duration":   "4 weeks",
                "price":      "€ 8,200 base + € 180 per onboarded employee",
                "engagement": "Fixed + per-seat on onboarding",
                "tier":       "Scale-ready",
            },
            {
                "num":   "06",
                "title": "Dispute Resolution",
                "blurb":
                    "Mediation, arbitration and strategic litigation — we "
                    "always favor a negotiated outcome, but when a case needs "
                    "to go to court we bring in dedicated counsel.",
                "deliverables": [
                    "Dispute assessment + strategy memo",
                    "Mediation or ADR attempt",
                    "Arbitration or civil-court representation",
                    "Weekly report on the state of the dispute",
                ],
                "duration":   "12 – 36 weeks depending on complexity",
                "price":      "Quote based on written scope",
                "engagement": "Mixed · phase fixed fee + success fee",
                "tier":       "Protection",
            },
            {
                "num":   "07",
                "title": "Fractional General Counsel",
                "blurb":
                    "A dedicated partner as part-time General Counsel for "
                    "scale-ups and SMEs that still need firm-grade counsel "
                    "without the cost of an in-house hire. Two to three days "
                    "a month, board presence included.",
                "deliverables": [
                    "On-site or video presence 2–3 days / month",
                    "Quarterly legal board book and risk dashboard",
                    "Key contracts + governance review",
                    "Escalation to every Martini & Partners desk",
                ],
                "duration":   "Quarterly retainer · 12-month minimum",
                "price":      "From € 5,400 / month",
                "engagement": "Recurring · board presence",
                "tier":       "Scale-ready",
            },
        ],

        "process_label":   "How we work",
        "process_heading": "From brief to first filing in two weeks.",
        "process": [
            ("S.01", "Discovery call",  "30 min video · scope and fit."),
            ("S.02", "Written quote",   "Within 5 days · fixed fees and timeline."),
            ("S.03", "Live dashboard",  "Kickoff in 48 hours · everything tracked."),
        ],

        "faq_label":   "Frequently asked",
        "faq_heading": "What you ask us on calls.",
        "faq": [
            ("Do you take engagements on variable success fees?",
             "Yes, but only on strategic transactions (M&A, fundraising, exit). "
             "On everything else we work on fixed fees or retainers."),
            ("How do you handle conflicts of interest?",
             "A conflict check is automated in the dashboard. We never accept "
             "two direct competitors in the same sector. The check runs before "
             "the discovery call, not after."),
            ("Do you work with freelancers and solo founders?",
             "Yes, but only on specific offerings — Stock Options, Privacy & AI, "
             "and B2B Contracts. For everything else we prefer companies with teams."),
            ("Can you sign an NDA up front?",
             "Yes — send us your standard NDA and we review it within 24 hours. "
             "Alternatively, we use our own mutual template, available inside "
             "the dashboard."),
        ],

        "cta_heading": "Not sure which offering is right for you?",
        "cta_intro":
            "Send us the scope and timeline — within 24 hours we'll point "
            "you to the right offering (or tell you this isn't our field). "
            "Free, no obligation, answer from a real partner.",
        "cta_primary":      "Send us the scope and timeline",
        "cta_primary_href": "contatti",
    },

    # ─── SETTORI ────────────────────────────────────────────────
    "settori": {
        "eyebrow":  "Sectors · where we move with ease",
        "headline": "Six sectors, <em>one method</em>, dedicated partners.",
        "intro":
            "Every sector has a lead partner and a supporting legal ops. "
            "\"Our sector\" isn't a marketing claim — it's the list of "
            "matters we've worked enough of to be certain we won't be "
            "learning on your file.",

        "sectors_label":   "The six practices",
        "sectors_heading": "Where we've <em>already solved</em> problems like yours.",

        "sectors": [
            {
                "num":   "01",
                "title": "Startup & Tech",
                "tagline": "For founders at round one or round three.",
                "pain_points": [
                    "Cap table and shareholder agreements that need tidying up",
                    "SAFE, convertible note or term sheet review before signing",
                    "Stock options with the correct 2026 tax treatment",
                    "GDPR + AI Act compliance before the investor pitch",
                ],
                "signals": [
                    "8 Series A closings in the last 24 months",
                    "3 exits managed on the vendor side",
                    "Lead partner · Avv. Giorgia Martini",
                ],
                "case_snippet":
                    "We advised a Milan fintech on its seed round with an "
                    "Italian fund + a UK business angel — clean cap table in "
                    "three weeks, closing in six.",
                "partner":    "Avv. Giorgia Martini",
                "legal_ops":  "Elena Vasile · legal ops lead",
            },
            {
                "num":   "02",
                "title": "SMEs & Family businesses",
                "tagline": "For second- or third-generation owners.",
                "pain_points": [
                    "Generational transition across multiple family branches",
                    "Outdated or missing shareholder agreements",
                    "Minority-fund entry into the capital structure",
                    "Governance with a still-informal board",
                ],
                "signals": [
                    "14 generational transitions closed since 2019",
                    "5 minority-fund entries into family SMEs",
                    "Lead partner · Avv. Chiara Belforte",
                ],
                "case_snippet":
                    "A Veneto family textile group asked us to handle the "
                    "transition to three brothers plus a second cousin — "
                    "shareholder agreement closed in twelve weeks, zero "
                    "estate disputes filed.",
                "partner":    "Avv. Chiara Belforte",
                "legal_ops":  "Matteo Orsi · legal ops",
            },
            {
                "num":   "03",
                "title": "Employment & HR",
                "tagline": "For HR teams that need to move fast.",
                "pain_points": [
                    "Individual or collective dismissal to run",
                    "Cross-border remote work (employees in EU or UK)",
                    "Restructuring with voluntary-exit packages",
                    "Stock options and benefits for scale-ups",
                ],
                "signals": [
                    "40+ individual dismissals closed in conciliation",
                    "12 voluntary-exit plans with zero litigation fallout",
                    "Lead partner · Avv. Sara Miccoli",
                ],
                "case_snippet":
                    "A Turin scale-up reduced headcount by 18% with no "
                    "pending litigation — using our individual-conciliation "
                    "method across 34 positions.",
                "partner":    "Avv. Sara Miccoli",
                "legal_ops":  "Luca Tagliavini · legal ops",
            },
            {
                "num":   "04",
                "title": "B2B contracts",
                "tagline": "For teams that sign MSAs every week.",
                "pain_points": [
                    "MSA / DPA / SOW to standardize",
                    "Redline negotiation with enterprise customers",
                    "SaaS licensing with US counterparties",
                    "Fragmented or non-existent contract archive",
                ],
                "signals": [
                    "Dedicated Slack channel · 48-hour SLA",
                    "Validated templates across 6 vertical sectors",
                    "Lead partner · Avv. Davide Romano",
                ],
                "case_snippet":
                    "A Turin B2B SaaS gave us the entire commercial "
                    "contracting function — since July 2024 we sign an "
                    "enterprise MSA every week with a median 8-day turn "
                    "from first draft to signing.",
                "partner":    "Avv. Davide Romano",
                "legal_ops":  "Alice Piatti · legal ops",
            },
            {
                "num":   "05",
                "title": "Dispute Resolution",
                "tagline": "For when a negotiation breaks down.",
                "pain_points": [
                    "Dispute with a supplier or enterprise customer",
                    "Arbitration under an international clause",
                    "Mandatory pre-litigation mediation",
                    "Reputational crisis management",
                ],
                "signals": [
                    "75% of disputes closed without judgment",
                    "4 ICC arbitrations handled in the last 24 months",
                    "Lead partner · Avv. Marco Trentini",
                ],
                "case_snippet":
                    "A Bologna SME with a €2.8 M dispute against a German "
                    "supplier — closed in mediation within 14 weeks with "
                    "a settlement more favorable than the original claim.",
                "partner":    "Avv. Marco Trentini",
                "legal_ops":  "Irene Bonomi · legal ops",
            },
            {
                "num":   "06",
                "title": "Privacy & AI",
                "tagline": "For companies working with data or models.",
                "pain_points": [
                    "GDPR audit ahead of a round or an M&A",
                    "AI Act gap analysis and risk-class mapping",
                    "DPIA on critical processes or predictive models",
                    "Data-breach response and Garante notification",
                ],
                "signals": [
                    "First Italian AI Act DPIA for a B2C marketplace",
                    "6 pre-M&A GDPR audits with zero deal impact",
                    "Lead partner · Avv. Giulia Masi",
                ],
                "case_snippet":
                    "A Rome marketplace brought its platform into AI Act "
                    "compliance ahead of the effective date — full mapping, "
                    "DPIA on 3 processes and a public policy ready, all in "
                    "6 weeks.",
                "partner":    "Avv. Giulia Masi",
                "legal_ops":  "Paolo Sangermano · legal ops",
            },
        ],

        "team_label":   "The full team",
        "team_heading": "Eight lawyers, <em>two legal ops</em>.",
        "team_intro":
            "The people of the firm — the names you'll find on the files "
            "and on every call. We have no junior-of-record: the seniors "
            "sit at the table from discovery to closing, the legal ops "
            "run the dashboard.",
        "team": [
            {"name": "Avv. Giorgia Martini",  "role": "Managing partner · Startup & Tech",        "office": "Milan",   "email": "giorgia@martinipartners.legal",
             "bio":  "12 years at DLA Piper · 2 Series A closed in 2025."},
            {"name": "Avv. Davide Romano",    "role": "Co-founder · B2B contracts",               "office": "Turin",   "email": "davide@martinipartners.legal",
             "bio":  "10 years at Bird & Bird · LL.M. Fordham · AIGA contributor."},
            {"name": "Avv. Chiara Belforte",  "role": "Partner · SMEs & Family",                  "office": "Bologna", "email": "chiara@martinipartners.legal",
             "bio":  "15 years at an Emilian family firm · Bocconi."},
            {"name": "Avv. Sara Miccoli",     "role": "Partner · Employment & HR",                "office": "Milan",   "email": "sara@martinipartners.legal",
             "bio":  "Former head of labour at a Milan boutique."},
            {"name": "Avv. Marco Trentini",   "role": "Partner · Dispute resolution",             "office": "Milan",   "email": "marco@martinipartners.legal",
             "bio":  "Specialized in ICC arbitration and commercial mediation."},
            {"name": "Avv. Giulia Masi",      "role": "Partner · Privacy & AI",                   "office": "Milan",   "email": "giulia@martinipartners.legal",
             "bio":  "Ex Italian Data Protection Authority · PhD in AI ethics."},
            {"name": "Avv. Tommaso Neri",     "role": "Senior associate · Startup & M&A",         "office": "Turin",   "email": "tommaso@martinipartners.legal",
             "bio":  "6 years at a Milan M&A boutique · focus on tech scale-ups."},
            {"name": "Avv. Beatrice Riva",    "role": "Senior associate · Contract-as-a-Service", "office": "Turin",   "email": "beatrice@martinipartners.legal",
             "bio":  "Specialized in cross-border SaaS licensing · IAPP CIPP/E."},
            {"name": "Elena Vasile",          "role": "Legal ops lead",                           "office": "Milan",   "email": "elena@martinipartners.legal",
             "bio":  "Former operations manager at a logistics scale-up · designs the dashboard flows."},
            {"name": "Matteo Orsi",           "role": "Legal ops · SME desk",                     "office": "Bologna", "email": "matteo@martinipartners.legal",
             "bio":  "Former paralegal at a Bologna tax firm · matter-archive specialist."},
        ],

        "cta_heading": "Your sector isn't on the list?",
        "cta_intro":
            "We do get matters outside our six sectors — we take them only "
            "if we have direct experience or if we co-work with a partner "
            "firm. Tell us the scope: within 24 hours we'll tell you if "
            "it's our field.",
        "cta_primary":      "Tell us about the matter",
        "cta_primary_href": "contatti",
    },

    # ─── INSIGHTS ───────────────────────────────────────────────
    "insights": {
        "eyebrow":  "Insights · 2026",
        "headline": "When a rule changes, <em>we write a note</em>.",
        "intro":
            "We don't run a newsletter. We don't run marketing sequences. "
            "When a rule changes or a case lands on the desk, someone at "
            "the firm writes a note — we publish it here because our "
            "clients ask for it, and our candidates read it before the "
            "interview.",

        "card_topic_label":   "Practice",
        "card_author_label":  "By",
        "card_reading_label": "Read time",

        "posts_intro":
            "Six recent notes. The full archive is on the client dashboard "
            "— here we publish only the ones of public interest.",

        "topics_label": "Practices",
        "topics":       ["All", "Startup & Tech", "Employment & HR", "Privacy & AI", "M&A", "Dispute"],

        "cta_heading": "Want our notes first?",
        "cta_intro":
            "Clients of the firm get the notes on the dashboard before "
            "public release. If that's relevant, book a discovery call — "
            "we'll show you how it works.",
        "cta_primary":      "Book a strategy call",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Strategy call",
        "headline": "Thirty minutes, over video, <em>no obligation</em>.",
        "intro":
            "Your first contact is with a partner, not a BDR. We scope the "
            "matter, the timeline, and any conflict of interest — before "
            "any fee discussion. Free, no obligation, answer from a real partner.",

        "slot_label": "Next available slot",
        "slot_value": "Thursday April 17 · 10:30",
        "slot_note":  "The call happens from the client dashboard · no Zoom account required",

        "form_label":   "Book the call",
        "form_heading": "Three steps, two minutes, one conversation.",
        "form_intro":
            "Information is processed under EU Reg. 679/2016 and kept on "
            "our encrypted dashboard with partner-only access. No third-party CRM.",
        "form_fields": [
            {"name": "name",      "label": "First name",     "type": "text",     "required": True,  "placeholder": "e.g. Giorgia",
             "helper": "Just the first name, thank you."},
            {"name": "surname",   "label": "Last name",      "type": "text",     "required": True,  "placeholder": "e.g. Rossi",
             "helper": "As it appears in your corporate documents."},
            {"name": "email",     "label": "Email",          "type": "email",    "required": True,  "placeholder": "giorgia@company.com",
             "helper": "Consumer domains are fine — we're not a 20th-century business-law firm."},
            {"name": "phone",     "label": "Phone",          "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Optional. Used only if the call falls through."},
            {"name": "company",   "label": "Company or firm","type": "text",     "required": True,  "placeholder": "e.g. Acme S.r.l.",
             "helper": "The registered or trading name."},
            {"name": "company_type", "label": "Company type","type": "select",   "required": True,
             "options": [
                 "Startup (pre-seed)",
                 "Startup (seed)",
                 "Scale-up (Series A or beyond)",
                 "SME / family business",
                 "Mature scale-up / corporate",
                 "Solo founder or freelancer",
                 "Other",
             ],
             "helper": "Helps us check whether you fit our practice."},
            {"name": "stage",      "label": "Stage",             "type": "select", "required": True,
             "options": [
                 "Still in internal discussion",
                 "Ready to start within a month",
                 "Ready to start within three months",
                 "Exploratory, no urgency",
             ],
             "helper": "Helps us book the right partner for your matter."},
            {"name": "help_type",  "label": "Type of support",   "type": "select", "required": True,
             "options": [
                 "Not sure yet · let's scope on the call",
                 "B2B contracts",
                 "Startup legal sprint / fundraising",
                 "M&A or generational transition",
                 "Employment, HR, stock options",
                 "Privacy, GDPR, AI Act",
                 "Dispute or litigation",
                 "Fractional General Counsel",
             ],
             "helper": "Pick \"Not sure yet\" if the scope spans multiple areas."},
            {"name": "message",   "label": "Tell us about the matter", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Max 600 characters. No counterparty names or sensitive data yet — we'll get there on the call after mutual NDA.",
             "helper": "Just enough to see if it's our field. "
                       "Counterparty names are shared only after mutual NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Who you are",
             "meta": "The person we'll speak to on the call.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "What you do",
             "meta": "For the preliminary conflict check.",
             "fields": ["company", "company_type", "stage"]},
            {"num": "03", "title": "What you need",
             "meta": "No sensitive detail here — we go into the substance only after mutual NDA.",
             "fields": ["help_type", "message"]},
        ],

        "form_submit_label": "Book the strategy call",
        "form_submit_note":
            "Answer from a real partner within 2 business hours. "
            "No BDR, no sequence, no \"someone will be in touch shortly\".",
        "form_consent":
            "I consent to the processing of my personal data under EU "
            "Regulation 679/2016. The data is kept on the firm's encrypted "
            "dashboard with partner-only access. No data is shared with "
            "third parties without explicit authorization.",

        "office_address_label": "Address",
        "office_area_label":    "Neighborhood",
        "office_phone_label":   "Phone",
        "office_email_label":   "Email",

        "offices_label": "The three offices",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Headquarters",
                "address": "Via Solferino 40 · 20121",
                "area":    "Brera · two steps from Piazza della Scala",
                "phone":   "+39 02 4546 7789",
                "email":   "milano@martinipartners.legal",
                "note":    "Every practice area · meeting rooms bookable from the dashboard",
            },
            {
                "city":    "Turin",
                "tag":     "Scale-up desk",
                "address": "Via Roma 324 · 10123",
                "area":    "Centro · close to Piazza Castello",
                "phone":   "+39 011 5667 2240",
                "email":   "torino@martinipartners.legal",
                "note":    "Tech scale-up desk · main contract-as-a-service office",
            },
            {
                "city":    "Bologna",
                "tag":     "SME desk",
                "address": "Via Indipendenza 18 · 40121",
                "area":    "Centro · close to Piazza Maggiore",
                "phone":   "+39 051 3344 8812",
                "email":   "bologna@martinipartners.legal",
                "note":    "SME and mid-market M&A desk · Emilia-Romagna corridor",
            },
        ],

        "channels_label": "Direct channels",
        "channels": [
            ("General email",      "hello@martinipartners.legal", "Answer within 2 business hours"),
            ("Milan switchboard",  "+39 02 4546 7789",            "Mon – Fri · 09:00 – 19:00"),
            ("Company LinkedIn",   "in/martini-partners",         "Public notes and weekly AMAs"),
        ],

        "footnote":
            "Martini & Partners does not do cold outreach. If someone "
            "contacts you as a BDR on our behalf, it isn't us. Every "
            "relationship starts from a referral, from a note of ours "
            "someone has read, or from this form.",
    },

    # ─── POSTS ──────────────────────────────────────────────────
    "posts": [
        {
            "slug":     "ai-act-pmi-italiane",
            "title":    "AI Act: what changes for Italian SMEs",
            "topic":    "Privacy & AI",
            "date":     "April 17, 2026",
            "reading":  "8 min",
            "author":   "Avv. Giulia Masi",
            "lead":
                "The AI Act enters into effective force on August 2, 2026 "
                "for high-risk systems. For Italian SMEs running predictive "
                "models in production — marketplaces, customer scoring, "
                "HR tech — the window to comply is four months. Here's how "
                "we're doing it with our clients.",
            "sections": [
                {
                    "heading": "Why it touches SMEs too",
                    "body":
                        "The common read is that the AI Act only hits the "
                        "giants — OpenAI, Mistral, Meta. That's wrong. The "
                        "directive classifies by use, not by the size of "
                        "the building company. A homegrown credit-scoring "
                        "algorithm from a seed-stage fintech falls into the "
                        "high-risk class just like one from a tier-one "
                        "investment bank — and the SME has fewer resources "
                        "to comply.",
                },
                {
                    "heading": "The four risk classes",
                    "body":
                        "Unacceptable risk (prohibited), high risk (strict "
                        "requirements), limited risk (mandatory transparency), "
                        "minimal risk (no specific obligations). Mapping "
                        "company systems into the four classes is the first "
                        "step — and for SMEs it takes about two weeks of "
                        "work with a legal ops + a product manager.",
                },
                {
                    "heading": "What to do now",
                    "body":
                        "Three concrete actions: a full inventory of AI "
                        "systems in production (including third-party "
                        "plug-ins like chatbots or recommendation engines), "
                        "an integrated DPIA for the high-risk systems, and "
                        "a public-facing policy that discloses AI use in "
                        "decision processes touching customers or employees. "
                        "For most SMEs this is a six-week project — our AI "
                        "Act Readiness offering covers it end-to-end.",
                },
            ],
            "takeaway":
                "The AI Act isn't a compliance checkbox — it's an "
                "opportunity to tidy up the systems that touch customer "
                "or employee data. The companies that get it right today "
                "sell better tomorrow.",
            "tags":     ["AI Act", "GDPR", "Compliance", "SMEs"],
        },
        {
            "slug":     "stock-option-2026",
            "title":    "Stock options 2026: new tax regime",
            "topic":    "Startup & Tech",
            "date":     "April 14, 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "Italy's 2026 Budget Law changed the tax treatment of "
                "stock-option plans for innovative startups and SMEs. The "
                "change is favorable — but the drafting leaves room for "
                "interpretation. Here's how we're setting up new plans "
                "and what to do with the existing ones.",
            "sections": [
                {
                    "heading": "What changes from January 1, 2026",
                    "body":
                        "Taxation now hits at the point of actual share "
                        "sale (no longer at vesting) for innovative startups "
                        "registered with the special registry. Capital-gains "
                        "rate stays at 26%. It's a material change: it "
                        "resolves the paradox of the employee paying tax "
                        "on shares they haven't monetized yet.",
                },
                {
                    "heading": "Do existing plans need to be rewritten?",
                    "body":
                        "Not necessarily. The new regime applies automatically "
                        "to plans that meet the requirements — innovative-"
                        "startup registration, minimum 24-month vesting, "
                        "awards to employees or directors in continuing "
                        "employment. Most recent plans are already compatible. "
                        "Plans written before 2022, however, almost always "
                        "need an update.",
                },
                {
                    "heading": "How to set up new plans",
                    "body":
                        "Three things to get right: draft the internal "
                        "rules with an explicit reference to the 2026 "
                        "regime, document the award date and the individual "
                        "vesting schedule for every employee, and give "
                        "employees a plain-English tax guide at the time "
                        "of the award. Our SO/SAR plan template is already updated.",
                },
            ],
            "takeaway":
                "For innovative startups the new regime is a clear "
                "simplification — and one more argument to bring a senior "
                "hire across from a large company into your founder team.",
            "tags":     ["Stock options", "Startup", "Tax", "HR"],
        },
        {
            "slug":     "smart-working-confine",
            "title":    "Remote work across borders: three scenarios",
            "topic":    "Employment & HR",
            "date":     "April 11, 2026",
            "reading":  "7 min",
            "author":   "Avv. Sara Miccoli",
            "lead":
                "Since 2023 most Italian companies have accepted cross-"
                "border remote work — but the rules on social-security "
                "contributions, tax withholding and applicable-labor-law "
                "jurisdiction remain messy. Three typical scenarios we see every month.",
            "sections": [
                {
                    "heading": "Scenario 1 · Italian employee relocating to Spain",
                    "body":
                        "If the employee works more than 183 days a year "
                        "in Spain, they become Spanish tax resident — the "
                        "Italian company has to pay Spanish Social Security "
                        "contributions (bilateral convention) and Spanish "
                        "IRPF withholding. The law of the employment "
                        "contract can remain Italian if expressly stipulated, "
                        "but minimum Spanish rights (leave, dismissal) apply anyway.",
                },
                {
                    "heading": "Scenario 2 · EU employee relocating to Italy",
                    "body":
                        "Simpler but not trivial. The company becomes an "
                        "Italian tax withholding agent, opens an INPS "
                        "position and pays Italian contributions. If the "
                        "employee has an original French or German contract, "
                        "renegotiation is needed — many companies choose "
                        "to issue a new Italian contract with a continuity "
                        "clause.",
                },
                {
                    "heading": "Scenario 3 · Italian employee relocating outside the EU",
                    "body":
                        "The most delicate. Without an adequate bilateral "
                        "convention (e.g. USA, Canada), there's a risk of "
                        "double taxation and double social-security "
                        "contributions. The clean solution is almost always "
                        "a local contract with a foreign entity (subsidiary "
                        "or PEO / EOR) — keeping the Italian contract "
                        "under a long-term assignment is only sustainable "
                        "for 18–24 months at most.",
                },
            ],
            "takeaway":
                "Before you say yes to a cross-border remote-work request, "
                "always verify the destination country. The rules change "
                "between EU, UK, USA and the rest of the world — and the "
                "cost to the company can swing by 30% between scenarios.",
            "tags":     ["Remote work", "HR", "Cross-border", "Employment"],
        },
        {
            "slug":     "contratti-saas-enterprise",
            "title":    "Enterprise SaaS contracts: three clauses that shouldn't be missing",
            "topic":    "B2B contracts",
            "date":     "April 8, 2026",
            "reading":  "5 min",
            "author":   "Avv. Davide Romano",
            "lead":
                "After signing more than three hundred enterprise SaaS "
                "MSAs in the last three years, we keep a mental checklist "
                "of clauses that should never be missing. Three we always "
                "recommend, even when the client has \"never seen them before\".",
            "sections": [
                {
                    "heading": "1. Liability cap proportional to and no less than 12 months of fees",
                    "body":
                        "The standard liability cap from the big vendors "
                        "(Salesforce, ServiceNow) is typically 12 months "
                        "of service fees. Accepting it is reasonable · "
                        "negotiating down to 3 or 6 months is often "
                        "possible for deals under €500K.",
                },
                {
                    "heading": "2. Data portability and export clause",
                    "body":
                        "The right to export all data in a machine-readable "
                        "format within 30 days of termination, at no extra "
                        "cost. Often absent, almost always negotiable.",
                },
                {
                    "heading": "3. Sub-processor notice period",
                    "body":
                        "The right to be notified at least 30 days before "
                        "a sub-processor change (hosting, email, analytics) "
                        "— with an opt-out right with no penalty if the "
                        "new sub-processor doesn't meet the agreed standards.",
                },
            ],
            "takeaway":
                "These three clauses land in 70% of the enterprise "
                "contracts we sign — the remaining 30% accept them when "
                "you ask with clean drafting. We have a template ready on the dashboard.",
            "tags":     ["SaaS", "Contracts", "Enterprise", "B2B"],
        },
        {
            "slug":     "mandati-m-and-a-2025",
            "title":    "Mid-market M&A: what we learned in 2025",
            "topic":    "M&A",
            "date":     "April 4, 2026",
            "reading":  "9 min",
            "author":   "Avv. Chiara Belforte",
            "lead":
                "In 2025 we closed seven mid-market M&A transactions — "
                "three vendor-side, four buyer-side, five domestic Italian "
                "and two cross-border. Three trends we saw often enough to "
                "deserve a note.",
            "sections": [
                {
                    "heading": "Earn-outs are back",
                    "body":
                        "After two years in which deals closed at a fixed "
                        "price with a founder exit at 6–12 months, in 2025 "
                        "the earn-out came back. Mid-market included. "
                        "Typically 25–35% of the price tied to post-closing "
                        "operational KPIs, 24–36 months duration. For the "
                        "founder it's an opportunity but it needs a "
                        "well-drafted earn-out contract to avoid disputes.",
                },
                {
                    "heading": "AI/privacy due diligence is now standard",
                    "body":
                        "Even the most classic fund now asks for a GDPR "
                        "compliance summary and a map of AI systems before "
                        "signing. A preventive vendor-side audit costs "
                        "€5–10K and saves you 2–3 weeks on the process.",
                },
                {
                    "heading": "Cross-border signings need more time",
                    "body":
                        "The two Italy-DACH transactions of 2025 took on "
                        "average 8 weeks longer than pure Italian signings "
                        "— between certified deed translation, antitrust "
                        "approval and German notary coordination. Plan for "
                        "it from day one rather than discovering it at DD.",
                },
            ],
            "takeaway":
                "2025 normalized the earn-out and made AI/privacy "
                "due diligence standard. On cross-border, better to "
                "overplan on time than stress the closing.",
            "tags":     ["M&A", "Funds", "Due diligence", "Cross-border"],
        },
        {
            "slug":     "dashboard-cliente-perche",
            "title":    "Why we built a client dashboard (instead of buying one)",
            "topic":    "Startup & Tech",
            "date":     "March 28, 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "In 2020 we evaluated Clio, MyCase, PracticePanther and "
                "six other \"practice management\" software products for "
                "law firms. None convinced us. We built our own — "
                "internally, with a part-time product manager. Here's "
                "why, and what we learned.",
            "sections": [
                {
                    "heading": "The problem with standard legal PM tools",
                    "body":
                        "Practice-management software for law firms is "
                        "built for 50+ person firms billing by the hour. "
                        "The UX is designed for assistants and lawyers "
                        "filling timesheets. We're ten people, we don't "
                        "bill by the hour, and our clients are product "
                        "managers used to Linear. Incompatible.",
                },
                {
                    "heading": "What we built",
                    "body":
                        "A Linear + Notion-style workspace with kanban "
                        "boards for matters, an encrypted document archive, "
                        "a shared deadline calendar and a chat channel for "
                        "every file. No timesheets — hours are logged at "
                        "week's end, in the open for the client. Six "
                        "months of development, cost €80K, today everyone uses it.",
                },
                {
                    "heading": "Why it became a commercial advantage",
                    "body":
                        "We discovered after the fact that the dashboard "
                        "is the first reason clients choose us. In pitches "
                        "we show a two-minute walkthrough of the real "
                        "workspace — and for companies used to Linear + "
                        "Notion it's a game-changer compared to the "
                        "email-PDFs of other firms.",
                },
            ],
            "takeaway":
                "Do the thing others won't. The dashboard was the most "
                "important investment of our first eight years — more "
                "than any new office or new hire.",
            "tags":     ["Dashboard", "Product", "Firm", "Tooling"],
        },
    ],
}

# D-047 compliance note:
# English locale tree · same shape as JURIS_CONTENT_IT. The skin files
# never author any English literal — every user-facing string in EN
# flows through this file.
