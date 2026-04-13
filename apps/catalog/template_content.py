"""Per-template inner-page content registry — full multi-page templates.

Where DNA (`template_dna.py`) defines a template's *visual* identity, this
file defines its *editorial* identity: every page of the actual website,
with realistic Italian content. Two templates that share an archetype can
have completely different content and still re-use the same visual chrome.

Why a Python registry, not a model?
-----------------------------------
- Content for full multi-page templates is structured (lists of doctors,
  courses, blog posts, opening hours), not flat JSON, so it benefits from
  Python's tuple/dict ergonomics during authoring.
- It's reviewed in code alongside the templates that consume it.
- It's intentionally scoped to *seed* content for the pilot phase. A future
  iteration will promote it to a real `TemplatePage` model so customers
  can edit it through the editor app — at that point this file becomes
  the seed source for `seed_template_content.py`.

Conventions
-----------
- Top-level keys are `WebTemplate.slug`.
- Each template entry is `{locale: <content_block>}`, with `it` as the
  authoritative source. Templates that are IT-only still carry the
  `{"it": ...}` wrap so the helper API is uniform.
- Each content block has:
    - `pages`     : list of {slug, label, kind} dicts that drive the nav
                    bar in the live preview. `kind` selects the inner-page
                    template file. `slug` and `kind` are stable across
                    locales — only `label` changes.
    - `home`      : content block for the homepage
    - `<page-slug>`: content block for any other inner page
    - `posts`     : (optional) list of {slug, title, ...} for the blog
                    listing + detail pages
- Templates without an entry here have no `live_template` URL space.

i18n pilot (Session 23 — Phase 2i.1)
------------------------------------
The cardio-studio-specialistico template is the first live template to
ship with 5-locale content (it / en / fr / es / ar). Its full locale-keyed
block lives in `template_content_cardio_i18n.py` and is imported here.
Dermatologia-elite-roma is the second template to ship 5-locale content
(it/en/fr/es/ar) as of Session 24 (Phase 2i.2). Its non-IT blocks live
in `template_content_dermatologia_i18n.py`. Gusto remains IT-only — its
dict is wrapped under `{"it": ...}` to keep the helper API uniform. Any
template without an entry for the requested locale automatically falls
back to `it` via `template_i18n.pick_localized`.

Adding a new template
---------------------
1. Add the template to `template_dna.py`.
2. Decide whether it re-uses an existing archetype skin or needs a new one.
3. Add an entry below with `pages` and one block per page slug, wrapped
   under `{"it": ...}` at minimum.
4. If new archetype: add `templates/live_templates/<category>/<archetype>/`.
5. Otherwise: just author the content — existing chrome handles it.
6. For multilingual rollout, add locale keys next to `it` and author the
   content per locale. Missing locales fall back to IT at render time.
"""
from __future__ import annotations

from typing import Any

from apps.catalog import template_i18n


# ---------------------------------------------------------------------------
# CARDIO — Studio Marani Cardiologia (specialist archetype)
# Editorial, prestigious, very-airy, cream + charcoal + accent red
#
# NOTE (Session 23, Phase 2i.1): the full 5-locale content block for cardio
# lives in `template_content_cardio_i18n.py`. This IT entry is kept inline
# because it is the authoritative source and benefits from being reviewed
# alongside Dermatologia + Gusto. The non-IT locale blocks (EN/FR/ES/AR)
# are isolated in the sister file so the pilot's size growth doesn't
# double-review this file. The two are zipped together at the bottom
# registry level.
# ---------------------------------------------------------------------------

CARDIO_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Studio",         "kind": "home"},
        {"slug": "studio",          "label": "Lo Studio",      "kind": "about"},
        {"slug": "visite",          "label": "Visite",         "kind": "services"},
        {"slug": "medici",          "label": "Medici",         "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Pubblicazioni",  "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contatti",       "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Richiedi visita","kind": "appointment"},
    ],

    # Site-wide chrome data (used by _base.html nav + footer)
    "site": {
        "logo_initial": "M",
        "logo_word":    "Studio Marani",
        "tag":          "Cardiologia clinica · Roma Parioli",
        "phone":        "+39 06 320 1144",
        "email":        "studio@maranicardiologia.it",
        "address":      "Viale Parioli 142 · 00197 Roma",
        "hours_compact": "Lun – Ven · 9:00 – 19:00",
        "hours_footer_rows": [
            "Sabato · solo reperibilità",
            "Domenica · chiuso",
        ],
        "license":      "Iscrizione OMCeO Roma 12 / 4408",
        "footer_intro":
            "Studio specialistico privato di cardiologia clinica e prevenzione "
            "cardiovascolare. Riceviamo solo su appuntamento.",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Cardiologia clinica · Roma Parioli",
        "headline": "Una cardiologia <em>su misura</em>, per chi non accetta scorciatoie.",
        "intro":
            "Visite specialistiche, secondi pareri, programmi di prevenzione "
            "individuale. Una sola agenda, un solo medico, una sola firma.",
        "primary_cta":   "Richiedi visita privata",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Lo studio",
        "secondary_href":"studio",

        "facts": [
            ("15", "anni di pratica clinica privata"),
            ("1.200", "visite specialistiche / anno"),
            ("4", "ospedali di riferimento a Roma"),
        ],

        "manifesto_drop_cap": "L",
        "manifesto":
            "a cardiologia non è una catena di montaggio. È un dialogo lungo, "
            "fatto di tempo, di anamnesi paziente, di esami letti due volte. "
            "Lo Studio Marani da quindici anni accompagna pazienti pubblici e "
            "privati in un percorso di prevenzione cardiovascolare costruito "
            "su misura — con discrezione e con metodo.",

        "signature_visits": [
            ("01", "Visita cardiologica completa",
             "Anamnesi estesa, ECG, refertazione e piano di follow-up con timeline personalizzata."),
            ("02", "Secondo parere specialistico",
             "Per pazienti con diagnosi complesse o terapie multiple già in corso, "
             "letta dossier alla mano insieme al medico curante."),
            ("03", "Programma di prevenzione",
             "Sei mesi di monitoraggio integrato con dietologo e medico dello sport, "
             "indicato per famiglie con storia familiare di eventi cardiovascolari."),
            ("04", "Holter & ecocardiografia",
             "Registrazione cardiaca delle 24 ore e ecocardiogramma transtoracico "
             "refertati in giornata, in studio."),
        ],

        "chief": {
            "name":  "Dr. Riccardo Marani",
            "role":  "Direttore clinico · Cardiologo",
            "bio":
                "Specialista in cardiologia formatosi all'Università La Sapienza di Roma "
                "e perfezionato all'Institut de Cardiologie de Montréal. "
                "Membro della Società Italiana di Cardiologia e dell'European Society of Cardiology. "
                "Autore di oltre 40 pubblicazioni indicizzate.",
            "portrait":
                "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d"
                "?auto=format&fit=crop&w=900&q=80",
        },

        "press": ["LANCET", "European Heart Journal", "Corriere Salute",
                  "Sole 24 Ore", "RAI Med"],
        "press_label": "Pubblicato su",

        # Hero right sidebar (the dark pulse column next to the headline)
        "hero_sidebar_top_label": "Direzione clinica",
        "hero_sidebar_quote":
            "«La cardiologia non è una catena di montaggio. "
            "È un dialogo lungo, fatto di tempo.»",
        "hero_sidebar_author": "— Lancet · 2024",
        "hero_sidebar_pulse": [
            ("Studio",      "Roma · Parioli"),
            ("Da",          "2010"),
            ("Riferimento", "Cardiologia clinica"),
        ],

        # Signature-visits section (the dark 01/02/03/04 field grid)
        "signature_visits_label":   "Visite & percorsi",
        "signature_visits_heading": "Sei percorsi clinici, <em>una sola firma.</em>",
        "signature_visits_intro":
            "Quattro fra le visite più richieste dello studio. "
            "L'elenco completo è nella pagina Visite.",

        # Chief-doctor section
        "chief_label":   "Direzione clinica",
        "chief_heading": "Una sola firma <em>per ogni cartella.</em>",

        # Technology / equipment section (Cardio-only — Derm uses gallery_strip)
        "tecnologie": {
            "label": "Tecnologie & strumentazione",
            "heading": "Diagnostica di <em>ultimo livello</em>, in studio.",
            "items": [
                {
                    "icon": "ecg",
                    "title": "ECG a 12 derivazioni",
                    "desc": "Elettrocardiogramma a riposo con refertazione immediata e confronto storico.",
                },
                {
                    "icon": "echo",
                    "title": "Ecocardiografia Philips EPIQ 7",
                    "desc": "Ecografia cardiaca 2D e color-Doppler di ultima generazione, refertata in giornata.",
                },
                {
                    "icon": "holter",
                    "title": "Holter Schiller MT-200",
                    "desc": "Registrazione ECG delle 24 ore con analisi di variabilità e aritmie silenti.",
                },
                {
                    "icon": "stress",
                    "title": "Test ergometrico",
                    "desc": "Test da sforzo su cicloergometro con monitoraggio continuo della pressione arteriosa.",
                },
            ],
        },

        # Patient testimonial (different voice for Cardio vs Derm)
        "testimonianza": {
            "quote":
                "Ho cercato per due anni un cardiologo che leggesse davvero la mia "
                "cartella prima di visitarmi. Allo Studio Marani hanno passato "
                "quaranta minuti sui miei esami prima ancora di toccare lo stetoscopio.",
            "author": "Paziente dello studio",
            "context": "Seconda opinione cardiologica · 2025",
        },

        # FAQ accordion (clinical cardio questions)
        "faq": {
            "label": "Domande frequenti",
            "heading": "Le domande che <em>ci rivolgete più spesso.</em>",
            "items": [
                ("Quanto dura una prima visita cardiologica?",
                 "Una prima visita completa dura circa quarantacinque minuti e include "
                 "anamnesi, esame obiettivo, ECG a 12 derivazioni, refertazione e "
                 "discussione del piano di follow-up. Non accettiamo visite di meno "
                 "di trenta minuti, nemmeno per i controlli."),
                ("Serve la richiesta del medico di base?",
                 "No. Essendo uno studio specialistico privato, non è necessaria "
                 "l'impegnativa del medico curante. È utile, ma non obbligatoria, "
                 "una lettera del medico di base con la storia clinica recente."),
                ("Posso portare esami di un altro ospedale?",
                 "Assolutamente sì. Il secondo parere è una delle nostre specialità. "
                 "Portateci tutti i referti, le lettere di dimissione e le terapie in "
                 "corso — li leggeremo insieme, pagina per pagina."),
                ("L'ecocardiogramma è doloroso?",
                 "No, è un esame completamente indolore e non invasivo. La sonda "
                 "viene appoggiata sul torace con un gel conduttore. L'esame dura "
                 "circa venti-trenta minuti."),
                ("Come funziona il programma di prevenzione?",
                 "Il programma semestrale include quattro visite cadenzate, due "
                 "ECG, un Holter delle 24 ore, una valutazione integrata con "
                 "dietologo e medico dello sport, e un canale diretto con il "
                 "medico dello studio per le urgenze."),
            ],
        },

        # Bottom CTA band
        "cta_heading":
            "Ogni visita è <em>concordata personalmente</em> con il medico.",
        "cta_primary_label":   "Richiedi visita privata",
        "cta_secondary_label": "Contatti dello studio",

        # Anchor subnav (dense home scaffold)
        "anchor_nav": [
            ("metodo",        "Metodo"),
            ("visite",        "Visite"),
            ("percorso",      "Percorso paziente"),
            ("tecnologie",    "Tecnologie"),
            ("medico",        "Direzione clinica"),
            ("studio",        "Sede & contatti"),
        ],

        # Patient journey / timeline (clinical reassurance)
        "percorso": {
            "label":   "Percorso paziente",
            "heading": "Cosa aspettarsi dalla <em>prima visita.</em>",
            "intro":
                "Una visita cardiologica allo Studio Marani segue sempre lo "
                "stesso protocollo: cinque tappe in quarantacinque minuti, "
                "senza fretta e senza scorciatoie.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Arrivo & accoglienza",
                    "desc": "La segreteria raccoglie i documenti, la cartella "
                            "precedente e consegna la scheda anamnestica. "
                            "Tempo medio in sala d'attesa: 4 minuti.",
                    "duration": "5 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Anamnesi approfondita",
                    "desc": "Lettura della cartella, storia familiare, "
                            "terapie in corso e stile di vita. Annotazione "
                            "personale del medico, non un questionario.",
                    "duration": "15 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Esame obiettivo + ECG",
                    "desc": "Auscultazione, misurazione pressoria su entrambi "
                            "gli arti, elettrocardiogramma a 12 derivazioni "
                            "con refertazione immediata.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Diagnostica mirata",
                    "desc": "Se indicato, ecocardiografia in studio o "
                            "programmazione di Holter / test ergometrico. "
                            "Mai esami di routine inutili.",
                    "duration": "Variabile",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Piano clinico scritto",
                    "desc": "Refertazione firmata in carta riciclata, timeline "
                            "dei controlli, canale diretto del medico per "
                            "domande successive.",
                    "duration": "10 min",
                },
            ],
        },

        # Insurance / trust strip — detraibilità, convenzioni, refertazione
        "insurance": {
            "label": "Garanzie & trasparenza",
            "items": [
                ("19%", "Detraibilità come spesa sanitaria",
                 "Fattura emessa in giornata con tracciabilità completa."),
                ("48h", "Tempi di refertazione",
                 "Holter ed ecocardiogramma consegnati entro 48 ore lavorative."),
                ("4", "Ospedali di riferimento",
                 "Rete di consulto con Policlinico Umberto I, Gemelli, "
                 "San Raffaele, Santo Spirito."),
                ("10 anni", "Archivio clinico tracciato",
                 "Cartella accessibile al paziente per dieci anni, copia "
                 "richiedibile in qualsiasi momento."),
            ],
        },

        # Location / sede — address, transport, accessibility
        "location": {
            "label":   "Sede dello studio",
            "heading": "Viale Parioli 142, <em>Roma.</em>",
            "intro":
                "Lo studio occupa il piano nobile di un edificio storico "
                "dei Parioli. Ingresso indipendente, sala d'attesa riservata "
                "e ambulatorio con diagnostica in loco.",
            "map_image":
                "https://api.mapbox.com/styles/v1/mapbox/light-v11/static/"
                "pin-l+9c2a2a(12.490,41.920)/12.490,41.920,14,0/"
                "800x560@2x?access_token=pk.eyJ1IjoibWFya2V0d2ViIiwiYSI6IlExIn0.x",
            "map_fallback_image":
                "https://images.unsplash.com/photo-1531572753322-ad063cecc140"
                "?auto=format&fit=crop&w=1200&q=80",
            "details": [
                ("Indirizzo",
                 "Viale Parioli 142\n00197 Roma"),
                ("Metropolitana",
                 "Linea A fermata Flaminio\n8 minuti a piedi"),
                ("Parcheggio",
                 "Parcheggio riservato convenzionato\nin Via Panama, 50 metri"),
                ("Accessibilità",
                 "Ingresso accessibile a sedie a rotelle\nAscensore diretto al piano"),
            ],
            "hours_short": [
                ("Lun – Ven", "9:00 – 19:00"),
                ("Sabato",    "Solo reperibilità"),
                ("Domenica",  "Chiuso"),
            ],
            "cta_label": "Ottieni indicazioni stradali",
            "cta_href":  "contatti",
        },
    },

    # ─── LO STUDIO (about) ─────────────────────────────────────
    "studio": {
        "eyebrow":  "Lo studio",
        "headline": "Quindici anni di <em>cardiologia clinica</em> indipendente.",
        "intro":
            "Lo Studio Marani nasce nel 2010 dall'idea di restituire alla "
            "cardiologia la sua dimensione di tempo lungo: visite di "
            "quarantacinque minuti, refertazione personale, follow-up "
            "telefonico diretto del medico.",

        "history": [
            ("2010",
             "Apertura del primo studio in Viale Parioli, due stanze e una segretaria. "
             "Le prime quindici cartelle cliniche sono ancora archiviate in originale."),
            ("2014",
             "Convenzione con il Policlinico Umberto I per i casi che richiedono "
             "ricovero o procedure interventistiche di secondo livello."),
            ("2017",
             "Acquisizione di un ecocardiografo Philips EPIQ 7 di ultima generazione "
             "e di un sistema Holter Schiller MT-200 per la diagnostica in giornata."),
            ("2020",
             "Allestimento di un secondo ambulatorio dedicato ai secondi pareri "
             "su dossier multidisciplinari, con accesso a teleconsulto europeo."),
            ("2024",
             "Ingresso della Dr.ssa Salieri come responsabile del programma "
             "di prevenzione cardiovascolare familiare."),
        ],

        "studio_image":
            "https://images.unsplash.com/photo-1631815587646-b85a1bb027e1"
            "?auto=format&fit=crop&w=1400&q=80",
        "studio_image_caption": "Ambulatorio di cardiologia · Viale Parioli, Roma",

        "method_title": "Metodo",
        "method_paragraphs": [
            "Una visita allo Studio Marani inizia sempre dalla cartella che il "
            "paziente porta con sé. Esami precedenti, lettere di dimissione, "
            "referti di medico curante, terapie attive. Tutto viene letto, "
            "annotato e discusso prima di toccare lo stetoscopio.",
            "L'anamnesi dura il tempo che serve: in media trentacinque minuti. "
            "Ne discende un piano clinico scritto, consegnato in mano al paziente "
            "in una cartellina di carta riciclata, con la firma del medico "
            "e la timeline dei controlli successivi.",
            "Ogni cartella resta accessibile al paziente per dieci anni e può "
            "essere richiesta in copia in qualsiasi momento, anche per il "
            "trasferimento ad altri specialisti.",
        ],

        "values": [
            ("Tempo",       "Quarantacinque minuti per ogni prima visita, mai meno."),
            ("Indipendenza","Nessuna affiliazione a case farmaceutiche o cliniche convenzionate."),
            ("Tracciabilità","Cartella clinica completa, ricostruibile in ogni momento."),
            ("Discrezione", "Riservatezza assoluta sui dati e sulle persone."),
        ],

        # Values section label + heading
        "values_label":   "Cosa garantiamo",
        "values_heading": "Quattro impegni che <em>non cambiano mai.</em>",

        # Bottom CTA band
        "cta_heading":
            "Vuoi conoscere i medici dello studio <em>prima di prenotare?</em>",
        "cta_primary_label":   "I tre medici dello studio →",
        "cta_secondary_label": "Richiedi visita privata →",
    },

    # ─── VISITE (services) ─────────────────────────────────────
    "visite": {
        "eyebrow":  "Le visite",
        "headline": "Sei percorsi clinici, <em>una sola firma.</em>",
        "intro":
            "Ogni visita allo Studio Marani è un percorso clinico definito, "
            "con una durata, un costo e un piano di follow-up scritti.",

        "service_image":
            "https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe"
            "?auto=format&fit=crop&w=1400&q=80",
        "service_image_caption": "Diagnostica strumentale · Studio Marani",

        "treatments": [
            ("Visita cardiologica completa",
             "45 min · prima visita",
             "Anamnesi estesa, esame obiettivo, elettrocardiogramma a 12 derivazioni, "
             "refertazione personale e piano di follow-up scritto.",
             "€ 220"),
            ("Visita di controllo",
             "30 min · pazienti già seguiti",
             "Aggiornamento terapia, ECG di controllo, lettura esami "
             "ematochimici recenti.",
             "€ 140"),
            ("Secondo parere specialistico",
             "60 min · su dossier",
             "Lettura completa di referti, esami strumentali e cartella clinica "
             "esistente, con relazione finale firmata e bibliografia di riferimento.",
             "€ 280"),
            ("Ecocardiografia transtoracica",
             "30 min · in studio",
             "Esame ecocardiografico bidimensionale e color-Doppler con sistema "
             "Philips EPIQ 7. Refertazione in giornata.",
             "€ 180"),
            ("Holter cardiaco 24h",
             "Registrazione + lettura",
             "Monitoraggio elettrocardiografico delle 24 ore con sistema "
             "Schiller MT-200, lettura e refertazione personale.",
             "€ 160"),
            ("Programma prevenzione 6 mesi",
             "Percorso annuale",
             "Quattro visite cadenzate, due ECG, un Holter, valutazione integrata "
             "con dietologo e medico dello sport, accesso al canale diretto del medico.",
             "€ 980"),
        ],

        "footnote":
            "Tutti i pagamenti sono detraibili come spese sanitarie. Lo studio "
            "rilascia ricevuta sanitaria con apposita marca da bollo. Per i "
            "pazienti residenti fuori Roma è possibile concordare un pacchetto "
            "che includa la teleconsultazione di follow-up.",

        "footnote_heading": "Note amministrative",

        # Bottom CTA band
        "cta_heading":
            "Una visita allo Studio Marani è <em>concordata personalmente</em>.",
        "cta_primary_label":   "Modulo di richiesta →",
        "cta_secondary_label": "Numero diretto della segreteria →",
    },

    # ─── MEDICI (team) ─────────────────────────────────────────
    "medici": {
        "eyebrow":  "I medici",
        "headline": "Tre firme, una sola <em>cartella clinica.</em>",
        "intro":
            "Lo studio è composto da tre cardiologi che condividono cartelle, "
            "metodi e standard di refertazione. Ogni paziente, però, ha sempre "
            "un solo medico di riferimento.",

        "portrait_city": "Roma · Parioli",

        "doctors": [
            {
                "name":  "Dr. Riccardo Marani",
                "role":  "Direttore clinico · Cardiologo",
                "tags":  ["Prevenzione cardiovascolare", "Secondi pareri", "Cardiologia clinica"],
                "bio":
                    "Specialista in cardiologia all'Università La Sapienza di Roma, "
                    "perfezionato in ecocardiografia clinica all'Institut de Cardiologie "
                    "de Montréal. Membro SIC e ESC. Autore di oltre quaranta pubblicazioni "
                    "indicizzate, fra cui due capitoli del trattato Braunwald-Italia.",
                "portrait":
                    "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d"
                    "?auto=format&fit=crop&w=900&q=80",
                "links": [
                    ("PubMed", "#"),
                    ("ORCID",  "#"),
                ],
            },
            {
                "name":  "Dr.ssa Margherita Salieri",
                "role":  "Cardiologa · Responsabile prevenzione",
                "tags":  ["Programma prevenzione", "Cardiologia familiare", "Riabilitazione"],
                "bio":
                    "Laureata a Bologna, dottorato di ricerca in fisiologia cardiovascolare "
                    "a Padova. Coordinatrice del programma di prevenzione cardiovascolare "
                    "familiare dello Studio Marani dal 2024. Si occupa in particolare di "
                    "donne in età perimenopausale e di nuclei familiari con storia di eventi precoci.",
                "portrait":
                    "https://images.unsplash.com/photo-1559839734-2b71ea197ec2"
                    "?auto=format&fit=crop&w=900&q=80",
                "links": [
                    ("Curriculum", "#"),
                ],
            },
            {
                "name":  "Dr. Andrea Lombardi",
                "role":  "Cardiologo · Diagnostica strumentale",
                "tags":  ["Ecocardiografia", "Holter", "Sport e cuore"],
                "bio":
                    "Specialista al Sant'Andrea di Roma, formato in ecocardiografia "
                    "avanzata al Saint-Joseph di Parigi. Dal 2018 referente per la "
                    "diagnostica strumentale dello studio. Consulente cardiologico "
                    "per due società sportive di Serie B.",
                "portrait":
                    "https://images.unsplash.com/photo-1612531385446-f7e6d131e1d0"
                    "?auto=format&fit=crop&w=900&q=80",
                "links": [
                    ("Pubblicazioni", "#"),
                ],
            },
        ],
    },

    # ─── PUBBLICAZIONI (blog list / detail) ────────────────────
    "pubblicazioni": {
        "eyebrow":  "Pubblicazioni & approfondimenti",
        "headline": "Lavori scientifici, <em>letture critiche</em>, divulgazione clinica.",
        "intro":
            "Una selezione delle pubblicazioni dello studio e dei testi divulgativi "
            "scritti per il pubblico generale. Tutti i contenuti sono rivisti "
            "personalmente dal Dr. Marani prima della pubblicazione.",

        # Lead post background image (blog_list hero)
        "lead_image":
            "https://images.unsplash.com/photo-1576091160550-2173dba999ef"
            "?auto=format&fit=crop&w=900&q=80",

        # Blog-detail footer strap + fallback body
        "footer_strap": "Studio Marani · Cardiologia clinica",
        "empty_body_fallback_paragraphs": [
            "Articolo in preparazione editoriale. La pubblicazione integrale sarà "
            "disponibile a breve.",
            "Questo segnaposto descrive la voce dell'articolo: una nota clinica "
            "scritta dal medico, in tono diretto e privo di tecnicismi, pensata "
            "per pazienti e familiari che cercano informazioni affidabili.",
        ],
    },

    "posts": [
        {
            "slug":     "secondo-parere-quando-richiederlo",
            "kicker":   "Pratica clinica",
            "title":    "Quando ha senso chiedere un secondo parere cardiologico",
            "date":     "12 marzo 2026",
            "read_min": 6,
            "author":   "Dr. Riccardo Marani",
            "lede":
                "Non è una sfiducia verso il primo medico. È un atto di igiene clinica "
                "che — quando fatto bene — protegge il paziente, il medico curante "
                "e il sistema sanitario.",
            "body": [
                ("p", "Ogni anno lo Studio riceve circa duecento richieste di secondo parere. "
                      "Quasi sempre arrivano da pazienti spaventati: una diagnosi inattesa, "
                      "una terapia complessa, un consiglio di intervento chirurgico. "
                      "Il primo lavoro che facciamo è abbassare la temperatura emotiva."),
                ("h2", "Tre situazioni in cui il secondo parere è indicato"),
                ("ol", [
                    "Diagnosi nuova e ad alto impatto, ricevuta in poche ore o in pronto soccorso.",
                    "Terapia farmacologica a lungo termine con effetti collaterali rilevanti.",
                    "Indicazione a procedura invasiva (impianto di pacemaker, cardioversione, ablazione)."
                ]),
                ("p", "In tutti gli altri casi — un semplice controllo annuale, "
                      "una variazione minore di pressione, un episodio isolato di palpitazioni — "
                      "è quasi sempre sufficiente parlare a fondo con il proprio cardiologo."),
                ("h2", "Cosa portare a un secondo parere"),
                ("p", "Un secondo parere senza documenti è un parere sbagliato. "
                      "Per lavorare bene servono: la lettera di dimissione del medico curante, "
                      "tutti gli esami strumentali in originale (ECG, eco, Holter, eventuali coronarografie), "
                      "le analisi del sangue degli ultimi sei mesi e l'elenco aggiornato della terapia "
                      "farmacologica attuale, comprese le posologie e gli orari di assunzione."),
                ("blockquote",
                 "Il secondo parere non sostituisce il medico curante: lo accompagna. "
                 "Se il dialogo fra i due specialisti funziona, il paziente vince due volte."),
            ],
        },
        {
            "slug":     "prevenzione-familiare-cardiovascolare",
            "kicker":   "Prevenzione",
            "title":    "Programma prevenzione cardiovascolare: cosa significa davvero",
            "date":     "27 febbraio 2026",
            "read_min": 4,
            "author":   "Dr.ssa Margherita Salieri",
            "lede":
                "Sei mesi di monitoraggio integrato non sono un pacchetto vendite. "
                "Sono uno strumento clinico per chi ha familiarità diretta con un evento "
                "cardiovascolare precoce.",
        },
        {
            "slug":     "ecocardiografia-quando-serve",
            "kicker":   "Diagnostica",
            "title":    "Ecocardiografia transtoracica: quando è davvero necessaria",
            "date":     "11 febbraio 2026",
            "read_min": 5,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "Non tutti i pazienti che chiedono 'l'ecocardio' ne hanno bisogno. "
                "Una guida onesta alle indicazioni cliniche reali e ai casi in cui "
                "rappresenta un esame di ridondanza.",
        },
        {
            "slug":     "donne-cuore-perimenopausa",
            "kicker":   "Cardiologia di genere",
            "title":    "Donne e cuore: il silenzio della perimenopausa",
            "date":     "23 gennaio 2026",
            "read_min": 7,
            "author":   "Dr.ssa Margherita Salieri",
            "lede":
                "Per decenni i protocolli cardiologici sono stati costruiti su pazienti "
                "uomini. Il risultato è che molte donne tra i quarantacinque e i sessanta "
                "anni ricevono ancora oggi diagnosi tardive o sbagliate.",
        },
        {
            "slug":     "sport-amatoriale-controlli",
            "kicker":   "Sport e cuore",
            "title":    "Sport amatoriale: i controlli cardiologici che servono davvero",
            "date":     "08 gennaio 2026",
            "read_min": 4,
            "author":   "Dr. Andrea Lombardi",
            "lede":
                "Tre grandi falsi miti sui controlli pre-attività sportiva amatoriale, "
                "da chi li firma quotidianamente per ciclisti, runner e nuotatori "
                "fra i quaranta e i sessant'anni.",
        },
    ],

    # ─── CONTATTI (contact) ────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contatti",
        "headline": "Un solo numero, <em>una sola persona</em> dall'altra parte del filo.",
        "intro":
            "Lo studio risponde personalmente alle telefonate dal lunedì al venerdì. "
            "La segreteria clinica è gestita direttamente dalla Sig.ra Adele Petrucci, "
            "che conosce ogni cartella e ogni paziente per nome.",

        "blocks": [
            ("Indirizzo",   "Viale Parioli 142", "00197 Roma · interno 4, scala B"),
            ("Telefono",    "+39 06 320 1144",   "Risposta diretta 9:00 – 19:00"),
            ("Email",       "studio@maranicardiologia.it", "Risposta entro la giornata lavorativa"),
            ("Urgenze",     "+39 335 642 8011",  "Linea riservata pazienti in carico"),
        ],

        "hours": [
            ("Lunedì",     "9:00 – 13:00", "15:00 – 19:00"),
            ("Martedì",    "9:00 – 13:00", "15:00 – 19:00"),
            ("Mercoledì",  "9:00 – 13:00", "15:00 – 19:00"),
            ("Giovedì",    "9:00 – 13:00", "15:00 – 19:00"),
            ("Venerdì",    "9:00 – 13:00", "—"),
            ("Sabato",     "Chiuso al pubblico", "Reperibilità telefonica per pazienti in carico"),
            ("Domenica",   "Chiuso", "—"),
        ],

        "transport": [
            ("Metro",   "Linea B · Termini → bus 168 fermata Parioli/Liegi"),
            ("Auto",    "Parcheggio convenzionato Q-Park Parioli, ingresso da Via Bertoloni"),
            ("Treno",   "Stazione Termini · 12 minuti in taxi"),
        ],

        "form_title": "Scrivi allo studio",
        "form_intro":
            "Per richieste non urgenti — informazioni sulle visite, costi, "
            "logistica — scrivici qui sotto. Risponde personalmente la segreteria clinica.",

        "hours_heading":     "Orari di apertura",
        "transport_heading": "Come raggiungerci",

        "form_placeholders": {
            "first_name": "Mario",
            "last_name":  "Rossi",
            "email":      "mario.rossi@email.it",
            "phone":      "+39 333 ...",
            "subject":    "Informazioni su una visita di controllo",
            "message":
                "Resta in poche righe — la segreteria ti contatta "
                "entro la giornata lavorativa.",
        },
        "form_helpers": {
            "first_name": "Solo nome di battesimo.",
            "last_name":  "Come appare sulla tessera sanitaria.",
            "email":      "Usiamo l'email solo per rispondere: niente newsletter.",
            "phone":      "Opzionale. Solo se preferisci essere richiamato.",
            "subject":    "Un titolo breve aiuta a smistare la richiesta.",
            "message":    "Resta nelle dieci righe — la segreteria risponde entro la giornata lavorativa.",
        },
        "form_consent":
            "Acconsento al trattamento dei dati personali secondo l'informativa privacy "
            "(Reg. UE 679/2016). I dati restano custoditi dallo studio e non sono comunicati a terzi.",
        "form_submit_note":
            "Risposta entro la giornata lavorativa · archiviazione cartacea riservata.",
    },

    # ─── RICHIEDI VISITA (appointment) ─────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Richiesta visita privata",
        "headline": "Una visita privata <em>non si prenota</em>: si concorda.",
        "intro":
            "Non esiste un calendario online. Lo studio riserva ogni primo "
            "appuntamento dopo aver letto una breve descrizione del caso. "
            "Le richieste vengono valutate personalmente dal medico entro 48 ore.",

        "process_label":   "Come funziona",
        "process_heading": "Quattro passaggi, in <em>quattro giorni lavorativi.</em>",

        "process": [
            ("01", "Compila il modulo",
             "Bastano dieci righe per inquadrare la tua richiesta. "
             "Allega gli esami recenti se vuoi: aiuta a non chiederteli due volte."),
            ("02", "Lettura clinica",
             "Il medico legge personalmente la richiesta entro 48 ore lavorative "
             "e valuta se la prima visita è di sua competenza."),
            ("03", "Proposta di appuntamento",
             "Se il caso è di nostra competenza, la segreteria propone "
             "due fasce orarie compatibili con le tue esigenze."),
            ("04", "Conferma e dossier",
             "Una volta confermato l'appuntamento ricevi via email l'elenco "
             "dei documenti da portare e l'indirizzo dello studio con le indicazioni di accesso."),
        ],

        "form_title": "Modulo di richiesta",
        "form_band_side_note":
            "Riserva qualche minuto. Le richieste compilate con cura sono lette "
            "dal medico per intero — quelle frettolose, no.",
        "form_band_side_note_small": "↓ Modulo riservato",

        # Per-field dicts: `type` drives the input kind, `full_width` marks full-row
        # fields, selects carry their option list inline. The chrome loops this list
        # directly instead of hand-writing the form.
        "form_fields": [
            {"name": "name", "label": "Nome e cognome", "placeholder": "Mario Rossi",
             "type": "text", "required": True, "full_width": False,
             "helper": "Come sulla tessera sanitaria."},
            {"name": "email", "label": "Email", "placeholder": "mario@email.it",
             "type": "email", "required": True, "full_width": False,
             "helper": "La proposta di appuntamento arriva qui."},
            {"name": "phone", "label": "Telefono", "placeholder": "+39 333 ...",
             "type": "tel", "required": True, "full_width": False,
             "helper": "La segreteria può richiamare per confermare."},
            {"name": "age", "label": "Età", "placeholder": "52",
             "type": "number", "required": False, "full_width": False,
             "helper": "Facoltativa."},
            {"name": "visit_type", "label": "Tipo di visita", "type": "select",
             "required": True, "full_width": False,
             "options": ["Prima visita", "Secondo parere",
                         "Programma prevenzione", "Visita di controllo"],
             "helper": "Se non sei sicuro, scegli Prima visita."},
            {"name": "availability", "label": "Disponibilità preferite", "type": "select",
             "required": True, "full_width": False,
             "options": ["Mattina", "Pomeriggio", "Indifferente"],
             "helper": "Serve solo ad allineare le due proposte di orario."},
            {"name": "referring_doctor", "label": "Medico curante",
             "placeholder": "Dr. ...",
             "type": "text", "required": False, "full_width": True,
             "helper": "Se sei inviato da un collega, indica il suo nome."},
            {"name": "case_description", "label": "Breve descrizione del caso",
             "placeholder":
                 "Sintomi, esami già eseguiti, diagnosi attuale, terapia in corso. "
                 "Resta nelle dieci righe.",
             "type": "textarea", "required": True, "full_width": True,
             "helper": "Le richieste lette dal medico sono quelle compilate con cura — non le frettolose."},
        ],

        # Sections carve the 8-field form into 4 logical groups so the form
        # reads as a short consultation, not an airline check-in. `fields`
        # references field `name` values declared in `form_fields` above.
        "form_sections": [
            {"num": "01", "title": "Chi sei",
             "meta": "Queste righe arrivano direttamente in segreteria.",
             "fields": ["name", "email", "phone", "age"]},
            {"num": "02", "title": "Di che visita hai bisogno",
             "meta": "Allinea la richiesta al perimetro dello studio.",
             "fields": ["visit_type", "availability", "referring_doctor"]},
            {"num": "03", "title": "Documenti utili (facoltativi)",
             "meta": "Referti, esami e ECG recenti aiutano il medico a "
                     "non chiederti di ripetere ciò che hai già fatto.",
             "fields": ["__upload__"]},
            {"num": "04", "title": "Descrivi il caso",
             "meta": "Dieci righe bastano. Il medico legge personalmente.",
             "fields": ["case_description"]},
        ],

        # File upload field — premium UI, optional, for lab reports / ECGs.
        "upload_field": {
            "name":       "referti",
            "label":      "Referti o esami recenti",
            "helper":     "PDF, JPG, PNG · fino a 5 file, massimo 10 MB complessivi. "
                          "Custoditi nell'archivio cifrato dello studio.",
            "accept":     ".pdf,.jpg,.jpeg,.png",
            "multiple":   True,
            "primary":    "Trascina qui i referti o",
            "link":       "sfoglia i tuoi documenti",
            "meta":       "PDF / JPG / PNG · max 10 MB",
        },

        "submit_label": "Invia richiesta",

        "form_submit_note":
            "Il medico legge ogni richiesta entro 48 ore lavorative. "
            "I dati clinici restano nell'archivio cartaceo dello studio.",

        "consent":
            "Acconsento al trattamento dei dati personali secondo l'informativa "
            "privacy ai sensi del Regolamento UE 679/2016. I dati clinici "
            "sono custoditi nel solo archivio cartaceo dello studio.",

        "footnote":
            "Lo studio non risponde a richieste anonime e non rilascia opinioni "
            "cliniche per email senza visita. Per informazioni amministrative "
            "(costi, orari, parcheggio) usa la pagina contatti.",
    },
}


# ---------------------------------------------------------------------------
# GUSTO — Osteria Moderna (fine-dining archetype)
# Editorial dark · Playfair Display + Lato · charcoal + gold + red
# ---------------------------------------------------------------------------

GUSTO_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Casa",       "kind": "home"},
        {"slug": "filosofia", "label": "Filosofia",  "kind": "about"},
        {"slug": "menu",      "label": "Menu",       "kind": "menu"},
        {"slug": "atmosfera", "label": "Atmosfera",  "kind": "gallery"},
        {"slug": "diario",    "label": "Diario",     "kind": "blog_list"},
        {"slug": "prenota",   "label": "Prenota",    "kind": "reservations"},
    ],

    "site": {
        "logo_initial": "OM",
        "logo_word":    "Osteria Moderna",
        "tag":          "Tavolo unico · Milano Brera · 14 coperti",
        "phone":        "+39 02 3611 9920",
        "email":        "concierge@osteriamoderna.it",
        "address":      "Via San Marco 17 · 20121 Milano",
        "hours_compact":"Mar – Sab · solo cena",
        "star_line":    "★ Una stella Michelin · est. 2018",
        "footer_intro":
            "Una stella Michelin dal 2018. Quattordici coperti, due servizi a "
            "settimana, un menù a otto atti che cambia ogni due settimane.",
        "footer_hours_1": "Mer – Sab · 20:00",
        "footer_hours_2": "Dom & Lun · chiuso",
        "copyright": "© 2026 Osteria Moderna · P. IVA 09456112094",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Tavolo unico · Milano Brera · 14 coperti",
        "headline": "Una serata in <em>otto atti.</em>",
        "intro":
            "Un menù degustazione che cambia ogni due settimane secondo il "
            "mercato del giorno. Solo cena. Solo prenotazione. Solo per quattordici.",
        "primary_cta":   "Riserva la serata",
        "primary_href":  "prenota",
        "secondary_cta": "Lo chef",
        "secondary_href":"filosofia",

        "chef_label":    "Lo chef",
        "star_tag":      "★ Atto V · Cioccolato 80%",
        "photo_label":   "Fotografia",
        "cuisine_label": "Cucina",

        "facts": [
            ("14",   "coperti per servizio"),
            ("8",    "atti nel menù degustazione"),
            ("180€", "menù completo · vini + 90€"),
        ],

        "manifesto_drop_cap": "U",
        "manifesto":
            "n menù che cambia ogni due settimane. Una sola sala da quattordici "
            "coperti. Una cucina a vista che lavora in silenzio per quattro ore "
            "filate. Da Osteria Moderna non si ordina alla carta — si entra "
            "in una storia che ha un inizio, un climax e una chiusura.",

        "signature_courses": [
            ("I",   "Ostrica & cetriolo",     "acetosella, perle di yuzu",        "Champagne Selosse"),
            ("II",  "Risotto al midollo",      "estratto di prezzemolo, caffè",     "Soave Pieropan '21"),
            ("III", "Capesanta arrostita",     "burro nocciola, capperi di Pantelleria", "Riesling Pacherhof"),
            ("IV",  "Piccione di Bresse",      "fichi neri, cardamomo verde",      "Barolo Cannubi '17"),
            ("V",   "Cioccolato 80%",          "olio EVO, sale Maldon",             "Marsala Vintage '99"),
        ],

        "chef": {
            "name":  "Lorenzo Fioravanti",
            "role":  "Chef patron · 1 stella Michelin",
            "bio":
                "Romano, classe 1981. Si forma da Bottura, da Cracco, "
                "da Brutscher al Mirazur. Apre Osteria Moderna nel 2014 in "
                "tre stanze di un palazzo settecentesco di Brera. "
                "Stella Michelin nel 2018, mantenuta fino a oggi.",
        },

        "courses_label": "Cinque atti del menù in corso · autunno '26",
        "courses_footline": "€ 180 / persona · vini in abbinamento + €90",
        "courses_full_cta": "Otto atti completi",
        "chef_link_filosofia": "La filosofia",
        "chef_link_diario": "Il diario",

        "press_label": "Pubblicato su",
        "press": ["GUIDA MICHELIN", "GAMBERO ROSSO", "IDENTITÀ GOLOSE",
                  "CORRIERE LIVING", "VOGUE FOOD"],

        # Ingredients/sourcing editorial band
        "ingredienti": {
            "label": "Materia prima",
            "heading": "Trentadue produttori, <em>tutti per nome.</em>",
            "text":
                "La rete di Osteria Moderna comprende trentadue piccoli produttori — "
                "pescatori liguri, allevatori piemontesi, ortolani lodigiani — di cui "
                "Lorenzo conosce personalmente il nome, l'indirizzo e il numero di "
                "telefono. Nessun intermediario, nessun catalogo, nessuna distribuzione.",
            "image":
                "https://images.unsplash.com/photo-1610348725531-843dff563e2c"
                "?auto=format&fit=crop&w=1000&q=80",
            "image_caption": "Ingredienti del menù autunno '26 · mercato del mattino",
        },

        # Atmosphere teaser — expanded to 4 images with lightbox
        "atmosphere_teaser": {
            "label": "L'atmosfera",
            "images": [
                ("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4"
                 "?auto=format&fit=crop&w=600&q=80",
                 "La sala principale"),
                ("https://images.unsplash.com/photo-1581349485608-9469926a8e5e"
                 "?auto=format&fit=crop&w=600&q=80",
                 "La cucina a vista"),
                ("https://images.unsplash.com/photo-1559329007-40df8a9345d8"
                 "?auto=format&fit=crop&w=600&q=80",
                 "La sala superiore"),
                ("https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
                 "?auto=format&fit=crop&w=600&q=80",
                 "Mise en place del venerdì sera"),
            ],
            "link_label": "Scopri l'atmosfera",
            "link_href":  "atmosfera",
        },

        # Awards/recognition section
        "riconoscimenti": {
            "label": "Riconoscimenti",
            "items": [
                ("★", "Stella Michelin", "Dal 2018 — confermata ogni anno"),
                ("GR", "Gambero Rosso", "Tre Forchette · Premio speciale cucina d'autore 2025"),
                ("IG", "Identità Golose", "Piatto dell'anno 2024 — Piccione di Bresse"),
                ("50B", "50 Best Discovery", "Incluso nella selezione 2026 Italia"),
            ],
        },

        # CTA section
        "cta_heading": "Quattordici coperti, <em>due servizi a settimana.</em>",
        "cta_primary": "Riserva la serata",
        "cta_secondary": "Vedi il menù completo",

        # Seasonal highlight card
        "stagione": {
            "label": "In questo momento",
            "title": "Menù autunno '26",
            "subtitle": "Otto atti · dal 6 al 19 ottobre",
            "text":
                "Il nuovo menù è in carta da lunedì. Otto piatti, quattro costruzioni "
                "nuove e quattro variazioni su temi che avevamo lasciato in archivio "
                "dal 2022. Prenotazione obbligatoria.",
            "cta_label": "Scopri gli otto atti →",
            "cta_href":  "menu",
        },

        # Producer showcase — 4 artisans portraits (editorial, not cheap)
        "produttori": {
            "label":   "Dai produttori",
            "heading": "Quattro mani, <em>una tavola sola.</em>",
            "intro":
                "Ogni mattina una parte della sala entra dalla porta della cucina. "
                "I volti sono questi. Le loro terre, i loro metodi — li trovate "
                "in carta, riga per riga.",
            "items": [
                {
                    "portrait":
                        "https://images.unsplash.com/photo-1552058544-f2b08422138a"
                        "?auto=format&fit=crop&w=800&q=80",
                    "name": "Roberto Tarbouriech",
                    "role": "Ostriche & crostacei",
                    "area": "Sète · Étang de Thau",
                    "blurb":
                        "Le ostriche Spéciales vengono dalla laguna dell'Étang de "
                        "Thau. Consegna lunedì, servite martedì sera.",
                },
                {
                    "portrait":
                        "https://images.unsplash.com/photo-1568213816046-0ee1c42bd559"
                        "?auto=format&fit=crop&w=800&q=80",
                    "name": "Famiglia Brezza",
                    "role": "Barolo & Langhe",
                    "area": "Barolo · Piemonte",
                    "blurb":
                        "Vigne di Cannubi e Sarmassa, lavorate senza enologo esterno. "
                        "Una carta verticale dal 2008 in poi.",
                },
                {
                    "portrait":
                        "https://images.unsplash.com/photo-1543418219-44e30b057fea"
                        "?auto=format&fit=crop&w=800&q=80",
                    "name": "Aloïs Lageder",
                    "role": "Biodinamica di montagna",
                    "area": "Pacherhof · Alto Adige",
                    "blurb":
                        "Vini bianchi che arrivano a noi in via diretta dalla "
                        "val d'Isarco. Niente filtro, niente chiarifica.",
                },
                {
                    "portrait":
                        "https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
                        "?auto=format&fit=crop&w=800&q=80",
                    "name": "Gianfranco Pieropan",
                    "role": "Soave classico",
                    "area": "Soave · Veneto",
                    "blurb":
                        "Calvarino e La Rocca, Soave Classico in purezza. "
                        "Accompagnano il secondo atto da sempre.",
                },
            ],
        },

        # Private dining / Chef's Table — exclusive experience block
        "private_dining": {
            "label":   "Eventi privati",
            "heading": "Chef's Table & <em>privatizzazioni.</em>",
            "intro":
                "Per dodici coperti in sala privata o per la sera intera "
                "— ventotto coperti, un solo menù, cucina a vista.",
            "experiences": [
                {
                    "icon": "fork",
                    "title": "Chef's Table",
                    "meta":  "12 coperti · da €190 / persona",
                    "desc":
                        "Tavolo unico affacciato sulla cucina. Menù di "
                        "otto atti in versione narrata direttamente "
                        "dallo chef. Disponibile il martedì.",
                },
                {
                    "icon": "door",
                    "title": "Privatizzazione serale",
                    "meta":  "28 coperti · da €5.800 / serata",
                    "desc":
                        "Intero ristorante, menù dedicato, fiori, maître "
                        "d'hôtel personale. Minimo due settimane di "
                        "anticipo, decliniamo il venerdì.",
                },
                {
                    "icon": "wine",
                    "title": "Degustazione di carta",
                    "meta":  "6 coperti · solo giovedì",
                    "desc":
                        "Una serata al mese con il sommelier su sei "
                        "bottiglie scelte tra i produttori in carta. "
                        "Solo su lista d'attesa, da prenotare.",
                },
            ],
            "cta_label": "Scrivi al concierge",
            "cta_href":  "prenota",
        },

        # Wine program — pairings, sommelier signature
        "wine_program": {
            "label":   "La cantina",
            "heading": "Quattrocento etichette, <em>tre abbinamenti notturni.</em>",
            "intro":
                "La carta segue il menù: ogni atto ha il suo abbinamento "
                "e due alternative — classica, contemporanea, non alcolica.",
            "sommelier": {
                "name": "Greta Vallesi",
                "role": "Maître & sommelier",
                "bio":
                    "Quindici anni tra Borgogna, Langhe e Champagne. "
                    "La carta è curata da lei, l'abbinamento è sempre "
                    "proposto al tavolo, mai imposto.",
            },
            "pairings": [
                ("01", "Pairing classico",
                 "Champagne en blanc, Soave Classico, Barolo riserva, Moscato.",
                 "+ €110"),
                ("02", "Pairing contemporaneo",
                 "Col Fondo veneto, Erbaluce lungo, Ribolla anfora, "
                 "Timorasso in verticale.",
                 "+ €130"),
                ("03", "Pairing zero-alcol",
                 "Kombucha artigianale, tè freddi in infusione lenta, "
                 "succo d'uva fermentato naturalmente.",
                 "+ €60"),
            ],
            "cellar_facts": [
                ("420", "etichette in carta"),
                ("18", "regioni vitivinicole"),
                ("2005", "verticale più antica (Brunello)"),
            ],
        },
    },

    # ─── FILOSOFIA (about) ─────────────────────────────────────
    "filosofia": {
        "eyebrow":  "Filosofia",
        "headline": "Un menù, una sala, <em>una serata sola.</em>",
        "intro":
            "Osteria Moderna nasce nel 2014 dall'idea che un ristorante non sia "
            "un servizio, ma un teatro. Quattordici coperti per servizio, due "
            "servizi alla settimana, un cuoco al banco e un maître in sala.",

        "history": [
            ("2014",
             "Lorenzo Fioravanti apre Osteria Moderna in tre stanze di un palazzo "
             "settecentesco di Brera. Sedici coperti, una sola brigata, un menù "
             "che cambia ogni venerdì."),
            ("2016",
             "Greta Vallesi entra come maître e cellar manager. La carta dei vini "
             "passa da 80 a 320 etichette, con un focus su piccoli vignaioli del "
             "Nord-Est e della Borgogna minore."),
            ("2018",
             "Una stella Michelin. Da quel momento il ristorante riduce a "
             "quattordici coperti per servizio e introduce il menù degustazione "
             "obbligatorio in otto atti."),
            ("2021",
             "Apertura della cucina a vista sulla sala. Lo chef cucina davanti "
             "agli ospiti per tutta la durata del servizio. Nessuna parete "
             "fra cuoco e tavolo."),
            ("2024",
             "Pubblicazione del libro 'Otto atti', edizioni Giunti, dedicato "
             "alle prime quaranta serate del menù invernale 2023/24."),
        ],

        "filosofia_image":
            "https://images.unsplash.com/photo-1559329007-40df8a9345d8"
            "?auto=format&fit=crop&w=1400&q=80",
        "filosofia_image_caption": "La cucina · Lorenzo Fioravanti al lavoro",

        "method_title": "Metodo",
        "method_paragraphs": [
            "Il menù degustazione cambia ogni due settimane secondo il mercato "
            "del giorno. Le materie prime arrivano da una rete di trentadue "
            "piccoli produttori — pescatori liguri, allevatori piemontesi, "
            "ortolani lodigiani — di cui Lorenzo conosce personalmente "
            "il nome, l'indirizzo e il numero di telefono.",
            "Ogni atto è pensato come un movimento di una sinfonia: c'è un "
            "preludio, un crescendo a metà serata, una pausa lirica, un "
            "finale che torna all'inizio per chiudere il cerchio. La sequenza "
            "viene riscritta da capo ogni due settimane — non si replicano "
            "mai le stesse transizioni.",
            "La carta dei vini è curata da Greta Vallesi: 320 etichette, di "
            "cui due terzi da piccoli produttori europei. L'abbinamento è "
            "facoltativo (€ 90 per il percorso completo) ma — diciamolo "
            "francamente — è la metà del lavoro che facciamo.",
        ],

        "values_label": "Cosa garantiamo",
        "values_heading": "Quattro promesse che <em>non cambiano mai</em>.",
        "values": [
            ("Tempo",        "Tre ore e mezza di servizio. Mai più, mai meno."),
            ("Stagione",     "Niente in sala che non sia di stagione locale."),
            ("Trasparenza",  "Conosciamo per nome ogni produttore in carta."),
            ("Discrezione",  "Niente foto del cuoco, niente social: in sala si mangia."),
        ],

        "cta_heading": "Vuoi vedere il menù <em>in corso questa settimana?</em>",
        "cta_menu": "Otto atti dell'autunno '26",
        "cta_prenota": "Riserva la serata",
    },

    # ─── MENU ──────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "Il menù",
        "headline": "Otto atti — <em>autunno '26</em>",
        "intro":
            "Il menù cambia integralmente ogni due settimane. Quanto segue è "
            "il programma in vigore dal 6 al 19 ottobre 2026. Due servizi alla "
            "settimana, dal mercoledì al sabato, una sola seduta dalle 20:00.",
        "courses_label": "Otto atti · servizio dalle 20:00",

        "courses": [
            ("I",    "Ostrica & cetriolo",
             "Ostrica Tarbouriech di Sète, gel di cetriolo bio del Lago di Como, acetosella selvatica, perle di yuzu sospese in olio d'oliva taggiasca.",
             "Champagne Anselme Selosse · Initial · Avize"),
            ("II",   "Risotto al midollo",
             "Carnaroli Riserva San Massimo del 2023, midollo arrostito su brace di vite, estratto di prezzemolo riccio, polvere di caffè monorigine etiopica.",
             "Soave Classico Pieropan · La Rocca '21"),
            ("III",  "Capesanta arrostita",
             "Capesanta di Galizia di pesca subacquea, burro nocciola al rosmarino, capperi di Pantelleria al sale, gel di limone di Amalfi.",
             "Riesling Pacherhof · Kerner Alto Adige '22"),
            ("IV",   "Pasta della casa",
             "Cappelletti tirati a mano, ripieno di cappone di Bresse e tartufo nero della Val Trebbia, brodo di cinghiale ridotto sette volte.",
             "Lambrusco di Sorbara Rinaldini · Rosé Brut"),
            ("V",    "Piccione di Bresse",
             "Petto al sangue laccato al miele di castagno, coscia confit ai fichi neri di Caprino, riduzione di Barolo, polvere di cardamomo verde guatemalteco.",
             "Barolo Riserva Cannubi · Brezza '17"),
            ("VI",   "Pre-dessert",
             "Sorbetto al sedano rapa, oxalis del nostro orto, granita di prugna di Dro, cristalli di sale rosa.",
             "—"),
            ("VII",  "Cioccolato 80%",
             "Cioccolato Domori Criollo 80%, olio extravergine di Tuscia, sale Maldon affumicato al melo, polvere di liquirizia calabrese.",
             "Marsala Vintage Marco De Bartoli · 1999"),
            ("VIII", "Mignardises",
             "Selezione di tre piccole pasticcerie d'autore, una al cioccolato, una agli agrumi, una al miele.",
             "Caffè monorigine Etiopia Yirgacheffe"),
        ],

        "wine_intro_title": "Carta dei vini",
        "wine_intro":
            "320 etichette, di cui due terzi da piccoli vignaioli europei. "
            "Greta Vallesi è in sala ogni sera per discutere ogni scelta — "
            "ma è anche disponibile a costruire un percorso di abbinamento "
            "su misura, fuori dal menù di abbinamento standard.",

        "wine_highlights": [
            ("Champagne", "62 etichette · 24 grower champagne"),
            ("Borgogna",  "48 produttori · focus su Côte de Beaune e Mâconnais"),
            ("Italia",    "112 etichette · Nord-Est, Alto Piemonte e Sicilia volcanica"),
            ("Vini liquorosi", "18 etichette · sherry, marsala, madeira, tokaji"),
        ],

        "footer":
            "Menù degustazione completo: € 180 a persona. Abbinamento vino "
            "facoltativo: € 90 a persona. Pacchetto magnum (sei calici da "
            "magnum, formato condiviso): + € 140. Tutte le intolleranze e "
            "le allergie vanno comunicate al momento della prenotazione.",
    },

    # ─── ATMOSFERA (gallery) ───────────────────────────────────
    "atmosfera": {
        "eyebrow":  "L'atmosfera",
        "headline": "Tre stanze, <em>quattordici sedie,</em> nessuna parete.",
        "intro":
            "Osteria Moderna occupa tre stanze di un palazzo settecentesco di "
            "Via San Marco, a Brera. Niente parete tra cucina e sala. "
            "Nessuna immagine sui social: per fotografare il piatto, qui, "
            "lo si guarda con calma da seduti.",

        "rooms": [
            ("La sala principale",
             "Il cuore del ristorante. Nove coperti, tre tavoli, una vetrata "
             "che dà sul cortile interno del palazzo."),
            ("La cucina a vista",
             "Cinque coperti al banco, di fronte ai fuochi. Lo chef cucina "
             "in silenzio per tutto il servizio."),
            ("La cantina",
             "Una stanza ipogea con 320 etichette. Visite private su prenotazione, "
             "in coda alla cena, accompagnati da Greta Vallesi."),
            ("Il cortile",
             "Da maggio a settembre, due tavoli en plein air sotto il glicine "
             "del cortile interno. Riservabili solo per cene complete."),
        ],

        "captions": [
            "La cucina a vista durante il servizio del venerdì sera.",
            "Il primo atto del menù autunno '26: ostrica e cetriolo.",
            "Greta Vallesi in cantina, fra le 320 etichette.",
            "Il cortile interno del palazzo settecentesco di Via San Marco.",
            "Lorenzo Fioravanti durante il servizio.",
            "La sala principale al termine della mise en place.",
        ],

        "cta_quote": "«Per fotografare il piatto, qui, lo si guarda con calma da seduti.»",
        "cta_desc": "Quattordici coperti per servizio. Solo prenotazione. Solo cena. Mer – Sab.",
        "cta_primary": "Riserva la serata",
        "cta_secondary": "Vedi il menù",
    },

    # ─── DIARIO (blog list / detail) ───────────────────────────
    "diario": {
        "eyebrow":  "Il diario di sala",
        "headline": "Note di lavoro, <em>di stagione</em>, di sala.",
        "intro":
            "Brevi appunti di Lorenzo Fioravanti e Greta Vallesi sui menù in "
            "corso, sui produttori, sulle serate memorabili e su quello che "
            "sta cambiando in cucina di settimana in settimana.",
        "read_article": "Leggi l'articolo",
        "min_label": "min",
        "min_read_label": "min di lettura",
        "crumb_label": "Diario",
        "back_link": "← Tutto il diario",
        "footer_label": "Osteria Moderna · Il diario di sala",
        "empty_body": [
            "Articolo in preparazione editoriale. La pubblicazione integrale "
            "sarà disponibile a breve, scritta personalmente dallo chef o dal maître.",
            "Questo segnaposto descrive la voce del Diario di Sala: brevi note di "
            "lavoro, riflessioni sui produttori, racconti di serate memorabili. "
            "Mai più di duemila parole, mai meno di cinquecento.",
        ],
    },

    "posts": [
        {
            "slug":     "menu-autunno-26",
            "kicker":   "Menù in corso",
            "title":    "Le otto idee del menù autunno '26",
            "date":     "5 ottobre 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "Il nuovo menù è entrato in carta lunedì notte. Otto piatti, "
                "quattro nuove costruzioni e quattro variazioni su temi che "
                "avevamo lasciato in archivio dal 2022.",
            "body": [
                ("p", "Costruire un menù degustazione è meno una questione di ricette "
                      "e più una questione di transizioni. Come si passa dal salato "
                      "al dolce. Come si torna indietro a metà serata. Come si "
                      "introduce la quarta portata senza rompere il ritmo. "
                      "Per il menù autunno '26 abbiamo lavorato per due settimane "
                      "soltanto sulle pause."),
                ("h2", "Le quattro idee nuove"),
                ("p", "Il primo atto, ostrica e cetriolo, è una rilettura di un piatto "
                      "che faceva il mio maestro Pierre Brutscher al Mirazur. "
                      "L'avevo in testa dal 2007, da quando ero suo apprendista. "
                      "Per quindici anni non sono riuscito a trovargli il finale. "
                      "L'ho trovato la scorsa estate, su una panchina di Sète, "
                      "guardando Tarbouriech raccogliere le sue ostriche all'alba."),
                ("p", "Il quarto atto — la pasta della casa — è la prima volta che "
                      "in tre anni infiliamo la pasta nel menù degustazione. "
                      "Il ripieno di cappone e tartufo nero è un omaggio a una "
                      "ricetta della Val Trebbia che la mia nonna materna preparava "
                      "il giorno di Natale."),
                ("h2", "Le quattro variazioni"),
                ("p", "Il piccione di Bresse torna in carta dopo due stagioni. È il "
                      "mio piatto-spina, quello che preferisco fra tutti quelli che "
                      "ho costruito da quando ho aperto. Stavolta lo accompagno con "
                      "una riduzione di Barolo Cannubi del '17 — un vino che Greta "
                      "ha trovato dopo sei mesi di telefonate alla cantina Brezza."),
                ("blockquote",
                 "Un menù degustazione non è una sequenza di piatti. È un percorso "
                 "che il cliente fa con il cuoco, e che il cuoco rifà ogni sera "
                 "insieme al cliente."),
                ("p", "Ringrazio Greta per l'abbinamento, la brigata di sala per la "
                      "pazienza con cui ha imparato in due settimane otto nuove "
                      "spiegazioni di sala, e tutti i produttori che ci hanno permesso "
                      "di costruire questo menù: Tarbouriech, San Massimo, Pacherhof, "
                      "i fratelli Brezza, Domori, Marco De Bartoli."),
            ],
        },
        {
            "slug":     "barolo-cannubi-17-brezza",
            "kicker":   "Carta dei vini",
            "title":    "Sei mesi di telefonate per un Barolo",
            "date":     "20 settembre 2026",
            "read_min": 4,
            "author":   "Greta Vallesi",
            "lede":
                "La storia di come è arrivato in carta il Barolo Cannubi '17 "
                "di Brezza, e perché lo abbiamo voluto a tutti i costi per "
                "il quinto atto del menù autunno.",
        },
        {
            "slug":     "cucina-a-vista",
            "kicker":   "La sala",
            "title":    "Cinque anni di cucina a vista: cosa abbiamo imparato",
            "date":     "29 agosto 2026",
            "read_min": 6,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "Aprire la cucina al pubblico ha cambiato il modo in cui si lavora "
                "in brigata. Ha cambiato anche il modo in cui i clienti mangiano. "
                "Una piccola riflessione a cinque anni dall'apertura del banco.",
        },
        {
            "slug":     "ostriche-tarbouriech",
            "kicker":   "I produttori",
            "title":    "Tarbouriech: l'ostricoltore che marea ogni dodici ore",
            "date":     "11 agosto 2026",
            "read_min": 5,
            "author":   "Lorenzo Fioravanti",
            "lede":
                "A Sète, in Linguadoca, Florent Tarbouriech ha inventato un "
                "metodo di allevamento che imita la marea atlantica nel "
                "Mediterraneo. Il risultato è l'ostrica del nostro primo atto.",
        },
        {
            "slug":     "libro-otto-atti",
            "kicker":   "Editoria",
            "title":    "Esce 'Otto atti', il primo libro di Osteria Moderna",
            "date":     "1 luglio 2026",
            "read_min": 3,
            "author":   "Greta Vallesi",
            "lede":
                "Il 4 luglio Giunti pubblica 'Otto atti — quaranta serate del "
                "menù invernale di Osteria Moderna'. Lorenzo lo racconta in "
                "presentazione il 12 luglio alla Triennale di Milano.",
        },
    ],

    # ─── PRENOTA (reservations / contact) ──────────────────────
    "prenota": {
        "eyebrow":  "Prenotazione",
        "headline": "Una cena <em>non si prenota</em>: si concorda.",
        "intro":
            "Da Osteria Moderna non esiste un calendario online. Le prenotazioni "
            "passano dal concierge personale del ristorante, Greta Vallesi, "
            "che risponde via email entro la giornata.",

        "process_label": "Come funziona",
        "process_heading": "Quattro passaggi, <em>quattro giorni di anticipo</em>.",
        "hours_label": "Servizi della settimana",
        "hours_heading": "Quattro sere, <em>una sola seduta</em>.",
        "private_heading": "Cene private",
        "form_submit": "Invia richiesta al concierge",

        "process": [
            ("01", "Scrivi a Greta",
             "Bastano poche righe: data preferita, numero di ospiti, eventuali "
             "intolleranze, occasione. Greta legge ogni richiesta personalmente."),
            ("02", "Proposta di serata",
             "Entro la giornata Greta propone una o due date compatibili "
             "(le uniche due serate disponibili sono mercoledì-sabato) "
             "e conferma il menù in vigore."),
            ("03", "Conferma & deposito",
             "Per confermare la prenotazione viene richiesto un piccolo deposito "
             "di € 80 a persona, che viene scalato dal conto finale."),
            ("04", "Brief della serata",
             "Il giorno prima riceverai una breve email con il dress code, "
             "il menù in carta e una nota sulla degustazione vini facoltativa."),
        ],

        "concierge": {
            "name":  "Greta Vallesi",
            "role":  "Maître & cellar manager",
            "email": "greta@osteriamoderna.it",
            "phone": "+39 02 3611 9920",
            "bio":
                "Romana di nascita, milanese di adozione. Quindici anni "
                "in sala, nove di cui da Osteria Moderna. Sommelier AIS dal 2014. "
                "In sala ogni sera dalle 18:30 alle 23:30.",
        },

        "hours": [
            ("Mercoledì",  "20:00 – 23:30",  "1 servizio · seduta unica"),
            ("Giovedì",    "20:00 – 23:30",  "1 servizio · seduta unica"),
            ("Venerdì",    "20:00 – 23:30",  "1 servizio · seduta unica"),
            ("Sabato",     "20:00 – 23:30",  "1 servizio · seduta unica"),
            ("Domenica",   "Chiuso",          "—"),
            ("Lun & Mar",  "Chiuso",          "Riposo settimanale della brigata"),
        ],

        "private_title": "Cene private & eventi",
        "private_intro":
            "Per cene private (anniversari, ricorrenze aziendali, "
            "presentazioni di prodotto) è possibile riservare l'intera "
            "sala in giorni di chiusura. Pacchetti su misura concordati "
            "personalmente con lo chef.",

        "form_title":  "Scrivi al concierge",
        # Per-field dicts keyed by name. Kept backward-compatible with the
        # tuple-loop in fine-dining/reservations.html by carrying `label`,
        # `placeholder` and `type` under their original positions.
        "form_fields": [
            {"name": "name",         "label": "Nome e cognome",
             "placeholder": "Mario Rossi", "type": "text", "required": True,
             "helper": "Greta vi saluta per nome in sala."},
            {"name": "email",        "label": "Email",
             "placeholder": "mario@email.it", "type": "email", "required": True,
             "helper": "La proposta di serata arriva qui."},
            {"name": "phone",        "label": "Telefono",
             "placeholder": "+39 333 ...", "type": "tel", "required": False,
             "helper": "Solo se preferite il contatto vocale."},
            {"name": "guests",       "label": "Numero di ospiti",
             "placeholder": "2", "type": "number", "required": True,
             "helper": "Seduta massima 24 coperti, minima 2."},
            {"name": "date",         "label": "Data preferita",
             "placeholder": "ven 16 ottobre", "type": "text", "required": True,
             "helper": "Aperto mercoledì-sabato. Greta propone la data compatibile più vicina."},
            {"name": "occasion",     "label": "Occasione",
             "placeholder": "", "type": "select", "required": True,
             "helper": "Greta adatta accoglienza, fiori e sequenza del menù."},
            {"name": "notes_food",   "label": "Intolleranze o allergie",
             "placeholder": "Eventuali intolleranze, allergie o richieste particolari",
             "type": "text", "required": False, "full_width": False,
             "helper": "Lo chef ricalibra il menù la mattina stessa."},
            {"name": "notes_extra",  "label": "Note per il concierge",
             "placeholder": "Greta legge personalmente ogni richiesta. Bastano poche righe.",
             "type": "textarea", "required": False, "full_width": True,
             "helper": "Anniversario, ospite vegetariano, sorpresa: qualunque dettaglio conta."},
        ],

        "form_sections": [
            {"num": "01", "title": "Chi prenota",
             "meta": "Queste righe le legge Greta, una alla volta.",
             "fields": ["name", "email", "phone"]},
            {"num": "02", "title": "La serata",
             "meta": "Serviamo una sola seduta, mercoledì-sabato.",
             "fields": ["guests", "date", "occasion"]},
            {"num": "03", "title": "Richieste particolari",
             "meta": "Bastano poche righe — Greta si muove sul resto.",
             "fields": ["notes_food", "notes_extra"]},
        ],

        "form_submit_note":
            "Greta risponde entro la giornata · conferma con deposito € 80 a persona, "
            "scalato dal conto finale.",

        "occasion_options": ["Cena romantica", "Compleanno", "Lavoro", "Indifferente"],
        "consent":
            "Acconsento al trattamento dei dati personali secondo l'informativa "
            "privacy ai sensi del Regolamento UE 679/2016.",

        "address_block": [
            ("Indirizzo",   "Via San Marco 17 · 20121 Milano"),
            ("Trasporti",   "Lanza M2 · 4 minuti a piedi · Brera"),
            ("Parcheggio",  "Convenzione APCOA Garibaldi 36 · navetta gratuita"),
        ],
    },
}


# ---------------------------------------------------------------------------
# DERMATOLOGIA ELITE — Studio Ricciardi Dermatologia (specialist archetype)
# Archetype-reuse validation: second template on the `specialist` archetype.
# Re-uses the Cardio chrome WITHOUT adding any new HTML. Differentiated by
# brand (Studio Ricciardi, not Marani), accent (forest green, not clinical red),
# font (Bodoni Moda, not Cormorant), editorial tone (dermatology: clinical +
# surgical + aesthetic), specialties, doctors, prices, press list and editorial
# copy. Page slugs follow CARDIO_CONTENT exactly because the specialist chrome
# hardcodes `pubblicazioni` as the blog parent page slug.
# ---------------------------------------------------------------------------

DERMATOLOGIA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Studio",          "kind": "home"},
        {"slug": "studio",          "label": "Lo Studio",       "kind": "about"},
        {"slug": "visite",          "label": "Visite",          "kind": "services"},
        {"slug": "medici",          "label": "Medici",          "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Pubblicazioni",   "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contatti",        "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Richiedi visita", "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "R",
        "logo_word":    "Studio Ricciardi",
        "tag":          "Dermatologia clinica, chirurgica ed estetica · Roma Veneto",
        "phone":        "+39 06 487 2311",
        "email":        "studio@ricciardidermatologia.it",
        "address":      "Via Veneto 116 · 00187 Roma",
        "hours_compact": "Lun – Ven · 10:00 – 20:00",
        "hours_footer_rows": [
            "Sabato · chirurgia su agenda",
            "Domenica · chiuso",
        ],
        "license":      "Iscrizione OMCeO Roma 3 / 11982",
        "footer_intro":
            "Studio specialistico privato di dermatologia clinica, chirurgica ed "
            "estetica. Riceviamo solo su appuntamento.",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Dermatologia clinica · Roma Veneto",
        "headline": "La pelle è una <em>carta d'identità</em>. La leggiamo per intero.",
        "intro":
            "Dermatologia clinica, chirurgica ed estetica in un unico studio privato a "
            "Via Veneto. Mappa nei digitale, diagnosi precoce dei tumori cutanei, "
            "chirurgia dermatologica in day-hospital e medicina estetica dermatologica.",
        "primary_cta":   "Prenota una prima visita",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Scopri lo studio",
        "secondary_href":"studio",

        "facts": [
            ("18",    "anni di dermatologia privata"),
            ("2.400", "mappature nevi all'anno"),
            ("3",     "sale dedicate · 1 chirurgica"),
        ],

        "manifesto_drop_cap": "O",
        "manifesto":
            "gni pelle racconta una storia che è scritta dall'ambiente, dal tempo, "
            "dai geni e dalle abitudini. Il dermatologo è il lettore di quella storia — "
            "con il dermatoscopio, con le mani, con l'occhio allenato di chi ha visto "
            "decine di migliaia di pazienti prima di voi. Allo Studio Ricciardi non "
            "abbiamo mai fretta di concludere una visita.",

        "signature_visits": [
            ("01", "Mappatura nevi digitale",
             "Videodermatoscopia ad alta risoluzione di tutti i nevi, archiviazione "
             "digitale e confronto con l'archivio storico del paziente. Refertata in giornata."),
            ("02", "Chirurgia dermatologica in day-hospital",
             "Escissione di lesioni sospette in anestesia locale con esame istologico "
             "dedicato. Piccola chirurgia plastica ricostruttiva inclusa nel percorso."),
            ("03", "Laser dermatologico",
             "Laser CO2 frazionato, laser vascolare e laser depilatorio di ultima "
             "generazione per cicatrici, vascolarizzazioni e chirurgia cutanea non invasiva."),
            ("04", "Medicina estetica dermatologica",
             "Filler, tossina botulinica, peeling medici e skinbooster eseguiti "
             "personalmente dal medico dermatologo. Mai delegati a personale non medico."),
        ],

        "chief": {
            "name":  "Dott.ssa Alessandra Ricciardi",
            "role":  "Direttore clinico · Dermatologa",
            "bio":
                "Specialista in dermatologia e venereologia all'Università Cattolica del "
                "Sacro Cuore di Roma, perfezionata in dermoscopia avanzata al Memorial "
                "Sloan Kettering di New York e in chirurgia dermatologica alla Charité di "
                "Berlino. Membro SIDeMaST, EADV e International Dermoscopy Society. "
                "Autrice di oltre cinquanta pubblicazioni indicizzate.",
            "portrait":
                "https://images.unsplash.com/photo-1638202993928-7267aad84c31"
                "?auto=format&fit=crop&w=900&q=80",
        },

        "press": ["JAMA Dermatology", "British Journal of Dermatology",
                  "Vanity Fair Wellness", "Corriere Salute", "Vogue Italia"],
        "press_label": "Pubblicato su",

        # Hero right sidebar (dark pulse column)
        "hero_sidebar_top_label": "Direzione clinica",
        "hero_sidebar_quote":
            "«La pelle non è un sintomo da zittire. "
            "È un tessuto che parla — basta imparare ad ascoltarlo.»",
        "hero_sidebar_author": "— JAMA Dermatology · 2025",
        "hero_sidebar_pulse": [
            ("Studio",      "Roma · Via Veneto"),
            ("Da",          "2008"),
            ("Riferimento", "Dermatologia integrata"),
        ],

        # Signature-visits section (dark 01/02/03/04 field grid)
        "signature_visits_label":   "Visite & percorsi",
        "signature_visits_heading": "Quattro aree cliniche, <em>un solo archivio.</em>",
        "signature_visits_intro":
            "Le quattro aree in cui lavoriamo ogni giorno. "
            "L'elenco completo dei percorsi è nella pagina Visite.",

        # Chief-doctor section
        "chief_label":   "Direzione clinica",
        "chief_heading": "Un solo archivio <em>per ogni pelle.</em>",

        # Credentials/certifications — unique to Derm (not on Cardio)
        "credentials": {
            "label": "Riconoscimenti & certificazioni",
            "items": [
                ("FotoFinder", "Centro certificato di riferimento per la dermoscopia digitale FotoFinder Systems", "dal 2012"),
                ("SIDeMaST", "Società Italiana di Dermatologia medica, chirurgica, estetica e delle MTS — membro attivo", ""),
                ("EADV", "European Academy of Dermatology and Venereology — full member", ""),
                ("IDS", "International Dermoscopy Society — Advanced Certified Dermoscopist", "dal 2015"),
            ],
        },

        # Gallery strip (Derm-only — Cardio uses tecnologie grid)
        "gallery_strip": {
            "label": "Direzione clinica & cosmeceutica",
            "images": [
                ("https://images.unsplash.com/photo-1638202993928-7267aad84c31"
                 "?auto=format&fit=crop&w=600&q=80",
                 "Direzione clinica · Studio Ricciardi"),
                ("https://images.unsplash.com/photo-1620916566398-39f1143ab7be"
                 "?auto=format&fit=crop&w=600&q=80",
                 "Linea cosmeceutica firmata"),
            ],
        },

        # Patient testimonial (different voice from Cardio — refined, aesthetic)
        "testimonianza": {
            "quote":
                "Cercavo una dermatologa che non avesse fretta. La Dottoressa Ricciardi "
                "ha passato venti minuti a studiare ogni neo con il dermatoscopio prima di "
                "dirmi una sola parola. È stata la visita più accurata della mia vita.",
            "author": "Paziente dello studio",
            "context": "Mappatura nevi digitale · 2025",
        },

        # FAQ accordion (dermatology-specific questions)
        "faq": {
            "label": "Domande frequenti",
            "heading": "Risposte alle domande <em>più comuni.</em>",
            "items": [
                ("Ogni quanto va fatta la mappatura dei nevi?",
                 "Raccomandiamo un controllo annuale per tutti. In caso di "
                 "familiarità per melanoma o di fototipo chiaro con molti nevi, "
                 "il controllo può essere semestrale. La mappatura digitale "
                 "permette di confrontare ogni neo con la sua versione precedente."),
                ("La chirurgia dermatologica è dolorosa?",
                 "L'escissione di lesioni sospette avviene in anestesia locale. "
                 "Il paziente sente solo la prima puntura dell'anestetico. "
                 "L'intervento dura in media venti minuti e si torna a casa "
                 "subito dopo, con una piccola medicazione."),
                ("Che differenza c'è tra estetica e dermatologia estetica?",
                 "La differenza è il medico. Nel nostro studio ogni trattamento "
                 "estetico — filler, tossina botulinica, peeling — è eseguito "
                 "personalmente da un dermatologo, mai delegato. Prima di ogni "
                 "trattamento estetico facciamo una visita dermatologica completa."),
                ("Posso portare i referti di un altro studio?",
                 "Sì, li leggiamo con attenzione. Se avete una mappatura digitale "
                 "precedente, portatela: il confronto cronologico fra immagini "
                 "prese con macchine diverse è possibile e utilissimo."),
                ("Come funziona il laser dermatologico?",
                 "Dipende dall'indicazione. Il laser CO2 frazionato lavora sulle "
                 "cicatrici e le cheratosi, il laser vascolare sulle lesioni dei "
                 "vasi superficiali. Ogni protocollo prevede una consulenza "
                 "preliminare gratuita con la dermatologa operatrice."),
            ],
        },

        # Bottom CTA band
        "cta_heading":
            "Un percorso che inizia <em>dalla prima visita.</em>",
        "cta_primary_label":   "Prenota una prima visita",
        "cta_secondary_label": "Contatti e indicazioni",

        # Treatment tabs — three clinical domains (boutique derm depth)
        "trattamenti_tabs": {
            "label":   "Aree di intervento",
            "heading": "Tre ambiti, <em>una sola direzione clinica.</em>",
            "intro":
                "Ogni ambito segue lo stesso metodo — consulenza preliminare, "
                "piano scritto, esecuzione dermatologica — e si integra con "
                "gli altri in un percorso continuo.",
            "tabs": [
                {
                    "id":       "clinica",
                    "label":    "Clinica",
                    "eyebrow":  "Dermatologia clinica",
                    "heading":  "Visite, mappature, monitoraggio.",
                    "body":
                        "La base dello studio. Prima visita approfondita, "
                        "mappatura digitale dei nevi con Fotofinder Vexia, "
                        "dermatoscopia e monitoraggio cronologico.",
                    "items": [
                        ("Prima visita dermatologica", "45 min · € 180"),
                        ("Mappatura digitale Fotofinder", "60 min · € 320"),
                        ("Controllo annuale", "30 min · € 140"),
                        ("Dermatologia pediatrica", "40 min · € 170"),
                    ],
                    "cta_label": "Tutte le visite cliniche →",
                    "cta_href":  "visite",
                },
                {
                    "id":       "chirurgia",
                    "label":    "Chirurgia",
                    "eyebrow":  "Chirurgia dermatologica",
                    "heading":  "Escissioni, laser CO2, correzioni.",
                    "body":
                        "Piccola chirurgia ambulatoriale in sala operatoria "
                        "certificata. Escissione di lesioni sospette con "
                        "esame istologico e sutura estetica dedicata.",
                    "items": [
                        ("Escissione di nevo", "30 min · € 420"),
                        ("Laser CO2 frazionato cicatrici", "60 min · € 520"),
                        ("Asportazione di cisti", "45 min · € 380"),
                        ("Correzione post-chirurgica", "40 min · € 290"),
                    ],
                    "cta_label": "Percorsi chirurgici →",
                    "cta_href":  "visite",
                },
                {
                    "id":       "estetica",
                    "label":    "Estetica",
                    "eyebrow":  "Dermatologia estetica",
                    "heading":  "Protocolli medici, mai estetisti.",
                    "body":
                        "Ogni trattamento è eseguito personalmente da una "
                        "dermatologa. Botulino, filler, peeling e laser "
                        "vascolari in un approccio conservativo e graduale.",
                    "items": [
                        ("Tossina botulinica terzo superiore", "20 min · da € 380"),
                        ("Filler acido ialuronico", "30 min · da € 420"),
                        ("Peeling chimico superficiale", "40 min · € 240"),
                        ("Laser vascolare", "30 min · da € 290"),
                    ],
                    "cta_label": "Protocolli estetici →",
                    "cta_href":  "visite",
                },
            ],
        },

        # Before / After comparison — hidden until clinically vetted patient
        # imagery is licensed (image-coherence pass: previous URLs depicted a
        # facial cupping treatment and a hairstylist team, neither acceptable
        # as a documented dermatologic result).
        "before_after": None,

        # Editorial / press feed — quadruple grid, square format
        "editorial_feed": {
            "label": "Dallo studio, nei mesi",
            "items": [
                ("https://images.unsplash.com/photo-1512290923902-8a9f81dc236c"
                 "?auto=format&fit=crop&w=800&q=80",
                 "Vogue Italia · marzo 2026",
                 "Intervista su patologie cutanee e menopausa"),
                ("https://images.unsplash.com/photo-1616394584738-fc6e612e71b9"
                 "?auto=format&fit=crop&w=800&q=80",
                 "Forum SIDeMaST 2026",
                 "Presentazione clinica su fotoprotezione pediatrica"),
                ("https://images.unsplash.com/photo-1620916566398-39f1143ab7be"
                 "?auto=format&fit=crop&w=800&q=80",
                 "Corriere Salute · febbraio",
                 "Consulenza sul percorso estetico medicalizzato"),
                ("https://images.unsplash.com/photo-1638202993928-7267aad84c31"
                 "?auto=format&fit=crop&w=800&q=80",
                 "Studio · gennaio 2026",
                 "Inaugurazione della nuova sala di chirurgia"),
            ],
        },
    },

    # ─── LO STUDIO (about) ─────────────────────────────────────
    "studio": {
        "eyebrow":  "Lo studio",
        "headline": "Diciotto anni di <em>dermatologia privata</em> integrata.",
        "intro":
            "Lo Studio Ricciardi nasce nel 2008 dall'idea che la dermatologia "
            "contemporanea non possa vivere di sole visite di controllo: servono "
            "tempo clinico, chirurgia dedicata e un ambulatorio estetico che parli "
            "la stessa lingua della diagnosi.",

        "history": [
            ("2008",
             "Apertura del primo studio in Via Veneto 116, tre stanze e una segretaria. "
             "La prima visita dermatologica viene erogata il 4 febbraio 2008."),
            ("2012",
             "Arriva la videodermatoscopia digitale FotoFinder ATBM, prima installazione "
             "in un privato romano. Le mappature nevi passano da cartacee ad archivio "
             "digitale incrementale, confrontabili anno dopo anno sulla stessa macchina."),
            ("2015",
             "Allestimento della sala chirurgica ambulatoriale dedicata, con anestesista "
             "esterno per gli interventi più complessi. Nasce il servizio di chirurgia "
             "dermatologica in day-hospital."),
            ("2019",
             "Arrivo del laser CO2 frazionato Lumenis UltraPulse e del laser vascolare "
             "Candela Vbeam Prima. Nasce l'area dermatologica laser, con protocolli "
             "dedicati a cicatrici, cheratosi attiniche e lesioni vascolari."),
            ("2024",
             "Ingresso della Dott.ssa Morelli come responsabile del percorso di medicina "
             "estetica dermatologica. L'estetica diventa, per la prima volta nello studio, "
             "un ambulatorio firmato da un dermatologo a tempo pieno."),
        ],

        "studio_image":
            "https://images.unsplash.com/photo-1620916566398-39f1143ab7be"
            "?auto=format&fit=crop&w=1400&q=80",
        "studio_image_caption": "Linea cosmeceutica · Studio Ricciardi, Roma",

        "method_title": "Metodo",
        "method_paragraphs": [
            "Una visita allo Studio Ricciardi inizia sempre da una domanda semplice:"
            "quando ha iniziato a notarla? Quella data è il nostro vero punto di "
            "partenza. Le lesioni cutanee non si leggono soltanto in sezione: si "
            "leggono nel tempo, confrontando fotografie, referti e sensazioni del paziente.",
            "Per ogni paziente costruiamo un archivio dermatoscopico digitale che "
            "accompagna la persona per tutta la vita: dalla prima visita in adolescenza "
            "fino ai controlli della maturità. Ogni nevo viene fotografato, catalogato "
            "e confrontato a ogni controllo successivo. È il cambiamento, non l'immagine "
            "isolata, a generare il sospetto clinico.",
            "La chirurgia dermatologica, quando indicata, viene eseguita in giornata, "
            "in anestesia locale, dallo stesso medico che ha posto l'indicazione. "
            "Il pezzo istologico viene affidato a un laboratorio specializzato in "
            "dermatopatologia, con il quale dialoghiamo direttamente al telefono "
            "per i casi di maggior complessità.",
        ],

        "values": [
            ("Precisione",       "Videodermatoscopia digitale per ogni paziente, a ogni controllo."),
            ("Prevenzione",      "Mappatura nevi annuale inserita d'ufficio in agenda dal secondo anno."),
            ("Tracciabilità",    "Archivio fotografico permanente, consegnabile al paziente in qualsiasi momento."),
            ("Estetica clinica", "Nessun trattamento estetico senza visita dermatologica preliminare."),
        ],

        # Values section label + heading
        "values_label":   "Cosa garantiamo",
        "values_heading": "Quattro impegni che <em>non cambiano mai.</em>",

        # Bottom CTA band
        "cta_heading":
            "Vuoi conoscere le dermatologhe dello studio <em>prima di prenotare?</em>",
        "cta_primary_label":   "Le tre dermatologhe dello studio →",
        "cta_secondary_label": "Richiedi visita privata →",
    },

    # ─── VISITE (services) ─────────────────────────────────────
    "visite": {
        "eyebrow":  "Le visite",
        "headline": "Sei percorsi clinici, <em>una sola cartella.</em>",
        "intro":
            "Ogni visita allo Studio Ricciardi è un percorso clinico definito, "
            "con una durata, un costo e un piano di follow-up scritti. "
            "Nessun forfait nascosto, nessun preventivo a voce.",

        "service_image":
            "https://images.unsplash.com/photo-1612349316228-5b7717e1404e"
            "?auto=format&fit=crop&w=1400&q=80",
        "service_image_caption": "Videodermatoscopia digitale · Studio Ricciardi",

        "treatments": [
            ("Visita dermatologica completa",
             "40 min · prima visita",
             "Anamnesi estesa, esame obiettivo della cute su tutto il corpo (compresi "
             "cuoio capelluto, cavo orale e area genitale), dermatoscopia manuale, "
             "refertazione personale e piano di follow-up scritto.",
             "€ 180"),
            ("Mappatura nevi digitale",
             "60 min · FotoFinder ATBM",
             "Videodermatoscopia ad alta risoluzione di tutti i nevi, archiviazione "
             "digitale, confronto con l'archivio storico, relazione scritta con il "
             "dettaglio delle lesioni a rischio.",
             "€ 240"),
            ("Chirurgia dermatologica ambulatoriale",
             "Su indicazione · day-hospital",
             "Escissione di lesioni sospette in anestesia locale, esame istologico "
             "eseguito da laboratorio specializzato in dermatopatologia, refertazione "
             "entro otto giorni lavorativi con consulto telefonico dedicato.",
             "da € 320"),
            ("Laser CO2 frazionato",
             "45 min · singola seduta",
             "Trattamento di cicatrici, rughe periorali, macchie solari e cheratosi "
             "attiniche con sistema Lumenis UltraPulse. Prima seduta sempre dopo "
             "visita dermatologica dedicata.",
             "€ 420"),
            ("Peeling medico dermatologico",
             "30 min · ciclo 4 sedute",
             "Peeling superficiali e medi (TCA, mandelico, salicilico, fenolo "
             "diluito) eseguiti personalmente dalla dermatologa, con protocollo "
             "individualizzato per fototipo e danno attinico.",
             "€ 260 / seduta"),
            ("Percorso prevenzione annuale",
             "Annuale · 3 incontri",
             "Visita dermatologica completa, mappatura nevi digitale con confronto "
             "storico, consulto fotoprotettivo personalizzato, canale diretto con "
             "il medico per urgenze minori durante l'anno.",
             "€ 580"),
        ],

        "footnote":
            "Tutti i pagamenti sono detraibili come spese sanitarie. Lo studio "
            "rilascia ricevuta sanitaria con marca da bollo. I preventivi per "
            "chirurgia dermatologica sono sempre scritti e firmati dal medico in "
            "anticipo, comprensivi di eventuali esami istologici e visite di follow-up.",

        "footnote_heading": "Note amministrative",

        # Bottom CTA band
        "cta_heading":
            "Una visita allo Studio Ricciardi è <em>preparata personalmente</em>.",
        "cta_primary_label":   "Modulo di richiesta →",
        "cta_secondary_label": "Numero diretto della segreteria →",
    },

    # ─── MEDICI (team) ─────────────────────────────────────────
    "medici": {
        "eyebrow":  "I medici",
        "headline": "Tre firme, una sola <em>sala operatoria.</em>",
        "intro":
            "Lo studio è composto da tre dermatologhe che condividono cartelle, "
            "archivio dermatoscopico e protocollo clinico. Ogni paziente, però, "
            "ha sempre una sola dermatologa di riferimento.",

        "portrait_city": "Roma · Via Veneto",

        "doctors": [
            {
                "name":  "Dott.ssa Alessandra Ricciardi",
                "role":  "Direttore clinico · Dermatologa",
                "tags":  ["Dermoscopia avanzata", "Tumori cutanei", "Dermatologia clinica"],
                "bio":
                    "Specialista in dermatologia e venereologia all'Università Cattolica "
                    "del Sacro Cuore di Roma, perfezionata in dermoscopia avanzata al "
                    "Memorial Sloan Kettering di New York. Membro SIDeMaST, EADV e "
                    "International Dermoscopy Society. Autrice di oltre cinquanta "
                    "pubblicazioni indicizzate, fra cui due capitoli del trattato Bolognia-Italia.",
                "portrait":
                    "https://images.unsplash.com/photo-1638202993928-7267aad84c31"
                    "?auto=format&fit=crop&w=900&q=80",
                "links": [
                    ("PubMed", "#"),
                    ("ORCID",  "#"),
                ],
            },
            {
                "name":  "Dott. Emanuele Vitali",
                "role":  "Dermatologo · Chirurgia dermatologica",
                "tags":  ["Chirurgia ambulatoriale", "Plastica ricostruttiva", "Dermatopatologia"],
                "bio":
                    "Specialista al Policlinico Gemelli di Roma, perfezionato in chirurgia "
                    "dermatologica alla Charité di Berlino. Dal 2015 responsabile della "
                    "sala chirurgica ambulatoriale dello studio. Consulente chirurgico "
                    "per due reparti dermatologici universitari romani.",
                "portrait":
                    "https://images.unsplash.com/photo-1612531385446-f7e6d131e1d0"
                    "?auto=format&fit=crop&w=900&q=80",
                "links": [
                    ("Curriculum", "#"),
                ],
            },
            {
                "name":  "Dott.ssa Caterina Morelli",
                "role":  "Dermatologa · Estetica & Laser",
                "tags":  ["Laser CO2", "Medicina estetica", "Peeling medici"],
                "bio":
                    "Specialista all'Università di Padova, dottorato di ricerca in "
                    "dermatologia estetica. Perfezionata in laserterapia al Wellman "
                    "Center di Boston. Dal 2024 responsabile del percorso di medicina "
                    "estetica dermatologica dello Studio Ricciardi. Nessuna delega a "
                    "personale non medico.",
                "portrait":
                    "https://images.unsplash.com/photo-1559839734-2b71ea197ec2"
                    "?auto=format&fit=crop&w=900&q=80",
                "links": [
                    ("Pubblicazioni", "#"),
                ],
            },
        ],
    },

    # ─── PUBBLICAZIONI (blog list / detail) ────────────────────
    "pubblicazioni": {
        "eyebrow":  "Pubblicazioni & approfondimenti",
        "headline": "Lavori scientifici, <em>letture critiche</em>, divulgazione dermatologica.",
        "intro":
            "Una selezione dei lavori dello studio e dei testi divulgativi scritti "
            "per il pubblico generale. Tutti i contenuti sono rivisti personalmente "
            "dalla Dott.ssa Ricciardi prima della pubblicazione.",

        # Lead post background image (blog_list hero)
        "lead_image":
            "https://images.unsplash.com/photo-1620916566398-39f1143ab7be"
            "?auto=format&fit=crop&w=900&q=80",

        # Blog-detail footer strap + fallback body
        "footer_strap": "Studio Ricciardi · Dermatologia integrata",
        "empty_body_fallback_paragraphs": [
            "Articolo in preparazione editoriale. La pubblicazione integrale sarà "
            "disponibile a breve.",
            "Questo segnaposto descrive la voce dell'articolo: una nota clinica "
            "scritta dalla dermatologa, in tono diretto e privo di tecnicismi, "
            "pensata per pazienti e familiari che cercano informazioni affidabili.",
        ],
    },

    "posts": [
        {
            "slug":     "mappatura-nei-quando-farla",
            "kicker":   "Prevenzione",
            "title":    "Mappatura nevi: ogni quanto farla davvero",
            "date":     "18 marzo 2026",
            "read_min": 7,
            "author":   "Dott.ssa Alessandra Ricciardi",
            "lede":
                "La domanda più frequente in ambulatorio è anche quella con la "
                "risposta più sfumata. Non esiste una frequenza universale: esiste "
                "il tuo fototipo, il tuo archivio e la tua storia familiare.",
            "body": [
                ("p", "Ogni anno in Italia vengono diagnosticati circa quindicimila nuovi casi "
                      "di melanoma cutaneo. È il tumore della pelle con la più alta letalità e, "
                      "allo stesso tempo, quello con la prognosi migliore quando preso in tempo. "
                      "Il confine fra queste due realtà si chiama dermoscopia digitale seriata."),
                ("h2", "Le tre categorie di rischio"),
                ("ol", [
                    "Paziente senza familiarità, pochi nevi (meno di 30), fototipo II-III: mappatura ogni 24 mesi.",
                    "Paziente con molti nevi (oltre 50), fototipo chiaro o pregresse scottature solari in età infantile: mappatura annuale.",
                    "Paziente con familiarità di primo grado per melanoma o nevo sospetto in archivio: mappatura ogni sei-dodici mesi."
                ]),
                ("p", "Le frequenze indicate non sono regole rigide: ogni dermatologo le "
                      "adatta al singolo paziente. Quello che conta è che la mappatura non "
                      "sia una prestazione isolata, ma un atto clinico ripetuto nel tempo — "
                      "con le stesse macchine, lo stesso medico e lo stesso archivio digitale."),
                ("h2", "Cosa significa 'archivio digitale'"),
                ("p", "Significa che ogni nevo viene fotografato in videodermatoscopia ad alta "
                      "risoluzione e archiviato con coordinate cutanee precise. A ogni controllo "
                      "successivo il medico non guarda un nevo nuovo: confronta la stessa foto "
                      "con quella dell'anno precedente. È il cambiamento, non l'immagine isolata, "
                      "a generare il sospetto clinico."),
                ("blockquote",
                 "La mappatura nevi non serve a cercare un melanoma. Serve a sapere, di ogni "
                 "lesione, come era l'anno scorso. È un atto di memoria clinica, prima che di diagnosi."),
                ("p", "Per i nuovi pazienti la prima mappatura è sempre un atto fondativo: "
                      "le fotografie di oggi diventano il metro di confronto per i prossimi "
                      "dieci anni. Vale la pena dedicarci un'ora di tempo clinico, e metà "
                      "della prima visita ne è dedicata."),
            ],
        },
        {
            "slug":     "chirurgia-dermatologica-ambulatoriale",
            "kicker":   "Chirurgia dermatologica",
            "title":    "Chirurgia dermatologica in day-hospital: cosa aspettarsi davvero",
            "date":     "2 marzo 2026",
            "read_min": 5,
            "author":   "Dott. Emanuele Vitali",
            "lede":
                "Le escissioni dermatologiche ambulatoriali fanno paura solo fino "
                "al momento dell'anestesia. Dopo, nel 95% dei casi, il paziente esce "
                "dallo studio con la stessa camminata con cui è entrato.",
        },
        {
            "slug":     "laser-co2-cicatrici",
            "kicker":   "Laser dermatologico",
            "title":    "Laser CO2 frazionato: quando è la scelta giusta per le cicatrici",
            "date":     "15 febbraio 2026",
            "read_min": 6,
            "author":   "Dott.ssa Caterina Morelli",
            "lede":
                "Il laser CO2 frazionato non cancella le cicatrici: le rimodella. "
                "Capire questa distinzione è il primo passo verso una scelta "
                "realistica e priva di aspettative irrealizzabili.",
        },
        {
            "slug":     "fotoprotezione-quotidiana",
            "kicker":   "Prevenzione",
            "title":    "Fotoprotezione quotidiana: le tre regole che davvero contano",
            "date":     "28 gennaio 2026",
            "read_min": 4,
            "author":   "Dott.ssa Alessandra Ricciardi",
            "lede":
                "Un SPF 50 applicato in quantità sbagliata vale un SPF 15 applicato "
                "bene. Dopo quindicimila visite dermatologiche, l'80% dei pazienti "
                "sbaglia sempre lo stesso passaggio.",
        },
        {
            "slug":     "medicina-estetica-dermatologica",
            "kicker":   "Estetica clinica",
            "title":    "Perché allo Studio Ricciardi l'estetica la fa solo il dermatologo",
            "date":     "10 gennaio 2026",
            "read_min": 5,
            "author":   "Dott.ssa Caterina Morelli",
            "lede":
                "La medicina estetica dermatologica non è un mestiere da delegare. "
                "Una scelta netta che raccontiamo ai pazienti alla prima visita, "
                "senza giri di parole.",
        },
    ],

    # ─── CONTATTI (contact) ────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contatti",
        "headline": "Una sola segreteria, <em>una sola persona</em> dall'altra parte del filo.",
        "intro":
            "Lo studio risponde personalmente alle telefonate dal lunedì al venerdì. "
            "La segreteria clinica è gestita dalla Sig.ra Bianca Martelli, che "
            "conosce ogni cartella e ogni paziente per nome da oltre dieci anni.",

        "blocks": [
            ("Indirizzo",   "Via Veneto 116", "00187 Roma · interno 3, scala A"),
            ("Telefono",    "+39 06 487 2311",   "Risposta diretta 10:00 – 20:00"),
            ("Email",       "studio@ricciardidermatologia.it", "Risposta entro 24 ore lavorative"),
            ("Urgenze",     "+39 339 221 7080",  "Linea riservata pazienti in carico"),
        ],

        "hours": [
            ("Lunedì",     "10:00 – 14:00", "15:30 – 20:00"),
            ("Martedì",    "10:00 – 14:00", "15:30 – 20:00"),
            ("Mercoledì",  "10:00 – 14:00", "15:30 – 20:00"),
            ("Giovedì",    "10:00 – 14:00", "15:30 – 20:00"),
            ("Venerdì",    "10:00 – 14:00", "15:30 – 19:00"),
            ("Sabato",     "Chirurgia su agenda", "Solo interventi programmati"),
            ("Domenica",   "Chiuso", "—"),
        ],

        "transport": [
            ("Metro",   "Linea A · fermata Barberini, 7 minuti a piedi"),
            ("Auto",    "Parcheggio convenzionato Saba Ludovisi, ingresso da Via Sicilia"),
            ("Treno",   "Stazione Termini · 11 minuti in taxi"),
        ],

        "form_title": "Scrivi allo studio",
        "form_intro":
            "Per richieste non urgenti — informazioni sulle visite, costi, "
            "preparazione alla mappatura — scrivici qui sotto. Risponde "
            "personalmente la segreteria clinica.",

        "hours_heading":     "Orari di apertura",
        "transport_heading": "Come raggiungerci",

        "form_placeholders": {
            "first_name": "Maria",
            "last_name":  "Bianchi",
            "email":      "maria.bianchi@email.it",
            "phone":      "+39 335 ...",
            "subject":    "Informazioni sulla prima visita dermatologica",
            "message":
                "Resta in poche righe — la segreteria ti contatta "
                "entro 24 ore lavorative.",
        },
        "form_helpers": {
            "first_name": "Solo nome di battesimo.",
            "last_name":  "Come appare sulla tessera sanitaria.",
            "email":      "Usiamo l'email solo per rispondere: niente newsletter.",
            "phone":      "Opzionale. Solo se preferisci essere richiamata.",
            "subject":    "Un titolo breve aiuta a smistare la richiesta.",
            "message":    "Resta nelle dieci righe — Bianca risponde entro 24 ore lavorative.",
        },
        "form_consent":
            "Acconsento al trattamento dei dati personali secondo l'informativa privacy "
            "(Reg. UE 679/2016). I dati restano custoditi dallo studio e non sono comunicati a terzi.",
        "form_submit_note":
            "Risposta entro 24 ore lavorative · archivio clinico riservato al medico curante.",
    },

    # ─── RICHIEDI VISITA (appointment) ─────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Richiesta visita dermatologica",
        "headline": "Una visita dermatologica <em>non si prenota</em>: si prepara.",
        "intro":
            "Non esiste un calendario online. Lo studio riserva ogni prima visita "
            "dopo aver letto una breve descrizione del caso. Le richieste vengono "
            "valutate personalmente dal medico entro 48 ore lavorative.",

        "process_label":   "Come funziona",
        "process_heading":
            "Quattro passaggi, in <em>quarantotto ore lavorative.</em>",

        "process": [
            ("01", "Compila il modulo",
             "Bastano dieci righe per inquadrare la tua richiesta. Se hai lesioni "
             "sospette, aggiungi una fotografia: aiuta a valutare la priorità in anticipo."),
            ("02", "Lettura clinica",
             "Il medico legge personalmente la richiesta entro 48 ore lavorative e "
             "valuta se la prima visita è di dermatologia clinica, chirurgica o estetica."),
            ("03", "Proposta di appuntamento",
             "La segreteria propone due fasce orarie compatibili con le tue esigenze "
             "e con la durata della visita (40 min per la generale, 60 min per la "
             "mappatura nevi completa)."),
            ("04", "Conferma e preparazione",
             "Ricevi via email l'elenco di cosa portare (esami precedenti, foto di "
             "lesioni, terapia in corso) e le indicazioni pratiche per la visita — "
             "struccata e senza smalto se prevista mappatura."),
        ],

        "form_title": "Modulo di richiesta",
        "form_band_side_note":
            "Riserva qualche minuto. Le richieste preparate con cura sono lette "
            "dalla dermatologa per intero — quelle frettolose, no.",
        "form_band_side_note_small": "↓ Modulo riservato",

        "form_fields": [
            {"name": "name", "label": "Nome e cognome", "placeholder": "Maria Bianchi",
             "type": "text", "required": True, "full_width": False,
             "helper": "Come sulla tessera sanitaria."},
            {"name": "email", "label": "Email", "placeholder": "maria@email.it",
             "type": "email", "required": True, "full_width": False,
             "helper": "La proposta di appuntamento arriva qui."},
            {"name": "phone", "label": "Telefono", "placeholder": "+39 335 ...",
             "type": "tel", "required": True, "full_width": False,
             "helper": "Bianca può richiamare per confermare."},
            {"name": "age", "label": "Età", "placeholder": "38",
             "type": "number", "required": False, "full_width": False,
             "helper": "Facoltativa."},
            {"name": "visit_type", "label": "Tipo di visita", "type": "select",
             "required": True, "full_width": False,
             "options": ["Visita dermatologica", "Mappatura nevi",
                         "Chirurgia dermatologica", "Medicina estetica"],
             "helper": "Se non sei sicura, scegli Visita dermatologica."},
            {"name": "availability", "label": "Disponibilità preferite", "type": "select",
             "required": True, "full_width": False,
             "options": ["Mattina", "Pomeriggio", "Indifferente"],
             "helper": "Serve solo ad allineare le due proposte di orario."},
            {"name": "referring_doctor", "label": "Medico curante", "placeholder": "Dr. ...",
             "type": "text", "required": False, "full_width": True,
             "helper": "Se sei inviata da un collega, indica il suo nome."},
            {"name": "case_description", "label": "Breve descrizione del caso",
             "placeholder":
                 "Motivo della visita, lesioni di interesse, sintomi recenti, "
                 "terapie in corso. Resta nelle dieci righe.",
             "type": "textarea", "required": True, "full_width": True,
             "helper": "Le richieste lette dalla dermatologa sono quelle preparate con cura."},
        ],

        "form_sections": [
            {"num": "01", "title": "Chi sei",
             "meta": "Queste righe arrivano direttamente a Bianca in segreteria.",
             "fields": ["name", "email", "phone", "age"]},
            {"num": "02", "title": "Che tipo di visita",
             "meta": "Allinea la richiesta al perimetro dello studio.",
             "fields": ["visit_type", "availability", "referring_doctor"]},
            {"num": "03", "title": "Fotografie o esami utili (facoltativi)",
             "meta": "Se hai lesioni sospette, una o due foto ben illuminate "
                     "aiutano a valutare la priorità in anticipo.",
             "fields": ["__upload__"]},
            {"num": "04", "title": "Descrivi il caso",
             "meta": "Dieci righe bastano. La dermatologa legge personalmente.",
             "fields": ["case_description"]},
        ],

        "upload_field": {
            "name":       "dermatologia_allegati",
            "label":      "Fotografie e referti",
            "helper":     "JPG, PNG o PDF · fino a 5 file, massimo 10 MB complessivi. "
                          "Custoditi nell'archivio digitale cifrato dello studio.",
            "accept":     ".pdf,.jpg,.jpeg,.png",
            "multiple":   True,
            "primary":    "Trascina qui foto e referti oppure",
            "link":       "sfoglia i tuoi documenti",
            "meta":       "JPG / PNG / PDF · max 10 MB",
        },

        "submit_label": "Invia richiesta",

        "form_submit_note":
            "La dermatologa legge ogni richiesta entro 48 ore lavorative. "
            "Fotografie e referti restano nell'archivio cifrato dello studio.",

        "consent":
            "Acconsento al trattamento dei dati personali secondo l'informativa "
            "privacy ai sensi del Regolamento UE 679/2016. I dati clinici e le "
            "fotografie dermatoscopiche sono custoditi in archivio digitale cifrato "
            "con accesso limitato al medico curante.",

        "footnote":
            "Lo studio non risponde a richieste anonime e non rilascia opinioni "
            "cliniche via email senza visita. Per informazioni amministrative "
            "(costi, orari, parcheggio) usa la pagina contatti.",
    },
}


# ---------------------------------------------------------------------------
# Top-level registry (locale-keyed per Phase 2i.1 — Session 23)
# ---------------------------------------------------------------------------
# Each entry is `{locale: content_tree}`. `it` is always authoritative.
# Cardio ships with 5 locales (it/en/fr/es/ar) — the 4 non-IT blocks live
# in `template_content_cardio_i18n.py` so this file stays browsable.
# Dermatologia ships with 5 locales as of Session 24 (Phase 2i.2).
# Gusto ships with 5 locales as of Session 29 (Phase 2i.2 step 2) — the 4
# non-IT blocks live in `template_content_gusto_i18n.py` alongside a new
# `.fd-*` RTL CSS block in the fine-dining _base.html.
# ---------------------------------------------------------------------------

from apps.catalog.template_content_cardio_i18n import (  # noqa: E402
    CARDIO_CONTENT_EN,
    CARDIO_CONTENT_FR,
    CARDIO_CONTENT_ES,
    CARDIO_CONTENT_AR,
)

from apps.catalog.template_content_dermatologia_i18n import (  # noqa: E402
    DERMATOLOGIA_CONTENT_EN,
    DERMATOLOGIA_CONTENT_FR,
    DERMATOLOGIA_CONTENT_ES,
    DERMATOLOGIA_CONTENT_AR,
)

from apps.catalog.template_content_gusto_i18n import (  # noqa: E402
    GUSTO_CONTENT_EN,
    GUSTO_CONTENT_FR,
    GUSTO_CONTENT_ES,
    GUSTO_CONTENT_AR,
)

# Phase 2g3.3 — Business live rollout (Session 32). Pragma + Elevate
# ship IT-only at promotion time; the i18n keys can be added later via
# the same recipe used for cardio/derm/gusto (Sessions 23/24/29).
from apps.catalog.template_content_pragma import PRAGMA_CONTENT_IT  # noqa: E402
from apps.catalog.template_content_elevate import ELEVATE_CONTENT_IT  # noqa: E402


TEMPLATE_CONTENT: dict[str, dict[str, dict[str, Any]]] = {
    "cardio-studio-specialistico": {
        "it": CARDIO_CONTENT_IT,
        "en": CARDIO_CONTENT_EN,
        "fr": CARDIO_CONTENT_FR,
        "es": CARDIO_CONTENT_ES,
        "ar": CARDIO_CONTENT_AR,
    },
    "dermatologia-elite-roma": {
        "it": DERMATOLOGIA_CONTENT_IT,
        "en": DERMATOLOGIA_CONTENT_EN,
        "fr": DERMATOLOGIA_CONTENT_FR,
        "es": DERMATOLOGIA_CONTENT_ES,
        "ar": DERMATOLOGIA_CONTENT_AR,
    },
    "gusto-fine-dining": {
        "it": GUSTO_CONTENT_IT,
        "en": GUSTO_CONTENT_EN,
        "fr": GUSTO_CONTENT_FR,
        "es": GUSTO_CONTENT_ES,
        "ar": GUSTO_CONTENT_AR,
    },
    "pragma-corporate-suite": {
        "it": PRAGMA_CONTENT_IT,
    },
    "elevate-startup-landing": {
        "it": ELEVATE_CONTENT_IT,
    },
}


# ---------------------------------------------------------------------------
# Helpers — all locale-aware. `locale` defaults to the pilot default (it).
# ---------------------------------------------------------------------------

def has_live_template(slug: str) -> bool:
    """Whether a template has full multi-page live preview content."""
    return slug in TEMPLATE_CONTENT


def _resolve(slug: str, locale: str | None) -> dict[str, Any] | None:
    """Return the locale-specific content block for a slug, or None."""
    entry = TEMPLATE_CONTENT.get(slug)
    if not entry:
        return None
    return template_i18n.pick_localized(entry, locale or template_i18n.DEFAULT_LOCALE)


def get_content(slug: str, locale: str | None = None) -> dict[str, Any] | None:
    """Return the content block for a template in the requested locale.

    Falls back to IT when the requested locale is missing — every template
    is guaranteed to have an `it` entry, so a locale miss always renders.
    """
    return _resolve(slug, locale)


def get_pages(slug: str, locale: str | None = None) -> list[dict[str, str]]:
    """Return the page navigation list for a template (locale-aware)."""
    block = _resolve(slug, locale)
    return block["pages"] if block else []


def find_page(slug: str, page_slug: str, locale: str | None = None) -> dict[str, str] | None:
    """Find the page dict for a given page slug, or None if missing."""
    for page in get_pages(slug, locale):
        if page["slug"] == page_slug:
            return page
    return None


def find_post(slug: str, post_slug: str, locale: str | None = None) -> dict[str, Any] | None:
    """Find a single blog/news post by slug (locale-aware)."""
    block = _resolve(slug, locale)
    if not block:
        return None
    for post in block.get("posts", []):
        if post["slug"] == post_slug:
            return post
    return None
