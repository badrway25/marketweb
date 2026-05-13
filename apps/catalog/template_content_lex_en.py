"""Phase 2g3.7 · Session 53 · Lex — English native-voice tree. Bar / cabinet / despacho / مكتب voice."""
from __future__ import annotations

from typing import Any


LEX_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Firm",            "kind": "home"},
        {"slug": "studio",    "label": "The Firm",        "kind": "about"},
        {"slug": "pratiche",  "label": "Practice Areas",  "kind": "services"},
        {"slug": "avvocati",  "label": "Our Lawyers",     "kind": "team"},
        {"slug": "notabili",  "label": "Notable Matters", "kind": "blog_list"},
        {"slug": "contatti",  "label": "Contact",         "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ─────────────────────
    "site": {
        "logo_initial":  "LF",
        "logo_word":     "Studio Legale Ferri",
        "tag":           "Rome Bar · since 1962",
        "phone":         "+39 06 4567 2300",
        "email":         "studio@studioferri.legal",
        "address":       "Via Piemonte 39 · 00187 Roma",
        "hours_compact": "Monday – Friday · 09:00 – 19:00",
        "hours_footer_rows": [
            "Saturday · by appointment only",
            "Sunday · closed",
        ],
        "license":       "Rome Bar Roll No. A18449 · VAT 03124770581",
        "nav_cta":       "Request a consultation",
        "footer_intro":
            "Studio Legale Ferri — sixty-two years of practice, two "
            "offices (Rome and Milan), fourteen members of the Bar. "
            "Competence, discretion, results.",
        "foot_studio":  "The Firm",
        "foot_pages":   "Pages",
        "foot_contact": "Contact",
        "foot_offices": "Offices",
        "offices_footer_rows": [
            "Rome · via Piemonte 39",
            "Milan · corso Venezia 11",
        ],

        # Cross-page meta labels (lifted from skin so each locale picks
        # up the right translation). Used by blog_list/blog_detail and
        # by services / team chrome strips.
        "case_practice_label":  "Practice",
        "case_year_label":      "Year",
        "case_outcome_label":   "Outcome",
        "case_lead_label":      "Lead counsel",
    },

    # ════════════════════════════════════════════════════════════
    # HOME (studio)
    # ════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":    "Studio Legale Ferri · Rome · Milan · since 1962",
        "headline":   "Sixty-two years at the bar, <em>one signature</em> on your file.",
        "intro":
            "We advise undertakings, families and professionals with "
            "a rigorous, tailored and discreet approach. Sixty-two "
            "years of practice, two offices, fourteen members of the "
            "Bar. Every engagement is supervised personally by a "
            "partner of the firm — from the opening of the file to "
            "the final judgment.",
        "primary_cta":   "Request a confidential consultation",
        "primary_href":  "contatti",
        "secondary_cta": "Practice areas",
        "secondary_href":"pratiche",

        # Hero — split-ledger-monogram silhouette
        # LEFT: gold vertical rule + eyebrow + serif drama headline + credit cells
        # RIGHT: monogram crest + meta_strip institutional rows
        "hero_credit_left":  ("Managing partner", "Avv. Prof. A. Ferri"),
        "hero_credit_right": ("Bars",             "Rome · Milan"),
        "hero_meta_strip": [
            ("Head office",       "Rome · via Piemonte"),
            ("Founding partners", "1962 · Ferri family"),
            ("Members of the Bar","14 · Rome Bar"),
        ],

        # Practice-area ledger — 4 numbered rows on home, full 12 on /pratiche
        "practice_label":   "Practice areas",
        "practice_heading": "Twelve disciplines, a single <em>signature</em>.",
        "practice_intro":
            "The firm's practice spans civil, commercial, corporate "
            "criminal and administrative law. Each engagement is "
            "coordinated by a senior partner and never delegated in "
            "full to junior fee-earners.",
        "practice": [
            ("01", "Corporate law",
             "Mergers and acquisitions, governance, commercial "
             "contracts and extraordinary transactions. Capital "
             "increases under Section 2343 of the Italian Civil Code "
             "with sworn appraisal, cross-border mergers, group "
             "restructurings, shareholders' agreements."),
            ("02", "Family law and succession",
             "Uncontested and contested separations, divorces, "
             "custody arrangements, cross-border succession, family "
             "trusts, donations and family pacts under Section "
             "768-bis of the Italian Civil Code."),
            ("03", "Employment law",
             "Individual and collective litigation, second-level "
             "collective bargaining, workplace safety under "
             "Legislative Decree 81/2008, dismissals for just cause "
             "and justified reason, settlements conducted before "
             "union authorities."),
            ("04", "White-collar crime",
             "Corporate offences under Sections 2621–2641 of the "
             "Italian Civil Code, administrative liability of "
             "entities under Legislative Decree 231/2001, white "
             "collar crimes, tax offences under Legislative Decree "
             "74/2000, compliance models and supervisory bodies."),
        ],

        # Stats band on dark ink — counter animation (D-081 binding)
        "stats_label":   "Sixty-two years of practice",
        "stats_heading": "The firm in numbers",
        "stats": [
            ("62",     "years of practice"),
            ("14",     "members of the Bar"),
            ("2,400+", "matters litigated"),
            ("96%",    "favourable outcomes"),
        ],

        # Partners portrait preview — 3 senior partners on home, 14 on /avvocati
        "partners_label":   "Leadership",
        "partners_heading": "Three partners, one direction",
        "partners_intro":
            "The partners of the firm sign every pleading personally. "
            "No engagement is accepted without a prior conflict check "
            "and formal attribution to a responsible partner.",
        "partners": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Managing partner · Corporate law",
                "foro":  "Rome Bar since 1986 · Supreme Court advocate since 1999",
                "bio":
                    "Son of the founder, he has led the firm since "
                    "2004. Associate professor of commercial law at "
                    "LUISS Guido Carli. Author of \"L'aumento di "
                    "capitale nelle società quotate\" (Giuffrè, 2018).",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Senior partner · Family law",
                "foro":  "Rome Bar since 1991 · Supreme Court advocate since 2003",
                "bio":
                    "Specialist in cross-border succession and family "
                    "pacts. Contributor to the journal \"Famiglia e "
                    "Diritto\" since 2007. Accredited family mediator "
                    "with the Mediators' Register of the Court of Rome.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Partner · White-collar crime",
                "foro":  "Rome Bar since 1995 · Supreme Court advocate since 2007",
                "bio":
                    "Former public prosecutor at the Milan Prosecution "
                    "Office (1998–2003), today specialised in Decree "
                    "231 matters and tax offences. Member of the "
                    "supervisory bodies of three industrial groups "
                    "listed on Euronext Milan.",
            },
        ],

        # Publications ribbon — riviste + opere monografiche
        "publications_label": "Publications and citations",
        "publications": [
            "FORO ITALIANO",
            "DIRITTO E GIUSTIZIA",
            "IL SOLE 24 ORE · LEGALE",
            "GUIDA AL DIRITTO",
            "CASSAZIONE PENALE",
            "RIVISTA DELLE SOCIETÀ",
        ],

        # Final CTA band — private-consultation ghost serif
        "cta_label":     "Confidential preliminary consultation",
        "cta_heading":   "A preliminary conversation with a partner.",
        "cta_intro":
            "The initial contact takes place directly with a partner "
            "of the firm. We discuss the scope of the engagement, any "
            "possible conflict of interest and an indicative fee — "
            "before any formal instruction and under the strict "
            "bounds of professional privilege.",
        "cta_primary":      "Request a consultation",
        "cta_primary_href": "contatti",
        "cta_secondary":    "About the firm",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════
    # STUDIO (about) — storia, fondatori, metodo, valori, sedi
    # ════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "The Firm · 1962 — 2026",
        "headline": "Sixty-two years of practice, <em>two generations</em> of the Ferri family.",
        "intro":
            "Studio Legale Ferri was founded in Rome in 1962 by "
            "Avv. Giuseppe Ferri, then a thirty-two-year-old "
            "resigning magistrate, with three corporate-law files "
            "and a single trainee. Sixty-two years on, we are "
            "fourteen members of the Bar, two offices, one unified "
            "governance — together with the independence from "
            "outside capital that the founder enshrined as the "
            "first rule of the partnership deed.",

        # History timeline — sei date che hanno definito lo studio
        "history_label":   "Firm history",
        "history_heading": "Six dates, sixty-two years",
        "history_intro":
            "Six milestones that mark the firm's trajectory — from "
            "the 1962 foundation to the 2004 generational handover, "
            "through to the opening of the Milan office in 2019. "
            "Behind each date lies a structural choice of "
            "independence, practice or geography that continues to "
            "shape our engagements today.",
        "history": [
            ("1962", "Foundation",
             "Avv. Giuseppe Ferri, having resigned from the "
             "magistracy, opened the firm at via Piemonte 39 with "
             "three corporate-law files and a single trainee."),
            ("1978", "Admission to the Supreme Court Bar",
             "After sixteen years of appearances before first- and "
             "second-instance courts, the founder was admitted to "
             "the Special Roll of Supreme Court Advocates — the "
             "civil practice could now appear before the Italian "
             "Supreme Court directly, without local counsel."),
            ("1989", "White-collar crime practice",
             "The firm established an autonomous white-collar crime "
             "department, anticipating by a decade the enactment of "
             "Legislative Decree 231/2001. The first compliance "
             "models were drafted for two industrial groups in the "
             "mechanical engineering sector."),
            ("2004", "Generational handover",
             "Avv. Prof. Alberto Ferri assumed the direction of the "
             "firm. The founder retained the role of Senior of "
             "Counsel until 2014. The partnership deed was updated "
             "to govern the admission of new partners by co-optation "
             "— never by acquisition."),
            ("2014", "International succession practice",
             "Following the entry into force of EU Regulation "
             "650/2012 on cross-border succession, the firm "
             "established a dedicated practice. The first "
             "engagements concerned Italian entrepreneurial "
             "families with assets in Switzerland and Luxembourg."),
            ("2019", "Milan office opens",
             "To support corporate-law and M&A work originating in "
             "northern Italy, the firm opened its second office at "
             "corso Venezia 11. Three partners and two permanent "
             "associates. The two offices operate under a single "
             "governance and share a unified conflict list."),
        ],

        # Method — quattro principi non negoziabili
        "values_label":   "Method",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "The four rules that distinguish a Studio Ferri "
            "engagement from a standard legal instruction. They "
            "appear in our engagement letters — not in marketing "
            "material.",
        "values": [
            ("01", "Absolute confidentiality",
             "Professional privilege under Section 622 of the "
             "Italian Criminal Code is applied in its widest sense: "
             "client identities are never disclosed, not even in "
             "anonymised form, without explicit written consent. "
             "The firm publishes no named case histories and cites "
             "no clients in promotional material."),
            ("02", "A partner for every engagement",
             "Every file is supervised personally by a partner of "
             "the professional association, from opening to final "
             "judgment. The partner signs all material pleadings "
             "and attends substantive hearings. No engagement is "
             "ever delegated in full to junior fee-earners."),
            ("03", "Rigorous conflict check",
             "Before accepting any new engagement, our in-house "
             "Compliance Officer verifies the absence of conflicts "
             "of interest across the active client roster and "
             "engagements closed within the previous five years. "
             "Where any doubt arises, the engagement is declined "
             "pre-emptively."),
            ("04", "Transparent fee arrangements",
             "Professional fees are agreed in writing within the "
             "engagement letter, in accordance with the parameters "
             "set out in Ministerial Decree 55/2014. Success fees "
             "are permitted only within the limits of the Italian "
             "Code of Professional Conduct. No reverse commissions, "
             "no verbal understandings with counterparties."),
        ],

        # Coordinates strip — le due sedi
        "coordinates_label": "Our offices",
        "coordinates": [
            ("Rome",    "Via Piemonte 39 · 00187 · Quirinale district"),
            ("Milan",   "Corso Venezia 11 · 20121 · Porta Venezia district"),
        ],

        # Page-level CTA
        "cta_heading":  "A confidential preliminary assessment.",
        "cta_intro":
            "The initial meeting takes place directly with a "
            "partner of the firm. We discuss the scope of the "
            "engagement, any possible conflict of interest and an "
            "indicative fee, under the strict bounds of "
            "confidentiality.",
        "cta_primary":      "Request a consultation",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # PRATICHE (services) — 12 aree di pratica
    # ════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Practice Areas · 2026",
        "headline": "Twelve disciplines, a single <em>signature</em>.",
        "intro":
            "The firm's twelve practice areas. Every client benefits "
            "from a multidisciplinary team — there is no separate "
            "charge for each practice; the engagement covers the "
            "combination of disciplines required to resolve the "
            "matter at hand.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":     "Responsible partner",
        "svc_jurisdiction_label": "Bar",

        # 12 services in airy ledger
        "services": [
            {
                "num":     "01",
                "title":   "Corporate law",
                "blurb":
                    "Company incorporation, governance, shareholders' "
                    "agreements and extraordinary transactions. "
                    "Capital increases under Section 2343 of the "
                    "Italian Civil Code with sworn appraisal, "
                    "cross-border mergers under Legislative Decree "
                    "108/2008, heterogeneous conversions, "
                    "proportional and non-proportional de-mergers.",
                "scope": [
                    "Incorporation and constitutional documents",
                    "Capital increases and Section 2343 appraisals",
                    "Shareholders' agreements and governance",
                    "Mergers, de-mergers, conversions",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Rome · Milan · Brussels Bars",
            },
            {
                "num":     "02",
                "title":   "M&A and extraordinary transactions",
                "blurb":
                    "Due diligence, drafting of share purchase "
                    "agreements and shareholders' agreements, "
                    "negotiation, post-deal integration. We act "
                    "either for the vendor or for the acquirer — "
                    "never both on the same transaction. Typical "
                    "matters: carve-outs, joint ventures, private "
                    "equity exits, family management buy-outs.",
                "scope": [
                    "Vendor-side legal due diligence",
                    "Buyer-side due diligence and SPA",
                    "Shareholders' agreements and earn-outs",
                    "Hundred-day post-merger integration",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Rome · Milan Bars",
            },
            {
                "num":     "03",
                "title":   "Family law",
                "blurb":
                    "Uncontested and contested separations, "
                    "divorces, custody arrangements for minors, "
                    "amendments to separation and divorce terms. "
                    "Family mediation in pre-litigation phases under "
                    "Section 5 of Legislative Decree 28/2010.",
                "scope": [
                    "Uncontested and contested separations",
                    "Contested and joint divorces",
                    "Custody and maintenance of minors",
                    "Family mediation",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Rome · Milan Bars",
            },
            {
                "num":     "04",
                "title":   "Succession and wealth planning",
                "blurb":
                    "Domestic and cross-border succession under "
                    "EU Regulation 650/2012, drafting of notarial "
                    "and holographic wills, estate divisions, "
                    "donations and family pacts under Section "
                    "768-bis of the Italian Civil Code. Family "
                    "trusts governed by the Hague Convention.",
                "scope": [
                    "International succession planning",
                    "Wills and family pacts",
                    "Estate divisions and arbitration",
                    "Family trusts and foundations",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Rome · Milan · Lugano Bars",
            },
            {
                "num":     "05",
                "title":   "Employment law",
                "blurb":
                    "Individual and collective litigation, "
                    "second-level collective bargaining, workplace "
                    "safety under Legislative Decree 81/2008, "
                    "dismissals under Section 18 of the Workers' "
                    "Statute and the Jobs Act, settlements before "
                    "union authorities under Section 411 of the "
                    "Italian Code of Civil Procedure.",
                "scope": [
                    "Individual and collective employment litigation",
                    "Dismissals for just cause and objective reasons",
                    "Second-level collective bargaining",
                    "Workplace safety and Decree 81/2008",
                ],
                "lead":   "Avv. Federica Ronchi",
                "jurisdiction": "Rome · Milan Bars",
            },
            {
                "num":     "06",
                "title":   "White-collar crime",
                "blurb":
                    "Corporate offences under Sections 2621–2641 of "
                    "the Italian Civil Code, administrative "
                    "liability of entities under Legislative Decree "
                    "231/2001, white-collar crimes, tax offences "
                    "under Legislative Decree 74/2000. Defence of "
                    "directors, statutory auditors and members of "
                    "supervisory bodies.",
                "scope": [
                    "Defence in Decree 231 proceedings",
                    "Corporate and tax offences",
                    "Compliance models and supervisory bodies",
                    "Internal investigations and whistleblowing",
                ],
                "lead":   "Avv. Lorenzo Marchetti",
                "jurisdiction": "Rome · Milan · Supreme Court",
            },
            {
                "num":     "07",
                "title":   "Commercial contracts",
                "blurb":
                    "Drafting and negotiation of Italian and "
                    "international commercial contracts — "
                    "distribution, agency, franchising, joint "
                    "ventures, licensing. Vienna Convention 1980 "
                    "on the international sale of goods.",
                "scope": [
                    "Distribution and commercial agency",
                    "Franchising and joint ventures",
                    "Intellectual property licensing and know-how",
                    "International contracts (CISG)",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Rome · Milan · Brussels Bars",
            },
            {
                "num":     "08",
                "title":   "Banking and finance",
                "blurb":
                    "Financing transactions, real and personal "
                    "security, banking litigation, compound interest, "
                    "usury, renegotiations, derivatives. Bank of "
                    "Italy supervision, CRR/CRD IV regulation, "
                    "Market Abuse Regulation and market abuse.",
                "scope": [
                    "Corporate and LBO financing",
                    "Banking litigation and usury claims",
                    "Derivative instruments (IRS, FX)",
                    "Bank of Italy supervision · MAR",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Rome · Milan Bars",
            },
            {
                "num":     "09",
                "title":   "Administrative law",
                "blurb":
                    "Litigation before the Regional Administrative "
                    "Courts and the Council of State, public "
                    "procurement under Legislative Decree 36/2023, "
                    "concessions, planning permissions, right of "
                    "access to records under Law 241/1990, "
                    "extraordinary appeals to the Head of State.",
                "scope": [
                    "Public procurement and concessions",
                    "Planning permissions and EIA",
                    "Right of access and transparency",
                    "TAR and Council of State appeals",
                ],
                "lead":   "Avv. Giulio Mancini",
                "jurisdiction": "Rome · TAR Lazio",
            },
            {
                "num":     "10",
                "title":   "Real estate",
                "blurb":
                    "Acquisitions and disposals of real estate "
                    "portfolios, development transactions, real "
                    "estate funds, commercial leases, condominium "
                    "litigation. Planning and land registry "
                    "verifications, notarial deeds coordinated with "
                    "trusted notaries.",
                "scope": [
                    "Real estate acquisitions and disposals",
                    "Development and real estate funds",
                    "Commercial leases (Law 392/78)",
                    "Condominium litigation",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Rome · Milan Bars",
            },
            {
                "num":     "11",
                "title":   "Data protection",
                "blurb":
                    "Compliance with EU Regulation 679/2016 (GDPR), "
                    "data mapping, DPIA, appointment of DPOs, "
                    "records of processing activities, data breach "
                    "management, litigation before the Italian Data "
                    "Protection Authority. AI Act and algorithmic "
                    "profiling.",
                "scope": [
                    "GDPR compliance and DPIA",
                    "DPO appointments and processing records",
                    "Data breaches and regulator notifications",
                    "AI Act and algorithmic profiling",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Rome · Milan Bars",
            },
            {
                "num":     "12",
                "title":   "Arbitration and ADR",
                "blurb":
                    "Ad hoc and institutional arbitration (CCI, "
                    "CAM, ICC, LCIA), civil and commercial "
                    "mediation under Legislative Decree 28/2010, "
                    "assisted negotiation under Law Decree "
                    "132/2014, contractual expert determinations.",
                "scope": [
                    "Arbitration CCI / CAM / ICC / LCIA",
                    "Civil and commercial mediation",
                    "Assisted negotiation",
                    "Contractual expertise and arbitrage",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Rome · Milan · Chamber of Arbitration",
            },
        ],

        # Process strip — come si svolge un mandato
        "process_label":   "Engagement process",
        "process_heading": "Four stages, one sequence",
        "process": [
            ("01", "Confidential preliminary meeting",
             "Initial meeting with a partner of the firm. We "
             "discuss the scope, any possible conflict of interest "
             "and an indicative fee. No written proposal at this "
             "stage — only a feasibility assessment."),
            ("02", "Engagement letter",
             "Within five days, a written engagement letter "
             "detailing scope, deliverables, timeline and "
             "professional fees pursuant to Ministerial Decree "
             "55/2014. The engagement is formalised only upon "
             "signature by both parties."),
            ("03", "Execution and representation",
             "The responsible partner signs all material pleadings "
             "personally and attends substantive hearings. The "
             "client receives periodic written reports on the "
             "status of the file — never through unencrypted "
             "electronic channels."),
            ("04", "Closure and archiving",
             "Upon final judgment or closure of the engagement, a "
             "confidential closing letter is issued summarising the "
             "outcome and providing a final opinion. Files are "
             "stored in an encrypted archive for ten years in "
             "accordance with the Italian Code of Professional "
             "Conduct."),
        ],

        # Final CTA
        "cta_heading":  "Which practice applies to your matter?",
        "cta_intro":
            "If the scope of the matter is not yet clear, please "
            "send a brief description of the issue to the firm's "
            "secretariat. We will direct you to the responsible "
            "partner within forty-eight hours, even where the "
            "engagement ultimately falls outside our acceptance "
            "criteria.",
        "cta_primary":      "Write to us",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # AVVOCATI (team) — 14 avvocati abilitati
    # ════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "Our Lawyers · 14 members of the Bar",
        "headline": "Fourteen lawyers, <em>one</em> direction.",
        "intro":
            "The firm comprises fourteen lawyers admitted to the "
            "Rome and Milan Bars — six partners of the professional "
            "association and eight associates. Admission is by "
            "co-optation, not by acquisition: each new partner "
            "requires unanimous approval.",

        # Card meta labels
        "lawyer_foro_label":  "Bar",
        "lawyer_year_label":  "Admitted",
        "lawyer_specialization_label": "Specialisation",

        # 14 avvocati — 6 soci + 8 associati
        "lawyers": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Managing partner",
                "specialization": "Corporate law · M&A · Arbitration",
                "foro":  "Rome Bar",
                "year":  "Admitted 1986 · Supreme Court advocate since 1999",
                "bio":
                    "Son of the founder, he has led the firm since "
                    "2004. Associate professor of commercial law at "
                    "LUISS Guido Carli. Author of \"L'aumento di "
                    "capitale nelle società quotate\" (Giuffrè, "
                    "2018) and of numerous articles in the "
                    "\"Rivista delle Società\".",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Senior partner",
                "specialization": "Family law · Succession",
                "foro":  "Rome Bar",
                "year":  "Admitted 1991 · Supreme Court advocate since 2003",
                "bio":
                    "Specialist in cross-border succession and "
                    "family pacts. Contributor to the journal "
                    "\"Famiglia e Diritto\" since 2007. Accredited "
                    "family mediator with the Mediators' Register "
                    "of the Court of Rome.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Partner",
                "specialization": "White-collar crime · Decree 231",
                "foro":  "Rome Bar · Supreme Court",
                "year":  "Admitted 1995 · Supreme Court advocate since 2007",
                "bio":
                    "Former public prosecutor at the Public "
                    "Prosecutor's Office in Milan (1998–2003). "
                    "Member of the supervisory bodies of three "
                    "industrial groups listed on Euronext Milan. "
                    "Lecturer at the School of Specialisation for "
                    "the Legal Professions.",
            },
            {
                "name":  "Avv. Federica Ronchi",
                "role":  "Partner",
                "specialization": "Employment law · Safety",
                "foro":  "Rome · Milan Bars",
                "year":  "Admitted 1999",
                "bio":
                    "Specialist in collective redundancies and "
                    "second-level collective bargaining. Adviser "
                    "to three major industrial undertakings on "
                    "union negotiations. Member of the Equal "
                    "Opportunities Committee of the Rome Bar.",
            },
            {
                "name":  "Avv. Stefano Bellini",
                "role":  "Partner",
                "specialization": "Commercial contracts · Real estate",
                "foro":  "Rome · Brussels Bars",
                "year":  "Admitted 2001",
                "bio":
                    "Expert in international commercial contracts "
                    "and complex real estate transactions. Admitted "
                    "to the Brussels Bar for EU-law practice. "
                    "LL.M. in International Business Law, "
                    "Université Libre de Bruxelles.",
            },
            {
                "name":  "Avv. Caterina Albini",
                "role":  "Partner",
                "specialization": "Banking · Data protection & GDPR",
                "foro":  "Milan Bar",
                "year":  "Admitted 2003",
                "bio":
                    "Coordinates the banking practice of the Milan "
                    "office. Specialist in derivatives and complex "
                    "financial instruments. Certified DPO under "
                    "UNI 11697:2017. Author of \"GDPR e "
                    "responsabilità del titolare\" (Wolters Kluwer, "
                    "2021).",
            },
            {
                "name":  "Avv. Giulio Mancini",
                "role":  "Of counsel",
                "specialization": "Administrative law · Procurement",
                "foro":  "Rome Bar · TAR Lazio",
                "year":  "Admitted 1998",
                "bio":
                    "Former judge of the TAR Lazio (2002–2014), "
                    "today private counsel in litigation before "
                    "the Regional Administrative Courts and the "
                    "Council of State. Specialist in public "
                    "procurement and service concessions. Member "
                    "of the Board of AIDA.",
            },
            {
                "name":  "Avv. Beatrice Lazzaro",
                "role":  "Associate",
                "specialization": "White-collar crime · Internal investigations",
                "foro":  "Rome Bar",
                "year":  "Admitted 2008",
                "bio":
                    "Member of the white-collar crime practice "
                    "since 2010. Specialised in corporate internal "
                    "investigations and whistleblowing under "
                    "Legislative Decree 24/2023. Lecturer on the "
                    "Master in Compliance 231 at LUMSA University.",
            },
            {
                "name":  "Avv. Marco Vergani",
                "role":  "Associate",
                "specialization": "M&A · Corporate law",
                "foro":  "Milan Bar",
                "year":  "Admitted 2011",
                "bio":
                    "Coordinator of the Milan office for mid-market "
                    "M&A transactions. Previous experience in a "
                    "leading international firm. Specialist in "
                    "cross-border Italy–DACH transactions, in "
                    "particular with German and Swiss counterparties.",
            },
            {
                "name":  "Avv. Sara Donati",
                "role":  "Associate",
                "specialization": "Family law · Minors",
                "foro":  "Rome Bar",
                "year":  "Admitted 2013",
                "bio":
                    "Specialised in custody proceedings for minors "
                    "and in proceedings before the Juvenile Court. "
                    "Court-appointed guardian ad litem in adoption "
                    "proceedings. Master's degree in Family Law at "
                    "Roma Tre University.",
            },
            {
                "name":  "Avv. Tommaso Ricci",
                "role":  "Associate",
                "specialization": "Employment · Collective litigation",
                "foro":  "Milan Bar",
                "year":  "Admitted 2014",
                "bio":
                    "Milan office. Specialised in collective "
                    "employment litigation and proceedings under "
                    "Law 223/1991 (collective redundancies). "
                    "Previous in-house experience at the legal "
                    "department of a listed industrial group in "
                    "manufacturing.",
            },
            {
                "name":  "Avv. Elisa Falcone",
                "role":  "Associate",
                "specialization": "Banking · Usury litigation",
                "foro":  "Milan Bar",
                "year":  "Admitted 2015",
                "bio":
                    "Specialised in banking litigation and in "
                    "actions for the declaration of compound "
                    "interest and usury. Coordinates the banking "
                    "section of the Milan office. Master's degree "
                    "in Banking Law at Bocconi University.",
            },
            {
                "name":  "Avv. Riccardo Zambelli",
                "role":  "Associate",
                "specialization": "Administrative · Planning",
                "foro":  "Rome Bar · TAR Lazio",
                "year":  "Admitted 2016",
                "bio":
                    "Member of the administrative law practice "
                    "with a focus on planning, environmental "
                    "impact assessment (EIA) and landscape "
                    "authorisations. Previous experience at the "
                    "legal department of a major infrastructure "
                    "operator.",
            },
            {
                "name":  "Avv. Chiara Tomei",
                "role":  "Associate",
                "specialization": "Data protection · AI Act · Tech",
                "foro":  "Milan Bar",
                "year":  "Admitted 2019",
                "bio":
                    "Specialised in data protection law, with a "
                    "focus on emerging issues in generative "
                    "artificial intelligence and AI Act compliance "
                    "(EU Regulation 2024/1689). Master's degree in "
                    "Law of New Technologies at Pavia University.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════
    # NOTABILI (blog_list) — cause notabili e pubblicazioni
    # ════════════════════════════════════════════════════════════
    "notabili": {
        "eyebrow":  "Notable matters and publications · 2018 — 2026",
        "headline": "Six selected engagements, <em>observing in full</em> the duty of confidentiality.",
        "intro":
            "A selection of notable matters and recent "
            "publications. In observance of professional "
            "privilege and Section 622 of the Italian Criminal "
            "Code, client identities are never disclosed: matters "
            "are identified by industrial sector and technical "
            "scope; publications by journal and subject matter.",

        # Lead post + list — 6 posts referenced below
        "lead_image": "https://images.pexels.com/photos/5668858/pexels-photo-5668858.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
    },

    # Posts powering blog_detail. URL: /notabili/<slug>/
    "posts": [
        {
            "slug":     "aumento-capitale-quotata-2343cc",
            "kicker":   "Corporate law",
            "title":    "Capital increase under Section 2343 of the Italian Civil Code for a listed company · sworn appraisal · 2024",
            "date":     "March 2024",
            "read_min": "8",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "On instruction of a listed industrial group "
                "operating in the energy sector, the firm assisted "
                "the board of directors in the resolution and "
                "execution of an in-kind capital increase of EUR "
                "145 million, involving the contribution of a "
                "foreign subsidiary valued by sworn appraisal under "
                "Section 2343 of the Italian Civil Code.",
            "body": [
                ("p",
                 "The engagement covered the entire deliberative "
                 "phase — from the drafting of the board's "
                 "explanatory report under Section 2441 of the "
                 "Italian Civil Code through to the appointment by "
                 "the Court of Rome of the expert tasked with the "
                 "sworn appraisal of the contributed subsidiary."),
                ("h2", "Regulatory framework"),
                ("p",
                 "The transaction was carried out in full compliance "
                 "with Section 2343 of the Italian Civil Code (sworn "
                 "appraisal) and Section 2441 of the Italian Civil "
                 "Code (pre-emption rights), with the exclusion of "
                 "pre-emption rights in favour of an institutional "
                 "investor identified by the board. The procedure "
                 "required a specific report from the board of "
                 "statutory auditors under Section 2441, paragraph "
                 "6, of the Italian Civil Code."),
                ("h2", "The firm's role"),
                ("p",
                 "The firm coordinated relations with Consob for "
                 "the filing of the offer prospectus, with the "
                 "Court of Rome for the appointment of the expert, "
                 "with the notary for the recording of the "
                 "extraordinary general meeting and with the "
                 "auditor for subsequent verifications under "
                 "Section 2343-bis of the Italian Civil Code."),
                ("blockquote",
                 "Compliance with the procedure under Section 2343 "
                 "of the Italian Civil Code is a condition of the "
                 "validity of the capital increase. Any operational "
                 "shortcut that seeks to compress the statutory "
                 "time limits exposes the transaction to the risk "
                 "of nullity."),
            ],
        },
        {
            "slug":     "modello-231-gruppo-utility",
            "kicker":   "White-collar crime",
            "title":    "Compliance model under Legislative Decree 231/2001 for a listed utility group",
            "date":     "November 2024",
            "read_min": "11",
            "author":   "Avv. Lorenzo Marchetti",
            "lede":
                "The firm drafted the compliance model under "
                "Legislative Decree 231/2001 for a listed utility "
                "group, following the renewal of its supervisory "
                "body. The engagement encompassed the mapping of "
                "predicate-offence risks, the design of operating "
                "protocols and internal training for sixty-two "
                "senior managers.",
            "body": [
                ("p",
                 "The engagement lasted nine months and proceeded "
                 "along three parallel workstreams: mapping of "
                 "predicate-offence risks, redesign of operating "
                 "protocols and mandatory training for exposed "
                 "personnel."),
                ("h2", "Predicate-offence risk mapping"),
                ("p",
                 "The twenty-two predicate offences relevant to "
                 "the utilities sector were mapped, with particular "
                 "attention to environmental offences under Section "
                 "25-undecies of Legislative Decree 231/2001 and "
                 "offences against public administration under "
                 "Section 25 of the same Decree. The mapping "
                 "exercise required interviews with forty process "
                 "owners."),
                ("h2", "Protocol design"),
                ("p",
                 "The operating protocols were redesigned in "
                 "accordance with the principles of segregation of "
                 "duties and documentary traceability. Particular "
                 "attention was paid to procurement processes, "
                 "public tenders and relations with the public "
                 "administration."),
            ],
        },
        {
            "slug":     "successione-internazionale-reg-650",
            "kicker":   "International succession",
            "title":    "Cross-border succession under EU Regulation 650/2012 · entrepreneurial family Italy–Switzerland",
            "date":     "September 2024",
            "read_min": "9",
            "author":   "Avv. Maria Grazia Conti",
            "lede":
                "For an entrepreneurial family from north-eastern "
                "Italy holding assets in Italy, Switzerland and "
                "Luxembourg, the firm coordinated the opening of "
                "the succession of the deceased — domiciled in "
                "Lugano for over twenty years — pursuant to EU "
                "Regulation 650/2012.",
            "body": [
                ("p",
                 "The succession raised complex private "
                 "international law questions, in particular "
                 "concerning the professio iuris under Article 22 "
                 "of Regulation 650/2012 in favour of Italian law, "
                 "exercised by the deceased through a holographic "
                 "will drawn up in Lugano in 2018."),
                ("h2", "Multi-jurisdictional coordination"),
                ("p",
                 "The firm coordinated relations with the Italian "
                 "notary for the acceptance of the inheritance, "
                 "with the Swiss fiduciary for the division of "
                 "bank accounts and with the Luxembourg Bar for "
                 "the liquidation of a Luxembourg holding company."),
                ("h2", "Outcome"),
                ("p",
                 "The entire procedure was concluded within "
                 "fourteen months, with a division agreement "
                 "ratified before a notary in Rome. No judicial "
                 "proceedings arose; inheritance tax was assessed "
                 "on a scheduled basis."),
            ],
        },
        {
            "slug":     "ferri-aumento-capitale-giuffre-2018",
            "kicker":   "Monograph",
            "title":    "\"L'aumento di capitale nelle società quotate\" · Giuffrè · 2018",
            "date":     "2018",
            "read_min": "5",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "The monograph, published by Giuffrè Francis "
                "Lefebvre in 2018, draws on the author's "
                "professional experience in capital increases for "
                "companies listed on Italian regulated markets. "
                "The work is today adopted by three Italian "
                "universities as a reference text for commercial "
                "law courses.",
            "body": [
                ("p",
                 "The volume is organised into twelve chapters "
                 "covering the various types of capital increase: "
                 "in cash, in kind, bonus issues, reserved issues, "
                 "and those with exclusion of pre-emption rights."),
                ("h2", "Structure of the work"),
                ("p",
                 "The first four chapters address the general "
                 "regime under Sections 2438–2444 of the Italian "
                 "Civil Code. The central chapters examine special "
                 "cases — increases delegated to the board, "
                 "divisible and indivisible increases, increases "
                 "with warrants. The final three chapters are "
                 "devoted to the peculiarities of listed "
                 "companies."),
            ],
        },
        {
            "slug":     "licenziamento-collettivo-l-223-91",
            "kicker":   "Employment law",
            "title":    "Collective redundancy procedure under Law 223/1991 · manufacturing group",
            "date":     "May 2024",
            "read_min": "7",
            "author":   "Avv. Federica Ronchi",
            "lede":
                "The firm assisted a manufacturing group in the "
                "mechanical engineering sector in a collective "
                "redundancy procedure under Law 223/1991, "
                "concluded through a union agreement and the "
                "reassignment of 78% of the surplus workforce.",
            "body": [
                ("p",
                 "The procedure concerned one hundred and forty "
                 "positions and was conducted in two phases — "
                 "joint examination at company level under Section "
                 "4 of Law 223/1991 and subsequent examination at "
                 "ministerial level before the Ministry of "
                 "Labour."),
                ("h2", "The union agreement"),
                ("p",
                 "The agreement, signed by all representative "
                 "trade unions, provided for the activation of a "
                 "bilateral retraining fund, voluntary redundancy "
                 "incentives for older workers and an internal "
                 "reassignment plan for the remaining staff."),
                ("h2", "Quantitative outcome"),
                ("p",
                 "Of the one hundred and forty employees "
                 "concerned, twenty-eight accepted voluntary "
                 "redundancy incentives, eighty-three were "
                 "reassigned to other production lines and "
                 "twenty-nine were supported by the bilateral "
                 "outplacement fund."),
            ],
        },
        {
            "slug":     "carve-out-dach-mid-cap-2023",
            "kicker":   "Cross-border M&A",
            "title":    "Carve-out and disposal of an industrial division to a German operator · 2023",
            "date":     "December 2023",
            "read_min": "10",
            "author":   "Avv. Marco Vergani",
            "lede":
                "The firm acted sell-side on the carve-out and "
                "disposal of an industrial division (EUR 112 "
                "million in annual revenues) to a German "
                "strategic operator, completed in the fourth "
                "quarter of 2023 after twenty-two weeks of "
                "negotiation.",
            "body": [
                ("p",
                 "The engagement covered the entire carve-out "
                 "transaction — from the preparation of the "
                 "teaser through the negotiation of the share "
                 "purchase agreement and into the first six weeks "
                 "of post-merger integration."),
                ("h2", "The phases"),
                ("ol", [
                    "Preparation of teaser and information memorandum",
                    "Vendor due diligence (legal, tax, employment)",
                    "Private auction among four potential acquirers",
                    "Negotiation of SPA and shareholders' agreement",
                    "Closing and hundred-day post-merger integration",
                ]),
                ("h2", "The result"),
                ("p",
                 "The disposal was completed at market EBITDA "
                 "multiple (8.4x), with an earn-out clause over "
                 "two financial years. One hundred per cent of "
                 "the contracts with the three leading DACH "
                 "customers were renewed within the six months "
                 "following closing."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════
    # CONTATTI (contact) — 2 sedi, form riservato
    # ════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Confidential preliminary consultation",
        "headline": "A preliminary conversation with a <em>partner of the firm</em>.",
        "intro":
            "The initial contact takes place directly with a "
            "partner of the professional association. We discuss "
            "the scope of the engagement, any possible conflict of "
            "interest and an indicative fee — under the bounds of "
            "professional privilege pursuant to Section 622 of the "
            "Italian Criminal Code, before any formal instruction.",

        # Form fields
        "form_label":   "Confidential form",
        "form_heading": "Complete the confidential form",
        "form_intro":
            "You will receive an acknowledgement of receipt within "
            "forty-eight working hours, signed by the partner "
            "responsible for the requested area. Information is "
            "processed in accordance with EU Regulation 679/2016 "
            "and held in an encrypted archive with access restricted "
            "to partners of the firm.",
        "form_fields": [
            {"name": "name", "label": "First name", "type": "text", "required": True,
             "placeholder": "e.g. Alexander",
             "helper": "Given name only, thank you."},
            {"name": "surname", "label": "Surname", "type": "text", "required": True,
             "placeholder": "e.g. Costa",
             "helper": "As shown on your identity document."},
            {"name": "email", "label": "Email address", "type": "email", "required": True,
             "placeholder": "alexander.costa@example.com",
             "helper": "For preliminary correspondence. We will not use your address for any other purpose."},
            {"name": "phone", "label": "Telephone", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Direct line of the point of contact, not a switchboard."},
            {"name": "capacity", "label": "Acting as", "type": "select", "required": True,
             "options": [
                 "Private individual",
                 "Entrepreneur or shareholder",
                 "Director or statutory auditor",
                 "General counsel of industrial group",
                 "Professional (accountant, notary, etc.)",
             ],
             "helper": "Helps us orient the preliminary meeting."},
            {"name": "practice", "label": "Practice area", "type": "select", "required": True,
             "options": [
                 "To be determined in meeting",
                 "Corporate law",
                 "M&A and extraordinary transactions",
                 "Family law",
                 "Succession and wealth planning",
                 "Employment law",
                 "White-collar crime",
                 "Commercial contracts",
                 "Banking and finance",
                 "Administrative law",
                 "Real estate",
                 "Data protection",
                 "Arbitration and ADR",
             ],
             "helper": "Select \"To be determined\" if the matter spans several areas."},
            {"name": "urgency", "label": "Urgency", "type": "select", "required": True,
             "options": [
                 "Within the current week",
                 "Within one month",
                 "Within three months",
                 "Exploratory, no urgency",
             ],
             "helper": "Helps us schedule the relevant partner."},
            {"name": "perimeter", "label": "Brief description of the matter",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Maximum 800 characters. Names of counterparties, "
                 "subsidiaries or third parties are disclosed only "
                 "after mutual NDA has been signed — never in this "
                 "form.",
             "helper":
                 "Sufficient for us to carry out the preliminary "
                 "conflict check and assign the file to the "
                 "responsible partner. Sensitive details are "
                 "discussed in person."},
        ],

        "form_sections": [
            {"num": "01", "title": "Point of contact",
             "meta": "The person who will sign any eventual engagement letter.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Capacity",
             "meta": "For the preliminary conflict check.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Subject of the consultation",
             "meta":
                 "No counterparty names here — technical scope is "
                 "discussed in the meeting following mutual NDA.",
             "fields": ["practice", "urgency", "perimeter"]},
            {"num": "04", "title": "Attachments (optional)",
             "meta":
                 "Preliminary documents, organisation charts or "
                 "standard NDAs may expedite the meeting.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Preliminary documents",
            "helper":
                "Preliminary documents, corporate organisation chart "
                "or standard NDA. PDF / DOCX · 15 MB maximum "
                "combined. Encrypted archive with access restricted "
                "to partners of the firm.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Drag documents here or",
            "link":     "select from your files",
            "meta":     "PDF / DOCX · 15 MB max · encrypted archive",
        },

        "form_submit_label": "Submit confidential request",
        "form_submit_note":
            "Acknowledgement signed by a partner within forty-eight "
            "working hours. No business development, no automation, "
            "no commercial communications.",
        "form_consent":
            "I consent to the processing of personal data pursuant "
            "to EU Regulation 679/2016 and acknowledge that the "
            "data is held in an encrypted archive with access "
            "restricted to partners of Studio Legale Ferri. Data "
            "is not disclosed to third parties without explicit "
            "written consent.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Address",
        "office_area_label":    "District",
        "office_phone_label":   "Telephone",
        "office_email_label":   "Email",
        "office_hours_label":   "Hours",

        # Sidebar — sedi + canali diretti
        "offices_label":   "Our offices",
        "offices": [
            {
                "city":    "Rome",
                "tag":     "Head office",
                "address": "Via Piemonte 39 · 00187",
                "area":    "Quirinale · near Piazza Barberini",
                "phone":   "+39 06 4567 2300",
                "email":   "roma@studioferri.legal",
                "hours":   "Mon – Fri · 09:00 – 19:00",
            },
            {
                "city":    "Milan",
                "tag":     "Milan office",
                "address": "Corso Venezia 11 · 20121",
                "area":    "Porta Venezia · near Giardini Pubblici",
                "phone":   "+39 02 7634 5500",
                "email":   "milano@studioferri.legal",
                "hours":   "Mon – Fri · 09:00 – 19:00",
            },
        ],

        "channels_label": "Direct channels",
        "channels": [
            ("Firm secretariat",
             "+39 06 4567 2300",
             "Mon – Fri · 09:00 – 19:00"),
            ("Institutional email",
             "studio@studioferri.legal",
             "Response within 48 working hours"),
            ("Certified email (PEC)",
             "studio.ferri@cert.ordineavvocatiroma.it",
             "For pleadings and notifications"),
        ],

        "footnote":
            "Studio Legale Ferri does not provide preliminary "
            "opinions by email without a first meeting with a "
            "partner. Administrative information (indicative fee "
            "parameters, invoicing arrangements, criteria for "
            "acceptance of an engagement) is presented during the "
            "confidential preliminary meeting, never in writing at "
            "the preliminary stage.",
    },
}


# ─────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract.
# Every visible string in the lawyer/classic-gold skin templates
# must come from THIS file (or from chrome.* / dna.content.*).
# Zero literal "Ferri", "1962", "Roma", "Via Piemonte", partner
# names, headline text, or other brand-specific strings in the
# .html files. When a new label is needed in the skin, add it here
# first (preferably under `site` if shared across pages, or under
# the page block if scoped) and read it via `{{ page_data.* }}` /
# `{{ site.* }}`.
# ─────────────────────────────────────────────────────────────────
