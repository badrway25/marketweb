"""Fiscus — Tax Advisory Firm · English locale content tree.

Wave 2 Pilot #1 — Phase X.4 · English locale for the Fiscus template.

Mirrors the shape of ``FISCUS_CONTENT_IT`` exactly — same keys, nesting
and list shapes. Only values are translated/adapted.

Voice register: institutional Financial Times / Harvard Business Review.
Formal, precise, never pitch-y — the register of a chartered accountant
who explains a regulation patiently without oversimplifying. Pragma EN
is the voice reference for the same corporate-suite archetype, but the
semantic domain here is tax advisory (income tax returns, statutory
audit, tax litigation, wealth planning), not board advisory.

Italian normative references are preserved verbatim — they are the
actual laws an Italian tax studio cites regardless of the client's
reading language. The first occurrence of each receives a brief
parenthetical clarification for the English reader (e.g. "art. 2477
c.c. (Italian Civil Code threshold for statutory audit)",
"D.Lgs. 39/2010 (Italian statutory audit decree)", "ODCEC (Italian
Association of Chartered Accountants)"). Proper names, Italian
addresses, Euro figures, albo numbers and years are kept as-is.
"""
from __future__ import annotations

from typing import Any


FISCUS_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Firm",           "kind": "home"},
        {"slug": "lo-studio",     "label": "The firm",       "kind": "about"},
        {"slug": "competenze",    "label": "Expertise",      "kind": "services"},
        {"slug": "casi-seguiti",  "label": "Engagements",    "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contact",        "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "F",
        "logo_word":    "Fiscus",
        "tag":          "Tax advisory firm · Milan · enrolled with ODCEC (Italian Association of Chartered Accountants) since 2003",
        "phone":        "+39 02 4951 3388",
        "email":        "segreteria@fiscusstudio.it",
        "address":      "Via Melzo 14 · 20129 Milano",
        "hours_compact": "Mon – Fri · 9:00 – 18:30 · by appointment",
        "hours_footer_rows": [
            "Saturday · by appointment near filing deadlines",
            "Sunday · closed",
        ],
        "license":      "Enrolled with ODCEC Milan · Section A · since 2003",
        "footer_intro":
            "Independent tax advisory firm for Italian-registered freelancers and "
            "businesses (partite IVA), SMEs and entrepreneurial families. Income "
            "tax returns, statutory financial statements, tax litigation and "
            "multi-year tax planning. Headquartered in Milan, on a recurring "
            "advisory basis — not one-off engagements.",
        "foot_studio":   "The firm",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Office",
        "offices_footer_rows": [
            "Milan · Porta Venezia",
        ],
        # Case study cross-page meta labels
        "case_practice_label":     "Area",
        "case_year_label":         "Year",
        "case_duration_label":     "Duration",
        "case_lead_label":         "Lead",
        "case_lead_partner_label": "Lead",
        "case_team_label":         "Team & timeline",
        "case_timeline_label":     "Timeline",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Tax advisory firm · Milan · enrolled with ODCEC (Italian Association of Chartered Accountants) since 2003",
        "headline":    "The <em>correct</em> filing, not the clever trick.",
        "intro":
            "Tax advisory firm for Italian-registered freelancers and businesses, "
            "SMEs and entrepreneurial families. Income tax returns, statutory "
            "financial statements, tax litigation and multi-year tax planning — "
            "no promises of tax savings, and with the filing calendar always "
            "in plain view.",
        "primary_cta":   "Initial consultation",
        "primary_href":  "contatti",
        "secondary_cta": "Download the filing-calendar guide",
        "secondary_href":"lo-studio",

        # Right-hand hero photo + credit overlay (fiscal-desk direction)
        "hero_image":              "https://images.pexels.com/photos/8927688/pexels-photo-8927688.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "hero_image_credit_left":  ("Direction",       "Dr. A. Ruffini"),
        "hero_image_credit_right": ("Founded",         "2003"),
        "hero_meta_strip": [
            ("Headquarters",    "Milan · Porta Venezia"),
            ("ODCEC roster",    "4 chartered accountants · since 2003"),
            ("Active clients",  "260 VAT-registered practices"),
        ],

        # Advisory pillars — three practice areas on home
        "pillars_label":   "Areas of expertise",
        "pillars_heading": "Three practices, one signature",
        "pillars_intro":
            "A single multidisciplinary team serves every client. A chartered "
            "accountant enrolled on the roster is not a cost to minimise: "
            "it is a professional safeguard worth choosing deliberately.",
        "pillars": [
            ("01", "Tax returns & statutory accounts",
             "Income tax returns, foreign-asset monitoring schedule (quadro RW) "
             "for overseas income, withholding-agent certifications, statutory "
             "financial statements — audit-ready, with the review calendar "
             "agreed in January and signatures lodged ahead of the Italian "
             "Revenue Agency's (Agenzia Entrate) deadlines."),
            ("02", "Tax litigation",
             "Support through tax assessments, voluntary disclosure (ravvedimento "
             "operoso), and appeals before the Provincial and Regional Tax Courts "
             "(Commissioni Tributarie). No promise of outcome — always a written "
             "preliminary probability estimate, on letterhead, before any "
             "engagement is signed."),
            ("03", "Wealth & generational succession",
             "Multi-year tax planning, family holding companies, succession and "
             "gift planning — for medium-to-high private estates and "
             "entrepreneurial families preparing a generational transfer over "
             "a 5-10 year horizon."),
        ],

        # KPI strip — document the studio's continuity track record
        "kpi_heading": "Twenty-two years of uninterrupted practice",
        "kpi_strip": [
            ("22",       "years since founding"),
            ("260",      "VAT-registered clients in portfolio"),
            ("€ 180 M",  "aggregate client revenue"),
            ("0",        "unforeseen penalties in 2025"),
        ],

        # Sectors ribbon — the client base
        "sectors_label": "Client sectors",
        "sectors": [
            "Freelancers & sole traders",
            "SME manufacturing",
            "Professional practices",
            "Private wealth",
            "Real estate",
        ],

        # Trust band — anonymized client categories (chartered accountants do not
        # disclose client logos under the duty of professional confidentiality)
        "trust_label":   "Clients who entrust their tax affairs to Fiscus",
        "trust_logos":   [
            "INDIVIDUAL VAT-REGISTERED PRACTICES",
            "PROFESSIONAL CONSULTANCIES",
            "SME MANUFACTURERS",
            "ENTREPRENEURIAL FAMILIES",
            "PRIVATE REAL-ESTATE HOLDINGS",
            "REGISTERED-PROFESSION MEMBERS",
        ],

        # Leadership preview — 3 partners on home
        "leadership_label":   "Direction",
        "leadership_heading": "The chartered accountants who will sit at your table",
        "leadership_intro":
            "Every client is handled personally by at least one partner enrolled "
            "with the ODCEC. No junior takeover, no quiet rotation — the partner "
            "you meet at the initial consultation signs the tax returns and "
            "stands accountable for the filings.",
        "leadership": [
            {
                "name":  "Dr. Andrea Ruffini",
                "role":  "Founding partner · Tax returns & statutory accounts",
                "bio":
                    "Chartered accountant enrolled with ODCEC Milan since 1999, "
                    "Section A. Statutory auditor (revisore legale) enrolled on "
                    "the Register of Statutory Auditors since 2004. Specialised "
                    "in corporate tax and statutory financial statements. "
                    "Co-founded the firm in 2003 with Dr. Balestrieri.",
                "credentials": [
                    "ODCEC Milan no. 4488/A (since 1999)",
                    "Statutory Auditor no. 137952 (since 2004)",
                    "Università Bocconi — CLEA '96",
                ],
            },
            {
                "name":  "Dr. Ilaria Balestrieri",
                "role":  "Partner · Tax litigation",
                "bio":
                    "Chartered accountant enrolled with ODCEC Milan since 2001, "
                    "Section A. Member of the Milan Bar since 2010 and qualified "
                    "to argue before the Supreme Court (Cassazionista), "
                    "specialised in tax litigation. Appears before the Provincial "
                    "and Regional Tax Courts of Lombardy and Piedmont.",
                "credentials": [
                    "ODCEC Milan no. 5611/A (since 2001)",
                    "Milan Bar Association (since 2010)",
                    "Supreme Court qualification since 2018",
                ],
            },
            {
                "name":  "Dr. Stefano Conti",
                "role":  "Partner · Wealth & generational succession",
                "bio":
                    "Chartered accountant enrolled with ODCEC Milan since 2008, "
                    "Section A. Specialist in estate planning for entrepreneurial "
                    "families — holding companies, trusts, succession. Joined "
                    "the firm in 2014, promoted to partner in 2019. Adjunct "
                    "lecturer in international taxation at LIUC Castellanza.",
                "credentials": [
                    "ODCEC Milan no. 7912/A (since 2008)",
                    "LL.M. Tax Law, Bocconi",
                    "TEP · Society of Trust and Estate Practitioners",
                ],
            },
        ],

        # Case studies preview — three recent mandates on home
        "cases_label":   "Engagements",
        "cases_heading": "Three engagements, three areas of expertise",
        "cases_intro":
            "A recent selection of clients served over the past three years. "
            "Under the duty of professional confidentiality, client names are "
            "replaced by sector code, but the figures are verifiable through a "
            "reference call.",

        # Final CTA band before footer — appointment-focused
        "cta_label":     "Initial consultation",
        "cta_heading":   "Forty-five minutes, open agenda, no commitment",
        "cta_intro":
            "The first meeting is held with a partner enrolled with the ODCEC. "
            "We discuss the area of expertise, the expected horizon of the "
            "engagement and an indicative professional fee — before any signed "
            "mandate. Existing clients book through the secure client area.",
        "cta_primary":   "Request an appointment",
        "cta_primary_href": "contatti",
        "cta_secondary": "Download the filing-calendar guide",
        "cta_secondary_href": "lo-studio",
    },

    # ─── LO STUDIO (about + values + team + history) ────────────
    "lo-studio": {
        "eyebrow":   "The firm · 2003 — 2026",
        "headline":  "An <em>independent</em> tax advisory firm, twenty-two years of uninterrupted practice.",
        "intro":
            "Fiscus was founded in Milan in 2003 by Andrea Ruffini and Ilaria "
            "Balestrieri — two chartered accountants enrolled with the ODCEC, "
            "trained in corporate taxation and tax litigation. We have grown "
            "by cooptation, never by acquisition, and have preserved our "
            "independence from third-party capital throughout.",

        # Studio history — 5-step timeline
        "history_label":   "Firm history",
        "history_heading": "Five milestones, twenty-two years",
        "history_intro":
            "Five dates that defined Fiscus. Each reflects a structural choice — "
            "on independence, on specialisation, on perimeter — that still "
            "shapes how we accept a new client today.",
        "history": [
            ("2003", "Founding",
             "Andrea Ruffini and Ilaria Balestrieri open Fiscus on Via Melzo, "
             "with twelve clients already in portfolio — all carried over from "
             "their prior firm with the clients' explicit written consent."),
            ("2008", "Tax-litigation practice",
             "Ilaria Balestrieri's admission to the Bar launches the litigation "
             "practice: appeals before Provincial and Regional Tax Courts, tax "
             "assessments, voluntary disclosure. First hearing before the "
             "Milan Provincial Tax Court in March 2009."),
            ("2014", "Dr. Conti joins the firm",
             "Stefano Conti joins as an associate to build the wealth practice — "
             "family holding companies, trusts, generational succession. "
             "Promoted to partner in 2019 after five years of supervision."),
            ("2020", "Digitalisation of tax filings",
             "Full integration with the Italian Revenue Agency via Entratel "
             "and electronic invoicing. Encrypted document archive with "
             "ten-year retention and client access through a secure portal."),
            ("2024", "Statutory-audit practice",
             "Andrea Ruffini formalises the statutory-audit practice for SMEs "
             "subject to the statutory-auditor requirement. Three active audit "
             "engagements by December 2024."),
        ],

        # Method / values — 4 principi
        "values_label":   "Method",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "The four rules that separate a Fiscus client from an ordinary "
            "advisory relationship. They are set out on the letterhead of the "
            "signed engagement mandate — not only on this page.",
        "values": [
            ("01", "Independence from external capital",
             "The firm's equity is held entirely by active partners. No "
             "corporate shareholder, no minority fund investor, no external "
             "investor of any kind. The selection of clients is never "
             "influenced by a third party's agenda — and long-standing "
             "clients know the relationship does not shift in tone because "
             "a partner has changed."),
            ("02", "One partner per client",
             "Every client has a reference partner enrolled with the ODCEC "
             "who personally follows the engagement from the opening of the "
             "file through to the signing of the tax returns. The partner "
             "met at the initial consultation stands accountable for the "
             "filings — no silent delegations, no year-end rotations."),
            ("03", "No promises of tax savings",
             "We do not sign engagement proposals that promise a percentage "
             "tax reduction: this is contrary to the ODCEC code of conduct, "
             "and is the hallmark of opportunistic relationships. Our "
             "profession is to apply the regulations correctly and to flag "
             "tax reliefs where they exist."),
            ("04", "Transparent annual retainer",
             "Annual fee agreed in December for the following year, revised "
             "only upon a genuine change of perimeter (new office, new VAT "
             "registration, new business unit). No hidden metered billing, "
             "no back-end commissions."),
        ],

        # Full team — 3 soci + 4 collaboratori iscritti albo o praticanti
        "team_label":   "Team",
        "team_heading": "Three partners, four associates, one governance",
        "team_intro":
            "The people who will handle your mandate. Every tax return is "
            "signed by a partner — associates support data collection, "
            "preliminary review and documentation management.",
        "team": [
            {"name": "Dr. Andrea Ruffini",
             "role": "Founding partner · Tax returns & statutory accounts · Statutory auditor",
             "office": "Milan",
             "bio": "Chartered accountant enrolled with ODCEC since 1999 and "
                    "statutory auditor since 2004. Bocconi CLEA '96. Co-founded the firm."},
            {"name": "Dr. Ilaria Balestrieri",
             "role": "Partner · Tax litigation · Qualified before the Supreme Court",
             "office": "Milan",
             "bio": "Chartered accountant enrolled with ODCEC since 2001 and "
                    "admitted to the Supreme Court bar since 2018. Appears in Lombardy and Piedmont."},
            {"name": "Dr. Stefano Conti",
             "role": "Partner · Wealth & generational succession · LIUC lecturer",
             "office": "Milan",
             "bio": "Chartered accountant enrolled with ODCEC since 2008. LL.M. "
                    "Tax Law, Bocconi. TEP since 2021."},
            {"name": "Dr. Serena Lomazzi",
             "role": "Associate · Personal-income tax returns",
             "office": "Milan",
             "bio": "Chartered accountant enrolled with ODCEC since 2017. "
                    "Coordinates data collection and the preparation of 730 and RPF returns."},
            {"name": "Dr. Giacomo Prevedini",
             "role": "Associate · SME statutory accounts · Trainee auditor",
             "office": "Milan",
             "bio": "Chartered accountant enrolled with ODCEC since 2021. "
                    "Handles ordinary bookkeeping and year-end accounts for the "
                    "SME manufacturers in the portfolio."},
            {"name": "Ms. Nadia Kouadio",
             "role": "Head of bookkeeping · Payroll & contributions",
             "office": "Milan",
             "bio": "Certified bookkeeper enrolled with the Labour Consultants' "
                    "roster since 2012. Manages payroll in partnership with an "
                    "external labour consultant, plus ordinary bookkeeping."},
        ],

        # Coordinates strip
        "coordinates_label": "Office",
        "coordinates": [
            ("Milan", "Via Melzo 14 · 20129 · Porta Venezia — 200 metres from Porta Venezia metro station"),
        ],

        # Page-level CTA
        "cta_heading": "An exploratory first meeting",
        "cta_intro":
            "The first forty-five minutes with a partner are an exploratory "
            "conversation, not a commercial proposal. We discuss the area of "
            "expertise, the time horizon and the indicative professional fee. "
            "At the end, you are free to choose another firm — and to take "
            "away all the preliminary documentation with you.",
        "cta_primary":  "Request an appointment",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Areas of expertise · 2026",
        "headline": "Six areas of expertise, <em>one signature</em>.",
        "intro":
            "Fiscus's six practice areas. Every client engages the full "
            "multidisciplinary team — we do not bill each area separately; "
            "the annual retainer covers the combination of disciplines the "
            "mandate requires.",

        # Card meta labels
        "svc_duration_label": "Typical duration",
        "svc_leader_label":   "Reference partner",

        # 6 areas in airy cards
        "services": [
            {
                "num":   "01",
                "title": "Income tax returns & ordinary taxation",
                "blurb":
                    "Income tax returns (Modello Redditi PF · SP · SC · ENC), "
                    "Modello 730, foreign-asset monitoring schedule (quadro RW) "
                    "for overseas income, withholding-agent certifications. We "
                    "work to a calendar agreed in January, with internal "
                    "deadlines set 30 days ahead of the Italian Revenue Agency's — "
                    "because a return signed on 30 September is better than one "
                    "signed on 30 November.",
                "scope": [
                    "Modello Redditi PF / SP / SC / ENC",
                    "Modello 730 for employees and pensioners",
                    "Quadro RW — foreign-asset monitoring schedule",
                    "Withholding-agent certifications (Certificazione Unica)",
                    "Voluntary disclosure (ravvedimento operoso) for amended returns",
                ],
                "duration": "Recurring annual engagement",
                "leader":   "Dr. Andrea Ruffini",
            },
            {
                "num":   "02",
                "title": "Statutory financial statements & ordinary bookkeeping",
                "blurb":
                    "Ordinary bookkeeping, CEE-format statutory financial "
                    "statements, notes to the accounts, management report, "
                    "shareholders' meeting minutes. For SMEs with a statutory "
                    "auditor in place, we also prepare the documentation for "
                    "the external auditor — audit-ready by March, filed with "
                    "the Chamber of Commerce by May.",
                "scope": [
                    "Ordinary and simplified bookkeeping",
                    "CEE-format financial statements + notes to the accounts",
                    "Filing with the Chamber of Commerce",
                    "Management report for limited-liability companies",
                    "Support to the statutory auditor and external auditor",
                ],
                "duration": "Recurring annual engagement",
                "leader":   "Dr. Andrea Ruffini",
            },
            {
                "num":   "03",
                "title": "Tax litigation",
                "blurb":
                    "Support through tax assessments with settlement, voluntary "
                    "disclosure (ravvedimento operoso), appeals before the "
                    "Provincial and Regional Tax Courts (Commissioni Tributarie), "
                    "and judicial settlement. Appearances in Lombardy and "
                    "Piedmont. For every file we issue a written preliminary "
                    "probability estimate before the engagement is signed.",
                "scope": [
                    "Tax assessment with settlement",
                    "Voluntary disclosure and payment-plan arrangements",
                    "Appeals to Provincial/Regional Tax Courts · Supreme Court (with counsel)",
                    "Judicial settlement",
                    "Self-review petitions to the Italian Revenue Agency",
                ],
                "duration": "3 to 24 months depending on the instance",
                "leader":   "Dr. Ilaria Balestrieri",
            },
            {
                "num":   "04",
                "title": "Tax planning & wealth",
                "blurb":
                    "Multi-year tax planning for medium-to-high private estates "
                    "and entrepreneurial families. Family holding companies, "
                    "trusts, foundations, tax-efficient insurance wrappers, "
                    "succession planning. Always on a 5-10 year horizon — never "
                    "annual tax-saving promises.",
                "scope": [
                    "Family holding companies and shareholder agreements",
                    "Trusts and family foundations",
                    "Succession and gift planning",
                    "Branch IV insurance-wrapper structuring",
                    "Assessment of tax-relief instruments (PIR, ELTIF)",
                ],
                "duration": "12 – 36 months for a structural reorganisation",
                "leader":   "Dr. Stefano Conti",
            },
            {
                "num":   "05",
                "title": "Payroll and labour consulting & withholding agent",
                "blurb":
                    "Payroll, social-security contributions and withholding-agent "
                    "duties for SMEs and professional practices — in partnership "
                    "with an external labour consultant enrolled with the CdL "
                    "roster. We cover the tax and accounting side; the labour "
                    "consultant covers employment law and social security.",
                "scope": [
                    "Payroll slips and monthly F24 payments",
                    "Withholding-agent Certificazione Unica",
                    "Modello 770",
                    "Support on INPS / INAIL / Labour Inspectorate audits",
                    "Coordination with external labour consultant (Ms. Kouadio)",
                ],
                "duration": "Recurring monthly engagement",
                "leader":   "Ms. Nadia Kouadio · Dr. A. Ruffini",
            },
            {
                "num":   "06",
                "title": "Statutory audit & statutory auditor",
                "blurb":
                    "Statutory audit for SMEs subject to the statutory-auditor "
                    "requirement — unlisted joint-stock companies and "
                    "limited-liability companies exceeding the thresholds set "
                    "out in art. 2477 c.c. (Italian Civil Code threshold for "
                    "statutory audit). Three active mandates at present. We "
                    "only act as external auditor, never as internal statutory "
                    "auditor within the same group.",
                "scope": [
                    "Statutory audit report under D.Lgs. 39/2010 (Italian statutory audit decree)",
                    "Quarterly periodic review of the accounts",
                    "Audit planning under ISA Italia",
                    "Communication with the internal statutory-auditor board",
                    "Presentation to the shareholders' meeting",
                ],
                "duration": "Three-year or nine-year engagement",
                "leader":   "Dr. Andrea Ruffini",
            },
        ],

        # Process — how a new client onboarding is run
        "process_label":   "How we work",
        "process_heading": "Four steps, one sequence",
        "process": [
            ("01", "Initial consultation",
             "Forty-five private minutes with a partner enrolled with the "
             "ODCEC. We discuss area of expertise, time horizon and indicative "
             "fee. No signed mandate, no cost."),
            ("02", "Written proposal",
             "Within seven business days, a three-page proposal setting out "
             "the perimeter of the engagement, the list of filings, the "
             "internal deadline calendar and the agreed annual retainer."),
            ("03", "File opening",
             "Delegation to the Italian Revenue Agency via Entratel, "
             "transfer of documentation from the previous accountant "
             "(where applicable), opening of the secure client area in "
             "the encrypted archive."),
            ("04", "Ongoing engagement",
             "A single reference partner for the entire engagement. "
             "Deadlines tracked 30 days ahead of Italian Revenue Agency "
             "dates. Annual review in December for the following year."),
        ],

        # Final CTA
        "cta_heading":   "Which area of expertise fits your situation?",
        "cta_intro":
            "If the perimeter is not yet clear, send us a short description "
            "of the situation (type of business, year of formation, any "
            "overdue filings). We respond within 48 business hours — even "
            "when the answer is \"we are not the right firm\".",
        "cta_primary":   "Write to us",
        "cta_primary_href": "contatti",
    },

    # ─── CASI SEGUITI (case-studies list) ───────────────────────
    "casi-seguiti": {
        "eyebrow":  "Engagements · 2022 — 2026",
        "headline": "Three engagements, <em>three areas of expertise</em>.",
        "intro":
            "A selection of engagements handled over the past four years. "
            "Clients are identified by sector code in compliance with the duty "
            "of professional confidentiality (art. 199 of the Italian Code of "
            "Criminal Procedure and the ODCEC Code of Conduct), but the "
            "figures are real and verifiable through a reference call with "
            "the client's internal contact.",

        "cases_label": "Engagements",
        "cases_intro":
            "A balanced selection across the three main areas — tax returns & "
            "statutory accounts, tax litigation, wealth. The complete list of "
            "cases available as references is provided as a PDF through the "
            "contact page.",

        "cta_heading":   "An engagement similar to yours?",
        "cta_intro":
            "The full dossiers (perimeter, aggregate figures, possible reference "
            "call with the client's internal contact) are accessible under "
            "mutual confidentiality undertaking. The undertaking is signed "
            "during the initial consultation, before any fee commitment.",
        "cta_primary":   "Request the full dossiers",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /casi-seguiti/<slug>/
    "posts": [
        {
            "slug":     "pmi-manifattura-bilancio-revisione",
            "title":    "Lombard SME manufacturer · statutory-audit appointment",
            "category": "Tax returns & statutory accounts",
            "year":     "2025",
            "duration": "10 weeks + three-year engagement",
            "client_code":
                "Manufacturing industry · Brescia · 42 employees · "
                "€ 12.4 M revenue · S.r.l. with statutory-auditor board under art. 2477",
            "lead":
                "First financial year subject to the statutory-audit requirement "
                "after exceeding the thresholds set out in art. 2477 c.c. "
                "(Italian Civil Code threshold for statutory audit). The client "
                "appointed Fiscus as external auditor in continuity with a "
                "long-standing ordinary tax engagement.",
            "sections": [
                {
                    "label": "The problem",
                    "heading": "Transition to statutory-auditor board mid-year",
                    "body":
                        "The company had exceeded, for the second consecutive "
                        "year, the dimensional thresholds under art. 2477 c.c. "
                        "(revenue > € 8.8 M, assets > € 4.4 M, headcount > 50). "
                        "The statutory-auditor board was appointed at the "
                        "shareholders' meeting in March 2025, and an external "
                        "statutory auditor had to be engaged under D.Lgs. "
                        "39/2010 (Italian statutory audit decree) within three "
                        "months. The company preferred continuity with its "
                        "long-standing tax firm — provided there was no "
                        "conflict of interest on the independence requirement.",
                },
                {
                    "label": "The approach",
                    "heading": "Segregation of practices and ISA planning",
                    "body":
                        "Fiscus accepted the audit engagement subject to "
                        "operational segregation: a different partner handles "
                        "the tax engagement (Dr. A. Ruffini) and the audit "
                        "engagement (Dr. I. Balestrieri, enrolled on the "
                        "Register of Statutory Auditors since 2011). Audit "
                        "planning followed ISA Italia 315 — assessment of the "
                        "internal control system, identification of significant "
                        "risks, determination of materiality. The audit plan "
                        "was shared with the statutory-auditor board before "
                        "execution.",
                },
                {
                    "label": "The outcome",
                    "heading": "Unqualified statutory-audit report",
                    "body":
                        "Statutory-audit report under art. 14 of D.Lgs. 39/2010 "
                        "published in May 2025 with no qualifications, no "
                        "emphasis-of-matter paragraphs and no material "
                        "uncertainties. The audit surfaced two recommendations "
                        "for strengthening the internal control system "
                        "(segregation of duties in the purchasing cycle, "
                        "month-end inventory procedure), which the company "
                        "implemented by September. Three-year audit engagement "
                        "confirmed for the 2025-2027 financial years.",
                },
            ],
            "kpi": [
                ("0",        "qualifications in the statutory-audit report"),
                ("2",        "recommendations implemented by the client"),
                ("3 years",  "statutory-audit engagement duration"),
                ("10 wks",   "from engagement to signed report"),
            ],
            "lead_partner": "Dr. Ilaria Balestrieri (audit) · Dr. Andrea Ruffini (tax)",
            "team":         "2 partners · 1 senior · 1 trainee auditor · 10 weeks",
            "next_label":   "Next engagement",
        },
        {
            "slug":     "contenzioso-tributario-accertamento-iva",
            "title":    "Tax litigation · VAT assessment on intra-EU transactions",
            "category": "Tax litigation",
            "year":     "2024",
            "duration": "14 months from assessment to Regional Tax Court ruling",
            "client_code":
                "Wholesale trade · Como · 18 employees · "
                "€ 6.2 M revenue · Italian Revenue Agency assessment € 187,000 VAT",
            "lead":
                "Italian Revenue Agency (Agenzia Entrate) assessment "
                "reclassifying intra-EU transactions as ordinary domestic "
                "supplies (presumption of domestic destination). The client "
                "engaged Fiscus at the pre-assessment adversarial stage, "
                "shortly before the settlement deadline.",
            "sections": [
                {
                    "label": "The problem",
                    "heading": "Domestic-invoice presumption on EU transactions",
                    "body":
                        "The Italian Revenue Agency issued a notice of "
                        "assessment for fiscal year 2021 reclaiming VAT of "
                        "€ 187,000, a 90% penalty and interest. The office "
                        "reclassified a series of transactions with a "
                        "Slovakian customer as ordinary domestic supplies, on "
                        "the assumption that the transport documentation did "
                        "not sufficiently evidence the actual exit of the "
                        "goods from Italian territory. The settlement deadline "
                        "was 28 days away.",
                },
                {
                    "label": "The approach",
                    "heading": "Adversarial proceeding with supplementary CMR documentation",
                    "body":
                        "Fiscus prepared a pre-assessment adversarial "
                        "submission in three weeks. Gathered: 64 original "
                        "CMR waybills stamped by the EU consignee, bank "
                        "statements evidencing payments by the Slovakian "
                        "customer from its Slovakian bank, historical VIES "
                        "verifications of the EU customer, a sworn expert "
                        "report from the client's head of logistics. The "
                        "documentation was filed both in the adversarial "
                        "proceeding and, in parallel, in the appeal to the "
                        "Provincial Tax Court (Commissione Tributaria) of "
                        "Como, to anticipate the possibility of administrative "
                        "rejection.",
                },
                {
                    "label": "The outcome",
                    "heading": "Appeal upheld at first instance and on appeal",
                    "body":
                        "The Provincial Tax Court of Como upheld the appeal "
                        "in full in June 2024, quashing the assessment with "
                        "ruling no. 412/2024. The Italian Revenue Agency "
                        "appealed to the Regional Tax Court of Lombardy, "
                        "which in December 2024 confirmed the first-instance "
                        "ruling and dismissed the office's appeal. The "
                        "judgment became final in January 2025. The client "
                        "recovered legal costs under art. 15 of D.Lgs. "
                        "546/1992 in the amount of € 14,200.",
                },
            ],
            "kpi": [
                ("€ 187,000", "VAT assessed — fully overturned"),
                ("100%",      "legal costs recovered under art. 15"),
                ("2/2",       "instances ruled in favour"),
                ("14 months", "from assessment to final judgment"),
            ],
            "lead_partner": "Dr. Ilaria Balestrieri",
            "team":         "1 Supreme-Court-qualified partner · 1 senior · 14 months",
            "next_label":   "Next engagement",
        },
        {
            "slug":     "wealth-passaggio-generazionale-holding",
            "title":    "Wealth · family holding for generational succession",
            "category": "Wealth & generational succession",
            "year":     "2025",
            "duration": "20 months from engagement to completion",
            "client_code":
                "Entrepreneurial family · Varese · aggregate estate "
                "€ 38 M (controlling interest in SME manufacturer + real estate + liquidity) · "
                "two children, both active in the business",
            "lead":
                "Entrepreneurial family holding a controlling interest in a "
                "second-tier SME manufacturer, three operating properties, "
                "two prime residential properties and significant liquidity. "
                "Founder aged 68, two children operational in the business, "
                "spouse not involved in management. Objective: prepare the "
                "generational transfer over a 7-10 year horizon.",
            "sections": [
                {
                    "label": "The problem",
                    "heading": "Heterogeneous estate, two children in different roles",
                    "body":
                        "The founder had three concrete concerns. First: "
                        "preserve the unity of corporate control after "
                        "succession — both children worked in the business, "
                        "but in different roles and with different outlooks. "
                        "Second: provide a liquidity exit for the spouse and "
                        "the non-operating branch of the family without "
                        "forcing the sale of shareholdings. Third: minimise "
                        "the tax impact of succession (inheritance tax above "
                        "the € 1 M threshold for direct-line relatives) "
                        "while fully complying with the regulations in force — "
                        "no offshore structures, no aggressive trusts.",
                },
                {
                    "label": "The approach",
                    "heading": "Family holding + shareholders' agreement + PIR",
                    "body":
                        "Fiscus coordinated a 20-month programme across four "
                        "phases. Phase 1 (months 1-4): incorporation of a "
                        "family holding S.r.l. with a tax-neutral contribution "
                        "of the operating shareholdings under art. 177 TUIR "
                        "(Italian Income Tax Code). Phase 2 (months 5-8): "
                        "drafting of the shareholders' agreement between the "
                        "two family branches with tag-along/drag-along "
                        "mechanisms to prevent future splits. Phase 3 "
                        "(months 9-14): gradual gift of the holding's shares "
                        "to the children, with lifetime usufruct reserved to "
                        "the founder and spouse — qualifying for the relief "
                        "under art. 3, paragraph 4-ter of D.Lgs. 346/1990 "
                        "(Italian inheritance and gift tax code, which "
                        "exempts controlling shareholdings from succession "
                        "duty). Phase 4 (months 15-20): subscription of "
                        "PIR-compliant instruments for the non-operating "
                        "branch of the family, funded by the dividend flows.",
                },
                {
                    "label": "The outcome",
                    "heading": "Tax-efficient succession + family governance",
                    "body":
                        "The structure was completed in September 2025. "
                        "Inheritance tax on the operating shareholdings "
                        "reduced to zero thanks to the relief under art. 3, "
                        "paragraph 4-ter (family settlement combined with "
                        "controlling holding). Shareholders' agreement "
                        "executed by the two siblings and the parents, with "
                        "buy-out clauses set at an independently appraised "
                        "value updated annually. The non-operating branch "
                        "(spouse and any grandchildren) receives regular "
                        "dividends from the holding and has subscribed "
                        "individual PIR allocations of € 180,000 each over "
                        "the 2025-2030 horizon. The founder retains voting "
                        "rights through usufruct until age 75, with an "
                        "additional 5-year option.",
                },
            ],
            "kpi": [
                ("€ 0",      "inheritance tax on the operating shareholdings"),
                ("100%",     "unity of control preserved"),
                ("20 months","from engagement to completion"),
                ("4/4",      "phases completed on schedule"),
            ],
            "lead_partner": "Dr. Stefano Conti",
            "team":         "1 partner · 1 senior · external notary · 20 months",
            "next_label":   "Next engagement",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Initial consultation",
        "headline": "Forty-five minutes, <em>open</em> agenda, no commitment.",
        "intro":
            "The first contact is held with a partner enrolled with the ODCEC. "
            "We discuss the area of expertise, the expected horizon of the "
            "engagement and an indicative professional fee — before any signed "
            "mandate. Existing clients book through the secure client area.",

        # Form fields — chartered-accountant onboarding shape
        "form_label":   "Request an appointment",
        "form_heading": "Complete the preliminary form",
        "form_intro":
            "You will receive confirmation within 48 business hours of "
            "submission. Data is processed under EU Reg. 2016/679 (GDPR) "
            "and held in the firm's encrypted archive with ten-year retention.",
        "form_fields": [
            {"name": "name",      "label": "First name",     "type": "text",     "required": True,  "placeholder": "e.g., Andrea",
             "helper": "First name only."},
            {"name": "surname",   "label": "Surname",        "type": "text",     "required": True,  "placeholder": "e.g., Ruffini",
             "helper": "As it appears on identification documents."},
            {"name": "company",   "label": "Company or sole trader name", "type": "text", "required": False,
             "placeholder": "e.g., Officine Meccaniche Bresciane S.r.l.",
             "helper": "Optional — complete if the contact is on behalf of a business."},
            {"name": "vat",       "label": "VAT number",     "type": "text",     "required": False, "placeholder": "IT 12345678901",
             "helper": "Optional — helpful if the engagement concerns corporate taxation."},
            {"name": "fiscal_code","label": "Italian fiscal code","type": "text","required": True,  "placeholder": "RFFNDR72M15F205Z",
             "helper": "Required — needed to enable the Entratel delegation should the engagement proceed."},
            {"name": "email",     "label": "Email",          "type": "email",    "required": True,  "placeholder": "andrea.ruffini@example.com",
             "helper": "We send the appointment confirmation to this address."},
            {"name": "phone",     "label": "Phone",          "type": "tel",      "required": True,  "placeholder": "+39 ...",
             "helper": "For any clarifying queries ahead of the appointment."},
            {"name": "area",      "label": "Area of expertise of interest", "type": "select", "required": True,
             "options": [
                 "To be defined at the appointment",
                 "Income tax returns and ordinary taxation",
                 "Statutory financial statements and ordinary bookkeeping",
                 "Tax litigation",
                 "Tax planning and wealth",
                 "Payroll and labour consulting",
                 "Statutory audit",
             ],
             "helper": "Choose \"To be defined\" if the situation is complex."},
            {"name": "time_slot", "label": "Preferred time slot", "type": "select", "required": True,
             "options": [
                 "Morning 9:00 – 12:00",
                 "Early afternoon 14:00 – 16:30",
                 "Late afternoon 16:30 – 18:30",
                 "No preference",
             ],
             "helper": "Near filing deadlines we give priority to morning slots."},
            {"name": "situation", "label": "Brief description of the situation", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "600 characters maximum. Example: \"Italian-registered freelance under the flat-rate (forfettario) regime since 2021, first year out of the flat-rate, need to plan the transition to ordinary bookkeeping.\"",
             "helper": "Enough to assess whether the situation falls within our areas of expertise and to prepare the first conversation."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "The person we will meet at the initial consultation.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Tax identifiers",
             "meta": "The Italian fiscal code is mandatory; VAT number and company name only if the engagement concerns a business activity.",
             "fields": ["fiscal_code", "vat", "company"]},
            {"num": "03", "title": "Scope of the meeting",
             "meta": "To schedule the reference partner in the preferred slot. No sensitive detail here — documents are brought to the appointment.",
             "fields": ["area", "time_slot", "situation"]},
            {"num": "04", "title": "Documentation (optional)",
             "meta": "Last income tax return, last financial statements, any notices from the Italian Revenue Agency: these can front-load the appointment.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Preliminary documents",
            "helper":   "Last income tax return (Modello Redditi or 730), last filed financial statements, notices received from the Italian Revenue Agency. "
                        "PDF · max 10 MB total. Encrypted archive with access limited to partners.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "Drag your documents here or",
            "link":     "browse from your archive",
            "meta":     "PDF · max 10 MB · AES-256 encrypted archive",
        },

        "form_submit_label": "Request an appointment",
        "form_submit_note":
            "Confirmation from a partner enrolled with the ODCEC within 48 "
            "business hours. No outsourced front desk, no automation — we "
            "read every request personally.",
        "form_consent":
            "I consent to the processing of my personal data under EU "
            "Reg. 2016/679 (GDPR). Data is held in the firm's encrypted "
            "archive with ten-year retention, accessed only by partners "
            "and roster-enrolled associates. No data is disclosed to "
            "third parties without explicit written authorisation.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Address",
        "office_area_label":    "Neighborhood",
        "office_phone_label":   "Phone",
        "office_email_label":   "Email",

        # Sidebar — office + direct channels
        "offices_label":   "Office",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Sole office",
                "address": "Via Melzo 14 · 20129",
                "area":    "Porta Venezia · 200 metres from Porta Venezia metro station",
                "phone":   "+39 02 4951 3388",
                "email":   "segreteria@fiscusstudio.it",
            },
        ],

        "channels_label": "Direct channels",
        "channels": [
            ("Firm reception",           "+39 02 4951 3388",           "Mon – Fri · 9:00 – 18:30"),
            ("Institutional email",      "segreteria@fiscusstudio.it", "Reply within 48 business hours"),
            ("Secure client area",       "area.fiscusstudio.it",       "For existing clients — deadlines + documents"),
        ],

        "footnote":
            "Fiscus does not respond to anonymous enquiries and does not "
            "issue preliminary tax opinions by email. Administrative "
            "information (indicative professional fee, billing terms, "
            "filing calendar for the proposed perimeter) is discussed at "
            "the initial consultation — free of charge and without "
            "commitment to engagement.",
    },
}
