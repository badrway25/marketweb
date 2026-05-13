"""Podere Le Querce — Tuscan family agriturismo (artisan-workshop · IT).

T59 · Wave 2 Pass-3 (2026-05-13) · 3rd reuse of artisan-workshop
archetype after Bottega + Sapori (D-051 Option A · zero new HTML
files). 2nd cross-category reuse after Albergo (skin lives at
ecommerce/, template lives at travel/ · `skin_source_category`
DNA field required).

Voice contract (IT):
- Editorial-rural register: Touring Club Italiano · Bell'Italia ·
  Slow Food editorial · Vie del Gusto · Gambero Rosso campagna.
  Familiar warmth (the family hosts you for a long lunch · `voi`
  plural across the contact band, `Lei` in form-helper text).
- Voice anchor `ospitalità contadina` — the Tuscan-rural register
  that foregrounds the multigenerational-family-hosts-you promise.
  Load-bearing in headline, atelier.statement_heading, soggiorno
  band CTAs, journal kicker, contatti faq.
- Vocabolario: podere · agriturismo · famiglia · contadino · vendemmia
  · raccolta · oliveto · vigna · orto · forno · stalla · cantina ·
  cucina · ospitalità · tavolata. Mai: resort · all-inclusive · spa
  cinque-stelle · check-in immediato · booking-engine.
- Concrete detail: Greve in Chianti · Chianti Classico DOCG · cinta
  senese · raccolta olive novembre · vendemmia settembre · Antinori
  (storica proprietà · 1934 atto di vendita ai bisnonni Pasquinelli
  documentato in archivio comunale) · Famiglia Pasquinelli (Maria
  classe 1962 matriarca · Carlo marito · Giovanni 35 cuoco · Anna
  32 orto e ospitalità) · 8 prodotti del podere venduti in dispensa.

Differentiation contract vs Bottega + Sapori (D-054 enforcement):
- Bottega è artisan-workshop tipografico-warm con Toscano-leather:
  Severino Falchi e Caterina Lippi · cuoio + ceramica + tessuti ·
  "fatto a mano" voice anchor · "phone-and-whatsapp" CTA. Macro
  tone: artigiano-fabbricazione.
- Sapori è artisan-workshop terroir-curatoriale con Langhe-wine:
  Brezza/Vajra/Boasso/Brovia · vino + tartufo + castelmagno ·
  "vignaiolo indipendente" voice anchor · "case-order-and-visit" CTA.
  Macro tone: sommelier-pacato.
- Podere Le Querce è artisan-workshop rural-hospitality con Chianti-
  family: Famiglia Pasquinelli matriarchi-multigenerazionali ·
  agriturismo + oliveto + vigna + dispensa contadina · "ospitalità
  contadina" voice anchor · "stay-and-take-home" CTA (la cassa del
  podere arriva a casa dopo il soggiorno). Macro tone: famiglia-che-
  ospita-famiglia.
- Palette: Bottega walnut #3E2723 + cream #D7CCC8 + orange #FF8F00;
  Sapori bordeaux #4A1E1F + travertino #F2E9D8 + olivo #6B7E47;
  Podere deep oak-green #3A4B2E + wheat-cream #E8DCB8 + harvest-
  copper #B8651F. ZERO overlap on primary across the 3 reuses.
- Typography: Bottega Libre Baskerville + Nunito Sans (warm-trattoria
  editorial); Sapori IBM Plex Serif + IBM Plex Sans (editorial-
  tipografico); Podere EB Garamond + Source Sans 3 (historical-
  Italian editorial · most classico of the three · matches Antinori-
  era heritage register).

Contract compliance — see factory/standards/artisan-workshop-shape-
contract.md (T58). All 22 checklist items in §9 of that contract
were verified at write time. Specifically the 4 T53-caught bugs
+ 2 silent-drift bugs (process_steps 5-key dict · faq_items q/a
dict) are avoided here.
"""
from __future__ import annotations

from typing import Any


# Interim Unsplash CC0 imagery pool · travel-agriturismo signal.
# X.5 curator pack `agriturismo.md` pending — these 6 URLs cover
# the load-bearing roles: hero podere golden hour · oliveto · vigna ·
# tavolata in cortile · cucina contadina · the family in the kitchen.
_PODERE_HERO = "https://images.unsplash.com/photo-1602941525521-46f6f1ab39ce?w=1600&q=80&auto=format&fit=crop"
_OLIVETO = "https://images.unsplash.com/photo-1567416661576-d8b6e92e63d2?w=1200&q=80&auto=format&fit=crop"
_VIGNA_CHIANTI = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_TAVOLATA = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200&q=80&auto=format&fit=crop"
_CUCINA_CONTADINA = "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=1200&q=80&auto=format&fit=crop"
_FAMIGLIA_PORTRAIT = "https://images.unsplash.com/photo-1573497019418-b400bb3ab074?w=1200&q=80&auto=format&fit=crop"
_OLIO_BOTTLE = "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=1200&q=80&auto=format&fit=crop"
_VINO_BOTTLE = "https://images.unsplash.com/photo-1474722883778-792e7990302f?w=1200&q=80&auto=format&fit=crop"
_VINSANTO = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_MIELE = "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=1200&q=80&auto=format&fit=crop"
_MARMELLATA = "https://images.unsplash.com/photo-1535990379313-50d1f6fc0c4f?w=1200&q=80&auto=format&fit=crop"
_PECORINO = "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=1200&q=80&auto=format&fit=crop"
_SALAME = "https://images.unsplash.com/photo-1599379892470-bbe1eb01ea75?w=1200&q=80&auto=format&fit=crop"
_CANTUCCI = "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_MARIA = "https://images.unsplash.com/photo-1559963110-71b394e7494d?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CARLO = "https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_GIOVANNI = "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_ANNA = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_PRODUCER = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"


PODERE_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Il podere",       "kind": "home"},
        {"slug": "dispensa",  "label": "La dispensa",     "kind": "shop"},
        {"slug": "prodotto",  "label": "Il prodotto",     "kind": "product"},
        {"slug": "famiglia",  "label": "La famiglia",     "kind": "about"},
        {"slug": "diario",    "label": "Diario di campagna","kind": "journal"},
        {"slug": "soggiorno", "label": "Soggiorno",       "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":    "Q",
        "logo_word":       "Podere Le Querce",
        "tag":             "Agriturismo di famiglia · Greve in Chianti · dal 1934",
        "phone":           "+39 055 853 261",
        "whatsapp":        "+39 339 458 1126",
        "whatsapp_link":   "https://wa.me/393394581126",
        "email":           "famiglia@podereleQuerce.it",
        "address":         "Località Le Querce 14 · 50022 Greve in Chianti · Firenze",
        "hours_compact":   "Aperto tutto l'anno · cucina su prenotazione 12:30 e 19:30",
        "hours_footer_rows": [
            "Ricevimento ospiti 8-22 · Maria in cucina dalle 7",
            "Dispensa aperta tutti i giorni 9-19 · domenica chiusa",
        ],
        "license":         "Codice CITRA 048-029-001 · Iscr. CCIAA Firenze 354210 · Az. Agricola Pasquinelli S.S.",
        "footer_intro":
            "Podere Le Querce è un'azienda agricola di famiglia a Greve in Chianti · "
            "13 ettari di terreno con oliveto storico, vigna di Sangiovese, orto, "
            "stalla di cinta senese, cantina e quattro camere di ospitalità rurale. "
            "Lavoriamo tutto in casa: olio, vino, miele, salami, pasta, cantucci. "
            "La famiglia Pasquinelli vive qui dal 1934. Quando venite ospiti, "
            "mangiate alla nostra tavola.",

        # Nav CTA — agriturismo-flavoured
        "nav_cta":         "Prenotate il soggiorno",
        "nav_cta_kind":    "appointment",

        # Footer labels
        "foot_studio":     "Il podere",
        "foot_pages":      "Mappa",
        "foot_contact":    "Soggiorno",
        "foot_stockists":  "Dove ci trovate",
        "stockists_rows": [
            "Mercato della Terra · Greve in Chianti · domenica mattina",
            "Slow Food Firenze · banco mensile",
            "Spedizione casa · Italia 24-48h · Europa 4-6 giorni",
            "Dispensa in podere · aperto al pubblico tutti i giorni 9-19",
        ],

        # Currency + product labels (used on shop cards + product page)
        "currency_symbol":   "€",
        "shop_filter_label": "Affina la dispensa",
        "shop_count_unit":   "prodotti del podere",
        "edition_label":     "Annata",
        "made_in_label":     "Prodotto a",
        "artisan_label":     "Mani di",
        "material_label":    "Materia prima",
        "shipping_label":    "Spedizione",
        "shipping_value":    "24-48h in Italia · spedizione refrigerata estate",
        "guarantee_label":   "Garanzia del podere",
        "guarantee_value":   "Sostituiamo gratuitamente ogni bottiglia rotta o difettata · entro 30 giorni",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Agriturismo · Greve in Chianti · dal 1934",
        "headline": "Quattro generazioni in un podere. <em>Ospitalità contadina</em>, tutto l'anno.",
        "intro":
            "Podere Le Querce è la casa della famiglia Pasquinelli dal 1934, quando "
            "i bisnonni Mario e Annetta l'acquistarono dalla famiglia Antinori con un "
            "atto di vendita conservato in comune. Oggi è un agriturismo con quattro "
            "camere, una cucina di famiglia con tavolata su prenotazione, e una "
            "dispensa contadina con i nostri otto prodotti.",

        "primary_cta":          "Prenotate il soggiorno",
        "primary_href":         "soggiorno",
        "secondary_cta":        "Visitate la dispensa",
        "secondary_href":       "dispensa",

        # Stamp panel — list[4] of tuple[2]
        "stamp_label":   "Il podere in quattro righe",
        "stamp_heading": "Quattro generazioni · una sola tavolata.",
        "stamp_rows": [
            ("Anno",              "1934 · atto di vendita Antinori → Pasquinelli"),
            ("Famiglia",          "Maria + Carlo + Giovanni + Anna · 4 alla guida"),
            ("Ettari",            "13 ettari · oliveto + vigna + orto + stalla"),
            ("Camere",            "4 camere · ospitalità rurale aperta tutto l'anno"),
        ],
        "stamp_footer":      "Mercato della Terra Greve · Slow Food Firenze · Spedizione casa Italia 24-48h",
        "stamp_corner_index": "Stagione",
        "stamp_corner_word":  "2026",

        # Latest items — list[4] of dict[8 keys=edition,id,image,meta,n,name,price,tag]
        "latest_label":       "Nella dispensa",
        "latest_heading":     "Otto prodotti del podere, sempre disponibili.",
        "latest_link_label":  "Tutti i prodotti",
        "latest_link_href":   "dispensa",
        "latest_items": [
            {
                "id":      "olio-evo-podere-2025",
                "n":       "N° 01",
                "image":   _OLIO_BOTTLE,
                "edition": "Raccolta 2025",
                "name":    "Olio EVO del Podere",
                "meta":    "Moraiolo + Frantoio + Leccino · 2.400 piante",
                "price":   "€ 28 / 500 ml",
                "tag":     "Nuovo · raccolta novembre",
            },
            {
                "id":      "chianti-classico-2022",
                "n":       "N° 02",
                "image":   _VINO_BOTTLE,
                "edition": "Vendemmia 2022",
                "name":    "Chianti Classico DOCG",
                "meta":    "Sangiovese 95% · 1,8 ha di vigna",
                "price":   "€ 22 / bottiglia",
                "tag":     "Cantina del podere",
            },
            {
                "id":      "miele-millefiori",
                "n":       "N° 04",
                "image":   _MIELE,
                "edition": "Estrazione luglio 2025",
                "name":    "Miele millefiori",
                "meta":    "12 arnie · radura di castagno",
                "price":   "€ 14 / 250 g",
                "tag":     "Cento per cento podere",
            },
            {
                "id":      "salame-cinta-senese",
                "n":       "N° 07",
                "image":   _SALAME,
                "edition": "Stagionatura 9 mesi",
                "name":    "Salame di Cinta Senese",
                "meta":    "Suini neri allevati allo stato semi-brado",
                "price":   "€ 38 / pezzo intero",
                "tag":     "8 capi in stalla",
            },
        ],

        # Makers — list[4] of dict[6 keys=craft,name,place,portrait,quote,since]
        # NB: in agriturismo register `makers` are local producers
        # whose products complete the table when family production
        # alone is not enough — pastore, mugnaio, norcino, monastero.
        "makers_label":   "I produttori del territorio",
        "makers_heading": "Quattro mani che completano la nostra tavola.",
        "makers_intro":
            "I prodotti del podere non bastano per la tavola di tutti gli "
            "ospiti · da quattro generazioni la famiglia Pasquinelli si "
            "appoggia agli stessi produttori del territorio. Tutti a meno "
            "di trenta chilometri.",
        "makers": [
            {
                "craft":    "Pastore · pecorino di latte crudo",
                "name":     "Andrea Falleri",
                "place":    "Lamole · 4 km dal podere",
                "since":    "Cliente della famiglia dal 1987",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "I Pasquinelli mi prendono il pecorino di Lamole da quando "
                    "ero ragazzo. Mio nonno lo dava al loro padre, e adesso io "
                    "lo do a Maria. È il modo in cui le cose si tramandano qui.",
            },
            {
                "craft":    "Mugnaio · grano duro Maremma",
                "name":     "Famiglia Bartoletti",
                "place":    "Roccastrada · 28 km dal podere",
                "since":    "Mulino della famiglia dal 1820",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Maciniamo il grano duro Senatore Cappelli a pietra · "
                    "Maria ne fa la pasta per la tavolata domenicale. Il "
                    "sapore di farina antica è il sapore della loro pasta.",
            },
            {
                "craft":    "Norcino · salami cinta senese",
                "name":     "Davide Pieri",
                "place":    "Castelfiorentino · 22 km dal podere",
                "since":    "Norcineria di famiglia dal 1958",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Il padre di Maria mi insegnò a tagliare il maiale a "
                    "regola d'arte nel 1972. Adesso che Maria alleva i cinti "
                    "senesi del podere, gli salami glieli lavoro io.",
            },
            {
                "craft":    "Monastero · marmellata di cotognata",
                "name":     "Suore di San Vivaldo",
                "place":    "Montaione · 18 km dal podere",
                "since":    "Monastero attivo dal XV secolo",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Le sorelle del monastero fanno la cotognata come la "
                    "facevano nel Quattrocento · cinque ore di cottura a "
                    "fuoco lento. Maria la mette in tavola con il pecorino.",
            },
        ],

        # Provenance items — list[4] of dict[4 keys=icon,title,desc,place]
        "provenance_label":   "Il podere",
        "provenance_heading": "Tredici ettari, quattro produzioni.",
        "provenance_intro":
            "Il podere conta 13 ettari coltivati direttamente dalla famiglia "
            "Pasquinelli. Quattro produzioni storiche · oliveto, vigna, orto, "
            "stalla · sono ancora gestite con i ritmi che Maria ha imparato "
            "dal padre.",
        "provenance_items": [
            {
                "icon":  "🌿",
                "title": "Oliveto storico",
                "desc": "2.400 piante di moraiolo, frantoio e leccino · alcune piante hanno più di 200 anni · raccolta a mano in novembre · spremitura a freddo entro 8 ore.",
                "place": "8 ettari sul versante sud-est del podere",
            },
            {
                "icon":  "🍇",
                "title": "Vigna di Sangiovese",
                "desc": "1,8 ettari di Sangiovese (95%) con piccole quote di Canaiolo e Colorino · vendemmia manuale a fine settembre · vinificazione in cantina della famiglia · imbottigliamento entro maggio.",
                "place": "1,8 ettari sul versante ovest · 380 m s.l.m.",
            },
            {
                "icon":  "🥕",
                "title": "Orto della cucina",
                "desc": "1 ettaro di orto stagionale · pomodori San Marzano, fagioli zolfini, zafferano, erbe officinali · niente prodotti acquistati per la tavola di Maria salvo i limoni d'inverno.",
                "place": "1 ettaro accanto alla casa colonica",
            },
            {
                "icon":  "🐖",
                "title": "Stalla di cinta senese",
                "desc": "8 capi di cinta senese (suino nero) allevati allo stato semibrado · alimentazione con ghianda dal bosco del podere e farro dell'orto · macellazione locale due volte l'anno.",
                "place": "2,2 ettari di bosco con stalla coperta",
            },
        ],

        # Care items — list[4] of tuple[2] · the four ospitalità promises
        "care_label":   "Le quattro promesse di casa",
        "care_heading": "Ospitalità contadina: poche regole, sempre rispettate.",
        "care_items": [
            ("Tavolata sempre con Maria",
             "Ogni cena è preparata e portata in tavola da Maria. Quando si "
             "siede con voi, è perché ha finito di servire — non per "
             "intrattenervi."),
            ("Niente check-in automatico",
             "Carlo o Giovanni vi accolgono al cancello e vi accompagnano "
             "alla camera. La chiave è una chiave vera, di ferro, con il "
             "nome della camera. Niente schede magnetiche."),
            ("Colazione fino alle 10:30",
             "Pane di Lorenzini caldo dal forno del podere · marmellate "
             "delle sorelle di San Vivaldo · miele dell'arnia · uova "
             "delle galline · caffè della miscela storica del podere."),
            ("Spedizione casa dopo il soggiorno",
             "Quando partite, la dispensa vi prepara una cassa di sei "
             "prodotti del podere a vostra scelta. Spediamo a casa entro "
             "una settimana · costo a parte solo della spedizione."),
        ],

        # Press strip — list[5] of scalar str (NOT dicts per contract)
        "press_label":   "Rassegna del podere",
        "press_items": [
            "Slow Food Firenze",
            "Bell'Italia · Toscana rurale",
            "Touring Club Italiano",
            "Gambero Rosso · Agriturismi 2025",
            "Vie del Gusto · Chianti Classico",
        ],

        # Journal teaser
        "journal_teaser_label":   "Dal diario di campagna",
        "journal_teaser_heading": "Tre voci da Greve in Chianti.",
        "journal_teaser_link":    "Leggi il diario",
        "journal_teaser_href":    "diario",

        # Final CTA
        "cta_label":          "Per prenotare la tavolata",
        "cta_heading":        "<em>Quattro camere</em>, una sola tavolata, una sola famiglia.",
        "cta_intro":
            "Le quattro camere del podere si prenotano direttamente con Maria "
            "tramite WhatsApp o telefono. La tavolata della cena si prenota "
            "all'arrivo · cuciniamo per quanti siete.",
        "cta_primary":        "Scrivete a Maria su WhatsApp",
        "cta_primary_href":   "soggiorno",
        "cta_secondary":      "Telefono diretto in cucina",
    },

    # ─── DISPENSA (shop · 8 farm products) ─────────────────────
    "dispensa": {
        "eyebrow":             "La dispensa contadina",
        "headline":            "Otto prodotti del podere · spedizione casa Italia 24-48h.",
        "intro":
            "La dispensa è la prosecuzione naturale della cucina di Maria: "
            "i prodotti che mangiate in tavola quando siete ospiti, li trovate "
            "qui per portarveli a casa. Spedizione refrigerata estate, "
            "cassa di legno timbrato a marchio del podere.",
        "filter_section_label": "Affina la dispensa",
        "filter_groups": [
            {
                "label":   "Produzione",
                "options": ["Olio EVO", "Vino", "Conserve", "Salumi", "Pasta · pane · dolci"],
            },
            {
                "label":   "Stagione",
                "options": ["Raccolta 2025", "Vendemmia 2022-2024", "Estrazione luglio", "Stagionatura lunga", "Sempre disponibili"],
            },
            {
                "label":   "Cassa di legno",
                "options": ["Cassa da 6 prodotti · scelta libera", "Cassa olio + vino", "Cassa colazione (miele + marmellata + cantucci)", "Cassa salumi"],
            },
        ],
        "sort_label":      "Ordina",
        "sort_options": [
            "Per produzione",
            "Per stagione",
            "Per stagionatura",
            "Per disponibilità",
        ],
        "result_count":    "8 prodotti del podere nella dispensa",
        "result_subtitle": "Sei a marchio del podere + due dai produttori del territorio · spedizione casa Italia 24-48h.",
        "featured_product_id": "olio-evo-podere-2025",

        # 8 products — full dict shape (11 keys per contract)
        "products": [
            {
                "id":         "olio-evo-podere-2025",
                "n":          "N° 01",
                "image":      _OLIO_BOTTLE,
                "edition":    "Raccolta 2025",
                "name":       "Olio EVO del Podere",
                "meta":       "Moraiolo 60% + Frantoio 25% + Leccino 15% · spremitura a freddo entro 8 ore dalla raccolta",
                "place":      "Greve in Chianti",
                "artisan":    "Maria + Carlo Pasquinelli",
                "price":      "€ 28 / 500 ml",
                "tag":        "Raccolta novembre",
                "available":  True,
            },
            {
                "id":         "chianti-classico-2022",
                "n":          "N° 02",
                "image":      _VINO_BOTTLE,
                "edition":    "Vendemmia 2022",
                "name":       "Chianti Classico DOCG",
                "meta":       "Sangiovese 95% · Canaiolo 4% · Colorino 1% · botte grande + 6 mesi bottiglia",
                "place":      "Vigna del podere · 1,8 ha · 380 m s.l.m.",
                "artisan":    "Giovanni Pasquinelli · enologo del podere",
                "price":      "€ 22 / 750 ml",
                "tag":        "Cantina del podere",
                "available":  True,
            },
            {
                "id":         "vin-santo-2018",
                "n":          "N° 03",
                "image":      _VINSANTO,
                "edition":    "Annata 2018 · affinamento 7 anni",
                "name":       "Vin Santo del Chianti",
                "meta":       "Malvasia bianca + Trebbiano · appassimento 4 mesi · caratelli da 50 litri di rovere",
                "place":      "Soffitta del podere · caratelli storici",
                "artisan":    "Carlo Pasquinelli · cantiniere",
                "price":      "€ 32 / 375 ml",
                "tag":        "Bottiglia mezza",
                "available":  True,
            },
            {
                "id":         "miele-millefiori",
                "n":          "N° 04",
                "image":      _MIELE,
                "edition":    "Estrazione luglio 2025",
                "name":       "Miele millefiori",
                "meta":       "12 arnie su radura di castagno · raccolta luglio · niente trattamenti chimici · niente alimentazione invernale",
                "place":      "Bosco del podere",
                "artisan":    "Anna Pasquinelli · apicoltrice",
                "price":      "€ 14 / 250 g",
                "tag":        "Cento per cento del podere",
                "available":  True,
            },
            {
                "id":         "marmellata-susine",
                "n":          "N° 05",
                "image":      _MARMELLATA,
                "edition":    "Lotto agosto 2025",
                "name":       "Marmellata di susine",
                "meta":       "Susine claudia gialla · zucchero 38% · niente pectina aggiunta · cottura a fuoco lento 4 ore",
                "place":      "Orto del podere · 3 piante storiche",
                "artisan":    "Maria Pasquinelli · cucina",
                "price":      "€ 9 / 280 g",
                "tag":        "Lotto piccolo",
                "available":  True,
            },
            {
                "id":         "pecorino-toscano-dop",
                "n":          "N° 06",
                "image":      _PECORINO,
                "edition":    "Stagionatura 6 mesi",
                "name":       "Pecorino Toscano DOP",
                "meta":       "Latte crudo di pecora · caglio naturale · stagionato in grotta · spazzolato a olio EVO del podere",
                "place":      "Lamole · 4 km dal podere",
                "artisan":    "Andrea Falleri · pastore",
                "price":      "€ 24 / forma piccola 600 g",
                "tag":        "Mani di Andrea",
                "available":  True,
            },
            {
                "id":         "salame-cinta-senese",
                "n":          "N° 07",
                "image":      _SALAME,
                "edition":    "Stagionatura 9 mesi",
                "name":       "Salame di Cinta Senese",
                "meta":       "Suini cinta senese del podere · allevamento semibrado · macellazione locale · stagionatura in cantina di pietra",
                "place":      "Stalla del podere + norcineria Pieri Castelfiorentino",
                "artisan":    "Davide Pieri · norcino",
                "price":      "€ 38 / pezzo intero 700 g",
                "tag":        "8 capi in stalla",
                "available":  True,
            },
            {
                "id":         "cantucci-mandorle",
                "n":          "N° 08",
                "image":      _CANTUCCI,
                "edition":    "Infornata settimanale",
                "name":       "Cantucci di mandorle",
                "meta":       "Mandorle non pelate · uova del podere · zucchero di canna · ricetta della nonna Annetta del 1948",
                "place":      "Forno del podere · cucina di Maria",
                "artisan":    "Maria Pasquinelli · cucina",
                "price":      "€ 12 / sacchetto 250 g",
                "tag":        "Ricetta di nonna Annetta",
                "available":  True,
            },
        ],

        "footer_note_label": "Spedizione e cassa",
        "footer_note":
            "Tutti i prodotti vengono spediti in cassa di legno marcata "
            "del podere · ordini sopra € 80 spedizione gratuita in Italia "
            "· altrimenti € 12 fisso. La cassa torna indietro a vostra "
            "discrezione · oppure resta come oggetto di cucina.",
    },

    # ─── PRODOTTO (product page · featured = Olio EVO 2025) ───
    "prodotto": {
        "id":           "olio-evo-podere-2025",
        "n":            "N° 01",
        "edition":      "Raccolta novembre 2025",
        "edition_note": "Annata 2025 limitata a 1.800 bottiglie · lotto 23/01",
        "name":         "Olio EVO del Podere",
        "subtitle":     "Moraiolo + Frantoio + Leccino · spremitura a freddo entro 8 ore",
        "price":        "€ 28 / bottiglia 500 ml",
        "vat_note":     "Iva inclusa · spedizione 24-48h in Italia",
        "intro":
            "L'olio del Podere Le Querce è il prodotto storico della casa · "
            "la famiglia Pasquinelli ha sempre venduto il proprio olio "
            "extravergine di oliva direttamente dai bisnonni Mario e "
            "Annetta. La raccolta 2025 è stata fatta a mano da una decina "
            "di persone (la famiglia più quattro stagionali) tra il 6 e "
            "il 19 novembre · spremitura a freddo entro otto ore.",

        # Gallery — list of scalar URL strings
        "gallery": [
            _OLIO_BOTTLE,
            _OLIVETO,
            _CUCINA_CONTADINA,
        ],

        "info_label": "Scheda tecnica",
        # info_rows — list[10] of tuple[2]
        "info_rows": [
            ("Cultivar",       "Moraiolo 60% · Frantoio 25% · Leccino 15%"),
            ("Raccolta",       "Manuale · 6-19 novembre 2025"),
            ("Spremitura",     "A freddo · entro 8 ore · 27 °C massima"),
            ("Acidità",        "0,18% · sotto la soglia di eccellenza"),
            ("Polifenoli",     "412 mg/kg · valore alto"),
            ("Bottiglia",      "Vetro scuro 500 ml · tappo a vite metallico"),
            ("Lotto",          "23/01 di 36 · etichetta numerata a mano"),
            ("Conservazione",  "Luogo fresco · al riparo dalla luce · entro 18 mesi"),
            ("Premi",          "Slow Food Presidio · Gambero Rosso 2 foglie 2025"),
            ("Disponibilità",  "1.800 bottiglie · disponibili fino a esaurimento"),
        ],

        "size_label":      "Formati disponibili",
        "size_intro":      "Bottiglia singola da 500 ml, cassa da 6 bottiglie con sconto del 12%, oppure latta da 3 litri per chi cucina molto.",
        # size_options — list[4] of SCALAR strings (per contract · NOT tuples)
        "size_options": [
            "Bottiglia 500 ml",
            "Cassa da 6 bottiglie · 500 ml",
            "Latta 3 litri",
            "Sacca regalo · 2 bottiglie + cantucci",
        ],
        "size_chart_link":   "Tutte le confezioni della dispensa",
        "size_chart_href":   "dispensa",

        "artisan_label":     "Mani di",
        "artisan_name":      "Maria + Carlo Pasquinelli",
        "artisan_role":      "Quarta generazione · al podere dal 1985",
        "artisan_bio":
            "Maria Pasquinelli (classe 1962) e Carlo Pasquinelli (classe "
            "1960) hanno preso le redini del podere nel 1985 dopo la "
            "morte di Mario, padre di Maria. Da allora curano l'oliveto "
            "in coppia · Carlo guida la raccolta a mano, Maria sovrintende "
            "la spremitura al frantoio cooperativo del Chianti. La famiglia "
            "non ha mai usato pesticidi sull'oliveto.",
        "artisan_portrait":  _PORTRAIT_MARIA,

        "buy_primary":       "Aggiungi alla cassa",
        "buy_secondary":     "Scrivete a Maria su WhatsApp",
        "buy_note":
            "Per ordini superiori a 12 bottiglie scrivete direttamente "
            "alla famiglia · vi confezioniamo una cassa speciale e "
            "calcoliamo lo sconto. Pagamento alla consegna in Italia, "
            "bonifico per Europa.",

        "care_label":  "Conservazione e uso",
        "care_intro":
            "L'olio del podere è un olio da consumare crudo · su pane caldo, "
            "fagioli, ribollita, bruschetta. Sconsigliato per fritture.",
        # care_items — list[5] of tuple[2]
        "care_items": [
            ("Temperatura",  "Conservare 14-18 °C · niente frigorifero · niente cucina calda"),
            ("Luce",         "Bottiglia di vetro scuro · proteggere comunque dalla luce diretta"),
            ("Consumo",      "Aperta · finire entro 4 mesi · poi sapore si attenua"),
            ("Sapidità",     "Verde, amaro e piccante in equilibrio · fruttato medio-intenso"),
            ("Abbinamento",  "Fagioli zolfini · pane senza sale · ribollita · bruschetta toscana"),
        ],

        "provenance_label":   "Dall'oliveto alla bottiglia",
        "provenance_heading": "Quattro passaggi a mano.",
        # provenance_steps — list[4] of 3-TUPLE (n, t, p) per contract
        "provenance_steps": [
            ("01", "Raccolta manuale",     "Sei al diciannove novembre 2025 · 10 persone · 6 settimane di raccolta a mano · cassette di plastica forata"),
            ("02", "Trasporto al frantoio", "Stesso giorno · entro 8 ore · 12 km al frantoio cooperativo del Chianti"),
            ("03", "Spremitura a freddo",  "27 °C massima · estrazione meccanica · niente acqua aggiunta · niente calore"),
            ("04", "Imbottigliamento",     "Marzo 2026 · al podere · bottiglia di vetro scuro 500 ml · lotto numerato a mano"),
        ],

        "related_label": "Altri prodotti del podere",
        "related_intro": "I prodotti della stessa stagione che completano la cassa.",
        # related_items — list[4] of dict[5 keys=image,n,name,meta,price]
        "related_items": [
            {
                "id":    "chianti-classico-2022",
                "n":     "N° 02",
                "image": _VINO_BOTTLE,
                "name":  "Chianti Classico DOCG · 2022",
                "meta":  "Vino della stessa annata storica · perfetto con la cassa olio",
                "price": "€ 22",
            },
            {
                "id":    "miele-millefiori",
                "n":     "N° 04",
                "image": _MIELE,
                "name":  "Miele millefiori",
                "meta":  "12 arnie · radura di castagno · estrazione luglio",
                "price": "€ 14",
            },
            {
                "id":    "marmellata-susine",
                "n":     "N° 05",
                "image": _MARMELLATA,
                "name":  "Marmellata di susine",
                "meta":  "Susine claudia · lotto agosto · cottura lenta 4 ore",
                "price": "€ 9",
            },
            {
                "id":    "cantucci-mandorle",
                "n":     "N° 08",
                "image": _CANTUCCI,
                "name":  "Cantucci di mandorle",
                "meta":  "Ricetta di nonna Annetta · forno settimanale del podere",
                "price": "€ 12",
            },
        ],
    },

    # ─── FAMIGLIA (about · La famiglia Pasquinelli) ───────────
    "famiglia": {
        "eyebrow":  "La famiglia Pasquinelli",
        "headline": "Quattro generazioni a Le Querce.",
        "intro":
            "Il podere Le Querce è la casa della famiglia Pasquinelli dal "
            "novembre 1934. I bisnonni Mario e Annetta lo acquistarono "
            "dalla famiglia Antinori con un atto di vendita conservato in "
            "comune. Da allora quattro generazioni si sono succedute nel "
            "podere · oggi al timone ci sono Maria e Carlo con i figli "
            "Giovanni e Anna.",

        "mission_label":   "La nostra missione",
        "mission_heading": "Ospitalità contadina come l'avete in mente.",
        "mission_text":
            "Cuciniamo per i nostri ospiti la stessa cucina che facciamo per "
            "noi · niente menu da ristorante, niente carrello di formaggi, "
            "niente sommelier. C'è Maria che porta in tavola la ribollita "
            "che ha fatto stamattina, Giovanni che apre il vino che ha "
            "imbottigliato in primavera, Anna che taglia il pane che ha "
            "infornato all'alba.",

        "process_label":   "Il calendario della famiglia",
        "process_heading": "Quattro stagioni, quattro tempi del podere.",
        # process_steps — list[4] of DICT[5 keys=n,title,place,desc,duration]
        # CANONICAL shape (NOT Sapori's broken {num/title/desc})
        "process_steps": [
            {
                "n":        "01",
                "title":    "Primavera · innesto e fioritura",
                "place":    "Oliveto + vigna + orto",
                "desc":
                    "Marzo-maggio · innesto delle viti, potatura dell'oliveto, "
                    "semina dell'orto · le quattro camere riaprono dopo la "
                    "chiusura tecnica di gennaio. Tavolata della Pasqua con "
                    "agnello di Zeri.",
                "duration": "Tre mesi · marzo-maggio",
            },
            {
                "n":        "02",
                "title":    "Estate · raccolta e ospitalità piena",
                "place":    "Tutto il podere",
                "desc":
                    "Giugno-agosto · pieno della stagione di ospitalità · "
                    "tavolate quotidiane di 12-16 ospiti · raccolta del miele · "
                    "raccolta del grano · raccolta delle conserve d'estate "
                    "(pomodori, susine, more, fichi).",
                "duration": "Tre mesi · giugno-agosto",
            },
            {
                "n":        "03",
                "title":    "Settembre · vendemmia",
                "place":    "Vigna + cantina",
                "desc":
                    "Settembre · vendemmia manuale del Sangiovese · "
                    "diciotto giorni di lavoro continuo in vigna · "
                    "cantina chiusa al pubblico nelle due settimane di "
                    "vinificazione · tavolata di chiusura vendemmia "
                    "con tutta la famiglia e i braccianti.",
                "duration": "Un mese · settembre",
            },
            {
                "n":        "04",
                "title":    "Autunno-inverno · olio e maiale",
                "place":    "Oliveto + stalla + cucina",
                "desc":
                    "Novembre · raccolta delle olive (sei settimane) · "
                    "dicembre macellazione dei cinti senesi · gennaio "
                    "produzione salami con il norcino Pieri · febbraio "
                    "chiusura tecnica del podere · marzo riapertura.",
                "duration": "Cinque mesi · novembre-marzo",
            },
        ],

        "founder_label":    "La matriarca",
        "founder_heading":  "Maria Pasquinelli · al podere dal 1985.",
        "founder_text":
            "Maria Pasquinelli (classe 1962) è terza generazione del podere "
            "· figlia di Giovanni e Maddalena Pasquinelli, nipote dei "
            "bisnonni Mario e Annetta che comprarono il podere agli "
            "Antinori. Ha preso in mano l'azienda nel 1985 dopo la morte "
            "del padre · sposata con Carlo (di un podere vicino) dal 1987 "
            "· due figli Giovanni (1990) e Anna (1993) che lavorano il "
            "podere a tempo pieno dal 2015. In cucina dalle sette del "
            "mattino, alla tavolata della sera con gli ospiti.",
        "founder_portrait":  _PORTRAIT_MARIA,
        "founder_caption":   "Maria Pasquinelli alla tavolata di domenica · fotografia di Paolo Codeluppi · estate 2024",

        "numbers_label": "Il podere in cifre",
        # numbers_items — list[4] of tuple[2]
        "numbers_items": [
            ("92",  "Anni di famiglia Pasquinelli al podere · dal 1934"),
            ("13",  "Ettari coltivati direttamente · oliveto + vigna + orto + bosco"),
            ("4",   "Camere di ospitalità · tutta la famiglia ai fornelli"),
            ("8",   "Prodotti della dispensa · sei a marchio del podere + due dai produttori del territorio"),
        ],

        "visit_label":          "Per visitare il podere",
        "visit_heading":        "Tavolata su prenotazione · oppure visita guidata.",
        "visit_text":
            "Visite guidate al podere su prenotazione · martedì e giovedì "
            "pomeriggio (ore 16) per ospiti non residenti. Tavolata della "
            "sera (12-16 persone) su prenotazione almeno 48 ore prima. "
            "Le quattro camere si prenotano direttamente con Maria.",
        "visit_primary":         "Prenotate la tavolata",
        "visit_primary_href":    "soggiorno",
        "visit_secondary":       "WhatsApp diretto a Maria",
    },

    # ─── DIARIO (journal · 3 entries) ─────────────────────────
    "diario": {
        "eyebrow":     "Diario di campagna",
        "headline":    "Tre voci da Greve in Chianti.",
        "intro":
            "Il diario del podere raccoglie le voci della famiglia · "
            "Maria scrive una volta al mese da gennaio 2018 · Giovanni e "
            "Anna aggiungono note di stagione. Annotazioni di lavoro · "
            "non racconti turistici.",
        "list_label":  "Tre note recenti",
        # entries — list[3] of dict[5 keys=n,title,place,excerpt,minutes]
        "entries": [
            {
                "n":       "001",
                "title":   "Vendemmia 2025 · il giorno della pioggia",
                "place":   "Vigna · 14 settembre 2025",
                "excerpt":
                    "La pioggia è arrivata il pomeriggio del decimo giorno · "
                    "abbiamo lavorato comunque · solo tre filari da terminare. "
                    "Giovanni ha portato la vasca grande sotto il pergolato · "
                    "Maria ha aperto la cucina · alle dieci di sera eravamo "
                    "tutti dentro con la zuppa di cavolo nero.",
                "minutes": "4 minuti di lettura",
            },
            {
                "n":       "002",
                "title":   "Raccolta olive 2025 · le piante più anziane",
                "place":   "Oliveto · 12 novembre 2025",
                "excerpt":
                    "Le piante di oltre duecento anni quest'anno hanno dato "
                    "molto meno · il caldo di agosto le ha provate. Carlo dice "
                    "che la pianta numero 47 (la più anziana, oltre 350 anni "
                    "secondo il libretto del 1923) ha dato solo 4 kg quest'anno "
                    "contro i 28 dell'anno scorso. Continueremo a curarla.",
                "minutes": "3 minuti di lettura",
            },
            {
                "n":       "003",
                "title":   "Anna inizia l'apicoltura · le prime tre arnie",
                "place":   "Bosco del podere · 22 aprile 2025",
                "excerpt":
                    "Anna ha portato a casa le prime tre arnie dal corso di "
                    "apicoltura di Vinci. Le ha sistemate nel bosco del "
                    "podere, dove c'è una radura di castagni. Maria dice che "
                    "il padre aveva tenuto le api fino al 1972 · poi più "
                    "nessuno. Vediamo se passano l'inverno.",
                "minutes": "5 minuti di lettura",
            },
        ],
        "footer_note_label": "Per ricevere il diario",
        "footer_note":
            "Il diario non ha newsletter automatica · se volete riceverlo "
            "scrivete a Maria. Spediamo una stampa cartacea alla fine "
            "dell'anno agli ospiti che ce lo chiedono.",
    },

    # ─── SOGGIORNO (contact · prenota la tavolata) ────────────
    "soggiorno": {
        "eyebrow":  "Soggiorno · prenotazione diretta",
        "headline": "Quattro camere, una sola tavolata.",
        "intro":
            "Le quattro camere del podere si prenotano direttamente con la "
            "famiglia Pasquinelli · niente piattaforma esterna, niente "
            "commissioni intermediarie. Scrivete a Maria · risponde "
            "personalmente entro la giornata, di solito tra le pause della "
            "cucina.",

        "form_section_label":   "Richiesta di soggiorno",
        "form_section_intro":
            "Indicate le date desiderate, il numero di ospiti e qualsiasi "
            "richiesta speciale · allergie, intolleranze, bambini, animali. "
            "Maria risponde dalla cucina entro 24 ore.",
        "form_helper_required": "I campi con · sono obbligatori",
        "form_submit_button":   "Inviate a Maria",
        "form_submit_note":
            "Conferma definitiva tramite caparra del 30% via bonifico · "
            "saldo all'arrivo al ricevimento del podere.",

        # form_fields — list[~7] of dict[5 keys=label,name,type,required,placeholder]
        "form_fields": [
            {
                "label":       "Nome e cognome",
                "name":        "name",
                "type":        "text",
                "required":    True,
                "placeholder": "Come vi presentate · Maria vi chiamerà per nome",
            },
            {
                "label":       "Email diretta",
                "name":        "email",
                "type":        "email",
                "required":    True,
                "placeholder": "Maria risponde da famiglia@podereleQuerce.it",
            },
            {
                "label":       "WhatsApp · oppure telefono",
                "name":        "phone",
                "type":        "tel",
                "required":    False,
                "placeholder": "+39 339 458 1126 · Maria risponde anche via WhatsApp",
            },
            {
                "label":       "Data di arrivo",
                "name":        "arrival",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Data di partenza",
                "name":        "departure",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Numero ospiti",
                "name":        "guests",
                "type":        "number",
                "required":    True,
                "placeholder": "Adulti + bambini",
            },
            {
                "label":       "Allergie, intolleranze, animali",
                "name":        "notes",
                "type":        "textarea",
                "required":    False,
                "placeholder": "Maria adatta la cucina · ditecelo qui",
                "rows":        5,
            },
        ],

        # Contact card
        "card_label":            "Per le risposte rapide",
        "card_address_label":    "Dove siamo",
        "card_address_value":    "Località Le Querce 14 · 50022 Greve in Chianti · Firenze",
        "card_phone_label":      "Cucina · Maria",
        "card_phone_value":      "+39 055 853 261",
        "card_whatsapp_label":   "WhatsApp diretto",
        "card_whatsapp_value":   "+39 339 458 1126 · Maria",
        "card_email_label":      "Email",
        "card_email_value":      "famiglia@podereleQuerce.it",
        "card_hours_label":      "Orari",
        # card_hours_rows — list of SCALAR strings (per contract · NOT tuples)
        "card_hours_rows": [
            "Cucina aperta tutto l'anno · pranzo 12:30 · cena 19:30",
            "Ricevimento ospiti 8-22 · Maria in cucina dalle 7",
            "Dispensa 9-19 · domenica chiusa (mercato di Greve)",
            "Chiusura tecnica · 1-28 febbraio",
        ],
        "card_directions_label": "Come ci si arriva",
        "card_directions_text":
            "Da Firenze 28 km · uscita autostrada A1 Firenze Sud · seguire "
            "Chiantigiana · 12 km dopo Greve in Chianti girare a destra "
            "verso Lamole · 1,4 km dal bivio. Cancello in legno con scritta "
            "«Podere Le Querce» a mano · suonate al campanello.",

        "faq_label": "Domande dalla cucina",
        # faq_items — list[5] of DICT[2 keys=q,a]
        # CANONICAL shape (NOT Sapori's broken 2-tuples)
        "faq_items": [
            {
                "q": "Si paga la tavolata anche se siamo ospiti delle camere?",
                "a":
                    "Sì · la cucina e l'ospitalità sono due cose distinte · "
                    "le camere si pagano per il pernottamento, la tavolata "
                    "si paga a parte · 35 € a persona per cena, 28 € per "
                    "pranzo (vino del podere incluso). Colazione invece "
                    "compresa nel prezzo della camera.",
            },
            {
                "q": "Si accettano bambini e animali?",
                "a":
                    "I bambini sono benvenuti · abbiamo lettini per i "
                    "piccoli, seggioloni per i più grandi · Anna spesso si "
                    "occupa di portarli in stalla a vedere i cinti senesi. "
                    "I cani piccoli sono ammessi nelle camere di sotto "
                    "(supplemento 15 € a notte) · grandi nella corte e nel "
                    "bosco, ma non in camera né in cucina.",
            },
            {
                "q": "Si può visitare il podere senza dormire?",
                "a":
                    "Sì · martedì e giovedì pomeriggio (ore 16, durata 90 "
                    "minuti, su prenotazione almeno 24 ore prima) Carlo "
                    "porta i visitatori in oliveto e in cantina · 20 € a "
                    "persona · degustazione di olio + vino + miele inclusa. "
                    "Senza prenotazione la dispensa è comunque aperta tutti "
                    "i giorni 9-19.",
            },
            {
                "q": "Si può prenotare il podere intero per matrimoni o eventi?",
                "a":
                    "Sì, per matrimoni intimi · massimo 36 ospiti · cerimonia "
                    "civile in giardino sotto il pergolato di glicine · "
                    "tavolata sotto il fienile restaurato · scrivere a "
                    "Maria almeno otto mesi prima della data. Non "
                    "organizziamo matrimoni con più di 36 ospiti né "
                    "eventi aziendali.",
            },
            {
                "q": "Si può comprare i prodotti senza venire al podere?",
                "a":
                    "Sì · la dispensa spedisce in tutta Italia (24-48 ore, "
                    "spedizione gratuita sopra € 80) e in Europa (4-6 "
                    "giorni). Cassa di legno timbrato a marchio del podere "
                    "· torna indietro a vostra discrezione · ordini sopra "
                    "12 bottiglie scrivete direttamente a Maria per uno "
                    "sconto.",
            },
        ],
    },
}
