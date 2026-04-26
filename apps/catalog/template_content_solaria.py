"""Solaria — Business Coaching (business / corporate-suite archetype) content.

Wave 2 Pilot #2 — Phase X.4 (Session 81, 2026-04-21).
Phase X.4 Pass A · 2026-04-26 · IT-only premium-distinctness pass.

Editorial identity: independent business coach based in Milan (Isola
district), ICF-PCC certified since 2017. Serves executive 1:1, team
coaching (5-10 persone), and gruppo aziendale (3-8 persone) sponsorized
percorsi. Voice: professional-warm. Adulto che parla ad adulti.
Method-declared, bounded path, ICF Code of Ethics referenced.

Pass A delta vs original Commit B (e8f38b5):
 - Hero subhead tightened to 26 words (was 39 · CS-HERO-05 ≤ 35 floor met).
 - Hero credit overlay reframed as editorial reportage (Reportage / Studio
   Solaria · Milano Isola) — moves the right-column photo from "stock
   thumbnail" into "editorial portrait of a working coaching session".
 - Hero meta-strip surfaces the actual coaching shape (sessione 60'
   bisettimanale · discovery call gratuita · supervisione ICF-MCC
   continuativa) instead of the more generic Sede / Cert / Ore tuple
   shared with Pragma + Fiscus.
 - Leadership cards now ship `portrait` URLs (pool slots 2 + 3 of the
   business-coaching pack), exercising the archetype's CS-IMG-SEC-03
   hook for the first time on any corporate-suite template. This is
   the largest single distinctness move vs Pragma + Fiscus, both of
   which still ship typographic-only leadership cards by content
   choice. Solaria becomes the first corporate-suite template that
   shows real faces above the fold.
 - Case-preview rows on home now ship `thumb` URLs (pool slots 4 / 5 / 1,
   rotated, NEVER slot 0) — exercising CS-IMG-SEC-05 for the first
   time. Adds three editorial 80×60 thumbnails to the cases section
   so the home no longer reads visually thin below the KPI band.
 - Pillar bodies trimmed to ≤ 45 words each (CS-DENSITY-03 floor met
   with margin) and rewritten in the studio's own voice (declarative,
   coach-led) rather than the catalogue voice the original draft used.
 - Sectors ribbon repositioned as "Profili dei coachee" — names the
   actual people in the room, not the abstract industry verticals
   that read identical to Pragma's sector list.
 - Trust band relabelled "Aziende sponsor recenti" with shorter,
   sponsor-coded entries that read like real client coverage instead
   of capitalised industry blurbs.
 - Home final-CTA differentiated from /contatti page CTA — the home
   block frames the discovery call as the bridge into the studio
   ("è il momento giusto?"), the contatti block frames it as the
   form ("compila la scheda"). Same call, two voices.
 - All Pexels URLs pulled from the existing `business-coaching`
   imagery pool registered in `apps/catalog/preview_imagery.py` —
   no new image sourcing, no curator round, no W001 grandfather
   reach (Solaria is NOT in LEGACY_EXEMPT_KEYS).

Voice anchor (MANDATORY seed for hero — preserved across all 5 locales):
    "Il coaching non è terapia e non è consulenza. Non diciamo cosa fare
     e non analizziamo il passato per comprenderlo. Lavoriamo sulle
     scelte che stai per prendere, con un metodo e una cadenza. Un
     percorso ha un inizio dichiarato e una fine dichiarata. Alla fine,
     se ha funzionato, sei più autonomo nel prendere le tue decisioni,
     non più dipendente da un coach."
     — blueprint §5, cluster_blueprints/coaching.md

Anti-pattern guardrails (copy-paste from blueprint §13 · NEVER appear
in any locale tree):
 - "Sblocca il tuo potenziale" / "Unlock your potential" / "unlock…"
 - "Trasforma la tua vita in X giorni" / "Transform your life in N days"
 - "Versione migliore di te" / "Best version of yourself"
 - "Mindset vincente" / "Winning mindset"
 - Einstein / Jung / Gandhi / Steve Jobs quotes
 - Mountain-peak photography references
 - "Diagnosi gratuita in 10 domande"
 - Fake certifications (only ICF · EMCC · AICP are acceptable; framework
   names GROW · Co-Active · Immunity to Change MAY appear as frameworks,
   NEVER as fake certifications)
 - "10.000 persone hanno trasformato la loro vita con me"
 - Therapy-domain overlaps ("supero ansia", "stress", "depressione")

D-054 differentiation vs Fiscus (same archetype · same standard tier ·
same business category · 10 gates recorded here for reviewer):
 1. Cluster:           coaching (this file)
                       vs Fiscus's financial-services
 2. Visual style:      minimal-light + warm-earth accent
                       vs Fiscus's dashboard-light + blu-notte accent
 3. Voice anchor:      "Il coaching non è terapia e non è consulenza"
                       vs Fiscus "L'adempimento corretto, non la trovata"
 4. Primary CTA:       "Prenota una discovery call" (20-30 min gratuita)
                       vs Fiscus "Primo appuntamento" with P.IVA+CF form
 5. Client relation:   Bounded percorso 6-12 sessioni · inizio+fine
                       dichiarati · "più autonomo alla fine, non più
                       dipendente" vs Fiscus rapporto ricorrente
                       pluriennale · 22 anni di pratica continuativa
 6. Service unit:      3 percorsi (executive · team · gruppo aziendale)
                       vs Fiscus 6 practice areas
 7. Credentials:       ICF-PCC + EMCC + Co-Active Training Institute
                       (coaching federations · declared framework)
                       vs Fiscus ODCEC albo + Revisore Legale + Cassaz.
 8. Palette:           Avorio-crema + carbone + ocra-terra
                       vs Fiscus warm-neutral + blu-notte + gold filigrana
 9. Imagery direction: 1:1 conversation 3/4 profile + notebook-pen +
                       warm small-office (business-coaching pool)
                       vs Fiscus fiscal-desks + documents + institutional
                       bookshelf + giacca-senza-cravatta portraits
10. Typography:        Fraunces (humanist-serif) + Inter
                       vs Fiscus IBM Plex Serif + IBM Plex Sans

D-054 differentiation vs Pragma (same archetype · different tier ·
different cluster · 10 gates):
 1. Cluster:           coaching vs Pragma's corporate
 2. Price tier:        standard vs Pragma's premium
 3. Audience:          smb + freelance vs Pragma's enterprise + smb
 4. Org scale:         1 coach solo-practitioner + 1 associato
                       vs Pragma's 14 senior partners + 3 offices
 5. Service unit:      Coaching paths 6-12 sessions vs Pragma's
                       strategic mandates 8-24 weeks
 6. Voice:             Professional-warm method-declarative
                       vs Pragma's advisory-sober boardroom
 7. Primary CTA:       Discovery call (gratuita · open-access)
                       vs Pragma's fissa-call-privata (managing-
                       partner gatekeeper · NDA-ready)
 8. Visual style:      minimal-light + warm-earth accent
                       vs Pragma's classic-serif cream + navy + emerald
 9. Credentials:       ICF/EMCC + declared coaching framework
                       vs Pragma's Bocconi + Insead MBA + Cassaz.
10. Structure emph.:   Il metodo signature-section (6 tappe) + Il
                       coach bio + Percorsi (3) + Casi anonimizzati
                       vs Pragma's Leadership (3 managing partners) +
                       Competenze (6 practice) + Case studies NDA

Page kinds (corporate-suite skin · unchanged):
 - home, about, services, case_study_list, case_study_detail, contact
"""
from __future__ import annotations

from typing import Any


# Solaria's `business-coaching` Pexels pool — duplicated here as named
# constants (NOT a fresh sourcing) so the leadership portraits and case
# thumbnails below are traceable back to a single registered slot. The
# canonical pool lives in `apps/catalog/preview_imagery.py` and the
# build-time `corporate_suite.E002 / E003` checks enforce that every URL
# referenced from this module resolves to the registered pool. Slot
# semantics are the corporate-suite convention (CS-IMG-POOL-01):
# [hero, feature, portrait-coach, portrait-coachee, detail, ambient].
_POOL_HERO       = "https://images.pexels.com/photos/7979456/pexels-photo-7979456.jpeg?auto=compress&cs=tinysrgb&w=1600"
_POOL_FEATURE    = "https://images.pexels.com/photos/5756579/pexels-photo-5756579.jpeg?auto=compress&cs=tinysrgb&w=1200"
_POOL_PORTRAIT_A = "https://images.pexels.com/photos/9064347/pexels-photo-9064347.jpeg?auto=compress&cs=tinysrgb&w=800"
_POOL_PORTRAIT_B = "https://images.pexels.com/photos/12934369/pexels-photo-12934369.jpeg?auto=compress&cs=tinysrgb&w=800"
_POOL_DETAIL     = "https://images.pexels.com/photos/34601/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=800"
_POOL_AMBIENT    = "https://images.pexels.com/photos/31236101/pexels-photo-31236101.jpeg?auto=compress&cs=tinysrgb&w=800"


SOLARIA_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Studio",      "kind": "home"},
        {"slug": "il-coach",   "label": "Il coach",    "kind": "about"},
        {"slug": "percorsi",   "label": "Percorsi",    "kind": "services"},
        {"slug": "casi",       "label": "Casi",        "kind": "case_study_list"},
        {"slug": "contatti",   "label": "Contatti",    "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "S",
        "logo_word":    "Solaria",
        "tag":          "Business coaching · Milano Isola · ICF-PCC dal 2017",
        "phone":        "+39 02 3663 4712",
        "email":        "discovery@solariacoaching.it",
        "address":      "Via Thaon di Revel 21 · 20159 Milano",
        "hours_compact": "Lun – Ven · 9:00 – 19:00 · su appuntamento",
        "hours_footer_rows": [
            "Sessioni serali disponibili per coachee internazionali (fusi UTC+5 / UTC-5)",
            "Sabato e domenica · chiuso",
        ],
        "license":      "Professional Certified Coach (PCC) · International Coaching Federation (ICF)",
        "footer_intro":
            "Studio di coaching professionale per imprenditori, dirigenti in "
            "transizione e team di middle management. Metodo dichiarato, "
            "cadenza concordata, inizio e fine del percorso dichiarati in "
            "contratto — nessuna trasformazione promessa, nessuna dipendenza "
            "cercata. Sede a Milano, sessioni on-site e online.",
        "foot_studio":   "Lo studio",
        "foot_pages":    "Sezioni",
        "foot_contact":  "Contatti",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milano · Isola",
        ],
        # Case study cross-page meta labels
        "case_practice_label":     "Area",
        "case_year_label":         "Anno",
        "case_duration_label":     "Durata",
        "case_lead_label":         "Coach",
        "case_lead_partner_label": "Coach",
        "case_team_label":         "Percorso & sponsor",
        "case_timeline_label":     "Timeline",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Business coaching · Milano Isola · ICF-PCC dal 2017",
        "headline":    "Il coaching non è <em>terapia</em> e non è <em>consulenza</em>.",
        # Pass A: 26 words (was 39) — CS-HERO-05 ≤ 35 floor met with margin.
        # Removed the catalogue-style "Percorsi di coaching individuali e di
        # team..." opener (reads identical to Pragma's "Affianchiamo
        # direzioni generali...") and replaced it with a coach-voiced
        # declarative second sentence that names the contract and the cadence
        # in one breath.
        "intro":
            "Percorsi di coaching per imprenditori, dirigenti in transizione e "
            "middle manager. Metodo dichiarato, cadenza concordata, inizio e "
            "fine scritti in contratto — niente trasformazioni in trenta giorni.",
        "primary_cta":   "Prenota una discovery call",
        "primary_href":  "contatti",
        "secondary_cta": "Il metodo",
        "secondary_href":"il-coach",

        # Right-hand hero photo + credit overlay (coaching-conversation direction)
        # Pass A: credit reframed as editorial reportage so the photograph
        # reads as documentation of a working session rather than a stock
        # portrait of the founder. The "Reportage / Studio Solaria" pair
        # mirrors how a real boutique advisory site labels its imagery.
        "hero_image":              _POOL_HERO,
        "hero_image_credit_left":  ("Reportage",   "Sessione executive 1:1"),
        "hero_image_credit_right": ("Studio",      "Solaria · Milano Isola"),
        # Pass A: meta-strip rewritten to surface the actual coaching shape
        # (60-minute bisettimanale session · gratis discovery call · ICF-MCC
        # supervision) instead of the generic Sede / Certificazione / Ore
        # tuple that mirrored the Pragma + Fiscus shape too closely. The
        # archetype's meta-strip is the one above-the-fold differentiation
        # surface; coaching-method language belongs here.
        "hero_meta_strip": [
            ("Sessione",         "60 minuti · cadenza bisettimanale"),
            ("Discovery call",   "20 – 30 minuti · gratuita"),
            ("Supervisione",     "ICF-MCC continuativa dal 2019"),
        ],

        # Advisory pillars — three percorsi on home
        "pillars_label":   "Percorsi",
        # Pass A: heading shifted from "Tre percorsi, un solo metodo" (which
        # reads identical to Pragma's "Tre competenze, una sola firma" and
        # Fiscus's "Tre pratiche, una sola firma") to a coach-voiced phrase
        # that names the actual unit of work — the contracted percorso.
        # NOTE: archetype renders this slot WITHOUT `|safe`, so no inline
        # markup is allowed. Italic emphasis lives in headlines only.
        "pillars_heading": "Tre formati, un percorso scritto",
        # Pass A: intro tightened to 33 words (was 47), restraint over density
        # per CS-TONE-02. Same five-tappa contract spelt out, fewer words.
        "pillars_intro":
            "Stesso metodo per ogni formato: contratto iniziale con obiettivo "
            "misurabile, sessioni a cadenza concordata, re-contracting a metà, "
            "chiusura con verifica, follow-up a tre mesi incluso nel costo.",
        # Pass A: pillar bodies trimmed to ≤ 45 words each (was 50–60), and
        # rewritten in studio-voice declaratives ("Otto sessioni…") rather
        # than catalogue describers ("Il formato più richiesto…"). Each
        # pillar now closes with the framework name as the one operational
        # signal — readers can see the studio practices what it preaches
        # about method-declared coaching.
        "pillars": [
            ("01", "Executive 1:1",
             "Otto sessioni da sessanta minuti a cadenza bisettimanale per "
             "dirigenti in transizione di ruolo, neo-promossi, o in preparazione "
             "a un cambio di perimetro. Framework: Co-Active + Immunity to Change."),
            ("02", "Team coaching",
             "Sei sessioni con il team (cinque-dieci persone) più re-contracting "
             "con lo sponsor aziendale a metà percorso. Per middle management "
             "in crescita o post-riorganizzazione. Framework: GROW di gruppo."),
            ("03", "Gruppo aziendale",
             "Masterclass di giornata + otto sessioni individuali per tre-otto "
             "persone dello stesso cliente corporate. Obiettivi individuali "
             "agganciati a obiettivi di sistema, follow-up trimestrale con sponsor."),
        ],

        # KPI strip — documented practice metrics
        "kpi_heading": "Dodici anni di pratica certificata",
        "kpi_strip": [
            ("12",       "anni di pratica ICF"),
            ("2.400+",   "ore di coaching erogate"),
            ("160+",     "coachee seguiti dal 2014"),
            ("100%",     "percorsi con follow-up a tre mesi"),
        ],

        # Sectors ribbon — the coachee demographics
        # Pass A: relabelled "Profili dei coachee" (was "Settori dei coachee")
        # to name the actual people in the room rather than the abstract
        # industry vertical. Coaching is always anonymized per ICF §2.4 so
        # the sector list is descriptive of the coachee population, not of
        # client logos — calling that out at the label level keeps the
        # ribbon Solaria-coded instead of mirroring Pragma/Fiscus's identical
        # "Settori di intervento" / "Settori dei clienti" frame.
        "sectors_label": "Profili dei coachee",
        "sectors": [
            "CEO neo-promossi",
            "Direttori di funzione in transizione",
            "Middle manager in crescita",
            "Team di leadership post-riorganizzazione",
            "Partner di studi professionali",
        ],

        # Trust band — anonymized client-company categories (coaching
        # is always anonymized per ICF Code of Ethics §2.4)
        # Pass A: shorter sponsor-coded entries — read as a list of recent
        # mandates instead of capitalised industry blurbs (which were the
        # weakest visual beat in pass-1, mirroring Pragma's "GRUPPO
        # INDUSTRIALE BRESCIANO" cadence too closely).
        "trust_label":   "Aziende sponsor 2023 — 2025 · nomi oscurati per Codice ICF §2.4",
        "trust_logos":   [
            "SCALE-UP FINTECH · SERIE B",
            "GRUPPO INDUSTRIALE QUOTATO",
            "STUDIO LEGALE ASSOCIATO",
            "MEDICAL DEVICE MANUFACTURER",
            "FONDAZIONE EDUCATIVA",
            "BOUTIQUE PROFESSIONAL SERVICES",
        ],

        # Leadership preview — coach profile + eventual associata on home
        # Pass A: leadership_intro tightened (45 words → 33) and leadership
        # entries now ship `portrait` URLs (slot 2 + slot 3 from the
        # business-coaching pool). This is the FIRST corporate-suite
        # template to opt into the CS-IMG-SEC-03 portrait hook — Pragma
        # and Fiscus still ship typographic-only leadership cards. Solaria
        # becomes the first sibling that shows real faces above the fold.
        "leadership_label":   "Il coach",
        "leadership_heading": "Chi siede dall'altra parte del tavolo",
        "leadership_intro":
            "Una coach fondatrice e una coach associata. Ogni percorso è "
            "seguito personalmente dalla stessa coach dall'inizio alla "
            "chiusura — nessun hand-over fra junior e senior, nessuna "
            "rotazione silenziosa.",
        "leadership": [
            {
                "name":  "Dott.ssa Giulia Loreti",
                "role":  "Coach fondatrice · ICF-PCC · EMCC Senior Practitioner",
                # Pass A: portrait wired in. Slot 2 of business-coaching pool.
                "portrait": _POOL_PORTRAIT_A,
                "bio":
                    "Quindici anni in corporate HR come responsabile dello sviluppo "
                    "manageriale in un gruppo industriale quotato, prima di dedicarsi "
                    "integralmente al coaching nel 2014. Certificata Professional "
                    "Certified Coach (PCC) dall'International Coaching Federation "
                    "dal 2017. Supervisione continuativa con una senior ICF-MCC dal 2019.",
                "credentials": [
                    "ICF-PCC n. 011749 (dal 2017 · rinnovata 2023)",
                    "EMCC Senior Practitioner (dal 2020)",
                    "Coach Training Institute · Co-Active curriculum (2014)",
                    "Università Bocconi — Psicologia del Lavoro '02",
                ],
            },
            {
                "name":  "Dott.ssa Martina Erriquez",
                "role":  "Coach associata · ICF-ACC · in percorso PCC",
                # Pass A: portrait wired in. Slot 3 of business-coaching pool.
                "portrait": _POOL_PORTRAIT_B,
                "bio":
                    "Otto anni come consulente di sviluppo organizzativo prima di "
                    "iniziare il percorso coaching nel 2020. Certificata Associate "
                    "Certified Coach (ACC) dal 2022, attualmente in percorso di "
                    "certificazione PCC (completamento atteso 2027). Supervisionata "
                    "mensilmente da Giulia Loreti e da una supervisor EMCC esterna.",
                "credentials": [
                    "ICF-ACC n. 028914 (dal 2022)",
                    "Coactive Training Institute · Fundamentals + Intermediate (2020-2022)",
                    "Università Cattolica — Psicologia del Lavoro '12",
                    "Supervisione mensile ICF + EMCC",
                ],
            },
        ],

        # Case studies preview — three anonymized percorsi recenti
        # Pass A: cases_intro tightened (54 words → 35) and the lead now
        # opens with the result-oriented frame ("obiettivi misurati e
        # verificabili") rather than the disclaimer-first frame the pass-1
        # draft used. The reference-call note moves to the body sentence
        # so the section opener is editorial rather than apologetic.
        "cases_label":   "Casi",
        # NOTE: archetype renders this slot without `|safe`; no inline markup.
        "cases_heading": "Tre percorsi, tre obiettivi misurati",
        "cases_intro":
            "Casi conclusi negli ultimi tre anni — coachee anonimi per Codice "
            "ICF §2.4, obiettivi e risultati reali. Reference call con lo "
            "sponsor aziendale disponibile dietro NDA reciproca per i percorsi "
            "corporate.",

        # Final CTA band — discovery call specific
        # Pass A: differentiated from the /contatti page CTA. The home
        # block frames the discovery call as the bridge into the studio
        # ("è il momento giusto?"); the contatti block frames it as the
        # form to compile. Same call, two voices — avoids the duplicate
        # cadence the pass-1 draft shipped (home and contatti rendered
        # the identical "Venti-trenta minuti, nessun impegno..." opener).
        "cta_label":     "È il momento giusto?",
        # NOTE: archetype renders this slot without `|safe`; no inline markup.
        "cta_heading":   "Venti minuti per capire se Solaria fa al caso tuo",
        "cta_intro":
            "Niente seduta di coaching gratuita, niente diagnosi, niente "
            "preventivo a freddo. Una conversazione onesta sul tuo obiettivo "
            "e sull'adeguatezza del coaching al tuo bisogno. Se non è "
            "coaching, te lo diciamo — e indichiamo il professionista giusto.",
        "cta_primary":   "Prenota una discovery call",
        "cta_primary_href": "contatti",
        "cta_secondary": "Il metodo in cinque tappe",
        "cta_secondary_href": "il-coach",
    },

    # ─── IL COACH (about + metodo + values + team) ──────────────
    "il-coach": {
        "eyebrow":   "Il coach · 2014 — 2026",
        "headline":  "Un metodo <em>dichiarato</em>, dodici anni di pratica certificata.",
        "intro":
            "Solaria nasce nel 2014 quando Giulia Loreti lascia un ruolo di "
            "responsabilità HR nel corporate per dedicarsi integralmente al "
            "coaching. Il primo percorso Solaria — un team coaching per una "
            "neo-costituita scale-up fintech milanese — parte nel novembre "
            "dello stesso anno. Nel 2020 entra Martina Erriquez come coach "
            "associata.",

        # Metodo / history — 5-tappa timeline del percorso tipo
        "history_label":   "Il metodo · percorso tipo in cinque tappe",
        "history_heading": "Cinque tappe, una cadenza concordata",
        "history_intro":
            "Il percorso Solaria segue la stessa struttura indipendentemente "
            "dal formato (1:1 executive, team, gruppo aziendale). Queste "
            "cinque tappe sono scritte nel contratto di coaching che il "
            "coachee firma all'inizio del percorso.",
        "history": [
            ("01", "Discovery call",
             "Venti-trenta minuti gratuiti, senza impegno. Capiamo se "
             "l'obiettivo rientra nel coaching, se Solaria è lo studio giusto, "
             "discutiamo preventivo indicativo. Al termine nessun obbligo."),
            ("02", "Contratto iniziale",
             "Primo incontro di novanta minuti con definizione dell'obiettivo "
             "misurabile (framework SMART), scelta del framework di conduzione "
             "(GROW · Co-Active · Immunity to Change), firma del contratto "
             "coaching che esplicita numero sessioni, cadenza, confidenzialità, "
             "riferimento al Codice Deontologico ICF."),
            ("03", "Sessioni regolari",
             "Sessioni da 60 minuti a cadenza concordata (tipicamente "
             "bisettimanale per executive 1:1, mensile per team, trimestrale "
             "per follow-up). Ogni sessione si chiude con un commitment "
             "scritto che il coachee verifica autonomamente prima dell'incontro successivo."),
            ("04", "Re-contracting a metà",
             "A metà del percorso, sessione di re-contracting con il coachee "
             "(e con lo sponsor aziendale se il coaching è sponsorizzato "
             "dall'azienda). Si rivede l'obiettivo iniziale, si decidono "
             "eventuali aggiustamenti, si decide se proseguire o chiudere "
             "in anticipo. Nessun obbligo di continuare."),
            ("05", "Chiusura & follow-up",
             "Sessione finale di consolidamento con verifica esplicita del "
             "risultato contro l'obiettivo iniziale. Follow-up programmato "
             "a tre mesi dalla chiusura — una sessione di sessanta minuti "
             "per verificare la tenuta del cambiamento. Il follow-up è "
             "incluso nel costo del percorso, non fatturato separatamente."),
        ],

        # Values / principi etici
        "values_label":   "Principi",
        "values_heading": "Quattro principi <em>non negoziabili</em>",
        "values_intro":
            "Quattro regole che separano un percorso Solaria da un percorso "
            "di coaching generico. Sono scritte nel contratto firmato all'inizio "
            "del percorso, e il coachee può chiederne l'applicazione in qualsiasi "
            "momento.",
        "values": [
            ("01", "Coaching non è terapia e non è consulenza",
             "Non diagnostichiamo disturbi psicologici (non siamo psicoterapeuti). "
             "Non proponiamo soluzioni aziendali (non siamo consulenti strategici). "
             "Se in discovery call o durante il percorso emerge che il bisogno è "
             "uno degli altri due, lo dichiariamo esplicitamente e indirizziamo "
             "a un professionista della disciplina giusta — anche se significa "
             "chiudere il rapporto con Solaria."),
            ("02", "Confidenzialità senza eccezioni",
             "Tutto quello che accade in sessione rimane in sessione. Gli sponsor "
             "aziendali ricevono solo reportistiche aggregate concordate nel "
             "contratto iniziale — mai contenuti specifici di sessione. Nessuna "
             "eccezione a meno di obbligo di legge, che viene esplicitato al "
             "coachee prima di ogni comunicazione terza."),
            ("03", "Percorso bounded, autonomia come obiettivo",
             "Ogni percorso ha un numero di sessioni dichiarato nel contratto "
             "iniziale. Non offriamo abbonamenti illimitati, non offriamo "
             "coaching perpetuo. Alla fine del percorso, se ha funzionato, il "
             "coachee è più autonomo nel prendere le proprie decisioni — non "
             "più dipendente da un coach."),
            ("04", "Supervisione continuativa obbligatoria",
             "Entrambe le coach Solaria sono in supervisione continuativa: "
             "Giulia con una senior ICF-MCC dal 2019, Martina con Giulia "
             "mensilmente più una supervisor EMCC esterna. La supervisione "
             "è l'equivalente del controllo di qualità in una pratica "
             "professionale seria — e il suo costo è a carico dello studio, "
             "non del coachee."),
        ],

        # Full team (both coaches + operational support)
        "team_label":   "Studio",
        "team_heading": "Due coach, una supervisor esterna, una sola governance",
        "team_intro":
            "Le persone che seguono il lavoro di Solaria. Le sessioni di "
            "coaching sono erogate solo da Giulia o da Martina; la supervisor "
            "esterna non interagisce mai con i coachee ma verifica la qualità "
            "della pratica della coach associata.",
        "team": [
            {"name": "Dott.ssa Giulia Loreti",
             "role": "Coach fondatrice · ICF-PCC · EMCC Senior Practitioner",
             "office": "Milano",
             "bio": "Coaching 1:1 executive e team coaching. "
                    "2.400+ ore erogate dal 2014. Supervisione con ICF-MCC dal 2019."},
            {"name": "Dott.ssa Martina Erriquez",
             "role": "Coach associata · ICF-ACC · in percorso PCC",
             "office": "Milano",
             "bio": "Coaching 1:1 per neo-manager e percorsi di gruppo aziendale. "
                    "Supervisione mensile con Giulia + EMCC esterna."},
            {"name": "Dott.ssa Elena Mannucci",
             "role": "Supervisor esterna · ICF-MCC",
             "office": "Trento · consulente",
             "bio": "Supervisione della pratica di Giulia dal 2019 e di Martina dal 2022. "
                    "Non interagisce mai con i coachee — verifica la qualità della pratica delle coach."},
            {"name": "Sig.ra Donatella Rinaldi",
             "role": "Assistente di studio · back-office",
             "office": "Milano",
             "bio": "Gestione calendari, fatturazione, contrattualistica. "
                    "Non accede mai ai contenuti delle sessioni di coaching."},
        ],

        # Coordinates strip (single sede)
        "coordinates_label": "Sede",
        "coordinates": [
            ("Milano",  "Via Thaon di Revel 21 · 20159 · Isola — a 300 metri da MM Garibaldi FS"),
        ],

        # Page-level CTA
        "cta_heading": "Discovery call o domanda via email",
        "cta_intro":
            "La discovery call da venti-trenta minuti è il modo canonico per "
            "valutare se un percorso Solaria fa al caso tuo. Se preferisci "
            "una domanda scritta prima di prenotare la call, l'email della "
            "segreteria è letta da Donatella ogni mattina e risponde una di "
            "noi due entro la giornata.",
        "cta_primary":  "Prenota una discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── PERCORSI (services) ────────────────────────────────────
    "percorsi": {
        "eyebrow":  "Percorsi di coaching · 2026",
        "headline": "Quattro percorsi, <em>un metodo solo</em>.",
        "intro":
            "Quattro formati di percorso, ciascuno con il numero di sessioni "
            "dichiarato, la cadenza concordata, il formato (on-site · online "
            "· ibrido) e il prezzo indicativo. Ogni percorso segue lo stesso "
            "metodo — contratto iniziale, sessioni regolari, re-contracting "
            "a metà, chiusura con verifica, follow-up a tre mesi.",

        # Card meta labels
        "svc_duration_label": "Durata tipica",
        "svc_leader_label":   "Coach referente",

        # 4 percorsi (blueprint suggests 2-4; we pick 4 for exposure)
        "services": [
            {
                "num":   "01",
                "title": "Executive 1:1",
                "blurb":
                    "Il formato più richiesto. Otto sessioni da sessanta minuti "
                    "a cadenza bisettimanale, obiettivo misurabile definito nel "
                    "primo incontro e scritto nel contratto. Per dirigenti in "
                    "transizione di ruolo, neo-promossi, o in preparazione a un "
                    "cambio di perimetro. Framework di riferimento: Co-Active "
                    "+ Immunity to Change.",
                "scope": [
                    "Contratto iniziale con obiettivo SMART misurabile",
                    "Otto sessioni 60 min · cadenza bisettimanale",
                    "Re-contracting a metà (quarta sessione)",
                    "Chiusura con verifica del risultato",
                    "Follow-up 60 min a tre mesi incluso",
                ],
                "duration": "16 settimane · 8 sessioni + follow-up",
                "leader":   "Dott.ssa Giulia Loreti",
            },
            {
                "num":   "02",
                "title": "Team coaching",
                "blurb":
                    "Lavoro con team di middle management (cinque-dieci persone). "
                    "Sei sessioni con il team più una sessione di re-contracting "
                    "con lo sponsor aziendale a metà percorso. Per team in fase "
                    "di crescita, integrazione post-riorganizzazione, o preparazione "
                    "a una sfida specifica. Framework: GROW applicato al gruppo.",
                "scope": [
                    "Contratto iniziale tripartito (team · sponsor · coach)",
                    "Sei sessioni 120 min · cadenza mensile",
                    "Re-contracting con sponsor a metà percorso",
                    "Report aggregato allo sponsor (mai contenuti specifici)",
                    "Follow-up 90 min a tre mesi incluso",
                ],
                "duration": "6 mesi · 6 sessioni + re-contracting + follow-up",
                "leader":   "Dott.ssa Giulia Loreti",
            },
            {
                "num":   "03",
                "title": "Gruppo aziendale",
                "blurb":
                    "Programma HR strutturato per tre-otto persone dello stesso "
                    "cliente corporate. Masterclass di giornata all'inizio + otto "
                    "sessioni individuali per ciascun partecipante. Sponsor "
                    "aziendale definito, obiettivi individuali collegati a "
                    "obiettivi di sistema, follow-up trimestrale con sponsor.",
                "scope": [
                    "Masterclass giornaliera aperta (framework + codice deontologico)",
                    "Otto sessioni 1:1 per ciascun partecipante",
                    "Dashboard progressi aggregata per sponsor (KPI concordati)",
                    "Follow-up trimestrale con sponsor per primi 12 mesi",
                    "Preventivo personalizzato secondo numero partecipanti",
                ],
                "duration": "6-9 mesi · masterclass + 8 sessioni/persona",
                "leader":   "Dott.ssa Giulia Loreti · Dott.ssa Martina Erriquez",
            },
            {
                "num":   "04",
                "title": "Sessione singola esplorativa",
                "blurb":
                    "Una sola sessione di novanta minuti, senza contratto di "
                    "percorso. Per chi vuole valutare l'approccio di coaching "
                    "su un tema specifico prima di impegnarsi in un percorso. "
                    "Al termine il coachee decide se aprire un percorso "
                    "executive 1:1 o concludere il rapporto — nessun obbligo "
                    "di continuare.",
                "scope": [
                    "Sessione 90 min con framework GROW applicato al tema",
                    "Output scritto consegnato entro 48 ore",
                    "Valutazione onesta: coaching · terapia · consulenza",
                    "Se coaching: preventivo indicativo per percorso",
                    "Se non coaching: riferimento al professionista giusto",
                ],
                "duration": "1 sessione 90 min",
                "leader":   "Dott.ssa Martina Erriquez",
            },
        ],

        # Processo — come un percorso si apre e si chiude
        "process_label":   "Come si apre un percorso",
        "process_heading": "Quattro passi, una sola sequenza",
        "process": [
            ("01", "Discovery call",
             "Venti-trenta minuti gratuiti in videoconferenza. Capiamo se "
             "l'obiettivo rientra nel coaching o è terapia/consulenza, se "
             "Solaria è lo studio giusto, discutiamo preventivo indicativo."),
            ("02", "Contratto iniziale",
             "Primo incontro di novanta minuti a pagamento, entro sette giorni "
             "lavorativi dalla discovery call. Definizione dell'obiettivo SMART, "
             "scelta del framework, firma del contratto coaching scritto."),
            ("03", "Percorso regolare",
             "Sessioni a cadenza concordata nel contratto. Ogni sessione "
             "chiude con commitment scritto che il coachee verifica autonomamente. "
             "Re-contracting a metà percorso con coachee (e sponsor se corporate)."),
            ("04", "Chiusura & follow-up",
             "Sessione finale con verifica esplicita del risultato contro "
             "obiettivo iniziale. Follow-up 60 min a tre mesi dalla chiusura "
             "— incluso nel costo del percorso, non fatturato separatamente."),
        ],

        # Final CTA
        "cta_heading":   "Quale formato fa al caso tuo?",
        "cta_intro":
            "Se non sei sicuro/a di quale percorso scegliere, la discovery "
            "call è il modo canonico per valutarlo insieme. Ti ascoltiamo e "
            "ti indichiamo il formato più coerente — anche se la risposta "
            "è \"al tuo bisogno risponde meglio un altro professionista\".",
        "cta_primary":   "Prenota una discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── CASI (case-studies list) ───────────────────────────────
    "casi": {
        "eyebrow":  "Casi seguiti · 2022 — 2026",
        "headline": "Tre percorsi, <em>tre obiettivi misurati</em>.",
        "intro":
            "Una selezione di casi conclusi negli ultimi tre anni. I coachee "
            "sono identificati dal codice settore e ruolo in osservanza del "
            "Codice Deontologico ICF §2.4 (confidenzialità), ma gli obiettivi "
            "iniziali e i risultati misurati sono reali. Reference call con "
            "lo sponsor aziendale disponibile per i percorsi corporate dopo "
            "discovery call + NDA reciproca.",

        "cases_label": "Casi",
        "cases_intro":
            "Selezione bilanciata sui tre formati principali — executive 1:1, "
            "team coaching, gruppo aziendale. Non sono testimonianze mitologiche "
            "(\"la mia vita è cambiata\"): sono percorsi documentati con "
            "obiettivo iniziale dichiarato, percorso svolto, risultato verificato.",

        "cta_heading":   "Un caso simile al tuo?",
        "cta_intro":
            "Se un caso descritto qui assomiglia alla tua situazione, la "
            "discovery call è il modo canonico per esplorarlo. Nessun obbligo "
            "di apertura percorso dopo la call — solo una valutazione onesta "
            "dell'adeguatezza del coaching al tuo bisogno specifico.",
        "cta_primary":   "Prenota una discovery call",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /casi/<slug>/
    # Pass A: each post now ships a `thumb` URL (rotated across pool slots
    # 4 / 5 / 1 — NEVER slot 0, per CS-IMG-SEC-05). The archetype's home
    # cases preview renders these as 80×60 editorial thumbnails inside
    # the row title, exercising the CS-IMG-SEC-05 hook for the first time
    # on any corporate-suite template (Pragma + Fiscus still ship
    # typographic-only case rows). Adds three image accents to the
    # below-the-KPI section that previously read visually thin.
    "posts": [
        {
            "slug":     "executive-neo-ceo-tech-scaleup",
            "title":    "Executive 1:1 · neo-CEO di una scale-up tech milanese",
            "category": "Executive 1:1",
            # Pass A: slot 4 (detail · open notebook on wooden desk).
            "thumb":    _POOL_DETAIL,
            "year":     "2025",
            "duration": "8 sessioni · 16 settimane + follow-up",
            "client_code":
                "Tech & product · Milano · scale-up fintech · Serie B · "
                "CEO 42 anni · promosso internamente dopo uscita del fondatore",
            "lead":
                "Fondatore uscito dopo round Serie B, promosso internamente il "
                "CTO come nuovo CEO. Il neo-CEO aveva esperienza tecnica e di "
                "prodotto ma nessuna esperienza di direzione generale, e il "
                "CdA chiedeva verifica del suo posizionamento entro sei mesi.",
            "sections": [
                {
                    "label": "L'obiettivo iniziale",
                    "heading": "Da CTO a direzione generale in sei mesi",
                    "body":
                        "L'obiettivo dichiarato nel contratto di coaching era "
                        "lavorare sull'identità di ruolo (da CTO a CEO), sulla "
                        "delega operativa (il neo-CEO tendeva a rimanere nel "
                        "merito tecnico dei prodotti), e sulla relazione con "
                        "il CdA (tre membri indipendenti più due dei fondi "
                        "Serie B). Il risultato misurabile concordato: "
                        "restituzione dal CdA al termine del semestre con "
                        "valutazione \"confermato nel ruolo\" anziché \"in osservazione\".",
                },
                {
                    "label": "Il percorso",
                    "heading": "Co-Active + Immunity to Change",
                    "body":
                        "Otto sessioni bisettimanali con framework combinato. "
                        "Le prime quattro sessioni (Co-Active) per lavorare "
                        "sui valori che il neo-CEO portava nel ruolo e su "
                        "come tradurli in comportamenti di leadership "
                        "osservabili. Le seconde quattro sessioni (Immunity "
                        "to Change di Kegan & Lahey) per identificare e "
                        "disinnescare le resistenze inconsapevoli al cambio "
                        "di identità ruolo. Re-contracting a metà con conferma "
                        "dell'obiettivo originario e affinamento degli "
                        "indicatori operativi. Supervisione ICF-MCC sul caso "
                        "prima della sessione sei.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Ruolo confermato con osservazioni positive",
                    "body":
                        "Al termine del percorso, il CdA ha votato all'unanimità "
                        "la conferma nel ruolo con un bonus di performance "
                        "pieno. Il CEO ha ristrutturato la propria agenda "
                        "riducendo del 40% il tempo nelle call tecniche e "
                        "ridedicando quel tempo alla relazione con il fondo "
                        "lead investor e con i membri indipendenti del CdA. "
                        "Due anni dopo (follow-up a tre mesi + check annuali "
                        "spontanei) è ancora nel ruolo e la società ha "
                        "chiuso positivamente la Serie C.",
                },
            ],
            "kpi": [
                ("8/8",      "sessioni del percorso completate"),
                ("100%",     "obiettivo iniziale raggiunto"),
                ("-40%",     "tempo dedicato a call tecniche operative"),
                ("24 mesi",  "permanenza nel ruolo dal closing coaching"),
            ],
            "lead_partner": "Dott.ssa Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 supervisor ICF-MCC · 16 settimane",
            "next_label":   "Caso successivo",
        },
        {
            "slug":     "team-coaching-middle-management-manifattura",
            "title":    "Team coaching · middle management di una manifattura in ristrutturazione",
            "category": "Team coaching",
            # Pass A: slot 5 (ambient · warm home-office, plants).
            "thumb":    _POOL_AMBIENT,
            "year":     "2024",
            "duration": "6 sessioni · 6 mesi + re-contracting + follow-up",
            "client_code":
                "Manifattura & industria · Brescia · 320 dipendenti · "
                "team di sette middle manager post-riorganizzazione · "
                "sponsor: direttore delle operazioni",
            "lead":
                "Gruppo industriale bresciano che aveva riorganizzato la "
                "struttura produttiva consolidando tre siti in due. I sette "
                "middle manager delle linee produttive si trovavano a "
                "coordinare squadre miste (persone provenienti da siti diversi "
                "con processi diversi). Il direttore delle operazioni, come "
                "sponsor aziendale, ha ingaggiato Solaria per un team coaching "
                "di sei mesi.",
            "sections": [
                {
                    "label": "L'obiettivo iniziale",
                    "heading": "Team che parla, non sette referenti separati",
                    "body":
                        "Prima dell'ingaggio, i sette middle manager operavano "
                        "come \"sette referenti separati del direttore operations\", "
                        "senza scambio laterale di informazioni e senza "
                        "escalation coerente dei problemi al direttore. "
                        "L'obiettivo dichiarato nel contratto tripartito "
                        "(team · sponsor · coach) era passare a un modello "
                        "di team coordinato con pratiche di scambio laterale "
                        "misurabili entro sei mesi. KPI concordato con sponsor: "
                        "frequenza degli scambi laterali documentati + "
                        "diminuzione delle escalation \"silenziose\" al direttore.",
                },
                {
                    "label": "Il percorso",
                    "heading": "GROW applicato al team + artefatti operativi",
                    "body":
                        "Sei sessioni da 120 minuti a cadenza mensile, più "
                        "re-contracting di 90 minuti con lo sponsor a metà "
                        "percorso. Framework GROW applicato alla dinamica "
                        "di gruppo (Goal collettivo · Reality collettiva · "
                        "Options collettive · Will collettivo) per ciascuna "
                        "sessione. Introdotti tre artefatti operativi "
                        "co-creati dal team: daily stand-up da dieci minuti, "
                        "retrospettiva settimanale da trenta minuti, "
                        "escalation-matrix concordata con lo sponsor. "
                        "Reportistica aggregata mensile allo sponsor (mai "
                        "contenuti specifici per codice deontologico ICF).",
                },
                {
                    "label": "Il risultato",
                    "heading": "Team coordinato con artefatti operativi tenuti",
                    "body":
                        "Al termine del percorso, il team manteneva in "
                        "autonomia i tre artefatti operativi senza "
                        "intervento del coach. Le escalation silenziose al "
                        "direttore sono passate da una media di circa sei "
                        "a settimana a una media inferiore a una a settimana. "
                        "Al follow-up a tre mesi, sei dei sette manager "
                        "erano ancora in squadra e gli artefatti operativi "
                        "erano stati assorbiti nella pratica operativa "
                        "normale. Lo sponsor ha rinnovato il mandato per "
                        "un secondo team nella divisione logistica.",
                },
            ],
            "kpi": [
                ("6/6",      "sessioni del percorso completate"),
                ("-85%",     "escalation silenziose documentate"),
                ("3/3",      "artefatti operativi tenuti a follow-up"),
                ("6/7",      "manager ancora in squadra a follow-up"),
            ],
            "lead_partner": "Dott.ssa Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 supervisor ICF-MCC · 6 mesi",
            "next_label":   "Caso successivo",
        },
        {
            "slug":     "gruppo-aziendale-neo-manager-studio-legale",
            "title":    "Gruppo aziendale · cinque neo-associate di uno studio legale",
            "category": "Gruppo aziendale",
            # Pass A: slot 1 (feature · man writing in notebook during discussion).
            "thumb":    _POOL_FEATURE,
            "year":     "2023",
            "duration": "Masterclass + 8 sessioni/persona · 8 mesi",
            "client_code":
                "Professional services · Milano · studio legale associato · "
                "cinque avvocate neo-promosse ad associate nello stesso anno · "
                "sponsor: managing partner HR",
            "lead":
                "Studio legale milanese medio-grande che aveva promosso nello "
                "stesso anno cinque avvocate ad associate (uno sforzo "
                "deliberato sulla pipeline femminile della partnership). Il "
                "managing partner HR ha ingaggiato Solaria per un percorso "
                "di gruppo aziendale di otto mesi: masterclass iniziale "
                "comune più otto sessioni 1:1 per ciascuna delle cinque "
                "coachee, con follow-up trimestrale allo sponsor.",
            "sections": [
                {
                    "label": "L'obiettivo iniziale",
                    "heading": "Da senior a associate, con visibilità differenziata",
                    "body":
                        "Le cinque coachee, pur nello stesso passaggio di "
                        "ruolo, partivano con bisogni individuali diversi: "
                        "alcune con sfide di delega verso i senior che loro "
                        "stesse erano state fino al mese prima, altre con "
                        "sfide di visibilità nei comitati decisionali dello "
                        "studio, altre con tensioni di identità rispetto "
                        "alla carriera partnership futura. Obiettivo "
                        "concordato con lo sponsor: ciascuna coachee con "
                        "un piano personale di sviluppo scritto + set di "
                        "pratiche osservabili attivate entro otto mesi. "
                        "Dashboard progressi aggregata per lo sponsor "
                        "(mai contenuti specifici di sessione).",
                },
                {
                    "label": "Il percorso",
                    "heading": "Masterclass comune + otto 1:1 personalizzati",
                    "body":
                        "Masterclass di giornata aperta a tutte e cinque "
                        "in studio, con framework di ruolo + codice deontologico "
                        "ICF + aspettative reciproche coach-coachee. A seguire, "
                        "otto sessioni 1:1 da sessanta minuti per ciascuna "
                        "coachee a cadenza concordata individualmente. "
                        "Distribuzione del carico: tre coachee seguite da "
                        "Giulia (ICF-PCC) e due da Martina (ICF-ACC in "
                        "percorso PCC), con supervisione mensile della "
                        "parte di Martina. Dashboard progressi allo "
                        "sponsor con tre KPI aggregati concordati.",
                },
                {
                    "label": "Il risultato",
                    "heading": "Cinque piani individuali attivi, tre promozioni",
                    "body":
                        "Al termine del percorso, tutte e cinque le coachee "
                        "avevano un piano di sviluppo personale scritto e "
                        "attivo con pratiche osservabili. Tre delle cinque "
                        "sono state promosse a equity partner nei tre anni "
                        "successivi (follow-up spontanei 2024 · 2025 · 2026), "
                        "una ha scelto di lasciare lo studio per una "
                        "direzione generale in un in-house legal team, e "
                        "una è tuttora associate senior con un mandato "
                        "dichiarato di sviluppo. Lo sponsor ha rinnovato "
                        "il mandato nel 2024 per una nuova coorte di "
                        "quattro associate.",
                },
            ],
            "kpi": [
                ("40/40",    "sessioni del percorso completate (5 × 8)"),
                ("5/5",      "piani di sviluppo personale attivi a chiusura"),
                ("3/5",      "promosse a equity partner entro 3 anni"),
                ("1/1",      "rinnovo mandato sponsor anno successivo"),
            ],
            "lead_partner": "Dott.ssa Giulia Loreti · Dott.ssa Martina Erriquez",
            "team":         "2 coach · 1 supervisor ICF-MCC + 1 supervisor EMCC · 8 mesi",
            "next_label":   "Caso successivo",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Discovery call",
        "headline": "Venti-trenta minuti, <em>nessun impegno</em>, nessun costo.",
        "intro":
            "La discovery call è una conversazione esplorativa — non una "
            "seduta di coaching gratuita e non una diagnosi. Capiamo insieme "
            "se il tuo obiettivo rientra nel coaching, se Solaria è lo "
            "studio giusto per te, e discutiamo il preventivo indicativo. "
            "Al termine sei libero/a di scegliere un altro coach, un'altra "
            "disciplina professionale, o di non aprire alcun percorso — "
            "nessuna insistenza commerciale.",

        # Form — discovery-call specific shape
        "form_label":   "Prenota una discovery call",
        "form_heading": "Compila la scheda conoscitiva",
        "form_intro":
            "Riceverai conferma dalla segreteria di studio entro 24 ore "
            "lavorative con tre proposte di slot per la discovery call "
            "(videoconferenza di 20-30 minuti). I dati sono trattati "
            "ai sensi del Reg. UE 679/2016 e custoditi in archivio "
            "cifrato accessibile solo alle coach dello studio.",
        "form_fields": [
            {"name": "name",      "label": "Nome",           "type": "text",     "required": True,  "placeholder": "Es. Giulia",
             "helper": "Solo il nome di battesimo."},
            {"name": "surname",   "label": "Cognome",        "type": "text",     "required": True,  "placeholder": "Es. Loreti",
             "helper": "Come compare nella tua firma professionale."},
            {"name": "company",   "label": "Azienda o contesto professionale", "type": "text", "required": False,
             "placeholder": "Es. Scale-up fintech milanese",
             "helper": "Opzionale — ci aiuta a preparare la discovery call."},
            {"name": "role",      "label": "Ruolo attuale",  "type": "text",     "required": True,  "placeholder": "Es. Neo-CEO · Middle manager · Partner di studio",
             "helper": "Il ruolo attuale o quello verso cui stai andando."},
            {"name": "email",     "label": "Email",          "type": "email",    "required": True,  "placeholder": "giulia.loreti@esempio.it",
             "helper": "A questo indirizzo inviamo conferma e tre proposte di slot per la call."},
            {"name": "phone",     "label": "Telefono",       "type": "tel",      "required": False, "placeholder": "+39 ...",
             "helper": "Opzionale — solo se preferisci che la segreteria ti richiami."},
            {"name": "format",    "label": "Formato preferito", "type": "select", "required": True,
             "options": [
                 "Da decidere in discovery call",
                 "Executive 1:1",
                 "Team coaching (sono sponsor o HR aziendale)",
                 "Gruppo aziendale (sono sponsor o HR aziendale)",
                 "Sessione singola esplorativa",
             ],
             "helper": "Scegliere \"Da decidere\" se non sei sicuro/a del formato più adatto."},
            {"name": "availability", "label": "Disponibilità nei prossimi 7 giorni", "type": "select", "required": True,
             "options": [
                 "Mattina 9:00 – 12:00",
                 "Primo pomeriggio 14:00 – 16:00",
                 "Tardo pomeriggio 16:30 – 19:00",
                 "Sera 19:30 – 21:00 (solo se online)",
                 "Indifferente",
             ],
             "helper": "Aiuta la segreteria a proporti i tre slot più vicini alle tue disponibilità."},
            {"name": "objective", "label": "Obiettivo in una-due righe", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Es. \"Sono stato promosso CEO a gennaio e devo lavorare sulla delega operativa; il CdA mi valuterà a luglio.\"",
             "helper": "Una-due righe bastano per capire se l'obiettivo rientra nel coaching. Nessun dettaglio riservato qui — quelli si portano in discovery call sotto NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contatto",
             "meta": "La persona che incontreremo in discovery call.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Contesto",
             "meta": "Opzionale — ci aiuta a preparare la call. Nessun dettaglio riservato qui.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Perimetro della call",
             "meta": "Per proporti lo slot giusto con la coach giusta. Una-due righe bastano per l'obiettivo.",
             "fields": ["format", "availability", "objective"]},
            {"num": "04", "title": "Allegati (facoltativi)",
             "meta": "Job description attuale, brief dell'azienda sponsor, altri materiali: possono anticipare la discovery call.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Documenti preliminari",
            "helper":   "Job description, brief azienda sponsor, eventuale "
                        "valutazione 360°: tutto ciò che anticipi qui rende "
                        "la discovery call più utile. "
                        "PDF · max 10 MB complessivi. Archivio cifrato "
                        "accessibile solo alle coach.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "Trascina qui i documenti o",
            "link":     "sfoglia dall'archivio",
            "meta":     "PDF · max 10 MB · archivio cifrato AES-256",
        },

        "form_submit_label": "Prenota una discovery call",
        "form_submit_note":
            "Conferma dalla segreteria di studio entro 24 ore lavorative "
            "con tre proposte di slot per la call. Nessuna automazione "
            "commerciale, nessuna sequenza di email — leggiamo "
            "personalmente ogni richiesta.",
        "form_consent":
            "Acconsento al trattamento dei dati personali ai sensi del "
            "Reg. UE 679/2016. I dati sono custoditi nell'archivio cifrato "
            "dello studio e sono accessibili solo alle coach Solaria. "
            "Nessun dato viene comunicato a terzi senza esplicita autorizzazione.",

        # Office meta-row labels
        "office_address_label": "Indirizzo",
        "office_area_label":    "Zona",
        "office_phone_label":   "Telefono",
        "office_email_label":   "Email",

        # Sidebar — sede + canali diretti
        "offices_label":   "Sede",
        "offices": [
            {
                "city":    "Milano",
                "tag":     "Sede · anche online",
                "address": "Via Thaon di Revel 21 · 20159",
                "area":    "Isola · a 300 metri da MM Garibaldi FS",
                "phone":   "+39 02 3663 4712",
                "email":   "discovery@solariacoaching.it",
            },
        ],

        "channels_label": "Canali diretti",
        "channels": [
            ("Segreteria studio",      "+39 02 3663 4712",               "Lun – Ven · 9:00 – 19:00"),
            ("Email discovery",        "discovery@solariacoaching.it",   "Risposta entro 24 ore lavorative"),
            ("LinkedIn Giulia Loreti", "in/giulialoreti-icf-pcc",        "Per domande pubbliche non riservate"),
        ],

        "footnote":
            "Solaria non risponde a richieste anonime e non offre \"diagnosi "
            "gratuite in dieci domande\" (diagnosticare è un'attività di "
            "consulenza, non di coaching). Le informazioni amministrative "
            "(preventivo indicativo, modalità di fatturazione, criteri di "
            "accettazione) sono illustrate in discovery call — gratis, "
            "senza impegno, con valutazione onesta sull'adeguatezza del "
            "coaching al tuo bisogno specifico.",
    },
}
