"""Solaria — Business Coaching · English locale content tree.

Phase X.4 Pass B · 2026-04-26 · Multilingual completion pass.

Mirrors the shape of `SOLARIA_CONTENT_IT` exactly — same keys, same
nesting, same list shapes. Only values are translated and adapted.

Voice register: warm-professional, adult-to-adult, ICF-aligned.
Native English equivalent of the IT register — calm, measured,
declarative. Reference voices: HBR coaching column, Forbes coaching
section, Coaching at Work magazine. NEVER funnel-pattern, NEVER
self-help hyperbole, NEVER mountain-peak metaphors.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved verbatim-in-
translation across all 5 locales):
    "Coaching is not therapy and is not consultancy. We do not say
     what to do and we do not analyse the past to understand it.
     We work on the choices you are about to make, with a method and
     a cadence. A path has a declared beginning and a declared end.
     At the end, if it has worked, you are more autonomous in your
     decisions — not more dependent on a coach."

Italian normative references and proper nouns are preserved (ICF
PCC/MCC/ACC, EMCC, Co-Active, GROW, Immunity to Change, Codice
Deontologico ICF §2.4, Reg. UE 679/2016). Italian addresses,
ODCEC/EMCC numbers, Italian phone format, Euro figures and years
are kept as-is. Anti-pattern guardrails (blueprint §13) carry
across: no "Unlock your potential", no "Transform your life in N
days", no "Best version of yourself", no "Winning mindset", no
Einstein/Jung/Gandhi/Steve Jobs quotes, no mountain-peak imagery.
"""
from __future__ import annotations

from typing import Any


# Pool URLs imported from the IT module — single source of truth so the
# build-time corporate_suite.E002/E003 checks see the same registered
# Pexels URLs across every locale.
from apps.catalog.template_content_solaria import (  # noqa: E402
    _POOL_HERO,
    _POOL_FEATURE,
    _POOL_PORTRAIT_A,
    _POOL_PORTRAIT_B,
    _POOL_DETAIL,
    _POOL_AMBIENT,
)


SOLARIA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Practice",   "kind": "home"},
        {"slug": "il-coach",   "label": "The coach",  "kind": "about"},
        {"slug": "percorsi",   "label": "Paths",      "kind": "services"},
        {"slug": "casi",       "label": "Cases",      "kind": "case_study_list"},
        {"slug": "contatti",   "label": "Contact",    "kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Solaria",
        "tag":          "Business coaching · Milan Isola · ICF-PCC certified since 2017",
        "phone":        "+39 02 3663 4712",
        "email":        "discovery@solariacoaching.it",
        "address":      "Via Thaon di Revel 21 · 20159 Milan",
        "hours_compact": "Mon – Fri · 9:00 – 19:00 · by appointment",
        "hours_footer_rows": [
            "Evening sessions available for international coachees (UTC+5 / UTC-5)",
            "Saturday and Sunday · closed",
        ],
        "license":      "Professional Certified Coach (PCC) · International Coaching Federation (ICF)",
        "footer_intro":
            "A professional coaching practice for entrepreneurs, executives "
            "in transition and middle-management teams. Declared method, "
            "agreed cadence, beginning and end of the engagement written into "
            "the contract — no transformations promised, no dependency sought. "
            "Based in Milan, sessions on-site and online.",
        "foot_studio":   "The practice",
        "foot_pages":    "Sections",
        "foot_contact":  "Contact",
        "foot_offices":  "Office",
        "offices_footer_rows": [
            "Milan · Isola",
        ],
        "case_practice_label":     "Area",
        "case_year_label":         "Year",
        "case_duration_label":     "Duration",
        "case_lead_label":         "Coach",
        "case_lead_partner_label": "Coach",
        "case_team_label":         "Path & sponsor",
        "case_timeline_label":     "Timeline",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Business coaching · Milan Isola · ICF-PCC certified since 2017",
        "headline":    "Coaching is not <em>therapy</em>, and not <em>consultancy</em>.",
        "intro":
            "Coaching paths for entrepreneurs, executives in transition and "
            "middle managers. Declared method, agreed cadence, beginning and "
            "end written into the contract — no thirty-day transformations.",
        "primary_cta":   "Book a discovery call",
        "primary_href":  "contatti",
        "secondary_cta": "The method",
        "secondary_href":"il-coach",

        "hero_image":              _POOL_HERO,
        "hero_image_credit_left":  ("Reportage",   "1:1 executive session"),
        "hero_image_credit_right": ("Practice",    "Solaria · Milan Isola"),
        "hero_meta_strip": [
            ("Session",          "60 minutes · fortnightly cadence"),
            ("Discovery call",   "20 – 30 minutes · no charge"),
            ("Supervision",      "ICF-MCC ongoing since 2019"),
        ],

        "pillars_label":   "Paths",
        "pillars_heading": "Three formats, one written engagement",
        "pillars_intro":
            "The same method for every format: an opening contract with a "
            "measurable goal, sessions at an agreed cadence, mid-path "
            "re-contracting, closure with verification, three-month follow-up "
            "included in the fee.",
        "pillars": [
            ("01", "Executive 1:1",
             "Eight 60-minute sessions on a fortnightly cadence for executives "
             "in transition, the newly promoted, or those preparing a change of "
             "remit. Frameworks: Co-Active + Immunity to Change."),
            ("02", "Team coaching",
             "Six sessions with the team (five to ten people) plus mid-path "
             "re-contracting with the corporate sponsor. For middle management "
             "in growth or post-restructuring. Framework: GROW for groups."),
            ("03", "Corporate group",
             "A day-long masterclass plus eight 1:1 sessions for three to eight "
             "people from the same corporate client. Individual goals tied to "
             "system goals, quarterly follow-up with the sponsor."),
        ],

        "kpi_heading": "Twelve years of certified practice",
        "kpi_strip": [
            ("12",       "years of ICF practice"),
            ("2,400+",   "coaching hours delivered"),
            ("160+",     "coachees worked with since 2014"),
            ("100%",     "engagements with three-month follow-up"),
        ],

        "sectors_label": "Coachee profiles",
        "sectors": [
            "Newly-promoted CEOs",
            "Function directors in transition",
            "Middle managers in growth",
            "Leadership teams post-restructuring",
            "Partners in professional firms",
        ],

        "trust_label":   "Sponsor companies 2023 — 2025 · names anonymized under ICF Code §2.4",
        "trust_logos":   [
            "FINTECH SCALE-UP · SERIES B",
            "LISTED INDUSTRIAL GROUP",
            "ASSOCIATED LAW FIRM",
            "MEDICAL DEVICE MANUFACTURER",
            "EDUCATIONAL FOUNDATION",
            "BOUTIQUE PROFESSIONAL SERVICES",
        ],

        "leadership_label":   "The coach",
        "leadership_heading": "Who sits across the table",
        "leadership_intro":
            "One founding coach and one associate coach. Every engagement is "
            "carried personally by the same coach from beginning to closure — "
            "no junior-to-senior hand-over, no quiet rotation.",
        "leadership": [
            {
                "name":  "Dr. Giulia Loreti",
                "role":  "Founding coach · ICF-PCC · EMCC Senior Practitioner",
                "portrait": _POOL_PORTRAIT_A,
                "bio":
                    "Fifteen years in corporate HR as head of management "
                    "development at a listed industrial group, before turning "
                    "fully to coaching in 2014. Professional Certified Coach "
                    "(PCC) credentialed by the International Coaching Federation "
                    "since 2017. Continuous supervision with an ICF-MCC senior since 2019.",
                "credentials": [
                    "ICF-PCC no. 011749 (since 2017 · renewed 2023)",
                    "EMCC Senior Practitioner (since 2020)",
                    "Coach Training Institute · Co-Active curriculum (2014)",
                    "Università Bocconi — MSc Work Psychology '02",
                ],
            },
            {
                "name":  "Dr. Martina Erriquez",
                "role":  "Associate coach · ICF-ACC · in PCC pathway",
                "portrait": _POOL_PORTRAIT_B,
                "bio":
                    "Eight years as an organisational-development consultant "
                    "before starting the coaching pathway in 2020. Associate "
                    "Certified Coach (ACC) credentialed since 2022, currently "
                    "in the PCC certification pathway (expected 2027). "
                    "Monthly supervision with Giulia Loreti and an external EMCC supervisor.",
                "credentials": [
                    "ICF-ACC no. 028914 (since 2022)",
                    "Co-Active Training Institute · Fundamentals + Intermediate (2020-2022)",
                    "Università Cattolica — MSc Work Psychology '12",
                    "Monthly ICF + EMCC supervision",
                ],
            },
        ],

        "cases_label":   "Cases",
        "cases_heading": "Three engagements, three measured outcomes",
        "cases_intro":
            "Engagements completed over the past three years — coachees "
            "anonymized under ICF Code §2.4, real goals and real outcomes. "
            "Reference call with the corporate sponsor available under mutual "
            "NDA for corporate engagements.",

        "cta_label":     "Is now the right moment?",
        "cta_heading":   "Twenty minutes to find out whether Solaria fits",
        "cta_intro":
            "No free coaching session, no diagnosis, no cold quote. An honest "
            "conversation about your goal and the suitability of coaching to "
            "your need. If it is not coaching, we say so — and point to the "
            "right professional.",
        "cta_primary":   "Book a discovery call",
        "cta_primary_href": "contatti",
        "cta_secondary": "The method in five steps",
        "cta_secondary_href": "il-coach",
    },

    # ─── IL COACH (about + method + values + team) ──────────────
    "il-coach": {
        "eyebrow":   "The coach · 2014 — 2026",
        "headline":  "A <em>declared</em> method, twelve years of certified practice.",
        "intro":
            "Solaria began in 2014 when Giulia Loreti left a senior HR role "
            "in corporate to dedicate herself fully to coaching. The first "
            "Solaria engagement — a team coaching for a newly-incorporated "
            "Milan fintech scale-up — started in November of the same year. "
            "Martina Erriquez joined as associate coach in 2020.",

        "history_label":   "The method · a typical path in five steps",
        "history_heading": "Five steps, an agreed cadence",
        "history_intro":
            "A Solaria path follows the same structure regardless of format "
            "(executive 1:1, team, corporate group). These five steps are "
            "written into the coaching contract the coachee signs at the start.",
        "history": [
            ("01", "Discovery call",
             "Twenty to thirty minutes, free of charge, no commitment. We work "
             "out whether the goal falls within coaching, whether Solaria is "
             "the right practice, and discuss an indicative quote. No "
             "obligation at the end."),
            ("02", "Opening contract",
             "A first ninety-minute paid meeting. We define the measurable "
             "goal (SMART framework), choose the conducting framework (GROW "
             "· Co-Active · Immunity to Change), and sign the coaching "
             "contract — number of sessions, cadence, confidentiality, and "
             "reference to the ICF Code of Ethics."),
            ("03", "Regular sessions",
             "60-minute sessions at the agreed cadence (typically fortnightly "
             "for executive 1:1, monthly for team, quarterly for follow-up). "
             "Each session closes with a written commitment the coachee "
             "verifies independently before the next meeting."),
            ("04", "Mid-path re-contracting",
             "Mid-engagement, a re-contracting session with the coachee (and "
             "with the corporate sponsor where coaching is sponsored). The "
             "original goal is reviewed, adjustments decided, and the "
             "decision taken to continue or close early. No obligation to continue."),
            ("05", "Closure & follow-up",
             "A final consolidation session with explicit verification of "
             "outcome against the opening goal. A scheduled three-month "
             "follow-up — a 60-minute session to verify the durability of "
             "the change. Follow-up is included in the engagement fee, "
             "never billed separately."),
        ],

        "values_label":   "Principles",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "Four rules that distinguish a Solaria engagement from generic "
            "coaching. They are written into the contract signed at the "
            "start, and the coachee can invoke them at any time during the path.",
        "values": [
            ("01", "Coaching is not therapy and not consultancy",
             "We do not diagnose psychological conditions (we are not "
             "psychotherapists). We do not propose corporate solutions (we "
             "are not strategy consultants). If during the discovery call or "
             "the engagement it emerges that the need is one of the other "
             "two, we say so explicitly and refer the coachee to a "
             "professional in the right discipline — even if it means "
             "closing the engagement with Solaria."),
            ("02", "Confidentiality without exception",
             "Whatever happens in session stays in session. Corporate "
             "sponsors receive only aggregate reporting agreed in the "
             "opening contract — never specific session content. No "
             "exceptions outside legal obligation, which is explained to "
             "the coachee before any third-party communication."),
            ("03", "A bounded path, autonomy as the goal",
             "Every engagement has a declared number of sessions written "
             "into the opening contract. We do not offer unlimited "
             "subscriptions or perpetual coaching. At the end, if it has "
             "worked, the coachee is more autonomous in making their own "
             "decisions — not more dependent on a coach."),
            ("04", "Mandatory continuous supervision",
             "Both Solaria coaches are in continuous supervision: Giulia "
             "with a senior ICF-MCC since 2019, Martina with Giulia monthly "
             "plus an external EMCC supervisor. Supervision is the "
             "equivalent of quality control in a serious professional "
             "practice — and its cost is borne by the practice, not the coachee."),
        ],

        "team_label":   "Practice",
        "team_heading": "Two coaches, one external supervisor, one governance",
        "team_intro":
            "The people behind Solaria's work. Coaching sessions are "
            "delivered only by Giulia or Martina; the external supervisor "
            "never interacts with coachees but verifies the quality of the "
            "associate coach's practice.",
        "team": [
            {"name": "Dr. Giulia Loreti",
             "role": "Founding coach · ICF-PCC · EMCC Senior Practitioner",
             "office": "Milan",
             "bio": "Executive 1:1 coaching and team coaching. "
                    "2,400+ hours delivered since 2014. Supervision with ICF-MCC since 2019."},
            {"name": "Dr. Martina Erriquez",
             "role": "Associate coach · ICF-ACC · in PCC pathway",
             "office": "Milan",
             "bio": "Executive 1:1 coaching for new managers and corporate-group paths. "
                    "Monthly supervision with Giulia + external EMCC."},
            {"name": "Dr. Elena Mannucci",
             "role": "External supervisor · ICF-MCC",
             "office": "Trento · consultant",
             "bio": "Supervises Giulia's practice since 2019 and Martina's since 2022. "
                    "Never interacts with coachees — verifies the quality of the coaches' practice."},
            {"name": "Ms. Donatella Rinaldi",
             "role": "Practice assistant · back-office",
             "office": "Milan",
             "bio": "Calendars, billing, contracts. "
                    "Never accesses the content of coaching sessions."},
        ],

        "coordinates_label": "Office",
        "coordinates": [
            ("Milan",  "Via Thaon di Revel 21 · 20159 · Isola — 300 m from Garibaldi FS metro"),
        ],

        "cta_heading": "Discovery call or written question",
        "cta_intro":
            "The 20-30 minute discovery call is the canonical way to assess "
            "whether a Solaria engagement fits your need. If you prefer to "
            "ask a written question before booking the call, the practice "
            "email is read by Donatella every morning and one of us answers "
            "within the working day.",
        "cta_primary":  "Book a discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── PERCORSI (services) ────────────────────────────────────
    "percorsi": {
        "eyebrow":  "Coaching paths · 2026",
        "headline": "Four paths, <em>one method</em>.",
        "intro":
            "Four engagement formats, each with a declared number of "
            "sessions, an agreed cadence, the format (on-site · online · "
            "hybrid) and an indicative price. Every path follows the same "
            "method — opening contract, regular sessions, mid-path "
            "re-contracting, closure with verification, three-month follow-up.",

        "svc_duration_label": "Typical duration",
        "svc_leader_label":   "Lead coach",

        "services": [
            {
                "num":   "01",
                "title": "Executive 1:1",
                "blurb":
                    "The most-requested format. Eight 60-minute sessions on "
                    "a fortnightly cadence, with a measurable goal defined in "
                    "the first meeting and written into the contract. For "
                    "executives in transition, the newly promoted, or those "
                    "preparing a change of remit. Reference frameworks: "
                    "Co-Active + Immunity to Change.",
                "scope": [
                    "Opening contract with a measurable SMART goal",
                    "Eight 60-minute sessions · fortnightly cadence",
                    "Mid-path re-contracting (fourth session)",
                    "Closure with outcome verification",
                    "60-minute three-month follow-up included",
                ],
                "duration": "16 weeks · 8 sessions + follow-up",
                "leader":   "Dr. Giulia Loreti",
            },
            {
                "num":   "02",
                "title": "Team coaching",
                "blurb":
                    "Work with middle-management teams (five to ten people). "
                    "Six sessions with the team plus a re-contracting "
                    "session with the corporate sponsor at mid-path. For "
                    "teams in growth, post-restructuring integration, or "
                    "preparation for a specific challenge. Framework: GROW "
                    "applied at group level.",
                "scope": [
                    "Tripartite opening contract (team · sponsor · coach)",
                    "Six 120-minute sessions · monthly cadence",
                    "Mid-path re-contracting with sponsor",
                    "Aggregate report to sponsor (never specific content)",
                    "90-minute three-month follow-up included",
                ],
                "duration": "6 months · 6 sessions + re-contracting + follow-up",
                "leader":   "Dr. Giulia Loreti",
            },
            {
                "num":   "03",
                "title": "Corporate group",
                "blurb":
                    "A structured HR programme for three to eight people from "
                    "the same corporate client. A day-long masterclass at the "
                    "start plus eight 1:1 sessions for each participant. "
                    "Defined corporate sponsor, individual goals tied to "
                    "system goals, quarterly follow-up with the sponsor.",
                "scope": [
                    "Opening day-long masterclass (framework + code of ethics)",
                    "Eight 1:1 sessions for each participant",
                    "Aggregate progress dashboard for sponsor (agreed KPIs)",
                    "Quarterly sponsor follow-up for the first 12 months",
                    "Tailored quote based on number of participants",
                ],
                "duration": "6-9 months · masterclass + 8 sessions/person",
                "leader":   "Dr. Giulia Loreti · Dr. Martina Erriquez",
            },
            {
                "num":   "04",
                "title": "Single exploratory session",
                "blurb":
                    "A single ninety-minute session, no path contract. For "
                    "anyone who wants to assess the coaching approach on a "
                    "specific topic before committing to a full path. At the "
                    "end the coachee decides whether to open an executive 1:1 "
                    "path or to close the engagement — no obligation to continue.",
                "scope": [
                    "90-minute session with GROW applied to the topic",
                    "Written output delivered within 48 hours",
                    "Honest assessment: coaching · therapy · consultancy",
                    "If coaching: indicative quote for a path",
                    "If not coaching: referral to the right professional",
                ],
                "duration": "1 session · 90 minutes",
                "leader":   "Dr. Martina Erriquez",
            },
        ],

        "process_label":   "How a path opens",
        "process_heading": "Four steps, one sequence",
        "process": [
            ("01", "Discovery call",
             "Twenty to thirty minutes free on video conference. We work out "
             "whether the goal falls within coaching or is therapy/consultancy, "
             "whether Solaria is the right practice, and discuss an indicative quote."),
            ("02", "Opening contract",
             "A first ninety-minute paid meeting within seven working days "
             "of the discovery call. SMART goal definition, framework choice, "
             "signed coaching contract."),
            ("03", "Regular path",
             "Sessions at the cadence agreed in the contract. Each session "
             "closes with a written commitment the coachee verifies "
             "independently. Mid-path re-contracting with the coachee (and "
             "the sponsor for corporate engagements)."),
            ("04", "Closure & follow-up",
             "Final session with explicit verification of outcome against "
             "the opening goal. A 60-minute three-month follow-up — included "
             "in the path fee, never billed separately."),
        ],

        "cta_heading":   "Which format fits your case?",
        "cta_intro":
            "If you are not sure which path to choose, the discovery call "
            "is the canonical way to work it out together. We listen and "
            "indicate the most coherent format — even when the answer is "
            "\"another professional fits your need better\".",
        "cta_primary":   "Book a discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── CASI (case-studies list) ───────────────────────────────
    "casi": {
        "eyebrow":  "Engagements · 2022 — 2026",
        "headline": "Three paths, <em>three measured outcomes</em>.",
        "intro":
            "A selection of engagements completed over the past three years. "
            "Coachees are identified by sector code and role under the ICF "
            "Code of Ethics §2.4 (confidentiality), but opening goals and "
            "measured outcomes are real. Reference call with the corporate "
            "sponsor available for corporate engagements after a discovery "
            "call and mutual NDA.",

        "cases_label": "Engagements",
        "cases_intro":
            "A balanced selection across the three main formats — executive "
            "1:1, team coaching, corporate group. Not mythological "
            "testimonials (\"my life changed\"): documented engagements with "
            "a declared opening goal, the path delivered, and a verified outcome.",

        "cta_heading":   "A case similar to yours?",
        "cta_intro":
            "If a case described here resembles your situation, the "
            "discovery call is the canonical way to explore it. No "
            "obligation to open a path after the call — only an honest "
            "assessment of the suitability of coaching to your specific need.",
        "cta_primary":   "Book a discovery call",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "executive-neo-ceo-tech-scaleup",
            "title":    "Executive 1:1 · newly-appointed CEO of a Milan tech scale-up",
            "category": "Executive 1:1",
            "thumb":    _POOL_DETAIL,
            "year":     "2025",
            "duration": "8 sessions · 16 weeks + follow-up",
            "client_code":
                "Tech & product · Milan · fintech scale-up · Series B · "
                "CEO 42 years old · promoted internally after the founder's exit",
            "lead":
                "The founder exited after a Series B round and the CTO was "
                "promoted internally as the new CEO. The new CEO had technical "
                "and product experience but no general-management experience, "
                "and the board was asking for a positioning review within six months.",
            "sections": [
                {
                    "label": "The opening goal",
                    "heading": "From CTO to general management in six months",
                    "body":
                        "The goal declared in the coaching contract was to "
                        "work on role identity (from CTO to CEO), on "
                        "operational delegation (the new CEO tended to stay "
                        "deep in product technicalities), and on the "
                        "relationship with the board (three independent "
                        "members plus two from the Series B funds). Agreed "
                        "measurable outcome: end-of-six-month feedback from "
                        "the board with a \"confirmed in role\" rather than "
                        "\"under observation\" verdict.",
                },
                {
                    "label": "The path",
                    "heading": "Co-Active + Immunity to Change",
                    "body":
                        "Eight fortnightly sessions with a combined "
                        "framework. The first four sessions (Co-Active) "
                        "worked on the values the new CEO brought into the "
                        "role and on translating them into observable "
                        "leadership behaviours. The following four sessions "
                        "(Immunity to Change by Kegan & Lahey) identified "
                        "and disarmed unconscious resistances to the "
                        "identity shift. Mid-path re-contracting with "
                        "confirmation of the original goal and refinement "
                        "of operational indicators. ICF-MCC supervision on "
                        "the case before session six.",
                },
                {
                    "label": "The outcome",
                    "heading": "Role confirmed with positive observations",
                    "body":
                        "At the end of the engagement, the board "
                        "unanimously confirmed the CEO in role with a full "
                        "performance bonus. The CEO restructured their "
                        "agenda by reducing time in technical calls by 40% "
                        "and re-allocating that time to the relationship "
                        "with the lead investor and the independent board "
                        "members. Two years later (three-month follow-up + "
                        "spontaneous yearly check-ins) they are still in "
                        "role and the company has closed Series C positively.",
                },
            ],
            "kpi": [
                ("8/8",      "engagement sessions completed"),
                ("100%",     "opening goal reached"),
                ("-40%",     "time on technical operating calls"),
                ("24 mos.",  "in-role tenure since coaching closure"),
            ],
            "lead_partner": "Dr. Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 ICF-MCC supervisor · 16 weeks",
            "next_label":   "Next case",
        },
        {
            "slug":     "team-coaching-middle-management-manifattura",
            "title":    "Team coaching · middle management of a manufacturer in restructuring",
            "category": "Team coaching",
            "thumb":    _POOL_AMBIENT,
            "year":     "2024",
            "duration": "6 sessions · 6 months + re-contracting + follow-up",
            "client_code":
                "Manufacturing & industry · Brescia · 320 employees · "
                "team of seven middle managers post-restructuring · "
                "sponsor: head of operations",
            "lead":
                "A Brescia-based industrial group had restructured its "
                "production base, consolidating three sites into two. The "
                "seven middle managers on the production lines now had to "
                "coordinate mixed teams (people from different sites with "
                "different processes). The head of operations, as corporate "
                "sponsor, engaged Solaria for a six-month team coaching.",
            "sections": [
                {
                    "label": "The opening goal",
                    "heading": "A team that talks, not seven separate referents",
                    "body":
                        "Before the engagement, the seven middle managers "
                        "operated as \"seven separate referents to the head "
                        "of operations\", with no lateral information "
                        "exchange and no coherent escalation of issues. The "
                        "goal declared in the tripartite contract (team · "
                        "sponsor · coach) was to move to a coordinated "
                        "team model with measurable lateral exchange "
                        "practices within six months. KPI agreed with the "
                        "sponsor: documented frequency of lateral exchange "
                        "+ reduction of \"silent\" escalations.",
                },
                {
                    "label": "The path",
                    "heading": "GROW applied to the team + operational artefacts",
                    "body":
                        "Six 120-minute sessions on a monthly cadence, plus "
                        "a 90-minute mid-path re-contracting with the "
                        "sponsor. GROW framework applied at group level "
                        "(collective Goal · collective Reality · collective "
                        "Options · collective Will) for each session. Three "
                        "operational artefacts co-created with the team "
                        "were introduced: a ten-minute daily stand-up, a "
                        "thirty-minute weekly retrospective, and an "
                        "escalation matrix agreed with the sponsor. Monthly "
                        "aggregate reporting to the sponsor (never "
                        "specific content, per ICF code of ethics).",
                },
                {
                    "label": "The outcome",
                    "heading": "A coordinated team with operational artefacts that hold",
                    "body":
                        "At the end of the engagement, the team was "
                        "running the three operational artefacts "
                        "autonomously without coach intervention. Silent "
                        "escalations to the head of operations dropped from "
                        "an average of about six per week to under one per "
                        "week. At three-month follow-up, six of the seven "
                        "managers were still on the team and the operational "
                        "artefacts had been absorbed into normal practice. "
                        "The sponsor renewed the engagement for a second "
                        "team in the logistics division.",
                },
            ],
            "kpi": [
                ("6/6",      "engagement sessions completed"),
                ("-85%",     "documented silent escalations"),
                ("3/3",      "operational artefacts holding at follow-up"),
                ("6/7",      "managers still on team at follow-up"),
            ],
            "lead_partner": "Dr. Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 ICF-MCC supervisor · 6 months",
            "next_label":   "Next case",
        },
        {
            "slug":     "gruppo-aziendale-neo-manager-studio-legale",
            "title":    "Corporate group · five newly-appointed associates of a law firm",
            "category": "Corporate group",
            "thumb":    _POOL_FEATURE,
            "year":     "2023",
            "duration": "Masterclass + 8 sessions/person · 8 months",
            "client_code":
                "Professional services · Milan · associated law firm · "
                "five women lawyers newly promoted to associate in the same year · "
                "sponsor: HR managing partner",
            "lead":
                "A medium-large Milan law firm had promoted five women "
                "lawyers to associate in the same year (a deliberate "
                "investment in the female partnership pipeline). The HR "
                "managing partner engaged Solaria for an eight-month "
                "corporate-group path: an opening shared masterclass plus "
                "eight 1:1 sessions for each of the five coachees, with "
                "quarterly follow-up to the sponsor.",
            "sections": [
                {
                    "label": "The opening goal",
                    "heading": "From senior to associate, with differentiated visibility",
                    "body":
                        "The five coachees, despite the same role "
                        "transition, started with different individual "
                        "needs: some with delegation challenges towards "
                        "senior associates they themselves had been the "
                        "month before, others with visibility challenges "
                        "in the firm's decision-making committees, others "
                        "with identity tensions about a future partnership "
                        "career. Agreed sponsor goal: each coachee with a "
                        "written personal development plan + a set of "
                        "observable practices activated within eight "
                        "months. Aggregate sponsor dashboard (never "
                        "specific session content).",
                },
                {
                    "label": "The path",
                    "heading": "Shared masterclass + eight personalised 1:1s",
                    "body":
                        "A day-long masterclass open to all five coachees "
                        "at the firm, with role framework + ICF code of "
                        "ethics + reciprocal coach-coachee expectations. "
                        "Then eight 60-minute 1:1 sessions per coachee at "
                        "an individually-agreed cadence. Load distribution: "
                        "three coachees followed by Giulia (ICF-PCC) and "
                        "two by Martina (ICF-ACC in PCC pathway), with "
                        "monthly supervision of Martina's cohort. Sponsor "
                        "progress dashboard with three agreed aggregate KPIs.",
                },
                {
                    "label": "The outcome",
                    "heading": "Five active personal plans, three promotions",
                    "body":
                        "At the end of the engagement, all five coachees "
                        "had a written and active personal development "
                        "plan with observable practices. Three of the five "
                        "have been promoted to equity partner in the "
                        "following three years (spontaneous follow-ups "
                        "2024 · 2025 · 2026), one has chosen to leave the "
                        "firm for a general-counsel role on an in-house "
                        "legal team, and one is still senior associate "
                        "with a declared development mandate. The sponsor "
                        "renewed the engagement in 2024 for a new cohort "
                        "of four associates.",
                },
            ],
            "kpi": [
                ("40/40",    "engagement sessions completed (5 × 8)"),
                ("5/5",      "personal plans active at closure"),
                ("3/5",      "promoted to equity partner within 3 years"),
                ("1/1",      "sponsor renewal the year after"),
            ],
            "lead_partner": "Dr. Giulia Loreti · Dr. Martina Erriquez",
            "team":         "2 coaches · 1 ICF-MCC + 1 EMCC supervisor · 8 months",
            "next_label":   "Next case",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Discovery call",
        "headline": "Twenty to thirty minutes, <em>no commitment</em>, no charge.",
        "intro":
            "The discovery call is an exploratory conversation — not a free "
            "coaching session and not a diagnosis. We work out together "
            "whether your goal falls within coaching, whether Solaria is "
            "the right practice for you, and discuss the indicative fee. "
            "At the end you are free to choose another coach, another "
            "professional discipline, or to open no path at all — no "
            "commercial pressure.",

        "form_label":   "Book a discovery call",
        "form_heading": "Fill in the briefing form",
        "form_intro":
            "You will receive confirmation from the practice secretariat "
            "within 24 working hours, with three slot proposals for the "
            "discovery call (a 20-30 minute video conference). Data is "
            "processed under EU Reg. 679/2016 (GDPR) and stored in the "
            "encrypted archive accessible only to the practice's coaches.",
        "form_fields": [
            {"name": "name",      "label": "First name",  "type": "text",     "required": True,  "placeholder": "E.g. Giulia",
             "helper": "First name only."},
            {"name": "surname",   "label": "Last name",   "type": "text",     "required": True,  "placeholder": "E.g. Loreti",
             "helper": "As it appears in your professional signature."},
            {"name": "company",   "label": "Company or professional context", "type": "text", "required": False,
             "placeholder": "E.g. Milan fintech scale-up",
             "helper": "Optional — helps us prepare the discovery call."},
            {"name": "role",      "label": "Current role", "type": "text",    "required": True,  "placeholder": "E.g. Newly-appointed CEO · Middle manager · Firm partner",
             "helper": "The current role or the one you are moving towards."},
            {"name": "email",     "label": "Email",       "type": "email",    "required": True,  "placeholder": "giulia.loreti@example.com",
             "helper": "We send confirmation and three slot proposals to this address."},
            {"name": "phone",     "label": "Phone",       "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Optional — only if you prefer the secretariat to call you back."},
            {"name": "format",    "label": "Preferred format", "type": "select", "required": True,
             "options": [
                 "Decide during discovery call",
                 "Executive 1:1",
                 "Team coaching (I am the corporate sponsor or HR)",
                 "Corporate group (I am the corporate sponsor or HR)",
                 "Single exploratory session",
             ],
             "helper": "Choose \"Decide\" if you are not sure which format fits."},
            {"name": "availability", "label": "Availability over the next 7 days", "type": "select", "required": True,
             "options": [
                 "Morning 9:00 – 12:00",
                 "Early afternoon 14:00 – 16:00",
                 "Late afternoon 16:30 – 19:00",
                 "Evening 19:30 – 21:00 (online only)",
                 "No preference",
             ],
             "helper": "Helps the secretariat propose the three closest slots."},
            {"name": "objective", "label": "Goal in one or two lines", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "E.g. \"I was promoted CEO in January and need to work on operational delegation; the board reviews me in July.\"",
             "helper": "One or two lines are enough to assess whether the goal falls within coaching. No confidential detail here — that goes into the discovery call under NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "The person we will meet on the discovery call.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Context",
             "meta": "Optional — helps us prepare the call. No confidential detail here.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Call perimeter",
             "meta": "So we propose the right slot with the right coach. One or two lines suffice for the goal.",
             "fields": ["format", "availability", "objective"]},
            {"num": "04", "title": "Attachments (optional)",
             "meta": "Current job description, sponsor brief, other materials: they can prepare the discovery call.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Preliminary documents",
            "helper":   "Job description, sponsor brief, possible 360° "
                        "assessment: anything you share here makes the "
                        "discovery call more useful. "
                        "PDF · max 10 MB total. Encrypted archive "
                        "accessible only to the coaches.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "Drag your documents here or",
            "link":     "browse from your archive",
            "meta":     "PDF · max 10 MB · AES-256 encrypted archive",
        },

        "form_submit_label": "Book a discovery call",
        "form_submit_note":
            "Confirmation from the practice secretariat within 24 working "
            "hours, with three slot proposals for the call. No commercial "
            "automation, no email sequences — every request is read personally.",
        "form_consent":
            "I consent to the processing of personal data under EU Reg. "
            "679/2016 (GDPR). Data is stored in the practice's encrypted "
            "archive and is accessible only to Solaria coaches. No data "
            "is shared with third parties without explicit authorisation.",

        "office_address_label": "Address",
        "office_area_label":    "Area",
        "office_phone_label":   "Phone",
        "office_email_label":   "Email",

        "offices_label":   "Office",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Office · also online",
                "address": "Via Thaon di Revel 21 · 20159",
                "area":    "Isola · 300 m from Garibaldi FS metro",
                "phone":   "+39 02 3663 4712",
                "email":   "discovery@solariacoaching.it",
            },
        ],

        "channels_label": "Direct channels",
        "channels": [
            ("Practice secretariat",  "+39 02 3663 4712",               "Mon – Fri · 9:00 – 19:00"),
            ("Discovery email",       "discovery@solariacoaching.it",   "Reply within 24 working hours"),
            ("LinkedIn Giulia Loreti","in/giulialoreti-icf-pcc",        "For non-confidential public questions"),
        ],

        "footnote":
            "Solaria does not respond to anonymous requests and does not "
            "offer \"free diagnosis in ten questions\" (diagnosing is a "
            "consultancy activity, not a coaching one). Administrative "
            "details (indicative quote, billing terms, acceptance criteria) "
            "are explained on the discovery call — free, no commitment, "
            "with an honest assessment of the suitability of coaching to "
            "your specific need.",
    },
}
