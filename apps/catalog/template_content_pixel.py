"""Pixel — Portfolio Fotografico (portfolio / cinematic-photographer archetype) content.

Phase 2g3.4 — Portfolio live rollout (Session 34, 2026-04-13).

Editorial identity: independent author photographer based between Milan
and Trieste, working in long-form reportage, editorial portrait and
brand commission. The voice is silent, slow, atmospheric — references
specific cameras, film stocks, light conditions, locations.
Photo direction is cinematic photostill (low-key reportage, still-life
gravity, portrait introspection), never glossy or staged.

Differentiation vs Chiara (10-gate D-054 — recorded here for reviewers):
 1. Hero image:        fullbleed cinematic dominant photo
                       vs Chiara's typographic-only ledger hero.
 2. First-2 imagery:   moody hero + filmstrip stills (photographer-pool)
                       vs Chiara's sketchbook + paste-up close-ups.
 3. Silhouette:        transparent dark nav + fullbleed-cover hero
                       vs Chiara hairline-rule + typographic-ledger hero.
 4. Section order:     hero → filmstrip → bio-excerpt → publications → contact
                       vs Chiara hero → ledger → ribbon → capabilities → commissions.
 5. Primary CTA:       "Apri la serie" + bracket-mono CTA on dark
                       vs Chiara "Richiedi il portfolio completo" + ghost-rule.
 6. Block rhythm:      compact image-dense
                       vs Chiara very-airy editorial chapters.
 7. Macro tone:        near-black + warm grey + accent pulse
                       vs Chiara cream paper + ink + accent rule.
 8. Imagery direction: cinematic photostill (low-key, observational)
                       vs Chiara studio work-in-progress (sketchbooks/paste-ups).
 9. Typography:        Archivo (geometric, technical) + Inter
                       vs Chiara Syne (display, designer-bookshelf) + Inter.
10. Inner pages:       series index + exhibitions + bio + commissioning
                       vs Chiara project ledger + design notes + capabilities.

Page kinds:
- home, series_list, series_detail, about (kind: about),
  publications (kind: publications), contact (kind: contact)
"""
from __future__ import annotations

from typing import Any


PIXEL_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Indice",        "kind": "home"},
        {"slug": "serie",         "label": "Serie",         "kind": "series_list"},
        {"slug": "biografia",     "label": "Biografia",     "kind": "about"},
        {"slug": "pubblicazioni", "label": "Pubblicazioni", "kind": "publications"},
        {"slug": "contatti",      "label": "Contatto",      "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial":   "P",
        "logo_word":      "Pixel — Lorenzo Bianchi",
        "logo_short":     "PXL",
        "tag":            "Fotografo autoriale · Milano · Trieste",
        "phone":          "+39 348 211 7720",
        "email":          "studio@lorenzobianchi.photo",
        "address":        "Via Tadino 18 · 20124 Milano",
        "hours_compact":  "Disponibile per commissioni · 2026 — 27",
        "license":        "Iscrizione Tau · Albo Fotografi Professionisti n. 4421/2014",
        "footer_intro":
            "Fotografo autoriale indipendente. Reportage di lungo "
            "respiro, ritratto editoriale e commissioni di marca per "
            "case editrici, gallerie e maison di moda. Rappresentato "
            "da Galleria Carla Sozzani per la stampa fine art.",
        # Primary nav bracket CTA (right-side) — lifted Session 39 per D-047
        "nav_cta":       "Apri conversazione",
        "foot_studio":   "Lo studio",
        "foot_pages":    "Indice",
        "foot_contact":  "Contatto",
        "foot_kit":      "Equipaggiamento",
        # EXIF-style footer cells
        "exif_footer": [
            ("Sede",        "Milano · Trieste"),
            ("Disponibile", "Commissioni 2026 — 27"),
            ("Rappresentanza", "Galleria Carla Sozzani · Milano"),
            ("Stampa",      "Atelier Druckwerkstatt · Berlino"),
        ],
        # Footer kit column rows (per-tenant — never inline in skin per D-047)
        "kit_footer_rows": [
            "Mamiya 7II · Sony α7R V",
            "Kodak Portra 400",
            "Stampa · Druckwerkstatt Berlino",
        ],
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        # Series counter chip (top-left of hero)
        "series_counter_label": "Serie corrente",
        "series_counter_value": "07 / 24",

        # Status pulse on nav (right side)
        "status_pulse": "Disponibile · 2026 — 27",

        # Eyebrow + headline
        "eyebrow":   "Fotografia autoriale · 2014 — 2026",
        # All-caps cinematic hero per archetype
        "headline":  "OSSERVARE COSA RESTA <em>quando la luce cambia</em>",
        "subhead":
            "Reportage di lungo respiro, ritratto editoriale e "
            "commissioni di marca. Lavoro a pellicola medio formato "
            "e in digitale a doppio sensore — per progetti che "
            "chiedono dieci giorni o tre anni di tempo.",
        "primary_cta":   "Apri la serie completa",
        "primary_href":  "serie",
        "secondary_cta": "Disponibilità 2026",
        "secondary_href":"contatti",

        # Hero image — fullbleed dominant
        "hero_image":
            "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
        "hero_image_alt":
            "Vista dal porto di Trieste alle 6:14 del mattino · "
            "novembre 2025 · pellicola Kodak Portra 400",

        # EXIF credit cells under hero (4-cell mono bar)
        "hero_credit_cells": [
            ("Camera",   "Mamiya 7II"),
            ("Pellicola","Kodak Portra 400"),
            ("Luogo",    "Porto Vecchio · Trieste"),
            ("Data",     "Novembre 2025"),
        ],

        # Featured series (filmstrip on home — 4 series)
        "filmstrip_label":   "Lavoro recente",
        "filmstrip_heading": "QUATTRO SERIE · 2024 — 2026",
        "filmstrip_intro":
            "Quattro lavori di lungo periodo chiusi negli ultimi due anni. "
            "Le serie complete sono accessibili nella sezione Serie — "
            "ogni serie comprende fra le venti e le quaranta immagini.",
        # Each: (num, title, discipline, year, slug-for-link)
        "filmstrip": [
            ("07", "Porto Vecchio · Trieste",
             "Reportage di lungo respiro", "2024 — 2026",
             "porto-vecchio-trieste"),
            ("06", "Atelier Velluti & Co.",
             "Commissione editoriale", "2025",
             "atelier-velluti"),
            ("05", "Le case di pietra",
             "Reportage architettonico", "2023 — 2024",
             "case-di-pietra-puglia"),
            ("04", "Ritratti del Po",
             "Ritratto autoriale", "2023",
             "ritratti-del-po"),
        ],

        # Reel — REMOVED per D-068 (Session 36).
        # A short-film claim without a real signed MP4 shipped as a placeholder
        # contradicts the cinematic-photographer identity; the "Play · 3:12" +
        # "Reel · 1080p · 24 fps" meta also trespassed into codec-theatre.
        # Lorenzo's identity is stills — the filmstrip + EXIF cells + series
        # index already carry the cinematic voice. When a genuine Carso reel
        # exists, this block can return with a real `src` and meta pruned of
        # pseudo-technical cues.

        # About excerpt — 3 sentences (full bio on /biografia)
        "about_label":   "Note autobiografiche",
        "about_heading": "LORENZO BIANCHI",
        "about_excerpt":
            "Nato a Trieste nel 1986, vivo fra Milano e il Carso "
            "triestino. Ho cominciato fotografando i mercati di Sarajevo "
            "nel 2009 e da allora non ho cambiato disciplina — solo "
            "tempi, luce e formato. Lavoro a pellicola Kodak Portra 400 "
            "in medio formato per il personale, in digitale doppio sensore "
            "Sony per le commissioni.",
        "about_cta":     "Leggi la biografia",
        "about_cta_href":"biografia",

        # Recent publications strip (3 selected)
        "publications_label":   "Pubblicato recentemente",
        "publications_heading": "STAMPA & EDITORIA · 2025",
        "publications": [
            ("FOAM Magazine n. 64",
             "Portfolio di otto pagine sulla serie «Porto Vecchio»",
             "Novembre 2025"),
            ("Internazionale n. 1612",
             "Reportage illustrato sulle case di pietra del Salento",
             "Settembre 2025"),
            ("Domus n. 1102",
             "Commissione editoriale per il numero monografico Carlo Scarpa",
             "Aprile 2025"),
        ],

        # Final CTA band — commission inquiry
        "cta_label":   "Commissioni · disponibilità 2026 — 2027",
        "cta_heading": "[ APRI UNA CONVERSAZIONE ]",
        "cta_intro":
            "Sono disponibile per commissioni editoriali, ritratto "
            "autoriale e progetti di lunga durata fino a settembre "
            "2027. Le commissioni di marca sono valutate caso per "
            "caso — preferisco i mandati con tempo lungo.",
        "cta_primary":      "Scrivi una breve",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Vai alla rappresentanza",
        "cta_secondary_href":"biografia",
    },

    # ─── SERIE (series_list) ────────────────────────────────────
    "serie": {
        "series_counter_label": "Archivio",
        "series_counter_value": "24 SERIE",
        "status_pulse":         "Disponibile · 2026 — 27",

        "eyebrow":   "Archivio delle serie · 2009 — 2026",
        "headline":  "VENTIQUATTRO SERIE, <em>una sola disciplina</em>",
        "subhead":
            "L'archivio completo delle serie firmate. Reportage di "
            "lungo respiro, ritratto autoriale, commissioni editoriali. "
            "La selezione mostrata copre i lavori più recenti — "
            "le serie storiche (2009 — 2018) sono accessibili su "
            "richiesta per studio o pubblicazione.",

        # Discipline filter pills
        "filter_label": "Discipline",
        "filters": [
            "Tutte",
            "Reportage di lungo respiro",
            "Ritratto autoriale",
            "Commissione editoriale",
            "Reportage architettonico",
        ],

        # Index intro band
        "index_label": "Selezione 2018 — 2026",
        "index_intro":
            "Cliccare la copertina per aprire la serie completa. "
            "Ogni serie comprende fra le venti e le quaranta immagini, "
            "con apparato critico e EXIF di scatto.",

        # CTA before footer
        "cta_label":   "Cercate qualcosa di specifico?",
        "cta_heading": "[ ARCHIVIO RISERVATO · STAMPA & STUDIO ]",
        "cta_intro":
            "Per accedere all'archivio storico (2009 — 2018), per "
            "richieste di stampa fine art, o per commissionare un nuovo "
            "lavoro: aprite una conversazione preliminare.",
        "cta_primary":      "Scrivi al fotografo",
        "cta_primary_href": "contatti",

        # Chrome labels shared by serie card + series_detail page.
        # Lifted Session 39 (D-047 lift) — same labels across every post,
        # so they live on the parent serie block rather than on each post.
        "card_arrow_label":        "apri serie",
        "post_discipline_label":   "Disciplina",
        "post_period_label":       "Periodo",
        "post_location_label":     "Luogo",
        "post_frames_label":       "Frame",
        "post_gallery_label":      "Galleria",
        "post_edition_label":      "Edizione",
    },

    # ─── BIOGRAFIA (about) ──────────────────────────────────────
    "biografia": {
        "series_counter_label": "Note autobiografiche",
        "series_counter_value": "1986 — 2026",
        "status_pulse":         "Sede · Milano + Trieste",

        "eyebrow":   "Note autobiografiche · 1986 — 2026",
        "headline":  "LORENZO BIANCHI <em>fotografo autoriale</em>",
        "subhead":
            "Nato a Trieste nel 1986, vivo fra Milano e il Carso "
            "triestino. Ho cominciato fotografando i mercati di Sarajevo "
            "nel 2009 — un saggio per Granta che non vide mai la luce. "
            "Da allora non ho cambiato disciplina, solo tempi, luce e formato.",

        # Bio statement — 5 paragraphs
        "statement_label":   "Statement",
        "statement_heading": "PERCHÉ FOTOGRAFO",
        "statement_paragraphs": [
            "Fotografo per stare a lungo in un luogo. La fotografia è "
            "l'unica disciplina che mi obbliga a tornare. Una serie, "
            "per me, sono dieci o venti viaggi a distanza di mesi nello "
            "stesso punto preciso, finché qualcosa cambia abbastanza "
            "da meritare uno scatto.",
            "Lavoro a pellicola in medio formato — Mamiya 7II, due "
            "obiettivi, Kodak Portra 400. Il rallentamento meccanico è "
            "la disciplina, non un vezzo. Sviluppo e stampo da me, "
            "in cucina trasformata in camera oscura per le piccole "
            "tirature, presso Druckwerkstatt Berlino per il fine art.",
            "Per le commissioni editoriali uso un sistema digitale "
            "Sony Alpha doppio sensore — la velocità di consegna che "
            "richiede una redazione non si concilia con il tempo "
            "della pellicola. Ma il modo di guardare resta lo stesso, "
            "il digitale è solo un altro carrello.",
            "Sono rappresentato dal 2018 dalla Galleria Carla Sozzani "
            "di Milano per la stampa fine art e il mercato secondario. "
            "Per le commissioni edituriali e di marca lavoro "
            "direttamente, senza agente — un agente significa un "
            "filtro fra il fotografo e il committente, e perdo le "
            "conversazioni che mi interessano di più.",
            "Insegno fotografia documentaria al CFP Bauer di Milano "
            "dal 2019 — un giorno la settimana, agli studenti del "
            "secondo anno. È l'unico impegno fisso del calendario "
            "dello studio. Tutto il resto è scelto per progetto.",
        ],

        # Camera kit — what we shoot with.
        # Availability label + value lifted Session 39 (D-047).
        "kit_label":                "Equipaggiamento di lavoro",
        "kit_heading":              "QUATTRO SISTEMI, UNA SOLA SCELTA PER PROGETTO",
        "kit_availability_label":   "Disponibile",
        "kit_availability_value":   "Per commissione",
        "kit": [
            ("01", "Mamiya 7II",
             "Telemetro medio formato 6 × 7 cm, due obiettivi (80mm e 43mm). "
             "Per i lavori personali a pellicola — reportage di lungo respiro "
             "e ritratto autoriale.",
             "Pellicola di studio", "Kodak Portra 400 + Tri-X 400"),
            ("02", "Sony α7R V + α7S III",
             "Doppio sensore (alta risoluzione + sensibilità). "
             "Per le commissioni editoriali e i lavori che richiedono "
             "consegna entro 72 ore.",
             "Obiettivi", "GM 24/35/85 + Voigtländer 50/1.5"),
            ("03", "Linhof Master Technika 4 × 5",
             "Banco ottico per stampa fine art e ritratto in studio. "
             "Riservato a otto-dieci scatti l'anno per la galleria.",
             "Lastra", "Ilford FP4+ · Foma Retropan 320"),
            ("04", "Camera oscura · cucina di Milano",
             "Sviluppo e stampa per le piccole tirature (fino a 18 × 24 cm). "
             "Le tirature fine art sono stampate da Druckwerkstatt Berlino "
             "in collaborazione con Anna Wedekind.",
             "Carta di studio", "Ilford Multigrade FB Classic"),
        ],

        # Exhibitions + publications timeline (selected — full list /pubblicazioni)
        "timeline_label":   "Mostre & pubblicazioni · selezione",
        "timeline_heading": "DODICI TAPPE, QUINDICI ANNI",
        "timeline": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "Mostra collettiva · serie «Porto Vecchio»"),
            ("2025", "FOAM Magazine n. 64",
             "Portfolio di otto pagine sulla serie «Porto Vecchio»"),
            ("2024", "Triennale Milano · «Geografia di una terra»",
             "Mostra personale · serie «Le case di pietra»"),
            ("2024", "World Press Photo Story of the Year · Finalist",
             "Categoria long-term projects, serie «Le case di pietra»"),
            ("2023", "Internazionale Festival Ferrara",
             "Mostra collettiva · serie «Ritratti del Po»"),
            ("2022", "Photo London · Galleria Carla Sozzani booth",
             "Stampe fine art · selezione 2018 — 2022"),
            ("2021", "Magnum Foundation Grant · finalista",
             "Categoria emerging photographer"),
            ("2020", "MAXXI Roma · «Diari del lockdown»",
             "Mostra collettiva · contributo personale 12 stampe"),
            ("2019", "GUP Magazine n. 60 · cover",
             "Saggio illustrato sull'archivio dei mercati di Sarajevo"),
            ("2018", "FOAM Talent · Amsterdam · selezione",
             "Serie «I treni notturni»"),
            ("2016", "Premio Marco Pesaresi · finalista",
             "Reportage italiano · «Il passaggio»"),
            ("2009", "Granta Magazine · saggio commissionato (mai pubblicato)",
             "I mercati di Sarajevo · esordio professionale"),
        ],

        # Final CTA — commissions
        "cta_heading":      "[ COMMISSIONI 2026 — 2027 ]",
        "cta_intro":
            "Lo studio accetta sei-otto commissioni l'anno, scelte per "
            "tempo disponibile e per coerenza con la disciplina. "
            "Le proposte editoriali e di marca sono valutate caso per "
            "caso — preferisco i mandati con tempo lungo.",
        "cta_primary":      "Apri una conversazione",
        "cta_primary_href": "contatti",
    },

    # ─── PUBBLICAZIONI (publications) ───────────────────────────
    "pubblicazioni": {
        "series_counter_label": "Archivio stampa",
        "series_counter_value": "47 PUBBLICAZIONI",
        "status_pulse":         "Aggiornato · gennaio 2026",

        "eyebrow":   "Pubblicazioni & mostre · 2009 — 2026",
        "headline":  "QUARANTASETTE PUBBLICAZIONI, <em>quindici anni</em>",
        "subhead":
            "L'archivio completo delle pubblicazioni in stampa, mostre "
            "personali e collettive, premi e residenze. La lista è "
            "aggiornata a gennaio 2026 — ulteriori uscite previste "
            "nel corso dell'anno.",

        # Press band — magazine + book covers
        "press_label":   "Stampa & editoria · principali uscite",
        "press_heading": "RIVISTE & MONOGRAFIE",
        "press": [
            {
                "year":    "2025",
                "outlet":  "FOAM Magazine n. 64",
                "type":    "Portfolio editoriale",
                "subject": "Serie «Porto Vecchio · Trieste»",
                "format":  "8 pagine · stampa offset · Amsterdam",
            },
            {
                "year":    "2025",
                "outlet":  "Internazionale n. 1612",
                "type":    "Reportage illustrato",
                "subject": "Serie «Le case di pietra · Salento»",
                "format":  "12 pagine · stampa rotocalco · Roma",
            },
            {
                "year":    "2025",
                "outlet":  "Domus n. 1102",
                "type":    "Commissione editoriale",
                "subject": "Numero monografico Carlo Scarpa",
                "format":  "16 pagine · stampa offset · Milano",
            },
            {
                "year":    "2024",
                "outlet":  "Le case di pietra (monografia)",
                "type":    "Volume monografico",
                "subject": "Reportage architettonico Salento 2023 — 24",
                "format":  "Editore Quodlibet · 168 pp. · 24 × 28 cm",
            },
            {
                "year":    "2024",
                "outlet":  "GUP Magazine n. 73",
                "type":    "Saggio critico",
                "subject": "Conversazione con Sarah Kelly su tempi lunghi",
                "format":  "10 pagine · stampa offset · Amsterdam",
            },
            {
                "year":    "2023",
                "outlet":  "Vogue Italia · sezione Photography",
                "type":    "Ritratto editoriale",
                "subject": "Ritratti del Po · serie selezionata",
                "format":  "6 pagine · stampa offset · Milano",
            },
            {
                "year":    "2022",
                "outlet":  "Aperture n. 248",
                "type":    "Saggio illustrato",
                "subject": "Riflessione sulla pellicola in tempo digitale",
                "format":  "8 pagine · stampa offset · New York",
            },
            {
                "year":    "2019",
                "outlet":  "GUP Magazine n. 60 · cover",
                "type":    "Cover + saggio illustrato",
                "subject": "Archivio mercati di Sarajevo 2009",
                "format":  "Cover + 14 pp. · stampa offset · Amsterdam",
            },
        ],

        # Exhibitions
        "exhibitions_label":   "Mostre · personali e collettive",
        "exhibitions_heading": "DODICI MOSTRE, QUINDICI ANNI",
        "exhibitions": [
            ("2026", "FOAM Talent Lounge · Amsterdam",
             "Collettiva · 18 fotografi internazionali",
             "Marzo — maggio 2026"),
            ("2024", "Triennale Milano · «Geografia di una terra»",
             "Personale · serie «Le case di pietra» · 38 stampe",
             "Settembre — dicembre 2024"),
            ("2023", "Internazionale Festival Ferrara",
             "Collettiva · sezione long-term projects",
             "Ottobre 2023"),
            ("2022", "Photo London · Galleria Carla Sozzani booth",
             "Mercato fine art · 14 stampe in vendita",
             "Maggio 2022"),
            ("2020", "MAXXI Roma · «Diari del lockdown»",
             "Collettiva · 12 stampe del contributo personale",
             "Settembre — novembre 2020"),
            ("2018", "FOAM Talent · Amsterdam · serie selezionata",
             "Collettiva · serie «I treni notturni» · 16 stampe",
             "Aprile — giugno 2018"),
        ],

        # Awards & residencies
        "awards_label":   "Premi & residenze",
        "awards_heading": "RICONOSCIMENTI",
        "awards": [
            ("2024", "World Press Photo · Finalist · long-term projects",
             "Serie «Le case di pietra»"),
            ("2023", "Magnum Foundation · Photography & Social Justice · selezione",
             "Programma di mentorship · 6 mesi a New York"),
            ("2021", "Magnum Foundation Grant · finalista emerging",
             "Borsa di studio per lavoro personale"),
            ("2020", "Premio Voglino · finalista",
             "Categoria reportage italiano"),
            ("2016", "Premio Marco Pesaresi · finalista",
             "Reportage italiano · «Il passaggio»"),
            ("2014", "Premio Angelo Frontoni · selezione",
             "Categoria fotografia documentaria"),
        ],

        # Final CTA — speaking + workshops
        "cta_heading":      "[ TALKS · WORKSHOP · LECTURE ]",
        "cta_intro":
            "Per richieste di intervento accademico (festival, scuole, "
            "università), workshop su pellicola medio formato o "
            "lecture editoriali: aprite una conversazione. La "
            "disponibilità si calenda con almeno tre mesi di anticipo.",
        "cta_primary":      "Apri una conversazione",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "series_counter_label": "Disponibilità",
        "series_counter_value": "2026 — 27",
        "status_pulse":         "Aperto a commissioni",

        "eyebrow":   "Conversazione preliminare · senza intermediari",
        "headline":  "[ APRI UNA CONVERSAZIONE ] <em>direttamente</em>",
        "subhead":
            "Le commissioni si discutono direttamente con il fotografo, "
            "senza agente. Per le proposte editoriali, di marca o "
            "per la stampa fine art (rappresentanza Galleria Carla "
            "Sozzani · Milano): scrivete una breve. Rispondo entro "
            "settantadue ore lavorative.",

        # Studio info side card (dark style)
        "studio_label":   "Studio operativo",
        "studio_address": "Via Tadino 18 · 20124 Milano",
        "studio_area":    "Porta Venezia · ingresso laterale · campanello «Bianchi»",
        "studio_metro":   "MM1 / MM3 Loreto · 4 minuti a piedi",
        "studio_hours":   "Disponibile per appuntamento · mai a sorpresa",
        # Studio-card row labels — lifted Session 39 final verify (D-047)
        "studio_row_address_label":  "Indirizzo",
        "studio_row_entrance_label": "Ingresso",
        "studio_row_metro_label":    "Metro",
        "studio_row_hours_label":    "Disponibile",

        # Form fields
        "form_label":   "Breve di commissione",
        "form_heading": "[ COMPILA LA BREVE ]",
        "form_intro":
            "Una breve di commissione è una descrizione strutturata "
            "del progetto fotografico. Non un brief di marketing — "
            "una conversazione preliminare per capire se la disciplina "
            "del lavoro corrisponde alla mia.",
        "form_fields": [
            {"name": "name",      "label": "Nome",          "type": "text",     "required": True,  "placeholder": "Es. Lorenzo",
             "helper": "Solo nome, grazie."},
            {"name": "surname",   "label": "Cognome",       "type": "text",     "required": True,  "placeholder": "Es. Bianchi",
             "helper": "Come compare in firma."},
            {"name": "organization", "label": "Organizzazione", "type": "text", "required": False, "placeholder": "Es. FOAM Magazine",
             "helper": "Se la commissione è editoriale o di marca."},
            {"name": "email",     "label": "Email",         "type": "email",    "required": True,  "placeholder": "lorenzo@foam.org",
             "helper": "Email diretta · risposta entro 72 ore lavorative."},
            {"name": "phone",     "label": "Telefono",      "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Solo se preferite essere richiamati."},
            {"name": "discipline", "label": "Disciplina della commissione", "type": "select", "required": True,
             "options": [
                 "Da definire in conversazione",
                 "Reportage di lungo respiro",
                 "Ritratto editoriale",
                 "Commissione di marca",
                 "Reportage architettonico",
                 "Stampa fine art (Galleria Sozzani)",
                 "Workshop / lecture",
             ],
             "helper": "Scegliere «da definire» se il perimetro non è ancora chiaro."},
            {"name": "timeline",  "label": "Tempo di esecuzione", "type": "select", "required": True,
             "options": [
                 "Entro un mese (consegna rapida)",
                 "Tre — sei mesi (commissione editoriale)",
                 "Sei — diciotto mesi (lavoro di lungo respiro)",
                 "Esplorativo · senza scadenza",
             ],
             "helper": "I tempi di consegna determinano formato (digitale vs pellicola)."},
            {"name": "location",  "label": "Luogo di scatto", "type": "text", "required": False,
             "placeholder": "Es. Salento · Trieste · Sarajevo",
             "helper": "Indicare città / regione / paese · serve per stimare i viaggi."},
            {"name": "story",     "label": "La storia che vorreste raccontare", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Massimo 1000 caratteri. Una descrizione del soggetto, delle ragioni "
                            "del progetto e della pubblicazione prevista. Niente brief di marketing "
                            "— qui interessa il contenuto, non il deliverable.",
             "helper": "Se non sapete da dove cominciare, scrivete cosa vi ha colpito."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che seguirà la commissione da lato committente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Pubblicazione",
             "meta": "Per capire il contesto editoriale o di marca.",
             "fields": ["organization"]},
            {"num": "03", "title": "Perimetro della commissione",
             "meta": "I tempi di consegna determinano il formato di cattura — pellicola vs digitale.",
             "fields": ["discipline", "timeline", "location", "story"]},
            {"num": "04", "title": "Riferimenti (facoltativi)",
             "meta": "Brief editoriale, piano di numero, immagini di riferimento. Possono anticipare la conversazione.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "brief_allegato",
            "label":    "Riferimenti preliminari",
            "helper":   "Brief editoriale, piano di numero, immagini di riferimento. "
                        "PDF / DOCX / JPG / PNG · max 25 MB complessivi.",
            "accept":   ".pdf,.docx,.jpg,.jpeg,.png",
            "multiple": True,
            "primary":  "Trascina qui i documenti o",
            "link":     "sfoglia dall'archivio",
            "meta":     "PDF / DOCX / JPG · max 25 MB",
        },

        "form_submit_label": "[ INVIA LA BREVE ]",
        "form_submit_note":
            "Risposta direttamente dal fotografo entro 72 ore lavorative. "
            "Nessun agente, nessuna automazione di lead.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016. Le richieste di commissione sono "
            "lette e archiviate solo dal fotografo. Per la stampa fine "
            "art (mercato secondario) la rappresentanza è della Galleria "
            "Carla Sozzani.",

        # Sidebar — channels (EXIF style)
        "channels_label": "Canali diretti",
        "channels": [
            ("Studio",          "studio@lorenzobianchi.photo",      "Risposta entro 72 ore"),
            ("Mobile",          "+39 348 211 7720",                 "Lun – Ven · 10:00 – 19:00"),
            ("Stampa fine art", "Galleria Carla Sozzani · Milano",  "Corso Como 10 · +39 02 6555 2223"),
            ("Insegnamento",    "CFP Bauer · Milano",               "Documentaria · 2° anno · giovedì"),
        ],

        "footnote":
            "Per la stampa fine art — vendita sul mercato secondario, "
            "edizioni limitate, esposizioni di galleria — la rappresentanza "
            "esclusiva è della Galleria Carla Sozzani di Milano dal 2018. "
            "Le richieste commerciali di stampa vanno indirizzate "
            "direttamente alla galleria.",
    },

    # ─── POSTS — drives /serie/<slug>/ series_detail ────────────
    "posts": [
        {
            "slug":        "porto-vecchio-trieste",
            "title":       "Porto Vecchio · Trieste",
            "category":    "Reportage di lungo respiro",
            "discipline":  "Reportage di lungo respiro",
            "year":        "2024 — 2026",
            "duration":    "24 mesi · 18 viaggi",
            "location":    "Porto Vecchio · Trieste · Italia",
            "frame_count": "47 fotografie",
            "edition":     "Edizione limitata · 12 + 2 AP per stampa",
            "print_meta": [
                ("Tiratura",       "12 + 2 AP per fotografia"),
                ("Stampa",         "Druckwerkstatt Berlino"),
                ("Carta",          "Hahnemühle Photo Rag Baryta 315 g/m²"),
                ("Rappresentanza", "Galleria Carla Sozzani · Milano"),
            ],
            "lead":
                "Ventiquattro mesi nel porto in via di dismissione di "
                "Trieste — un'area di sessantasei ettari fra il mare "
                "Adriatico e la città, in transizione fra l'archeologia "
                "industriale asburgica e un futuro urbanistico ancora "
                "indecidibile. Quarantasette fotografie a pellicola "
                "Kodak Portra 400 medio formato.",
            "cover_image":
                "https://images.unsplash.com/photo-1517021897933-0e0319cfbc28?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Camera",      "Mamiya 7II · 80mm + 43mm"),
                ("Pellicola",   "Kodak Portra 400 medio formato"),
                ("Periodo",     "Novembre 2024 — gennaio 2026"),
                ("Stampa",      "Druckwerkstatt Berlino · 30 × 40 cm"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=1600&q=85&auto=format&fit=crop",
                 "Frame 03",
                 "Porto Vecchio all'alba · Bacino San Marco · novembre 2024"),
                ("https://images.unsplash.com/photo-1505820013142-f86a3439c5b2?w=1600&q=85&auto=format&fit=crop",
                 "Frame 11",
                 "Magazzini abbandonati · febbraio 2025 · 6:14 del mattino"),
                ("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600&q=85&auto=format&fit=crop",
                 "Frame 18",
                 "Vista dall'idroscalo · primavera 2025"),
                ("https://images.unsplash.com/photo-1499346030926-9a72daac6c63?w=1600&q=85&auto=format&fit=crop",
                 "Frame 24",
                 "Cantiere navale dismesso · estate 2025"),
                ("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=85&auto=format&fit=crop",
                 "Frame 31",
                 "Linea d'acqua · ottobre 2025 · luce di taglio"),
                ("https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=1600&q=85&auto=format&fit=crop",
                 "Frame 39",
                 "Vista finale · gennaio 2026 · ultimo viaggio"),
            ],
            "sections": [
                {
                    "label": "La serie",
                    "heading": "Sessantasei ettari, ventiquattro mesi",
                    "body":
                        "Il Porto Vecchio di Trieste è un'area di "
                        "sessantasei ettari sul mare Adriatico, "
                        "dismessa dal 1991 e in attesa di un piano "
                        "urbanistico definitivo. La serie segue il suo "
                        "stato sospeso fra novembre 2024 e gennaio 2026 "
                        "— diciotto viaggi, tre stagioni complete, "
                        "una sola luce della mattina presto. Il lavoro "
                        "è stato pubblicato su FOAM Magazine n. 64 "
                        "(novembre 2025) ed è in mostra al FOAM Talent "
                        "Lounge di Amsterdam da marzo 2026.",
                },
                {
                    "label": "Il metodo",
                    "heading": "Pellicola, alba, ritorno",
                    "body":
                        "Ho fotografato sempre con Mamiya 7II e pellicola "
                        "Kodak Portra 400 medio formato — due obiettivi, "
                        "ottanta e quarantatré millimetri. L'intero "
                        "lavoro è stato fatto fra le 5:30 e le 7:00 del "
                        "mattino, prima dell'arrivo del personale di "
                        "vigilanza. La luce di Trieste in quella fascia "
                        "oraria è particolare — la bora notturna pulisce "
                        "l'aria, l'acqua del bacino è specchio, il sole "
                        "non è ancora alzato sul Carso.",
                },
                {
                    "label": "L'edizione",
                    "heading": "Stampa fine art · dodici copie",
                    "body":
                        "L'edizione fine art comprende dodici stampe "
                        "+ due artist proof per ogni fotografia, "
                        "stampate su carta Hahnemühle Photo Rag Baryta "
                        "315 g/m² presso Druckwerkstatt Berlino in "
                        "collaborazione con Anna Wedekind. Il formato "
                        "di stampa è 30 × 40 cm. La distribuzione "
                        "fine art è esclusiva della Galleria Carla "
                        "Sozzani di Milano.",
                },
            ],
            "next_label": "Serie successiva",
        },
        {
            "slug":        "case-di-pietra-puglia",
            "title":       "Le case di pietra · Salento",
            "category":    "Reportage architettonico",
            "discipline":  "Reportage architettonico",
            "year":        "2023 — 2024",
            "duration":    "16 mesi · 9 viaggi",
            "location":    "Salento · Puglia · Italia",
            "frame_count": "62 fotografie",
            "edition":     "Edizione monografica · Quodlibet · 168 pp.",
            "print_meta": [
                ("Tiratura",       "1.500 copie · prima ristampa esaurita"),
                ("Stampa",         "Quodlibet · Macerata"),
                ("Carta",          "Munken Pure 130 g/m² · uncoated"),
                ("Rappresentanza", "Galleria Carla Sozzani · Milano"),
            ],
            "lead":
                "Sedici mesi nelle masserie di pietra a secco del "
                "Salento meridionale — quaranta edifici, nessun "
                "intervento contemporaneo. Reportage architettonico "
                "documentale, pubblicato in monografia da Quodlibet "
                "(novembre 2024) e Internazionale n. 1612 (settembre 2025).",
            "cover_image":
                "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Camera",      "Mamiya 7II + Sony α7R V"),
                ("Pellicola",   "Kodak Portra 400 + digitale doppio"),
                ("Periodo",     "Marzo 2023 — luglio 2024"),
                ("Stampa",      "Volume Quodlibet · 24 × 28 cm · 168 pp."),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1543248939-4296e1fea89b?w=1600&q=85&auto=format&fit=crop",
                 "Frame 04",
                 "Masseria San Giovanni · Otranto · primavera 2023"),
                ("https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=1600&q=85&auto=format&fit=crop",
                 "Frame 12",
                 "Trullo dei Cento Giganti · Locorotondo · estate 2023"),
                ("https://images.unsplash.com/photo-1512100356356-de1b84283e18?w=1600&q=85&auto=format&fit=crop",
                 "Frame 22",
                 "Masseria Pulicchia · Galatina · autunno 2023"),
                ("https://images.unsplash.com/photo-1518131672697-613becd4fab5?w=1600&q=85&auto=format&fit=crop",
                 "Frame 31",
                 "Lamia interna · Sannicola · gennaio 2024"),
                ("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=85&auto=format&fit=crop",
                 "Frame 41",
                 "Vista del muro a secco · Specchia · marzo 2024"),
                ("https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=1600&q=85&auto=format&fit=crop",
                 "Frame 53",
                 "Cortile interno · Tricase · luglio 2024"),
            ],
            "sections": [
                {
                    "label": "La serie",
                    "heading": "Quaranta edifici, sedici mesi",
                    "body":
                        "Il reportage documenta quaranta edifici di "
                        "pietra a secco del Salento meridionale — "
                        "masserie, lamie, trulli minori, pajare. "
                        "L'idea era documentarli prima di un eventuale "
                        "restauro o demolizione, in collaborazione con "
                        "il Centro Studi Salentini di Lecce. Sedici "
                        "mesi di lavoro, nove viaggi, sessantadue "
                        "fotografie selezionate.",
                },
                {
                    "label": "Il metodo",
                    "heading": "Doppio formato per documentazione",
                    "body":
                        "A differenza dei lavori personali, qui ho "
                        "lavorato a doppio formato — Mamiya 7II per gli "
                        "esterni a pellicola e Sony α7R V per gli "
                        "interni in digitale (per la documentazione "
                        "architettonica precisa). I due formati "
                        "convivono nel volume Quodlibet senza "
                        "distinzione editoriale evidente — la pellicola "
                        "e il digitale, lavorati in stampa, "
                        "diventano indistinguibili a 24 × 28 cm.",
                },
                {
                    "label": "Il volume",
                    "heading": "Centosessantotto pagine, Quodlibet",
                    "body":
                        "Il volume monografico «Le case di pietra» è "
                        "stato pubblicato da Quodlibet (novembre 2024) "
                        "con saggio critico di Salvatore Settis. Centosessantotto "
                        "pagine, formato 24 × 28 cm, brossura cucita, "
                        "carta uncoated Munken Pure 130 g/m². Tiratura "
                        "1.500 copie, prima ristampa esaurita in tre mesi. "
                        "Selezione finalista al World Press Photo 2024 "
                        "categoria long-term projects.",
                },
            ],
            "next_label": "Serie successiva",
        },
        {
            "slug":        "ritratti-del-po",
            "title":       "Ritratti del Po",
            "category":    "Ritratto autoriale",
            "discipline":  "Ritratto autoriale",
            "year":        "2023",
            "duration":    "8 mesi · 7 viaggi",
            "location":    "Delta del Po · Veneto · Italia",
            "frame_count": "28 fotografie",
            "edition":     "Pubblicato · Vogue Italia photography",
            "print_meta": [
                ("Tiratura",       "8 + 2 AP per stampa selezionata"),
                ("Stampa",         "Tirature personali · cucina di Milano"),
                ("Carta",          "Ilford Multigrade FB Classic"),
                ("Rappresentanza", "Galleria Carla Sozzani · Milano"),
            ],
            "lead":
                "Ventotto ritratti di pescatori, vongolare e "
                "conduttori di chiatta del Delta del Po veneto. "
                "Otto mesi di lavoro fra primavera e autunno 2023, "
                "pubblicato sulla sezione Photography di Vogue Italia "
                "(dicembre 2023) e in mostra al Festival Internazionale "
                "di Ferrara (ottobre 2023).",
            "cover_image":
                "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=2000&q=85&auto=format&fit=crop",
            "exif_credits": [
                ("Camera",      "Mamiya 7II · 80mm"),
                ("Pellicola",   "Kodak Portra 400 medio formato"),
                ("Periodo",     "Aprile — novembre 2023"),
                ("Stampa",      "Tirature personali · cucina di Milano"),
            ],
            "gallery": [
                ("https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=1600&q=85&auto=format&fit=crop",
                 "Frame 01",
                 "Aldo · pescatore · Pila · maggio 2023"),
                ("https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=1600&q=85&auto=format&fit=crop",
                 "Frame 06",
                 "Maria · vongolara · Goro · giugno 2023"),
                ("https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=1600&q=85&auto=format&fit=crop",
                 "Frame 12",
                 "Carlo e Giuseppe · fratelli pescatori · luglio 2023"),
                ("https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=1600&q=85&auto=format&fit=crop",
                 "Frame 17",
                 "Anna · ristoratrice · settembre 2023"),
                ("https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=1600&q=85&auto=format&fit=crop",
                 "Frame 22",
                 "Luca · conduttore di chiatta · ottobre 2023"),
                ("https://images.unsplash.com/photo-1521252659862-eec69941b071?w=1600&q=85&auto=format&fit=crop",
                 "Frame 28",
                 "Ritratto finale · novembre 2023 · ultima luce"),
            ],
            "sections": [
                {
                    "label": "La serie",
                    "heading": "Ventotto persone, otto mesi",
                    "body":
                        "Una serie di ventotto ritratti di chi vive il "
                        "Delta del Po veneto come luogo di lavoro — "
                        "pescatori, vongolare, ristoratori, conduttori "
                        "di chiatta. Otto mesi di lavoro fra aprile e "
                        "novembre 2023, sette viaggi nelle due province "
                        "(Rovigo + Ferrara). Ogni ritratto è preceduto "
                        "da almeno una giornata passata con il soggetto "
                        "— mai sessioni «mordi e fuggi».",
                },
                {
                    "label": "Il metodo",
                    "heading": "Una sola macchina, una sola luce",
                    "body":
                        "Tutti i ritratti sono stati fatti con Mamiya "
                        "7II e ottanta millimetri, in luce naturale "
                        "disponibile — niente flash, niente pannelli "
                        "diffusori. La pellicola è sempre Kodak Portra "
                        "400, sviluppata in casa. La scelta del singolo "
                        "obiettivo (al posto di una corredata di tre o "
                        "quattro) è una disciplina formale — costringe "
                        "a muoversi rispetto al soggetto, non a girare "
                        "l'anello dell'obiettivo.",
                },
                {
                    "label": "La pubblicazione",
                    "heading": "Vogue Italia · Festival Ferrara",
                    "body":
                        "La serie è stata pubblicata sulla sezione "
                        "Photography di Vogue Italia (dicembre 2023, "
                        "sei pagine) ed esposta in mostra collettiva "
                        "al Festival Internazionale di Ferrara "
                        "(ottobre 2023, dodici stampe selezionate). "
                        "Una stampa è entrata nella collezione "
                        "permanente del MAXXI di Roma.",
                },
            ],
            "next_label": "Serie successiva",
        },
    ],
}
