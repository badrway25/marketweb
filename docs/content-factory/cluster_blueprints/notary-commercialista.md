# Cluster Blueprint · `notary-commercialista`

**Status**: Wave 2 pilot cluster. Pilot template target: `atto-notai-associati`.

---

## 1 · Identity

- **Cluster slug**: `notary-commercialista`
- **Cluster human name (IT)**: Notaio & commercialista
- **Macro-category**: `lawyer`
- **Archetypes that serve this cluster**: `classic-gold`
- **Cluster enrolled since**: X.2 Commit 2

### Identity summary

Studi notarili (notai singoli o associati), studi di revisione legale dei conti, commercialisti con pubblico ufficiale / CTU, studi misti notaio + commercialista + revisore. Il professionista pubblico ufficiale — in particolare il notaio — ha una funzione giuridica peculiare: non è un consulente, è l'incaricato dallo Stato di attribuire pubblica fede ad atti. Il sito deve comunicare questa specificità con sobrietà istituzionale, evitando qualsiasi tono commerciale o di vendita di servizi.

Distinto da `classic-law` (avvocatura contenziosa) e `modern-law-tech` (legal-tech/IP). Distinto anche da `financial-services` (commercialisti non-pubblici-ufficiali).

---

## 2 · Audience

- **Primary audience slugs**: `studio · smb · enterprise`
- **End-customer**: cliente privato per compravendita immobiliare · coniugi per atto matrimoniale · eredi in successione · socio/imprenditore per costituzione società · consiglio di amministrazione per delibera assembleare · ente per pubblicazione atti.
- **Decision maker**: notaio titolare (monocratico o associato · la figura è personale, non trasferibile).

---

## 3 · Positioning

### What the site must achieve (top 3)

1. Comunicare serietà istituzionale: il notaio è un pubblico ufficiale con responsabilità di Stato.
2. Orientare il cliente non-esperto (cosa serve per comprare casa · cosa serve per fare testamento · cosa serve per costituire una SRL) senza improvvisarsi consulente via web.
3. Facilitare il contatto rispettando la diversità dei procedimenti (atti pubblici hanno tempistiche diverse da consulenze).

### What the site must avoid

- "Richiedi il tuo atto online": il notaio riceve fisicamente le parti (tranne limitate eccezioni di atti a distanza autorizzati).
- Claim di velocità: il tempo del notaio dipende dalla documentazione del cliente e da terzi (Agenzia Entrate · ipotecaria · comuni).
- Promozione di un atto a "prezzo base" · "da X€": gli onorari notarili hanno una tabella ministeriale.
- Toni da coaching o consulenza: il notaio non consulta, redige atti pubblici.

### Competitive positioning

`istituzionale · pubblico-ufficiale · procedurale-chiaro`

---

## 4 · Terminology dictionary

| Termine (IT) | Definizione | Sinonimi vietati | Tono / nota |
|---|---|---|---|
| `notaio` | pubblico ufficiale | `notaio-di-fiducia` (improprio) | formale-istituzionale |
| `studio notarile` | organizzazione dello studio | `agenzia notarile` (errato) | formale |
| `atto pubblico` | atto con pubblica fede | — | core |
| `atto notarile` | atto redatto da notaio | — | core |
| `rogito` | atto di compravendita immobiliare | — | quotidiano · ok |
| `autentica di firma` | certificazione firma | `firma notarile` (ok) | tecnico |
| `procura` | conferimento poteri di rappresentanza | — | tecnico |
| `testamento pubblico` | testamento redatto da notaio | `testamento dal notaio` (ok) | tecnico |
| `testamento olografo` | testamento scritto a mano dal testatore | — | tecnico |
| `successione` | procedura ereditaria | — | core |
| `dichiarazione di successione` | documento fiscale post-decesso | — | tecnico-fiscale |
| `donazione` | atto di trasferimento a titolo gratuito | — | core |
| `costituzione di società` | atto nascita ente giuridico | `fondazione` (confondibile) | core |
| `statuto` | documento fondativo società | — | tecnico |
| `delibera assembleare` | decisione organo sociale verbalizzata | — | tecnico |
| `fusione · scissione · trasformazione` | operazioni societarie straordinarie | — | tecnico |
| `mutuo ipotecario` | finanziamento con garanzia immobile | `prestito con ipoteca` | tecnico |
| `ipoteca` | garanzia reale su immobile | — | tecnico |
| `catasto` | registro immobiliare | — | tecnico |
| `visura catastale` | estratto dati immobile | — | tecnico |
| `ispezione ipotecaria` | verifica esistenza ipoteche | — | tecnico |
| `preliminare di compravendita` | promessa di vendita (`compromesso`) | `compromesso` (ok in quotidiano) | tecnico |
| `APE · attestato prestazione energetica` | documento obbligatorio vendita | — | tecnico |
| `tabella onorari notarili` | riferimento tariffario | `tariffario` (ok) | formale |
| `Archivio Notarile` | archiviazione di Stato atti | — | istituzionale |
| `Consiglio Notarile` | organo territoriale della categoria | — | istituzionale |
| `pubblica fede` | valore legale dell'atto notarile | — | formale · concetto core |
| `revisore legale dei conti` | iscritto al Registro dei Revisori | — | formale (se studio misto) |
| `consulente tecnico d'ufficio · CTU` | professionista nominato dal giudice | — | formale |

---

## 5 · Voice & tone

- **Register**: institutional-formal. Distante, ma non scortese. Un tono che riconosce il ruolo pubblico del notaio e la soggezione del cliente non-esperto.
- **Sentence length**: medie, con precisione. Subordinata per la norma citata, principale per l'indicazione operativa.
- **Pronouns**: `Lei` sempre. `il Notaio` (con maiuscola) quando si riferisce al titolare nel suo ruolo istituzionale.
- **Rhetorical devices allowed**: citazione di articoli del codice civile (art. 587 c.c. per testamento pubblico), riferimento a Legge Notarile (L. 89/1913), spiegazione dei documenti da produrre, timeline orientativa di procedure.
- **Rhetorical devices banned**: metafore (`il tuo atto come la chiave di una nuova vita`), urgenze (`ultimi giorni di agevolazione`), promesse (`procedura veloce garantita`), call-to-action da e-commerce.

### Voice anchor

*"Il Notaio è un pubblico ufficiale. Quando firma un atto, attribuisce pubblica fede — significa che quell'atto è credibile senza bisogno di prova ulteriore, in Italia e all'estero. Il nostro studio si occupa di dare a ciascun atto la forma che la legge richiede, e di guidare le parti nella comprensione di quello che stanno firmando. I tempi dipendono dai documenti. Le informazioni dipendono dalla situazione. La consulenza preliminare, gratuita e senza impegno, serve a capire cosa serve."*

---

## 6 · Copy skeleton by page kind

### Home

- **Hero headline**: 8-12 parole · "Studio Notarile" + riferimento a area specializzazione se rilevante.
- **Hero lead**: 2 righe · titolare + sede + aree di competenza principali.
- **Primary CTA**: "Richiedi un primo incontro".
- **Secondary CTA**: "Aree di competenza" (collegamento a pagina atti).
- **3-6 value props**: notaio iscritto da anno X · competenze riconosciute (revisore legale · CTU · ecc.) · multi-lingua se applicabile · archivio integrato · collaborazione con uffici catastali · assistenza anche in lingua straniera.
- **Signature section**: "I nostri atti più frequenti" con 4-6 tipologie + 1 riga di orientamento.

### Il Notaio / Chi siamo

- Bio del Notaio titolare: nome · data iscrizione al ruolo · sede distretto Notarile · eventuali specializzazioni post-laurea · lingue · anni di attività.
- Se studio associato: bio di ciascun Notaio.
- Collaboratori dello studio (praticanti · impiegati · commercialista di studio se misto).

### Aree di competenza

- 6-10 aree: compravendita immobiliare · mutui · successioni · testamenti · donazioni · costituzione società · operazioni straordinarie societarie · procure · autentiche · atti di famiglia.
- Per ciascuna: cos'è · quando serve · documenti da portare · tempistica orientativa.

### Documenti / Cosa portare

- Lista chiara per le procedure più richieste: compravendita, mutuo, successione, testamento, SRL.
- Per ciascuna: documenti obbligatori · documenti utili · tempi orientativi · contatto pre-atto.

### Tariffe / Onorari

- Spiegazione della tabella ministeriale · onorari professionali aggiuntivi · imposte e tasse a parte.
- Modalità richiesta preventivo scritto.
- NO listino pubblico con cifre: pubblicità non ammessa per pubblici ufficiali.

### Contatti

- Indirizzo · telefono · email · form preliminare (nome · tipo di atto · urgenza · contatto).
- Orari ricevimento (spesso su appuntamento).
- Lingue parlate.

---

## 7 · Search keywords pack

### Core
`notaio commercialista revisore contabile atti-notarili`

### Aliases
`studio-notarile rogito successione costituzione-società mutuo-notaio testamento-pubblico`

### Synonyms cross-locale
`notary (en)` · `notaire (fr)` accettati se il cluster template serve clientela espatriata (caso comune nelle città turistiche).

### Exclude
`notaio-economico · migliore-notaio · rogito-rapido · offerta-notaio · atto-online-scontato`

---

## 8 · Imagery pack pointer

Pack target: `imagery/packs/notary-commercialista.md`.

**Direzione imagery**:
- **Soggetti**: stanza dello studio con scrivania imponente in legno, dettaglio di penna stilografica e timbro, mani che firmano un documento (profilo, non frontale), ritratto del Notaio composto (abito · espressione seria), dettaglio di volumi di codice civile su scaffale.
- **Palette**: classic-serif coerente — beige · rosso-porpora muto · oro-muto · legno nobile · cuoio. Evitare tono corporate-freddo (blu · grigio tecnico).
- **Composizione**: classica, simmetrica, grave. Luce calda e morbida.
- **Evitare**: il Notaio con cartella da avvocato contemporaneo (confondibile con avvocato); immagini di "stretta di mano successo"; stock "firma del contratto al chiudere" con smile.

---

## 9 · Audience tags

```
["studio", "smb", "enterprise"]
```

---

## 10 · Price tier rationale

**Tier consigliato**: `premium`.

**Motivazione**: coerente con archetype `classic-gold` (Lex) · target clientela qualificata (compravendite immobiliari, operazioni societarie) · la solidità visiva comunica affidabilità istituzionale. Deviazione verso `standard` solo per studi notarili di piccoli paesi con comunicazione volutamente sobria.

---

## 11 · Feature flag expectations

| Flag | Expected | Rationale |
|---|---|---|
| `has_shop` | `False` | Assolutamente no (atti non si vendono online) |
| `has_booking` | `True` | Richiesta primo incontro è la conversion |
| `has_portfolio` | `False` | Non esistono casi pubblicabili (riservatezza atti) |
| `has_blog` | `False` | Opzionale solo per notai che pubblicano note giuridiche |
| `has_video` | `False` | Inopportuno per lo stile dello studio |
| `has_rtl` | `True` | D-098 |
| `is_multi_page` | `True` | Home + Notaio + aree + documenti + tariffe + contatti |

---

## 12 · Example brand names

- **Atto — Notai Associati** (pilot template)
- **Studio Notarile Conti**
- **Ceccarelli & Partners — Notai**

---

## 13 · Anti-patterns

- ❌ "Il tuo notaio di fiducia a un clic": il notaio non si sceglie come un servizio.
- ❌ Countdown su promozioni di atti: inadeguato al ruolo pubblico ufficiale.
- ❌ Logo con simbolo di "check verde" o "velocità": banalizzazione.
- ❌ "Oltre 1000 rogiti firmati": numeri da vetrina, non da studio notarile.
- ❌ "Il tuo atto notarile in 48 ore": tempistica spesso irrealistica e scorretta.
- ❌ Testimonianze clienti con nome e foto: riservatezza delle parti negli atti.
- ❌ Immagini "stretta di mano + chiavi di casa" con sfondo di casa nuova: tono da agenzia immobiliare.
- ❌ "Esperti in diritto ereditario, societario, commerciale e civile": elenco esaustivo che perde focus.
- ❌ Mescolare identità "notaio e avvocato" se lo studio ha entrambi: sono professioni distinte, separarle.

---

## 14 · D-054 differentiation notes

### Sibling templates

Nessuno pre-pilot.

### Adjacency notes

**Adiacente a**:
- `classic-law` (Lex) — stesso archetipo · stesso registro istituzionale.
- `financial-services` — tono formale · mondo dei numeri/atti.

**Distinto da**:
- `classic-law` — avvocato rappresenta parte in contenzioso/giudizio. Notaio rappresenta lo Stato e attribuisce pubblica fede. Terminologia diversa (azione giudiziaria vs atto pubblico).
- `modern-law-tech` — legal-tech/IP/privacy/startup. Il notaio NON è un consulente tech; il suo ruolo è istituzionale.
- `financial-services` — commercialista gestisce fiscalità e contabilità nel privato. Notaio ha funzione di pubblico ufficiale · atti pubblici · archivio di Stato.
- `corporate-suite` — azienda che si presenta al mercato · tono commerciale. Studio notarile non "si presenta al mercato" · si rende riconoscibile con sobrietà.

### Differentiation matrix (sibling futuri)

1. Specializzazione dominante (immobiliare vs societario vs successioni vs atti di famiglia)
2. Dimensione studio (notaio singolo vs associati vs studio interdisciplinare)
3. Presenza di commercialista/revisore nello studio (studio misto)
4. Lingue di lavoro (IT vs IT + EN · comuni per atti internazionali)
5. Palette (beige-classico vs grigio-scuro-nobile vs cuoio-rosso muto)
6. Location (città-hub finanziario vs provincia · tono diverso)
7. Sezione "internationals" per clientela straniera (sì/no)
8. Tone hero (sobrio-dichiarativo vs ampio-editoriale)
9. Presenza sezione "faq procedure comuni" (sì/no)
10. Eventuale area "notariato digitale" se lo studio usa piattaforme tipo FirmaCert/ADAM

---

## 15 · Changelog

| Data | Autore | Modifica |
|---|---|---|
| 2026-04-20 | Phase Lead | Initial blueprint · X.3 Commit 2 |
