# Cornice · Voice anchor proof · LF-2 · 5th corporate-suite sibling

```yaml
report_type:        voice-anchor-proof
template_slug:      cornice-architettura
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · cornice-architettura · A.4 copy authoring (paper-only · pre-code)
agent:              copy-author (post-A.3 imagery LGTM · pre-A.5 build)
date:               2026-04-30
inputs_consumed:
  - factory/reports/copy/cornice-architettura/copy-authoring.md (paired · §1 voice contract · §12 em-audit · §13 swap test)
  - factory/reports/corporate-suite/cornice-architettura/intake.md §3 §5 §9 (binding voice positioning + em-word + tone)
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md §3 §11 (DNA voice anchor + multilingual contract)
  - factory/reports/corporate-suite/cornice-architettura/prebuild-quick-checks.md §Check 5 (studio-name-swap canonical procedure)
  - apps/catalog/template_dna.py (Pragma · Fiscus · Solaria · Continua voice_anchor strings · for collision check)
  - factory/standards/corporate-suite-design-standard.md §11 (terminology lock) · CS-TYPE-02 (one em per heading)
  - factory/standards/corporate-suite-blocking-rules.md §3.4 (voice anchor banlist + structural rules)
outputs:
  - factory/reports/copy/cornice-architettura/voice-anchor-proof.md (this file · paired with copy-authoring + content-volume)
status_tag:         VOICE-ANCHOR-PROOF-COMPLETE · ready for A.5 build handoff (voice axis)
verdict:            ANCHOR LOCKED · sub-cluster identity unmistakable · banlist clean · swap test PASS · ready for build
next_action:        A.5 template-builder treats §1.1 as binding · A.6 style-critic re-runs §3 swap test on render ·
                    A.7 IT walk records §3 verdict on live DOM with wordmark hidden in dev tools (CS-TONE-05)
```

This file proves three things:
1. **The voice anchor is decision-locked, structurally distinct from every existing sibling's framing, and respects every CS-TYPE-02 / CS-EXEC-04 banlist rule.**
2. **The em-word `argomento` is the right curatorial-architectural noun, supports translation across IT/EN/FR/ES/AR, and survives Solaria's contrast-pair temptation.**
3. **The "remove the studio name" test passes at copy-paper level on the hero and on the stakeholder one-liner; the architectural sub-cluster vocabulary is structural, not adjectival, so removal does not collapse the page into generic.**

---

## §1 · The voice anchor (verbatim · binding)

### §1.1 · Italian (initial locale · binding for IT pass at workflow A)

```
Voice anchor:    Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.
Em-word:         argomento     (the curatorial-architectural NOUN — the project's KIND, not its action)
Em-count:        1             (CS-TYPE-02 default · NOT contrast-pair)
Word count:      11
Sentence count:  1
Negation form:   "non … reso"  (the anchor declares what the project IS by contrasting against
                                 what it is NOT — the active negation is the editorial signature)
```

### §1.2 · Cross-locale planning (workflow C contract · NOT in scope for IT pass)

```
EN:   "Every project is a built <em>argument</em>, not a service rendered."
FR:   "Chaque projet est un <em>argument</em> construit, pas un service rendu."
ES:   "Cada proyecto es un <em>argumento</em> construido, no un servicio prestado."
AR:   "كلّ مشروع <em>حُجَّةٌ</em> مَبنِيَّة، لا خدمة مُؤدَّاة."
      (italic substitute via Naskh-italic OR Kufi weight-shift — decision at C pre-flight per
       planner-brief §11 · IT pass does NOT depend on this resolved)

Translator binding (per planner-brief §11):
   - italic carries the curatorial-architectural NOUN (a project's KIND, not its action)
   - translators MUST italicise the equivalent of `argomento`
   - do NOT italicise the verb è / is / construit / built / construido / es / هو
   - the "non … reso" negation form must be preserved (or its locale equivalent)
   - drop-cap on narrative para 1 first letter is per-locale (L · G · L · C · ...)
```

The cross-locale plan is recorded here for completeness; the IT pass is the only authored locale at A.4 per the task scope. Workflow C handles the four additional locales after IT walk PASS.

### §1.3 · Side-quote anchor (paired with voice anchor on hero RIGHT 4-col)

```
Side-quote (IT):   L'architettura buona si <em>argomenta</em> — non si dimostra,
                    non si vende, non si decora.
Em-word:           argomenta  (verb form of the anchor noun · reinforces the motif at hero scale)
Em-count:          1          (CS-TYPE-02 default · NOT contrast-pair)
Negation triplet:  non si dimostra · non si vende · non si decora  — refuses three rival framings:
                       · si dimostra      → academic / scientific framing (refused)
                       · si vende         → commercial / SaaS framing (refused)
                       · si decora        → decorative / cosmetic framing (refused)
                   This triplet is the editorial-curatorial signature: architecture argues,
                   it does not prove, sell, or decorate.
```

The side-quote is **per-locale rewriteable** at A.4 copy-translation entry (workflow C) per planner-brief §11 — the constraint is that the rewrite must contain the locale's translation of `si argomenta` as the active verb. This freedom keeps the side-quote from breaking under translation while preserving the argument frame.

---

## §2 · Why `argomento` is the right em-word (binding rationale)

### §2.1 · Semantic register

`argomento` in Italian carries three layered meanings:
1. **Standard sense**: an argument · a position · a thesis (in rhetoric · in writing · in conversation)
2. **Editorial sense**: the subject of a piece of writing or publication ("l'argomento del fascicolo · l'argomento del numero")
3. **Architectural sense (specialist)**: the conceptual programme of a project · what the project ARGUES for in built form ("l'argomento del progetto")

The voice anchor's em-word lands all three meanings simultaneously. For a non-architect reader (Comune assessor · enti culturali director · privato con sensibilità editoriale), meaning 1 lands first — **Cornice projects are arguments**. For an architect reader (committenza pubblica · concorso jury · Soprintendenza), meaning 3 lands — **Cornice projects have an editorial-curatorial programme stated in advance**. Both readings are legitimate; the em-word does not over-specialise.

This layered semantics is **why `argomento` is the right em-word** — and why a flatter alternative would weaken the page:

| Alternative em-word | Why rejected |
|---|---|
| `progetto` | Too generic · already saturated on the page · would weaken not strengthen the anchor |
| `opera` | Closer but reads "art object" rather than "editorial argument" — drifts away from the curatorial-publication framing |
| `monografia` | Too specialist · loses meaning 1 entirely · only architects would understand on first read |
| `firma` | Reads "signature / authorship" — would tilt the studio toward star-architect framing, which Cornice explicitly avoids ("la nostra firma è quella di un architetto solo, non di un brand a più mani" — humble register) |
| `fabbrica` | Reads "building under construction" — too physical · misses the curatorial layer |
| `costruzione` | The participle `costruito` is already in the anchor; italicising it would emphasise the wrong half (the action) over the noun (the kind) |
| `tesi` | Too academic · would tilt the studio toward "atelier accademico" — a different sub-cluster entirely |

### §2.2 · CS-TYPE-02 audit

```
CS-TYPE-02 binding:
   Italic <em> on ONE load-bearing word per heading (CS-TYPE-02 default).
   Solaria's contrast-pair (TWO em-wraps in one heading) is a DEVIATION
   reserved for Solaria.

Cornice voice anchor: 1 em on `argomento` ✓
Cornice side-quote:    1 em on `argomenta` ✓
Cornice CTA-closer h2: 1 em on `argomento` (verbatim repeat) ✓
Cornice narrative pull-quotes: 1 em each on `prima · autore · regola` ✓
Cornice card 7-10 h3:  1 em each on `geometria · lotto · argomento · minore` ✓
Cornice leadership h2: 1 em on `Roveri` ✓
Cornice sectors counter footnote: 1 em on `novanta` ✓
Cornice contact page h1: 1 em on `pagina` ✓

Total italic em occurrences across IT home + chrome:  12
Em-per-heading max:                                    1
CS-TYPE-02 audit:                                      PASS (12/12)
```

### §2.3 · Solaria contrast-pair temptation explicitly avoided

Solaria's voice anchor uses TWO ems in one sentence (the contrast-pair: `non è X · è Y`). It is the only sibling allowed this pattern (D-098 family-level deviation reserved for the bounded-method coaching register).

Cornice's voice anchor `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` carries a NEGATION (`non un servizio reso`) but NOT a second `<em>` — the negated noun `servizio` is plain text, not italic. This is a deliberate restraint:

```
Solaria pattern (NOT used by Cornice):
   "Non è X. È <em>Y</em>." OR "Non <em>X</em>. <em>Y</em>."  — TWO em-wraps

Cornice pattern (used):
   "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."
                                                     ↑ negation in plain text
   ONE em-wrap. The contrast lives in the prose, not in the typography.
```

**Why the restraint is correct**: Cornice's editorial-curatorial register is austere · the studio publishes opere monografiche · the typography refuses ostentation. A second italic would push the heading toward Solaria's manifesto register — which is structurally NOT Cornice. The restraint is the cluster-distinctness signal at the typography layer.

### §2.4 · Hyperbole banlist audit (CS-EXEC-04)

```
CS-EXEC-04 banlist hits in voice anchor or side-quote:

   `trasforma`           ABSENT ✓
   `sblocca`             ABSENT ✓
   `rivoluziona`         ABSENT ✓
   `ridefinisce`         ABSENT ✓
   `disrupt`             ABSENT ✓
   `innovativo`          ABSENT ✓
   `all'avanguardia`     ABSENT ✓
   `cutting-edge`        ABSENT ✓
   `soluzioni su misura` ABSENT ✓
   `partner di fiducia`  ABSENT ✓
   Einstein quote        ABSENT ✓
   Steve Jobs quote      ABSENT ✓
   Le Corbusier misquote ABSENT ✓
   Frank Lloyd Wright misquote ABSENT ✓

Anchor banlist verdict: PASS (14/14 banned items absent)
```

Cornice's voice anchor uses **plain operational verbs** (`è · costruito · reso`) and **architectural-editorial nouns** (`progetto · argomento · servizio`). The most "elevated" word in the anchor is `argomento` — and that elevation is the load-bearing point of the anchor, not a decorative flourish.

---

## §3 · Studio-name-swap test (CS-TONE-05 · re-bound at A.6 + A.7)

Per `prebuild-quick-checks.md §Check 5` and CS-TONE-05, the voice anchor + first-scroll copy must still uniquely describe THIS template after the studio name is removed or replaced. This test re-runs at three points: paper authoring (here · A.4), style-critic (A.6), and live walk with wordmark hidden in dev tools (A.7).

### §3.1 · Test on the voice anchor in isolation

```
A · As written:
    "Ogni progetto è un argomento costruito, non un servizio reso."

B · With "Cornice" prepended (current layout context):
    "Cornice — Ogni progetto è un argomento costruito, non un servizio reso."

C · With "Cornice" removed and replaced by "Studio Acme":
    "Studio Acme — Ogni progetto è un argomento costruito, non un servizio reso."

D · With "Cornice" removed and replaced by "[___]":
    "[___] — Ogni progetto è un argomento costruito, non un servizio reso."

VERDICT: PASS

Reasons B and C and D still uniquely describe THIS template:
  - "argomento costruito" — the curatorial-architectural noun + participle pair is
    the structural framing. No sibling claims this. The pair survives any wordmark.
  - "non un servizio reso" — explicit refusal of service-vendor framing. Pragma
    sells advisory, Fiscus sells presidio, Solaria sells coaching, Continua sells
    custodia. All four are services. Cornice declares it is NOT.
  - Cannot describe Pragma (B2B advisory · sells decisions, not arguments)
  - Cannot describe Fiscus (commercialista · sells presidio + scadenze)
  - Cannot describe Solaria (coaching · sells percorso bounded-method)
  - Cannot describe Continua (stewardship · sells generations-of-mandate)

The voice anchor in isolation is sub-cluster-distinguishing. Architecture studios
are the only practitioners who deliberately frame their work as "arguments,
not services."
```

### §3.2 · Test on the 36-word stakeholder first-scroll one-liner

```
A · With wordmark visible:
    "Cornice è uno studio di architettura editoriale di Milano. Pubblicano i
     loro progetti come un argomento costruito — ogni opera con il proprio
     fascicolo monografico. Lavorano per committenze pubbliche e private,
     con qualifica MIBAC per il restauro."

B · With wordmark removed (A.7 dev-tools simulation):
    "[___] è uno studio di architettura editoriale di Milano. Pubblicano i
     loro progetti come un argomento costruito — ogni opera con il proprio
     fascicolo monografico. Lavorano per committenze pubbliche e private,
     con qualifica MIBAC per il restauro."

C · With wordmark swapped to "Studio Acme":
    "Studio Acme è uno studio di architettura editoriale di Milano. Pubblicano
     i loro progetti come un argomento costruito — ogni opera con il proprio
     fascicolo monografico. Lavorano per committenze pubbliche e private,
     con qualifica MIBAC per il restauro."

VERDICT: PASS

Reasons B and C still uniquely describe Cornice:
  · "studio di architettura editoriale" — architecture-firm sub-cluster.
    None of Pragma (advisory) · Fiscus (commercialista) · Solaria (coaching) ·
    Continua (stewardship) describes architecture. Sub-cluster vocabulary
    is structural, not adjectival.
  · "fascicolo monografico" — editorial-publication framing. The studio
    publishes its own work. None of the four siblings publishes its work
    as monographs.
  · "qualifica MIBAC per il restauro" — explicit Italian institutional
    qualification. Architecture-specific. No other sibling has MIBAC.
  · "committenze pubbliche e private" — Italian institutional vocabulary.
    Pragma uses "mandati B2B" not "committenze." Fiscus uses "clientela"
    not "committenze." Solaria uses "individui executive." Continua uses
    "famiglie patrimonialiste."

Architectural sub-cluster vocabulary on 36-word stakeholder one-liner:
   "studio · architettura · editoriale · Milano · architettura · MIBAC ·
    restauro" — 7 of 36 words ≈ 17% architectural.

The vocabulary is STRUCTURAL, not adjectival. Removing the wordmark does
NOT collapse the page into generic.
```

### §3.3 · Test re-binding at A.6 and A.7

```
A.6 style-critic binding:
   Re-run §3.1 + §3.2 tests on the rendered home page first-scroll copy.
   Specifically verify the architectural sub-cluster vocabulary lands in:
      - h1 voice anchor (Italian word `progetto` ✓)
      - subhead (Italian words `architettura · editoriale · committenze ·
                                fascicoli` ✓)
      - sectors-ribbon (Italian words `intervento · tipologia` ✓)
      - leadership credentials (Italian acronyms `OAPPC · CNAPPC · MIBAC` ✓)
   If any of the four surfaces fails to surface its tier vocabulary, copy
   returns to A.4 narrow re-author of THAT surface.

A.7 IT browser walk binding:
   Use Chrome dev-tools to set `display: none` on the wordmark element.
   Read the home first-scroll aloud.
   The page should still uniquely describe an Italian architecture studio
   that publishes its work as monographic fascicoli.
   If the page reads as generic creative practice, or as any of Pragma /
   Fiscus / Solaria / Continua, A.7 routes to A.8 narrow copy-fix on the
   first-scroll surfaces (hero subhead + narrative para 1 first sentence).

A.9 release-gatekeeper aggregate:
   Includes the §3.1 + §3.2 test re-runs in the release-readiness audit
   before flipping tier=draft → tier=published_live. Failure delays flip,
   does not block walk PASS.
```

---

## §4 · Sibling voice anchor distinctness (cross-check vs apps/catalog/template_dna.py)

The four existing siblings carry voice anchors structurally distinct from Cornice's. This section cross-references each.

### §4.1 · vs Pragma (LF-1 · advisory · navy/cool/cool/cool)

```
Pragma framing (intake §3 + apps/catalog/template_dna.py):
  voice positioning:    decisional-gravity · institutional advisory
  framing noun class:   decisione · mandato · presidio · responsabilità
  CTA:                  "Fissa una call privata"
  conversion pattern:   advisory-mandate-call

Cornice framing (this file §1.1):
  voice positioning:    editorial-curatorial · architectural-discipline
  framing noun class:   argomento · progetto · opera · cantiere · fascicolo
  CTA:                  "Apri un fascicolo progetto"
  conversion pattern:   project-dossier-submission

Distinctness on voice axis:
  · stance differs:      decisional-gravity vs editorial-curatorial → DIFFER
  · noun class differs:  decisione vs argomento → DIFFER
  · CTA verb differs:    "fissa" (schedule) vs "apri" (open · publish) → DIFFER
  · conversion differs:  call vs dossier-submission → DIFFER

  4-axis distinctness vs Pragma: 4/4 → PASS (≥4/5 gate)
```

### §4.2 · vs Fiscus (LF-3 · commercialista · cool/warm/cool)

```
Fiscus framing (intake §3 + apps/catalog/template_dna.py):
  voice positioning:    presidio + scadenze-first · institutional-fiscal
  framing noun class:   scadenza · presidio · adempimento · regime
  CTA:                  "Primo appuntamento"
  conversion pattern:   appuntamento-scheduled

Cornice framing:
  voice positioning:    editorial-curatorial · architectural-discipline
  framing noun class:   argomento · progetto · opera · cantiere · fascicolo
  CTA:                  "Apri un fascicolo progetto"
  conversion pattern:   project-dossier-submission

Distinctness on voice axis:
  · stance differs:      presidio-scadenze vs editorial-curatorial → DIFFER
  · noun class differs:  scadenza vs argomento → DIFFER
  · CTA verb differs:    "primo" (first appointment) vs "apri" (open dossier) → DIFFER
  · conversion differs:  appointment vs dossier-submission → DIFFER

  4-axis distinctness vs Fiscus: 4/4 → PASS
```

### §4.3 · vs Solaria (LF-4 · coaching · warm/warm/warm)

```
Solaria framing (intake §3 + apps/catalog/template_dna.py · `bounded executive coaching`):
  voice positioning:    bounded-method · "non terapia, non consulenza"
  framing noun class:   percorso · cadenza · ritmo · individuo
  CTA:                  "Prenota una discovery call"
  conversion pattern:   discovery-call
  em pattern:           CONTRAST-PAIR (TWO em-wraps in voice anchor — Solaria's reservation)

Cornice framing:
  voice positioning:    editorial-curatorial · architectural-discipline
  framing noun class:   argomento · progetto · opera · cantiere · fascicolo
  CTA:                  "Apri un fascicolo progetto"
  conversion pattern:   project-dossier-submission
  em pattern:           SINGLE em (Cornice respects CS-TYPE-02 default · NOT contrast-pair)

Distinctness on voice axis:
  · stance differs:      bounded-method vs editorial-curatorial → DIFFER
  · noun class differs:  percorso vs argomento → DIFFER
  · CTA verb differs:    "prenota" (book discovery) vs "apri" (open dossier) → DIFFER
  · conversion differs:  discovery-call vs dossier-submission → DIFFER
  · em pattern differs:  contrast-pair vs single em → DIFFER

  5-axis distinctness vs Solaria: 5/5 → PASS

Cornice closing line (§6.6 of copy-authoring) explicitly NEGATES Solaria's framing:
   "Nessuna call di scoperta. Nessun preventivo a consumo."
   → "Nessuna call di scoperta" refuses Solaria's discovery-call convention by name.
```

### §4.4 · vs Continua (LF-5 · stewardship · cool/cool/warm)

```
Continua framing (intake §3 + apps/catalog/template_dna.py · stewardship-grade family office):
  voice positioning:    stewardship-longitudinal · custodial multi-gen
  framing noun class:   generazioni · custodia · mandato · continuità
  voice anchor em-word: `generazioni` (the longitudinal-temporal noun)
  CTA:                  "Avvia un dialogo di mandato"
  conversion pattern:   mandate-dialogue

Cornice framing:
  voice positioning:    editorial-curatorial · architectural-discipline
  framing noun class:   argomento · progetto · opera · cantiere · fascicolo
  voice anchor em-word: `argomento` (the curatorial-publication noun)
  CTA:                  "Apri un fascicolo progetto"
  conversion pattern:   project-dossier-submission

Distinctness on voice axis:
  · stance differs:      stewardship-longitudinal vs editorial-curatorial → DIFFER
  · noun class differs:  generazioni vs argomento → DIFFER
  · em-word differs:     temporal-longitudinal vs curatorial-publication → DIFFER (orthogonal axes)
  · CTA verb differs:    "avvia" (initiate dialogue) vs "apri" (open dossier) → DIFFER
  · conversion differs:  dialogue vs dossier-submission → DIFFER

  5-axis distinctness vs Continua: 5/5 → PASS

Cornice closing line (§6.6 of copy-authoring) explicitly NEGATES Continua's framing:
   "Solo l'argomento del progetto, e la sua regola."
   → No "dialogo di mandato" framing · architectural argument is per-project,
     NOT per-mandate-across-decades. Single-commission framing refused
     stewardship-longitudinal framing without naming Continua.
```

### §4.5 · Aggregate sibling distinctness on voice axis

```
                      Pragma     Fiscus     Solaria     Continua
stance               4/4 ✓      4/4 ✓      5/5 ✓       5/5 ✓
noun class           ✓          ✓          ✓           ✓
CTA verb             ✓          ✓          ✓           ✓
conversion           ✓          ✓          ✓           ✓
em pattern           N/A        N/A        ✓ (key)     N/A

DISTINCTNESS GATE: ≥4/5 → all 4 siblings PASS

The voice axis is the safest axis in the Cornice DNA — sub-cluster vocabulary
+ negation pattern + dossier-CTA together make the architectural-firm
identity unmistakable.
```

---

## §5 · Em-word audit on the full home (12-occurrence ledger · CS-TYPE-02)

| # | Surface | Heading or quote | Em-word | Function |
|---|---|---|---|---|
| 1 | Hero h1 (LF-2 L1) | `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` | `argomento` | curatorial-noun · voice anchor |
| 2 | Hero side-quote (LF-2 L1 · 4-col) | `L'architettura buona si <em>argomenta</em> — non si dimostra, non si vende, non si decora.` | `argomenta` | verb form of anchor noun · motif reinforcement |
| 3 | Narrative pull-quote 1 (LF-2 L4) | `Il rilievo è la <em>prima</em> forma di rispetto.` | `prima` | ordinal · architectural-method emphasis |
| 4 | Narrative pull-quote 2 (LF-2 L4) | `Un <em>autore</em> non è chi firma più progetti…` | `autore` | authorship-stance noun |
| 5 | Narrative pull-quote 3 (LF-2 L4) | `Pubblicare un progetto … significa lasciare <em>regola</em>` | `regola` | discipline-method noun |
| 6 | Sectors counter footnote | `dal 2008, <em>novanta</em> fascicoli aperti` | `novanta` | numeric anchor · counts-the-publications signature |
| 7 | Leadership h2 (LF-2 L6) | `Marco <em>Roveri</em>` | `Roveri` | family name · single-principal signature |
| 8 | Cases card 7 h3 (LF-2 L7) | `Biblioteca civica · l'argomento è la <em>geometria</em> del modulo` | `geometria` | project-specific argument noun |
| 9 | Cases card 8 h3 (LF-2 L7) | `Via Volpe — sei alloggi sul <em>lotto</em> stretto` | `lotto` | site-specific noun |
| 10 | Cases card 9 h3 (LF-2 L7) | `Palazzo Lignari — la corte come <em>argomento</em> civile` | `argomento` | curatorial-noun · motif recurrence |
| 11 | Cases card 10 h3 (LF-2 L7) | `La cornice del fronte <em>minore</em> — una nota critica` | `minore` | typological adjective |
| 12 | CTA-closer h2 (LF-2 cream) | `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` | `argomento` | voice anchor verbatim repeat |

**Audit summary**:
- **12 italic ems on home + chrome · all on distinct headings or quotes**
- **One em per heading/quote** — CS-TYPE-02 binding holds 12/12
- **`argomento` (or `argomenta`) appears as the em on 4 of 12 surfaces** (#1, #2, #10, #12) — the editorial-curatorial motif
- **9 of 12 ems are diverse** (`prima · autore · regola · novanta · Roveri · geometria · lotto · minore` plus 1 motif-noun) — proves the home is not trapped in single-word obsession
- **Solaria's contrast-pair pattern (TWO ems in one heading) is structurally NOT used** anywhere

**Motif-vs-repetition resolution**:
The 4 occurrences of `argomento` (or `argomenta`) are spread across 4 distinct surface classes (hero h1 · hero side-quote · cases card 9 h3 · CTA-closer h2). Between #1 and #12, the reader encounters ~1480 words of intervening copy. This is a literary motif, not a repetition. CS-TYPE-02 audit passes.

If A.6 critique conservatively flags the recurrence as covert two-em pattern, the documented A.4 fallback is to swap card 9's em from `argomento` to `civile` — see `copy-authoring.md §18 Risk C-3` for the trade-off analysis. A.4 author recommends KEEPING the motif because it is the editorial-curatorial signature.

---

## §6 · Anti-pattern audit (the "studio creativo generico" trap)

This is the test the planner specifically asked to be proven: that Cornice does NOT collapse into "studio creativo generico" copy. The audit applies a 6-point negative test.

```
6-point "studio creativo generico" detector:

  1. Adjectival hyperbole density (modern · innovativo · all'avanguardia · premium ·
     straordinario · raffinato · prestigioso)
     Cornice scan:                          ABSENT (0 occurrences in home + chrome)
     → PASS

  2. Generic action verbs (progettiamo · trasformiamo · creiamo · sblocchiamo · realizziamo
     · sviluppiamo · ridefiniamo)
     Cornice scan:                          1 instance of `realizziamo`-stem
                                            ("opere realizzate" · footer + sectors counter)
                                            — the participle is institutional and used
                                            with a noun (opere), NOT as a stand-alone
                                            action-verb-banner.
                                            Zero instances of trasformiamo, creiamo, sblocchiamo,
                                            sviluppiamo, ridefiniamo.
     → PASS

  3. Future-fantasy framing (il futuro · futuro dell'architettura · spazi del domani ·
     visione del futuro)
     Cornice scan:                          ABSENT (0 occurrences)
     → PASS

  4. Generic abstract nouns (qualità · eccellenza · esperienza · passione · innovazione ·
     creatività · talento)
     Cornice scan:                          ABSENT in headings and pull-quotes
                                            ZERO in voice anchor or hero subhead
                                            → PASS

  5. Stock acronyms or invented institutions (la Nostra Visione · il Metodo CORNICE · il
     Nostro DNA · il CornicePensiero)
     Cornice scan:                          ABSENT (0 occurrences)
     → PASS

  6. Generic creative-studio CTAs ("Iniziamo a parlare" · "Raccontaci il tuo progetto" ·
     "Costruiamo insieme")
     Cornice scan:                          ABSENT
                                            CTA is `Apri un fascicolo progetto` — institutional
                                            architectural verb · not creative-studio framing.
     → PASS

6-point detector verdict: 0/6 hits. Cornice does NOT collapse into "studio creativo generico."

The Cornice prose is held by:
  · architectural sub-cluster vocabulary at structural density (56+ Tier-1/2 hits in 615w narrative)
  · institutional credentials by name (OAPPC · CNAPPC · MIBAC · D.M. 154/2017 · D.lgs. 24/2023 ·
    Codice Beni Culturali · Soprintendenza · CNAPPC tariffe minime)
  · concrete project facts (lot dimensions · year · committenza · fascicolo numbers)
  · explicit refusals (the closing line refuses 4 conventional CTAs by name)
```

---

## §7 · Architectural-vocabulary surface map (proof of sub-cluster identity)

The home page surfaces 56+ architectural sub-cluster terms across 1541 words. This section maps them by surface, proving the architectural identity is structural at every section.

```
SURFACE-BY-SURFACE ARCHITECTURAL VOCABULARY MAP:

§6.1 hero (66w · 7 architectural terms · density 11%):
  argomento · progetto · architettura · committenze · fascicoli · studio · 2008
  + side-quote: architettura · argomenta

§6.2 narrative (615w · 56 Tier-1/2 hits across 4 paragraphs · density 9%):
  Para 1 (110w · 14 hits): architettura · argomenta · studio · architettura · editoriale ·
    progetto · argomento · sito · committenza · vincolo · opere · cantiere · contesto · programma
  Para 2 (131w · 19 hits): commissione · rilievo · opera · contesto · committenza · vincoli ·
    PRG · Soprintendenza · paesaggio · argomento · progetto · cantiere · sito · collaudo ·
    opera · collana · monografica · architettura · regola
  Para 3 (150w · 23 hits): committenze · autore · esecutore · Comuni · restaurano · corte ·
    edificio · concorso · architetto · brand · autoriale · argomento · strutturisti ·
    paesaggisti · restauratori · cantiere · studio · pratiche · permissioni · bandi pubblici ·
    Soprintendenza · progetto · fascicolo
  Para 4 (134w · cluster of references): opere · pubblichiamo · portfolio · argomenti ·
    costruiti · tipologia · cantiere · scheda · sito · committenza · programma · cronologia ·
    vincolo · argomento · progetto · concorso · culturale · edificio · residenziale ·
    restauro · corte · cornice · fronte · programma · argomento

§6.3 sectors-ribbon (143w · 12 typology terms + 8 institutional terms · density 14%):
  intervento · scala · opera · programma · committenza · vincolo · paesaggistico · storico
  + 12 typologies: residenziale · pubblico · interno · paesaggio · restauro · concorso ·
    culturale · uffici · industriale · sanitario · scolastico · misto-uso
  + restauro · concorso · qualifica MIBAC · Soprintendenza · commissioni pubbliche ·
    gara · concorso · sacro · infrastruttura · allestimento museale · paesaggio agricolo
  + collana · novanta fascicoli · opere realizzate · concorsi consegnati · pubblicazioni ·
    fascicoli aperti · committenze in corso

§6.4 leadership-single (239w · 22 institutional terms · density 9%):
  Cornice · Milano · Bologna · studi di restauro pubblico · Politecnico di Milano ·
  cattedra di restauro architettonico · École Polytechnique de Lausanne · stereotomici ·
  volte in pietra · studio · rilievo · argomento · fascicolo · cantiere · collaudo ·
  collana monografica · opere · progettazione del restauro · Politecnico di Milano ·
  restauro · Palazzo Lignari · MIBAC · concorso · biblioteca civica · cantiere ·
  edificio residenziale · lotto · cornice · fronte minore · concorsi pubblici ·
  responsabilità autoriale · monografie · collana · saggi · Casabella · Domus ·
  Il Giornale dell'Architettura
  + 4 credentials: Albo OAPPC · Iscritto Ordine degli Architetti di Milano · CNAPPC ·
    MIBAC qualifica restauro · D.M. 154/2017 · Politecnico di Milano · Cattedra di Restauro

§6.5 cases-magazine-grid (361w body · 4 per-card project facts):
  Card 7: concorso vinto · Pietrasanta · biblioteca civica · cinta muraria · vincolo
    paesaggistico · doppia fronte · modulo · aule di lettura · deposito · portico ·
    cemento a vista · cornice del fronte · cantiere · committenza · Comune
  Card 8: opera realizzata · Roma · Tiburtino · alloggi · lotto urbano · fronte ·
    profondità · corte cieca · livelli · sottotetto · struttura in c.a. · laterizio
    faccia a vista · committenza privata · appalto · progetto integrale · preliminare ·
    collaudo · fascicolo · collana
  Card 9: restauro pubblico · Bologna · Palazzo Lignari · piano nobile · istituto culturale ·
    portico restaurato · pavimentazioni in cotto · interventi storici · cesura · MIBAC
    qualifica restauro · Soprintendenza Belle Arti
  Card 10: pubblicazione · saggio · collana · regola della cornice · fronti minori ·
    edilizia ottocentesca · tipologie · proporzione · cornice · dispositivo civile ·
    co-edizione · DAStU · libreria

§6.6 cta-closer (65w · 8 institutional terms):
  commissioni · fascicolo progetto · argomento · servizio · brief · sito · tipologia ·
  cronoprogramma · documenti · architettura · Milano · 2008 · call di scoperta · preventivo

DENSITY ACROSS HOME:
  Total words on home (incl chrome): 1541
  Total architectural sub-cluster terms surfaced: ≥120 (some recur)
  Unique architectural terms: ≥85
  Density: ≥5.5% of total prose · holds editorial-curatorial register firmly

The architectural vocabulary is STRUCTURAL — present in every section, not concentrated in
one show-off block. Removal of any single section would still leave the sub-cluster identity
unmistakable in the remaining sections. This is the editorial-curatorial register's spine.
```

---

## §8 · Verdict + final voice anchor (binding)

```
=================================================================
VOICE ANCHOR PROOF · cornice-architettura · A.4 final
=================================================================

Final voice anchor (IT · binding · verbatim):
   "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."

Em-word:                             argomento
Em-count per heading:                1 (CS-TYPE-02 default)
Em-pattern type:                     SINGLE em (NOT Solaria's contrast-pair)
Negation form:                       "non … reso" (refuses service-vendor framing)

Side-quote (binding · paired with hero anchor):
   "L'architettura buona si <em>argomenta</em> — non si dimostra,
    non si vende, non si decora."

Em-word:                             argomenta (verb form of anchor noun)
Negation triplet:                    refuses dimostra · vende · decora


SIBLING DISTINCTNESS GATES:
   vs Pragma (decisional-gravity · advisory):       4/4 axes DIFFER → PASS
   vs Fiscus (presidio-scadenze · commercialista):  4/4 axes DIFFER → PASS
   vs Solaria (bounded-method · coaching):           5/5 axes DIFFER → PASS
   vs Continua (stewardship-longitudinal · custodia): 5/5 axes DIFFER → PASS

   AGGREGATE GATE (≥4/5 vs every sibling on voice axis): PASS


HYPERBOLE BANLIST (CS-EXEC-04):              0/14 hits — PASS
SIBLING-CTA BANLIST (CS-CTA-02 + intake §4): 0/9 hits — PASS
"STUDIO CREATIVO GENERICO" 6-POINT DETECTOR: 0/6 hits — PASS
CS-TYPE-02 ONE-EM-PER-HEADING:               12/12 — PASS


STUDIO-NAME-SWAP TEST (CS-TONE-05):
   Test §3.1 voice anchor in isolation:        PASS
   Test §3.2 36-word stakeholder one-liner:    PASS
   Test re-bound at A.6 style-critic:          BINDING
   Test re-bound at A.7 walk on live render:   BINDING


STRUCTURAL VOCABULARY DENSITY:
   ≥85 unique architectural sub-cluster terms across 1541w home
   ≥5.5% density of total prose
   Architectural identity is STRUCTURAL not adjectival
   Survives wordmark removal (B and C swap-test)


ANCHOR LOCKED:                                 YES
SUB-CLUSTER IDENTITY UNMISTAKABLE:             YES
READY FOR A.5 BUILD:                            YES
A.6 CRITIC RE-RUN BINDING:                      §3 + §4 + §5 + §6
A.7 WALK RE-RUN BINDING:                        §3.1 + §3.2 on live DOM
A.9 RELEASE-GATEKEEPER AGGREGATE INPUT:         §4.5 distinctness gates · §8 verdict block
```

---

## §9 · After this file

This file is paired with `copy-authoring.md` (the paper Italian content system) and `content-volume-check.md` (the per-beat word-budget ledger and floor calibration). The three files together form the binding A.4 output for Cornice.

A.5 build picks up the voice anchor verbatim from §1.1 of this file and surfaces it on:
1. `home.html` hero h1 (LF-2 L1 · stacked-editorial)
2. `home.html` cta-closer-cream h2 (LF-2-specific cream-band closer)

A.6 style-critic re-runs §3 swap test + §5 em-audit + §6 anti-pattern audit on the rendered home.

A.7 IT browser walk verifies the voice anchor renders correctly with the italic on `argomento` at all 6 viewports, and re-runs the swap test with the wordmark hidden in dev tools.

Workflow C (5 locales) extends this anchor to EN/FR/ES/AR per planner-brief §11; the IT pass at workflow A does NOT depend on the cross-locale extension.

No application code touched. No registry edit. IT only at this step.
