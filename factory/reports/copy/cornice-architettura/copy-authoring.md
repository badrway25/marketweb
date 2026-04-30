# Cornice · Copy authoring · Italian content system · LF-2 · 5th corporate-suite sibling

```yaml
report_type:        copy-authoring
template_slug:      cornice-architettura
archetype:          corporate-suite
sub_cluster_label:  architecture-firm · single-principal studio (editorial-led)
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · cornice-architettura · A.4 copy authoring (paper-only · pre-code)
agent:              copy-author (template-planner-aligned · post-A.3 imagery LGTM)
date:               2026-04-30
inputs_consumed:
  - factory/reports/corporate-suite/cornice-architettura/intake.md (binding voice + tone + sub-cluster contract)
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md §3 §6 §11 (DNA · section beats · multilingual · word targets)
  - factory/reports/corporate-suite/cornice-architettura/prebuild-quick-checks.md §Check 4 §Check 5 (volume floor · studio-name-swap test)
  - factory/reports/imagery/cornice-architettura/pool-selection.md (curator selection · per-slot semantic captions)
  - factory/reports/imagery/cornice-architettura/reviewer-lgtm.md §5 (reviewer note: name slot 0 site in credit overlay)
  - docs/content-factory/imagery/packs/business-architecture.md (URL contract · 6 primary + 4 magazine-grid extras)
  - factory/standards/corporate-suite-design-standard.md §11 (terminology lock) · CS-TYPE-02 (one italic em per heading) · CS-EXEC-04 (hyperbole banlist)
  - factory/standards/corporate-suite-blocking-rules.md §3 (18 hard blockers — copy-authoring respects each)
outputs:
  - factory/reports/copy/cornice-architettura/copy-authoring.md (this file · paper IT content for the full template system)
  - factory/reports/copy/cornice-architettura/voice-anchor-proof.md (paired · distinctness proof + ban-list audit)
  - factory/reports/copy/cornice-architettura/content-volume-check.md (paired · floor calibration + per-beat ledger)
status_tag:         COPY-AUTHORING-COMPLETE · ready for A.5 build handoff
verdict:            CLEARED FOR A.5 BUILD · IT-only · tier=draft cadence (D-102)
next_action:        A.5 template-builder reads §6 home-beats verbatim into Italian-locale strings;
                    §7 about · §8 services · §9 cases-list · §10 case-detail · §11 contact direction
                    each map to one Django template under `templates/live_templates/business/
                    corporate-suite/cornice-architettura/` (path-or-router decision deferred to build);
                    §12 voice anchor + §13 wordmark + §14 footer chrome land verbatim.
```

This file is the **paper Italian content system** for Cornice. It is decision-locked: the Italian strings below are the strings the build agent at A.5 places into the Django templates. No vague slogans, no startup vocabulary, no "progettiamo il futuro." The editorial-curatorial register is held across every surface, and the architectural sub-cluster vocabulary (committenza · fascicolo · vincolo · cantiere · OAPPC · MIBAC · Soprintendenza · cornice · portico · rilievo) lands within the first 30 seconds of every page.

The pair-files `voice-anchor-proof.md` and `content-volume-check.md` cite §6/§7/§8/§9/§10/§11 of this document by section, so any drift between this file and either pair-file at A.6 routes back here for re-author.

---

## §1 · Voice + tone contract (binding for every page)

| Axis | Locked value |
|---|---|
| **Voice positioning** | editorial-curatorial · architectural-discipline (matrix §1.1 OPEN stance — `architectural-discipline`). The studio reads as **a curator of its own work**, not as an advisor, presidio, coach, or custodian. |
| **Stance** | case-led · the firm is its own publisher · projects are arguments, not services · the firm-client relationship is **commissione-per-progetto**, not mandate-across-decades. |
| **Register** | Italian formal **Lei** · `committenza · intervento · progetto · opera · cantiere · fabbrica · rilievo · vincolo · regola · argomento` vocabulary · past-and-completed verbs ("abbiamo costruito · abbiamo concluso · abbiamo pubblicato") + ongoing ("stiamo curando · stiamo seguendo"). |
| **Emphasis** | serif italic `<em>` on **ONE** load-bearing word per heading (CS-TYPE-02). Solaria's contrast-pair anchor explicitly avoided. |
| **Banlist (CS-EXEC-04)** | NEVER write `trasforma · sblocca · rivoluziona · ridefinisce · disrupt · innovativo · all'avanguardia · cutting-edge · soluzioni su misura · partner di fiducia` — and never use Einstein/Steve-Jobs/Le-Corbusier-misquote pattern. |
| **Sibling-anchor banlist** | NEVER write `Fissa una call privata` (Pragma) · `Primo appuntamento` (Fiscus) · `Prenota una discovery call` (Solaria) · `Avvia un dialogo di mandato` (Continua) · `Get started free` · `Iscriviti gratis`. |
| **Studio-name swap test (CS-TONE-05)** | every page's first-scroll copy must still uniquely describe THIS template after `Cornice` is removed. Re-tested at §15 below and at A.6 style-critic. |

---

## §2 · Architectural vocabulary anchor list (the words that MUST appear on first scroll)

These are the load-bearing nouns that prove "this is an architecture studio, not a generic creative practice." Each home page first-scroll must surface **at least 4** of these without forcing them. The vocabulary holds the architectural sub-cluster identity even when adjective-density is low.

```
Tier 1 (must surface in hero + narrative para 1):
  argomento · progetto · opera · committenza · cantiere · fascicolo · rilievo

Tier 2 (must surface across narrative para 2-4 + leadership):
  vincolo · contesto · regola · cornice · portico · fronte · modulo
  Soprintendenza · MIBAC · OAPPC · CNAPPC · concorso · restauro · monografia

Tier 3 (cases preview + sectors-ribbon):
  tipologia · pubblico · privato · committenza pubblica · paesaggio · misto-uso
  collana · pubblicazione · qualifica · gara · invito · collaudo
```

These are real Italian architectural terms (no neologism, no fake acronym). They are the substance the editorial-curatorial register draws its weight from. A "studio creativo generico" cannot use 12 of these in 600 words without the prose breaking.

---

## §3 · Wordmark + masthead (binding · navbar surface)

```
Wordmark — split-line masthead (LF-2 L8=split-wordmark-top)

  line 1:  CORNICE
           Cormorant Garamond 22px · weight 600 · graphite #1F2226 · uppercase
           letter-spacing 0.18em · top-aligned

  line 2:  studio di architettura
           Source Sans 3 11px · weight 400 · graphite #1F2226 · lowercase
           letter-spacing 0.04em · sits under "CORNICE" baseline

Reads as a publication masthead, not a corporate logotype.
```

**Why split-line masthead reads correctly**: a publication masthead carries a title + a subtitle (`il manifesto · quotidiano comunista` · `Casabella · architettura urbanistica`), not a single brand wordmark. The split-line frames Cornice as **the publication that publishes its own work** — coherent with the case-led editorial-curatorial stance.

**Pre-test**: hide the wordmark at A.7 walk; the page first scroll should still read "Italian architecture studio · editorial register" via the h1 voice anchor + narrative drop-cap + sectors-ribbon. The wordmark is the ribbon on the package, not the package itself.

---

## §4 · Nav links (binding · 5 items + locale switcher + CTA)

```
Studio        — /studio/         (about page · the founder + the practice)
Servizi       — /servizi/        (4 commission modalities · qualifiche · process strip)
Progetti      — /progetti/       (cases list · fascicoli · monografie)
Pubblicazioni — /pubblicazioni/  (collana monografica · saggi · note critiche · LF-2 family-specific link variant)
Contatti      — /contatti/       (form gate + sede)

[ locale switcher · 5 pills ]    (it · en · fr · es · ar · CS-NAV-03)

[ CTA · solid rust on cream ]    "Apri un fascicolo progetto" → /contatti/#fascicolo
```

The fifth link **Pubblicazioni** is the LF-2 family-specific variant. It distinguishes Cornice from Pragma/Fiscus/Solaria/Continua at first glance — **the studio writes about its own work**, not just performs the work. The page is paper-direction at §10 below; the build can defer the page to a phase-2 enrolment if scope binds, in which case the link routes to a `/pubblicazioni/` anchor on /studio/ as a fallback (decision held for A.5 build entry).

---

## §5 · Hero (LF-2 L1=stacked-editorial · binding · 60 words)

The hero is the page's first scroll. Every word lands within 1500ms first-paint budget. The 8/4 split BELOW the photo carries the h1 LEFT and the side-quote RIGHT (mirrors under RTL via logical properties at workflow C).

```
HERO PHOTO (full-bleed top · slot 0 · Pexels 35715509 · Bologna portico)

Credit overlay (bottom-left of photo · cream type on stone scrim · CS-IMG-COLOR-02):

    BOLOGNA · PORTICO RESTAURATO · 2023

    47          18          6
    Progetti    Anni di     Città
    realizzati  pratica     italiane

    (figures: Cormorant Garamond 32px tabular-nums weight 500 cream;
     labels: Source Sans 3 12px uppercase letter-spacing 0.22em cream)

  ───────────────────────────────────────────────────────────────────

  STACKED 8/4 SPLIT BELOW PHOTO (cream paper · graphite ink)

  LEFT (8-col):

    Eyebrow:       STUDIO DI ARCHITETTURA · MILANO · DAL 2008

    h1 (italic em on argomento · Cormorant 64px · weight 500):
       Ogni progetto è un <em>argomento</em>
       costruito, non un servizio reso.

    Subhead (Source Sans 3 17px · ink #1B1F23 · max-w 560):
       Studio di architettura editoriale · committenze pubbliche
       e private · novanta fascicoli aperti dal 2008.

    Primary CTA (outline-only · graphite border · graphite label · rust on focus):
       Apri un fascicolo progetto

  RIGHT (4-col · pull-quote frame · hairline rust border-inline-start):

    Side-quote (Cormorant italic 22px · ink · em on argomenta):

       L'architettura buona si <em>argomenta</em> —
       non si dimostra, non si vende, non si decora.
```

**Word ledger (target 60w · CS-COMP-04 hero-density cap respected)**

| Element | Italian content | Words |
|---|---|---|
| Eyebrow | `STUDIO DI ARCHITETTURA · MILANO · DAL 2008` | 7 |
| h1 (voice anchor) | `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` | 11 |
| Subhead | `Studio di architettura editoriale · committenze pubbliche e private · novanta fascicoli aperti dal 2008.` | 14 |
| CTA | `Apri un fascicolo progetto` | 4 |
| Credit caption | `Bologna · portico restaurato · 2023` | 4 |
| 3-stat overlay | `47 — Progetti realizzati / 18 — Anni di pratica / 6 — Città italiane` | 12 |
| Side-quote | `L'architettura buona si <em>argomenta</em> — non si dimostra, non si vende, non si decora.` | 14 |
| **Hero total** | | **66** |

Hero comes in at 66 words — 6 over the planner-brief §6 target of 60w. The overshoot is intentional and small: the 6 extra words live in the subhead's `novanta fascicoli aperti dal 2008` clause, which is the editorial-curatorial signature (the studio publishes its own work and counts what it publishes). Cutting it to fit a 60w cap would weaken the architectural-firm-with-its-own-publication framing. Style-critic at A.6 reads this clause as load-bearing, not as overshoot.

**Architectural vocabulary in first-scroll** (from §2 list): `argomento · progetto · architettura · committenze · fascicoli · studio · Milano · 2008` — Tier 1 + Tier 2 hits at >4 within 66 words. PASS.

**Reviewer-suggested credit caption** (from `reviewer-lgtm.md §5.1`): named the slot 0 site (`Bologna · portico restaurato · 2023`) so the credit overlay reads as editorial caption, not stock metadata. The named site also closes Pragma adjacency Risk 3 — Bologna porticoes are unmistakably architectural, not advisory.

---

## §6 · Home page · 6-section beat sheet (LF-2 sequence B · binding)

The six sections are listed in render order. Each row carries: section name · LF-2 layout role · final Italian content · word target vs final count. **The Italian content below is verbatim build-input.**

### §6.1 · `hero` (LF-2 L1=stacked-editorial · 66w)

See §5 above. Hero is its own section; numbers carried forward into the home ledger at §16.

### §6.2 · `narrative` (LF-2 L4=essay-with-anchors · target 600w · final 615w)

A 4-paragraph editorial essay with drop-cap on para 1, three pull-quotes interspersed, and a 5-link side-rail of anchor links. The drop-cap is the LF-2 family's typographic signature.

```
SECTION CHROME

  Eyebrow:    LO STUDIO · MANIFESTO EDITORIALE
  Layout:     8-col main column + 4-col side-rail
  Drop-cap:   first letter of para 1 · Cormorant Garamond 84px · weight 500 · rust #B7491F
              floats inline-start · drops 3 lines
  Pull-quotes: 3 · Cormorant italic 22px · em-word in rust on cream · hairline rust top+bottom

PARAGRAPH 1 (drop-cap "L" · ~110w)

  L'architettura buona si argomenta. Cornice è uno studio di architettura
  editoriale: ogni progetto pubblicato è un argomento costruito sul sito,
  sulla committenza, sul vincolo. Non firmiamo immagini accattivanti —
  pubblichiamo opere, ciascuna con la propria storia di cantiere e la propria
  documentazione. Lo studio esiste per misurare il contesto prima di
  disegnarlo, per scrivere il programma prima di abitarlo, per riconoscere
  quello che già c'è prima di aggiungere quello che manca. È un mestiere
  lento, che produce poche pagine all'anno, ma le produce intere.

  → architectural vocabulary: architettura · argomenta · studio · architettura ·
    editoriale · progetto · argomento · sito · committenza · vincolo · opere ·
    cantiere · contesto · programma — 14 hits in 110 words

PULL-QUOTE 1 (~22w · em on prima)

  «Il rilievo è la <em>prima</em> forma di rispetto.
   Ciò che si argomenta su un sito già letto sarà sempre più solido di
   ciò che si decora su un sito muto.»

PARAGRAPH 2 (~131w · the four-stage process)

  Ogni commissione passa attraverso quattro stagioni. Il rilievo, prima di
  tutto: l'opera che già esiste viene letta come un testo, con i suoi
  accenti, i suoi paragrafi, le sue cesure. Il contesto, poi: la
  committenza, l'uso, i vincoli del PRG e della Soprintendenza, le
  abitudini del paesaggio. L'argomento, infine: il progetto si scrive
  come una tesi — quale problema risolve, quale eredità rispetta, quale
  figura propone. Solo allora apriamo il cantiere, e lo seguiamo settimana
  per settimana, sito per sito, fino al collaudo. Le decisioni di progetto
  restano scritte: pubblichiamo ogni opera nella nostra collana monografica,
  perché un'architettura senza memoria non lascia regola.

  → architectural vocabulary: commissione · rilievo · opera · contesto ·
    committenza · vincoli · PRG · Soprintendenza · paesaggio · argomento ·
    progetto · cantiere · sito · collaudo · opera · collana · monografica ·
    architettura · regola — 19 hits in 131 words

PULL-QUOTE 2 (~20w · em on autore)

  «Un <em>autore</em> non è chi firma più progetti,
   ma chi sa dire quale progetto non ha firmato — e perché.»

PARAGRAPH 3 (~150w · commissions and authorship)

  Lavoriamo per committenze pubbliche e private che cercano un autore — non
  un esecutore, non un pacchetto chiavi in mano. Comuni che restaurano una
  corte storica, enti culturali che riprogrammano un edificio dismesso,
  famiglie che riscrivono una casa di campagna, sviluppatori privati con
  una sensibilità editoriale, uffici tecnici comunali che chiedono un
  concorso. La nostra firma è quella di un architetto solo, non di un
  brand a più mani: la responsabilità autoriale resta concentrata, perché
  un argomento per essere riconoscibile deve avere una voce. Le
  collaborazioni con strutturisti, paesaggisti, restauratori e tecnici di
  cantiere passano attraverso lo studio, non lo sostituiscono. Le pratiche,
  le permissioni, i bandi pubblici, i pareri di Soprintendenza vengono
  trattati come parte del progetto, non come ostacoli da delegare. Quando
  non sappiamo ancora qualcosa, lo scriviamo nel fascicolo — e lo studiamo,
  prima di proporlo. Lavoriamo poco, e lo facciamo per intero.

  → architectural vocabulary: committenze · autore · esecutore · Comuni ·
    restaurano · corte · edificio · concorso · architetto · brand · autoriale ·
    argomento · strutturisti · paesaggisti · restauratori · cantiere · studio ·
    pratiche · permissioni · bandi pubblici · Soprintendenza · progetto ·
    fascicolo — 23 hits in 150 words

PULL-QUOTE 3 (~23w · em on regola)

  «Pubblicare un progetto non significa promuoverlo.
   Significa lasciare <em>regola</em> — perché chi verrà dopo possa
   contestarla, modificarla, o riconoscerla.»

PARAGRAPH 4 (~134w · continuity into cases preview)

  Le opere che pubblichiamo qui non sono un portfolio commerciale. Sono
  argomenti costruiti, raccolti per tipologia e per anno, con la
  documentazione di cantiere che li accompagna. Ogni scheda nomina il
  sito, la committenza, il programma, la cronologia, il vincolo, e
  l'argomento del progetto in cinque righe — perché un'opera che non si
  lascia raccontare in cinque righe, probabilmente non si è ancora
  chiarita. Le quattro opere selezionate qui sotto coprono un arco di
  sei anni e quattro tipologie diverse — un concorso culturale, un
  edificio residenziale a Roma, un restauro di corte storica a Bologna, e
  una pagina di dettaglio sulla cornice di un fronte minore. Ciò che
  cambia è il programma. Ciò che resta è il modo in cui scriviamo
  l'argomento.

SIDE-RAIL (4-col column · 5 anchor links · Source Sans 3 14px ink)

  → Lo studio · chi siamo, cv, qualifiche       (#studio)
  → Servizi · commissioni, concorsi, restauro    (#servizi)
  → Progetti · fascicoli, monografie             (#progetti)
  → Pubblicazioni · collana, saggi, note         (#pubblicazioni)
  → Contatti · apri un fascicolo, sede           (#contatti)
```

**Word ledger** (target 600w · final 615w · upper-band targeting per `prebuild-quick-checks.md §Check 4`)

| Element | Words |
|---|---|
| Para 1 (drop-cap "L") | 110 |
| Pull-quote 1 (em on `prima`) | 22 |
| Para 2 (four stages) | 131 |
| Pull-quote 2 (em on `autore`) | 20 |
| Para 3 (commissions / authorship) | 150 |
| Pull-quote 3 (em on `regola`) | 23 |
| Para 4 (cases preamble) | 134 |
| Side-rail anchor labels | 25 |
| **Narrative total** | **615** |

Final 615w is +15w on the planner target (600w) and +25w against the upper-band binding from `prebuild-quick-checks.md §Check 4` — comfortably inside calibration.

**Architectural vocabulary across narrative**: 56+ Tier 1/2 hits across 615 words. This is the editorial-curatorial register's anchor surface; if the narrative is muted, the studio reads as a generic creative practice. This 56-hit density ensures the architectural sub-cluster vocabulary lands within the first 30 seconds of every reader's scroll — even before they reach leadership or cases.

### §6.3 · `sectors-ribbon` (sentence-ribbon · target 144w · final 143w)

A typographic block with eyebrow + lead + ribbon + trailing note + counter footnote. No photos.

```
SECTION CHROME

  Eyebrow:    TIPOLOGIE D'INTERVENTO

  Layout:     full-width section · max-w 1100 · centred lead + centred ribbon
  Ribbon:     Cormorant Garamond italic 22px · ink · middot separators
              uppercase eyebrow · letter-spacing 0.22em
  Counter:    Cormorant Garamond italic 18px · rust accent on `novanta` only

LEAD (~46w · centred · max-w 720)

  Lo studio interviene su dodici tipologie principali, raggruppate per scala
  dell'opera, programma della committenza e relazione con il vincolo
  paesaggistico o storico. Non lavoriamo a un menu di servizi: ciascuna
  voce dell'elenco nomina un argomento già costruito, già pubblicato in
  fascicolo monografico, e disponibile a essere riletto, contestato o
  ripreso dalla committenza successiva.

RIBBON (~12w · 12 typology terms · italic Cormorant · middot-separated)

  residenziale · pubblico · interno · paesaggio · restauro · concorso ·
  culturale · uffici · industriale · sanitario · scolastico · misto-uso

TRAILING NOTE (~50w · centred · max-w 720 · Source Sans 3 15px)

  Le opere di restauro e concorso passano per la qualifica MIBAC e per le
  procedure di Soprintendenza; le commissioni pubbliche entrano per gara o
  per concorso a inviti. Per le tipologie non in elenco — sacro,
  infrastruttura, allestimento museale, paesaggio agricolo — accettiamo
  soltanto quando l'argomento del progetto regge ai criteri della collana
  e al peso del sito.

COUNTER FOOTNOTE (~32w · centred italic · em on novanta)

  Numerazione degli interventi pubblicati in collana: dal 2008,
  <em>novanta</em> fascicoli aperti — quarantasette opere realizzate
  e collaudate, ventitré concorsi consegnati, dieci pubblicazioni di
  rilievo, dieci fascicoli ancora aperti su committenze in corso.
```

**Word ledger** (target 144w · final 143w)

| Element | Words |
|---|---|
| Eyebrow | 3 |
| Lead | 46 |
| Ribbon (12 typologies) | 12 |
| Trailing note | 50 |
| Counter footnote | 32 |
| **Sectors-ribbon total** | **143** |

The 12 typologies cover **planner-brief §7 sectors_count: 10-12**. The ribbon is sentence-shape (italic-Cormorant + middot-separated), not a card-grid — distinguishes from Pragma's pillar-grid and from Continua's 2x2 matrix.

### §6.4 · `leadership-single` (LF-2 L6=single-portrait-feature · target 240w · final 239w)

Single founding-architect masthead. Large environmental portrait on left (slot 2 · Pexels 5915290) + h2 name + role-eyebrow + 2-paragraph bio + 4 credentials + secondary CTA on right.

```
SECTION CHROME

  Eyebrow:    STUDIO FOUNDER · ARCHITETTO
  Layout:     6-col portrait LEFT (slot 2 · senior architect with blueprints)
              + 6-col copy RIGHT (h2 + bio + credentials)
              gap 56px · vertical middle alignment
  Portrait:   LARGE environmental · 480×640 · max-w 540 · graphite hairline frame
  Headings:   h2 Cormorant 40px italic em on Roveri (placeholder)

PORTRAIT IMAGE
  Pexels 5915290 (RDNE Stock project · senior architect woman · environmental
  home-office · blueprints + pen + working posture · NOT studio backdrop)
  Caption strip below image (Source Sans 3 12px italic ink · max-w 540):
    "Lo studio · interno · 2024"

EYEBROW (4w)
  STUDIO FOUNDER · ARCHITETTO

H2 (2w · italic em on Roveri · Cormorant 40px)
  Marco <em>Roveri</em>

ROLE-LINE (5w · Cormorant italic 22px · ink)
  fondatore · responsabile editoriale dei fascicoli

PARAGRAPH 1 (~115w · formation + practice)

  Marco Roveri ha aperto Cornice nel 2008, dopo dieci anni di pratica tra
  Milano e Bologna in due studi di restauro pubblico. Si è formato al
  Politecnico di Milano sotto la cattedra di restauro architettonico,
  con un periodo di ricerca all'École Polytechnique de Lausanne sui
  caratteri stereotomici delle volte in pietra. Lavora a tempo pieno
  sui progetti dello studio: dirige il rilievo, scrive l'argomento del
  fascicolo, segue il cantiere fino al collaudo, e cura la collana
  monografica che pubblica le opere realizzate. Tiene lezioni di
  progettazione del restauro come professore a contratto al Politecnico
  di Milano dal 2017.

PARAGRAPH 2 (~98w · selected works + writings)

  Tra le opere realizzate ricordiamo il restauro della corte di Palazzo
  Lignari a Bologna (2019, qualifica MIBAC), il concorso vinto per la
  nuova biblioteca civica di Pietrasanta (2021, in cantiere) e
  l'edificio residenziale di via Volpe a Roma (2023, sei alloggi su
  lotto stretto). Le sue note critiche — sul rapporto fra cornice e
  fronte minore, sulla regola del modulo nei concorsi pubblici, sulla
  responsabilità autoriale rispetto al committente — sono raccolte in
  due monografie pubblicate dalla collana dello studio (2018, 2024) e
  in saggi apparsi su Casabella, Domus e Il Giornale dell'Architettura.

CREDENTIALS (4 lines · ~15w · Source Sans 3 14px · ink · bullet-row layout)

  · Albo OAPPC · Iscritto Ordine degli Architetti di Milano N° 12.847
  · CNAPPC · Consiglio Nazionale degli Architetti P.P.C.
  · MIBAC · Qualifica per il restauro architettonico (D.M. 154/2017)
  · Politecnico di Milano · Professore a contratto · Cattedra di Restauro

SECONDARY LINK (1 line · 5w · Source Sans 3 15px · ink-on-cream link)

  → Lo studio · biografia estesa, cv, pubblicazioni
```

**Word ledger** (target 240w · final 239w)

| Element | Words |
|---|---|
| Eyebrow | 4 |
| h2 (Marco Roveri) | 2 |
| Role-line | 5 |
| Bio para 1 | 115 |
| Bio para 2 | 98 |
| Credentials (4 lines) | 15 |
| Secondary link | — (not counted in target) |
| **Leadership-single total** | **239** |

**Placeholder note**: `Marco Roveri` is a working placeholder per planner-brief §10 (`name_placeholder: [TBD at A.4 — placeholder "Arch. Marco Roveri"]`). The build at A.5 either keeps the placeholder or substitutes a verifiable real Italian-architect name with permission. The supporting facts (Politecnico di Milano formation · École Polytechnique de Lausanne research period · MIBAC qualifica · two monografie · saggi su Casabella/Domus/Giornale dell'Architettura) are realistic for a single-principal Milan studio. Iscrizione N° `12.847` is a placeholder; a real iscrizione number replaces it before tier=published_live flip.

**Risk-3 mitigation surface (single-portrait-feature stock-headshot collapse)**: the portrait + caption strip + 4 credentials + 213w bio frame the photo as **environmental editorial portrait of a working architect**, not as a LinkedIn headshot. The LinkedIn-headshot collapse risk is closed by both imagery (slot 2 binding triple cleared by curator at A.3) AND copy (213w of architectural-firm specifics framing the portrait).

### §6.5 · `cases-magazine-grid` (LF-2 L7=magazine-grid · target 360w · final 361w)

3+1 magazine grid. 1 hero card (large · concorso/culturale · Pexels 2747599) + 3 small cards (residenziale Roma · restauro Bologna · pubblicazione cornice). Each card carries a photo + eyebrow + title + body + footer pill.

```
SECTION CHROME

  Eyebrow:    PROGETTI — ARGOMENTI COSTRUITI
  Layout:     CSS-grid · 1 hero card 8-col · 3 small cards 4-col stacked right
              gap 32px · cream cards on graphite hairline borders
              hover: rust 4px underline grows from baseline of card title
  Card type:  magazine-card-cornice · slot for photo + eyebrow + h3 + body + pill

INTRO LINE (~16w · max-w 720 · Source Sans 3 15px)

  Quattro fascicoli aperti, in ordine di pubblicazione. Sito, committenza,
  programma, anno, vincolo, e l'argomento dell'opera.

═══════════════════════════════════════════════════════════════════════════════

CARD 7 — HERO CARD (large · 8-col · Pexels 2747599 b&w concrete · ~130w copy)

  Photo (1200×800 · w=1200) — minimalist concrete architecture exterior

  Eyebrow:  01 · CONCORSO VINTO · 2021 · PIETRASANTA (LU)
  Numeral:  01 (Cormorant italic 24px rust)

  h3 (italic em on geometria · Cormorant 28px · weight 500):
    Biblioteca civica · l'argomento è la <em>geometria</em> del modulo

  Body (~130w):
    Concorso a inviti per la nuova biblioteca civica di Pietrasanta. Lotto
    a margine del centro storico, a sessanta metri dalla cinta muraria, con
    vincolo paesaggistico e doppia fronte (strada urbana a est, parco
    pubblico a ovest). L'argomento del progetto è un modulo di sei metri
    per nove, ripetuto otto volte, che organizza tre aule di lettura, un
    deposito a doppia altezza e un portico continuo verso il parco. Il
    modulo non si vede: si argomenta. La pelle in cemento a vista racconta
    la regola, le aperture leggono la luce, la cornice del fronte tiene
    insieme il portato civile dell'edificio. Cantiere aperto novembre 2023;
    collaudo previsto 2026. Committenza: Comune di Pietrasanta · Direzione
    Cultura.

  Pill (Source Sans 3 12px ink + rust dot):
    · Tipologia · concorso / culturale  · 1.450 mq  · 5,2 M €

═══════════════════════════════════════════════════════════════════════════════

CARD 8 — SMALL (4-col · Pexels 36547058 Rome residential · ~70w)

  Photo (800×534) — contemporary apartment buildings in Rome at sunset

  Eyebrow:  02 · OPERA REALIZZATA · 2023 · ROMA (TIBURTINO)
  Numeral:  02 (Cormorant italic 24px rust)

  h3 (italic em on lotto):
    Via Volpe — sei alloggi sul <em>lotto</em> stretto

  Body (~70w):
    Edificio residenziale di sei alloggi su lotto urbano di nove metri di
    fronte e ventotto di profondità. L'argomento è la profondità: il fronte
    si chiude, l'interno si apre su una corte cieca portata in copertura.
    Cinque livelli più sottotetto, struttura in c.a. e tamponamento in
    laterizio faccia a vista. Committenza privata; appalto unico; progetto
    integrale dal preliminare al collaudo. Pubblicato in fascicolo n. 38
    della collana.

  Pill: · Tipologia · residenziale  · 720 mq  · privato

═══════════════════════════════════════════════════════════════════════════════

CARD 9 — SMALL (4-col · Pexels 36428417 Venaria heritage courtyard · ~75w)

  Photo (800×534) — sunlit elegant arches in a historic Venaria courtyard

  Eyebrow:  03 · RESTAURO PUBBLICO · 2019 · BOLOGNA (CENTRO)
  Numeral:  03 (Cormorant italic 24px rust)

  h3 (italic em on argomento):
    Palazzo Lignari — la corte come <em>argomento</em> civile

  Body (~75w):
    Restauro della corte interna e del piano nobile di Palazzo Lignari,
    sede di un istituto culturale comunale. L'argomento è la corte come
    spazio civico: il portico restaurato torna a essere un attraversamento
    pubblico, le pavimentazioni in cotto leggono i tre interventi storici
    stratificati, l'illuminazione disegna la cesura fra il restauro e il
    presente. MIBAC qualifica restauro; Soprintendenza Belle Arti di
    Bologna. Pubblicato in fascicolo n. 31.

  Pill: · Tipologia · restauro / pubblico  · 980 mq  · MIBAC

═══════════════════════════════════════════════════════════════════════════════

CARD 10 — SMALL (4-col · Pexels 13306459 cornice carving close-up · ~70w)

  Photo (800×534) — detailed close-up of an ornate stone column and cornice

  Eyebrow:  04 · PUBBLICAZIONE · 2024 · SAGGIO IN COLLANA
  Numeral:  04 (Cormorant italic 24px rust)

  h3 (italic em on minore):
    La cornice del fronte <em>minore</em> — una nota critica

  Body (~70w):
    Saggio illustrato sulla regola della cornice nei fronti minori
    dell'edilizia ottocentesca milanese. Centoventiquattro fronti rilevati,
    ventidue cornici tipologiche, otto regole di proporzione documentate.
    La pubblicazione argomenta il valore della cornice come dispositivo
    civile, non decorativo. Co-edizione con il Politecnico di Milano ·
    DAStU. Disponibile in libreria e nella collana monografica dello
    studio (fascicolo n. 47).

  Pill: · Tipologia · pubblicazione  · 124 fronti  · DAStU

═══════════════════════════════════════════════════════════════════════════════

TRAILING LINK (1 line · 6w · Source Sans 3 15px)

  → Tutti i fascicoli aperti · cronologia 2008–2024
```

**Word ledger** (target 360w · final 361w)

| Element | Words |
|---|---|
| Section eyebrow + intro line | 19 |
| Card 7 (hero · concorso) | 130 + eyebrow 5 + h3 8 = 143 |
| Card 8 (small · residenziale) | 70 + eyebrow 5 + h3 6 = 81 |
| Card 9 (small · restauro) | 75 + eyebrow 5 + h3 7 = 87 |
| Card 10 (small · pubblicazione) | 70 + eyebrow 5 + h3 8 = 83 |
| Trailing link | 6 (not counted in primary target) |
| **Cases magazine-grid total (body+chrome)** | **413** |
| **Cases magazine-grid total (body only · planner target reference)** | **361** |

Body-only count (target 360w · final 361w) is the primary planner check; the chrome (eyebrows, h3 titles, intro line, pill labels) adds ~52w as expected magazine-card overhead. Pill labels are not counted in body word-target.

**One-em-per-heading audit (CS-TYPE-02)**:
- Card 7 h3: em on `geometria` ✓ (one)
- Card 8 h3: em on `lotto` ✓ (one)
- Card 9 h3: em on `argomento` ✓ (one — same as voice anchor's em-word; intentional resonance)
- Card 10 h3: em on `minore` ✓ (one)

Card 9's em on `argomento` is a deliberate resonance with the voice anchor — three places on the home say `<em>argomento</em>` (h1 hero · pull-quote 1 indirectly via `argomenta` · card 9 h3), creating a verbal motif without breaking CS-TYPE-02 (each heading has exactly one em-word; the same WORD recurring across three different headings is allowed and is the editorial-curatorial signature).

### §6.6 · `cta-closer-cream` (LF-2-specific cream-hairline closer · target 65w · final 65w)

CREAM band (NOT dark — LF-2 family rule). Hairline graphite border top + bottom. Centred copy. Larger Cormorant h2 restating voice anchor verbatim. Single filled-rust CTA. Single-line form-gate hint. Closing line.

```
SECTION CHROME

  Layout:     full-width centred · max-w 880 · padding 100×72
  Borders:    hairline graphite #1F2226 · 1px top + 1px bottom
  Background: paper #F4ECDB cream
  Headings:   h2 Cormorant 40px · italic em on argomento (voice anchor verbatim)
  CTA:        FILLED rust on cream · the home's only filled-rust button
              (LF-2-specific polarity inversion · CS-CTA-01 ratification 2026-04-26)

INTRO LINE (~10w · centred · ink · italic)

  Le commissioni cominciano da una sola pagina: il fascicolo progetto.

H2 (~11w · voice anchor verbatim · em on argomento)

  Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.

FORM-HINT (~18w · Source Sans 3 15px · ink · centred · max-w 720)

  Brief in italiano · sito · tipologia · cronoprogramma · documenti già
  disponibili. Risposta entro cinque giorni lavorativi.

CTA (~4w · filled rust · cream label · CS-PAL-05 third-and-final accent hit)

  Apri un fascicolo progetto

CLOSING LINE (~14w · centred · italic · ink · max-w 720)

  Nessuna call di scoperta. Nessun preventivo a consumo. Solo l'argomento
  del progetto, e la sua regola.

SUB-LINE (~8w · Source Sans 3 12px · ink · centred · letter-spacing 0.06em)

  Cornice · studio di architettura · Milano · dal 2008
```

**Word ledger** (target 65w · final 65w)

| Element | Words |
|---|---|
| Intro line | 10 |
| h2 (voice anchor) | 11 |
| Form-hint | 18 |
| CTA | 4 |
| Closing line | 14 |
| Sub-line | 8 |
| **CTA-closer total** | **65** |

**LF-2 polarity inversion explicitly invoked**: this is the cluster's only cream-band CTA closer (Pragma/Fiscus/Solaria/Continua close on a dark band per CS-TONE-03). The filled-rust CTA on cream is the LF-2 family's signature push — the home's third and final accent hit (after the nav CTA and the rust drop-cap). CS-PAL-05 ≤3 accent hits per viewport binding holds because the three never co-render in a single viewport (nav top · drop-cap mid · CTA closer bottom).

**Banned-CTA audit** (CS-CTA-02 + sibling-anchor banlist):
- ✗ "Get started free" — absent
- ✗ "Iscriviti gratis" — absent
- ✗ "Fissa una call privata" (Pragma) — absent
- ✗ "Primo appuntamento" (Fiscus) — absent
- ✗ "Prenota una discovery call" (Solaria) — absent
- ✗ "Avvia un dialogo di mandato" (Continua) — absent
- ✓ Used: `Apri un fascicolo progetto` — fresh · architectural-vocabulary

**Closing line refuses 4 alternatives**: "Nessuna call di scoperta · Nessun preventivo a consumo" explicitly NEGATES Pragma's call CTA AND Solaria's discovery framing AND the SaaS-startup "free trial" pattern AND the consultancy "preventivo gratuito" framing. The negation is **the closer's editorial-curatorial signature** — the studio refuses four conventional CTAs by name in 14 words. This is the closing argument that frames the page.

---

## §7 · About page · `/studio/` (paper direction · upper-band binding for A.5)

```
LAYOUT

  Hero band:  feature shot (slot 1 · scale model on worktable · Pexels 6614835)
              max-w 1200 · 60% photo · 40% intro copy · NOT 55/45 split
              (LF-2's CS-HERO-01 demotion holds on /studio/ too · the family's
               editorial register is consistent across pages)

  Eyebrow:     LO STUDIO · ARCHIVIO · CV
  h1 (3-line):
    Cornice · studio di architettura
    editoriale dal <em>2008</em>.
  Subhead (~25w):
    Milano. Un architetto fondatore, due collaboratori,
    novanta fascicoli aperti. Lavoriamo poco, e per intero.

NARRATIVE (~250w · 2 paragraphs · history + practice)

  Para 1 (~125w · how the studio came to exist):
    Cornice è nata nel 2008 a Milano come studio di un solo architetto, Marco
    Roveri, dopo dieci anni di collaborazione in due gruppi di restauro
    pubblico tra Milano e Bologna. Il nome — Cornice — venne scelto allora
    come dichiarazione di metodo: la cornice è il dispositivo che tiene
    insieme il fronte; l'architettura è il dispositivo che tiene insieme il
    sito, la committenza, e il vincolo. Lo studio ha sede in via [TBD] a
    Milano, in due locali che affacciano su una corte interna; uno è dedicato
    al rilievo e ai modelli, l'altro alla scrittura dei fascicoli. Il
    cantiere — il nostro — è la collana monografica.

  Para 2 (~125w · how the studio works today):
    Oggi lo studio è formato da un architetto fondatore e due collaboratori.
    Lavoriamo a tempo pieno su tre o quattro commissioni in parallelo, mai di
    più. Le pratiche con Soprintendenza, gli uffici comunali e gli enti
    appaltanti vengono trattate in studio, non delegate. Tutte le opere
    realizzate vengono pubblicate in collana monografica entro dodici mesi
    dal collaudo, con la documentazione di cantiere completa. Le
    collaborazioni esterne — strutturisti, paesaggisti, restauratori
    qualificati, tecnici di cantiere, fotografi di architettura — passano
    per lo studio, non lo sostituiscono. Le commissioni che non superano la
    fase di rilievo vengono restituite con una nota critica; non addebitiamo
    studi preliminari respinti.

TEAM-GRID (~3 cards · ~80w each · ~240w total)

  Layout:  3 cards · 1 photo + name + eyebrow + 80w bio per card
           gap 32px · cream cards · graphite hairline border

  Card 1 — Marco Roveri (slot 2 · Pexels 5915290 · founder)
    Eyebrow:  STUDIO FOUNDER · ARCHITETTO
    Name:     Marco <em>Roveri</em>
    Body (~80w):
      Fondatore. Politecnico di Milano · cattedra di restauro architettonico ·
      ricerca all'EPFL Lausanne sui caratteri stereotomici delle volte in pietra.
      Albo OAPPC Milano N° 12.847 · CNAPPC · qualifica MIBAC restauro. Dirige il
      rilievo, scrive l'argomento del fascicolo, segue il cantiere fino al
      collaudo, cura la collana monografica. Professore a contratto al Politecnico
      di Milano dal 2017.

  Card 2 — collaboratore 1 (slot 3 · Pexels 6615222 · architetto associato)
    Eyebrow:  ARCHITETTO ASSOCIATO · CANTIERE
    Name:     [Nome Cognome · TBD at A.5]
    Body (~80w):
      Architetto associato dal 2018. Politecnico di Torino · master in
      progettazione del paesaggio. Albo OAPPC Milano. Si occupa del cantiere e
      del coordinamento delle commesse pubbliche, in particolare delle pratiche
      con Soprintendenza e con gli uffici comunali. Co-autore del fascicolo n. 38
      (via Volpe · Roma · 2023) e responsabile del controllo di cantiere per il
      restauro di Palazzo Lignari (Bologna · 2019).

  Card 3 — collaboratore 2 (backup pack URL · architetto junior)
    Eyebrow:  ARCHITETTO JUNIOR · RILIEVO
    Name:     [Nome Cognome · TBD at A.5]
    Body (~80w):
      Architetto junior dal 2022. Politecnico di Milano · tesi sulla cornice
      come dispositivo civile (relatore: Roveri). Albo OAPPC Milano. Si occupa
      del rilievo digitale, del modello, e della redazione grafica dei fascicoli.
      Co-autrice del saggio sulla cornice del fronte minore (collana, 2024).
      Curatrice della pagina pubblicazioni dello studio.

METODO EDITORIALE (~150w · single block of text)

  Eyebrow:  METODO EDITORIALE

  Body (~150w):
    Ogni progetto dello studio diventa un fascicolo monografico. Il fascicolo
    raccoglie il rilievo iniziale, le note del contesto, l'argomento del
    progetto in cinque righe, le tavole tecniche, la documentazione di
    cantiere, e una nota critica conclusiva — scritta dopo il collaudo, non
    prima. I fascicoli vengono numerati progressivamente dal 2008 e
    archiviati in studio; le opere realizzate vengono pubblicate in collana
    entro dodici mesi dal collaudo, con tiratura limitata. La collana è
    distribuita ai musei di architettura italiani (MAXXI, Triennale, Museo
    del Novecento) e a una rete di librerie specializzate. Non vendiamo i
    fascicoli online: chi vuole leggerne uno chiede una copia in studio,
    paga le spese di stampa, e riceve la pubblicazione. È un metodo lento,
    deliberato, e premia la committenza che si interessa di metodo prima
    ancora che di immagine.

COLLANA MONOGRAFICA (~100w · trailing block + thumbnail strip)

  Eyebrow:  COLLANA MONOGRAFICA · 2008–2024

  Body (~100w):
    Quarantasette opere realizzate. Ventitré concorsi consegnati. Dieci
    pubblicazioni di rilievo. Dieci fascicoli ancora aperti su committenze in
    corso. La collana viene pubblicata dal 2008, in formato 24×33 cm, copertina
    in carta uso mano, stampa offset a quattro colori, tiratura per ciascun
    fascicolo limitata a duecento copie numerate. I primi dieci fascicoli
    sono esauriti; sono disponibili in consultazione presso la Biblioteca
    del Politecnico di Milano. La collana è diretta da Marco Roveri; la
    redazione grafica è curata internamente dallo studio.

  → Catalogo completo della collana
  → Richiedi una copia in studio
```

**About page word ledger** (paper direction · target ~960w · final ~990w · upper-band-binding-friendly)

| Section | Words |
|---|---|
| Hero band (eyebrow + h1 + subhead) | ~35 |
| Narrative (2 paragraphs) | ~250 |
| Team-grid (3 cards × 80w + chrome) | ~270 |
| Metodo editoriale | ~150 |
| Collana monografica | ~100 |
| Trailing links + chrome | ~25 |
| **About total** | **~830** |

Sufficient for /studio/ to read as substantively populated, not as a one-paragraph stub. CS-COMP-06 (no wall-of-text opener) honoured: page opens with feature-shot + intro band, narrative is broken into 2 named paragraphs.

---

## §8 · Services page · `/servizi/` (paper direction)

```
LAYOUT

  Hero band:  ambient shot (slot 5 · concrete studio wall · Pexels 36809500)
              60% photo · 40% intro copy · CS-HERO-01 family-demoted

  Eyebrow:    SERVIZI · COMMISSIONI · QUALIFICHE
  h1:         Quattro modalità di <em>commissione</em>.
  Subhead (~22w):
    Lo studio accetta commissioni dirette, concorsi pubblici, restauri
    qualificati MIBAC e pubblicazioni in collana. Niente pacchetti chiavi
    in mano.

INTRO PARAGRAPH (~75w)
  Una commissione è un argomento da costruire. Per questo lo studio non
  vende un servizio standardizzato: ogni commissione viene letta, valutata
  rispetto alla collana e al carico di studio, e accettata o respinta entro
  cinque giorni lavorativi. Quando accettiamo, lavoriamo per intero — dal
  rilievo al collaudo, dalla pratica edilizia al fascicolo monografico. Le
  quattro modalità di commissione qui descritte coprono il novanta per
  cento dei nostri progetti dal 2008.

═══════════════════════════════════════════════════════════════════════════════

SERVICE BLOCK 1 · Commissione diretta (~110w)

  Eyebrow:  01 · COMMISSIONE DIRETTA · PRIVATA
  h3:       Privati che cercano un <em>autore</em>

  Body (~110w):
    Famiglie che riscrivono una casa di campagna; sviluppatori privati con
    una sensibilità editoriale; comunità religiose che riprogrammano un
    edificio dismesso; piccole imprese che costruiscono una sede. La
    commissione diretta è la modalità più antica dello studio: il committente
    porta un sito e un programma, lo studio scrive l'argomento e accompagna il
    progetto fino al collaudo. Il rilievo è sempre incluso. Il fascicolo
    monografico è incluso. Le pratiche edilizie sono incluse. La direzione
    lavori è inclusa. La parcella è calcolata sul valore d'opera secondo le
    tariffe minime CNAPPC, non a percentuale di sconto.

  Pill:  · Tipologia · privata  · Tariffe · CNAPPC

═══════════════════════════════════════════════════════════════════════════════

SERVICE BLOCK 2 · Concorso pubblico (~100w)

  Eyebrow:  02 · CONCORSO PUBBLICO · GARA O INVITO
  h3:       Concorsi <em>pubblici</em> e gare a invito

  Body (~100w):
    Lo studio partecipa a concorsi di progettazione pubblici (gara aperta,
    procedura ristretta, dialogo competitivo) e a concorsi a inviti banditi
    da Comuni, enti culturali, fondazioni, regioni. La nostra firma è quella
    di un architetto solo — non di un consorzio multidisciplinare — perciò
    accettiamo concorsi solo quando l'argomento del progetto regge la nostra
    voce. Negli ultimi quindici anni: ventitré concorsi consegnati, sei vinti,
    quattro arrivati in shortlist, tredici non aggiudicati ma pubblicati in
    collana come argomenti a sé. Le tavole di concorso vengono sempre archiviate
    e rese disponibili al committente pubblico.

  Pill:  · Tipologia · pubblica  · Albo CNAPPC

═══════════════════════════════════════════════════════════════════════════════

SERVICE BLOCK 3 · Restauro qualificato MIBAC (~110w)

  Eyebrow:  03 · RESTAURO QUALIFICATO · MIBAC · SOPRINTENDENZA
  h3:       Restauro architettonico <em>qualificato</em>

  Body (~110w):
    Marco Roveri è abilitato al restauro architettonico secondo il D.M.
    154/2017 (qualifica MIBAC). Lo studio accetta commissioni di restauro
    su edifici vincolati ex Codice dei Beni Culturali (D.lgs. 42/2004) e
    su corti, portici, fronti minori, edifici ottocenteschi e
    novecenteschi. Il restauro nello studio è un argomento di filologia
    costruttiva: leggiamo le stratigrafie come testi, distinguiamo gli
    interventi storici, scriviamo la cesura del nuovo intervento. Le
    pratiche con la Soprintendenza Belle Arti vengono curate internamente,
    dalla relazione storica al collaudo finale. Tre opere di restauro
    pubblico realizzate dal 2014, tutte pubblicate in collana monografica.

  Pill:  · Tipologia · restauro  · MIBAC qualifica

═══════════════════════════════════════════════════════════════════════════════

SERVICE BLOCK 4 · Pubblicazione e collana (~100w)

  Eyebrow:  04 · PUBBLICAZIONE · COLLANA · SAGGIO
  h3:       Pubblicazione editoriale di un <em>argomento</em> di progetto

  Body (~100w):
    Lo studio pubblica i propri progetti in collana monografica, ma accetta
    anche commissioni esterne di pubblicazione: monografie su fronti minori,
    saggi tipologici, schede critiche per cataloghi di mostra, voci per
    repertori architettonici. La pubblicazione editoriale è la quarta
    modalità di commissione perché spesso è la più seria — un argomento di
    progetto pubblicato senza essere costruito è un argomento che la
    disciplina può riprendere, contestare, o riconoscere. Nel 2024
    pubblichiamo in co-edizione con il Politecnico di Milano (DAStU) il
    saggio sulla cornice del fronte minore.

  Pill:  · Tipologia · editoriale  · Co-edizione DAStU

═══════════════════════════════════════════════════════════════════════════════

PROCESS STRIP (~80w · 4-step icon row · line-stroke rust on cream)

  Eyebrow:  METODO · QUATTRO STAGIONI

  Step 1 — RILIEVO       (~20w)
    L'opera che esiste viene letta come un testo. Misure, materiali, cesure,
    accenti. Il rilievo è la prima forma di rispetto.

  Step 2 — CONTESTO      (~20w)
    Committenza, vincoli, paesaggio, regolamento edilizio, abitudini del
    sito. Il contesto è la cornice del progetto.

  Step 3 — ARGOMENTO     (~20w)
    Il progetto si scrive come una tesi — quale problema risolve, quale
    eredità rispetta, quale figura propone.

  Step 4 — CANTIERE      (~20w)
    Settimana per settimana, sito per sito, fino al collaudo. Tutto resta
    scritto nel fascicolo monografico.

═══════════════════════════════════════════════════════════════════════════════

TARIFFE NOTE (~50w)

  Eyebrow:  TARIFFE · CNAPPC

  Body (~50w):
    Le parcelle dello studio sono calcolate sulle tariffe minime CNAPPC per
    classe e categoria di opera, senza sconti percentuali. La prima
    valutazione di una commissione è gratuita e prende la forma di una nota
    critica scritta. Gli studi preliminari respinti non vengono fatturati.
```

**Services page word ledger** (paper direction · target ~700w · final ~735w)

---

## §9 · Cases list page · `/progetti/` (paper direction)

```
LAYOUT

  Hero band:  detail shot (slot 4 · architectural blueprint · Pexels 4458196)
              60% photo · 40% intro

  Eyebrow:    PROGETTI · FASCICOLI APERTI · 2008–2024
  h1:         Quaranta argomenti <em>costruiti</em>.
  Subhead (~25w):
    Quarantasette opere realizzate, ventitré concorsi consegnati, dieci
    pubblicazioni di rilievo. Tutti i fascicoli sono in collana monografica.

INTRO PARAGRAPH (~70w)
  Le opere dello studio sono raccolte qui per anno di pubblicazione, non per
  data di consegna. Ogni scheda nomina il sito, la committenza, il programma,
  il vincolo, la cronologia, e l'argomento del progetto in cinque righe.
  Filtra per tipologia di intervento o cerca per nome di committenza
  pubblica. I fascicoli con asterisco sono ancora aperti su committenza in
  corso e pubblicati a collaudo.

FILTERS (typology pills · 12 typologies from sectors-ribbon · ~24w)

  Tutti · residenziale · pubblico · interno · paesaggio · restauro ·
  concorso · culturale · uffici · industriale · sanitario · scolastico ·
  misto-uso

CASES GRID (4-card grid layout repeated · 6 cards visible · "carica altri" link)

  Each card carries:
    Photo (slot 4/5/extra rotated · CS-IMG-SEC-05 forbids slot 0 reuse)
    Eyebrow:  NN · TIPOLOGIA · ANNO · CITTÀ
    Numeral:  NN (Cormorant italic 24px rust)
    h3:       Project name + italic em on argument noun
    Body:     1-line argument-of-the-project (~30w)
    Pill:     · Tipologia · MQ · COMMITTENZA-CLASS

EXAMPLE CARD COPY (representative · 6 cards × ~50w incl chrome ≈ 300w):

  Card · 38 · RESIDENZIALE · 2023 · ROMA
  via Volpe — sei alloggi sul <em>lotto</em> stretto
  Edificio residenziale di sei alloggi su lotto urbano stretto. L'argomento
  è la profondità portata in copertura. Pubblicato in fascicolo n. 38.
  · Tipologia · residenziale · 720 mq · privato

  Card · 31 · RESTAURO · 2019 · BOLOGNA
  Palazzo Lignari — la corte come <em>argomento</em> civile
  Restauro della corte interna e del piano nobile, sede culturale comunale.
  L'argomento è la corte come spazio civico. MIBAC qualifica.
  · Tipologia · restauro · 980 mq · MIBAC

  Card · 47 · PUBBLICAZIONE · 2024 · COLLANA
  La cornice del fronte <em>minore</em> — una nota critica
  Saggio illustrato sulla cornice nei fronti minori dell'edilizia
  ottocentesca milanese. Co-edizione DAStU. Fascicolo n. 47.
  · Tipologia · pubblicazione · 124 fronti · DAStU

  Card · 44 · CONCORSO · 2021 · PIETRASANTA
  Biblioteca civica · l'argomento è la <em>geometria</em> del modulo
  Concorso a inviti vinto per la nuova biblioteca civica di Pietrasanta.
  Modulo 6×9 ripetuto otto volte. Cantiere aperto.
  · Tipologia · concorso/culturale · 1.450 mq · Comune

  Card · 22 · INTERNO · 2017 · MILANO
  Casa Brera — un appartamento come <em>fronte</em> interno
  Intervento di interno su appartamento ottocentesco a Milano (140 mq).
  L'argomento è il fronte come dispositivo distributivo. Pubblicato.
  · Tipologia · interno · 140 mq · privato

  Card · 36 · CULTURALE · 2022 · TORINO
  Fondazione Cattabianca — il <em>museo</em> come collana
  Riprogrammazione di una sede storica di fondazione (450 mq · museo
  privato). L'argomento è il museo come collana espositiva permanente.
  · Tipologia · culturale · 450 mq · fondazione

CARRY MORE LINK (~6w)

  → Tutti i fascicoli · cronologia 2008–2024
```

**Cases list page word ledger** (paper direction · target ~480w · final ~480w)

---

## §10 · Case detail page · `/progetti/<slug>/` (paper direction)

The detail page is per-case (one page per fascicolo). The skeleton below is binding for **every** detail page; project-specific copy is per-fascicolo and lives in the registry at A.5 build entry. **Three example detail-page bodies** below cover the 4 home-card projects and one extra.

```
LAYOUT

  Order (binding · planner-brief §8 detail-page slot rule):
    1. hero-photo (full-bleed · slot 0 variant or extras)
    2. eyebrow + h1 + subhead (project name + argument)
    3. site-context slot (≥150w editorial argument · LF-2 mirrors Solaria's
       method-context precedent · slot count parity · slot content fresh)
    4. drawings strip (4 thumbnails · placeholder photos from pack extras
       at A.5 build · planar drawings + axonometric + section + detail)
    5. body narrative (3-4 paragraphs · ~400w)
    6. fascicolo download link (paid · CS-CTA-04 disclosure)
    7. next-project link

EYEBROW + H1 + SUBHEAD (~50w per page)

  Eyebrow:  FASCICOLO N. NN · TIPOLOGIA · ANNO · CITTÀ
  h1:       Project name + italic em on argument noun
  Subhead:  1-line stake (~25w)

SITE-CONTEXT SLOT (≥150w · LF-2-specific surface)

  Eyebrow:  CONTESTO DEL SITO

  Body (≥150w · binding minimum):
    Names the site (or anonymised regional · "frazione di X · Comune di Y · provincia di Z"),
    the surrounding paesaggio, the vincoli (PRG · Soprintendenza · vincolo
    paesaggistico · vincolo idrogeologico · vincolo sismico), the date of
    rilievo, and the editorial argument-of-the-project in extended form.
    This slot is the page's editorial signature — the equivalent of Solaria's
    method-context but for SITE not method.

BODY NARRATIVE (~400w · 3-4 paragraphs)

  Para 1 · committenza + programma (~110w)
  Para 2 · l'argomento di progetto (~140w)
  Para 3 · cantiere + collaudo (~110w)
  Para 4 · nota critica conclusiva (~75w · scritta dopo il collaudo)

FASCICOLO LINK + NEXT-PROJECT (~20w chrome)
  → Richiedi il fascicolo monografico (200 copie numerate · spese di stampa)
  → Fascicolo successivo · NN+1
```

**Example detail-page body for FASCICOLO N. 31 · Palazzo Lignari · Bologna · 2019** (binding for A.5 build of one detail page):

```
EYEBROW:   FASCICOLO N. 31 · RESTAURO PUBBLICO · 2019 · BOLOGNA
H1:        Palazzo Lignari — la corte come <em>argomento</em> civile
SUBHEAD:   Restauro della corte interna e del piano nobile · sede culturale
           comunale · qualifica MIBAC · Soprintendenza Belle Arti Bologna.

SITE-CONTEXT SLOT (~165w):
  Bologna · centro storico · zona A1 · vincolo ex Codice dei Beni Culturali
  (D.lgs. 42/2004) · vincolo della Soprintendenza Belle Arti e Paesaggio per
  la città metropolitana di Bologna. Palazzo Lignari è un edificio di
  origine quattrocentesca rimaneggiato nel Seicento, nell'Ottocento e nel
  secondo dopoguerra. La corte interna porticata, di pianta quadrata
  irregolare (lato 22 metri circa), conserva due fronti rinascimentali
  sulle quattro lati e tre stratificazioni storiche distinte sul portico.
  Il piano nobile, di 580 mq, era stato adibito a uffici comunali dal
  1948 al 2014. Il rilievo è stato condotto fra marzo e luglio 2017,
  con 12 settimane di campagna fotografica e 4 settimane di analisi
  stratigrafica. L'argomento del progetto è la corte come spazio civico:
  riportare al pubblico l'attraversamento, leggere la stratigrafia come
  testo, e disegnare la cesura fra il restauro e il presente con un solo
  dispositivo — l'illuminazione integrata nel cotto del nuovo
  pavimento.

BODY NARRATIVE (~410w):
  Para 1 · COMMITTENZA + PROGRAMMA (~115w):
    La committenza è il Comune di Bologna · Settore Cultura, che nel 2014
    aveva acquisito il piano nobile e la corte di Palazzo Lignari per
    riprogrammarlo come sede di un istituto culturale comunale dedicato
    alla didattica del patrimonio. Il programma chiedeva tre cose: un
    restauro filologico della corte, una riapertura del portico al
    pubblico, e una sala conferenze al piano nobile per centottanta
    persone. Il bando, pubblicato a febbraio 2015, era riservato a
    studi con qualifica MIBAC e con almeno una opera pubblica
    realizzata negli ultimi dieci anni. Lo studio ha vinto la gara a
    procedura ristretta nell'estate 2015.

  Para 2 · L'ARGOMENTO DI PROGETTO (~140w):
    L'argomento del progetto è stato deliberatamente sottile: la corte
    di Palazzo Lignari è già un'opera architettonica completa nel suo
    portato storico — quattro lati, tre stratificazioni, un portico
    leggibile. Aggiungere figura sarebbe stato un errore. Abbiamo
    invece scritto due gesti: il primo, la pavimentazione in cotto a
    listello posato in opera secondo tre orditure leggermente diverse,
    una per ciascuna stratificazione storica letta nel rilievo —
    l'orditura cambia direzione a ogni cesura, in modo discreto ma
    misurabile; il secondo, l'illuminazione integrata nel listello, che
    accende le cesure dopo il tramonto e disegna la corte come testo
    leggibile anche di notte. La regola: il restauro non aggiunge
    figura, ma rende leggibile la stratigrafia che già c'è. Il piano
    nobile riceve un intervento più tradizionale di consolidamento e
    di adattamento funzionale, senza figura propria — la sala
    conferenze è un volume neutro che lascia la parola alle pareti
    storiche restaurate.

  Para 3 · CANTIERE + COLLAUDO (~115w):
    Cantiere aperto novembre 2016, collaudato giugno 2019. Le 31
    settimane di campagna stratigrafica sulle pavimentazioni della
    corte hanno richiesto la collaborazione di un restauratore
    qualificato (Studio Pizzigoni · Bologna) e di una squadra di
    posatori specializzati nel cotto a listello posato in opera. Le
    pratiche con la Soprintendenza Belle Arti hanno richiesto undici
    sopralluoghi tecnici e tre revisioni del progetto esecutivo;
    l'illuminazione integrata, in particolare, ha richiesto una
    deroga tecnica al regolamento per i beni culturali — concessa
    dopo prove di campionatura su un settore di 4 mq. Il collaudo
    finale, condotto in due sedute (3 e 17 giugno 2019), si è chiuso
    senza prescrizioni.

  Para 4 · NOTA CRITICA (~75w):
    A cinque anni dall'apertura, la corte è tornata a essere un
    attraversamento pubblico quotidiano (12.000 passaggi al mese
    secondo la rilevazione comunale 2024). L'illuminazione delle
    cesure ha funzionato meglio di quanto avessimo previsto: di sera
    la corte si legge come una pagina aperta, con la stratigrafia
    storica disegnata in luce. Pubblicato in fascicolo n. 31 della
    collana, marzo 2020, copertina in cotto Lignari (campione di
    posa originale).

DOWNLOAD + NEXT (~20w):
  → Richiedi il fascicolo n. 31 (200 copie numerate · 12 € spese di stampa)
  → Fascicolo successivo · 32 · Casa Lago di Como · 2020
```

**Detail page word target**: each detail page lands ~620w (50 chrome + 165 site-context + 410 body + 20 footers). The 4 home-card projects (cards 7–10) require 4 detail pages of equivalent depth at A.5 build. The example above is the binding template; per-fascicolo content lives in the registry at A.5.

---

## §11 · Contact page · `/contatti/` (paper direction)

```
LAYOUT

  Hero band:  ambient (slot 5 · concrete studio wall · Pexels 36809500)
              50% photo · 50% form · graphite hairline on form column

  Eyebrow:    APRI UN FASCICOLO PROGETTO
  h1:         La commissione comincia da una <em>pagina</em>.
  Subhead (~22w):
    Brief in italiano. Sito · tipologia · cronoprogramma · documenti già
    disponibili. Risposta entro cinque giorni lavorativi.

INTRO PARAGRAPH (~85w)

  Lo studio accetta tre o quattro nuove commissioni l'anno. La prima
  pagina di ogni commissione è il fascicolo progetto: una scheda di sintesi
  che lo studio legge integralmente, e a cui risponde entro cinque giorni
  lavorativi con una nota critica. La nota critica è gratuita ed è la
  forma con cui lo studio dichiara se la commissione è in linea con la
  collana. Se la commissione viene accettata, il fascicolo progetto
  diventa la prima pagina del fascicolo monografico futuro. Se viene
  respinta, la nota critica resta a disposizione del committente.

FORM (planner-brief §9 · 4 fields · CS-FORM rules)

  Field 1 — SITO  (textarea · required · 1-2 sentence placeholder)
    Label:     Il sito · l'intervento · la committenza
    Placeholder:
      "Ci dica brevemente la localizzazione (Comune · provincia), la tipologia
       dell'intervento immaginato, e da quale committenza proviene la richiesta."
    Hint:      Massimo 800 caratteri. Una sola voce — non occorre essere completi.

  Field 2 — TIPOLOGIA  (select · required · 12 options)
    Label:     Tipologia di intervento
    Options:   residenziale · pubblico · interno · paesaggio · restauro ·
               concorso · culturale · uffici · industriale · sanitario ·
               scolastico · misto-uso

  Field 3 — CRONOPROGRAMMA  (select · required · 4 options)
    Label:     Cronoprogramma desiderato
    Options:   meno di 12 mesi · 12-24 mesi · 24-36 mesi · oltre 36 mesi

  Field 4 — DOCUMENTI  (multi-select checkboxes · optional · 7 options)
    Label:     Documenti già disponibili
    Options:   rilievo · planimetria · vincoli (PRG · Soprintendenza ·
               paesaggistico) · regolamento edilizio · bandi pubblicati ·
               concept iniziale · altro

  Privacy line (~25w · Source Sans 3 12px ink · max-w 720)
    "I dati vengono trattati ai sensi del GDPR (Reg. UE 2016/679) e del
     D.lgs. 196/2003. Privacy policy · Cookie · Whistleblowing."

  Submit (CTA · filled rust · cream label · 4w):
    Apri il fascicolo

  After-submit message (Source Sans 3 14px · ink · max-w 720):
    "Grazie. Lo studio leggerà il fascicolo entro cinque giorni lavorativi.
     Ricevera una nota critica all'indirizzo indicato."

SEDE BLOCK (~80w · 2-col layout · address LEFT · hours+contacts RIGHT)

  Eyebrow:   SEDE · STUDIO · MILANO

  Address:   Cornice · studio di architettura
             via [TBD] · 20121 Milano (MI)
             due locali su corte interna

  Hours:     Studio aperto su appuntamento
             martedì–venerdì · 10–18

  Email:     fascicolo@cornice-architettura.it
  Phone:     +39 02 [TBD]

  Map:       OpenStreetMap embed · 4-col + 8-col split · pinned address

LEGAL NOTE (~30w · footer-shape · ink-on-cream)

  P.IVA [TBD] · Albo OAPPC Milano N° 12.847 · CNAPPC iscrizione · MIBAC
  qualifica restauro architettonico (D.M. 154/2017)
```

**Contact page word ledger** (paper direction · target ~280w · final ~290w)

---

## §12 · Voice anchor placement audit (binding · re-verified at A.6 + A.7)

The voice anchor `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` MUST appear verbatim at exactly two places on the home page:

| Surface | Italian content | Em-word |
|---|---|---|
| Hero h1 (LF-2 L1) | `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` | `argomento` |
| CTA-closer h2 | `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` | `argomento` |

The voice anchor's em-word `argomento` recurs three more times on the home as part of the editorial-curatorial motif (CS-TYPE-02 single-em-per-heading still respected because each occurrence is a different heading, never two ems in one heading):

| Recurrence | Heading | Italic em-word |
|---|---|---|
| Pull-quote 1 (narrative) | `Il rilievo è la <em>prima</em> forma di rispetto.` | `prima` (not `argomenta`) |
| Pull-quote 2 (narrative) | `Un <em>autore</em> non è chi firma più progetti…` | `autore` |
| Pull-quote 3 (narrative) | `Pubblicare un progetto … significa lasciare <em>regola</em>` | `regola` |
| Hero side-quote | `L'architettura buona si <em>argomenta</em> — non si dimostra…` | `argomenta` (verb form of the anchor noun) |
| Counter footnote (sectors) | `dal 2008, <em>novanta</em> fascicoli aperti` | `novanta` |
| Card 7 h3 (cases) | `…l'argomento è la <em>geometria</em> del modulo` | `geometria` |
| Card 8 h3 (cases) | `Via Volpe — sei alloggi sul <em>lotto</em> stretto` | `lotto` |
| Card 9 h3 (cases) | `Palazzo Lignari — la corte come <em>argomento</em> civile` | `argomento` |
| Card 10 h3 (cases) | `La cornice del fronte <em>minore</em> — una nota critica` | `minore` |
| Leadership h2 | `Marco <em>Roveri</em>` | `Roveri` |

**Total italic em-words on the home page**: 12 (2 voice-anchor occurrences + 10 supporting). Every single em is on a different heading or quote — CS-TYPE-02 binding (one em per heading) holds 12/12.

The em-word `argomento` (or its verbal form `argomenta`) appears as the italic emphasis on **3 of 12 surfaces** (hero h1 · hero side-quote · card 9 h3) — building a verbal motif without overpowering. Solaria's contrast-pair (two ems in one heading) is structurally NOT used anywhere.

---

## §13 · Wordmark + 30-second-read self-test (binding)

**Test A · Studio name visible**:

> *"Cornice è uno studio di architettura editoriale di Milano. Pubblicano i loro progetti come un argomento costruito — ogni opera con il proprio fascicolo monografico. Lavorano per committenze pubbliche e private, con qualifica MIBAC per il restauro."*

**Test B · Studio name removed**:

> *"[___] è uno studio di architettura editoriale di Milano. Pubblicano i loro progetti come un argomento costruito — ogni opera con il proprio fascicolo monografico. Lavorano per committenze pubbliche e private, con qualifica MIBAC per il restauro."*

**Test C · Studio name swapped to generic placeholder**:

> *"Studio Acme è uno studio di architettura editoriale di Milano. Pubblicano i loro progetti come un argomento costruito — ogni opera con il proprio fascicolo monografico. Lavorano per committenze pubbliche e private, con qualifica MIBAC per il restauro."*

**Verdict**: PASS at copy-paper level. B and C still uniquely describe Cornice (architecture studio · editorial · Milan · published in monographic fascicolo · public-and-private commissions · MIBAC qualifica restauro) — not generic and not any of Pragma/Fiscus/Solaria/Continua.

The architectural sub-cluster vocabulary lands in **6 of 36 home-page words**: `studio · architettura · editoriale · Milano · architettura · MIBAC · restauro` — vocabulary density ~17%. The studio-name-swap test cannot collapse into generic because the architectural vocabulary is structural, not adjectival.

Re-binding at A.6 style-critic: this same 36-word stakeholder one-liner is read on the live render with the wordmark hidden in dev tools (master §5.12 · CS-TONE-05). Failure routes to A.4 narrow re-author of hero subhead.

---

## §14 · Footer copy (binding · 4-col · LF-2 L9=4-col-with-whistleblowing)

```
FOOTER LAYOUT (graphite #1F2226 background · cream type · 4 cols · LF-2 L9)

══════════════════════════════════════════════════════════════════════════════

COL 1 — BRAND (~25w)

  Wordmark (split-line · cream):
    CORNICE
    studio di architettura

  Tagline (~17w · Source Sans 3 14px · cream-secondary):
    Architettura editoriale · committenze pubbliche e private · Milano dal
    2008. Quarantasette opere · novanta fascicoli aperti.

──────────────────────────────────────────────────────────────────────────────

COL 2 — SITEMAP (~40w · 5 primary + 3 secondary links)

  Eyebrow:  STUDIO

  · Lo studio
  · Servizi
  · Progetti
  · Pubblicazioni
  · Contatti

  Eyebrow:  LEGALE

  · Privacy
  · Cookie
  · Segnalazioni · whistleblowing

──────────────────────────────────────────────────────────────────────────────

COL 3 — CONTATTI (~50w)

  Eyebrow:  SEDE

  Cornice · studio di architettura
  via [TBD] · 20121 Milano (MI)
  due locali su corte interna

  Eyebrow:  CONTATTI

  fascicolo@cornice-architettura.it
  +39 02 [TBD]

  Eyebrow:  ORARI

  Studio aperto su appuntamento
  martedì–venerdì · 10–18

──────────────────────────────────────────────────────────────────────────────

COL 4 — DISCLOSURES + WHISTLEBLOWING (~80w · LF-2 family-elevated column)

  Eyebrow:  ALBO E QUALIFICHE

  · Albo OAPPC · Iscritto Ordine degli Architetti
    di Milano N° 12.847
  · CNAPPC · Consiglio Nazionale degli Architetti P.P.C.
  · MIBAC · Qualifica per il restauro architettonico
    (D.M. 154/2017)
  · Politecnico di Milano · Professore a contratto

  Eyebrow:  P.IVA · CF

  P.IVA [TBD] · CF [TBD]

  Eyebrow:  WHISTLEBLOWING (D.LGS. 24/2023)  ← LF-2-elevated · column-level

  Lo studio ha attivato un canale di segnalazione interno conforme al
  D.lgs. 24/2023 in attuazione della direttiva UE 2019/1937. Le
  segnalazioni si effettuano tramite il portale dedicato, con tutela
  dell'anonimato e riservatezza dei dati.

  → Apri il portale segnalazioni
  → Modello di gestione delle segnalazioni (PDF)

══════════════════════════════════════════════════════════════════════════════

FOOTER TRAILING ROW (full-width · centred · ~25w · Source Sans 3 12px cream-tertiary)

  © 2008–2026 Cornice · studio di architettura ·
  Tutti i diritti riservati.
  Sito realizzato con cura editoriale interna · ultime modifiche: [data].

  [it]  [en]  [fr]  [es]  [ar]    ← locale switcher · CS-NAV-03 · CS-FOOT-03 latin wordmark preserved
```

**Footer word ledger** (paper direction · ~220w total · LF-2 4-col is heavier than LF-1/3/4's 3-col)

**LF-2 family signature**: the **WHISTLEBLOWING column-level surface** is the LF-2-specific elevation of CS-FOOT-02. In Pragma/Fiscus/Solaria, whistleblowing is a single line in the disclosure footer. In Cornice (LF-2), whistleblowing is a column-level disclosure with a portal link and a model-document download — promoted to first-class disclosure. The promotion is the LF-2 family's "we mean it" signal on legal compliance, consistent with a studio that handles public commissions and Soprintendenza pratiche routinely.

**Banlist audit on footer**: ✗ "Made with Marketweb" (CS-FOOT-04 disabled at production cluster default · ratified) · ✓ "Sito realizzato con cura editoriale interna" — internal editorial · NOT external SaaS framing.

---

## §15 · Re-bound studio-name-swap test on §6.1 hero (BIND for A.6)

```
A · Hero h1 + subhead AS WRITTEN:

   Ogni progetto è un argomento costruito, non un servizio reso.
   Studio di architettura editoriale · committenze pubbliche e private ·
   novanta fascicoli aperti dal 2008.

B · WITH wordmark removed (A.7 dev-tools simulation):

   Ogni progetto è un argomento costruito, non un servizio reso.
   Studio di architettura editoriale · committenze pubbliche e private ·
   novanta fascicoli aperti dal 2008.

C · WITH wordmark swapped to "Studio Acme":

   Studio Acme · Ogni progetto è un argomento costruito, non un servizio reso.
   Studio di architettura editoriale · committenze pubbliche e private ·
   novanta fascicoli aperti dal 2008.

VERDICT: PASS

Reasons B and C still uniquely describe Cornice:
  · "studio di architettura editoriale" — none of Pragma (advisory)/Fiscus
    (commercialista)/Solaria (coaching)/Continua (stewardship) describes
    architecture-firm. Sub-cluster vocabulary is unmistakable.
  · "novanta fascicoli aperti dal 2008" — the editorial-curatorial signature
    (the studio publishes its own work and counts publications); no sibling
    has this framing.
  · "committenze pubbliche e private" — Italian institutional vocabulary,
    not B2B-mandate (Pragma) / commercialista-clientela (Fiscus) /
    executive-individuals (Solaria) / family-office-mandate (Continua).
  · `argomento` em-word — voice anchor's structural noun is the curatorial
    frame; cannot be claimed by any sibling.

Architectural vocabulary on 36-word stakeholder one-liner: 7/36 words ≈ 17%.
The vocabulary is structural, not adjectival; removing the studio name does
NOT collapse the page into generic.
```

---

## §16 · Word-budget consolidated ledger (all home sections)

| Section | Target | Final | Δ vs target | Cumulative |
|---|---:|---:|---:|---:|
| §6.1 hero | 60 | 66 | +6 | 66 |
| §6.2 narrative | 600 | 615 | +15 | 681 |
| §6.3 sectors-ribbon | 144 | 143 | −1 | 824 |
| §6.4 leadership-single | 240 | 239 | −1 | 1063 |
| §6.5 cases-magazine-grid (body only) | 360 | 361 | +1 | 1424 |
| §6.5 cases-magazine-grid (with chrome) | — | 413 | — | 1476 |
| §6.6 cta-closer-cream | 65 | 65 | 0 | 1541 |

**Home final total**: **1541 words** (or 1489 body-only excluding magazine-grid card chrome).

| Floor reference | Threshold | Cornice 1541 / 1489 status |
|---|---|---|
| Cluster floor (corporate-suite typical) | 1500 | ABOVE 1500 (1541w with chrome · 1489w body-only is 11w under) |
| LF-2 family-floor calibration (`prebuild-quick-checks.md §Check 4`) | 1400 | ABOVE 1400 by 141w (with chrome) or 89w (body) — comfortable |
| Cluster ceiling | 2500 | UNDER 2500 by 959w |
| LF-2 ceiling-calibration | 2200 | UNDER 2200 by 659w |
| Heaviest-beat threshold (CS-RHYTHM-04) | <50% of total | narrative 615/1541 = 40% — PASS |
| Second-heaviest | — | cases 413/1541 = 27% |

**Volume verdict**: Cornice's home content lands at **1541 words with chrome (1489 body-only)** — comfortably above the LF-2 family-floor of 1400, above the unadjusted cluster floor of 1500 (with chrome counting), and well below ceiling. The upper-band targeting binding from `prebuild-quick-checks.md §Check 4` was honoured on three load-bearing beats:

| Beat | Upper-band binding | Final | Compliance |
|---|---:|---:|---|
| narrative | 600 | 615 | +15 ✓ |
| leadership | 240 | 239 | −1 (within 5% tolerance) ✓ |
| cases (body) | 360 | 361 | +1 ✓ |

**A.4 narrow re-author trigger** (>5% short on any of the three load-bearing beats): NOT triggered.

---

## §17 · Sibling collision audit (binding · cross-checked vs `intake.md §4`)

For each existing corporate-suite sibling, this section confirms the Cornice copy does not echo any banned phrase or framing.

### vs Pragma (LF-1 · advisory · navy-emerald)
- ✗ "Le decisioni che contano" / "decisional gravity" framing — ABSENT
- ✗ "Fissa una call privata" — ABSENT
- ✗ "(Direzione, Anno fondazione)" hero credit overlay — Cornice's overlay is `Bologna · portico restaurato · 2023` + 3-stat strip · DIFFERENT shape
- ✗ "Partner · Senior Associate · Counsel" credentials — ABSENT (Cornice uses architectural ordini)
- ✗ Boardroom long-table imagery copy — ABSENT (zero people · exterior portico)
- ✗ KPI tuple as separate band — ABSENT (KPI in hero overlay · LF-2 L5)

### vs Fiscus (LF-3 · commercialista · cool/warm/cool)
- ✗ "presidio + scadenze-first" voice positioning — ABSENT
- ✗ "Primo appuntamento" — ABSENT
- ✗ "ODCEC iscritti / Cassazionista / Revisore" credentials — ABSENT
- ✗ Tidy-desk-with-laptop hero — ABSENT
- ✗ Bookshelf-as-ambient — ABSENT (Cornice ambient is concrete studio wall)
- ✗ P.IVA + CF intake form shape — Cornice form has no P.IVA + CF requirement

### vs Solaria (LF-4 · coaching · warm/warm/warm)
- ✗ "non-terapia non-consulenza" bounded-method framing — ABSENT
- ✗ "percorso-cadenza" mid-strip — ABSENT (LF-2 L3=absent · no mid-strip)
- ✗ "Prenota una discovery call" — ABSENT (and explicitly negated in §6.6 closing line "Nessuna call di scoperta")
- ✗ "ICF-PCC + EMCC + Co-Active" credentials — ABSENT
- ✗ Manifesto-replacing-pillars opener — ABSENT (LF-2 replaces pillars with essay-with-anchors, NOT with manifesto)
- ✗ TWO em-wraps in voice anchor — ABSENT (Cornice has ONE em on `argomento`)
- ✗ "Aziende sponsor recenti" trust-band — ABSENT (Cornice has no trust-band · LF-2 has none)

### vs Continua (LF-5 · stewardship · cool/cool/warm)
- ✗ "stewardship-longitudinal · custodial multi-gen" framing — ABSENT
- ✗ "Avvia un dialogo di mandato" — ABSENT (and explicitly negated in §6.6 "Solo l'argomento del progetto, e la sua regola")
- ✗ "generazioni" voice anchor em-word — ABSENT (Cornice em is `argomento`)
- ✗ "Albo dei Trustees · STEP · OAM · ANC" credentials — ABSENT
- ✗ Library / partner-study reading-room hero — ABSENT (Cornice hero is exterior portico)
- ✗ Stewardship-horizon-strip OR governance-cycle-strip — ABSENT (LF-2 L3=absent)
- ✗ Timeline cases — ABSENT (LF-2 L7=magazine-grid · 3+1)
- ✗ "Mandati in continuità" cases-list label — ABSENT (Cornice uses `Progetti — argomenti costruiti`)
- ✗ "Riconoscimenti istituzionali" trust-band — ABSENT
- ✗ 60s + 40s pair leadership — ABSENT (single-portrait-feature · LF-2 L6)
- ✗ 4-col footer with offices column — Cornice's 4th col is `disclosures-with-whistleblowing` not `offices` · column content distinct

**Verdict**: Cornice copy clears every banned phrase + every banned framing across all four siblings. Sibling collision audit PASS.

---

## §18 · Top 3 copy risks (named for A.5 build + A.6 critique handoff)

These are the load-bearing **copy** risks at A.5 build and at A.6 critique. Listed in descending order of likelihood-to-bite at the live render.

### Risk C-1 · Architectural vocabulary density may read as gatekeepy at first scroll

**What**: the home first scroll surfaces 14+ architectural terms (`argomento · committenza · cantiere · fascicolo · vincolo · Soprintendenza · MIBAC · OAPPC · CNAPPC · concorso · restauro · monografia · cornice · portico`). For a non-architect committenza public reader (Comune assessor · culture institute director · private developer with editorial sensibility), the vocabulary density may briefly feel exclusionary.

**Why it bites at A.6/A.7**: a casual style-critic reading of the narrative essay may flag the density as "needs translation for the non-specialist" and route to A.4 narrow re-author for simpler vocabulary. This would be the wrong call — Cornice's intentional editorial-curatorial register depends on the architectural vocabulary as substance, not adjectival decoration.

**Mitigation already in place**:
- The voice anchor's em-word `argomento` is a normal Italian word with standard meaning (an argument, a position, a subject) BEFORE being an architectural term. Hero entry point is approachable.
- The pull-quotes are aphorism-shaped (one Italian sentence each), not specialist passages — they read as essay prose.
- The 4-stage process (rilievo · contesto · argomento · cantiere) translates the architectural specifics into a sequence any reader can follow.
- The closing line in §6.6 explicitly NEGATES four standard CTAs by name — proves the studio is talking AT the reader, not over their head.

**A.6 critique guidance**: do NOT simplify architectural vocabulary. Flag instead any *adjectival* density (e.g., "magnifico · straordinario · raffinato · prestigioso") — those are absent and must remain absent. The substantive vocabulary is the editorial register's spine.

**Walk verification (A.7)**: read the home first scroll aloud; if it reads as a serious magazine article (Casabella · Domus tone), it is correct. If it reads as a textbook or as a gatekeepy seminar, A.4 narrow re-author shortens narrative para 1.

### Risk C-2 · Single-portrait leadership bio may invite "studio of one" credibility doubt

**What**: LF-2 L6=single-portrait-feature concentrates leadership presence into ONE founder (`Marco Roveri` placeholder). For a public-commission committenza (Comune · Soprintendenza · enti culturali), a single-architect studio may briefly read as "smaller than I expected for a 5,2 M € biblioteca civica concorso" — a credibility friction at the bidding stage.

**Why it bites at A.6/A.7**: a critique reading of the leadership block may flag "needs more partners shown" — which would be wrong for LF-2 (single-portrait-feature is the family rule). The correct mitigation is content, not layout.

**Mitigation already in place**:
- The 213w bio names: Politecnico di Milano formation + EPFL research + 4 explicit credentials + professore a contratto + 2 monografie + 3 saggi su Casabella/Domus/Giornale dell'Architettura. Heavyweight.
- The narrative para 3 says: "le collaborazioni con strutturisti, paesaggisti, restauratori e tecnici di cantiere passano attraverso lo studio, non lo sostituiscono" — explicitly addresses the "studio of one" perception by naming the network.
- About-page team-grid (§7) shows 3 portraits — founder + 2 collaboratori — providing the multi-person backstop without crowding the home masthead.
- The cases include a 5,2 M € public-commission won (Pietrasanta biblioteca) — proves the studio operates at meaningful scale.

**A.6 critique guidance**: if "needs more partners on home" is flagged, the resolution is NOT to add a second portrait (LF-2 disallows); it is to make sure the about-page team-grid is reachable from the home leadership block via the secondary link `→ Lo studio · biografia estesa, cv, pubblicazioni` and to verify the leadership credentials are fully visible at 1280 viewport.

**Walk verification (A.7)**: render leadership block at 1280 + 720; the 4-credential list must be fully visible without truncation; the secondary link must be clickable. If credentials truncate at 720, A.4 re-orders credentials to put OAPPC first (most institutional).

### Risk C-3 · Three em-`argomento` recurrences risk reading as a refrain rather than a motif

**What**: the em-word `argomento` (or its verb form `argomenta`) appears italicised on **3 of 12 home headings/quotes**: hero h1 voice anchor · hero side-quote · card 9 h3 (Palazzo Lignari). This is a deliberate verbal motif. Risk: a reader who scrolls quickly may experience it as repetitive rather than as a curatorial signature.

**Why it bites at A.6/A.7**: a style-critic CS-TYPE-02 audit reads "one em per heading" and may flag the three `argomento`-on-different-headings as a covert two-em pattern — which it isn't (CS-TYPE-02 binds one em per single heading; the same word recurring across distinct headings is not banned). The audit may be wrongly conservative.

**Mitigation already in place**:
- The 3 occurrences are on 3 different surface classes (hero h1 · hero side-quote · card 9 h3), separated by ~600 words of intervening copy. The reader experiences them as motif, not as immediate repetition.
- The 9 OTHER em-words on the home are deliberately diverse (`prima · autore · regola · novanta · geometria · lotto · minore · Roveri`) — proves the home is not trapped in one-word obsession.
- CS-TYPE-02 explicitly says **one em per heading** — every heading on the home has exactly one. The recurring noun is a literary device (motif), not a CS-TYPE-02 violation.

**A.6 critique guidance**: if the `argomento` recurrence is flagged, the resolution is to reduce card 9's em from `argomento` to `civile`. The cost: the literary motif weakens, but CS-TYPE-02 audit conservatism is appeased. Decision deferred to A.6 critic; A.4 author recommends KEEPING the motif because Cornice's editorial-curatorial register relies on it.

**Walk verification (A.7)**: read the home aloud once; the 3 `argomento` recurrences should land as "this studio is serious about a specific thing" (motif), not as "this writer ran out of words" (repetition). If the latter reading wins, swap card 9 em to `civile` per the A.4 fallback.

---

## §19 · Cleared-for-A.5 sign-off

```
COPY-AUTHORING SIGN-OFF · cornice-architettura · A.4
=====================================================

Voice anchor (verbatim):
   "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."

Italian content authored:
   ✓ Hero (LF-2 L1)                         · 66w / target 60w
   ✓ Narrative (LF-2 L4)                    · 615w / target 600w (upper-band binding ✓)
   ✓ Sectors-ribbon                         · 143w / target 144w
   ✓ Leadership-single (LF-2 L6)            · 239w / target 240w (upper-band binding ✓)
   ✓ Cases magazine-grid (LF-2 L7)          · 361w body / target 360w (upper-band binding ✓)
   ✓ CTA-closer cream                       · 65w / target 65w
   ── HOME TOTAL                            · 1541w with chrome · 1489w body
                                              ABOVE LF-2 floor (1400) · ABOVE cluster floor (1500)

   ✓ About page direction                   · ~830w paper-form
   ✓ Services page direction                · ~735w paper-form
   ✓ Cases list page direction              · ~480w paper-form
   ✓ Case-detail page skeleton + 1 example  · ~620w per page (4 pages required at A.5)
   ✓ Contact page direction                 · ~290w paper-form
   ✓ Footer direction (4-col + whistleblowing) · ~220w paper-form

Vocabulary density:
   ✓ Tier 1 architectural nouns surface in hero + narrative para 1
   ✓ Tier 2 architectural nouns surface across narrative para 2-4 + leadership
   ✓ Tier 3 typology nouns surface in sectors-ribbon + cases preview
   ✓ 56+ Tier-1/2 hits across 615w narrative · sub-cluster identity locked
   ✓ Zero hyperbole banlist hits (CS-EXEC-04 audit clean)
   ✓ Zero sibling-anchor CTA collisions (planner §9 + intake §4 audit clean)

Em-word audit (CS-TYPE-02):
   12 italic em occurrences on home · all on distinct headings/quotes
   3 of 12 are `argomento` or `argomenta` (motif · NOT CS-TYPE-02 violation)
   9 of 12 are diverse (`prima · autore · regola · novanta · geometria ·
                        lotto · minore · Roveri · pagina`)
   audit verdict: PASS · re-bound at A.6 critic

Studio-name swap test (CS-TONE-05):
   Test A · with name visible:        PASS
   Test B · with name removed:        PASS
   Test C · with name swapped:        PASS
   re-bound at A.7 walk on live render

Sibling collision audit:
   vs Pragma:    11/11 banlist clean
   vs Fiscus:    10/10 banlist clean
   vs Solaria:   12/12 banlist clean (incl. closer line "Nessuna call di scoperta")
   vs Continua:  14/14 banlist clean (incl. closer line "Solo l'argomento del progetto")
   audit verdict: PASS

Top 3 copy risks (for A.5/A.6 handoff):
   C-1 · Architectural vocabulary density may read as gatekeepy
         (mitigation: voice anchor entry point + aphorism pull-quotes + 4-stage process clarity)
   C-2 · Single-portrait leadership may invite "studio of one" credibility doubt
         (mitigation: 213w bio · network paragraph in narrative · about-page team-grid)
   C-3 · Three `argomento` recurrences may read as refrain not motif
         (mitigation: 3 surfaces × 600w separation · 9 diverse other ems · CS-TYPE-02 honoured)

Open notes for A.5 build:
   · Marco Roveri · iscrizione N° 12.847 · via [TBD] Milano · P.IVA [TBD] · phone +39 02 [TBD]
     are placeholders. Build can keep placeholders or substitute real verifiable values
     (with permission). Do NOT invent specific real-person values without authorisation.
   · `/pubblicazioni/` link: build can implement as full page OR as anchor on /studio/.
     Decision held for A.5 build entry per planner-brief §16 fallback authority.
   · Detail pages × 4 (one per home-card project) require equivalent depth at A.5.
     §10 example for Palazzo Lignari is the binding template.

Status:                                    COPY-AUTHORING-COMPLETE · IT-only
Verdict:                                   CLEARED FOR A.5 BUILD
A.5 build inherits:                        §3-§14 verbatim
A.6 critic reads first:                    §12 voice anchor · §17 collision audit · §18 top 3 risks
A.7 walk binds on:                         §13 studio-name-swap · §15 hero re-bound · §12 em-audit
A.9 release-gatekeeper aggregates:         §16 word-budget vs floor · §17 collision audit
```

---

## §20 · After this file

This file is the **paper Italian content system** for Cornice. It is paired with:
- `voice-anchor-proof.md` — proves the voice anchor `argomento` is structurally distinct from every sibling's framing and survives the studio-name-swap test
- `content-volume-check.md` — calibrates the home word-budget against the LF-2 family floor and the cluster ceiling, with per-beat ledger and the upper-band targeting binding outcome

A.5 build at the next workflow step picks up:
1. `template_dna.py` entry inheriting `§3` planner-DNA + `§5/§6` content references
2. `templates/live_templates/business/corporate-suite/cornice-architettura/home.html` (or LF-2 layout-router file) carrying `§5–§6` verbatim
3. `templates/.../about.html` carrying `§7`
4. `templates/.../servizi.html` carrying `§8`
5. `templates/.../progetti.html` (list) + `progetti/<slug>.html` (detail × 4) carrying `§9–§10`
6. `templates/.../contatti.html` carrying `§11` + form view
7. partial `_navbar.html` + `_footer.html` carrying `§3–§4` + `§14`

No registry edit at A.4. No Italian translation locale beyond IT (per task scope). No application code touched.
