"""SaluteVita — Poliambulatorio Milano (clinic archetype) — IT content tree.

Phase 2h — Medical second wave (2026-04-15).

Voice contract (IT):
- Institutional-accessible register. Warm but professional, never editorial
  serif drama. "voi/tu" neutro, come parla un poliambulatorio moderno al
  paziente: chiaro, rassicurante, preciso senza paternalismo.
- Concrete details: Milano Stazione Centrale, Via Galvani 18, 40+ specialisti,
  aperto Lun-Sab 7:00-21:00, numero verde 800 123 456, convenzioni Inail /
  Unisalute / Generali Welion / RBM / Previmedical / Caspie / MioDottore.
- Booking-widget conversion pattern: grande form di prenotazione online a
  destra dell'hero, numero verde sempre accessibile nella nav, CTA primario
  "Prenota una visita" su ogni pagina.

Differentiation contract vs Cardio/Dermatologia (D-054 enforcement):
- Cardio + Derm sono "specialist" archetype: palette paper/navy/accent,
  prestigious-editorial serif Cormorant/Bodoni, tono da centro d'eccellenza.
- SaluteVita è "clinic" archetype: palette bianco clinico / teal / cyan /
  verde, sans moderne Nunito Sans + Inter, tono da poliambulatorio
  multispecialistico istituzionale accessibile.
- Hero silhouette distinto: split-booking widget (non photo-hero né
  editorial-magazine). Nav: solid-phone (non rule-hairline). Cards:
  icon-grid (non editorial-large). CTA: booking online (non richiesta
  email prima-visita). Density: medium (non airy editoriale).
- Imagery pool: "medical" Pexels (reception teal, consultazioni luminose,
  sala d'attesa moderna) — curato per evitare collisioni visive con
  cardio/derm che usano "medical-cardio"/"medical-derm".
"""
from __future__ import annotations

from typing import Any


# ============================================================
# SVG ICONS — sobri, single-stroke, current-color compatible
# ============================================================

ICO_STETHOSCOPE = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M4 2v6a4 4 0 0 0 4 4v0a4 4 0 0 0 4-4V2"/>'
    '<path d="M8 12v3a5 5 0 0 0 5 5h1a5 5 0 0 0 5-5v-1"/>'
    '<circle cx="19" cy="11" r="2"/>'
    '</svg>'
)
ICO_BABY = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M9 12h.01"/><path d="M15 12h.01"/>'
    '<path d="M10 16c.5.3 1.5.5 2 .5s1.5-.2 2-.5"/>'
    '<path d="M19 6.3a9 9 0 1 1-15.8 5.2"/>'
    '<path d="M3 6.3A9 9 0 0 1 18.8 11.5"/>'
    '</svg>'
)
ICO_DERM = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<circle cx="12" cy="12" r="10"/>'
    '<circle cx="9" cy="10" r="1"/>'
    '<circle cx="15" cy="11" r="1.2"/>'
    '<circle cx="11" cy="15" r="0.9"/>'
    '</svg>'
)
ICO_ULTRASOUND = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M4 4h16v16H4z" fill="none"/>'
    '<path d="M4 14c2-3 4-3 6 0s4 3 6 0 2-3 4 0"/>'
    '<circle cx="6" cy="7" r="1"/>'
    '</svg>'
)
ICO_WOMAN = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<circle cx="12" cy="6" r="3"/>'
    '<path d="M8 21l2-9h4l2 9"/>'
    '<path d="M10 14h4"/>'
    '</svg>'
)
ICO_BONE = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M4 9a3 3 0 0 1 3-3 3 3 0 0 1 3 3l4 4a3 3 0 0 1 3-3 3 3 0 0 1 3 3 3 3 0 0 1-3 3 3 3 0 0 1-3-3l-4-4a3 3 0 0 1-3 3 3 3 0 0 1-3-3z"/>'
    '</svg>'
)
ICO_BRAIN = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M9 3a3 3 0 0 0-3 3v0a3 3 0 0 0-3 3 3 3 0 0 0 2 2.8v2.4A3 3 0 0 0 3 17a3 3 0 0 0 3 3 3 3 0 0 0 3 2 3 3 0 0 0 3-2 3 3 0 0 0 3 2 3 3 0 0 0 3-2 3 3 0 0 0 3-3 3 3 0 0 0-2-2.8v-2.4A3 3 0 0 0 21 9a3 3 0 0 0-3-3 3 3 0 0 0-3-3 3 3 0 0 0-3 2 3 3 0 0 0-3-2z"/>'
    '</svg>'
)
ICO_EYE = (
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/>'
    '<circle cx="12" cy="12" r="3"/>'
    '</svg>'
)


# ============================================================
# SALUTE CONTENT — IT
# ============================================================

SALUTE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Home",            "kind": "home"},
        {"slug": "studio",      "label": "Lo studio",       "kind": "about"},
        {"slug": "servizi",     "label": "Servizi",         "kind": "services"},
        {"slug": "prevenzione", "label": "Prevenzione",     "kind": "prevention"},
        {"slug": "medici",      "label": "Medici",          "kind": "team"},
        {"slug": "contatti",    "label": "Contatti",        "kind": "contact"},
        {"slug": "prenota",     "label": "Prenota",         "kind": "appointment"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "S",
        "logo_word":    "SaluteVita",
        "tag":          "Poliambulatorio · Milano Centrale",
        "phone_label":  "Numero verde",
        "phone":        "800 123 456",
        "phone_tel":    "+39800123456",
        "email":        "prenota@salutevita.clinic",
        "address":      "Via Galvani 18 · 20124 Milano",
        "hours_compact": "Lun – Sab · 7:00 – 21:00",
        "hours_footer_rows": [
            "Lun – Ven · 7:00 – 21:00",
            "Sab · 8:00 – 18:00",
            "Domenica · chiuso",
        ],
        "foot_extra_label": "Convenzioni",
        "foot_extra_rows": [
            "Inail · Unisalute · Generali",
            "RBM Salute · Previmedical",
            "Caspie · MioDottore",
        ],
        "license": "Iscr. reg. strutture sanitarie ATS Milano · P.IVA 09812345678",
        "footer_intro":
            "Poliambulatorio multispecialistico nel cuore di Milano Centrale. "
            "Oltre 40 medici, 12 reparti, aperto 6 giorni su 7 per essere "
            "un punto di riferimento vicino alle persone dal 1998.",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":   "Poliambulatorio · Milano Centrale · dal 1998",
        "headline":  'Visita prenotata in trenta secondi, <em>medici che vorrai rivedere</em>.',
        "subhead":
            "Oltre 40 specialisti, percorsi diagnostici integrati e un'esperienza "
            "paziente pensata per metterti a tuo agio dal primo contatto. "
            "Prenota online in 30 secondi, aperto Lun-Sab 7:00-21:00.",
        "primary_cta":    "Prenota una visita",
        "primary_href":   "prenota",
        "secondary_cta":  "Numero verde 800 123 456",
        "secondary_href": "contatti",
        "trust_note":     "Risposta entro 2 ore · senza obbligo",

        "stats": [
            ("40+",  "Medici specialisti"),
            ("12",   "Reparti"),
            ("98%",  "Pazienti che tornerebbero"),
        ],

        "booking_widget": {
            "aria_label":  "Prenotazione online in tre passaggi",
            "title":       "Prenota online in 30 secondi",
            "subtitle":    "Prima data spesso entro 48 ore lavorative",
            "badge":       "6 slot liberi oggi",
            "specialty_label": "Specialità",
            "specialty_value": "Cardiologia",
            "date_label":      "Prima data disponibile",
            "date_value":      "Mar 14 Apr · 10:30",
            "doctor_label":    "Medico",
            "doctor_value":    "Dr.ssa Elisa Conti",
            "cta":             "Conferma prenotazione",
            "footnote":        "Gratis · disdici fino a 24h prima",
            "secure_label":    "Dati crittografati",
        },

        # Band stats (4 orizzontali sotto hero)
        "stats_strip": [
            ("1998",    "Anno di fondazione"),
            ("28.000",  "Pazienti seguiti ogni anno"),
            ("6",       "Giorni di apertura su 7"),
            ("€ 0",     "Costo prima telefonata"),
        ],

        "specialties_label": "Le nostre specialità",
        "specialties_heading": 'Dodici reparti sotto <em>un solo tetto</em>.',
        "specialties_intro":
            "Tutte le visite più richieste da una famiglia milanese, coordinate "
            "tra loro: se il cardiologo chiede un'ecografia, la prenoti in giornata "
            "nello stesso edificio.",
        "specialties": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "title":    "Cardiologia",
                "blurb":    "Visita cardiologica, ECG a riposo e sotto sforzo, "
                            "ecocardiografia, holter pressorio e delle 24 ore.",
                "link_label": "Scopri il reparto",
            },
            {
                "icon_svg": ICO_BABY,
                "title":    "Pediatria",
                "blurb":    "Bilanci di salute 0-14 anni, vaccinazioni, "
                            "consulenza pediatrica urgente entro 24 ore.",
                "link_label": "Scopri il reparto",
            },
            {
                "icon_svg": ICO_DERM,
                "title":    "Dermatologia",
                "blurb":    "Mappatura nei in dermatoscopia digitale, dermatiti, "
                            "acne, controlli oncologici della pelle.",
                "link_label": "Scopri il reparto",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "title":    "Radiologia & Diagnostica",
                "blurb":    "Ecografia multi-organo, TAC, risonanza magnetica, "
                            "mammografia. Referto in giornata su richiesta.",
                "link_label": "Scopri il reparto",
            },
            {
                "icon_svg": ICO_WOMAN,
                "title":    "Ginecologia",
                "blurb":    "Visite ostetrico-ginecologiche, ecografia "
                            "transvaginale, pap-test, percorsi in gravidanza.",
                "link_label": "Scopri il reparto",
            },
            {
                "icon_svg": ICO_BONE,
                "title":    "Ortopedia & Fisioterapia",
                "blurb":    "Visita ortopedica, infiltrazioni ecoguidate, "
                            "riabilitazione post-operatoria con fisioterapista dedicato.",
                "link_label": "Scopri il reparto",
            },
            {
                "icon_svg": ICO_BRAIN,
                "title":    "Neurologia",
                "blurb":    "Visita neurologica, elettroencefalogramma, "
                            "valutazione cefalee ricorrenti e disturbi del sonno.",
                "link_label": "Scopri il reparto",
            },
            {
                "icon_svg": ICO_EYE,
                "title":    "Oculistica",
                "blurb":    "Visita completa, OCT retina, campo visivo, "
                            "valutazione della cataratta in collaborazione con centri "
                            "chirurgici convenzionati.",
                "link_label": "Scopri il reparto",
            },
        ],

        "journey_label":    "Il percorso paziente",
        "journey_heading":  'Dalla prenotazione al referto, <em>quattro passi semplici</em>.',
        "journey_intro":
            "Abbiamo disegnato il percorso pensando a come una famiglia vorrebbe essere "
            "accolta: nessuna coda in piedi, nessun foglio perso, nessun secondo "
            "racconto della stessa storia.",
        "journey_steps": [
            {"num": "01", "title": "Prenotazione online",
             "body": "Scegli specialità, medico e orario in 30 secondi. Ti arriva "
                     "un promemoria SMS due giorni prima."},
            {"num": "02", "title": "Accoglienza",
             "body": "Reception aperta dalle 7:00. Ti accompagniamo in sala d'attesa "
                     "e ti chiamiamo per nome quando il medico è pronto."},
            {"num": "03", "title": "Visita",
             "body": "Il medico ha già la tua storia clinica davanti. Visita "
                     "approfondita, esami in giornata quando possibile."},
            {"num": "04", "title": "Referto digitale",
             "body": "Referto e prescrizioni nella tua area paziente entro 24 ore. "
                     "Scaricabili in PDF, condivisibili con il tuo medico di base."},
        ],

        "prevenzione_label":   "Check-up di prevenzione",
        "prevenzione_heading": 'Prevenire costa <em>meno</em> di curare.',
        "prevenzione_intro":
            "Tre pacchetti pensati per le fasce di età che più richiedono controlli "
            "regolari. Sconto del 15% per chi rinnova il check-up entro 12 mesi.",
        "prevenzione_cards": [
            {
                "eyebrow":  "Donna 40+",
                "title":    "Check-up Donna 40+",
                "desc":     "Visita ginecologica, ecografia pelvica, pap-test, "
                            "mammografia e consulenza nutrizionale in un'unica mattina.",
                "includes": [
                    "Visita ginecologica completa",
                    "Pap-test e HPV-test",
                    "Ecografia pelvica + mammografia",
                    "Consulenza nutrizionale 30 min",
                ],
                "duration_label": "Durata",
                "duration":       "3 ore",
                "price_label":    "Prezzo tutto incluso",
                "price":          "€ 320",
                "cta":            "Prenota il check-up",
            },
            {
                "eyebrow":  "Uomo 45+",
                "title":    "Check-up Uomo 45+",
                "desc":     "Cardiologia, urologia, controllo metabolico, "
                            "ecografia addome e prostata. Referto unico entro 48 ore.",
                "includes": [
                    "Visita cardiologica + ECG",
                    "Visita urologica + PSA",
                    "Ecografia addome completo",
                    "Profilo metabolico lipidico",
                ],
                "duration_label": "Durata",
                "duration":       "3,5 ore",
                "price_label":    "Prezzo tutto incluso",
                "price":          "€ 280",
                "cta":            "Prenota il check-up",
            },
            {
                "eyebrow":  "Over 60",
                "title":    "Check-up Over 60",
                "desc":     "Valutazione cardiovascolare, ossea, neurologica e "
                            "oculistica. Coordinato da un medico internista "
                            "che tiene insieme il quadro.",
                "includes": [
                    "Cardiologia + ecocardio + holter",
                    "MOC densitometria ossea",
                    "Visita neurologica cognitiva",
                    "Oculistica + tonometria",
                ],
                "duration_label": "Durata",
                "duration":       "4 ore",
                "price_label":    "Prezzo tutto incluso",
                "price":          "€ 420",
                "cta":            "Prenota il check-up",
            },
        ],

        "team_label":   "I nostri specialisti",
        "team_heading": 'Otto volti <em>dei reparti più richiesti</em>.',
        "team_intro":
            "Oltre 40 medici collaborano con SaluteVita. Qui vedi i responsabili "
            "degli otto reparti più prenotati: il resto dello staff è nella pagina "
            "dedicata.",
        "team_ribbon_people": [
            {
                "avatar": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr.ssa Elisa Conti",
                "specialty":"Cardiologia",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Marco Ferri",
                "specialty":"Pediatria",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr.ssa Sofia Lenzi",
                "specialty":"Dermatologia",
            },
            {
                "avatar": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Luca Russo",
                "specialty":"Radiologia",
            },
            {
                "avatar": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr.ssa Chiara Moretti",
                "specialty":"Ginecologia",
            },
            {
                "avatar": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Paolo Serra",
                "specialty":"Ortopedia",
            },
            {
                "avatar": "https://images.pexels.com/photos/7659562/pexels-photo-7659562.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Andrea Villa",
                "specialty":"Neurologia",
            },
            {
                "avatar": "https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr.ssa Laura Bianchi",
                "specialty":"Oculistica",
            },
        ],
        "team_footnote_prefix": "Oltre 40 specialisti compongono lo staff completo.",
        "team_footnote_link":   "Vedi tutti i medici",

        "partners_label":   "Convenzioni e assicurazioni",
        "partners_heading": "Lavoriamo in rete con le principali casse e assicurazioni sanitarie italiane.",
        "partners": [
            "Inail", "Unisalute", "Generali Welion",
            "RBM Salute", "Previmedical", "Caspie",
            "MioDottore", "Consap",
        ],

        "cta_band": {
            "heading":      "Serve una visita questa settimana?",
            "body":         "Prenota online in 30 secondi oppure chiamaci al numero verde: la segreteria risponde tutti i giorni dalle 7:00 alle 21:00.",
            "primary_cta":  "Prenota online",
            "primary_href": "prenota",
            "secondary_cta":"Chiama 800 123 456",
        },
    },

    # ─── STUDIO (about) ──────────────────────────────────────────
    "studio": {
        "eyebrow":   "Lo studio · dal 1998 a Milano",
        "headline":  'Un punto di riferimento <em>vicino</em> alle persone.',
        "intro":
            "SaluteVita nasce nel 1998 dall'idea di tre medici milanesi: "
            "ridurre la distanza tra l'ospedale e la famiglia, offrendo un "
            "poliambulatorio completo a due passi dalla Stazione Centrale.",

        "values_label":   "I nostri valori",
        "values_heading": 'Quattro cose che <em>non cambieremo</em>.',
        "values": [
            {"title": "Multidisciplinarietà",
             "body":  "Nessun paziente viene rimbalzato: se serve un esame, "
                      "lo prenotiamo noi nello stesso edificio. Referti condivisi "
                      "tra specialisti."},
            {"title": "Accoglienza",
             "body":  "La segreteria risponde dalle 7:00. Ti chiamiamo per nome, "
                      "niente numerini, niente file in piedi."},
            {"title": "Tecnologia al servizio",
             "body":  "Cartella clinica digitale, referti in PDF entro 24 ore, "
                      "dermatoscopia digitale, risonanza 1.5T di ultima generazione."},
            {"title": "Continuità",
             "body":  "Se tre anni fa la tua bambina era dal nostro pediatra, "
                      "oggi trovi la stessa storia clinica quando le serve "
                      "l'ortopedico. Senza ripartire da zero."},
        ],

        "photo_label":   "Lo studio",
        "photo_heading": "Quattro piani, dodici reparti, una segreteria sola.",
        "photo_body":
            "L'edificio di Via Galvani 18 ospita ambulatori, sala prelievi, "
            "diagnostica per immagini e fisioterapia. Tutto al piano terra "
            "o al primo piano, accessibile senza barriere, con parcheggio "
            "convenzionato a 40 metri.",
        "photo_caption": "Via Galvani 18 · zona Stazione Centrale",
        "photo_src":     "https://images.pexels.com/photos/7108324/pexels-photo-7108324.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",

        "timeline_label":   "La nostra storia",
        "timeline_heading": 'Ventisei anni, <em>una cosa sola</em>: la persona davanti.',
        "timeline": [
            {"year": "1998", "title": "L'inizio",
             "body": "Tre medici — un internista, una pediatra, un cardiologo — "
                     "aprono il primo ambulatorio in Via Galvani con 180 metri quadri."},
            {"year": "2008", "title": "Il secondo piano",
             "body": "Inauguriamo la diagnostica per immagini con risonanza, TAC, "
                     "mammografia. I reparti diventano otto."},
            {"year": "2018", "title": "Cartella digitale",
             "body": "Passaggio completo alla cartella clinica digitale e "
                     "all'area paziente online. Referti in 24 ore su ogni esame."},
            {"year": "2024", "title": "Oggi",
             "body": "40+ specialisti, 12 reparti, 28.000 pazienti seguiti "
                     "ogni anno. Restiamo la clinica di famiglia che eravamo."},
        ],

        "cta_band": {
            "heading":    "Vuoi conoscerci di persona?",
            "body":       "Prenota la tua prima visita o vieni a trovarci: la reception è aperta dalle 7:00 di mattina, senza appuntamento.",
            "primary_cta":"Prenota una visita",
            "secondary_cta": "Chiama 800 123 456",
        },
    },

    # ─── SERVIZI (services) ──────────────────────────────────────
    "servizi": {
        "eyebrow":   "Servizi · 12 reparti · 40+ specialisti",
        "headline":  'Tutte le visite <em>di cui una famiglia ha bisogno</em>.',
        "intro":
            "Dalla cardiologia alla fisioterapia, passando per pediatria, "
            "dermatologia e diagnostica per immagini. Ogni visita prenotabile "
            "online, con prezzi chiari e pacchetti di prevenzione dedicati.",

        "svc_label":   "Tutti i servizi",
        "svc_heading": 'Visite specialistiche, <em>prezzi trasparenti</em>.',
        "price_label": "Prima visita",
        "book_cta":    "Prenota",

        "services": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "eyebrow":  "Cardiologia",
                "title":    "Visita cardiologica con ECG",
                "desc":     "Anamnesi approfondita, auscultazione, ECG a 12 "
                            "derivazioni, valutazione del rischio cardiovascolare "
                            "e indicazioni per ulteriori esami quando necessari.",
                "items":    ["ECG incluso", "Referto in giornata", "Durata 40 min"],
                "price":    "€ 140",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Cardiologia",
                "title":    "Ecocardiografia color-doppler",
                "desc":     "Valutazione morfologica e funzionale del cuore con "
                            "ecografo di ultima generazione. Utile per soffi, "
                            "ipertensione e controlli post-evento.",
                "items":    ["Doppler incluso", "Referto 24h", "Durata 35 min"],
                "price":    "€ 160",
            },
            {
                "icon_svg": ICO_BABY,
                "eyebrow":  "Pediatria",
                "title":    "Visita pediatrica 0-14",
                "desc":     "Bilancio di salute, crescita, sviluppo psicomotorio, "
                            "alimentazione. Su richiesta consulenza vaccinale "
                            "secondo calendario regionale.",
                "items":    ["0-14 anni", "Richiesta urgente 24h", "Durata 45 min"],
                "price":    "€ 120",
            },
            {
                "icon_svg": ICO_DERM,
                "eyebrow":  "Dermatologia",
                "title":    "Mappatura nei in dermatoscopia digitale",
                "desc":     "Controllo oncologico della pelle con videodermatoscopio. "
                            "Immagini archiviate per confronto annuale. Consigliata a "
                            "partire dai 30 anni.",
                "items":    ["Archivio 5 anni", "Immagini digitali", "Durata 40 min"],
                "price":    "€ 180",
            },
            {
                "icon_svg": ICO_WOMAN,
                "eyebrow":  "Ginecologia",
                "title":    "Visita ostetrico-ginecologica + ecografia",
                "desc":     "Visita completa con ecografia transvaginale o addominale. "
                            "Percorsi dedicati per la prima gravidanza e la menopausa.",
                "items":    ["Pap-test disponibile", "Ecografia inclusa", "Durata 45 min"],
                "price":    "€ 150",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Radiologia",
                "title":    "Risonanza magnetica 1.5T",
                "desc":     "Apparecchio aperto di ultima generazione, adatto anche "
                            "a pazienti claustrofobici. Referto radiologico entro "
                            "24 ore lavorative.",
                "items":    ["Aperta · no claustrofobia", "Referto 24h", "Durata 30 min"],
                "price":    "da € 220",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Ortopedia",
                "title":    "Visita ortopedica + ecografia muscolare",
                "desc":     "Valutazione clinica e ecografica in un'unica seduta. "
                            "Infiltrazioni ecoguidate con acido ialuronico "
                            "o cortisonico su indicazione.",
                "items":    ["Ecografia inclusa", "Infiltrazioni disponibili", "Durata 40 min"],
                "price":    "€ 150",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Fisioterapia",
                "title":    "Seduta di fisioterapia riabilitativa",
                "desc":     "Percorso personalizzato con fisioterapista dedicato, "
                            "su prescrizione dell'ortopedico o del medico curante. "
                            "Pacchetti da 5 e 10 sedute.",
                "items":    ["Pacchetti disponibili", "Post-chirurgia", "Durata 50 min"],
                "price":    "€ 55 · seduta",
            },
            {
                "icon_svg": ICO_BRAIN,
                "eyebrow":  "Neurologia",
                "title":    "Visita neurologica con EEG",
                "desc":     "Valutazione cefalee, disturbi del sonno, tremori, "
                            "con possibilità di elettroencefalogramma nella stessa "
                            "seduta. Su richiesta test cognitivi.",
                "items":    ["EEG disponibile", "Test cognitivi", "Durata 50 min"],
                "price":    "€ 170",
            },
            {
                "icon_svg": ICO_EYE,
                "eyebrow":  "Oculistica",
                "title":    "Visita oculistica completa",
                "desc":     "Misurazione della vista, tonometria, fondo oculare, "
                            "OCT della retina. Valutazione chirurgica della cataratta "
                            "in collaborazione con centri convenzionati.",
                "items":    ["OCT incluso", "Tonometria", "Durata 35 min"],
                "price":    "€ 130",
            },
        ],

        "faq_label":   "Domande frequenti",
        "faq_heading": 'Le <em>tre</em> domande che ci fate più spesso.',
        "faqs": [
            ("Posso usare la mia assicurazione sanitaria o fondo cassa?",
             "Sì. SaluteVita è convenzionata con Unisalute, Generali Welion, RBM "
             "Salute, Previmedical, Caspie e Consap. Il fondo copre direttamente "
             "la prestazione senza anticipo, nella maggior parte dei casi. Inviaci "
             "la tessera quando prenoti e ti confermiamo la copertura in 24 ore."),
            ("In quanti giorni ricevo il referto?",
             "Visite cliniche: referto digitale entro 24 ore lavorative nella tua "
             "area paziente. Diagnostica per immagini (ecografia, TAC, risonanza): "
             "referto radiologico in 24-48 ore. Se serve in giornata, chiedi al "
             "momento della prenotazione: su richiesta è quasi sempre possibile."),
            ("Posso disdire o spostare l'appuntamento?",
             "Certo. Puoi modificare o annullare dall'area paziente fino a 24 ore "
             "prima, senza costi. Sotto le 24 ore chiamaci al numero verde 800 123 "
             "456: valutiamo caso per caso, senza penale per motivi sanitari."),
        ],

        "cta_band": {
            "heading":    "Scegli il servizio, noi pensiamo al resto.",
            "body":       "Prenota online in pochi secondi: se non trovi la specialità che cerchi, chiama il numero verde e ti indirizziamo noi.",
            "primary_cta":"Prenota una visita",
            "secondary_cta":"Chiama 800 123 456",
        },
    },

    # ─── PREVENZIONE (prevention) ────────────────────────────────
    "prevenzione": {
        "eyebrow":   "Prevenzione · tre percorsi dedicati",
        "headline":  'Un check-up completo in <em>mezza giornata</em>.',
        "intro":
            "Tre pacchetti pensati per le fasce di età in cui i controlli contano "
            "di più: donna 40+, uomo 45+, over 60. Un medico internista coordina "
            "tutto e ti consegna un unico referto in 48 ore.",

        "pack_label":   "I tre percorsi",
        "pack_heading": 'Scegli in base <em>all\'età e al profilo</em>.',
        "duration_label": "Durata",
        "exams_label":    "Esami",

        "packages": [
            {
                "eyebrow": "DONNA 40+",
                "title":   "Check-up Donna 40+",
                "desc":    "Pensato per chi vuole tenere sotto controllo salute "
                           "ginecologica, senologica e metabolica in una mattina sola.",
                "price":   "€ 320",
                "price_meta": "tutto incluso",
                "duration": "3 ore",
                "exams_count": "7 esami",
                "includes": [
                    "Visita ginecologica con ecografia pelvica",
                    "Pap-test e HPV-test",
                    "Mammografia bilaterale",
                    "Consulenza nutrizionale 30 minuti",
                    "Esame del sangue profilo metabolico",
                    "Visita senologica di controllo",
                    "Referto unico entro 48 ore",
                ],
                "cta":      "Prenota il check-up",
                "is_popular": True,
                "popular_label": "Più richiesto",
            },
            {
                "eyebrow": "UOMO 45+",
                "title":   "Check-up Uomo 45+",
                "desc":    "Il controllo che tutti rimandiamo e non dovremmo mai "
                           "rimandare: cuore, prostata, metabolismo, fegato.",
                "price":   "€ 280",
                "price_meta": "tutto incluso",
                "duration": "3,5 ore",
                "exams_count": "7 esami",
                "includes": [
                    "Visita cardiologica con ECG",
                    "Ecocardiografia color-doppler",
                    "Visita urologica con PSA",
                    "Ecografia addome completo",
                    "Profilo lipidico e glicemico",
                    "Valutazione del rischio cardiovascolare",
                    "Referto unico entro 48 ore",
                ],
                "cta":      "Prenota il check-up",
                "is_popular": False,
                "popular_label": "",
            },
            {
                "eyebrow": "OVER 60",
                "title":   "Check-up Over 60",
                "desc":    "Un quadro completo coordinato da un medico internista "
                           "che tiene insieme cuore, ossa, cervello e occhi.",
                "price":   "€ 420",
                "price_meta": "tutto incluso",
                "duration": "4 ore",
                "exams_count": "9 esami",
                "includes": [
                    "Visita cardiologica + ecocardio + holter 24h",
                    "MOC densitometria ossea",
                    "Visita neurologica con test cognitivi",
                    "Visita oculistica con OCT retina",
                    "Tonometria e campo visivo",
                    "Profilo metabolico completo",
                    "Visita internistica di coordinamento",
                    "Colloquio finale con medico referente",
                    "Referto unico entro 48 ore",
                ],
                "cta":      "Prenota il check-up",
                "is_popular": False,
                "popular_label": "",
            },
        ],

        "how_label":   "Come funziona",
        "how_heading": 'Quattro passi <em>senza sorprese</em>.',
        "how_steps": [
            {"num": "01", "title": "Prenota online",
             "body": "Scegli il check-up più adatto e il giorno. Ti arriva "
                     "conferma via email con le istruzioni di preparazione."},
            {"num": "02", "title": "Digiuno la mattina",
             "body": "Per gli esami del sangue serve digiuno di 8 ore. "
                     "Acqua naturale consentita fino a un'ora prima."},
            {"num": "03", "title": "Una mezza giornata da noi",
             "body": "Arrivi alle 7:30, esci entro mezzogiorno. Tutti gli "
                     "esami in sequenza, senza tempi morti tra uno e l'altro."},
            {"num": "04", "title": "Referto unico a 48 ore",
             "body": "Il medico coordinatore ti chiama per commentare i "
                     "risultati e consegnarti il PDF riepilogativo."},
        ],

        "cta_band": {
            "heading":    "Un check-up all'anno per dormire meglio.",
            "body":       "Prenota oggi, ti richiamiamo entro due ore per confermare data e istruzioni di preparazione.",
            "primary_cta":"Prenota un check-up",
            "secondary_cta":"Chiama 800 123 456",
        },
    },

    # ─── MEDICI (team) ───────────────────────────────────────────
    "medici": {
        "eyebrow":   "Medici · 40+ specialisti",
        "headline":  'Chi si prenderà cura <em>di te</em>.',
        "intro":
            "I sei medici che rappresentano i reparti più prenotati. "
            "Lo staff completo conta oltre 40 specialisti: se cerchi qualcuno "
            "in particolare, chiama la segreteria, ti aiutiamo a trovarlo.",

        "book_cta": "Prenota con lui/lei",

        "doctors": [
            {
                "portrait": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Cardiologia · responsabile di reparto",
                "name":     "Dr.ssa Elisa Conti",
                "credentials":
                    "Specializzazione in Cardiologia all'Università di Milano. "
                    "22 anni di pratica clinica, formazione al Centro Cardiologico "
                    "Monzino. Socio della Società Italiana di Cardiologia.",
                "tags": ["Cardiologia", "Ecocardio", "Prevenzione CV"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Pediatria · responsabile di reparto",
                "name":     "Dr. Marco Ferri",
                "credentials":
                    "Pediatra di libera scelta, specializzazione alla Clinica De Marchi. "
                    "18 anni con le famiglie milanesi, focus su neonatologia e "
                    "disturbi respiratori dell'infanzia.",
                "tags": ["0-14 anni", "Vaccinazioni", "Pneumologia pediatrica"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Dermatologia",
                "name":     "Dr.ssa Sofia Lenzi",
                "credentials":
                    "Dermatologa, specializzazione all'Università Vita-Salute San "
                    "Raffaele. Esperienza decennale in dermatoscopia digitale e "
                    "controlli oncologici della pelle.",
                "tags": ["Dermatoscopia", "Oncologia cutanea", "Acne"],
            },
            {
                "portrait": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Radiologia · direttore della diagnostica",
                "name":     "Dr. Luca Russo",
                "credentials":
                    "Radiologo, 25 anni di esperienza ospedaliera prima di passare "
                    "a SaluteVita nel 2015. Referente per risonanza e TAC, dirige "
                    "l'équipe di 6 tecnici di radiologia.",
                "tags": ["Risonanza 1.5T", "TAC", "Ecografia multi-organo"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Ginecologia · ostetricia",
                "name":     "Dr.ssa Chiara Moretti",
                "credentials":
                    "Ginecologa e ostetrica, specializzazione alla Mangiagalli. "
                    "Segue percorsi della gravidanza fisiologica, menopausa e "
                    "prevenzione oncologica femminile.",
                "tags": ["Gravidanza", "Menopausa", "Pap + HPV"],
            },
            {
                "portrait": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Ortopedia · medicina dello sport",
                "name":     "Dr. Paolo Serra",
                "credentials":
                    "Ortopedico, specializzazione all'Istituto Galeazzi. "
                    "Esperto in ecografia muscoloscheletrica e infiltrazioni "
                    "ecoguidate, segue atleti di serie A e amatoriali.",
                "tags": ["Ecografia muscolare", "Infiltrazioni", "Sport"],
            },
        ],

        "footnote_strong": "Oltre 40 specialisti nello staff completo.",
        "footnote_body":
            "Neurologia, oculistica, otorinolaringoiatria, urologia, endocrinologia "
            "e altre 7 specialità. Contatta la segreteria per conoscere il medico "
            "giusto per la tua richiesta: ",
        "footnote_link": "scrivici dalla pagina contatti",
    },

    # ─── CONTATTI (contact) ──────────────────────────────────────
    "contatti": {
        "eyebrow":   "Contatti · via Galvani 18 · Milano",
        "headline":  'Siamo <em>dove serve</em>: a due passi dalla Centrale.',
        "intro":
            "Reception aperta dalle 7:00 alle 21:00 dal lunedì al venerdì. "
            "Scrivici o chiamaci: rispondiamo entro due ore nei giorni "
            "lavorativi, senza risponditori automatici.",

        "map_aria":    "Mappa illustrativa della sede SaluteVita in Via Galvani 18, Milano",
        "map_stamp":   "Via Galvani 18 · Milano Centrale",

        "address_label": "Indirizzo",
        "email_label":   "Email",

        "hours_heading": "Orari di apertura",
        "hours_table": [
            ("Lunedì – Venerdì",  "7:00 – 21:00"),
            ("Sabato",             "8:00 – 18:00"),
            ("Domenica",           "Chiuso"),
            ("Festivi",            "Chiuso · numero verde attivo"),
        ],

        "access": [
            {"icon": "car",        "title": "Parcheggio convenzionato",
             "body": "Garage Centrale a 40 metri. € 2/ora per i pazienti SaluteVita."},
            {"icon": "metro",      "title": "Metropolitana",
             "body": "M2/M3 Stazione Centrale · 4 minuti a piedi. Tram 5 e 9 davanti."},
            {"icon": "wheelchair", "title": "Accesso disabili",
             "body": "Ingresso senza barriere, ascensore, bagno attrezzato al piano terra."},
            {"icon": "info",       "title": "Urgenze",
             "body": "Non siamo un pronto soccorso. Per urgenze sanitarie chiamare 112."},
        ],

        "form_title": "Scrivici un messaggio",
        "form_intro":
            "Se hai una domanda generica o vuoi informazioni prima di prenotare, "
            "scrivici qui. Rispondiamo entro due ore lavorative.",

        "form_fields": [
            {"name": "nome",       "label": "Nome",       "type": "text",     "placeholder": "Mario",              "required": True},
            {"name": "cognome",    "label": "Cognome",    "type": "text",     "placeholder": "Rossi",              "required": True},
            {"name": "email",      "label": "Email",      "type": "email",    "placeholder": "mario.rossi@email.it", "required": True},
            {"name": "telefono",   "label": "Telefono",   "type": "tel",      "placeholder": "+39 ...",             "required": False},
            {"name": "specialita", "label": "Specialità di interesse", "type": "select", "required": False,
             "options": ["Cardiologia", "Pediatria", "Dermatologia", "Radiologia",
                         "Ginecologia", "Ortopedia", "Neurologia", "Oculistica",
                         "Altro / informazioni generali"]},
            {"name": "oggetto",    "label": "Oggetto",    "type": "text",     "placeholder": "Informazioni prevenzione", "required": True},
            {"name": "messaggio",  "label": "Messaggio",  "type": "textarea", "placeholder": "Raccontaci brevemente di cosa hai bisogno…",
             "required": True, "full_width": True,
             "helper": "Non inviare dati sanitari sensibili in questo modulo: per referti usa l'area paziente."},
        ],
        "consent":
            "Acconsento al trattamento dei dati personali ai sensi del Regolamento UE "
            "2016/679 per l'unico scopo di rispondere a questa richiesta.",
        "submit_label": "Invia messaggio",
        "form_note":    "Risposta entro 2 ore lavorative",
    },

    # ─── PRENOTA (appointment) ───────────────────────────────────
    "prenota": {
        "eyebrow":   "Prenota · online in 30 secondi",
        "headline":  'Scegli quando, <em>noi ci occupiamo del resto</em>.',
        "intro":
            "Compila il modulo sotto: ti richiamiamo entro due ore lavorative "
            "per confermare data, medico e preparazione. Se preferisci parlare "
            "con una persona, chiama il numero verde 800 123 456.",

        # Premium forms sections (D-066 compliance)
        "form_sections": [
            {"num": "01", "title": "I tuoi dati", "meta": "richiesto per contattarti",
             "fields": ["nome", "cognome", "email", "telefono", "data_nascita", "codice_fiscale"]},
            {"num": "02", "title": "Dettagli visita", "meta": "tipo e specialità",
             "fields": ["specialita", "medico_preferito", "tipo_visita", "convenzione"]},
            {"num": "03", "title": "Quando ti va bene", "meta": "ti richiamiamo per confermare",
             "fields": ["data_preferita", "fascia_orario", "note"]},
        ],

        "form_fields": [
            # Section 01 — dati paziente
            {"name": "nome",            "label": "Nome",            "type": "text",  "placeholder": "Mario",               "required": True},
            {"name": "cognome",         "label": "Cognome",         "type": "text",  "placeholder": "Rossi",               "required": True},
            {"name": "email",           "label": "Email",           "type": "email", "placeholder": "mario.rossi@email.it","required": True,
             "helper": "Ti mandiamo il promemoria SMS e il referto digitale qui."},
            {"name": "telefono",        "label": "Telefono",        "type": "tel",   "placeholder": "+39 335 ...",          "required": True},
            {"name": "data_nascita",    "label": "Data di nascita", "type": "date",  "placeholder": "gg/mm/aaaa",           "required": True},
            {"name": "codice_fiscale",  "label": "Codice fiscale",  "type": "text",  "placeholder": "RSSMRA80A01F205X",     "required": False,
             "helper": "Utile se hai una convenzione: lo recuperiamo più veloce."},
            # Section 02 — dettagli visita
            {"name": "specialita",      "label": "Specialità",      "type": "select","required": True,
             "options": ["Cardiologia", "Pediatria", "Dermatologia",
                         "Radiologia & Diagnostica", "Ginecologia",
                         "Ortopedia & Fisioterapia", "Neurologia", "Oculistica",
                         "Check-up di prevenzione", "Altra specialità"]},
            {"name": "medico_preferito","label": "Medico preferito","type": "select","required": False,
             "options": ["Nessuna preferenza · primo disponibile",
                         "Dr.ssa Elisa Conti · Cardiologia",
                         "Dr. Marco Ferri · Pediatria",
                         "Dr.ssa Sofia Lenzi · Dermatologia",
                         "Dr. Luca Russo · Radiologia",
                         "Dr.ssa Chiara Moretti · Ginecologia",
                         "Dr. Paolo Serra · Ortopedia",
                         "Dr. Andrea Villa · Neurologia",
                         "Dr.ssa Laura Bianchi · Oculistica"]},
            {"name": "tipo_visita",     "label": "Tipo di visita",  "type": "select","required": True,
             "options": ["Prima visita", "Visita di controllo", "Esame diagnostico",
                         "Consulenza urgente (entro 24-48h)"]},
            {"name": "convenzione",     "label": "Usa una convenzione?", "type": "select", "required": False,
             "options": ["Nessuna · pago privatamente",
                         "Unisalute", "Generali Welion", "RBM Salute",
                         "Previmedical", "Caspie", "MioDottore", "Consap",
                         "Inail", "Altra assicurazione / fondo cassa"]},
            # Section 03 — preferenze orario
            {"name": "data_preferita",  "label": "Data preferita",  "type": "date",  "placeholder": "gg/mm/aaaa", "required": True,
             "helper": "Scegli entro 30 giorni. Se trovi posto prima, ti avvisiamo."},
            {"name": "fascia_orario",   "label": "Fascia oraria",   "type": "select","required": True,
             "options": ["Mattina presto · 7:00 – 9:00",
                         "Mattina · 9:00 – 12:00",
                         "Primo pomeriggio · 13:00 – 16:00",
                         "Tardo pomeriggio · 16:00 – 19:00",
                         "Sera · 19:00 – 21:00",
                         "Nessuna preferenza"]},
            {"name": "note",            "label": "Note per il medico", "type": "textarea",
             "placeholder": "Scrivi qui eventuali sintomi, terapie in corso o domande specifiche…",
             "required": False, "full_width": True,
             "helper": "Facoltativo. Ti chiediamo solo ciò che serve al medico per prepararsi."},
        ],

        "consent":
            "Acconsento al trattamento dei dati personali secondo il Regolamento UE "
            "2016/679 e l'informativa sanitaria di SaluteVita. I dati saranno "
            "utilizzati esclusivamente per la gestione della prenotazione.",
        "submit_label":     "Conferma prenotazione",
        "form_submit_note": "Ti richiamiamo entro 2 ore lavorative",

        # Sidebar "come funziona"
        "help_title": "Come funziona la prenotazione",
        "help_steps": [
            {"num": "1", "title": "Compili il modulo",
             "body": "Bastano 90 secondi. Nessun pagamento anticipato richiesto."},
            {"num": "2", "title": "Ti richiamiamo in 2 ore",
             "body": "Una persona della segreteria conferma data, medico e indicazioni di preparazione."},
            {"num": "3", "title": "Promemoria SMS",
             "body": "Due giorni prima ricevi SMS con data, orario e ambulatorio."},
            {"num": "4", "title": "Referto digitale",
             "body": "Entro 24-48h referto e prescrizioni nella tua area paziente, scaricabili in PDF."},
        ],

        # Sidebar "alternativa"
        "alt_title": "Preferisci parlare con una persona?",
        "alt_body":
            "Il numero verde è gratuito e attivo 7 giorni su 7, dalle 7:00 alle 21:00. "
            "Rispondiamo in media in meno di 40 secondi.",

        # Trust bullets
        "trust": [
            "Dati crittografati end-to-end (AES-256, standard sanitario)",
            "Disdici o sposta fino a 24h prima, senza costi",
            "Convenzioni con 8 principali assicurazioni e casse sanitarie",
        ],
    },
}
