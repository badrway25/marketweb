# Phase 2g3.7 · Session 53 · Juris Avv. Martini & Partners — modern-transparent archetype.
# Advisory-modern tone.
#
# Editorial identity: advisory boutique legale moderna con sede a Milano
# (Solferino 40) + uffici a Torino e Bologna. Voice: prima persona plurale
# ("Noi"), strategica, orientata alla soluzione, tech-forward. Differenziata
# in modo netto da Lex (serif Cormorant, retaggio 62 anni, consulenza
# riservata): Juris è sans DM Sans, fondato 2018, partner giovani, dashboard
# condivisa, tariffe chiare, "strategy call" non "consulenza".
#
# Differentiation vs Lex (10-gate D-054):
#  1. Typography:       DM Sans + Inter (kinetic sans)
#                       vs Lex Cormorant serif (forensic)
#  2. Palette:          Slate #2D3748 + confident blue + gold-yellow
#                       vs Lex ink black + gold + bordeaux
#  3. Navbar:           floating pill with wordmark + blue CTA
#                       vs Lex ink crest bar with gold underline
#  4. Hero:             centered manifesto, NO big photo
#                       vs Lex split ledger with forensic portrait
#  5. Card style:       advisory-sector-pill (rounded blue outline)
#                       vs Lex practice-area numbered ledger rows
#  6. Section order:    sector grid → process sprint → metrics → insights
#                       vs Lex heritage → practice → ledger → doctrine
#  7. Primary CTA:      "Prenota una strategy call" + next-slot chip
#                       vs Lex "Richiedi una consulenza riservata" + dossier
#  8. Heritage pitch:   founded 2018, young partners, tech-forward
#                       vs Lex 62-year heritage, senior partner prof. title
#  9. Imagery:          bright modern meeting rooms, glass, laptops
#                       vs Lex ink archive, leather-bound codes, mahogany
# 10. Forms:            3-step intake with company-stage picker + next-slot
#                       vs Lex confidential form with NDA pre-notice
#
# D-047 compliance: the file hosts ALL literal copy. Skin files never
# hardcode a single user-facing string. Every sector name, partner name,
# office address, form label is either a key of this tree or a structural
# token like data-lm="counter".
from __future__ import annotations

from typing import Any


JURIS_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Home",       "kind": "home"},
        {"slug": "approccio",  "label": "Approccio",  "kind": "about"},
        {"slug": "servizi",    "label": "Servizi",    "kind": "services"},
        {"slug": "settori",    "label": "Settori",    "kind": "team"},
        {"slug": "insights",   "label": "Insights",   "kind": "blog_list"},
        {"slug": "contatti",   "label": "Contatti",   "kind": "contact"},
    ],

    # Site-wide chrome
    "site": {
        "logo_initial": "M",
        "logo_word":    "Martini & Partners",
        "tag":          "Advisory legale · dal 2018",
        "phone":        "hello@martinipartners.legal",
        "email":        "hello@martinipartners.legal",
        "address":      "Via Solferino 40 · 20121 Milano",
        "hours_compact":"Strategy call · Lun – Ven · 09:00 – 19:00",
        "hours_footer_rows": [
            "Video call dal nostro dashboard",
            "Risposta entro 2 ore lavorative",
        ],
        "license":      "Iscr. Ordine Avvocati Milano MI18224 · P.IVA 10123540967",
        "nav_cta":      "Prenota una strategy call",
        "footer_intro":
            "Martini & Partners è lo studio che unisce diritto, tecnologia e "
            "strategia per startup, PMI e professionisti. Tariffe chiare, "
            "tempi definiti, un dashboard condiviso.",
        "foot_studio":  "Lo studio",
        "foot_pages":   "Pagine",
        "foot_contact": "Contatti",
        "foot_offices": "Uffici",
        "offices_footer_rows": [
            "Milano · via Solferino 40",
            "Torino · via Roma 324",
            "Bologna · via Indipendenza 18",
        ],
        # Cross-page meta labels (blog/insights detail)
        "post_date_label":    "Pubblicato",
        "post_reading_label": "Lettura",
        "post_author_label":  "A cura di",
        "post_topic_label":   "Area",
        "post_back_label":    "Tutti gli insights",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Martini & Partners · Milano · Torino · Bologna",
        "headline":    "Il diritto, <em>dalla tua parte.</em>",
        "intro":
            "Affianchiamo startup, PMI e professionisti nelle decisioni "
            "legali che contano — con tempi chiari, tariffe trasparenti e "
            "un dashboard condiviso dove segui l'avanzamento del tuo caso.",
        "primary_cta":    "Prenota una strategy call",
        "primary_href":   "contatti",
        "secondary_cta":  "Come lavoriamo",
        "secondary_href": "approccio",

        # Sprint chip — fixed pinned "prossimo slot"
        "sprint_chip":     "Strategy call · prossimo slot 17 aprile",
        "sprint_chip_cta": "Prenota →",

        # Sector grid — 6 cells
        "sectors_label":   "Settori",
        "sectors_heading": "Sei aree, un solo <em>metodo</em>.",
        "sectors_intro":
            "Ogni settore è seguito da una coppia partner + legal ops. "
            "Il primo partner con cui parli è lo stesso che firma il mandato "
            "— niente passaggi di mano, niente BDR.",
        "sectors": [
            ("01", "Startup & Tech",
             "Fundraising, cap table, IP, compliance GDPR e AI Act per aziende digitali."),
            ("02", "PMI & Famiglia",
             "Passaggio generazionale, governance, patti parasociali e M&A mid-market."),
            ("03", "Lavoro & HR",
             "Contratti, licenziamenti, welfare, stock option e remote-work internazionale."),
            ("04", "Contrattualistica B2B",
             "SaaS, licensing, partnership, vendor due-diligence e MSA in inglese."),
            ("05", "Dispute resolution",
             "Mediazione, arbitrato, ADR e contenzioso strategico."),
            ("06", "Privacy & AI",
             "GDPR, AI Act, data mapping, DPIA e policy per aziende data-driven."),
        ],

        # Process sprint — S.01 / S.02 / S.03
        "process_label":   "Come lavoriamo",
        "process_heading": "Dal brief al <em>primo atto</em> in due settimane.",
        "process_intro":
            "Non vendiamo ore, vendiamo risultati. Il metodo è lo stesso per "
            "ogni cliente — dalla seed che fa il primo round alla PMI al "
            "quarto mandato di fila. Tre passi, zero mistero.",
        "process": [
            ("S.01", "Discovery call",
             "30 min via video · capiamo il problema, non vendiamo il servizio."),
            ("S.02", "Offerta chiara",
             "Tempi, fasi, costo fisso o a consumo — tutto scritto, zero sorprese."),
            ("S.03", "Dashboard live",
             "Segui in tempo reale atti, scadenze, documenti e ore lavorate."),
        ],

        # Outcome metrics band — counter-animated
        "metric_label":    "I numeri dello studio",
        "metric_heading":  "Otto anni sul campo, tre città, cento mandati l'anno.",
        "metric_strip": [
            ("180+", "aziende assistite"),
            ("14",   "giorni · tempo medio primo atto"),
            ("4.9",  "★ soddisfazione clienti"),
            ("0",    "€ setup fee, sempre"),
        ],

        # Trust band — client wordmarks (anonymized sector references)
        "trust_label": "Abbiamo seguito negli ultimi dodici mesi",
        "trust_logos": [
            "UNA FINTECH MILANESE · SEED ROUND",
            "UN GRUPPO FAMIGLIA VENETO · PASSAGGIO",
            "UN SAAS B2B TORINESE · SERIE A",
            "UNA PMI BOLOGNESE · M&A CROSS-BORDER",
            "UN MARKETPLACE ROMANO · POLICY AI",
            "UNA SCALE-UP FIRENZE · STOCK OPTION",
        ],

        # Insights preview — 3 recent articles with CTA to full list
        "insights_label":   "Insights · ultima settimana",
        "insights_heading": "Cosa leggiamo <em>in studio</em>.",
        "insights_intro":
            "Le note che scriviamo quando una norma cambia. Le leggono i "
            "nostri clienti la mattina, con il caffè — nessuna newsletter, "
            "nessun lead magnet.",
        "insights_link":    "Tutti gli insights →",
        "insights_link_href":"insights",
        "insights": [
            ("17 apr", "AI Act · cosa cambia per le PMI italiane",           "ai-act-pmi-italiane"),
            ("14 apr", "Stock option 2026 · nuova disciplina fiscale",       "stock-option-2026"),
            ("11 apr", "Smart-working oltre confine · tre scenari",           "smart-working-confine"),
        ],

        # Final CTA — glass panel with primary blue pill
        "cta_label":     "Pronti a parlarne?",
        "cta_heading":   "Trenta minuti, video call, niente impegno.",
        "cta_intro":
            "Il primo incontro è con un partner, non con un BDR. "
            "Se il problema non è di nostra competenza, ti indirizziamo "
            "allo studio giusto — anche se non lavori con noi.",
        "cta_primary":      "Prenota una strategy call",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Leggi il nostro metodo",
        "cta_secondary_href":"approccio",
    },

    # ─── APPROCCIO (about) ──────────────────────────────────────
    "approccio": {
        "eyebrow":  "Il nostro metodo · 2018 — 2026",
        "headline": "Non vendiamo ore, <em>vendiamo risultati.</em>",
        "intro":
            "Siamo nati nel 2018 da un'insoddisfazione concreta — due partner "
            "che avevano lavorato per dieci anni in studi d'affari milanesi "
            "internazionali e non sopportavano più il modello a parcella "
            "oraria, i junior parcheggiati e i dashboard legali degli anni "
            "Novanta. Abbiamo aperto Martini & Partners per farlo diversamente.",

        # Manifesto — 4 principles in card grid
        "manifesto_label":   "Manifesto",
        "manifesto_heading": "Quattro principi, <em>non negoziabili</em>.",
        "manifesto_intro":
            "Li scriviamo in prima pagina del mandato. Non sono slogan, "
            "sono regole operative — se saltano questi quattro, non lavoriamo "
            "con voi (o voi non lavorate più con noi).",
        "manifesto": [
            ("01", "Prima il problema, poi la parcella",
             "La discovery call è gratuita. Scriviamo l'offerta solo dopo aver "
             "capito se il problema è nostro e se la soluzione vale la parcella. "
             "Se non è nostro campo, vi indirizziamo allo studio giusto — anche "
             "senza compenso di segnalazione."),
            ("02", "Tariffa scritta, mai oraria",
             "Ogni mandato ha un costo fisso o un tetto massimo. La parcella "
             "oraria la usiamo solo per urgenze non pianificabili, sempre "
             "comunicata prima di iniziare. Nessuna nota spese a sorpresa, "
             "nessuna voce generica \"studio pratica\"."),
            ("03", "Un partner, dal primo atto all'ultimo",
             "Il partner che incontri in discovery è lo stesso che firma "
             "l'atto finale. Il team cambia per specializzazione, non per "
             "seniorità — non avrete mai un junior che non conoscete sul vostro "
             "fascicolo senza averlo approvato in anticipo."),
            ("04", "Dashboard condiviso, sempre",
             "Ogni cliente ha un workspace dedicato con stato delle pratiche, "
             "documenti, atti depositati, ore lavorate e timeline delle scadenze. "
             "Non spediamo PDF via email — tutto passa per il dashboard, "
             "sempre aggiornato, sempre esportabile."),
        ],

        # Story — studio timeline
        "story_label":   "La storia",
        "story_heading": "Otto anni, tre città, un solo metodo.",
        "story": [
            ("2018", "Fondazione a Milano",
             "Giorgia Martini (ex-DLA Piper) e Davide Romano (ex-Bird & Bird) "
             "aprono lo studio in via Solferino con tre mandati già firmati "
             "da ex-clienti della loro esperienza precedente."),
            ("2020", "Primo dashboard interno",
             "Costruiamo con un product manager ex-Zalando la prima versione "
             "del dashboard cliente. Nasce l'idea di farlo diventare la "
             "differenza del metodo Martini & Partners."),
            ("2022", "Apertura desk Torino",
             "Apriamo il secondo ufficio a Torino per seguire da vicino "
             "i mandati con scale-up piemontesi — da quella sede passano "
             "oggi la metà dei mandati startup dello studio."),
            ("2024", "Apertura desk Bologna",
             "Il terzo desk a Bologna presidia il corridoio Emilia-Romagna "
             "con focus su PMI familiari e M&A mid-market. Nel 2025 arrivano "
             "anche le prime pratiche AI Act."),
            ("2026", "Studio a dimensione corrente",
             "Oggi siamo in otto avvocati + due legal ops. Non pensiamo di "
             "crescere oltre — preferiamo selezionare i mandati piuttosto "
             "che aprire un quarto ufficio."),
        ],

        # Dashboard screenshot description — visual teaser
        "dashboard_label":   "Il dashboard cliente",
        "dashboard_heading": "Segui il tuo mandato come <em>segui un deploy</em>.",
        "dashboard_intro":
            "Ogni cliente ha accesso a un workspace cifrato con le sue "
            "pratiche, i documenti, le scadenze e le ore effettivamente "
            "lavorate. Ispirato più a Linear che a un portale legale — "
            "perché lavoriamo per persone che nel loro mestiere usano Linear.",
        "dashboard_features": [
            ("Stato delle pratiche",  "Ogni fascicolo ha un kanban con stato · owner · prossima scadenza."),
            ("Documenti versionati",  "Atti depositati, bozze, allegati — con history e commenti inline."),
            ("Ore lavorate, in chiaro","Le ore di ogni partner e legal ops, aggiornate ogni venerdì sera."),
            ("Scadenze calendario",    "Ogni scadenza è un evento · puoi sincronizzarla con Google Calendar."),
            ("Export fiscale",         "Un click per l'estrazione fattura + note spese per il commercialista."),
            ("Accesso condiviso",      "Inviti il CFO, il CEO, il commercialista — con permessi granulari."),
        ],
        # Decorative dashboard mock — kanban columns + sidebar items rendered
        # in the aria-hidden UI preview. Lifted here for D-047 strictness and
        # so each locale renders the mock in its own register.
        "dashboard_mock": {
            "url":         "martini-partners.dashboard",
            "sidebar":     ["Pratiche", "Atti", "Ore", "Scadenze", "Team"],
            "sidebar_active_index": 0,
            "columns": [
                {"label": "Discovery",
                 "cards": [
                     {"title": "Fintech · seed",      "accent": False},
                     {"title": "PMI · passaggio",     "accent": False},
                 ]},
                {"label": "Live",
                 "cards": [
                     {"title": "Scale-up · Serie A",  "accent": True},
                     {"title": "SaaS · MSA",          "accent": False},
                     {"title": "M&A · due diligence", "accent": False},
                 ]},
                {"label": "Closing",
                 "cards": [
                     {"title": "HR · stock option",   "accent": False},
                 ]},
            ],
        },

        # Founders — 2 managing partners on about
        "founders_label":   "Fondatori",
        "founders_heading": "Due avvocati, <em>un'idea condivisa</em>.",
        "founders": [
            {
                "name":  "Avv. Giorgia Martini",
                "role":  "Managing partner · Startup & Tech",
                "bio":
                    "Dodici anni in DLA Piper Milano, dipartimento corporate. "
                    "Ha chiuso due Series A con fondi italiani e un round "
                    "cross-border con Orange Ventures. Coordina la pratica "
                    "startup e il desk Milano.",
                "credentials": [
                    "Bocconi (Giurisprudenza '10)",
                    "LL.M. NYU '13",
                    "Membro Italian Tech Alliance",
                ],
            },
            {
                "name":  "Avv. Davide Romano",
                "role":  "Co-founder · Contrattualistica B2B",
                "bio":
                    "Dieci anni in Bird & Bird, dipartimento tech & comms. "
                    "Specializzato in SaaS licensing, MSA cross-border e "
                    "contrattualistica per piattaforme marketplace. "
                    "Coordina il desk Torino e la pratica AI Act.",
                "credentials": [
                    "Sapienza (Giurisprudenza '11)",
                    "LL.M. Fordham '14",
                    "Contributor AIGA",
                ],
            },
        ],

        # Coordinates strip
        "offices_label": "Le sedi",
        "offices": [
            ("Milano",   "Via Solferino 40 · 20121 · Brera",           "Quartier generale · tutte le practice"),
            ("Torino",   "Via Roma 324 · 10123 · Centro",              "Desk scale-up + corridor piemontese"),
            ("Bologna",  "Via Indipendenza 18 · 40121 · Centro",       "Desk PMI + corridor Emilia-Romagna"),
        ],

        # Page CTA
        "cta_heading": "Vuoi vedere il dashboard dal vivo?",
        "cta_intro":
            "La discovery call include un walkthrough del workspace cliente. "
            "Ti mostriamo come è fatto, cosa vedi, cosa esporti e come lo "
            "integriamo con i tuoi strumenti (Notion, Slack, Google Workspace).",
        "cta_primary":      "Prenota la discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── SERVIZI (services) ─────────────────────────────────────
    "servizi": {
        "eyebrow":  "Servizi · 2026",
        "headline": "Sette offerte, <em>tempi certi</em>, prezzi dichiarati.",
        "intro":
            "Le sette offerte dello studio. Ogni offerta ha un perimetro "
            "scritto, una timeline indicativa e un costo fisso o a tetto. "
            "Niente listino orario generico, niente \"da definire in call\".",

        # Card meta labels
        "svc_duration_label": "Durata",
        "svc_price_label":    "Prezzo",
        "svc_deliverables_label": "Cosa consegniamo",
        "svc_engagement_label":   "Modalità",

        # 7 services — rich cards
        "services": [
            {
                "num":   "01",
                "title": "Startup Legal Sprint",
                "blurb":
                    "Tutto il setup legale per una startup che chiude il seed round "
                    "in tre settimane — statuto, patti parasociali, term sheet, "
                    "onboarding investitori e cap table pulito.",
                "deliverables": [
                    "Statuto e patti parasociali personalizzati",
                    "Term sheet e SAFE/CLN review",
                    "Cap table aggiornato su Ledgy o Capdesk",
                    "Onboarding dei primi investitori in call",
                ],
                "duration":   "3 settimane",
                "price":      "€ 6.500 tutto incluso",
                "engagement": "Fisso · 60% al via · 40% a closing round",
                "tier":       "Seed-ready",
            },
            {
                "num":   "02",
                "title": "M&A Advisory PMI",
                "blurb":
                    "Affianchiamo PMI familiari in operazioni straordinarie — "
                    "cessione quote, ingresso di fondi, M&A cross-border italo-DACH. "
                    "Lato vendor o acquirer, mai entrambi nel medesimo dossier.",
                "deliverables": [
                    "Due diligence legale e fiscale",
                    "Valutazione e draft SPA",
                    "Negoziazione e assistenza al closing",
                    "Post-closing · integrazione 100 giorni",
                ],
                "duration":   "12 – 24 settimane secondo perimetro",
                "price":      "€ 45.000 base + success fee 0.8%",
                "engagement": "Misto · fisso base + success fee a closing",
                "tier":       "Mid-market",
            },
            {
                "num":   "03",
                "title": "Contract-as-a-Service B2B",
                "blurb":
                    "Per SaaS e scale-up che firmano MSA ogni settimana — un team "
                    "dedicato gestisce redazione, negoziazione e archivio "
                    "contrattuale. Un canale Slack, un SLA di 48 ore, tariffa mensile.",
                "deliverables": [
                    "MSA / DPA / SOW templates personalizzati",
                    "Negoziazione redline con controparti",
                    "Archivio contratti su Notion o Juro",
                    "Report mensile con KPI tempi e volumi",
                ],
                "duration":   "Abbonamento mensile · minimo 6 mesi",
                "price":      "Da € 3.200 / mese",
                "engagement": "Ricorrente · canale Slack + dashboard",
                "tier":       "Scale-ready",
            },
            {
                "num":   "04",
                "title": "Privacy & AI Act Readiness",
                "blurb":
                    "Audit completo GDPR + mapping rischi AI Act per aziende "
                    "data-driven. DPIA, registro trattamenti, policy interne, "
                    "formazione team e readiness report per CdA o investitori.",
                "deliverables": [
                    "GDPR audit + registro trattamenti aggiornato",
                    "AI Act gap analysis e mapping classi di rischio",
                    "DPIA sui processi critici (max 4)",
                    "Training di due ore al team operativo",
                ],
                "duration":   "6 settimane",
                "price":      "€ 12.500 tutto incluso",
                "engagement": "Fisso · 50% al via · 50% a consegna report",
                "tier":       "Compliance",
            },
            {
                "num":   "05",
                "title": "Stock Option & Welfare",
                "blurb":
                    "Disegno e implementazione dei piani di stock option per "
                    "startup e scale-up — compreso il trattamento fiscale 2026 e "
                    "i profili employment law per contratti italiani e cross-border.",
                "deliverables": [
                    "Piano SO/SAR disegnato su misura",
                    "Regolamento interno + onboarding dipendenti",
                    "Trattamento fiscale 2026 documentato",
                    "Accordi con fondi per lock-up e tag-along",
                ],
                "duration":   "4 settimane",
                "price":      "€ 8.200 base + € 180 / dipendente onboard",
                "engagement": "Fisso + per-seat su onboarding",
                "tier":       "Scale-ready",
            },
            {
                "num":   "06",
                "title": "Dispute Resolution",
                "blurb":
                    "Mediazione, arbitrato e contenzioso strategico — privilegiamo "
                    "sempre la soluzione negoziale, ma quando è necessario "
                    "portare una causa in aula lo facciamo con partner dedicati.",
                "deliverables": [
                    "Assessment del contenzioso + strategy memo",
                    "Tentativo di mediazione o ADR",
                    "Assistenza in arbitrato o giudizio ordinario",
                    "Report settimanale stato della controversia",
                ],
                "duration":   "12 – 36 settimane secondo complessità",
                "price":      "Preventivo su perimetro scritto",
                "engagement": "Misto · fisso per fase + success fee",
                "tier":       "Protection",
            },
            {
                "num":   "07",
                "title": "Fractional General Counsel",
                "blurb":
                    "Un partner dedicato come General Counsel part-time per scale-up "
                    "e PMI che hanno ancora bisogno di competenza da studio senza "
                    "il costo del ruolo interno. Due-tre giorni al mese, presenza in CdA.",
                "deliverables": [
                    "Presenza fisica o in video call 2-3 gg / mese",
                    "Board book legale e risk dashboard trimestrale",
                    "Contratti principali + governance review",
                    "Escalation a tutti i desk Martini & Partners",
                ],
                "duration":   "Abbonamento trimestrale · minimo 12 mesi",
                "price":      "Da € 5.400 / mese",
                "engagement": "Ricorrente · presenza in CdA",
                "tier":       "Scale-ready",
            },
        ],

        # Process repeated here for services page
        "process_label":   "Come lavoriamo",
        "process_heading": "Dal brief al primo atto in due settimane.",
        "process": [
            ("S.01", "Discovery call", "30 min video · perimetro e fit."),
            ("S.02", "Offerta scritta", "Entro 5 gg · costi e timeline fissi."),
            ("S.03", "Dashboard live", "Kickoff in 48 ore · tutto tracciato."),
        ],

        # FAQ strip for services page
        "faq_label":   "Domande frequenti",
        "faq_heading": "Quello che ci chiedete in call.",
        "faq": [
            ("Accettate mandati con success fee variabile?",
             "Sì, ma solo su operazioni straordinarie (M&A, fundraising, exit). "
             "Su tutto il resto lavoriamo a costo fisso o abbonamento."),
            ("Come gestite i conflitti di interesse?",
             "Un conflict check è automatizzato nel dashboard. Non accettiamo "
             "mai due clienti in concorrenza diretta nello stesso settore. "
             "La verifica avviene prima della discovery call, non dopo."),
            ("Lavorate anche con freelance e professionisti singoli?",
             "Sì, ma solo su offerte specifiche — Stock Option, Privacy & AI, "
             "e Contrattualistica B2B. Sul resto preferiamo aziende con team."),
            ("Potete firmare un NDA in anticipo?",
             "Sì, inviaci il vostro NDA standard — lo rivediamo entro 24 ore. "
             "In alternativa, usiamo il nostro template reciproco, disponibile "
             "nel dashboard."),
        ],

        # Page CTA
        "cta_heading": "Non siete sicuri di quale offerta scegliere?",
        "cta_intro":
            "Scrivici perimetro e timeline — entro 24 ore ti indirizziamo "
            "all'offerta giusta (o ti diciamo che non è il nostro campo). "
            "Gratuito, senza impegno, risposta di un partner reale.",
        "cta_primary":      "Scrivici perimetro e timeline",
        "cta_primary_href": "contatti",
    },

    # ─── SETTORI (team kind — but rendered as sector pages) ─────
    "settori": {
        "eyebrow":  "Settori · dove ci muoviamo bene",
        "headline": "Sei settori, <em>un solo metodo</em>, partner dedicati.",
        "intro":
            "Ogni settore ha un partner responsabile e una legal ops di "
            "supporto. Il nostro \"settore\" non è un claim di marketing — è "
            "la lista di pratiche che abbiamo lavorato abbastanza da "
            "essere sicuri di non doverla imparare sul vostro caso.",

        # Sector cards — structure used by template
        "sectors_label":   "Le sei aree",
        "sectors_heading": "Dove <em>abbiamo già risolto</em> problemi come i vostri.",

        "sectors": [
            {
                "num":   "01",
                "title": "Startup & Tech",
                "tagline": "Per founder al primo round o al terzo.",
                "pain_points": [
                    "Cap table e patti parasociali da rimettere in ordine",
                    "SAFE, CLN, term sheet da rivedere prima di firmare",
                    "Stock option con trattamento fiscale 2026 corretto",
                    "Compliance GDPR + AI Act prima del pitch agli investitori",
                ],
                "signals": [
                    "8 Series A chiusi negli ultimi 24 mesi",
                    "3 exit gestiti lato vendor",
                    "Partner dedicato · Avv. Giorgia Martini",
                ],
                "case_snippet":
                    "Abbiamo seguito una fintech milanese nel seed round con "
                    "un fondo italiano + un business angel UK — cap table "
                    "pulito in tre settimane, closing in sei.",
                "partner":    "Avv. Giorgia Martini",
                "legal_ops":  "Elena Vasile · legal ops lead",
            },
            {
                "num":   "02",
                "title": "PMI & Famiglia",
                "tagline": "Per imprenditori di seconda o terza generazione.",
                "pain_points": [
                    "Passaggio generazionale con più rami familiari",
                    "Patti parasociali obsoleti o assenti",
                    "Ingresso di un fondo di minoranza nel capitale",
                    "Governance con CdA ancora informale",
                ],
                "signals": [
                    "14 passaggi generazionali chiusi dal 2019",
                    "5 ingressi fondo minority in PMI familiari",
                    "Partner dedicato · Avv. Chiara Belforte",
                ],
                "case_snippet":
                    "Un gruppo familiare veneto del tessile ci ha affidato "
                    "il passaggio a tre fratelli più un cugino di secondo grado — "
                    "patto parasociale chiuso in dodici settimane, zero cause "
                    "ereditarie aperte.",
                "partner":    "Avv. Chiara Belforte",
                "legal_ops":  "Matteo Orsi · legal ops",
            },
            {
                "num":   "03",
                "title": "Lavoro & HR",
                "tagline": "Per HR che devono muoversi veloci.",
                "pain_points": [
                    "Licenziamento individuale o collettivo da gestire",
                    "Smart-working cross-border (dipendenti in EU o UK)",
                    "Ristrutturazione con uscite incentivate",
                    "Stock option e welfare per scale-up",
                ],
                "signals": [
                    "40+ licenziamenti individuali chiusi in conciliazione",
                    "12 piani di uscita incentivata con impatto zero in causa",
                    "Partner dedicato · Avv. Sara Miccoli",
                ],
                "case_snippet":
                    "Una scale-up torinese ha ridotto la forza lavoro "
                    "del 18% senza una causa aperta — usando il nostro "
                    "metodo di conciliazione individuale su 34 posizioni.",
                "partner":    "Avv. Sara Miccoli",
                "legal_ops":  "Luca Tagliavini · legal ops",
            },
            {
                "num":   "04",
                "title": "Contrattualistica B2B",
                "tagline": "Per chi firma MSA ogni settimana.",
                "pain_points": [
                    "MSA / DPA / SOW da standardizzare",
                    "Negoziazione redline con clienti enterprise",
                    "Licensing SaaS con controparti USA",
                    "Archivio contratti frammentato o inesistente",
                ],
                "signals": [
                    "Canale Slack dedicato · SLA 48 ore",
                    "Template validati per 6 settori verticali",
                    "Partner dedicato · Avv. Davide Romano",
                ],
                "case_snippet":
                    "Un SaaS B2B torinese ci ha affidato l'intera "
                    "contrattualistica commerciale — da luglio 2024 firmiamo "
                    "ogni settimana un MSA enterprise con tempi medi di "
                    "8 giorni dalla prima bozza al signing.",
                "partner":    "Avv. Davide Romano",
                "legal_ops":  "Alice Piatti · legal ops",
            },
            {
                "num":   "05",
                "title": "Dispute Resolution",
                "tagline": "Per quando una trattativa va male.",
                "pain_points": [
                    "Contenzioso con fornitore o cliente enterprise",
                    "Arbitrato su clausola internazionale",
                    "Mediazione obbligatoria pre-causa",
                    "Crisis management reputazionale",
                ],
                "signals": [
                    "75% delle controversie chiuse senza sentenza",
                    "4 arbitrati ICC gestiti negli ultimi 24 mesi",
                    "Partner dedicato · Avv. Marco Trentini",
                ],
                "case_snippet":
                    "Una PMI bolognese con un contenzioso da 2.8 M € contro "
                    "un fornitore tedesco — chiuso in mediazione in 14 "
                    "settimane con un accordo transattivo più favorevole "
                    "della domanda iniziale.",
                "partner":    "Avv. Marco Trentini",
                "legal_ops":  "Irene Bonomi · legal ops",
            },
            {
                "num":   "06",
                "title": "Privacy & AI",
                "tagline": "Per aziende che lavorano con dati o modelli.",
                "pain_points": [
                    "GDPR audit prima di un round o di un M&A",
                    "AI Act gap analysis e mapping classi di rischio",
                    "DPIA su processi critici o modelli predittivi",
                    "Data breach response e notifica al Garante",
                ],
                "signals": [
                    "Prima DPIA AI Act italiana per marketplace B2C",
                    "6 audit GDPR pre-M&A con impatto zero sul deal",
                    "Partner dedicato · Avv. Giulia Masi",
                ],
                "case_snippet":
                    "Un marketplace romano ha adeguato la propria piattaforma "
                    "all'AI Act prima dell'entrata in vigore effettiva — "
                    "mapping completo, DPIA su 3 processi e policy pubblica "
                    "pronta, tutto in 6 settimane.",
                "partner":    "Avv. Giulia Masi",
                "legal_ops":  "Paolo Sangermano · legal ops",
            },
        ],

        # Team list — all 10 people on sector page
        "team_label":   "Il team completo",
        "team_heading": "Otto avvocati, <em>due legal ops</em>.",
        "team_intro":
            "Il team dello studio — i nomi che trovi sui fascicoli e nelle "
            "call. Non abbiamo junior-of-record: i senior siedono al tavolo "
            "dalla discovery al closing, i legal ops operano sul dashboard.",
        "team": [
            {"name": "Avv. Giorgia Martini",  "role": "Managing partner · Startup & Tech",        "office": "Milano",  "email": "giorgia@martinipartners.legal",
             "bio":  "12 anni DLA Piper · 2 Series A chiusi nel 2025."},
            {"name": "Avv. Davide Romano",    "role": "Co-founder · Contrattualistica B2B",       "office": "Torino",  "email": "davide@martinipartners.legal",
             "bio":  "10 anni Bird & Bird · LL.M. Fordham · AIGA contributor."},
            {"name": "Avv. Chiara Belforte",  "role": "Partner · PMI & Famiglia",                 "office": "Bologna", "email": "chiara@martinipartners.legal",
             "bio":  "15 anni in studio familiare emiliano · Bocconi."},
            {"name": "Avv. Sara Miccoli",     "role": "Partner · Lavoro & HR",                    "office": "Milano",  "email": "sara@martinipartners.legal",
             "bio":  "Ex responsabile labour department di boutique milanese."},
            {"name": "Avv. Marco Trentini",   "role": "Partner · Dispute resolution",             "office": "Milano",  "email": "marco@martinipartners.legal",
             "bio":  "Specializzato in arbitrati ICC e mediazione commerciale."},
            {"name": "Avv. Giulia Masi",      "role": "Partner · Privacy & AI",                    "office": "Milano",  "email": "giulia@martinipartners.legal",
             "bio":  "Ex Autorità Garante · dottorato su AI ethics."},
            {"name": "Avv. Tommaso Neri",     "role": "Senior associate · Startup & M&A",         "office": "Torino",  "email": "tommaso@martinipartners.legal",
             "bio":  "6 anni in boutique M&A milanese · focus scale-up tech."},
            {"name": "Avv. Beatrice Riva",    "role": "Senior associate · Contract-as-a-Service", "office": "Torino",  "email": "beatrice@martinipartners.legal",
             "bio":  "Specializzata in SaaS licensing cross-border · IAPP CIPP/E."},
            {"name": "Elena Vasile",          "role": "Legal ops lead",                           "office": "Milano",  "email": "elena@martinipartners.legal",
             "bio":  "Ex operations manager in scale-up logistics · progetta i flussi dashboard."},
            {"name": "Matteo Orsi",           "role": "Legal ops · PMI desk",                     "office": "Bologna", "email": "matteo@martinipartners.legal",
             "bio":  "Ex paralegale studio tributario bolognese · esperto archivistica pratiche."},
        ],

        # Page CTA
        "cta_heading": "Il vostro settore non è in questa lista?",
        "cta_intro":
            "Ci sono mandati che ci arrivano fuori dai sei settori — li "
            "accettiamo solo se abbiamo esperienza specifica o se "
            "co-lavoriamo con uno studio partner. Scriveteci il perimetro: "
            "in 24 ore vi diciamo se è il nostro campo.",
        "cta_primary":      "Raccontaci il caso",
        "cta_primary_href": "contatti",
    },

    # ─── INSIGHTS (blog_list) ───────────────────────────────────
    "insights": {
        "eyebrow":  "Insights · 2026",
        "headline": "Quando cambia una norma, <em>scriviamo una nota</em>.",
        "intro":
            "Non abbiamo una newsletter. Non abbiamo sequence di marketing. "
            "Quando una norma cambia o un caso arriva sulla scrivania "
            "qualcuno in studio scrive una nota — la pubblichiamo qui "
            "perché i nostri clienti ce la chiedono, e i nostri candidati "
            "la leggono prima del colloquio.",

        # Card meta
        "card_topic_label":   "Area",
        "card_author_label":  "A cura di",
        "card_reading_label": "Lettura",

        "posts_intro":
            "Sei note recenti. L'archivio completo è sul dashboard cliente "
            "— qui pubblichiamo solo quelle di interesse pubblico.",

        # Topics filter bar
        "topics_label": "Aree",
        "topics":       ["Tutti", "Startup & Tech", "Lavoro & HR", "Privacy & AI", "M&A", "Dispute"],

        # Page CTA
        "cta_heading": "Vuoi ricevere le nostre note prima?",
        "cta_intro":
            "I clienti dello studio ricevono le note sul dashboard prima "
            "della pubblicazione. Se vi interessa, prenotate una discovery call "
            "— e vi facciamo vedere come funziona.",
        "cta_primary":      "Prenota una strategy call",
        "cta_primary_href": "contatti",
    },

    # ─── CONTATTI (contact) ─────────────────────────────────────
    "contatti": {
        "eyebrow":  "Strategy call",
        "headline": "Trenta minuti, video call, <em>niente impegno</em>.",
        "intro":
            "Il primo contatto è con un partner, non con un BDR. "
            "Discutiamo il perimetro, la timeline e l'eventuale conflitto "
            "di interesse — prima di qualsiasi proposta economica. "
            "Gratuito, senza impegno, risposta di un partner reale.",

        # Next-slot chip above the form
        "slot_label": "Prossimo slot disponibile",
        "slot_value": "Giovedì 17 aprile · 10:30",
        "slot_note":  "La call avviene dal dashboard cliente · non serve Zoom account",

        # Form fields
        "form_label":   "Prenota la call",
        "form_heading": "Tre step, due minuti, una conversazione.",
        "form_intro":
            "Le informazioni sono trattate ai sensi del Reg. UE 679/2016 "
            "e custodite sul nostro dashboard cifrato con accesso limitato ai "
            "partner. Niente CRM di terze parti.",
        "form_fields": [
            {"name": "name",      "label": "Nome",           "type": "text",     "required": True,  "placeholder": "Es. Giorgia",
             "helper": "Solo il nome di battesimo, grazie."},
            {"name": "surname",   "label": "Cognome",        "type": "text",     "required": True,  "placeholder": "Es. Rossi",
             "helper": "Come compare nei documenti aziendali."},
            {"name": "email",     "label": "Email",          "type": "email",    "required": True,  "placeholder": "giorgia@azienda.com",
             "helper": "Accettiamo anche domini consumer — non siamo uno studio d'affari novecentesco."},
            {"name": "phone",     "label": "Telefono",       "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Facoltativo. Lo usiamo solo se la call salta."},
            {"name": "company",   "label": "Azienda o studio", "type": "text",   "required": True,  "placeholder": "Es. Acme S.r.l.",
             "helper": "Il nome registrato o il nome commerciale."},
            {"name": "company_type", "label": "Tipo azienda",  "type": "select", "required": True,
             "options": [
                 "Startup (pre-seed)",
                 "Startup (seed)",
                 "Scale-up (Serie A o oltre)",
                 "PMI / azienda familiare",
                 "Scale-up mature / corporate",
                 "Professionista o freelance",
                 "Altro",
             ],
             "helper": "Serve a capire se siete nel nostro perimetro."},
            {"name": "stage",      "label": "Stage",            "type": "select", "required": True,
             "options": [
                 "Ancora in discussione interna",
                 "Pronti a partire entro un mese",
                 "Pronti a partire entro tre mesi",
                 "Esplorativo, nessuna urgenza",
             ],
             "helper": "Aiuta a prenotare il partner giusto sul vostro caso."},
            {"name": "help_type",  "label": "Tipo di supporto", "type": "select", "required": True,
             "options": [
                 "Non so ancora · da capire in call",
                 "Contrattualistica B2B",
                 "Startup legal sprint / fundraising",
                 "M&A o passaggio generazionale",
                 "Lavoro, HR, stock option",
                 "Privacy, GDPR, AI Act",
                 "Contenzioso o dispute",
                 "Fractional General Counsel",
             ],
             "helper": "Scegliete \"Non so ancora\" se il perimetro copre più aree."},
            {"name": "message",   "label": "Raccontaci il caso", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Max 600 caratteri. Niente nomi di controparti o dati sensibili — li vediamo in call dopo NDA reciproca.",
             "helper": "Quel che basta per capire se è il nostro campo. "
                       "I nomi delle controparti si condividono solo dopo NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Chi sei",
             "meta": "La persona con cui parleremo in call.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Cosa fate",
             "meta": "Per il conflict-check preliminare.",
             "fields": ["company", "company_type", "stage"]},
            {"num": "03", "title": "Cosa vi serve",
             "meta": "Nessun dettaglio sensibile qui — entriamo nel merito solo dopo NDA reciproca.",
             "fields": ["help_type", "message"]},
        ],

        "form_submit_label": "Prenota la strategy call",
        "form_submit_note":
            "Risposta di un partner reale entro 2 ore lavorative. "
            "Niente BDR, niente sequence, niente \"a breve vi ricontatteremo\".",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Regolamento UE 679/2016. I dati sono custoditi sul dashboard "
            "cifrato dello studio con accesso limitato ai partner. Nessun "
            "dato viene comunicato a terzi senza esplicita autorizzazione.",

        # Office address labels
        "office_address_label": "Indirizzo",
        "office_area_label":    "Quartiere",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",

        # Offices — 3 cards
        "offices_label": "Le tre sedi",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Quartier generale",
                "address": "Via Solferino 40 · 20121",
                "area":    "Brera · a due passi da Piazza della Scala",
                "phone":   "+39 02 4546 7789",
                "email":   "milano@martinipartners.legal",
                "note":    "Desk di tutte le practice · meeting room bookabili dal dashboard",
            },
            {
                "city":    "Torino",
                "tag":     "Desk scale-up",
                "address": "Via Roma 324 · 10123",
                "area":    "Centro · vicino Piazza Castello",
                "phone":   "+39 011 5667 2240",
                "email":   "torino@martinipartners.legal",
                "note":    "Desk scale-up tech · sede principale contract-as-a-service",
            },
            {
                "city":    "Bologna",
                "tag":     "Desk PMI",
                "address": "Via Indipendenza 18 · 40121",
                "area":    "Centro · vicino Piazza Maggiore",
                "phone":   "+39 051 3344 8812",
                "email":   "bologna@martinipartners.legal",
                "note":    "Desk PMI ed M&A mid-market · corridor Emilia-Romagna",
            },
        ],

        "channels_label": "Canali diretti",
        "channels": [
            ("Email generale",        "hello@martinipartners.legal", "Risposta entro 2 ore lavorative"),
            ("Centralino Milano",     "+39 02 4546 7789",             "Lun – Ven · 09:00 – 19:00"),
            ("LinkedIn aziendale",    "in/martini-partners",          "Note pubbliche e AMA settimanali"),
        ],

        "footnote":
            "Martini & Partners non fa cold outreach. Se qualcuno si presenta "
            "come BDR per conto nostro, non siamo noi. Tutte le relazioni "
            "nascono da referral, da una nostra nota letta o da questo form.",
    },

    # ─── POSTS (insights detail) ────────────────────────────────
    "posts": [
        {
            "slug":     "ai-act-pmi-italiane",
            "title":    "AI Act · cosa cambia per le PMI italiane",
            "topic":    "Privacy & AI",
            "date":     "17 aprile 2026",
            "reading":  "8 min",
            "author":   "Avv. Giulia Masi",
            "lead":
                "L'AI Act entra in vigore effettivo il 2 agosto 2026 per i "
                "sistemi ad alto rischio. Per le PMI italiane che usano "
                "modelli predittivi in produzione — marketplace, scoring "
                "clienti, HR tech — la finestra per adeguarsi è di quattro "
                "mesi. Ecco come lo stiamo facendo con i nostri clienti.",
            "sections": [
                {
                    "heading": "Perché riguarda anche le PMI",
                    "body":
                        "La lettura comune è che l'AI Act colpisca solo i "
                        "giganti — OpenAI, Mistral, Meta. È sbagliata. La "
                        "Direttiva classifica per uso, non per dimensione "
                        "dell'azienda che sviluppa. Un algoritmo di scoring "
                        "creditizio fatto in casa da una fintech seed ricade "
                        "in un alto rischio esattamente come uno di una banca "
                        "d'affari — e la PMI ha meno risorse per adeguarsi.",
                },
                {
                    "heading": "Le quattro classi di rischio",
                    "body":
                        "Rischio inaccettabile (vietato), alto rischio "
                        "(requisiti molto stringenti), rischio limitato "
                        "(trasparenza obbligatoria), rischio minimo (nessun "
                        "obbligo specifico). La mappatura dei sistemi aziendali "
                        "nelle quattro classi è il primo passo — e per le PMI "
                        "richiede in media due settimane di lavoro con un "
                        "legal ops + un product manager.",
                },
                {
                    "heading": "Cosa fare ora",
                    "body":
                        "Tre azioni concrete: un inventario completo dei "
                        "sistemi AI in produzione (inclusi i plug-in di "
                        "third-party come chatbot o recommendation engine), "
                        "una DPIA integrata per i sistemi a rischio alto, "
                        "e una policy pubblica che dichiari l'uso di AI "
                        "nei processi decisionali che toccano clienti o "
                        "dipendenti. Per la maggior parte delle PMI è un "
                        "progetto da sei settimane — il nostro AI Act "
                        "Readiness lo copre integralmente.",
                },
            ],
            "takeaway":
                "L'AI Act non è un esercizio burocratico — è un'opportunità "
                "per fare ordine sui sistemi aziendali che usano dati dei "
                "clienti o dei dipendenti. Chi si adegua bene oggi vende "
                "meglio domani.",
            "tags":     ["AI Act", "GDPR", "Compliance", "PMI"],
        },
        {
            "slug":     "stock-option-2026",
            "title":    "Stock option 2026 · nuova disciplina fiscale",
            "topic":    "Startup & Tech",
            "date":     "14 aprile 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "La Legge di Bilancio 2026 ha modificato il trattamento "
                "fiscale dei piani di stock option per startup e PMI "
                "innovative. La modifica è favorevole — ma la formulazione "
                "lascia margini di interpretazione. Vediamo come stiamo "
                "impostando i piani nuovi e cosa fare con quelli esistenti.",
            "sections": [
                {
                    "heading": "Cosa cambia dal 1° gennaio 2026",
                    "body":
                        "La tassazione si applica al momento della vendita "
                        "effettiva delle azioni (non più al vesting) per "
                        "startup innovative iscritte al registro speciale. "
                        "L'aliquota di capital gain rimane al 26%. È una "
                        "modifica significativa: elimina il paradosso del "
                        "dipendente che paga tasse su azioni che non ha "
                        "ancora monetizzato.",
                },
                {
                    "heading": "I piani esistenti vanno riscritti?",
                    "body":
                        "Non necessariamente. La nuova disciplina si applica "
                        "automaticamente ai piani che rispettano i requisiti — "
                        "iscrizione a startup innovativa, vesting minimo di "
                        "24 mesi, assegnazione a dipendenti o amministratori "
                        "in continuità di rapporto. La maggior parte dei piani "
                        "recenti è già compatibile. I piani scritti prima "
                        "del 2022 invece richiedono quasi sempre un aggiornamento.",
                },
                {
                    "heading": "Come impostare i piani nuovi",
                    "body":
                        "Tre cose da fare bene: scrivere il regolamento "
                        "interno con riferimento esplicito alla disciplina "
                        "2026, documentare la data di assegnazione e il "
                        "piano di vesting individuale per ogni dipendente, "
                        "e fornire al dipendente una guida fiscale in "
                        "italiano al momento dell'assegnazione. Il nostro "
                        "template di piano SO/SAR è già aggiornato.",
                },
            ],
            "takeaway":
                "Per le startup innovative la nuova disciplina è una "
                "semplificazione netta — e un argomento in più per "
                "convincere un senior a lasciare una grande azienda per "
                "entrare nel team founder.",
            "tags":     ["Stock option", "Startup", "Fisco", "HR"],
        },
        {
            "slug":     "smart-working-confine",
            "title":    "Smart-working oltre confine · tre scenari",
            "topic":    "Lavoro & HR",
            "date":     "11 aprile 2026",
            "reading":  "7 min",
            "author":   "Avv. Sara Miccoli",
            "lead":
                "Dopo il 2023 la maggior parte delle aziende italiane ha "
                "accettato lo smart-working oltre confine — ma le regole "
                "su contributi previdenziali, ritenute fiscali e giurisdizione "
                "del diritto del lavoro applicabile restano confuse. "
                "Tre scenari tipo che vediamo ogni mese.",
            "sections": [
                {
                    "heading": "Scenario 1 · Dipendente italiano che si trasferisce in Spagna",
                    "body":
                        "Se il dipendente lavora più di 183 giorni l'anno "
                        "in Spagna, diventa fiscalmente residente spagnolo — "
                        "l'azienda italiana deve versare contributi Social "
                        "Security spagnola (convenzione bilaterale) e "
                        "ritenute IRPF spagnole. La legge del contratto "
                        "di lavoro rimane italiana se espressamente pattuito, "
                        "ma i diritti minimi spagnoli (ferie, licenziamento) "
                        "si applicano comunque.",
                },
                {
                    "heading": "Scenario 2 · Dipendente EU che si trasferisce in Italia",
                    "body":
                        "Più semplice ma non banale. L'azienda diventa "
                        "sostituto d'imposta italiano, apre posizione INPS "
                        "e versa contributi italiani. Se il dipendente ha "
                        "un contratto francese o tedesco originario, "
                        "bisogna rinegoziare — molte aziende scelgono di "
                        "stipulare un contratto italiano nuovo con clausola "
                        "di continuità.",
                },
                {
                    "heading": "Scenario 3 · Dipendente italiano che si trasferisce extra-EU",
                    "body":
                        "Il più delicato. Senza convenzione bilaterale "
                        "adeguata (es. USA, Canada), si rischia doppia "
                        "imposizione fiscale e doppia contribuzione "
                        "previdenziale. La soluzione pulita è quasi sempre "
                        "un contratto locale con entità estera (controllata "
                        "o PEO / EOR) — il mantenimento del contratto "
                        "italiano con trasferta lunga è sostenibile solo "
                        "per 18-24 mesi al massimo.",
                },
            ],
            "takeaway":
                "Prima di dire \"sì\" a uno smart-working oltre confine, "
                "verificate sempre il paese di destinazione. Le regole "
                "cambiano tra EU, UK, USA e resto del mondo — e i costi "
                "per l'azienda possono variare del 30% tra scenari diversi.",
            "tags":     ["Smart-working", "HR", "Cross-border", "Lavoro"],
        },
        {
            "slug":     "contratti-saas-enterprise",
            "title":    "Contratti SaaS enterprise · tre clausole che non devono mancare",
            "topic":    "Contrattualistica B2B",
            "date":     "08 aprile 2026",
            "reading":  "5 min",
            "author":   "Avv. Davide Romano",
            "lead":
                "Dopo aver firmato più di trecento MSA SaaS enterprise "
                "negli ultimi tre anni, abbiamo una lista mentale di "
                "clausole che non dovrebbero mai mancare. Tre che "
                "consigliamo sempre, anche se il cliente \"non le ha mai viste\".",
            "sections": [
                {
                    "heading": "1. Liability cap proporzionato e non inferiore a 12 mesi di fee",
                    "body":
                        "Il cap di responsabilità standard proposto dai "
                        "grandi vendor (es. Salesforce, ServiceNow) è "
                        "spesso pari a 12 mesi di fee del servizio. "
                        "Accettarlo è ragionevole · negoziare al ribasso "
                        "a 3 o 6 mesi è spesso possibile per deal sotto "
                        "i 500K €.",
                },
                {
                    "heading": "2. Data portability e export clause",
                    "body":
                        "Il diritto di esportare tutti i dati in un "
                        "formato machine-readable entro 30 giorni dal "
                        "termination, senza costi aggiuntivi. Spesso "
                        "assente, quasi sempre negoziabile.",
                },
                {
                    "heading": "3. Sub-processor notice period",
                    "body":
                        "Il diritto di essere notificati almeno 30 giorni "
                        "prima di un cambio di sub-processor (hosting, "
                        "email, analytics) — con diritto di opt-out "
                        "senza penale se il nuovo sub-processor non rispetta "
                        "i propri standard.",
                },
            ],
            "takeaway":
                "Queste tre clausole si trovano nel 70% dei contratti "
                "enterprise che firmiamo — il restante 30% si convince "
                "se le chiedete con un drafting chiaro. Noi abbiamo un "
                "template pronto nel dashboard.",
            "tags":     ["SaaS", "Contratti", "Enterprise", "B2B"],
        },
        {
            "slug":     "mandati-m-and-a-2025",
            "title":    "M&A mid-market · quello che abbiamo imparato nel 2025",
            "topic":    "M&A",
            "date":     "04 aprile 2026",
            "reading":  "9 min",
            "author":   "Avv. Chiara Belforte",
            "lead":
                "Nel 2025 abbiamo chiuso sette operazioni di M&A mid-market "
                "— tre lato vendor, quattro lato acquirer, cinque italiane "
                "e due cross-border. Ecco le tre tendenze che abbiamo visto "
                "ripetersi abbastanza da meritarne una nota.",
            "sections": [
                {
                    "heading": "Gli earn-out sono tornati",
                    "body":
                        "Dopo due anni in cui le cessioni si chiudevano con "
                        "prezzo fisso e uscita del fondatore a 6-12 mesi, "
                        "nel 2025 l'earn-out è riapparso. Anche nel mid-market. "
                        "Tipicamente 25-35% del prezzo legato a KPI operativi "
                        "post-closing, durata 24-36 mesi. Per il fondatore è "
                        "un'opportunità ma richiede un contratto di earn-out "
                        "scritto bene per evitare contenzioso.",
                },
                {
                    "heading": "La due diligence AI/privacy è diventata normale",
                    "body":
                        "Anche il fondo più classico ormai chiede un "
                        "riassunto della compliance GDPR e una mappa dei "
                        "sistemi AI prima di firmare. Un audit preventivo "
                        "vendor-side costa 5-10K € e ti fa guadagnare "
                        "2-3 settimane sul processo.",
                },
                {
                    "heading": "I signing cross-border richiedono più tempo",
                    "body":
                        "Le due operazioni italo-DACH del 2025 hanno "
                        "richiesto in media 8 settimane più dei signing "
                        "italiani puri — tra traduzione certificata degli "
                        "atti, approvazione antitrust e coordinamento con "
                        "notaio tedesco. Meglio pianificarlo dall'inizio "
                        "che scoprirlo alla due.",
                },
            ],
            "takeaway":
                "Il 2025 ha normalizzato l'earn-out e reso standard la "
                "due diligence AI/privacy. Sul cross-border, meglio "
                "overplan del tempo che stressare il closing.",
            "tags":     ["M&A", "Fondi", "Due diligence", "Cross-border"],
        },
        {
            "slug":     "dashboard-cliente-perche",
            "title":    "Perché abbiamo costruito un dashboard cliente (invece di comprarlo)",
            "topic":    "Startup & Tech",
            "date":     "28 marzo 2026",
            "reading":  "6 min",
            "author":   "Avv. Giorgia Martini",
            "lead":
                "Nel 2020 abbiamo valutato Clio, MyCase, PracticePanther e "
                "altri sei software \"practice management\" per studi legali. "
                "Nessuno ci convinceva. Abbiamo costruito il nostro — "
                "internamente, con un product manager part-time. "
                "Ecco perché, e cosa ne abbiamo imparato.",
            "sections": [
                {
                    "heading": "Il problema dei PM legali standard",
                    "body":
                        "I software practice management per studi legali "
                        "sono costruiti per studi da 50+ persone che fatturano "
                        "a ore. La UX è pensata per segretarie e avvocati "
                        "che compilano timesheet. Noi siamo 10 persone, "
                        "non fatturiamo a ore e i nostri clienti sono "
                        "product manager abituati a Linear. Incompatibile.",
                },
                {
                    "heading": "Cosa abbiamo costruito",
                    "body":
                        "Un workspace sul modello Linear + Notion con "
                        "kanban per le pratiche, un archivio documentale "
                        "cifrato, un calendario condiviso delle scadenze "
                        "e un chat canale per ogni fascicolo. Niente "
                        "timesheet — le ore si tracciano a fine settimana, "
                        "in chiaro per il cliente. Sei mesi di sviluppo, "
                        "costo € 80K, oggi lo usano tutti.",
                },
                {
                    "heading": "Perché è stato un vantaggio commerciale",
                    "body":
                        "Abbiamo scoperto a posteriori che il dashboard è "
                        "il primo motivo per cui i clienti ci scelgono. "
                        "Nei pitch mostriamo un walkthrough di due minuti "
                        "del workspace reale — e per aziende abituate a "
                        "Linear + Notion è un game-changer rispetto ai "
                        "PDF via email degli altri studi.",
                },
            ],
            "takeaway":
                "Fai la cosa che gli altri non vogliono fare. Il dashboard "
                "è stato l'investimento più importante dei primi otto anni — "
                "più di ogni nuovo ufficio o nuova assunzione.",
            "tags":     ["Dashboard", "Product", "Studio", "Tooling"],
        },
    ],
}

# D-047 compliance note:
# This file is the single source of truth for every user-facing string
# on the juris-avvocato-moderno template. The skin files
# (templates/live_templates/lawyer/modern-transparent/*.html) reference
# `page_data.*`, `site.*`, `chrome.*` and `posts.*` exclusively — no
# literal Italian/English strings are authored in the HTML layer.
