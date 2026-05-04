"""Causa — Studio legale (corporate-suite archetype) content.

Phase X.6 · A.5 build · IT-only · tier=draft (D-102 cadence). 6th
corporate-suite sibling · 1st evidence-led litigation-boutique variant ·
2nd LF-2 (Editorial Spread) occupant after Cornice. The intake/planner/
imagery/copy briefs live at:

    factory/reports/causa/causa-planner-brief.md
    factory/reports/causa/causa-imagery-pack.md
    factory/reports/imagery/causa-legale/pool-selection.md
    factory/reports/copy/causa-legale/copy-authoring.md

Editorial identity: a single-principal Cassazionista litigation boutique
in Milano whose proof IS its public-record sentences. Each cause carried
to court is an evidence incardinated in the official record, never a
decoratively defended opinion. Voice positioning is forensic-publication ·
evidence-led · public-record register, explicitly NOT decisional-gravity
(Pragma) · NOT presidio-with-scadenze (Fiscus) · NOT bounded-method
(Solaria) · NOT stewardship-longitudinal (Continua) · NOT curatorial-
thesis (Cornice).

Forbidden similarities (planner-brief §3 + copy-authoring §3 — the load-
bearing anti-collision contract Causa shares with the LF-2 family):
- vs Cornice (LF-2 first occupant · highest collision risk):
    no `argomento` voice anchor · no Cormorant Garamond · no Source
    Sans 3 · no graphite + pietra-serena + rust palette · no Bologna
    golden-hour portico hero · no Marta Roveri founder · no STUDIO DI
    ARCHITETTURA descriptor · no fascicolo-progetto CTA · no
    architectural-press vocabulary (`argomenta · monografia · saggio ·
    concorso · restauro · MIBAC · OAPPC · DAStU`).
- vs Pragma:   no boardroom long-table · no Fissa una call CTA · no
               navy + emerald palette · no 4-partner card-grid.
- vs Fiscus:   no fiscal-calendar · no P.IVA gate · no Iscritto Sezione
               A · Revisore Legale credential vocabulary.
- vs Solaria:  no terapia/consulenza two-em pair · no discovery-call
               CTA · no Inter body sans (CS-LAYOUT-20 third-use ban).
- vs Continua: no `generazioni` voice anchor · no library reading-room
               mahogany hero · no pine + brass palette · no Avvia un
               dialogo di mandato CTA · no 4-pillar 2x2 governance.

LF-2 family signatures inherited verbatim (per Cornice's first-occupant
binding · planner-brief §2.4):
- Cream-paper navbar (`cs-nav--lf2`) · split-line masthead · filled
  trailing CTA pill · 5-link inline · NO phone-right.
- Zero dark bands on home (CS-TONE-03 demoted at LF-2 family level).
- LF-2-scoped Naskh AR h1 swap (`html[dir="rtl"] body.cs-lf-lf-2`) —
  Causa inherits the selector verbatim · workflow C only · IT-only at
  this build.
- Stacked-editorial hero (full-bleed photo TOP · 8/4 below-fold split).
- KPI tuple inside hero photo's bottom-left credit-overlay frame
  (L5=hero-overlay · NOT a separate dark band).
- Narrative essay with drop-cap on para 1 + 3 pull-quotes interspersed
  + sticky 4-link side-rail (L4=essay-with-anchors).
- 12-cell sectors-ribbon (italic middot-separated · NO photos).
- Single-portrait masthead (L6=single-portrait-feature · 1 portrait
  · 224w bio · 4 credentials).
- 3+1 magazine-grid cases (L7=magazine-grid · 1 hero card + 3 small).
- Cream-hairline CTA closer (NOT dark · LF-2 polarity inversion).
- 4-col footer with whistleblowing column (L9=4-col-with-whistleblowing).

Polarity strategy — full cool · matte-on-matte · zero metallic. The
third polarity dimension per `corporate-suite-distinctness-matrix.md
§1.3`: bottle-green primary + bone secondary + obsidian accent. NOT
graphite + pietra-serena + rust (Cornice). NOT pine + pewter + brass
(Continua). NOT navy + emerald (Pragma). The accent surface deployment
is body-typographic-only (drop-cap · pull-quote em · CTA fill · focus
ring) — explicitly NOT chrome-metallic (Continua's brass deployment
class).
"""
from __future__ import annotations

from typing import Any


# ─── Imagery placeholder · A.6 review-lock mitigation ─────────────────
# At A.6 IT review-lock the 10 Pexels URLs from the A.3 imagery pack
# were verified live in the browser sandbox and ALL resolved to wrong
# subjects (group portraits of casual youths, a bowl of food, a half-
# nude male model, a residential bay-window living-room, etc. — see
# `factory/reports/causa/causa-a6-it-review-lock.md §3 F1`). The 4
# slot-0 backups documented in `business-litigation.md §slot-0-hero
# -backups` were also live-checked: backup 11 = palm tree · backup 12
# = 404 · backup 13 = night cityscape · backup 14 (pre-cleared codex-
# spread fallback) = 3-person warm-mahogany consultation. The entire
# pack appears curator-hallucinated.
#
# Conservative narrow A.6 mitigation: substitute every photographic
# surface (hero · feature · 2 portraits · detail · ambient · 4 case-
# card photos) with a single inline SVG data URL that renders the
# locked palette (bottle-green #14342B + bone #F0EBE0 + obsidian
# #0B0A0E) as a gradient placeholder. The layout shape, typography,
# copy, KPI tuple, voice anchor, navbar pill, and footer chrome all
# remain reviewable; only the photographic content is HELD pending an
# A.5b imagery re-curate (real Pexels search-and-verify pass).
#
# This mitigation touches CONTENT only (this file). It does NOT touch:
#   apps/catalog/preview_imagery.py (the business-legale pool stays at
#       the curator URLs · those URLs only feed the marketplace
#       preview-tile composition · Causa is tier=draft so the catalog
#       does not surface them publicly · A.5b will re-curate)
#   apps/catalog/template_dna.py (the imagery_key indirection stays)
#   apps/catalog/template_content.py (registry stays)
#   any chrome / LF-2 family / sibling content
#
# The placeholder is bottle-green primary on bone secondary with a
# faint obsidian rule at the bottom — visually unmistakable as an
# imagery hold (NOT a real photo) so the user reviewing the IT draft
# cannot mistake it for shipped content.
# Base64-encoded so the SVG body contains zero <, >, ', or " characters
# at the Django template-render layer (avoids HTML auto-escape mangling
# the SVG markup when the data URL appears in CSS background-image).
_IMAGERY_HOLD_PLACEHOLDER = (
    "data:image/svg+xml;base64,"
    "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAx"
    "NjAwIDkwMCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgc2xpY2UiPjxkZWZzPjxs"
    "aW5lYXJHcmFkaWVudCBpZD0iZyIgeDE9IjAiIHkxPSIwIiB4Mj0iMSIgeTI9IjEiPjxzdG9w"
    "IG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMxNDM0MkIiLz48c3RvcCBvZmZzZXQ9IjU1JSIg"
    "c3RvcC1jb2xvcj0iIzFhM2UzNCIvPjxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0i"
    "IzBCMUExNCIvPjwvbGluZWFyR3JhZGllbnQ+PC9kZWZzPjxyZWN0IHdpZHRoPSIxNjAwIiBo"
    "ZWlnaHQ9IjkwMCIgZmlsbD0idXJsKCNnKSIvPjxyZWN0IHg9IjAiIHk9Ijg3MCIgd2lkdGg9"
    "IjE2MDAiIGhlaWdodD0iMzAiIGZpbGw9IiMwQjBBMEUiIG9wYWNpdHk9IjAuNCIvPjx0ZXh0"
    "IHg9IjgwMCIgeT0iNDU1IiBmb250LWZhbWlseT0iR2VvcmdpYSxzZXJpZiIgZm9udC1zaXpl"
    "PSIyOCIgZm9udC1zdHlsZT0iaXRhbGljIiBmaWxsPSIjRjBFQkUwIiBvcGFjaXR5PSIwLjU1"
    "IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5pbWFnZXJ5IGhvbGQgJiMxODM7IEEuNWIgcmUtY3Vy"
    "YXRlIHBlbmRpbmc8L3RleHQ+PC9zdmc+"
)
_HERO_COURTROOM_INTERIOR = _IMAGERY_HOLD_PLACEHOLDER
_FEATURE_OPEN_CODEX = _IMAGERY_HOLD_PLACEHOLDER
_PORTRAIT_FOUNDER = _IMAGERY_HOLD_PLACEHOLDER
_PORTRAIT_ASSOCIATA = _IMAGERY_HOLD_PLACEHOLDER
_DETAIL_CODEX_PAGE = _IMAGERY_HOLD_PLACEHOLDER
_AMBIENT_CODEX_SHELVES = _IMAGERY_HOLD_PLACEHOLDER

# Magazine-grid extras (LF-2 L7=magazine-grid · 3+1 layout) — also
# under A.6 imagery hold per F1 finding above.
_CASE_HIGHCOURT_EXTERIOR = _IMAGERY_HOLD_PLACEHOLDER
_CASE_FASCICOLI_STACK = _IMAGERY_HOLD_PLACEHOLDER
_CASE_BENCH_CHAIR = _IMAGERY_HOLD_PLACEHOLDER
_CASE_CODEX_SPINE = _IMAGERY_HOLD_PLACEHOLDER


CAUSA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        # Causa's 5-link nav reads (in render order):
        # `Studio · Materie · Pubblicazioni · Contenzioso · Contatti`.
        # Per copy-authoring §5.2 the 5 labels MUST share zero tokens
        # with Cornice's `Lo studio · Archivio · Servizi · Progetti ·
        # Contatti` (planner-brief §13.10 hard ban). Mapping:
        #
        #   home          → "Studio"          (manifesto · evidence-led
        #                                       overview · the firm's
        #                                       voice anchor in 5 sections)
        #   materie       → "Materie"         (12 areas of contenzioso)
        #   studio        → "Pubblicazioni"   (about · CV + bio + 14 voci
        #                                       in massimario interno + sede)
        #   contenzioso   → "Contenzioso"     (4 public-record sentences
        #                                       in chronological-inverse
        #                                       cronologia 1995-2024)
        #   contatti      → "Contatti"        (parere preliminare · 7
        #                                       forensic intake fields)
        #
        # Pubblicazioni rolls into the Studio (about) page rather than
        # shipping as a separate page (planner-brief §11 budget +
        # copy-authoring §5.2 fallback path) — keeps the page cohort at 5
        # and the route count identical to Cornice's 5-page LF-2 shape.
        {"slug": "home",        "label": "Studio",        "kind": "home"},
        {"slug": "materie",     "label": "Materie",       "kind": "services"},
        {"slug": "studio",      "label": "Pubblicazioni", "kind": "about"},
        {"slug": "contenzioso", "label": "Contenzioso",   "kind": "case_study_list"},
        {"slug": "contatti",    "label": "Contatti",      "kind": "contact"},
    ],

    # ─── Site-wide chrome (used by _base.html nav + footer) ─────
    "site": {
        "logo_initial": "C",
        # Causa reads as a split-line forensic-publication masthead under
        # LF-2 (line 1 = wordmark · line 2 = subtitle). Forbidden vs
        # Cornice's `studio di architettura` per planner-brief §13.11
        # hard ban — the descriptor must read forensic-publication, not
        # architectural-press.
        "logo_word":      "CAUSA",
        "logo_subtitle":  "studio legale",
        "tag":            "Studio legale · Milano · dal 1995",
        "phone":          "+39 02 7634 8210",
        "email":          "parere@causa.legal",
        "address":        "via Borgonuovo 14 · 20121 Milano",
        "hours_compact":  "Lun – Ven · 09:00 – 18:00 · su appuntamento",
        "hours_footer_rows": [
            "Sabato · solo per termini in scadenza",
            "Domenica · chiuso · risposta entro lunedì",
        ],
        "license":
            "Albo Avvocati Milano · Cassazionista dal 2003 · "
            "ENCA mediatori · Albo CTU forense Tribunale di Milano",
        "footer_intro":
            "Studio legale di patrocinio editoriale. Cassazionista "
            "fondatore Lorenzo Marchetti · iscritto Albo Avvocati di "
            "Milano dal 1995. Sede di Milano · Foro di Milano. "
            "Patrocinio in tutti i gradi di giudizio fino alla "
            "Cassazione · ventotto sentenze citate · quattordici voci "
            "in massimario interno · trentuno anni di patrocinio.",
        "foot_studio":   "Studio",
        "foot_pages":    "Pagine",
        "foot_contact":  "Contatti",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milano · via Borgonuovo 14 · sede unica",
            "Ricevimento su appuntamento · lunedì-venerdì",
            "Foro di Milano · pratiche con cancelleria interne",
        ],
        # LF-2 footer L9 = 4-col-with-whistleblowing. Forensic-firm-
        # specific column content per AC-12 (planner-brief §13.18 hard
        # ban on copy-pasting Cornice's architecture-firm whistleblowing
        # content). Responsabile is an associato senior, NOT the
        # founder, per Codice Deontologico Forense + D.lgs. 24/2023
        # independence requirement.
        "whistleblowing_footer": {
            "heading":      "Segnalazioni",
            "eyebrow":      "Canale interno · D.lgs. 24/2023",
            "note":
                "Lo studio ha istituito un canale di segnalazione "
                "interno conforme al D.lgs. 24/2023 (direttiva UE "
                "2019/1937). Responsabile della prevenzione: avvocato "
                "associato senior, indipendente dal fondatore. "
                "Riservatezza garantita ai sensi della normativa "
                "vigente. Aperto a collaboratori, associati e "
                "segreteria.",
            "email":        "whistleblowing@causa.legal",
            "policy_label": "Modello di gestione delle segnalazioni",
            "policy_href":  "contatti",
        },
        # Case-detail cross-page meta labels. Causa re-frames Cornice's
        # editorial-architectural vocabulary ("Tipologia / Anno fascicolo
        # / Stato di cantiere") into forensic-publication vocabulary
        # ("Materia / Grado / Anno · deposito / Patrocinio").
        "case_practice_label":     "Materia",
        "case_year_label":         "Anno · deposito",
        "case_duration_label":     "Grado · esito",
        "case_lead_label":         "Patrocinio",
        "case_lead_partner_label": "Patrocinio",
        "case_team_label":         "Redazione studio",
        "case_timeline_label":     "Cronologia processuale",
    },

    # ─── HOME (LF-2 sequence B) ─────────────────────────────────
    # Render order (lf2/content.html):
    #   1. cs-hero (LF-2 stacked-editorial · photo TOP + 8/4 split BELOW
    #      with KPI in hero credit overlay · L5=hero-overlay)
    #   2. cs-narrative (LF-2 L4=essay-with-anchors · drop-cap + 3
    #      pull-quotes + side-rail · forensic-publication essay)
    #   3. cs-sectors (sentence-ribbon · 12 materie del contenzioso)
    #   4. cs-leadership-single (LF-2 L6=single-portrait-feature ·
    #      Lorenzo Marchetti · senior Cassazionista in chambers)
    #   5. cs-cases-magazine (LF-2 L7=magazine-grid · 3+1 · 4 public-
    #      record sentences in chronological-inverse order)
    #   6. cs-cta-closer (cream hairline-bordered · NOT dark · LF-2
    #      polarity · voice anchor verbatim recurrence on h2)
    "home": {
        "eyebrow":     "STUDIO LEGALE · MILANO · DAL 1995",
        # Voice anchor verbatim · italic on the forensic-publication
        # noun `evidenza` (copy-authoring §1 + §6.1 · CS-TYPE-02 single
        # em). Surface 1/2 of the LF-2 voice anchor recurrence rule
        # (AC-15) — second surface lands at cs-cta-closer h2 below.
        "headline":
            "Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.",
        "intro":
            "Studio legale di patrocinio editoriale · Cassazionista "
            "fondatore · ventotto sentenze citate dal 1995.",
        "primary_cta":   "Apri un parere preliminare",
        "primary_href":  "contatti",
        "secondary_cta": "Studio · sede di Milano",
        "secondary_href":"studio",

        # LF-2 stacked-editorial hero — full-bleed empty courtroom
        # photo TOP with credit overlay carrying 3-stat KPI tuple
        # (L5=hero-overlay · CS-TONE-03 demoted at family level; KPI
        # lives in the photo's overlay, NOT on a separate dark band).
        # Hero subject is empty courtroom interior (cool light · vertical
        # timber + bone walls · zero people) per planner-brief §4
        # binding-triple. NOT Bologna golden-hour portico (Cornice). NOT
        # library reading-room (Continua). NOT boardroom (Pragma).
        "hero_image":              _HERO_COURTROOM_INTERIOR,
        "hero_image_alt":
            "Aula di tribunale vuota · luce fredda · pareti in legno "
            "verticale e tinte bone · interno architettonico",
        "hero_image_credit_left":  ("Aula di tribunale · interno · 2024", "Foro di Milano"),
        "hero_image_credit_right": ("Sede dello studio", "Milano · via Borgonuovo 14"),
        # 3-stat KPI tuple inside the hero credit overlay (LF-2 L5).
        # Forensic-publication register: sentenze citate + voci in
        # massimario + anni di patrocinio. Anti-collision per copy-
        # authoring §5.5 — NOT (HQ · Equipe · Mandati) Pragma · NOT
        # (novanta fascicoli · 2008 · 38 menzioni) Cornice · NOT
        # (mese · scadenza · ambito) Fiscus · NOT (presidio · figura
        # · orizzonte) Continua.
        "hero_meta_strip": [
            ("Sentenze citate",        "28"),
            ("Voci in massimario",     "14"),
            ("Anni di patrocinio",     "31"),
        ],
        # Side-quote in the right-4-col under the hero photo (LF-2 8/4
        # split BELOW). Em on the verb form `incardina` (verb-form
        # derived from anchor noun · CS-TYPE-02 single em · copy-
        # authoring §6.1).
        "hero_side_quote":
            "Patrocinio davanti alla Corte di Cassazione e nei "
            "gradi di merito. Lo studio sostiene ciò che "
            "<em>incardina</em> nel fascicolo processuale: la "
            "prova depositata, la massima citabile, la materia "
            "del diritto.",

        # Narrative essay (L4=essay-with-anchors · 4 paragraphs · drop-
        # cap on para 1 in obsidian-tinted GT Sectra 84px on bone · 3
        # pull-quotes interspersed · side-rail of 4 anchor links).
        # Replaces cs-pillars (LF-2 has no pillars). The drop-cap is
        # the LF-2 family typographic signature; for Causa it's
        # OBSIDIAN-tinted on bone (matte-on-matte · zero warm-display
        # · planner-brief §10 + §13.5 hard ban on Cornice's rust).
        "narrative_label":   "LO STUDIO · METODO PROBATORIO",
        "narrative_drop":    "L",
        # Pre-interleaved narrative blocks · paragraphs and pull-quotes
        # in render order (4 paragraphs · 3 quotes between them).
        # CS-TYPE-02 single italic em respected per heading-level
        # surface (each pull-quote is its own surface; em on the
        # forensic-publication load-bearing word). Verb-family is
        # `incardinare · sostenere · patrocinare · depositare ·
        # invocare · proporre` per copy-authoring §4.5 — explicitly
        # NOT `argomentare · costruire l'argomento` (Cornice's family).
        "narrative_blocks": [
            ("drop",
             "a giurisprudenza buona si incardina. Causa è uno studio "
             "legale di patrocinio editoriale: ogni causa portata in "
             "udienza è una prova incardinata sull'oggetto del "
             "contenzioso, sul grado di giudizio, sulla giurisdizione. "
             "Non firmiamo opinioni decorative — depositiamo memorie, "
             "ciascuna con la propria documentazione e la propria "
             "massima citabile. Lo studio esiste per misurare il "
             "fascicolo prima di patrocinarlo, per scrivere la massima "
             "prima di sostenerla, per riconoscere ciò che è già stato "
             "deciso prima di proporre ciò che ancora va deciso. È un "
             "mestiere lento, che apre poche cause all'anno, ma le "
             "porta fino in Cassazione."),

            ("quote",
             "La <em>giurisdizione</em> è la prima forma di rispetto. "
             "Ciò che si sostiene davanti al foro corretto sarà sempre "
             "più solido di ciò che si decanta nel grado sbagliato."),

            ("para",
             "Ogni causa passa attraverso quattro stagioni. La "
             "giurisdizione, prima di tutto: la materia che già esiste "
             "viene letta come un fascicolo, con i suoi precedenti, i "
             "suoi gradi, le sue eccezioni preliminari. Il merito, "
             "poi: l'oggetto del contenzioso, le parti in causa, la "
             "fascia di valore, l'urgenza procedurale, l'evidenza "
             "preliminare allegabile. La massima, infine: il ricorso "
             "si scrive come una tesi citabile — quale principio "
             "invoca, quale orientamento conferma, quale evidenza "
             "deposita. Solo allora apriamo il giudizio, e lo seguiamo "
             "udienza per udienza, grado per grado, fino al deposito "
             "della decisione. Le memorie restano scritte: pubblichiamo "
             "le sentenze ottenute nel massimario interno dello studio, "
             "perché un patrocinio senza memoria non lascia massima."),

            ("quote",
             "Una <em>massima</em> non è chi vince più cause, ma chi "
             "sa dire quale ricorso non ha depositato — e perché."),

            ("para",
             "Patrociniamo per imprese e privati che cercano un "
             "avvocato — non un esecutore di standard, non un "
             "assistente in pacchetto. Aziende con contenzioso "
             "bancario complesso, professionisti con responsabilità "
             "professionale contestata, contribuenti con avvisi di "
             "accertamento aggressivi, enti privati con contenzioso "
             "amministrativo regolatorio, parti civili in giudizi "
             "penali tributari. La nostra firma è quella di un "
             "Cassazionista solo, non di una società tra avvocati a "
             "più mani: la responsabilità tecnica resta concentrata, "
             "perché un'evidenza per essere sostenuta deve avere una "
             "voce. Le collaborazioni con consulenti tecnici, periti "
             "contabili, fiscalisti specializzati e consiglieri di "
             "parte passano attraverso lo studio, non lo sostituiscono. "
             "Patrociniamo poco, e fino in fondo."),

            ("quote",
             "Pubblicare una massima non significa pubblicizzarla. "
             "Significa lasciare evidenza <em>sostenuta</em> — perché "
             "chi verrà dopo possa contestarla, distinguerla, o "
             "riconoscerla."),

            ("para",
             "Le sentenze che pubblichiamo qui non sono un curriculum "
             "forense. Sono evidenze incardinate, raccolte per materia "
             "e per anno, con la documentazione del giudizio che le "
             "accompagna. Ogni scheda nomina la giurisdizione, il "
             "grado, la materia, l'anno, l'oggetto del contenzioso, e "
             "la massima depositata in cinque righe — perché una "
             "decisione che non si lascia raccontare in cinque righe, "
             "probabilmente non si è ancora chiarita. Le quattro "
             "decisioni selezionate qui sotto coprono un arco di "
             "quattro anni e quattro materie diverse: un orientamento "
             "delle Sezioni Unite sulla responsabilità professionale, "
             "una cassazione civile in contenzioso bancario, una "
             "sentenza del TAR Lombardia in amministrativo regolatorio, "
             "e un appello tributario a Milano."),
        ],
        # Side-rail anchor links (4 links · Manrope 14px ink-on-bone).
        # Per copy-authoring §6.2 final block. Anti-collision: NOT
        # Cornice's `Lo studio · Servizi · Progetti · Contatti`.
        "narrative_side_rail": [
            ("Studio · l'avvocato fondatore",       "studio"),
            ("Materie · le dodici materie",          "materie"),
            ("Pubblicazioni · massimario interno",   "studio"),
            ("Contatti · apri un parere preliminare", "contatti"),
        ],

        # Sectors-ribbon (typographic block · 12 materie del contenzioso
        # · NO photos). NOT a card-grid (Pragma) · NOT a 2x2 matrix
        # (Continua) · NOT a calendar (Fiscus) · NOT a percorso
        # (Solaria) · NOT Cornice's `tipologie d'intervento`.
        "sectors_label":    "MATERIE · IL CAMPO DEL CONTENZIOSO",
        "sectors_lead":
            "Dodici materie del contenzioso: tutte trattate in studio, "
            "mai delegate a corrispondenti esterni. Lo studio non si "
            "dichiara generalista né specialistico — sceglie le cause "
            "per oggetto, per grado di giudizio e per giurisdizione.",
        # 12 cells · 1-3 words each · Manrope 14px uppercase
        # letter-spacing 0.04em (per copy-authoring §4.3 + §6.3).
        "sectors": [
            "penale tributario", "civile contrattualistica", "amministrativo regolatorio",
            "contenzioso bancario", "responsabilità professionale", "recupero crediti complesso",
            "diritto societario", "tributario", "esecuzioni",
            "lavoro complesso", "CTU forense", "ENCA mediation",
        ],
        "sectors_trailing":
            "Una materia entra in studio quando l'evidenza è "
            "incardinabile e la giurisprudenza è leggibile. Esce "
            "quando il fascicolo non si lascia scrivere in cinque "
            "righe.",
        "sectors_counter":
            "Ventotto sentenze citate · quattordici massime "
            "pubblicate dal Foro Italiano e dalla Giurisprudenza "
            "Italiana fra il <em>2008</em> e il 2024 · trentuno anni "
            "di patrocinio in tutti i gradi fino alla Cassazione.",

        # Leadership · LF-2 L6=single-portrait-feature. ONE founder
        # masthead (NOT a 4-card grid like Pragma · NOT a 3-pillar
        # photo trio like Continua · NOT typographic-only like
        # Pragma/Fiscus). R-LF2-1 binding-triple satisfied (50s-or-
        # senior + chambers-with-codices-mid-ground + environmental-
        # NOT-studio-backdrop). R-LF2-2 founder-identity gender-name-
        # pronouns lock per copy-authoring §1: Lorenzo Marchetti ·
        # masculine throughout · 60s · Cassazionista dal 2003.
        "leadership_label":   "STUDIO FOUNDER · AVVOCATO CASSAZIONISTA",
        "leadership_heading": "Lorenzo <em>Marchetti</em>",
        "leadership_role":
            "fondatore · responsabile delle memorie e dei ricorsi in Cassazione",
        "leadership_caption": "Lo studio · chambers di via Borgonuovo · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Lorenzo Marchetti ha aperto Causa nel 1995 a Milano, dopo "
            "otto anni di patrocinio in due studi legali milanesi "
            "specializzati in contenzioso civile commerciale e in "
            "diritto bancario. Si è laureato in Giurisprudenza "
            "all'Università degli Studi di Milano nel 1987, con una "
            "tesi sul concorso apparente di norme nel diritto "
            "tributario, e ha conseguito la specializzazione in "
            "diritto privato presso la stessa università. È iscritto "
            "all'Albo Avvocati di Milano dal 1995 e abilitato al "
            "patrocinio davanti alle Magistrature Superiori "
            "(Cassazionista) dal 2003. Lavora a tempo pieno sui "
            "contenziosi dello studio: dirige la redazione delle "
            "memorie, scrive i ricorsi in Cassazione, segue il "
            "giudizio fino al deposito della decisione, e cura il "
            "massimario interno che pubblica le sentenze ottenute.",

            "Tra le sentenze citate ricordiamo l'orientamento delle "
            "Sezioni Unite del 2024 in tema di responsabilità "
            "professionale del consulente fiscale, la cassazione civile "
            "sez. III del 2023 sul diritto del cliente bancario al "
            "rimborso degli interessi anatocistici, una sentenza del "
            "TAR Lombardia del 2022 sulla legittimità di un "
            "provvedimento sanzionatorio AGCOM, e la cassazione "
            "tributaria del 2021 sull'interpretazione dell'art. 36-bis "
            "D.P.R. 600/1973. Le sue voci sono raccolte in quattordici "
            "massime pubblicate dal Foro Italiano e dalla "
            "Giurisprudenza Italiana fra il 2008 e il 2024.",
        ],
        # Forensic-publication register per copy-authoring §4.4.
        # R-CAU-3 mitigation: zero `Sezione A · Revisore Legale ·
        # Iscritto Sezione · Albo Dottori Commercialisti` (Fiscus's
        # mixed-Albo set). Cassazionista is the founder's actual
        # title here, not a commercialista credential vocabulary item.
        "leadership_credentials": [
            "Albo Avvocati Milano · Iscritto Ordine degli Avvocati di Milano · dal 1995",
            "Cassazionista · abilitato al patrocinio davanti alle Magistrature Superiori dal 2003",
            "ENCA · Ente Nazionale Conciliazione Avvocati · iscritto sezione mediatori",
            "Albo CTU forense · Tribunale di Milano · sezione contenzioso civile",
        ],
        "leadership_secondary_cta_label": "Studio · biografia estesa, voci in massimario",
        "leadership_secondary_cta_href":  "studio",

        # Cases magazine-grid · LF-2 L7=magazine-grid · 3+1 layout.
        # 1 hero card (large · 8-col · Cass. SS.UU. 2024 landmark) +
        # 3 small cards (4-col each: Cass. civ. III bancario 2023 ·
        # TAR Lombardia AGCOM 2022 · App. Milano tributario 2021).
        # Each card carries photo + eyebrow + h3 (italic em on a
        # forensic-publication noun · per LF-2 family rule) + body
        # + pill (citation + grade + role).
        # Hero-card-as-lead-story binding (AC-10 + R-LF2-4): card 1
        # is unambiguously the lead landmark (largest photo · Cass.
        # SS.UU. = highest forensic register · longest em-word
        # `incardinata` paying off the hero h1's `evidenza
        # incardinata`).
        "cases_label":   "CONTENZIOSO — EVIDENZE INCARDINATE",
        "cases_intro":
            "Quattro evidenze depositate, in ordine cronologico "
            "inverso. Giurisdizione, grado, materia, anno, oggetto "
            "del contenzioso e la massima.",
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · CASS. SS.UU. · 2024 · RESPONSABILITÀ PROFESSIONALE",
                "title":
                    "Sezioni Unite — la responsabilità professionale "
                    "del consulente fiscale, riletta come obbligazione "
                    "di risultato <em>incardinata</em> sull'evidenza "
                    "preliminare",
                "body":
                    "Causa è patrono di parte ricorrente nel ricorso "
                    "che le Sezioni Unite della Corte di Cassazione "
                    "hanno deciso nell'aprile 2024, con rimessione "
                    "dalla terza sezione civile. La controversia "
                    "opponeva un contribuente al proprio consulente "
                    "fiscale, in tema di responsabilità professionale "
                    "per omessa segnalazione di un termine di "
                    "impugnazione in materia tributaria. Lo studio "
                    "ha sostenuto, e la Corte ha accolto, "
                    "l'orientamento secondo cui la responsabilità del "
                    "consulente fiscale si incardina sull'evidenza "
                    "preliminare di cui il professionista poteva e "
                    "doveva essere a conoscenza al momento "
                    "dell'incarico — rileggendo la prestazione come "
                    "obbligazione di risultato circoscritto. La "
                    "massima è stata pubblicata dal Foro Italiano "
                    "(massima n. 14 del massimario interno).",
                "pill":
                    "Cassazione SS.UU.  ·  grado di legittimità  ·  2024  ·  ricorrente",
                "photo":    _CASE_HIGHCOURT_EXTERIOR,
                "photo_alt":
                    "Dettaglio architettonico di alta corte italiana · "
                    "frontone classico con iscrizione latina · luce "
                    "fredda overcast",
                "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · CASS. CIV. SEZ. III · 2023 · CONTENZIOSO BANCARIO",
                "title":
                    "Cassazione civile sez. III — anatocismo bancario "
                    "e onere della prova nella <em>giurisprudenza</em> "
                    "di legittimità",
                "body":
                    "Causa ha patrocinato il cliente bancario nella "
                    "cassazione civile sez. III dell'ottobre 2023, in "
                    "tema di rimborso degli interessi anatocistici "
                    "corrisposti su un conto corrente di "
                    "corrispondenza fra il 2003 e il 2014. Lo studio "
                    "ha sostenuto la riconducibilità dell'onere "
                    "probatorio del nesso eziologico in capo "
                    "all'istituto bancario, conforme all'orientamento "
                    "di legittimità consolidato dal 2014. La sentenza "
                    "ha cassato con rinvio. Massima n. 11 del "
                    "massimario interno.",
                "pill":
                    "Cass. civ. III  ·  grado di legittimità  ·  2023  ·  ricorrente",
                "photo":    _CASE_FASCICOLI_STACK,
                "photo_alt":
                    "Stack di fascicoli legali con etichette di "
                    "registro · luce fredda da scrivania · macro · "
                    "zero persone",
                "slug":     "cass-civ-iii-anatocismo-bancario-2023",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · TAR LOMBARDIA · 2022 · AMMINISTRATIVO REGOLATORIO",
                "title":
                    "TAR Lombardia — annullamento di un provvedimento "
                    "sanzionatorio AGCOM e il <em>principio</em> di "
                    "proporzionalità",
                "body":
                    "Causa è patrono di parte ricorrente nel giudizio "
                    "di primo grado avanti il TAR Lombardia, sez. III, "
                    "conclusosi nell'aprile 2022 con annullamento del "
                    "provvedimento sanzionatorio AGCOM impugnato per "
                    "eccesso di potere e violazione del principio di "
                    "proporzionalità della sanzione amministrativa "
                    "pecuniaria, alla luce dell'orientamento del "
                    "Consiglio di Stato del 2019. La sentenza non è "
                    "stata appellata da AGCOM. Massima n. 9 del "
                    "massimario interno.",
                "pill":
                    "TAR Lombardia  ·  primo grado  ·  2022  ·  ricorrente",
                "photo":    _CASE_BENCH_CHAIR,
                "photo_alt":
                    "Sedia da banco giudiziale vuota · alta spalliera "
                    "in rovere · pannelli verticali in legno alle "
                    "spalle · luce fredda · zero persone",
                "slug":     "tar-lombardia-agcom-proporzionalita-2022",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · CORTE D'APPELLO MILANO · 2021 · TRIBUTARIO",
                "title":
                    "Appello Milano — l'art. 36-bis D.P.R. 600/1973 e "
                    "il perimetro della <em>controversia</em> tributaria",
                "body":
                    "Causa ha sostenuto, in grado di appello presso la "
                    "Corte d'Appello di Milano sez. tributaria, "
                    "l'interpretazione restrittiva dell'art. 36-bis "
                    "D.P.R. 600/1973 in materia di liquidazione "
                    "automatizzata delle dichiarazioni dei redditi. La "
                    "sentenza, depositata nel settembre 2021, ha "
                    "riformato la decisione di primo grado della "
                    "Commissione Tributaria, annullando la cartella di "
                    "pagamento. Massima n. 7 del massimario interno.",
                "pill":
                    "App. Milano trib.  ·  secondo grado  ·  2021  ·  appellante",
                "photo":    _CASE_CODEX_SPINE,
                "photo_alt":
                    "Macro del dorso di un codice rilegato · "
                    "tipografia oro su pelle scura · numerazione "
                    "romana del volume · luce fredda morbida",
                "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
            },
        ],
        "cases_trailing_label": "Tutto il contenzioso · cronologia 1995–2024",
        "cases_trailing_href":  "contenzioso",

        # CTA closer (LF-2 cream-hairline · NOT dark · LF-2-specific
        # polarity inversion · CS-TONE-03 demoted at family level).
        # Voice anchor verbatim recurrence on h2 (surface 2/2 of
        # AC-15) — with em on `evidenza`. Filled-bottle-green CTA pill
        # (NOT rust · NOT brass · NOT emerald · planner-brief §13.12
        # hard ban on Cornice's filled-rust). Closing-line negation
        # is forensic-register: `Nessuna call di scoperta · Nessun
        # mandato senza screening` — copy-authoring §6.6 negation
        # closer (shape-shared with Cornice's two-negation closer per
        # LF-2 family rule, content explicitly different).
        "cta_label":     "PARERE PRELIMINARE",
        "cta_intro":
            "I patrocini cominciano da una sola pagina: il parere preliminare.",
        # Voice anchor restated VERBATIM at the closer (copy-authoring
        # §1 + §6.6 + AC-15).
        "cta_heading":
            "Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.",
        "cta_form_hint":
            "Oggetto del contenzioso · grado di giudizio · controparte · "
            "fascia di valore · giurisdizione · evidenza preliminare "
            "allegabile. Risposta entro cinque giorni lavorativi.",
        "cta_primary":   "Apri un parere preliminare",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "Nessuna call di scoperta. Nessun mandato senza "
            "screening. Solo l'evidenza, e la sua giurisdizione.",
        "cta_sub_line":
            "Causa · studio legale · Milano · dal 1995",
    },

    # ─── STUDIO (about · Pubblicazioni nav-label) ───────────────
    # The about page is the firm's CV / biography / massimario archive
    # / sede page. Per copy-authoring §7. The navbar surfaces this
    # page as "Pubblicazioni" (planner-brief §11 + copy-authoring
    # §5.2 fallback path: `pubblicazioni` rolled into Studio anchor
    # rather than shipping as a separate page).
    "studio": {
        "eyebrow":   "LO STUDIO · CHI SIAMO · CV",
        "headline":
            "Causa · studio legale di patrocinio editoriale dal <em>1995</em>.",
        "intro":
            "Milano. Un avvocato fondatore, due associati, una "
            "segreteria. Patrociniamo poco, e fino in fondo.",
        # Navbar CTA pill repeats Causa's primary CTA on every inner
        # page (the corporate-suite `_base.html` reads
        # `page_data.primary_cta` with a default of "Apri un fascicolo"
        # — Cornice's literal — so omitting this field would bleed
        # Cornice's CTA copy onto Causa's navbar across all inner
        # pages, breaching planner-brief §13.7 hard ban on the
        # fascicolo / dossier mental model).
        "primary_cta":  "Apri un parere preliminare",

        # History strip — five structural choices, thirty-one years
        # of forensic-publication practice. Mirrors LF-2 about's
        # history-strip composition (Cornice precedent · five dates).
        "history_label":   "TAPPE DELLO STUDIO",
        "history_heading": "Cinque date, trentuno anni di patrocinio editoriale.",
        "history_intro":
            "Cinque scelte strutturali dietro le quali si legge il "
            "carattere dello studio — l'autorialità di un Cassazionista "
            "solo, il massimario interno come metodo, la giurisdizione "
            "come prima forma di rispetto, la materia come campo del "
            "contenzioso, il patrocinio fino al deposito della "
            "decisione.",
        "history": [
            ("1995", "Fondazione",
             "Lorenzo Marchetti apre Causa in via Borgonuovo a Milano, "
             "dopo otto anni di patrocinio in due studi legali "
             "milanesi specializzati in contenzioso civile commerciale "
             "e in diritto bancario. La sede è scelta per una sola "
             "ragione: tre locali su una corte interna, uno per la "
             "redazione delle memorie, uno per il massimario interno, "
             "uno per la segreteria."),
            ("2003", "Abilitazione Cassazionista",
             "Lorenzo Marchetti consegue l'abilitazione al patrocinio "
             "davanti alle Magistrature Superiori (Cassazionista). Da "
             "quell'anno lo studio accetta ricorsi per cassazione in "
             "materia civile, tributaria e amministrativa, e cura le "
             "memorie di parte resistente in giudizi di legittimità."),
            ("2008", "Prima massima pubblicata in massimario",
             "La prima sentenza di legittimità citante un orientamento "
             "sostenuto dallo studio viene pubblicata dal Foro "
             "Italiano. Da quell'anno lo studio registra ogni sentenza "
             "ottenuta — vinta o perduta — nel massimario interno "
             "entro sessanta giorni dal deposito."),
            ("2018", "Iscrizione Albo CTU forense",
             "Lo studio si iscrive all'Albo CTU forense del Tribunale "
             "di Milano (sezione contenzioso civile). Da quell'anno "
             "accetta consulenze tecniche d'ufficio su contenzioso "
             "societario, valutazioni d'azienda contestate e "
             "responsabilità contabile."),
            ("2024", "Quattordicesima massima in massimario interno",
             "La quattordicesima massima dello studio entra nel "
             "massimario interno: l'orientamento delle Sezioni Unite "
             "in tema di responsabilità professionale del consulente "
             "fiscale, con rimessione dalla terza sezione civile. "
             "Patrocinio del cliente ricorrente, sentenza depositata "
             "in aprile, massima pubblicata dal Foro Italiano."),
        ],

        # Values · four non-negotiable principles (per copy-authoring
        # §7 ASSOCIATI block + §6.2 narrative essence). Forensic-
        # publication register throughout — explicitly NOT Cornice's
        # `Un architetto autoriale · Il rilievo come primo gesto`.
        "values_label":   "PRINCIPI EDITORIALI",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Sono i quattro principi che separano un patrocinio Causa "
            "da un mandato standardizzato. Sono scritti nel patto di "
            "mandato firmato in prima udienza, non sul sito.",
        "values": [
            ("01", "Un Cassazionista autoriale",
             "La firma del ricorso è quella di un avvocato solo, non "
             "di una società tra avvocati a più mani. La responsabilità "
             "tecnica resta concentrata, perché un'evidenza per essere "
             "sostenuta deve avere una voce. Le collaborazioni esterne "
             "passano attraverso lo studio, non lo sostituiscono."),
            ("02", "La giurisdizione come primo gesto",
             "Ogni causa si apre con uno screening serio della "
             "giurisdizione. La materia che già esiste viene letta "
             "come un fascicolo, con i suoi precedenti, i suoi gradi, "
             "le sue eccezioni preliminari. Niente patrocinio prima "
             "che il foro, il grado e la giurisdizione siano stati "
             "letti integralmente."),
            ("03", "Il massimario interno come metodo",
             "Tutte le sentenze ottenute — vinte e perdute — vengono "
             "registrate nel massimario interno entro sessanta giorni "
             "dal deposito, con la documentazione del giudizio "
             "completa. Il massimario non è marketing: è la regola "
             "che lasciamo a chi verrà dopo."),
            ("04", "Niente screening respinti a pagamento",
             "I pareri preliminari che non superano la fase di "
             "screening vengono restituiti con una nota motivata, "
             "gratuitamente. Non addebitiamo screening respinti. La "
             "valutazione dell'incardinabilità dell'evidenza è la "
             "porta dello studio, non un servizio a consumo."),
        ],

        "team_label":   "STUDIO E ASSOCIATI",
        "team_heading": "Tre avvocati, una sola sede, una sola segreteria.",
        "team_intro":
            "Lo studio è formato da un avvocato fondatore Cassazionista, "
            "due associati e una segreteria. Patrociniamo a tempo pieno "
            "fra dodici e diciotto cause in parallelo — mai più di "
            "venti. Le pratiche con la cancelleria, gli uffici della "
            "Procura, l'Avvocatura dello Stato e gli enti regolatori "
            "vengono trattate in studio, non delegate a corrispondenti "
            "esterni.",
        "team": [
            {"name": "Lorenzo Marchetti",
             "role": "Studio Founder · Avvocato Cassazionista",
             "office": "Milano",
             "bio":
                "Fondatore. Università degli Studi di Milano · "
                "Giurisprudenza · specializzazione in diritto privato. "
                "Albo Avvocati Milano dal 1995 · Cassazionista dal "
                "2003 · ENCA mediatori · Albo CTU forense Tribunale di "
                "Milano. Dirige la redazione delle memorie, scrive i "
                "ricorsi in Cassazione, cura il massimario interno."},
            {"name": "Avv. Chiara Bevilacqua",
             "role": "Avvocata associata · Societario + bancario",
             "office": "Milano",
             "bio":
                "Associata dal 2017 · Albo Avvocati Milano dal 2014 · "
                "specializzazione in diritto societario e contenzioso "
                "bancario · supervisiona le memorie di parte ricorrente "
                "nei contenziosi societari e nelle azioni di "
                "responsabilità · referente per il massimario interno "
                "· iscritta sezione mediatori ENCA dal 2020."},
            {"name": "Avv. Tommaso De Luca",
             "role": "Avvocato associato · Amministrativo + tributario",
             "office": "Milano",
             "bio":
                "Associato dal 2021 · Albo Avvocati Milano dal 2018 · "
                "specializzazione in diritto amministrativo e "
                "contenzioso tributario · referente per i ricorsi al "
                "TAR Lombardia e alle Commissioni Tributarie · Albo "
                "CTU forense Tribunale di Milano dal 2022 (sezione "
                "contenzioso civile)."},
        ],

        "coordinates_label": "LA SEDE",
        "coordinates": [
            ("Milano", "via Borgonuovo 14 · 20121 · tre locali su corte interna"),
            ("Studio", "ricevimento su appuntamento · lunedì-venerdì · 09:00-18:00"),
            ("Foro di Milano", "pratiche con la cancelleria curate internamente · zero corrispondenti esterni"),
        ],

        "cta_heading": "Un patrocinio comincia da una sola pagina.",
        "cta_intro":
            "La prima pagina di ogni patrocinio è il parere "
            "preliminare: una scheda di sintesi che lo studio legge "
            "integralmente, e a cui risponde entro cinque giorni "
            "lavorativi con una nota motivata. Se il parere è "
            "negativo, la nota motivata viene comunque consegnata "
            "gratuitamente · senza addebito di screening · senza "
            "obbligo di mandato.",
        "cta_primary":   "Apri un parere preliminare",
        "cta_primary_href": "contatti",
    },

    # ─── MATERIE (services) ────────────────────────────────────
    # Per copy-authoring §8. 12 materie del contenzioso · grid 4×3
    # at 1100+ · 2×6 at 880 · 1×12 at 720 · per services.html template
    # rendering. Each block: num · h3 · body · scope · meta tuple.
    "materie": {
        "eyebrow":  "MATERIE · LE DODICI MATERIE DEL CONTENZIOSO",
        "headline": "Le <em>materie</em> del contenzioso — dodici, tutte trattate in studio.",
        "intro":
            "Lo studio non si dichiara generalista né specialistico. "
            "Le materie sono il campo del contenzioso: ciò che "
            "determina la giurisdizione e il grado di giudizio. Una "
            "materia entra in studio quando l'evidenza è "
            "incardinabile e la giurisprudenza è leggibile in cinque "
            "righe.",
        "primary_cta":  "Apri un parere preliminare",

        "svc_duration_label": "Foro · grado",
        "svc_leader_label":   "Patrocinio",

        "services": [
            {
                "num":   "01",
                "title": "Penale tributario",
                "blurb":
                    "Patrocinio in tutti i gradi del processo penale "
                    "tributario per imprenditori, amministratori e "
                    "liberi professionisti. Difesa nei giudizi per "
                    "omessa dichiarazione, omesso versamento, "
                    "sottrazione fraudolenta al pagamento delle "
                    "imposte ai sensi del D.lgs. 74/2000.",
                "scope": [
                    "Difesa di imputati e parti civili",
                    "Riti speciali e patteggiamento ex art. 444 c.p.p.",
                    "Ricorsi per cassazione penale (sez. III + sez. V)",
                    "Coordinamento con consulenti tributari di parte",
                ],
                "duration": "Tribunale · App. · Cassazione",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "02",
                "title": "Civile contrattualistica",
                "blurb":
                    "Contenzioso civile su contratti commerciali, "
                    "fornitura, agenzia, distribuzione, "
                    "somministrazione. Azioni di inadempimento, "
                    "risoluzione contrattuale, risarcimento danno e "
                    "azioni di nullità per vizio di consenso.",
                "scope": [
                    "Cause di valore superiore a € 50.000",
                    "Atti di citazione e memorie autorizzate",
                    "Provvedimenti d'urgenza ex art. 700 c.p.c.",
                    "Ricorsi per cassazione civile",
                ],
                "duration": "Tribunale · App. · Cassazione",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "03",
                "title": "Amministrativo regolatorio",
                "blurb":
                    "Ricorsi contro atti delle Autorità indipendenti "
                    "(AGCOM, AGCM, Garante Privacy, ANAC). "
                    "Impugnazione di provvedimenti sanzionatori, di "
                    "diniego, di inibitoria. Patrocinio in primo "
                    "grado TAR e in appello al Consiglio di Stato.",
                "scope": [
                    "Ricorsi al TAR Lombardia · sez. III · regolatorie",
                    "Appelli al Consiglio di Stato · sez. VI",
                    "Memorie di trattazione orale",
                    "Coordinamento con consulenti tecnici di parte",
                ],
                "duration": "TAR · Cons. Stato",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "04",
                "title": "Contenzioso bancario",
                "blurb":
                    "Cause contro istituti di credito per anatocismo "
                    "bancario, usura, errata segnalazione in Centrale "
                    "Rischi, contestazione di contratti di mutuo, "
                    "leasing e derivati. Patrocinio in tutti i gradi, "
                    "fino alla Cassazione civile.",
                "scope": [
                    "CTU contabili e perizie di parte",
                    "Azioni di restituzione e di nullità clausole",
                    "Ricorsi per cassazione civile sez. I + III",
                    "Coordinamento con periti bancari indipendenti",
                ],
                "duration": "Trib. · App. · Cassazione",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "05",
                "title": "Responsabilità professionale",
                "blurb":
                    "Azioni di responsabilità contro consulenti "
                    "fiscali, avvocati, medici, professionisti "
                    "tecnici. Patrocinio sia per la parte danneggiata "
                    "sia per il professionista convenuto. Materia in "
                    "costante evoluzione giurisprudenziale (cfr. "
                    "Cass. SS.UU. 2024).",
                "scope": [
                    "Azioni risarcitorie contrattuali ed "
                    "extracontrattuali",
                    "Quantificazione del danno secondo legittimità",
                    "Ricorsi per cassazione civile (anche SS.UU.)",
                    "Memorie tecniche e ricostruzione dell'evidenza",
                ],
                "duration": "Trib. · App. · Cassazione · SS.UU.",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "06",
                "title": "Recupero crediti complesso",
                "blurb":
                    "Recupero crediti commerciali superiori a € "
                    "50.000 · decreti ingiuntivi e relative "
                    "opposizioni · esecuzioni mobiliari e immobiliari "
                    "· azioni revocatorie ordinarie e fallimentari.",
                "scope": [
                    "Decreti ingiuntivi e opposizioni",
                    "Esecuzioni presso terzi e revocatorie",
                    "Pignoramenti immobiliari e mobiliari",
                    "Coordinamento con periti estimativi",
                ],
                "duration": "Trib. · Esecuzioni",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "07",
                "title": "Diritto societario contenzioso",
                "blurb":
                    "Azioni di responsabilità contro amministratori, "
                    "sindaci e direttori generali. Impugnazione di "
                    "delibere assembleari e consiliari. Patti "
                    "parasociali, covenant breach. Contenzioso fra "
                    "soci in società di capitali.",
                "scope": [
                    "Azioni ex artt. 2392-2395 c.c.",
                    "Impugnazioni delibere ex art. 2377 c.c.",
                    "Cause innanzi al Tribunale delle Imprese",
                    "Ricorsi per cassazione civile sez. I",
                ],
                "duration": "Trib. impr. · App. · Cassazione",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "08",
                "title": "Tributario",
                "blurb":
                    "Ricorsi contro avvisi di accertamento "
                    "dell'Agenzia delle Entrate. Patrocinio davanti "
                    "alle Corti di Giustizia Tributaria di primo e "
                    "secondo grado. Ricorsi per cassazione in materia "
                    "tributaria.",
                "scope": [
                    "Cartelle di pagamento e iscrizioni a ruolo",
                    "Avvisi di accertamento e rettifica",
                    "Memorie di contraddittorio preventivo",
                    "Ricorsi ex art. 360 c.p.c. n. 3",
                ],
                "duration": "CGT 1° · CGT 2° · Cassazione",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "09",
                "title": "Esecuzioni",
                "blurb":
                    "Procedure esecutive mobiliari, immobiliari, "
                    "presso terzi. Opposizioni all'esecuzione e agli "
                    "atti esecutivi. Patrocinio dei creditori "
                    "procedenti e dei debitori esecutati.",
                "scope": [
                    "Pignoramenti immobiliari e procedure di vendita",
                    "Opposizioni ex artt. 615, 617, 619 c.p.c.",
                    "Distribuzione del ricavato",
                    "Coordinamento con custodi giudiziari",
                ],
                "duration": "Trib. esecuzioni",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "10",
                "title": "Lavoro complesso",
                "blurb":
                    "Contenzioso lavoristico ad alta complessità — "
                    "licenziamenti dirigenziali, mobbing, "
                    "demansionamento, retribuzione variabile "
                    "contestata. Casi con risvolti societari o "
                    "regolatori. NO contenzioso individuale standard.",
                "scope": [
                    "Licenziamenti ex artt. 18 St. lav. + Jobs Act",
                    "Azioni risarcitorie da mobbing e demansionamento",
                    "Patti di non concorrenza e ricorsi cautelari",
                    "Ricorsi per cassazione civile sez. lavoro",
                ],
                "duration": "Trib. lav. · App. · Cassazione",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "11",
                "title": "CTU forense",
                "blurb":
                    "Lo studio è iscritto all'Albo CTU forense del "
                    "Tribunale di Milano (sezione contenzioso "
                    "civile). Consulenze tecniche su contenzioso "
                    "societario, valutazioni d'azienda contestate e "
                    "responsabilità contabile.",
                "scope": [
                    "CTU su contenzioso societario",
                    "Valutazioni d'azienda contestate",
                    "Responsabilità contabile e finanziaria",
                    "Relazioni peritali su mandato del giudice",
                ],
                "duration": "CTU · Trib. Milano",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "12",
                "title": "ENCA mediation",
                "blurb":
                    "Lo studio è iscritto sezione mediatori ENCA "
                    "(Ente Nazionale Conciliazione Avvocati). "
                    "Mediazione civile obbligatoria nelle materie di "
                    "legge, mediazione delegata, e procedure "
                    "arbitrali in convenzione di arbitrato rituale.",
                "scope": [
                    "Mediazione civile obbligatoria ex D.lgs. 28/2010",
                    "Mediazioni delegate dal giudice",
                    "Arbitrati rituali ex artt. 806 ss. c.p.c.",
                    "Verbali di accordo e di chiusura motivata",
                ],
                "duration": "ENCA · arbitrato",
                "leader":   "Chiara Bevilacqua",
            },
        ],

        "process_label":   "METODO · QUATTRO STAGIONI DEL PATROCINIO",
        "process_heading": "Quattro fasi, una sola sequenza forense.",
        "process": [
            ("01", "Giurisdizione",
             "La materia che già esiste viene letta come un "
             "fascicolo. Foro, grado, eccezioni preliminari. La "
             "giurisdizione è la prima forma di rispetto e dura "
             "tipicamente cinque giorni di screening."),
            ("02", "Merito",
             "Oggetto del contenzioso, parti in causa, fascia di "
             "valore, urgenza procedurale, evidenza preliminare "
             "allegabile. Il merito è la cornice del patrocinio: "
             "definisce quale ricorso si scrive e quale no."),
            ("03", "Massima",
             "Il ricorso si scrive come una tesi citabile — quale "
             "principio invoca, quale orientamento conferma, quale "
             "evidenza deposita. Cinque righe in cui la decisione "
             "deve potersi raccontare."),
            ("04", "Deposito",
             "Udienza per udienza, grado per grado, fino al deposito "
             "della decisione. Tutte le sentenze ottenute restano "
             "scritte nel massimario interno · pubblicate entro "
             "sessanta giorni dal deposito."),
        ],

        "cta_heading":   "Quale materia fa al caso del vostro contenzioso?",
        "cta_intro":
            "Se la materia non è chiara, ci scriva una breve "
            "descrizione dell'oggetto del contenzioso e del grado "
            "di giudizio attuale. Le indicheremo la materia giusta "
            "entro cinque giorni lavorativi · entro quarantotto ore "
            "se l'urgenza è procedurale (termine in scadenza · "
            "udienza fissata).",
        "cta_primary":   "Apri un parere preliminare",
        "cta_primary_href": "contatti",
    },

    # ─── CONTENZIOSO (case_study_list) ─────────────────────────
    # Per copy-authoring §9. The cases list page renders the 4 case-
    # detail posts (rendered from the registry below · NO per-template
    # detail templates · CS-IMG-SEC-08 / Chiara A.13 precedent).
    "contenzioso": {
        "eyebrow":  "CONTENZIOSO · CRONOLOGIA 1995-2024",
        "headline":
            "Le sentenze citate — la <em>cronologia</em> del patrocinio · 1995–2024.",
        "intro":
            "Quattordici massime pubblicate dal Foro Italiano e "
            "dalla Giurisprudenza Italiana, più gli altri "
            "contenziosi selezionati. Tutte registrate nel "
            "massimario interno entro sessanta giorni dal deposito.",
        "primary_cta":  "Apri un parere preliminare",

        "cases_label": "Quattro decisioni rappresentative · in dettaglio",
        "cases_intro":
            "Lo studio registra ogni sentenza ottenuta — vinta o "
            "perduta — nel massimario interno entro sessanta giorni "
            "dal deposito. Le quattro decisioni in evidenza qui "
            "sotto sono quelle scelte editorialmente per illustrare "
            "il metodo dello studio: una per le Sezioni Unite di "
            "Cassazione, una per la cassazione civile sezione "
            "semplice, una per il giudizio amministrativo, e una "
            "per il contenzioso tributario in appello.",

        "cta_heading":   "Una causa simile alla vostra?",
        "cta_intro":
            "I fascicoli completi (memorie, ricorsi, controricorsi, "
            "documentazione di giudizio, nota a sentenza) sono "
            "disponibili in studio dietro richiesta motivata. La "
            "consultazione è gratuita ai sensi del Codice "
            "Deontologico Forense; la copia integrale del "
            "massimario interno si ottiene a copertura delle spese "
            "di stampa.",
        "cta_primary":   "Apri un parere preliminare",
        "cta_primary_href": "contatti",
    },

    # ─── POSTS · case_study_detail ─────────────────────────────
    # 4 case-detail entries · per copy-authoring §10. Registry-only
    # rendering (CS-IMG-SEC-08 + Chiara A.13 precedent · the platform
    # reads each entry and renders /contenzioso/<slug>/ from the
    # registry, NOT from per-template detail templates).
    #
    # Ethical audit (Codice Deontologico Forense art. 28 · always-on
    # anonymization): zero direct client naming across all 4 entries.
    # Each entry uses TYPE-OF-PARTY language ("il cliente bancario ·
    # l'operatore di comunicazioni elettroniche · il contribuente ·
    # il consulente fiscale convenuto"). Sentence numbers are
    # placeholders ([TBD]) for the draft tier — the build either
    # substitutes a real public-record citation OR keeps [TBD] for
    # tier=draft and substitutes pre-public-flip per copy-authoring
    # §10 closing note.
    "posts": [
        {
            "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
            "title":
                "Sezioni Unite — la responsabilità professionale del "
                "consulente fiscale, riletta come obbligazione di "
                "risultato incardinata sull'evidenza preliminare",
            "category": "Responsabilità professionale",
            "year":     "2024 · deposito aprile",
            "duration": "Cassazione SS.UU. · grado di legittimità · cassata senza rinvio",
            "client_code":
                "Cassazione · Sezioni Unite civili · rimessione dalla "
                "terza sezione civile · ricorrente principale · "
                "controparte: consulente fiscale convenuto · materia: "
                "responsabilità professionale · obbligazione di "
                "risultato circoscritto vs obbligazione di mezzi.",
            "lead":
                "La controversia è stata rimessa alla cognizione "
                "delle Sezioni Unite della Corte di Cassazione dalla "
                "terza sezione civile, in ragione del contrasto fra "
                "due orientamenti di legittimità sulla qualificazione "
                "dell'obbligazione del consulente fiscale rispetto "
                "alla segnalazione tempestiva di un termine di "
                "impugnazione tributaria.",
            "sections": [
                {
                    "label": "La giurisdizione",
                    "heading": "Rimessione dalla terza sezione civile alle Sezioni Unite",
                    "body":
                        "Il giudizio è stato rimesso alla cognizione "
                        "delle Sezioni Unite della Corte di "
                        "Cassazione dalla terza sezione civile, con "
                        "ordinanza interlocutoria del settembre "
                        "2023, in ragione del contrasto fra due "
                        "orientamenti di legittimità sulla "
                        "qualificazione dell'obbligazione del "
                        "consulente fiscale. Il primo orientamento "
                        "(dominante fra il 2014 e il 2020) "
                        "qualificava l'obbligazione come "
                        "obbligazione di mezzi, con conseguente "
                        "prova del nesso eziologico in capo al "
                        "cliente; il secondo orientamento "
                        "(emergente dal 2021) qualificava "
                        "l'obbligazione come obbligazione di "
                        "risultato circoscritto.",
                },
                {
                    "label": "L'argomento sostenuto",
                    "heading": "Obbligazione di risultato incardinata sull'evidenza preliminare",
                    "body":
                        "Lo studio, quale patrocinio del cliente "
                        "ricorrente, ha sostenuto l'orientamento "
                        "dell'obbligazione di risultato circoscritto, "
                        "invocando il principio della prevedibilità "
                        "dell'evidenza preliminare al momento del "
                        "conferimento dell'incarico professionale. "
                        "La memoria difensiva ha richiamato "
                        "l'orientamento della cassazione civile "
                        "sezione III del 2022 sui criteri di "
                        "prevedibilità del termine di impugnazione "
                        "in materia tributaria, e ha proposto la "
                        "rilettura dell'obbligazione come "
                        "responsabilità incardinata sulla diligenza "
                        "qualificata richiesta al consulente.",
                },
                {
                    "label": "L'esito",
                    "heading": "Cassata senza rinvio · massima n. 14",
                    "body":
                        "Le Sezioni Unite hanno accolto la "
                        "ricostruzione sostenuta dallo studio, "
                        "confermando l'orientamento "
                        "dell'obbligazione di risultato circoscritto "
                        "e incardinandolo sul criterio della "
                        "prevedibilità dell'evidenza preliminare. La "
                        "sentenza ha cassato senza rinvio la "
                        "sentenza di secondo grado della Corte "
                        "d'Appello, dichiarando la responsabilità "
                        "del consulente fiscale convenuto e "
                        "quantificando il danno secondo la "
                        "giurisprudenza consolidata di legittimità. "
                        "La massima è stata pubblicata dal Foro "
                        "Italiano (massima n. 14 del massimario "
                        "interno dello studio).",
                },
            ],
            "kpi": [
                ("SS.UU.",       "Sezioni Unite civili"),
                ("aprile 2024",  "deposito sentenza"),
                ("cassata",      "senza rinvio"),
                ("massima 14",   "Foro Italiano"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Avvocato fondatore + 1 associata · redazione del "
                "ricorso, controricorso e memoria difensiva in vista "
                "dell'udienza alle Sezioni Unite",
            "next_label":   "Cronologia successiva",
        },
        {
            "slug":     "cass-civ-iii-anatocismo-bancario-2023",
            "title":
                "Cassazione civile sez. III — anatocismo bancario e "
                "onere della prova nella giurisprudenza di "
                "legittimità",
            "category": "Contenzioso bancario",
            "year":     "2023 · deposito ottobre",
            "duration": "Cass. civ. III · grado di legittimità · cassata con rinvio",
            "client_code":
                "Cassazione · sezione III civile · ricorrente · "
                "controparte: istituto di credito resistente · "
                "materia: anatocismo bancario · onere della prova "
                "del nesso eziologico in capo all'istituto.",
            "lead":
                "Il giudizio di primo e secondo grado avevano "
                "respinto la domanda del cliente bancario di "
                "rimborso degli interessi anatocistici. Lo studio ha "
                "proposto ricorso per cassazione, sostenendo la "
                "riconducibilità dell'onere probatorio in capo "
                "all'istituto di credito.",
            "sections": [
                {
                    "label": "I gradi precedenti",
                    "heading": "Tribunale di Milano sez. imprese e Corte d'Appello di Milano",
                    "body":
                        "Il giudizio di primo grado avanti il "
                        "Tribunale di Milano sez. imprese e quello "
                        "di secondo grado avanti la Corte d'Appello "
                        "di Milano avevano respinto la domanda del "
                        "cliente bancario di rimborso degli "
                        "interessi anatocistici corrisposti su un "
                        "conto corrente di corrispondenza fra il "
                        "2003 e il 2014, con la motivazione che il "
                        "cliente non aveva fornito prova specifica "
                        "dell'illegittima capitalizzazione.",
                },
                {
                    "label": "L'argomento sostenuto",
                    "heading": "Onere probatorio incardinato sull'istituto bancario",
                    "body":
                        "Lo studio ha proposto ricorso per "
                        "cassazione, sostenendo la riconducibilità "
                        "dell'onere probatorio del nesso eziologico "
                        "in capo all'istituto bancario, in "
                        "conformità all'orientamento di legittimità "
                        "consolidato dalla cassazione civile "
                        "sezione I del 2014 e dalle Sezioni Unite "
                        "del 2018. Il ricorso ha articolato la "
                        "rilettura della disciplina dell'anatocismo "
                        "bancario nel quadro dell'asimmetria "
                        "informativa fra istituto di credito e "
                        "cliente correntista.",
                },
                {
                    "label": "L'esito",
                    "heading": "Cassata con rinvio · massima n. 11",
                    "body":
                        "La cassazione civile sez. III ha cassato "
                        "la sentenza di appello con rinvio alla "
                        "Corte d'Appello di Milano in diversa "
                        "composizione, recependo l'orientamento "
                        "sostenuto dallo studio. Il giudizio di "
                        "rinvio è stato disposto sotto il principio "
                        "di legittimità conforme. La massima è "
                        "stata registrata nel massimario interno "
                        "(n. 11) ed è in attesa di pubblicazione "
                        "esterna.",
                },
            ],
            "kpi": [
                ("Cass. III",    "sezione semplice"),
                ("ottobre 2023", "deposito sentenza"),
                ("cassata",      "con rinvio"),
                ("massima 11",   "massimario interno"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Avvocato fondatore + 1 associata · ricorso per "
                "cassazione, controricorso e memoria depositata in "
                "vista dell'udienza · supporto perito bancario "
                "indipendente",
            "next_label":   "Cronologia successiva",
        },
        {
            "slug":     "tar-lombardia-agcom-proporzionalita-2022",
            "title":
                "TAR Lombardia — annullamento di un provvedimento "
                "sanzionatorio AGCOM e il principio di "
                "proporzionalità",
            "category": "Amministrativo regolatorio",
            "year":     "2022 · deposito aprile",
            "duration": "TAR Lombardia · primo grado · annullamento integrale",
            "client_code":
                "TAR Lombardia · sezione III · ricorrente · "
                "controparte: AGCOM · materia: amministrativo "
                "regolatorio · provvedimento sanzionatorio "
                "pecuniario · principio di proporzionalità ex "
                "Cons. Stato sez. VI 2019.",
            "lead":
                "Lo studio ha proposto ricorso al TAR Lombardia per "
                "l'annullamento di un provvedimento sanzionatorio "
                "AGCOM irrogato nei confronti di un operatore di "
                "comunicazioni elettroniche per asserita violazione "
                "delle norme sulla trasparenza delle offerte "
                "commerciali.",
            "sections": [
                {
                    "label": "L'atto impugnato",
                    "heading": "Provvedimento sanzionatorio AGCOM ex art. 98 D.lgs. 259/2003",
                    "body":
                        "Lo studio ha proposto ricorso al TAR "
                        "Lombardia per l'annullamento di un "
                        "provvedimento sanzionatorio AGCOM irrogato "
                        "nei confronti di un operatore di "
                        "comunicazioni elettroniche per asserita "
                        "violazione delle norme sulla trasparenza "
                        "delle offerte commerciali. La sanzione era "
                        "stata irrogata all'esito di una fase "
                        "istruttoria con contraddittorio "
                        "procedimentale di sei mesi.",
                },
                {
                    "label": "I motivi di ricorso",
                    "heading": "Eccesso di potere e violazione del principio di proporzionalità",
                    "body":
                        "Il ricorso è stato fondato su due motivi "
                        "principali. Il primo, per eccesso di "
                        "potere sotto il profilo del difetto di "
                        "istruttoria: l'Autorità non aveva "
                        "acquisito alcuni elementi probatori "
                        "prodotti dall'operatore in sede di "
                        "contraddittorio procedimentale. Il "
                        "secondo, per violazione del principio di "
                        "proporzionalità della sanzione "
                        "amministrativa pecuniaria, alla luce "
                        "dell'orientamento del Consiglio di Stato "
                        "sez. VI del 2019 sui criteri di "
                        "determinazione della sanzione tenendo "
                        "conto della gravità della condotta, del "
                        "comportamento dell'agente e della sua "
                        "capacità contributiva.",
                },
                {
                    "label": "L'esito",
                    "heading": "Annullamento integrale · massima n. 9",
                    "body":
                        "Il TAR Lombardia ha accolto il ricorso, "
                        "annullando integralmente il provvedimento "
                        "sanzionatorio per violazione del principio "
                        "di proporzionalità. La sentenza non è "
                        "stata appellata da AGCOM. La massima è "
                        "stata registrata nel massimario interno "
                        "(n. 9) e ha contribuito al consolidamento "
                        "dell'orientamento sulla proporzionalità "
                        "delle sanzioni regolatorie.",
                },
            ],
            "kpi": [
                ("TAR Lomb.",    "sezione III"),
                ("aprile 2022",  "deposito sentenza"),
                ("annullato",    "integralmente"),
                ("massima 9",    "massimario interno"),
            ],
            "lead_partner": "Tommaso De Luca · Avvocato associato",
            "team":
                "Avvocato associato + avvocato fondatore · ricorso "
                "introduttivo, memoria di replica alle "
                "controdeduzioni AGCOM e memoria di trattazione "
                "orale",
            "next_label":   "Cronologia successiva",
        },
        {
            "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
            "title":
                "Corte d'Appello Milano sez. tributaria — l'art. "
                "36-bis D.P.R. 600/1973 e il perimetro della "
                "controversia tributaria",
            "category": "Tributario",
            "year":     "2021 · deposito settembre",
            "duration": "App. Milano trib. · secondo grado · riformata in appello",
            "client_code":
                "Corte d'Appello Milano · sezione tributaria · "
                "appellante · controparte: Agenzia delle Entrate · "
                "materia: tributario · liquidazione automatizzata "
                "ex art. 36-bis D.P.R. 600/1973 · perimetro "
                "contributivo restrittivo.",
            "lead":
                "Il giudizio di primo grado avanti la Commissione "
                "Tributaria Provinciale di Milano si era concluso "
                "con il rigetto del ricorso del contribuente "
                "avverso una cartella di pagamento emessa a seguito "
                "di controllo automatizzato ex art. 36-bis D.P.R. "
                "600/1973.",
            "sections": [
                {
                    "label": "Il primo grado",
                    "heading": "Commissione Tributaria Provinciale di Milano · rigetto del ricorso",
                    "body":
                        "Il giudizio di primo grado avanti la "
                        "Commissione Tributaria Provinciale di "
                        "Milano si era concluso con il rigetto del "
                        "ricorso del contribuente avverso una "
                        "cartella di pagamento emessa a seguito di "
                        "controllo automatizzato ex art. 36-bis "
                        "D.P.R. 600/1973. La Commissione aveva "
                        "ritenuto sufficiente il controllo "
                        "meramente formale per fondare la pretesa "
                        "tributaria.",
                },
                {
                    "label": "L'argomento sostenuto",
                    "heading": "Interpretazione restrittiva dell'art. 36-bis D.P.R. 600/1973",
                    "body":
                        "Lo studio ha proposto appello, sostenendo "
                        "l'interpretazione restrittiva dell'art. "
                        "36-bis che limita il controllo "
                        "automatizzato a una liquidazione meramente "
                        "aritmetica delle imposte dichiarate, senza "
                        "possibilità di rettifica del contenuto "
                        "sostanziale della dichiarazione "
                        "(orientamento della cassazione tributaria "
                        "del 2017 e del 2019). La memoria difensiva "
                        "ha articolato la rilettura del perimetro "
                        "della controversia tributaria nel quadro "
                        "del riparto fra controllo automatizzato e "
                        "rettifica sostanziale.",
                },
                {
                    "label": "L'esito",
                    "heading": "Riformata in appello · massima n. 7",
                    "body":
                        "La Corte d'Appello ha accolto integralmente "
                        "l'appello, annullando la cartella di "
                        "pagamento e condannando l'Agenzia delle "
                        "Entrate alle spese di giudizio. La "
                        "sentenza non è stata impugnata in "
                        "Cassazione e ha contribuito al "
                        "consolidamento dell'orientamento "
                        "restrittivo. Massima n. 7 del massimario "
                        "interno.",
                },
            ],
            "kpi": [
                ("App. Milano",   "sezione tributaria"),
                ("settembre 2021", "deposito sentenza"),
                ("riformata",     "in appello"),
                ("massima 7",     "massimario interno"),
            ],
            "lead_partner": "Tommaso De Luca · Avvocato associato",
            "team":
                "Avvocato associato + avvocato fondatore · atto di "
                "appello, memoria di replica all'Agenzia delle "
                "Entrate e memoria di trattazione orale",
            "next_label":   "Cronologia successiva",
        },
    ],

    # ─── CONTATTI ──────────────────────────────────────────────
    # Per copy-authoring §11. The 7-field forensic intake that screens
    # the parere preliminare. Anti-collision: NOT Cornice (project
    # scope + budget range + timeline horizon · architecture intake).
    # NOT Pragma (call-request shape). NOT Fiscus (P.IVA + CF gate).
    # NOT Solaria (discovery-call request). NOT Continua (mandate-
    # dialogue framing).
    "contatti": {
        "eyebrow":  "APRI UN PARERE PRELIMINARE",
        "headline": "Apri un <em>parere</em> preliminare — la prima pagina del patrocinio.",
        "intro":
            "Lo studio risponde entro cinque giorni lavorativi · "
            "entro quarantotto ore se l'urgenza è procedurale "
            "(termine in scadenza · udienza fissata).",
        "primary_cta":  "Apri un parere preliminare",

        "form_label":   "PARERE PRELIMINARE",
        "form_heading": "Compila la scheda di screening",
        "form_intro":
            "Il parere preliminare è la prima pagina del "
            "patrocinio: lo studio legge l'oggetto del contenzioso, "
            "il grado di giudizio attuale, la giurisdizione, la "
            "fascia di valore e l'urgenza, e restituisce una "
            "valutazione della incardinabilità dell'evidenza e "
            "della leggibilità della giurisprudenza in cinque "
            "righe. Il parere NON è un mandato difensivo · NON è "
            "un preventivo a consumo · NON è una call di scoperta. "
            "È uno screening tecnico, motivato per iscritto, da "
            "cui decidere insieme se aprire il fascicolo. Se il "
            "parere è negativo, la nota motivata viene comunque "
            "consegnata gratuitamente.",

        # Form fields per planner-brief §8 + copy-authoring §11.
        # 7 forensic-intake fields: oggetto · grado · controparte ·
        # valore · urgenza · evidenza preliminare · giurisdizione.
        # NO P.IVA + CF (Fiscus collision avoided · planner-brief
        # §3.3 hard ban). NO budget bracket (Cornice collision
        # avoided · §3.2 hard ban).
        "form_fields": [
            {"name": "name",      "label": "Nome",     "type": "text", "required": True,
             "placeholder": "Es. Marco",
             "helper": "Solo il nome di battesimo, grazie."},
            {"name": "surname",   "label": "Cognome",  "type": "text", "required": True,
             "placeholder": "Es. Bianchi",
             "helper": "Come compare nei documenti del committente."},
            {"name": "email",     "label": "Email",    "type": "email", "required": True,
             "placeholder": "marco@dominio.it",
             "helper": "Una casella che riceve la nota motivata fiduciaria."},
            {"name": "phone",     "label": "Telefono", "type": "tel", "required": False,
             "placeholder": "+39 ...",
             "helper": "Linea diretta per il primo contatto. Facoltativo."},
            {"name": "oggetto", "label": "Oggetto del contenzioso",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Descriva in 5-10 righe l'oggetto del contenzioso, "
                 "le parti, il punto in discussione. Non occorre "
                 "essere completi · una descrizione sintetica è "
                 "sufficiente.",
             "helper":
                 "Quanto basta a capire se la materia è incardinabile. "
                 "Non allegare ancora il fascicolo completo · le cifre "
                 "e gli altri dati si discutono in prima udienza."},
            {"name": "grado", "label": "Grado di giudizio attuale", "type": "select", "required": True,
             "options": [
                 "primo grado (Tribunale · CGT · TAR)",
                 "appello (Corte d'Appello · CGT 2° · Cons. Stato)",
                 "Cassazione (in corso o da proporre)",
                 "giudizio amministrativo non avviato",
                 "giudizio non ancora avviato (parere preventivo)",
             ],
             "helper": "Il grado in cui si trova attualmente la causa."},
            {"name": "controparte", "label": "Tipologia di controparte", "type": "text", "required": True,
             "placeholder":
                 "Es. istituto bancario · ente pubblico · controparte "
                 "commerciale · pubblica amministrazione · privato",
             "helper":
                 "Non è necessario nominare la controparte specifica "
                 "in questa fase · solo la tipologia."},
            {"name": "valore", "label": "Fascia di valore", "type": "select", "required": True,
             "options": [
                 "fino a € 50.000",
                 "€ 50.000 — € 250.000",
                 "€ 250.000 — € 1 M",
                 "€ 1 M — € 5 M",
                 "oltre € 5 M",
             ],
             "helper": "Il valore stimato della controversia."},
            {"name": "urgenza", "label": "Urgenza procedurale", "type": "select", "required": True,
             "options": [
                 "ordinaria (nessun termine in scadenza)",
                 "qualificata (termine entro 30 giorni)",
                 "procedurale (termine entro 7 giorni)",
             ],
             "helper":
                 "L'urgenza determina la cadenza di risposta dello "
                 "studio · 5 giorni lavorativi · 48 ore se procedurale."},
            {"name": "giurisdizione", "label": "Giurisdizione", "type": "select", "required": True,
             "options": [
                 "Italia (foro italiano)",
                 "Unione Europea (CGUE · TUE)",
                 "extra-UE (con elementi di diritto internazionale privato)",
             ],
             "helper": "La giurisdizione è la prima forma di rispetto."},
        ],

        # 3-section grouping per planner-brief §8 form structure.
        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che firmerà la procura alle liti, una volta avviato il mandato.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Oggetto del contenzioso",
             "meta": "L'oggetto è il primo testo del fascicolo. Cinque-dieci righe bastano.",
             "fields": ["oggetto"]},
            {"num": "03", "title": "Inquadramento procedurale",
             "meta": "Grado · controparte · valore · urgenza · giurisdizione.",
             "fields": ["grado", "controparte", "valore", "urgenza", "giurisdizione"]},
        ],

        "form_submit_label": "Apri il parere preliminare",
        "form_submit_note":
            "Lo studio leggerà la scheda entro cinque giorni "
            "lavorativi · entro quarantotto ore se l'urgenza è "
            "procedurale · e risponderà con una nota motivata "
            "all'indirizzo indicato. Nessun BDR esterno, nessuna "
            "automazione di sequence — il primo contatto è con "
            "l'avvocato.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi "
            "del Reg. UE 679/2016 e del D.lgs. 196/2003. I dati "
            "sono trattati ai fini esclusivi della valutazione del "
            "parere · custoditi presso lo studio di via Borgonuovo "
            "con accesso limitato ai tre avvocati. Sono informato "
            "del canale whistleblowing (D.lgs. 24/2023) attivo "
            "presso lo studio. Lo studio rispetta il segreto "
            "professionale ai sensi dell'art. 622 c.p. e del "
            "Codice Deontologico Forense.",

        "office_address_label": "Indirizzo",
        "office_area_label":    "Zona",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",

        "offices_label":   "LA SEDE",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Sede unica · Foro di Milano",
                "address": "via Borgonuovo 14 · 20121",
                "area":    "Brera · vicino Tribunale di Milano",
                "phone":   "+39 02 7634 8210",
                "email":   "parere@causa.legal",
            },
        ],

        "channels_label": "CANALI DIRETTI",
        "channels": [
            ("Segreteria di studio",                "+39 02 7634 8210",                 "Lun – Ven · 09:00 – 18:00"),
            ("Email per pareri preliminari",        "parere@causa.legal",               "Risposta entro 5 giorni"),
            ("PEC per atti già nei termini",        "causa.legale@pec.causa.legal",     "Atti urgenti · entro 24 ore"),
            ("Whistleblowing (D.lgs. 24/2023)",     "whistleblowing@causa.legal",       "Canale interno · cifrato"),
        ],

        "footnote":
            "Causa rispetta il segreto professionale ai sensi "
            "dell'art. 622 c.p. e del Codice Deontologico Forense. "
            "La consultazione del sito non costituisce conferimento "
            "di mandato. Lo studio non risponde a richieste anonime "
            "e non rilascia pareri preliminari per iscritto senza "
            "una scheda di screening compilata. Le informazioni sui "
            "compensi sono illustrate in prima udienza, secondo le "
            "tariffe forensi minime e i parametri D.M. 55/2014. Il "
            "canale whistleblowing è gestito ai sensi del D.lgs. "
            "24/2023 ed è accessibile a collaboratori, associati e "
            "segreteria.",
    },
}
