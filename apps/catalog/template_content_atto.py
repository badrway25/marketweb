"""Atto · Studio Notarile Conti–Sironi–Verri · Italian content tree.

Wave 1 Pass-3 (T47 · 2026-05-12). First reuse of the `classic-gold`
archetype after Lex. Zero new HTML files: reuses
`templates/live_templates/lawyer/classic-gold/` skin verbatim.

D-054 distinctness against Lex (11 axes confirmed):
- brand: 3-notary association vs 1-founder boutique
- accent: ink-blue #1F3A5F (notarial-archive) vs Lex gold #C5A55A (ledger-prestige)
- font: Source Serif 4 + Public Sans vs Lex Cormorant Garamond + Inter
- conversion: primo-incontro-orientamento (30 min · gratuito · no commitment) vs Lex private-consultation (paid retainer)
- voice anchor: `atto pubblico` (the public-faith deed) vs Lex `riservatezza`
- founder type: 3 notai associati (collegiate · pubblici ufficiali) vs Lex Avv. Prof. Ferri (academic singolo)
- geography: Milano single Distretto vs Roma+Milano dual-foro
- imagery direction: notarile-archivio-istituzionale vs Lex legal-heritage-ink
- service catalog: 7 tipologie di atti vs Lex 12 practice areas
- proof surface: Distretto Notarile + iscrizione al ruolo vs Lex firm-KPIs
- CTA verb: "Richiedi un primo incontro" (notary §6 binding) vs Lex "Richiedi una consulenza riservata"

IT-only at T47 Pass-3 build per D-102 cadence. Tier stays `draft` until
T48 (workflow C multilingual + public flip handshake).
"""
from __future__ import annotations

from typing import Any


# ─── Imagery — verified Pexels URLs from notary-commercialista X.3 pack ────
_NOTARY_HERO = "https://images.pexels.com/photos/6077091/pexels-photo-6077091.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
_NOTARY_SIGNING = "https://images.pexels.com/photos/5235410/pexels-photo-5235410.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
_NOTARY_PORTRAIT_F1 = "https://images.pexels.com/photos/6077124/pexels-photo-6077124.jpeg?auto=compress&cs=tinysrgb&w=800&h=1200&fit=crop"
_NOTARY_PORTRAIT_M = "https://images.pexels.com/photos/7841445/pexels-photo-7841445.jpeg?auto=compress&cs=tinysrgb&w=800&h=1200&fit=crop"
_NOTARY_DETAIL = "https://images.pexels.com/photos/5669602/pexels-photo-5669602.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop"
_NOTARY_AMBIENT = "https://images.pexels.com/photos/1842502/pexels-photo-1842502.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop"


ATTO_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Studio",        "kind": "home"},
        {"slug": "studio",        "label": "Lo Studio",     "kind": "about"},
        {"slug": "pratiche",      "label": "Aree di Atti",  "kind": "services"},
        {"slug": "avvocati",      "label": "I Notai",       "kind": "team"},
        {"slug": "pubblicazioni", "label": "Pubblicazioni", "kind": "blog_list"},
        {"slug": "contatti",      "label": "Contatti",      "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ──────────────────────────
    "site": {
        "logo_initial":  "CSV",
        "logo_word":     "Studio Notarile Conti–Sironi–Verri",
        "tag":           "Distretto Notarile di Milano · dal 2007",
        "phone":         "+39 02 7641 1898",
        "email":         "studio@notaiconti-sironi-verri.it",
        "address":       "Via Manin 12 · 20121 Milano",
        "hours_compact": "Lunedì – Venerdì · 09:00 – 18:30",
        "hours_footer_rows": [
            "Sabato · su appuntamento per atti urgenti",
            "Domenica · chiuso",
        ],
        "license":
            "Notai iscritti al Distretto Notarile di Milano · "
            "Consiglio Notarile dei Distretti Riuniti di Milano, "
            "Busto Arsizio, Lodi, Monza e Varese · L. 89/1913",
        "nav_cta":       "Richiedi un primo incontro",
        "footer_intro":
            "Studio Notarile Conti–Sironi–Verri — diciassette anni di "
            "atto pubblico al servizio di famiglie, imprese e operatori "
            "del Distretto Notarile di Milano. Tre notai associati, "
            "una sola firma per la pubblica fede.",
        "foot_studio":  "Lo studio",
        "foot_pages":   "Pagine",
        "foot_contact": "Contatti",
        "foot_offices": "Sede",
        "offices_footer_rows": [
            "Milano · via Manin 12",
            "Distretto Notarile di Milano",
        ],

        # Cross-page meta labels (lifted from skin for locale support).
        "case_practice_label":  "Tipologia di atto",
        "case_year_label":      "Anno",
        "case_outcome_label":   "Esito",
        "case_lead_label":      "Notaio rogante",
    },

    # ════════════════════════════════════════════════════════════════════
    # HOME (studio)
    # ════════════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":  "Studio Notarile Conti–Sironi–Verri · Milano · dal 2007",
        "headline": "Diciassette anni di <em>atto pubblico</em>, una firma che vale per legge.",
        "intro":
            "Lo studio assiste privati, famiglie e imprese nella "
            "redazione dell'atto notarile — rogiti di compravendita, "
            "successioni, atti societari, donazioni, mutui ipotecari, "
            "procure e testamenti. Ogni atto è redatto personalmente "
            "da uno dei tre notai associati, iscritti al ruolo del "
            "Distretto Notarile di Milano, nel pieno esercizio della "
            "funzione di pubblico ufficiale e della pubblica fede "
            "che la legge le riconosce.",
        "primary_cta":    "Richiedi un primo incontro",
        "primary_href":   "contatti",
        "secondary_cta":  "Aree di atti",
        "secondary_href": "pratiche",

        # Hero — split-ledger-monogram silhouette
        "hero_credit_left":  ("Notaio fondatore",  "Dott.ssa M. B. Conti"),
        "hero_credit_right": ("Distretto",         "Milano · iscrizione al ruolo"),
        "hero_meta_strip": [
            ("Sede dello studio",   "Milano · via Manin 12"),
            ("Notai associati",     "Tre · iscritti dal 2007/2014/2021"),
            ("Atti rogati",         "4.200+ · IT · EN · FR"),
        ],

        # Practice-area ledger — 4 rows on home, full 7 on /pratiche
        "practice_label":   "Aree di atti",
        "practice_heading": "Sette tipologie di <em>atto</em>, una sola pubblica fede.",
        "practice_intro":
            "Lo studio si occupa delle principali tipologie di atto "
            "notarile previste dall'ordinamento. Ogni atto pubblico è "
            "redatto personalmente da un notaio dello studio, letto al "
            "comparente nella lingua scelta (italiano, inglese o "
            "francese) e iscritto a repertorio ai sensi della Legge "
            "Notarile (L. 89/1913).",
        "practice": [
            ("01", "Rogiti di compravendita immobiliare",
             "Redazione del rogito notarile per la compravendita di "
             "immobili residenziali, commerciali e produttivi. "
             "Verifiche presso il catasto, ispezioni ipotecarie e "
             "controllo della regolarità urbanistica precedono la "
             "stipula. L'atto è ricevuto in forma pubblica con la "
             "pubblica fede riconosciuta dall'art. 2700 c.c."),
            ("02", "Successioni e dichiarazioni",
             "Apertura della successione, redazione della dichiarazione "
             "di successione, accettazione di eredità con beneficio "
             "d'inventario, pubblicazione del testamento olografo, "
             "rinunce e divisioni ereditarie. Per le successioni "
             "transfrontaliere si applica il Reg. UE 650/2012."),
            ("03", "Atti societari e operazioni straordinarie",
             "Costituzione di società per atto pubblico ai sensi degli "
             "artt. 2328 e 2463 c.c., modifiche statutarie, verbali di "
             "assemblea straordinaria, fusioni, scissioni e "
             "trasformazioni. Lo studio segue l'intero iter dalla "
             "delibera al deposito presso il Registro delle Imprese."),
            ("04", "Mutui ipotecari e garanzie reali",
             "Atti di mutuo fondiario e ipotecario, costituzione di "
             "ipoteca volontaria, surroghe ex L. 40/2007, atti "
             "ricognitivi e cancellazioni. Coordinamento operativo "
             "con l'istituto erogante per la sottoscrizione "
             "contestuale al rogito di compravendita."),
        ],

        # Stats band — counter animation (notarial-institutional facts)
        "stats_label":   "Diciassette anni di pubblica fede",
        "stats_heading": "I numeri dello studio",
        "stats": [
            ("3",      "notai iscritti al ruolo"),
            ("17",     "anni dalla fondazione"),
            ("4.200+", "atti rogati"),
            ("3",      "lingue di rogito (IT/EN/FR)"),
        ],

        # Partners portrait preview — 3 notai associati
        "partners_label":   "I tre notai",
        "partners_heading": "Tre notai, un solo studio",
        "partners_intro":
            "Lo studio è retto da tre notai associati, ciascuno iscritto "
            "al ruolo del Distretto Notarile di Milano e responsabile "
            "delle proprie tipologie di atto. La firma è personale: "
            "il notaio che riceve il comparente è lo stesso che redige, "
            "legge e sottoscrive l'atto pubblico in forma di repertorio.",
        "partners": [
            {
                "name":  "Notaio dott.ssa Maria Beatrice Conti",
                "role":  "Notaio fondatore · Atti societari · M&A internazionali",
                "foro":  "Distretto Notarile di Milano · iscritta al ruolo dal 2007",
                "bio":
                    "Fondatrice dello studio, riceve gli atti di "
                    "costituzione di società, operazioni straordinarie "
                    "e atti pubblici in lingua inglese. Già praticante "
                    "presso studio notarile internazionale di Milano "
                    "(2004-2006), si occupa in particolare di "
                    "M&A cross-border e di gruppi multinazionali con "
                    "controllata italiana.",
            },
            {
                "name":  "Notaio dott. Andrea Sironi",
                "role":  "Notaio associato · Diritto societario · CTU Tribunale di Milano",
                "foro":  "Distretto Notarile di Milano · iscritto al ruolo dal 2014",
                "bio":
                    "Si occupa di atti societari ordinari e straordinari, "
                    "patti parasociali, finanziamenti soci e operazioni "
                    "di equity. CTU presso il Tribunale di Milano per "
                    "perizie ex art. 2343 c.c. Componente della "
                    "Commissione Studi del Consiglio Notarile dei "
                    "Distretti Riuniti di Milano.",
            },
            {
                "name":  "Notaio dott. Stefano Verri",
                "role":  "Notaio associato · Immobiliare · Successioni",
                "foro":  "Distretto Notarile di Milano · iscritto al ruolo dal 2021",
                "bio":
                    "Riceve gli atti di compravendita immobiliare, mutuo "
                    "ipotecario, donazione e successione. Revisore "
                    "legale iscritto al registro tenuto dal MEF, "
                    "coordina le verifiche urbanistiche e catastali "
                    "preliminari al rogito. Già praticante notarile a "
                    "Milano e Brescia (2017-2020).",
            },
        ],

        # Publications ribbon — riviste notarili
        "publications_label": "Pubblicazioni e citazioni",
        "publications": [
            "NOTARIATO",
            "RIVISTA DEL NOTARIATO",
            "GUIDA AL DIRITTO",
            "CNN NOTIZIE",
            "RIVISTA TRIMESTRALE DI DIRITTO E PROCEDURA",
            "FEDERNOTAI",
        ],

        # Final CTA band — first-meeting (orientamento) ghost serif
        "cta_label":      "Primo incontro di orientamento",
        "cta_heading":    "Trenta minuti per inquadrare l'atto.",
        "cta_intro":
            "Il primo incontro con uno dei notai dello studio dura "
            "circa trenta minuti, è gratuito e non vincolante. Si "
            "discute la tipologia di atto, l'elenco dei documenti "
            "preliminari da raccogliere e la tabella degli onorari "
            "notarili applicabili. Nessuna decisione operativa viene "
            "richiesta in questa fase.",
        "cta_primary":       "Richiedi un primo incontro",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "Conosci lo studio",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════════════
    # STUDIO (about) — storia, notai associati, valori, sede
    # ════════════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "Lo studio · 2007 — 2026",
        "headline": "Diciassette anni di <em>atto pubblico</em>, tre notai associati.",
        "intro":
            "Lo Studio Notarile Conti–Sironi–Verri nasce a Milano nel "
            "2007 dall'iscrizione al ruolo della Notaio dott.ssa Maria "
            "Beatrice Conti, primo notaio del distretto a ricevere "
            "atti pubblici in lingua inglese. Lo studio è cresciuto "
            "per cooptazione di colleghi e oggi conta tre notai "
            "associati e sei collaboratori a tempo pieno, tutti "
            "operativi nella sede unica di via Manin 12.",

        # History timeline — sei date che hanno definito lo studio
        "history_label":   "Storia dello studio",
        "history_heading": "Sei date, diciassette anni",
        "history_intro":
            "Sei pietre miliari che segnano la traiettoria dello "
            "studio — dalla prima iscrizione al ruolo del 2007 "
            "all'ingresso del terzo notaio nel 2021. Ogni passaggio "
            "ha definito la composizione collegiale dell'associazione "
            "e l'ampliamento delle tipologie di atto trattate.",
        "history": [
            ("2007", "Iscrizione al ruolo del notaio fondatore",
             "La Notaio dott.ssa Maria Beatrice Conti viene iscritta "
             "al ruolo del Distretto Notarile di Milano e apre lo "
             "studio in via Manin 12. I primi atti riguardano "
             "costituzioni di società di capitali per imprenditori "
             "del Nord-Italia."),
            ("2011", "Atti pubblici trilingui",
             "Lo studio inizia a ricevere atti pubblici redatti in "
             "italiano, inglese e francese ai sensi dell'art. 54 "
             "Legge Notarile. La sezione internazionale serve "
             "soprattutto gruppi multinazionali con controllata "
             "italiana e famiglie residenti all'estero."),
            ("2014", "Ingresso del Notaio Andrea Sironi",
             "Il Notaio dott. Andrea Sironi, già praticante di lungo "
             "corso nel Distretto, viene cooptato come secondo notaio "
             "dell'associazione. Si specializza in atti societari, "
             "operazioni straordinarie e perizie di stima ex "
             "art. 2343 c.c."),
            ("2018", "Sezione successioni e immobiliare",
             "Lo studio struttura una sezione dedicata alle successioni "
             "e all'immobiliare. Vengono codificate le procedure "
             "interne di ispezione ipotecaria e visura catastale "
             "preliminari al rogito di compravendita."),
            ("2021", "Ingresso del Notaio Stefano Verri",
             "Il Notaio dott. Stefano Verri completa la composizione "
             "collegiale dell'associazione. Revisore legale iscritto "
             "al registro tenuto dal MEF, assume la responsabilità "
             "operativa della sezione immobiliare e delle successioni."),
            ("2025", "Diciassette anni di pubblica fede",
             "Lo studio supera i quattromiladuecento atti rogati. "
             "I tre notai associati sono attivi nella formazione "
             "professionale: la dott.ssa Conti come componente della "
             "Commissione Studi del Consiglio Notarile, il dott. "
             "Sironi come CTU presso il Tribunale di Milano, il "
             "dott. Verri come docente di pratica notarile."),
        ],

        # Method — quattro principi non negoziabili
        "values_label":   "Metodo notarile",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Sono le quattro regole operative che orientano il lavoro "
            "dello studio. Non descrivono uno stile commerciale ma "
            "una pratica professionale fedele alla Legge Notarile "
            "(L. 89/1913) e al Codice Deontologico del Consiglio "
            "Nazionale del Notariato.",
        "values": [
            ("01", "Imparzialità del pubblico ufficiale",
             "Il notaio è pubblico ufficiale e agisce a tutela di "
             "tutte le parti dell'atto, mai di una sola. Lo studio "
             "non accetta incarichi di parte: nessun atto viene "
             "predisposto a vantaggio dell'una o dell'altra parte "
             "contraente. Le indicazioni operative sono uguali per "
             "venditore e acquirente, donante e donatario, conferente "
             "e conferitaria."),
            ("02", "Verifica documentale preliminare",
             "Prima di ricevere il rogito, lo studio verifica i "
             "documenti urbanistici, catastali e ipotecari relativi "
             "all'immobile o alla società oggetto dell'atto. La "
             "visura catastale, l'ispezione ipotecaria e l'APE "
             "vengono raccolte direttamente, mai delegate alle "
             "parti, e sono allegate all'atto come da prassi."),
            ("03", "Lettura integrale al comparente",
             "L'atto pubblico viene letto integralmente ai comparenti "
             "ai sensi dell'art. 51 Legge Notarile, in italiano o "
             "nella lingua scelta fra quelle in cui il notaio è "
             "abilitato (IT/EN/FR). Solo dopo la lettura e l'esplicita "
             "approvazione viene apposta la firma e il numero di "
             "repertorio."),
            ("04", "Tabella onorari notarili trasparente",
             "Gli onorari sono determinati secondo la tabella in "
             "vigore approvata dal Consiglio Nazionale del Notariato. "
             "Lo studio comunica per iscritto il preventivo "
             "indicativo prima di ogni rogito, comprensivo di imposte "
             "e tasse di registro. Nessuna voce viene aggiunta in "
             "sede di stipula."),
        ],

        # Coordinates strip — sede unica milanese
        "coordinates_label": "La sede",
        "coordinates": [
            ("Milano · sede",         "Via Manin 12 · 20121 · Porta Nuova"),
            ("Distretto Notarile",    "Milano · Consiglio Notarile dei Distretti Riuniti"),
        ],

        # Page-level CTA
        "cta_heading":  "Un primo incontro per inquadrare l'atto.",
        "cta_intro":
            "Il primo incontro con uno dei notai dello studio è "
            "gratuito, dura circa trenta minuti e non vincola a "
            "nessun adempimento successivo. Si discute la tipologia "
            "di atto, i documenti preliminari e la tabella degli "
            "onorari notarili applicabili.",
        "cta_primary":       "Richiedi un primo incontro",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # PRATICHE (services) — 7 tipologie di atti notarili
    # ════════════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Aree di atti · 2026",
        "headline": "Sette tipologie di <em>atto notarile</em>, una sola firma.",
        "intro":
            "Le sette tipologie di atto trattate dallo studio. Ogni "
            "atto pubblico è redatto personalmente da un notaio "
            "dell'associazione, iscritto al ruolo del Distretto "
            "Notarile di Milano, e iscritto a repertorio ai sensi "
            "della Legge Notarile (L. 89/1913). Le voci di tabella "
            "onorari notarili sono comunicate per iscritto prima "
            "della stipula.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":          "Notaio responsabile",
        "svc_jurisdiction_label":  "Distretto",

        # 7 atti notarili
        "services": [
            {
                "num":   "01",
                "title": "Rogiti di compravendita immobiliare",
                "blurb":
                    "Redazione del rogito notarile per la compravendita "
                    "di immobili residenziali, commerciali e produttivi. "
                    "Lo studio si occupa anche del preliminare di "
                    "compravendita (compromesso) e degli atti di "
                    "permuta. La pubblica fede dell'atto è riconosciuta "
                    "dall'art. 2700 c.c.",
                "scope": [
                    "Visura catastale e ispezione ipotecaria",
                    "Verifica della regolarità urbanistica e APE",
                    "Preliminare di compravendita registrato",
                    "Rogito pubblico letto al comparente",
                ],
                "lead":          "Notaio dott. Stefano Verri",
                "jurisdiction":  "Milano · Distretto Notarile",
            },
            {
                "num":   "02",
                "title": "Successioni e dichiarazioni",
                "blurb":
                    "Apertura della successione, redazione della "
                    "dichiarazione di successione presso l'Agenzia "
                    "delle Entrate, accettazione di eredità con "
                    "beneficio d'inventario, pubblicazione del "
                    "testamento olografo, divisioni ereditarie. "
                    "Per le successioni internazionali si applica "
                    "il Reg. UE 650/2012.",
                "scope": [
                    "Dichiarazione di successione",
                    "Accettazione beneficiata e con riserva",
                    "Pubblicazione testamento olografo",
                    "Divisioni ereditarie e rinunce",
                ],
                "lead":          "Notaio dott. Stefano Verri",
                "jurisdiction":  "Milano · UE 650/2012",
            },
            {
                "num":   "03",
                "title": "Atti societari · costituzioni · operazioni straordinarie",
                "blurb":
                    "Costituzione di società per atto pubblico ai "
                    "sensi degli artt. 2328 e 2463 c.c., modifiche "
                    "statutarie, verbali di assemblea straordinaria, "
                    "fusioni ex artt. 2501 ss. c.c., scissioni "
                    "proporzionali e non, trasformazioni eterogenee. "
                    "Deposito al Registro delle Imprese a cura dello studio.",
                "scope": [
                    "Costituzione di s.p.a. e s.r.l.",
                    "Modifiche statutarie e patti parasociali",
                    "Fusioni, scissioni, trasformazioni",
                    "Deposito al Registro delle Imprese",
                ],
                "lead":          "Notaio dott. Andrea Sironi",
                "jurisdiction":  "Milano · CCIAA Milano Monza Brianza Lodi",
            },
            {
                "num":   "04",
                "title": "Mutui ipotecari e garanzie reali",
                "blurb":
                    "Atti di mutuo fondiario e ipotecario, costituzione "
                    "di ipoteca volontaria, surroghe ex L. 40/2007 "
                    "(portabilità del mutuo), atti ricognitivi del "
                    "credito e cancellazioni d'ipoteca. La stipula "
                    "avviene di norma contestualmente al rogito di "
                    "compravendita.",
                "scope": [
                    "Mutuo fondiario contestuale al rogito",
                    "Costituzione di ipoteca volontaria",
                    "Surroga ex L. 40/2007 (portabilità)",
                    "Cancellazione e riduzione d'ipoteca",
                ],
                "lead":          "Notaio dott. Stefano Verri",
                "jurisdiction":  "Milano · Agenzia delle Entrate",
            },
            {
                "num":   "05",
                "title": "Donazioni · atti tra vivi",
                "blurb":
                    "Atto pubblico di donazione di immobili, denaro o "
                    "partecipazioni sociali ai sensi degli artt. 769 "
                    "e ss. c.c. Lo studio si occupa anche delle "
                    "donazioni indirette, dei patti di famiglia ex "
                    "art. 768-bis c.c. e delle donazioni con riserva "
                    "di usufrutto.",
                "scope": [
                    "Donazione immobiliare con/senza riserva di usufrutto",
                    "Donazione di partecipazioni sociali",
                    "Patti di famiglia (art. 768-bis c.c.)",
                    "Pianificazione fiscale e imposta sulle donazioni",
                ],
                "lead":          "Notaio dott.ssa Maria Beatrice Conti",
                "jurisdiction":  "Milano · Agenzia delle Entrate",
            },
            {
                "num":   "06",
                "title": "Procure · autentiche di firma",
                "blurb":
                    "Procura speciale e procura generale ai sensi "
                    "dell'art. 1387 c.c., autentica di firma su "
                    "scrittura privata, autentica di copia conforme. "
                    "Lo studio rilascia procure trilingui (IT/EN/FR) "
                    "per atti da compiersi all'estero, con apostille "
                    "ai sensi della Convenzione dell'Aja del 1961.",
                "scope": [
                    "Procura speciale e procura generale",
                    "Autentica di firma su scrittura privata",
                    "Autentica di copia conforme",
                    "Apostille e legalizzazione internazionale",
                ],
                "lead":          "Notaio dott.ssa Maria Beatrice Conti",
                "jurisdiction":  "Milano · Convenzione Aja 1961",
            },
            {
                "num":   "07",
                "title": "Testamenti · pianificazione successoria",
                "blurb":
                    "Testamento pubblico ai sensi dell'art. 603 c.c., "
                    "ricezione del testamento olografo, testamento "
                    "internazionale ex Convenzione di Washington 1973. "
                    "Lo studio assiste i comparenti nella ricognizione "
                    "del patrimonio, nella quantificazione della "
                    "quota disponibile e nella legittima.",
                "scope": [
                    "Testamento pubblico in forma di repertorio",
                    "Ricezione di testamento olografo",
                    "Testamento internazionale (Washington 1973)",
                    "Pianificazione legittima e quota disponibile",
                ],
                "lead":          "Notaio dott. Stefano Verri",
                "jurisdiction":  "Milano · Archivio Notarile",
            },
        ],

        # Process strip — come si svolge la pratica dell'atto
        "process_label":   "Iter dell'atto",
        "process_heading": "Quattro fasi, una sola sequenza",
        "process": [
            ("01", "Primo incontro di orientamento",
             "Trenta minuti gratuiti con uno dei notai dell'associazione. "
             "Si inquadra la tipologia di atto, si chiarisce l'elenco "
             "dei documenti preliminari e si comunica la tabella degli "
             "onorari notarili applicabili. Nessuna decisione operativa "
             "richiesta in questa fase."),
            ("02", "Raccolta documentale e verifiche",
             "Lo studio raccoglie e verifica direttamente i documenti "
             "necessari: visura catastale, ispezione ipotecaria, "
             "regolarità urbanistica, APE, certificati anagrafici. "
             "Il comparente riceve l'elenco scritto di ciò che resta "
             "a sua cura."),
            ("03", "Predisposizione e bozza dell'atto",
             "Il notaio responsabile predispone la bozza dell'atto e "
             "la trasmette al comparente almeno cinque giorni "
             "lavorativi prima della stipula, per consentire una "
             "lettura riflessiva. Eventuali chiarimenti vengono "
             "discussi in un secondo incontro tecnico."),
            ("04", "Stipula, lettura e iscrizione a repertorio",
             "Il notaio legge l'atto al comparente ai sensi "
             "dell'art. 51 Legge Notarile, in italiano o nella "
             "lingua scelta. Dopo la firma, l'atto viene iscritto "
             "a repertorio, registrato presso l'Agenzia delle "
             "Entrate e conservato in originale presso lo studio."),
        ],

        # Final CTA
        "cta_heading":  "Non è chiaro quale atto serve?",
        "cta_intro":
            "Se la tipologia dell'atto non è ancora definita, è "
            "possibile chiedere un primo incontro di orientamento. "
            "Nei trenta minuti gratuiti, uno dei notai dello studio "
            "indirizza alla pratica corretta e comunica l'elenco "
            "dei documenti preliminari da raccogliere.",
        "cta_primary":       "Richiedi un primo incontro",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # AVVOCATI (team) — i tre notai associati
    # ════════════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "I notai · tre iscritti al ruolo",
        "headline": "Tre notai associati, <em>una sola</em> firma di pubblica fede.",
        "intro":
            "Lo studio è composto da tre notai associati, tutti "
            "iscritti al ruolo del Distretto Notarile di Milano. "
            "L'ingresso nell'associazione avviene per cooptazione "
            "unanime fra i notai già associati, mai per acquisizione "
            "di studio: ogni nuovo notaio porta in dote la propria "
            "iscrizione e le proprie specializzazioni. Sei "
            "collaboratori a tempo pieno completano l'organico.",

        # Card meta labels
        "lawyer_foro_label":           "Distretto",
        "lawyer_year_label":           "Iscrizione al ruolo",
        "lawyer_specialization_label": "Tipologie di atto",

        # 3 notai associati
        "lawyers": [
            {
                "name":           "Notaio dott.ssa Maria Beatrice Conti",
                "role":           "Notaio fondatore dello studio",
                "specialization": "Atti societari · M&A · donazioni · procure trilingui",
                "foro":           "Distretto Notarile di Milano",
                "year":           "Iscritta al ruolo dal 2007",
                "bio":
                    "Fondatrice dello Studio Notarile Conti–Sironi–Verri, "
                    "ha aperto la sede di via Manin 12 nel marzo 2007 "
                    "subito dopo l'iscrizione al ruolo del Distretto "
                    "Notarile di Milano. Riceve atti pubblici in "
                    "italiano, inglese e francese ai sensi dell'art. 54 "
                    "Legge Notarile, con particolare specializzazione "
                    "in costituzioni di società per gruppi multinazionali "
                    "con controllata italiana, fusioni cross-border e "
                    "procure internazionali con apostille ai sensi della "
                    "Convenzione dell'Aja. Componente della Commissione "
                    "Studi del Consiglio Notarile dei Distretti Riuniti "
                    "di Milano, Busto Arsizio, Lodi, Monza e Varese.",
            },
            {
                "name":           "Notaio dott. Andrea Sironi",
                "role":           "Notaio associato · diritto societario",
                "specialization": "Atti societari · operazioni straordinarie · perizie ex art. 2343 c.c.",
                "foro":           "Distretto Notarile di Milano",
                "year":           "Iscritto al ruolo dal 2014",
                "bio":
                    "Cooptato nell'associazione nel 2015 dopo otto anni "
                    "di pratica notarile presso primario studio milanese, "
                    "si occupa di atti societari ordinari e straordinari, "
                    "patti parasociali, finanziamenti soci, aumenti di "
                    "capitale ex artt. 2441 e 2443 c.c. CTU presso il "
                    "Tribunale di Milano per perizie di stima ex art. "
                    "2343 c.c. e per la stima del valore di liquidazione "
                    "ex art. 2437-ter c.c. Docente di pratica notarile "
                    "presso la Scuola di Notariato della Lombardia.",
            },
            {
                "name":           "Notaio dott. Stefano Verri",
                "role":           "Notaio associato · immobiliare e successioni",
                "specialization": "Rogiti compravendita · mutui · successioni · testamenti",
                "foro":           "Distretto Notarile di Milano",
                "year":           "Iscritto al ruolo dal 2021",
                "bio":
                    "Ultimo entrato nell'associazione, completa la "
                    "composizione collegiale dei tre notai. Si occupa "
                    "di rogiti di compravendita immobiliare, mutui "
                    "ipotecari, surroghe ex L. 40/2007 e dell'intera "
                    "filiera successoria — apertura della successione, "
                    "dichiarazione di successione, pubblicazione del "
                    "testamento olografo, accettazione con beneficio "
                    "d'inventario. Revisore legale iscritto al "
                    "registro tenuto dal MEF dal 2018, coordina le "
                    "verifiche urbanistiche, catastali e ipotecarie "
                    "preliminari ai rogiti dello studio.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════════
    # PUBBLICAZIONI (blog_list) — pubblicazioni e approfondimenti notarili
    # ════════════════════════════════════════════════════════════════════
    "pubblicazioni": {
        "eyebrow":  "Pubblicazioni e approfondimenti · 2023 — 2026",
        "headline": "Cinque approfondimenti sull'<em>atto notarile</em> contemporaneo.",
        "intro":
            "Una selezione di approfondimenti e pubblicazioni redatti "
            "dai notai dello studio o citati su riviste di settore. "
            "Gli articoli orientano comparenti, imprenditori e "
            "professionisti nelle principali tipologie di atto — "
            "compravendita, successione, costituzione di società, "
            "donazione e procura — senza pretesa di esaustività né "
            "valore di consulenza nel caso concreto.",

        # Lead post image
        "lead_image": _NOTARY_HERO,

        # Footer strap and fallbacks
        "footer_strap":
            "Le pubblicazioni dello studio hanno finalità divulgativa. "
            "Per il caso concreto è necessario un primo incontro con "
            "uno dei notai dell'associazione.",
        "empty_body_fallback_paragraphs": [
            "L'articolo è in corso di redazione. Lo studio pubblica "
            "i propri approfondimenti dopo lettura collegiale dei "
            "tre notai associati, per evitare imprecisioni o "
            "valutazioni superate da modifiche normative.",
            "Per il caso concreto è possibile richiedere un primo "
            "incontro di orientamento (trenta minuti gratuiti) con "
            "uno dei notai dello studio.",
        ],
    },

    # Posts powering blog_detail. URL: /pubblicazioni/<slug>/
    "posts": [
        {
            "slug":     "atto-pubblico-mercato-immobiliare-2026",
            "kicker":   "Rogiti immobiliari",
            "title":    "L'atto pubblico nel mercato immobiliare 2026 · prassi notarili e verifiche preliminari",
            "date":     "Aprile 2026",
            "read_min": "9",
            "author":   "Notaio dott. Stefano Verri",
            "lede":
                "Una ricognizione delle verifiche urbanistiche, "
                "catastali e ipotecarie che lo studio compie "
                "prima di ricevere un rogito di compravendita "
                "immobiliare, alla luce delle modifiche introdotte "
                "dal D.Lgs. 23/2023 in materia di trasparenza "
                "energetica e dalla giurisprudenza più recente "
                "della Cassazione sulla difformità urbanistica.",
            "body": [
                ("p",
                 "Il rogito notarile di compravendita immobiliare è "
                 "atto pubblico ai sensi dell'art. 2699 c.c. e "
                 "produce la pubblica fede riconosciuta dall'art. "
                 "2700 c.c. Il notaio rogante, in qualità di "
                 "pubblico ufficiale, è tenuto a verificare in "
                 "via preliminare la regolarità urbanistica, "
                 "catastale e ipotecaria dell'immobile."),
                ("h2", "Le tre verifiche preliminari"),
                ("p",
                 "Lo studio raccoglie tre serie di documenti prima "
                 "della stipula: la visura catastale aggiornata, "
                 "l'ispezione ipotecaria ventennale e l'attestato "
                 "di prestazione energetica (APE) in corso di "
                 "validità. La verifica della regolarità "
                 "urbanistica si fonda inoltre sull'esame dei "
                 "titoli abilitativi depositati presso il Comune."),
                ("h2", "Il ruolo del notaio"),
                ("p",
                 "Il notaio non è consulente di parte: assiste "
                 "entrambi i comparenti nell'inquadramento dell'atto "
                 "e nella lettura delle clausole. Eventuali "
                 "criticità urbanistiche emerse in sede di verifica "
                 "vengono comunicate per iscritto a venditore e "
                 "acquirente, in modo che la decisione di stipulare "
                 "o rinviare sia consapevole."),
                ("blockquote",
                 "La pubblica fede dell'atto pubblico è tutelata "
                 "solo se le verifiche preliminari sono state "
                 "compiute con la diligenza propria del pubblico "
                 "ufficiale. Ogni omissione documentale espone "
                 "le parti a rischi di nullità o annullabilità "
                 "successiva al rogito."),
            ],
        },
        {
            "slug":     "successioni-famiglia-orientamento",
            "kicker":   "Successioni",
            "title":    "Successioni in famiglia · orientarsi senza confusione fra dichiarazione, accettazione e divisione",
            "date":     "Febbraio 2026",
            "read_min": "8",
            "author":   "Notaio dott. Stefano Verri",
            "lede":
                "I passaggi reali della successione mortis causa nel "
                "diritto italiano. Dall'apertura della successione "
                "alla dichiarazione presso l'Agenzia delle Entrate, "
                "passando per la pubblicazione del testamento "
                "olografo, l'accettazione con beneficio d'inventario "
                "e la divisione ereditaria. Quando serve l'atto "
                "notarile, quando basta la scrittura privata.",
            "body": [
                ("p",
                 "La successione si apre al momento della morte "
                 "del de cuius nel luogo del suo ultimo domicilio "
                 "ai sensi dell'art. 456 c.c. Da questo istante "
                 "decorrono i termini per la dichiarazione di "
                 "successione (dodici mesi) e per le eventuali "
                 "rinunce o accettazioni con beneficio d'inventario."),
                ("h2", "Dichiarazione di successione"),
                ("p",
                 "Lo studio predispone la dichiarazione di "
                 "successione da presentare all'Agenzia delle "
                 "Entrate nei dodici mesi successivi all'apertura "
                 "della successione. La dichiarazione contiene "
                 "l'elenco dei beni del de cuius, dei chiamati "
                 "all'eredità e delle eventuali passività deducibili."),
                ("h2", "Quando serve l'atto notarile"),
                ("p",
                 "L'atto notarile è necessario per la pubblicazione "
                 "del testamento olografo ai sensi dell'art. 620 "
                 "c.c., per l'accettazione di eredità con beneficio "
                 "d'inventario ex art. 484 c.c., per la divisione "
                 "ereditaria di beni immobili e per le rinunce "
                 "all'eredità contenenti beni immobili."),
            ],
        },
        {
            "slug":     "costituzione-srl-semplificata-passaggi-reali",
            "kicker":   "Atti societari",
            "title":    "Costituzione di s.r.l. semplificata · i passaggi reali oltre la modulistica",
            "date":     "Dicembre 2025",
            "read_min": "7",
            "author":   "Notaio dott. Andrea Sironi",
            "lede":
                "La costituzione di s.r.l. semplificata ex art. "
                "2463-bis c.c. è in apparenza una procedura standard "
                "a costo ridotto. Nei fatti l'atto pubblico richiede "
                "una serie di valutazioni preliminari che lo "
                "schema-tipo non copre: oggetto sociale, "
                "amministrazione, conferimenti, modalità di "
                "convocazione dell'assemblea.",
            "body": [
                ("p",
                 "La s.r.l. semplificata, introdotta dal D.L. 1/2012, "
                 "rappresenta una versione a costo notarile ridotto "
                 "(onorari notarili azzerati per la costituzione, "
                 "imposta di registro ridotta) della s.r.l. "
                 "ordinaria. Lo statuto è conforme al modello "
                 "ministeriale e non può essere modificato in fase "
                 "di costituzione."),
                ("h2", "Le scelte preliminari"),
                ("p",
                 "Nonostante lo statuto-tipo, restano da definire "
                 "alcune scelte rilevanti: l'oggetto sociale (che "
                 "deve essere lecito e determinato), la composizione "
                 "dell'organo amministrativo (amministratore unico o "
                 "consiglio di amministrazione), la durata della "
                 "società, le modalità di convocazione dell'assemblea, "
                 "i conferimenti in denaro dei soci."),
                ("h2", "L'atto pubblico costitutivo"),
                ("p",
                 "L'atto costitutivo è ricevuto in forma di atto "
                 "pubblico ai sensi dell'art. 2463-bis comma 2 c.c. "
                 "e iscritto al Registro delle Imprese a cura del "
                 "notaio entro venti giorni dalla stipula. La "
                 "lettura ai soci comparenti è integrale, in "
                 "italiano o nella lingua scelta fra quelle in cui "
                 "il notaio è abilitato."),
            ],
        },
        {
            "slug":     "donazione-coniugi-riforma-2024",
            "kicker":   "Donazioni",
            "title":    "Donazione fra coniugi · cosa cambia con la riforma del 2024 e con la circolare 32/E",
            "date":     "Ottobre 2025",
            "read_min": "10",
            "author":   "Notaio dott.ssa Maria Beatrice Conti",
            "lede":
                "La donazione fra coniugi è atto pubblico tipico ai "
                "sensi degli artt. 769 e ss. c.c. Le modifiche "
                "normative del 2024 e la circolare 32/E "
                "dell'Agenzia delle Entrate hanno chiarito alcuni "
                "profili applicativi sull'imposta sulle donazioni, "
                "sulle franchigie e sulla revocabilità per "
                "sopravvenienza di figli.",
            "body": [
                ("p",
                 "La donazione fra coniugi è disciplinata dagli "
                 "artt. 769 e ss. del codice civile ed è soggetta "
                 "alla forma dell'atto pubblico a pena di nullità "
                 "ex art. 782 c.c. La franchigia per l'imposta "
                 "sulle donazioni fra coniugi è di un milione di "
                 "euro per ciascun donatario."),
                ("h2", "Riserva di usufrutto e nuda proprietà"),
                ("p",
                 "Una scelta comune nelle donazioni immobiliari fra "
                 "coniugi è la donazione della nuda proprietà con "
                 "riserva di usufrutto in capo al donante. "
                 "L'operazione, perfettamente legittima ex art. "
                 "796 c.c., permette al donante di conservare il "
                 "godimento del bene mantenendone le rendite."),
                ("h2", "Revocabilità per sopravvenienza di figli"),
                ("p",
                 "La donazione è revocabile per sopravvenienza di "
                 "figli ex art. 803 c.c. quando il donante, al "
                 "tempo dell'atto, non aveva figli o discendenti. "
                 "La revocabilità si estende ai figli adottati con "
                 "adozione legittimante intervenuti dopo la "
                 "donazione."),
            ],
        },
        {
            "slug":     "procura-art-1387-cc-quando-serve",
            "kicker":   "Procure",
            "title":    "Procura ai sensi dell'art. 1387 c.c. · quando serve e come si redige (con apostille)",
            "date":     "Luglio 2025",
            "read_min": "6",
            "author":   "Notaio dott.ssa Maria Beatrice Conti",
            "lede":
                "La procura è atto con cui il rappresentato "
                "conferisce al rappresentante il potere di "
                "compiere uno o più atti giuridici in suo nome. "
                "Quando l'atto da compiersi richiede la forma "
                "dell'atto pubblico — ad esempio una compravendita "
                "immobiliare — anche la procura deve essere "
                "ricevuta in forma di atto pubblico.",
            "body": [
                ("p",
                 "L'art. 1387 c.c. disciplina i casi in cui la "
                 "procura è necessaria per compiere atti giuridici "
                 "in nome del rappresentato. Per il principio di "
                 "simmetria formale (art. 1392 c.c.), la procura "
                 "deve avere la stessa forma richiesta per l'atto "
                 "che il rappresentante deve compiere."),
                ("h2", "Procura speciale e generale"),
                ("p",
                 "La procura speciale conferisce il potere di "
                 "compiere un atto determinato (ad esempio: la "
                 "vendita di un immobile preciso). La procura "
                 "generale conferisce il potere di compiere tutti "
                 "gli atti rientranti in una categoria (ad "
                 "esempio: tutti gli atti di ordinaria "
                 "amministrazione del patrimonio del rappresentato)."),
                ("h2", "Procure trilingui e apostille"),
                ("p",
                 "Per gli atti da compiersi all'estero, lo studio "
                 "redige procure in italiano e nella lingua del "
                 "paese di destinazione (inglese o francese) ai "
                 "sensi dell'art. 54 Legge Notarile. L'apostille "
                 "ai sensi della Convenzione dell'Aja del 1961 "
                 "viene apposta a cura del Procuratore della "
                 "Repubblica presso il Tribunale di Milano."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════════════
    # CONTATTI (contact) — sede unica milanese, form orientamento
    # ════════════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Primo incontro di orientamento · gratuito · non vincolante",
        "headline": "Trenta minuti con un <em>notaio</em> per inquadrare l'atto.",
        "intro":
            "Il primo incontro avviene direttamente con uno dei tre "
            "notai dell'associazione. Si discute la tipologia di "
            "atto, l'elenco dei documenti preliminari da raccogliere "
            "e la tabella degli onorari notarili applicabili. "
            "L'incontro dura circa trenta minuti, è gratuito e non "
            "vincola a nessun adempimento successivo.",

        # Form fields
        "form_label":   "Modulo di richiesta",
        "form_heading": "Richieda un primo incontro di orientamento",
        "form_intro":
            "Riceverà conferma di ricezione entro quarantotto ore "
            "lavorative dalla segreteria dello studio, con la "
            "proposta di tre fasce orarie disponibili e l'indicazione "
            "del notaio responsabile della tipologia di atto. I dati "
            "vengono trattati ai sensi del Regolamento UE 679/2016 "
            "e custoditi su sistemi conformi alle linee guida del "
            "Consiglio Nazionale del Notariato.",
        "form_fields": [
            {"name": "name", "label": "Nome", "type": "text", "required": True,
             "placeholder": "Es. Anna",
             "helper": "Solo il nome di battesimo, come compare nel documento di identità."},
            {"name": "surname", "label": "Cognome", "type": "text", "required": True,
             "placeholder": "Es. Bianchi",
             "helper": "Come compare nel documento di identità del comparente."},
            {"name": "email", "label": "Indirizzo email", "type": "email", "required": True,
             "placeholder": "anna.bianchi@esempio.it",
             "helper": "Per la corrispondenza preliminare. Non utilizziamo l'indirizzo per altri scopi."},
            {"name": "phone", "label": "Telefono", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Linea diretta del referente per gli accordi sull'orario."},
            {"name": "capacity", "label": "In qualità di", "type": "select", "required": True,
             "options": [
                 "Privato cittadino",
                 "Imprenditore o socio di società",
                 "Amministratore di società",
                 "Erede o legatario",
                 "Professionista (commercialista, avvocato, agente immobiliare)",
                 "Istituto di credito o assicurazione",
             ],
             "helper": "Per orientare il colloquio e individuare il notaio responsabile."},
            {"name": "act_type", "label": "Tipologia di atto", "type": "select", "required": True,
             "options": [
                 "Da definire in colloquio",
                 "Rogito di compravendita immobiliare",
                 "Mutuo ipotecario o surroga",
                 "Successione o dichiarazione di successione",
                 "Testamento pubblico o pubblicazione olografo",
                 "Costituzione di società o atto societario",
                 "Fusione, scissione o trasformazione",
                 "Donazione o patto di famiglia",
                 "Procura speciale o generale",
                 "Autentica di firma o copia conforme",
             ],
             "helper": "Scelga \"Da definire\" se la tipologia non è ancora chiara."},
            {"name": "timing", "label": "Tempi indicativi", "type": "select", "required": True,
             "options": [
                 "Entro un mese",
                 "Entro tre mesi",
                 "Entro sei mesi",
                 "Esplorativo, nessuna scadenza definita",
             ],
             "helper": "Per calendarizzare il primo incontro e l'iter dell'atto."},
            {"name": "language", "label": "Lingua del rogito (se rilevante)", "type": "select", "required": False,
             "options": [
                 "Italiano",
                 "Italiano con traduzione in inglese",
                 "Italiano con traduzione in francese",
                 "Da valutare in colloquio",
             ],
             "helper": "Lo studio riceve atti pubblici in italiano, inglese e francese."},
            {"name": "scope", "label": "Breve descrizione dell'atto",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Massimo 600 caratteri. Indicare in via sintetica "
                 "l'oggetto dell'atto (ad esempio: \"compravendita "
                 "di appartamento sito in Milano, lato venditore\"). "
                 "I dati dei terzi vengono raccolti solo in sede di "
                 "incontro, mai in questo modulo.",
             "helper":
                 "Quanto basta a inquadrare la tipologia di atto e "
                 "indirizzare la pratica al notaio responsabile. "
                 "I dettagli si discutono in sede di primo incontro."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona che parteciperà al primo incontro come comparente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Posizione",
             "meta": "Per indirizzare la richiesta al notaio responsabile.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Tipologia di atto",
             "meta":
                 "Nessun dato di terzi qui — i nominativi di "
                 "controparti, eredi o conferenti si raccolgono "
                 "in sede di primo incontro.",
             "fields": ["act_type", "timing", "language", "scope"]},
            {"num": "04", "title": "Documenti preliminari (facoltativi)",
             "meta":
                 "Visure catastali, atti precedenti, planimetrie o "
                 "bozze possono velocizzare l'inquadramento.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Documenti preliminari",
            "helper":
                "Visure catastali, atti di provenienza, planimetrie, "
                "bozze di statuto. PDF / DOCX · max 15 MB complessivi. "
                "I documenti sono custoditi su archivio cifrato "
                "secondo le linee guida del Consiglio Nazionale "
                "del Notariato.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Trascini qui i documenti oppure",
            "link":     "selezioni dall'archivio",
            "meta":     "PDF / DOCX · max 15 MB · archivio cifrato",
        },

        "form_submit_label": "Richiedi un primo incontro",
        "form_submit_note":
            "Conferma di ricezione entro quarantotto ore lavorative "
            "con la proposta di tre fasce orarie. Nessuna automazione "
            "commerciale, nessun BDR, nessuna comunicazione di "
            "marketing successiva.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi "
            "del Regolamento UE 679/2016 e dichiaro di essere "
            "informato che i dati vengono custoditi su sistemi "
            "conformi alle linee guida del Consiglio Nazionale del "
            "Notariato e dell'Archivio Notarile. I dati non vengono "
            "comunicati a terzi senza esplicito consenso scritto "
            "del comparente.",

        # Office meta-row labels
        "office_address_label": "Indirizzo",
        "office_area_label":    "Zona",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",
        "office_hours_label":   "Orario",

        # Sidebar — sede unica, canali diretti
        "offices_label":   "La sede",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Sede unica dello studio",
                "address": "Via Manin 12 · 20121",
                "area":    "Porta Nuova · a 200 metri da Repubblica M3",
                "phone":   "+39 02 7641 1898",
                "email":   "studio@notaiconti-sironi-verri.it",
                "hours":   "Lun – Ven · 09:00 – 18:30",
            },
        ],

        "channels_label": "Canali diretti",
        "channels": [
            ("Segreteria dello studio",
             "+39 02 7641 1898",
             "Lun – Ven · 09:00 – 18:30"),
            ("Email istituzionale",
             "studio@notaiconti-sironi-verri.it",
             "Risposta entro 48 ore lavorative"),
            ("PEC certificata",
             "studio.contisironi@postacertificata.notariato.it",
             "Per atti, notifiche e depositi telematici"),
        ],

        "footnote":
            "Lo Studio Notarile Conti–Sironi–Verri non rilascia "
            "pareri vincolanti via email senza un primo incontro "
            "di orientamento con uno dei tre notai dell'associazione. "
            "La tabella degli onorari notarili applicabili al caso "
            "concreto viene comunicata per iscritto al termine del "
            "primo incontro, prima di qualsiasi conferimento "
            "formale di incarico.",
    },
}


# ─────────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract.
# Every visible string in the lawyer/classic-gold skin templates
# must come from THIS file (or from chrome.* / dna.content.*).
# Zero literal "Conti", "Sironi", "Verri", "2007", "Milano",
# "via Manin", notai names, headline text, or other brand-specific
# strings in the .html files. The skin is reused verbatim from Lex —
# the distinctness lives in the content tree, not in the templates.
# ─────────────────────────────────────────────────────────────────────
