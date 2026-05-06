"""Causa — Studio legale (corporate-suite archetype) ·
English locale content tree.

Phase X.6 Causa · workflow C · multilingual rollout on top of the
locked LF-2 Italian draft (A.6 review-lock + A.5b imagery re-curate +
slice-01 + slice-02 + motion_profile DNA pass 1). Mirrors the shape
of ``CAUSA_CONTENT_IT`` exactly — same keys, same nesting, same list
shapes. Only values are translated and adapted.

Voice register: forensic-publication · evidence-led · public-record.
Native English equivalent of the IT register — the legal-press English
of UK barristers' chambers, the Law Reports, ICLR Weekly, Journal of
the Society of Legal Scholars and the Cambridge Law Journal.
Adult-to-adult, declarative, never SaaS-marketing, never general-
counsel-pitch. Reference voices: UK Supreme Court press digests,
Cambridge / OUP legal-press editorials, Law Society Gazette critical
columns.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved
verbatim-in-translation across all 5 locales · the load-bearing
italic moves with the equivalent PUBLIC-RECORD-EVIDENCE noun · per
factory/reports/copy/causa-legale/voice-anchor-lock.md §4.2 +
factory/reports/causa/causa-planner-brief.md §11):
    "Every ruling is <em>evidence</em> on the record — not an opinion defended."

Italian normative references and Italian proper nouns are preserved
verbatim (D.lgs. 24/2023 whistleblowing · D.lgs. 196/2003 privacy ·
D.M. 55/2014 forensic tariffs · Codice Deontologico Forense · art.
622 c.p. professional secrecy · D.lgs. 28/2010 mandatory mediation ·
D.lgs. 74/2000 tax-criminal · D.lgs. 259/2003 telecoms · ENCA · CTU
forense · Tribunale di Milano · Cassazione · TAR Lombardia · Corte
d'Appello di Milano · Foro di Milano · Foro Italiano · Giurisprudenza
Italiana · Albo Avvocati · Reg. UE 679/2016 / GDPR). Italian addresses,
phone formats, Euro figures and years are kept as-is. Italian sentence-
identifiers carry verbatim across all locales (Cass. SS.UU. n.
11237/2024 · Cass. civ. sez. III n. 28914/2023 · TAR Lombardia sez.
III n. 814/2022 · Corte d'Appello Milano sez. trib. n. 3187/2021).
Anti-pattern guardrails carry across: no "Get the verdict you
deserve", no "Best litigation firm in Milan", no Latin-decorative
gavel iconography, no "tier-1 trial lawyer" labels.
"""
from __future__ import annotations

from typing import Any


# Pool URLs imported from the IT module — single source of truth so
# the build-time corporate_suite checks see the same registered Pexels
# URLs across every locale. Mirrors the Solaria / Continua / Cornice
# Pass C precedent.
from apps.catalog.template_content_causa import (  # noqa: E402
    _HERO_COURTROOM_INTERIOR,
    _PORTRAIT_FOUNDER,
    _CASE_HIGHCOURT_EXTERIOR,
    _CASE_FASCICOLI_STACK,
    _CASE_BENCH_CHAIR,
    _CASE_CODEX_SPINE,
)


CAUSA_CONTENT_EN: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "The studio",   "kind": "home"},
        {"slug": "materie",     "label": "Practice",     "kind": "services"},
        {"slug": "studio",      "label": "Publications", "kind": "about"},
        {"slug": "contenzioso", "label": "Litigation",   "kind": "case_study_list"},
        {"slug": "contatti",    "label": "Contact",      "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":     "CAUSA",
        "logo_subtitle": "studio legale",
        "tag":           "Law firm · Milan · since 1995",
        "phone":         "+39 02 7634 8210",
        "email":         "parere@causa.legal",
        "address":       "Via Borgonuovo 14 · 20121 Milan",
        "hours_compact": "Mon – Fri · 09:00 – 18:00 · by appointment",
        "hours_footer_rows": [
            "Saturday · only for filings under deadline",
            "Sunday · closed · reply by Monday",
        ],
        "license":
            "Albo Avvocati Milano · Cassazionista since 2003 · "
            "ENCA mediators register · Albo CTU forense Tribunale di Milano",
        "footer_intro":
            "Editorial litigation boutique. Founding partner Lorenzo "
            "Marchetti · admitted to the Milan Bar since 1995. Single "
            "office in Milan · Foro di Milano. Litigation in every "
            "instance through to the Cassation Court · twenty-eight "
            "rulings cited · fourteen entries in the firm's internal "
            "repertory · thirty-one years of editorial practice.",
        "foot_studio":   "Studio",
        "foot_pages":    "Pages",
        "foot_contact":  "Contact",
        "foot_offices":  "Office",
        "offices_footer_rows": [
            "Milan · Via Borgonuovo 14 · single office",
            "By appointment · Monday-Friday",
            "Foro di Milano · court filings handled in-house",
        ],
        "whistleblowing_footer": {
            "heading":      "Whistleblowing",
            "eyebrow":      "Internal channel · D.lgs. 24/2023",
            "note":
                "The firm operates an internal reporting channel "
                "compliant with D.lgs. 24/2023 (EU Directive "
                "2019/1937). Reporting officer: senior associate, "
                "independent of the founding partner. "
                "Confidentiality safeguarded under the regulations. "
                "Open to associates, employees and the secretariat.",
            "email":        "whistleblowing@causa.legal",
            "policy_label": "Reporting management policy",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Subject",
        "case_year_label":         "Year · filing",
        "case_duration_label":     "Instance · outcome",
        "case_lead_label":         "Lead counsel",
        "case_lead_partner_label": "Lead counsel",
        "case_team_label":         "Drafting team",
        "case_timeline_label":     "Procedural chronology",
    },

    "home": {
        "eyebrow":     "LAW FIRM · MILAN · SINCE 1995",
        # Voice anchor verbatim · italic on the public-record-evidence
        # noun `evidence` (English equivalent of `evidenza` per
        # voice-anchor-lock §4.2). Carries the forensic-press sense
        # ("evidence on the record"), distinct from `proof` (proof of
        # fact) or `testimony` (witness statement). Surface 1/2 of the
        # LF-2 voice anchor recurrence (AC-15) — second surface lands
        # at cs-cta-closer h2 below.
        "headline":
            "Every ruling is <em>evidence</em> on the record — not an opinion defended.",
        "intro":
            "Editorial litigation boutique · founding Cassazionista "
            "partner · twenty-eight rulings cited since 1995.",
        "primary_cta":   "Submit a preliminary opinion",
        "primary_href":  "contatti",
        "secondary_cta": "The studio · single office in Milan",
        "secondary_href":"studio",

        "hero_image":              _HERO_COURTROOM_INTERIOR,
        "hero_image_alt":
            "Empty courtroom · cool light · vertical timber and bone "
            "walls · architectural interior",
        "hero_image_credit_left":  ("Courtroom · interior · 2024", "Foro di Milano"),
        "hero_image_credit_right": ("Studio office", "Milan · Via Borgonuovo 14"),
        # Slice-01 R6 EVID-5 provenance-tooltip body (verbatim
        # numerals + slug preserved across locales).
        "hero_image_provenance":
            "Pexels · CC0 · St George's Hall, Liverpool · no. 33939830",
        "hero_image_provenance_aria":
            "Photograph provenance · Pexels library · CC0 licence",
        "hero_meta_strip": [
            ("Rulings cited",          "28"),
            ("Repertory entries",      "14"),
            ("Years of practice",      "31"),
        ],
        # Side-quote em on the verb form `enters` — verb-form derived
        # from the public-record-evidence anchor. Per voice-anchor-lock
        # §6.4: the side-quote em moves with the verb-form of the
        # public-record-evidence anchor in each locale, within the
        # forensic-press register. EN uses `enters on the record` — the
        # standard barristers'-chambers idiom for placing matter on the
        # public record.
        "hero_side_quote":
            "Counsel before the Court of Cassation and in every "
            "instance below. The firm argues only what it "
            "<em>enters</em> on the record: the evidence filed, the "
            "ruling fit to be cited, the matter of law itself.",

        "narrative_label":   "THE STUDIO · METHOD OF PROOF",
        "narrative_drop":    "G",
        # Slice-02 R3 TIME-3 chronological-tick rail (six milestones).
        # Italian sentence-identifiers preserved verbatim; labels
        # translated. The rail is gated on motion_time3 + content
        # presence; locale parity preserves the AC-V1 sub-variant.
        "narrative_chronotick": [
            ("1995", "Founding · Milan"),
            ("2003", "Cassazionista qualification"),
            ("2008", "First ruling in the internal repertory"),
            ("2014", "First SS.UU. referral"),
            ("2018", "Albo CTU forense registration"),
            ("2024", "Fourteenth entry · SS.UU. on professional liability"),
        ],
        "narrative_blocks": [
            ("drop",
             "ood case-law is grounded. Causa is an editorial "
             "litigation boutique: every cause carried to court is "
             "evidence grounded on the subject of the dispute, on "
             "the instance, on the jurisdiction. We do not sign "
             "decorative opinions — we file pleadings, each with "
             "its own documentation and its own ruling fit to be "
             "cited. The firm exists to measure the file before "
             "litigating it, to write the ruling before arguing it, "
             "to recognise what has already been decided before "
             "proposing what is yet to be decided. It is a slow "
             "craft, opening few causes a year, but carrying them "
             "through to Cassation."),

            ("quote",
             "<em>Jurisdiction</em> is the first form of respect. "
             "What is argued before the right court will always be "
             "more solid than what is decanted in the wrong instance."),

            ("para",
             "Every cause passes through four seasons. Jurisdiction, "
             "first of all: the matter as it already exists is read "
             "as a file, with its precedents, its instances, its "
             "preliminary objections. Then the merits: the subject "
             "of the dispute, the parties, the value bracket, the "
             "procedural urgency, the preliminary evidence available "
             "to be filed. Then the ruling: the brief is written "
             "like a thesis fit to be cited — which principle it "
             "invokes, which orientation it confirms, which "
             "evidence it places on the record. Only then do we "
             "open the litigation, and follow it hearing by hearing, "
             "instance by instance, through to the filing of the "
             "decision. The pleadings stay written: we publish the "
             "rulings obtained in the firm's internal repertory, "
             "because counsel without memory leaves no rule."),

            ("quote",
             "A <em>ruling</em> is not who wins more causes, but "
             "who can name the brief they did not file — and why."),

            ("para",
             "We act for businesses and individuals seeking a "
             "barrister — not a standard executor, not a packaged "
             "associate. Companies with complex banking litigation, "
             "professionals with contested professional liability, "
             "taxpayers facing aggressive assessments, private "
             "bodies with regulatory administrative litigation, "
             "civil parties in tax-criminal proceedings. Our "
             "signature is that of a single Cassazionista, not a "
             "multi-handed law-firm brand: technical responsibility "
             "stays concentrated, because evidence to be argued must "
             "have one voice. Collaborations with technical "
             "consultants, accounting experts, specialist tax "
             "advisors and party counsel pass through the firm — "
             "they do not replace it. We act for few, and through "
             "to the end."),

            ("quote",
             "Publishing a ruling is not promoting it. "
             "It means leaving evidence <em>argued</em> — so that "
             "whoever comes after may contest it, distinguish it, "
             "or recognise it."),

            ("para",
             "The rulings published here are not a forensic CV. "
             "They are evidence on the record, gathered by subject "
             "and by year, with the litigation documentation that "
             "accompanies them. Each card names the jurisdiction, "
             "the instance, the subject, the year, the matter in "
             "dispute, and the ruling filed in five lines — because "
             "a decision that cannot be told in five lines has "
             "probably not yet been clarified. The four decisions "
             "selected below cover four years and four different "
             "subjects: a Joint Sections orientation on professional "
             "liability, a civil cassation in banking litigation, a "
             "TAR Lombardia ruling in regulatory administrative "
             "matter, and a tax appeal in Milan."),
        ],
        "narrative_side_rail": [
            ("Studio · the founding partner",        "studio"),
            ("Practice · the twelve subjects",       "materie"),
            ("Publications · internal repertory",    "studio"),
            ("Contact · submit a preliminary opinion", "contatti"),
        ],

        "sectors_label":    "PRACTICE · THE FIELD OF LITIGATION",
        "sectors_lead":
            "Twelve subjects of litigation: all handled in the "
            "studio, never delegated to external correspondents. The "
            "firm does not declare itself general nor specialist — "
            "it picks its causes by subject, by instance and by "
            "jurisdiction.",
        "sectors": [
            "tax-criminal", "civil contracts", "regulatory administrative",
            "banking litigation", "professional liability", "complex debt recovery",
            "corporate", "tax", "enforcement",
            "complex employment", "court-appointed expert", "ENCA mediation",
        ],
        "sectors_trailing":
            "A subject enters the studio when the evidence is "
            "fit to be placed on the record and the case-law is "
            "readable. It leaves when the file cannot be written "
            "in five lines.",
        "sectors_counter":
            "Twenty-eight rulings cited · fourteen rulings published "
            "by the Foro Italiano and Giurisprudenza Italiana between "
            "<em>2008</em> and 2024 · thirty-one years of practice "
            "in every instance through to Cassation.",

        "leadership_label":   "STUDIO FOUNDER · CASSAZIONISTA",
        "leadership_heading": "Lorenzo <em>Marchetti</em>",
        "leadership_role":
            "founder · responsible for the pleadings and the Cassation briefs",
        "leadership_caption": "The studio · chambers on Via Borgonuovo · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Lorenzo Marchetti opened Causa in Milan in 1995, after "
            "eight years of practice in two Milanese firms "
            "specialised in commercial civil litigation and banking "
            "law. He read law at the Università degli Studi di "
            "Milano (1987), with a thesis on apparent concurrence of "
            "norms in tax law, and obtained the specialisation in "
            "private law at the same university. He has been "
            "admitted to the Milan Bar since 1995 and qualified to "
            "appear before the Higher Magistratures (Cassazionista) "
            "since 2003. He works full-time on the firm's litigation: "
            "he directs the drafting of the pleadings, writes the "
            "Cassation briefs, follows the proceedings to filing of "
            "the decision, and curates the internal repertory that "
            "publishes the rulings obtained.",

            "Among the rulings cited: the 2024 Joint Sections "
            "orientation on the professional liability of the tax "
            "consultant, the 2023 Cassazione civile sez. III decision "
            "on the bank client's right to repayment of compounded "
            "interest, a 2022 ruling of the TAR Lombardia on the "
            "lawfulness of an AGCOM penalty, and the 2021 tax "
            "cassation on the interpretation of art. 36-bis D.P.R. "
            "600/1973. His entries are gathered in fourteen rulings "
            "published by the Foro Italiano and the Giurisprudenza "
            "Italiana between 2008 and 2024.",
        ],
        "leadership_credentials": [
            "Albo Avvocati Milano · Milan Bar registration · since 1995",
            "Cassazionista · admitted to plead before the Higher Magistratures since 2003",
            "ENCA · National Council for Lawyers' Conciliation · mediators' section",
            "Albo CTU forense · Tribunale di Milano · civil-litigation section",
        ],
        "leadership_secondary_cta_label": "Studio · extended biography, repertory entries",
        "leadership_secondary_cta_href":  "studio",

        "cases_label":   "LITIGATION — EVIDENCE ON THE RECORD",
        "cases_intro":
            "Four pieces of evidence filed, in reverse "
            "chronological order. Jurisdiction, instance, subject, "
            "year, matter in dispute, and the ruling filed.",
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · CASS. SS.UU. · 2024 · PROFESSIONAL LIABILITY",
                "title":
                    "Joint Sections — the professional liability of "
                    "the tax consultant, reread as an obligation of "
                    "result <em>grounded</em> on the preliminary evidence",
                "body":
                    "Causa acted for the appellant in the case "
                    "decided by the Joint Civil Sections of the "
                    "Court of Cassation in April 2024, on referral "
                    "from the third civil section. The dispute "
                    "opposed a taxpayer to his tax consultant, on "
                    "the professional liability for failure to flag "
                    "a tax-litigation deadline. The studio argued, "
                    "and the Court accepted, the orientation under "
                    "which the tax consultant's liability is "
                    "grounded on the preliminary evidence the "
                    "professional could and should have known at the "
                    "moment the engagement was accepted — rereading "
                    "the engagement as an obligation of "
                    "circumscribed result. The ruling has been "
                    "published by the Foro Italiano (entry no. 14 "
                    "of the firm's internal repertory).",
                "pill":
                    "Cassazione SS.UU.  ·  legitimacy instance  ·  2024  ·  appellant",
                "photo":    _CASE_HIGHCOURT_EXTERIOR,
                "photo_alt":
                    "Architectural detail of an Italian high court · "
                    "classical pediment with Latin inscription · "
                    "cool overcast light",
                "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
                # Slice-02 R2 EVID-3 case-citation-pop snippet.
                # Italian sentence number preserved verbatim; the
                # paraphrase translates while keeping the legal
                # principle as the em-target. CTA label translates.
                "citation_label": "View ruling no. 14",
                "citation":
                    "Cass. SS.UU. n. 11237/2024 — The "
                    "<em>liability</em> of the tax consultant is "
                    "grounded on the preliminary evidence the "
                    "professional could and should have known at "
                    "the moment the engagement was accepted, the "
                    "performance reread as an obligation of result "
                    "circumscribed to the matter of the mandate. "
                    "Entry no. 14 of the internal repertory · "
                    "published Foro Italiano 2024.",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · CASS. CIV. SEZ. III · 2023 · BANKING LITIGATION",
                "title":
                    "Civil Cassation Section III — compounded "
                    "banking interest and the burden of proof in "
                    "the <em>case-law</em> of legitimacy",
                "body":
                    "Causa acted for the bank client in the civil "
                    "cassation Section III of October 2023, on the "
                    "repayment of compounded interest charged on a "
                    "current account between 2003 and 2014. The "
                    "studio argued the assignment of the burden of "
                    "proof of the causal link to the bank, in line "
                    "with the legitimacy orientation consolidated "
                    "since 2014. The ruling quashed with remand. "
                    "Entry no. 11 of the internal repertory.",
                "pill":
                    "Cass. civ. III  ·  legitimacy instance  ·  2023  ·  appellant",
                "photo":    _CASE_FASCICOLI_STACK,
                "photo_alt":
                    "Stack of legal files with register labels · "
                    "cool desk light · macro · zero people",
                "slug":     "cass-civ-iii-anatocismo-bancario-2023",
                "citation_label": "View ruling no. 11",
                "citation":
                    "Cass. civ. sez. III n. 28914/2023 — On the "
                    "repayment of <em>compounded</em> interest "
                    "charged on a current bank account, the burden "
                    "of proof of the causal link between quarterly "
                    "capitalisation and balance inflation rests on "
                    "the bank, in line with the legitimacy "
                    "orientation consolidated since 2014. Quashed "
                    "with remand. Entry no. 11 of the internal "
                    "repertory.",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · TAR LOMBARDIA · 2022 · REGULATORY ADMINISTRATIVE",
                "title":
                    "TAR Lombardia — annulment of an AGCOM penalty "
                    "and the <em>principle</em> of proportionality",
                "body":
                    "Causa acted for the appellant in the first-"
                    "instance proceedings before TAR Lombardia, "
                    "Section III, concluded in April 2022 with the "
                    "annulment of the AGCOM penalty challenged for "
                    "excess of power and breach of the principle of "
                    "proportionality of the administrative monetary "
                    "sanction, in light of the 2019 Council of "
                    "State orientation. The ruling was not appealed "
                    "by AGCOM. Entry no. 9 of the internal repertory.",
                "pill":
                    "TAR Lombardia  ·  first instance  ·  2022  ·  appellant",
                "photo":    _CASE_BENCH_CHAIR,
                "photo_alt":
                    "Empty judicial bench seat · high oak back · "
                    "vertical timber panels behind · cool light · "
                    "zero people",
                "slug":     "tar-lombardia-agcom-proporzionalita-2022",
                "citation_label": "View ruling no. 9",
                "citation":
                    "TAR Lombardia sez. III n. 814/2022 — Annulment "
                    "of the AGCOM penalty for excess of power and "
                    "breach of the <em>principle</em> of "
                    "proportionality of the administrative monetary "
                    "sanction, in light of the orientation of the "
                    "Council of State sec. VI 4419/2019. Ruling not "
                    "appealed by AGCOM. Entry no. 9 of the internal "
                    "repertory.",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · MILAN COURT OF APPEAL · 2021 · TAX",
                "title":
                    "Milan Court of Appeal — art. 36-bis D.P.R. "
                    "600/1973 and the perimeter of the tax "
                    "<em>dispute</em>",
                "body":
                    "Causa argued, on appeal before the Corte "
                    "d'Appello di Milano sez. tributaria, the "
                    "restrictive interpretation of art. 36-bis "
                    "D.P.R. 600/1973 on the automated assessment of "
                    "income-tax returns. The ruling, filed in "
                    "September 2021, reversed the first-instance "
                    "decision of the Tax Commission and annulled "
                    "the payment notice. Entry no. 7 of the "
                    "internal repertory.",
                "pill":
                    "App. Milano trib.  ·  second instance  ·  2021  ·  appellant",
                "photo":    _CASE_CODEX_SPINE,
                "photo_alt":
                    "Macro of a leather-bound codex spine · "
                    "gilt typography on dark leather · Roman "
                    "numbering · soft cool light",
                "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
                "citation_label": "View ruling no. 7",
                "citation":
                    "Corte d'Appello Milano sez. trib. n. 3187/2021 "
                    "— Restrictive interpretation of art. 36-bis "
                    "D.P.R. 29 September 1973 no. 600 on the "
                    "automated assessment of income-tax returns · "
                    "the perimeter of the tax <em>dispute</em> is "
                    "limited to mere material and arithmetic errors "
                    "detectable from the return, excluding any "
                    "substantive evaluation. Ruling reversed on "
                    "appeal. Entry no. 7 of the internal repertory.",
            },
        ],
        "cases_trailing_label": "All litigation · chronology 1995–2024",
        "cases_trailing_href":  "contenzioso",

        "cta_label":     "PRELIMINARY OPINION",
        "cta_intro":
            "Every brief begins from a single page: the preliminary opinion.",
        # Voice anchor verbatim recurrence on cta-closer h2 (surface
        # 2/2 of AC-15) — em on `evidence`, the public-record-evidence
        # cognate.
        "cta_heading":
            "Every ruling is <em>evidence</em> on the record — not an opinion defended.",
        "cta_form_hint":
            "Subject of the dispute · instance · counterparty · "
            "value bracket · jurisdiction · preliminary evidence "
            "available. Reply within five working days.",
        "cta_primary":   "Submit a preliminary opinion",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "No discovery call. No mandate without screening. "
            "Only the evidence, and its jurisdiction.",
        "cta_sub_line":
            "Causa · law firm · Milan · since 1995",
    },

    "studio": {
        "eyebrow":   "THE STUDIO · WHO WE ARE · CV",
        "headline":
            "Causa · editorial litigation boutique since <em>1995</em>.",
        "intro":
            "Milan. One founding partner, two associates, one "
            "secretariat. We act for few, and through to the end.",
        "primary_cta":  "Submit a preliminary opinion",

        "history_label":   "STUDIO MILESTONES",
        "history_heading": "Five dates, thirty-one years of editorial practice.",
        "history_intro":
            "Five structural choices behind which the firm's "
            "character can be read — the authoriality of a single "
            "Cassazionista, the internal repertory as method, "
            "jurisdiction as the first form of respect, the subject "
            "as the field of litigation, counsel through to the "
            "filing of the decision.",
        "history": [
            ("1995", "Founding",
             "Lorenzo Marchetti opens Causa on Via Borgonuovo in "
             "Milan, after eight years of practice in two Milanese "
             "firms specialised in commercial civil litigation and "
             "banking law. The office is chosen for one reason "
             "alone: three rooms on an inner courtyard, one for "
             "the drafting of pleadings, one for the internal "
             "repertory, one for the secretariat."),
            ("2003", "Cassazionista qualification",
             "Lorenzo Marchetti obtains the qualification to plead "
             "before the Higher Magistratures (Cassazionista). "
             "From that year the firm accepts cassation appeals on "
             "civil, tax and administrative matters, and curates "
             "the briefs for respondents in legitimacy proceedings."),
            ("2008", "First ruling published in the internal repertory",
             "The first legitimacy ruling citing an orientation "
             "argued by the studio is published by the Foro "
             "Italiano. From that year the firm records every "
             "ruling obtained — won or lost — in the internal "
             "repertory within sixty days of filing."),
            ("2018", "Albo CTU forense registration",
             "The firm registers with the Albo CTU forense of the "
             "Tribunale di Milano (civil-litigation section). From "
             "that year it accepts court-appointed expert duties on "
             "corporate litigation, contested company valuations "
             "and accounting liability."),
            ("2024", "Fourteenth entry in the internal repertory",
             "The firm's fourteenth ruling enters the internal "
             "repertory: the Joint Sections orientation on the "
             "professional liability of the tax consultant, on "
             "referral from the third civil section. Counsel for "
             "the appellant client, ruling filed in April, entry "
             "published by the Foro Italiano."),
        ],

        "values_label":   "EDITORIAL PRINCIPLES",
        "values_heading": "Four <em>non-negotiable</em> principles",
        "values_intro":
            "Four principles separate a Causa engagement from a "
            "standardised mandate. They are written into the "
            "engagement letter signed at the first meeting, not on "
            "the website.",
        "values": [
            ("01", "An authorial Cassazionista",
             "The signature on the brief is that of a single "
             "barrister, not a multi-handed law-firm brand. "
             "Technical responsibility stays concentrated, because "
             "evidence to be argued must have one voice. External "
             "collaborations pass through the firm — they do not "
             "replace it."),
            ("02", "Jurisdiction as the first gesture",
             "Every cause opens with a serious jurisdiction "
             "screening. The matter as it already exists is read as "
             "a file, with its precedents, its instances, its "
             "preliminary objections. No engagement before the "
             "court, the instance and the jurisdiction have been "
             "read in full."),
            ("03", "The internal repertory as method",
             "Every ruling obtained — won and lost — is recorded in "
             "the internal repertory within sixty days of filing, "
             "with the complete proceedings documentation. The "
             "repertory is not marketing: it is the rule we leave "
             "behind for those who come after."),
            ("04", "No paid screening rejections",
             "Preliminary opinions that do not pass the screening "
             "stage are returned with a written motivated note, "
             "free of charge. We do not invoice rejected screenings. "
             "Assessing whether the evidence can be placed on the "
             "record is the door of the studio, not a metered "
             "service."),
        ],

        "team_label":   "STUDIO AND ASSOCIATES",
        "team_heading": "Three barristers, one office, one secretariat.",
        "team_intro":
            "The studio is made up of one founding Cassazionista "
            "barrister, two associates and one secretariat. We work "
            "full-time on twelve to eighteen causes in parallel — "
            "never more than twenty. Court filings, the prosecutor's "
            "office, the State Bar and regulators are handled in-"
            "house, never delegated to external correspondents.",
        "team": [
            {"name": "Lorenzo Marchetti",
             "role": "Studio Founder · Cassazionista",
             "office": "Milan",
             "bio":
                "Founder. Università degli Studi di Milano · Law · "
                "specialisation in private law. Milan Bar since 1995 "
                "· Cassazionista since 2003 · ENCA mediators · Albo "
                "CTU forense Tribunale di Milano. Directs the "
                "drafting of pleadings, writes the Cassation briefs, "
                "curates the internal repertory."},
            {"name": "Avv. Chiara Bevilacqua",
             "role": "Associate · Corporate + banking",
             "office": "Milan",
             "bio":
                "Associate since 2017 · Milan Bar since 2014 · "
                "specialisation in corporate law and banking "
                "litigation · supervises the appellant pleadings in "
                "corporate disputes and liability actions · curator "
                "of the internal repertory · ENCA mediators since "
                "2020."},
            {"name": "Avv. Tommaso De Luca",
             "role": "Associate · Administrative + tax",
             "office": "Milan",
             "bio":
                "Associate since 2021 · Milan Bar since 2018 · "
                "specialisation in administrative law and tax "
                "litigation · curator for the appeals to the TAR "
                "Lombardia and the Tax Commissions · Albo CTU "
                "forense Tribunale di Milano since 2022 (civil-"
                "litigation section)."},
        ],

        "coordinates_label": "THE OFFICE",
        "coordinates": [
            ("Milan", "Via Borgonuovo 14 · 20121 · three rooms on an inner courtyard"),
            ("Studio", "by appointment · Monday-Friday · 09:00-18:00"),
            ("Foro di Milano", "court filings handled in-house · zero external correspondents"),
        ],

        "cta_heading": "An engagement begins from a single page.",
        "cta_intro":
            "The first page of every engagement is the preliminary "
            "opinion: a one-page screening the studio reads in "
            "full, replying within five working days with a "
            "motivated note. If the opinion is negative, the note "
            "is delivered free of charge · no screening invoiced · "
            "no obligation to retain the firm.",
        "cta_primary":   "Submit a preliminary opinion",
        "cta_primary_href": "contatti",
    },

    "materie": {
        "eyebrow":  "PRACTICE · THE TWELVE SUBJECTS OF LITIGATION",
        "headline": "The <em>subjects</em> of litigation — twelve, all handled in-studio.",
        "intro":
            "The firm does not declare itself general nor "
            "specialist. The subjects are the field of litigation: "
            "what determines the jurisdiction and the instance. A "
            "subject enters the studio when the evidence can be "
            "placed on the record and the case-law is readable in "
            "five lines.",
        "primary_cta":  "Submit a preliminary opinion",

        "svc_duration_label": "Court · instance",
        "svc_leader_label":   "Lead counsel",

        "services": [
            {
                "num":   "01",
                "title": "Tax-criminal",
                "blurb":
                    "Counsel in every instance of tax-criminal "
                    "proceedings for entrepreneurs, directors and "
                    "self-employed professionals. Defence in "
                    "proceedings for failure to file, failure to "
                    "pay and fraudulent subtraction of tax under "
                    "D.lgs. 74/2000.",
                "scope": [
                    "Defence of accused and civil parties",
                    "Special procedures and plea-bargain ex art. 444 c.p.p.",
                    "Cassation criminal appeals (sec. III + sec. V)",
                    "Coordination with party-appointed tax consultants",
                ],
                "duration": "Tribunal · App. · Cassation",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "02",
                "title": "Civil contracts",
                "blurb":
                    "Civil litigation on commercial contracts, "
                    "supply, agency, distribution, services. "
                    "Actions for breach, contractual rescission, "
                    "damages and actions for nullity due to consent "
                    "defects.",
                "scope": [
                    "Causes above € 50,000",
                    "Writs of summons and authorised pleadings",
                    "Urgent measures ex art. 700 c.p.c.",
                    "Civil cassation appeals",
                ],
                "duration": "Tribunal · App. · Cassation",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "03",
                "title": "Regulatory administrative",
                "blurb":
                    "Appeals against the acts of the independent "
                    "Authorities (AGCOM, AGCM, Privacy Guarantor, "
                    "ANAC). Challenges to penalty acts, refusal "
                    "acts, injunctive measures. Counsel at first "
                    "instance before the TAR and on appeal before "
                    "the Council of State.",
                "scope": [
                    "Appeals to TAR Lombardia · sec. III · regulatory",
                    "Appeals to the Council of State · sec. VI",
                    "Oral-hearing pleadings",
                    "Coordination with party-appointed technical experts",
                ],
                "duration": "TAR · Council of State",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "04",
                "title": "Banking litigation",
                "blurb":
                    "Causes against banks for compounded interest, "
                    "usury, erroneous Central Risk Office reporting, "
                    "challenges to mortgage contracts, leasing and "
                    "derivatives. Counsel in every instance, "
                    "through to civil Cassation.",
                "scope": [
                    "Accounting expertises and party reports",
                    "Restitution actions and clause-nullity actions",
                    "Civil cassation appeals sec. I + III",
                    "Coordination with independent banking experts",
                ],
                "duration": "Trib. · App. · Cassation",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "05",
                "title": "Professional liability",
                "blurb":
                    "Liability actions against tax consultants, "
                    "lawyers, doctors and technical professionals. "
                    "Counsel both for the harmed party and for the "
                    "professional defendant. A subject in constant "
                    "case-law evolution (see Cass. SS.UU. 2024).",
                "scope": [
                    "Contractual and extracontractual damages actions",
                    "Quantification of damage according to legitimacy",
                    "Cassation appeals (also SS.UU.)",
                    "Technical pleadings and reconstruction of evidence",
                ],
                "duration": "Trib. · App. · Cassation · SS.UU.",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "06",
                "title": "Complex debt recovery",
                "blurb":
                    "Recovery of commercial credits above € 50,000 "
                    "· payment orders and related oppositions · "
                    "movable and immovable enforcement · ordinary "
                    "and bankruptcy revocatory actions.",
                "scope": [
                    "Payment orders and oppositions",
                    "Third-party enforcement and revocatory actions",
                    "Real-estate and movable enforcement",
                    "Coordination with valuation experts",
                ],
                "duration": "Trib. · Enforcement",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "07",
                "title": "Corporate litigation",
                "blurb":
                    "Liability actions against directors, statutory "
                    "auditors and general managers. Challenges to "
                    "resolutions of shareholders' meetings and "
                    "boards. Shareholders' agreements, covenant "
                    "breach. Litigation among shareholders in "
                    "limited-liability companies.",
                "scope": [
                    "Actions ex artt. 2392-2395 c.c.",
                    "Challenges to resolutions ex art. 2377 c.c.",
                    "Causes before the Companies Tribunal",
                    "Civil cassation appeals sec. I",
                ],
                "duration": "Companies Trib. · App. · Cassation",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "08",
                "title": "Tax",
                "blurb":
                    "Appeals against tax assessments of the "
                    "Italian Revenue Agency. Counsel before the "
                    "Tax Justice Courts at first and second "
                    "instance. Cassation appeals on tax matters.",
                "scope": [
                    "Payment notices and tax-roll registrations",
                    "Tax assessment and rectification notices",
                    "Pre-trial cross-examination pleadings",
                    "Appeals ex art. 360 c.p.c. n. 3",
                ],
                "duration": "CGT 1° · CGT 2° · Cassation",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "09",
                "title": "Enforcement",
                "blurb":
                    "Movable, immovable and third-party "
                    "enforcement procedures. Oppositions to "
                    "enforcement and to enforcement acts. Counsel "
                    "for proceeding creditors and seized debtors.",
                "scope": [
                    "Real-estate seizures and sale procedures",
                    "Oppositions ex artt. 615, 617, 619 c.p.c.",
                    "Distribution of proceeds",
                    "Coordination with judicial custodians",
                ],
                "duration": "Trib. enforcement",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "10",
                "title": "Complex employment",
                "blurb":
                    "High-complexity employment litigation — "
                    "executive dismissals, harassment, "
                    "demotion, contested variable pay. Cases with "
                    "corporate or regulatory implications. NO "
                    "standard individual litigation.",
                "scope": [
                    "Dismissals ex artt. 18 St. lav. + Jobs Act",
                    "Damages actions for harassment and demotion",
                    "Non-compete agreements and interim appeals",
                    "Cassation appeals · employment section",
                ],
                "duration": "Labour Trib. · App. · Cassation",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "11",
                "title": "Court-appointed expert",
                "blurb":
                    "The studio is registered with the Albo CTU "
                    "forense of the Tribunale di Milano (civil-"
                    "litigation section). Technical expert duties "
                    "on corporate litigation, contested company "
                    "valuations and accounting liability.",
                "scope": [
                    "CTU on corporate litigation",
                    "Contested company valuations",
                    "Accounting and financial liability",
                    "Expert reports on judge's mandate",
                ],
                "duration": "CTU · Trib. Milano",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "12",
                "title": "ENCA mediation",
                "blurb":
                    "The firm is registered in the mediators' "
                    "section of ENCA (National Council for Lawyers' "
                    "Conciliation). Mandatory civil mediation in "
                    "the matters of law, judge-delegated mediation, "
                    "and arbitration procedures under ritual-"
                    "arbitration agreements.",
                "scope": [
                    "Mandatory civil mediation ex D.lgs. 28/2010",
                    "Judge-delegated mediation",
                    "Ritual arbitrations ex artt. 806 ss. c.p.c.",
                    "Settlement and motivated-closure minutes",
                ],
                "duration": "ENCA · arbitration",
                "leader":   "Chiara Bevilacqua",
            },
        ],

        "process_label":   "METHOD · FOUR SEASONS OF COUNSEL",
        "process_heading": "Four phases, one forensic sequence.",
        "process": [
            ("01", "Jurisdiction",
             "The matter as it already exists is read as a file. "
             "Court, instance, preliminary objections. Jurisdiction "
             "is the first form of respect and typically takes five "
             "days of screening."),
            ("02", "Merits",
             "Subject of the dispute, parties, value bracket, "
             "procedural urgency, preliminary evidence available. "
             "The merits are the frame of counsel: they define "
             "which brief is written and which is not."),
            ("03", "Ruling",
             "The brief is written like a thesis fit to be cited "
             "— which principle it invokes, which orientation it "
             "confirms, which evidence it places on the record. "
             "Five lines in which the decision must be tellable."),
            ("04", "Filing",
             "Hearing by hearing, instance by instance, through to "
             "the filing of the decision. Every ruling obtained "
             "stays written in the internal repertory · published "
             "within sixty days of filing."),
        ],

        "cta_heading":   "Which subject suits your dispute?",
        "cta_intro":
            "If the subject is unclear, write us a brief "
            "description of the dispute and the current instance. "
            "We will indicate the right subject within five working "
            "days · within forty-eight hours if the urgency is "
            "procedural (deadline expiring · hearing scheduled).",
        "cta_primary":   "Submit a preliminary opinion",
        "cta_primary_href": "contatti",
    },

    "contenzioso": {
        "eyebrow":  "LITIGATION · CHRONOLOGY 1995-2024",
        "headline":
            "The rulings cited — the <em>chronology</em> of practice · 1995–2024.",
        "intro":
            "Fourteen rulings published by the Foro Italiano and "
            "the Giurisprudenza Italiana, plus the other selected "
            "litigation. All recorded in the internal repertory "
            "within sixty days of filing.",
        "primary_cta":  "Submit a preliminary opinion",

        "cases_label": "Four representative decisions · in detail",
        "cases_intro":
            "The firm records every ruling obtained — won or lost "
            "— in the internal repertory within sixty days of "
            "filing. The four decisions featured below are those "
            "selected editorially to illustrate the firm's method: "
            "one for the Joint Sections of the Court of "
            "Cassation, one for the civil cassation simple "
            "section, one for the administrative jurisdiction, "
            "and one for the tax appeal.",

        "cta_heading":   "A cause similar to yours?",
        "cta_intro":
            "Complete files (pleadings, briefs, replies, "
            "proceedings documentation, rulings notes) are "
            "available in the studio on motivated request. "
            "Consultation is free of charge under the Codice "
            "Deontologico Forense; the printed copy of the "
            "internal repertory is provided at print cost.",
        "cta_primary":   "Submit a preliminary opinion",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
            "title":
                "Joint Sections — the professional liability of the "
                "tax consultant, reread as an obligation of result "
                "grounded on the preliminary evidence",
            "category": "Professional liability",
            "year":     "2024 · April filing",
            "duration": "Cassazione SS.UU. · legitimacy instance · quashed without remand",
            "client_code":
                "Cassazione · Joint Civil Sections · referral from "
                "the third civil section · principal appellant · "
                "counterparty: tax-consultant defendant · subject: "
                "professional liability · obligation of "
                "circumscribed result vs obligation of means.",
            "lead":
                "The dispute was referred to the cognition of the "
                "Joint Sections of the Court of Cassation by the "
                "third civil section, in light of the conflict "
                "between two legitimacy orientations on the "
                "qualification of the tax consultant's obligation "
                "with respect to the timely flagging of a tax-"
                "litigation deadline.",
            "sections": [
                {
                    "label": "The jurisdiction",
                    "heading": "Referral from the third civil section to the Joint Sections",
                    "body":
                        "The proceedings were referred to the "
                        "cognition of the Joint Sections of the "
                        "Court of Cassation by the third civil "
                        "section, by interlocutory order of "
                        "September 2023, in light of the conflict "
                        "between two legitimacy orientations on "
                        "the qualification of the tax consultant's "
                        "obligation. The first orientation "
                        "(dominant between 2014 and 2020) "
                        "qualified the obligation as an obligation "
                        "of means, with the consequent burden of "
                        "proving the causal link on the client; "
                        "the second (emerging from 2021) qualified "
                        "the obligation as an obligation of "
                        "circumscribed result.",
                },
                {
                    "label": "The argument advanced",
                    "heading": "Obligation of result grounded on the preliminary evidence",
                    "body":
                        "The studio, as counsel for the appellant "
                        "client, argued the orientation of the "
                        "obligation of circumscribed result, "
                        "invoking the principle of foreseeability "
                        "of the preliminary evidence at the moment "
                        "of acceptance of the professional "
                        "engagement. The defence brief recalled "
                        "the orientation of the civil cassation "
                        "section III of 2022 on the criteria of "
                        "foreseeability of the tax-litigation "
                        "deadline, and proposed the rereading of "
                        "the obligation as a liability grounded on "
                        "the qualified diligence required of the "
                        "consultant.",
                },
                {
                    "label": "The outcome",
                    "heading": "Quashed without remand · entry no. 14",
                    "body":
                        "The Joint Sections accepted the "
                        "reconstruction argued by the studio, "
                        "confirming the orientation of the "
                        "obligation of circumscribed result and "
                        "grounding it on the criterion of "
                        "foreseeability of the preliminary "
                        "evidence. The ruling quashed without "
                        "remand the second-instance decision of "
                        "the Court of Appeal, declaring the "
                        "liability of the tax-consultant defendant "
                        "and quantifying the damage according to "
                        "the consolidated legitimacy case-law. "
                        "The entry has been published by the Foro "
                        "Italiano (entry no. 14 of the firm's "
                        "internal repertory).",
                },
            ],
            "kpi": [
                ("SS.UU.",      "Joint Civil Sections"),
                ("April 2024",  "ruling filed"),
                ("quashed",     "without remand"),
                ("entry 14",    "Foro Italiano"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Founding partner + 1 associate · drafting of the "
                "appeal, response and defence brief in view of the "
                "Joint Sections hearing",
            "next_label":   "Next chronology",
        },
        {
            "slug":     "cass-civ-iii-anatocismo-bancario-2023",
            "title":
                "Civil Cassation Section III — compounded banking "
                "interest and the burden of proof in the case-law "
                "of legitimacy",
            "category": "Banking litigation",
            "year":     "2023 · October filing",
            "duration": "Cass. civ. III · legitimacy instance · quashed with remand",
            "client_code":
                "Cassazione · third civil section · appellant · "
                "counterparty: respondent bank · subject: "
                "compounded banking interest · burden of proof of "
                "the causal link assigned to the bank.",
            "lead":
                "The first- and second-instance proceedings had "
                "rejected the bank client's claim for repayment of "
                "compounded interest. The studio appealed to "
                "cassation, arguing the assignment of the burden "
                "of proof to the bank.",
            "sections": [
                {
                    "label": "The previous instances",
                    "heading": "Tribunal of Milan · Companies Section · and Court of Appeal of Milan",
                    "body":
                        "The first-instance proceedings before the "
                        "Tribunal of Milan · Companies Section · "
                        "and the second-instance proceedings "
                        "before the Court of Appeal of Milan had "
                        "rejected the bank client's claim for "
                        "repayment of compounded interest charged "
                        "on a current account between 2003 and "
                        "2014, on the ground that the client had "
                        "not provided specific proof of the "
                        "unlawful capitalisation.",
                },
                {
                    "label": "The argument advanced",
                    "heading": "Burden of proof grounded on the bank",
                    "body":
                        "The studio appealed to cassation, "
                        "arguing the assignment of the burden of "
                        "proof of the causal link to the bank, in "
                        "line with the legitimacy orientation "
                        "consolidated by the civil cassation "
                        "section I in 2014 and by the Joint "
                        "Sections in 2018. The appeal articulated "
                        "the rereading of the discipline of "
                        "compounded banking interest within the "
                        "framework of the informational asymmetry "
                        "between bank and account holder.",
                },
                {
                    "label": "The outcome",
                    "heading": "Quashed with remand · entry no. 11",
                    "body":
                        "The civil cassation section III quashed "
                        "the appellate ruling with remand to the "
                        "Court of Appeal of Milan in different "
                        "composition, accepting the orientation "
                        "argued by the studio. The remand "
                        "proceedings were ordered under the "
                        "principle of legitimacy in conformity. "
                        "The entry has been recorded in the "
                        "internal repertory (no. 11) and is "
                        "awaiting external publication.",
                },
            ],
            "kpi": [
                ("Cass. III",     "civil section"),
                ("October 2023",  "ruling filed"),
                ("quashed",       "with remand"),
                ("entry 11",      "internal repertory"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Founding partner + 1 associate · cassation "
                "appeal, response and brief filed for the hearing "
                "· support of an independent banking expert",
            "next_label":   "Next chronology",
        },
        {
            "slug":     "tar-lombardia-agcom-proporzionalita-2022",
            "title":
                "TAR Lombardia — annulment of an AGCOM penalty and "
                "the principle of proportionality",
            "category": "Regulatory administrative",
            "year":     "2022 · April filing",
            "duration": "TAR Lombardia · first instance · full annulment",
            "client_code":
                "TAR Lombardia · section III · appellant · "
                "counterparty: AGCOM · subject: regulatory "
                "administrative · monetary penalty · principle of "
                "proportionality ex Council of State sec. VI 2019.",
            "lead":
                "The studio appealed to the TAR Lombardia for the "
                "annulment of an AGCOM penalty issued against an "
                "electronic-communications operator for alleged "
                "breach of the rules on transparency of commercial "
                "offers.",
            "sections": [
                {
                    "label": "The challenged act",
                    "heading": "AGCOM penalty ex art. 98 D.lgs. 259/2003",
                    "body":
                        "The studio appealed to the TAR Lombardia "
                        "for the annulment of an AGCOM penalty "
                        "issued against an electronic-"
                        "communications operator for alleged "
                        "breach of the rules on transparency of "
                        "commercial offers. The penalty had been "
                        "issued at the conclusion of an "
                        "investigation phase with six months of "
                        "procedural cross-examination.",
                },
                {
                    "label": "The grounds of appeal",
                    "heading": "Excess of power and breach of the principle of proportionality",
                    "body":
                        "The appeal was based on two principal "
                        "grounds. The first, for excess of power "
                        "under the head of failure of "
                        "investigation: the Authority had not "
                        "acquired some evidentiary elements "
                        "produced by the operator during the "
                        "procedural cross-examination. The second, "
                        "for breach of the principle of "
                        "proportionality of the administrative "
                        "monetary sanction, in light of the 2019 "
                        "Council of State sec. VI orientation on "
                        "the criteria for determining the sanction "
                        "considering the gravity of the conduct, "
                        "the conduct of the agent and his ability "
                        "to pay.",
                },
                {
                    "label": "The outcome",
                    "heading": "Full annulment · entry no. 9",
                    "body":
                        "The TAR Lombardia accepted the appeal, "
                        "annulling the penalty in full for breach "
                        "of the principle of proportionality. The "
                        "ruling was not appealed by AGCOM. The "
                        "entry has been recorded in the internal "
                        "repertory (no. 9) and has contributed to "
                        "the consolidation of the orientation on "
                        "the proportionality of regulatory "
                        "sanctions.",
                },
            ],
            "kpi": [
                ("TAR Lomb.",     "section III"),
                ("April 2022",    "ruling filed"),
                ("annulled",      "in full"),
                ("entry 9",       "internal repertory"),
            ],
            "lead_partner": "Tommaso De Luca · Associate",
            "team":
                "Associate + founding partner · introductory "
                "appeal, reply brief to AGCOM and oral-hearing brief",
            "next_label":   "Next chronology",
        },
        {
            "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
            "title":
                "Milan Court of Appeal · tax section — art. 36-bis "
                "D.P.R. 600/1973 and the perimeter of the tax "
                "dispute",
            "category": "Tax",
            "year":     "2021 · September filing",
            "duration": "App. Milano trib. · second instance · reversed on appeal",
            "client_code":
                "Corte d'Appello Milano · tax section · appellant "
                "· counterparty: Italian Revenue Agency · subject: "
                "tax · automated assessment ex art. 36-bis D.P.R. "
                "600/1973 · restrictive contributory perimeter.",
            "lead":
                "The first-instance proceedings before the "
                "Provincial Tax Commission of Milan had concluded "
                "with the rejection of the taxpayer's appeal "
                "against a payment notice issued following an "
                "automated check ex art. 36-bis D.P.R. 600/1973.",
            "sections": [
                {
                    "label": "The first instance",
                    "heading": "Provincial Tax Commission of Milan · appeal rejected",
                    "body":
                        "The first-instance proceedings before the "
                        "Provincial Tax Commission of Milan had "
                        "concluded with the rejection of the "
                        "taxpayer's appeal against a payment "
                        "notice issued following an automated "
                        "check ex art. 36-bis D.P.R. 600/1973. The "
                        "Commission had held a merely formal check "
                        "sufficient to ground the tax claim.",
                },
                {
                    "label": "The argument advanced",
                    "heading": "Restrictive interpretation of art. 36-bis D.P.R. 600/1973",
                    "body":
                        "The studio appealed, arguing the "
                        "restrictive interpretation of art. 36-bis "
                        "which limits the automated check to a "
                        "merely arithmetic assessment of the "
                        "declared taxes, with no possibility of "
                        "rectification of the substantive content "
                        "of the return (orientation of the tax "
                        "cassation of 2017 and 2019). The defence "
                        "brief articulated the rereading of the "
                        "perimeter of the tax dispute within the "
                        "framework of the distribution between "
                        "automated check and substantive "
                        "rectification.",
                },
                {
                    "label": "The outcome",
                    "heading": "Reversed on appeal · entry no. 7",
                    "body":
                        "The Court of Appeal accepted the appeal "
                        "in full, annulling the payment notice "
                        "and ordering the Italian Revenue Agency "
                        "to pay the costs of proceedings. The "
                        "ruling was not appealed to the Court of "
                        "Cassation and has contributed to the "
                        "consolidation of the restrictive "
                        "orientation. Entry no. 7 of the internal "
                        "repertory.",
                },
            ],
            "kpi": [
                ("App. Milan",     "tax section"),
                ("September 2021", "ruling filed"),
                ("reversed",       "on appeal"),
                ("entry 7",        "internal repertory"),
            ],
            "lead_partner": "Tommaso De Luca · Associate",
            "team":
                "Associate + founding partner · appeal pleadings, "
                "reply brief to the Italian Revenue Agency and "
                "oral-hearing brief",
            "next_label":   "Next chronology",
        },
    ],

    "contatti": {
        "eyebrow":  "SUBMIT A PRELIMINARY OPINION",
        "headline": "Submit a <em>preliminary</em> opinion — the first page of counsel.",
        "intro":
            "The firm replies within five working days · within "
            "forty-eight hours if the urgency is procedural "
            "(deadline expiring · hearing scheduled).",
        "primary_cta":  "Submit a preliminary opinion",

        "form_label":   "PRELIMINARY OPINION",
        "form_heading": "Fill in the screening sheet",
        "form_intro":
            "The preliminary opinion is the first page of "
            "counsel: the firm reads the subject of the dispute, "
            "the current instance, the jurisdiction, the value "
            "bracket and the urgency, and returns an assessment "
            "of whether the evidence can be placed on the record "
            "and whether the case-law is readable in five lines. "
            "The opinion is NOT a defence mandate · NOT a metered "
            "estimate · NOT a discovery call. It is a technical "
            "screening, motivated in writing, from which to decide "
            "together whether to open the file. If the opinion is "
            "negative, the motivated note is delivered free of "
            "charge.",

        "form_fields": [
            {"name": "name",      "label": "First name", "type": "text", "required": True,
             "placeholder": "e.g. Marco",
             "helper": "Given name only, please."},
            {"name": "surname",   "label": "Surname",  "type": "text", "required": True,
             "placeholder": "e.g. Bianchi",
             "helper": "As it appears in the client's documents."},
            {"name": "email",     "label": "Email",    "type": "email", "required": True,
             "placeholder": "marco@domain.com",
             "helper": "An inbox that will receive the fiduciary motivated note."},
            {"name": "phone",     "label": "Phone", "type": "tel", "required": False,
             "placeholder": "+39 ...",
             "helper": "Direct line for the first contact. Optional."},
            {"name": "oggetto", "label": "Subject of the dispute",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Describe in 5-10 lines the subject of the "
                 "dispute, the parties and the point at issue. "
                 "Completeness is not required · a synthetic "
                 "description is enough.",
             "helper":
                 "Enough to tell whether the subject can be "
                 "placed on the record. Do not yet attach the "
                 "complete file · figures and other data are "
                 "discussed at the first meeting."},
            {"name": "grado", "label": "Current instance", "type": "select", "required": True,
             "options": [
                 "first instance (Tribunal · CGT · TAR)",
                 "appeal (Court of Appeal · CGT 2° · Council of State)",
                 "Cassation (in progress or to be filed)",
                 "administrative proceedings not yet opened",
                 "proceedings not yet opened (preliminary opinion)",
             ],
             "helper": "The instance in which the cause currently sits."},
            {"name": "controparte", "label": "Counterparty type", "type": "text", "required": True,
             "placeholder":
                 "e.g. bank · public body · commercial "
                 "counterparty · public administration · private",
             "helper":
                 "It is not necessary to name the specific "
                 "counterparty at this stage · only the type."},
            {"name": "valore", "label": "Value bracket", "type": "select", "required": True,
             "options": [
                 "up to € 50,000",
                 "€ 50,000 — € 250,000",
                 "€ 250,000 — € 1 M",
                 "€ 1 M — € 5 M",
                 "above € 5 M",
             ],
             "helper": "The estimated value of the dispute."},
            {"name": "urgenza", "label": "Procedural urgency", "type": "select", "required": True,
             "options": [
                 "ordinary (no deadline expiring)",
                 "qualified (deadline within 30 days)",
                 "procedural (deadline within 7 days)",
             ],
             "helper":
                 "Urgency determines the firm's reply cadence · "
                 "5 working days · 48 hours if procedural."},
            {"name": "giurisdizione", "label": "Jurisdiction", "type": "select", "required": True,
             "options": [
                 "Italy (Italian forum)",
                 "European Union (CJEU · TUE)",
                 "extra-EU (with elements of private international law)",
             ],
             "helper": "Jurisdiction is the first form of respect."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contact",
             "meta": "The person who will sign the power of attorney once the engagement is opened.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Subject of the dispute",
             "meta": "The subject is the file's first text. Five-to-ten lines are enough.",
             "fields": ["oggetto"]},
            {"num": "03", "title": "Procedural framing",
             "meta": "Instance · counterparty · value · urgency · jurisdiction.",
             "fields": ["grado", "controparte", "valore", "urgenza", "giurisdizione"]},
        ],

        "form_submit_label": "Submit the preliminary opinion",
        "form_submit_note":
            "The firm will read the sheet within five working days "
            "· within forty-eight hours if the urgency is "
            "procedural · and will reply with a motivated note to "
            "the address indicated. No external BDR, no sequence "
            "automation — first contact is with the barrister.",
        "form_consent":
            "I consent to the processing of my personal data "
            "pursuant to Reg. UE 679/2016 and D.lgs. 196/2003. "
            "Data are processed for the sole purpose of "
            "evaluating the opinion · kept at the studio on Via "
            "Borgonuovo with access limited to the three "
            "barristers. I am informed of the whistleblowing "
            "channel (D.lgs. 24/2023) active at the studio. "
            "The firm respects professional secrecy under art. "
            "622 c.p. and the Codice Deontologico Forense.",

        "office_address_label": "Address",
        "office_area_label":    "Area",
        "office_phone_label":   "Phone",
        "office_email_label":   "Email",

        "offices_label":   "THE OFFICE",
        "offices": [
            {
                "city":    "Milan",
                "tag":     "Single office · Foro di Milano",
                "address": "Via Borgonuovo 14 · 20121",
                "area":    "Brera · near the Tribunale di Milano",
                "phone":   "+39 02 7634 8210",
                "email":   "parere@causa.legal",
            },
        ],

        "channels_label": "DIRECT CHANNELS",
        "channels": [
            ("Studio reception",                    "+39 02 7634 8210",                "Mon – Fri · 09:00 – 18:00"),
            ("Email for preliminary opinions",      "parere@causa.legal",              "Reply within 5 days"),
            ("PEC for filings already in deadline", "causa.legale@pec.causa.legal",    "Urgent acts · within 24 hours"),
            ("Whistleblowing (D.lgs. 24/2023)",     "whistleblowing@causa.legal",      "Internal channel · encrypted"),
        ],

        "footnote":
            "Causa respects professional secrecy under art. 622 "
            "c.p. and the Codice Deontologico Forense. The "
            "consultation of the website does not constitute "
            "engagement of the firm. The firm does not respond to "
            "anonymous requests and does not issue preliminary "
            "opinions in writing without a completed screening "
            "sheet. Information on fees is illustrated at the "
            "first meeting, according to the minimum forensic "
            "tariffs and the parameters D.M. 55/2014. The "
            "whistleblowing channel is operated under D.lgs. "
            "24/2023 and is open to associates, employees and the "
            "secretariat.",
    },
}
