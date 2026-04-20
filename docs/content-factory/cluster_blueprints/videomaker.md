# Cluster Blueprint · `videomaker`

**Status**: Wave 2 pilot cluster. Pilot template target: `fotogramma-films`.

---

## 1 · Identity

- **Cluster slug**: `videomaker`
- **Cluster human name (IT)**: Videomaker & motion
- **Macro-category**: `portfolio`
- **Archetypes that serve this cluster**: `cinematic-photographer`
- **Cluster enrolled since**: X.2 Commit 2

### Identity summary

Videomaker di cortometraggi editoriali, director freelance, motion designer, filmmaker pubblicitari, documentaristi, DOP (direttori della fotografia), registi di videoclip e film istituzionali. Il prodotto è un portfolio di sequenze, non di singoli frame. Il sito deve essere organizzato per essere "letto" in orizzontale, con embedded reel e case study. Distinto da `photographer` perché il frame non è l'unità di misura — lo è la sequenza.

---

## 2 · Audience

- **Primary audience slugs**: `freelance · studio`
- **End-customer**: agenzie pubblicitarie · case di produzione · brand manager · direttori artistici · editori/magazine con sezione video · institutional/corporate cliente diretto.
- **Decision maker**: il regista/videomaker stesso (solo-practitioner) oppure il producer di una piccola casa di produzione.

---

## 3 · Positioning

### What the site must achieve (top 3)

1. Aprire con un reel: primo elemento sopra la fold è il reel o una sequenza chiave di 15-30 secondi.
2. Organizzare i lavori per tipologia (commercial · docu · videoclip · corporate · series) con filtri.
3. Facilitare il contatto dei decision maker (producer/direttore artistico) con una call-to-action da case di produzione, non da e-commerce.

### What the site must avoid

- "Raccontiamo la tua storia con passione": banale, generico, non differenzia.
- Hero statico con foto del regista: il videomaker è il suo lavoro, non il suo volto.
- Lista cliente-logo senza contesto: dice che hai lavorato, non cosa hai fatto.
- Copy "da artista" oscuro ("un'esplorazione onirica del tempo"): il cliente non compra poesia, compra capability tecnica.

### Competitive positioning

`reel-first · case-study-driven · director-voiced`

---

## 4 · Terminology dictionary

| Termine (IT) | Definizione | Sinonimi vietati | Tono / nota |
|---|---|---|---|
| `reel` | bobina dimostrativa · compilation | `video-presentazione` | core |
| `showreel` | equivalente di reel | — | ok |
| `corto` | cortometraggio indipendente | `short-film` (ok) | core |
| `commercial` | pubblicità video | `pubblicità` (ok) | ok |
| `TVC` | commercial tradizionale · broadcast | — | tecnico-settoriale |
| `spot` | sinonimo di commercial | — | core |
| `branded content` | contenuto pagato editoriale | `contenuto sponsorizzato` | settoriale |
| `videoclip` | video musicale | `music-video` (ok) | core |
| `docu-fiction` | ibrido documentario/fiction | — | tecnico |
| `documentario` | film non-fiction | `doc` (ok informale) | core |
| `corporate video` | video aziendale istituzionale | — | ok |
| `direttore della fotografia` · `DOP` | responsabile immagine | `cameraman` (riduttivo) | tecnico |
| `regista` | responsabile creativo/narrativo | `director` (ok) | core |
| `producer` | responsabile produzione | `produttore` (ok) | core |
| `pre-produzione · produzione · post-produzione` | le 3 fasi | — | core |
| `color grading` | correzione colore avanzata | `color correction` (diverso) | tecnico |
| `color correction` | correzione colore base | — | tecnico |
| `editing · montaggio` | assemblaggio sequenze | — | core |
| `script supervisor` · `sceneggiatore` | chi scrive/segue script | — | tecnico |
| `storyboard` | scenografia disegnata scena per scena | — | core |
| `scaletta` | ordine delle riprese | `shooting-list` | tecnico |
| `sound design` | progettazione sonora | — | tecnico |
| `location scouting` | ricerca locations | — | tecnico |
| `sede di produzione` | casa di produzione | — | core |
| `cliente commerciale` | brand/agenzia committente | — | B2B |
| `agenzia di pubblicità` | committente indiretto | — | B2B |
| `festival circuit` | ciclo di festival per corti | — | settoriale |
| `aspect ratio` | rapporto video | `proporzione` | tecnico |
| `anamorphic` | lenti cinema wide | — | tecnico |
| `frame-rate` | fotogrammi al secondo | `fps` (ok) | tecnico |
| `brief` | documento cliente iniziale | `briefing` (ok) | B2B |

---

## 5 · Voice & tone

- **Register**: cinematic-editorial. Asciutto, professionale, da director's statement. Mai autoelogio.
- **Sentence length**: brevi e definitive. Verbi d'azione.
- **Pronouns**: `io` o `noi` (se casa di produzione) · il cliente è "il brand", "il regista ospite", "la committenza".
- **Rhetorical devices allowed**: annotazioni tecniche brevi ("girato in 2.35:1, anamorfico"), titoli di progetto con nome cliente e anno, attenzione alla credit list (non omettere i produttori).
- **Rhetorical devices banned**: "passione per il video", "raccontare la tua storia", "trasformare idee in immagini", "catturare l'essenza del brand".

### Voice anchor

*"Lavoro con marchi che hanno qualcosa di preciso da dire e poco tempo per dirlo. Una pre-produzione fatta bene è metà del film. In set gestisco da director · la casa di produzione mette il producer · il DOP è uno dei tre con cui lavoro da anni. Non vendo 'creatività senza limiti'. Vendo sequenze che funzionano al terzo secondo. Il reel in home è il mio CV visivo: se parla, passiamo ai progetti. Se non parla, non ha senso chiamarsi."*

---

## 6 · Copy skeleton by page kind

### Home

- **Hero**: reel embedded (Vimeo/YouTube privato o hosted). 15-30 sec di montaggio. Autoplay muto · click per audio.
- **Headline sotto reel**: 5-8 parole · statement asciutto ("Film per brand con qualcosa da dire").
- **Primary CTA**: "Contatta per un brief" o "Richiedi il reel completo".
- **Secondary CTA**: "I lavori".
- **3-4 lines statement** sotto reel: disciplina (director · DOP · motion · docu) · area (commercial · videoclip · documentario) · scala di lavoro (indy / casa media / spot broadcast).

### Lavori / Works

- Griglia filtrabile per tipo (commercial · docu · videoclip · corporate · institutional).
- Per ogni lavoro: titolo · cliente · anno · ruolo (director · DOP · editor) · link embedded video.
- Hover/click apre una scheda con: brief · approccio · credit list · risultato.

### Progetto singolo (detail page)

- Reel in alto.
- Metadata: cliente · anno · ruolo · durata · aspect-ratio · location.
- Bio del progetto (1-2 paragrafi asciutti).
- Credit list completa (producer · DOP · editor · color · sound · music).
- Premi/festival (se applicabile).
- 2-3 still frame editoriali in orizzontale.

### Chi / Director

- Ritratto di contesto (set, non studio) + bio 2 paragrafi.
- Background (formazione · case di produzione · clienti ricorrenti).
- Riconoscimenti / festival (senza enfasi).
- Lingue di lavoro.
- Attrezzatura principale (se lo studio ne fa un asset: "usiamo cineprese Arri Alexa...", mirato al pubblico producer).

### Servizi / Offerta

- 3-5 aree di intervento. Per ciascuna: tipologia progetto · range durata · metodo di lavoro · tempistiche medie.
- Esempi: "Commercial TVC 30" · "Branded content 2-3 minuti" · "Videoclip 3-4 minuti" · "Corporate institutional 1-2 minuti" · "Documentario short 10-15 minuti".

### Contatti

- Form: nome · azienda/agenzia · ruolo (director/producer/brand) · brief breve · budget range · deadline · link/reference.
- Indicazione chiara: "Guardiamo ogni brief serio, rispondiamo entro 48h".
- Indirizzo sede + sede secondaria se presente.

---

## 7 · Search keywords pack

### Core
`videomaker motion-design filmmaker regia cinematografia`

### Aliases
`director spot-commercial videoclip documentario corporate-video reel`

### Synonyms cross-locale
`director (en) · réalisateur (fr)` accettati come termine settoriale globale.

### Exclude
`videomaker-economico · miglior-videomaker · videomaker-matrimoni (altro cluster) · low-budget-commercial · fai-da-te-video`

---

## 8 · Imagery pack pointer

Pack target: `imagery/packs/videomaker.md`.

**Direzione imagery**:
- **Soggetti**: still frame di riprese reali (preferiti ai BTS), dettagli di camera Arri/RED, regista sul set con cuffie e monitor, set notturno con luci, frame editoriali di film con aspect-ratio cinema.
- **Palette**: cinematic-noir coerente con visual style `cinematic-fullbleed` — tonalità scure, alte luci controllate, contrasti forti.
- **Composizione**: fullbleed editorial, letterbox a volte, dettagli ravvicinati.
- **Evitare**: foto con DSLR in primo piano, "giovani-creativi-con-hoodie-davanti-computer", set stock con luci giocattolo, grafiche di "video come qualità superiore".

---

## 9 · Audience tags

```
["freelance", "studio"]
```

---

## 10 · Price tier rationale

**Tier consigliato**: `premium`.

**Motivazione**: target professionale B2B (agenzie · brand · case di produzione), target customer è habituato a premium. Il cluster richiede reel embed di qualità e portfolio denso → presentazione premium coerente. Deviazione verso `standard` solo per videomaker debuttanti con portfolio ridotto.

---

## 11 · Feature flag expectations

| Flag | Expected | Rationale |
|---|---|---|
| `has_shop` | `False` | — |
| `has_booking` | `False` | Contatto avviene via brief scritto, non via prenotazione slot |
| `has_portfolio` | `True` | Portfolio è core · distintivo cluster |
| `has_blog` | `False` | Opzionale (director's journal se lo ha) |
| `has_video` | `True` | Unico cluster che ha video come asset primario |
| `has_rtl` | `True` | D-098 |
| `is_multi_page` | `True` | Home + lavori + progetto-detail + director + servizi + contatti |

---

## 12 · Example brand names

- **Fotogramma — Films** (pilot template)
- **Linea — Studio di Regia**
- **Regìa Indipendente — Independent Director**

---

## 13 · Anti-patterns

- ❌ "Trasformiamo le tue idee in film": generico.
- ❌ Home senza reel: il cluster esiste per mostrare il reel.
- ❌ Solo logo clienti grandi (Apple · Coca-Cola · Nike): senza case study, sembra vantato.
- ❌ "Registi appassionati di storytelling": cliché.
- ❌ Portfolio in lista testuale senza video embedded: controproducente.
- ❌ Pagina contatti senza campo "budget range": fa perdere tempo su brief irrealizzabili.
- ❌ Mescolare videomaker professionista e "wedding videographer": cluster diversi.
- ❌ "Specialista in tutti i formati da 15 secondi a 2 ore": perde focus.
- ❌ Reel in home > 60 secondi: perde attenzione del buyer.
- ❌ Credit list omessa: segnala ego-only portfolio, penalizzato in industria.

---

## 14 · D-054 differentiation notes

### Sibling templates

Nessuno pre-pilot.

### Adjacency notes

**Adiacente a**:
- `photographer` (Pixel) — stesso archetipo · stesso macro portfolio.
- `designer-editorial` (Chiara) — stesso macro · diversa disciplina visiva.

**Distinto da**:
- `photographer` — fotografo lavora in fermo-immagine, il frame è unità di misura. Videomaker lavora in sequenza, il reel è unità. Portfolio differente (statico vs embedded video).
- `designer-editorial` — designer è grafico/editoriale/brand; videomaker è cinematico/registico.
- `illustrator` — illustratore lavora in disegno/vettoriale; videomaker in ripresa/montaggio.
- `creative` (agency-creative-studio) — creative agency ha team multidisciplinare; videomaker è specializzato mono-disciplina.

### Differentiation matrix (sibling futuri)

1. Specializzazione (commercial vs documentario vs videoclip vs corporate vs branded content vs DOP)
2. Ruolo dominante (director vs DOP vs editor vs producer)
3. Scala (solo-freelance vs piccola casa di produzione vs studio medio)
4. Target cliente (agenzie pubblicitarie vs brand diretti vs editori vs istituzionali)
5. Reel style (fullbleed cinematic vs docu-editoriale vs motion-design grafico)
6. Aspect ratio dominante (2.35:1 cinema · 16:9 broadcast · 1:1 social)
7. Palette (dark-noir vs warm-editorial vs bianco-minimal motion-design)
8. Credit-list (sempre completo vs sintetico)
9. Presenza sezione awards/festival
10. Lingue di lavoro (IT vs IT + EN · importante per spot broadcast internazionali)

---

## 15 · Changelog

| Data | Autore | Modifica |
|---|---|---|
| 2026-04-20 | Phase Lead | Initial blueprint · X.3 Commit 2 |
