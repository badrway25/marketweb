"""Continua — Family-office stewardship (corporate-suite archetype) content.

Phase X.4 design-orchestrator first real candidate (pass 1 IT,
2026-04-29). 4th corporate-suite sibling · 1st family-office variant.
The build brief lives at
``design-orchestrator/real-candidates/continua-build-brief.md`` and the
distinctness proof at ``…/continua-distinctness-proof.md`` (5/5 vs
Pragma · 5/5 vs Fiscus · 5/5 vs Solaria on the 4-of-5 axes gate).

Editorial identity: a stewardship-grade family office that custodies a
family's patrimony across generations, governed via a Family Council
(Consiglio di Famiglia), measured in decades rather than market cycles.
Three stewards (NOT solo-practitioner), one principal seat in Milano
(Brera), multi-partner stewardship office. Voice is custodial,
longitudinal, multi-generational — explicitly NOT Pragma's decisional-
gravity, NOT Fiscus's presidio + scadenze-first, NOT Solaria's bounded-
method coaching framing.

Differentiation vs Pragma + Fiscus + Solaria (D-054 10-gate · matrix
§1 row-by-row in the distinctness proof):
 1. Cluster:      family-office multigenerazionale (governance-led)
                  vs Pragma corporate-advisory (boardroom B2B)
                  vs Fiscus commercialista presidio (annual fiscal)
                  vs Solaria executive coaching (bounded percorso)
 2. Voice anchor: "La continuità di una famiglia si misura in
                  <em>generazioni</em>." — italic on a TEMPORAL noun
                  vs Pragma "decisioni che contano" (agency word)
                  vs Fiscus "adempimento corretto" (imperative)
                  vs Solaria "non terapia non consulenza" (contrast pair)
 3. Hero subject: library / partner-study reading room with brass lamp
                  on partner desk — object-led, zero people (cluster's
                  first), single archival object focal
                  vs Pragma boardroom long-table (1-4 people)
                  vs Fiscus tidy desk + multiple documents (object-adj)
                  vs Solaria 1:1 conversation (1-2 people)
 4. Hero meta-strip: "stewardship-horizon-strip" — Mandato medio · 18
                  anni / Generazioni in carico · 3 / Riunioni CdF · 4
                  per anno (cadence, not number/calendar/arc)
                  vs Pragma KPI tuple (numbers)
                  vs Fiscus fiscal-calendar (deadlines)
                  vs Solaria percorso-cadenza (session arc)
 5. Mid-strip:    governance-cycle-strip — three cells (eyebrow ·
                  figure · context-line) on cream paper between the
                  KPI band and sectors ribbon. The differentiator beat
                  · names a RHYTHM not a deadline or a session count
                  · Pragma has none · Fiscus has fiscal-calendar ·
                  Solaria has percorso-cadenza
 6. Palette:      pine `#0F3A30` + pewter `#5A6E78` + brass `#B0875E`
                  · cool/cool/warm (matrix §1.3 the only OPEN warmth
                  combo) · brass is the load-bearing differentiator
                  visible at ≥ 5 viewport touchpoints
                  vs Pragma navy/blue/emerald (cool/cool/cool)
                  vs Fiscus gray-blue/gold/blunotte (cool/warm/cool)
                  vs Solaria warm-carbon/ocra/caramel (warm/warm/warm)
 7. Typography:   Crimson Pro (heading · classical book-jacket ratios,
                  strong italic personality on temporal noun) + Public
                  Sans (body · gov-designed, public-trust signal,
                  explicitly NOT Inter)
                  vs Pragma Merriweather + Inter
                  vs Fiscus IBM Plex Serif + IBM Plex Sans
                  vs Solaria Fraunces + Inter
 8. CTA copy:     "Avvia un dialogo di mandato" — multi-year framing
                  vs Pragma "Fissa una call privata"
                  vs Fiscus "Primo appuntamento"
                  vs Solaria "Prenota una discovery call"
 9. Form gate:    scope familiare + orizzonte temporale (5y/10y/25y/
                  multi-generazionale) + struttura attuale (holding/
                  fondazione/trust/patto/nessuna). The horizon-selector
                  is the differentiating field; no sibling has it.
                  Explicitly NOT Pragma NDA-ready boardroom form ·
                  NOT Fiscus P.IVA + CF · NOT Solaria ICF code-of-
                  ethics-referenced booking
10. Leadership:  3 stewards, photo-present · 60s + 40s + 50s + 2 women
                  + 1 man + 3 visible ethnicities (closes Solaria's
                  30sCx2 demographic gap forward, takes the photo-
                  present precedent forward). NOT Pragma "Partner /
                  Senior Associate / Counsel". NOT Fiscus "ODCEC /
                  Cassazionista". NOT Solaria "ICF-PCC / EMCC".

Hard prohibitions explicitly satisfied (build-brief §2 + distinctness
proof §3):
- ✓ No URL appearing in `business-corporate`/`business-fiscal`/
   `business-coaching` pools (cross-cluster grep clean at A.3 intake)
- ✓ Inter is NOT body sans (Public Sans replaces it · 3rd-use cluster
   collapse risk closed at matrix §1.4)
- ✓ `--primary-2: #2c3e6b` is NOT introduced
- ✓ Hero meta-strip is NOT KPI tuple / fiscal-calendar / percorso-cadenza
- ✓ `--primary` `#0F3A30` L* ≈ 21 — well under the 40 cream-safe ceiling
- ✓ No lorem ipsum / placeholder copy
- ✓ Pexels-only · no Unsplash carve-out (Pragma legacy is the only one)
- ✓ No geometric sans on heading

The IT pass at workflow A does NOT depend on AR resolution — multilingual
lands in workflow C with the verbatim-in-translation voice anchor and
real Arabic RTL via Noto Kufi heading swap. This file is IT-only by
design at draft tier (D-102 cadence).

Page kinds:
- home, about, services, case_study_list, case_study_detail, contact
"""
from __future__ import annotations

from typing import Any


# ─── Pexels-only imagery pool · single source of truth ─────────────────
# Phase X.4b Continua Pass B (multilingual rollout · 2026-04-30) extracts
# the inline image URLs into module-level constants so each locale tree
# (`continua_en/fr/es/ar`) imports the same Pexels frames. The `_POOL_*`
# convention mirrors the Solaria Pass B precedent. Image substitution
# across locales is forbidden — every locale must render the same frames
# the IT walk approved at the LF-5 rebuild.
_HERO_IMAGE = (
    "https://images.pexels.com/photos/36093623/pexels-photo-36093623.jpeg"
    "?auto=compress&cs=tinysrgb&w=1600"
)
_PILLAR_ICON_01 = (
    "https://images.pexels.com/photos/4467737/pexels-photo-4467737.jpeg"
    "?auto=compress&cs=tinysrgb&w=200"
)
_PILLAR_ICON_02 = (
    "https://images.pexels.com/photos/5668887/pexels-photo-5668887.jpeg"
    "?auto=compress&cs=tinysrgb&w=200"
)
_PILLAR_ICON_03 = (
    "https://images.pexels.com/photos/1153213/pexels-photo-1153213.jpeg"
    "?auto=compress&cs=tinysrgb&w=200"
)
_PILLAR_ICON_04 = (
    "https://images.pexels.com/photos/3201588/pexels-photo-3201588.jpeg"
    "?auto=compress&cs=tinysrgb&w=200"
)
_PORTRAIT_ELEONORA = (
    "https://images.pexels.com/photos/5333750/pexels-photo-5333750.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)
_PORTRAIT_TOMAS = (
    "https://images.pexels.com/photos/7841828/pexels-photo-7841828.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)
_PORTRAIT_GINEVRA = (
    "https://images.pexels.com/photos/8424881/pexels-photo-8424881.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)


CONTINUA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Lo studio",      "kind": "home"},
        {"slug": "chi-siamo",     "label": "Chi siamo",      "kind": "about"},
        {"slug": "custodia",      "label": "Custodia",       "kind": "services"},
        {"slug": "mandati",       "label": "Mandati",        "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contatti",       "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer.
    "site": {
        "logo_initial": "C",
        # Continua reads as a single-word wordmark (build-brief §7) ·
        # Latin preserved under RTL · CS-NAV-06.
        "logo_word":    "Continua",
        "tag":          "Family office multigenerazionale · Milano",
        "phone":        "+39 02 7600 4188",
        "email":        "mandato@continua.it",
        "address":      "Via San Marco 22 · 20121 Milano",
        "hours_compact":"Lun – Ven · 9:30 – 18:30 · su appuntamento",
        "hours_footer_rows": [
            "Sabato · solo Consigli di Famiglia programmati",
            "Domenica · chiuso",
        ],
        "license":      "Iscrizione Albo dei Trustees · STEP Affiliate · ANC audit di continuità",
        "footer_intro":
            "Custodi del patrimonio familiare attraverso le generazioni. "
            "Una boutique di stewardship indipendente, mandati di custodia "
            "su orizzonte multigenerazionale, governance familiare presidiata "
            "dal Consiglio di Famiglia. Sede principale a Milano, partnership "
            "fiduciarie a Lugano e Lussemburgo.",
        "foot_studio":   "Lo studio",
        "foot_pages":    "Pagine",
        "foot_contact":  "Contatti",
        "foot_offices":  "Sedi",
        "offices_footer_rows": [
            "Milano · Brera (sede principale)",
            "Lugano · Riva Caccia (corrispondente fiduciario)",
            "Luxembourg · Boulevard Royal (corrispondente trustee)",
        ],
        # Phase X.4b · LF-5 footer column. The whistleblowing channel
        # (D.lgs. 24/2023) is surfaced as a first-class footer column,
        # not buried in the legal row. CS-FOOT-02 legal row at the
        # bottom of `_base.html` continues to carry the privacy /
        # cookie / segnalazioni link — this column adds the channel's
        # institutional identity (custodian + email + policy link).
        "whistleblowing_footer": {
            "heading":      "Segnalazioni",
            "eyebrow":      "Canale interno · D.lgs. 24/2023",
            "note":
                "Canale cifrato gestito dal Compliance Officer. "
                "Riservato a membri della famiglia in mandato e a "
                "stewards Continua. Verbalizzazione fiduciaria.",
            "email":        "whistleblowing@continua.it",
            "policy_label": "Tutela del segnalante",
            "policy_href":  "contatti",
        },
        # Case study cross-page meta labels (rendered on case_study_list +
        # case_study_detail). Continua re-frames Pragma's "Practice / Anno /
        # Durata" toward "Profilo / Generazioni / Anni in mandato" to
        # signal stewardship-duration over engagement-per-quarter.
        "case_practice_label":     "Profilo",
        "case_year_label":         "In mandato dal",
        "case_duration_label":     "Anni in continuità",
        "case_lead_label":         "Steward referente",
        "case_lead_partner_label": "Senior steward",
        "case_team_label":         "Team & cadenza",
        "case_timeline_label":     "Tappe di continuità",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Family office · Milano · stewardship multigenerazionale",
        # Voice anchor verbatim · italic on the temporal noun "generazioni"
        # (build-brief §3 · CS-TYPE-02).
        "headline":
            "La continuità di una famiglia si misura in <em>generazioni</em>.",
        "intro":
            "Custodi del patrimonio familiare attraverso le generazioni. "
            "Una boutique di stewardship indipendente — un Consiglio di "
            "Famiglia, un mandato che non si misura in trimestri, una "
            "vigilanza fiduciaria che attraversa il passaggio fra padri, "
            "figli e nipoti.",
        "primary_cta":   "Avvia un dialogo di mandato",
        "primary_href":  "contatti",
        "secondary_cta": "Lo studio di custodia",
        "secondary_href":"chi-siamo",

        # Right-hand object-led photo (slot 0 · historic library room
        # with rich wooden interiors · partner desk in foreground · NO
        # people · build-brief §4 hard rejection rule on documents > 1 /
        # laptop / human). The slot was re-curated live at A.3
        # (2026-04-29) when the initial candidate returned a Scrabble-
        # tile composition · curator-verified replacement.
        "hero_image":              _HERO_IMAGE,
        # Hero credit overlay (NOT "Direzione, Anno fondazione" — that
        # composition was used twice already by Pragma + Fiscus).
        "hero_image_credit_left":  ("Custodi del mandato", "Iscrizione Albo Trustees"),
        "hero_image_credit_right": ("Sede principale",     "Milano · Brera"),
        # Stewardship-horizon-strip (build-brief §3 · NOT KPI tuple ·
        # NOT fiscal-calendar · NOT percorso-cadenza).
        "hero_meta_strip": [
            ("Mandato medio",          "18 anni"),
            ("Generazioni in carico",  "3"),
            ("Riunioni CdF",           "4 / anno"),
        ],

        # Pillars 4-up (CS-DENSITY-02 within bound · upper-band targeting
        # for the §7.1 word budget · ~95w body each). Legacy 3-tuple
        # shape preserved for backward compatibility with any consumer
        # outside the LF-5 home (services page card scaffold etc.); the
        # LF-5 home reads `pillars_matrix` instead.
        "pillars_label":   "Custodia",
        "pillars_heading": "Quattro presidi, <em>un solo</em> mandato",
        "pillars_intro":
            "Quattro pratiche che lavorano in continuità sullo stesso "
            "patrimonio. Non si paga per ciascun presidio separatamente — "
            "il mandato copre la combinazione di custodia, governance, "
            "successione e compliance per l'orizzonte concordato con la famiglia.",
        "pillars": [
            ("01", "Custodia patrimoniale",
             "Custodiamo il patrimonio familiare nei suoi quattro strati — asset "
             "finanziari liquidi, partecipazioni industriali, immobili strumentali "
             "e di famiglia — attraverso il ciclo delle generazioni, in coerenza "
             "con il patto familiare in vigore e i mandati fiduciari sottostanti."),
            ("02", "Governance familiare",
             "Facilitiamo il Consiglio di Famiglia con cadenza trimestrale, "
             "redigiamo e revisioniamo il patto familiare, disegniamo le "
             "voting structures dei rami e i codici di comportamento condivisi "
             "fra generazioni in carico e generazioni entranti."),
            ("03", "Successione strutturata",
             "Pianifichiamo il passaggio multigenerazionale — donazioni "
             "modulate, holding di famiglia, trust dedicati, formazione "
             "tecnica e di governance per la generazione entrante prima del "
             "trasferimento effettivo della responsabilità decisionale."),
            ("04", "Compliance fiduciaria",
             "Vigilanza fiduciaria continuativa, audit di continuità annuale "
             "indipendente, presidio normativo in evoluzione (D.lgs. 24/2023 "
             "whistleblowing, Codice della Crisi, OAM mediazione creditizia) "
             "e custodia documentale a accesso controllato sui registri di famiglia."),
        ],

        # LF-5 2×2 matrix (CS-LAYOUT-04 = `2x2-with-image`). Each pillar
        # carries a small monochrome icon image rendered at ≤80px with
        # `filter: grayscale(1)` so palette chrome holds. Pexels-only,
        # Albo-style object glyphs (deed seal, gavel-on-ledger, family
        # tree on parchment, compliance binder). Body copy rewritten in
        # tighter blurb cadence (≤44 char/line at desktop) so the icon
        # + title + body cluster reads as one structural unit, not as
        # the legacy numbered-grid pillar.
        "pillars_matrix": [
            {
                "num":   "01",
                "title": "Custodia patrimoniale",
                "body":
                    "Quattro strati custoditi simultaneamente — finanziario "
                    "liquido, partecipazioni industriali, immobili strumentali "
                    "e di famiglia — in coerenza con il patto familiare.",
                # Object-led monochrome icon. Pexels frame curated for
                # archive/seal/document subject — A.3 imagery floor at
                # CS-IMG-SRC-01 (Pexels-only). The grayscale filter at
                # the CSS layer flattens any incidental warm-tone in
                # the source so the matrix reads as four sober marks.
                "icon_image": _PILLAR_ICON_01,
            },
            {
                "num":   "02",
                "title": "Governance familiare",
                "body":
                    "Consiglio di Famiglia trimestrale. Verbalizzazione "
                    "fiduciaria. Patto familiare a revisione triennale. "
                    "Voting structures dedicate per ramo.",
                "icon_image": _PILLAR_ICON_02,
            },
            {
                "num":   "03",
                "title": "Successione strutturata",
                "body":
                    "Holding di famiglia, trust dedicati, donazioni "
                    "modulate. Programma biennale di formazione "
                    "tecnica della generazione entrante.",
                "icon_image": _PILLAR_ICON_03,
            },
            {
                "num":   "04",
                "title": "Compliance fiduciaria",
                "body":
                    "Audit di continuità ANC annuale. Presidio AML, "
                    "Codice della Crisi, D.lgs. 24/2023. Custodia "
                    "documentale a accesso controllato.",
                "icon_image": _PILLAR_ICON_04,
            },
        ],

        # KPI band — the ONE dark band on home (CS-TONE-03). Mix of
        # duration + scope, NOT pure numeric — signals stewardship time-
        # axis, not B2B-advisory chest-thump.
        "kpi_heading": "Diciotto anni di mandati in continuità",
        "kpi_strip": [
            ("18",      "anni · orizzonte medio mandato"),
            ("3",       "generazioni · famiglie in carico"),
            ("€ 1.8 B", "patrimonio in custodia"),
            ("4",       "riunioni CdF · anno"),
        ],

        # Governance-cycle-strip — the differentiator beat (build-brief
        # §6 row 4 · LF-5 promotes it from slot-4 to slot-2 immediately
        # after the hero). 3 cells, cream paper, each a (eyebrow ·
        # figure · context-line) triple — NOT (label · figure). Names a
        # CADENCE, not a number / calendar / session arc. Reframed as
        # "Ciclo di governance" (was "Ritmo di governance") to mark
        # the slot-2 promotion as a governance opening, not a mid-page
        # cadence aside.
        "cycle_label":   "Ciclo di governance",
        "cycle_heading": "La continuità ha una <em>cadenza</em>, non una scadenza.",
        "cycle_intro":
            "Tre ritmi che governano il mandato — non KPI, non scadenze "
            "fiscali, non sessioni di coaching. Sono i battiti regolari "
            "di un Family Council, ripetuti negli anni e attraversati "
            "dalle generazioni.",
        "cycle_strip": [
            ("Cadenza CdF", "4 riunioni / anno",
             "Calendario di governance condiviso con la famiglia · verbalizzazione "
             "fiduciaria · ordine del giorno aperto a entrambe le generazioni in carico."),
            ("Audit di continuità", "annuale",
             "Verifica indipendente sulla coerenza pluriennale del mandato "
             "(ANC) · review della custodia documentale · esito comunicato in "
             "CdF di dicembre."),
            ("Patto familiare", "revisione triennale",
             "Aggiornamento delle regole interne, con o senza la generazione "
             "entrante a tavolo · clausole di voto e di tutela dei rami "
             "ridiscusse ogni tre anni."),
        ],

        # Sectors ribbon — "Profili familiari" (NOT "Settori di intervento")
        # · 8 segments per build-brief §6 row 5.
        "sectors_label": "Profili familiari",
        "sectors": [
            "Famiglie imprenditoriali",
            "Holding di partecipazioni",
            "Fondazioni di famiglia",
            "Gruppi multi-asset",
            "Seconde generazioni in trasferimento",
            "Trustees indipendenti",
            "Ufficio di rappresentanza",
            "Single family office estero",
        ],

        # Trust band — preserved for any non-LF-5 future re-routing,
        # though LF-5's section sequence D drops the trust marquee
        # (sectors band absorbs the function). Keep populated so
        # multilingual locales keep tier-coverage parity.
        "trust_label":   "Riconoscimenti istituzionali",
        "trust_logos":   [
            "ALBO DEI TRUSTEES",
            "STEP AFFILIATE",
            "ANC AUDIT DI CONTINUITÀ",
            "OAM MEDIATORI CREDITIZI",
            "ASSOCIAZIONE BANCHE FIDUCIARIE",
            "FAMILY OFFICE NETWORK ITALIA",
        ],

        # LF-5 sectors-band whistleblowing eyebrow. The home-level
        # whistleblowing flag surfaces D.lgs. 24/2023 visibly on the
        # cream sectors ribbon so the channel reads as first-class
        # custodial chrome, not a buried legal-row line. Channel
        # address itself lives in `site.whistleblowing_footer` and in
        # the contact page channel list.
        "whistleblowing": {
            "eyebrow":      "Tutela del segnalante",
            "channel_name": "Canale interno · D.lgs. 24/2023",
        },

        # Leadership — "Custodi del mandato" · photo-present · 3 stewards
        # spanning 40s · 50s · 60s + 2 women + 1 man + 3 visible
        # ethnicities (build-brief §10). Each card carries ONE real albo
        # credential — NOT a list of 3-4 like Solaria's.
        "leadership_label":   "Custodi del mandato",
        "leadership_heading": "Tre custodi che siederanno al vostro Consiglio di Famiglia.",
        "leadership_intro":
            "Ogni mandato è seguito personalmente da almeno un Senior "
            "Steward, che siede in CdF dall'apertura del fascicolo alla "
            "transizione fra generazioni. Nessuno steward di ricambio, "
            "nessun affiancamento esterno non concordato.",
        "leadership": [
            {
                "name":  "Eleonora Marchesi",
                "role":  "Senior Steward",
                # LF-5 environmental anchor — names where the steward is
                # photographed standing (vault · partner desk · CdF
                # round-table). Shifts the read from "headshot" to
                # "custodian of a room", which is what the family office
                # actually sells. Empty string degrades to typographic.
                "station": "Sala dell'archivio · Brera",
                "bio":
                    "Trentacinque anni di pratica fiduciaria fra Milano e "
                    "Lugano. Iscritta all'Albo dei Trustees dal 2007, ha "
                    "presidiato sette mandati di continuità su tre "
                    "generazioni complete e undici trasferimenti "
                    "intergenerazionali documentati.",
                "credentials": [
                    "Albo dei Trustees · Iscrizione 2007",
                ],
                # Curator-verified at A.3 re-curate (2026-04-29) ·
                # senior woman 60s · institutional · solves Solaria
                # 30sCx2 demographic gap on the senior side.
                "portrait": _PORTRAIT_ELEONORA,
            },
            {
                "name":  "Tomas Okafor",
                "role":  "Family Officer",
                "station": "Tavolo del Consiglio · sede principale",
                "bio":
                    "Quattordici anni di pratica fra family office "
                    "anglosassoni e advisory continentale. STEP Affiliate "
                    "dal 2014, coordina la facilitazione del Consiglio di "
                    "Famiglia e la formazione tecnica della generazione "
                    "entrante prima del trasferimento di responsabilità.",
                "credentials": [
                    "STEP Affiliate · 2014",
                ],
                # Curator-verified at A.3 re-curate (2026-04-29) ·
                # mature businessman 40s · West African heritage ·
                # explicit visible age + gender + ethnicity variation
                # vs Eleonora 60s slot · Mitigation §12 Warning 4.
                "portrait": _PORTRAIT_TOMAS,
            },
            {
                "name":  "Ginevra Conti",
                "role":  "Compliance Officer",
                "station": "Studio del compliance · custodia documentale",
                "bio":
                    "Ventidue anni nella vigilanza fiduciaria dei patrimoni "
                    "privati. OAM iscritta come mediatore creditizio dal "
                    "2011, presidia il rispetto del D.lgs. 24/2023 "
                    "(whistleblowing) e l'audit di continuità annuale di "
                    "ogni mandato in carico.",
                "credentials": [
                    "OAM · Iscrizione mediatori creditizi",
                ],
                # Curator-verified at A.3 re-curate (2026-04-29) ·
                # senior woman in brown blazer holding notebook · 50s ·
                # warm-tone wardrobe contrast vs Eleonora's coral · keeps
                # the 3-card row reading as 3 distinct demographics
                # without re-using a portrait already in the slot 2-3 pair.
                "portrait": _PORTRAIT_GINEVRA,
            },
        ],

        # Cases preview — "Mandati in continuità" · multi-year duration
        # markers · 4 mandates with anonymized profiles (build-brief
        # §6 row 7 + §8 cases shape). LF-5 reads `cases_timeline` (year
        # + title + horizon vertical), not `posts` (numbered list-row).
        "cases_label":   "Mandati in continuità",
        "cases_heading": "Quattro mandati, quattro generazioni, <em>una sola cadenza</em>.",
        "cases_intro":
            "Una selezione di mandati in continuità — non chiusi, ancora "
            "in carico. I nomi delle famiglie sono divulgati solo dietro "
            "patto di riservatezza fiduciaria.",

        # LF-5 timeline (CS-LAYOUT-07 = `timeline`). Year-on-rail +
        # mandate title + horizon column + arrow link to detail. The
        # entries point at the same `posts` table that powers the
        # case-study detail pages — slug parity is mandatory so the
        # timeline rows reach `case_study_detail` exactly like the
        # legacy `posts` iteration did. Keep timeline rows ordered by
        # year of intake (oldest first reads as a custodial timeline).
        "cases_timeline": [
            {
                "slug":          "famiglia-b-fondazione-di-famiglia",
                "year":          "2011",
                "eyebrow":       "Fondazione di famiglia",
                "title":         "Famiglia B · 3ª generazione · ramo filantropico + industriale",
                "horizon_label": "Orizzonte",
                "horizon":       "15 anni in continuità · audit congiunto",
            },
            {
                "slug":          "famiglia-a-quarta-generazione-holding-industriale",
                "year":          "2014",
                "eyebrow":       "Holding industriale",
                "title":         "Famiglia A · 4ª generazione · sei rami familiari",
                "horizon_label": "Orizzonte",
                "horizon":       "12 anni · rinnovo del mandato 2034",
            },
            {
                "slug":          "famiglia-d-single-family-office-estero",
                "year":          "2017",
                "eyebrow":       "Single family office",
                "title":         "Famiglia D · custodia cross-border IT · CH · LU",
                "horizon_label": "Orizzonte",
                "horizon":       "9 anni · estensione AML 2030",
            },
            {
                "slug":          "famiglia-c-trasferimento-intergenerazionale",
                "year":          "2019",
                "eyebrow":       "Trasferimento intergenerazionale",
                "title":         "Famiglia C · 2ª → 3ª generazione · trust dedicati",
                "horizon_label": "Orizzonte",
                "horizon":       "Passaggio decennale · 2026 — 2029",
            },
        ],

        # Final CTA band before footer — restates voice anchor (build-
        # brief §6 row 8). Single filled-brass CTA on dark band.
        "cta_label":     "Un primo dialogo riservato",
        "cta_heading":   "La continuità di una famiglia si misura in <em>generazioni</em>.",
        "cta_intro":
            "Il primo dialogo avviene con un Senior Steward. Discutiamo "
            "il perimetro del mandato, l'orizzonte temporale e l'eventuale "
            "conflitto fiduciario — prima di qualsiasi proposta di "
            "Consiglio di Famiglia. Non vendiamo la prima riunione: la "
            "regaliamo, una sola volta, per famiglia.",
        "cta_primary":   "Avvia un dialogo di mandato",
        "cta_primary_href": "contatti",
        "cta_secondary": "Scarica il dossier istituzionale",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "Lo studio · 2007 — 2026",
        "headline":  "Una boutique di custodia, <em>diciannove</em> anni di mandati in continuità.",
        "intro":
            "Continua nasce a Milano nel 2007 come ufficio di custodia "
            "per due famiglie imprenditoriali lombarde. Da allora abbiamo "
            "presidiato il passaggio fra padri e figli su sette mandati "
            "complessivi, mai per acquisizione, mai con capitale di terzi.",

        # Studio history — 5-step timeline (NOT a wall-of-text · CS-COMP-06).
        "history_label":   "Tappe di continuità",
        "history_heading": "Cinque date, diciannove anni di stewardship.",
        "history_intro":
            "Cinque scelte strutturali dietro le quali si legge il "
            "carattere dello studio — l'indipendenza dal capitale di "
            "terzi, la cadenza trimestrale del CdF, l'audit di continuità "
            "annuale, il patto familiare triennale, il passaggio "
            "intergenerazionale come metodo prima che come prodotto.",
        "history": [
            ("2007", "Fondazione",
             "Eleonora Marchesi e due co-stewards aprono lo studio in via San Marco "
             "a Milano, su mandato di due famiglie imprenditoriali lombarde, "
             "per la custodia patrimoniale su orizzonte ventennale."),
            ("2011", "Iscrizione OAM mediatori creditizi",
             "Ginevra Conti entra come Compliance Officer e attiva la "
             "vigilanza fiduciaria continuativa sui mandati in carico, "
             "secondo il principio della separazione fra custodia e advisory."),
            ("2014", "STEP Affiliate · Family Officer",
             "Tomas Okafor entra come Family Officer e introduce la "
             "facilitazione del Consiglio di Famiglia — quattro riunioni "
             "all'anno, ordine del giorno condiviso, verbalizzazione fiduciaria."),
            ("2019", "Audit di continuità (ANC)",
             "Lo studio adotta il protocollo ANC per l'audit di continuità "
             "annuale — verifica indipendente sulla coerenza pluriennale di "
             "ciascun mandato, esito sempre comunicato in CdF di dicembre."),
            ("2024", "Corrispondenti fiduciari Lugano + Luxembourg",
             "Per accompagnare i mandati di trasferimento intergenerazionale "
             "delle famiglie italiane, attiviamo partnership fiduciarie a "
             "Riva Caccia e a Boulevard Royal — mai sedi proprie, sempre "
             "corrispondenti accreditati."),
        ],

        # Method / values — 4 non-negotiable principles (CS-DENSITY-02).
        "values_label":   "Principi di custodia",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Sono i quattro principi che separano un mandato Continua da "
            "un incarico advisory standard. Sono scritti nel patto di "
            "mandato firmato in CdF, non sul sito.",
        "values": [
            ("01", "Indipendenza dal capitale di terzi",
             "Il capitale dello studio è interamente in mano agli stewards "
             "attivi. Nessun fondo, nessun gruppo bancario, nessun azionista "
             "esterno. La scelta dei mandati non è mai influenzata da agende "
             "di terzi che possano condizionare la custodia."),
            ("02", "Un Senior Steward per ogni mandato",
             "Un Senior Steward siede in CdF dall'apertura del fascicolo al "
             "passaggio della responsabilità. Niente steward-of-record che "
             "spariscono dopo il primo dialogo: il custode incontrato in "
             "prima riunione è lo stesso che firmerà il passaggio "
             "intergenerazionale."),
            ("03", "Audit di continuità indipendente",
             "Ogni mandato è soggetto, una volta all'anno, a un audit di "
             "continuità (ANC) condotto da un revisore esterno allo studio. "
             "L'esito viene comunicato in CdF di dicembre senza filtro: la "
             "famiglia conosce sempre lo stato di custodia del proprio patrimonio."),
            ("04", "Riservatezza fiduciaria",
             "Nessun caso di studio reso pubblico, nessuna newsletter sugli "
             "andamenti dei mandati, nessuna referenza incrociata fra "
             "famiglie. Le anonimizzazioni mostrate nelle pagine pubbliche "
             "sono concordate caso per caso e firmate in CdF."),
        ],

        # Full team — 6 stewards / officers (CS-DENSITY-05).
        "team_label":   "Stewards & officers",
        "team_heading": "Sei custodi, tre sedi, una sola cadenza.",
        "team_intro":
            "Le persone che siederanno in Consiglio di Famiglia. "
            "Stewards, non consulenti, e non vi affidiamo a un "
            "dipartimento — il custode incontrato in prima riunione "
            "è lo stesso che presidierà il passaggio fra le generazioni.",
        "team": [
            {"name": "Eleonora Marchesi",
             "role": "Senior Steward · Custodia",
             "office": "Milano",
             "bio": "Trentacinque anni di pratica fiduciaria. Iscritta "
                    "all'Albo dei Trustees dal 2007 · sette mandati di "
                    "continuità su tre generazioni complete."},
            {"name": "Tomas Okafor",
             "role": "Family Officer · Governance",
             "office": "Milano",
             "bio": "STEP Affiliate dal 2014. Facilitazione del CdF e "
                    "formazione della generazione entrante prima del "
                    "trasferimento di responsabilità."},
            {"name": "Ginevra Conti",
             "role": "Compliance Officer · Vigilanza fiduciaria",
             "office": "Milano",
             "bio": "OAM mediatori creditizi dal 2011. Presidio del D.lgs. "
                    "24/2023 (whistleblowing) e dell'audit di continuità "
                    "annuale per ciascun mandato in carico."},
            {"name": "Lorenzo Pellegrini",
             "role": "Steward · Successione strutturata",
             "office": "Milano",
             "bio": "Diciotto anni nel passaggio generazionale dei "
                    "patrimoni industriali lombardi. Coordina holding di "
                    "famiglia, trust dedicati e formazione tecnica della "
                    "generazione entrante."},
            {"name": "Camille Béranger",
             "role": "Corrispondente fiduciario",
             "office": "Luxembourg",
             "bio": "Vent'anni di pratica nel diritto del trust di "
                    "Luxembourg. Custodisce le strutture cross-border per "
                    "le famiglie italiane con seconde residenze fiscali."},
            {"name": "Sofia Pessina",
             "role": "Junior Steward · Patti familiari",
             "office": "Milano",
             "bio": "Sei anni di pratica nella redazione e revisione dei "
                    "patti familiari. Affianca i Senior Stewards nelle "
                    "riunioni di CdF e nei cicli di revisione triennale."},
        ],

        "coordinates_label": "Le sedi",
        "coordinates": [
            ("Milano",     "Via San Marco 22 · 20121 · Brera"),
            ("Lugano",     "Riva Caccia 1 · 6900 · corrispondente fiduciario"),
            ("Luxembourg", "Boulevard Royal 28 · L-2449 · corrispondente trustee"),
        ],

        # Page-level CTA
        "cta_heading": "Un primo dialogo riservato.",
        "cta_intro":
            "I primi quarantacinque minuti con un Senior Steward sono un "
            "dialogo esplorativo, non una proposta commerciale. Si discute "
            "il perimetro del mandato, l'orizzonte temporale e l'eventuale "
            "conflitto fiduciario — prima di qualsiasi convocazione di Consiglio.",
        "cta_primary":  "Avvia un dialogo di mandato",
        "cta_primary_href": "contatti",
    },

    # ─── CUSTODIA (services · 4 pillars expanded into discrete cards) ──
    "custodia": {
        "eyebrow":  "Custodia · governance · successione · compliance · 2026",
        "headline": "Quattro presidi, <em>una sola firma fiduciaria</em>.",
        "intro":
            "Le quattro pratiche di Continua. Ogni famiglia accede a un "
            "team di stewardship che le presidia tutte simultaneamente — "
            "non si paga per ciascun presidio separatamente, il mandato "
            "copre la combinazione di custodia, governance, successione e "
            "compliance richiesta dall'orizzonte concordato in Consiglio "
            "di Famiglia.",

        # Card meta labels — re-framed for stewardship cadence over
        # advisory engagement. NOT Pragma's "Durata · Lead partner"
        # · NOT Fiscus's "Cassazione · Iscrizione".
        "svc_duration_label": "Cadenza",
        "svc_leader_label":   "Steward referente",

        "services": [
            {
                "num":   "01",
                "title": "Custodia patrimoniale",
                "blurb":
                    "Custodiamo il patrimonio nei suoi quattro strati — finanziario "
                    "liquido, partecipazioni industriali, immobili strumentali, "
                    "immobili di famiglia. La custodia non è gestione di "
                    "portafoglio: è la presa in carico, anno dopo anno, della "
                    "coerenza fra il patrimonio e il patto familiare in vigore.",
                "scope": [
                    "Reportistica trimestrale firmata congiuntamente",
                    "Registro di custodia digitale ad accesso controllato",
                    "Audit di continuità ANC annuale indipendente",
                    "Coordinamento dei corrispondenti fiduciari esteri",
                ],
                "duration": "Trimestrale · audit annuale",
                "leader":   "Eleonora Marchesi",
            },
            {
                "num":   "02",
                "title": "Governance familiare",
                "blurb":
                    "Facilitiamo il Consiglio di Famiglia con cadenza trimestrale, "
                    "verbalizzazione fiduciaria depositata presso lo studio, "
                    "redazione e revisione triennale del patto familiare. La "
                    "governance non è una riunione: è la ripetizione regolare "
                    "di un battito di custodia attraversato dalle generazioni.",
                "scope": [
                    "Quattro Consigli di Famiglia all'anno",
                    "Verbalizzazione fiduciaria depositata",
                    "Voting structures dedicate per ramo familiare",
                    "Codice di comportamento intergenerazionale",
                ],
                "duration": "4 CdF / anno · revisione patto triennale",
                "leader":   "Tomas Okafor",
            },
            {
                "num":   "03",
                "title": "Successione strutturata",
                "blurb":
                    "Pianifichiamo il passaggio intergenerazionale su orizzonte "
                    "decennale — donazioni modulate, holding di famiglia, trust "
                    "dedicati per rami minorenni o non operativi. La successione "
                    "non si improvvisa il giorno della firma del notaio: si "
                    "prepara con un programma biennale di formazione tecnica.",
                "scope": [
                    "Holding di famiglia e patti parasociali",
                    "Trust dedicati per rami minorenni",
                    "Donazioni modulate su orizzonte decennale",
                    "Formazione biennale della generazione entrante",
                ],
                "duration": "Orizzonte decennale · formazione biennale",
                "leader":   "Lorenzo Pellegrini",
            },
            {
                "num":   "04",
                "title": "Compliance fiduciaria",
                "blurb":
                    "Vigilanza fiduciaria continuativa sul rispetto del D.lgs. "
                    "24/2023 (whistleblowing), del Codice della Crisi, della "
                    "normativa OAM mediazione creditizia e delle direttive AML "
                    "applicabili. La compliance non è un ostacolo amministrativo: "
                    "è la garanzia di continuità del mandato fra le generazioni.",
                "scope": [
                    "Canale whistleblowing interno cifrato",
                    "Vigilanza AML rinforzata su movimenti cross-border",
                    "Audit di continuità ANC annuale indipendente",
                    "Custodia documentale a accesso controllato",
                ],
                "duration": "Continuativo · audit ANC annuale",
                "leader":   "Ginevra Conti",
            },
        ],

        # Process strip — how a mandate is run.
        "process_label":   "Come custodiamo",
        "process_heading": "Quattro fasi, una sola sequenza.",
        "process": [
            ("01", "Primo dialogo riservato",
             "Quarantacinque minuti con un Senior Steward. Si discute il "
             "perimetro del mandato e l'orizzonte temporale, mai una "
             "proposta economica."),
            ("02", "Patto di mandato",
             "Entro dieci giorni, un patto di mandato fiduciario di "
             "quattro pagine con perimetro, orizzonte, cadenza dei "
             "Consigli e tariffario fiduciario trasparente."),
            ("03", "Apertura del fascicolo",
             "Insediamento del primo Consiglio di Famiglia. Il Senior "
             "Steward siede in CdF dall'apertura del fascicolo al "
             "passaggio della responsabilità."),
            ("04", "Continuità + audit annuale",
             "Quattro CdF all'anno, audit di continuità ANC indipendente "
             "ogni dicembre, revisione triennale del patto familiare. "
             "Il mandato non si chiude: si rinnova in continuità."),
        ],

        # Final CTA
        "cta_heading":   "Quale presidio fa al caso della vostra famiglia?",
        "cta_intro":
            "Se il perimetro non è chiaro, ci scriva una breve descrizione "
            "del nucleo familiare e dell'orizzonte temporale concordato. "
            "Le indicheremo lo Steward giusto entro 72 ore — anche se non "
            "apriamo mandato.",
        "cta_primary":   "Avvia un dialogo di mandato",
        "cta_primary_href": "contatti",
    },

    # ─── MANDATI (case_study_list) ─────────────────────────────
    "mandati": {
        "eyebrow":  "Mandati in continuità · 2007 — 2026",
        "headline": "Quattro mandati, quattro generazioni, una sola <em>cadenza fiduciaria</em>.",
        "intro":
            "Una selezione dei mandati in carico — non chiusi, ancora in "
            "continuità. I nomi delle famiglie sono divulgati solo dietro "
            "patto di riservatezza fiduciaria. Le tappe mostrate sono "
            "concordate caso per caso e firmate in Consiglio di Famiglia.",

        # Card-list of mandates (full posts in `posts` above).
        "cases_label": "Mandati in carico",
        "cases_intro":
            "Per ogni mandato mostriamo profilo familiare, generazioni in "
            "carico, anni di continuità, scope concordato e cadenza di "
            "audit. Le famiglie sono codificate per ramo (A · B · C · D) "
            "secondo l'ordine cronologico di entrata in mandato.",

        "cta_heading":   "Un mandato simile al vostro?",
        "cta_intro":
            "I dossier completi (perimetro fiduciario, orizzonte, cadenza "
            "del CdF, audit ANC più recente) sono accessibili dietro patto "
            "di riservatezza fiduciaria reciproco. La firma avviene in "
            "primo dialogo, prima di qualsiasi proposta di mandato.",
        "cta_primary":   "Richiedi i dossier integrali",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /mandati/<slug>/
    "posts": [
        {
            "slug":     "famiglia-a-quarta-generazione-holding-industriale",
            "title":    "Famiglia A · 4ª generazione · holding industriale lombarda",
            "category": "Famiglia imprenditoriale",
            "year":     "2014",
            "duration": "12 anni · in continuità",
            "client_code":
                "Holding industriale · 4ª generazione · 6 rami familiari · "
                "patrimonio industriale lombardo · scope: continuità + "
                "governance + audit triennale.",
            "lead":
                "Una holding industriale lombarda alla quarta generazione "
                "di custodia, sei rami familiari, due generazioni "
                "contemporaneamente in carico. Continua presidia il "
                "passaggio fra terza e quarta generazione dal 2014.",
            "sections": [
                {
                    "label": "Il contesto",
                    "heading": "Sei rami, due generazioni, un patrimonio condiviso",
                    "body":
                        "Nel 2014 la holding entrava nella fase di "
                        "passaggio fra la terza generazione (quattro fratelli "
                        "fondatori) e la quarta (dodici cugini, sei rami "
                        "familiari). Il patto familiare in vigore — redatto "
                        "nel 1989 — non prevedeva voting structures per "
                        "la quarta generazione e la terza non aveva ancora "
                        "concordato un calendario di trasferimento. Continua "
                        "è stata chiamata a presidiare la cadenza del "
                        "Consiglio di Famiglia e a impostare il passaggio.",
                },
                {
                    "label": "La custodia",
                    "heading": "Cadenza trimestrale + revisione triennale del patto",
                    "body":
                        "Continua ha impostato il Consiglio di Famiglia a "
                        "cadenza trimestrale dal 2014, con verbale "
                        "fiduciario depositato dopo ogni riunione. Nel "
                        "2017 è stata completata la prima revisione "
                        "triennale del patto familiare, con voting "
                        "structures dedicate ai sei rami della quarta "
                        "generazione e clausola di tutela per i rami non "
                        "operativi. Audit di continuità ANC ogni dicembre.",
                },
                {
                    "label": "Il passaggio",
                    "heading": "Patto familiare 2023 · trasferimento progressivo",
                    "body":
                        "La revisione triennale 2023 del patto familiare "
                        "ha formalizzato il calendario di trasferimento "
                        "progressivo della responsabilità decisionale dalla "
                        "terza alla quarta generazione su orizzonte "
                        "settennale (2024-2031). Il programma biennale di "
                        "formazione tecnica della quarta generazione è "
                        "stato avviato nel 2024. La continuità del mandato "
                        "Continua è stata rinnovata fino al 2034.",
                },
            ],
            "kpi": [
                ("12 anni",   "in continuità · dal 2014"),
                ("4ª",        "generazione in carico"),
                ("6",         "rami familiari · voting structures dedicate"),
                ("2034",      "rinnovo del mandato"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Family Officer + Compliance Officer · CdF trimestrale · audit ANC annuale",
            "next_label":   "Mandato successivo",
        },
        {
            "slug":     "famiglia-b-fondazione-di-famiglia",
            "title":    "Famiglia B · fondazione di famiglia · 3ª generazione",
            "category": "Fondazione di famiglia",
            "year":     "2011",
            "duration": "15 anni · in continuità",
            "client_code":
                "Fondazione di famiglia · 3ª generazione · 4 rami · "
                "patrimonio filantropico + partecipazioni industriali · "
                "scope: governance + compliance + audit triennale.",
            "lead":
                "Una fondazione di famiglia lombarda alla terza generazione, "
                "patrimonio filantropico affiancato da partecipazioni "
                "industriali strumentali. Continua presidia la governance "
                "fondativa e la compliance fiduciaria dal 2011.",
            "sections": [
                {
                    "label": "Il contesto",
                    "heading": "Una fondazione, due nature di patrimonio",
                    "body":
                        "La fondazione, costituita nel 1986, custodisce "
                        "un patrimonio filantropico di € 240 M e "
                        "partecipazioni di controllo in tre realtà "
                        "industriali lombarde. La terza generazione, "
                        "entrata in carico nel 2009, ha richiesto a "
                        "Continua nel 2011 di presidiare la governance "
                        "fondativa e la compliance separata fra il ramo "
                        "filantropico e il ramo industriale.",
                },
                {
                    "label": "La custodia",
                    "heading": "Separazione delle due nature · audit congiunto",
                    "body":
                        "Continua ha impostato due Consigli di Famiglia "
                        "distinti — uno fondativo e uno industriale — "
                        "con riunioni trimestrali concatenate e ordine "
                        "del giorno coordinato dal Family Officer. "
                        "L'audit di continuità ANC è congiunto sui due "
                        "rami una volta all'anno, con esito comunicato "
                        "alla famiglia in CdF di dicembre.",
                },
                {
                    "label": "Il presidio",
                    "heading": "Compliance D.lgs. 24/2023 + AML rinforzata",
                    "body":
                        "Dal 2023 Continua ha esteso il presidio "
                        "fiduciario alla nuova normativa whistleblowing "
                        "(D.lgs. 24/2023) per la fondazione, con canale "
                        "di segnalazione interno dedicato e "
                        "verbalizzazione presso il Compliance Officer. "
                        "AML rinforzata sui movimenti del ramo industriale "
                        "in coerenza con le direttive 2024.",
                },
            ],
            "kpi": [
                ("15 anni",   "in continuità · dal 2011"),
                ("3ª",        "generazione in carico"),
                ("€ 240 M",   "patrimonio filantropico in custodia"),
                ("2",         "Consigli di Famiglia · cadenza trimestrale"),
            ],
            "lead_partner": "Ginevra Conti · Compliance Officer",
            "team":         "Senior Steward + Family Officer + Compliance Officer · 2 CdF trimestrali · audit ANC annuale congiunto",
            "next_label":   "Mandato successivo",
        },
        {
            "slug":     "famiglia-c-trasferimento-intergenerazionale",
            "title":    "Famiglia C · trasferimento intergenerazionale · 2 → 3 generazione",
            "category": "Famiglia in trasferimento",
            "year":     "2019",
            "duration": "7 anni · in trasferimento",
            "client_code":
                "Famiglia imprenditoriale · 2ª → 3ª generazione · 3 rami · "
                "trust dedicati + holding di famiglia · scope: successione "
                "strutturata + formazione della generazione entrante.",
            "lead":
                "Un patrimonio industriale familiare in trasferimento dalla "
                "seconda alla terza generazione, tre rami familiari, "
                "orizzonte di passaggio decennale. Continua coordina la "
                "successione strutturata e la formazione tecnica dei "
                "successori dal 2019.",
            "sections": [
                {
                    "label": "Il contesto",
                    "heading": "Una transizione su orizzonte decennale",
                    "body":
                        "Nel 2019 la seconda generazione (tre fratelli, "
                        "fondatori dell'impresa nel 1978) ha richiesto a "
                        "Continua di impostare il passaggio decennale "
                        "verso la terza generazione (sette successori "
                        "anagrafici, di cui cinque attivi nel business). "
                        "Il primo step è stato la separazione fra holding "
                        "operativa e holding di famiglia, con trust dedicati "
                        "per i due rami minorenni.",
                },
                {
                    "label": "La struttura",
                    "heading": "Holding di famiglia + trust dedicati",
                    "body":
                        "Continua ha presidiato la costituzione della "
                        "holding di famiglia nel 2020 e dei due trust "
                        "dedicati nel 2021. Il programma biennale di "
                        "formazione tecnica dei cinque successori attivi "
                        "è iniziato nel 2022, con sessioni mensili "
                        "facilitate dal Family Officer e una giornata "
                        "annuale di simulazione di Consiglio di Famiglia.",
                },
                {
                    "label": "Il rinnovo",
                    "heading": "Patto familiare 2025 · revisione triennale",
                    "body":
                        "La revisione triennale del patto familiare 2025 "
                        "ha formalizzato la voting structure post-trasferimento, "
                        "il calendario di passaggio della responsabilità "
                        "decisionale (2026-2029) e le clausole di tutela "
                        "dei due rami minorenni. La continuità del mandato "
                        "Continua è stata rinnovata fino al 2032 con "
                        "presidio sul completamento del passaggio.",
                },
            ],
            "kpi": [
                ("7 anni",    "in trasferimento · dal 2019"),
                ("2 → 3",     "generazione in passaggio"),
                ("2",         "trust dedicati · rami minorenni"),
                ("2032",      "rinnovo del mandato"),
            ],
            "lead_partner": "Lorenzo Pellegrini · Steward Successione",
            "team":         "Senior Steward + Family Officer + Steward Successione · CdF trimestrale · formazione mensile + annuale",
            "next_label":   "Mandato successivo",
        },
        {
            "slug":     "famiglia-d-single-family-office-estero",
            "title":    "Famiglia D · single family office estero · custodia cross-border",
            "category": "Single family office estero",
            "year":     "2017",
            "duration": "9 anni · in continuità",
            "client_code":
                "Single family office · 2ª generazione · 1 ramo principale · "
                "patrimonio cross-border IT/CH/LU · scope: custodia + "
                "compliance + corrispondenti fiduciari Lugano + Luxembourg.",
            "lead":
                "Un single family office italiano con patrimonio "
                "cross-border (Italia, Svizzera, Luxembourg). Continua "
                "presidia la custodia patrimoniale e la compliance "
                "fiduciaria coordinando i corrispondenti di Lugano e "
                "Boulevard Royal dal 2017.",
            "sections": [
                {
                    "label": "Il contesto",
                    "heading": "Un patrimonio in tre giurisdizioni",
                    "body":
                        "Nel 2017 la famiglia richiedeva il coordinamento "
                        "fiduciario di un patrimonio distribuito su tre "
                        "giurisdizioni — Italia (immobili strumentali e "
                        "di famiglia), Svizzera (asset finanziari liquidi), "
                        "Luxembourg (trust dedicati per i rami non "
                        "operativi). Continua ha attivato i due "
                        "corrispondenti fiduciari accreditati a Lugano "
                        "(Riva Caccia) e a Boulevard Royal."},
                {
                    "label": "La custodia",
                    "heading": "Reportistica unificata + audit congiunto",
                    "body":
                        "Continua produce una reportistica trimestrale "
                        "unificata sui tre rami giurisdizionali, firmata "
                        "dal Senior Steward + Compliance Officer + "
                        "corrispondenti accreditati. L'audit di continuità "
                        "ANC è congiunto sui tre rami una volta all'anno, "
                        "con esito comunicato in CdF di gennaio (sfasata "
                        "rispetto al ciclo italiano per allineamento "
                        "fiscale cross-border).",
                },
                {
                    "label": "L'evoluzione",
                    "heading": "Direttive AML 2024 · presidio rinforzato",
                    "body":
                        "Dal 2024 Continua coordina il presidio AML "
                        "rinforzato secondo le direttive europee 2024, "
                        "con verifica trimestrale dei movimenti cross-border "
                        "e doppia firma fiduciaria per le operazioni > € 500K. "
                        "Il mandato è stato esteso al 2030 con scope "
                        "coordinato sui tre corrispondenti.",
                },
            ],
            "kpi": [
                ("9 anni",   "in continuità · dal 2017"),
                ("3",        "giurisdizioni · IT · CH · LU"),
                ("trimestrale","reportistica unificata"),
                ("2030",     "rinnovo del mandato"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Compliance Officer + 2 corrispondenti accreditati · audit ANC annuale congiunto",
            "next_label":   "Mandato successivo",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Primo dialogo riservato",
        "headline": "Quarantacinque minuti, agenda <em>familiare</em>, nessun impegno.",
        "intro":
            "Il primo dialogo avviene con un Senior Steward. Discutiamo "
            "il perimetro del mandato, l'orizzonte temporale e l'eventuale "
            "conflitto fiduciario — prima di qualsiasi convocazione di "
            "Consiglio. Le informazioni sensibili sono custodite in "
            "archivio cifrato a accesso limitato agli stewards.",

        "form_label":   "Avvia un dialogo di mandato",
        "form_heading": "Compila il modulo riservato",
        "form_intro":
            "Riceverà conferma da un Senior Steward entro 72 ore "
            "lavorative dall'invio. I dati sono trattati ai sensi del "
            "Reg. UE 679/2016 e custoditi in archivio cifrato presso lo "
            "studio di via San Marco. Nessun BDR esterno, nessuna "
            "automazione di sequence — il dialogo si apre con uno steward, "
            "sempre.",

        # Form fields — scope familiare + orizzonte temporale + struttura
        # attuale (build-brief §9 · the horizon-selector is the differentiating
        # field). NO P.IVA + CF (Fiscus collision avoided).
        "form_fields": [
            {"name": "name",      "label": "Nome",     "type": "text", "required": True,
             "placeholder": "Es. Eleonora",
             "helper": "Solo il nome di battesimo, grazie."},
            {"name": "surname",   "label": "Cognome",  "type": "text", "required": True,
             "placeholder": "Es. Marchesi",
             "helper": "Come compare nel patto familiare in vigore (se presente)."},
            {"name": "family",    "label": "Nucleo familiare", "type": "text", "required": True,
             "placeholder": "Es. Famiglia Marchesi · ramo lombardo",
             "helper": "Il nome con cui ci si presenta in Consiglio di Famiglia."},
            {"name": "role",      "label": "Ruolo nella famiglia", "type": "text", "required": True,
             "placeholder": "Es. Capofamiglia · Successore designato · Membro CdF",
             "helper": "La posizione nel passaggio fra generazioni in carico."},
            {"name": "email",     "label": "Email riservata", "type": "email", "required": True,
             "placeholder": "eleonora@famigliamarchesi.it",
             "helper": "Una casella che riceve solo comunicazioni fiduciarie. Non utilizzeremo domini consumer per il primo contatto."},
            {"name": "phone",     "label": "Telefono diretto", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Linea diretta del referente, non centralino di azienda."},
            {"name": "horizon",   "label": "Orizzonte temporale",  "type": "select", "required": True,
             "options": [
                 "5 anni",
                 "10 anni",
                 "25 anni",
                 "Multi-generazionale (orizzonte oltre 25 anni)",
             ],
             "helper": "L'orizzonte concordato in famiglia per il mandato di custodia. Aiuta a calendare il Senior Steward giusto."},
            {"name": "structure", "label": "Struttura attuale",    "type": "select", "required": True,
             "options": [
                 "Holding di famiglia",
                 "Fondazione di famiglia",
                 "Trust dedicato (italiano o estero)",
                 "Patto di famiglia in vigore",
                 "Nessuna formalizzazione",
             ],
             "helper": "La struttura giuridica esistente (anche se non ancora formalizzata)."},
            {"name": "scope",     "label": "Scope familiare", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Massimo 800 caratteri. Ci dica brevemente la struttura attuale e la sua preoccupazione di continuità — sarà custodito in archivio cifrato fin da questo modulo.",
             "helper": "Quanto basta a capire se il mandato è di nostra competenza. I nomi degli altri rami e le cifre si condividono solo dopo patto di riservatezza fiduciaria reciproco."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che firmerà l'eventuale patto di riservatezza fiduciaria reciproco prima del primo Consiglio.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Famiglia",
             "meta": "Per il conflict-check fiduciario preliminare.",
             "fields": ["family", "role"]},
            {"num": "03", "title": "Mandato di custodia",
             "meta": "L'orizzonte e la struttura — il dettaglio del patrimonio si discute solo in dialogo, mai per iscritto in fase di primo contatto.",
             "fields": ["horizon", "structure", "scope"]},
            {"num": "04", "title": "Allegati (facoltativi)",
             "meta": "Patto familiare in vigore, statuto della fondazione, atto istitutivo del trust o dossier successorio: anticipano la prima riunione e abbreviano il dialogo.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "dossier_familiare",
            "label":    "Documenti preliminari",
            "helper":   "Patto familiare in vigore, statuto della fondazione, "
                        "atto istitutivo del trust o dossier successorio. "
                        "PDF / DOCX · max 20 MB complessivi. Archivio cifrato "
                        "con accesso limitato agli stewards Continua.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Trascina qui i documenti o",
            "link":     "sfoglia dall'archivio",
            "meta":     "PDF / DOCX · max 20 MB · archivio cifrato fiduciario",
        },

        "form_submit_label": "Avvia un dialogo di mandato",
        "form_submit_note":
            "Conferma da un Senior Steward entro 72 ore lavorative. "
            "Nessun BDR esterno, nessuna automazione di sequence — il "
            "dialogo si apre con uno steward, sempre.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016 e del D.lgs. 196/2003 come modificato. "
            "I dati sono custoditi in archivio cifrato presso lo studio di "
            "via San Marco con accesso limitato agli stewards Continua. "
            "Nessun dato viene comunicato a terzi senza esplicita "
            "autorizzazione fiduciaria. Sono informato del canale "
            "whistleblowing (D.lgs. 24/2023) attivo presso lo studio.",

        "office_address_label": "Indirizzo",
        "office_area_label":    "Zona",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",

        # Sidebar — sedi + canali diretti.
        "offices_label":   "Le sedi",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Sede principale",
                "address": "Via San Marco 22 · 20121",
                "area":    "Brera · vicino Piazza San Marco",
                "phone":   "+39 02 7600 4188",
                "email":   "milano@continua.it",
            },
            {
                "city":    "Lugano",
                "tag":     "Corrispondente fiduciario",
                "address": "Riva Caccia 1 · 6900",
                "area":    "Centro · vicino Piazza della Riforma",
                "phone":   "+41 91 922 7700",
                "email":   "lugano@continua.it",
            },
            {
                "city":    "Luxembourg",
                "tag":     "Corrispondente trustee",
                "address": "Boulevard Royal 28 · L-2449",
                "area":    "Ville Haute · vicino Place d'Armes",
                "phone":   "+352 24 87 5500",
                "email":   "luxembourg@continua.it",
            },
        ],

        "channels_label": "Canali diretti",
        "channels": [
            ("Segreteria di custodia", "+39 02 7600 4188",            "Lun – Ven · 9:30 – 18:30"),
            ("Email fiduciaria",       "mandato@continua.it",         "Risposta entro 72 ore"),
            ("Whistleblowing (D.lgs. 24/2023)", "whistleblowing@continua.it", "Canale interno cifrato · verbalizzato dal Compliance Officer"),
        ],

        "footnote":
            "Continua non risponde a richieste anonime e non rilascia "
            "pareri preliminari per iscritto senza un primo dialogo con un "
            "Senior Steward. Le informazioni amministrative (compensi "
            "indicativi, modalità di fatturazione, criteri di accettazione "
            "del mandato) sono illustrate in primo dialogo, mai per iscritto. "
            "Il canale whistleblowing è gestito dal Compliance Officer ai "
            "sensi del D.lgs. 24/2023 ed è accessibile anche ai soli membri "
            "della famiglia in mandato.",
    },
}
