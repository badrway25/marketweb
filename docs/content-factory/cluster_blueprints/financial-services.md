# Cluster Blueprint · `financial-services`

**Status**: Wave 2 pilot cluster. Pilot template target: `fiscus-commercialista` (see `pilot_batch/x4_wave2_first_10.md`).

---

## 1 · Identity

- **Cluster slug**: `financial-services`
- **Cluster human name (IT)**: Servizi finanziari
- **Macro-category**: `business`
- **Archetypes that serve this cluster**: `corporate-suite` (only)
- **Cluster enrolled since**: X.2 Commit 2

### Identity summary

Commercialisti, studi tributari, revisori contabili, consulenti del lavoro, wealth manager indipendenti: professionisti il cui prodotto primario è la riduzione del rischio fiscale e la precisione delle scadenze. Il sito non vende competenza generica — la dichiara con linguaggio da addetti ai lavori (normativa, codici, scadenze), e la inquadra in un impegno di relazione continuativa con il cliente. Non è consulenza strategica (quello è `professional-services`), non è coaching (quello è `coaching`).

---

## 2 · Audience

- **Primary audience slugs**: `smb · freelance · studio`
- **End-customer of the template's customer**: piccoli imprenditori, professionisti con partita IVA, amministratori di PMI, sostituti d'imposta, clienti privati con patrimonio medio-alto (wealth management).
- **Decision maker**: owner dello studio (commercialista iscritto all'albo) o socio di uno studio associato.

---

## 3 · Positioning

### What the site must achieve (top 3)

1. Dichiarare competenza tecnica verificabile (specializzazioni, qualifiche, iscrizioni albo).
2. Presentare il percorso di onboarding del cliente (cosa succede quando prenoti un primo appuntamento).
3. Comunicare continuità — scadenze anno-su-anno, non transazioni una tantum.

### What the site must avoid

- "Risparmio fiscale garantito" e varianti: reato professionale, oltre che etico.
- "Ti seguiamo come una famiglia" (promessa relazionale generica e inflazionata).
- Claim sulla vittoria in contenziosi tributari senza citazione verificabile.
- Grafiche "up-and-to-the-right" generiche: lo studio fiscale non è una SaaS growth platform.

### Competitive positioning (2-3 adjectives)

`preciso · continuativo · istituzionale`

---

## 4 · Terminology dictionary

| Termine (IT) | Definizione / uso | Sinonimi vietati | Tono / nota locale |
|---|---|---|---|
| `dichiarazione dei redditi` | atto fiscale annuale obbligatorio | `tax return` (anglismo inutile) | neutro-tecnico |
| `regime forfettario` | regime agevolato per partita IVA | `flat tax` (impreciso) | tecnico |
| `F24` | modello di pagamento unificato | — | tecnico-quotidiano |
| `studio tributario` | studio specializzato in fiscalità | `fiscal studio` (anglismo) | preferibile a "studio di commercialisti" quando la specializzazione è tributaria |
| `revisione contabile` | verifica indipendente dei bilanci | `audit` (in contesti non-big-4) | formale |
| `bilancio d'esercizio` | documento contabile annuale | — | tecnico |
| `consulente del lavoro` | albo diverso dal commercialista | `HR consultant` (vietato se parliamo di CdL iscritti all'albo) | chiarire ruolo |
| `Ires · Irap · Iva` | imposte principali | — | tecnico |
| `accertamento` | procedura di verifica da Agenzia Entrate | `audit` | formale-difensivo |
| `ravvedimento operoso` | sanatoria volontaria errori fiscali | — | tecnico |
| `contenzioso tributario` | disputa con l'amministrazione | `tax litigation` | formale |
| `Commissione Tributaria` | organo giurisdizionale | — | formale |
| `CAF` | centro assistenza fiscale | — | quotidiano |
| `partita IVA` | identificativo fiscale | `VAT number` (anglismo inutile in IT) | quotidiano |
| `sostituto d'imposta` | datore di lavoro/committente con obbligo ritenuta | — | tecnico |
| `certificazione unica` / `CU` | documento annuale reddito lavoratore | — | tecnico-quotidiano |
| `pianificazione fiscale` | strategia fiscale pluriennale | `tax planning` (accettabile in wealth management) | formale |
| `wealth management` | gestione patrimoniale | `gestione patrimoni` (ok) | formale · registro alto |
| `successione` | trasferimento ereditario | `estate planning` (solo in wealth context) | formale |
| `quadro RW` | sezione dichiarazione per redditi esteri | — | tecnico |
| `studio associato` | forma societaria tra professionisti | `firm` | formale |
| `parcella` | onorario professionale | `invoice` (per altri contesti) | formale-economico |
| `consulenza ricorrente` | rapporto continuativo | `subscription` (anglismo impreciso) | formale |
| `delega Entratel` | autorizzazione trasmissione telematica | — | tecnico-addetto |
| `albo dei commercialisti` | iscrizione ODCEC obbligatoria | — | formale |

---

## 5 · Voice & tone

- **Register**: formal-precise. Non caldo-caloroso ma nemmeno freddo-corporate. Il registro è quello di chi spiega una normativa con pazienza, senza semplificare eccessivamente.
- **Sentence length preference**: medie, costruite con subordinate rispettose della legge italiana. Non eleganti periodi ciceroniani — frasi che reggono una virgola di troppo perché la norma lo richiede.
- **Pronouns**: `Lei` formale nel primo piano-CTA, `noi/voi` quando si parla dello studio e del cliente.
- **Rhetorical devices allowed**: citazione diretta di articoli di legge (TUIR, D.P.R. 600/1973), date di scadenza, dati quantitativi concreti (fatturati soglia, aliquote).
- **Rhetorical devices banned**: metafore sportive (no "quarterback del tuo bilancio"), urgenze finte ("ultime 48 ore per"), claim di risparmio percentuale ("-40% di tasse!").

### Voice anchor

*"Ci occupiamo dell'adempimento corretto, non della trovata. Il lavoro principale avviene tra marzo e dicembre, e consiste in controllare due volte, tenere traccia, firmare quando serve. Nelle settimane che precedono una scadenza ci sentiamo più spesso del solito. Fuori da quelle settimane, rispondiamo entro la giornata. Ogni anno il lavoro è lo stesso, e ogni anno cambia: per questo un commercialista non è un costo da minimizzare, è un presidio da scegliere."*

---

## 6 · Copy skeleton by page kind

### Home

- **Hero headline (IT · 8-12 parole)**: deve contenere un riferimento concreto al servizio (parola chiave: "fiscale", "tributario", "bilancio") — non uno slogan astratto.
- **Hero lead**: 2 righe · una frase dice cosa fai, una frase dice chi serve.
- **Primary CTA**: "Primo appuntamento gratuito" o "Richiedi un preventivo" (quando onorario forfait).
- **Secondary CTA**: "Scarica la guida scadenze" (lead-magnet solido).
- **3-6 value props**: scadenze gestite con anticipo · software aggiornato · risposta entro 24h · specializzazioni certificate · parcella trasparente.
- **Signature section**: "Calendario delle scadenze" con 6-8 date chiave del prossimo trimestre.

### Chi siamo / Studio

- Storia dello studio (quando è stato fondato, soci attuali).
- Bio dei professionisti — richiede campi: `nome`, `ruolo`, `iscrizione-albo` (numero + ordine), `anni-esperienza`, `specializzazioni-certificate`.
- Certificazioni/qualifiche (CTU, revisore legale, consulente del lavoro).

### Servizi / Aree di competenza

- 4-8 aree: dichiarazione redditi, bilancio, consulenza societaria, contenzioso, wealth management, consulenza del lavoro, revisione, IVA.
- Per ciascuna: 1 titolo · 2-3 righe di descrizione · 3-5 bullet di contenuto reale (non "professionalità e attenzione al cliente").

### Scadenze / Calendario fiscale

- Lista 10-15 scadenze chiave dell'anno con date precise + breve descrizione.
- Sezione newsletter opt-in per "promemoria scadenze" (NO raccolta dato se il template non ha form booking).

### Contatti

- Form richiesta appuntamento: nome · partita-IVA/CF · area di interesse · fascia oraria preferita · messaggio.
- Orari ufficio (esplicitare che cambiano in prossimità scadenze).
- Indirizzi sedi (studio ha spesso 2 sedi nello stesso capoluogo).

---

## 7 · Search keywords pack

### Core (3-6)
`commercialista fiscale finanza tasse contabilità`

### Aliases (0-8)
`dichiarazione-redditi wealth-management revisore studio-tributario partita-iva`

### Synonyms cross-locale
`tax-advisor (en) · expert-comptable (fr) · asesor-fiscal (es)` — usare SOLO se il cluster template ha audience internazionale esplicita.

### Terms to exclude
`risparmio-fiscale-garantito · migliore-commercialista · tasse-zero · finanza-facile · guadagna-con-le-tasse`

---

## 8 · Imagery pack pointer

Pack target (Commit 3): `imagery/packs/financial-services.md`.

**Direzione imagery**:
- **Soggetti richiesti**: scrivanie con documenti a piramide, persona che rivede un prospetto, mani su tastiera di una calcolatrice (sì, ancora — ha forza visiva), stringa di numeri in stampa, un tavolo di riunione sobrio con caffè, ritratti di persona in giacca senza cravatta (credibilità SMB).
- **Palette**: toni neutri caldi (beige, carta, legno chiaro) + accento blu-notte per affidabilità. Evitare verde-dollaro e oro-eccesso.
- **Composizione**: chiusa, profondità di campo ridotta, editorial-editoriale non stock-ridente.
- **Evitare**: operatori col sorriso stock, frecce up-to-the-right, infografiche, grafici a torta colorati, "hand-shake business" cliché.

---

## 9 · Audience tags

```
["smb", "freelance", "studio"]
```

---

## 10 · Price tier rationale

**Tier consigliato**: `standard`.

**Motivazione**: il prodotto cliente medio dello studio è un servizio ricorrente SMB (5-25k€/anno), non un contratto enterprise. Premium si giustifica solo per studi dedicati a wealth management o grandi patrimoni — in quel caso, il template può essere overridden a `premium` con note nel PR.

---

## 11 · Feature flag expectations

| Flag | Expected | Rationale |
|---|---|---|
| `has_shop` | `False` | Servizi fiscali non si vendono a carrello |
| `has_booking` | `True` | Primo appuntamento è la call-to-action primaria |
| `has_portfolio` | `False` | Non c'è un portfolio di lavori; i clienti non sono case study pubbliche |
| `has_blog` | `False` (opzionale) | Un blog fiscale serio richiede manutenzione continua; sconsigliato in MVP |
| `has_video` | `False` | Video corporate sul sito di uno studio tributario sembra sempre fuori luogo |
| `has_rtl` | `True` | D-098 uniforme |
| `is_multi_page` | `True` | Multi-pagina per natura (home · studio · servizi · scadenze · contatti minimo) |

---

## 12 · Example brand names

- **Fiscus — Studio Tributario** (pilot template)
- **Conti & Associati Commercialisti**
- **Libris — Studio Revisori Contabili**

---

## 13 · Anti-patterns

- ❌ "Risparmia fino al 40% sulle tasse" — sconfinamento normativo, linguaggio da promozione bancaria.
- ❌ "Il tuo commercialista di fiducia" — cliché inflazionato; dire invece "il tuo studio tributario di riferimento".
- ❌ "Esperti da 30 anni nel settore" senza nome del fondatore e anno di iscrizione albo.
- ❌ Stock di persona che indica un grafico a barre su monitor.
- ❌ Form contatti senza richiesta di P.IVA o CF: segnala poca serietà della pipeline.
- ❌ Bullet point "onestà · trasparenza · professionalità": le virtù non sono un servizio.
- ❌ "Area clienti" senza sistema di autenticazione reale (Wave 2 non include auth cliente).

---

## 14 · D-054 differentiation notes

### Sibling templates in cluster

Nessuno (cluster vuoto pre-pilot). `fiscus-commercialista` è il primo.

### Adjacency notes

**Questo cluster deve sentirsi adiacente a**:
- `notary-commercialista` (mondo dei professionisti del numero/atto · tono istituzionale).
- `professional-services` (B2B · servizio ricorrente).

**Questo cluster deve sentirsi distinto da**:
- `coaching` — coaching vende cambiamento/accountability, financial-services vende conformità.
- `corporate` (Pragma) — Pragma è azienda strutturata che si presenta al mercato; financial-services è uno studio professionale che si presenta a clienti fisici/PMI.
- `modern-law-tech` — quella è legge, qui è fiscalità. Terminologia diversa (TUIR vs GDPR, F24 vs contratti).

### Differentiation matrix (quando arriverà un sibling N+1)

Assi obbligatori di differenziazione fra due template `financial-services`:
1. Specializzazione (tributario vs wealth vs consulenza del lavoro vs revisione)
2. Palette (neutro caldo vs neutro freddo)
3. Segmento audience (micro-imprese vs PMI vs patrimoni privati)
4. Presenza/assenza della sezione "Calendario scadenze"
5. Stile ritratti (giacca-e-cravatta vs casual-smart)
6. Tono hero (dichiarativo-tecnico vs narrativo-editoriale)
7. Presenza lead-magnet (guida PDF vs webinar vs checklist)
8. Profondità ricorrenza (trimestrale vs mensile)
9. Form contatti richiede CF o anche solo email
10. Presenza area "contenzioso" (distintiva: non tutti gli studi la offrono)

---

## 15 · Changelog

| Data | Autore | Modifica |
|---|---|---|
| 2026-04-20 | Phase Lead | Initial blueprint · X.3 Commit 2 |
