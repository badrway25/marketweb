"""Pragma — Corporate Suite · English content tree.

Mirrors the shape of ``PRAGMA_CONTENT_IT`` exactly — same keys, nesting and
list shapes. Authored for the live i18n rollout of the corporate-suite
archetype (institutional B2B advisory boutique, Milan · Frankfurt · Zürich).

Voice register: Anglo-American institutional advisory (FT · HBR · McKinsey
Quarterly · Bain case studies). Sober, boardroom-grade, formal. Never
startup-tech, never SaaS idiom.
"""
from __future__ import annotations

from typing import Any


PRAGMA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Studio",        "kind": "home"},
        {"slug": "chi-siamo",     "label": "About",         "kind": "about"},
        {"slug": "competenze",    "label": "Practices",     "kind": "services"},
        {"slug": "case-studies",  "label": "Case studies",  "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contact",       "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pragma Advisors",
        "tag":          "Corporate advisory · Milan",
        "phone":        "+39 02 3611 9900",
        "email":        "segreteria@pragmaadvisors.it",
        "address":      "Via Filodrammatici 10 · 20121 Milan",
        "hours_compact":"Mon – Fri · 9:00 – 19:00 · by appointment",
        "hours_footer_rows": [
            "Saturday · scheduled board calls only",
            "Sunday · closed",
        ],
        "license":      "CONSOB Independent Advisors registry no. 1148/2009",
        "footer_intro":
            "Independent advisory boutique for the chief executives and "
            "boards of established mid-cap companies. Strategy, M&A, "
            "governance and ESG. Headquartered in Milan, with permanent "
            "desks in Frankfurt and Zürich.",
        # Footer column headings — per-template (not shared chrome)
        "foot_studio":   "The firm",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Offices",
        "offices_footer_rows": [
            "Milan · Porta Nuova",
            "Frankfurt am Main · Bockenheim",
            "Zürich · Paradeplatz",
        ],
        # Case study cross-page meta labels
        "case_practice_label":     "Practice",
        "case_year_label":         "Year",
        "case_duration_label":     "Duration",
        "case_lead_label":         "Lead",
        "case_lead_partner_label": "Lead partner",
        "case_team_label":         "Team & timeline",
        "case_timeline_label":     "Timeline",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Corporate advisory · Milan · Frankfurt · Zürich",
        "headline":    "Where the decisions <em>that matter</em> are made.",
        "intro":
            "We partner with the chief executives and boards of established "
            "mid-cap companies on their structural decisions — three-year "
            "industrial plans, M&A transactions, governance frameworks and "
            "ESG trajectories. An independent boutique, twenty-two years "
            "of confidential engagements.",
        "primary_cta":   "Request a private call",
        "primary_href":  "contatti",
        "secondary_cta": "Download the firm dossier",
        "secondary_href":"chi-siamo",

        # Right-hand boardroom photo + credit overlay
        "hero_image":              "https://images.pexels.com/photos/6950031/pexels-photo-6950031.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "hero_image_credit_left":  ("Photography",      "Lombard Industrial Board · 2025"),
        "hero_image_credit_right": ("Founded",          "2004"),
        "hero_meta_strip": [
            ("Headquarters",     "Milan · Porta Nuova"),
            ("Senior partners",  "14 partners"),
            ("Active mandates",  "42 engagements"),
        ],

        # Advisory pillars — three-practice grid
        "pillars_label":   "Practice",
        "pillars_heading": "Three disciplines, one signature",
        "pillars_intro":
            "A single multidisciplinary team serves every mandate. Our "
            "partners do not sell — they sit at the table from the first "
            "brief to the signed engagement letter.",
        "pillars": [
            ("01", "Board advisory",
             "We counsel boards and chief executives through step-change "
             "decisions — three-year industrial plans, shareholder "
             "reorganisations, family successions and reputational crisis "
             "management."),
            ("02", "Growth & M&A",
             "Due diligence, valuation, negotiation and post-deal integration "
             "in 10 – 12 weeks, with sector-dedicated teams. We act either "
             "vendor-side or buyer-side, never both on the same dossier."),
            ("03", "Governance & ESG",
             "CSRD compliance, integrated reporting, 231 organisational "
             "models, board-committee architecture and sustainability "
             "policies for listed industrial groups and regulated "
             "financial-services firms."),
        ],

        # KPI strip on dark navy band
        "kpi_heading": "Twenty-two years of confidential engagements",
        "kpi_strip": [
            ("22",      "years in practice"),
            ("180+",    "engagements closed"),
            ("€ 1.4 B", "transacted value"),
            ("94%",     "repeat-engagement rate"),
        ],

        # Sectors ribbon
        "sectors_label": "Sectors served",
        "sectors": [
            "Industry & manufacturing",
            "Financial services",
            "Energy & utilities",
            "Retail & consumer",
            "Healthcare & pharma",
        ],

        # Trust band — institutional client logos as text wordmarks
        "trust_label":   "Clients who have chosen Pragma in the last five years",
        "trust_logos":   [
            "BRESCIA INDUSTRIAL GROUP",
            "ITALY MEZZANINE FUND",
            "TURIN BIOTECH",
            "EMILIA AGRICULTURAL BANK",
            "NORTHERN RENEWABLE ENERGY",
            "TUSCAN FAMILY RETAIL",
        ],

        # Leadership preview — three managing partners on home
        "leadership_label":   "Leadership",
        "leadership_heading": "The partners who will sit at your table",
        "leadership_intro":
            "Every mandate is led personally by at least one managing "
            "partner. No stand-in executives, no parked juniors.",
        "leadership": [
            {
                "name":  "Dr. Federico Seregni",
                "role":  "Managing partner · Board advisory",
                "bio":
                    "Twenty years at McKinsey & Company as a senior partner in the "
                    "industrial practice. Independent director on three listed boards. "
                    "Specialises in industrial plans and family successions within "
                    "Italian manufacturing.",
                "credentials": [
                    "Bocconi (CLEACC '95)",
                    "Insead MBA '01",
                    "Board member, Confindustria Lombardia",
                ],
            },
            {
                "name":  "Avv. Caterina Foschini",
                "role":  "Managing partner · Growth & M&A",
                "bio":
                    "Over 70 M&A transactions closed between Italy and the DACH "
                    "region. Formerly at Bonelli Erede, she led two strategic exits "
                    "in the Italian consumer private-equity segment.",
                "credentials": [
                    "Cattolica (Law '98)",
                    "LL.M. Frankfurt am Main",
                    "AIDC, IBA M&A Forum",
                ],
            },
            {
                "name":  "Eng. Marco Lavezzi",
                "role":  "Managing partner · Governance & ESG",
                "bio":
                    "Former head of sustainability at a listed utility group. "
                    "Coordinates CSRD engagements, integrated reporting and 231 "
                    "models for the firm's governance practice clients.",
                "credentials": [
                    "Politecnico Milano (Management Eng. '02)",
                    "Certified GRI · CDP",
                    "Member, CASUR-ANRI",
                ],
            },
        ],

        # Case studies preview — three on home, full list on /case-studies
        "cases_label":   "Recent work",
        "cases_heading": "Three mandates, three directions",
        "cases_intro":
            "A recent selection of closed engagements. For reasons of "
            "confidentiality, client names are disclosed only under NDA.",

        # Final CTA band before footer
        "cta_label":     "A preliminary conversation",
        "cta_heading":   "Thirty minutes, narrow agenda, no commitment",
        "cta_intro":
            "The first call is always with a senior partner. We discuss "
            "the perimeter, the timeline and any conflict of interest — "
            "before any commercial proposal is issued.",
        "cta_primary":   "Request the call",
        "cta_primary_href": "contatti",
        "cta_secondary": "Download the firm dossier",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "The firm · 2004 — 2026",
        "headline":  "An <em>independent</em> boutique, twenty-two years of confidential mandates.",
        "intro":
            "Pragma Advisors was founded in Milan in 2004 by a group of "
            "professionals with consulting, financial and legal backgrounds. "
            "We have grown by cooptation — never by acquisition — and have "
            "preserved our independence from third-party capital from day one.",

        # Studio history — 5-step timeline
        "history_label":   "Studio history",
        "history_heading": "Five milestones, twenty-two years",
        "history_intro":
            "Five dates that defined Pragma. Behind each of these "
            "milestones lies a structural choice — on independence, "
            "on geography, on practice — that still guides how we "
            "accept a mandate today.",
        "history": [
            ("2004", "Foundation",
             "Federico Seregni and three partners open Pragma in Via Filodrammatici, "
             "with four board-advisory mandates already signed."),
            ("2009", "CONSOB Independent Advisors registry",
             "Listing in the Italian register of independent financial advisors — "
             "the M&A practice is now able to act as a formal advisor of record."),
            ("2014", "Frankfurt office opens",
             "Caterina Foschini leads the opening of the DACH office, dedicated "
             "to cross-border Italy-Germany manufacturing mandates."),
            ("2019", "Governance & ESG practice launches",
             "Marco Lavezzi joins as managing partner to build the ESG practice, "
             "with the first CSRD mandates from two utility groups."),
            ("2024", "Zürich office opens",
             "To serve the wealth-structuring mandates of Italian entrepreneurial "
             "families, we open our Paradeplatz office."),
        ],

        # Method / values
        "values_label":   "Method",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "These are the four rules that separate a Pragma mandate "
            "from a standard strategic-consulting engagement. You will "
            "find them written on the letterhead of every signed "
            "engagement — not in marketing copy.",
        "values": [
            ("01", "Independence from external capital",
             "The firm's equity is held entirely by active partners. No "
             "corporate shareholder, no minority private-equity investor, "
             "no external capital of any kind. The selection of a mandate "
             "is never influenced by a third party's agenda."),
            ("02", "One partner per mandate",
             "A managing partner sits at the table from the opening of the "
             "file through the closing signature. No partner-of-record who "
             "disappears after the pitch — the senior advisor you meet on "
             "the first call is the one who will sign the engagement's close."),
            ("03", "No conflicts, ever",
             "We never advise two direct competitors in the same sector. On "
             "an M&A transaction, we never act for vendor and acquirer on "
             "the same dossier. Our internal Compliance Officer clears every "
             "new mandate before acceptance."),
            ("04", "Transparent fees",
             "Daily rate disclosed in the proposal, success fees only on "
             "extraordinary transactions and always itemised on the invoice. "
             "No commission clawbacks, no verbal arrangements with financial "
             "counterparties."),
        ],

        # Full team — 6 senior advisors + the 3 managing partners
        "team_label":   "Senior partners",
        "team_heading": "Fourteen partners, three offices, one governance",
        "team_intro":
            "The people who will work on your mandate. Our partners are "
            "not consultants, and we do not hand you off to a department — "
            "they sit at the table from start to finish.",
        "team": [
            {"name": "Dr. Federico Seregni",
             "role": "Managing partner · Board advisory",
             "office": "Milan",
             "bio": "Former senior partner at McKinsey, twenty years of industrial "
                    "plans. Independent director on three listed boards."},
            {"name": "Avv. Caterina Foschini",
             "role": "Managing partner · M&A",
             "office": "Frankfurt",
             "bio": "70+ transactions closed between Italy and the DACH region. "
                    "Formerly at Bonelli Erede, specialised in cross-border consumer."},
            {"name": "Eng. Marco Lavezzi",
             "role": "Managing partner · Governance & ESG",
             "office": "Milan",
             "bio": "Leads the CSRD and 231 model practice. Former head of "
                    "sustainability at a listed utility group."},
            {"name": "Dr. Sabina Erlanger",
             "role": "Senior partner · Wealth structuring",
             "office": "Zürich",
             "bio": "Twenty years in Swiss private banking. Leads the "
                    "generational-transfer mandates for Italian entrepreneurial families."},
            {"name": "Dr. Lorenzo Pellizzari",
             "role": "Senior partner · Industry & manufacturing",
             "office": "Milan",
             "bio": "Former chief executive of a Brescia-based metalworking group. "
                    "Strategic practice for the Lombardy and Veneto supply chains."},
            {"name": "Dr. Giulia Antinori",
             "role": "Senior partner · Financial services",
             "office": "Milan",
             "bio": "Formerly McKinsey financial services. Transformation mandates "
                    "for Italian regional banks and asset managers."},
        ],

        # Coordinates strip
        "coordinates_label": "Our offices",
        "coordinates": [
            ("Milan",      "Via Filodrammatici 10 · 20121 · Porta Nuova"),
            ("Frankfurt",  "Bockenheimer Landstr. 51 · 60325 · Westend"),
            ("Zürich",     "Paradeplatz 8 · 8001 · Innenstadt"),
        ],

        # Page-level CTA
        "cta_heading": "A confidential preliminary assessment",
        "cta_intro":
            "The first thirty minutes with a partner are an exploratory "
            "conversation, not a commercial proposal. We discuss the "
            "perimeter of the mandate, the timeline and any conflict of "
            "interest.",
        "cta_primary":  "Request the call",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Practice areas · 2026",
        "headline": "Six practices, <em>one signature</em>.",
        "intro":
            "Pragma's six practices. Every client engages a multidisciplinary "
            "team — we do not bill each practice separately, the mandate "
            "covers the combination of disciplines the engagement requires.",

        # Card meta labels
        "svc_duration_label": "Duration",
        "svc_leader_label":   "Lead partner",

        # 6 services in airy cards
        "services": [
            {
                "num":   "01",
                "title": "Board advisory",
                "blurb":
                    "We counsel boards and chief executives through step-change decisions. "
                    "Three-year industrial plans, shareholder restructurings, family "
                    "successions, reputational crisis management and interim mandates.",
                "scope": [
                    "Industrial plans and strategic review",
                    "Family succession and governance",
                    "Interim CFO / COO mandates",
                    "Crisis communication to the board",
                ],
                "duration": "8 – 14 weeks per cycle",
                "leader":   "Dr. Federico Seregni",
            },
            {
                "num":   "02",
                "title": "Growth & M&A",
                "blurb":
                    "Due diligence, valuation, negotiation and post-deal "
                    "integration. We act vendor-side or buyer-side, never "
                    "both on the same dossier. Transaction types: carve-outs, "
                    "joint ventures, private-equity exits, family MBOs.",
                "scope": [
                    "Vendor due diligence and teaser",
                    "Buyer-side scouting and valuation",
                    "Negotiation and SPA support",
                    "Post-merger integration, first 100 days",
                ],
                "duration": "10 – 24 weeks depending on perimeter",
                "leader":   "Avv. Caterina Foschini",
            },
            {
                "num":   "03",
                "title": "Governance & ESG",
                "blurb":
                    "CSRD alignment, integrated reporting, 231 organisational "
                    "models, board-committee architecture. For listed "
                    "industrial groups and family businesses preparing for "
                    "listing on Euronext Growth.",
                "scope": [
                    "CSRD compliance and integrated reporting",
                    "231 organisational models",
                    "Board committees and policy",
                    "Pre-IPO governance readiness",
                ],
                "duration": "12 – 18 weeks per cycle",
                "leader":   "Eng. Marco Lavezzi",
            },
            {
                "num":   "04",
                "title": "Wealth structuring",
                "blurb":
                    "Wealth planning for Italian entrepreneurial families with "
                    "international perimeter. Family holding companies, "
                    "trusts, family offices and generational transfer.",
                "scope": [
                    "Family holding companies and shareholders' agreements",
                    "Trusts and family foundations",
                    "Family office and advisory committee",
                    "Generational transfer and succession",
                ],
                "duration": "16 – 36 weeks per restructuring",
                "leader":   "Dr. Sabina Erlanger",
            },
            {
                "num":   "05",
                "title": "Industry & manufacturing",
                "blurb":
                    "Vertical practice for the Lombardy and Veneto industrial "
                    "supply chains. Operational diagnostics, supply-chain "
                    "redesign, strategic make-or-buy decisions, international "
                    "production footprint.",
                "scope": [
                    "Multi-plant operational diagnostics",
                    "Supply-chain redesign",
                    "Strategic make-or-buy",
                    "Opening foreign production sites",
                ],
                "duration": "10 – 20 weeks per project",
                "leader":   "Dr. Lorenzo Pellizzari",
            },
            {
                "num":   "06",
                "title": "Financial services",
                "blurb":
                    "Strategic transformation for Italian regional banks, "
                    "asset managers and regulated fintechs. Strategic "
                    "repositioning, banking M&A and Bank of Italy "
                    "prudential reporting.",
                "scope": [
                    "Strategic repositioning for banks",
                    "Banking and asset-management M&A",
                    "Bank of Italy / EBA compliance",
                    "Front-to-back operating models",
                ],
                "duration": "12 – 24 weeks depending on perimeter",
                "leader":   "Dr. Giulia Antinori",
            },
        ],

        # Process strip — how a mandate is run
        "process_label":   "How we work",
        "process_heading": "Four phases, one sequence",
        "process": [
            ("01", "Exploratory call",
             "Thirty confidential minutes with a managing partner. "
             "We discuss the perimeter — no commercial proposal yet."),
            ("02", "Written proposal",
             "Within five days, a three-page mandate proposal covering "
             "perimeter, deliverables, timeline and transparent fee schedule."),
            ("03", "Execution",
             "Dedicated team from opening through closing. The managing "
             "partner sits in every steering meeting — never a junior."),
            ("04", "Closing & follow-up",
             "Confidential closing memo for the board, plus quarterly "
             "follow-up at no cost for the following twelve months."),
        ],

        # Final CTA
        "cta_heading":   "Which practice fits your situation?",
        "cta_intro":
            "If the perimeter is not yet clear, send us a short description "
            "of the problem. We will direct you to the right partner within "
            "48 hours — even if we do not take on the mandate.",
        "cta_primary":   "Write to us",
        "cta_primary_href": "contatti",
    },

    # ─── CASE-STUDIES (list) ────────────────────────────────────
    "case-studies": {
        "eyebrow":  "Selected mandates · 2022 — 2026",
        "headline": "Three mandates, <em>three directions</em>.",
        "intro":
            "A selection of mandates closed over the last four years. "
            "Clients are identified by sector code (in observance of "
            "NDAs), but the output metrics are real and verifiable "
            "through a reference call.",

        # Card-list of case studies (full posts in `posts` below)
        "cases_label": "Cases",
        "cases_intro":
            "A balanced selection across our three main streams — board "
            "advisory, M&A and governance. The complete list is available "
            "as a PDF on request via the contact page.",

        "cta_heading":   "A case similar to yours?",
        "cta_intro":
            "The full dossiers (perimeter, KPIs, reference call with the "
            "client's CFO) are accessible under mutual NDA. The NDA is "
            "signed on the first call, before any commercial proposal.",
        "cta_primary":   "Request the full dossiers",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /case-studies/<slug>/
    "posts": [
        {
            "slug":     "manifatturiero-bresciano-piano-industriale",
            "title":    "Brescia manufacturing group · 2025-28 industrial plan",
            "category": "Board advisory",
            "year":     "2025",
            "duration": "14 weeks",
            "client_code": "Industry & manufacturing · Brescia · 320 employees · €78M revenue",
            "lead":
                "Three plants, two shareholding families at odds on the "
                "future perimeter. Pragma realigned the three-year industrial "
                "plan ahead of the board's renewal.",
            "sections": [
                {
                    "label": "The problem",
                    "heading": "Two families, three conflicting plans",
                    "body":
                        "The group was founded in 1968 by the merger of two "
                        "family businesses. In 2024 the board faced three "
                        "competing industrial plans: shutting down the oldest "
                        "plant, opening a fourth site in Romania, or carving "
                        "out the components division for sale to a private-"
                        "equity fund. The two shareholding families were "
                        "backing incompatible scenarios, and the board's "
                        "mandate was due to expire within twelve months.",
                },
                {
                    "label": "The approach",
                    "heading": "Operational diagnostics + governance review",
                    "body":
                        "Pragma worked along three parallel tracks. The "
                        "industry & manufacturing practice ran a nine-week "
                        "operational diagnostic across the three plants, "
                        "with OEE measurement, line-by-line costing and "
                        "sector benchmarking. In parallel, the board-"
                        "advisory practice mediated between the two "
                        "families through three alignment workshops. The "
                        "governance practice reviewed the shareholders' "
                        "agreement and proposed a new board charter with "
                        "strengthened quorum requirements.",
                },
                {
                    "label": "The outcome",
                    "heading": "Three-year plan approved unanimously",
                    "body":
                        "The 2025–28 industrial plan was approved unanimously "
                        "by the board and the extraordinary shareholders' "
                        "meeting. The oldest plant was converted (not closed) "
                        "to production of wind-energy components — €4M in "
                        "capex financed through a Simest facility. The "
                        "components carve-out was set aside. The new "
                        "shareholders' agreement reduced blocking quorums "
                        "by 40%.",
                },
            ],
            "kpi": [
                ("€ 4 M",   "capex conversion financed"),
                ("0",       "plants closed (3 preserved)"),
                ("100%",    "board approval of the plan"),
                ("12 months", "before the board renewal"),
            ],
            "lead_partner": "Dr. Federico Seregni · Dr. Lorenzo Pellizzari",
            "team":         "3 partners · 4 seniors · 2 juniors · 14 weeks",
            "next_label":   "Next mandate",
        },
        {
            "slug":     "carve-out-consumer-italia-dach",
            "title":    "Consumer carve-out · cross-border Italy-DACH transaction",
            "category": "Growth & M&A",
            "year":     "2024",
            "duration": "22 weeks",
            "client_code": "Retail & consumer · Vicenza · 540 employees · €112M revenue",
            "lead":
                "Carve-out of the private-label division of a Vicenza-based "
                "retail group, sold to a German strategic operator. Pragma "
                "acted sell-side, from teaser through integration.",
            "sections": [
                {
                    "label": "The problem",
                    "heading": "A strategic division, a divided shareholding",
                    "body":
                        "The private-label division represented 28% of "
                        "group revenue but 51% of group EBITDA, and had "
                        "grown on DACH clients (DM, Lidl Germany) who did "
                        "not feel adequately served by an Italian structure. "
                        "Part of the shareholder base was pushing for a "
                        "carve-out with sale to a German strategic operator; "
                        "another part preferred to preserve the perimeter "
                        "and seek an Italian industrial partner.",
                },
                {
                    "label": "The approach",
                    "heading": "Vendor due diligence + parallel scouting",
                    "body":
                        "Pragma ran a complete vendor due diligence "
                        "(operational, financial, legal, tax) in ten weeks. "
                        "In parallel, the scouting workstream approached "
                        "six potential acquirers — three DACH strategic "
                        "operators, two European private-equity funds with "
                        "a consumer focus, and one Italian operator. The "
                        "sale was structured as a private auction over "
                        "four weeks with a formal process letter.",
                },
                {
                    "label": "The outcome",
                    "heading": "Sale at target multiple, no disruption",
                    "body":
                        "The sale closed at the target EBITDA multiple "
                        "(8.4x), with a 24-month earn-out clause. Post-"
                        "merger integration preserved 80% of the division's "
                        "workforce (production operators and commercial "
                        "staff). 100% of the contracts with the three "
                        "largest DACH clients were renewed within six "
                        "months of closing.",
                },
            ],
            "kpi": [
                ("8.4 x",    "EBITDA multiple at closing"),
                ("80%",      "of transferred workforce retained"),
                ("100%",     "DACH contracts renewed post-closing"),
                ("22 wks",   "from engagement to signing"),
            ],
            "lead_partner": "Avv. Caterina Foschini · Dr. Giulia Antinori",
            "team":         "2 partners · 5 seniors · 3 juniors · 22 weeks",
            "next_label":   "Next mandate",
        },
        {
            "slug":     "csrd-utility-quotata-roadmap",
            "title":    "CSRD roadmap for a listed utility group",
            "category": "Governance & ESG",
            "year":     "2025",
            "duration": "18 weeks",
            "client_code": "Energy & utilities · Bologna · 1,800 employees · €420M revenue",
            "lead":
                "First CSRD reporting cycle for a utility group listed on "
                "Euronext Milan. Double materiality, scope 1-2-3 baseline, "
                "sustainability governance reconfigured.",
            "sections": [
                {
                    "label": "The problem",
                    "heading": "Fragmented reporting, incomplete baseline",
                    "body":
                        "The group had historically produced a voluntary "
                        "GRI sustainability report, but its scope 3 baseline "
                        "was incomplete, its materiality was not double "
                        "(impact + financial), and its KPIs were not audit-"
                        "ready. The first mandatory CSRD exercise fell on "
                        "fiscal year 2025, to be published in April 2026 — "
                        "eighteen months of runway.",
                },
                {
                    "label": "The approach",
                    "heading": "Double materiality + baseline + governance",
                    "body":
                        "Pragma ran three parallel streams over eighteen "
                        "weeks. Stream A — double materiality assessment "
                        "with 38 stakeholders consulted (suppliers, "
                        "customers, unions, environmental NGOs, "
                        "institutional investors). Stream B — completion "
                        "of the scope 1-2-3 baseline under GHG Protocol "
                        "methodology with external validation. Stream C — "
                        "governance reconfiguration: board-level "
                        "sustainability committee, updated ESG policy, "
                        "KPIs integrated into the industrial plan.",
                },
                {
                    "label": "The outcome",
                    "heading": "First audit-ready CSRD report, on time",
                    "body":
                        "The first CSRD report was published with a "
                        "limited-assurance opinion from the external "
                        "auditor (zero qualifications). 142 ESRS datapoints "
                        "fully covered. The board-level sustainability "
                        "committee has been active since Q1 2026, with a "
                        "Pragma member acting as independent technical "
                        "observer for the first year. The group's MSCI "
                        "ESG rating improved by two notches.",
                },
            ],
            "kpi": [
                ("142",  "ESRS datapoints covered"),
                ("0",    "auditor qualifications"),
                ("38",   "stakeholders consulted"),
                ("+ 2",  "MSCI ESG rating notches"),
            ],
            "lead_partner": "Eng. Marco Lavezzi",
            "team":         "1 partner · 4 seniors · 2 juniors · 18 weeks",
            "next_label":   "Next mandate",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Preliminary conversation",
        "headline": "Thirty minutes, a <em>narrow</em> agenda, no commitment.",
        "intro":
            "The first contact is always with a managing partner. We "
            "discuss the perimeter of the mandate, the timeline and any "
            "conflict of interest — before any commercial proposal is "
            "issued.",

        # Form fields — generic loop in chrome
        "form_label":   "Request the call",
        "form_heading": "Complete the confidential form",
        "form_intro":
            "You will receive confirmation within 48 working hours of "
            "submission. Sensitive information is processed under EU "
            "Reg. 2016/679 (GDPR) and held in an encrypted archive "
            "accessible only to the partners of the firm.",
        "form_fields": [
            {"name": "name",      "label": "First name",     "type": "text",     "required": True,  "placeholder": "e.g., Frederick",
             "helper": "First name only, thank you."},
            {"name": "surname",   "label": "Surname",        "type": "text",     "required": True,  "placeholder": "e.g., Seregni",
             "helper": "As it appears on the organisation chart."},
            {"name": "company",   "label": "Company",        "type": "text",     "required": True,  "placeholder": "e.g., Lombard Industrial Group",
             "helper": "Registered corporate name, not trading name."},
            {"name": "role",      "label": "Role",           "type": "text",     "required": True,  "placeholder": "e.g., CFO · CEO · Board member",
             "helper": "Position on the board or within the executive team."},
            {"name": "email",     "label": "Business email", "type": "email",    "required": True,  "placeholder": "federico.seregni@group.com",
             "helper": "We do not accept consumer domains (Gmail/Outlook/Libero) for this first contact."},
            {"name": "phone",     "label": "Phone",          "type": "tel",      "required": True,  "placeholder": "+39 ...",
             "helper": "Direct line of the contact, not switchboard."},
            {"name": "practice",  "label": "Practice of interest", "type": "select", "required": True,
             "options": [
                 "To define in call",
                 "Board advisory",
                 "Growth & M&A",
                 "Governance & ESG",
                 "Wealth structuring",
                 "Industry & manufacturing",
                 "Financial services",
             ],
             "helper": "Select \"To define\" if the perimeter spans more than one practice."},
            {"name": "horizon",   "label": "Time horizon",   "type": "select", "required": True,
             "options": [
                 "Within one month",
                 "Within three months",
                 "Within six months",
                 "Exploratory, no urgency",
             ],
             "helper": "Helps us schedule the right partner for the mandate."},
            {"name": "perimeter", "label": "Brief description of the perimeter", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "600 characters maximum. No counterparty names — these "
                            "will be discussed only under mutual NDA.",
             "helper": "Enough to assess whether the mandate falls within our competence. "
                       "Counterparty names are shared only after mutual NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "The person who will sign the preliminary NDA.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Company",
             "meta": "For the preliminary conflict check.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Mandate perimeter",
             "meta": "No sensitive detail here — the technical perimeter is shared on call, after mutual NDA.",
             "fields": ["practice", "horizon", "perimeter"]},
            {"num": "04", "title": "Attachments (optional)",
             "meta": "Company profile, governance one-pager or standard NDA: these can front-load the call.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "briefing_allegato",
            "label":    "Preliminary documents",
            "helper":   "Company profile, governance one-pager or standard NDA. "
                        "PDF / DOCX · 15 MB maximum in total. Encrypted archive "
                        "with access limited to Pragma partners.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Drag your documents here or",
            "link":     "browse from your archive",
            "meta":     "PDF / DOCX · max 15 MB · encrypted archive",
        },

        "form_submit_label": "Request the call",
        "form_submit_note":
            "Confirmation from a managing partner within 48 working hours. "
            "No external BDR, no automated sequence.",
        "form_consent":
            "I consent to the processing of my personal data under EU "
            "Reg. 2016/679 (GDPR). The data is held in an encrypted "
            "archive accessible only to Pragma partners. No data is "
            "disclosed to third parties without explicit authorisation.",

        # Office meta-row labels
        "office_address_label": "Address",
        "office_area_label":    "Neighborhood",
        "office_phone_label":   "Phone",
        "office_email_label":   "Email",

        # Sidebar — offices + contact channels
        "offices_label":   "Offices",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Headquarters",
                "address": "Via Filodrammatici 10 · 20121",
                "area":    "Porta Nuova · near Piazza della Scala",
                "phone":   "+39 02 3611 9900",
                "email":   "milano@pragmaadvisors.it",
            },
            {
                "city":    "Frankfurt",
                "tag":     "DACH desk",
                "address": "Bockenheimer Landstr. 51 · 60325",
                "area":    "Westend · near Alte Oper",
                "phone":   "+49 69 8870 4400",
                "email":   "frankfurt@pragmaadvisors.it",
            },
            {
                "city":    "Zürich",
                "tag":     "Wealth desk",
                "address": "Paradeplatz 8 · 8001",
                "area":    "Innenstadt · near Bahnhofstrasse",
                "phone":   "+41 44 215 7700",
                "email":   "zurich@pragmaadvisors.it",
            },
        ],

        "channels_label": "Direct channels",
        "channels": [
            ("Advisory desk",        "+39 02 3611 9900",             "Mon – Fri · 9:00 – 19:00"),
            ("Institutional email",  "segreteria@pragmaadvisors.it", "Reply within 48 hours"),
            ("Corporate LinkedIn",   "in/pragma-advisors",           "For media relations"),
        ],

        "footnote":
            "Pragma Advisors does not reply to anonymous enquiries and does "
            "not issue preliminary opinions by email without a first call "
            "with a partner. Administrative information (indicative fees, "
            "billing terms, mandate-acceptance criteria) is discussed on "
            "the first call, not in writing.",
    },
}
