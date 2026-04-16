# Catalog Expansion Strategy

**Sessione 54 · 2026-04-15 · architettura, non implementazione**
**Branch:** `phase-catalog-expansion-strategy-v1`
**Baseline:** `phase-integration-baseline-v14`
**Catalogo corrente:** 20/20 `published_live`, 8 categorie MVP CHIUSE, 19 archetipi spediti, 9/9 con commerce v2.

---

## 1. Executive Summary

Il marketplace ha appena chiuso l'MVP a 20 template `published_live` su 8 categorie. La domanda strategica adesso non è "quanti altri template facciamo", ma **come organizziamo il sistema per arrivare a centinaia di mestieri senza diventare una libreria di quasi-cloni e senza imporci un refactor continuo**.

Questa sessione propone:

- **Un modello a 4 livelli** (categoria → archetipo → **preset professionale** → editor cliente). Il livello "preset professionale" è nuovo e risolve il dilemma "categoria-per-mestiere vs template-per-mestiere".
- **Una tassonomia di 14 categorie top-level** stabili nel medio termine (oggi sono 8). Le restanti coprono **l'asse "mestieri italiani locali"** (automotive, home services, local food, personal services, professional services, education, fitness, hotel, events) che il catalogo MVP non tocca.
- **Una libreria di ~75 preset professionali** che si ottengono **riusando 19 archetipi esistenti + 11 nuovi archetipi**. Riuso aggressivo: il pattern `dermatologia su specialist = ZERO nuovo HTML` (D-051 Option A archetype-reuse) si scala a tutto il catalogo.
- **Una matrice DNA-locked vs editor-editable** che blinda gli invarianti di brand e libera ai clienti la personalizzazione utile.
- **Decisione finale: editor-foundation FIRST, poi preset-driven expansion.** Costruire altri 50 template senza editor è un debito che paghiamo 50 volte. Aprire l'editor su 20 template solidi e poi aggiungere preset è un investimento che si recupera ogni volta.

I 4 deliverable scritti questa sessione:

1. **Questo documento** — strategia ed executive plan.
2. **`PROFESSION_PRESET_TAXONOMY.md`** — registro concreto dei preset professionali con archetipo di provenienza, cosa cambia, cosa resta fisso.
3. **Aggiornamenti coordinati** a `CATEGORY_ROADMAP.md`, `TODO_NEXT.md`, `DECISIONS.md` (D-083 / D-084 / D-085), `AGENT_HANDOFF.md`, `SESSION_LOG.md`.
4. **Memory entry** Session 54 con i pointer ai due nuovi documenti.

Non viene modificato nessun template `published_live`. Nessun nuovo template viene creato. Nessun branch di rollout viene aperto.

---

## 2. Audit del Catalogo Attuale

### 2.1 Stato spedito (snapshot Session 53)

| Categoria | Template `published_live` | Archetipi distinti | Reuso archetipi | Multilingue (5 locali + RTL) |
|-----------|---------------------------|-------------------|-----------------|------------------------------|
| Medical | 5 (cardio · derm · salute · benessere · famiglia) | 4 (specialist · clinic · wellness · family) | sì (cardio + derm su `specialist`) | 5/5 |
| Restaurant | 3 (gusto · sapore · brace) | 3 (fine-dining · trattoria-warm · street-modern) | no | 3/3 |
| Business | 2 (pragma · elevate) | 2 (corporate-suite · startup-saas-landing) | no | 2/2 |
| Portfolio | 2 (chiara · pixel) | 2 (editorial-designer-grid · cinematic-photographer) | no | 2/2 |
| eCommerce | 2 (bottega · luxe) | 2 (artisan-workshop · fashion-editorial) | no | 2/2 |
| Agency | 2 (vertex · aura) | 2 (agency-creative-studio · agency-digital-studio) | no | 2/2 |
| Lawyer | 2 (lex · juris) | 2 (classic-gold · modern-transparent) | no | 2/2 |
| Real-estate | 2 (casa · villa) | 2 (mass-market · ultra-luxury-cinematic) | no | 2/2 |
| **Totale** | **20** | **19 (4+3+2+2+2+2+2+2)** | **1 reuso (derm/specialist)** | **20/20** |

### 2.2 Pattern strutturali consolidati

Il sistema ha distillato — su 53 sessioni — un **kit di pattern riusabili**, non una collezione di hack ad-hoc. I pattern che meritano di diventare la base dell'espansione:

1. **DNA-driven preview compositions** (D-040..D-051). Ogni archetipo è una composizione HTML separata in `templates/preview_compositions/<cat>/<arch>.html` con i suoi token CSS, le sue immagini, il suo silhouette.
2. **Per-archetype skin folders** (Session 11+). `templates/live_templates/<cat>/<arch>/` ospita il sito multi-pagina completo. Stesso archetipo = stessa cartella, diversi template = diversi `template_content_<slug>.py`.
3. **Chrome-Authoring Contract D-047**. Ogni stringa visibile proviene dal content registry, mai hardcoded nello skin. Ha dimostrato di funzionare 14 volte (cardio→derm reuse, poi 13 nuovi archetipi).
4. **Live Preview Law D-053** — baseline pages per categoria, niente template "single-page sponsorizzati".
5. **Premium Differentiation Law D-054** — 10 gate per coppia di sibling, applicati anche a pagine interne. È il motivo per cui Lex e Juris non si confondono.
6. **Tier model D-055/D-057** — `published_live` vs `draft`. Permette di lavorare in pubblico mantenendo la vetrina premium.
7. **Locale-keyed content registry** (D-059/D-063). `TEMPLATE_CONTENT[slug] = {locale: tree}`. Zero gettext/.po. Native voice per locale.
8. **Stub-files-first locale wiring** (Session 41+). Importi stay green; sub-agent translator overwrites lo stub.
9. **8-agent parallel content authoring** — recipe ormai stabile per 4 locali × 2 template per sessione.
10. **Pexels primary CDN** (D-077). Immagini hot-link verificate per sourcing veloce e legalmente pulito.
11. **Live Motion language D-058 + D-061 + D-081**. Profili motion (clinical / editorial / cinematic / off) decidibili per archetipo, con counter dinamici come gate D-054 #11 implicito.
12. **Editor Schema Blueprint D-064**. Non implementato, ma la forma dell'editor è già contrattualizzata.

### 2.3 Limiti strutturali del modello attuale (se lo lasciassimo così verso 100+ professioni)

| Limite | Sintomo se non risolto | Quando esplode |
|--------|------------------------|----------------|
| **No livello "preset professionale"** | Per "panettiere" si aprirebbe una nuova categoria o si forzerebbe restaurant. Entrambe sbagliate. | Già a +5 nuove professioni. |
| **Template = unità di scaling** | 100 mestieri = 100 template = 100 content tree × 5 locali. Insostenibile. | A 30-40 template si rompe la qualità della redazione native-voice. |
| **Skin folders per-archetype, 8-15 pagine ciascuno** | Senza editor, ogni preset professionale richiede un nuovo content tree autoriale di ~3000-9000 LOC × 5 locali. | Già al primo "estetista" sotto wellness diventa evidente. |
| **No campo `profession_preset` su `WebTemplate`** | Browse "trova un template per parrucchiere" non esiste. Solo browse per categoria. | Quando il marketing inizia a parlare ai clienti finali. |
| **No editor cliente** | Ogni template è uno snapshot fisso. Il cliente che vuole sostituire 4 dottori con 4 dentisti deve scaricare e modificare HTML. | È già il limite attuale del prodotto. |
| **No varianti di sezione** | Una sezione "team" è un'unica forma per archetipo. Un dentista che vuole "team con specializzazioni" vs uno psicologo che vuole "team con approccio terapeutico" devono usare la stessa shape. | Evidente al primo onboarding di una vertical. |
| **5 locali, 4 lingue** | OK fino a EU + MENA. Il giorno che serve DE/PT/PL diventa una sessione di lift CHROME_I18N + 4 nuovi tree per template `published_live` × 20 = 80 tree. | Al primo cliente germanico. |
| **Imagery pools per-archetype, IDs cablati** | 14 archetipi = 14 pools = ~84 URL Pexels/Unsplash. Aggiungerne 11 = ~150 URL totali. Verificabile. Aggiungerne 50 = 350 URL. Curatela diventa lavoro a tempo pieno. | A 25-30 archetipi. |

### 2.4 Aree mature vs aree fragili

**Mature** (riusabili immediatamente per espansione):

- Preview pipeline + DNA dimensions
- Per-archetype skin folder pattern
- D-047 chrome-authoring contract
- Locale-keyed content tree con 5 locali + RTL
- Tier gating + selectors centralizzati
- Live motion + live forms + live media + live interactions library
- Commerce v2 (Stripe + payments + merchant scoping + 5 locali)

**Fragili** (richiedono rinforzo prima di scalare a 100+ professioni):

- **Tassonomia top-level**: 8 categorie sono scolpite per il MVP marketplace generico, non per il mondo dei mestieri italiani locali (artigiani, servizi alla persona, retail di quartiere).
- **Slot semantici di sezione**: oggi `team` significa "lista di persone con foto e bio". Per un fabbro o un elettricista significa "1 persona, foto del furgone, certificazioni". Manca la modulazione.
- **Asset library**: Pexels/Unsplash sono OK per stock fashion e medical. Per "salumeria di quartiere" o "carrozzeria con hangar" la qualità degrada. Va prevista una pipeline di sourcing curato.
- **Editor cliente assente**: tutto è snapshot, nessuna personalizzazione. È il blocco principale per scalare a 100+ professioni in modo sostenibile.

### 2.5 Cosa l'audit ci insegna

Tre conclusioni:

1. **L'asse "mestieri italiani locali" è scoperto**. Le 8 categorie attuali coprono il marketplace digitale generico (agency, business, ecommerce, portfolio + 4 verticali), ma non il mondo reale del cliente italiano: meccanico, idraulico, panettiere, parrucchiere. Servono 6-8 nuove categorie top-level.
2. **Il problema "quanti template servono" è la domanda sbagliata**. La domanda giusta è "quanti **archetipi** servono" + "quanti **preset professionali per archetipo** servono". Un archetipo `local-trade-shop` può ospitare 6 preset (panettiere, salumeria, macelleria, pasticceria, gastronomia, formaggi) con stesso skin e contenuti diversi.
3. **Senza editor, non si scala**. Ogni preset richiederebbe un content tree autoriale completo. Con editor, il content tree diventa il **seme** che il cliente personalizza.

---

## 3. Tassonomia Futura Consigliata

### 3.1 Principio di selezione

Una categoria top-level esiste se e solo se:

- **Il cliente la cerca per nome.** "Cerco un sito per la mia palestra" è una categoria. "Cerco un sito per la mia attività di trasporti merci con piccola flotta" non lo è — è un preset.
- **Ha un conversion pattern strutturalmente diverso** dalle altre. "Hotel" ha booking widget + room availability che nessun'altra categoria ha. "Palestra" ha class schedule + abbonamenti.
- **Ospita ≥ 3 archetipi distinti**. Se una categoria può vivere con 1 archetipo, è in realtà un preset di un'altra categoria.
- **Sopravvive al test del catalogo browseable**. Le card della categoria devono leggersi come prodotti diversi da chi sfoglia, non come "altre 30 varianti dello stesso template".

### 3.2 Categorie top-level (medio termine: 14)

| # | Categoria | Slug | Stato | Perché esiste | Archetipi target | Esempi di preset professionali |
|---|-----------|------|-------|---------------|------------------|--------------------------------|
| 1 | Medical & Care | `medical` | ✅ esistente (5 live) | Conversion: booking · CTA: prenota visita · trust: licenze + medici | 4 esistenti + opzionale `pharmacy` | dentista · fisioterapista · psicologo · farmacia · ostetrica · podologo · ottico · veterinario |
| 2 | Restaurant & Food | `restaurant` | ✅ esistente (3 live) | Conversion: prenotazione/ordine · CTA: prenota tavolo / ordina · trust: menu + storia | 3 esistenti + opzionale `bistro-modern` | trattoria · pizzeria · ristorante · steakhouse · sushi · vegano · fine dining · cocktail bar · enoteca · gastropub · brewery |
| 3 | Hotel & Hospitality | `hospitality` | 🆕 NUOVA | Conversion: room booking · CTA: verifica disponibilità · trust: foto stanze + recensioni · sezione availability calendar | 4 nuovi: `boutique-hotel` · `b&b-warm` · `agriturismo-rurale` · `resort-luxury` | hotel cittadino · b&b · agriturismo · masseria · resort SPA · ostello design · rifugio alpino |
| 4 | Local Food Retail | `food-retail` | 🆕 NUOVA | Conversion: ordina/prenota/passa · CTA: ordina la torta / prenota il taglio · trust: filiera + lavorazione · sezione "oggi in vetrina" | 3 nuovi: `bakery-warm` · `deli-counter` · `artisan-food-shop` | panettiere · pasticcere · gelateria · salumeria · macelleria · formaggi · gastronomia · pescheria · enoteca · torrefazione · drogheria bio |
| 5 | Automotive Services | `automotive` | 🆕 NUOVA | Conversion: prenotazione officina · CTA: prenota tagliando / preventivo · trust: certificazioni + flotta auto-cliente · sezione servizi standard | 3 nuovi: `garage-trust` · `bodyshop-clean` · `dealership-showroom` | meccanico · carrozziere · gommista · elettrauto · centro revisioni · detailing · concessionario auto · concessionario moto · ricambi |
| 6 | Home Services & Trades | `trades` | 🆕 NUOVA | Conversion: chiamata/preventivo · CTA: chiama ora / WhatsApp / preventivo gratuito · trust: lavori fatti + tempi · sezione "interventi tipici" | 3 nuovi: `single-trade-pro` (1 mestiere) · `multi-trade-team` (squadra) · `emergency-pro` (h24) | idraulico · elettricista · muratore · falegname · fabbro · imbianchino · pavimentista · piastrellista · serramentista · giardiniere · disinfestatore · spurgo · pronto intervento h24 |
| 7 | Personal Services & Beauty | `beauty` | 🆕 NUOVA | Conversion: prenotazione cabine/poltrone · CTA: prenota appuntamento · trust: foto lavori + team · sezione listino tariffe | 3 nuovi: `salon-fashion` · `barber-classic` · `aesthetic-spa` | parrucchiere donna · barbiere classico · centro estetico · solarium · nail bar · centro tatuaggi · centro massaggi · sopracciglia/ciglia · trucco sposa |
| 8 | Wellness & Fitness | `wellness-fit` | 🆕 NUOVA | Conversion: prova lezione + abbonamento · CTA: prima lezione gratis / iscriviti · trust: trainer + risultati · sezione orari corsi/abbonamenti | 3 nuovi: `gym-strength` · `yoga-studio-soft` · `boutique-fitness-bold` | palestra fitness · CrossFit box · yoga studio · pilates · personal trainer · centro arrampicata · piscina · centro benessere termale · scuola danza · arti marziali |
| 9 | Professional Services | `professional` | 🆕 NUOVA | Conversion: consulenza · CTA: richiedi consulenza · trust: ordini + casi · sezione "servizi advisory" | 3 nuovi: `consultant-advisory` · `accountant-trust` · `notary-institutional` | commercialista · consulente del lavoro · notaio · architetto · ingegnere · geometra · agronomo · perito · agenzia investigativa · traduttore certificato |
| 10 | Education & Training | `education` | 🆕 NUOVA | Conversion: iscrizione corso · CTA: scopri il programma / iscriviti · trust: docenti + diplomi · sezione catalogo corsi + calendario | 3 nuovi: `language-school-bright` · `vocational-academy-pro` · `private-tutor-warm` | scuola di lingue · scuola di musica · scuola di danza · doposcuola · ripetizioni · accademia professionale · corsi di cucina · master/università private · autoscuola |
| 11 | Events & Wedding | `events` | 🆕 NUOVA | Conversion: contatto consulenza evento · CTA: organizza il tuo evento · trust: portfolio eventi · sezione gallery + servizi inclusi | 2-3 nuovi: `wedding-romantic` · `event-planner-corporate` · `catering-events-warm` | wedding planner · event planner · catering eventi · location ricevimenti · animazione · fotografo eventi · DJ · noleggio attrezzature |
| 12 | Lawyer | `lawyer` | ✅ esistente (2 live) | Conversion: consulenza privata · CTA: prenota consulto · trust: pratiche/casi · sezione practice areas | 2 esistenti, possibile 3° `boutique-tax-firm` | avvocato civile · penale · societario · famiglia · lavoro · tributarista · studio associato |
| 13 | Real Estate | `real-estate` | ✅ esistente (2 live) | Conversion: visita immobile · CTA: richiedi visita / dossier privato · trust: immobili + agenzia · sezione listings | 2 esistenti, possibile 3° `commercial-real-estate` | agenzia residenziale · ville di lusso · immobiliare commerciale · gestione locazioni · property finder |
| 14 | Business / Agency / Portfolio / eCommerce | (4 categorie esistenti separate) | ✅ esistenti (8 live totali) | Vetrina prodotto/servizio digitale per knowledge-economy. **Restano 4 categorie distinte**, non sono fuse perché conversion pattern e buyer persona divergono. | 2+2+2+2 esistenti | Espandibili con preset (es. business → SaaS B2B / consulting boutique / corporate institutional / fintech startup / industrial-B2B; agency → branding studio / web-only studio / advertising agency; ecommerce → home-décor / outdoor / artisan-jewelry / specialty-foods; portfolio → illustrator / 3D-artist / motion-designer) |

**Numeri:**
- 14 categorie top-level (oggi 8, +6 nuove).
- ~30 archetipi target (oggi 19, +11 nuovi). Escluse mini-varianti delle categorie esistenti.
- ~75-90 preset professionali concreti (oggi 0 formalizzati, ~20 impliciti nei template live).

### 3.3 Decisioni di accorpamento (e perché NON si fanno categorie ultra-granulari)

**Categorie che NON esistono come top-level** (e perché):

- ❌ **Dentista**, **Fisioterapista**, **Psicologo** — sono **preset** dentro `medical`. Conversion pattern, scheletro pagine, baseline pages sono identici. Cambia solo il contenuto.
- ❌ **Idraulico**, **Elettricista**, **Muratore** — sono preset di `trades`. Conversion (chiamata/WhatsApp/preventivo) e silhouette pagina (hero + servizi-base + lavori fatti + zone coperte + contatto rapido) coincidono.
- ❌ **Panettiere**, **Salumeria**, **Macelleria** — preset di `food-retail`. Stesso archetipo `bakery-warm` o `deli-counter` con contenuto diverso.
- ❌ **Hotel**, **B&B**, **Agriturismo** — sotto `hospitality`. Anche se variano molto in tono, la conversion (room availability + booking + galleria stanze) e l'asset critico (foto stanze + recensioni + posizione mappa) sono comuni.
- ❌ **Yoga**, **CrossFit**, **Pilates** — preset di `wellness-fit`. Stesso conversion (prova lezione + abbonamento + class schedule).
- ❌ **Wedding planner**, **Event planner**, **Catering eventi** — preset di `events`. Portfolio + servizi inclusi + form contatto evento.

**Test di promozione preset → categoria:**

> Promuovi un preset a categoria solo quando: (a) il conversion pattern è strutturalmente diverso da tutto il resto, (b) le baseline pages sono incompatibili, (c) almeno 5+ preset autoriali viventi della stessa famiglia esistono e meritano uno spazio dedicato per browseability.

Esempio applicato: oggi "salone parrucchieri" è preset di `beauty`. Domani, se nascono 15 preset diversi (parrucchiere donna premium, barbiere classico, barbiere brutalist hipster, salone unisex, salone afro, salone bambini, ecc.), può aver senso splittare `beauty` in `hair-salon` e `beauty-spa`. Ma non oggi.

---

## 4. Modello Strutturale Consigliato

### 4.1 Diagramma a 4 livelli

```
┌─────────────────────────────────────────────────────────────────────┐
│  LIVELLO 1 — CATEGORIA (browse + market container)                 │
│  Es: medical · trades · food-retail · hospitality · ...            │
│  - 14 nel medio termine                                            │
│  - Slug URL stabile (/templates/medical/, /templates/trades/, ...) │
│  - Definisce: baseline pages (D-053), CHROME_I18N namespace        │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LIVELLO 2 — ARCHETIPO (struttura · design · conversion DNA)       │
│  Es: clinic · specialist · wellness · family (medical)             │
│      single-trade-pro · multi-trade-team · emergency-pro (trades)  │
│  - 3-5 per categoria                                               │
│  - VIVE come: 1 cartella `templates/live_templates/<cat>/<arch>/`  │
│    + 1 voce `template_dna.py` + 1 composition preview              │
│  - Definisce: HTML scheletro, CSS tokens, motion profile,          │
│    section_order, conversion_pattern, hero/navbar/footer style,    │
│    imagery direction, font_pairing, baseline page kinds            │
│  - Riusabile da N preset (zero new HTML per preset)                │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LIVELLO 3 — PRESET PROFESSIONALE (variante settoriale ready-use)  │
│  Es: dentista · fisioterapista · psicologo (su clinic + specialist)│
│      idraulico · elettricista · muratore (su single-trade-pro)     │
│      panettiere · salumeria · pasticceria (su bakery-warm)         │
│  - 4-8 per archetipo                                               │
│  - VIVE come: 1 voce `profession_presets.py` + content tree IT     │
│    seed + tassonomia tag + palette fork + imagery seed             │
│  - Cosa cambia rispetto all'archetipo: copy, dish/service/product  │
│    names, CTA wording, palette tweak (entro range archetype),      │
│    imagery pool (curated subset), tono di voce settoriale          │
│  - Cosa NON cambia: silhouette, conversion pattern, section_order, │
│    motion profile, baseline page kinds, font pairing               │
│  - Multi-locale: presetto seed in IT, sub-agent traduttori per     │
│    EN/FR/ES/AR (la voce native cambia per locale dentro lo stesso  │
│    preset, esattamente come oggi)                                  │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LIVELLO 4 — EDITOR CLIENTE (personalizzazione finale)             │
│  - Il customer parte da un preset e personalizza:                  │
│    palette (entro brand-safe range), foto, copy, contatti,         │
│    listino, team, orari, sezioni opt-in/opt-out, locali attivi     │
│  - Vincoli enforced: D-047 (zero hardcoded), D-053 (baseline       │
│    pages non eliminabili), D-054 (no recolor di sibling),          │
│    D-057 (`tier=published_live` solo se completeness ok)           │
│  - Persistenza: `CustomerProject` + `ProjectContent` (sparse diff) │
│  - VIVE come: schema in `EDITOR_SCHEMA_BLUEPRINT.md` (esistente)   │
│    + futuri moduli `apps/editor/`                                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Cosa appartiene a ciascun livello (regole nette)

| Livello | Cosa contiene | Cosa NON contiene |
|---------|--------------|-------------------|
| **Categoria** | URL slug, baseline page kinds (D-053), CHROME_I18N namespace, browse facets | HTML, CSS, copy, palette, font |
| **Archetipo** | HTML skin folder, CSS scoped (`.cl-*` / `.tw-*` / ...), motion profile, section_order, hero/navbar/footer style, conversion_pattern, font_pairing, imagery direction, baseline page wirings | Copy specifico (rinviato a content registry), palette finale (rinviata a tokens), nomi propri, dati cliente |
| **Preset professionale** | Content tree seed IT, palette fork (entro range archetype), imagery pool seed, CTA wording settoriale, voice register, tono settoriale, tag tassonomici, page slug suggeriti | HTML (riusa archetype), CSS scoped (riusa archetype), conversion pattern (riusa archetype), section order (riusa archetype salvo opt-in/out di blocchi opzionali) |
| **Editor cliente** | Override palette, override copy, override foto, override team/listino/orari, opt-in/out sezioni opzionali, riordino sezioni, attivazione locali, SEO meta | Cambio archetype (è un nuovo project), cambio conversion pattern (DNA-locked), cambio silhouette (DNA-locked) |

### 4.3 Esempi concreti del modello in azione

**Esempio A — `dentista-studio-bianco-romano` (preset professionale che riusa archetipo esistente):**

- Categoria: `medical`
- Archetipo: `clinic` (esistente, da Salute)
- Preset: `dentista-clinico-pulito` (nuovo)
- Cosa cambia rispetto a Salute: brand "Studio Dentistico Bianco", palette tweak (azzurro clinico → bianco-azzurro/grigio neutrale), team da pediatri/internisti a 3 dentisti + igienista, listino da "visita generale + ECG" a "igiene + faccette + impianti", sezione "prevenzione" diventa "igiene professionale + ortodonzia bambini", page slug stays `home/studio/servizi/prevenzione/medici/contatti/prenota`
- Cosa NON cambia: skin folder `templates/live_templates/medical/clinic/` invariata, conversion pattern booking-widget, section_order, font Nunito Sans + Inter, motion profile clinical
- LOC nuovo: ~600-900 LOC content_dentista_bianco_IT.py (poi 4 traduzioni × ~700 LOC) — **zero new HTML**

**Esempio B — `idraulico-pronto-intervento-roma` (preset su archetipo NUOVO):**

- Categoria: `trades` (NUOVA)
- Archetipo: `emergency-pro` (NUOVO — h24, telefono giant + WhatsApp + form rapido + zone coperte + lavori risolti recenti + recensioni Google)
- Preset: `idraulico-pronto-intervento` (nuovo)
- Cosa cambia rispetto agli altri preset di `emergency-pro` (es. `elettricista-h24`, `spurgo-h24`): palette (blu/giallo idraulico vs giallo/nero elettrico vs verde/grigio spurgo), copy ("Perdita d'acqua? Arrivo in 45 min" vs "Sbalzi di tensione? Diagnosi gratuita" vs "Pozzo intasato? Spurgo entro 90 min"), service list, foto degli interventi tipici (pool pexels distinta), zone coperte, certificazioni di settore
- Cosa NON cambia: skin folder `templates/live_templates/trades/emergency-pro/` (1 sola), conversion pattern phone-and-whatsapp + sticky CTA, section_order, motion profile clinical
- LOC nuovo: 1 nuovo archetipo (skin folder ~3000-5000 LOC) + 1 preset content tree ~700 LOC. Aggiungere il SECONDO preset (es. elettricista-h24) costa solo ~700 LOC.

**Esempio C — `panettiere-cesare-quartiere` (preset su archetipo NUOVO):**

- Categoria: `food-retail` (NUOVA)
- Archetipo: `bakery-warm` (NUOVO — vetrina prodotti del giorno + storia famiglia + lavorazione + sezione "oggi nel forno" + form ordini per occasioni speciali)
- Preset: `panettiere-pane-tradizionale`
- Cosa cambia rispetto a `pasticcere-pane-dolce` o `salumiere-banco-prima-scelta` (altri preset dello stesso archetipo): palette (forno caldo, ocra-marrone vs pasticceria pastello vs salumeria bordeaux), prodotti in vetrina, vocabolario ("filone integrale" vs "millefoglie" vs "guanciale di Amatrice"), tono di voce ("dal 1962, lievito madre" vs "fragranza francese, tecnica italiana" vs "norcineria di tradizione")
- Cosa NON cambia: skin `bakery-warm`, hero photo-frame + chalkboard, conversion pattern (chiamata + WhatsApp + form ordini speciali), section_order

### 4.4 Persistenza schema-level del modello

Per supportare il modello, il database evolve in modo additivo (NO breaking change):

```python
# apps/catalog/models.py — additions

class WebTemplate(models.Model):
    # esistenti…
    profession_preset = models.SlugField(blank=True, db_index=True)
    # es. "dentista-clinico-pulito", "idraulico-pronto-intervento"
    # vuoto = template autoriale (i 20 attuali), non legato a un preset
    
    parent_archetype = models.SlugField(blank=True, db_index=True)
    # es. "clinic", "specialist", "single-trade-pro"
    # popolato per ogni template per fare query "tutti i template che riusano archetype X"

# Nuova app: apps/profession_presets/ (Phase F oltre — vedi roadmap §8)
# Per Phase A/B basta `apps/catalog/profession_presets.py` come dict registry
```

### 4.5 Cosa NON è un livello del modello

- **Pagine** (`home`, `about`, `services`, …) NON sono un livello — sono entità derivate dall'archetype + content registry, già modellate via `pages[]` nel content tree.
- **Sezioni** (hero, facts, manifesto, …) NON sono un livello — sono porzioni del content tree governate dall'archetype `section_order` + customer overrides.
- **Locali** NON sono un livello — sono dimensione orizzontale che attraversa preset (dentista IT/EN/FR/ES/AR) e si gestisce dentro il content tree con la shape `{slug: {locale: tree}}`.
- **Tier** (`published_live` / `draft`) NON è un livello — è uno stato di pubblicazione applicato a un template.

---

## 5. Archetipi per Categoria

Questa sezione propone una matrice **categoria × archetipo** con tutti i tratti di DNA (D-054 dimensions). I 19 archetipi esistenti restano invariati. Gli 11 nuovi sono nuovi e da costruire.

Legenda colonne: HS = hero silhouette, NB = navbar style, CT = conversion pattern, MP = motion profile, IM = imagery direction, FT = font pairing, RU = riusabilità (quanti preset stimati può ospitare).

### 5.1 Medical & Care (4 esistenti + 1 opzionale)

| Archetipo | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `clinic` ✅ | split-booking | solid-phone | booking-widget | clinical | bright clinical teal | Nunito Sans + Inter | home/studio/servizi/prevenzione/medici/contatti/prenota | poliambulatorio · clinica generalista · centro analisi · dentista clinico · ortopedia · centro vaccinale | 8-10 |
| `specialist` ✅ | editorial-serif | minimal-serif | private-request | clinical | cream paper editorial | Cormorant + Inter / Bodoni Moda + Inter | home/studio/visite/medici/pubblicazioni/contatti | cardiologo · dermatologo · oncologo · neurologo · andrologo · ginecologo top-tier · centro fertilità | 6-8 |
| `wellness` ✅ | full-bleed-manifesto | pill-floating | calendar-spot | editorial | sage serene | Cormorant Garamond + Nunito | home/filosofia/rituali/ambienti/professionisti/contatti/prenota | centro olistico · spa medica · centro yoga-terapia · medicina integrata · medicina ayurvedica | 5-7 |
| `family` ✅ | centered-soft | soft-pastel | phone-and-chat | clinical | warm peach | Quicksand + Nunito | home/studio/visite/crescita/pediatre/contatti | pediatra · ostetrica · centro famiglia · centro adolescenza · centro disturbi alimentari | 4-6 |
| `pharmacy` 🆕 (opzionale) | counter-warm + servizi grid | solid-cross | service-and-call | clinical | green-cross natural | Source Sans 3 + Lora | home/farmacia/servizi/prodotti/orari/contatti | farmacia comunale · farmacia notturna · parafarmacia · farmacia rurale | 4-5 |

### 5.2 Restaurant & Food (3 esistenti + 1 opzionale)

| Archetipo | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `fine-dining` ✅ | editorial-plate | serif-centered | concierge-reservation | editorial | dark editorial moody | Playfair + Lato | home/filosofia/menu/atmosfera/diario/prenota | ristorante stellato · cucina autoriale · enoteca con cucina · sushi top-tier · steakhouse fine | 6-8 |
| `trattoria-warm` ✅ | warm-photo-frame | warm-bar | phone-and-whatsapp | clinical | warm cream butter | Libre Baskerville + Source Sans 3 + Caveat | home/menu/storia/forno/eventi/contatti | trattoria · pizzeria napoletana · osteria · pizzeria al taglio · gastropub familiare | 8-10 |
| `street-modern` ✅ | product-cutout | bold-pill | order-now-delivery | cinematic | bright food product | Big Shoulders + Inter + JetBrains Mono | home/menu/lab/moments/ordina/contatti | smashburger · streetfood · pokè · bao · taqueria · vegan fast · cocktail bar | 6-8 |
| `bistro-modern` 🆕 (opzionale) | hero-image-grid | sans-centered | reservation-online | editorial | warm-modern bistro | Inter + Cormorant | home/menu/cucina/eventi/storia/prenota | bistrot · brasserie italiana · cucina contemporanea · veg restaurant · raw food | 5-7 |

### 5.3 Hotel & Hospitality (4 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `boutique-hotel` 🆕 | editorial-cover | minimal-serif | room-availability | editorial | architectural editorial | Cormorant + Inter | home/camere/esperienza/posizione/ristorante/prenota | hotel boutique · hotel design · hotel storico cittadino | 5-7 |
| `b&b-warm` 🆕 | photo-warm-frame | warm-bar | direct-booking | clinical | warm domestic | Lora + Open Sans | home/camere/colazione/dintorni/recensioni/contatti | b&b · piccola pensione · charming home · airbnb-host professionale | 6-8 |
| `agriturismo-rurale` 🆕 | hero-landscape | rustic-bar | call-and-form | clinical | golden-hour countryside | Frank Ruhl + Karla | home/storia/camere/ristorante/attività/contatti | agriturismo · masseria · cascina · rifugio · resort rurale | 6-8 |
| `resort-luxury` 🆕 | fullbleed-cinematic | minimal-dark | concierge-private | cinematic | luxury cinematic | Cormorant Garamond + Montserrat | home/esperienza/suites/SPA/gastronomia/concierge | resort 5* · masseria di lusso · luxury SPA · private island | 4-6 |

### 5.4 Local Food Retail (3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `bakery-warm` 🆕 | photo-frame-product | warm-bar | call-and-orders-form | clinical | warm artisan product | Libre Baskerville + Nunito Sans | home/oggi-in-vetrina/lavorazione/storia/ordini-speciali/contatti | panettiere · pasticcere · gelateria artigianale · cioccolateria · biscottificio | 8-10 |
| `deli-counter` 🆕 | counter-photo-strip | sans-bold | call-and-whatsapp | clinical | counter product strip | Source Sans 3 + Bitter | home/banco/produttori/ricette/eventi/contatti | salumiere · macelleria · pescheria · formaggi · gastronomia da banco · drogheria bio | 8-10 |
| `artisan-food-shop` 🆕 | editorial-portrait | minimal-serif | private-tasting-form | editorial | artisan editorial | Cormorant + Inter | home/produttori/catalogo/laboratorio/storia/contatti | enoteca · torrefazione · oleificio · birrificio · norcineria · tartufaia · caseificio | 6-8 |

### 5.5 Automotive Services (3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `garage-trust` 🆕 | hero-officina | solid-phone | booking-tagliando | clinical | clean garage | Inter + Roboto Mono | home/servizi/officina/preventivo/recensioni/contatti | meccanico · elettrauto · centro revisioni · centro pneumatici · climatizzazione auto | 7-9 |
| `bodyshop-clean` 🆕 | before-after-hero | sans-centered | preventivo-online | clinical | bodyshop precision | Inter + JetBrains Mono | home/lavorazioni/galleria-prima-dopo/preventivo/storia/contatti | carrozziere · centro vetri · detailing · wrapping · centro restauro auto d'epoca | 5-7 |
| `dealership-showroom` 🆕 | cinematic-vehicle | minimal-dark | book-test-drive | cinematic | showroom cinematic | Montserrat + Inter | home/catalogo/marche/finanziamenti/post-vendita/contatti | concessionario auto · concessionario moto · concessionario veicoli commerciali · noleggio premium · car broker | 5-7 |

### 5.6 Home Services & Trades (3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `single-trade-pro` 🆕 | hero-portrait-trade | sticky-phone | call-and-form | clinical | trade portrait + work | Nunito + Inter | home/servizi/lavori/zone-coperte/preventivo/contatti | idraulico singolo · elettricista singolo · falegname · fabbro · imbianchino · piastrellista · serramentista · giardiniere singolo | 10-12 |
| `multi-trade-team` 🆕 | hero-team-truck | warm-bar | call-and-team | clinical | team + crews | Manrope + Inter | home/servizi/squadra/cantieri/preventivo/contatti | impresa edile · ditta multiservizi · ditta ristrutturazioni · impresa pulizie · impresa giardinaggio | 6-8 |
| `emergency-pro` 🆕 | giant-phone-h24 | bold-emergency | phone-priority | clinical | emergency action | Inter + Roboto | home/servizi-urgenti/zone-h24/recensioni/garanzie/contatti | pronto intervento idraulico · elettricista h24 · spurgo · disinfestazione · fabbro h24 · soccorso stradale | 6-8 |

### 5.7 Personal Services & Beauty (3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `salon-fashion` 🆕 | fullbleed-portrait | minimal-serif | book-online | editorial | fashion-portrait | Playfair + Inter | home/servizi/team/galleria/listino/prenota | parrucchiere donna · barbiere fashion · salone unisex premium · salone afro · trucco sposa | 6-8 |
| `barber-classic` 🆕 | vintage-photo-strong | bold-uppercase | walk-in-or-book | editorial | vintage barber | Oswald + Roboto + Roboto Slab | home/servizi/storia/team/listino/prenota | barbiere tradizionale · barbiere vintage · barbiere brutalist · barbiere uomo classico | 4-6 |
| `aesthetic-spa` 🆕 | photo-cinematic-relax | pill-soft | book-treatment | editorial | wellness sensorial | Cormorant + Source Sans | home/trattamenti/cabine/team/listino/prenota | centro estetico · solarium · nail bar · centro massaggi · sopracciglia · centro benessere viso | 7-9 |

### 5.8 Wellness & Fitness (3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `gym-strength` 🆕 | hero-action-bold | bold-pill | trial-class | cinematic | gym dynamic | Bebas Neue + Inter | home/sale-attrezzi/trainer/abbonamenti/calendario/contatti | palestra fitness · CrossFit box · powerlifting · strongman · functional training | 5-7 |
| `yoga-studio-soft` 🆕 | full-bleed-quiet | pill-floating | book-class | editorial | sensorial wellness | Cormorant + Karla | home/filosofia/discipline/insegnanti/calendario/contatti | yoga studio · pilates · centro meditazione · barre · stretching · qi gong | 5-7 |
| `boutique-fitness-bold` 🆕 | hero-class-energy | sans-centered | trial-class-bookwidget | cinematic | boutique fitness energetic | Manrope + Inter | home/discipline/coach/abbonamenti/calendario/contatti | spinning boutique · TRX · indoor cycling · HIIT · barre boutique · piscina coach | 5-7 |

### 5.9 Professional Services (3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `consultant-advisory` 🆕 | editorial-quiet | minimal-serif | private-discovery | editorial | consulting editorial | IBM Plex Serif + Inter | home/approccio/aree/casi/insights/contatti | business consultant · strategy advisor · consulente del lavoro premium · consulente HR · consulente compliance | 6-8 |
| `accountant-trust` 🆕 | split-trust-numbers | solid-blue | book-consultation | clinical | numbers trust | Source Sans 3 + Inter | home/servizi/team/risorse/preventivo/contatti | commercialista · consulente fiscale · revisore dei conti · consulente del lavoro standard · CAF | 5-7 |
| `notary-institutional` 🆕 | classical-cover | serif-institutional | private-appointment | editorial | institutional gravity | Cormorant + Lora | home/studio/atti/competenze/orari/contatti | notaio · studio associato notarile · perito legale · agenzia investigativa istituzionale · ordine professionale | 4-6 |

### 5.10 Education & Training (3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `language-school-bright` 🆕 | hero-students-bright | pill-color | request-info | clinical | bright educational | Manrope + Inter | home/corsi/livelli/insegnanti/calendario/iscrizione | scuola di lingue · doposcuola lingue · esami certificazione · scuola italiano per stranieri | 5-7 |
| `vocational-academy-pro` 🆕 | hero-portfolio-grid | bold-academic | request-brochure | editorial | academy professional | Plus Jakarta + Inter | home/programmi/docenti/sbocchi/iscrizioni/contatti | accademia professionale · master · scuola di cucina · scuola di musica · scuola di danza · scuola di moda | 6-8 |
| `private-tutor-warm` 🆕 | photo-warm-tutor | sans-warm | call-and-form | clinical | warm 1:1 study | Quicksand + Nunito | home/materie/insegnante/risultati/orari/contatti | ripetizioni · tutor singolo · doposcuola di quartiere · tutor universitario · preparazione esami | 4-6 |

### 5.11 Events & Wedding (2-3 NUOVI)

| Archetipo 🆕 | HS | NB | CT | MP | IM | FT | Page kinds | Mestieri target | RU |
|-----------|----|----|----|----|----|-----|-----------|-----------------|----|
| `wedding-romantic` 🆕 | fullbleed-romantic | minimal-script | book-consultation | editorial | romantic wedding | Cormorant + Cardo + Allura | home/servizi/portfolio/storia/contatti/preventivo | wedding planner · catering matrimoni · location matrimoni · fotografo matrimoni · floral design eventi | 4-6 |
| `event-planner-corporate` 🆕 | grid-events-portfolio | sans-bold | private-brief | editorial | corporate events | Inter + Cormorant | home/eventi/case-study/team/brief/contatti | event planner corporate · agenzia eventi · fiere · attivazioni · roadshow · galà aziendali | 4-5 |
| `catering-events-warm` 🆕 (opzionale) | hero-buffet | warm-bar | request-quote | clinical | catering warm food | Lora + Source Sans | home/menu/eventi-tipo/galleria/preventivo/contatti | catering · food truck eventi · banqueting · cucina mobile · noleggio attrezzature catering | 4-5 |

### 5.12 Lawyer / Real-Estate / Business / Agency / Portfolio / eCommerce (esistenti)

Restano com'è — 2+2+2+2+2+2 = 12 archetipi. Espandibili con preset (vedi `PROFESSION_PRESET_TAXONOMY.md`) senza nuovi archetipi nel medio termine.

### 5.13 Conteggio finale archetipi

- **Esistenti:** 19
- **Nuovi proposti (medio termine):** 11 (3 trades + 3 food-retail + 4 hospitality + 3 automotive + 3 beauty + 3 wellness-fit + 3 professional + 3 education + 2-3 events + 1 opzionale pharmacy + 1 opzionale bistro-modern). Totale **17-22** se si include tutto il roadmap; **medio termine ragionevole = 11 nuovi** (uno per nuova categoria nelle prime 6 categorie nuove + 3 per due categorie ricche di varianti — trades e food-retail).

**Numero target finale medio termine: 30 archetipi** (19 esistenti + 11 nuovi). Lungo termine: 35-40.

---

## 6. Preset Professionali — Approccio

I preset professionali concreti vivono nel documento dedicato: **`PROFESSION_PRESET_TAXONOMY.md`** (registro completo, ~75-90 preset).

### 6.1 Cosa è un preset (in 1 frase)

> Un preset professionale è il **content seed completo di un mestiere specifico** sopra un archetipo riusato, autoriale in IT con 4 traduzioni native, palette/imagery curate, pronto per essere clonato dal cliente come `CustomerProject` di partenza.

### 6.2 Cosa cambia tra preset dello stesso archetipo

| Dimensione | Cambia? | Esempio |
|------------|---------|---------|
| Skin folder HTML/CSS | NO | tutti i preset di `clinic` usano `templates/live_templates/medical/clinic/` |
| Conversion pattern | NO | tutti i preset di `clinic` hanno booking-widget |
| Section order | NO (salvo opt-in/out di blocchi opzionali) | tutti i preset di `clinic` hanno hero → stats → servizi → prevenzione → medici → CTA |
| Hero silhouette | NO | tutti i preset di `clinic` hanno split-booking |
| Font pairing | NO | tutti i preset di `clinic` hanno Nunito Sans + Inter |
| Motion profile | NO | tutti i preset di `clinic` hanno motion clinical |
| Palette tokens | TWEAK (entro range archetype) | dentista pulito vs poliambulatorio teal vs ortopedia warm |
| Imagery pool | SI (curated subset di `medical` o nuovo subpool) | dentista usa pool con riuniti odontoiatrici, poliambulatorio usa pool clinico generale |
| Copy/voce settoriale | SI (autoriale per preset) | terminologia dentale vs generalista vs ortopedica |
| Service/dish/product names | SI | "igiene professionale + faccette + impianti" vs "visita generale + ECG + analisi del sangue" |
| CTA wording | SI (entro pattern) | "Prenota una visita" vs "Fissa la prima igiene" vs "Prenota la radiografia" |
| Tag tassonomici | SI | `dentista`, `igiene-orale`, `impianti` vs `cardiologia`, `ECG`, `holter` |

### 6.3 Quando un nuovo preset diventa un nuovo archetipo

Il preset si promuove ad archetipo solo se **rompe ≥ 4 dimensioni D-054**:

- Cambia conversion pattern (es. il preset richiede un calendario di slot live, non una richiesta async)
- Cambia hero silhouette (es. richiede un preventivatore interattivo nel hero, non testo + foto)
- Cambia silhouette generale (es. richiede una sezione listings tipo real-estate che non c'è in `clinic`)
- Cambia motion profile (es. non è più clinical ma cinematic)

Se rompe 0-3 dimensioni → resta preset. Se rompe ≥ 4 → diventa archetipo. Questo è il **gate di promozione preset → archetipo**.

### 6.4 Numeri preset target

| Categoria | Archetipi | Preset target medio termine |
|-----------|-----------|------------------------------|
| Medical | 4-5 | 12-15 |
| Restaurant | 3-4 | 10-12 |
| Hospitality | 4 | 8-10 |
| Food retail | 3 | 12-15 |
| Automotive | 3 | 8-10 |
| Trades | 3 | 15-20 |
| Beauty | 3 | 8-10 |
| Wellness-fit | 3 | 8-10 |
| Professional | 3 | 8-10 |
| Education | 3 | 8-10 |
| Events | 2-3 | 5-7 |
| Lawyer | 2 | 5-7 |
| Real-estate | 2 | 4-6 |
| Business | 2 | 5-7 |
| Agency | 2 | 4-6 |
| Portfolio | 2 | 4-6 |
| eCommerce | 2 | 6-8 |
| **Totale** | **30** | **130-170 preset (target lungo)** |

**Realistico medio termine (Phase B+C, 12-18 mesi):** **75-90 preset**. Lungo termine: 130-170.

---

## 7. DNA-Locked vs Editable Matrix

Questa matrice è il contratto vincolante per quando l'editor verrà acceso. Estende e formalizza la sezione 5 di `EDITOR_SCHEMA_BLUEPRINT.md` allineandola al modello a 4 livelli.

### 7.1 Tassonomia di editabilità

| Livello | Descrizione | Chi può modificare |
|---------|-------------|-------------------|
| **DNA-locked** | Cambia solo se cambi archetipo (= nuovo CustomerProject). Contratto del marketplace, non modificabile dal cliente. | Solo team marketweb (decisione architetturale per archetipo) |
| **Preset-driven** | Stabilito dal preset professionale. Il cliente può fare override entro il range del preset (palette tweak, imagery alternative). | Cliente entro range preset |
| **Editor-editable** | Personalizzazione cliente vera. Copy, foto, contatti, listino, team, sezioni opt-in/out. | Cliente liberamente |
| **Tier-gated** | Editabile solo da tier `pro` o `business` del marketplace (dopo lancio commerciale). | Cliente abbonato a tier alto |
| **Don't expose v1** | Non esporre nell'editor v1 perché complica senza valore aggiunto. Esponi quando arriva un caso reale. | (nessuno per ora) |

### 7.2 Matrice completa per dimensione

| Dimensione | DNA-locked | Preset-driven | Editor-editable | Tier-gated | Don't expose v1 |
|------------|:----------:|:-------------:|:---------------:|:----------:|:---------------:|
| **Archetype** (HTML skin) | ✅ | | | | |
| **Hero silhouette** (split / fullbleed / editorial / centered / cutout) | ✅ | | | | |
| **Navbar style** (solid-phone / pill-floating / minimal-serif / …) | ✅ | | | | |
| **Footer style** (4col / compact / spa-social) | ✅ | | | | |
| **Section order (default)** | | ✅ (preset baseline) | ✅ (cliente riordina, MA non rimuove baseline) | | |
| **Conversion pattern** (booking / phone / private-request / …) | ✅ | | | | |
| **Motion profile** (clinical / editorial / cinematic / off) | | ✅ (default) | ✅ (cliente sceglie tra 4) | | |
| **Font pairing** (heading + body) | | ✅ (default) | ✅ (cliente sceglie da curated list) | | |
| **Palette tokens** (primary / secondary / accent / paper) | | ✅ (preset baseline) | ✅ (entro contrast gate D-054) | | |
| **Density** (compact / medium / airy / very-airy) | | ✅ (default) | ✅ (cliente sceglie 3-4 step) | | |
| **Imagery direction** (high-level brief) | ✅ | | | | |
| **Imagery pool key** | | ✅ (preset baseline) | ✅ (cliente carica le sue) | | |
| **Hero copy** (headline / eyebrow / intro) | | ✅ (preset seed) | ✅ | | |
| **Hero stats / facts** | | ✅ (preset seed, 0-4 items) | ✅ | | |
| **Section copy** (manifesto / about / services / …) | | ✅ (preset seed) | ✅ | | |
| **Service / Visit / Product / Dish list** | | ✅ (preset seed) | ✅ (add/remove/reorder entro min/max) | | |
| **Team / Doctors / Operators list** | | ✅ (preset seed) | ✅ (add/remove/reorder) | | |
| **Pricing / Pricelist** | | ✅ (preset seed) | ✅ | ✅ (commerce-tier) | |
| **Contact info** (address / phone / email / hours) | | | ✅ | | |
| **WhatsApp / chat channel** | | ✅ (preset default) | ✅ | | |
| **Map / location** | | ✅ (preset placeholder) | ✅ | | |
| **Form fields** (label / placeholder / type / options) | | ✅ (preset seed) | ✅ (add/remove entro min hard) | | |
| **Form hard fields** (name + email + phone + date for `appointment`) | ✅ | | | | |
| **CTA wording** | | ✅ (preset seed) | ✅ (entro brand voice) | | |
| **Blog enabled / disabled** | | ✅ (preset default) | ✅ | | |
| **Blog post listing variant** | | ✅ (preset default) | ✅ (3 choices) | | |
| **Blog post layout** | | ✅ (preset default) | ✅ (2 choices) | | |
| **Sezioni opzionali opt-in/out** | | | ✅ (visibility toggle) | | |
| **Sezioni baseline (D-053)** | ✅ (cannot be removed) | | | | |
| **Locale set** (which of 5 active) | | ✅ (preset default IT) | ✅ (add EN/FR/ES/AR) | ✅ (full 5-locale = pro tier) | |
| **Locale tree per locale** | | ✅ (preset seed if active) | ✅ | | |
| **SEO meta per page** (title / description / og_image) | | ✅ (preset seed) | ✅ | | |
| **Page slug (custom URL)** | ✅ (`home` locked) | | ✅ (URL-safe, IT canonical preferito) | | |
| **Page kind** (home / about / services / blog / …) | ✅ (DNA enum) | | | | |
| **Add new page** (within supported kinds) | | | ✅ | | |
| **Custom HTML / Custom CSS injection** | | | | | ✅ (Don't expose v1 — premium-quality risk) |
| **Custom JS injection** | | | | | ✅ (Don't expose v1 — security + perf risk) |
| **Per-section CSS overrides** | | | | | ✅ (Don't expose v1 — frammenta DNA) |
| **Domain mapping** | | | | ✅ (commerce-tier) | |
| **Stripe keys / payment provider** | | | | ✅ (commerce-tier) | |
| **Multi-tenant / multi-storefront** | | | | ✅ (business-tier) | |
| **Editor di team multi-utente** | | | | ✅ (business-tier) | |

### 7.3 Decisioni vincolanti

1. **DNA-locked è davvero locked.** L'editor non espone mai un'opzione di cambio archetype. Cambiare archetype = nuovo `CustomerProject`. Questo evita il caos "cliente che cerca di forzare specialist a fare booking-widget".
2. **Preset-driven è il default editabile.** Quando il cliente apre l'editor, i campi mostrano i valori del preset come placeholder + valore corrente; reset = torna al preset. Non al template autoriale generico, MAI.
3. **Editor-editable rispetta sempre i contract D-047 + D-053 + D-054 + D-057.** L'editor blocca a livello UI o validation gli stati che violano (es. provare a rimuovere baseline page → warning bloccante; provare a impostare palette identica a sibling → suggerimento accent shift; provare a pubblicare con campi required vuoti → tier resta `draft`).
4. **Tier-gated arriva DOPO Phase Editor v1.** Phase Editor v1 espone solo `Editor-editable`. Tier-gated entra in Phase G (commerce + tier monetization).
5. **Don't expose v1 NON è "mai esporre".** È "non esporre v1 perché complica il quality floor". Quando ci sarà una use-case forte (es. cliente design-team che vuole iniettare CSS), riconsidereremo.

---

## 8. Strategia Editor — Decisione Esplicita

### 8.1 La domanda

> È più giusto fare subito molti nuovi template (50+) e poi costruire l'editor, oppure fermarsi prima e costruire l'Editor Foundation v1 con i 20 template attuali?

### 8.2 La risposta: **Editor Foundation v1 PRIMA, poi preset-driven expansion**

**Motivazioni:**

1. **Costo lineare vs costo amortizzato.** Senza editor, ogni nuovo preset professionale costa ~600-900 LOC IT + 4 traduzioni (~700 LOC × 4) = ~3500-5000 LOC totali. Con editor, il preset è uno **snapshot seed** che il cliente clona e personalizza — il preset diventa un asset 1-volta, non un asset N-volte. Sopra 30-40 preset il delta è enorme.
2. **Native voice non è scalabile a mano.** Mantenere "panettiere voice = Madia EN, Le Pain Quotidien FR, Forn Sant Antoni ES, ovens of Cairo AR" su ciascun nuovo preset richiede un copywriter native per locale per preset. A 75 preset = 75 × 5 copywriter pass = insostenibile per redazione interna. **L'editor sposta l'autorialità sul cliente** (che usa il preset come stencil + sostituisce i suoi nomi/dati/foto), liberando il team marketweb dal collo di bottiglia copywriter.
3. **Il modello a 4 livelli funziona solo con editor.** Senza editor, il "preset professionale" è un altro template — la differenza tra preset e template scompare. Con editor, il preset diventa un seed che ha **valore amplificato** dal customer fork.
4. **L'EDITOR_SCHEMA_BLUEPRINT è già autoriale e completo** (Session 30, D-064). Non stiamo partendo da zero. Lo scaffold di `apps/editor/` è già nell'ARCHITECTURE.md. Lo stato persistenza è già delineato (`CustomerProject` + `ProjectContent` + `ProjectDesignTokens`). Manca l'implementazione dei moduli, ma il contratto esiste.
5. **Phase 3 unblock gate è MET** (Session 53). La roadmap esplicitamente sblocca "auth / checkout / editor / projects / commerce" a 20/20 `published_live`. Quel momento è ora.
6. **Test reale del modello.** I 20 template attuali coprono 8 categorie con 14 archetipi. **Sono un campione sufficiente** per validare il modello editor su tutte le shape (medical/specialist con form complessi, restaurant con menu+wine, ecommerce con storefront+commerce v2, portfolio con project_detail, real-estate con listings, lawyer con practice_areas). Aggiungere 50 nuovi template prima dell'editor non aumenta l'evidenza che ci serve — la satura.

### 8.3 Cosa "Editor Foundation v1" significa concretamente

| Modulo Editor v1 | In scope | Out of scope (rinviato a v2+) |
|------------------|----------|------------------------------|
| `CustomerProject` model + admin CRUD | ✅ | |
| `ProjectContent` sparse-diff overlay (per-locale) | ✅ | |
| `ProjectDesignTokens` overlay (palette / fonts / motion / density) | ✅ | |
| Live renderer reads from project (not solo da static registry) | ✅ | |
| Form-based editor UI (server-rendered, no SPA) — text/image/list/toggle/select/color/font widgets | ✅ | |
| Add/remove/reorder items in `list<T>` con min/max constraint | ✅ | |
| Visibility toggle per sezione | ✅ | |
| Section reorder (drag & drop, hero locked first, CTA locked last) | ✅ | |
| Locale activation + per-locale tree editor | ✅ | |
| Preset library — clona preset → CustomerProject seed | ✅ | |
| Tier validation (D-057): blocca publish_live se completeness < 100% required | ✅ | |
| D-054 sibling-distance check: blocca palette+font+hero+section_order combo che cade entro 2/10 di sibling | ✅ | |
| D-053 baseline page enforcement: blocca rimozione baseline | ✅ | |
| Image upload + library picker | ✅ (v1: upload + library; v2: AI generation) | AI image gen |
| Custom HTML/CSS/JS injection | | ❌ rinviato (v2+) |
| Multi-user team editing | | ❌ rinviato (v3+) |
| Live SPA editor con WebSocket | | ❌ v1 = page-reload-based |
| AI copywriter assist | | ❌ rinviato (v3+) |
| A/B testing variant | | ❌ rinviato (v3+) |
| Analytics dashboard | | ❌ rinviato (v3+) |

### 8.4 Quanto costa Editor Foundation v1

Stima ragionata (parallelo ai pattern già usati):

- **Models + migrations**: 1-2 sessioni
- **Live renderer overlay**: 2-3 sessioni
- **Form-based editor UI v1** (server-rendered, ~30-40 form per archetype): 4-6 sessioni
- **Preset library + clone**: 1-2 sessioni
- **D-053/D-054/D-057 validators**: 2-3 sessioni
- **Image upload + library**: 1-2 sessioni
- **Locale management UI**: 1-2 sessioni
- **End-to-end QA + smoke**: 2-3 sessioni

**Totale stimato: ~14-23 sessioni** (3-5 settimane parallele a roadmap normale).

### 8.5 Come evitare di rifare lavoro quando i preset cresceranno

Tre regole vincolanti per l'editor v1:

1. **Editor v1 NON deve sapere dei preset.** Editor v1 modifica un `CustomerProject`. Il `CustomerProject` viene creato da un seed (template autoriale o preset). L'editor non sa se il seed era preset o template — lavora sul project. **Quando i preset cresceranno**, basta aggiungerne nel registry + far apparire la nuova card "clona preset"; l'editor non cambia.
2. **Schema additivo, mai breaking.** Ogni nuovo `kind` di sezione (es. `class_schedule` per `gym-strength`) è additivo. L'editor mostra il nuovo `kind` solo per gli archetypi che lo dichiarano. Nessuna migrazione su template esistenti.
3. **DNA `template_dna.py` resta source of truth per ciò che è locked.** L'editor legge `template_dna.py` per sapere cosa esporre. Aggiungere un nuovo archetype = aggiungere DNA entry; l'editor lo accoglie senza cambi.

---

## 9. Priorità di Espansione (Rollout Roadmap Eseguibile)

### 9.1 Fasi proposte

```
Phase A — Editor Foundation v1                          ← PROSSIMI 2-3 mesi
  ↓
Phase B — Trades + Local-food preset library            ← 2 mesi
  ↓
Phase C — Beauty + Wellness-fit preset library          ← 2 mesi
  ↓
Phase D — Hospitality + Automotive preset library       ← 2 mesi
  ↓
Phase E — Professional + Education preset library       ← 2 mesi
  ↓
Phase F — Events + preset extension delle 8 cat MVP     ← 2 mesi
  ↓
Phase G — Tier-gated features + commerce monetization   ← 2-3 mesi
```

### 9.2 Phase A — Editor Foundation v1 (PRIORITÀ ASSOLUTA)

**Goal:** aprire `apps/editor/` su tutti i 20 template attuali. Un cliente può clonare un template, modificare copy/foto/team/listino/contatti/palette/font, attivare locali, pubblicare in `draft` o `published_live`.

**Sub-phasing:**
1. **A.1** — Models, migrations, admin CRUD per CustomerProject/ProjectContent/ProjectDesignTokens
2. **A.2** — Live renderer overlay (project.json overlay sopra registry)
3. **A.3** — Editor UI v1 form-based per gli 8-10 `kind` più frequenti (nav/hero/section/form/contact/blog/footer/locale)
4. **A.4** — Preset library = lista template autoriali con "clona" CTA
5. **A.5** — Validators D-053/D-054/D-057 + tier flip
6. **A.6** — Image upload + library
7. **A.7** — Locale activation + per-locale tree editor
8. **A.8** — End-to-end QA + smoke harness

**Rationale per A.4:** introdurre la card "clona preset" anche se i preset ancora sono solo i 20 template autoriali. Quando in Phase B+ arrivano i preset veri, l'infrastruttura clonatore esiste già.

**Decisione bloccante:** durante Phase A, **NESSUN nuovo template / archetipo / preset** viene aggiunto. La protezione di "non scalare prima di avere editor" è binding.

### 9.3 Phase B — Trades + Local-food (preset library prima espansione)

**Perché iniziare da queste due:** sono **categorie ad alto numero di mestieri italiani locali, con conversion pattern semplice (telefono/WhatsApp/form), bassa complessità tecnica, alta domanda di mercato**. Ogni preset costa poco perché riusa molto.

**Trades:**
- 3 nuovi archetypi: `single-trade-pro`, `multi-trade-team`, `emergency-pro`
- 12-15 preset target: idraulico · elettricista · muratore · falegname · fabbro · imbianchino · piastrellista · serramentista · giardiniere · pronto intervento idraulico · pronto intervento elettrico · spurgo · disinfestazione · impresa edile · impresa pulizie

**Local-food retail:**
- 3 nuovi archetypi: `bakery-warm`, `deli-counter`, `artisan-food-shop`
- 12-15 preset target: panettiere · pasticcere · gelateria · cioccolateria · biscottificio · salumeria · macelleria · pescheria · formaggi · gastronomia · drogheria bio · enoteca · torrefazione · oleificio · birrificio

**Output Phase B:** **6 nuovi archetypi** + **24-30 preset** + categoria `trades` e `food-retail` aperte sul marketplace.

### 9.4 Phase C — Beauty + Wellness-fit

- 6 nuovi archetypi: `salon-fashion`, `barber-classic`, `aesthetic-spa` + `gym-strength`, `yoga-studio-soft`, `boutique-fitness-bold`
- 16-20 preset

### 9.5 Phase D — Hospitality + Automotive

- 7 nuovi archetypi: `boutique-hotel`, `b&b-warm`, `agriturismo-rurale`, `resort-luxury` + `garage-trust`, `bodyshop-clean`, `dealership-showroom`
- 16-20 preset

### 9.6 Phase E — Professional + Education

- 6 nuovi archetypi: `consultant-advisory`, `accountant-trust`, `notary-institutional` + `language-school-bright`, `vocational-academy-pro`, `private-tutor-warm`
- 16-20 preset

### 9.7 Phase F — Events + Preset extension MVP

- 2-3 nuovi archetypi `wedding-romantic`, `event-planner-corporate`, opzionale `catering-events-warm`
- 5-7 preset events
- **+ Preset extension** delle 8 categorie MVP esistenti (es. medical aggiunge dentista/fisioterapista/psicologo come preset; restaurant aggiunge pizzeria napoletana/sushi/pokè; ecommerce aggiunge home-décor/specialty-foods)
- 20-30 preset MVP-extension

### 9.8 Phase G — Tier monetization + commerce

- Tier free / pro / business
- Domain mapping
- Multi-storefront, multi-user
- Stripe Connect multi-account
- Coupons, refunds, tax engine
- Marketplace fee + commissioni

### 9.9 Riepilogo numeri finali roadmap

| Phase | Archetypi nuovi | Preset nuovi | Categorie nuove | Mesi stimati |
|-------|----------------|--------------|-----------------|--------------|
| A — Editor v1 | 0 | 0 | 0 | 2-3 |
| B — Trades + Food retail | 6 | 24-30 | 2 | 2 |
| C — Beauty + Wellness-fit | 6 | 16-20 | 2 | 2 |
| D — Hospitality + Automotive | 7 | 16-20 | 2 | 2 |
| E — Professional + Education | 6 | 16-20 | 2 | 2 |
| F — Events + MVP extension | 3 | 25-37 | 1 | 2 |
| G — Tier + commerce | 0 | 0 | 0 | 2-3 |
| **Totale 14-16 mesi** | **+28** | **+97-127** | **+9** | **14-16** |

Stato finale catalogo dopo Phase G: **48 archetypi, 120-150 preset, 17 categorie, multi-tier monetization attiva**.

---

## 10. Proposta Numerica + Decisione Finale

### 10.1 Numeri target di sintesi

| Asse | Oggi (Session 53) | Medio termine (post Phase F) | Lungo termine |
|------|-------------------|------------------------------|---------------|
| **Categorie top-level** | 8 | **14-16** | 17-20 |
| **Archetipi totali** | 19 | **28-30** | 35-40 |
| **Archetipi per categoria** | 2-4 | **2-4** (constante) | 2-5 |
| **Preset professionali** | 0 (impliciti nei 20 template) | **75-90** | 130-170 |
| **Preset per categoria** | n/a | **5-12** | 8-15 |
| **Template autoriali** (i 20 attuali) | 20 | 20-25 (no più di 1-2 nuovi per archetipo nuovo) | 25-30 |
| **CustomerProject derivati da preset** | 0 | dipende dal mercato | dipende dal mercato |
| **Locali supportati** | 5 (it/en/fr/es/ar) | 5 → 7 (+ de + pt) | 7-10 |

### 10.2 Sequenza editor-vs-templates

- **Pre-editor (oggi, Session 54):** 20 template autoriali, 0 preset.
- **Phase A:** 20 template autoriali, 0 preset, **Editor v1 acceso**.
- **Post Phase B-C-D-E-F:** 25-30 template autoriali (non gonfiati), **75-90 preset** che vivono in `profession_presets.py` + content seeds, ogni preset moltiplicato dai CustomerProject.

### 10.3 Decisione finale (testo binding per i prossimi 6 mesi)

> **Phase A — Editor Foundation v1 — è il prossimo workstream.**
>
> Nessun nuovo template `published_live`, nessun nuovo archetipo, nessuna nuova categoria viene aperta finché Phase A non è chiusa con i criteri di accettazione di §8.3.
>
> Durante Phase A, le sessioni di catalog espansione si concentrano su:
> - Documentazione del modello (questa sessione, Session 54)
> - Eventuali fix critici sui 20 `published_live` (security, accessibility, mobile audit)
> - Nessuna nuova autorialità di template/preset
>
> Quando Phase A chiude, **Phase B (Trades + Local-food retail)** apre la prima ondata preset-driven, validando il modello a 4 livelli su categorie ad alta densità di mestieri italiani locali.
>
> Il modello di sviluppo cambia da "n template autoriali, content tree manuale" a "1 archetipo skin + n preset seed + clienti che forkano via editor". Questa è la transizione strategica chiave del prodotto.

### 10.4 Criterio di successo (binding)

A 12 mesi da oggi (2027-04), il prodotto è in salute se:
1. ✅ Editor Foundation v1 è in produzione, usato da almeno N customer-project reali
2. ✅ Catalogo offre 14+ categorie, 28+ archetipi, 75+ preset
3. ✅ I 20 template originari sono **invariati o solo polished** — zero rewrite
4. ✅ Customer può clonare un preset, personalizzare in <30 min, pubblicare in `draft` in <1 ora, in `published_live` quando completo
5. ✅ Multi-locale rimane native-voice (no machine translation) per template autoriali; per CustomerProject il customer carica le sue traduzioni
6. ✅ Premium Differentiation Law D-054 resta passata su tutte le coppie sibling (anche tra preset diversi della stessa categoria)
7. ✅ Zero violazioni Live Preview Law D-053 (ogni `published_live`, sia template sia CustomerProject, ha le baseline pages complete)

---

## 11. Riassunto in 12 punti

1. **Catalogo MVP è chiuso a 20/20 `published_live` su 8 categorie.** Phase 3 unblock gate MET.
2. **Il sistema ha pattern di sviluppo molto solidi** (DNA, D-047 chrome contract, D-053/D-054/D-057, locale-keyed registry, archetype reuse). Sono la base affidabile per scalare.
3. **L'asse "mestieri italiani locali" è scoperto.** Servono 6-8 nuove categorie top-level (trades, food-retail, hospitality, automotive, beauty, wellness-fit, professional, education, events).
4. **Modello a 4 livelli risolve il dilemma "categoria-per-mestiere vs template-per-mestiere":** categoria → archetipo → **preset professionale** → editor cliente.
5. **30 archetipi medio termine** (19 esistenti + 11 nuovi). 35-40 lungo termine.
6. **75-90 preset professionali medio termine.** 130-170 lungo termine.
7. **DNA-locked vs editor-editable matrix è completa** (sezione 7) e allineata a `EDITOR_SCHEMA_BLUEPRINT.md`.
8. **DECISIONE: Editor Foundation v1 PRIMA, poi preset-driven expansion.** Nessun nuovo template autoriale prima dell'editor.
9. **Phase A (Editor v1) costa ~14-23 sessioni / 2-3 mesi.**
10. **Phase B-F (preset rollout) procede categoria-per-categoria** con priorità `trades + food-retail` → `beauty + wellness-fit` → `hospitality + automotive` → `professional + education` → `events + MVP extension`.
11. **Le 8 categorie MVP esistenti restano invariate.** Nessuna fusione, nessuno spostamento, nessun rebrand. Si espandono con preset, non con riassetto.
12. **Phase G (tier monetization + commerce extensions)** chiude il ciclo a ~14-16 mesi.

---

## Pointer

- **`PROFESSION_PRESET_TAXONOMY.md`** — registro concreto dei 75-90 preset.
- **`CATEGORY_ROADMAP.md`** — aggiornato a 14 categorie + Phase A-G.
- **`EDITOR_SCHEMA_BLUEPRINT.md`** — contratto editor (D-064, esistente).
- **`DECISIONS.md`** — D-083 (Modello a 4 livelli), D-084 (Tassonomia 14 categorie), D-085 (Editor-first sequencing).
- **`AGENT_HANDOFF.md`** — istruzioni Session 54 → Phase A.
- **`SESSION_LOG.md`** — entry Session 54.
