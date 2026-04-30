"""Continua — Family-office stewardship (corporate-suite archetype) ·
English locale content tree.

Phase X.4b Continua Pass B · 2026-04-30 · Multilingual rollout pass on
top of the approved LF-5 Italian layout. Mirrors the shape of
``CONTINUA_CONTENT_IT`` exactly — same keys, same nesting, same list
shapes. Only values are translated and adapted.

Voice register: institutional, custodial, longitudinal, multi-
generational. Native English equivalent of the IT register — the family-
office English of Pictet, Cazenove Capital, Stonehage Fleming. Adult-to-
adult, declarative, never SaaS-marketing. Reference voices: STEP Journal,
The Wealth Mosaic, Family Capital column.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved verbatim-in-translation
across all 5 locales · the load-bearing italic moves with the equivalent
TEMPORAL noun):
    "The continuity of a family is measured in <em>generations</em>."

Italian normative references and proper nouns are preserved (D.lgs.
24/2023 whistleblowing, Codice della Crisi, OAM mediazione creditizia,
Albo dei Trustees, STEP, ANC audit, Codice Deontologico, Reg. UE
679/2016, Consiglio di Famiglia / Family Council). Italian addresses,
phone formats, Euro figures and years are kept as-is. Anti-pattern
guardrails carry across: no "Unlock generational wealth", no "Future-
proof your legacy", no "Best version of your family office", no Warren
Buffett / J.P. Morgan / Rockefeller quotes, no boardroom-cliché stock-
photo references.
"""
from __future__ import annotations

from typing import Any


# Pool URLs imported from the IT module — single source of truth so the
# build-time corporate_suite checks see the same registered Pexels URLs
# across every locale. Mirrors the Solaria Pass B precedent.
from apps.catalog.template_content_continua import (  # noqa: E402
    _HERO_IMAGE,
    _PILLAR_ICON_01,
    _PILLAR_ICON_02,
    _PILLAR_ICON_03,
    _PILLAR_ICON_04,
    _PORTRAIT_ELEONORA,
    _PORTRAIT_TOMAS,
    _PORTRAIT_GINEVRA,
)


CONTINUA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "The practice",  "kind": "home"},
        {"slug": "chi-siamo",  "label": "About",          "kind": "about"},
        {"slug": "custodia",   "label": "Stewardship",    "kind": "services"},
        {"slug": "mandati",    "label": "Mandates",       "kind": "case_study_list"},
        {"slug": "contatti",   "label": "Contact",        "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":    "Continua",
        "tag":          "Multi-generational family office · Milan",
        "phone":        "+39 02 7600 4188",
        "email":        "mandato@continua.it",
        "address":      "Via San Marco 22 · 20121 Milan",
        "hours_compact":"Mon – Fri · 9:30 – 18:30 · by appointment",
        "hours_footer_rows": [
            "Saturday · scheduled Family Councils only",
            "Sunday · closed",
        ],
        "license":      "Albo dei Trustees registered · STEP Affiliate · ANC continuity audit",
        "footer_intro":
            "Stewards of family wealth across the generations. An "
            "independent stewardship boutique, custodial mandates set on "
            "a multi-generational horizon, family governance presided "
            "over by the Family Council. Principal office in Milan, "
            "fiduciary correspondents in Lugano and Luxembourg.",
        "foot_studio":   "The practice",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Offices",
        "offices_footer_rows": [
            "Milan · Brera (principal office)",
            "Lugano · Riva Caccia (fiduciary correspondent)",
            "Luxembourg · Boulevard Royal (trustee correspondent)",
        ],
        "whistleblowing_footer": {
            "heading":      "Whistleblowing",
            "eyebrow":      "Internal channel · D.lgs. 24/2023",
            "note":
                "Encrypted channel managed by the Compliance Officer. "
                "Reserved for family members under mandate and Continua "
                "stewards. Fiduciary minute-keeping.",
            "email":        "whistleblowing@continua.it",
            "policy_label": "Whistleblower protection",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Profile",
        "case_year_label":         "Mandate opened",
        "case_duration_label":     "Years in continuity",
        "case_lead_label":         "Lead steward",
        "case_lead_partner_label": "Senior steward",
        "case_team_label":         "Team & cadence",
        "case_timeline_label":     "Continuity milestones",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Family office · Milan · multi-generational stewardship",
        "headline":
            "The continuity of a family is measured in <em>generations</em>.",
        "intro":
            "Stewards of family wealth across the generations. An "
            "independent stewardship boutique — one Family Council, a "
            "mandate that is not measured in quarters, fiduciary "
            "oversight that travels through the passage from fathers to "
            "children to grandchildren.",
        "primary_cta":   "Begin a mandate dialogue",
        "primary_href":  "contatti",
        "secondary_cta": "The custodial practice",
        "secondary_href":"chi-siamo",

        "hero_image":              _HERO_IMAGE,
        "hero_image_credit_left":  ("Mandate stewards", "Albo dei Trustees registered"),
        "hero_image_credit_right": ("Principal office", "Milan · Brera"),
        "hero_meta_strip": [
            ("Mandate horizon",        "18 years average"),
            ("Generations under care", "3"),
            ("Family Councils",        "4 per year"),
        ],

        "pillars_label":   "Stewardship",
        "pillars_heading": "Four practices, <em>one single</em> mandate",
        "pillars_intro":
            "Four practices working in continuity on the same wealth. "
            "Each practice is not billed separately — the mandate covers "
            "the combined custody, governance, succession and compliance "
            "agreed with the family for the declared horizon.",
        "pillars": [
            ("01", "Wealth custody",
             "We hold family wealth across its four layers — liquid "
             "financial assets, industrial holdings, operating real estate "
             "and family real estate — through the cycle of generations, "
             "in coherence with the family pact in force and the "
             "underlying fiduciary mandates."),
            ("02", "Family governance",
             "We facilitate the Family Council on a quarterly cadence, "
             "draft and review the family pact, design branch voting "
             "structures and the codes of conduct shared across "
             "incumbent and incoming generations."),
            ("03", "Structured succession",
             "We plan the multi-generational handover — modulated "
             "donations, family holdings, dedicated trusts, technical "
             "and governance training for the incoming generation "
             "before the actual transfer of decision-making responsibility."),
            ("04", "Fiduciary compliance",
             "Continuous fiduciary oversight, independent annual "
             "continuity audit, evolving regulatory presidio (D.lgs. "
             "24/2023 whistleblowing, Codice della Crisi, OAM credit "
             "mediation) and access-controlled documentary custody on "
             "the family registers."),
        ],

        "pillars_matrix": [
            {
                "num":   "01",
                "title": "Wealth custody",
                "body":
                    "Four layers held in continuity — liquid financial, "
                    "industrial holdings, operating and family real "
                    "estate — coherent with the family pact in force.",
                "icon_image": _PILLAR_ICON_01,
            },
            {
                "num":   "02",
                "title": "Family governance",
                "body":
                    "Quarterly Family Council. Fiduciary minutes. "
                    "Triennially reviewed family pact. Voting structures "
                    "dedicated to each branch.",
                "icon_image": _PILLAR_ICON_02,
            },
            {
                "num":   "03",
                "title": "Structured succession",
                "body":
                    "Family holdings, dedicated trusts, modulated "
                    "donations. Two-year technical training programme "
                    "for the incoming generation.",
                "icon_image": _PILLAR_ICON_03,
            },
            {
                "num":   "04",
                "title": "Fiduciary compliance",
                "body":
                    "Annual ANC continuity audit. AML, Codice della "
                    "Crisi and D.lgs. 24/2023 presidio. Access-controlled "
                    "documentary custody.",
                "icon_image": _PILLAR_ICON_04,
            },
        ],

        "kpi_heading": "Eighteen years of continuing mandates",
        "kpi_strip": [
            ("18",      "years · average mandate horizon"),
            ("3",       "generations · families under care"),
            ("€ 1.8 B", "wealth in custody"),
            ("4",       "Family Councils · per year"),
        ],

        "cycle_label":   "Governance cycle",
        "cycle_heading": "Continuity keeps a <em>cadence</em>, not a deadline.",
        "cycle_intro":
            "Three rhythms that govern the mandate — not KPIs, not tax "
            "deadlines, not coaching sessions. They are the regular "
            "beats of a Family Council, repeated across the years and "
            "carried through the generations.",
        "cycle_strip": [
            ("Family Council cadence", "4 meetings / year",
             "Governance calendar shared with the family · fiduciary "
             "minute-keeping · agenda open to both incumbent generations."),
            ("Continuity audit", "annual",
             "Independent verification of the mandate's multi-year "
             "coherence (ANC) · documentary-custody review · outcome "
             "communicated at the December Family Council."),
            ("Family pact", "triennial review",
             "Update of the internal rules, with or without the incoming "
             "generation at the table · voting and branch-protection "
             "clauses re-discussed every three years."),
        ],

        "sectors_label": "Family profiles",
        "sectors": [
            "Entrepreneurial families",
            "Holding companies",
            "Family foundations",
            "Multi-asset groups",
            "Second generations in transfer",
            "Independent trustees",
            "Representative offices",
            "Foreign single family offices",
        ],

        "trust_label":   "Institutional recognitions",
        "trust_logos":   [
            "ALBO DEI TRUSTEES",
            "STEP AFFILIATE",
            "ANC CONTINUITY AUDIT",
            "OAM CREDIT MEDIATORS",
            "ASSOCIAZIONE BANCHE FIDUCIARIE",
            "FAMILY OFFICE NETWORK ITALIA",
        ],

        "whistleblowing": {
            "eyebrow":      "Whistleblower protection",
            "channel_name": "Internal channel · D.lgs. 24/2023",
        },

        "leadership_label":   "Mandate stewards",
        "leadership_heading": "Three stewards who will sit on your Family Council.",
        "leadership_intro":
            "Every mandate is followed personally by at least one "
            "Senior Steward, who sits on the Family Council from the "
            "opening of the file through to the transition between "
            "generations. No stand-in steward, no unagreed external "
            "side-by-side.",
        "leadership": [
            {
                "name":  "Eleonora Marchesi",
                "role":  "Senior Steward",
                "station": "Archive room · Brera",
                "bio":
                    "Thirty-five years of fiduciary practice between "
                    "Milan and Lugano. Registered with the Albo dei "
                    "Trustees since 2007, she has presided over seven "
                    "continuity mandates spanning three full generations "
                    "and eleven documented intergenerational handovers.",
                "credentials": [
                    "Albo dei Trustees · registered 2007",
                ],
                "portrait": _PORTRAIT_ELEONORA,
            },
            {
                "name":  "Tomas Okafor",
                "role":  "Family Officer",
                "station": "Council table · principal office",
                "bio":
                    "Fourteen years of practice between Anglo-Saxon "
                    "family offices and continental advisory. STEP "
                    "Affiliate since 2014, he coordinates the "
                    "facilitation of the Family Council and the "
                    "technical training of the incoming generation "
                    "before the transfer of responsibility.",
                "credentials": [
                    "STEP Affiliate · 2014",
                ],
                "portrait": _PORTRAIT_TOMAS,
            },
            {
                "name":  "Ginevra Conti",
                "role":  "Compliance Officer",
                "station": "Compliance studio · documentary custody",
                "bio":
                    "Twenty-two years in fiduciary oversight of private "
                    "wealth. OAM-registered as credit mediator since "
                    "2011, she presides over compliance with D.lgs. "
                    "24/2023 (whistleblowing) and the annual continuity "
                    "audit of every mandate under care.",
                "credentials": [
                    "OAM · credit mediators register",
                ],
                "portrait": _PORTRAIT_GINEVRA,
            },
        ],

        "cases_label":   "Continuing mandates",
        "cases_heading": "Four mandates, four generations, <em>one single cadence</em>.",
        "cases_intro":
            "A selection of continuing mandates — not closed, still "
            "under care. The names of the families are disclosed only "
            "under reciprocal fiduciary confidentiality.",

        "cases_timeline": [
            {
                "slug":          "famiglia-b-fondazione-di-famiglia",
                "year":          "2011",
                "eyebrow":       "Family foundation",
                "title":         "Family B · 3rd generation · philanthropic + industrial branch",
                "horizon_label": "Horizon",
                "horizon":       "15 years in continuity · joint audit",
            },
            {
                "slug":          "famiglia-a-quarta-generazione-holding-industriale",
                "year":          "2014",
                "eyebrow":       "Industrial holding",
                "title":         "Family A · 4th generation · six family branches",
                "horizon_label": "Horizon",
                "horizon":       "12 years · mandate renewal 2034",
            },
            {
                "slug":          "famiglia-d-single-family-office-estero",
                "year":          "2017",
                "eyebrow":       "Single family office",
                "title":         "Family D · cross-border custody IT · CH · LU",
                "horizon_label": "Horizon",
                "horizon":       "9 years · AML extension 2030",
            },
            {
                "slug":          "famiglia-c-trasferimento-intergenerazionale",
                "year":          "2019",
                "eyebrow":       "Intergenerational transfer",
                "title":         "Family C · 2nd → 3rd generation · dedicated trusts",
                "horizon_label": "Horizon",
                "horizon":       "Decennial handover · 2026 — 2029",
            },
        ],

        "cta_label":     "A first confidential dialogue",
        "cta_heading":   "The continuity of a family is measured in <em>generations</em>.",
        "cta_intro":
            "The first dialogue takes place with a Senior Steward. We "
            "discuss the mandate's perimeter, the time horizon and any "
            "fiduciary conflict — before any proposal of a Family "
            "Council. We do not sell the first meeting: we offer it "
            "once, free, per family.",
        "cta_primary":   "Begin a mandate dialogue",
        "cta_primary_href": "contatti",
        "cta_secondary": "Download the institutional dossier",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "The practice · 2007 — 2026",
        "headline":  "A custody boutique, <em>nineteen</em> years of continuing mandates.",
        "intro":
            "Continua was born in Milan in 2007 as a custody office for "
            "two Lombard entrepreneurial families. Since then we have "
            "presided over the passage from fathers to children on "
            "seven mandates in total, never by acquisition, never with "
            "third-party capital.",

        "history_label":   "Continuity milestones",
        "history_heading": "Five dates, nineteen years of stewardship.",
        "history_intro":
            "Five structural choices behind which the character of the "
            "practice can be read — independence from third-party "
            "capital, the quarterly cadence of the Family Council, the "
            "annual continuity audit, the triennial family pact, the "
            "intergenerational handover as a method before it is a product.",
        "history": [
            ("2007", "Founding",
             "Eleonora Marchesi and two co-stewards open the practice on "
             "Via San Marco in Milan, on mandate from two Lombard "
             "entrepreneurial families, for wealth custody on a twenty-year horizon."),
            ("2011", "OAM credit-mediator registration",
             "Ginevra Conti joins as Compliance Officer and activates "
             "continuous fiduciary oversight on mandates under care, "
             "following the principle of separation between custody and advisory."),
            ("2014", "STEP Affiliate · Family Officer",
             "Tomas Okafor joins as Family Officer and introduces the "
             "facilitation of the Family Council — four meetings per "
             "year, shared agenda, fiduciary minute-keeping."),
            ("2019", "Continuity audit (ANC)",
             "The practice adopts the ANC protocol for the annual "
             "continuity audit — independent verification of each "
             "mandate's multi-year coherence, outcome always communicated "
             "at the December Family Council."),
            ("2024", "Lugano + Luxembourg fiduciary correspondents",
             "To accompany the intergenerational transfer mandates of "
             "Italian families, we activate fiduciary partnerships at "
             "Riva Caccia and Boulevard Royal — never owned offices, "
             "always accredited correspondents."),
        ],

        "values_label":   "Custodial principles",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "Four principles that distinguish a Continua mandate from a "
            "standard advisory engagement. They are written into the "
            "mandate pact signed at the Family Council, not on the website.",
        "values": [
            ("01", "Independence from third-party capital",
             "The capital of the practice is held entirely by the "
             "active stewards. No fund, no banking group, no external "
             "shareholder. The choice of mandates is never influenced "
             "by third-party agendas that could compromise custody."),
            ("02", "One Senior Steward per mandate",
             "A Senior Steward sits on the Family Council from the "
             "opening of the file to the transfer of responsibility. "
             "No steward-of-record who disappears after the first "
             "dialogue: the steward met at the first meeting is the "
             "one who will sign the intergenerational handover."),
            ("03", "Independent continuity audit",
             "Every mandate is subject, once a year, to a continuity "
             "audit (ANC) conducted by an external reviewer. The "
             "outcome is communicated at the December Family Council "
             "without filter: the family always knows the state of "
             "custody of its wealth."),
            ("04", "Fiduciary confidentiality",
             "No public case study, no newsletter on mandate "
             "performance, no cross-referrals between families. The "
             "anonymisations shown on public pages are agreed case by "
             "case and signed at the Family Council."),
        ],

        "team_label":   "Stewards & officers",
        "team_heading": "Six stewards, three offices, one single cadence.",
        "team_intro":
            "The people who will sit on your Family Council. Stewards, "
            "not consultants, and we do not entrust you to a department "
            "— the steward met at the first meeting is the one who "
            "will preside over the handover between generations.",
        "team": [
            {"name": "Eleonora Marchesi",
             "role": "Senior Steward · Custody",
             "office": "Milan",
             "bio": "Thirty-five years of fiduciary practice. Registered "
                    "with the Albo dei Trustees since 2007 · seven "
                    "continuity mandates across three full generations."},
            {"name": "Tomas Okafor",
             "role": "Family Officer · Governance",
             "office": "Milan",
             "bio": "STEP Affiliate since 2014. Family Council "
                    "facilitation and incoming-generation training "
                    "before the transfer of responsibility."},
            {"name": "Ginevra Conti",
             "role": "Compliance Officer · Fiduciary oversight",
             "office": "Milan",
             "bio": "OAM credit mediator since 2011. Presidio of D.lgs. "
                    "24/2023 (whistleblowing) and of the annual "
                    "continuity audit on every mandate under care."},
            {"name": "Lorenzo Pellegrini",
             "role": "Steward · Structured succession",
             "office": "Milan",
             "bio": "Eighteen years in the generational handover of "
                    "Lombard industrial wealth. Coordinates family "
                    "holdings, dedicated trusts and technical training "
                    "of the incoming generation."},
            {"name": "Camille Béranger",
             "role": "Fiduciary correspondent",
             "office": "Luxembourg",
             "bio": "Twenty years in Luxembourg trust law. Holds "
                    "cross-border structures for Italian families with "
                    "secondary tax residencies."},
            {"name": "Sofia Pessina",
             "role": "Junior Steward · Family pacts",
             "office": "Milan",
             "bio": "Six years in drafting and review of family pacts. "
                    "Supports the Senior Stewards in Family Council "
                    "meetings and triennial review cycles."},
        ],

        "coordinates_label": "Offices",
        "coordinates": [
            ("Milan",      "Via San Marco 22 · 20121 · Brera"),
            ("Lugano",     "Riva Caccia 1 · 6900 · fiduciary correspondent"),
            ("Luxembourg", "Boulevard Royal 28 · L-2449 · trustee correspondent"),
        ],

        "cta_heading": "A first confidential dialogue.",
        "cta_intro":
            "The first forty-five minutes with a Senior Steward are an "
            "exploratory dialogue, not a commercial proposal. We "
            "discuss the mandate's perimeter, the time horizon and any "
            "fiduciary conflict — before any Family Council is called.",
        "cta_primary":  "Begin a mandate dialogue",
        "cta_primary_href": "contatti",
    },

    # ─── CUSTODIA (services · 4 pillars) ────────────────────────
    "custodia": {
        "eyebrow":  "Custody · governance · succession · compliance · 2026",
        "headline": "Four practices, <em>one single fiduciary signature</em>.",
        "intro":
            "Continua's four practices. Every family has access to a "
            "stewardship team that holds them all simultaneously — "
            "each practice is not billed separately, the mandate "
            "covers the combination of custody, governance, succession "
            "and compliance required for the horizon agreed at the "
            "Family Council.",

        "svc_duration_label": "Cadence",
        "svc_leader_label":   "Lead steward",

        "services": [
            {
                "num":   "01",
                "title": "Wealth custody",
                "blurb":
                    "We hold wealth across its four layers — liquid "
                    "financial, industrial holdings, operating real "
                    "estate, family real estate. Custody is not "
                    "portfolio management: it is the year-by-year "
                    "stewardship of coherence between the wealth and "
                    "the family pact in force.",
                "scope": [
                    "Quarterly reporting jointly signed",
                    "Digital custody register · access-controlled",
                    "Independent annual ANC continuity audit",
                    "Coordination of foreign fiduciary correspondents",
                ],
                "duration": "Quarterly · annual audit",
                "leader":   "Eleonora Marchesi",
            },
            {
                "num":   "02",
                "title": "Family governance",
                "blurb":
                    "We facilitate the Family Council on a quarterly "
                    "cadence, with fiduciary minute-keeping deposited "
                    "at the practice and triennial drafting and review "
                    "of the family pact. Governance is not a meeting: "
                    "it is the regular repetition of a custodial beat "
                    "carried through the generations.",
                "scope": [
                    "Four Family Councils per year",
                    "Fiduciary minutes deposited",
                    "Voting structures dedicated per branch",
                    "Intergenerational code of conduct",
                ],
                "duration": "4 Councils / year · triennial pact review",
                "leader":   "Tomas Okafor",
            },
            {
                "num":   "03",
                "title": "Structured succession",
                "blurb":
                    "We plan the intergenerational handover on a "
                    "ten-year horizon — modulated donations, family "
                    "holdings, dedicated trusts for minor or non-"
                    "operating branches. Succession is not improvised "
                    "on the day the notary signs: it is prepared with "
                    "a two-year technical training programme.",
                "scope": [
                    "Family holdings and shareholder pacts",
                    "Dedicated trusts for minor branches",
                    "Modulated donations on a ten-year horizon",
                    "Two-year incoming-generation training",
                ],
                "duration": "Ten-year horizon · two-year training",
                "leader":   "Lorenzo Pellegrini",
            },
            {
                "num":   "04",
                "title": "Fiduciary compliance",
                "blurb":
                    "Continuous fiduciary oversight on compliance with "
                    "D.lgs. 24/2023 (whistleblowing), Codice della "
                    "Crisi, OAM credit-mediation regulation and "
                    "applicable AML directives. Compliance is not an "
                    "administrative obstacle: it is the guarantee of "
                    "the mandate's continuity across generations.",
                "scope": [
                    "Encrypted internal whistleblowing channel",
                    "Reinforced AML on cross-border movements",
                    "Independent annual ANC continuity audit",
                    "Access-controlled documentary custody",
                ],
                "duration": "Continuous · annual ANC audit",
                "leader":   "Ginevra Conti",
            },
        ],

        "process_label":   "How we hold custody",
        "process_heading": "Four phases, one single sequence.",
        "process": [
            ("01", "First confidential dialogue",
             "Forty-five minutes with a Senior Steward. We discuss the "
             "mandate's perimeter and time horizon, never a commercial proposal."),
            ("02", "Mandate pact",
             "Within ten days, a four-page fiduciary mandate pact with "
             "perimeter, horizon, Council cadence and transparent "
             "fiduciary fee schedule."),
            ("03", "Opening of the file",
             "Inauguration of the first Family Council. The Senior "
             "Steward sits on the Council from the opening of the file "
             "to the transfer of responsibility."),
            ("04", "Continuity + annual audit",
             "Four Councils per year, independent ANC continuity audit "
             "every December, triennial review of the family pact. "
             "The mandate does not close: it renews in continuity."),
        ],

        "cta_heading":   "Which practice fits your family?",
        "cta_intro":
            "If the perimeter is not clear, write us a brief description "
            "of the family nucleus and the time horizon agreed within "
            "the family. We will indicate the right Steward within 72 "
            "hours — even if we do not open a mandate.",
        "cta_primary":   "Begin a mandate dialogue",
        "cta_primary_href": "contatti",
    },

    # ─── MANDATI (case_study_list) ─────────────────────────────
    "mandati": {
        "eyebrow":  "Continuing mandates · 2007 — 2026",
        "headline": "Four mandates, four generations, one single <em>fiduciary cadence</em>.",
        "intro":
            "A selection of mandates under care — not closed, still in "
            "continuity. The names of the families are disclosed only "
            "under reciprocal fiduciary confidentiality. The milestones "
            "shown are agreed case by case and signed at the Family Council.",

        "cases_label": "Mandates under care",
        "cases_intro":
            "For every mandate we show family profile, generations under "
            "care, years in continuity, agreed scope and audit cadence. "
            "The families are coded by branch (A · B · C · D) following "
            "the chronological order of mandate opening.",

        "cta_heading":   "A mandate similar to yours?",
        "cta_intro":
            "Full dossiers (fiduciary perimeter, horizon, Council "
            "cadence, most recent ANC audit) are accessible under "
            "reciprocal fiduciary confidentiality. The signature "
            "happens in the first dialogue, before any mandate proposal.",
        "cta_primary":   "Request the full dossiers",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "famiglia-a-quarta-generazione-holding-industriale",
            "title":    "Family A · 4th generation · Lombard industrial holding",
            "category": "Entrepreneurial family",
            "year":     "2014",
            "duration": "12 years · in continuity",
            "client_code":
                "Industrial holding · 4th generation · 6 family branches · "
                "Lombard industrial wealth · scope: continuity + "
                "governance + triennial audit.",
            "lead":
                "A Lombard industrial holding at its fourth generation "
                "of custody, six family branches, two generations "
                "simultaneously under care. Continua has presided over "
                "the handover from third to fourth generation since 2014.",
            "sections": [
                {
                    "label": "The context",
                    "heading": "Six branches, two generations, one shared wealth",
                    "body":
                        "In 2014 the holding was entering the handover "
                        "phase between the third generation (four "
                        "founding siblings) and the fourth (twelve "
                        "cousins, six family branches). The family pact "
                        "in force — drafted in 1989 — did not provide "
                        "voting structures for the fourth generation "
                        "and the third had not yet agreed a transfer "
                        "calendar. Continua was called upon to preside "
                        "over the cadence of the Family Council and to "
                        "set the handover.",
                },
                {
                    "label": "Custody",
                    "heading": "Quarterly cadence + triennial pact review",
                    "body":
                        "Continua set the Family Council on a quarterly "
                        "cadence from 2014, with fiduciary minutes "
                        "deposited after each meeting. In 2017 the first "
                        "triennial review of the family pact was "
                        "completed, with voting structures dedicated to "
                        "the six branches of the fourth generation and "
                        "a protection clause for non-operating branches. "
                        "ANC continuity audit every December.",
                },
                {
                    "label": "The handover",
                    "heading": "Family pact 2023 · progressive transfer",
                    "body":
                        "The 2023 triennial review of the family pact "
                        "formalised the calendar of progressive transfer "
                        "of decision-making responsibility from third to "
                        "fourth generation on a seven-year horizon "
                        "(2024-2031). The two-year technical training "
                        "programme for the fourth generation began in "
                        "2024. Continua's mandate has been renewed "
                        "through 2034.",
                },
            ],
            "kpi": [
                ("12 years", "in continuity · since 2014"),
                ("4th",      "generation under care"),
                ("6",        "family branches · dedicated voting structures"),
                ("2034",     "mandate renewal"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Family Officer + Compliance Officer · quarterly Council · annual ANC audit",
            "next_label":   "Next mandate",
        },
        {
            "slug":     "famiglia-b-fondazione-di-famiglia",
            "title":    "Family B · family foundation · 3rd generation",
            "category": "Family foundation",
            "year":     "2011",
            "duration": "15 years · in continuity",
            "client_code":
                "Family foundation · 3rd generation · 4 branches · "
                "philanthropic wealth + industrial holdings · "
                "scope: governance + compliance + triennial audit.",
            "lead":
                "A Lombard family foundation at its third generation, "
                "philanthropic wealth alongside operating industrial "
                "holdings. Continua has presided over foundation "
                "governance and fiduciary compliance since 2011.",
            "sections": [
                {
                    "label": "The context",
                    "heading": "One foundation, two natures of wealth",
                    "body":
                        "The foundation, established in 1986, holds a "
                        "philanthropic wealth of € 240 M and controlling "
                        "stakes in three Lombard industrial entities. "
                        "The third generation, in care since 2009, "
                        "asked Continua in 2011 to preside over "
                        "foundation governance and the separated "
                        "compliance between philanthropic and "
                        "industrial branches.",
                },
                {
                    "label": "Custody",
                    "heading": "Separation of the two natures · joint audit",
                    "body":
                        "Continua set up two distinct Family Councils — "
                        "one foundational and one industrial — with "
                        "concatenated quarterly meetings and an agenda "
                        "coordinated by the Family Officer. The ANC "
                        "continuity audit is joint across both branches "
                        "once a year, with outcome communicated to the "
                        "family at the December Council.",
                },
                {
                    "label": "Presidio",
                    "heading": "D.lgs. 24/2023 compliance + reinforced AML",
                    "body":
                        "Since 2023 Continua has extended fiduciary "
                        "presidio to the new whistleblowing regulation "
                        "(D.lgs. 24/2023) for the foundation, with a "
                        "dedicated internal reporting channel and "
                        "minute-keeping by the Compliance Officer. "
                        "Reinforced AML on industrial-branch movements "
                        "in coherence with the 2024 directives.",
                },
            ],
            "kpi": [
                ("15 years", "in continuity · since 2011"),
                ("3rd",      "generation under care"),
                ("€ 240 M",  "philanthropic wealth in custody"),
                ("2",        "Family Councils · quarterly cadence"),
            ],
            "lead_partner": "Ginevra Conti · Compliance Officer",
            "team":         "Senior Steward + Family Officer + Compliance Officer · 2 quarterly Councils · joint annual ANC audit",
            "next_label":   "Next mandate",
        },
        {
            "slug":     "famiglia-c-trasferimento-intergenerazionale",
            "title":    "Family C · intergenerational transfer · 2nd → 3rd generation",
            "category": "Family in transfer",
            "year":     "2019",
            "duration": "7 years · in transfer",
            "client_code":
                "Entrepreneurial family · 2nd → 3rd generation · 3 branches · "
                "dedicated trusts + family holding · scope: structured "
                "succession + incoming-generation training.",
            "lead":
                "An industrial family wealth in transfer from second to "
                "third generation, three family branches, decennial "
                "handover horizon. Continua has coordinated structured "
                "succession and the technical training of the "
                "successors since 2019.",
            "sections": [
                {
                    "label": "The context",
                    "heading": "A transition on a decennial horizon",
                    "body":
                        "In 2019 the second generation (three siblings, "
                        "founders of the company in 1978) asked Continua "
                        "to set the decennial handover towards the third "
                        "generation (seven biological successors, of "
                        "whom five active in the business). The first "
                        "step was the separation between operating "
                        "holding and family holding, with dedicated "
                        "trusts for the two minor branches.",
                },
                {
                    "label": "The structure",
                    "heading": "Family holding + dedicated trusts",
                    "body":
                        "Continua has presided over the establishment "
                        "of the family holding in 2020 and the two "
                        "dedicated trusts in 2021. The two-year "
                        "technical training programme for the five "
                        "active successors began in 2022, with monthly "
                        "sessions facilitated by the Family Officer and "
                        "an annual day-long Family Council simulation.",
                },
                {
                    "label": "The renewal",
                    "heading": "Family pact 2025 · triennial review",
                    "body":
                        "The 2025 triennial review of the family pact "
                        "formalised the post-handover voting structure, "
                        "the calendar for transfer of decision-making "
                        "responsibility (2026-2029) and the protection "
                        "clauses for the two minor branches. Continua's "
                        "mandate has been renewed through 2032 with "
                        "presidio over the completion of the handover.",
                },
            ],
            "kpi": [
                ("7 years", "in transfer · since 2019"),
                ("2 → 3",   "generations in handover"),
                ("2",       "dedicated trusts · minor branches"),
                ("2032",    "mandate renewal"),
            ],
            "lead_partner": "Lorenzo Pellegrini · Steward Succession",
            "team":         "Senior Steward + Family Officer + Steward Succession · quarterly Council · monthly + annual training",
            "next_label":   "Next mandate",
        },
        {
            "slug":     "famiglia-d-single-family-office-estero",
            "title":    "Family D · foreign single family office · cross-border custody",
            "category": "Foreign single family office",
            "year":     "2017",
            "duration": "9 years · in continuity",
            "client_code":
                "Single family office · 2nd generation · 1 principal branch · "
                "cross-border wealth IT/CH/LU · scope: custody + "
                "compliance + Lugano + Luxembourg fiduciary correspondents.",
            "lead":
                "An Italian single family office with cross-border "
                "wealth (Italy, Switzerland, Luxembourg). Continua has "
                "presided over wealth custody and fiduciary compliance "
                "by coordinating the Lugano and Boulevard Royal "
                "correspondents since 2017.",
            "sections": [
                {
                    "label": "The context",
                    "heading": "A wealth in three jurisdictions",
                    "body":
                        "In 2017 the family asked for fiduciary "
                        "coordination of a wealth distributed across "
                        "three jurisdictions — Italy (operating and "
                        "family real estate), Switzerland (liquid "
                        "financial assets), Luxembourg (dedicated trusts "
                        "for the non-operating branches). Continua "
                        "activated the two accredited fiduciary "
                        "correspondents in Lugano (Riva Caccia) and "
                        "Boulevard Royal."},
                {
                    "label": "Custody",
                    "heading": "Unified reporting + joint audit",
                    "body":
                        "Continua produces unified quarterly reporting "
                        "across the three jurisdictional branches, "
                        "signed by the Senior Steward + Compliance "
                        "Officer + accredited correspondents. The ANC "
                        "continuity audit is joint across the three "
                        "branches once a year, with outcome communicated "
                        "at the January Family Council (offset from the "
                        "Italian cycle for cross-border tax alignment).",
                },
                {
                    "label": "The evolution",
                    "heading": "AML 2024 directives · reinforced presidio",
                    "body":
                        "Since 2024 Continua has coordinated reinforced "
                        "AML presidio under the 2024 European directives, "
                        "with quarterly verification of cross-border "
                        "movements and double fiduciary signature for "
                        "operations > € 500K. The mandate has been "
                        "extended through 2030 with scope coordinated "
                        "across the three correspondents.",
                },
            ],
            "kpi": [
                ("9 years",     "in continuity · since 2017"),
                ("3",           "jurisdictions · IT · CH · LU"),
                ("quarterly",   "unified reporting"),
                ("2030",        "mandate renewal"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Compliance Officer + 2 accredited correspondents · joint annual ANC audit",
            "next_label":   "Next mandate",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "First confidential dialogue",
        "headline": "Forty-five minutes, a <em>family</em> agenda, no commitment.",
        "intro":
            "The first dialogue takes place with a Senior Steward. We "
            "discuss the mandate's perimeter, the time horizon and any "
            "fiduciary conflict — before any Family Council is called. "
            "Sensitive information is held in encrypted archive with "
            "access limited to the stewards.",

        "form_label":   "Begin a mandate dialogue",
        "form_heading": "Complete the confidential form",
        "form_intro":
            "You will receive confirmation from a Senior Steward within "
            "72 working hours of submission. Data is processed under EU "
            "Reg. 679/2016 and held in the encrypted archive at the "
            "Via San Marco practice. No external BDR, no sequence "
            "automation — the dialogue opens with a steward, always.",

        "form_fields": [
            {"name": "name",      "label": "First name",   "type": "text", "required": True,
             "placeholder": "E.g. Eleonora",
             "helper": "First name only, please."},
            {"name": "surname",   "label": "Last name",    "type": "text", "required": True,
             "placeholder": "E.g. Marchesi",
             "helper": "As it appears in the family pact in force (if any)."},
            {"name": "family",    "label": "Family nucleus", "type": "text", "required": True,
             "placeholder": "E.g. Marchesi Family · Lombard branch",
             "helper": "The name under which you introduce yourself at the Family Council."},
            {"name": "role",      "label": "Role within the family", "type": "text", "required": True,
             "placeholder": "E.g. Family principal · Designated successor · Council member",
             "helper": "Your position in the handover between generations under care."},
            {"name": "email",     "label": "Confidential email", "type": "email", "required": True,
             "placeholder": "eleonora@famigliamarchesi.it",
             "helper": "An inbox that receives only fiduciary communications. We will not use consumer domains for the first contact."},
            {"name": "phone",     "label": "Direct phone",  "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "The direct line of the contact, not a corporate switchboard."},
            {"name": "horizon",   "label": "Time horizon",  "type": "select", "required": True,
             "options": [
                 "5 years",
                 "10 years",
                 "25 years",
                 "Multi-generational (horizon beyond 25 years)",
             ],
             "helper": "The horizon agreed within the family for the custody mandate. Helps us calendar the right Senior Steward."},
            {"name": "structure", "label": "Current structure", "type": "select", "required": True,
             "options": [
                 "Family holding",
                 "Family foundation",
                 "Dedicated trust (Italian or foreign)",
                 "Family pact in force",
                 "No formalisation",
             ],
             "helper": "The existing legal structure (even if not yet formalised)."},
            {"name": "scope",     "label": "Family scope",  "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Up to 800 characters. Briefly describe the current structure and your continuity concern — it will be held in encrypted archive from this form onwards.",
             "helper": "Enough to assess whether the mandate falls within our competence. Names of other branches and figures are shared only after reciprocal fiduciary confidentiality."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "The person who will sign any reciprocal fiduciary confidentiality before the first Council.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Family",
             "meta": "For the preliminary fiduciary conflict-check.",
             "fields": ["family", "role"]},
            {"num": "03", "title": "Custody mandate",
             "meta": "The horizon and the structure — the wealth detail is discussed only in dialogue, never in writing at the first-contact stage.",
             "fields": ["horizon", "structure", "scope"]},
            {"num": "04", "title": "Attachments (optional)",
             "meta": "Family pact in force, foundation statute, trust deed or succession dossier: they anticipate the first meeting and shorten the dialogue.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "dossier_familiare",
            "label":    "Preliminary documents",
            "helper":   "Family pact in force, foundation statute, trust "
                        "deed or succession dossier. PDF / DOCX · max 20 "
                        "MB total. Encrypted archive with access limited "
                        "to Continua stewards.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Drag the documents here or",
            "link":     "browse from your archive",
            "meta":     "PDF / DOCX · max 20 MB · fiduciary encrypted archive",
        },

        "form_submit_label": "Begin a mandate dialogue",
        "form_submit_note":
            "Confirmation from a Senior Steward within 72 working hours. "
            "No external BDR, no sequence automation — the dialogue "
            "opens with a steward, always.",
        "form_consent":
            "I consent to the processing of personal data under EU Reg. "
            "679/2016 and the amended D.lgs. 196/2003. Data is held in "
            "the encrypted archive at the Via San Marco practice with "
            "access limited to Continua stewards. No data is shared "
            "with third parties without explicit fiduciary "
            "authorisation. I am informed of the whistleblowing "
            "channel (D.lgs. 24/2023) active at the practice.",

        "office_address_label": "Address",
        "office_area_label":    "Area",
        "office_phone_label":   "Phone",
        "office_email_label":   "Email",

        "offices_label":   "Offices",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Principal office",
                "address": "Via San Marco 22 · 20121",
                "area":    "Brera · near Piazza San Marco",
                "phone":   "+39 02 7600 4188",
                "email":   "milano@continua.it",
            },
            {
                "city":    "Lugano",
                "tag":     "Fiduciary correspondent",
                "address": "Riva Caccia 1 · 6900",
                "area":    "Centre · near Piazza della Riforma",
                "phone":   "+41 91 922 7700",
                "email":   "lugano@continua.it",
            },
            {
                "city":    "Luxembourg",
                "tag":     "Trustee correspondent",
                "address": "Boulevard Royal 28 · L-2449",
                "area":    "Ville Haute · near Place d'Armes",
                "phone":   "+352 24 87 5500",
                "email":   "luxembourg@continua.it",
            },
        ],

        "channels_label": "Direct channels",
        "channels": [
            ("Custody secretariat",            "+39 02 7600 4188",            "Mon – Fri · 9:30 – 18:30"),
            ("Fiduciary email",                "mandato@continua.it",         "Reply within 72 hours"),
            ("Whistleblowing (D.lgs. 24/2023)","whistleblowing@continua.it",  "Internal encrypted channel · minute-kept by the Compliance Officer"),
        ],

        "footnote":
            "Continua does not respond to anonymous requests and does "
            "not issue preliminary written opinions without a first "
            "dialogue with a Senior Steward. Administrative information "
            "(indicative fees, billing terms, mandate-acceptance "
            "criteria) is illustrated in the first dialogue, never in "
            "writing. The whistleblowing channel is managed by the "
            "Compliance Officer under D.lgs. 24/2023 and is also "
            "accessible to family members under mandate alone.",
    },
}
