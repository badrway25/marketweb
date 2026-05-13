"""Atto · Studio Notarile Conti–Sironi–Verri · English locale tree.

Wave 1 Pass-4 (T48 · 2026-05-12). English translation of `ATTO_CONTENT_IT`
defined in `template_content_atto.py`. Mirrors the lawyer/classic-gold
archetype shape verbatim: every top-level key, nested key and tuple arity
matches the IT tree (D-054 distinctness axes preserved across locales).

Translation workflow: T48 Workflow C (four sub-agent parallel translators,
one per content cluster — home/studio, pratiche, avvocati, posts/contatti).
Each cluster was rendered under the institutional-legal register of an
Anglo-American legal correspondent (think FT Law section, NYT Legal
correspondent) — sober, precise, no marketingese, no US-attorney bombast.

Voice anchor: the Italian load-bearing term `atto pubblico` renders as
`public deed` (the closest functional equivalent to the public-faith
notarial deed of Roman-Latin tradition). The italic-em surfaces are
preserved one-to-one across IT → EN: every `<em>atto pubblico</em>` in
the IT tree has its `<em>public deed</em>` counterpart at the same
structural location in the EN tree. Standalone `<em>atto</em>` shortens
to `<em>deed</em>` for sentence flow. Adjacent vocabulary stays inside
the same register: `notarial deed`, `public faith`, `notary's roll`,
`Milan Notarial District`, `public official`.

Non-localizable carry-overs (preserved verbatim from IT):
- phone +39 02 7641 1898, email, PEC address
- Italian Civil Code citations (`art. X c.c.`, `L. 89/1913` etc.)
- Italian press / publication outlets (`NOTARIATO`, `RIVISTA DEL NOTARIATO`,
  `GUIDA AL DIRITTO`, `CNN NOTIZIE`, `RIVISTA TRIMESTRALE DI DIRITTO E
  PROCEDURA`, `FEDERNOTAI`)
- Photo Pexels URLs (shared `_NOTARY_*` helper constants)
- Brand name `Studio Notarile Conti–Sironi–Verri` (the legal Italian entity)
- Prices in € with Latin digits
- Address: `Milano` → `Milan`, postal code 20121 preserved
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_atto import (
    _NOTARY_AMBIENT,  # noqa: F401  — re-export for callers
    _NOTARY_DETAIL,   # noqa: F401
    _NOTARY_HERO,
    _NOTARY_PORTRAIT_F1,  # noqa: F401
    _NOTARY_PORTRAIT_M,   # noqa: F401
    _NOTARY_SIGNING,      # noqa: F401
)


ATTO_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Practice",       "kind": "home"},
        {"slug": "studio",        "label": "The Practice",   "kind": "about"},
        {"slug": "pratiche",      "label": "Types of Deeds", "kind": "services"},
        {"slug": "avvocati",      "label": "Our Notaries",   "kind": "team"},
        {"slug": "pubblicazioni", "label": "Publications",   "kind": "blog_list"},
        {"slug": "contatti",      "label": "Contact",        "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ──────────────────────────
    "site": {
        "logo_initial":  "CSV",
        "logo_word":     "Studio Notarile Conti–Sironi–Verri",
        "tag":           "Milan Notarial District · since 2007",
        "phone":         "+39 02 7641 1898",
        "email":         "studio@notaiconti-sironi-verri.it",
        "address":       "Via Manin 12 · 20121 Milan",
        "hours_compact": "Monday – Friday · 09:00 – 18:30",
        "hours_footer_rows": [
            "Saturday · by appointment for urgent deeds",
            "Sunday · closed",
        ],
        "license":
            "Notaries enrolled with the Milan Notarial District · "
            "Notarial Council of the Joint Districts of Milan, "
            "Busto Arsizio, Lodi, Monza and Varese · L. 89/1913",
        "nav_cta":       "Request an initial consultation",
        "footer_intro":
            "Studio Notarile Conti–Sironi–Verri — seventeen years of "
            "public deeds in the service of families, businesses and "
            "professionals across the Milan Notarial District. Three "
            "associated notaries, one signature carrying public faith.",
        "foot_studio":  "The practice",
        "foot_pages":   "Pages",
        "foot_contact": "Contact",
        "foot_offices": "Office",
        "offices_footer_rows": [
            "Milan · via Manin 12",
            "Milan Notarial District",
        ],

        # Cross-page meta labels (lifted from skin for locale support).
        "case_practice_label":  "Type of deed",
        "case_year_label":      "Year",
        "case_outcome_label":   "Outcome",
        "case_lead_label":      "Notary of record",
    },

    # ════════════════════════════════════════════════════════════════════
    # HOME (studio)
    # ════════════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":  "Studio Notarile Conti–Sironi–Verri · Milan · since 2007",
        "headline": "Seventeen years of the <em>public deed</em>, one signature that holds in law.",
        "intro":
            "The practice advises individuals, families and businesses "
            "on the drafting of the notarial deed — sale and purchase "
            "conveyances, successions, corporate deeds, gifts, mortgage "
            "loans, powers of attorney and wills. Every deed is drawn "
            "up personally by one of the three associated notaries, "
            "all enrolled on the roll of the Milan Notarial District, "
            "in the full exercise of their function as public officials "
            "and of the public faith the law confers on that office.",
        "primary_cta":    "Request an initial consultation",
        "primary_href":   "contatti",
        "secondary_cta":  "Types of deeds",
        "secondary_href": "pratiche",

        # Hero — split-ledger-monogram silhouette
        "hero_credit_left":  ("Founding notary",  "M. B. Conti, Notary"),
        "hero_credit_right": ("District",         "Milan · enrolled on the roll"),
        "hero_meta_strip": [
            ("Office",             "Milan · via Manin 12"),
            ("Associated notaries","Three · enrolled 2007 / 2014 / 2021"),
            ("Deeds executed",     "4,200+ · IT · EN · FR"),
        ],

        # Practice-area ledger — 4 rows on home, full 7 on /pratiche
        "practice_label":   "Types of deeds",
        "practice_heading": "Seven categories of <em>deed</em>, one public faith.",
        "practice_intro":
            "The practice handles the principal categories of notarial "
            "deed contemplated by Italian law. Each public deed is "
            "drawn up personally by one of the notaries of the firm, "
            "read aloud to the appearing party in the language of "
            "their choice (Italian, English or French) and entered in "
            "the register pursuant to the Notarial Act (L. 89/1913).",
        "practice": [
            ("01", "Real-estate sale and purchase deeds",
             "Drafting of the notarial conveyance for the sale and "
             "purchase of residential, commercial and industrial "
             "property. Cadastral searches, mortgage searches and "
             "planning compliance checks precede execution. The deed "
             "is received in public form, carrying the public faith "
             "recognised by art. 2700 of the Italian Civil Code."),
            ("02", "Successions and estate declarations",
             "Opening of the succession, drafting of the inheritance "
             "tax return, acceptance of an estate with benefit of "
             "inventory, publication of holographic wills, "
             "renunciations and partitions among heirs. Cross-border "
             "successions are handled under Reg. EU 650/2012."),
            ("03", "Corporate deeds and extraordinary transactions",
             "Incorporation of companies by public deed pursuant to "
             "arts. 2328 and 2463 c.c., amendments to articles of "
             "association, minutes of extraordinary shareholders' "
             "meetings, mergers, demergers and conversions. The "
             "practice handles the entire process from resolution "
             "through filing with the Companies Register."),
            ("04", "Mortgage loans and security interests",
             "Land and mortgage loan deeds, voluntary mortgage "
             "creation, subrogations under L. 40/2007, "
             "acknowledgement deeds and mortgage releases. "
             "Operational coordination with the lending institution "
             "for execution concurrent with the conveyance of sale."),
        ],

        # Stats band — counter animation (notarial-institutional facts)
        "stats_label":   "Seventeen years of public faith",
        "stats_heading": "The practice in figures",
        "stats": [
            ("3",      "notaries on the roll"),
            ("17",     "years since founding"),
            ("4,200+", "deeds executed"),
            ("3",      "drafting languages (IT/EN/FR)"),
        ],

        # Partners portrait preview — 3 notai associati
        "partners_label":   "The three notaries",
        "partners_heading": "Three notaries, one practice",
        "partners_intro":
            "The practice is led by three associated notaries, each "
            "enrolled on the roll of the Milan Notarial District and "
            "responsible for their own categories of deed. The "
            "signature is personal: the notary who receives the "
            "appearing party is the same one who drafts, reads aloud "
            "and signs the public deed entered in the register.",
        "partners": [
            {
                "name":  "Maria Beatrice Conti, Notary",
                "role":  "Founding notary · Corporate deeds · International M&A",
                "foro":  "Milan Notarial District · on the roll since 2007",
                "bio":
                    "Founder of the practice, she receives deeds of "
                    "incorporation, extraordinary transactions and "
                    "public deeds drafted in English. Formerly trainee "
                    "with an international notarial practice in Milan "
                    "(2004-2006), she focuses in particular on "
                    "cross-border M&A and on multinational groups "
                    "operating through an Italian subsidiary.",
            },
            {
                "name":  "Andrea Sironi, Notary",
                "role":  "Associated notary · Corporate law · Court-appointed expert, Court of Milan",
                "foro":  "Milan Notarial District · on the roll since 2014",
                "bio":
                    "Handles ordinary and extraordinary corporate "
                    "deeds, shareholders' agreements, shareholder "
                    "loans and equity transactions. Court-appointed "
                    "expert (CTU) before the Court of Milan for "
                    "valuations pursuant to art. 2343 c.c. Member of "
                    "the Studies Commission of the Notarial Council "
                    "of the Joint Districts of Milan.",
            },
            {
                "name":  "Stefano Verri, Notary",
                "role":  "Associated notary · Real estate · Successions",
                "foro":  "Milan Notarial District · on the roll since 2021",
                "bio":
                    "Receives deeds of real-estate sale and purchase, "
                    "mortgage loans, gifts and successions. Statutory "
                    "auditor enrolled on the register kept by the "
                    "Ministry of the Economy and Finance, he "
                    "coordinates the planning and cadastral checks "
                    "preliminary to each conveyance. Formerly a "
                    "notarial trainee in Milan and Brescia (2017-2020).",
            },
        ],

        # Publications ribbon — riviste notarili
        "publications_label": "Publications and citations",
        "publications": [
            "NOTARIATO",
            "RIVISTA DEL NOTARIATO",
            "GUIDA AL DIRITTO",
            "CNN NOTIZIE",
            "RIVISTA TRIMESTRALE DI DIRITTO E PROCEDURA",
            "FEDERNOTAI",
        ],

        # Final CTA band — first-meeting (orientamento) ghost serif
        "cta_label":      "Initial orientation consultation",
        "cta_heading":    "Thirty minutes to frame the deed.",
        "cta_intro":
            "The first meeting with one of the notaries lasts about "
            "thirty minutes; it is free of charge and carries no "
            "obligation. The discussion covers the category of deed, "
            "the list of preliminary documents to be gathered and "
            "the schedule of applicable notarial fees. No operational "
            "decision is required at this stage.",
        "cta_primary":       "Request an initial consultation",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "About the practice",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════════════
    # STUDIO (about) — history, associated notaries, values, office
    # ════════════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "The practice · 2007 — 2026",
        "headline": "Seventeen years of the <em>public deed</em>, three associated notaries.",
        "intro":
            "Studio Notarile Conti–Sironi–Verri opened in Milan in "
            "2007 upon the enrolment of Maria Beatrice Conti, Notary, "
            "the first notary of the district to receive public deeds "
            "drafted in English. The practice has grown by co-option "
            "of colleagues and today comprises three associated "
            "notaries and six full-time staff, all operating from a "
            "single office at via Manin 12.",

        # History timeline — six dates that defined the practice
        "history_label":   "History of the practice",
        "history_heading": "Six dates, seventeen years",
        "history_intro":
            "Six milestones that mark the trajectory of the practice "
            "— from the founder's first enrolment on the roll in 2007 "
            "to the entry of the third notary in 2021. Each step "
            "shaped the collegial composition of the association and "
            "broadened the categories of deed handled.",
        "history": [
            ("2007", "Enrolment of the founding notary",
             "Maria Beatrice Conti, Notary, is enrolled on the roll "
             "of the Milan Notarial District and opens the practice "
             "at via Manin 12. The earliest deeds concern the "
             "incorporation of joint-stock companies for entrepreneurs "
             "in Northern Italy."),
            ("2011", "Trilingual public deeds",
             "The practice begins receiving public deeds drafted in "
             "Italian, English and French pursuant to art. 54 of the "
             "Notarial Act. The international desk serves principally "
             "multinational groups operating through an Italian "
             "subsidiary and families resident abroad."),
            ("2014", "Andrea Sironi, Notary, joins the practice",
             "Andrea Sironi, Notary, a long-standing trainee within "
             "the district, is co-opted as the second notary of the "
             "association. He specialises in corporate deeds, "
             "extraordinary transactions and valuation reports under "
             "art. 2343 c.c."),
            ("2018", "Successions and real-estate desk",
             "The practice formalises a dedicated successions and "
             "real-estate desk. Internal procedures are codified for "
             "mortgage searches and cadastral checks preliminary to "
             "each sale-and-purchase conveyance."),
            ("2021", "Stefano Verri, Notary, joins the practice",
             "Stefano Verri, Notary, completes the collegial "
             "composition of the association. A statutory auditor "
             "enrolled on the register kept by the Ministry of the "
             "Economy and Finance, he assumes operational "
             "responsibility for the real-estate and successions desk."),
            ("2025", "Seventeen years of public faith",
             "The practice passes the four-thousand-two-hundred mark "
             "in deeds executed. The three associated notaries are "
             "active in professional training: Conti as a member of "
             "the Studies Commission of the Notarial Council, Sironi "
             "as court-appointed expert before the Court of Milan, "
             "Verri as a lecturer in notarial practice."),
        ],

        # Method — four non-negotiable principles
        "values_label":   "Notarial method",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "Four operating rules that guide the work of the practice. "
            "They describe not a commercial style but a professional "
            "practice faithful to the Notarial Act (L. 89/1913) and to "
            "the Code of Conduct of the National Council of the "
            "Italian Notariat.",
        "values": [
            ("01", "Impartiality of the public official",
             "The notary is a public official and acts in the "
             "interest of all parties to the deed, never of one alone. "
             "The practice does not accept partisan instructions: no "
             "deed is drafted to the advantage of one or the other "
             "contracting party. Operational guidance is identical "
             "for seller and buyer, donor and donee, contributor and "
             "recipient company."),
            ("02", "Preliminary documentary verification",
             "Before receiving the deed, the practice verifies the "
             "planning, cadastral and mortgage documentation relating "
             "to the property or company that is the subject of the "
             "deed. The cadastral certificate, the mortgage search "
             "and the energy performance certificate (APE) are "
             "obtained directly, never delegated to the parties, and "
             "are annexed to the deed in accordance with established "
             "practice."),
            ("03", "Reading in full to the appearing party",
             "The public deed is read in full to the appearing "
             "parties pursuant to art. 51 of the Notarial Act, in "
             "Italian or in the language of their choice from those "
             "in which the notary is qualified to draft (IT/EN/FR). "
             "Only after the reading and the express approval are "
             "the signature and register number affixed."),
            ("04", "Transparent schedule of notarial fees",
             "Fees are determined according to the schedule in force "
             "approved by the National Council of the Italian "
             "Notariat. The practice issues a written indicative "
             "estimate before each deed, inclusive of taxes and "
             "registration duty. No item is added at the moment of "
             "execution."),
        ],

        # Coordinates strip — single Milan office
        "coordinates_label": "The office",
        "coordinates": [
            ("Milan · office",        "Via Manin 12 · 20121 · Porta Nuova"),
            ("Notarial District",     "Milan · Notarial Council of the Joint Districts"),
        ],

        # Page-level CTA
        "cta_heading":  "An initial consultation to frame the deed.",
        "cta_intro":
            "The first meeting with one of the notaries of the "
            "practice is free of charge, lasts about thirty minutes "
            "and carries no commitment to any subsequent step. The "
            "discussion covers the category of deed, the preliminary "
            "documents and the schedule of applicable notarial fees.",
        "cta_primary":       "Request an initial consultation",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # PRATICHE (services) — 7 categories of notarial deed
    # ════════════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Types of deeds · 2026",
        "headline": "Seven categories of <em>notarial deed</em>, one signature.",
        "intro":
            "The seven categories of deed handled by the practice. "
            "Each public deed is drawn up personally by one of the "
            "notaries of the association, enrolled on the roll of "
            "the Milan Notarial District, and entered in the register "
            "pursuant to the Notarial Act (L. 89/1913). The schedule "
            "of notarial fees is communicated in writing before "
            "execution.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":          "Notary in charge",
        "svc_jurisdiction_label":  "District",

        # 7 categories of notarial deed
        "services": [
            {
                "num":   "01",
                "title": "Real-estate sale and purchase deeds",
                "blurb":
                    "Drafting of the notarial conveyance for the sale "
                    "and purchase of residential, commercial and "
                    "industrial property. The practice also handles "
                    "preliminary sale-and-purchase agreements "
                    "(compromesso) and barter deeds. The public faith "
                    "of the deed is recognised by art. 2700 c.c.",
                "scope": [
                    "Cadastral certificate and mortgage search",
                    "Planning compliance check and APE",
                    "Registered preliminary sale-and-purchase agreement",
                    "Public deed read to the appearing party",
                ],
                "lead":          "Stefano Verri, Notary",
                "jurisdiction":  "Milan · Notarial District",
            },
            {
                "num":   "02",
                "title": "Successions and estate declarations",
                "blurb":
                    "Opening of the succession, drafting of the "
                    "inheritance tax return before the Revenue Agency, "
                    "acceptance of an estate with benefit of "
                    "inventory, publication of holographic wills, "
                    "partitions among heirs. International successions "
                    "are handled under Reg. EU 650/2012.",
                "scope": [
                    "Inheritance tax return",
                    "Acceptance with benefit of inventory or reservation",
                    "Publication of holographic will",
                    "Partitions and renunciations",
                ],
                "lead":          "Stefano Verri, Notary",
                "jurisdiction":  "Milan · EU 650/2012",
            },
            {
                "num":   "03",
                "title": "Corporate deeds · incorporations · extraordinary transactions",
                "blurb":
                    "Incorporation of companies by public deed "
                    "pursuant to arts. 2328 and 2463 c.c., amendments "
                    "to articles of association, minutes of "
                    "extraordinary shareholders' meetings, mergers "
                    "under arts. 2501 et seq. c.c., proportional and "
                    "non-proportional demergers, heterogeneous "
                    "conversions. Filing with the Companies Register "
                    "is handled by the practice.",
                "scope": [
                    "Incorporation of S.p.A. and S.r.l.",
                    "Amendments to articles and shareholders' agreements",
                    "Mergers, demergers, conversions",
                    "Filing with the Companies Register",
                ],
                "lead":          "Andrea Sironi, Notary",
                "jurisdiction":  "Milan · Chamber of Commerce Milan Monza Brianza Lodi",
            },
            {
                "num":   "04",
                "title": "Mortgage loans and security interests",
                "blurb":
                    "Land and mortgage loan deeds, voluntary mortgage "
                    "creation, subrogations under L. 40/2007 "
                    "(mortgage portability), credit acknowledgement "
                    "deeds and mortgage releases. Execution typically "
                    "takes place concurrently with the sale-and-"
                    "purchase conveyance.",
                "scope": [
                    "Mortgage loan executed alongside the conveyance",
                    "Voluntary mortgage creation",
                    "Subrogation under L. 40/2007 (portability)",
                    "Mortgage release and reduction",
                ],
                "lead":          "Stefano Verri, Notary",
                "jurisdiction":  "Milan · Revenue Agency",
            },
            {
                "num":   "05",
                "title": "Gifts · inter vivos deeds",
                "blurb":
                    "Public deeds of gift of real property, cash or "
                    "shareholdings pursuant to arts. 769 et seq. c.c. "
                    "The practice also handles indirect gifts, family "
                    "agreements under art. 768-bis c.c. and gifts "
                    "with reservation of usufruct.",
                "scope": [
                    "Real-estate gift with or without reservation of usufruct",
                    "Gift of shareholdings",
                    "Family agreements (art. 768-bis c.c.)",
                    "Tax planning and gift tax treatment",
                ],
                "lead":          "Maria Beatrice Conti, Notary",
                "jurisdiction":  "Milan · Revenue Agency",
            },
            {
                "num":   "06",
                "title": "Powers of attorney · authentication of signatures",
                "blurb":
                    "Special and general powers of attorney pursuant "
                    "to art. 1387 c.c., authentication of signatures "
                    "on private deeds, authentication of certified "
                    "copies. The practice issues trilingual powers "
                    "of attorney (IT/EN/FR) for deeds to be executed "
                    "abroad, with apostille pursuant to the 1961 "
                    "Hague Convention.",
                "scope": [
                    "Special and general powers of attorney",
                    "Authentication of signatures on private deeds",
                    "Authentication of certified copies",
                    "Apostille and international legalisation",
                ],
                "lead":          "Maria Beatrice Conti, Notary",
                "jurisdiction":  "Milan · Hague Convention 1961",
            },
            {
                "num":   "07",
                "title": "Wills · succession planning",
                "blurb":
                    "Public wills pursuant to art. 603 c.c., receipt "
                    "of holographic wills, international wills under "
                    "the 1973 Washington Convention. The practice "
                    "assists appearing parties with the inventory of "
                    "assets, the quantification of the disposable "
                    "quota and the forced share of compulsory heirs.",
                "scope": [
                    "Public will entered in the register",
                    "Receipt of holographic will",
                    "International will (Washington 1973)",
                    "Forced share and disposable quota planning",
                ],
                "lead":          "Stefano Verri, Notary",
                "jurisdiction":  "Milan · Notarial Archive",
            },
        ],

        # Process strip — how the deed proceeds
        "process_label":   "How the deed proceeds",
        "process_heading": "Four stages, one sequence",
        "process": [
            ("01", "Initial orientation consultation",
             "Thirty minutes, free of charge, with one of the notaries "
             "of the association. The discussion frames the category "
             "of deed, sets out the list of preliminary documents and "
             "communicates the schedule of applicable notarial fees. "
             "No operational decision is required at this stage."),
            ("02", "Document gathering and verification",
             "The practice gathers and verifies the necessary "
             "documents directly: cadastral certificate, mortgage "
             "search, planning compliance, energy performance "
             "certificate (APE) and personal-status records. The "
             "appearing party receives a written list of what "
             "remains for them to provide."),
            ("03", "Draft of the deed",
             "The notary in charge prepares the draft of the deed "
             "and forwards it to the appearing party at least five "
             "working days before execution, to allow for a "
             "considered reading. Any clarifications are discussed "
             "in a second technical meeting."),
            ("04", "Execution, reading and entry in the register",
             "The notary reads the deed to the appearing party "
             "pursuant to art. 51 of the Notarial Act, in Italian "
             "or in the language of their choice. After signature, "
             "the deed is entered in the register, registered with "
             "the Revenue Agency and kept in original form at the "
             "practice."),
        ],

        # Final CTA
        "cta_heading":  "Unsure which deed you need?",
        "cta_intro":
            "If the category of deed is not yet defined, an initial "
            "orientation consultation may be requested. During the "
            "thirty minutes, free of charge, one of the notaries of "
            "the practice directs you to the correct procedure and "
            "communicates the list of preliminary documents to be "
            "gathered.",
        "cta_primary":       "Request an initial consultation",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # AVVOCATI (team) — the three associated notaries
    # ════════════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "The notaries · three on the roll",
        "headline": "Three associated notaries, <em>one</em> signature of public faith.",
        "intro":
            "The practice comprises three associated notaries, all "
            "enrolled on the roll of the Milan Notarial District. "
            "Entry into the association proceeds by unanimous "
            "co-option among the existing notaries, never by "
            "acquisition of an outside practice: each new notary "
            "brings their own enrolment and their own specialisations. "
            "Six full-time staff complete the team.",

        # Card meta labels
        "lawyer_foro_label":           "District",
        "lawyer_year_label":           "Year of enrolment",
        "lawyer_specialization_label": "Categories of deed",

        # 3 associated notaries
        "lawyers": [
            {
                "name":           "Maria Beatrice Conti, Notary",
                "role":           "Founding notary of the practice",
                "specialization": "Corporate deeds · M&A · gifts · trilingual powers of attorney",
                "foro":           "Milan Notarial District",
                "year":           "On the roll since 2007",
                "bio":
                    "Founder of Studio Notarile Conti–Sironi–Verri, "
                    "she opened the office at via Manin 12 in March "
                    "2007 immediately upon enrolment on the roll of "
                    "the Milan Notarial District. She receives "
                    "public deeds in Italian, English and French "
                    "pursuant to art. 54 of the Notarial Act, with "
                    "particular specialisation in the incorporation "
                    "of companies for multinational groups operating "
                    "through an Italian subsidiary, cross-border "
                    "mergers and international powers of attorney "
                    "with apostille under the Hague Convention. "
                    "Member of the Studies Commission of the "
                    "Notarial Council of the Joint Districts of "
                    "Milan, Busto Arsizio, Lodi, Monza and Varese.",
            },
            {
                "name":           "Andrea Sironi, Notary",
                "role":           "Associated notary · corporate law",
                "specialization": "Corporate deeds · extraordinary transactions · valuations under art. 2343 c.c.",
                "foro":           "Milan Notarial District",
                "year":           "On the roll since 2014",
                "bio":
                    "Co-opted into the association in 2015 after "
                    "eight years of notarial practice with a leading "
                    "Milan firm, he handles ordinary and "
                    "extraordinary corporate deeds, shareholders' "
                    "agreements, shareholder loans and share capital "
                    "increases under arts. 2441 and 2443 c.c. "
                    "Court-appointed expert (CTU) before the Court "
                    "of Milan for valuations under art. 2343 c.c. "
                    "and for the determination of liquidation values "
                    "under art. 2437-ter c.c. Lecturer in notarial "
                    "practice at the School of Notariat of Lombardy.",
            },
            {
                "name":           "Stefano Verri, Notary",
                "role":           "Associated notary · real estate and successions",
                "specialization": "Sale-and-purchase deeds · mortgages · successions · wills",
                "foro":           "Milan Notarial District",
                "year":           "On the roll since 2021",
                "bio":
                    "The most recent entrant to the association, he "
                    "completes the collegial composition of the "
                    "three notaries. He handles real-estate sale "
                    "and purchase deeds, mortgage loans, "
                    "subrogations under L. 40/2007 and the full "
                    "succession chain — opening of the succession, "
                    "inheritance tax return, publication of "
                    "holographic wills, acceptance with benefit of "
                    "inventory. A statutory auditor enrolled on the "
                    "register kept by the Ministry of the Economy "
                    "and Finance since 2018, he coordinates the "
                    "planning, cadastral and mortgage checks "
                    "preliminary to the conveyances of the practice.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════════
    # PUBBLICAZIONI (blog_list) — notarial publications and analyses
    # ════════════════════════════════════════════════════════════════════
    "pubblicazioni": {
        "eyebrow":  "Publications and analyses · 2023 — 2026",
        "headline": "Five analyses of the contemporary <em>notarial deed</em>.",
        "intro":
            "A selection of analyses and publications written by the "
            "notaries of the practice or cited in trade journals. The "
            "articles guide appearing parties, business owners and "
            "professionals through the principal categories of deed "
            "— sale and purchase, succession, incorporation of "
            "companies, gift and power of attorney — without any "
            "claim to completeness and without standing as advice on "
            "any specific case.",

        # Lead post image
        "lead_image": _NOTARY_HERO,

        # Footer strap and fallbacks
        "footer_strap":
            "The publications of the practice serve an explanatory "
            "purpose. For any specific case, an initial consultation "
            "with one of the notaries of the association is required.",
        "empty_body_fallback_paragraphs": [
            "The article is in preparation. The practice publishes "
            "its analyses only after collegial review by the three "
            "associated notaries, in order to avoid inaccuracies or "
            "assessments rendered obsolete by changes in legislation.",
            "For any specific case, an initial orientation "
            "consultation (thirty minutes, free of charge) may be "
            "requested with one of the notaries of the practice.",
        ],
    },

    # Posts powering blog_detail. URL: /pubblicazioni/<slug>/
    "posts": [
        {
            "slug":     "atto-pubblico-mercato-immobiliare-2026",
            "kicker":   "Real-estate deeds",
            "title":    "The public deed in the 2026 real-estate market · notarial practice and preliminary checks",
            "date":     "April 2026",
            "read_min": "9",
            "author":   "Stefano Verri, Notary",
            "lede":
                "A survey of the planning, cadastral and mortgage "
                "checks the practice carries out before receiving a "
                "real-estate sale-and-purchase conveyance, in light "
                "of the changes introduced by Legislative Decree "
                "23/2023 on energy transparency and of the most "
                "recent case law of the Court of Cassation on "
                "planning non-conformity.",
            "body": [
                ("p",
                 "The notarial conveyance for the sale and purchase "
                 "of real property is a public deed pursuant to "
                 "art. 2699 c.c. and produces the public faith "
                 "recognised by art. 2700 c.c. The notary of record, "
                 "acting as a public official, is required to verify "
                 "in advance the planning, cadastral and mortgage "
                 "regularity of the property."),
                ("h2", "The three preliminary checks"),
                ("p",
                 "The practice gathers three sets of documents before "
                 "execution: the up-to-date cadastral certificate, "
                 "the twenty-year mortgage search and the energy "
                 "performance certificate (APE) in current validity. "
                 "The planning compliance check is further grounded "
                 "in the review of the building permits filed with "
                 "the municipality."),
                ("h2", "The role of the notary"),
                ("p",
                 "The notary is not the adviser of either party: "
                 "they assist both appearing parties in framing the "
                 "deed and reading the clauses. Any planning issues "
                 "that emerge during verification are communicated "
                 "in writing to seller and buyer, so that the "
                 "decision to proceed or to postpone is taken with "
                 "full knowledge of the facts."),
                ("blockquote",
                 "The public faith of the public deed is preserved "
                 "only where the preliminary checks have been "
                 "carried out with the diligence proper to the "
                 "public official. Every documentary omission "
                 "exposes the parties to subsequent risks of "
                 "nullity or voidability."),
            ],
        },
        {
            "slug":     "successioni-famiglia-orientamento",
            "kicker":   "Successions",
            "title":    "Successions within the family · finding your way through declaration, acceptance and partition",
            "date":     "February 2026",
            "read_min": "8",
            "author":   "Stefano Verri, Notary",
            "lede":
                "The actual stages of succession mortis causa under "
                "Italian law. From the opening of the succession "
                "through the inheritance tax return before the "
                "Revenue Agency, the publication of holographic "
                "wills, the acceptance with benefit of inventory and "
                "the partition of the estate. When the notarial deed "
                "is required, when a private writing will suffice.",
            "body": [
                ("p",
                 "The succession opens at the moment of the death of "
                 "the deceased at the place of their last domicile "
                 "pursuant to art. 456 c.c. From that instant the "
                 "deadlines run for the inheritance tax return "
                 "(twelve months) and for any renunciations or "
                 "acceptances with benefit of inventory."),
                ("h2", "Inheritance tax return"),
                ("p",
                 "The practice prepares the inheritance tax return "
                 "to be filed with the Revenue Agency within twelve "
                 "months of the opening of the succession. The "
                 "return sets out the list of the deceased's assets, "
                 "the persons called to the inheritance and any "
                 "deductible liabilities."),
                ("h2", "When the notarial deed is required"),
                ("p",
                 "The notarial deed is required for the publication "
                 "of a holographic will pursuant to art. 620 c.c., "
                 "for the acceptance of an estate with benefit of "
                 "inventory under art. 484 c.c., for the partition "
                 "of an estate containing real property and for "
                 "renunciations relating to estates containing real "
                 "property."),
            ],
        },
        {
            "slug":     "costituzione-srl-semplificata-passaggi-reali",
            "kicker":   "Corporate deeds",
            "title":    "Incorporation of a simplified S.r.l. · the real steps beyond the standard form",
            "date":     "December 2025",
            "read_min": "7",
            "author":   "Andrea Sironi, Notary",
            "lede":
                "The incorporation of a simplified S.r.l. under "
                "art. 2463-bis c.c. is, on the face of it, a "
                "standard procedure at reduced cost. In practice the "
                "public deed calls for a series of preliminary "
                "decisions which the standard template does not "
                "cover: corporate purpose, governance, contributions, "
                "rules for convening the shareholders' meeting.",
            "body": [
                ("p",
                 "The simplified S.r.l., introduced by Law Decree "
                 "1/2012, is a reduced-cost version of the ordinary "
                 "S.r.l. (notarial fees waived for incorporation, "
                 "reduced registration tax). The articles follow "
                 "the ministerial template and cannot be amended at "
                 "the moment of incorporation."),
                ("h2", "The preliminary choices"),
                ("p",
                 "Notwithstanding the standard articles, a number of "
                 "material choices remain to be settled: the "
                 "corporate purpose (which must be lawful and "
                 "determinate), the composition of the governing "
                 "body (sole director or board of directors), the "
                 "duration of the company, the rules for convening "
                 "the shareholders' meeting and the cash "
                 "contributions of the shareholders."),
                ("h2", "The public deed of incorporation"),
                ("p",
                 "The deed of incorporation is received in the form "
                 "of a public deed pursuant to art. 2463-bis "
                 "paragraph 2 c.c. and entered in the Companies "
                 "Register by the notary within twenty days of "
                 "execution. The reading to the appearing "
                 "shareholders is in full, in Italian or in the "
                 "language of their choice from those in which the "
                 "notary is qualified to draft."),
            ],
        },
        {
            "slug":     "donazione-coniugi-riforma-2024",
            "kicker":   "Gifts",
            "title":    "Gifts between spouses · what changes after the 2024 reform and Circular 32/E",
            "date":     "October 2025",
            "read_min": "10",
            "author":   "Maria Beatrice Conti, Notary",
            "lede":
                "A gift between spouses is a typical public deed "
                "under arts. 769 et seq. c.c. The 2024 legislative "
                "changes and Circular 32/E of the Revenue Agency "
                "have clarified a number of points of application "
                "concerning gift tax, allowances and revocability "
                "for subsequent birth of children.",
            "body": [
                ("p",
                 "Gifts between spouses are governed by arts. 769 "
                 "et seq. of the Civil Code and require the form of "
                 "a public deed on pain of nullity under art. 782 "
                 "c.c. The allowance for gift tax between spouses "
                 "is one million euro per donee."),
                ("h2", "Reservation of usufruct and bare ownership"),
                ("p",
                 "A common choice in real-estate gifts between "
                 "spouses is the gift of the bare ownership with "
                 "reservation of usufruct in favour of the donor. "
                 "The arrangement, entirely lawful under art. 796 "
                 "c.c., allows the donor to retain the enjoyment of "
                 "the property and the income it produces."),
                ("h2", "Revocability for subsequent birth of children"),
                ("p",
                 "A gift may be revoked for the subsequent birth of "
                 "children under art. 803 c.c. where the donor, at "
                 "the time of the deed, had no children or "
                 "descendants. Revocability extends to children "
                 "adopted by full adoption occurring after the gift."),
            ],
        },
        {
            "slug":     "procura-art-1387-cc-quando-serve",
            "kicker":   "Powers of attorney",
            "title":    "The power of attorney under art. 1387 c.c. · when it is required and how it is drafted (with apostille)",
            "date":     "July 2025",
            "read_min": "6",
            "author":   "Maria Beatrice Conti, Notary",
            "lede":
                "A power of attorney is the deed by which the "
                "principal confers on the agent the authority to "
                "carry out one or more legal acts in their name. "
                "Where the act to be carried out requires the form "
                "of a public deed — a real-estate conveyance, for "
                "instance — the power of attorney too must be "
                "received in the form of a public deed.",
            "body": [
                ("p",
                 "Art. 1387 c.c. governs the cases in which a power "
                 "of attorney is required to carry out legal acts "
                 "in the name of the principal. Under the principle "
                 "of formal symmetry (art. 1392 c.c.), the power of "
                 "attorney must take the same form as the act the "
                 "agent is to carry out."),
                ("h2", "Special and general powers of attorney"),
                ("p",
                 "A special power of attorney confers the authority "
                 "to carry out a specific act (the sale of a "
                 "specified property, for example). A general power "
                 "of attorney confers the authority to carry out "
                 "all acts falling within a category (all acts of "
                 "ordinary administration of the principal's "
                 "patrimony, for example)."),
                ("h2", "Trilingual powers of attorney and apostille"),
                ("p",
                 "For acts to be carried out abroad, the practice "
                 "drafts powers of attorney in Italian and in the "
                 "language of the destination country (English or "
                 "French) pursuant to art. 54 of the Notarial Act. "
                 "The apostille under the 1961 Hague Convention is "
                 "affixed by the Public Prosecutor at the Court of "
                 "Milan."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════════════
    # CONTATTI (contact) — single Milan office, orientation form
    # ════════════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Initial orientation consultation · free of charge · no obligation",
        "headline": "Thirty minutes with a <em>notary</em> to frame the deed.",
        "intro":
            "The first meeting takes place directly with one of the "
            "three notaries of the association. The discussion covers "
            "the category of deed, the list of preliminary documents "
            "to be gathered and the schedule of applicable notarial "
            "fees. The meeting lasts about thirty minutes, is free "
            "of charge and carries no commitment to any subsequent "
            "step.",

        # Form fields
        "form_label":   "Request form",
        "form_heading": "Request an initial orientation consultation",
        "form_intro":
            "You will receive acknowledgement of receipt within "
            "forty-eight working hours from the practice's "
            "secretariat, together with the offer of three available "
            "time slots and the indication of the notary in charge "
            "of your category of deed. Data are processed pursuant "
            "to Regulation EU 679/2016 and held on systems compliant "
            "with the guidelines of the National Council of the "
            "Italian Notariat.",
        "form_fields": [
            {"name": "name", "label": "First name", "type": "text", "required": True,
             "placeholder": "e.g. Anna",
             "helper": "First name only, as it appears on your identity document."},
            {"name": "surname", "label": "Family name", "type": "text", "required": True,
             "placeholder": "e.g. Bianchi",
             "helper": "As it appears on the appearing party's identity document."},
            {"name": "email", "label": "Email address", "type": "email", "required": True,
             "placeholder": "anna.bianchi@example.com",
             "helper": "For preliminary correspondence. We do not use the address for any other purpose."},
            {"name": "phone", "label": "Telephone", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Direct line of the contact person for scheduling."},
            {"name": "capacity", "label": "In the capacity of", "type": "select", "required": True,
             "options": [
                 "Private individual",
                 "Entrepreneur or company shareholder",
                 "Company director",
                 "Heir or legatee",
                 "Professional (accountant, lawyer, estate agent)",
                 "Bank or insurance institution",
             ],
             "helper": "To frame the consultation and identify the notary in charge."},
            {"name": "act_type", "label": "Category of deed", "type": "select", "required": True,
             "options": [
                 "To be defined at the consultation",
                 "Real-estate sale-and-purchase conveyance",
                 "Mortgage loan or subrogation",
                 "Succession or inheritance tax return",
                 "Public will or publication of holographic will",
                 "Incorporation of a company or corporate deed",
                 "Merger, demerger or conversion",
                 "Gift or family agreement",
                 "Special or general power of attorney",
                 "Authentication of signature or certified copy",
             ],
             "helper": "Choose \"To be defined\" if the category is not yet clear."},
            {"name": "timing", "label": "Indicative timing", "type": "select", "required": True,
             "options": [
                 "Within one month",
                 "Within three months",
                 "Within six months",
                 "Exploratory, no defined deadline",
             ],
             "helper": "To schedule the initial consultation and the course of the deed."},
            {"name": "language", "label": "Language of the deed (if relevant)", "type": "select", "required": False,
             "options": [
                 "Italian",
                 "Italian with English translation",
                 "Italian with French translation",
                 "To be discussed at the consultation",
             ],
             "helper": "The practice receives public deeds in Italian, English and French."},
            {"name": "scope", "label": "Brief description of the deed",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Up to 600 characters. Please indicate in outline "
                 "the subject matter of the deed (for example: "
                 "\"sale and purchase of an apartment located in "
                 "Milan, seller's side\"). Third-party data are "
                 "gathered only at the consultation itself, never "
                 "in this form.",
             "helper":
                 "Enough to frame the category of deed and direct "
                 "the matter to the notary in charge. Details are "
                 "discussed at the initial consultation."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact person",
             "meta": "The person who will attend the initial consultation as appearing party.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Position",
             "meta": "To direct the request to the notary in charge.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Category of deed",
             "meta":
                 "No third-party data at this stage — the names of "
                 "counterparties, heirs or contributors are gathered "
                 "at the initial consultation.",
             "fields": ["act_type", "timing", "language", "scope"]},
            {"num": "04", "title": "Preliminary documents (optional)",
             "meta":
                 "Cadastral certificates, prior deeds, floor plans "
                 "or drafts may speed up the framing of the matter.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Preliminary documents",
            "helper":
                "Cadastral certificates, deeds of origin, floor "
                "plans, draft articles of association. PDF / DOCX · "
                "max 15 MB total. Documents are held on an "
                "encrypted archive in accordance with the "
                "guidelines of the National Council of the Italian "
                "Notariat.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Drag the documents here or",
            "link":     "select from your files",
            "meta":     "PDF / DOCX · max 15 MB · encrypted archive",
        },

        "form_submit_label": "Request an initial consultation",
        "form_submit_note":
            "Acknowledgement of receipt within forty-eight working "
            "hours with the offer of three available time slots. "
            "No commercial automation, no BDR, no subsequent "
            "marketing communications.",
        "form_consent":
            "I consent to the processing of personal data pursuant "
            "to Regulation EU 679/2016 and I declare that I have "
            "been informed that the data are held on systems "
            "compliant with the guidelines of the National Council "
            "of the Italian Notariat and of the Notarial Archive. "
            "The data are not disclosed to third parties without "
            "the express written consent of the appearing party.",

        # Office meta-row labels
        "office_address_label": "Address",
        "office_area_label":    "Area",
        "office_phone_label":   "Telephone",
        "office_email_label":   "Email",
        "office_hours_label":   "Hours",

        # Sidebar — single office, direct channels
        "offices_label":   "The office",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Sole office of the practice",
                "address": "Via Manin 12 · 20121",
                "area":    "Porta Nuova · 200 metres from Repubblica M3",
                "phone":   "+39 02 7641 1898",
                "email":   "studio@notaiconti-sironi-verri.it",
                "hours":   "Mon – Fri · 09:00 – 18:30",
            },
        ],

        "channels_label": "Direct channels",
        "channels": [
            ("Practice secretariat",
             "+39 02 7641 1898",
             "Mon – Fri · 09:00 – 18:30"),
            ("Institutional email",
             "studio@notaiconti-sironi-verri.it",
             "Reply within 48 working hours"),
            ("Certified PEC",
             "studio.contisironi@postacertificata.notariato.it",
             "For deeds, notifications and electronic filings"),
        ],

        "footnote":
            "Studio Notarile Conti–Sironi–Verri does not issue "
            "binding opinions by email without an initial "
            "orientation consultation with one of the three "
            "notaries of the association. The schedule of notarial "
            "fees applicable to the specific case is communicated "
            "in writing at the conclusion of the initial "
            "consultation, before any formal instructions are given.",
    },
}


# ─────────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract (locale mirror).
# Every visible string in the lawyer/classic-gold skin templates
# must come from this file (or from chrome.* / dna.content.*) when
# the EN locale is active. Shape-parity with ATTO_CONTENT_IT is the
# contract: every top-level key, nested key and tuple arity matches
# the IT tree. The skin is reused verbatim — locale distinctness lives
# in the content tree, never in the .html files.
# ─────────────────────────────────────────────────────────────────────
