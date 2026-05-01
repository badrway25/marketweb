"""Cornice — Architecture studio (corporate-suite archetype) content.

Phase X.5 · A.5 build · IT-only · tier=draft (D-102 cadence). 5th
corporate-suite sibling · 1st architecture-firm variant · 1st LF-2
(Editorial Spread) occupant. The intake/planner/imagery/copy briefs
live at:

    factory/reports/corporate-suite/cornice-architettura/intake.md
    factory/reports/corporate-suite/cornice-architettura/planner-brief.md
    factory/reports/imagery/cornice-architettura/pool-selection.md
    factory/reports/copy/cornice-architettura/copy-authoring.md

Editorial identity: a single-principal architecture studio that
publishes its work as case-led editorial — each commission a built
argument, catalogued and annotated, not sold as a service. Voice
positioning is editorial-curatorial · architectural-discipline,
explicitly NOT decisional-gravity (Pragma) · NOT presidio (Fiscus) ·
NOT bounded-method (Solaria) · NOT stewardship-longitudinal
(Continua).

Forbidden similarities (intake §4 · 47 explicit anti-collision lines):
- vs Pragma:   no 55/45 hero · no separate cs-kpi-band · no boardroom
- vs Fiscus:   no fiscal-calendar mid-strip · no P.IVA/CF intake
- vs Solaria:  no percorso-cadenza · no 30s × 2 portrait pair
- vs Continua: no library-reading-room hero · no timeline cases ·
               no 60s + 40s portrait pair · no `argomento` collision
               with `generazioni` voice anchor (different em-noun)

LF-2 family-level demotions of cluster invariants (declared, not silent):
- CS-HERO-01 (55/45 hero)        → LF-2 declares stacked-editorial
- CS-TONE-03 (one dark band)     → LF-2 declares zero dark bands
- CS-RHYTHM-02 (sequence A)      → LF-2 declares sequence B
- CS-NAV-01 (sticky-top primary) → LF-2 declares split-wordmark on cream
- CS-FOOT-01 (3-col footer)      → LF-2 declares 4-col with whistleblowing
"""
from __future__ import annotations

from typing import Any


# ─── Pexels-only imagery pool · single source of truth ─────────────────
# Curator-approved at A.3 (factory/reports/imagery/cornice-architettura/
# pool-selection.md · reviewer-lgtm.md). Cross-cluster grep CLEAN against
# business-corporate · business-fiscal · business-coaching · business-
# stewardship pools. The 6 primary slots follow the canonical
# [hero, feature, portrait, portrait, detail, ambient] order; the 4
# magazine-grid extras are LF-2 specific (L7 needs 4 distinct case-card
# photos).

_HERO_BOLOGNA_PORTICO = (
    "https://images.pexels.com/photos/35715509/pexels-photo-35715509.jpeg"
    "?auto=compress&cs=tinysrgb&w=1600"
)
_FEATURE_SCALE_MODEL = (
    "https://images.pexels.com/photos/6614835/pexels-photo-6614835.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200"
)
_PORTRAIT_FOUNDER = (
    "https://images.pexels.com/photos/5915290/pexels-photo-5915290.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)
_PORTRAIT_COLLABORATOR = (
    "https://images.pexels.com/photos/6615222/pexels-photo-6615222.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)
_DETAIL_BLUEPRINT = (
    "https://images.pexels.com/photos/4458196/pexels-photo-4458196.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)
_AMBIENT_STUDIO_WALL = (
    "https://images.pexels.com/photos/36809500/pexels-photo-36809500.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)

# Magazine-grid extras (LF-2 L7=magazine-grid · 3+1 layout)
_CASE_CONCORSO = (
    "https://images.pexels.com/photos/2747599/pexels-photo-2747599.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200"
)
_CASE_RESIDENZIALE = (
    "https://images.pexels.com/photos/36547058/pexels-photo-36547058.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)
_CASE_RESTAURO = (
    "https://images.pexels.com/photos/36428417/pexels-photo-36428417.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)
_CASE_CORNICE_DETAIL = (
    "https://images.pexels.com/photos/13306459/pexels-photo-13306459.jpeg"
    "?auto=compress&cs=tinysrgb&w=800"
)


CORNICE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        # Home label deliberately distinct from the about-page label so the
        # navbar reads as 5 editorial-architectural sections without
        # repetition. Home = "Lo studio" (overview · the editorial
        # manifesto) · About = "Archivio" (history + cv + collana
        # monografica). Pattern follows Continua's home/about pair where
        # the two labels are different words, not the same word twice.
        {"slug": "home",      "label": "Lo studio",     "kind": "home"},
        {"slug": "studio",    "label": "Archivio",      "kind": "about"},
        {"slug": "servizi",   "label": "Servizi",       "kind": "services"},
        {"slug": "progetti",  "label": "Progetti",      "kind": "case_study_list"},
        {"slug": "contatti",  "label": "Contatti",      "kind": "contact"},
    ],

    # ─── Site-wide chrome (used by _base.html nav + footer) ─────
    "site": {
        "logo_initial": "C",
        # Cornice reads as a split-line publication masthead under
        # LF-2 (line 1 = wordmark · line 2 = subtitle). The
        # `logo_subtitle` field is the LF-2-specific second line; the
        # base nav reads it conditionally for split-wordmark families.
        "logo_word":      "CORNICE",
        "logo_subtitle":  "studio di architettura",
        "tag":            "Architettura editoriale · Milano · dal 2008",
        "phone":          "+39 02 6610 4708",
        "email":          "fascicolo@cornice-architettura.it",
        "address":        "via Pasquale Paoli 9 · 20143 Milano",
        "hours_compact":  "Mar – Ven · 10:00 – 18:00 · su appuntamento",
        "hours_footer_rows": [
            "Sabato · solo su appuntamento di rilievo",
            "Domenica · chiuso",
        ],
        "license":        "Albo OAPPC Milano N° 12.847 · CNAPPC · MIBAC qualifica restauro",
        "footer_intro":
            "Architettura editoriale · committenze pubbliche e private · "
            "Milano dal 2008. Quarantasette opere realizzate, ventitré "
            "concorsi consegnati, novanta fascicoli aperti in collana "
            "monografica.",
        "foot_studio":   "Studio",
        "foot_pages":    "Pagine",
        "foot_contact":  "Contatti",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milano · via Paoli 9 (sede unica)",
            "Studio aperto su appuntamento · martedì-venerdì",
            "Cantieri attivi · Bologna · Pietrasanta · Roma",
        ],
        # LF-2 footer L9 = 4-col-with-whistleblowing. The whistleblowing
        # column-level surface is the family signature on legal compliance
        # — not a footnote, a column. Mirrors the LF-5 elevation of the
        # same slot. CS-FOOT-02 (D.lgs. 24/2023) is binding for the
        # cluster; LF-2 promotes it to a column like LF-5 does.
        "whistleblowing_footer": {
            "heading":      "Segnalazioni",
            "eyebrow":      "Canale interno · D.lgs. 24/2023",
            "note":
                "Lo studio ha attivato un canale di segnalazione interno "
                "conforme al D.lgs. 24/2023 (direttiva UE 2019/1937). "
                "Tutela dell'anonimato e riservatezza dei dati. Il canale "
                "è aperto a committenze pubbliche, fornitori di cantiere "
                "e collaboratori esterni.",
            "email":        "whistleblowing@cornice-architettura.it",
            "policy_label": "Modello di gestione delle segnalazioni",
            "policy_href":  "contatti",
        },
        # Case-study cross-page meta labels. Cornice re-frames the
        # advisory "Practice / Anno / Durata" into editorial-architectural
        # vocabulary: "Tipologia / Anno / Stato di cantiere".
        "case_practice_label":     "Tipologia",
        "case_year_label":         "Anno fascicolo",
        "case_duration_label":     "Stato di cantiere",
        "case_lead_label":         "Architetto referente",
        "case_lead_partner_label": "Architetto referente",
        "case_team_label":         "Squadra di cantiere",
        "case_timeline_label":     "Cronologia di cantiere",
    },

    # ─── HOME (LF-2 sequence B) ─────────────────────────────────
    # Render order (lf2/content.html):
    #   1. cs-hero (LF-2 stacked-editorial · photo TOP + 8/4 split BELOW
    #      with KPI in hero credit overlay · L5=hero-overlay)
    #   2. cs-narrative (LF-2 L4=essay-with-anchors · drop-cap + 3
    #      pull-quotes + side-rail)
    #   3. cs-sectors (sentence-ribbon · 12 typologies)
    #   4. cs-leadership-single (LF-2 L6=single-portrait-feature)
    #   5. cs-cases-magazine (LF-2 L7=magazine-grid · 3+1)
    #   6. cs-cta-closer (cream hairline-bordered · NOT dark · LF-2 polarity)
    "home": {
        "eyebrow":     "STUDIO DI ARCHITETTURA · MILANO · DAL 2008",
        # Voice anchor verbatim · italic on the curatorial noun
        # `argomento` (copy-authoring §1 · CS-TYPE-02 single em).
        "headline":
            "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.",
        "intro":
            "Studio di architettura editoriale · committenze pubbliche e "
            "private · novanta fascicoli aperti dal 2008.",
        "primary_cta":   "Apri un fascicolo progetto",
        "primary_href":  "contatti",
        "secondary_cta": "Lo studio · pubblicazioni",
        "secondary_href":"studio",

        # LF-2 stacked-editorial hero — full-bleed photo TOP with credit
        # overlay carrying 3-stat tuple (L5=hero-overlay · CS-TONE-03
        # demoted at family level; KPI lives in the photo's overlay,
        # not on a separate dark band).
        "hero_image":              _HERO_BOLOGNA_PORTICO,
        "hero_image_alt":          "Portico restaurato a Bologna · 2023",
        "hero_image_credit_left":  ("Bologna · portico restaurato · 2023", "fascicolo n. 31"),
        "hero_image_credit_right": ("Sede dello studio", "Milano · via Paoli 9"),
        # 3-stat strip inside the hero credit overlay (LF-2 L5).
        # CS-DENSITY-04 cap (≤3 figures in overlay) respected.
        "hero_meta_strip": [
            ("Progetti realizzati",  "47"),
            ("Anni di pratica",      "18"),
            ("Città italiane",       "6"),
        ],
        # Side-quote in the right-4-col under the hero photo (LF-2 8/4
        # split BELOW). Em on the verb form `argomenta` — building the
        # editorial-curatorial motif (copy-authoring §12).
        "hero_side_quote":
            "L'architettura buona si <em>argomenta</em> — non si "
            "dimostra, non si vende, non si decora.",

        # Narrative essay (L4=essay-with-anchors · 4 paragraphs · drop-cap
        # on para 1 in rust Cormorant 84px · 3 pull-quotes interspersed ·
        # side-rail of anchor links). Replaces cs-pillars (LF-2 has no
        # pillars). The drop-cap is the LF-2 family typographic signature.
        "narrative_label":   "LO STUDIO · MANIFESTO EDITORIALE",
        "narrative_drop":    "L",
        # Pre-interleaved narrative blocks · paragraphs and pull-quotes
        # in render order (4 paragraphs · 3 quotes between them).
        # Each item is a (kind, text) tuple where kind is `para`, `drop`
        # (first paragraph with rust drop-cap), or `quote`. CS-TYPE-02
        # single italic em respected per heading-level surface (each
        # pull-quote is its own surface; em on the load-bearing word).
        "narrative_blocks": [
            ("drop",
             "'architettura buona si argomenta. Cornice è uno studio di "
             "architettura editoriale: ogni progetto pubblicato è un "
             "argomento costruito sul sito, sulla committenza, sul "
             "vincolo. Non firmiamo immagini accattivanti — pubblichiamo "
             "opere, ciascuna con la propria storia di cantiere e la "
             "propria documentazione. Lo studio esiste per misurare il "
             "contesto prima di disegnarlo, per scrivere il programma "
             "prima di abitarlo, per riconoscere quello che già c'è prima "
             "di aggiungere quello che manca. È un mestiere lento, che "
             "produce poche pagine all'anno, ma le produce intere."),

            ("quote",
             "Il rilievo è la <em>prima</em> forma di rispetto. "
             "Ciò che si argomenta su un sito già letto sarà sempre più "
             "solido di ciò che si decora su un sito muto."),

            ("para",
             "Ogni commissione passa attraverso quattro stagioni. Il "
             "rilievo, prima di tutto: l'opera che già esiste viene "
             "letta come un testo, con i suoi accenti, i suoi paragrafi, "
             "le sue cesure. Il contesto, poi: la committenza, l'uso, i "
             "vincoli del PRG e della Soprintendenza, le abitudini del "
             "paesaggio. L'argomento, infine: il progetto si scrive come "
             "una tesi — quale problema risolve, quale eredità rispetta, "
             "quale figura propone. Solo allora apriamo il cantiere, e "
             "lo seguiamo settimana per settimana, sito per sito, fino "
             "al collaudo. Le decisioni di progetto restano scritte: "
             "pubblichiamo ogni opera nella nostra collana monografica, "
             "perché un'architettura senza memoria non lascia regola."),

            ("quote",
             "Un <em>autore</em> non è chi firma più progetti, "
             "ma chi sa dire quale progetto non ha firmato — e perché."),

            ("para",
             "Lavoriamo per committenze pubbliche e private che cercano "
             "un autore — non un esecutore, non un pacchetto chiavi in "
             "mano. Comuni che restaurano una corte storica, enti "
             "culturali che riprogrammano un edificio dismesso, famiglie "
             "che riscrivono una casa di campagna, sviluppatori privati "
             "con una sensibilità editoriale, uffici tecnici comunali "
             "che chiedono un concorso. La nostra firma è quella di un "
             "architetto solo, non di un brand a più mani: la "
             "responsabilità autoriale resta concentrata, perché un "
             "argomento per essere riconoscibile deve avere una voce. "
             "Le collaborazioni con strutturisti, paesaggisti, "
             "restauratori e tecnici di cantiere passano attraverso lo "
             "studio, non lo sostituiscono."),

            ("quote",
             "Pubblicare un progetto non significa promuoverlo. "
             "Significa lasciare <em>regola</em> — perché chi verrà dopo "
             "possa contestarla, modificarla, o riconoscerla."),

            ("para",
             "Le opere che pubblichiamo qui non sono un portfolio "
             "commerciale. Sono argomenti costruiti, raccolti per "
             "tipologia e per anno, con la documentazione di cantiere "
             "che li accompagna. Ogni scheda nomina il sito, la "
             "committenza, il programma, la cronologia, il vincolo, e "
             "l'argomento del progetto in cinque righe — perché un'opera "
             "che non si lascia raccontare in cinque righe, probabilmente "
             "non si è ancora chiarita."),
        ],
        # Side-rail anchor links (5 links · Source Sans 3 14px ink).
        "narrative_side_rail": [
            ("Lo studio", "studio"),
            ("Servizi · commissioni", "servizi"),
            ("Progetti · fascicoli", "progetti"),
            ("Contatti · sede", "contatti"),
        ],

        # Sectors-ribbon (typographic block · 12 typologies · NO photos).
        # NOT a card-grid (Pragma) · NOT a 2x2 matrix (Continua) ·
        # NOT a calendar (Fiscus) · NOT a percorso (Solaria).
        "sectors_label":    "TIPOLOGIE D'INTERVENTO",
        "sectors_lead":
            "Lo studio interviene su dodici tipologie principali, "
            "raggruppate per scala dell'opera, programma della "
            "committenza e relazione con il vincolo paesaggistico o "
            "storico. Non lavoriamo a un menu di servizi: ciascuna voce "
            "dell'elenco nomina un argomento già costruito, già "
            "pubblicato in fascicolo monografico.",
        "sectors": [
            "residenziale", "pubblico", "interno", "paesaggio",
            "restauro", "concorso", "culturale", "uffici",
            "industriale", "sanitario", "scolastico", "misto-uso",
        ],
        "sectors_trailing":
            "Le opere di restauro e concorso passano per la qualifica "
            "MIBAC e per le procedure di Soprintendenza; le commissioni "
            "pubbliche entrano per gara o per concorso a inviti.",
        "sectors_counter":
            "Numerazione degli interventi pubblicati in collana: dal "
            "2008, <em>novanta</em> fascicoli aperti — quarantasette "
            "opere realizzate e collaudate, ventitré concorsi "
            "consegnati, dieci pubblicazioni di rilievo.",

        # Leadership · LF-2 L6=single-portrait-feature. ONE founding
        # architect masthead (NOT a 3-card grid like Continua's L6 ·
        # NOT typographic-only like Pragma/Fiscus). Mitigation §12
        # Warning 4 binding: portrait MUST read environmental, NOT
        # headshot.
        "leadership_label":   "STUDIO FOUNDER · ARCHITETTA",
        "leadership_heading": "Marta <em>Roveri</em>",
        "leadership_role":    "fondatrice · responsabile editoriale dei fascicoli",
        "leadership_caption": "Lo studio · interno · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Marta Roveri ha aperto Cornice nel 2008, dopo dieci anni "
            "di pratica tra Milano e Bologna in due studi di restauro "
            "pubblico. Si è formata al Politecnico di Milano sotto la "
            "cattedra di restauro architettonico, con un periodo di "
            "ricerca all'École Polytechnique de Lausanne sui caratteri "
            "stereotomici delle volte in pietra. Lavora a tempo pieno "
            "sui progetti dello studio: dirige il rilievo, scrive "
            "l'argomento del fascicolo, segue il cantiere fino al "
            "collaudo, e cura la collana monografica che pubblica le "
            "opere realizzate.",

            "Tra le opere realizzate ricordiamo il restauro della corte "
            "di Palazzo Lignari a Bologna (2019, qualifica MIBAC), il "
            "concorso vinto per la nuova biblioteca civica di "
            "Pietrasanta (2021, in cantiere) e l'edificio residenziale "
            "di via Volpe a Roma (2023, sei alloggi su lotto stretto). "
            "Le sue note critiche — sul rapporto fra cornice e fronte "
            "minore, sulla regola del modulo nei concorsi pubblici — "
            "sono raccolte in due monografie pubblicate dalla collana "
            "dello studio (2018, 2024) e in saggi apparsi su "
            "Casabella, Domus e Il Giornale dell'Architettura.",
        ],
        "leadership_credentials": [
            "Albo OAPPC · Iscritto Ordine degli Architetti di Milano N° 12.847",
            "CNAPPC · Consiglio Nazionale degli Architetti P.P.C.",
            "MIBAC · Qualifica per il restauro architettonico (D.M. 154/2017)",
            "Politecnico di Milano · Professoressa a contratto · Cattedra di Restauro",
        ],
        "leadership_secondary_cta_label": "Lo studio · biografia estesa",
        "leadership_secondary_cta_href":  "studio",

        # Cases magazine-grid · LF-2 L7=magazine-grid · 3+1 layout.
        # 1 hero card (large · 8-col) + 3 small cards (4-col each).
        # Each card carries photo + eyebrow + title + body + pill.
        "cases_label":   "PROGETTI — ARGOMENTI COSTRUITI",
        "cases_intro":
            "Quattro fascicoli aperti, in ordine di pubblicazione. "
            "Sito, committenza, programma, anno, vincolo, e l'argomento "
            "dell'opera.",
        # The 4 cards: 1 hero + 3 small.
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · CONCORSO VINTO · 2021 · PIETRASANTA (LU)",
                "title":    "Biblioteca civica · l'argomento è la <em>geometria</em> del modulo",
                "body":
                    "Concorso a inviti per la nuova biblioteca civica di "
                    "Pietrasanta. Lotto a margine del centro storico, a "
                    "sessanta metri dalla cinta muraria, con vincolo "
                    "paesaggistico e doppia fronte (strada urbana a est, "
                    "parco pubblico a ovest). L'argomento del progetto è "
                    "un modulo di sei metri per nove, ripetuto otto "
                    "volte, che organizza tre aule di lettura, un "
                    "deposito a doppia altezza e un portico continuo "
                    "verso il parco. La pelle in cemento a vista "
                    "racconta la regola, le aperture leggono la luce, "
                    "la cornice del fronte tiene insieme il portato "
                    "civile dell'edificio.",
                "pill":     "Tipologia · concorso / culturale  ·  1.450 mq  ·  5,2 M €",
                "photo":    _CASE_CONCORSO,
                "photo_alt":"Architettura minimalista in cemento · concorso Pietrasanta",
                "slug":     "biblioteca-pietrasanta-concorso",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · OPERA REALIZZATA · 2023 · ROMA (TIBURTINO)",
                "title":    "Via Volpe — sei alloggi sul <em>lotto</em> stretto",
                "body":
                    "Edificio residenziale di sei alloggi su lotto "
                    "urbano di nove metri di fronte e ventotto di "
                    "profondità. L'argomento è la profondità: il fronte "
                    "si chiude, l'interno si apre su una corte cieca "
                    "portata in copertura. Cinque livelli più "
                    "sottotetto, struttura in c.a. e tamponamento in "
                    "laterizio faccia a vista. Pubblicato in fascicolo "
                    "n. 38 della collana.",
                "pill":     "Tipologia · residenziale  ·  720 mq  ·  privato",
                "photo":    _CASE_RESIDENZIALE,
                "photo_alt":"Edifici residenziali contemporanei a Roma · via Volpe",
                "slug":     "via-volpe-roma-residenziale",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · RESTAURO PUBBLICO · 2019 · BOLOGNA (CENTRO)",
                "title":    "Palazzo Lignari — la corte come <em>argomento</em> civile",
                "body":
                    "Restauro della corte interna e del piano nobile di "
                    "Palazzo Lignari, sede di un istituto culturale "
                    "comunale. L'argomento è la corte come spazio "
                    "civico: il portico restaurato torna a essere un "
                    "attraversamento pubblico, le pavimentazioni in "
                    "cotto leggono i tre interventi storici "
                    "stratificati. MIBAC qualifica restauro; "
                    "Soprintendenza Belle Arti di Bologna.",
                "pill":     "Tipologia · restauro / pubblico  ·  980 mq  ·  MIBAC",
                "photo":    _CASE_RESTAURO,
                "photo_alt":"Corte storica bolognese restaurata · Palazzo Lignari",
                "slug":     "palazzo-lignari-bologna-restauro",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · PUBBLICAZIONE · 2024 · SAGGIO IN COLLANA",
                "title":    "La cornice del fronte <em>minore</em> — una nota critica",
                "body":
                    "Saggio illustrato sulla regola della cornice nei "
                    "fronti minori dell'edilizia ottocentesca milanese. "
                    "Centoventiquattro fronti rilevati, ventidue "
                    "cornici tipologiche, otto regole di proporzione "
                    "documentate. La pubblicazione argomenta il valore "
                    "della cornice come dispositivo civile, non "
                    "decorativo. Co-edizione con il Politecnico di "
                    "Milano · DAStU.",
                "pill":     "Tipologia · pubblicazione  ·  124 fronti  ·  DAStU",
                "photo":    _CASE_CORNICE_DETAIL,
                "photo_alt":"Dettaglio di cornice e capitello · saggio in collana 2024",
                "slug":     "cornice-fronte-minore-saggio",
            },
        ],
        "cases_trailing_label": "Tutti i fascicoli aperti · cronologia 2008–2024",
        "cases_trailing_href":  "progetti",

        # CTA closer (LF-2 cream-hairline · NOT dark · LF-2-specific
        # polarity inversion · CS-TONE-03 demoted at family level).
        "cta_label":     "FASCICOLO PROGETTO",
        "cta_intro":
            "Le commissioni cominciano da una sola pagina: il fascicolo progetto.",
        # Voice anchor restated VERBATIM at the closer (copy-authoring §12).
        "cta_heading":
            "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.",
        "cta_form_hint":
            "Brief in italiano · sito · tipologia · cronoprogramma · documenti già "
            "disponibili. Risposta entro cinque giorni lavorativi.",
        "cta_primary":   "Apri un fascicolo progetto",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "Nessuna call di scoperta. Nessun preventivo a consumo. "
            "Solo l'argomento del progetto, e la sua regola.",
        "cta_sub_line":
            "Cornice · studio di architettura · Milano · dal 2008",
    },

    # ─── STUDIO (about) ────────────────────────────────────────
    "studio": {
        "eyebrow":   "LO STUDIO · ARCHIVIO · CV",
        "headline":  "Cornice · studio di architettura editoriale dal <em>2008</em>.",
        "intro":
            "Milano. Un'architetta fondatrice, due collaboratori, "
            "novanta fascicoli aperti. Lavoriamo poco, e per intero.",

        "history_label":   "TAPPE DELLO STUDIO",
        "history_heading": "Cinque date, sedici anni di pratica editoriale.",
        "history_intro":
            "Cinque scelte strutturali dietro le quali si legge il "
            "carattere dello studio — l'autorialità di un architetto "
            "solo, la collana monografica come metodo, il rilievo come "
            "primo gesto di rispetto, la cornice come dispositivo "
            "civile, il restauro qualificato come pratica di lettura.",
        "history": [
            ("2008", "Fondazione",
             "Marta Roveri apre Cornice in via Paoli a Milano, dopo "
             "dieci anni di collaborazione in due studi di restauro "
             "pubblico tra Milano e Bologna. La sede è scelta per "
             "una sola ragione: due locali su una corte interna, uno "
             "per il rilievo, uno per la scrittura."),
            ("2014", "Qualifica MIBAC restauro",
             "Marta Roveri ottiene la qualifica per il restauro "
             "architettonico (D.M. 154/2017). Da quell'anno lo studio "
             "accetta commissioni di restauro su edifici vincolati ex "
             "Codice dei Beni Culturali e cura le pratiche con la "
             "Soprintendenza Belle Arti."),
            ("2017", "Cattedra al Politecnico di Milano",
             "Marta Roveri viene nominata Professoressa a contratto "
             "sulla Cattedra di Restauro al Politecnico di Milano. La "
             "pratica didattica entra nel metodo dello studio: il "
             "rilievo, il contesto e l'argomento si scrivono come tesi."),
            ("2019", "Palazzo Lignari · primo restauro pubblico",
             "Lo studio consegna il restauro della corte e del piano "
             "nobile di Palazzo Lignari a Bologna (sede culturale "
             "comunale · Soprintendenza Belle Arti). Pubblicato in "
             "fascicolo n. 31 della collana monografica."),
            ("2024", "Saggio sulla cornice del fronte minore",
             "Co-edizione con il Politecnico di Milano · DAStU · saggio "
             "illustrato sulla regola della cornice nei fronti minori "
             "dell'edilizia ottocentesca milanese. Pubblicato in "
             "fascicolo n. 47. La collana monografica raggiunge "
             "novanta fascicoli aperti."),
        ],

        "values_label":   "PRINCIPI EDITORIALI",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Sono i quattro principi che separano un fascicolo Cornice "
            "da una commissione standardizzata. Sono scritti nel patto "
            "di mandato firmato in prima riunione, non sul sito.",
        "values": [
            ("01", "Un architetto autoriale",
             "La firma del progetto è quella di un architetto solo, non "
             "di un brand a più mani. La responsabilità autoriale resta "
             "concentrata, perché un argomento per essere riconoscibile "
             "deve avere una voce. Le collaborazioni esterne passano "
             "attraverso lo studio, non lo sostituiscono."),
            ("02", "Il rilievo come primo gesto",
             "Ogni commissione si apre con un rilievo serio. L'opera "
             "che già esiste viene letta come un testo, con i suoi "
             "accenti, i suoi paragrafi, le sue cesure. Niente progetto "
             "prima che il sito sia stato letto integralmente."),
            ("03", "La collana monografica come metodo",
             "Tutte le opere realizzate vengono pubblicate in collana "
             "monografica entro dodici mesi dal collaudo, con la "
             "documentazione di cantiere completa. La collana non è "
             "marketing: è la regola che lasciamo a chi verrà dopo."),
            ("04", "Niente preventivi a consumo",
             "Le parcelle dello studio sono calcolate sulle tariffe "
             "minime CNAPPC per classe e categoria, senza sconti "
             "percentuali. La prima valutazione di una commissione è "
             "gratuita; gli studi preliminari respinti non vengono "
             "fatturati."),
        ],

        "team_label":   "STUDIO E COLLABORATORI",
        "team_heading": "Tre architetti, una sola sede.",
        "team_intro":
            "Lo studio è formato da un'architetta fondatrice e due "
            "collaboratori. Lavoriamo a tempo pieno su tre o quattro "
            "commissioni in parallelo, mai di più. Le pratiche con "
            "Soprintendenza, gli uffici comunali e gli enti appaltanti "
            "vengono trattate in studio, non delegate.",
        "team": [
            {"name": "Marta Roveri",
             "role": "Studio Founder · Architetta",
             "office": "Milano",
             "bio": "Fondatrice. Politecnico di Milano · cattedra di "
                    "restauro architettonico · ricerca all'EPFL Lausanne "
                    "sui caratteri stereotomici delle volte in pietra. "
                    "Albo OAPPC Milano N° 12.847 · CNAPPC · qualifica "
                    "MIBAC restauro. Professore a contratto al "
                    "Politecnico di Milano dal 2017."},
            {"name": "Architetto associato",
             "role": "Architetto associato · Cantiere",
             "office": "Milano",
             "bio": "Architetto associato dal 2018. Politecnico di "
                    "Torino · master in progettazione del paesaggio. "
                    "Albo OAPPC Milano. Si occupa del cantiere e del "
                    "coordinamento delle commesse pubbliche, in "
                    "particolare delle pratiche con Soprintendenza e "
                    "con gli uffici comunali."},
            {"name": "Architetto junior",
             "role": "Architetto junior · Rilievo",
             "office": "Milano",
             "bio": "Architetto junior dal 2022. Politecnico di Milano "
                    "· tesi sulla cornice come dispositivo civile "
                    "(relatrice: Roveri). Albo OAPPC Milano. Si occupa "
                    "del rilievo digitale, del modello, e della "
                    "redazione grafica dei fascicoli. Co-autrice del "
                    "saggio sulla cornice (collana, 2024)."},
        ],

        "coordinates_label": "LA SEDE",
        "coordinates": [
            ("Milano", "via Pasquale Paoli 9 · 20143 · due locali su corte interna"),
            ("Studio", "aperto su appuntamento · martedì-venerdì · 10:00-18:00"),
            ("Cantieri attivi", "Bologna · Pietrasanta · Roma · in corso 2024-2026"),
        ],

        "cta_heading": "Una commissione comincia da una sola pagina.",
        "cta_intro":
            "La prima pagina di ogni commissione è il fascicolo "
            "progetto: una scheda di sintesi che lo studio legge "
            "integralmente, e a cui risponde entro cinque giorni "
            "lavorativi con una nota critica.",
        "cta_primary":   "Apri un fascicolo progetto",
        "cta_primary_href": "contatti",
    },

    # ─── SERVIZI (services) ────────────────────────────────────
    "servizi": {
        "eyebrow":  "SERVIZI · COMMISSIONI · QUALIFICHE",
        "headline": "Quattro modalità di <em>commissione</em>.",
        "intro":
            "Lo studio accetta commissioni dirette, concorsi pubblici, "
            "restauri qualificati MIBAC e pubblicazioni in collana. "
            "Niente pacchetti chiavi in mano.",

        "svc_duration_label": "Cadenza",
        "svc_leader_label":   "Architetto referente",

        "services": [
            {
                "num":   "01",
                "title": "Commissione diretta",
                "blurb":
                    "Famiglie che riscrivono una casa di campagna, "
                    "sviluppatori privati con sensibilità editoriale, "
                    "comunità religiose che riprogrammano un edificio "
                    "dismesso, piccole imprese che costruiscono una "
                    "sede. La commissione diretta è la modalità più "
                    "antica dello studio: il committente porta un sito "
                    "e un programma, lo studio scrive l'argomento e "
                    "accompagna il progetto fino al collaudo.",
                "scope": [
                    "Rilievo iniziale incluso · cinque giorni di campagna",
                    "Fascicolo monografico incluso · pubblicato a collaudo",
                    "Pratiche edilizie e direzione lavori incluse",
                    "Tariffe minime CNAPPC · senza sconti percentuali",
                ],
                "duration": "Da rilievo a collaudo · 18-30 mesi",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "02",
                "title": "Concorso pubblico",
                "blurb":
                    "Lo studio partecipa a concorsi di progettazione "
                    "pubblici (gara aperta, procedura ristretta, "
                    "dialogo competitivo) e a concorsi a inviti banditi "
                    "da Comuni, enti culturali, fondazioni, regioni. La "
                    "nostra firma è quella di un architetto solo — non "
                    "di un consorzio multidisciplinare — perciò "
                    "accettiamo concorsi solo quando l'argomento del "
                    "progetto regge la nostra voce.",
                "scope": [
                    "Ventitré concorsi consegnati dal 2008",
                    "Sei vinti · quattro in shortlist · tredici pubblicati",
                    "Tavole archiviate e disponibili al committente",
                    "Iscrizione CNAPPC verificabile",
                ],
                "duration": "Dipende dal bando · 2-9 mesi",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "03",
                "title": "Restauro qualificato MIBAC",
                "blurb":
                    "Marta Roveri è abilitata al restauro "
                    "architettonico secondo il D.M. 154/2017. Lo "
                    "studio accetta commissioni di restauro su edifici "
                    "vincolati ex Codice dei Beni Culturali (D.lgs. "
                    "42/2004) e su corti, portici, fronti minori, "
                    "edifici ottocenteschi e novecenteschi. Le "
                    "stratigrafie si leggono come testi.",
                "scope": [
                    "Qualifica MIBAC verificabile (D.M. 154/2017)",
                    "Pratiche Soprintendenza curate internamente",
                    "Tre opere di restauro pubblico realizzate",
                    "Pubblicazione integrale in collana monografica",
                ],
                "duration": "24-48 mesi · vincoli inclusi",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "04",
                "title": "Pubblicazione editoriale",
                "blurb":
                    "Lo studio pubblica i propri progetti in collana "
                    "monografica, ma accetta anche commissioni esterne "
                    "di pubblicazione: monografie su fronti minori, "
                    "saggi tipologici, schede critiche per cataloghi di "
                    "mostra, voci per repertori architettonici. Un "
                    "argomento di progetto pubblicato senza essere "
                    "costruito è un argomento che la disciplina può "
                    "riprendere.",
                "scope": [
                    "Saggio illustrato · 80-200 pagine",
                    "Co-edizione con istituzioni accademiche",
                    "Tiratura limitata · 200 copie numerate",
                    "Distribuzione musei + librerie specializzate",
                ],
                "duration": "Da incarico a stampa · 12-18 mesi",
                "leader":   "Marta Roveri",
            },
        ],

        "process_label":   "METODO · QUATTRO STAGIONI",
        "process_heading": "Quattro fasi, una sola sequenza editoriale.",
        "process": [
            ("01", "Rilievo",
             "L'opera che esiste viene letta come un testo. Misure, "
             "materiali, cesure, accenti. Il rilievo è la prima forma "
             "di rispetto e dura tipicamente cinque giorni di campagna."),
            ("02", "Contesto",
             "Committenza, vincoli del PRG, vincoli paesaggistici e "
             "della Soprintendenza, regolamento edilizio, abitudini "
             "del sito. Il contesto è la cornice del progetto."),
            ("03", "Argomento",
             "Il progetto si scrive come una tesi — quale problema "
             "risolve, quale eredità rispetta, quale figura propone. "
             "Cinque righe in cui l'opera deve potersi raccontare."),
            ("04", "Cantiere",
             "Settimana per settimana, sito per sito, fino al collaudo. "
             "Tutto resta scritto nel fascicolo monografico — "
             "pubblicato entro dodici mesi dal collaudo."),
        ],

        "cta_heading":   "Quale modalità fa al caso del vostro progetto?",
        "cta_intro":
            "Se la modalità non è chiara, ci scriva una breve "
            "descrizione del sito e dell'intervento immaginato. Le "
            "indicheremo la modalità giusta entro cinque giorni "
            "lavorativi — anche se non apriamo fascicolo.",
        "cta_primary":   "Apri un fascicolo progetto",
        "cta_primary_href": "contatti",
    },

    # ─── PROGETTI (case_study_list) ────────────────────────────
    "progetti": {
        "eyebrow":  "PROGETTI · FASCICOLI APERTI · 2008-2024",
        "headline": "Quaranta argomenti <em>costruiti</em>.",
        "intro":
            "Quarantasette opere realizzate, ventitré concorsi "
            "consegnati, dieci pubblicazioni di rilievo. Tutti i "
            "fascicoli sono in collana monografica.",

        "cases_label": "Quattro fascicoli rappresentativi · in dettaglio",
        "cases_intro":
            "Per ogni fascicolo aperto qui pubblichiamo la pagina di "
            "argomento — sito, committenza, programma, cronologia, "
            "vincolo, e l'argomento del progetto in cinque righe.",

        "cta_heading":   "Un argomento simile al vostro?",
        "cta_intro":
            "I fascicoli completi (rilievo, tavole tecniche, "
            "documentazione di cantiere, nota critica conclusiva) sono "
            "disponibili in studio dietro richiesta motivata. La "
            "consultazione è gratuita; il fascicolo stampato si "
            "ottiene a copertura delle spese di stampa.",
        "cta_primary":   "Richiedi un fascicolo in studio",
        "cta_primary_href": "contatti",
    },

    # ─── POSTS · case_study_detail ─────────────────────────────
    "posts": [
        {
            "slug":     "biblioteca-pietrasanta-concorso",
            "title":    "Biblioteca civica · l'argomento è la geometria del modulo",
            "category": "Concorso · culturale",
            "year":     "2021",
            "duration": "Cantiere aperto · collaudo previsto 2026",
            "client_code":
                "Concorso a inviti vinto · Comune di Pietrasanta "
                "(Direzione Cultura) · 1.450 mq · 5,2 M € · vincolo "
                "paesaggistico · doppia fronte (urbana + parco).",
            "lead":
                "Concorso a inviti per la nuova biblioteca civica di "
                "Pietrasanta. L'argomento del progetto è un modulo di "
                "sei metri per nove, ripetuto otto volte, che organizza "
                "tre aule di lettura, un deposito a doppia altezza e un "
                "portico continuo verso il parco pubblico.",
            "sections": [
                {
                    "label": "Il sito",
                    "heading": "Una doppia fronte e un vincolo paesaggistico",
                    "body":
                        "Lotto a margine del centro storico di "
                        "Pietrasanta, a sessanta metri dalla cinta "
                        "muraria, con vincolo paesaggistico ex Codice "
                        "dei Beni Culturali (D.lgs. 42/2004) e doppia "
                        "fronte: strada urbana a est, parco pubblico a "
                        "ovest. Il rilievo si è chiuso con dodici "
                        "settimane di campagna nel 2020, due "
                        "stratigrafie sui muretti perimetrali e una "
                        "campagna fotografica sui contesti adiacenti.",
                },
                {
                    "label": "L'argomento",
                    "heading": "Un modulo che si argomenta, non si vede",
                    "body":
                        "Il modulo di sei metri per nove si ripete "
                        "otto volte secondo una matrice ortogonale. La "
                        "pelle in cemento a vista racconta la regola, "
                        "le aperture leggono la luce solare lungo "
                        "l'arco della giornata, la cornice del fronte "
                        "tiene insieme il portato civile dell'edificio "
                        "verso la strada e l'apertura al parco verso "
                        "ovest. Il modulo non si vede: si argomenta.",
                },
                {
                    "label": "Il cantiere",
                    "heading": "Cantiere aperto novembre 2023",
                    "body":
                        "Cantiere aperto novembre 2023 con "
                        "consegna del progetto esecutivo a maggio "
                        "2023. Direzione lavori dello studio. "
                        "Collaudo previsto giugno 2026, con apertura "
                        "al pubblico settembre 2026 in occasione "
                        "dell'inaugurazione della stagione culturale "
                        "comunale. Il fascicolo monografico verrà "
                        "pubblicato a collaudo (n. 44 della collana).",
                },
            ],
            "kpi": [
                ("1.450 mq", "superficie netta"),
                ("8",        "moduli ripetuti"),
                ("5,2 M €",  "valore d'opera"),
                ("2026",     "collaudo previsto"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architetto + 2 collaboratori · strutturista esterno · DL interna",
            "next_label":   "Fascicolo successivo",
        },
        {
            "slug":     "via-volpe-roma-residenziale",
            "title":    "Via Volpe — sei alloggi sul lotto stretto",
            "category": "Residenziale · privato",
            "year":     "2023",
            "duration": "Realizzato · collaudo giugno 2023",
            "client_code":
                "Edificio residenziale · sei alloggi · committenza "
                "privata · lotto urbano 9×28 m · 720 mq SLP · cinque "
                "livelli + sottotetto · pubblicato in fascicolo n. 38.",
            "lead":
                "Edificio residenziale di sei alloggi su lotto urbano "
                "di nove metri di fronte e ventotto di profondità. "
                "L'argomento è la profondità: il fronte si chiude, "
                "l'interno si apre su una corte cieca portata in "
                "copertura.",
            "sections": [
                {
                    "label": "Il sito",
                    "heading": "Nove metri di fronte, ventotto di profondità",
                    "body":
                        "Lotto residenziale al Tiburtino, Roma, in "
                        "una via di edilizia mista degli anni "
                        "Cinquanta. Vincoli del PRG comunale "
                        "abbastanza permissivi sull'altezza, ma "
                        "stretti sulla profondità di affaccio. La "
                        "committenza chiedeva sei alloggi vendibili, "
                        "garage interrato, area verde condivisa.",
                },
                {
                    "label": "L'argomento",
                    "heading": "La profondità portata in copertura",
                    "body":
                        "L'argomento del progetto risolve il vincolo "
                        "di profondità portando la corte cieca dal "
                        "piano interrato al piano di copertura — un "
                        "patio comune in quota, cinque metri per "
                        "otto, illuminato da lucernario. Il fronte "
                        "su strada si chiude in laterizio faccia a "
                        "vista; gli alloggi ricevono luce dai due "
                        "lati corti e dal patio in copertura.",
                },
                {
                    "label": "Il cantiere",
                    "heading": "Diciannove mesi · cantiere chiuso 2023",
                    "body":
                        "Cantiere aperto ottobre 2021, collaudato "
                        "giugno 2023. Struttura in c.a., tamponamento "
                        "in laterizio faccia a vista, infissi in "
                        "alluminio anodizzato bronzo. Direzione "
                        "lavori dello studio. Il fascicolo n. 38 è "
                        "stato pubblicato in collana a giugno 2024.",
                },
            ],
            "kpi": [
                ("720 mq",   "superficie SLP totale"),
                ("6",        "alloggi · 70-130 mq"),
                ("19 mesi",  "durata cantiere"),
                ("n. 38",    "fascicolo in collana"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architetto + 2 collaboratori · strutturista + DL interna",
            "next_label":   "Fascicolo successivo",
        },
        {
            "slug":     "palazzo-lignari-bologna-restauro",
            "title":    "Palazzo Lignari — la corte come argomento civile",
            "category": "Restauro · pubblico",
            "year":     "2019",
            "duration": "Realizzato · collaudo giugno 2019",
            "client_code":
                "Restauro corte interna + piano nobile · Comune di "
                "Bologna (Settore Cultura) · qualifica MIBAC · "
                "Soprintendenza Belle Arti Bologna · 980 mq · "
                "pubblicato in fascicolo n. 31 della collana (2020).",
            "lead":
                "Restauro della corte interna e del piano nobile di "
                "Palazzo Lignari, sede di un istituto culturale "
                "comunale dedicato alla didattica del patrimonio. "
                "L'argomento è la corte come spazio civico.",
            "sections": [
                {
                    "label": "Il sito",
                    "heading": "Una corte porticata di origine quattrocentesca",
                    "body":
                        "Bologna, centro storico, zona A1. Vincolo ex "
                        "Codice dei Beni Culturali (D.lgs. 42/2004) e "
                        "vincolo Soprintendenza Belle Arti per la "
                        "città metropolitana. Palazzo Lignari è di "
                        "origine quattrocentesca, rimaneggiato nel "
                        "Seicento, nell'Ottocento e nel secondo "
                        "dopoguerra. La corte interna porticata "
                        "conserva due fronti rinascimentali e tre "
                        "stratificazioni storiche distinte.",
                },
                {
                    "label": "L'argomento",
                    "heading": "Il restauro non aggiunge figura, rende leggibile la stratigrafia",
                    "body":
                        "Abbiamo scritto due gesti: il primo, la "
                        "pavimentazione in cotto a listello posato in "
                        "opera secondo tre orditure leggermente "
                        "diverse, una per ciascuna stratificazione "
                        "storica letta nel rilievo; il secondo, "
                        "l'illuminazione integrata nel listello, che "
                        "accende le cesure dopo il tramonto e disegna "
                        "la corte come testo leggibile anche di "
                        "notte. La regola: il restauro rende leggibile "
                        "la stratigrafia che già c'è.",
                },
                {
                    "label": "Il cantiere",
                    "heading": "Trentuno mesi · campagna stratigrafica indipendente",
                    "body":
                        "Cantiere aperto novembre 2016, collaudato "
                        "giugno 2019. Le 31 settimane di campagna "
                        "stratigrafica sulle pavimentazioni hanno "
                        "richiesto la collaborazione di un "
                        "restauratore qualificato e di una squadra di "
                        "posatori specializzati. Le pratiche con la "
                        "Soprintendenza hanno richiesto undici "
                        "sopralluoghi tecnici e tre revisioni del "
                        "progetto esecutivo. Collaudo senza prescrizioni.",
                },
            ],
            "kpi": [
                ("980 mq",   "corte + piano nobile"),
                ("31 mesi",  "durata cantiere"),
                ("n. 31",    "fascicolo in collana 2020"),
                ("MIBAC",    "qualifica restauro"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architetto + 2 collaboratori · restauratore esterno · DL interna",
            "next_label":   "Fascicolo successivo",
        },
        {
            "slug":     "cornice-fronte-minore-saggio",
            "title":    "La cornice del fronte minore — una nota critica",
            "category": "Pubblicazione · saggio",
            "year":     "2024",
            "duration": "Pubblicato · in libreria",
            "client_code":
                "Saggio illustrato · co-edizione Politecnico di Milano "
                "(DAStU) · 124 fronti rilevati · 22 cornici tipologiche "
                "· 8 regole di proporzione · pubblicato in fascicolo "
                "n. 47 della collana (2024) · tiratura 200 copie.",
            "lead":
                "Saggio illustrato sulla regola della cornice nei "
                "fronti minori dell'edilizia ottocentesca milanese. La "
                "pubblicazione argomenta il valore della cornice come "
                "dispositivo civile, non decorativo.",
            "sections": [
                {
                    "label": "Il rilievo",
                    "heading": "Centoventiquattro fronti minori a Milano",
                    "body":
                        "Il rilievo si è chiuso fra il 2021 e il 2023 "
                        "su centoventiquattro fronti minori "
                        "ottocenteschi nei quartieri Brera, Magenta, "
                        "Porta Nuova e Porta Romana. Per ciascun "
                        "fronte: rilievo grafico in scala 1:50, "
                        "campagna fotografica in luce diurna e "
                        "radente, schedatura tipologica della "
                        "cornice e dei suoi rapporti con il fronte.",
                },
                {
                    "label": "L'argomento",
                    "heading": "La cornice come dispositivo civile",
                    "body":
                        "La cornice del fronte minore non è un "
                        "ornamento: è il dispositivo civile che tiene "
                        "insieme la facciata dell'edificio con la "
                        "cortina della via. È la regola che permette "
                        "a fronti diversi di stare in conversazione. "
                        "Il saggio argomenta otto regole di "
                        "proporzione documentabili e venti tipologie "
                        "ricorrenti, e propone una linea-guida "
                        "operativa per il restauro contemporaneo.",
                },
                {
                    "label": "La pubblicazione",
                    "heading": "Co-edizione Politecnico DAStU · 200 copie",
                    "body":
                        "Pubblicazione in co-edizione con il "
                        "Politecnico di Milano · DAStU. Formato "
                        "24×33 cm, 192 pagine, copertina in carta "
                        "uso mano, stampa offset a quattro colori, "
                        "tiratura limitata a 200 copie numerate. "
                        "Distribuzione: librerie specializzate · "
                        "biblioteche del Politecnico · Triennale di "
                        "Milano · MAXXI Architettura.",
                },
            ],
            "kpi": [
                ("124",      "fronti rilevati"),
                ("22",       "cornici tipologiche"),
                ("192",      "pagine illustrate"),
                ("200",      "copie numerate"),
            ],
            "lead_partner": "Marta Roveri · Studio Founder",
            "team":         "Architetto + 2 collaboratori · co-edizione DAStU",
            "next_label":   "Fascicolo successivo",
        },
    ],

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "APRI UN FASCICOLO PROGETTO",
        "headline": "La commissione comincia da una <em>pagina</em>.",
        "intro":
            "Brief in italiano. Sito · tipologia · cronoprogramma · "
            "documenti già disponibili. Risposta entro cinque giorni "
            "lavorativi.",

        "form_label":   "FASCICOLO PROGETTO",
        "form_heading": "Compila il fascicolo iniziale",
        "form_intro":
            "Lo studio accetta tre o quattro nuove commissioni l'anno. "
            "La prima pagina di ogni commissione è il fascicolo "
            "progetto: lo studio lo legge integralmente, e a cui "
            "risponde entro cinque giorni lavorativi con una nota "
            "critica. La nota critica è gratuita ed è la forma con "
            "cui dichiariamo se la commissione è in linea con la "
            "collana.",

        # Form fields per planner-brief §9 · 4 architecture-vocabulary
        # fields. NO P.IVA + CF (Fiscus collision avoided).
        "form_fields": [
            {"name": "name",      "label": "Nome",     "type": "text", "required": True,
             "placeholder": "Es. Anna",
             "helper": "Solo il nome di battesimo, grazie."},
            {"name": "surname",   "label": "Cognome",  "type": "text", "required": True,
             "placeholder": "Es. Bianchi",
             "helper": "Come compare nei documenti del committente."},
            {"name": "email",     "label": "Email",    "type": "email", "required": True,
             "placeholder": "anna@dominio.it",
             "helper": "Una casella che riceve la nota critica fiduciaria."},
            {"name": "phone",     "label": "Telefono", "type": "tel", "required": False,
             "placeholder": "+39 ...",
             "helper": "Linea diretta per il primo contatto. Facoltativo."},
            {"name": "tipologia", "label": "Tipologia di intervento", "type": "select", "required": True,
             "options": [
                 "residenziale",
                 "pubblico",
                 "interno",
                 "paesaggio",
                 "restauro",
                 "concorso",
                 "culturale",
                 "uffici",
                 "industriale",
                 "sanitario",
                 "scolastico",
                 "misto-uso",
             ],
             "helper": "La tipologia dell'intervento immaginato."},
            {"name": "cronoprogramma", "label": "Cronoprogramma desiderato", "type": "select", "required": True,
             "options": [
                 "Meno di 12 mesi",
                 "Tra 12 e 24 mesi",
                 "Tra 24 e 36 mesi",
                 "Oltre 36 mesi",
             ],
             "helper": "L'orizzonte temporale concordato con la committenza."},
            {"name": "documenti", "label": "Documenti già disponibili", "type": "select", "required": False,
             "options": [
                 "Rilievo · planimetria",
                 "Vincoli · PRG · Soprintendenza",
                 "Regolamento edilizio · bandi",
                 "Concept iniziale",
                 "Altro",
                 "Nessuno (cominciamo dal rilievo)",
             ],
             "helper": "I documenti già disponibili al committente. Facoltativo."},
            {"name": "sito", "label": "Il sito · l'intervento · la committenza",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Massimo 800 caratteri. Ci dica brevemente la "
                 "localizzazione (Comune · provincia), la tipologia "
                 "dell'intervento e da quale committenza proviene la "
                 "richiesta. Una sola voce — non occorre essere "
                 "completi.",
             "helper":
                 "Quanto basta a capire se il sito merita un rilievo. "
                 "Le cifre e gli altri dati si discutono in prima "
                 "riunione, mai per iscritto in fase di primo contatto."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che firmerà la committenza in prima riunione.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Argomento di progetto",
             "meta": "Tipologia · cronoprogramma · documenti già disponibili.",
             "fields": ["tipologia", "cronoprogramma", "documenti"]},
            {"num": "03", "title": "Il sito",
             "meta": "Il sito è il primo testo del progetto. Quattrocento parole bastano.",
             "fields": ["sito"]},
        ],

        "form_submit_label": "Apri il fascicolo",
        "form_submit_note":
            "Lo studio leggerà il fascicolo entro cinque giorni "
            "lavorativi e risponderà con una nota critica all'indirizzo "
            "indicato. Nessun BDR esterno, nessuna automazione di "
            "sequence — il primo contatto è con l'architetto.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi "
            "del Reg. UE 679/2016 e del D.lgs. 196/2003. I dati sono "
            "custoditi presso lo studio di via Paoli con accesso "
            "limitato ai tre architetti. Sono informato del canale "
            "whistleblowing (D.lgs. 24/2023) attivo presso lo studio.",

        "office_address_label": "Indirizzo",
        "office_area_label":    "Zona",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",

        "offices_label":   "LA SEDE",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Sede unica",
                "address": "via Pasquale Paoli 9 · 20143",
                "area":    "Sant'Agostino · vicino Bocconi",
                "phone":   "+39 02 6610 4708",
                "email":   "fascicolo@cornice-architettura.it",
            },
        ],

        "channels_label": "CANALI DIRETTI",
        "channels": [
            ("Segreteria di studio",                "+39 02 6610 4708",                 "Mar – Ven · 10:00 – 18:00"),
            ("Email fiduciaria",                    "fascicolo@cornice-architettura.it","Risposta entro 5 giorni"),
            ("Whistleblowing (D.lgs. 24/2023)",     "whistleblowing@cornice-architettura.it", "Canale interno · cifrato"),
        ],

        "footnote":
            "Cornice non risponde a richieste anonime e non rilascia "
            "pareri preliminari per iscritto senza un primo dialogo. "
            "Le informazioni sui compensi sono illustrate in prima "
            "riunione, secondo le tariffe minime CNAPPC. Il canale "
            "whistleblowing è gestito ai sensi del D.lgs. 24/2023 ed "
            "è accessibile a committenze pubbliche, fornitori di "
            "cantiere e collaboratori esterni.",
    },
}
