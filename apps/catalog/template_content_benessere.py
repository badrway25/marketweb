"""Italian content registry for the `benessere-centro-olistico` template.

Dedicated file (Session-41+ pattern) keeping template_content.py lean.
Voice: serene / sensory / ritual. Brand: Studio Armonia — centro olistico
a Bergamo Alta, Via Arena 15, 800m sul livello del mare.

The skin (templates/live_templates/medical/wellness/*.html) is fully
D-047 compliant: every user-facing string below is consumed through
`page_data.*`, `site.*` or `chrome.*` — no literal IT copy in the HTML.
"""
from __future__ import annotations

from typing import Any


# ---------------------------------------------------------------------------
# Shared imagery (mirrors preview_imagery.py `medical-wellness` pool, plus a
# small set of coherent Pexels additions for therapist portraits / rooms).
# All URLs are Pexels, already proven offline-safe in other templates.
# ---------------------------------------------------------------------------

_HERO_IMG = (
    "https://images.pexels.com/photos/6560308/pexels-photo-6560308.jpeg"
    "?auto=compress&cs=tinysrgb&w=1800&h=1200&fit=crop"
)
_AMBIENT_MASSAGE = (
    "https://images.pexels.com/photos/6560252/pexels-photo-6560252.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=1600&fit=crop"
)
_AMBIENT_TEA = (
    "https://images.pexels.com/photos/2752031/pexels-photo-2752031.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=1600&fit=crop"
)
_AMBIENT_CANDLES = (
    "https://images.pexels.com/photos/6186740/pexels-photo-6186740.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=1600&fit=crop"
)
_AMBIENT_RITUAL = (
    "https://images.pexels.com/photos/6766585/pexels-photo-6766585.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=1600&fit=crop"
)
_AMBIENT_YOGA = (
    "https://images.pexels.com/photos/8436719/pexels-photo-8436719.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=1600&fit=crop"
)
# Extended rooms (curated wellness/spa pool — verified offline-safe URLs)
_ROOM_HAMMAM = (
    "https://images.pexels.com/photos/3865712/pexels-photo-3865712.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=1000&fit=crop"
)
_ROOM_WATER = (
    "https://images.pexels.com/photos/3188/love-romantic-bath-candlelight.jpg"
    "?auto=compress&cs=tinysrgb&w=1400&h=1000&fit=crop"
)
_ROOM_TISANERIA = (
    "https://images.pexels.com/photos/1793035/pexels-photo-1793035.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=1000&fit=crop"
)
_ROOM_GARDEN = (
    "https://images.pexels.com/photos/4498360/pexels-photo-4498360.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=1000&fit=crop"
)
_ROOM_MEDITATION = (
    "https://images.pexels.com/photos/3822843/pexels-photo-3822843.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=1000&fit=crop"
)
_ROOM_RECEPTION = (
    "https://images.pexels.com/photos/6663573/pexels-photo-6663573.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=1000&fit=crop"
)

# Therapist portraits (calm, natural light, neutral backdrops)
_PORTRAIT_SARA = (
    "https://images.pexels.com/photos/5407206/pexels-photo-5407206.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_PORTRAIT_DAVIDE = (
    "https://images.pexels.com/photos/8436718/pexels-photo-8436718.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_PORTRAIT_YARA = (
    "https://images.pexels.com/photos/6551070/pexels-photo-6551070.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_PORTRAIT_ELENA = (
    "https://images.pexels.com/photos/3822622/pexels-photo-3822622.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_PORTRAIT_MIGUEL = (
    "https://images.pexels.com/photos/4498174/pexels-photo-4498174.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)

# Map / area (Bergamo Alta, non-satellite — editorial stone-wall wide shot)
_MAP_IMG = (
    "https://images.pexels.com/photos/11742489/pexels-photo-11742489.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop"
)


# ---------------------------------------------------------------------------
# BENESSERE_CONTENT_IT — complete 7-page tree, Italian primary voice.
# ---------------------------------------------------------------------------

BENESSERE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",           "label": "Casa",            "kind": "home"},
        {"slug": "filosofia",      "label": "Filosofia",       "kind": "about"},
        {"slug": "rituali",        "label": "Rituali",         "kind": "services"},
        {"slug": "ambienti",       "label": "Ambienti",        "kind": "gallery"},
        {"slug": "professionisti", "label": "Professionisti",  "kind": "team"},
        {"slug": "contatti",       "label": "Contatti",        "kind": "contact"},
        {"slug": "prenota",        "label": "Prenota",         "kind": "appointment"},
    ],

    # Site-wide chrome data (used by _base.html nav + footer)
    "site": {
        "logo_initial":  "A",
        "logo_word":     "Studio Armonia",
        "tag":           "Centro olistico · Bergamo Alta · 800 m s.l.m.",
        "nav_cta":       "Prenota un rituale",
        "phone":         "+39 035 412 998",
        "email":         "ritual@studioarmonia.it",
        "address":       "Via Arena 15 · 24129 Bergamo Alta",
        "hours_compact": "Lun – Sab · su prenotazione",
        "hours_footer_rows": [
            "Lun – Ven · 9:00 – 20:00",
            "Sabato · 9:00 – 18:00",
            "Domenica · giornata del silenzio",
        ],
        "license":       "Operatori certificati FIF e SIAF",
        "footer_intro":
            "Studio Armonia è un centro olistico indipendente nato nel 2011 "
            "fra le mura di Bergamo Alta. Rituali su misura, operatori "
            "certificati, tempi lenti — per chi cerca un respiro, non una "
            "prestazione.",
        "socials": [
            ("Instagram", "#"),
            ("Journal",   "#"),
            ("Telegram",  "#"),
        ],
    },

    # ───────────────────────── HOME ─────────────────────────
    "home": {
        "hero_image":  _HERO_IMG,
        "eyebrow":     "Centro olistico · Bergamo Alta",
        "headline":    'Un respiro è la misura del <em>nostro tempo</em>',
        "subhead":
            "Rituali su misura ispirati alle tradizioni mediterranee e "
            "orientali, in un rifugio di pietra fuori dal tempo a ottocento "
            "metri sul livello del mare.",
        "primary_cta":   "Riserva il tuo rituale",
        "secondary_cta": "Sfoglia i trattamenti",
        "hero_meta": [
            "Bergamo Alta",
            "Dal 2011",
            "Cinque operatori certificati",
            "Silenzio la domenica",
        ],

        # Manifesto — drop-cap "I" sull'incipit
        "manifesto_label": "Manifesto · Studio Armonia",
        "manifesto":
            "In Armonia non si viene per aggiungere — si viene per togliere. "
            "Togliere la fretta, la voce dentro che rimprovera, la postura "
            "stanca di chi porta tre pensieri contemporaneamente. I nostri "
            "rituali sono fatti di tempo lento, olii caldi, acque sorgive e "
            "silenzi scelti. Non siamo una spa d'albergo: siamo un laboratorio "
            "di presenza, aperto da quindici anni fra le mura alte di Bergamo.",
        "manifesto_signature": "— Chiara Bonomi, fondatrice",

        # Rituali pricelist home (4 rituali in evidenza)
        "rituali_label": "Rituali in evidenza",
        "rituali_heading": 'Quattro <em>misure di tempo</em> fra cui scegliere',
        "rituali_intro":
            "L'elenco completo di dieci rituali è nella pagina dedicata. Qui "
            "i più richiesti, per chi arriva per la prima volta.",
        "rituali": [
            ("Massaggio Mediterraneo",
             "55 minuti · olio d'oliva e agrumi di Sorrento",
             "€ 85"),
            ("Rituale Hammam",
             "90 minuti · vapore, sale grezzo, argilla rossa",
             "€ 120"),
            ("Riequilibrio Energetico",
             "60 minuti · pranoterapia e respiro guidato",
             "€ 95"),
            ("Ayurveda Abhyanga",
             "90 minuti · olii caldi, due operatrici",
             "€ 135"),
        ],

        # Benefits trio — 3 parole-chiave
        "benefits_label": "Cosa portiamo via",
        "benefits_heading": 'Tre <em>parole</em>, non tre promesse',
        "benefits_intro":
            "Non promettiamo trasformazioni radicali in novanta minuti. "
            "Promettiamo un rallentamento misurato e ripetibile.",
        "benefits": [
            ("Equilibrio",
             "Un sistema nervoso che si allenta, una postura che si ritrova, "
             "un ritmo respiratorio che smette di inseguire le scadenze."),
            ("Respiro",
             "La pratica respiratoria è il filo rosso di ogni rituale. "
             "Ne usciamo sapendo dove sta il nostro diaframma — e a che punto "
             "si era fermato."),
            ("Radicamento",
             "Contatto con il proprio peso, con la pietra antica del pavimento, "
             "con il territorio. Non si medita nel vuoto: si medita a casa."),
        ],

        # Ambienti 4-photo strip (home preview)
        "ambients_label": "Ambienti · Studio Armonia",
        "ambients_heading": 'Un edificio del <em>Seicento</em>, restaurato con discrezione',
        "ambients_intro":
            "Palazzo Bonomi Suardi, Via Arena 15. Quattro sale, un chiostro "
            "con erbe officinali, una tisaneria aperta a tutti gli ospiti.",
        "ambients": [
            (_AMBIENT_MASSAGE, "Sala del Massaggio",    "luce radente dalle vetrate a tutt'altezza"),
            (_AMBIENT_TEA,     "Tisaneria delle Erbe",  "raccolte nel chiostro · servite in porcellana"),
            (_AMBIENT_CANDLES, "Sala del Rituale",      "candele di cera d'api · asciugamani caldi"),
            (_AMBIENT_YOGA,    "Studio del Respiro",    "parquet antico · tappeti in lana grezza"),
        ],

        # Therapist trio (home preview)
        "therapists_label": "Operatori",
        "therapists_heading": 'Cinque <em>mani</em> che conoscono il nome di ogni ospite',
        "therapists_intro":
            "Ogni rituale è condotto personalmente da un operatore certificato. "
            "L'elenco completo, con biografie estese, è nella pagina Professionisti.",
        "therapists_trio": [
            {
                "name": "Sara Conti",
                "role": "Naturopata · Co-fondatrice",
                "bio":
                    "Dodici anni di pratica, formazione presso l'Istituto Riza "
                    "di Milano. Si occupa di fitoterapia, idroterapia alpina e "
                    "del programma stagionale di depurazione.",
                "portrait": _PORTRAIT_SARA,
            },
            {
                "name": "Davide Lai",
                "role": "Osteopata D.O.",
                "bio":
                    "Diplomato alla Scuola Superiore di Osteopatia Italiana, "
                    "specializzato in tecniche craniosacrali e viscerali. "
                    "Riceve il martedì e il giovedì.",
                "portrait": _PORTRAIT_DAVIDE,
            },
            {
                "name": "Yara Bonomi",
                "role": "Operatrice ayurveda",
                "bio":
                    "Formata a Varkala (India) e certificata dalla S.I.A. "
                    "Conduce i rituali Abhyanga e il Lomi-Lomi hawaiano, sempre "
                    "a quattro mani con un secondo operatore.",
                "portrait": _PORTRAIT_YARA,
            },
        ],

        # Sensory journey (4 step vertical)
        "journey_label": "Come si svolge",
        "journey_heading": 'La <em>visita</em>, passo per passo',
        "journey_intro":
            "Ogni rituale segue la stessa liturgia: accoglienza silenziosa, "
            "trattamento, pausa tisana, respiro. Non abbiamo casse sonore né "
            "musiche forzate — il tempo si misura da sé.",
        "journey": [
            {
                "num": "01",
                "title": "Accoglienza",
                "body":
                    "Alla soglia lasci scarpe, telefono e fretta. Ti viene "
                    "offerta una tisana calda stagionale, un foglio di carta "
                    "riciclata per annotare richieste e attenzioni, dieci "
                    "minuti di silenzio prima di entrare in sala.",
            },
            {
                "num": "02",
                "title": "Rituale del corpo",
                "body":
                    "Il trattamento che hai scelto — massaggio, hammam, "
                    "shiatsu — è condotto dal tuo operatore con olii preparati "
                    "in casa e stoffe in lino naturale. Non ci sono tempi "
                    "d'attesa in sala.",
            },
            {
                "num": "03",
                "title": "Pausa tisana",
                "body":
                    "Dopo il rituale, quindici minuti nella tisaneria con una "
                    "miscela tarata sulla stagione e sulla tua costituzione: "
                    "ortica in primavera, melissa d'estate, zenzero d'inverno.",
            },
            {
                "num": "04",
                "title": "Respiro di chiusura",
                "body":
                    "Tre minuti di respirazione guidata prima di riconsegnare "
                    "telefono e scarpe. È la parte più breve della liturgia — "
                    "ed è quella che porterai a casa.",
            },
        ],

        # Calendar-spot CTA (7 giorni, sabato soldout)
        "calendar_label": "Prossime disponibilità",
        "calendar_heading": 'Scegli il tuo <em>momento</em>',
        "calendar_intro":
            "Una selezione delle fasce aperte questa settimana. Per l'agenda "
            "completa e per richieste speciali, usa il modulo nella pagina "
            "Prenota.",
        "calendar": [
            {"day": "Lun", "num": "14", "month": "Apr",
             "slots": ["10:00", "14:30", "17:00"], "has_slots": True, "soldout": False},
            {"day": "Mar", "num": "15", "month": "Apr",
             "slots": ["09:30", "15:00"],         "has_slots": True, "soldout": False},
            {"day": "Mer", "num": "16", "month": "Apr",
             "slots": ["11:00", "16:30"],         "has_slots": True, "soldout": False},
            {"day": "Gio", "num": "17", "month": "Apr",
             "slots": ["completo"],                "has_slots": False, "soldout": True},
            {"day": "Ven", "num": "18", "month": "Apr",
             "slots": ["10:30", "14:00", "18:00"], "has_slots": True, "soldout": False},
            {"day": "Sab", "num": "19", "month": "Apr",
             "slots": ["completo"],                "has_slots": False, "soldout": True},
            {"day": "Dom", "num": "20", "month": "Apr",
             "slots": ["silenzio"],                "has_slots": False, "soldout": True},
        ],
        "calendar_cta": "Apri il modulo di prenotazione",

        # Press band (Italian wellness editorial press)
        "press_label": "Raccontati su",
        "press": [
            "Vogue Italia Living",
            "Marie Claire",
            "Io Donna",
            "Natural Style",
            "Corriere della Sera · Salute",
        ],
    },

    # ──────────────────── FILOSOFIA (about) ────────────────────
    "filosofia": {
        "eyebrow":  "La nostra filosofia",
        "headline": "Tre parole, <em>nessuna promessa</em>",
        "intro":
            "Studio Armonia nasce nel 2011 da un'idea semplice: un centro "
            "olistico che non venda trasformazioni, ma restituisca tempo. "
            "Tre pilastri — Respiro, Rituale, Natura — ispirano ogni scelta, "
            "dal palinsesto dei trattamenti alle erbe della tisaneria.",

        "pillars": [
            {
                "init":  "R",
                "title": "Respiro",
                "body":
                    "Il respiro è il filo rosso di ogni rituale. Ogni "
                    "trattamento comincia e finisce con tre minuti di pratica "
                    "respiratoria — lo chiamiamo ritmo del ritorno.",
            },
            {
                "init":  "R",
                "title": "Rituale",
                "body":
                    "Non sedute, non pacchetti: rituali. Ciascuno con una "
                    "liturgia precisa, ripetibile, che non dipende dall'umore "
                    "dell'operatore né dall'agenda della settimana.",
            },
            {
                "init":  "N",
                "title": "Natura",
                "body":
                    "Le nostre materie vengono dal territorio: olio d'oliva "
                    "pugliese, sale dell'Adriatico, argille dei colli emiliani, "
                    "erbe raccolte nel chiostro da marzo a ottobre.",
            },
        ],

        "photo_image": _AMBIENT_RITUAL,
        "photo_caption":
            "Sala del Rituale · Palazzo Bonomi Suardi, Bergamo Alta",
        "photo_sub": "Restauro conservativo · 2011",

        "timeline_label": "La nostra storia",
        "timeline_heading": "Quindici anni di <em>lavoro silenzioso</em>",
        "timeline": [
            {
                "year":  "2011",
                "title": "La prima sala in Via Arena",
                "body":
                    "Chiara Bonomi e Sara Conti aprono il primo spazio al "
                    "piano terra di Palazzo Bonomi Suardi. Due stanze, una "
                    "sala d'attesa, una tisaneria di quattro metri quadrati.",
            },
            {
                "year":  "2014",
                "title": "Il chiostro delle erbe officinali",
                "body":
                    "Viene restaurato il chiostro interno e piantato il primo "
                    "giardino di erbe officinali: melissa, lavanda, salvia "
                    "sclarea, iperico, ortica, menta piperita.",
            },
            {
                "year":  "2018",
                "title": "L'hammam e la sala del vapore",
                "body":
                    "Aggiunta la sala hammam con volta a botte in mattoni "
                    "recuperati, progettata dall'architetto Valeria Cipolli "
                    "in dialogo con la Soprintendenza.",
            },
            {
                "year":  "2022",
                "title": "Lo studio del respiro",
                "body":
                    "Apertura dello Studio del Respiro al primo piano, con "
                    "parquet antico restaurato, dedicato a yoga, meditazione "
                    "e pratiche somatiche di gruppo (massimo sei persone).",
            },
        ],

        "cta_label": "Il passo successivo",
        "cta_heading": 'Conoscere <em>Studio Armonia</em> dal vivo',
        "cta_sub":
            "La soglia non si varca online. Prenota un rituale breve — "
            "sessantacinque minuti — e lascia che lo spazio faccia il resto.",
        "cta_primary":   "Riserva un rituale",
        "cta_secondary": "Sfoglia i rituali",
    },

    # ──────────────────── RITUALI (services) ────────────────────
    "rituali": {
        "eyebrow":  "Listino rituali",
        "headline": "Dieci rituali, <em>nessuna corsia veloce</em>",
        "intro":
            "Ogni rituale ha una durata precisa, un operatore dedicato, "
            "una liturgia che si è depositata negli anni. I prezzi sono "
            "definitivi — non esistono sovrapprezzi weekend né supplementi.",

        "treatments": [
            {
                "name":  "Massaggio Mediterraneo",
                "meta":  "55 min · olio d'oliva di Sorrento e agrumi",
                "desc":
                    "Pressioni lunghe, olio caldo estratto a freddo, essenze "
                    "di bergamotto e limone di Sorrento. Indicato per chi "
                    "arriva per la prima volta o per chi cerca un rituale "
                    "introduttivo non invasivo.",
                "price": "€ 85",
            },
            {
                "name":  "Rituale Hammam",
                "meta":  "90 min · vapore, sale grezzo, argilla rossa",
                "desc":
                    "Ventiquattro minuti in sala vapore con oli essenziali di "
                    "eucalipto, scrub al sale grezzo dell'Adriatico, maschera "
                    "di argilla rossa dei colli bolognesi, doccia sorgiva, "
                    "tisana di chiusura. A quattro mani.",
                "price": "€ 120",
            },
            {
                "name":  "Riequilibrio Energetico",
                "meta":  "60 min · pranoterapia e respiro guidato",
                "desc":
                    "Seduta non-contact di pranoterapia condotta da Chiara "
                    "Bonomi, con pratica respiratoria guidata nei primi e "
                    "ultimi dieci minuti. Adatta anche in gravidanza dal "
                    "secondo trimestre.",
                "price": "€ 95",
            },
            {
                "name":  "Idroterapia Alpina",
                "meta":  "75 min · acque sorgive del Monte Resegone",
                "desc":
                    "Percorso di tre vasche a temperatura crescente con acque "
                    "sorgive imbottigliate alla fonte, alternate a getti "
                    "freddi. Conduce il percorso Davide Lai.",
                "price": "€ 110",
            },
            {
                "name":  "Pietre Calde",
                "meta":  "75 min · basalto vulcanico · olio di mandorle",
                "desc":
                    "Dodici pietre di basalto riscaldate a 48°C appoggiate "
                    "sui punti Shu del dorso, massaggio di scioglimento con "
                    "olio di mandorle dolci e oli essenziali di incenso.",
                "price": "€ 105",
            },
            {
                "name":  "Ayurveda Abhyanga",
                "meta":  "90 min · olii caldi medicati · due operatrici",
                "desc":
                    "Rituale classico ayurvedico condotto da Yara Bonomi in "
                    "coppia con una seconda operatrice. Oli medicati scelti "
                    "sulla base della costituzione (Vata, Pitta, Kapha) "
                    "rilevata durante il colloquio preliminare.",
                "price": "€ 135",
            },
            {
                "name":  "Shiatsu",
                "meta":  "60 min · pressioni sui meridiani · futon",
                "desc":
                    "Seduta tradizionale di shiatsu condotta da Miguel "
                    "Ferrari su futon giapponese. Il ricevente resta "
                    "abbigliato con indumenti comodi forniti dallo studio.",
                "price": "€ 90",
            },
            {
                "name":  "Lomi-Lomi",
                "meta":  "75 min · massaggio hawaiano a onde lunghe",
                "desc":
                    "Onde lunghe con avambraccio e palmo della mano, oli "
                    "tropicali di cocco e monoi. Conduce Yara Bonomi, "
                    "certificata dalla Hawaiian Lomi-Lomi School di Kauai.",
                "price": "€ 115",
            },
            {
                "name":  "Craniosacrale",
                "meta":  "55 min · tocco leggero · fluidi cerebrali",
                "desc":
                    "Seduta osteopatica craniosacrale condotta da Davide Lai. "
                    "Pressioni leggerissime (inferiori a cinque grammi) per "
                    "ascoltare e accompagnare il ritmo dei fluidi. "
                    "Compatibile con gravidanza.",
                "price": "€ 95",
            },
            {
                "name":  "Rituale Madre-Terra",
                "meta":  "105 min · rituale completo stagionale",
                "desc":
                    "Il nostro rituale più lungo, pensato per i cambi di "
                    "stagione: idroterapia breve, scrub corpo intero, "
                    "massaggio con olii della stagione, rito di chiusura con "
                    "campana tibetana e tisana di rosa canina.",
                "price": "€ 150",
            },
        ],
        "reserve_label": "Riserva",

        "advice_label":   "Prima del trattamento",
        "advice_heading": "Tre <em>attenzioni</em> che consigliamo",
        "advice": [
            {
                "title": "Arriva quindici minuti prima",
                "body":
                    "La transizione non è un lusso: è parte del rituale. "
                    "Quindici minuti in sala d'attesa, con una tisana calda, "
                    "permettono al sistema nervoso di allinearsi allo spazio.",
            },
            {
                "title": "Evita il caffè nelle due ore precedenti",
                "body":
                    "La caffeina rende il corpo più reattivo alle pressioni "
                    "e accorcia la finestra di rilassamento. Una tisana, un "
                    "bicchiere d'acqua tiepida, una camomilla: meglio.",
            },
            {
                "title": "Comunica ogni attenzione",
                "body":
                    "Gravidanza, ciclo mestruale, intolleranze olfattive, "
                    "infortuni recenti, farmaci assunti: vanno sempre "
                    "comunicati in fase di prenotazione. Non sono imbarazzanti, "
                    "sono utili al tuo operatore.",
            },
        ],

        "packages_label":   "Pacchetti · week-end lunghi",
        "packages_heading": 'Due <em>soggiorni</em> pensati come parentesi',
        "packages_intro":
            "Due proposte cucite con hotel convenzionati nella Bergamo Alta "
            "per chi desidera un soggiorno breve, di recupero.",
        "packages": [
            {
                "tag":       "Giornata singola",
                "title":     "Respiro",
                "duration":  "1 giornata · 3 rituali · tisane illimitate",
                "desc":
                    "Una giornata intera nello studio con tre rituali "
                    "concatenati, accesso alla tisaneria dalle dieci alle "
                    "diciotto, pranzo leggero in-house a cura dello chef "
                    "Matteo Riva.",
                "includes": [
                    "Ingresso dalle 10:00, uscita entro le 18:00",
                    "Riequilibrio Energetico (60 min)",
                    "Massaggio Mediterraneo (55 min)",
                    "Rituale Madre-Terra breve (75 min)",
                    "Pranzo leggero · tisaneria illimitata",
                ],
                "price": "€ 340",
                "cta":   "Riserva il Respiro",
            },
            {
                "tag":       "Tre giorni",
                "title":     "Detox 3 giorni",
                "duration":  "3 giornate · 5 rituali · tisaneria stagionale",
                "desc":
                    "Tre giornate cucite con l'Hotel Gombit quattro stelle "
                    "(camera doppia inclusa), cinque rituali distribuiti nei "
                    "tre giorni, piano alimentare vegetariano concordato con "
                    "la naturopata.",
                "includes": [
                    "Pernottamento 2 notti · Hotel Gombit 4★",
                    "Cinque rituali su tre giornate",
                    "Piano alimentare vegetariano a cura della naturopata",
                    "Accesso libero al chiostro e allo Studio del Respiro",
                    "Kit stagionale da portare a casa · valore € 85",
                ],
                "price": "€ 920",
                "cta":   "Riserva i 3 giorni",
            },
        ],

        "cta_label": "Il passo successivo",
        "cta_heading": 'Una sola <em>soglia</em> da attraversare',
        "cta_sub":
            "Prenota il rituale che ti incuriosisce di più. Se non sei "
            "sicuro di quale scegliere, scrivici: ti orientiamo noi.",
        "cta_primary":   "Apri il modulo di prenotazione",
        "cta_secondary": "Chiedi un consiglio",
    },

    # ──────────────────── AMBIENTI (gallery) ────────────────────
    "ambienti": {
        "eyebrow":  "Palazzo Bonomi Suardi",
        "headline": 'Otto <em>sale</em>, un chiostro, una tisaneria',
        "intro":
            "Ogni ambiente è stato restaurato in dialogo con la "
            "Soprintendenza ai Beni Architettonici di Bergamo. Mattoni a "
            "vista, parquet antico, vetrate che aprono sul chiostro delle "
            "erbe officinali.",
        "rooms": [
            {
                "span":  "a",
                "image": _ROOM_HAMMAM,
                "tag":   "Sala I · Hammam",
                "title": "Hammam a volta",
                "sub":
                    "Volta a botte in mattoni recuperati dal restauro, "
                    "seduta a due livelli, scrub al sale grezzo e getto "
                    "sorgivo a freddo.",
            },
            {
                "span":  "b",
                "image": _AMBIENT_MASSAGE,
                "tag":   "Sala II · Massaggi",
                "title": "Sala del Sole",
                "sub":
                    "Due lettini affiancati per i rituali a quattro mani. "
                    "Luce radente da sud-est.",
            },
            {
                "span":  "c",
                "image": _ROOM_WATER,
                "tag":   "Sala III · Acqua",
                "title": "Sala del Rituale d'Acqua",
                "sub":
                    "Vasca idroterapica in rame martellato, percorso di tre "
                    "temperature. Acqua sorgiva del Resegone.",
            },
            {
                "span":  "d",
                "image": _ROOM_TISANERIA,
                "tag":   "Tisaneria",
                "title": "Tisaneria delle Erbe",
                "sub":
                    "Miscele stagionali raccolte dal nostro chiostro. "
                    "Servite in porcellana bianca di Limoges.",
            },
            {
                "span":  "e",
                "image": _ROOM_GARDEN,
                "tag":   "Chiostro",
                "title": "Giardino officinale",
                "sub":
                    "Melissa, lavanda, salvia sclarea, iperico, ortica. "
                    "Accessibile a tutti gli ospiti.",
            },
            {
                "span":  "f",
                "image": _AMBIENT_YOGA,
                "tag":   "Studio del Respiro",
                "title": "Studio del Respiro",
                "sub":
                    "Parquet antico restaurato, tappeti in lana grezza, "
                    "massimo sei persone per sessione di gruppo.",
            },
            {
                "span":  "g",
                "image": _ROOM_MEDITATION,
                "tag":   "Sala IV · Meditazione",
                "title": "Camera del Silenzio",
                "sub":
                    "Sei tatami in cotone biologico, campana tibetana "
                    "d'epoca, luce di candele di cera d'api.",
            },
            {
                "span":  "h",
                "image": _ROOM_RECEPTION,
                "tag":   "Ingresso",
                "title": "Soglia · Reception",
                "sub":
                    "Pavimento originale del Seicento, libro degli "
                    "ospiti, prima tisana calda dopo la soglia.",
            },
        ],

        "cta_label": "Il passo successivo",
        "cta_heading": 'Attraversa <em>la soglia</em>',
        "cta_sub":
            "Gli ambienti si abitano, non si fotografano. Il modo migliore "
            "per conoscerli è un rituale breve di sessanta minuti.",
        "cta_primary":   "Riserva un rituale",
        "cta_secondary": "Scegli un trattamento",
    },

    # ──────────────────── PROFESSIONISTI (team) ────────────────────
    "professionisti": {
        "eyebrow":  "Gli operatori",
        "headline": 'Cinque <em>firme</em>, un solo libro degli ospiti',
        "intro":
            "Ogni operatore ha una formazione specifica, un proprio "
            "calendario, una propria firma di trattamento. Chi ti accoglie "
            "alla soglia è lo stesso che ti accompagna al rituale.",

        "people": [
            {
                "name":     "Sara Conti",
                "role":     "Naturopata · Co-fondatrice",
                "portrait": _PORTRAIT_SARA,
                "tags":     ["Fitoterapia", "Idroterapia", "Programma stagionale"],
                "bio":
                    "Diplomata in Naturopatia all'Istituto Riza di Milano nel "
                    "2009 e certificata FIF. Dopo cinque anni allo Spa du "
                    "Château di Annecy, rientra a Bergamo e co-fonda Studio "
                    "Armonia con Chiara Bonomi. Cura il programma stagionale "
                    "di depurazione e il giardino officinale del chiostro.",
                "quote":
                    "«Non esiste una dieta disintossicante. Esiste un'attenzione "
                    "ripetuta a come mangi, quando respiri, quanto dormi.»",
            },
            {
                "name":     "Davide Lai",
                "role":     "Osteopata D.O.",
                "portrait": _PORTRAIT_DAVIDE,
                "tags":     ["Craniosacrale", "Viscerale", "Strutturale"],
                "bio":
                    "Diplomato alla Scuola Superiore di Osteopatia Italiana "
                    "(S.S.O.I.) nel 2014, si è specializzato in tecniche "
                    "craniosacrali e viscerali. Riceve il martedì e il "
                    "giovedì su prenotazione, è il riferimento dello studio "
                    "per post-parto e dolore cronico.",
                "quote":
                    "«Il corpo sa già come guarire — il mio lavoro è "
                    "ascoltare dove ha smesso di farlo.»",
            },
            {
                "name":     "Yara Bonomi",
                "role":     "Operatrice ayurveda",
                "portrait": _PORTRAIT_YARA,
                "tags":     ["Abhyanga", "Lomi-Lomi", "Shirodhara"],
                "bio":
                    "Formata a Varkala (Kerala, India) presso la Kerala "
                    "Ayurveda Academy nel 2016, certificata dalla Società "
                    "Italiana di Ayurveda (S.I.A.). Conduce i rituali "
                    "Abhyanga e Shirodhara — sempre a quattro mani — e il "
                    "Lomi-Lomi hawaiano.",
                "quote":
                    "«L'abhyanga non è un massaggio: è una conversazione "
                    "con la pelle, fatta di olio e di tempo.»",
            },
            {
                "name":     "Elena Rossi",
                "role":     "Maestra yoga certificata RYT-500",
                "portrait": _PORTRAIT_ELENA,
                "tags":     ["Hatha", "Yin", "Respiro somatico"],
                "bio":
                    "Certificata RYT-500 dalla Yoga Alliance dopo quattro "
                    "anni di pratica a Rishikesh e due anni di studio con "
                    "Judith Hanson Lasater a San Francisco. Conduce le "
                    "sessioni di gruppo nello Studio del Respiro il "
                    "mercoledì, venerdì e sabato mattina.",
                "quote":
                    "«Lo yoga che faccio fare qui non è una ginnastica "
                    "esotica: è un modo per ricordare dove stanno le spalle.»",
            },
            {
                "name":     "Miguel Ferrari",
                "role":     "Operatore shiatsu · FISIEO",
                "portrait": _PORTRAIT_MIGUEL,
                "tags":     ["Shiatsu Namikoshi", "Do-in", "Medicina cinese"],
                "bio":
                    "Diplomato alla Scuola Europea di Shiatsu di Milano nel "
                    "2018 e iscritto alla FISIEO. Riceve il lunedì, mercoledì "
                    "e venerdì. Cura una rubrica mensile sulle stagioni del "
                    "corpo secondo la medicina tradizionale cinese.",
                "quote":
                    "«Le pressioni non sono la tecnica: la tecnica è dove "
                    "ascolto prima di premere.»",
            },
        ],

        "philo_label": "La filosofia degli operatori",
        "philo_quote":
            "«Un rituale ben fatto non <em>aggiunge</em> nulla a chi lo riceve: "
            "gli ricorda soltanto cosa sapeva già.»",
        "philo_attr": "— Manifesto degli operatori · 2015",

        "cta_label":   "Il passo successivo",
        "cta_heading": 'Riserva il tuo <em>primo incontro</em>',
        "cta_primary": "Apri il modulo di prenotazione",
    },

    # ──────────────────── CONTATTI (contact) ────────────────────
    "contatti": {
        "eyebrow":  "Trovare lo studio",
        "headline": 'Via Arena 15, <em>Bergamo Alta</em>',
        "intro":
            "Siamo al centro della città alta medievale, a pochi passi da "
            "Piazza Vecchia e dalla Basilica di Santa Maria Maggiore. "
            "L'ingresso è segnalato da una targa in ottone satinato.",

        "map_image": _MAP_IMG,

        "blocks": [
            {"label": "Indirizzo",
             "value": "Via Arena 15",
             "sub":   "24129 Bergamo Alta · Palazzo Bonomi Suardi"},
            {"label": "Telefono",
             "value": "+39 035 412 998",
             "sub":   "Risposta diretta 9:00 – 19:00"},
            {"label": "Email",
             "value": "ritual@studioarmonia.it",
             "sub":   "Risposta entro la giornata"},
            {"label": "Richieste speciali",
             "value": "+39 346 772 4108",
             "sub":   "WhatsApp · attivo 9:00 – 18:00"},
        ],

        "access_label": "Come raggiungerci",
        "access": [
            {"mode": "Auto",
             "text": "Parcheggio Monterosso (Via Fara), poi cinque minuti a "
                     "piedi fino a Via Arena."},
            {"mode": "Funicolare",
             "text": "Funicolare di Bergamo Alta da Viale Vittorio Emanuele, "
                     "discesa Mercato delle Scarpe, due minuti a piedi."},
            {"mode": "A piedi",
             "text": "Dalla stazione FS di Bergamo Bassa via autobus linea 1 "
                     "(15 minuti), oppure 35 minuti di passeggiata urbana."},
        ],

        "form_title": "Scrivici",
        "form_intro":
            "Per informazioni su rituali, regali rituali o pacchetti "
            "soggiorno, usa il modulo qui sotto. Rispondiamo sempre entro "
            "la giornata lavorativa successiva.",

        "form_placeholders": {
            "name":    "Chiara Ferrari",
            "email":   "chiara@email.it",
            "phone":   "+39 333 ...",
            "message":
                "Vorrei prenotare un rituale per un regalo, "
                "preferibilmente nel pomeriggio del venerdì.",
        },
        "form_helpers": {
            "name":     "Come preferisci essere chiamata o chiamato.",
            "email":    "Usiamo l'email solo per risponderti.",
            "phone":    "Se preferisci essere richiamata, indicalo qui.",
            "interest": "Se non sei sicura, scegli Consulenza iniziale.",
            "message":  "Resta in poche righe, siamo bravi a rispondere alle "
                        "domande concrete.",
        },
        "form_fields": {
            "interest_label": "Rituale di interesse",
            "interest_options": [
                "Consulenza iniziale",
                "Massaggio Mediterraneo",
                "Rituale Hammam",
                "Riequilibrio Energetico",
                "Ayurveda Abhyanga",
                "Pacchetto Respiro",
                "Pacchetto Detox 3 giorni",
                "Regalo rituale",
                "Altro",
            ],
        },
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Reg. UE 679/2016. I dati restano custoditi in Studio Armonia "
            "e non sono ceduti a terzi.",
        "form_submit_note":
            "Risposta entro la giornata lavorativa successiva.",

        "hours_label":   "Orari",
        "hours_heading": 'Aperti <em>sei giorni</em> su sette',
        "hours_note":
            "La domenica Studio Armonia osserva la giornata del silenzio. "
            "Per urgenze gli ospiti in percorso possono scrivere a "
            "ritual@studioarmonia.it — risposta garantita entro tre ore.",
        "hours": [
            {"day": "Lunedì",    "value": "9:00 – 20:00"},
            {"day": "Martedì",   "value": "9:00 – 20:00"},
            {"day": "Mercoledì", "value": "9:00 – 20:00"},
            {"day": "Giovedì",   "value": "9:00 – 20:00"},
            {"day": "Venerdì",   "value": "9:00 – 20:00"},
            {"day": "Sabato",    "value": "9:00 – 18:00"},
            {"day": "Domenica",  "value": "Giornata del silenzio"},
        ],
    },

    # ──────────────────── PRENOTA (appointment) ────────────────────
    "prenota": {
        "eyebrow":  "Prenotazione",
        "headline": 'Il rituale comincia quando <em>attraversi la soglia</em>',
        "intro":
            "La prenotazione è il primo gesto del rituale. Scegli la "
            "giornata che ti invita di più, compila il modulo sotto: ti "
            "ricontattiamo entro due ore lavorative per confermare.",

        # 7-day calendar widget (calendar-spot, more complete than home)
        "calendar_heading": 'Sette giorni di <em>prossima disponibilità</em>',
        "calendar_hint":    "Indicativo · conferma via email",
        "calendar": [
            {"day": "Lun", "num": "14", "month": "Apr",
             "slots": ["10:00", "14:30", "17:00"], "has_slots": True, "soldout": False},
            {"day": "Mar", "num": "15", "month": "Apr",
             "slots": ["09:30", "13:00", "15:00"], "has_slots": True, "soldout": False},
            {"day": "Mer", "num": "16", "month": "Apr",
             "slots": ["11:00", "16:30"],          "has_slots": True, "soldout": False},
            {"day": "Gio", "num": "17", "month": "Apr",
             "slots": ["completo"],                 "has_slots": False, "soldout": True},
            {"day": "Ven", "num": "18", "month": "Apr",
             "slots": ["10:30", "14:00", "18:00"], "has_slots": True, "soldout": False},
            {"day": "Sab", "num": "19", "month": "Apr",
             "slots": ["completo"],                 "has_slots": False, "soldout": True},
            {"day": "Dom", "num": "20", "month": "Apr",
             "slots": ["silenzio"],                 "has_slots": False, "soldout": True},
        ],

        # Dark-band form wrapper
        "form_title":
            'Modulo di <em>prenotazione</em>',
        "form_side_note":
            "Riserva cinque minuti per compilare con cura. Più dettagli ci "
            "lasci, più il rituale che ti proponiamo sarà coerente con te.",
        "form_side_small": "↓ Modulo riservato",

        "why_label": "Perché prenotare online",
        "why": [
            "Conferma via email entro due ore lavorative.",
            "Cancellazione gentile entro le 24 ore precedenti, senza costi.",
            "Intolleranze e attenzioni vengono lette in anticipo dall'operatore.",
            "Il tuo slot resta bloccato fino a conferma da parte nostra.",
        ],

        "form_fields": [
            {"name": "name", "label": "Nome e cognome",
             "placeholder": "Chiara Ferrari",
             "type": "text", "required": True, "full_width": False,
             "helper": "Come preferisci essere chiamata."},
            {"name": "email", "label": "Email",
             "placeholder": "chiara@email.it",
             "type": "email", "required": True, "full_width": False,
             "helper": "La conferma arriva qui."},
            {"name": "phone", "label": "Telefono",
             "placeholder": "+39 333 ...",
             "type": "tel", "required": True, "full_width": False,
             "helper": "Usato solo in caso di necessità."},
            {"name": "ritual", "label": "Rituale",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Massaggio Mediterraneo (55 min · € 85)",
                 "Rituale Hammam (90 min · € 120)",
                 "Riequilibrio Energetico (60 min · € 95)",
                 "Idroterapia Alpina (75 min · € 110)",
                 "Pietre Calde (75 min · € 105)",
                 "Ayurveda Abhyanga (90 min · € 135)",
                 "Shiatsu (60 min · € 90)",
                 "Lomi-Lomi (75 min · € 115)",
                 "Craniosacrale (55 min · € 95)",
                 "Rituale Madre-Terra (105 min · € 150)",
                 "Pacchetto Respiro (1 giorno · € 340)",
                 "Pacchetto Detox 3 giorni (€ 920)",
             ],
             "helper": "Se non sei sicura, scegli Massaggio Mediterraneo: è "
                       "l'introduzione più gentile al nostro lavoro."},
            {"name": "duration", "label": "Durata preferita",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "55 minuti",
                 "60 minuti",
                 "75 minuti",
                 "90 minuti",
                 "105 minuti",
             ],
             "helper": "Facoltativa · coerente con il rituale scelto."},
            {"name": "therapist", "label": "Operatore preferito",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "Indifferente",
                 "Sara Conti (naturopata)",
                 "Davide Lai (osteopata)",
                 "Yara Bonomi (ayurveda)",
                 "Elena Rossi (yoga)",
                 "Miguel Ferrari (shiatsu)",
             ],
             "helper": "Se preferisci un operatore specifico, indicalo."},
            {"name": "date", "label": "Data preferita",
             "placeholder": "14 aprile 2026",
             "type": "date", "required": True, "full_width": False,
             "helper": "Indica la prima scelta, proporremo alternative se "
                       "non fosse disponibile."},
            {"name": "slot", "label": "Fascia oraria",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Mattina (9:00 – 12:30)",
                 "Primo pomeriggio (13:00 – 15:30)",
                 "Pomeriggio (15:30 – 18:00)",
                 "Fine pomeriggio (18:00 – 20:00)",
             ],
             "helper": "Le fasce sono indicative, confermiamo l'orario preciso."},
            {"name": "notes", "label": "Attenzioni e intolleranze",
             "placeholder":
                 "Gravidanza? Intolleranze olfattive? Infortuni recenti? "
                 "Qualcosa che il tuo operatore dovrebbe sapere? Qui lo "
                 "leggiamo.",
             "type": "textarea", "required": False, "full_width": True,
             "helper": "Nulla è troppo piccolo. Gravidanza, ciclo, farmaci, "
                       "ansie: leggiamo tutto in anticipo."},
        ],

        "form_sections": [
            {"num": "01", "title": "Chi sei",
             "meta": "Le tue coordinate di base.",
             "fields": ["name", "email", "phone"]},
            {"num": "02", "title": "Il rituale che desideri",
             "meta": "Se hai dubbi, scegli indifferente — ti consigliamo noi.",
             "fields": ["ritual", "duration", "therapist"]},
            {"num": "03", "title": "Quando",
             "meta": "Indicaci una prima scelta · confermiamo via email.",
             "fields": ["date", "slot"]},
            {"num": "04", "title": "Attenzioni",
             "meta": "Tutto ciò che il tuo operatore deve sapere prima.",
             "fields": ["notes"]},
        ],

        "consent":
            "Acconsento al trattamento dei dati personali secondo "
            "l'informativa privacy (Reg. UE 679/2016). I dati clinici e le "
            "attenzioni comunicate restano nell'archivio interno riservato.",

        "submit_label": "Riserva il tuo momento",
        "form_submit_note":
            "Confermiamo la disponibilità entro due ore lavorative.",

        "footnote":
            "La prenotazione è confermata solo dopo la nostra email di "
            "risposta. La cancellazione gentile è possibile senza costi "
            "fino a ventiquattro ore prima del rituale — dopo, tratteniamo "
            "il 50% del valore come tutela dell'operatore.",
    },
}
