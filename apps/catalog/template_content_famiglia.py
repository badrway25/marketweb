"""Famiglia — Pediatria Famiglia Plus (family archetype · Torino Crocetta)
— IT content tree.

Phase medical second wave (Session 52, 2026-04-15).

Voice contract (IT) — warm-family-protective
--------------------------------------------
- Parent-facing, never clinical-institutional. Uses "voi/i vostri bambini"
  as the default register. Reassuring, unhurried, attentive.
- Concrete language of growth and listening: "crescita", "ascolto",
  "tempi lunghi", "trent minuti", "bilancio", "casa più che reparto".
- Voice markers: "I bambini non vanno curati come piccoli adulti. Vanno
  ascoltati come persone in crescita.", "Lo studio come una casa, non
  come un reparto.", "Da noi una visita dura trenta minuti, non dieci."
- Phone-and-WhatsApp conversion pattern: big phone number + WhatsApp pill
  on every page. Never a 20-field booking form, never a calendar-spot,
  never online scheduling. The form on /contatti/ is a short message
  gateway, not an appointment request.

Differentiation contract vs the other 4 medical templates (D-054)
-----------------------------------------------------------------
- Famiglia = warm peach paper (#FDF7F1) + deep warm brown (#4A2E2A) + coral
  (#E97B5C), Quicksand rounded headings, Nunito body, pill-soft buttons.
- vs Cardio (cardiologia-marani-roma) — cream paper + Cormorant serif +
  gold accent + editorial prestigious. Famiglia is rounded-friendly,
  NEVER editorial serif.
- vs Dermatologia (dermatologia-elite-roma) — cream paper + Cormorant +
  specialist derm tone. Famiglia photography is family, NOT cosmetic
  before/after treatments.
- vs Salute (clinic archetype, parallel rollout) — teal booking-widget
  institutional. Famiglia has NO booking widget, NO teal, NO full-split.
- vs Benessere (wellness archetype, parallel rollout) — sage green serene
  olistico. Famiglia is coral-warm, NEVER sage, NEVER olistico vocabulary.

Differentiation vocabulary
--------------------------
Famiglia uses: studio, casa, crescita, ascolto, pediatra, bilancio,
adolescente, neonato, genitori, insieme, tempo, reperibilità.
Famiglia does NOT use: benessere olistico, prevenzione cardiovascolare,
estetica, terapia, booking online, slot disponibili.
"""
from __future__ import annotations

from typing import Any


FAMIGLIA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Home",      "kind": "home"},
        {"slug": "studio",   "label": "Lo studio", "kind": "about"},
        {"slug": "visite",   "label": "Visite",    "kind": "services"},
        {"slug": "crescita", "label": "Crescita",  "kind": "faq"},
        {"slug": "pediatre", "label": "Pediatre",  "kind": "team"},
        {"slug": "contatti", "label": "Contatti",  "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pediatria Famiglia Plus",
        "tag":          "Studio pediatrico · Torino Crocetta",
        "phone":        "011 549 21 88",
        "phone_tel":    "+390115492188",
        "whatsapp":     "+39 349 123 4567",
        "whatsapp_link": "https://wa.me/393491234567",
        "nav_cta_wa":   "WhatsApp",
        "email":        "studio@crocettapediatria.it",
        "address":      "Corso Galileo Ferraris 140 · 10129 Torino",
        "emergency_tel": "+393491234567",

        "hours_compact": "Lun – Ven · 8:30 – 12:30 · 15:00 – 19:00",
        "hours_footer_rows": [
            "Sabato · 9:00 – 12:00 · solo urgenze",
            "Domenica · reperibilità telefonica",
        ],
        "license":
            "P.IVA 11234120014 · Iscrizione OMCeO Torino 08/5412",
        "footer_intro":
            "Studio pediatrico privato nel quartiere Crocetta di Torino. "
            "Tre pediatre, una neonatologa e un'infermiera dedicata. "
            "Visite di trenta minuti, reperibilità telefonica nei festivi, "
            "ascolto vero dei bambini e dei loro genitori.",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":       "Studio pediatrico · Torino Crocetta",
        "headline":      "Cresciamo <em>insieme</em> ai vostri bambini.",
        "subhead":
            "Quattro pediatre, una psicomotricista e un'infermiera "
            "dedicata. Visite tranquille, tempi lunghi, ascolto vero — "
            "perché ogni famiglia merita un punto di riferimento, non un "
            "numero di sportello.",
        "primary_cta":   "Chiama lo studio",
        "secondary_cta": "Scrivi su WhatsApp",

        "hero_image":
            "https://images.pexels.com/photos/7447009/pexels-photo-7447009.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=1250&fit=crop",
        "hero_image_alt":
            "Pediatra durante il bilancio di salute con una bambina "
            "nello studio luminoso Crocetta",
        "hero_ribbon":   "Convenzionato SSN",
        "hero_stamp_initial": "E",
        "hero_stamp_name":    "Dr.ssa Rambaldi",
        "hero_stamp_meta":    "oggi in studio · 8:30 – 13:00",

        "trust_items": [
            {"icon": "clock",  "label": "Visite da trenta minuti, mai dieci"},
            {"icon": "shield", "label": "Reperibilità h24 per i pazienti in carico"},
            {"icon": "people", "label": "Studio a misura di famiglia dal 1998"},
        ],

        # ── Intro trio · età pediatriche ──
        "age_groups": [
            {
                "icon":  "baby",
                "range": "0 – 2 anni",
                "title": "Neonato e primo anno",
                "blurb":
                    "Il percorso che parte dalla prima settimana di vita: "
                    "allattamento, sonno, bilanci di salute, rientro da "
                    "Sant'Anna o Mauriziano. La Dr.ssa Conti vi segue in "
                    "prima persona fino ai due anni compiuti.",
                "items": [
                    "Visita post-nascita entro sette giorni",
                    "Bilanci di salute al 1°, 3°, 6°, 9°, 12° mese",
                    "Supporto allattamento e sonno",
                ],
            },
            {
                "icon":  "child",
                "range": "3 – 10 anni",
                "title": "Infanzia ed età scolare",
                "blurb":
                    "Gli anni della scuola materna e primaria: "
                    "vaccinazioni, certificati sportivi, "
                    "valutazione della crescita, piccoli imprevisti "
                    "e tutte le domande che un genitore normalmente "
                    "tiene per sé.",
                "items": [
                    "Bilanci di salute annuali",
                    "Calendario vaccinale completo",
                    "Certificati sportivi non agonistici",
                ],
            },
            {
                "icon":  "teen",
                "range": "11 – 18 anni",
                "title": "Adolescente",
                "blurb":
                    "La fase più delicata, quella in cui i ragazzi "
                    "vogliono parlare senza i genitori in stanza. "
                    "Visite dedicate, ascolto riservato, un canale "
                    "WhatsApp per le domande che non si fanno a voce.",
                "items": [
                    "Visita annuale in autonomia",
                    "Endocrinologia, crescita, pubertà",
                    "Canale riservato per l'adolescente",
                ],
            },
        ],

        # ── Le pediatre · portrait stack ──
        "team_label":   "Le pediatre dello studio",
        "team_heading": "Quattro firme, <em>una sola cartella di famiglia.</em>",
        "team_intro":
            "Lo studio è composto da quattro pediatre che condividono "
            "cartelle, protocolli e standard di visita. Ogni bambino, "
            "però, ha sempre una pediatra di riferimento — la stessa "
            "persona dai primi bilanci all'adolescenza.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Pediatra di famiglia",
                "spec":  "Nutrizione infantile",
                "wa_label": "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Pediatra allergologa",
                "spec":  "Asma e dermatiti",
                "wa_label": "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Pediatra endocrinologa",
                "spec":  "Crescita e pubertà",
                "wa_label": "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Pediatra neonatologa",
                "spec":  "Sonno e allattamento",
                "wa_label": "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
        ],

        "team_note":
            "Il team clinico è completato da Luisa Ferraro, infermiera "
            "pediatrica con quindici anni di esperienza al Regina "
            "Margherita, e da Giada Porro, psicomotricista specializzata "
            "nei disturbi dello sviluppo 0-6 anni.",

        # ── Percorso della crescita · milestone timeline ──
        "journey_label":   "Percorso della crescita",
        "journey_heading": "Dalle prime settimane al <em>diploma</em>.",
        "journey_intro":
            "Un bambino incontra la stessa pediatra almeno dodici volte "
            "prima dei diciotto anni. Ogni incontro è un bilancio, "
            "non una visita di emergenza. Ecco le cinque tappe che "
            "segnano di più il percorso.",

        "journey_steps": [
            {
                "age":   "1 mese",
                "title": "Primo bilancio",
                "desc":  "La pediatra incontra il neonato in studio entro "
                         "i quaranta giorni: peso, riflessi, allattamento, "
                         "sonno e prime rassicurazioni ai genitori.",
            },
            {
                "age":   "6 mesi",
                "title": "Svezzamento",
                "desc":  "Consigli pratici sull'introduzione dei primi "
                         "cibi solidi, valutazione della crescita "
                         "auxologica e prima parte del calendario "
                         "vaccinale.",
            },
            {
                "age":   "1 anno",
                "title": "Primo compleanno",
                "desc":  "Bilancio completo di fine primo anno, "
                         "motricità, linguaggio, prime interazioni "
                         "sociali. Si consolidano le abitudini della "
                         "famiglia.",
            },
            {
                "age":   "3 anni",
                "title": "Ingresso a scuola",
                "desc":  "Il passaggio alla scuola materna: certificato, "
                         "controlli visivi e uditivi, valutazione "
                         "delle autonomie e dei ritmi di sonno.",
            },
            {
                "age":   "6 anni",
                "title": "Età scolare",
                "desc":  "Bilancio prima della scuola primaria, postura, "
                         "alimentazione, primi controlli della vista e "
                         "consigli sull'attività fisica.",
            },
        ],

        # ── FAQ accordion genitori ──
        "faq_label":   "Domande dei genitori",
        "faq_heading": "Le domande che ci <em>arrivano</em> più spesso.",
        "faq_intro":
            "Abbiamo raccolto le otto domande più frequenti che i "
            "genitori ci fanno al telefono o in sala d'attesa. "
            "Se la vostra non è qui, ci trovate al numero dello studio "
            "o su WhatsApp.",

        "faq": [
            (
                "Quando devo chiamare la pediatra?",
                "Subito in caso di febbre sopra i 38,5 °C nel primo "
                "trimestre di vita, pianto inconsolabile, rifiuto "
                "totale del cibo o del latte per più di 12 ore, "
                "diarrea con sangue, lesioni cutanee diffuse. "
                "Per tutto il resto — una febbre moderata, una "
                "tosse notturna, un eritema solare — si può "
                "aspettare l'orario mattutino e chiamare in "
                "serenità. Lo studio risponde personalmente.",
            ),
            (
                "Come faccio a prenotare una prima visita?",
                "Basta chiamare lo 011 549 21 88 dal lunedì al "
                "venerdì: la segreteria, gestita da Silvia Pairetto, "
                "raccoglie il nome del bambino, l'età e il motivo "
                "della visita. In alternativa si può scrivere su "
                "WhatsApp al numero dedicato, anche fuori orario. "
                "Non esiste un calendario online: preferiamo "
                "parlare prima.",
            ),
            (
                "Cosa devo portare alla prima visita?",
                "Il libretto sanitario del bambino, l'eventuale "
                "lettera di dimissione dall'ospedale, le vaccinazioni "
                "già eseguite, e — se il bambino ha più di un anno — "
                "il diario dello svezzamento. Non servono esami "
                "recenti: la pediatra chiede solo ciò di cui ha "
                "realmente bisogno.",
            ),
            (
                "Lo studio è accessibile con il passeggino?",
                "Sì, l'ingresso è al piano terra rialzato di "
                "Corso Galileo Ferraris 140 con due gradini e una "
                "rampa laterale. All'interno c'è un angolo "
                "passeggini nella sala d'attesa e il bagno è "
                "attrezzato con fasciatoio. Tutte le stanze di "
                "visita sono al piano terra.",
            ),
            (
                "Cosa succede la sera o il fine settimana?",
                "La Dr.ssa Rambaldi e la Dr.ssa Greco si alternano "
                "nella reperibilità telefonica per i pazienti in "
                "carico: serate infrasettimanali, notte, sabato "
                "pomeriggio e domenica. Il numero dedicato viene "
                "comunicato dopo la prima visita. Per le emergenze "
                "vere resta sempre il 118 o il Regina Margherita.",
            ),
            (
                "Quali vaccini sono obbligatori?",
                "Il decreto Lorenzin del 2017 prevede dieci "
                "vaccinazioni obbligatorie per l'iscrizione alla "
                "scuola dell'obbligo. Lo studio segue il calendario "
                "nazionale della Regione Piemonte e offre un "
                "percorso vaccinale riservato, senza code ASL, con "
                "possibilità di scaglionare le dosi su richiesta "
                "dei genitori.",
            ),
            (
                "Quanto dura una visita di controllo?",
                "Una visita di bilancio allo studio dura sempre "
                "trenta minuti, anche se il bambino sta benissimo. "
                "È il tempo minimo per fare l'esame obiettivo, "
                "pesare e misurare con calma, aggiornare il libretto "
                "e rispondere alle domande dei genitori senza che "
                "nessuno si senta di fretta.",
            ),
            (
                "Quanto costa una visita pediatrica privata?",
                "La prima visita costa 90 euro, i bilanci successivi "
                "70 euro, le visite di controllo 60 euro. Le "
                "famiglie con due o più bambini iscritti hanno uno "
                "sconto del 15%. Tutti i pagamenti sono detraibili "
                "come spese sanitarie con ricevuta emessa in "
                "giornata.",
            ),
        ],

        # ── Studio child-friendly gallery ──
        "gallery_label":   "Lo studio",
        "gallery_heading": "Una casa, <em>non un reparto.</em>",
        "gallery_intro":
            "Abbiamo pensato ogni stanza perché il bambino non abbia "
            "paura di entrare. Dalla sala d'attesa con i libri al "
            "fasciatoio riscaldato, dai giochi al tavolino bassi alla "
            "stanza colorata delle visite.",
        "gallery": [
            {
                "src": "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                       "?auto=compress&cs=tinysrgb&w=1000&h=800&fit=crop",
                "cap": "Sala visite · piano terra",
            },
            {
                "src": "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Angolo stetoscopio giocoso",
            },
            {
                "src": "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Sala allattamento",
            },
            {
                "src": "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Sala bilanci neonato",
            },
            {
                "src": "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Ingresso · Corso Galileo Ferraris",
            },
        ],

        # ── Orari band ──
        "hours_heading": "Orari di apertura",
        "hours": [
            ("Lun – Ven",  "8:30 – 12:30  ·  15:00 – 19:00"),
            ("Sabato",     "9:00 – 12:00  ·  solo urgenze"),
            ("Domenica",   "Reperibilità telefonica"),
            ("Festivi",    "Linea dedicata pazienti in carico"),
        ],
        "urgency_label": "Urgenze notturne",
        "urgency_title": "Siamo vicini anche fuori orario.",
        "urgency_text":
            "I pazienti in carico hanno un numero dedicato di "
            "reperibilità notturna e festiva, aperto tutti i giorni "
            "dalle 19:30 alle 8:00. Per le emergenze resta il 118 "
            "o il Regina Margherita.",
        "urgency_phone": "+39 349 123 4567",

        # ── Bottom CTA band ──
        "cta_heading":     "Hai bisogno di <em>noi</em>?",
        "cta_lead":
            "Chiamare lo studio è il modo più semplice e più umano "
            "per iniziare. Rispondiamo personalmente, senza menù "
            "telefonici e senza tempi d'attesa. Se preferite, siamo "
            "anche su WhatsApp.",
        "cta_phone_label": "Telefono studio",
        "cta_or":          "oppure",
        "cta_wa_label":    "Scrivici su WhatsApp",
    },

    # ─── LO STUDIO (about) ───────────────────────────────────────
    "studio": {
        "eyebrow":  "Lo studio",
        "headline": "Dal 1998, <em>una casa</em> per le famiglie di Crocetta.",
        "intro":
            "Nasciamo come studio pediatrico di quartiere nel 1998, "
            "per iniziativa della Dr.ssa Rambaldi. In ventisette anni "
            "abbiamo seguito oltre tremila bambini — molti dei quali "
            "oggi sono diventati genitori che ci riportano i loro "
            "figli. È il complimento più bello che potessimo ricevere.",

        "values": [
            {
                "icon":  "clock",
                "title": "Tempi lunghi",
                "desc":  "Trenta minuti per ogni visita, mai meno. "
                         "Il tempo è l'unico strumento che davvero "
                         "fa la differenza fra una diagnosi giusta e "
                         "una sbagliata.",
            },
            {
                "icon":  "ear",
                "title": "Ascolto vero",
                "desc":  "Ascoltiamo prima i genitori, poi i bambini, "
                         "poi i ragazzi. Ognuno con il proprio spazio "
                         "e con la propria voce.",
            },
            {
                "icon":  "home",
                "title": "Ambiente di casa",
                "desc":  "Stanze colorate ma non infantili, luce "
                         "naturale, odori rassicuranti. Uno studio "
                         "deve essere una casa, non un reparto.",
            },
            {
                "icon":  "people",
                "title": "Continuità",
                "desc":  "Ogni bambino ha la sua pediatra di "
                         "riferimento, la stessa dai primi bilanci "
                         "alla diciottesima candelina. Le cartelle "
                         "si condividono, non le persone.",
            },
        ],

        "studio_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600&h=700&fit=crop",
        "studio_image_caption":
            "Ambulatorio pediatrico · Corso Galileo Ferraris 140, Torino",

        "history_label":   "Ventisette anni di studio",
        "history_heading": "Quattro tappe, <em>tre generazioni</em> di bambini.",
        "history_intro":
            "Lo studio ha cambiato tre indirizzi nella stessa via, "
            "ha allargato il team da una a cinque professioniste e ha "
            "attraversato tre riforme del sistema sanitario. Una cosa "
            "non è mai cambiata: la visita dura trenta minuti.",

        "history": [
            (
                "1998",
                "La Dr.ssa Elisa Rambaldi apre il primo studio "
                "pediatrico in Via Morgari, due stanze e una "
                "segretaria. Le prime quindici famiglie sono ancora "
                "tutte in cartella.",
            ),
            (
                "2008",
                "Trasferimento in Corso Galileo Ferraris 140, "
                "piano terra con accesso passeggino. Entra la "
                "Dr.ssa Marta Greco come pediatra allergologa e "
                "Silvia Pairetto come segretaria clinica.",
            ),
            (
                "2016",
                "Ampliamento del team con la Dr.ssa Lucia Sferra "
                "(endocrinologia pediatrica) e avvio della "
                "psicomotricità per i disturbi dello sviluppo con "
                "Giada Porro.",
            ),
            (
                "2026",
                "Lo studio raggiunge le cinque professioniste con "
                "l'ingresso della Dr.ssa Beatrice Conti (neonatologia) "
                "e inaugura il canale WhatsApp dedicato all'adolescenza.",
            ),
        ],

        "cta_heading":
            "Volete conoscere le pediatre <em>prima</em> di prenotare?",
        "cta_lead":
            "Potete leggere i loro percorsi, guardare i loro volti e "
            "scegliere chi preferite per la prima visita. Se siete "
            "indecisi, chiamateci: vi aiutiamo noi a trovare la "
            "persona giusta per il vostro bambino.",
        "cta_primary_label":   "Chiama lo studio",
        "cta_secondary_label": "Le quattro pediatre",
    },

    # ─── VISITE (services) ───────────────────────────────────────
    "visite": {
        "eyebrow":  "Le visite",
        "headline": "Otto tipi di visita, <em>un solo modo</em> di fare pediatria.",
        "intro":
            "Ogni visita allo studio è un percorso con un tempo, un "
            "motivo e un costo chiari. Chiamate lo studio per "
            "prenotare: insieme scegliamo la visita giusta per "
            "l'età e il motivo del bambino.",

        "visits": [
            {
                "icon":     "baby",
                "title":    "Bilancio del neonato",
                "duration": "45 min · 0 – 12 mesi",
                "desc":
                    "La prima valutazione completa dopo la nascita: "
                    "peso, lunghezza, riflessi arcaici, controllo "
                    "delle anche, supporto all'allattamento e al "
                    "sonno. Si ripete al 1°, 3°, 6°, 9° e 12° mese.",
                "bring_label": "Cosa portare",
                "bring":    "Libretto sanitario, lettera di dimissione "
                            "dall'ospedale, eventuali esami neonatali.",
                "cta_label": "Prenota al telefono",
            },
            {
                "icon":     "child",
                "title":    "Bilancio dell'infanzia",
                "duration": "30 min · 1 – 10 anni",
                "desc":
                    "Controllo annuale della crescita, valutazione "
                    "delle autonomie, postura, alimentazione e "
                    "sviluppo psico-motorio. È il bilancio più "
                    "richiesto dello studio.",
                "bring_label": "Cosa portare",
                "bring":    "Libretto sanitario aggiornato, diario "
                            "alimentare di una settimana se possibile.",
                "cta_label": "Prenota al telefono",
            },
            {
                "icon":     "vaccine",
                "title":    "Vaccinazioni",
                "duration": "20 min · tutte le età",
                "desc":
                    "Calendario vaccinale della Regione Piemonte "
                    "eseguito in studio senza code ASL. È possibile "
                    "scaglionare le dosi e concordare un percorso "
                    "personalizzato in caso di esitazione vaccinale.",
                "bring_label": "Cosa portare",
                "bring":    "Libretto vaccinale, documento di "
                            "identità del genitore accompagnatore.",
                "cta_label": "Prenota al telefono",
            },
            {
                "icon":     "sport",
                "title":    "Visita sportiva",
                "duration": "30 min · 6 – 18 anni",
                "desc":
                    "Certificato medico non agonistico per la scuola "
                    "e le attività sportive amatoriali. Comprende "
                    "esame obiettivo, misurazione pressoria ed ECG "
                    "a riposo quando indicato.",
                "bring_label": "Cosa portare",
                "bring":    "Modulo della società sportiva e "
                            "libretto sanitario.",
                "cta_label": "Prenota al telefono",
            },
            {
                "icon":     "moon",
                "title":    "Consulenza sonno",
                "duration": "45 min · 0 – 4 anni",
                "desc":
                    "Per genitori esausti e bambini che non dormono. "
                    "Analisi del contesto familiare, piano di "
                    "normalizzazione del ritmo sonno-veglia e "
                    "follow-up telefonico settimanale per un mese.",
                "bring_label": "Cosa portare",
                "bring":    "Diario del sonno del bambino "
                            "compilato per sette giorni.",
                "cta_label": "Prenota al telefono",
            },
            {
                "icon":     "leaf",
                "title":    "Visita allergologica",
                "duration": "45 min · 2 – 18 anni",
                "desc":
                    "Valutazione allergologica pediatrica: storia "
                    "clinica dettagliata, Prick test, indicazioni "
                    "su asma, dermatite atopica e allergie "
                    "alimentari. Segue la Dr.ssa Greco.",
                "bring_label": "Cosa portare",
                "bring":    "Eventuali esami ematici recenti e "
                            "diario dei sintomi.",
                "cta_label": "Prenota al telefono",
            },
            {
                "icon":     "skin",
                "title":    "Dermatologia pediatrica",
                "duration": "30 min · tutte le età",
                "desc":
                    "Per dermatiti, eritemi, piccole lesioni "
                    "cutanee e nei in crescita. Segue la Dr.ssa Greco "
                    "con il supporto fotografico per il confronto "
                    "nel tempo.",
                "bring_label": "Cosa portare",
                "bring":    "Foto cronologiche della lesione se "
                            "disponibili, elenco dei prodotti usati.",
                "cta_label": "Prenota al telefono",
            },
            {
                "icon":     "apple",
                "title":    "Consulenza nutrizione",
                "duration": "45 min · 6 mesi – 18 anni",
                "desc":
                    "Per svezzamento difficile, selettività "
                    "alimentare, sovrappeso, sottopeso o semplice "
                    "insicurezza dei genitori. Segue la Dr.ssa "
                    "Rambaldi con piano scritto personalizzato.",
                "bring_label": "Cosa portare",
                "bring":    "Diario alimentare di sette giorni, "
                            "curve di crescita del libretto.",
                "cta_label": "Prenota al telefono",
            },
        ],

        "tips_label":   "Tre consigli ai genitori",
        "tips_heading": "Cose che vorremmo <em>sapeste</em> prima di chiamarci.",
        "tips_intro":
            "Alcune raccomandazioni valgono più di una visita. "
            "Le abbiamo messe qui perché siamo convinte che un "
            "genitore informato è un genitore più sereno — e un "
            "bambino più sereno.",

        "tips": [
            {
                "title": "La febbre non è il nemico",
                "text":
                    "La febbre è un meccanismo di difesa, non un "
                    "problema da abbattere subito. Preoccupatevi "
                    "dei comportamenti del bambino — se mangia, "
                    "se beve, se gioca — più del numero sul "
                    "termometro.",
            },
            {
                "title": "Cinque minuti bastano",
                "text":
                    "Ogni sera, prima di dormire, chiedete al "
                    "vostro bambino com'è andata la giornata. Non "
                    "a cena, non mentre cucinate. In camera, "
                    "con lui o lei. Cinque minuti cambiano tutto.",
            },
            {
                "title": "Chiamate senza paura",
                "text":
                    "Non esiste una domanda stupida in pediatria. "
                    "Lo studio risponde al telefono dal lunedì al "
                    "venerdì: chiamare prima di preoccuparsi è "
                    "sempre la cosa giusta da fare.",
            },
        ],

        "cta_heading":
            "Per prenotare una visita, il modo più semplice resta <em>chiamare</em>.",
        "cta_primary_label":   "Chiama lo studio",
        "cta_secondary_label": "Scrivi su WhatsApp",
    },

    # ─── CRESCITA (faq) ──────────────────────────────────────────
    "crescita": {
        "eyebrow":  "Crescita & rassicurazioni",
        "headline": "Le domande che <em>accompagnano</em> i primi diciotto anni.",
        "intro":
            "Abbiamo raccolto qui le domande che più spesso ci "
            "arrivano dai genitori, raggruppate per area tematica. "
            "È una guida di prima lettura: per tutto il resto, "
            "parlatene con la vostra pediatra di riferimento.",

        "topics": [
            {
                "icon":  "apple",
                "meta":  "Area 01",
                "title": "Nutrizione e alimentazione",
                "intro":
                    "Dalla montata lattea all'adolescenza, "
                    "l'alimentazione è il terreno dove genitori e "
                    "pediatre dialogano di più. Quattro domande che "
                    "raccogliamo ogni settimana.",
                "items": [
                    (
                        "A che età comincio lo svezzamento?",
                        "Le linee guida attuali indicano il sesto "
                        "mese compiuto come momento ottimale per "
                        "iniziare, quando il bambino sta seduto da "
                        "solo, ha perso il riflesso di estrusione "
                        "e mostra interesse per il cibo degli "
                        "adulti. Non c'è un giorno magico: si "
                        "inizia quando il bambino è pronto, non "
                        "quando il calendario dice così.",
                    ),
                    (
                        "Mio figlio è troppo magro?",
                        "Il peso da solo non dice nulla. Vanno "
                        "sempre letti insieme tre valori: peso, "
                        "altezza e indice di massa corporea "
                        "rapportati alla curva di crescita "
                        "personale del bambino. Un bambino che "
                        "cresce regolarmente lungo il suo "
                        "percentile — anche se è il decimo — sta "
                        "benissimo.",
                    ),
                    (
                        "Come gestisco un bambino selettivo?",
                        "La selettività alimentare tra i 2 e i 5 "
                        "anni è fisiologica. Niente lotte a tavola, "
                        "niente ricatti e niente piatti speciali: "
                        "si propone, si ripropone, si aspetta. "
                        "Se dopo i sei anni la selettività "
                        "persiste su gruppi interi di alimenti, "
                        "chiamate lo studio.",
                    ),
                    (
                        "Gli integratori servono davvero?",
                        "Nella stragrande maggioranza dei casi, no. "
                        "Un bambino che mangia varia non ha "
                        "bisogno di integratori, eccetto la "
                        "vitamina D nei primi anni e la vitamina K "
                        "nel neonato. Tutto il resto è marketing, "
                        "non pediatria.",
                    ),
                ],
            },
            {
                "icon":  "moon",
                "meta":  "Area 02",
                "title": "Sonno e riposo",
                "intro":
                    "Il sonno è il tema che sfinisce di più i "
                    "genitori nei primi tre anni. Quattro "
                    "rassicurazioni basate sulla pratica clinica, "
                    "non sui libri.",
                "items": [
                    (
                        "Quante ore deve dormire un bambino?",
                        "Da 0 a 3 mesi: 14–17 ore al giorno, "
                        "distribuite. Da 4 a 11 mesi: 12–15 ore. "
                        "Da 1 a 2 anni: 11–14 ore. Da 3 a 5 anni: "
                        "10–13 ore. Ogni bambino ha comunque il "
                        "suo ritmo: variazioni di due ore sono "
                        "normali.",
                    ),
                    (
                        "È normale che si svegli ogni due ore?",
                        "Nei primi sei mesi sì, è fisiologico: "
                        "lo stomaco del lattante è piccolo e il "
                        "ciclo circadiano non è ancora maturo. "
                        "Dopo i sei mesi, se i risvegli restano "
                        "frequenti, possiamo costruire insieme "
                        "un piano di normalizzazione.",
                    ),
                    (
                        "Posso addormentarlo accanto a me?",
                        "Il co-sleeping nella stessa stanza "
                        "(ma non nello stesso letto) è "
                        "raccomandato fino ai 12 mesi. Dopo, "
                        "dipende dalle abitudini della famiglia: "
                        "nessun approccio è sbagliato se "
                        "funziona per genitori e bambino.",
                    ),
                    (
                        "Quando posso togliere il pannolino di notte?",
                        "Il controllo notturno sfintere arriva "
                        "mediamente fra i 3 e i 5 anni. Non è "
                        "una gara: alcuni bambini sono pronti a "
                        "2 anni e mezzo, altri a 6. Se a 7 anni "
                        "ci sono ancora enuresi frequenti, "
                        "parliamone.",
                    ),
                ],
            },
            {
                "icon":  "vaccine",
                "meta":  "Area 03",
                "title": "Vaccinazioni e malattie comuni",
                "intro":
                    "Il mondo delle vaccinazioni è cambiato nel "
                    "2017 con il decreto Lorenzin. Qui rispondiamo "
                    "alle quattro domande più frequenti — con "
                    "pazienza e con i dati.",
                "items": [
                    (
                        "Quali vaccinazioni sono obbligatorie?",
                        "Sono dieci: difterite, tetano, pertosse, "
                        "epatite B, poliomielite, HiB, morbillo, "
                        "rosolia, parotite e varicella. "
                        "L'obbligo vale per l'iscrizione alla "
                        "scuola dell'obbligo (0-16 anni) ed è "
                        "regolato dal decreto Lorenzin del 2017.",
                    ),
                    (
                        "Posso scaglionare le dosi?",
                        "Sì, lo studio offre percorsi "
                        "personalizzati per chi preferisce "
                        "distribuire le vaccinazioni su più "
                        "appuntamenti invece che somministrare "
                        "tre vaccini in un'unica sessione. Ne "
                        "parliamo insieme al primo bilancio.",
                    ),
                    (
                        "Come gestisco la sesta malattia?",
                        "La sesta malattia (roseola infantum) "
                        "colpisce i bambini tra i 6 mesi e i 2 "
                        "anni: tre giorni di febbre alta "
                        "improvvisa seguiti da un'eruzione "
                        "cutanea rosa. Si gestisce con "
                        "antipiretici e pazienza. Chiamateci "
                        "solo se la febbre supera i 40 °C o "
                        "dura più di quattro giorni.",
                    ),
                    (
                        "Devo preoccuparmi per la tosse?",
                        "Una tosse fino a tre settimane dopo un "
                        "raffreddore è normale: le vie aeree del "
                        "bambino sono più reattive. Chiamateci "
                        "se la tosse è accompagnata da febbre "
                        "che non scende in cinque giorni, "
                        "respiro sibilante o rientramenti "
                        "intercostali visibili.",
                    ),
                ],
            },
            {
                "icon":  "comp",
                "meta":  "Area 04",
                "title": "Comportamento e sviluppo",
                "intro":
                    "Le domande meno mediche sono spesso le più "
                    "importanti. Qui rispondiamo su sviluppo "
                    "psicomotorio, capricci, adolescenza.",
                "items": [
                    (
                        "A quale età parla un bambino?",
                        "Le prime parole arrivano tra i 10 e i "
                        "18 mesi, le prime frasi tra i 18 e i 24 "
                        "mesi. Se a 24 mesi un bambino non "
                        "combina due parole, è ragionevole "
                        "richiedere una valutazione "
                        "psicomotoria — che in studio svolgiamo "
                        "con Giada Porro.",
                    ),
                    (
                        "I capricci sono normali?",
                        "Sì, sono fisiologici e cruciali: "
                        "sono il modo con cui il bambino "
                        "sperimenta l'autonomia e i limiti. "
                        "Non si puniscono, si contengono. "
                        "Diventano un problema quando "
                        "coinvolgono aggressività fisica "
                        "regolare o autolesionismo.",
                    ),
                    (
                        "Quanto tempo davanti allo schermo?",
                        "Le linee guida OMS indicano zero "
                        "schermo fino ai 2 anni, massimo 1 ora "
                        "al giorno fra i 2 e i 5 anni, massimo "
                        "2 ore dopo i 5 anni. Televisione, "
                        "tablet e smartphone sono tutti "
                        "schermi: contate anche il cartone al "
                        "mattino.",
                    ),
                    (
                        "Come parlo a mio figlio adolescente?",
                        "Meno di quanto vorreste, e con più "
                        "ascolto di quanto crediate. Le "
                        "domande aperte funzionano sempre "
                        "meglio delle domande chiuse: 'Com'è "
                        "stata la giornata?' battendo '"
                        "Hai studiato?' dieci a zero. E "
                        "ricordate: il silenzio non è rifiuto, "
                        "è pensiero.",
                    ),
                ],
            },
        ],

        "materials_label":   "Materiali utili",
        "materials_heading": "Tre guide <em>scaricabili</em>.",
        "materials_intro":
            "Abbiamo preparato tre vademecum in PDF che i genitori "
            "possono scaricare e consultare a casa. Sono scritti "
            "dalle pediatre dello studio, aggiornati al 2026.",

        "materials": [
            {
                "title":    "Vademecum neonato",
                "desc":
                    "Ventotto pagine sui primi tre mesi di vita: "
                    "allattamento, sonno, bagnetto, vaccinazioni "
                    "iniziali, quando chiamare lo studio.",
                "size":     "PDF · 2,4 MB",
                "dl_label": "Scarica",
            },
            {
                "title":    "Calendario vaccinale 2026",
                "desc":
                    "Il calendario vaccinale aggiornato della "
                    "Regione Piemonte in versione riassuntiva, "
                    "con date consigliate e opzionali.",
                "size":     "PDF · 1,1 MB",
                "dl_label": "Scarica",
            },
            {
                "title":    "Guida allo svezzamento",
                "desc":
                    "Dal sesto mese al primo anno: quali cibi "
                    "introdurre, in che ordine, con quali "
                    "accortezze. Con ricette della Dr.ssa "
                    "Rambaldi.",
                "size":     "PDF · 3,1 MB",
                "dl_label": "Scarica",
            },
        ],

        "cta_heading":
            "Non avete trovato la <em>vostra</em> domanda?",
        "cta_lead":
            "Chiamateci o scriveteci su WhatsApp: rispondiamo "
            "personalmente in giornata. Non ci sono domande "
            "stupide, in pediatria.",
        "cta_primary_label":   "Chiama lo studio",
        "cta_secondary_label": "Scrivi su WhatsApp",
    },

    # ─── PEDIATRE (team) ─────────────────────────────────────────
    "pediatre": {
        "eyebrow":  "Le pediatre",
        "headline": "Quattro firme, <em>una sola cartella</em> di famiglia.",
        "intro":
            "Siamo quattro pediatre con formazioni diverse e un "
            "solo modo di lavorare: trenta minuti per ogni visita, "
            "cartelle condivise fra colleghe, continuità di "
            "relazione con ogni bambino dalla nascita ai diciotto "
            "anni.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Fondatrice · Pediatra di famiglia",
                "tag":   "Fondatrice",
                "specs": ["Nutrizione infantile", "Svezzamento", "Età scolare"],
                "bio":
                    "Laurea in Medicina e Chirurgia all'Università di "
                    "Torino, specializzazione in Pediatria al Regina "
                    "Margherita. Apre lo studio nel 1998 con "
                    "l'obiettivo di restituire alla pediatria "
                    "territoriale la sua dimensione di tempo lungo. "
                    "Autrice del volume «Crescere insieme», "
                    "Einaudi Ragazzi 2019.",
                "exp_label": "Esperienza",
                "exp_value": "28 anni · oltre 3.000 cartelle in attivo",
                "wa_label":  "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Pediatra · Allergologia e dermatologia",
                "tag":   "Allergologia",
                "specs": ["Asma pediatrica", "Dermatite atopica", "Allergie alimentari"],
                "bio":
                    "Laurea e specializzazione in Pediatria "
                    "all'Università di Pavia, master in Allergologia "
                    "Pediatrica al San Raffaele di Milano. Dal 2008 "
                    "nello studio Crocetta, dove segue il percorso "
                    "allergologico e dermatologico pediatrico. "
                    "Referente per l'Istituto Giannina Gaslini di "
                    "Genova per le consulenze territoriali.",
                "exp_label": "Esperienza",
                "exp_value": "22 anni · allergologia pediatrica dal 2006",
                "wa_label":  "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Pediatra · Endocrinologia",
                "tag":   "Endocrinologia",
                "specs": ["Crescita", "Pubertà precoce", "Tiroide pediatrica"],
                "bio":
                    "Laurea all'Università Federico II di Napoli, "
                    "specializzazione in Pediatria all'Università di "
                    "Bologna, fellowship in Endocrinologia "
                    "Pediatrica al Children's Hospital di Boston. "
                    "Dal 2016 nello studio, dove si occupa di "
                    "crescita, pubertà e disturbi endocrinologici "
                    "nelle fasce d'età 8-18 anni.",
                "exp_label": "Esperienza",
                "exp_value": "18 anni · endocrinologia pediatrica",
                "wa_label":  "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Pediatra · Neonatologia",
                "tag":   "Neonatologia",
                "specs": ["Allattamento", "Sonno 0-3 anni", "Prematurità"],
                "bio":
                    "Laurea e specializzazione all'Università di "
                    "Torino, quindici anni al reparto di "
                    "Neonatologia del Sant'Anna, dove ha seguito "
                    "oltre duemila neonati prematuri e a termine. "
                    "Consulente IBCLC per l'allattamento. Entra "
                    "nello studio nel 2026 per occuparsi del "
                    "primo anno di vita e del supporto alle "
                    "neomamme.",
                "exp_label": "Esperienza",
                "exp_value": "15 anni · Sant'Anna · IBCLC dal 2014",
                "wa_label":  "Scrivi su WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
        ],

        "extra_title": "Il team clinico è completato da due professioniste.",
        "extra_text":
            "Luisa Ferraro, infermiera pediatrica con quindici anni "
            "di reparto al Regina Margherita, segue le vaccinazioni "
            "e i prelievi in studio. Giada Porro, psicomotricista "
            "specializzata nei disturbi dello sviluppo 0-6 anni, "
            "riceve il martedì e il giovedì su appuntamento.",
    },

    # ─── CONTATTI (contact) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contatti & accesso",
        "headline": "Un <em>numero</em>, una persona, una risposta.",
        "intro":
            "Silvia Pairetto risponde personalmente al telefono dal "
            "lunedì al venerdì. Conosce ogni cartella, ogni nome e "
            "ogni mamma di questo studio. Per le richieste non "
            "urgenti c'è anche WhatsApp e il modulo qui sotto.",

        "address_label": "Dove siamo",
        "address_line":  "Corso Galileo Ferraris 140",
        "address_sub":   "10129 Torino · Quartiere Crocetta · piano terra rialzato",
        "phone_label":   "Telefono",
        "email_label":   "Email",

        "map_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=750&fit=crop",

        "travel_heading": "Come raggiungerci",
        "travel": [
            {
                "icon":  "metro",
                "title": "Metropolitana",
                "text":  "Linea 1 · fermata Re Umberto, 4 minuti a piedi verso Corso Galileo Ferraris.",
            },
            {
                "icon":  "car",
                "title": "Auto e parcheggio",
                "text":  "Parcheggio convenzionato Q-Park Crocetta in Via Governolo 22, 80 metri dallo studio.",
            },
            {
                "icon":  "walk",
                "title": "A piedi",
                "text":  "A cinque minuti dal Parco del Valentino e dalla Stazione Porta Nuova (15 minuti a piedi).",
            },
        ],

        "hours_heading": "Orari di apertura",
        "hours": [
            ("Lun – Ven",  "8:30 – 12:30 · 15:00 – 19:00"),
            ("Sabato",     "9:00 – 12:00 · solo urgenze"),
            ("Domenica",   "Reperibilità telefonica"),
            ("Festivi",    "Linea dedicata"),
        ],

        "form_title": "Scrivi allo studio",
        "form_intro":
            "Per informazioni non urgenti — costi, orari, documenti, "
            "prima visita — scriveteci qui. Rispondiamo entro la "
            "giornata lavorativa. Per le urgenze, telefonate.",

        "label_parent_name": "Nome del genitore",
        "label_child_age":   "Età del bambino",
        "label_reason":      "Motivo del contatto",

        "reason_options": [
            "Prima visita",
            "Controllo di routine",
            "Vaccinazioni",
            "Consulenza su un problema specifico",
            "Informazioni amministrative",
            "Altro",
        ],

        "form_placeholders": {
            "parent_name": "Giulia Bianchi",
            "email":       "giulia.bianchi@email.it",
            "phone":       "+39 333 …",
            "child_age":   "4 anni e mezzo",
            "message":
                "Scrivete qui la vostra richiesta. "
                "Rispondiamo in giornata lavorativa.",
        },
        "form_helpers": {
            "parent_name": "Indicate il nome del genitore che scrive.",
            "email":       "Rispondiamo qui entro la giornata.",
            "phone":       "Opzionale — utile se preferite essere richiamati.",
            "child_age":   "Età e, se volete, nome del bambino.",
            "reason":      "Se non siete sicuri, scegliete «Altro».",
            "message":
                "Qualche riga basta — per tutto il resto si parla "
                "meglio al telefono.",
        },
        "form_consent":
            "Acconsento al trattamento dei dati personali secondo "
            "l'informativa privacy ai sensi del Reg. UE 679/2016. "
            "I dati dei bambini sono custoditi dallo studio e non "
            "vengono comunicati a terzi.",
        "form_submit_note":
            "Risposta entro la giornata lavorativa · per le urgenze, "
            "chiamate direttamente lo studio.",
    },
}
