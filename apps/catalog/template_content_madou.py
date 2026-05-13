"""Content tree · `madou-pasticceria` · T49 Wave 1 Pass-5.

Builds on the `fine-dining` archetype (1st reuse after Gusto · D-051
Option A: zero new HTML files). Distinctness vs Gusto carried by:

  * Brand   — `Madou · Pasticceria Atelier` (Torino) vs `Osteria
              Moderna` (Milano Brera).
  * Persona — Carla Madou, pasticciera (vs Lorenzo Fioravanti, chef).
  * Voice anchor — `lievitazione lenta` repeated across surfaces as
              load-bearing pastry-craft promise (vs Gusto's `otto
              atti` tasting-menu anchor).
  * Conversion — `saturday-laminate-preorder` + custom cake commission
              (vs Gusto `concierge-reservation`).
  * Palette — #3D2817 cacao primary / #F4E8D0 powdered-sugar
              secondary / #C8965C burnt-caramel-gold accent (vs Gusto
              coffee/amber/blood-red).
  * Conversion verbs — `Pre-ordina la sfoglia del sabato` &
              `Scrivi alla pasticciera` (vs `Riserva la serata`).
  * Section repurposing — the fine-dining template's `wine_program`
              key is repurposed as a `lieviti madre` collection
              (sourdough mother yeasts), `private_dining` as
              `cake design su commessa / eventi su misura`. Same
              shape, different domain.
  * Imagery — X.3 curator pack `bakery-pasticceria.md` consumed
              verbatim (Pexels 24 URLs: 8 hero / 5 portrait / 5
              detail / 6 gallery). T50 multilingual pass may swap to
              brand-shot photography if needed.

Tier seeds at `draft` per D-102 cadence. Multilingual EN/FR/ES/AR +
AAA walk + public flip happen in T50.
"""

from typing import Any


MADOU_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",         "label": "Casa",          "kind": "home"},
        {"slug": "forno",        "label": "Il forno",      "kind": "about"},
        {"slug": "pasticceria",  "label": "Pasticceria",   "kind": "menu"},
        {"slug": "vetrina",      "label": "Vetrina",       "kind": "gallery"},
        {"slug": "diario",       "label": "Diario",        "kind": "blog_list"},
        {"slug": "ordina",       "label": "Ordini",        "kind": "reservations"},
    ],

    "site": {
        "logo_initial":  "MD",
        "logo_word":     "Madou",
        "tag":           "Pasticceria Atelier · Torino Borgo Po · dal 2011",
        "phone":         "+39 011 8195 770",
        "email":         "atelier@madou-pasticceria.it",
        "address":       "Via Sant'Ottavio 36 · 10124 Torino",
        "hours_compact": "Mar – Sab · 7:30 – 19:30 · Dom 7:30 – 13:00",
        "star_line":     "★ Tre Torte · Gambero Rosso · 2023 · 2024 · 2025",
        "footer_intro":
            "Quindici anni di lievitazione lenta. Una sala di lavoro a vista, "
            "una vetrina di pasta cruda, due forni a soletta refrattaria. "
            "Niente pre-impasti industriali, niente surgelati, niente fretta.",
        "footer_hours_1": "Mar – Sab · 7:30 – 19:30",
        "footer_hours_2": "Dom · 7:30 – 13:00 · Lun · riposo",
        "copyright": "© 2026 Madou Atelier S.r.l. · P. IVA 11237680016",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # T49: hero plate URL threaded into the fine-dining template via
        # page_data so Madou swaps Gusto's plated-dish hero for the
        # pasticceria vetrina without forking home.html. URL from X.3
        # curator pack `bakery-pasticceria.md` (Pexels CC0-compatible).
        "hero_plate_url":
            "https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600",
        "eyebrow":  "Pasticceria Atelier · Torino Borgo Po · dal 2011",
        "headline": "Dodici ore di <em>lievitazione lenta,</em> una sfoglia che si lascia ascoltare.",
        "intro":
            "Sfoglie laminate a freddo, lievitazione naturale con pasta madre "
            "rinfrescata ogni dodici ore, cremerie montate alla minuta. La "
            "vetrina cambia ogni giorno secondo quello che è uscito dal forno "
            "all'alba.",
        "primary_cta":   "Pre-ordina la sfoglia del sabato",
        "primary_href":  "ordina",
        "secondary_cta": "La pasticciera",
        "secondary_href":"forno",

        # Repurposed labels (Gusto's "chef" → Madou's "pasticciera")
        "chef_label":    "La pasticciera",
        "star_tag":      "★ Tre Torte · Gambero Rosso 2025",
        "photo_label":   "Fotografia",
        "cuisine_label": "Pasticciera",

        "facts": [
            ("12 h", "lievitazione minima · pasta sfoglia"),
            ("3",    "lieviti madre vivi in atelier · dal 2011"),
            ("0",    "pre-impasti industriali · 0 surgelati · 0 mix"),
        ],

        "manifesto_drop_cap": "Q",
        "manifesto":
            "uando entra una sfoglia in forno, da Madou si interrompe il "
            "lavoro per quattro minuti e si ascolta. Il rumore della sfoglia "
            "che si gonfia — le bolle d'aria che si liberano fra i 64 strati "
            "di pasta laminata — è il primo indicatore se quel lotto sarà "
            "venduto sabato mattina o se andrà alla brigata. Niente cronometro, "
            "niente termometro: solo l'orecchio.",

        # Pasticceria signature — 5 "lievitati" (vs Gusto 5 "atti")
        "signature_courses": [
            ("I",    "Croissant viennoise",         "12 ore di lievitazione · 64 strati · burro normanno di Isigny",  "Caffè monorigine Etiopia Sidamo"),
            ("II",   "Maritozzo con la panna",      "lievitazione naturale 24 ore · panna fresca montata alla minuta", "Cioccolata calda Madagascar 72%"),
            ("III",  "Millefoglie alla nocciola",   "tre strati di sfoglia caramellata · crema chantilly nocciola IGP", "Bicerin tradizionale torinese"),
            ("IV",   "Bignè al cioccolato Domori",  "pasta choux della casa · ganache fondente Criollo 80%",            "Tè nero Darjeeling First Flush"),
            ("V",    "Saint Honoré ai marroni",     "stagionale autunno · marroni di Cuneo IGP · crema mousseline",     "Vino dolce Erbaluce passito"),
        ],

        # Persona — pasticciera Carla Madou
        "chef": {
            "name":  "Carla Madou",
            "role":  "Pasticciera atelier · classe 1979",
            "bio":
                "Torinese, classe 1979. Apprendistato da Iginio Massari a "
                "Brescia per quattro anni, poi due anni da Pierre Hermé a "
                "Parigi, infine due da Cristian Beduschi a Ginevra. Apre "
                "Madou nel 2011 in una ex-tipografia di Borgo Po, con una "
                "sola intuizione: lavorare solo con lieviti madre vivi e "
                "rinfrescati ogni dodici ore.",
        },

        "courses_label": "Cinque lievitati della settimana · ottobre '26",
        "courses_footline": "Vetrina viva — quello che vedete è uscito stamattina dal forno",
        "courses_full_cta": "Tutta la pasticceria",
        "chef_link_filosofia": "Il forno e le mani",
        "chef_link_diario": "Il diario di farina",

        "press_label": "Pubblicata su",
        "press": ["GAMBERO ROSSO PASTICCERIE", "DISSAPORE", "COOK CORRIERE",
                  "IDENTITÀ DI PASTICCERIA", "VOGUE CIBO"],

        # Ingredients/sourcing editorial band — pasticceria-specific
        "ingredienti": {
            "label":   "Materia prima",
            "heading": "Sedici fornitori, <em>tutti per nome.</em>",
            "text":
                "La filiera Madou è breve e tracciabile riga per riga. Il "
                "burro arriva da una latteria normanna di Isigny-sur-Mer · "
                "le uova da una fattoria a sessanta chilometri da Torino · "
                "le farine da un mulino a pietra in Val Susa · il cacao da "
                "tre piantagioni single-origin (Madagascar, Venezuela, "
                "Repubblica Dominicana) selezionate sul campo nel 2019.",
            "image":
                "https://images.pexels.com/photos/28183472/pexels-photo-28183472.jpeg"
                "?auto=compress&cs=tinysrgb&w=1000",
            "image_caption":
                "Pasta laminata sul marmo refrigerato · lavorazione delle 5:30 del mattino",
        },

        # Atmosphere teaser — pasticceria-specific imagery
        "atmosphere_teaser": {
            "label": "La vetrina viva",
            "images": [
                ("https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "La vetrina del sabato mattina"),
                ("https://images.pexels.com/photos/16140003/pexels-photo-16140003.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Decorazione a mano · torta su commessa"),
                ("https://images.pexels.com/photos/30853716/pexels-photo-30853716.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Croissant alla viennoise appena sfornati"),
                ("https://images.pexels.com/photos/31000323/pexels-photo-31000323.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Macarons stagionali · ottobre '26"),
            ],
            "link_label": "Entra in vetrina",
            "link_href":  "vetrina",
        },

        # Awards/recognition — pastry awards (not Michelin)
        "riconoscimenti": {
            "label": "Riconoscimenti",
            "items": [
                ("★★★", "Tre Torte · Gambero Rosso", "Premio annuale · 2023 · 2024 · 2025"),
                ("AMPI", "Accademia Maestri Pasticceri", "Membro dal 2017 · sede Brescia"),
                ("CMP",  "Coppa del Mondo Pasticceria", "Squadra Italia · alternato 2022 · 4° posto Lione"),
                ("DIS",  "Dissapore · 50 Pasticcerie", "Prima posizione Piemonte 2024 · top 5 Italia 2025"),
            ],
        },

        # CTA section
        "cta_heading": "Solo lievitazione lenta, <em>solo quello che esce dal forno la mattina.</em>",
        "cta_primary":  "Pre-ordina la sfoglia del sabato",
        "cta_secondary": "Scopri tutta la pasticceria",

        # Seasonal highlight card — pasticceria seasonal
        "stagione": {
            "label":     "In vetrina ora",
            "title":     "Pasticceria autunno '26",
            "subtitle":  "Marroni, persimmon, cioccolato monorigine · dal 6 ottobre",
            "text":
                "La carta autunno si apre il 6 ottobre con il Saint Honoré ai "
                "marroni di Cuneo IGP, la millefoglie al kaki astringente del "
                "Bel Paese e il Mont-Blanc 2026 in versione monoporzione. "
                "Tutta la pasticceria autunnale resta in vetrina fino al 30 "
                "novembre, poi si passa al Natale.",
            "cta_label": "Scopri tutta la carta autunno →",
            "cta_href":  "pasticceria",
        },

        # Producer showcase — pastry supply chain (vs Gusto wine producers)
        "produttori": {
            "label":   "I fornitori",
            "heading": "Sedici mani, <em>una vetrina sola.</em>",
            "intro":
                "Ogni materia prima Madou ha un fornitore con nome, indirizzo "
                "e numero di telefono. Burro, latte, uova, farine, cacao, "
                "frutta, miele — niente arriva da catalogo. Tutti i fornitori "
                "sono stati visitati personalmente da Carla almeno una volta.",
            "items": [
                {
                    "portrait":
                        "https://images.pexels.com/photos/8477754/pexels-photo-8477754.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Pierre Marchais",
                    "role": "Burro normanno AOP",
                    "area": "Isigny-sur-Mer · Normandia",
                    "blurb":
                        "Il burro Isigny AOP arriva ogni mercoledì in carico "
                        "refrigerato a 4°C. Latteria familiare dal 1932, "
                        "quattro vacche normande per ettaro.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/8188937/pexels-photo-8188937.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Famiglia Brero",
                    "role": "Mulino a pietra Val Susa",
                    "area": "Bussoleno · Piemonte",
                    "blurb":
                        "Macinatura a pietra in tre passaggi · grano "
                        "tenero Bologna 100% locale · niente raffinazione. "
                        "Tre tipi di farina, una al mese in esclusiva.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/11869895/pexels-photo-11869895.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Olivier Domori",
                    "role": "Cacao single-origin",
                    "area": "Sambirano · Madagascar",
                    "blurb":
                        "Tre piantagioni selezionate sul campo da Carla nel "
                        "2019. Cacao Criollo trinitario al 80%, tostato a "
                        "freddo in Italia · partita tracciata per lotto.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/29198586/pexels-photo-29198586.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Anna Negroni",
                    "role": "Frutta stagionale Cuneo",
                    "area": "Lagnasco · Piemonte",
                    "blurb":
                        "Pesche di Cuneo IGP a giugno · marroni IGP a "
                        "ottobre · kaki astringenti a novembre. Otto "
                        "ettari, raccolta a mano, niente celle.",
                },
            ],
        },

        # Repurposed `private_dining` → `eventi su misura` / cake design
        "private_dining": {
            "label":   "Eventi su misura",
            "heading": "Cake design & <em>commesse private.</em>",
            "intro":
                "Da Madou si possono ordinare torte cerimoniali, "
                "wedding cake e piccole produzioni private per eventi. "
                "Tre vie d'ingresso, ognuna con tempi e prezzi diversi.",
            "experiences": [
                {
                    "icon": "fork",
                    "title": "Torta su commessa",
                    "meta":  "Min. 8 porzioni · da €18 / porzione",
                    "desc":
                        "Disegno personalizzato sulla base di tre incontri "
                        "preliminari con Carla. Tempi di consegna: due "
                        "settimane minimo. Decoriamo solo a mano, niente "
                        "stampi industriali.",
                },
                {
                    "icon": "door",
                    "title": "Wedding cake",
                    "meta":  "Da 40 porzioni · da €22 / porzione",
                    "desc":
                        "Quattro mesi di lavoro a quattro mani con la "
                        "coppia. Tre prove gusto incluse nel servizio. "
                        "Consegna in atelier o trasporto refrigerato a "
                        "carico Madou nel Piemonte centrale.",
                },
                {
                    "icon": "wine",
                    "title": "Buffet privato",
                    "meta":  "20 – 60 ospiti · da €38 / ospite",
                    "desc":
                        "Solo pasticceria mignon · 8 referenze, "
                        "150 pezzi minimi. Cottura il giorno dell'evento, "
                        "consegna refrigerata. Cosa di sabato pomeriggio "
                        "lasciamo libero.",
                },
            ],
            "cta_label": "Scrivi alla pasticciera",
            "cta_href":  "ordina",
        },

        # Repurposed `wine_program` → `lieviti madre` collection
        "wine_program": {
            "label":   "L'archivio dei lieviti",
            "heading": "Tre lieviti madre vivi, <em>una sola pasticceria.</em>",
            "intro":
                "L'atelier conserva tre lieviti madre attivi, ognuno con "
                "una sua firma di acidità e una sua resa. Ogni lievitato "
                "Madou è abbinato al lievito che gli appartiene — niente "
                "lievito di birra, niente miglioratori.",
            "sommelier": {
                "name": "Tommaso Rinaldi",
                "role": "Maestro lievitista · responsabile pasta madre",
                "bio":
                    "Apprendista da Carla dal 2014, responsabile del "
                    "rinfresco delle tre paste madri dal 2018. Rinfresca "
                    "ogni dodici ore, alle 5:30 e alle 17:30. Conserva la "
                    "memoria di farina di ogni partita.",
            },
            "pairings": [
                ("01", "Madre M-1 · sfoglia laminata",
                 "Lievito attivo dal 2011 · acidità lattica dominante · "
                 "pH 4.2 · pieghe rapide, riposo lungo. Usato per croissant, "
                 "kouign-amann, brioche col tuppo.",
                 "12 – 16 h"),
                ("02", "Madre M-2 · panettoni e lievitati alti",
                 "Madre nata nel 2014 da rinfresco a triplo. Acidità mista "
                 "acetica-lattica, pH 4.5 · sviluppo verticale aggressivo. "
                 "Solo panettone, colomba e veneziana.",
                 "36 – 48 h"),
                ("03", "Madre M-3 · pan brioche e laminati dolci",
                 "Madre rinfrescata con miele di castagno · acidità contenuta, "
                 "pH 4.7 · profumo di nocciola tostata. Maritozzi, brioche "
                 "tonde, treccia al cioccolato.",
                 "8 – 12 h"),
            ],
            "cellar_facts": [
                ("3",   "lieviti madre vivi"),
                ("12h", "frequenza rinfresco fissa"),
                ("2011", "anno della prima madre · M-1"),
            ],
        },
    },

    # ─── FORNO (about) — Gusto's "filosofia" page ────────────
    "forno": {
        "eyebrow":  "Il forno",
        "headline": "Quindici anni di forno, <em>una sola promessa di sfoglia.</em>",
        "intro":
            "Madou nasce nel 2011 in una ex-tipografia di Borgo Po, a "
            "Torino. L'atelier ha una sola sala di lavoro a vista sulla "
            "strada e due forni a soletta refrattaria. La promessa è "
            "sempre la stessa: zero pre-impasti, zero surgelati, zero "
            "miscele industriali. Solo lievitazione lenta, solo materia "
            "prima tracciata.",

        "history": [
            ("2011",
             "Carla Madou apre l'atelier in via Sant'Ottavio dopo otto anni "
             "tra Brescia (Massari), Parigi (Hermé) e Ginevra (Beduschi). "
             "Quattro coperti al banco, due referenze di pasticceria, una "
             "sola madre — M-1, fondata con farina del mulino Brero."),
            ("2014",
             "Tommaso Rinaldi entra come apprendista e nel giro di tre anni "
             "diventa responsabile dei lieviti madre. Nasce M-2, la madre "
             "dei panettoni, da rinfresco a triplo della M-1."),
            ("2017",
             "Carla viene ammessa all'Accademia Maestri Pasticceri Italiani "
             "(AMPI), seconda donna piemontese a entrarci dopo Sonia Balacchi."),
            ("2021",
             "Trasferimento dell'atelier in via Sant'Ottavio 36, la ex-tipografia "
             "completamente ristrutturata. Tre forni, due laminatori, una "
             "vetrina di quindici metri lineari aperta sulla strada."),
            ("2023",
             "Gambero Rosso assegna le Tre Torte (massimo riconoscimento "
             "pasticcero) e le conferma nel 2024 e nel 2025. Madou diventa "
             "tappa fissa del circuito pasticcerie d'autore italiane."),
        ],

        "filosofia_image":
            "https://images.pexels.com/photos/30918889/pexels-photo-30918889.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400",
        "filosofia_image_caption": "Il laboratorio · Carla Madou al laminatoio",

        "method_title": "Metodo",
        "method_paragraphs": [
            "Tutta la pasticceria Madou parte dal rinfresco della madre. "
            "Alle 5:30 del mattino Tommaso rinfresca le tre paste madri e "
            "stacca le quantità per le impastate del giorno · alle 17:30 "
            "rinfresca di nuovo per le impastate notturne. È un orario "
            "fisso, indipendente da Natale, Pasqua o ferragosto.",
            "Le sfoglie laminate vengono preparate la sera prima e riposano "
            "in cella a 4°C per dodici ore minime, sedici ore per i lotti "
            "del sabato. Il burro viene battuto a freddo · il sale di Mothia "
            "viene aggiunto in scaglie · le pieghe sono sempre quattro, mai "
            "tre · il ciclo di laminazione finale produce 64 strati di "
            "pasta visibili al taglio.",
            "Le cremerie si preparano a vista alla minuta. Niente pasticceria "
            "Madou esce dal banco con una crema preparata più di due ore "
            "prima · le frolle si tagliano a mano · le ganache si emulsionano "
            "con frusta al passaggio successivo. Lavorare alla minuta è il "
            "motivo per cui non vendiamo cake design senza preavviso.",
        ],

        "values_label": "Cosa garantiamo",
        "values_heading": "Quattro promesse <em>non negoziabili</em>.",
        "values": [
            ("Tempo",        "Dodici ore minime di lievitazione · sedici per il sabato."),
            ("Filiera",      "Sedici fornitori, tutti visitati di persona almeno una volta."),
            ("Trasparenza",  "Niente miscele, niente miglioratori, niente surgelati."),
            ("Mano",         "Decorazione a mano · cremerie alla minuta · niente stampo industriale."),
        ],

        "cta_heading": "Vuoi vedere la <em>pasticceria della settimana in corso?</em>",
        "cta_menu": "Cinque lievitati di ottobre '26",
        "cta_prenota": "Pre-ordina la sfoglia del sabato",
    },

    # ─── PASTICCERIA (menu) — Gusto's "menu" page ────────────
    "pasticceria": {
        "eyebrow":  "La carta della settimana",
        "headline": "Vetrina viva — <em>autunno '26</em>",
        "intro":
            "La pasticceria Madou cambia ogni settimana secondo il forno "
            "del lunedì notte. Quanto segue è la carta in vigore dal 6 al "
            "12 ottobre 2026 · vetrina aperta dal martedì al sabato, "
            "domenica solo mattina, lunedì riposo.",
        "courses_label": "Cinque lievitati · ottobre '26",

        "courses": [
            ("I",     "Croissant viennoise",
             "Pasta sfoglia lievitata 12 ore · burro normanno AOP Isigny · "
             "64 strati visibili al taglio · spennellata di tuorlo a uovo "
             "intero · zucchero a velo di Mothia spruzzato all'uscita dal forno.",
             "Caffè monorigine Etiopia Sidamo · Caffè Vergnano per Madou"),
            ("II",    "Maritozzo con la panna",
             "Pasta brioche lievitata 24 ore con M-3 · panna fresca della "
             "latteria Inalpi montata alla minuta · vaniglia Tahitian intera "
             "di Madagascar · zucchero filato a corona.",
             "Cioccolata calda Madagascar Domori 72%"),
            ("III",   "Millefoglie alla nocciola",
             "Tre strati di sfoglia caramellata · crema chantilly alla "
             "nocciola Piemonte IGP del Mulino Brero · granella di nocciola "
             "tostata sul piano refrattario.",
             "Bicerin tradizionale torinese · ricetta storica caffè Al Bicerin"),
            ("IV",    "Bignè al cioccolato Domori",
             "Pasta choux della casa · ganache fondente cacao Criollo "
             "Domori 80% · lucidatura allo sciroppo di glucosio · "
             "guarnizione a punta · zucchero a velo a piacere.",
             "Tè nero Darjeeling First Flush · selezione Damman 2026"),
            ("V",     "Saint Honoré ai marroni",
             "Solo autunno · bignè ripieni di crema mousseline al marrone · "
             "marroni IGP di Cuneo del campo di Anna Negroni · pasta sfoglia "
             "alla base · zucchero filato a corona dorata.",
             "Erbaluce di Caluso passito · selezione Cieck · 50 cl in mescita"),
            ("VI",    "Mont-Blanc 2026",
             "Vermicelli di castagne IGP del Mortara · crema chantilly "
             "vaniglia · cuore di meringa francese cotta a 90°C per "
             "quattro ore · finitura a passamano.",
             "Caffè turco al cardamomo verde · servizio in caffettiera di rame"),
            ("VII",   "Tarte au chocolat Sambirano",
             "Pasta frolla al cacao 22% · ganache fondente Madagascar "
             "Sambirano 72% · sale di Mothia a scaglie · finitura "
             "a olio extravergine di Taggia.",
             "—"),
            ("VIII",  "Macarons stagione",
             "Sei macarons stagionali · zafferano dell'Abruzzo, lampone "
             "del Roero, castagna di Cuneo, cioccolato Sambirano, vaniglia "
             "Tahitian, oliva taggiasca · cottura a 165°C per 12 minuti.",
             "Tè bianco Pai Mu Tan · selezione Damman"),
        ],

        # Wine_program → repurposed as caffè & tisaneria
        "wine_intro_title": "Caffetteria & tisaneria",
        "wine_intro":
            "Da Madou si abbina ogni lievitato con un caffè monorigine "
            "tostato a Torino da Vergnano o una tisana selezionata da "
            "Damman. La carta dei tè e dei caffè è completa, gli "
            "abbinamenti sono a discrezione del banco — chiedete a "
            "Tommaso al passaggio in cassa.",

        "wine_highlights": [
            ("Caffè monorigine", "8 origini · Etiopia, Brasile, Colombia, Guatemala, Vietnam, Sambirano"),
            ("Tè neri & verdi",  "22 selezioni Damman · Darjeeling, Ceylon, Sencha, Genmaicha"),
            ("Cioccolate calde", "6 origini · Madagascar, Venezuela, Ecuador, Dominicana, Tanzania, Ghana"),
            ("Bevande tradizionali", "Bicerin · vin brulé alla cannella · ponce alla mandarina · zabaione"),
        ],

        "footer":
            "Vetrina aperta dal martedì al sabato · pre-ordine sabato "
            "consigliato dal mercoledì. La sfoglia del sabato si esaurisce "
            "regolarmente entro le 11:00. Per ordini superiori a 12 pezzi, "
            "scrivere a atelier@madou-pasticceria.it almeno 48 ore prima.",
    },

    # ─── VETRINA (gallery) — Gusto's "atmosfera" ─────────────
    "vetrina": {
        "eyebrow":  "La vetrina",
        "headline": "Quindici metri di vetrina, <em>una vetrina sola.</em>",
        "intro":
            "Madou occupa una ex-tipografia di Via Sant'Ottavio · la "
            "vetrina è aperta sulla strada per quindici metri lineari e "
            "lascia vedere tutto il laboratorio. Niente parete fra "
            "il forno e il marciapiede di Borgo Po.",

        "rooms": [
            ("La vetrina di strada",
             "Quindici metri di vetrina lungo Via Sant'Ottavio · "
             "esposizione a doppio livello · refrigerazione a +4°C "
             "per le cremerie · vetrina secca a +18°C per i lievitati."),
            ("La sala di lavoro a vista",
             "L'atelier vero — quattro postazioni: laminato, lievitati, "
             "cremerie, decorazione. Tutta la pasticceria si vede "
             "in tempo reale dalla vetrina · niente cucina nascosta."),
            ("La sala di degustazione",
             "Otto coperti al banco, di fronte al laminatoio. Aperta "
             "solo per le degustazioni guidate del giovedì pomeriggio · "
             "tre ore con Carla, sei lievitati, tre caffè monorigine."),
            ("Il cortile dell'ex-tipografia",
             "Da maggio a settembre, quattro tavoli en plein air sotto "
             "il glicine dell'ex-tipografia. Aperti solo a colazione · "
             "menu fisso del lunedì, croissant + bicerin."),
        ],

        "captions": [
            "La vetrina del sabato mattina · esposizione 7:30.",
            "Decorazione a mano · wedding cake autunno '26.",
            "I croissant alla viennoise appena sfornati alle 6:00.",
            "I macarons di ottobre '26 · sei gusti stagionali.",
            "Carla Madou al laminatoio · pasta sfoglia delle 5:30.",
            "Il banco al passaggio del primo cliente · martedì 7:30.",
        ],

        "cta_quote": "«Niente parete fra il forno e il marciapiede di Borgo Po.»",
        "cta_desc": "Vetrina aperta Mar – Sab · 7:30 – 19:30 · Dom 7:30 – 13:00 · Lun riposo.",
        "cta_primary": "Pre-ordina la sfoglia del sabato",
        "cta_secondary": "Vedi tutta la pasticceria",
    },

    # ─── DIARIO (blog list / detail) ──────────────────────────
    "diario": {
        "eyebrow":  "Il diario di farina",
        "headline": "Note di forno, <em>di lievito,</em> di laboratorio.",
        "intro":
            "Brevi appunti di Carla Madou e Tommaso Rinaldi sulle "
            "lievitazioni in corso, sulle materie prime stagionali, "
            "sui pasticci più belli e su quello che non sta funzionando "
            "in pasticceria di settimana in settimana.",
        "read_article": "Leggi l'articolo",
        "min_label": "min",
        "min_read_label": "min di lettura",
        "crumb_label": "Diario",
        "back_link": "← Tutto il diario",
        "footer_label": "Madou Pasticceria Atelier · Il diario di farina",
        "empty_body": [
            "Articolo in preparazione editoriale. La pubblicazione integrale "
            "sarà disponibile a breve, scritta personalmente dalla pasticciera "
            "o dal maestro lievitista.",
            "Questo segnaposto descrive la voce del Diario di Farina: brevi "
            "note di lavoro, riflessioni sui lieviti madre, racconti di "
            "lievitazioni che vanno male. Mai più di duemila parole, mai "
            "meno di cinquecento.",
        ],
    },

    "posts": [
        {
            "slug":     "vetrina-autunno-26",
            "kicker":   "Vetrina in corso",
            "title":    "Le cinque idee della vetrina autunno '26",
            "date":     "6 ottobre 2026",
            "read_min": 5,
            "author":   "Carla Madou",
            "lede":
                "La nuova carta è entrata in vetrina ieri notte. Cinque "
                "lievitati, due rivisitazioni di classici di pasticceria "
                "torinese e una pasta sfoglia che ho rincorso per tre anni.",
            "body": [
                ("p", "Costruire una vetrina autunnale è meno una questione "
                      "di ricette e più una questione di tempi di "
                      "lievitazione. La temperatura della cella scende, "
                      "i lieviti rallentano · le madri rispondono più "
                      "lentamente. Per la carta autunno '26 abbiamo lavorato "
                      "due settimane solo sui tempi di riposo del Saint "
                      "Honoré ai marroni."),
                ("h2", "Le cinque idee nuove"),
                ("p", "Il primo lievitato, il Saint Honoré ai marroni di "
                      "Cuneo, è una rilettura del Saint Honoré classico "
                      "francese fatta su tre materie prime piemontesi: "
                      "marroni di Cuneo IGP del campo di Anna Negroni, "
                      "panna fresca della latteria Inalpi e pasta sfoglia "
                      "al burro normanno. Ne avevo voglia dal 2022, da "
                      "quando ero passata da Lione e avevo assaggiato "
                      "quello di Cyril Lignac · ma volevo una versione "
                      "torinese, non parigina."),
                ("h2", "Le rivisitazioni"),
                ("p", "Il Mont-Blanc 2026 e il maritozzo con la panna sono "
                      "due dolci ai quali sto lavorando da sette anni · "
                      "nessuno dei due nasce ad ottobre, ma è in ottobre "
                      "che le rispettive materie prime entrano al loro "
                      "meglio: i marroni di Mortara per il primo, la "
                      "panna autunnale per il secondo. Il maritozzo, in "
                      "particolare, l'ho cambiato sette volte in dodici "
                      "mesi. Adesso è giusto."),
                ("h2", "Una pasta sfoglia"),
                ("p", "Il croissant alla viennoise è il pezzo di cui sono "
                      "più orgogliosa di questa carta. È una pasta sfoglia "
                      "lievitata 12 ore in cella a +4°C, con burro Isigny "
                      "AOP battuto a freddo e farina del mulino Brero. "
                      "Sessantaquattro strati visibili al taglio, una "
                      "bolla d'aria ogni 0.4 millimetri di pasta. È il "
                      "lievitato a cui sono arrivata dopo otto anni di "
                      "tentativi, e l'unica ragione per cui sono qui."),
                ("h2", "Cosa esce sabato"),
                ("p", "Il sabato Madou produce 220 croissant alla viennoise "
                      "che si esauriscono regolarmente entro le 11:00. "
                      "Il pre-ordine dal giovedì è quindi caldamente "
                      "consigliato — soprattutto da ottobre, quando la "
                      "domanda torna a salire con il primo freddo."),
            ],
        },
        {
            "slug":     "lievito-madre-m2",
            "kicker":   "Lievito madre",
            "title":    "Perché abbiamo aspettato sette anni prima di fare il panettone",
            "date":     "28 settembre 2026",
            "read_min": 6,
            "author":   "Tommaso Rinaldi",
            "lede":
                "Madou ha messo in carta il panettone solo nel 2018, sette "
                "anni dopo l'apertura. La ragione è una sola: la madre M-2 "
                "non era pronta. Ecco perché.",
            "body": [
                ("p", "Il panettone richiede una madre madre · molti pasticcieri "
                      "si fanno la madre quando aprono la pasticceria, ma per "
                      "il panettone di alta gamma serve una madre che abbia "
                      "lavorato almeno tre anni, sviluppato il suo profilo "
                      "acetico, trovato il suo equilibrio. La M-1 di Madou — "
                      "fondata nel 2011 — era una madre lattica, perfetta per "
                      "la sfoglia ma poco aggressiva per il panettone."),
                ("h2", "Come nasce la M-2"),
                ("p", "Nel 2014 ho preso un pezzo da 200 grammi di M-1 e l'ho "
                      "rinfrescata a triplo per quaranta giorni · ogni dodici "
                      "ore, sempre. È così che si \"vira\" una madre lattica "
                      "verso un profilo misto · è un processo che ho imparato "
                      "da Achille Zoia. Dopo i quaranta giorni, la madre era "
                      "diventata abbastanza acetica per il panettone, ma "
                      "ancora troppo giovane."),
                ("h2", "Quattro anni di attesa"),
                ("p", "Dal 2014 al 2018 ho rinfrescato la M-2 ogni dodici "
                      "ore senza saltare una sola volta · neanche a Natale, "
                      "neanche in agosto. Carla la chiamava \"la madre del "
                      "futuro\" perché non la usavamo mai. Nel novembre 2018, "
                      "alla settima prova, il panettone è uscito come "
                      "doveva uscire. Da allora la M-2 produce solo "
                      "panettone, colomba e veneziana, niente altro."),
            ],
        },
    ],

    # ─── ORDINA (reservations) — Gusto's "prenota" ────────────
    "ordina": {
        "eyebrow":      "Ordini & commesse",
        "headline":     "Pre-ordina la sfoglia del sabato.",
        "intro":
            "La vetrina del sabato si esaurisce regolarmente entro le 11:00. "
            "Per assicurarsi i lievitati, conviene pre-ordinare dal "
            "mercoledì · ritiro al banco dalle 7:30 alle 13:00. Per torte "
            "su commessa e wedding cake, scrivere a atelier@madou-"
            "pasticceria.it almeno due settimane prima.",
        "primary_label":   "Cosa vuoi pre-ordinare?",
        "primary_placeholder": "Sabato 18 ottobre · 12 croissant alla viennoise + 4 maritozzi · ritiro alle 9:30",
        "name_label":      "Nome e cognome",
        "phone_label":     "Telefono",
        "email_label":     "Email",
        "submit_label":    "Invia il pre-ordine",
        "submit_note":     "Riceverai conferma dal banco entro 24 h. Il pre-ordine si paga al ritiro.",

        "contact_block": {
            "address_label": "Atelier",
            "address":       "Via Sant'Ottavio 36 · 10124 Torino · Borgo Po",
            "phone_label":   "Banco",
            "phone":         "+39 011 8195 770",
            "email_label":   "Email",
            "email":         "atelier@madou-pasticceria.it",
            "hours_label":   "Orari",
            "hours_list": [
                "Mar – Sab · 7:30 – 19:30",
                "Dom · 7:30 – 13:00",
                "Lun · riposo",
            ],
        },

        "policy_label": "Note di pre-ordine",
        "policy_paragraphs": [
            "Il pre-ordine sabato si chiude il venerdì alle 18:00. Oltre "
            "quell'ora, accettiamo solo se la produzione del giorno lo permette.",
            "Per ordini superiori a 12 pezzi, contattare il banco direttamente. "
            "Per le wedding cake, due settimane minime di anticipo · per il "
            "cake design, tre settimane.",
            "Le materie prime tracciate (burro Isigny, cacao Sambirano, marroni "
            "IGP, nocciole IGP) seguono il calendario stagionale. In caso di "
            "rottura di stock, vi proponiamo una variante coerente.",
        ],

        "small_print":
            "Madou Atelier S.r.l. · P. IVA 11237680016 · Via Sant'Ottavio 36, "
            "10124 Torino · Pasticceria Atelier dal 2011.",
    },
}
