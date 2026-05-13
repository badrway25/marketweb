"""Petro · Studio Veterinario Cane Gatto Esotici · Italian content tree.

Wave 1 Pass-7 (T51 · 2026-05-12). Fourth template on the `specialist`
archetype after Cardio + Dermatologia + Denti. Zero new HTML files —
reuses `templates/live_templates/medical/specialist/` skin verbatim.

Differentiation against the 3 prior specialist reuses:
  * Cardio  · cardiology     · #9c2a2a red          · Cormorant + Inter   · Dr. R. Marani      · Roma Parioli · "su misura"
  * Derm    · dermatology    · #3d5437 forest-green · Bodoni Moda + Inter · Dr.ssa Ricciardi   · Roma Veneto · "carta d'identità"
  * Denti   · dentistry      · #0F2D40 + #2BC4A4 mint · DM Serif Display + Inter · Dr.ssa Vespa · Milano Brera · "igiene"
  * Petro   · veterinary     · #1c1612 + #A86E3C bronze-tabacco · Lora + Inter · Dr. Marco Petro · Padova · "cura preventiva"

Voice anchor: `cura preventiva` — the load-bearing veterinary
clinical promise (preventive medicine: vaccinations, annual check-up,
geriatric screening) repeated as italic em across surfaces. Distinct
from human-medical anchors (su misura · carta d'identità · igiene)
because it foregrounds the preventive-care model that defines the
veterinary practice register: animals don't speak — the vet's job is
to read what they cannot say before disease arrives.

Brand:        Studio Veterinario Petro · Cane Gatto Esotici (Padova, Borgo Trento)
Palette:      #1c1612 ink + #f7f3ee cream + #A86E3C bronze-tabacco
              (4th polarity — NOT red NOT green NOT mint NOT deep-blue)
Typography:   Lora + Inter (humanist book serif · veterinary textbook
              register · NOT Cormorant/Bodoni/DM Serif)
Lead doctor:  Dr. Marco Petro, veterinario · classe 1974 (oldest +
              wisdom register vs Denti's classe ~1980 Vespa) ·
              Università di Padova vet faculty + Royal Veterinary
              College London + Cornell University Vet School stage ·
              gender male (counterbalances Denti+Derm female)
Visit verb:   "Prenota una visita preventiva" (preventive-booking
              conversion · distinct from Cardio/Derm `private-request`
              `Richiedi visita privata` and Denti `booking-widget`
              `Prenota igiene`)
Imagery:      Pet-clinic warm — veterinarian examining dog/cat/exotic
              pets · X.3 curator pack `docs/content-factory/imagery/
              packs/veterinary.md` (24 Pexels CC0 URLs · 8 hero / 5
              portrait / 5 detail / 6 gallery) consumed verbatim ·
              ZERO URL overlap with medical-cardiology (Unsplash) /
              medical-dermatology (Unsplash) / medical-dental
              (Pexels).
Cluster:      `veterinary` (medical category) — activates for the
              first time (was 0 templates). Pre-seeded in
              seed_profession_clusters.py:287-293.

IT-only at T51 Pass-7 build per D-102 cadence (workflow A.5 phase).
EN/FR/ES/AR locale trees land as T52 workflow C multilingual rollout.
Tier stays `draft` until that multilingual pass + AAA walk + public
flip handshake. Staff preview reachable via `?preview=1`.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from the X.3 curator pack
# `docs/content-factory/imagery/packs/veterinary.md`. All URLs
# Pexels License (CC0-compatible · commercial use OK).
_CHIEF_PORTRAIT = (
    # Veterinarian with white coat examining a small dog · matches
    # Dr. Petro "veterinario direttore" hands-on persona
    "https://images.pexels.com/photos/6235648/pexels-photo-6235648.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_STUDIO_IMAGE = (
    # Veterinary clinic interior — exam table + bright clinical
    "https://images.pexels.com/photos/7468978/pexels-photo-7468978.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop"
)
_LEAD_IMAGE = (
    # Bright veterinary clinic consultation · used as blog_list lead
    "https://images.pexels.com/photos/6235244/pexels-photo-6235244.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_MAP_FALLBACK = (
    # Modern veterinary clinic reception · map-fallback when Mapbox
    # tile fails to load
    "https://images.pexels.com/photos/6235241/pexels-photo-6235241.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_SERVICE_IMAGE = (
    # Vet auscultating cat patient close-up — visite page hero
    "https://images.pexels.com/photos/7470779/pexels-photo-7470779.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=900&fit=crop"
)


PETRO_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Studio",                "kind": "home"},
        {"slug": "studio",          "label": "Lo Studio",             "kind": "about"},
        {"slug": "visite",          "label": "Visite",                "kind": "services"},
        {"slug": "medici",          "label": "Veterinari",            "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Diario clinico",        "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contatti",              "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Prenota una visita",    "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "P",
        "logo_word":    "Petro",
        "tag":          "Studio veterinario · Padova Borgo Trento · cane gatto esotici",
        "phone":        "+39 049 6731 220",
        "email":        "studio@studiopetro.it",
        "address":      "Via Belzoni 71 · 35121 Padova",
        "hours_compact": "Lun – Ven · 8:00 – 20:00 · Sab 9:00 – 13:00",
        "hours_footer_rows": [
            "Domenica · solo emergenze su chiamata",
            "Reperibilità notturna 24/7 · +39 333 410 7726",
        ],
        "license":      "Iscrizione Ordine Veterinari Padova n. 1428 · Direttore sanitario Dr. M. Petro",
        "footer_intro":
            "Studio veterinario indipendente di medicina preventiva, "
            "chirurgia dei tessuti molli e cura geriatrica per cane, "
            "gatto e piccoli esotici. Tre veterinari, una sola cartella "
            "per ogni animale, reperibilità notturna su chiamata.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Medicina veterinaria · Padova Borgo Trento",
        "headline": "Gli animali non parlano. La <em>cura preventiva</em> ascolta prima.",
        "intro":
            "Visite preventive annuali, vaccinazioni a calendario, "
            "diagnostica per immagini e chirurgia dei tessuti molli "
            "per cane, gatto e piccoli esotici. Tre veterinari "
            "associati, reperibilità notturna su chiamata, una sola "
            "cartella clinica condivisa per ogni paziente.",
        "primary_cta":   "Prenota una visita preventiva",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "I veterinari",
        "secondary_href":"medici",

        "facts": [
            ("17",    "anni di studio veterinario indipendente"),
            ("4.200", "animali curati ogni anno"),
            ("3",     "veterinari associati in sede"),
        ],

        "manifesto_drop_cap": "G",
        "manifesto":
            "li animali non descrivono il dolore: lo nascondono. Il "
            "gatto si rifugia, il cane mangia di meno, il coniglio "
            "smette di muoversi. Per questo da Petro la medicina è "
            "soprattutto preventiva — visita annuale completa, "
            "screening geriatrico semestrale dai sette anni in su, "
            "controllo dentale ogni due, vaccinazioni a calendario. "
            "Quando l'animale arriva in studio per sintomi visibili, "
            "spesso siamo già alla metà del problema. La nostra "
            "cartella clinica esiste per arrivarci prima.",

        "hero_sidebar_top_label": "Direzione clinica",
        "hero_sidebar_quote":
            "«Gli animali non dicono dove fa male. La visita "
            "preventiva è l'unico modo onesto di praticare la "
            "medicina veterinaria — il resto è solo emergenza.»",
        "hero_sidebar_author": "— Dr. Marco Petro · Direttore sanitario · Iscrizione OMV Padova 1428",
        "hero_sidebar_pulse": [
            ("Studio",      "Padova · Borgo Trento"),
            ("Dal",         "2008"),
            ("Riferimento", "Cane gatto esotici"),
        ],

        "anchor_nav": [
            ("metodo",        "Metodo clinico"),
            ("visite",        "Visite preventive"),
            ("percorso",      "Percorso paziente"),
            ("medico",        "Direzione clinica"),
            ("studio",        "Sede & contatti"),
        ],

        "signature_visits_label":   "Quattro famiglie di intervento",
        "signature_visits_heading": "Quattro percorsi clinici, <em>una sola cartella per ogni animale.</em>",
        "signature_visits_intro":
            "Le quattro famiglie più richieste della medicina "
            "veterinaria di piccoli animali. L'elenco completo è "
            "nella pagina Visite.",
        "signature_visits": [
            ("01", "Visita preventiva annuale",
             "Esame obiettivo completo, peso e BCS, ascoltazione "
             "cardiopolmonare, palpazione addominale, controllo "
             "dentale, anamnesi vaccinale e profilassi parassitaria. "
             "Quaranta minuti, su appuntamento."),
            ("02", "Vaccinazioni & profilassi",
             "Vaccini cane (DA2PPi-L) e gatto (FRCP-FeLV) secondo "
             "calendario WSAVA. Profilassi filaria, leishmania, "
             "zecche. Vaccini coniglio (RHDV-Mixoma) e furetto. "
             "Libretto sanitario aggiornato in sede."),
            ("03", "Chirurgia tessuti molli",
             "Sterilizzazione cane e gatto in laparoscopia (mini "
             "invasiva, ridotti tempi di recupero), asportazione "
             "neoformazioni cutanee, chirurgia oncologica con esame "
             "istologico, suture estetiche."),
            ("04", "Diagnostica per immagini",
             "Ecografia addominale e cardiaca in sede, "
             "radiografia digitale con immagini consegnate al "
             "proprietario, citologia ago-aspirato letta in 24 ore "
             "dal laboratorio convenzionato Università di Padova."),
        ],

        "trattamenti_tabs": {
            "label":   "Listino visite & interventi",
            "heading": "Cosa facciamo, con <em>quale criterio.</em>",
            "intro":
                "Quattro famiglie cliniche, ciascuna con un "
                "protocollo scritto e un costo dichiarato. Niente "
                "preventivi personalizzati per le voci di routine — "
                "solo per piani di cura strutturati (chirurgia "
                "complessa, terapia oncologica, riabilitazione).",
            "tabs": [
                {
                    "id":      "preventiva",
                    "label":   "Preventiva",
                    "eyebrow": "Medicina preventiva",
                    "heading": "Quaranta minuti, una volta l'anno.",
                    "body":
                        "La visita preventiva annuale non è un controllo "
                        "veloce: è una valutazione clinica completa di "
                        "quaranta minuti con anamnesi, esame obiettivo "
                        "sistematico, controllo dentale, peso/BCS, "
                        "ascoltazione e palpazione. Dai sette anni in su "
                        "si aggiunge lo screening geriatrico semestrale.",
                    "items": [
                        ("Visita preventiva annuale cane/gatto", "40 min · € 65"),
                        ("Screening geriatrico (≥ 7 anni)", "60 min · € 95"),
                        ("Visita preventiva esotici (coniglio/furetto)", "45 min · € 75"),
                        ("Anamnesi pre-adozione cucciolo/gattino", "30 min · € 50"),
                    ],
                    "cta_label": "Tutti i protocolli preventivi →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "vaccinazioni",
                    "label":   "Vaccinazioni",
                    "eyebrow": "Vaccini & profilassi parassitaria",
                    "heading": "Protocollo WSAVA, libretto in sede.",
                    "body":
                        "I vaccini seguono le linee guida WSAVA (cane "
                        "DA2PPi-L core annuale, gatto FRCP-FeLV core "
                        "triennale dopo richiamo). Il libretto sanitario "
                        "si rilascia in sede, anche elettronico via app. "
                        "Profilassi antiparassitaria mensile o "
                        "trimestrale secondo razza e contesto.",
                    "items": [
                        ("Vaccino cane DA2PPi-L (annuale)", "appuntamento · € 45"),
                        ("Vaccino gatto FRCP + FeLV", "appuntamento · € 55"),
                        ("Vaccino coniglio RHDV1+2 / Mixoma", "appuntamento · € 50"),
                        ("Profilassi filaria + zecche (12 mesi)", "piano · € 95"),
                    ],
                    "cta_label": "Calendario vaccinale completo →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "chirurgia",
                    "label":   "Chirurgia",
                    "eyebrow": "Chirurgia tessuti molli",
                    "heading": "Laparoscopia mini-invasiva sempre che possibile.",
                    "body":
                        "Sterilizzazione cane e gatto in laparoscopia "
                        "(tre piccoli accessi · ricovero giornaliero · "
                        "ridotto dolore post-operatorio). Asportazione "
                        "neoformazioni cutanee con esame istologico "
                        "presso il laboratorio di Anatomia patologica "
                        "dell'Università di Padova. Suture estetiche "
                        "sottocuticulari riassorbibili.",
                    "items": [
                        ("Sterilizzazione gatta (laparoscopia)", "intervento · € 320"),
                        ("Sterilizzazione cagna < 20 kg", "intervento · € 480"),
                        ("Sterilizzazione cagna > 20 kg", "intervento · € 620"),
                        ("Asportazione neoformazione cutanea + istologico", "intervento · € 220"),
                    ],
                    "cta_label": "Percorsi chirurgici completi →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "diagnostica",
                    "label":   "Diagnostica",
                    "eyebrow": "Diagnostica per immagini & laboratorio",
                    "heading": "Eco, radiografia digitale, citologia in 24 ore.",
                    "body":
                        "Ecografia addominale e cardiaca in sede con "
                        "Esaote MyLab Omega · radiografia digitale "
                        "Carestream con consegna delle immagini al "
                        "proprietario via cloud · citologia ago-aspirato "
                        "letta in 24 ore dal laboratorio di Anatomia "
                        "patologica dell'Università di Padova. Esami "
                        "ematochimici processati in sede in 30 minuti.",
                    "items": [
                        ("Ecografia addominale completa", "30 min · € 95"),
                        ("Ecografia cardiaca (ecocardio)", "45 min · € 130"),
                        ("Radiografia digitale (2 proiezioni)", "20 min · € 75"),
                        ("Esami ematochimici completi in sede", "30 min · € 85"),
                    ],
                    "cta_label": "Protocolli diagnostici →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Direzione clinica",
        "chief_heading": "Un solo veterinario <em>firma ogni cartella.</em>",
        "chief": {
            "name":  "Dr. Marco Petro",
            "role":  "Direttore sanitario · Medicina interna & chirurgia tessuti molli",
            "bio":
                "Laurea in Medicina Veterinaria all'Università di Padova "
                "nel 2000, perfezionamento al Royal Veterinary College "
                "di Londra (2002-2004) in piccoli animali, stage di "
                "specializzazione alla Cornell University Vet School "
                "(NY, USA) nel 2006. Membro SCIVAC (Società Culturale "
                "Italiana Veterinari Animali Compagnia) e ANMVI "
                "(Associazione Nazionale Medici Veterinari Italiani). "
                "Iscrizione Ordine Veterinari Padova n. 1428 dal 2001. "
                "Direttore sanitario dello studio dal 2008.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "percorso": {
            "label":   "Percorso paziente",
            "heading": "Cosa aspettarsi dalla <em>prima visita.</em>",
            "intro":
                "La prima visita allo studio dura un'ora ed è dedicata "
                "alla costruzione della cartella clinica completa: "
                "anamnesi, esame obiettivo, eventuale ecografia "
                "addominale di base, piano di cura scritto. Mai "
                "interventi non urgenti alla prima visita.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Check-in & anamnesi",
                    "desc": "Segreteria, scheda anamnestica completa "
                            "(razza, età, alimentazione, ambiente, "
                            "convivenza con altri animali), eventuali "
                            "esami pregressi del veterinario precedente.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Esame obiettivo completo",
                    "desc": "Peso e Body Condition Score, ascoltazione "
                            "cardiopolmonare, palpazione addominale, "
                            "ispezione cavo orale, controllo cute e "
                            "mantello, palpazione linfonodi.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Diagnostica di base",
                    "desc": "Ecografia addominale orientativa (se "
                            "indicata), eventuali prelievi per esami "
                            "ematochimici processati in sede in trenta "
                            "minuti. Radiografia se sospetto trauma.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Piano di cura scritto",
                    "desc": "Discussione con il proprietario del piano "
                            "preventivo o terapeutico, preventivo "
                            "dettagliato voce per voce, consegna anche "
                            "via mail in formato PDF.",
                    "duration": "10 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Programmazione & follow-up",
                    "desc": "Calendario delle visite di richiamo, "
                            "promemoria via WhatsApp per vaccini e "
                            "profilassi, canale diretto con la "
                            "segreteria per dubbi non urgenti.",
                    "duration": "5 min",
                },
            ],
        },

        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
        "press_label": "Pubblicato su",

        "faq": {
            "label": "Domande frequenti",
            "heading": "Le domande che <em>i proprietari ci rivolgono più spesso.</em>",
            "items": [
                ("Ogni quanto serve una visita preventiva?",
                 "Per cane e gatto adulti sani la cadenza è annuale. "
                 "Dai sette anni in su (animali geriatrici) si aggiunge "
                 "una visita di screening semestrale con esami "
                 "ematochimici. Per coniglio e furetto la cadenza è "
                 "semestrale fin dalla prima visita perché "
                 "l'aspettativa di vita è più breve."),
                ("Praticate la sterilizzazione laparoscopica?",
                 "Sì, su gatta e cagna fino a 35 kg. La sterilizzazione "
                 "in laparoscopia comporta tre piccoli accessi "
                 "addominali da 5 mm invece dell'incisione "
                 "tradizionale, ricovero giornaliero, dolore "
                 "post-operatorio ridotto e ritorno alla normalità "
                 "in 48 ore. Sulle taglie superiori a 35 kg si valuta "
                 "caso per caso."),
                ("Visitate anche conigli, furetti, uccelli e rettili?",
                 "Coniglio, furetto e cavia sì, su tutti i percorsi "
                 "(preventiva, vaccinazioni, chirurgia, diagnostica). "
                 "Uccelli e rettili solo per visite di base — per "
                 "patologie complesse rimandiamo a colleghi specialisti "
                 "in animali esotici delle cliniche universitarie."),
                ("Avete servizio di reperibilità notturna?",
                 "Sì, il dottor Petro è reperibile 24/7 per i propri "
                 "pazienti al numero +39 333 410 7726. Per emergenze "
                 "su animali non in cartella indirizziamo all'Ospedale "
                 "Veterinario dell'Università di Padova (Legnaro, "
                 "aperto 24h) oppure alla Clinica San Marco di "
                 "Veggiano."),
                ("Come funziona il piano di prevenzione annuale?",
                 "Comprende visita preventiva, vaccini cane DA2PPi-L o "
                 "gatto FRCP, profilassi mensile filaria e zecche, "
                 "screening ematochimico annuale, un richiamo "
                 "semestrale gratuito. Costo € 245/anno per cane, "
                 "€ 195/anno per gatto. Sconto 15% sugli interventi "
                 "chirurgici programmati nei dodici mesi successivi."),
            ],
        },

        "cta_heading":
            "Ogni piano di cura è <em>scritto, dichiarato, condiviso col proprietario.</em>",
        "cta_primary_label":   "Prenota una visita preventiva",
        "cta_secondary_label": "Contatti dello studio",

        "location": {
            "label":   "Sede dello studio",
            "heading": "Via Belzoni 71, <em>Padova.</em>",
            "intro":
                "Lo studio occupa il piano terra di un edificio "
                "ottocentesco in zona Borgo Trento, a quattrocento "
                "metri dalla Stazione Centrale e dieci minuti a piedi "
                "dalla Facoltà di Medicina Veterinaria. Tre sale "
                "visita separate cane/gatto/esotici, sala chirurgica, "
                "sala diagnostica con ecografo ed Rx digitale, area "
                "ricovero giornaliero.",
            "map_image": "",
            "map_fallback_image": _MAP_FALLBACK,
            "details": [
                ("Indirizzo",
                 "Via Belzoni 71\n35121 Padova"),
                ("Stazione",
                 "Padova Centrale\n6 minuti a piedi"),
                ("Parcheggio",
                 "Parcheggio Borgo Trento gratuito\n80 metri dallo studio"),
                ("Accessibilità",
                 "Ingresso a piano terra senza scalini\naccessibile a carrozzine e trasportini grandi"),
            ],
            "hours_short": [
                ("Lun – Ven", "8:00 – 20:00"),
                ("Sabato",    "9:00 – 13:00"),
                ("Domenica",  "Solo emergenze su chiamata"),
            ],
            "cta_label": "Ottieni indicazioni stradali",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) ────────────────────────────────────────
    "studio": {
        "eyebrow":   "Lo studio · Padova Borgo Trento",
        "headline":  "Tre veterinari, <em>una cartella per ogni animale.</em>",
        "intro":
            "Studio Veterinario Petro è uno studio associato fondato "
            "nel 2008 da Marco Petro insieme a due colleghi formatisi "
            "all'Università di Padova. Tre veterinari, una sola "
            "cartella clinica condivisa per ogni paziente, una sola "
            "firma in calce a ogni piano di cura. Reperibilità "
            "notturna su chiamata per i pazienti in cartella.",
        "history": [
            ("2008",
             "Marco Petro apre lo studio in Via Belzoni con un solo "
             "ambulatorio e un'assistente. Settantacinque animali in "
             "cartella nel primo anno."),
            ("2012",
             "Ingresso della Dr.ssa Anna Bressan come secondo "
             "veterinario associato · specializzazione in animali "
             "esotici (coniglio, furetto, cavia, piccoli rettili)."),
            ("2015",
             "Apertura della sala chirurgica con anestesia inalatoria "
             "isofluorano e monitoraggio multiparametrico. Avvio "
             "della chirurgia laparoscopica per le sterilizzazioni."),
            ("2018",
             "Acquisto dell'ecografo Esaote MyLab Omega e dell'Rx "
             "digitale Carestream. Tutta la diagnostica per immagini "
             "viene portata in sede."),
            ("2023",
             "Ingresso del Dr. Tommaso Zen come terzo associato · "
             "specializzazione in oncologia veterinaria e chirurgia "
             "ricostruttiva. Lo studio chiude l'anno con 4.200 "
             "animali in cartella."),
        ],
        "studio_image": _STUDIO_IMAGE,
        "studio_image_caption": "Sala visita · Via Belzoni 71 · Padova",
        "method_title": "Il metodo Petro",
        "method_paragraphs": [
            "La medicina veterinaria di piccoli animali non somiglia "
            "alla medicina umana per un motivo: il paziente non parla. "
            "Il gatto che inizia a bere il triplo del normale ha già "
            "una insufficienza renale a metà strada. Il cane che zoppica "
            "a giorni alterni ha già un'artrosi avanzata. Per questo da "
            "Petro la cura preventiva non è un servizio aggiuntivo: è "
            "il primo capitolo, e per molti pazienti è anche l'unico "
            "che davvero serve.",
            "La cartella clinica è una sola — la stessa per i tre "
            "associati — perché un animale non è il paziente di un "
            "singolo veterinario, è il paziente dello studio. Quando "
            "Anna nota una neoformazione cutanea sospetta durante la "
            "vaccinazione, lo segnala a Tommaso per l'asportazione "
            "chirurgica nello stesso documento clinico. Niente cure "
            "frammentate, niente referti che si perdono fra colleghi.",
            "I costi sono dichiarati per le voci di routine (visita "
            "preventiva, vaccini, sterilizzazione, ecografia, "
            "diagnostica di base). Per i piani strutturati — terapia "
            "oncologica, riabilitazione post-traumatica, chirurgia "
            "ortopedica complessa — il preventivo è personalizzato "
            "dopo una valutazione clinica completa, ma sempre "
            "consegnato per iscritto e firmato in calce.",
        ],
        "values_label":   "Valori dello studio",
        "values_heading": "Quattro impegni, <em>scritti in cartella.</em>",
        "values": [
            ("Cura preventiva sempre",
             "La visita preventiva annuale è il punto di partenza "
             "di ogni rapporto con il paziente. Mai un intervento "
             "non urgente senza anamnesi completa."),
            ("Una sola cartella",
             "Tre veterinari condividono la stessa cartella "
             "clinica per ogni animale. Nessun referto perso, "
             "nessun follow-up mancato fra colleghi."),
            ("Costi dichiarati",
             "Tariffe scritte per le voci di routine. Preventivo "
             "in PDF firmato per ogni piano complesso prima "
             "dell'avvio dei trattamenti."),
            ("Reperibilità per i propri pazienti",
             "Reperibilità notturna 24/7 al numero diretto del "
             "dottor Petro per gli animali già in cartella. "
             "Nessun paziente lasciato a sé."),
        ],
        "cta_heading":
            "Il primo passo è sempre <em>una visita preventiva di un'ora.</em>",
        "cta_primary_label":   "Conosci i veterinari",
        "cta_secondary_label": "Prenota la prima visita",
        "press_label": "Pubblicato su",
        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
    },

    # ─── VISITE (services) ─────────────────────────────────────
    "visite": {
        "eyebrow":  "Visite & interventi",
        "headline": "Quattro famiglie di intervento, <em>una sola cartella per animale.</em>",
        "intro":
            "L'elenco completo dei percorsi clinici disponibili in "
            "sede. I costi indicati sono per le voci di routine; per "
            "piani strutturati il preventivo viene scritto dopo "
            "valutazione clinica completa.",
        "service_image": _SERVICE_IMAGE,
        "service_image_caption": "Ascoltazione cardiopolmonare · visita preventiva",
        # Treatments — 4-tuples (name, meta, desc, price) per
        # specialist services.html:121 unpacking contract.
        "treatments": [
            ("Visita preventiva annuale cane/gatto",
             "40 min · su appuntamento",
             "Anamnesi completa, peso e Body Condition Score, "
             "ascoltazione cardiopolmonare, palpazione addominale, "
             "controllo cavo orale, ispezione cute e mantello, "
             "palpazione linfonodi, verifica calendario vaccinale "
             "e antiparassitario.",
             "€ 65"),
            ("Screening geriatrico (≥ 7 anni)",
             "60 min · semestrale",
             "Visita completa + esami ematochimici (emocromo, "
             "funzionalità renale ed epatica, elettroliti, T4 nel "
             "gatto), pressione arteriosa, ecografia addominale "
             "orientativa. Indicato per cane e gatto dai sette anni "
             "in su.",
             "€ 95"),
            ("Vaccino cane DA2PPi-L (annuale)",
             "appuntamento · 30 min",
             "Vaccino combinato cimurro, adenovirus, parvovirus, "
             "parainfluenza, leptospirosi quattro ceppi (L4). "
             "Calendario WSAVA, libretto sanitario aggiornato in sede.",
             "€ 45"),
            ("Vaccino gatto FRCP + FeLV",
             "appuntamento · 30 min",
             "Vaccino combinato rinotracheite, calicivirus, "
             "panleucopenia + vaccino leucemia felina (FeLV). Per "
             "gatti che vivono in casa solo FRCP triennale dopo "
             "richiamo, costo € 40.",
             "€ 55"),
            ("Sterilizzazione gatta in laparoscopia",
             "intervento · ricovero giornaliero",
             "Ovariectomia mini-invasiva con tre accessi da 5 mm, "
             "anestesia inalatoria isofluorano, monitoraggio "
             "multiparametrico, suture sottocuticulari riassorbibili. "
             "Dimissione in giornata.",
             "€ 320"),
            ("Sterilizzazione cagna < 20 kg (laparoscopia)",
             "intervento · ricovero giornaliero",
             "Ovariectomia in laparoscopia con tre accessi "
             "addominali, anestesia inalatoria, analgesia "
             "multimodale post-operatoria, dimissione in giornata.",
             "€ 480"),
            ("Ecografia addominale completa",
             "30 min · su appuntamento",
             "Esaote MyLab Omega · valutazione di fegato, milza, "
             "reni, vescica, pareti gastrointestinali, linfonodi "
             "mesenterici, prostata. Referto consegnato in giornata.",
             "€ 95"),
            ("Ecocardiografia",
             "45 min · su appuntamento",
             "Studio ecografico delle camere cardiache, valutazione "
             "delle valvole, misurazione di frazione di eiezione e "
             "contrattilità. Indicato pre-anestesia su pazienti "
             "geriatrici o razze predisposte (Cavalier King Charles, "
             "Boxer, Maine Coon).",
             "€ 130"),
        ],
        "footnote_heading": "Cosa non facciamo in sede",
        "footnote":
            "Cardiologia interventistica, neurochirurgia, ortopedia "
            "ricostruttiva complessa, ostetricia degli equini. Per "
            "questi casi indirizziamo all'Ospedale Veterinario "
            "dell'Università di Padova (Legnaro) con cui abbiamo una "
            "convenzione diretta e una corsia preferenziale per i "
            "nostri pazienti.",
        "cta_heading":
            "Vuoi prenotare una <em>visita preventiva o un controllo?</em>",
        "cta_primary_label":   "Prenota una visita",
        "cta_secondary_label": "Conosci i veterinari",
    },

    # ─── MEDICI (team) ─────────────────────────────────────────
    "medici": {
        "eyebrow":  "I veterinari",
        "headline": "Tre veterinari associati, <em>tre specializzazioni complementari.</em>",
        "intro":
            "Tre veterinari condividono lo studio dal 2008 (Marco), "
            "dal 2012 (Anna) e dal 2023 (Tommaso). Tre specializzazioni "
            "complementari coprono medicina interna, animali esotici "
            "e chirurgia ricostruttiva. Una sola cartella clinica per "
            "ogni paziente.",
        "doctors": [
            {
                "name":  "Dr. Marco Petro",
                "role":  "Direttore sanitario",
                "specialty": "Medicina interna · chirurgia tessuti molli",
                "bio":
                    "Laurea Università di Padova 2000. Royal Veterinary "
                    "College Londra 2002-2004. Cornell University Vet "
                    "School (NY, USA) stage 2006. Iscrizione OMV Padova "
                    "1428 dal 2001. Direttore sanitario dal 2008. "
                    "Membro SCIVAC e ANMVI.",
                "portrait": _CHIEF_PORTRAIT,
                "year_label": "Dal",
                "year": "2008",
            },
            {
                "name":  "Dr.ssa Anna Bressan",
                "role":  "Veterinario associato",
                "specialty": "Animali esotici · coniglio, furetto, cavia, rettili",
                "bio":
                    "Laurea Università di Padova 2010. Master in "
                    "Medicina degli Animali Esotici a Cremona "
                    "(Università di Milano) 2011-2012. Membro AAEMV "
                    "(Associazione Italiana Veterinari per Animali "
                    "Esotici). Conduce la sezione esotici dello "
                    "studio dal 2012.",
                "portrait":
                    "https://images.pexels.com/photos/6235113/pexels-photo-6235113.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Dal",
                "year": "2012",
            },
            {
                "name":  "Dr. Tommaso Zen",
                "role":  "Veterinario associato",
                "specialty": "Oncologia veterinaria · chirurgia ricostruttiva",
                "bio":
                    "Laurea Università di Bologna 2014. "
                    "Specializzazione in Oncologia Veterinaria "
                    "all'Università di Madrid 2017-2019. "
                    "Pubblicazioni su Journal of Small Animal "
                    "Practice (2018) e Veterinary Surgery (2020). "
                    "Conduce la sezione chirurgica oncologica dello "
                    "studio dal 2023.",
                "portrait":
                    "https://images.pexels.com/photos/6234600/pexels-photo-6234600.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Dal",
                "year": "2023",
            },
        ],
        "portrait_city": "Padova · Borgo Trento",
    },

    # ─── PUBBLICAZIONI (blog_list) ─────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Diario clinico dello studio",
        "headline": "Note di lavoro <em>dalla sala visita.</em>",
        "intro":
            "Brevi appunti dei tre veterinari sui protocolli clinici "
            "in uso, sui casi più rappresentativi dell'anno, sui "
            "vaccini e sulle profilassi di stagione. Lettura riservata "
            "ai proprietari di pazienti in cartella e ai colleghi.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Veterinario Petro · Il diario clinico",
        "empty_body_fallback_paragraphs": [
            "Articolo in preparazione editoriale. La pubblicazione "
            "integrale sarà disponibile a breve, scritta personalmente "
            "da uno dei tre veterinari associati.",
            "Questo segnaposto descrive la voce del Diario Clinico: "
            "brevi note di lavoro, riflessioni sui protocolli "
            "preventivi, racconti di casi clinici rappresentativi. "
            "Mai più di duemila parole, mai meno di cinquecento.",
        ],
    },

    "posts": [
        {
            "slug":     "calendario-vaccinale-2026",
            "kicker":   "Vaccinazioni in corso",
            "title":    "Il calendario vaccinale dello studio · aggiornamento 2026",
            "date":     "8 ottobre 2026",
            "read_min": 4,
            "author":   "Dr. Marco Petro",
            "cover_image": _LEAD_IMAGE,
            "lede":
                "WSAVA ha rilasciato a settembre le nuove linee guida "
                "sui vaccini core per cane e gatto. Cosa cambia da "
                "ottobre 2026 nel calendario di richiamo dei nostri "
                "pazienti.",
            "body": [
                ("p", "Le linee guida WSAVA 2026 confermano la cadenza "
                      "annuale per i vaccini core cane (DA2PPi-L) e "
                      "consolidano il passaggio a triennale dopo "
                      "richiamo per i vaccini core gatto (FRCP) per "
                      "i gatti che vivono in ambiente domestico chiuso. "
                      "Per i gatti con accesso esterno la cadenza "
                      "rimane annuale anche per FRCP."),
                ("h2", "Cosa cambia per la profilassi"),
                ("p", "La leptospirosi quattro ceppi (L4) resta core "
                      "annuale per il cane in ambiente urbano padovano "
                      "— l'incidenza nelle ultime stagioni è risultata "
                      "stabile ma non in calo. Per il gatto in "
                      "ambiente domestico ricalibriamo a triennale il "
                      "FeLV dopo il richiamo del primo anno, mentre "
                      "per i gatti free-roaming il FeLV resta annuale."),
                ("h2", "Cosa facciamo da ottobre"),
                ("p", "I proprietari dei pazienti in cartella riceveranno "
                      "via WhatsApp il piano vaccinale aggiornato. Per "
                      "i nuovi pazienti il calendario viene costruito "
                      "alla prima visita preventiva sulla base di "
                      "razza, età, ambiente di vita e contatto con "
                      "altri animali."),
            ],
        },
        {
            "slug":     "sterilizzazione-laparoscopia-perche",
            "kicker":   "Chirurgia",
            "title":    "Perché preferiamo la laparoscopia per la sterilizzazione",
            "date":     "25 settembre 2026",
            "read_min": 5,
            "author":   "Dr. Tommaso Zen",
            "cover_image":
                "https://images.pexels.com/photos/7470769/pexels-photo-7470769.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "lede":
                "Dal 2015 lo studio esegue la sterilizzazione di "
                "gatte e cagne in laparoscopia mini-invasiva. Ecco "
                "perché è il nostro standard e quando facciamo "
                "ancora l'intervento tradizionale.",
            "body": [
                ("p", "La sterilizzazione in laparoscopia comporta tre "
                      "accessi addominali da 5 mm invece dell'incisione "
                      "tradizionale di 4-7 cm. La differenza non è "
                      "estetica: è prima di tutto fisiologica. Dolore "
                      "post-operatorio ridotto, ritorno alla normalità "
                      "in 48 ore, rischio di complicanze infettive "
                      "abbattuto, ricovero giornaliero invece di una "
                      "notte."),
                ("h2", "Quando facciamo ancora la chirurgia tradizionale"),
                ("p", "Tre situazioni cliniche. Primo: cagne sopra i "
                      "35 kg, dove l'accesso laparoscopico diventa "
                      "tecnicamente complesso (l'ovaio è profondo, lo "
                      "spazio operatorio limitato). Secondo: piometra "
                      "(infezione uterina) — l'utero va rimosso "
                      "intero e va bene anche l'accesso aperto. Terzo: "
                      "tumori ovarici, per la stessa ragione."),
                ("h2", "I numeri dello studio"),
                ("p", "Dal 2015 a oggi abbiamo eseguito circa 1.400 "
                      "sterilizzazioni laparoscopiche. Tasso di "
                      "complicanze maggiori sotto l'1 %. Tasso di "
                      "complicanze minori (sieromi, edemi locali) "
                      "intorno al 3 %. Indice di soddisfazione "
                      "del proprietario (questionario di follow-up "
                      "a sette giorni) sopra il 95 %."),
            ],
        },
    ],

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contatti & sede",
        "headline": "Tre canali, <em>una sola segreteria.</em>",
        "intro":
            "Per appuntamenti di routine si prenota dal modulo "
            "online o per telefono in orario di apertura. Per "
            "emergenze il numero di reperibilità è attivo 24/7 "
            "per i pazienti in cartella.",
        # Blocks — 3-tuples (label, value, sub) per specialist
        # contact.html:105 unpacking contract.
        "blocks": [
            ("Segreteria",
             "+39 049 6731 220",
             "Lun – Ven · 8:00 – 20:00 · Sab 9:00 – 13:00"),
            ("Reperibilità notturna",
             "+39 333 410 7726",
             "24/7 · solo per pazienti già in cartella"),
            ("Email",
             "studio@studiopetro.it",
             "Risposta entro 24 h in orario di apertura"),
            ("Sede",
             "Via Belzoni 71 · 35121 Padova",
             "Borgo Trento · 6 minuti dalla Stazione Centrale"),
        ],
        "form_title": "Scrivici",
        "form_intro":
            "Per appuntamenti di routine usa il modulo Prenota una "
            "visita. Questo modulo è per richieste generiche, "
            "richiesta di copia della cartella clinica, secondo "
            "parere o domande sui protocolli.",
        "form_placeholders": {
            "name":    "Nome e cognome",
            "email":   "Email",
            "phone":   "Telefono",
            "subject": "Oggetto",
            "message": "Come possiamo aiutarti? Indica anche il nome e la specie dell'animale.",
        },
        "form_helpers": {
            "name":    "Verrà usato per intestare l'eventuale risposta.",
            "email":   "Risponderemo entro 24 ore in orario di apertura.",
            "phone":   "Solo per richiedere richiami telefonici.",
            "subject": "Esempio: «richiesta secondo parere» o «copia cartella clinica».",
        },
        "form_consent":
            "Accetto il trattamento dei dati ai sensi del GDPR. Privacy policy disponibile in sede.",
        "form_submit_note":
            "Per emergenze cliniche su pazienti in cartella, "
            "chiamare il numero di reperibilità 24/7. Questo "
            "modulo non è monitorato fuori dagli orari di apertura.",
        "hours_heading": "Orari di apertura",
        # hours — 3-tuples (day, am, pm) per specialist contact.html:175.
        "hours": [
            ("Lun – Ven", "8:00 – 13:00", "14:30 – 20:00"),
            ("Sabato",    "9:00 – 13:00", "chiuso"),
            ("Domenica",  "chiuso",       "reperibilità su chiamata"),
        ],
        "transport_heading": "Come arrivare",
        "transport": [
            ("Treno",      "Stazione Centrale di Padova · 6 minuti a piedi"),
            ("Auto",       "Uscita Padova Est · 12 minuti in auto"),
            ("Tram",       "SIR1 fermata Borgo Trento · 2 minuti a piedi"),
            ("Parcheggio", "Parcheggio Borgo Trento gratuito · 80 metri dallo studio"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) ─────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Prenota una visita",
        "headline": "Una visita preventiva, <em>quaranta minuti.</em>",
        "intro":
            "Prenota online la prima visita preventiva del tuo "
            "animale. La segreteria conferma l'appuntamento entro "
            "24 ore in orario di apertura. Per emergenze chiamare "
            "il numero di reperibilità.",
        "process_label": "Come funziona",
        "process_heading": "Tre passaggi, <em>una sola visita.</em>",
        # process — 3-tuples (num, title, blurb) per specialist
        # appointment.html:97 unpacking contract.
        "process": [
            ("01", "Compila il modulo",
             "Indica il nome dell'animale, la specie, la razza, "
             "l'età, il motivo della visita. Eventuali esami "
             "pregressi possono essere allegati o portati in studio."),
            ("02", "Conferma in 24 ore",
             "La segreteria contatta entro 24 ore per confermare "
             "data e orario. Per visite urgenti (zoppia improvvisa, "
             "inappetenza, vomito ricorrente) chiamare direttamente "
             "in segreteria."),
            ("03", "Prima visita di 60 minuti",
             "Anamnesi, esame obiettivo completo, diagnostica di "
             "base se indicata, piano di cura scritto. Il preventivo "
             "è consegnato anche in PDF."),
        ],
        "form_title": "Modulo di prenotazione",
        "form_band_side_note":
            "Visita preventiva — 40 minuti — € 65 (cane/gatto), "
            "€ 75 (esotici).",
        "form_band_side_note_small":
            "I costi sono dichiarati per le voci di routine. Per "
            "piani strutturati il preventivo viene scritto dopo "
            "la prima visita.",
        "form_fields": [
            {
                "name":    "owner_name",
                "label":   "Nome del proprietario",
                "type":    "text",
                "required": True,
                "placeholder": "Nome e cognome del proprietario",
            },
            {
                "name":    "email",
                "label":   "Email",
                "type":    "email",
                "required": True,
                "placeholder": "Per la conferma dell'appuntamento",
            },
            {
                "name":    "phone",
                "label":   "Telefono",
                "type":    "tel",
                "required": True,
                "placeholder": "Per eventuali contatti veloci",
            },
            {
                "name":    "pet_name",
                "label":   "Nome dell'animale",
                "type":    "text",
                "required": True,
                "placeholder": "Es. Luna · Briciola · Pepe",
            },
            {
                "name":    "pet_species",
                "label":   "Specie e razza",
                "type":    "text",
                "required": True,
                "placeholder": "Es. Gatto · Coniglio nano · Cane Border Collie",
            },
            {
                "name":    "pet_age",
                "label":   "Età dell'animale",
                "type":    "text",
                "required": True,
                "placeholder": "Es. 8 anni · 6 mesi",
            },
            {
                "name":    "visit_reason",
                "label":   "Motivo della visita",
                "type":    "textarea",
                "required": True,
                "placeholder":
                    "Es. Visita preventiva annuale · controllo "
                    "post-operatorio · dubbi su alimentazione. "
                    "Per emergenze chiamare la reperibilità.",
            },
        ],
        "submit_label": "Invia la richiesta",
        "consent":
            "Accetto il trattamento dei dati personali e sanitari "
            "del mio animale ai sensi del GDPR. La cartella "
            "clinica sarà condivisa fra i tre veterinari associati "
            "dello studio.",
        "footnote":
            "Per emergenze cliniche fuori dagli orari di apertura "
            "(zoppia improvvisa, vomito ricorrente, prostrazione, "
            "trauma), chiamare il numero di reperibilità 24/7: "
            "+39 333 410 7726. Per pazienti non ancora in cartella "
            "indirizziamo all'Ospedale Veterinario di Legnaro o "
            "alla Clinica San Marco di Veggiano.",
    },
}
