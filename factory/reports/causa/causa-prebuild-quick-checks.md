# Causa · prebuild quick checks

**Status**: paper-only · Phase X.6 Step 1 · workflow A.2 · prebuild gate
**Date**: 2026-05-03
**Template**: Causa (`causa-legale`) · corporate-suite 6th sibling · LF-2 second occupant
**Companion files**: `causa-planner-brief.md` (DNA + anti-collision contract) · `causa-distinctness-proof.md` (5-column scoring)
**Purpose**: a focused pass that confirms the planner brief's preconditions hold BEFORE A.3 imagery curation begins. Each check returns one of three outcomes: **GO** (pass · proceed) · **HOLD** (pass with mitigation that must occur before next step) · **RESPEC** (fail · re-open the planner brief).
**Scope of the gate**: Phase X.6 Step 1 closure. A GO across all checks authorizes Phase X.6 Step 2 = workflow A.3 imagery curation. A HOLD blocks A.3 until the named mitigation lands. A RESPEC blocks until the planner brief is amended.

---

## §1 · Family availability and LF-2 second-occupant validity

### 1.1 · LF-2 family availability

| Probe | Reading | Source |
|---|---|---|
| Is LF-2 currently occupied? | **Yes · 1 occupant (Cornice)** | `corporate-suite-live-family-map.md §1` (5-sibling state) |
| Does LF-2 admit a second occupant? | **Yes · LF-2 is documented as multi-occupant by intent** | `corporate-suite-live-family-map.md §4 · LF-2 second-occupant fit list` |
| Is the LF-2 reference pack complete (planner-readable end-to-end)? | **Yes · AC-1..AC-16 + §5 don't-copy + §6 inherit-verbatim + §7 walk gates + §8 risks + §9 intake questions** | `cornice-lf2-reference-pack.md` |
| Has CS-LAYOUT-11 (one sibling per family) been updated to admit LF-2 multi-occupancy? | **Not applicable · LF-2 is structurally documented as multi-occupant in the live map · CS-LAYOUT-11 governs cross-family occupancy, not in-family occupancy** | `corporate-suite-layout-variance-rules.md · CS-LAYOUT-11` |
| Has Cornice's flip closed cleanly (LF-2 first occupant is `tier=published_live` and stable)? | **Yes · Cornice flipped 2026-05-01 · catalog 24/0 · 5 locales 200 anon · AR Naskh holds anon · zero Naskh leakage** | `phase_x5_cornice_public_flip.md` |

**Outcome 1.1**: **GO** · LF-2 family available for second-occupant build.

### 1.2 · LF-2 second-occupant validity for Causa

| Probe | Reading |
|---|---|
| Does Causa fit the "portfolio-of-work-led firm whose proof IS its case-bundle" criterion? | **Yes** · Cassazionista boutique · proof = sentenze citate, giurisprudenza, pubblicazioni in massimario, ENCA mediations |
| Is Causa's professional fit on the canonical second-occupant list (`live-family-map.md §4 · LF-2`)? | **Yes · evidence-led litigation is the FIRST item on the list** |
| Do all 7 family questions (`cornice-lf2-reference-pack.md §9`) clear? | **Yes · 7/7** (per `causa-planner-brief.md §2.2`) |
| Does Causa inherit the full L1–L9 tuple verbatim per AC-1? | **Yes · stacked-editorial · B · absent · essay-with-anchors · hero-overlay · single-portrait-feature · magazine-grid · split-wordmark-top · 4-col-with-whistleblowing** |
| Does Causa flip any cell that would force LF-{NEW}? | **No · zero cell flips · the brief locks the inheritance verbatim** |
| Does Causa's audience verb conflict with any of the 5 live verbs (interview · read · schedule · declare · entrust)? | **No · Causa = "plead" · genuinely unclaimed** |
| Does Causa's proof tactic conflict with any of the 5 live tactics (numeric Pragma/Fiscus · curatorial-architectural Cornice · qualitative-method Solaria · longitudinal Continua)? | **No · Causa = public-record · genuinely unclaimed** |

**Outcome 1.2**: **GO** · LF-2 second-occupant binding is canonical.

### 1.3 · Family validity composite outcome

**§1 outcome: GO** · LF-2 second occupancy is the correct binding for Causa. No family-level preconditions block A.3 entry.

---

## §2 · Palette collision risk

### 2.1 · Per-sibling per-token collision read

| Sibling | Sibling primary | Sibling accent | Causa primary collision | Causa accent collision | Polarity strategy collision |
|---|---|---|---|---|---|
| Pragma | navy `#1E293B` | emerald `#10B981` | Causa `#14342B`-class is bottle-green · NOT navy · ≥large ΔE | obsidian `#0B0A0E` is deep neutral · NOT emerald · ≥large ΔE | Pragma = full-cool · Causa = full-cool — **same axis** but different hue family + different polarity sub-strategy (matte-on-matte vs cool-cool-with-emerald) |
| Cornice | graphite `#1c1d20` | terracotta-rust `#a14a2c` | Causa bottle-green ≠ graphite (different hue · greener · less neutral) · safely distinct on cream | obsidian ≠ rust (opposite warmth · matte vs warm-display) · safely distinct | Cornice = neutral-with-warm-display-only-rust · Causa = full-cool-matte-on-matte — opposite warmth axis |
| Fiscus | dark gray-blue `#1F2937` | deep navy `#1C3D5A` | Causa bottle-green ≠ gray-blue (different hue family) | obsidian ≠ deep navy (matte neutral vs blue-saturated) | Fiscus = mixed (warm sec + cool acc) · Causa = full-cool-matte — different polarity strategy |
| Solaria | warm dark carbon `#2B2A28` | warm caramel `#8B5A2B` | Causa bottle-green ≠ warm carbon (cool vs warm) | obsidian ≠ caramel (matte vs warm-display) | Solaria = full-warm · Causa = full-cool — opposite axis |
| Continua | **pine `#0F3A30`** | **brass `#B0875E`** | **Causa bottle-green target `#14342B`-class — closest neighbour · estimated ΔE ~6-8 on the 7-bit RGB read · planner must verify ≥6 ΔE at A.5 build** | obsidian ≠ brass (matte neutral vs warm chrome) · zero metallic deployment | Continua = cool-cool-with-WARM-CHROME-METALLIC · Causa = full-cool-matte-on-matte-NO-METALLIC — opposite metallic strategy |

### 2.2 · Continua adjacency · the load-bearing risk

The single highest palette risk is Causa primary `#14342B`-class vs Continua pine `#0F3A30`. They are both deep cool greens. The planner's three-vector mitigation:

1. **Hex distance verification at A.5**: target ≥6 ΔE on perceptual distance (visible at 1 second on side-by-side test). If `#14342B` lands within 6 ΔE of `#0F3A30`, the planner shifts the target to `#163C2F` or `#1F4438` to widen distance. This is an A.5 build-time verification; the Causa primary is locked at the *class* (bottle-green, not pine) at A.2 and at the *exact hex* at A.5.
2. **Polarity strategy differentiator**: Continua deploys brass as warm chrome (nav wordmark accent · footer crest); Causa deploys obsidian as body-typographic-only (drop-cap · pull-quote em · CTA fill optional · focus ring). The third polarity dimension (`matrix §1.3 · matte-on-matte without metallic`) makes the polarity strategies opposite even where the primary cool tone is adjacent.
3. **Subject-class differentiator**: Continua hero = library reading-room interior · interior-warm-mahogany · horizontal partner-desk. Causa hero = empty courtroom interior · cool-light · vertical timber + bone walls · zero mahogany · zero books-on-desk. The 1-second material/temperature read is opposite even where the green primary is adjacent.

The combined polarity-vector + subject-class differentiator means a residual ΔE 4-6 on primary still produces a non-collision read. The verification still fires at A.5.

### 2.3 · Cornice palette collision read

Causa secondary = bone `#F0EBE0`-class · Cornice secondary = pietra-serena `#cdc9c0`. The bone is **warmer + lighter** on cream than pietra-serena. The risk: at low contrast, both read as "warm cream-grey paper." Mitigation: at A.5 build, the planner ships bone with a yellow-channel offset such that the navbar masthead `CAUSA / studio legale` reads warmer than Cornice's `CORNICE / studio di architettura` on side-by-side capture. Verification: side-by-side 1920 capture test at A.6 review-lock against Cornice frozen.

### 2.4 · Polarity strategy uniqueness across cluster

| Sibling | Polarity strategy | Causa equivalent? |
|---|---|---|
| Pragma | cool-cool (full cool · cool-saturated accent) | No · Causa is matte-on-matte not cool-saturated |
| Cornice | neutral-with-warm-display-only-rust | No · Causa has zero warm display |
| Fiscus | warm-sec + cool-acc (mixed) | No · Causa is full-cool |
| Solaria | warm-on-warm (full warm) | No · Causa is full-cool |
| Continua | cool-cool-with-warm-chrome-only-metallic | No · Causa has zero metallic |
| **Causa** | **full-cool-matte-on-matte-zero-metallic** | **Unique third polarity dimension** per matrix §1.3 |

Causa occupies a previously unclaimed polarity strategy. This is the strongest single-axis differentiator in the brief.

### 2.5 · Palette collision composite outcome

**§2 outcome: HOLD** · the composite is GO at the polarity-strategy axis (uniqueness clear), but the Continua pine adjacency requires an explicit hex-distance verification at A.5 build (≥6 ΔE on perceptual distance) before the build can ship. The HOLD is **NOT** an A.3 blocker — A.3 imagery curation can begin without the hex lock. The HOLD lifts at A.5 with a single side-by-side test against Continua home.

**Mitigation owner**: planner at A.5 build · target window: A.5 step "tokens.css authoring."
**Mitigation cost**: 1 hex shift OR 0 if `#14342B`-class lands ≥6 ΔE on first authoring.
**Escalation if mitigation fails**: shift to `#1F4438` (deeper) or `#163C2F` (slightly bluer) · still in bottle-green class · still cool-on-cool · re-test against Continua.

---

## §3 · Imagery feasibility risk

### 3.1 · New pool `business-legale` feasibility

| Probe | Reading |
|---|---|
| Does a Pexels search for "courtroom interior empty" return ≥10 candidate URLs at premium quality (≥1920 width · landscape · zero people)? | **Likely yes** · the pool category is well-populated on Pexels (search-term volume estimate: courtroom architecture interior + aula tribunale + supreme court chamber + judicial bench all have ≥30 results per term) |
| Are 6 of those URLs available with cool-light + vertical timber/bone walls (NOT warm-mahogany horizontal partner-desk · NOT golden-hour stone)? | **Likely yes · planner-confidence MEDIUM-HIGH** · cool-lit empty courtrooms are common in Pexels' architecture sub-pool · the curator escape hatch at A.3 (codex-spread fallback) covers the case where ≥4 courtroom URLs cannot be sourced |
| Does the curator escape hatch (legal-codex spread) have its own sub-pool? | **Yes** · "open law book annotated" / "law tome desk" / "codice civile" returns ≥20 results · risk = visual proximity to Fiscus desk · mitigated by close-up zoom |
| Are 4 case-card photos sourceable in the same pool with zero overlap on hero + portrait? | **Likely yes** · case-card photos can include: courtroom architectural detail · law-codex close-up · gavel detail · scales of justice (cliché — to be avoided) · supreme-court bench detail · forensic-document detail |
| Is the leadership portrait (senior Cassazionista in chambers · 50s-or-senior · environmental-NOT-studio-backdrop) sourceable? | **Risk: MEDIUM** · environmental portraits of senior lawyers in chambers are less common than corporate-headshot stock · curator must filter aggressively at A.3 · planner-binding triple (50s-or-senior + chambers-with-codices-mid-ground + environmental-NOT-studio-backdrop) is the audit checklist · per R-LF2-1 · this is a known LF-2 risk inherited from Cornice's enrollment |
| Does CS-IMG-SRC-04 zero-overlap grep automate the cluster-pool isolation? | **Yes** · existing automation greps `business-{corporate,architecture,fiscal,coaching,stewardship}` URL lists vs new pool · ships a CI gate |

### 3.2 · The leadership portrait risk · single-portrait stock-headshot collapse (R-LF2-1)

This is the single highest imagery risk and the one that bit Cornice at A.6 review-lock (the Marta vs Marco gender-mismatch on the portrait). For Causa, the planner mandates:

- Curator at A.3 binds the **environmental composition triple** BEFORE A.5 build:
  1. Subject = 50s-or-senior (visible age cue · NOT 30-something).
  2. Environment = chambers + codices + vertical timber wainscoting (zero drafting tools · zero mahogany partner-desk).
  3. Framing = 3/4 environmental (the room is half the subject) · NOT flat-light LinkedIn-style headshot.
- Curator at A.3 sources **2-3 portrait candidate URLs** (not 1 · the planner reviews finalists at A.4 with founder-identity gender lock).
- Founder gender / name / pronouns locked at A.5 build · the portrait selection drives the gender lock OR the gender lock drives the portrait selection · the planner picks one path at A.5 entry and stays consistent across all surfaces.

### 3.3 · Imagery feasibility composite outcome

**§3 outcome: GO with HOLD on R-LF2-1** · the pool is feasible · the courtroom interior subject is sourceable · the case-card photos are sourceable · the leadership portrait carries the LF-2 family-shared risk that requires curator binding at A.3 BEFORE A.5 build. The HOLD is the curator's deliverable at A.3 (not a planner-brief amendment).

**Mitigation owner**: imagery curator at A.3.
**Mitigation cost**: 1 curator pass · environmental-composition-triple binding · 6 URLs minimum · 2-3 portrait finalists.
**Escalation if A.3 cannot source 6 courtroom URLs at the cool-light + zero-mahogany filter**: invoke the codex-spread backup subject class (per `causa-planner-brief.md §4`) for ≤2 case cards while preserving the courtroom hero · OR widen pool to "supreme court chamber" / "legal aula" Italian-EU search.

---

## §4 · Content-volume estimate

### 4.1 · Per-section content volume read

| Section | Content units required | Volume estimate | Source |
|---|---|---|---|
| Hero h1 + side-quote | 1 anchor sentence (with em on `evidenza`) + 1 side-quote with verb-form em | ~30-40 words IT | LF-2 family-shared (Cornice precedent · 35 words) |
| Hero KPI tuple | 3 cells: `(N landmark sentenze · pubblicazioni in massimario · anni di patrocinio)` | 3 short numerical phrases · ~12-15 words | LF-2 family-shared |
| Hero credit overlay caption | `(Albo Avvocati Milano · Cassazionista dal AAAA)` | ~6 words IT | Causa-specific |
| Narrative essay (slot-2) | 1 drop-cap paragraph + 2 paragraphs + 3 pull-quotes (each 1 short sentence with em-word) | ~250-300 words IT · matches Cornice essay length (Cornice = ~280 words) | LF-2 family-shared |
| Sticky 4-link side-rail labels | `Studio · Materie · Pubblicazioni · Contatti` | 4 labels · ~6 words | Causa-specific |
| Sectors ribbon (slot-3) | 12 typology cells (Penale tributario · Civile contrattualistica · etc.) | 12 short labels · ~24 words | Causa-specific (planner-locked at brief §7) |
| Leadership single (slot-4) | h2 + role + 2-paragraph bio + 4 credentials | ~150-180 words IT · matches Cornice leadership length | LF-2 family-shared |
| Cases magazine grid (slot-5) | 4 cases · each = eyebrow + h3 + body (2-3 lines) + pill-link · 1 hero + 3 small | ~200-260 words IT total (heavier on hero card) | LF-2 family-shared |
| CTA closer (slot-6) | h2 (anchor verbatim) + body sentence + primary CTA copy + secondary action | ~40-50 words IT | LF-2 family-shared |
| Navbar 5-link labels | `Studio · Materie · Pubblicazioni · Contenzioso · Contatti` | 5 labels · ~10 words | Causa-specific |
| Footer 4 columns + whistleblowing | column headings + content + D.lgs. 24/2023 channel + privacy reference | ~100-120 words IT | Sub-cluster-specific (forensic firm) |
| **Home page IT total** | | **~830-1,030 words** | |

### 4.2 · Multi-locale volume read (workflow C)

| Locale | Multiplier | Total words estimate |
|---|---|---|
| IT | 1.0x | ~830-1,030 |
| EN | 0.95x (typical IT-to-EN density) | ~790-980 |
| FR | 1.05x (typical IT-to-FR density) | ~870-1,080 |
| ES | 1.00x | ~830-1,030 |
| AR | 0.85x (typical IT-to-AR density) | ~700-880 |
| **5-locale total** | | **~4,020-5,000 words across home alone** |

### 4.3 · Case-detail page volume (registry-only · 4 detail pages)

Each case-detail = sentence citation + body summary + outcome + role-of-firm. Per Chiara/A.13 precedent, detail pages render from registry · NO per-template detail-page templates. Estimated 150-200 words IT per detail · 4 detail × 5 locales = 20 routes · ~750-1,000 words IT total · ~3,500-4,500 words across 5 locales.

### 4.4 · Other home-band feeds (case-parent slug + cases-parent fallback)

Per `phase_x4_corporate_suite_case_parent_fix.md` (closed 2026-04-29), the corporate-suite cluster shares `cases_parent_slug` resolver. Causa inherits this — the case-parent fallback for `home.html:660` works automatically; no Causa-specific code edit needed. Volume: 0 additional content.

### 4.5 · Content-volume composite outcome

**§4 outcome: GO** · ~830-1,030 IT words for home + ~750-1,000 IT for case details = ~1,580-2,030 IT words total · scaling to ~7,500-9,500 words across 5 locales. This is **comparable to Cornice's authoring envelope** (~1,800 IT words at A.5 + ~7,500 across 5 locales at workflow C). No content-volume blocker for A.3 entry.

The content authoring is workflow A.4 (Phase X.6 Step 3) · NOT A.3 · NOT this brief. Volume estimate confirms feasibility within the standard A.4 budget.

---

## §5 · Remove-the-studio-name test (CS-TONE-05) at paper level

The CS-TONE-05 test is the cluster's load-bearing tonal-distinctness probe: "if the studio name is removed from the entire site, would a reader still identify this firm at first scroll?" The paper-level pass at the planner-brief level looks at the textual / visual signals only (no live render).

### 5.1 · The 1-second read without `CAUSA / studio legale`

Reading the brief's locked DNA + section rhythm, what does a wordmark-stripped Causa home produce in the first 30 seconds?

| Signal | Causa's reading without wordmark |
|---|---|
| Hero photo | empty courtroom interior · cool-light · vertical timber + bone walls · zero people |
| Hero h1 anchor sentence | `Ogni sentenza è un'evidenza incardinata, non un'opinione difesa.` |
| Hero KPI tuple | `(landmark sentenze · pubblicazioni in massimario · anni di patrocinio)` |
| Hero credit overlay | `(Albo Avvocati Milano · Cassazionista dal AAAA)` |
| Narrative essay drop-cap + 3 pull-quotes | forensic-publication register · em-words on legal nouns (`evidenza · incardinata · giurisdizione`) |
| Sectors ribbon | `Penale tributario · Civile contrattualistica · Amministrativo regolatorio · Contenzioso bancario · Responsabilità professionale · …` |
| Leadership single | senior Cassazionista in chambers · `Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario` |
| Cases magazine | 4 cards citing `Cass. civ. sez. III · Cass. SS.UU. · TAR Lombardia · Corte d'Appello` shapes |
| CTA closer | `Apri un parere preliminare` · parere-screening intake |
| Navbar (wordmark stripped) | cream-paper masthead · `Studio · Materie · Pubblicazioni · Contenzioso · Contatti` · filled-bottle-green CTA pill |

### 5.2 · The 1-second read

Without the wordmark, the reader sees: an empty courtroom · landmark sentenze · Cassazionista · ENCA · pubblicazioni in massimario · sectors ribbon of legal practice areas · case cards citing real Italian sentence shapes · "Apri un parere preliminare." The first 30-second read is **unmistakably "this is an evidence-led Cassazionista boutique."** The wordmark is not load-bearing; the studio's identity reads from the surfaces alone.

### 5.3 · Distinguishability vs all 5 live siblings on wordmark-stripped read

| Sibling | Wordmark-stripped 1-second read | Causa wordmark-stripped read | Collapses? |
|---|---|---|---|
| Pragma | navy + emerald · boardroom long-table · KPI tuple `(HQ · Equipe · Mandati)` · "Fissa una call privata" | bottle-green + bone · empty courtroom · KPI `(landmark sentenze · pubblicazioni · patrocinio)` · "Apri un parere preliminare" | NO |
| Cornice | graphite + pietra-serena + rust · Bologna golden-hour portico · `(novanta fascicoli · 2008 · 38 menzioni)` · `argomento` em · "Apri un fascicolo progetto" | bottle-green + bone + obsidian · empty courtroom · landmark sentenze · `evidenza` em · "Apri un parere preliminare" | NO |
| Fiscus | warm-neutral + blu-notte + gold · tidy desk + documents · fiscal-calendar slot-4 · "Primo appuntamento" + P.IVA gate | bottle-green + bone + obsidian · empty courtroom · NO calendar · NO P.IVA gate · forensic intake | NO |
| Solaria | warm-carbon + ocra + caramel · 1:1 conversation · two-em contrast pair (`terapia/consulenza`) · "Prenota una discovery call" | bottle-green + bone + obsidian · empty courtroom · ONE em on `evidenza` · "Apri un parere preliminare" | NO |
| Continua | pine + pewter + brass · library reading-room mahogany · governance-cycle pillars · "Avvia un dialogo di mandato" | bottle-green + bone + obsidian · empty courtroom (cool-light · timber+bone · zero mahogany) · narrative essay · "Apri un parere preliminare" | NO (cool-cool adjacency mitigated by polarity strategy + subject material register) |

### 5.4 · CS-TONE-05 composite outcome

**§5 outcome: GO** · the wordmark-stripped Causa home reads unmistakably as an evidence-led Cassazionista boutique · zero collapse into any of the 5 live siblings · the audience verb "plead" is communicated by the surfaces alone · CS-TONE-05 passes at paper level. Live verification at A.6 review-lock will re-run this test on the rendered home page · the paper test is a precondition · not a substitute.

---

## §6 · Other prebuild verifications

### 6.1 · Booking-flag cohort

| Probe | Reading |
|---|---|
| Does Causa belong in `has_booking=False` cohort? | **Yes · litigation-shaped · parere-screening (NOT scheduled-booking)** |
| Does the cohort test (`apps/catalog/tests.py · test_medical_and_restaurant_templates_have_booking_flag`) need an explicit Causa entry? | **Likely yes · 1 explicit-literal test edit at A.5 build · adds Causa to FALSE cohort · NOT a behavior change** |
| Risk: pre-existing booking-flag failure (per memory · `545/546 tests`) | **Pre-existing · NOT Causa-introduced · Causa build does not regress this further · planner monitors at A.5 walk** |

**§6.1 outcome**: GO at paper level · 1 test edit at A.5 build (not a Step 1 blocker).

### 6.2 · Frozen-sibling regression budget

| Probe | Reading |
|---|---|
| Do all 5 frozen siblings (Pragma · Cornice · Fiscus · Solaria · Continua) currently render 200 anonymous? | **Yes per Cornice flip log** (`phase_x5_cornice_public_flip.md` · 4/4 frozen siblings 200 + Cornice 200 · 5/5 anon) |
| Does Causa A.5 build risk drift on any frozen sibling? | **No · the build path adds 1 new template + new pool · no shared template edits · no cluster-CSS edits planned** |
| Walk gate F2-WALK-12 (5 × 200 anonymous + 0 px wireframe drift) — is this gate locked into A.6? | **Yes · per LF-2 walk gates (`cornice-lf2-reference-pack.md §7`)** |

**§6.2 outcome**: GO · zero frozen-sibling risk visible at planner level.

### 6.3 · Test-suite delta estimate (at A.5)

| Edit | Estimate |
|---|---|
| New template tests | ~5-7 dedicated tests (mirrors Cornice's enrollment pattern) |
| Booking-flag cohort entry | 1 explicit-literal edit |
| Catalog-count tests at flip (NOT at A.5) | 7 explicit-literal bumps (24→25 · "24+"→"25+") · workflow D / public flip · NOT A.5 |
| Related-templates limit re-binding (if Causa promotion bumps anyone past category-fallback ceiling) | 0-1 edit · workflow D / public flip · NOT A.5 |
| Total at A.5 | **~6-8 test edits** |
| Total at workflow D (flip cascade) | **~7-8 test edits** |

**§6.3 outcome**: GO · estimate is in line with Cornice's (~7-9 edits at A.5 + flip).

### 6.4 · Catalog count and tier sequence

| Probe | Reading |
|---|---|
| Current catalog count | **24 published_live / 0 draft** (per memory · post-Cornice flip 2026-05-01) |
| Causa A.5 lands as | `+1 draft` → 24 published_live / 1 draft |
| Causa workflow D / public flip lands as | `tier=draft` → `tier=published_live` → 25 published_live / 0 draft |
| Counter cascade | home counter `24+` → `25+` · catalog header `25 template disponibili` |

**§6.4 outcome**: GO · cascade is mechanical · matches Cornice precedent.

### 6.5 · Editor / projects / commerce isolation

| Probe | Reading |
|---|---|
| Does Causa A.5 require an `apps/editor/` change? | **No** · enrollment is closed (per memory · A.6 → A.17b CLOSED 2026-04-20) · Causa is corporate-suite SIBLING build · NOT editor enrollment |
| Does Causa A.5 require an `apps/projects/` change? | **No** |
| Does Causa A.5 require an `apps/commerce/` change? | **No** |

**§6.5 outcome**: GO · respects the editor program closure · zero apps/editor/projects/commerce surface area at A.5 build.

---

## §7 · Outcome roll-up

| Check | Outcome | Notes |
|---|---|---|
| §1 family availability + LF-2 second-occupant validity | **GO** | LF-2 occupied 1/N · multi-occupant by intent · 7/7 family questions clear · L1–L9 inheritance verbatim |
| §2 palette collision risk | **HOLD** | Continua pine adjacency requires ≥6 ΔE hex-distance verification at A.5 · NOT an A.3 blocker · polarity strategy uniqueness clear |
| §3 imagery feasibility risk | **GO with HOLD on R-LF2-1** | Pool feasible · curator binds environmental-composition-triple at A.3 · 2-3 portrait finalists |
| §4 content-volume estimate | **GO** | ~830-1,030 IT home + ~750-1,000 IT case-details · scales to ~7,500-9,500 across 5 locales · matches Cornice envelope |
| §5 remove-the-studio-name test (CS-TONE-05) at paper level | **GO** | Wordmark-stripped read = "evidence-led Cassazionista boutique" unmistakably · zero collapse vs 5 live siblings |
| §6.1 booking-flag cohort | **GO** | 1 explicit-literal test edit at A.5 |
| §6.2 frozen-sibling regression budget | **GO** | Zero risk visible at planner level |
| §6.3 test-suite delta estimate | **GO** | ~6-8 edits at A.5 · ~7-8 at flip |
| §6.4 catalog count + tier sequence | **GO** | Mechanical cascade · matches Cornice |
| §6.5 editor / projects / commerce isolation | **GO** | Zero surface area |

### Composite gate outcome

**Overall: GO to A.3 imagery curation.** The two HOLDs are NOT A.3 blockers:

- The §2 palette HOLD lifts at A.5 build (hex-distance verification · single side-by-side test).
- The §3 R-LF2-1 HOLD lifts at A.3 (curator binds environmental-composition-triple as the deliverable of A.3 itself).

There is **NO RESPEC**. The planner brief's preconditions hold. Phase X.6 Step 1 closes on this gate. Phase X.6 Step 2 = A.3 imagery curator pack may begin.

---

## §8 · The exact next action after this gate

> On orchestrator sign-off of `causa-planner-brief.md` + `causa-distinctness-proof.md` + this checks file, open Phase X.6 Step 2 = workflow A.3 imagery curator pack at `factory/reports/causa/causa-imagery-pack.md`. The curator's deliverables are: (a) 6 Pexels URLs minimum in NEW `business-legale` pool (zero overlap grep against `business-{corporate,architecture,fiscal,coaching,stewardship}`); (b) environmental-composition-triple binding for the leadership portrait (50s-or-senior + chambers-with-codices-mid-ground + environmental-NOT-studio-backdrop · 2-3 finalists for planner review); (c) hero subject class shortlist (≥4 courtroom-interior URLs · cool-light · zero people · vertical timber + bone walls · zero mahogany · zero golden-hour · zero portico exterior); (d) 4 case-card photos with zero overlap on hero + portrait; (e) backup codex-spread URLs as escape hatch if courtroom pool is too thin. **No application code, registry, or tier change at Step 2.**

This file is **paper-only**. It is the prebuild gate; A.3 is the imagery deliverable.
