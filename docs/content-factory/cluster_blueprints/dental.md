# Cluster Blueprint · `dental`

**Status**: Wave 2 pilot cluster. Pilot template target: `denti-co-studio`.

---

## 1 · Identity

- **Cluster slug**: `dental`
- **Cluster human name (IT)**: Studio dentistico
- **Macro-category**: `medical`
- **Archetypes that serve this cluster**: `specialist` (shared con Cardio + Derm pre-esistenti)
- **Cluster enrolled since**: X.2 Commit 2

### Identity summary

Studio dentistico moderno, studio di odontoiatria conservativa, centro di implantologia e ortodonzia, studi familiari pluri-odontoiatra. Il paziente arriva preoccupato (dolore · estetica · budget · paura dello studio). Il sito deve abbassare la soglia d'ansia con chiarezza, mostrare la moderna strumentazione senza fare pubblicità, e facilitare la prenotazione della prima visita. Distinto dal generico `multi-clinic` (clinica multispecialistica) perché l'odontoiatria ha lessico, apparato e ansia specifici.

---

## 2 · Audience

- **Primary audience slugs**: `smb · studio`
- **End-customer**: paziente 25-75 · genitore che cerca pediatria odontoiatrica per un figlio · giovane adulto con problema estetico · anziano con protesi da rifare.
- **Decision maker**: odontoiatra titolare (1-3 soci) o responsabile di uno studio con 4-10 poltrone.

---

## 3 · Positioning

### What the site must achieve (top 3)

1. Ridurre l'ansia del primo contatto: linguaggio chiaro, "prima visita di valutazione gratuita o 30€".
2. Dichiarare le specializzazioni presenti (implantologia · ortodonzia invisibile · conservativa · endodonzia · pedodonzia · chirurgia maxillofacciale).
3. Comunicare trasparenza di costi e piani di trattamento (non listino, ma "ti facciamo preventivo scritto").

### What the site must avoid

- Immagine di denti iper-bianchi di modella: standard estetico irrealistico e stressante.
- "Sorriso perfetto garantito": affermazione clinica vietata · impossibile da garantire.
- Trattamenti a prezzi "da XXX€" in evidenza: pubblicità sanitaria regolamentata.
- Testimonial con volto completo senza consenso: violazione GDPR + codice deontologico.

### Competitive positioning

`clinico-rassicurante · tecnologicamente-aggiornato · trasparente`

---

## 4 · Terminology dictionary

| Termine (IT) | Definizione | Sinonimi vietati | Tono / nota |
|---|---|---|---|
| `odontoiatria` | disciplina medica dentale | `dentistica` (errato · non esiste) | formale |
| `odontoiatra` | medico specializzato | `dentista` (quotidiano · entrambi usati) | entrambi accettati, `odontoiatra` più formale |
| `igiene dentale` | profilassi · rimozione tartaro | `pulizia` (quotidiano) | core |
| `implantologia` | inserimento di impianti dentali | — | tecnico |
| `impianto` | vite titanio sostituto radice | `vite` | tecnico |
| `protesi fissa` | corona · ponte | — | tecnico |
| `protesi mobile` | dentiera parziale/totale | `dentiera` (quotidiano accettato) | entrambi ok |
| `ortodonzia` | correzione malocclusioni | — | tecnico |
| `ortodonzia invisibile` | allineatori trasparenti tipo Invisalign | `mascherine` (generico) | tecnico-moderno |
| `faccette` | veneer estetici dentali | `veneer` | tecnico |
| `sbiancamento` | trattamento estetico | `whitening` | tecnico · quotidiano ok |
| `conservativa` | cura della carie senza rimuovere dente | `otturazione` (un sottoinsieme) | tecnico |
| `endodonzia` | devitalizzazione · cura canale radicolare | `devitalizzazione` (ok in quotidiano) | tecnico |
| `parodontologia` | cura gengive e tessuti di sostegno | `parodonzia` (varianti entrambe ok) | tecnico |
| `pedodonzia` | odontoiatria pediatrica | `odontoiatria-per-bambini` | tecnico-caldo |
| `chirurgia maxillofacciale` | interventi chirurgici complessi | — | tecnico |
| `estrazione` | rimozione dente | — | core |
| `radiografia panoramica · OPT` | esame diagnostico completo | — | tecnico |
| `cone beam · CBCT` | TAC 3D dentale | — | tecnico-moderno |
| `piano di trattamento` | sequenza concordata di cure | `piano di cura` (ok) | formale |
| `preventivo scritto` | quantificazione economica firmata | `preventivo` (ok) | formale · trasparenza |
| `consenso informato` | documento legale pre-intervento | — | formale |
| `anestesia locale` | blocco del dolore zona | — | tecnico |
| `seduta di igiene` | appuntamento periodico | `seduta dall'igienista` | core |
| `richiamo periodico` | controllo cadenzato 6-12 mesi | — | core |
| `emergenza odontoiatrica` | urgenza dolore acuto | — | core |
| `studio accreditato SSN` | se applicabile | — | informativo |

---

## 5 · Voice & tone

- **Register**: clinical-friendly. Professionale ma umano. Il registro è quello di un medico che spiega una procedura a un paziente ansioso, senza infantilizzare.
- **Sentence length**: brevi, dichiarative. Domande del paziente anticipate ("Fa male?", "Quanto costa?", "Quanto dura?").
- **Pronouns**: `Lei` formale con il paziente. Eccezione: sezione pediatria può usare `tu` ai bambini ma parlare al genitore con `Lei`.
- **Rhetorical devices allowed**: anticipare la domanda del paziente, chiarire tempi (`una seduta di implantologia dura circa 90 minuti`), descrivere sensazioni attese (`il primo giorno può esserci gonfiore`).
- **Rhetorical devices banned**: "un sorriso smagliante", "regala un sorriso a te stesso", "scopri il segreto del sorriso perfetto", "offerta ortodonzia solo questo mese".

### Voice anchor

*"Lei arriva in studio spesso con un problema preciso: un dolore, un dente rotto, un preventivo di un altro studio da capire. Il nostro lavoro comincia con l'ascolto, continua con una visita di valutazione che dura 30-40 minuti, e si chiude con un piano di trattamento scritto. Non facciamo pressione sulla decisione. Se il trattamento può aspettare un mese, lo diciamo. Se è urgente, anche."*

---

## 6 · Copy skeleton by page kind

### Home

- **Hero headline**: 8-12 parole · nominare l'attività ("studio dentistico" o una specializzazione chiave).
- **Hero lead**: 2 righe · posizionamento (famiglia · implantologia · estetica) + tono rassicurante.
- **Primary CTA**: "Prenota la prima visita" (o "la visita di valutazione").
- **Secondary CTA**: "Le nostre specializzazioni" o "Dove siamo".
- **3-6 value props**: prima visita strutturata · preventivo scritto sempre · specialità (pediatria · ortodonzia invisibile · implantologia) · tecnologia CBCT · anestesia computerizzata (se presente) · accreditato SSN (se applicabile).
- **Signature section**: "Come si svolge la prima visita" in 4-5 step.

### Il team

- Odontoiatra titolare + collaboratori.
- Per ogni medico: nome · specializzazione · iscrizione albo (OMCeO · nr. + data) · anni esperienza · lingua/e parlata/e.
- Igienista/e presenti.

### Specialità / Trattamenti

- 6-10 trattamenti. Per ciascuno: cos'è · quando serve · come si svolge · quante sedute · tempi di recupero.
- NO PREZZI in pagina (pubblicità sanitaria regolamentata). Usare "richiedi preventivo".

### Tecnologie

- 3-6 apparecchi chiave (radiografia panoramica · CBCT · laser · scanner intraorale · poltrona con anestesia computerizzata).
- Per ciascuno: a cosa serve · perché migliora la cura.

### Pazienti / FAQ

- 10-15 FAQ reali raccolte dall'esperienza dello studio (non generiche).
- Esempi: "Dolori dopo implantologia?", "Posso allattare durante il trattamento?", "Quanto dura un allineatore?", "Accettate adulti per ortodonzia?"

### Contatti / Sede

- Indirizzo + Google Maps + parcheggio.
- Orari.
- Telefono + email.
- Form prenotazione prima visita: nome · telefono · motivo visita (breve) · preferenza orario.
- Emergenze odontoiatriche: numero + orari.

---

## 7 · Search keywords pack

### Core
`dentista odontoiatra igiene-dentale implantologia ortodonzia`

### Aliases
`studio-dentistico impianto-dentale faccette allineatori devitalizzazione sbiancamento`

### Synonyms cross-locale
`dentist (en) · dentiste (fr)` solo se audience internazionale.

### Exclude
`sorriso-perfetto · denti-bianchi-in-una-seduta · offerta-impianto · dentista-low-cost · ortodonzia-veloce · dentista-indolore`

---

## 8 · Imagery pack pointer

Pack target: `imagery/packs/dental.md`.

**Direzione imagery**:
- **Soggetti**: poltrona odontoiatrica moderna pulita, dettaglio di strumenti sterilizzati, ritratto odontoiatra con mascherina abbassata (non frontale sorridente), famiglia in sala d'attesa con bambino tranquillo, interno studio con design contemporaneo sobrio.
- **Palette**: bianco + celeste chiaro + legno chiaro (coerente con D-054 minimal-light). Evitare verde-medicale istituzionale, bianco-chirurgico estremo.
- **Composizione**: chiara, luminosa, spazi ampi. Mostrare ordine e pulizia.
- **Evitare**: close-up denti iper-bianchi alla stock, sorrisi finti con apparecchio, mani mediche guantate che mostrano pollice in su, siringhe in primo piano, denti al microscopio.

---

## 9 · Audience tags

```
["smb", "studio"]
```

---

## 10 · Price tier rationale

**Tier consigliato**: `standard`.

**Motivazione**: uno studio dentistico di quartiere è piccolo business medico, tier standard è coerente. Deviazione verso `premium` per studi di implantologia specializzati o cliniche multi-poltrona con tecnologie avanzate (CBCT · laser CO2 · scanner intraorale di ultima generazione).

---

## 11 · Feature flag expectations

| Flag | Expected | Rationale |
|---|---|---|
| `has_shop` | `False` | — |
| `has_booking` | `True` | Prenotazione visita è la CTA primaria |
| `has_portfolio` | `False` | Casi prima-dopo sono delicati (GDPR · consenso) |
| `has_blog` | `False` | Ingestibile per un piccolo studio |
| `has_video` | `False` | Opzionale solo con tour studio |
| `has_rtl` | `True` | D-098 |
| `is_multi_page` | `True` | Home + team + specialità + tecnologie + FAQ + contatti |

---

## 12 · Example brand names

- **Denti+Co — Studio Dentistico** (pilot template)
- **Studio Morelli Odontoiatria**
- **Centro Dentale Navigli**

---

## 13 · Anti-patterns

- ❌ "Sorriso da attore" come slogan: standard irrealistico.
- ❌ Foto prima/dopo di sbiancamento senza chiaro consenso del paziente.
- ❌ Offerta "implantologia da 599€": pubblicità sanitaria regolamentata, evitare.
- ❌ "Zero dolore garantito": affermazione clinica impossibile.
- ❌ Foto di una mano con siringa in primo piano: aumenta ansia.
- ❌ Stock photo di bambino iper-sorridente con dentista: posa falsa.
- ❌ "Dentista per adulti e bambini" come categoria generica senza sezione pediatria dedicata.
- ❌ "Tradizione familiare da tre generazioni" senza nome/data del fondatore.
- ❌ Spammare parole come "estetica · sorriso · bellezza": medicalizza la vanità.
- ❌ Landing con countdown "-20% sbiancamento · ultime 24 ore": tono da e-commerce, non da studio medico.

---

## 14 · D-054 differentiation notes

### Sibling templates

Nessuno pre-pilot.

### Adjacency notes

**Adiacente a**:
- `specialist` (stesso archetipo · Cardio + Derm).
- `multi-clinic` (stesso macro · tono clinical-friendly).
- `family-pediatric` (pazienti anche bambini, overlap parziale).

**Distinto da**:
- `specialist` (Cardio/Derm) — `specialist` è medicina specialistica non-chirurgica di ambulatorio. `dental` è odontoiatria con poltrona + strumenti dedicati + paura paziente specifica.
- `multi-clinic` — `multi-clinic` è poliambulatorio con 10 discipline diverse. `dental` è mono-disciplina approfondita.
- `family-pediatric` — `family-pediatric` è pediatra generale + ginecologa di famiglia. `dental` può avere pediatria odontoiatrica ma come sottodisciplina, non come anima.
- `veterinary` — mondo diverso (animali).
- `wellness-holistic` — ideologia diversa · odontoiatria è allopatica clinica, wellness-holistic è integrative.

### Differentiation matrix (sibling futuri)

1. Specializzazione dominante (implantologia vs ortodonzia invisibile vs conservativa vs pediatria)
2. Presenza sezione pediatria dedicata (sì vs no)
3. Tecnologie chiave (CBCT + laser + scanner vs strumentazione base)
4. Dimensione (solo titolare vs studio con 5 poltrone)
5. Palette (bianco-celeste vs grigio-legno vs beige-caldo)
6. Accreditamento SSN (sì/no)
7. Lingue parlate (IT vs IT + EN)
8. Zona geo-target (quartiere vs città-hub)
9. Focus estetico vs clinico-funzionale
10. Fascia età pazienti target (famiglia vs adulti vs anziani · anche protesica)

---

## 15 · Changelog

| Data | Autore | Modifica |
|---|---|---|
| 2026-04-20 | Phase Lead | Initial blueprint · X.3 Commit 2 |
