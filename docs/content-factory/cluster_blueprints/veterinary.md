# Cluster Blueprint · `veterinary`

**Status**: Wave 2 pilot cluster. Pilot template target: `petro-veterinario`.

---

## 1 · Identity

- **Cluster slug**: `veterinary`
- **Cluster human name (IT)**: Veterinario
- **Macro-category**: `medical`
- **Archetypes that serve this cluster**: `specialist`
- **Cluster enrolled since**: X.2 Commit 2

### Identity summary

Ambulatori veterinari, cliniche veterinarie pluri-specialistiche, veterinari specializzati (dermatologia veterinaria, cardiologia, ortopedia, chirurgia, comportamentalisti animali). Il cliente è un proprietario (pet-parent) che porta un essere vivente non parlante. Il sito deve: riconoscere l'ansia (spesso maggiore del paziente umano), dichiarare specializzazioni e apparecchi, facilitare la prenotazione · includere l'emergenza 24h se offerta. Distinto da `specialist` (medicina umana) per animale-parlante target, e da `family-pediatric` per target non-umano.

---

## 2 · Audience

- **Primary audience slugs**: `smb · studio`
- **End-customer**: proprietario di cane/gatto 28-65 anni · amante animali esotici (conigli · roditori · uccelli · rettili) · proprietario di cavalli (buiatria/ippiatria se lo studio la fa) · allevatori.
- **Decision maker**: veterinario titolare (1-3 soci) o direttore sanitario di clinica medio-grande.

---

## 3 · Positioning

### What the site must achieve (top 3)

1. Essere rassicurante di fronte a situazioni che variano dal richiamo vaccinale all'urgenza notturna.
2. Dichiarare le specie trattate (cani/gatti · esotici · rettili · uccelli · cavalli).
3. Comunicare trasparenza (visita programmata vs urgenza, costi indicativi di prima visita, modalità pagamento).

### What the site must avoid

- Foto di cuccioli "tipicissimi" iper-fotografati: tono stock.
- "Noi amiamo gli animali come te": ovvio, non differenzia.
- Prezzi indicati come "da XX€" per attirare: pubblicità sanitaria veterinaria regolamentata.
- Minimizzare l'urgenza ("non preoccuparti, andrà tutto bene"): impossibile da garantire clinicamente.

### Competitive positioning

`clinico-empatico · specie-diversificato · disponibile`

---

## 4 · Terminology dictionary

| Termine (IT) | Definizione | Sinonimi vietati | Tono / nota |
|---|---|---|---|
| `ambulatorio veterinario` | studio base per animali | `clinica` (quando più grande) | core |
| `clinica veterinaria` | struttura grande multi-specializzata | — | core |
| `medico veterinario` | titolo professionale (non "dottore" generico) | `dottore veterinario` (ok) | formale |
| `direttore sanitario` | veterinario responsabile clinica | — | formale |
| `iscrizione FNOVI` | iscrizione ordine veterinari | `iscrizione albo` | formale |
| `pet parent` / `proprietario` | cliente dello studio | `padrone` (desueto/scorretto) | core · pet parent ok in tono moderno |
| `animale d'affezione` | cane · gatto · coniglio domestici | `pet` (anglismo accettato nel marketing) | formale |
| `esotici` | roditori · uccelli · rettili · anfibi | `animali strani` | core |
| `prevenzione` | vaccini · antiparassitari · check-up | — | core |
| `vaccinazione` | somministrazione protocollo vaccinale | — | core |
| `chip di identificazione` | microchip obbligatorio cani | `microchip` (anglismo accettato) | core |
| `passaporto europeo` | documento viaggio animale | — | core |
| `sterilizzazione` | intervento chirurgico | `castrazione` (più specifico) | tecnico |
| `radiografia` | esame diagnostico | — | tecnico |
| `ecografia` | esame diagnostico | — | tecnico |
| `analisi ematologiche` | esami del sangue | `sangue` (ok quotidiano) | tecnico |
| `chirurgia dei tessuti molli` | operazioni addome/pelle | — | tecnico |
| `ortopedia veterinaria` | cura ossa e articolazioni | — | tecnico |
| `dermatologia veterinaria` | cura pelle/pelo/allergie | — | tecnico |
| `oftalmologia veterinaria` | cura occhi animali | — | tecnico |
| `odontostomatologia veterinaria` | cura bocca animale | `dentista degli animali` (generico) | tecnico |
| `comportamentalista` | veterinario esperto in comportamento | `pet-coach` (marketing generico) | tecnico |
| `emergenza 24h` | pronto soccorso veterinario | `urgenza` (quotidiano) | core |
| `ricovero` | degenza post-operatoria | — | core |
| `day-hospital` | ricovero giornaliero | `day-care` | tecnico |
| `check-up geriatrico` | controllo animali anziani | `controllo senior` | tecnico |
| `food sensitivity test` | test intolleranze alimentari | — | tecnico |
| `ecocardiografia` | ecografia cuore | — | tecnico-specialistico |

---

## 5 · Voice & tone

- **Register**: empathetic-clinical. Riconoscere la preoccupazione del proprietario senza drammatizzare. Tono di medico che ha visto mille casi simili.
- **Sentence length**: brevi, dichiarative, rassicuranti dove appropriato (`i controlli periodici sono brevi, di solito 20 minuti`).
- **Pronouns**: `Lei` con il proprietario · nominare l'animale "il suo cane", "la sua gatta", "il suo coniglio" (riconosce la relazione senza antropomorfizzare).
- **Rhetorical devices allowed**: anticipare domanda ("Il primo vaccino quando va fatto?"), dare tempi realistici ("i risultati degli esami sono pronti in 24-48 ore"), chiarire il percorso di cura.
- **Rhetorical devices banned**: "il tuo migliore amico a quattro zampe", "pelosetti", "abbracci a coda scodinzolante", "lui è una persona per te, e anche per noi".

### Voice anchor

*"Il suo animale non parla, ma ha un corpo che reagisce in modi prevedibili. Noi leggiamo i segnali. Quando arriva in ambulatorio, ascoltiamo prima il proprietario, poi osserviamo l'animale, poi procediamo con una visita. Un controllo programmato dura 20-30 minuti. Un'urgenza può durare quanto serve. Non semplifichiamo se la situazione è complicata, ma spieghiamo sempre quello che stiamo vedendo."*

---

## 6 · Copy skeleton by page kind

### Home

- **Hero headline**: 8-12 parole · nominare "ambulatorio veterinario" o "clinica veterinaria" + eventualmente specie (es. "anche per animali esotici").
- **Hero lead**: 2 righe · chi siete (dimensione · specializzazioni · anni di attività).
- **Primary CTA**: "Prenota una visita".
- **Secondary CTA**: "Emergenze" (link a pagina dedicata con numero urgenza) se lo studio offre 24h.
- **3-6 value props**: veterinari iscritti FNOVI · strumenti diagnostici (ecografia · radiografia · CT se presente) · specializzazioni · animali esotici anche · pagamenti rateali · convenzioni assicurazioni animali.
- **Signature section**: "Come si svolge la prima visita" · 4-5 step.

### Il team

- Veterinari con nome · specializzazione · iscrizione FNOVI (numero · data) · lingue parlate.
- Tecnici veterinari / infermieri se presenti.
- Foto singole in ambiente ambulatorio (non pose stock).

### Prestazioni / Servizi

- 6-10 aree: prevenzione · vaccinazioni · chirurgia · ortopedia · dermatologia · oftalmologia · ecografia/radiografia · analisi laboratorio · ricovero · comportamentalista.
- Per ciascuna: definizione · quando serve · durata media · cosa aspettarsi.

### Specie trattate

- Cani · gatti · conigli · piccoli roditori · uccelli · rettili · cavalli (se applicabile).
- Per specie esotica dichiarare livello di specializzazione (cliniche generaliste spesso non trattano esotici, il dichiararlo è feature).

### Emergenze

- Sezione dedicata se lo studio offre 24h/reperibilità.
- Numero telefonico urgenza · orari di reperibilità · cosa fare prima di arrivare (non somministrare cibo · tenere l'animale al caldo · ecc.).

### Prezzi / Trasparenza

- NO listino pubblico (pubblicità sanitaria regolamentata).
- Indicare: "La prima visita è programmata; preventivo scritto per interventi chirurgici o specialistici".
- Modalità pagamento: contanti · carta · bancomat · pagamento rateale (se offerto).

### Contatti

- Indirizzo · mappa · parcheggio · accesso animali difficili (passo carraio · sala separata gatti/cani).
- Orari · chiusura settimanale · reperibilità fine settimana.
- Telefono · email · form prenotazione.

---

## 7 · Search keywords pack

### Core
`veterinario clinica-animali ambulatorio-veterinario animali-domestici cane`

### Aliases
`gatto esotici roditori uccelli rettili emergenza-veterinaria`

### Synonyms cross-locale
`veterinarian (en) · vétérinaire (fr) · veterinario (es)` · accettati se il cluster template serve clientela espatriata.

### Exclude
`miglior-veterinario-città · veterinario-low-cost · veterinario-24h-economico · pet-coach · animal-healer · cura-naturale-animali`

---

## 8 · Imagery pack pointer

Pack target: `imagery/packs/veterinary.md`.

**Direzione imagery**:
- **Soggetti**: ritratto veterinario con cane sulla poltrona (composto · non sorriso stock), mani che visitano un gatto tranquillo, sala d'attesa con un proprietario e un trasportino, primi piani di stetoscopio su pelo, ecografia in corso, cagnolino in day-hospital con copertina.
- **Palette**: bianco + celeste o verde muschio (clinical-friendly + natura), accento caldo (legno chiaro).
- **Composizione**: calma, illuminata, punto di vista basso occasionalmente (all'altezza dell'animale).
- **Evitare**: cuccioli iper-sorridenti stock, "cagnolino con stetoscopio addosso" · gag fotografica, gatti "arrabbiati" posati, veterinario-con-mano-alzata in cima a montagna di libri.

---

## 9 · Audience tags

```
["smb", "studio"]
```

---

## 10 · Price tier rationale

**Tier consigliato**: `standard`.

**Motivazione**: ambulatori di quartiere sono piccoli business. Deviazione verso `premium` per cliniche veterinarie multi-specializzate con CT/MRI/camera iperbarica o eccellenze in un'area specifica (es. neurologia veterinaria).

---

## 11 · Feature flag expectations

| Flag | Expected | Rationale |
|---|---|---|
| `has_shop` | `False` | Vendita mangimi/farmaci online è regolamentata, fuori scope MVP |
| `has_booking` | `True` | Prenotazione visita primaria |
| `has_portfolio` | `False` | — |
| `has_blog` | `False` | Ingestibile per staff piccolo |
| `has_video` | `False` | Solo video tour ambulatorio se valorizzante |
| `has_rtl` | `True` | D-098 |
| `is_multi_page` | `True` | Home + team + prestazioni + specie + emergenze + contatti |

---

## 12 · Example brand names

- **Petro — Ambulatorio Veterinario** (pilot template)
- **Zampa Lieve — Clinica Veterinaria**
- **Gli Amici — Ambulatorio di Quartiere**

---

## 13 · Anti-patterns

- ❌ "Trattiamo i tuoi pelosetti con amore": infantilizza il servizio, che è clinico.
- ❌ Foto di cagnolino vestito con maglietta: banalizza l'esperienza.
- ❌ "Siamo i veterinari dei tuoi figli a quattro zampe": retorica familiare imposta.
- ❌ Stock photo veterinario che regge un cucciolo in alto a mo' di trofeo.
- ❌ "Esperti in tutte le specie" — incoerente se lo studio non tratta rettili o cavalli.
- ❌ "Visita gratuita ai nuovi pazienti": pubblicità sanitaria regolamentata · evitare.
- ❌ Confondere veterinario e "behaviorist" non-certificato: se lo studio offre comportamentalista, è veterinario con ECVAA (specialist) o iscrizione specialistica.
- ❌ "Amo gli animali dalla nascita" come bio del veterinario: cliché.
- ❌ Mettere in evidenza esami a basso costo su home: medicalizza con logica e-commerce.

---

## 14 · D-054 differentiation notes

### Sibling templates

Nessuno pre-pilot.

### Adjacency notes

**Adiacente a**:
- `specialist` (stesso archetipo · medicina specialistica con visita di valutazione).
- `dental` (stesso archetipo, target anch'esso delicato ma umano).

**Distinto da**:
- `specialist` (Cardio/Derm) — medicina umana. Target umano adulto. Paziente parla.
- `family-pediatric` — medicina umana della famiglia. Target genitore + bambino umano.
- `dental` — medicina umana odontoiatrica. Target paziente che parla (anche bambini).
- `multi-clinic` — medicina umana con più discipline. Veterinario ha CLINICA veterinaria solo per animali.
- `wellness-holistic` — medicina umana integrative. Veterinario è allopatico clinico.

### Differentiation matrix (sibling futuri)

1. Specializzazione (generalista cane-gatto vs esotici vs cavalli vs alta-specialità tipo neurologia)
2. Dimensione (ambulatorio 1 vet vs clinica 5+ vet con day-hospital)
3. Presenza 24h/reperibilità notturna
4. Palette (bianco-celeste standard vs verde-muschio natura vs legno-grigio moderno)
5. Tone hero (diretto-clinico vs rassicurante-empatico)
6. Sezione "esotici" dedicata vs accenno
7. Presenza comportamentalista
8. Fascia prezzo/target (quartiere vs city-hub premium)
9. Chirurgia avanzata (sì/no) vs rimando a centro specialistico
10. Sezione "trasportare l'animale" (tips educativi vs assente)

---

## 15 · Changelog

| Data | Autore | Modifica |
|---|---|---|
| 2026-04-20 | Phase Lead | Initial blueprint · X.3 Commit 2 |
