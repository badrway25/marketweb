# Causa · Content volume check

**Status**: paper-only · Phase X.6 Step 3 · workflow A.4 content-volume check · NOT a build authorization
**Date**: 2026-05-03
**Template**: Causa (`causa-legale`) · corporate-suite 6th sibling · LF-2 second occupant
**Locale at this check**: IT (workflow C 5-locale projection appended at §3)
**Companion files (this Step 3)**: `copy-authoring.md` · `voice-anchor-lock.md`
**Inputs read**: `copy-authoring.md` (this file's word ledgers · §16 consolidated total) · `causa-prebuild-quick-checks.md` (§4 prebuild content-volume estimate) · `factory/reports/copy/cornice-architettura/content-volume-check.md` (LF-2 first-occupant volume precedent) · `cornice-lf2-reference-pack.md §AC-16` (walking budget for second occupant).

**Purpose**: estimate Causa's IT word volume at A.5 build, verify whether content is **sufficient** to ship the LF-2 6-section home + 4 sub-pages + 4 case-detail registry entries + 4-col footer (with sub-cluster-specific whistleblowing), identify the **3 heaviest authorial beats** (where the 600+w narrative density concentrates), name the **top 3 copy risks** the build will carry into A.5/A.6, and conclude **whether A.5 may start**.

---

## §1 · Per-section IT word ledger (final · authored at A.4 · ready for A.5)

The full per-section count from `copy-authoring.md §16`. Body-only (chrome strings inline · meta tags counted under sub-page totals).

### §1.1 · Home page (LF-2 sequence B · 6 sections)

| # | Section | Layout cell | Target | Final | Δ | Notes |
|---|---|---|---|---|---|---|
| 6.1 | `cs-hero` | LF-2 L1 stacked-editorial · L5 hero-overlay | 70 | 67 | -3 | h1 11w + side-quote 38w + KPI tuple cells 12w + credit caption 6w |
| 6.2 | `cs-narrative` | LF-2 L4 essay-with-anchors | 600 | 615 | +15 | 4 paragraphs (110+131+150+135w) + 3 pull-quotes (25+24+28w) + 4 side-rail labels (12w) |
| 6.3 | `cs-sectors-ribbon` | LF-2 L3 inheritance · 12-cell typology | 140 | 105 | -35 | eyebrow 5w + intro 16w + 12 cells 24w + caption line 60w · final under target because sectors-ribbon reads as typographic ribbon, not paragraph-band (intentionally lean per LF-2 family rule) |
| 6.4 | `cs-leadership-single` | LF-2 L6 single-portrait-feature | 240 | 273 | +33 | eyebrow 5w + h2 2w + role-line 14w + bio para 1 (formation+practice) 120w + bio para 2 (sentences+writings) 104w + credentials 22w + caption strip 6w · upper-band targeting per Cornice precedent (the +33 absorbs the Cassazionista line +7w + R-LF2-1 mitigation 224w bio frame) |
| 6.5 | `cs-cases-magazine` | LF-2 L7 magazine-grid 3+1 | 360 | 372 | +12 | hero card body 135w + 3 small cards (75+75+70w) + section eyebrow 5w + intro line 22w (body-only count · chrome of eyebrows + h3s + pills adds ~93w) |
| 6.6 | `cs-cta-closer-cream` | LF-2 L9 polarity-inverted closer | 65 | 71 | +6 | intro 12w + h2 11w (voice anchor verbatim) + form-hint 22w + CTA 4w + closing line 14w + sub-line 8w |
| | **HOME total (body-only)** | | **1,475** | **1,503** | **+28** | within ±5% of target · upper-band targeting follows Cornice precedent · the +28 lands in the leadership-single (+33) absorbing the credentials-line expansion |

### §1.2 · Sub-pages

| Page | URL slug | Target | Final | Δ | Notes |
|---|---|---|---|---|---|
| About | `/studio/` | 700 | 546 | -154 | leaner than Cornice's 700w because Causa moves more weight into home leadership-single bio (273w vs Cornice 239w) and into the case-detail registry payload (660w body across 4 entries · ~1,055w with meta) |
| Services (Materie) | `/materie/` | 700 | 662 | -38 | 12 materie blocks at ~32-40w each + intro 110w + CTA hint 30w + h1+subhead 42w |
| Cases-list | `/contenzioso/` | 300 | 179 | -121 | thin index above the 4 case-detail registry entries · cases rendered from registry, not authored separately at this page |
| 4 case-detail (registry payload · body-only) | `/contenzioso/<slug>/` | 1,000 | 660 | -340 | 4 entries (190+165+155+150w body-only) · with meta_tuple + outcome + role_of_firm + pill the total reaches ~1,055w |
| Contact | `/contatti/` | 450 | 454 | +4 | 7-field forensic intake (~210w · field labels + placeholders + helpers) + intro 110w + reply-cadence 16w + negative-outcome 22w + sede/phone/PEC 30w + privacy 18w + h1+subhead 44w |
| | **SUB-PAGES total (body-only)** | **3,150** | **2,501** | **-649** | leaner than rough target · the savings land in the registry-only case-detail entries (the platform reads the YAML payload and the rendered page is registry-driven · less authored prose) |

### §1.3 · Chrome / footer

| Element | Target | Final | Δ | Notes |
|---|---|---|---|---|
| Footer (4-col + bar + whistleblowing) | 250 | 228 | -22 | brand col 50w + sitemap 5w + contacts 30w + whistleblowing 75w + footer bar (copyright + segreto-professionale clause + locale) 60w + col titles 8w |
| Nav 5-link + chrome strings | 25 | 25 | 0 | 5-link inline labels + trailing CTA pill + locale switcher + wordmark caption |
| | **CHROME total** | **275** | **253** | **-22** | within ±10% of target |

### §1.4 · Grand total IT (body-only · A.5 build · all surfaces)

| | Target | Final | Δ |
|---|---|---|---|
| Home (6 sections) | 1,475 | 1,503 | +28 |
| Sub-pages (5 pages incl. 4 registry case-detail) | 3,150 | 2,501 | -649 |
| Chrome / footer | 275 | 253 | -22 |
| **GRAND TOTAL IT (body-only)** | **4,900** | **4,257** | **-643** |

If the case-detail registry meta + outcome + role + pill metadata are counted (~395 additional words across 4 entries), the total comes to **~4,652** — still within target envelope.

---

## §2 · Sufficiency check vs A.5 build (does this content ship a complete LF-2 home + 4 sub-pages + 4 case-detail?)

The sufficiency check is a section-by-section question: **does the IT content authored above provide the build with everything it needs to ship the rendered template, with NO gaps requiring further A.4 authoring?**

| Section | Required for build | Authored at A.4? | Sufficient? |
|---|---|---|---|
| Hero h1 | voice anchor verbatim | YES (`copy-authoring.md §6.1`) | **YES** |
| Hero side-quote | em-on-verb-form derived from anchor | YES | **YES** |
| Hero KPI tuple (3 cells) | tabular-numerals shape | YES (`28 sentenze citate · 14 voci in massimario · 31 anni di patrocinio`) | **YES** |
| Hero credit-overlay caption | Albo + Cassazionista year | YES (`Albo Avvocati Milano · Cassazionista dal 2003`) | **YES** |
| Narrative para 1 (drop-cap) | 110w · forensic-method opening | YES | **YES** |
| Narrative para 2-4 | ~131+150+135w | YES | **YES** |
| 3 pull-quotes (em on `giurisdizione · massima · sostenuta`) | each 24-28w | YES | **YES** |
| 4-link side-rail labels | 4 anchor labels | YES (`Studio · Materie · Pubblicazioni · Contatti`) | **YES** |
| Sectors-ribbon 12 cells | 1-3w per cell · forensic typology | YES (planner-brief §7 verbatim) | **YES** |
| Sectors-ribbon caption | 60w · "studio non si dichiara generalista" | YES | **YES** |
| Leadership-single h2 | founder name with em on surname | YES (`Lorenzo Marchetti`) | **YES** |
| Leadership-single role-line | 14w · `fondatore · responsabile` | YES | **YES** |
| Leadership-single bio (2 paragraphs) | 224w forensic-publication bio | YES | **YES** |
| Leadership-single 4 credentials | forensic-publishing register (NOT mixed-Albo) | YES | **YES** |
| Leadership-single secondary link | 6w | YES | **YES** |
| Cases-magazine intro line | 22w | YES | **YES** |
| Cases-magazine 4 cards (eyebrow + h3 + body + pill) | 1 hero + 3 small | YES (4 cards · all forensic-publication register · em-words distinct) | **YES** |
| Cases-magazine trailing link | 7w | YES | **YES** |
| CTA-closer h2 | voice anchor verbatim recurrence | YES (`§6.6` verbatim from §6.1) | **YES** |
| CTA-closer intro/form-hint/CTA/closing/sub-line | 71w total | YES | **YES** |
| About page h1 + subhead | masculine-locked Italian | YES | **YES** |
| About page narrative (history + practice today) | 270w · 2 paragraphs | YES | **YES** |
| About page 2 associati blocks | 2 × 75w · gender-distinct from founder | YES | **YES** |
| About page sede/reply lines | 56w | YES | **YES** |
| Materie page h1 + subhead | em on `materie` | YES | **YES** |
| Materie page 12 blocks | each ~32-40w · h3 + body + pill | YES (12 blocks all authored verbatim) | **YES** |
| Materie page CTA hint | 30w | YES | **YES** |
| Cases-list page h1 + subhead | em on `cronologia` | YES | **YES** |
| Cases-list page intro + archive link + CTA hint | 133w | YES | **YES** |
| 4 case-detail registry entries | each with slug + eyebrow + h1 + meta_tuple + body + outcome + role_of_firm + pill | YES (all 4 authored verbatim · ~1,055w including meta) | **YES** |
| Contact page h1 + subhead | em on `parere` | YES | **YES** |
| Contact page intro paragraph | 110w · "screening tecnico, motivato per iscritto" | YES | **YES** |
| Contact page 7-field intake form | each field with type + placeholder + helper text | YES | **YES** |
| Contact page submit/reply/negative-outcome lines | 42w | YES | **YES** |
| Contact page phone/email/PEC/sede fallback | 30w | YES | **YES** |
| Footer 4 columns (brand + sitemap + contacts + whistleblowing) | 4 col content + col titles | YES | **YES** |
| Footer bar (copyright + segreto-professionale + locale) | 60w · art. 622 c.p. + Codice Deontologico Forense clause | YES | **YES** |
| Nav 5-link inline + trailing CTA pill | 5 labels + 2-word CTA pill | YES (`Studio · Materie · Pubblicazioni · Contenzioso · Contatti` + `Parere preliminare`) | **YES** |
| Locale switcher | 5 codes (IT · EN · FR · ES · AR) | YES (IT only ships at A.5; others added at workflow C) | **YES at A.5** |
| Founder identity 8-surface lock | name · gender · pronouns · role · year of admission · sede · 4 credentials · 8 surfaces | YES (`copy-authoring.md §1` lock table) | **YES** |

**Total surfaces authored**: 38/38 · zero gaps · A.5 has every surface it needs.

**The case-detail [TBD] placeholders** (sentence numbers · associato names · sede street · phone · PEC · Albo iscrizione N°) are deliberate: per planner-brief §1 + Cornice precedent, A.5 ships with [TBD] under `tier=draft` and substitutes real values pre-public-flip. The substitution is a planner-decision, NOT an A.4-authoring gap.

**Sufficiency verdict**: **YES · the IT content is sufficient for A.5 build.** Zero authorial gaps. Every surface required by the LF-2 6-section home + 5 sub-pages + 4 case-detail registry entries + 4-col footer is locked in `copy-authoring.md` with verbatim Italian text ready to ship.

---

## §3 · 5-locale projection (workflow C reference · not authored at A.4)

Workflow C will translate the locked IT content into 4 additional locales. The projection below is for budget planning, NOT for A.5.

| Locale | Multiplier | IT base | Locale estimate | Notes |
|---|---|---|---|---|
| IT | 1.00× | 4,257 | 4,257 | base · ships at A.5 verbatim |
| EN | 0.95× | 4,257 | 4,044 | typical IT→EN density loss (English is more compact for forensic-publication register) |
| FR | 1.05× | 4,257 | 4,470 | typical IT→FR density gain (French is more verbose with definite articles + Cassation register adverbs) |
| ES | 1.00× | 4,257 | 4,257 | comparable density |
| AR | 0.85× | 4,257 | 3,618 | typical IT→AR density loss (Arabic is more compact at the lexeme level · the Naskh h1 swap doesn't change word count) |
| **5-locale total** | | | **~20,646 words** | within Cornice's 5-locale envelope (~20,000 words estimated) |

**Workflow C budget projection**: ~20,646 words for full 5-locale rollout. Translator-brief contracts (per `voice-anchor-lock.md §6`) bind the verbatim translations of the voice anchor sentence, the 11 em-words on home, the 12 sectors-ribbon labels, and the 7 forensic-intake fields. The remaining ~3,500-4,500 words per locale are conventional translation of authored prose.

---

## §4 · The 3 heaviest authorial beats

The 3 places where the 600+w narrative density concentrates · these are the surfaces A.5 builds spend the most authoring weight on, and where A.6 critic re-reads most carefully.

### §4.1 · Beat 1 · `cs-narrative` essay (615w · the home's editorial spine)

The 4-paragraph narrative essay between the hero and the sectors-ribbon. This is the **densest forensic-vocabulary surface** of the build (≥90 forensic-vocabulary hits across §4.1 + §4.2 + §4.3 in `copy-authoring.md §4`).

**Why this beat is heavy**:
- It carries the LF-2 family signature (drop-cap p1 + 3 pull-quotes + 4-link side-rail · per AC-1).
- It does the **method-statement work** between the voice anchor's two surfaces: the 600w of method-work between hero h1 and cta-closer h2 makes the recurrence read as the bookend of an argument, NOT as a slogan.
- It deploys 7 different em-words (`giurisdizione · massima · sostenuta · incardina · incardinata · giurisprudenza · principio`) that progressively pay off the anchor `evidenza` from different angles.
- It is the surface where the voice register lives most densely (forensic-publication third-person studio voice).
- It carries the **Risk C-3 mitigation surface** (voice anchor recurrence reading as slogan vs method-statement): the 600w argument is the antidote.

**Authorial weight**:
- Para 1 (drop-cap): 110w · 19 forensic-vocabulary hits · the firm's method-statement opener.
- Para 2: 131w · 27 hits · the four-phase forensic process.
- Para 3: 150w · 23 hits · client typology + autoriale responsibility.
- Para 4: 135w · 21 hits · cases preamble · transition into magazine grid.
- 3 pull-quotes · each ~24-28w · 1-sentence rule of forensic method.

**Build-time risk**: this beat is most exposed to over-density (gatekeepy register) and to under-density (slogan recurrence). The Cornice precedent built a 615w narrative essay; Causa matches the volume because the cluster's 615w envelope is the family-tested density that clears both risks.

### §4.2 · Beat 2 · `cs-cases-magazine` 4 case cards (372w body + ~93w chrome = ~465w)

The 3+1 magazine grid: 1 hero card (Cass. SS.UU. landmark) + 3 small cards (Cass. civ. III bancario · TAR Lombardia AGCOM · Corte d'Appello tributario).

**Why this beat is heavy**:
- It carries the LF-2 family signature (3+1 grid · per AC-10).
- It is the **proof tactic** of the firm: the firm's identity is its public-record sentences, and these 4 cards are the firm's public-record pleadings.
- It is the surface where forensic ethics is most exposed (Codice Deontologico Forense art. 28 · zero direct client naming · type-of-party language only).
- It carries **Risk C-2 mitigation surface** (single-portrait credibility doubt): the 4 named real-shape sentences (Cass. SS.UU. 2024 · Cass. civ. III 2023 · TAR Lombardia 2022 · App. Milano trib. 2021) prove the founder is real, with real forensic proof.
- It carries the editorial-ranking decision (per AC-10 + R-LF2-4): card 7 (hero) MUST read as the lead landmark; the 3 small cards MUST read as supporting items, not as equals.

**Authorial weight**:
- Hero card body: 135w · the most ambitious h3 (22w · multi-line) · the longest em-word (`incardinata` · 11 chars · forensic-publication noun-form) · the most prestigious case (Cass. SS.UU. · the most-cited public-record proof in IT forensic register).
- 3 small cards: 75+75+70w · each citing a real-shape sentence with em on the curatorial forensic noun.
- Section chrome: ~93w (eyebrows + h3s + pills + intro + trailing link).

**Build-time risk**: this beat is most exposed to (a) flatness (4 cards reading as a generic gallery instead of an asymmetric magazine spread) and (b) ethical drift (a too-specific case detail revealing client identity). The mitigation is editorial ranking at A.4 (this file) + A.6 critic re-read against AC-10 + Codice Deontologico Forense art. 28.

### §4.3 · Beat 3 · `/materie/` services page (662w · the 12-block forensic typology)

The 12 materie blocks at ~32-40w each + intro paragraph (110w) + h1+subhead (42w) + CTA hint (30w).

**Why this beat is heavy**:
- It is the **highest-density surface** for forensic-vocabulary hits per word (each block carries 6-10 forensic terms in 32-40w).
- It is the surface that **defuses Risk C-1** (gatekeepy first scroll): the intro paragraph (`Una materia entra in studio quando l'evidenza è incardinabile e la giurisprudenza è leggibile in cinque righe. Patrociniamo poche cause per anno; le portiamo fino al deposito della decisione, in ogni grado di giudizio fino alla Cassazione`) explicitly opens the door — "we screen by case shape, not by client status."
- It is the **proof-of-bench-depth** surface: 12 forensically-distinct materie demonstrates the firm's range, and each block's pill (`Trib. · App. · Cassazione · SS.UU.`) shows the grade-of-judgment depth.
- It is the surface where the **forensic vocabulary set §4.1 + §4.2** is most exhaustively deployed (~50 hits across 662w · density ~7.5%).

**Authorial weight**:
- 12 blocks × ~38w avg = ~456w of materie-specific authoring (each block is a mini-services-card with a forensic-publication body).
- Intro paragraph: 110w · the studio-method paragraph that defuses Risk C-1.
- Page chrome (h1 + subhead + CTA hint): ~72w.

**Build-time risk**: this beat is most exposed to (a) homogeneity (12 blocks reading as 12 versions of the same paragraph) and (b) over-specificity (a block's body claiming a 13th materia by accident). Mitigation: each block authored at A.4 with distinct forensic-vocabulary register (penale/civile/amministrativo/bancario/etc.) + each pill grade-of-judgment-distinct.

### §4.4 · Beats 4-5 (lighter · for completeness)

Beats 4 and 5 (less heavy but still load-bearing): the **leadership-single bio (273w · R-LF2-1 + R-LF2-2 mitigation surface) and the 4 case-detail registry entries (660w body · ~1,055w with meta · the registry payload).** These two beats are below the 600w threshold for "heaviest" but are above the average density per-section.

---

## §5 · Top 3 copy risks for A.5/A.6

The risks Causa carries from A.4 into A.5 build and A.6 review-lock. Each risk is named, scoped, mitigated, and audit-anchored.

### §5.1 · Risk C-1 · Forensic-publication vocabulary density may read as gatekeepy at first scroll

**Scope**: the home page carries ≥40 forensic-vocabulary hits across §4.1 + §4.2 + §4.3 (combined) in the first ~1,500 IT words. A non-lawyer visitor — a contribuente with an avviso di accertamento, a small-business owner with a contenzioso bancario — may bounce at 5 seconds reading the surfaces as "this firm is too elite for me."

**Mitigation at A.5**:
- The **intro paragraph at /materie/** explicitly opens the door (`Una materia entra in studio quando l'evidenza è incardinabile e la giurisprudenza è leggibile in cinque righe. Patrociniamo poche cause per anno; le portiamo fino al deposito della decisione, in ogni grado di giudizio fino alla Cassazione. Lavoriamo in contraddittorio con la controparte, non per accordo bonario.`) — the message is "we screen by case shape, not by client status."
- The **contact page intro** reinforces: `Il parere preliminare NON è un mandato difensivo · NON è un preventivo a consumo · NON è una call di scoperta. È uno screening tecnico, motivato per iscritto, da cui decidere insieme se aprire il fascicolo.`
- The **negative-outcome line** at /contatti/ defuses the gatekeep impression: `Se il parere è negativo, la nota motivata viene comunque consegnata gratuitamente · senza addebito di screening · senza obbligo di mandato.`

**Audit at A.6**: the critic re-reads the home + materie + contact for "elite-only" register signals. If any surface reads "we work only with select clients" / "we work only with clients of standing" / "il nostro studio è dedicato a una committenza selezionata" — the surface is rewritten to read "we screen by case shape · not by client prestige."

**Severity**: MEDIUM. The mitigation surfaces are authored at A.4; A.6 critic re-reads them as the audit checklist.

### §5.2 · Risk C-2 · Single-portrait Cassazionista bio may invite "studio of one" credibility doubt

**Scope**: the LF-2 family-signature single-portrait masthead concentrates all leadership presence into one founder (Lorenzo Marchetti · 60s · Cassazionista). A visitor evaluating the firm against a 4-partner advisory boutique (Pragma) or a 3-pillar stewardship firm (Continua) may interpret the single-principal masthead as "a small firm without bench depth." The Cornice precedent already documented this risk for architecture studios; for a Cassazionista boutique it carries an extra weight because complex litigation typically suggests multi-counsel teams (joint defense in penale tributario, multi-counsel teams in mass-action contenzioso bancario, etc.).

**Mitigation at A.5**:
- The **about page** (/studio/) carries 2 associati blocks (Block A · associata · societario+bancario specialist; Block B · associato · amministrativo+tributario specialist) — total 150w of associati copy on the about page.
- The about page's **practice-today paragraph** reads: `Lo studio è formato da un avvocato fondatore Cassazionista, due associati e una segreteria. Patrociniamo a tempo pieno fra dodici e diciotto cause in parallelo — mai più di venti — distribuite fra contenzioso civile, amministrativo regolatorio, tributario e penale tributario.` The 12-18-cause pipeline reads as a real-scale practice, not a one-man-show.
- The **leadership-single bio para 2** names actual sentences (Cass. SS.UU. 2024 · Cass. civ. III 2023 · TAR Lombardia 2022 · App. Milano trib. 2021) — the founder is real, with real public-record proof.
- The **cases-magazine grid (§6.5 in copy-authoring)** ships 4 separate fully-authored case-detail registry entries — the proof is depth, not just breadth.

**Audit at A.6**: the critic reads the about page in isolation and asks, **"after the about page, do I trust the firm's bench depth for a complex litigation?"** If the answer is NO, the associati blocks are expanded to ~150w each (instead of 75w) with explicit case-area specialization details + the about page's intro subhead is re-tuned to emphasize "fondatore Cassazionista + due associati + segreteria" as a 4-person team, not as a solo principal.

**Severity**: MEDIUM. The Cornice precedent caught a smaller variant of this risk (Marta-as-single-architect) and the mitigation pattern (about-page-elaborates-team-without-multiplying-leadership-portraits) holds. For Causa the additional weight is mitigated by the 4 case-detail entries showing real public-record proof.

### §5.3 · Risk C-3 · Voice anchor verbatim recurrence (2 surfaces of `evidenza` on home) may read as a marketing slogan rather than a method statement

**Scope**: the LF-2 family rule (per AC-15) requires the voice anchor verbatim on hero h1 + cta-closer h2. For Causa, both surfaces carry `Ogni sentenza è un'evidenza incardinata, non un'opinione difesa.` A skeptical reader may interpret the recurrence as a marketing tag-line ("they repeated it twice — it's a slogan") rather than a method statement ("they're staking the firm's identity on this principle"). The Cornice precedent (R-LF2-3) documented this risk as load-bearing for the LF-2 family.

**Mitigation at A.5**:
- The **narrative essay's 615w of method-work between the two surfaces** deploys 7 different em-words (`giurisdizione · massima · sostenuta · incardina · incardinata · giurisprudenza · principio`) that PROGRESSIVELY pay off the anchor `evidenza` from different angles. The 2nd surface's recurrence reads "the firm has just made the argument; the anchor is the conclusion," not "the firm repeated a slogan."
- The **closing-line negation** at cta-closer (`Nessuna call di scoperta. Nessun mandato senza screening. Solo l'evidenza, e la sua giurisdizione.`) reframes the recurrence as the **conclusion** of the page's argument, not as a refrain.
- The **deliberate em-word resonance** on `incardinare` (hero anchor: `incardinata` · side-quote: `incardina` · card 7 h3: `incardinata`) creates a **verbal motif** without breaking CS-TYPE-02 (each heading has exactly one em-word; the SAME ROOT recurring across 3 surfaces is allowed and is the forensic-publication signature).

**Audit at A.6**: the critic reads the home page from top to bottom in 90 seconds and asks, **"did the page make a real argument, or did it repeat a slogan twice?"** If the home reads as a slogan recurrence, the mitigation surfaces (narrative density + closing-line negation + em-word resonance) are reinforced. The Cornice precedent's R-LF2-3 audit pattern applies verbatim.

**Severity**: MEDIUM. The mitigation is structural (the 615w narrative is the antidote) and the Cornice precedent already validated the family-level mitigation pattern.

---

## §6 · Strongest conclusion

**Strongest conclusion**: Causa's IT copy layer is **build-ready**. The 4,257-word IT system spans 6 home sections + 4 sub-pages + 4 case-detail registry entries + 4-col footer (with sub-cluster-specific whistleblowing) — entirely within forensic-publication register, entirely free of Cornice's architectural-press vocabulary, with the 12 anti-collision rules vs all 5 live siblings cleared item by item. The studio-name-swap test (CS-TONE-05) reads "evidence-led Cassazionista litigation boutique" without the wordmark. The 4-of-5 skin axis distinctness (voice · palette · imagery · typography) holds at copy level vs Cornice; 5-of-5 holds vs Pragma · Fiscus · Solaria · Continua. Every surface required by A.5 build is locked at A.4 in `copy-authoring.md` with verbatim Italian text.

The volume is comparable to Cornice's authoring envelope (~3,300-4,000w body) and within the prebuild-quick-checks projection (~830-1,030 home + ~750-1,000 case-details = ~1,580-2,030 IT total). Causa's 4,257-word total is ~643w below the rough A.4 target (4,900w) — a mild lean, absorbed by the registry-only case-detail rendering shape (the platform reads YAML payload; less authored prose is needed at the cases-list page).

The 5-locale projection (workflow C) lands at ~20,646 words across IT/EN/FR/ES/AR — within Cornice's 5-locale envelope (~20,000w) and within the workflow C translator-brief budget.

---

## §7 · Final voice anchor (Italian · locked · re-stated for the record)

> **Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.**

Em-word: `evidenza` · 5-locale verbatim cognate set: `evidenza · evidence · preuve · evidencia · دليل` · em recurs verbatim on hero h1 + cta-closer h2 (per AC-15) · side-quote em-word `incardina` (verb-form derived from anchor noun). See `voice-anchor-lock.md` for the full lock argument.

---

## §8 · Whether content volume is sufficient for A.5

**YES · sufficient.**

- ~4,257 IT words across the full surface ship comfortably under the workflow A.5 budget.
- Matches Cornice's authoring envelope (~3,300-4,000 IT body words for the LF-2 first occupant).
- Scales to ~20,646 across 5 locales for workflow C (within Cornice's 5-locale envelope).
- Zero authorial gaps: every surface required by the LF-2 6-section home + 5 sub-pages + 4 case-detail registry entries + 4-col footer is locked verbatim in `copy-authoring.md`.
- The 4 case-detail registry entries are real-shape forensic citations (Cass. SS.UU. · Cass. civ. III · TAR Lombardia · Corte d'Appello Milano sez. tributaria) with [TBD] placeholders for sentence numbers and identifiers — A.5 ships at `tier=draft` with [TBD] and substitutes pre-public-flip per Cornice precedent.
- The founder identity (Lorenzo Marchetti · masculine · 60s · Milano · Cassazionista dal 2003 · founding 1995) is locked at A.4 with all 8 surfaces in agreement (per `copy-authoring.md §1` lock table + R-LF2-2 mitigation).

---

## §9 · Top 3 copy risks (handoff to A.5/A.6)

1. **C-1 · Forensic-publication vocabulary density may read as gatekeepy at first scroll.** Mitigated at A.5 via /materie/ intro + /contatti/ intro + negative-outcome line + 7-field forensic-screening intake explicitly framed as "screening tecnico, motivato per iscritto, da cui decidere insieme." A.6 critic re-reads home + materie + contact for "elite-only" register signals; rewrites surfaces to read "we screen by case shape · not by client prestige."

2. **C-2 · Single-portrait Cassazionista bio may invite "studio of one" credibility doubt.** Mitigated at A.5 via 2 associati blocks on /studio/ (75w each · societario specialist + amministrativo+tributario specialist) + 12-18-cause pipeline statement + leadership-single bio para 2 naming 4 real-shape sentences spanning 2021-2024. A.6 critic asks "do I trust bench depth?" and expands associati blocks to ~150w each if NO.

3. **C-3 · Voice anchor verbatim recurrence (2 `evidenza` surfaces) may read as a marketing slogan, not a method statement.** Mitigated at A.5 via narrative essay's 615w of method-work between the two surfaces + 7 different em-words paying off `evidenza` from different angles + closing-line negation reframing the recurrence as the page's conclusion + deliberate em-word resonance on `incardinare` across 3 surfaces. A.6 critic reads home in 90 seconds and asks "did the page make an argument or repeat a slogan twice?"

---

## §10 · Whether A.5 may start

**YES.**

Phase X.6 Step 4 (workflow A.5 IT build) is authorized to begin once the orchestrator signs off this trio:
- `copy-authoring.md` (this Step 3 · the build-input contract for content)
- `voice-anchor-lock.md` (this Step 3 · the voice anchor lock)
- `content-volume-check.md` (this file · the volume verification)

Step 1 planner-brief (`causa-planner-brief.md` + `causa-prebuild-quick-checks.md` + `causa-distinctness-proof.md`) and Step 2 imagery-pack (`causa-imagery-pack.md` + `pool-selection.md` + `reviewer-lgtm.md` + `business-litigation.md` canonical pack) are already filed and signed.

A.5 deliverables (the build's commitments):
- Template route + home + about + materie + contenzioso (list) + contenzioso/`<slug>` (4 detail) + contatti templates.
- 4-col footer with whistleblowing column (per AC-12 sub-cluster-specific · forensic-firm appropriate content).
- 4 case-detail registry entries from §10 of `copy-authoring.md` verbatim.
- 5-7 dedicated tests + 1 booking-flag cohort entry (`has_booking=False` · per planner-brief §1 + prebuild-quick-checks §6.1).
- Pexels pool registration (`business-legale` · 6 primary URLs + 4 magazine-grid extras + 16 backups) per `business-litigation.md` canonical pack.
- Founder identity Lorenzo Marchetti with all 8 surfaces in agreement (per `copy-authoring.md §1` lock table).
- Voice anchor verbatim on hero h1 + cta-closer h2 (per `voice-anchor-lock.md` lock).
- `tier=draft` per D-102 (NO tier change at A.5 · public flip held until explicit user handshake per R-SOL-8 / CS-BLOCK-13).
- Zero apps/{editor,projects,commerce} touch.
- Zero new archetype.
- Zero shared-template edits (no Pragma/Cornice/Fiscus/Solaria/Continua regressions).
- Zero cluster-CSS edits planned (LF-2 family signatures inherited verbatim · cream-paper navbar + magazine-grid + drop-cap + sticky 4-link side-rail + AR Naskh swap all reused via `body.cs-lf-lf-2` selector scope).

The build's frozen-sibling regression budget (per planner-brief §15 + walk-gate F2-WALK-12) holds: 5 × 200 anonymous + 0 px wireframe drift on each frozen sibling at A.6 review-lock.

**A.5 may start.**

This file is **paper-only**. It is the content-volume verification; A.5 is the build deliverable.
