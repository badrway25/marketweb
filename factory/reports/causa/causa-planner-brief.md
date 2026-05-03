# Causa · planner brief (workflow A.2)

**Status**: paper-only · Phase X.6 Step 1 · workflow A.2 planner brief · NOT a build authorization
**Date**: 2026-05-03
**Template**: Causa (`causa-legale`) · corporate-suite 6th sibling · LF-2 second occupant
**Scope**: paper layer for A.3 imagery curation · zero application code · zero registry change · zero tier change · zero apps/{editor,projects,commerce} touch · zero new archetype
**Sources**: `factory/reports/hardening/sixth-sibling-territory-scout.md` · `design-orchestrator/real-candidates/sixth-sibling-{shortlist,recommended-intake}.md` · `cornice-lf2-reference-pack.md` · `corporate-suite-{distinctness-matrix,reference-pack,layout-family-assignment,live-family-map}.md` · `next-template-brief-schema.md`
**Companion files written same pass**: `causa-prebuild-quick-checks.md` · `causa-distinctness-proof.md`

---

## §1 · DNA

The single source of truth for the Causa template, locked at planner level. Every downstream pass (A.3 curator · A.5 builder · A.6 critic · A.7 walker) reads this section as the contract.

| Field | Value |
|---|---|
| `template_slug` | `causa-legale` |
| `studio_name` | **Causa** (working name; planner does NOT re-bid at A.2 — the name is locked in `sixth-sibling-recommended-intake.md §1`) |
| `wordmark_descriptor_pair` | `CAUSA / studio legale` (split-line masthead · cream-paper navbar `cs-nav--lf2`) |
| `cluster` | `corporate-suite` |
| `sub_cluster_label` | `studio-legale-cassazionista` · evidence-led litigation boutique |
| `family` | **LF-2 second occupant** · inherits L1–L9 verbatim per `cornice-lf2-reference-pack.md §AC-1` |
| `family_hypothesis_status` | locked at intake (`sixth-sibling-recommended-intake.md §2`) · NOT re-opened at A.2 |
| `audience_profile` | imprese e privati con contenzioso complesso · ricorsi in Cassazione · responsabilità professionale · contenzioso bancario · contenzioso tributario · diritto amministrativo regolatorio · ENCA / Albo CTU expert testimony engagements |
| `org_scale` | 1 senior Cassazionista (50s-or-senior · founder · single-principal masthead) + 2-3 associati + 1 segreteria · 1 sede Milano (NOT Bologna · NOT Rome — geographic adjacency rules in §3) |
| `org_form` | studio individuale di avvocato cassazionista (NOT studio associato · NOT società tra avvocati STA · NOT family-office · NOT consultancy boutique) |
| `audience_verb` | **plead** (the visitor is asking whether this firm will litigate a complex case before a court — the sixth verb is genuinely unclaimed in the cluster) |
| `proof_tactic` | **public-record** · sentenze citate · giurisprudenza · pubblicazioni in massimario · expert testimony engagements (the sixth proof tactic the catalog is missing) |
| `voice_anchor_noun` | `evidenza` · 5-locale set: `evidenza → evidence → preuve → evidencia → دليل` · em-word strategy = ONE em per heading on `evidenza` (NOT two-em contrast pair · Solaria's exception is forbidden here) |
| `voice_anchor_sentence_IT` | `Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.` |
| `voice_anchor_recurrence` | exactly 2 home surfaces · hero h1 + cs-cta-closer-cream h2 · per AC-15 |
| `register` | `Lei` polite Italian · forensic-publication voice · third-person studio voice (`Lo studio incardina · Lo studio sostiene`) · adversarial-resolution stance |
| `tone_label` | evidence-first · litigation-precise · public-record register |
| `stakeholder_one_liner` | "evidence-led Cassazionista litigation · public-record proof" |
| `heading_serif` | **GT Sectra** · primary · with **Source Serif Pro** as licence-fallback declared at planner level (NOT re-decided at A.5) |
| `body_sans` | **Manrope** · NO fallback (Inter is forbidden per CS-LAYOUT-20 · 3rd cluster use collapses body-sans differentiation) |
| `palette_primary` | bottle-green · target token `#14342B`-class · L\* ≤ 40 on cream · `is_primary_safe_on_cream()` PASS · explicitly NOT pine `#0F3A30` (Continua) |
| `palette_secondary` | bone · target token `#F0EBE0`-class · warmer than pietra-serena `#cdc9c0` (Cornice) · cooler than fiscus warm-neutral cream |
| `palette_accent` | obsidian · target token `#0B0A0E`-class · deep neutral · **zero metallic** |
| `polarity_strategy` | full cool · matte-on-matte · zero metallic — third polarity dimension per matrix §1.3 ("matte-on-matte without metallic"); opposite of Continua's "cool-with-warm-chrome-metallic-only" |
| `accent_deployment_surfaces` | obsidian = body-typographic-only (drop-cap accent · pull-quote em · CTA fill optional · focus ring) · obsidian NEVER deploys as metallic chrome (different surface-class from Continua's brass) |
| `target_tier` | `draft` · per D-102 default · public flip held until explicit user handshake (R-SOL-8 / CS-BLOCK-13 / D-102 cadence · same shape as Solaria + Continua + Cornice flips) |
| `locales_at_A5` | `[it]` only · per D-102 cadence · others added at workflow C |
| `locales_at_workflowC` | 5 locales · IT preserved + EN/FR/ES/AR added · AR `dir=rtl` parity with Naskh h1 (LF-2 family-scoped) |
| `pexels_pack_status` | `not started` at A.2 · `curator briefed` is the deliverable of A.3 (this brief authorizes A.3 to begin) |
| `image_pool` | new pool `business-legale` · Pexels-only · 6 URLs minimum · zero overlap grep against `business-{corporate,architecture,fiscal,coaching,stewardship}` (CS-IMG-SRC-04) |
| `motion_posture` | inherited cluster invariant · low motion · staggered reveals · `prefers-reduced-motion` honored · NO marquee (LF-2 family signature inherited from Cornice) · do NOT differentiate Causa via motion |
| `booking_flag` | likely `has_booking=False` · litigation-shaped (parere-screening, NOT scheduled-booking) · planner verifies cohort at A.5 build against `apps/catalog/tests.py · test_medical_and_restaurant_templates_have_booking_flag` |

---

## §2 · Family-fit argument · why LF-2 second occupant is the correct binding

### 2.1 · The fit matches LF-2's reference profile to the line

`corporate-suite-live-family-map.md §4` enumerates LF-2 second-occupant fit as: "portfolio-of-work-led firm whose proof IS its case studies (evidence-led litigation · independent directorship case-bundle · audit-led methodology with published methodology pieces · longitudinal research practice with publications)." **Evidence-led litigation is the FIRST item on that list.** The fit is canonical, not stretched.

### 2.2 · The 7 family questions clear at intake

Per `cornice-lf2-reference-pack.md §9` the LF-2 candidate must answer 7 questions. Causa's answers, locked from `sixth-sibling-recommended-intake.md §11`:

1. **Portfolio-of-work-led professional fit?** YES. A Cassazionista boutique's proof IS its case-bundle (sentenze citate, giurisprudenza, expert testimony in massimario, ENCA mediations). The firm pleads cases; its history is its publication.
2. **≥4 publishable case studies with editorial weight?** YES. A real Cassazionista boutique typically has multiple landmark sentences per year; Causa's content brief at A.4 ships 4 cases (1 hero landmark + 3 supporting · all public-record).
3. **Voice register tolerates a curatorial noun anchor?** YES. `evidenza` lands as a forensic-publication noun, not a service-oriented or outcome-oriented one. The em recurrence reads as a method statement, not a marketing claim.
4. **Hero subject differs materially from Bologna golden-hour portico?** YES. Empty courtroom interior · cool light · zero people · vertical timber + bone walls. Different geographical (courtroom-not-portico), different material (timber+bone-not-stone), different temperature (cool-not-golden-hour) registers.
5. **Single principal whose portrait carries the masthead?** YES. Single-principal Cassazionista (the firm's founder · 50s-or-senior). 2-3 associati support but do NOT appear on the masthead.
6. **Compliance posture warrants 4-col-with-whistleblowing footer?** YES. D.lgs. 24/2023 applies to the Italian forensic firm cohort — the 4th column carries the firm's whistleblowing channel (responsabile della prevenzione · email · privacy reference). Sub-cluster-specific content per AC-12.
7. **Heading serif / body sans / palette / CTA-noun all clear vs Cornice on the matrix?** YES. GT Sectra ≠ Cormorant Garamond · Manrope ≠ Source Sans 3 · bottle-green+bone+obsidian ≠ graphite+pietra-serena+rust · `evidenza` ≠ `argomento` · "Apri un parere preliminare" is NOT a fascicolo cognate per AC-8.

7 of 7 family questions clear. The LF-2 second-occupant intake is authorized at the family-fit level.

### 2.3 · L1–L9 inheritance (locked verbatim)

Causa ships the LF-2 9-cell tuple verbatim. **Do not flip cells.** A flipped cell exits the family and forces an LF-{NEW} declaration.

```
L1 · stacked-editorial          (full-bleed photo TOP · 8/4 below-fold typographic)
L2 · B section sequence         (cs-hero · cs-narrative · cs-sectors-ribbon · cs-leadership-single · cs-cases-magazine · cs-cta-closer-cream)
L3 · absent                     (no named cadence cell · narrative essay covers role)
L4 · essay-with-anchors         (drop-cap p1 · 3 pull-quotes · sticky 4-link side-rail)
L5 · hero-overlay               (KPI inside hero photo's bottom-left credit-overlay frame)
L6 · single-portrait-feature    (1 environmental portrait + 2-paragraph bio + 4 credentials)
L7 · magazine-grid              (3+1 · 1 hero card spans rows 1-3 + 3 small cards stacked)
L8 · split-wordmark-top         (cream-paper navbar · split-line masthead · filled trailing CTA · NO phone-right)
L9 · 4-col-with-whistleblowing  (4th column = forensic-firm D.lgs. 24/2023 channel)
```

### 2.4 · LF-2 family signatures inherited verbatim (per `cornice-lf2-reference-pack.md §6`)

- Cream-paper navbar (`cs-nav--lf2`) shape · split-line masthead · filled trailing CTA pill · 5-link inline · NO phone-right.
- Zero dark bands on home (CS-TONE-03 family-scoped demotion · do NOT introduce a dark band to "ground the page" — that breaks the family's editorial register).
- LF-2-scoped Naskh AR h1 swap (`html[dir="rtl"] body.cs-lf-lf-2 { --heading: 'Noto Naskh Arabic', ... }` · do NOT re-bind selector to a sub-class · do NOT move scope to `:root`).
- Hairline-bordered cream CTA closer with voice anchor verbatim recurrence (filled-bottle-green CTA pill on cream paper · NOT dark band).
- Sticky 4-link side-rail in the narrative band.
- Three pull-quotes interspersed in the narrative essay (each with own italic em-word).
- Drop-cap on paragraph 1 of narrative (84px serif · accent-tinted · obsidian-tinted on cream).
- KPI tuple inside hero photo's bottom-left credit-overlay frame (NOT on a dark band · NOT in meta-strip · NOT on the typographic side).
- Single-portrait masthead requiring environmental-not-studio framing (the room is half the subject).
- Magazine 3+1 grid for cases (1 hero card spans rows 1-3 + 3 small cards stacked).
- Voice anchor verbatim on EXACTLY 2 home surfaces (hero h1 + CTA closer h2).

### 2.5 · LF-6 first-occupant rejection (locked at intake)

The territory scout rejected LF-6 first occupant for sibling 6 because: (a) it bundles family-extensibility-test with sub-cluster-build (multi-session unknown-cost diversion); (b) the LF-2 family must be proved repeatable BEFORE the cluster activates a new family. LF-6 is held for sibling 7 (Memoria · audit-led methodology). This brief does NOT re-open the LF-6 question.

### 2.6 · LF-{NEW} rejection (locked at intake)

A litigation boutique does not require a new layout grammar. Its proof is case-bundle; LF-2 was built for exactly that proof shape. Choosing LF-{NEW} would be over-claiming a difference that is in fact a sub-cluster variation inside an existing family. Held for sibling 8 (notarile boutique).

---

## §3 · Anti-collision rules vs all 5 live siblings

This section is the planner's binding ban list. The builder at A.5 reads this as the contract; the critic at A.6 reads this as the audit checklist. Each entry is the **specific cell** of the live sibling that Causa must NOT repeat.

### 3.1 · Must NOT repeat from Pragma (LF-1)

| Cell | Pragma's claim | Causa's required difference |
|---|---|---|
| Voice anchor | decisional gravity · `Lei` partner · CdA vocab | `evidenza` curatorial-thesis-NOT-cognate · forensic-publication register |
| Palette macro | navy + emerald + cream (cool advisory `#1E293B`/`#3B82F6`/`#10B981`) | bottle-green + bone + obsidian (full cool · matte-on-matte · zero metallic) |
| Heading serif | Merriweather | GT Sectra (NEVER Merriweather) |
| Body sans | Inter | Manrope (Inter explicitly forbidden — would be 3rd cluster use, collapses body-sans differentiation per CS-LAYOUT-20) |
| Hero geometry | split-55-45 grid | stacked-editorial (LF-2 inheritance · 9/9 layout-axis difference vs Pragma) |
| Hero subject | boardroom long-table · multi-partner advisory scene | empty courtroom interior · zero people · vertical timber + bone walls |
| Hero meta-strip | KPI tuple `(HQ · Equipe · Mandati)` as separate strip | KPI tuple lives inside hero photo's credit-overlay frame · cells = `(N landmark sentenze · pubblicazioni in massimario · anni di patrocinio)` |
| Section sequence | A · pillars + KPI band + leadership grid | B · narrative essay + sectors ribbon + single-portrait + magazine grid |
| Leadership feel | typographic-grid · 4-card partner row | single-portrait masthead · 1 environmental portrait + 4 credentials |
| Credentials | "Partner · Senior Associate · Counsel" titles | "Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario · Albo CTU" |
| Cases proof | list-row · anonymized client engagements | magazine-grid 3+1 · public-record sentences |
| CTA copy | "Fissa una call privata" | "Apri un parere preliminare" (parere-screening NOT booking) |

### 3.2 · Must NOT repeat from Cornice (LF-2 first occupant — load-bearing)

This is the highest-collision risk because Causa shares LF-2 with Cornice by intent. **Layout axes are family-shared (intentionally · per AC-2); skin axes must score ≥4/5 vs Cornice.** The list below is non-negotiable.

| Cell | Cornice's claim | Causa's required difference |
|---|---|---|
| Voice anchor noun | `argomento` · curatorial-thesis · `argomento → argument → argument → argumento → حُجَّة` | `evidenza` · public-record-evidence · `evidenza → evidence → preuve → evidencia → دليل` · explicitly NOT a curatorial-thesis cognate per AC-3 |
| Voice anchor sentence | `Ogni progetto è un argomento costruito, non un servizio reso.` | `Ogni sentenza è un'evidenza incardinata, non un'opinione difesa.` |
| Heading serif | Cormorant Garamond | GT Sectra (forensic-publication register · NOT architectural-press Garamond revival) |
| Body sans | Source Sans 3 | Manrope |
| Palette | graphite + pietra-serena + terracotta-rust (warm-display-on-cool-chrome) | bottle-green + bone + obsidian (full cool · matte-on-matte · zero metallic) |
| Accent deployment | rust deployed display-side-only (drop-cap · pull-quote em · CTA fill · focus ring · NEVER chrome) | obsidian deployed body-typographic-only (drop-cap · pull-quote em · CTA fill optional · focus ring) — same surface-class but different polarity (matte neutral vs warm display) |
| Hero subject | Bologna golden-hour portico · exterior · stone-warm · golden-hour shadow · "Italian classical architecture" 1-second read | empty courtroom interior · interior · cool light · vertical timber + bone walls · "litigation chamber" 1-second read · per AC-4 (NOT any northern-Italian-portico, NOT any golden-hour stone-architectural-shadow exterior) |
| Hero KPI tuple cells | `(novanta fascicoli · 2008 · 38 menzioni)` | `(N landmark sentenze · pubblicazioni in massimario · anni di patrocinio)` — same hero-overlay shape (LF-2 family-shared per AC-2), different cell content |
| Hero credit overlay caption | `(Direzione · Anno fondazione)` | `(Albo Avvocati Milano · Cassazionista dal AAAA)` |
| CTA copy | "Apri un fascicolo progetto" · fascicolo / dossier mental model | "Apri un parere preliminare" · parere-screening · evidence-and-jurisdiction intake · explicitly NOT in fascicolo / dossier semantic family per AC-8 (NOT "Apri un dossier" · NOT "Apri un fascicolo" · NOT "Open a brief" · NOT "Open a record" · NOT "Open a folder" · NOT "Open a case file") |
| Conversion form | project scope + budget range + timeline horizon (architecture intake) | oggetto del contenzioso · grado di giudizio attuale · controparte · fascia di valore · urgenza · evidenza preliminare allegabile · giurisdizione |
| Wordmark + descriptor | `CORNICE / studio di architettura · DAL 2008` | `CAUSA / studio legale` (different studio name AND descriptor pair · per AC-11) |
| 5-link nav labels | `Lo studio · Archivio · Servizi · Progetti · Contatti` | `Studio · Materie · Pubblicazioni · Contenzioso · Contatti` (5-link inline shape inherited per AC-11 · labels picked fresh) |
| Trailing CTA pill colour | filled-rust | filled-bottle-green (NOT rust · NOT brass · NOT emerald — match new accent · per AC-11) |
| Founder identity | Marta Roveri · feminine Italian · architect-with-drafting-tools | (planner authors fresh at A.4 · single-principal Cassazionista · gender-name-pronouns lock at A.5 · per R-LF2-2 mitigation: portrait + name + pronouns + role + bio + intro + team-card role + studio-founder-eyebrow ALL agree before A.6) |
| Leadership room props | drafting tools · architecture studio backdrop | chambers · codices · law tomes · zero drafting tools · per AC-9 environmental-not-studio binding |
| Leadership credentials | OAPPC Milano · MIBAC · monografia · concorsi | Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario · Albo CTU |
| Case slugs | `biblioteca-pietrasanta-concorso · via-volpe-roma-residenziale · palazzo-lignari-bologna-restauro · cornice-fronte-minore-saggio` | (planner authors fresh at A.4 · 1 landmark sentence + 3 supporting public-record cases) |
| Em-word set across home | `argomento · argomenta · geometria · lotto · argomento · minore` | (planner authors 12 fresh em-words at A.4 anchored on `evidenza` recurrence + forensic-publication register) |
| 4th footer column content | architecture studio's whistleblowing channel | forensic firm's whistleblowing channel · D.lgs. 24/2023 · responsabile della prevenzione (forensic-firm-appropriate name) · email · privacy reference · per AC-12 sub-cluster-specific |
| Pexels URLs | 6 URLs in `business-architecture` pool | 6 URLs in NEW `business-legale` pool · zero overlap grep against `business-architecture` (CS-IMG-SRC-04 enforces) |
| Geographic anchor | Bologna (case slug includes `bologna` · portico subject is Bolognese) | Milano (sede Milano · NOT Bologna · NOT Rome — explicit guardrail per intake §1) |

### 3.3 · Must NOT repeat from Fiscus (LF-3)

| Cell | Fiscus's claim | Causa's required difference |
|---|---|---|
| Voice anchor | adempimento corretto · presidio + scadenze | `evidenza` · forensic-publication |
| Palette | warm-neutral + blu-notte + gold (`#B58F4A`/`#1C3D5A`) | bottle-green + bone + obsidian |
| Heading serif | IBM Plex Serif | GT Sectra |
| Body sans | IBM Plex Sans | Manrope |
| Hero geometry | split-55-45 grid + slot-4 fiscal-calendar | stacked-editorial · NO calendar-strip |
| Hero subject | tidy desk + documents | empty courtroom interior · zero documents-on-desk |
| Hero meta-strip | fiscal-calendar `(mese · scadenza · ambito)` at slot-4 | KPI in hero overlay (LF-2 family-shared) |
| CTA copy | "Primo appuntamento" + P.IVA/CF intake | "Apri un parere preliminare" · NO P.IVA gate |
| Credentials | "Iscritto Sezione A · Cassazionista · Revisore Legale" | "Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario · Albo CTU" — Fiscus claims "Cassazionista" as a credential vocabulary item; Causa's masthead carries Cassazionista as the founder's actual title (the firm IS Cassazionista) — but the **credential set** must read forensic-publishing-register, NOT mixed-Albo+revisione register |

### 3.4 · Must NOT repeat from Solaria (LF-4)

| Cell | Solaria's claim | Causa's required difference |
|---|---|---|
| Voice anchor | `terapia` · `consulenza` contrast pair (TWO em-words) | `evidenza` · ONE em per heading (NOT two-em contrast pair · CS-EXEC-01 default) |
| Palette | warm-carbon + ocra + caramel (full warm) | bottle-green + bone + obsidian (full cool · matte-on-matte) |
| Heading serif | Fraunces | GT Sectra |
| Body sans | Inter (forbidden for Causa per CS-LAYOUT-20) | Manrope |
| Hero subject | 1:1 conversation | empty courtroom interior · zero people |
| Section sequence | C · manifesto + percorsi at slots 2-3 | B · narrative + sectors ribbon at slots 2-3 |
| L6 leadership | absent (single-practitioner exception) | single-portrait masthead · LF-2 SHIPS leadership · single-principal does NOT mean L6 omitted in LF-2 |
| Credentials | "ICF-PCC · EMCC Senior Practitioner · AICP" | forensic-publishing register |
| CTA copy | "Prenota una discovery call" | "Apri un parere preliminare" · NO discovery-call mental model |

### 3.5 · Must NOT repeat from Continua (LF-5 — closest palette/imagery adjacency · highest second-axis collision risk)

This is the **second highest collision risk** after Cornice. Continua is also cool-on-cool. Causa must prove non-collapse on three vectors: palette polarity, hero subject material register, leadership room props.

| Cell | Continua's claim | Causa's required difference |
|---|---|---|
| Voice anchor | `generazioni` · stewardship-temporal | `evidenza` · public-record-evidence · NOT temporal-longitudinal |
| Palette | pine + pewter + brass (`#0F3A30`/`#5A6E78`/`#B0875E` · cool-on-cool with WARM CHROME-ONLY metallic) | bottle-green + bone + obsidian (full cool · matte-on-matte · **zero metallic** — different polarity strategy: third dimension "matte-on-matte without metallic" per matrix §1.3) |
| Specific hex collision | pine `#0F3A30` | bottle-green target `#14342B`-class · explicitly NOT pine · planner verifies hex distance ≥6 ΔE at A.5 |
| Accent deployment surface | brass = chrome-only (nav wordmark accent · footer crest · NEVER body display) | obsidian = body-typographic-only (drop-cap accent · pull-quote em · CTA fill optional · focus ring · NEVER metallic chrome) — opposite surface-class deployment |
| Heading serif | Crimson Pro | GT Sectra |
| Body sans | Public Sans | Manrope |
| Hero geometry | object-overlay (h1 sits ON the photo's lower-third) | stacked-editorial (LF-2 inheritance · h1 sits BELOW-fold on cream paper) |
| Hero subject | library reading-room interior · interior-warm-mahogany · horizontal partner-desk · books and warm wood | empty courtroom interior · cool-light · vertical timber + bone walls · zero books-on-desk · zero mahogany · the 1-second read is "litigation chamber" NOT "stewardship reading-room" |
| Hero subject material register | warm mahogany horizontal furniture (partner-desk dominant) | cool timber vertical structure (aula columns / wainscoting dominant) |
| Hero color temperature | warm interior (mahogany + brass + amber light) | cool interior (timber + bone + daylight through high windows) |
| Section sequence | D · governance-cycle slot-2 · 4-pillar 2×2 matrix | B · narrative essay slot-2 · sectors ribbon slot-3 |
| Leadership feel | pillar-photo (3 environmental portraits across pillars) | single-portrait masthead (LF-2 family-shared · single-principal — NOT 3 environmental portraits) |
| Cases-preview shape | timeline | magazine-grid 3+1 (LF-2 family-shared) |
| Navbar geometry | condensed-minimal-top | split-wordmark-top cream-paper (LF-2 family-shared) |
| CTA copy | "Avvia un dialogo di mandato" · family-office mandate-dialogue | "Apri un parere preliminare" · parere-screening · NOT mandate-dialogue mental model |

### 3.6 · Cluster-invariant prohibitions (CS-LAYOUT-20 · non-negotiable · NO waiver)

- Inter as body sans (Pragma + Solaria already · 3rd use collapses cluster body-sans differentiation).
- Geometric sans on headings (Montserrat · Poppins · Raleway · CS-TYPE-01).
- Lorem ipsum / "Replace this text" / "Your headline here" anywhere (CS-MARKET-02 / CS-MARKET-03).
- Unsplash URLs · Pexels-only (CS-IMG-SRC-01).
- `--primary-2: #2c3e6b` hardcoded (AP7 · CS-PAL-03).
- `--primary` palette hex with L\* > 40 on cream paper (CS-PAL-01).
- Fake credentials · "Certified X Expert" · invented albo IDs (CS-EXEC-03).
- Any URL appearing in `business-{corporate,architecture,fiscal,coaching,stewardship}` pools (CS-IMG-SRC-04 · grep enforces zero overlap automatically).

---

## §4 · Hero subject class · the 1-second read

| Field | Value |
|---|---|
| Primary subject class | **empty courtroom interior** (architectural-aula · vertical timber + bone walls · cool-light · daylight through high windows or muted interior · zero people · interior-architectural composition) |
| Imagery direction (DNA) | `legal-courtroom-interior` (or `legal-aula-interior` if the latter parses cleaner in the seeder · planner picks final tag at A.5) |
| Pool source | NEW pool `business-legale` · Pexels-only · 6 URLs minimum · zero overlap grep against `business-{corporate,architecture,fiscal,coaching,stewardship}` (CS-IMG-SRC-04 · automated) |
| Subject density | zero people · interior-architectural |
| Color temperature | cool light · daylight through high windows OR muted interior · NOT warm-mahogany (Continua) · NOT golden-hour (Cornice) · NOT flat office daylight (Pragma) · NOT desk lamp warm (Fiscus) |
| Aspect ratio | 16:9 landscape preferred for full-bleed hero · 4:5 portrait acceptable as fallback URL (the magazine-grid hero card is portrait-friendly) |
| Backup subject class (curator escape hatch · only if courtroom-interior pool is too thin at A.3 scout) | **legal-codex spread on a desk** (open law tome with annotations + brass stamp/seal · close-up object-led · zero people) — still object-led + zero-people · still LF-2-fitting · risk = visual proximity to Fiscus's "tidy desk + documents" — mitigated by close-up zoom on the codex (NOT a wide desk shot) · planner-approved fallback only if ≥4 courtroom URLs cannot be sourced |
| Why this works | The aula di tribunale is a 1-second-readable "this firm pleads in court" cue. Different geographical (courtroom-not-portico-not-reading-room) · different material (timber+bone-not-mahogany-not-stone) · different temperature (cool-not-golden-hour-not-warm) registers from all 5 live siblings. Object-led + zero-people composition fits LF-2's editorial-publication register without colliding with Cornice's exterior architecture or Continua's interior stewardship-archive. |
| Critical guardrail | **NO mahogany.** **NO horizontal partner-desk.** **NO books-on-desk.** **NO golden-hour stone.** **NO Italian portico.** **NO conversation scene.** **NO drafting tools.** Each is a frozen-sibling collision. |

---

## §5 · Leadership composition

| Field | Value |
|---|---|
| Cell | `cs-leadership-single` (LF-2 L6 = single-portrait-feature · family-shared) |
| Composition | 2-col grid · ONE large environmental portrait LEFT · h2 + role + 2-paragraph bio + 4-credential list RIGHT |
| Subject | single principal · senior Cassazionista · 50s-or-senior · founder · the firm IS this person |
| Portrait framing | environmental · 3/4 framing · the room is half the subject · chambers + codices background · zero LinkedIn-headshot read · per AC-9 |
| Portrait room props | codices on shelves · law tomes (real Italian law texts · NOT Latin classics · NOT generic books) · vertical timber wainscoting · zero drafting tools (Cornice claim) · zero mahogany partner-desk (Continua claim) |
| Portrait color | cool register (NOT warm-mahogany lighting) · matches hero photo's color temperature |
| Founder gender / name / pronouns | locked at A.5 build · NOT mid-build · NOT at A.6 · per R-LF2-2 mitigation. Every surface (portrait + name + pronouns + role + bio + intro + team-card role + studio-founder-eyebrow) MUST agree before A.6 review-lock. The Cornice incident (Marta vs Marco mismatch) is the load-bearing precedent. |
| Founder identity | open at A.2 · planner authors at A.4 · constraint: Italian-readable name · single-principal voice · "fondatrice" or "fondatore" gendered consistently across all 5 locales |
| Role title | "Avvocato Cassazionista · Founder" or "Avvocata Cassazionista · Founder" depending on gender lock |
| Bio register | 2 paragraphs · forensic-publication voice · third-person studio voice · references to landmark sentences and ENCA contributions WITHOUT naming sensitive client cases (the proof comes from public-record citations on the cases page, not in the bio) |
| Credentials list (4 items · ordered) | 1. **Albo Avvocati Milano** (with appropriate Albo registration shape · NOT inventing a number — planner authors realistic Albo reference at A.4) · 2. **Cassazionista** (with year of admission to Cassazionista jurisdiction) · 3. **ENCA · giornalisti / mediatori** (Ente Nazionale Conciliazione Avvocati · forensic-publication body) · 4. **Pubblicazioni in massimario** (with count of cited massimario entries) · OPTIONAL 5th line if pubblicazioni line is short: **Albo CTU forense** (Consulente Tecnico d'Ufficio) |
| Credentials register vs Fiscus | Fiscus uses "Iscritto Sezione A · Cassazionista · Revisore Legale" (mixed Albo+revisione). Causa uses forensic-publishing register (Albo Avvocati + ENCA + pubblicazioni in massimario · NO Revisore Legale · NO Sezione A literal). |
| Anti-collapse guardrail | per R-LF2-1: portrait must NOT be a flat-light LinkedIn-style headshot. The curator at A.3 binds the environmental composition triple (50s-or-senior + chambers-with-codices-mid-ground + environmental-NOT-studio-backdrop) BEFORE the build at A.5. |

---

## §6 · Magazine-grid logic (cs-cases-magazine)

| Field | Value |
|---|---|
| Cell | `cs-cases-magazine` (LF-2 L7 = magazine-grid · family-shared 3+1 shape) |
| Composition | 2-col CSS grid · 1 hero card LEFT spans rows 1-3 · 3 small cards stacked RIGHT |
| Hero card | the firm's lead landmark sentence (the Cassazionista's most-cited public-record proof) · largest photo · most ambitious h3 · most curatorial em-word · per AC-10 hero-card-as-lead-story binding |
| 3 supporting cards | 3 additional public-record sentences · supporting items · ranked editorially BEFORE build · per AC-10 (the lead story is a curatorial decision, not an alphabetical accident) |
| Each card carries | photo + eyebrow + h3 (italic em on the curatorial noun · per LF-2 family rule) + body (2-3 lines) + pill (link to detail page) |
| Em-word set across 4 cards | 4 fresh em-words (planner authors at A.4 · anchored on `evidenza` recurrence + forensic-publication register) · examples for planner reference: `evidenza · giurisdizione · incardinata · massima` (subject to A.4 final author pass) |
| Proof tactic | **public-record** · each card cites a real sentence shape (Cass. civ. sez. III · Cass. SS.UU. · TAR Lombardia · Corte d'Appello) · NO anonymized clients · NO "Cliente del settore X" · NO list-row format |
| Case slugs | NOT Cornice's `biblioteca-pietrasanta-concorso · via-volpe-roma-residenziale · palazzo-lignari-bologna-restauro · cornice-fronte-minore-saggio` · planner authors 4 fresh slugs at A.4 · slug shape suggestion: `<area-of-law>-<jurisdiction>-<year>` or `<sentence-citation-flat>` |
| Detail-page policy | registry-only (no per-template detail-page templates · per Chiara/A.13 precedent — case detail pages render from the registry) · 4 case-detail routes per locale at workflow C (5 locales × 4 cases = 20 case-detail routes minimum) |
| Anti-collapse guardrail | per R-LF2-4: if all 4 cases read "equally good," the grid collapses into a generic gallery. Editorial ranking happens at A.4 copy-authoring, NOT at A.5 build. The hero card must be unambiguously the lead story (largest landmark · most ambitious h3 · longest em-word). |
| Photography | 4 case photos · one per card · cool-light · object-led OR architectural-detail-led · zero overlap with the hero photo and the leadership portrait · all sourced from `business-legale` Pexels pool |

---

## §7 · Section rhythm (LF-2 B verbatim)

```
slot-1 · cs-hero                  · stacked-editorial · empty courtroom photo TOP · 8/4 below-fold (h1 LEFT · side-quote RIGHT)
                                    KPI tuple inside photo's bottom-left credit-overlay frame
                                    `(N landmark sentenze · pubblicazioni in massimario · anni di patrocinio)`
                                    h1 carries voice anchor verbatim with em on `evidenza`
                                    side-quote em moves with verb-form derived from anchor noun (e.g., `incardinare` · `incardinata`)

slot-2 · cs-narrative             · evidence-led method essay · 2-col grid
                                    drop-cap p1 (84px GT Sectra · obsidian-tinted on cream · NOT rust)
                                    3 pull-quotes interspersed (each carries 1 italic em-word from forensic-publication register)
                                    sticky 4-link side-rail RIGHT (`Studio · Materie · Pubblicazioni · Contatti`)
                                    NOT verbatim from Cornice's `Servizi · Progetti · Pubblicazioni · Studio`

slot-3 · cs-sectors-ribbon        · 12-cell typology row · legal practice areas
                                    Penale tributario · Civile contrattualistica · Amministrativo regolatorio
                                    Contenzioso bancario · Responsabilità professionale · Recupero crediti complesso
                                    Diritto societario contenzioso · Tributario · Esecuzioni
                                    Lavoro complesso · CTU forense · ENCA mediation
                                    NO trust marquee · sectors-ribbon absorbs trust function (LF-2 family signature)

slot-4 · cs-leadership-single     · single-portrait masthead per §5
                                    senior Cassazionista in chambers
                                    2-paragraph bio + 4 credentials

slot-5 · cs-cases-magazine        · 3+1 grid per §6
                                    1 hero card (lead landmark sentence) + 3 small cards stacked
                                    public-record proof on every card

slot-6 · cs-cta-closer-cream      · cream paper · hairline obsidian borders
                                    filled-bottle-green CTA pill (NOT rust · NOT brass · NOT emerald)
                                    h2 carries voice anchor verbatim recurrence with em on `evidenza`
                                    primary CTA "Apri un parere preliminare"
                                    secondary action = phone number or contact line
```

**Six sections · zero dark bands on home · CS-TONE-03 inherited demotion (LF-2 family-scoped per AC-14).**

---

## §8 · CTA personality

| Field | Value |
|---|---|
| Primary CTA copy | **"Apri un parere preliminare"** |
| Mental model | **parere-screening-then-mandate** · the firm gives a preliminary legal opinion before deciding to take the case · evidence-and-jurisdiction intake (NOT contact + reason · NOT P.IVA/CF · NOT NDA · NOT discovery-call · NOT mandate-dialogue · NOT fascicolo) |
| Conversion form fields (7) | 1. oggetto del contenzioso (free text · 1 paragraph) · 2. grado di giudizio attuale (radio · primo grado / appello / Cassazione / amministrativo / non avviato) · 3. controparte (free text · 1 line) · 4. fascia di valore (radio · 5 buckets) · 5. urgenza (radio · 3 buckets · scadenza data optional) · 6. evidenza preliminare allegabile (file upload optional · accepted: PDF · NOT mandatory) · 7. giurisdizione (radio · Italia / EU / extra-EU) |
| CTA closer h2 (voice anchor surface 2) | verbatim recurrence of hero h1 anchor sentence with em on `evidenza` · per AC-15 |
| Secondary action on CTA closer | phone number (Italian-readable Milan number shape · planner authors at A.5) OR email (`info@causa.legal` · placeholder pattern) — the firm IS contactable but the primary path is parere-screening |
| Tone | evidence-bound · screening-before-mandate · forensic-publication register |
| Filled CTA pill colour | bottle-green (matches palette primary · hairline obsidian border on hover) |
| Banned CTA copy (cluster + family) | "Get started free" / "Sign up" / "Iscriviti gratis" (CS-CTA-02) · "Fissa una call privata" (Pragma) · "Apri un fascicolo progetto" (Cornice) · "Primo appuntamento" (Fiscus) · "Prenota una discovery call" (Solaria) · "Avvia un dialogo di mandato" (Continua) · any fascicolo / dossier / "open a case file" mental model (AC-8) |
| CTA on the navbar | the trailing CTA pill in `cs-nav--lf2` carries shorter copy · suggestion: "Parere preliminare" or "Contatta lo studio" — planner picks final at A.5 with A.6 critique to verify it does NOT collide with the closer's longer copy |

---

## §9 · Typography direction

| Field | Value |
|---|---|
| Heading serif | **GT Sectra** primary · **Source Serif Pro** as licence-fallback (planner declares the fallback at A.2 · NOT re-decided at A.5) |
| Heading scale | h1 hero 56-64px (cream paper, below-fold of hero) · h2 closer 40-48px · h2 section 36-40px · h3 cards 22-26px · h4/h5 inherited from cluster scale |
| Drop-cap | 84px GT Sectra · obsidian-tinted on cream (NOT rust · NOT brass · per accent deployment rule §1) · paragraph 1 of `cs-narrative` · accent-tinted means the drop-cap carries a slightly desaturated obsidian fill on the cream background |
| Body sans | **Manrope** · NO fallback (Inter explicitly forbidden per CS-LAYOUT-20 · 3rd cluster use collapses body-sans differentiation) |
| Body scale | 17px paragraph · 15px caption · 14-15px nav inline · 13-14px footer · inherited from cluster |
| Italic em strategy | **ONE em per heading** on `evidenza` · 2-surface verbatim recurrence (LF-2 family rule · hero h1 + cs-cta-closer-cream h2) · explicitly NOT two-em contrast pair (Solaria's exception forbidden here · per CS-EXEC-01 default) |
| Em-word set across home (12 words target) | anchored on `evidenza` recurrence + forensic-publication register · planner authors final 12 at A.4 · examples for builder reference: `evidenza · incardinata · giurisdizione · massima · sentenza · patrocinio · evidenza · sostenuta · materia · fascicolo` (note: `fascicolo` here is allowed AS A NORMAL NOUN in body copy · banned ONLY as the CTA mental model per AC-8) |
| Pull-quote em-words (3 quotes in narrative) | each pull-quote carries 1 italic em-word from forensic-publication register · all 3 distinct from each other and from `evidenza` |
| Letter-spacing | inherited cluster default · CS-TYPE-05 RTL letter-spacing reset (the 10 LF-5 eyebrow surfaces from Continua's STRONG fix · RTL-scoped · byte-equivalent on LTR · planner verifies inherited at A.5) |
| AR heading font | LF-2-scoped Naskh swap (`html[dir="rtl"] body.cs-lf-lf-2 { --heading: 'Noto Naskh Arabic', 'Cormorant Garamond', Georgia, serif; }`) — Causa inherits this verbatim · do NOT re-bind selector to `body.cs-lf-causa` or any sub-class · per AC-13 |
| Latin wordmark in AR locale | preserved · CS-NAV-06 / CS-FOOT-03 · the wordmark `CAUSA / studio legale` stays Latin even in AR render |
| Latin numerics in AR locale | preserved on the hero KPI tuple (Western Arabic numerals 0-9) · CS-NAV-06 / CS-FOOT-03 |

---

## §10 · Palette direction

| Token | Value | Polarity / surface | Verifies against |
|---|---|---|---|
| `--primary` | bottle-green · target `#14342B`-class · L\* ≤ 40 on cream | nav text · footer base · h1 default · CTA fill · body deep ink | CS-PAL-01 (L\* ≤ 40 on cream) · `is_primary_safe_on_cream()` PASS · ≥6 ΔE distance from Continua pine `#0F3A30` |
| `--secondary` | bone · target `#F0EBE0`-class | navbar background (`cs-nav--lf2` cream-paper) · CTA closer cream · narrative essay paper · footer base | warmer than Cornice pietra-serena `#cdc9c0` · cooler than Fiscus warm-neutral cream · contrast verified for nav inline links + filled CTA pill on this background |
| `--accent` | obsidian · target `#0B0A0E`-class · deep neutral · zero metallic | drop-cap accent (paragraph 1 of narrative) · pull-quote em colour · CTA hairline border · focus ring | NEVER deployed as metallic chrome (≠ Continua brass) · NEVER deployed in nav wordmark accent (≠ Continua brass-on-nav) · body-typographic-only deployment surface |
| `--display-warm` | NOT USED · Causa is matte-on-matte · zero warm display accent | n/a | matrix §1.3 third polarity dimension = "matte-on-matte without metallic" |
| `--metallic` | NOT USED | n/a | zero metallic deployment · third polarity dimension differentiator vs Continua |

**Macro tone**: bottle-green + bone + obsidian (full cool · matte-on-matte · zero metallic) — the polarity strategy is "full cool · matte-on-matte" — opposite of Continua's "cool-with-warm-chrome-only-metallic" and orthogonal to Cornice's "neutral-with-warm-display-only-rust."

**Hex distance verifications (the planner verifies at A.5)**:
- Causa `--primary` vs Continua pine `#0F3A30`: ≥6 ΔE (visible at 1 second on side-by-side test).
- Causa `--secondary` vs Cornice pietra-serena `#cdc9c0`: visibly warmer / lighter on cream comparison.
- Causa `--accent` vs Continua brass `#B0875E`: opposite hue family · opposite chroma · zero collision.

---

## §11 · Multilingual expectation

Per D-102 cadence:
- **A.5 build**: ships **IT only** · `[it]` locales array · `tier=draft`.
- **A.6 review-lock**: IT-only · the 6th sibling clears the LF-2 12 walk gates AND the frozen-sibling regression on Pragma · Cornice · Fiscus · Solaria · Continua at IT only.
- **Workflow C (multilingual)**: extends to **5 locales** (IT preserved · EN/FR/ES/AR added) · AR `dir=rtl` parity with Naskh h1 (LF-2-scoped) · voice anchor verbatim-in-translation across 5 locales.
- **Workflow D / Public flip**: held until explicit user handshake · per R-SOL-8 / CS-BLOCK-13 / D-102 cadence · same shape as Solaria + Continua + Cornice flips (1 registry edit + `sync_template_tiers` + 7 explicit-literal test bumps in `apps/catalog/tests.py` from `24` → `25` and `"24+"` → `"25+"` · plus related-templates limit re-binding if Causa promotion bumps anyone past category-fallback ceiling).

### Voice anchor recurrence across locales (CS-EXEC-01 · F2 · per `cornice-lf2-reference-pack.md §D1` LF-2 rule):

| Locale | Anchor sentence (working draft · planner re-bids the exact wording at A.4 — but the em-word and the verbatim-in-translation contract is locked here) | em-word | Translator bind |
|---|---|---|---|
| IT | `Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.` | `evidenza` | public-record-evidence sense · Italian forensic register |
| EN | `Every ruling is <em>evidence</em> on the record — not an opinion defended.` | `evidence` | public-record-evidence sense · NOT proof-as-statistics · NOT testimony · NOT clue · UK/US legal register both work |
| FR | `Chaque décision est une <em>preuve</em> versée au dossier — non une opinion défendue.` | `preuve` | preuve-versée-au-dossier sense · French Cassation register |
| ES | `Cada sentencia es una <em>evidencia</em> incardinada — no una opinión defendida.` | `evidencia` | evidencia-en-el-expediente sense · Spanish forensic register |
| AR | `كلُّ حكمٍ <em>دليلٌ</em> مُثبَتٌ في السجل، لا رأيٌ يُدافَع عنه.` | `دليل` | دليل-مُثبَت-في-السجل sense · MENA legal-press register · NOT شهادة (testimony) · NOT قرينة (circumstantial proof) |

The em moves with the **public-record-evidence sense** in every locale (NOT proof-as-statistics, NOT testimony, NOT clue — *evidence-on-the-record*). Translator brief at workflow C carries this as a binding contract.

Voice anchor lives on **exactly 2 home surfaces**: hero h1 + CTA closer h2 (per AC-15). NOT on the navbar wordmark, NOT on the side-quote, NOT on an interstitial.

---

## §12 · AR handling expectation

### AR posture inherited from Cornice's LF-2 first-occupant resolution (per `cornice-lf2-reference-pack.md §D9`)

| Item | Causa's binding |
|---|---|
| `dir="rtl"` | `<html dir="rtl">` for AR locale · cluster default |
| h1 font swap | `html[dir="rtl"] body.cs-lf-lf-2 { --heading: 'Noto Naskh Arabic', 'Cormorant Garamond', Georgia, serif; }` · LF-2 family-scoped via `body.cs-lf-lf-2` selector · do NOT re-bind to a sub-class · do NOT move scope to `:root` · do NOT introduce a Causa-specific selector. Verbatim selector inheritance per AC-13. |
| h2/h3 font | inherited cluster default Naskh OR Kufi per cluster spec — the LF-2 swap targets h1 only (the masthead's editorial-publication register) · the body remains the cluster default for cohesion |
| Latin wordmark preservation | `CAUSA / studio legale` rendered in Latin even in AR (CS-NAV-06) |
| Latin numerics preservation | hero KPI tuple uses Western Arabic numerals (0-9) in AR (CS-FOOT-03) |
| RTL letter-spacing reset (CS-TYPE-05) | inherited from Continua's STRONG fix · RTL-scoped on the 10 LF-5 eyebrow surfaces · byte-equivalent on LTR · planner verifies inherited at A.5 (Causa's eyebrow surfaces inherit the same reset where they're scoped to LF-2) |
| Voice anchor recurrence in AR | `كلُّ حكمٍ دليلٌ مُثبَتٌ في السجل، لا رأيٌ يُدافَع عنه.` · `دليل` em-word verbatim on hero h1 + CTA closer h2 |
| AR sectors-ribbon | 12 typology cells translate cleanly · `Penale tributario` → `جزائي ضريبي` · etc. · planner authors final translation at workflow C with translator |
| AR navigation | RTL layout · 5-link inline row mirrors LTR · `Studio · Materie · Pubblicazioni · Contenzioso · Contatti` → AR equivalents · trailing CTA pill mirrors RTL |
| AR hero photo | unchanged · empty courtroom interior is locale-neutral subject |
| AR walk gate | F2-WALK-8 (Cornice precedent): AR locale renders Naskh h1 (`Noto Naskh Arabic` first in fontFamily computed-style) · Latin wordmark + Latin numerics preserved · zero Naskh leakage to LF-1/LF-3/LF-4/LF-5 (probe Continua AR h1 = Kufi at workflow D) |

### AR-specific risk: R-LF2-6 (Naskh leakage)

The Naskh h1 swap is `body.cs-lf-lf-2`-scoped. A Causa build that strips the selector or moves it to `:root` leaks Naskh into Continua's LF-5 AR render. The probe at workflow D + public flip catches it · the planner brief mandates the second occupant must NOT relax the scope.

---

## §13 · Explicit "must NOT repeat" list from Cornice (the high-collision-risk sibling)

This is the load-bearing anti-collision section. Causa shares LF-2 with Cornice; the layout axes are family-shared by intent; the skin axes must score ≥4/5 vs Cornice. Below is the explicit ban list, item by item.

### 13.1 · Voice anchor (hard ban · no waiver)

- **MUST NOT use** `argomento` as voice anchor noun.
- **MUST NOT use** any direct curatorial-thesis cognate: `argument` (EN/FR) · `argumento` (ES) · `حُجَّة / ḥujja` (AR) · `theme` · `topic` · `subject` · `thesis` · `claim` · `case` (in the case-study sense).
- **MUST NOT** carry the curatorial-thesis sense on the em-word.
- **MUST use** `evidenza` and its public-record-evidence cognates (`evidence · preuve · evidencia · دليل`) · per AC-3.

### 13.2 · Voice anchor sentence

- **MUST NOT** ship `Ogni progetto è un argomento costruito, non un servizio reso.` or any near-paraphrase.
- **MUST** ship a forensic-publication-register sentence that reads "we plead what is incardinated, not what is opined" at the meta level · planner final wording at A.4.

### 13.3 · Heading serif (hard ban · no waiver)

- **MUST NOT use** Cormorant Garamond.
- **MUST NOT use** any Cormorant family variant (Cormorant SC · Cormorant Infant · Cormorant Upright).
- **MUST use** GT Sectra primary · Source Serif Pro fallback.

### 13.4 · Body sans (hard ban · no waiver)

- **MUST NOT use** Source Sans 3.
- **MUST NOT use** Source Sans Pro (the elder sibling).
- **MUST use** Manrope · NO fallback.

### 13.5 · Palette (hard ban · no waiver)

- **MUST NOT use** graphite (`#1c1d20` or any hex within ≤6 ΔE).
- **MUST NOT use** pietra-serena (`#cdc9c0` or any warm-cool stone tone within ≤6 ΔE) as secondary.
- **MUST NOT use** terracotta-rust (`#a14a2c` or any warm rust/copper/terracotta within ≤6 ΔE) as accent.
- **MUST NOT** deploy a warm display accent (rust-family · copper-family · terracotta-family).
- **MUST** ship bottle-green primary + bone secondary + obsidian accent · matte-on-matte · zero metallic.

### 13.6 · Hero photography subject (hard ban · no waiver)

- **MUST NOT** ship Bologna golden-hour portico OR any northern-Italian-portico exterior.
- **MUST NOT** ship any golden-hour stone-architectural-shadow exterior.
- **MUST NOT** ship any subject that reads "Italian classical architecture" at 1 second.
- **MUST NOT** ship any exterior architectural · stone-warm · landscape orientation matching Cornice's 16:9 portico framing pattern.
- **MUST** ship empty courtroom interior · cool light · zero people · vertical timber + bone walls (per §4 above).

### 13.7 · CTA copy + mental model (hard ban · no waiver)

- **MUST NOT** ship "Apri un fascicolo progetto."
- **MUST NOT** ship any fascicolo / dossier / "open a folder/file/case" mental model.
- **MUST NOT** ship "Apri un dossier" / "Apri un fascicolo" / "Open a brief" / "Open a record" / "Open a folder" / "Open a case file" · per AC-8 ban list.
- **MUST** ship "Apri un parere preliminare" · parere-screening mental model (per §8 above).

### 13.8 · Conversion form fields

- **MUST NOT** ship project scope + budget range + timeline horizon (architecture intake shape).
- **MUST** ship the 7-field forensic intake (per §8 above).

### 13.9 · Studio identity (hard ban · no waiver)

- **MUST NOT** be Marta Roveri (Cornice's founder identity is locked).
- **MUST NOT** be a Milanese or Bolognese architecture studio.
- **MUST NOT** carry "STUDIO DI ARCHITETTURA · DAL 2008" as wordmark descriptor.
- **MUST** be a Milanese (NOT Bologna · NOT Rome · explicit guardrail) Cassazionista boutique.

### 13.10 · Navbar 5-link labels (hard ban · no waiver)

- **MUST NOT** ship `Lo studio · Archivio · Servizi · Progetti · Contatti` verbatim.
- **MUST** ship `Studio · Materie · Pubblicazioni · Contenzioso · Contatti` (planner-locked at this brief).

### 13.11 · Wordmark + descriptor pair

- **MUST NOT** ship `CORNICE / studio di architettura`.
- **MUST** ship `CAUSA / studio legale` (split-line masthead · cream-paper navbar `cs-nav--lf2` · same shape · different content per AC-11).

### 13.12 · Trailing CTA pill colour

- **MUST NOT** ship filled-rust trailing CTA pill (Cornice claim).
- **MUST NOT** ship any rust-family fill on the navbar trailing CTA.
- **MUST** ship filled-bottle-green trailing CTA pill (matches Causa's accent deployment via primary).

### 13.13 · Em-word set across home

- **MUST NOT** ship `argomento · argomenta · geometria · lotto · argomento · minore` em-word set.
- **MUST** ship 12 fresh em-words at A.4 anchored on `evidenza` recurrence + forensic-publication register.

### 13.14 · Leadership room props

- **MUST NOT** ship drafting tools in the masthead portrait background.
- **MUST NOT** ship architecture studio backdrop (drafting tables · architectural models · rolled blueprints).
- **MUST** ship chambers + codices + law tomes + vertical timber wainscoting (per §5 above).

### 13.15 · Leadership credentials

- **MUST NOT** ship OAPPC Milano · MIBAC commission marks · published monografia · concorsi (Cornice's set).
- **MUST** ship Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario · (optional) Albo CTU forense.

### 13.16 · Case slugs

- **MUST NOT** ship `biblioteca-pietrasanta-concorso · via-volpe-roma-residenziale · palazzo-lignari-bologna-restauro · cornice-fronte-minore-saggio` (Cornice's set).
- **MUST** ship 4 fresh case slugs at A.4 (1 landmark sentence + 3 supporting public-record cases · slug shape suggestion: `<area-of-law>-<jurisdiction>-<year>` or `<sentence-citation-flat>`).

### 13.17 · Pexels URLs

- **MUST NOT** ship any URL appearing in `business-architecture` pool.
- **MUST NOT** ship any URL appearing in `business-{corporate,fiscal,coaching,stewardship}` pools (cluster-invariant CS-IMG-SRC-04).
- **MUST** ship 6 NEW URLs in NEW `business-legale` Pexels pool · zero overlap grep enforces automatically.

### 13.18 · 4th footer column content

- **MUST NOT** copy-paste Cornice's architecture studio whistleblowing channel content.
- **MUST** ship forensic firm's whistleblowing channel · D.lgs. 24/2023 · responsabile della prevenzione (forensic-firm-appropriate name) · email · privacy reference · per AC-12 sub-cluster-specific.

### 13.19 · Geographic anchor

- **MUST NOT** be Bologna (Cornice's geography).
- **MUST** be Milano · explicit guardrail per intake §1.

### 13.20 · KPI tuple cell content

- **MUST NOT** ship `(novanta fascicoli · 2008 · 38 menzioni)` (Cornice's tuple).
- **MUST** ship `(N landmark sentenze · pubblicazioni in massimario · anni di patrocinio)` · same hero-overlay shape (LF-2 family-shared per AC-2) · different cell content.

### 13.21 · Hero credit overlay caption

- **MUST NOT** ship `(Direzione · Anno fondazione)` (Cornice's caption).
- **MUST** ship `(Albo Avvocati Milano · Cassazionista dal AAAA)`.

### 13.22 · CS-TONE-03 family demotion · do NOT extend

- **MUST NOT** invoke the CS-TONE-03 demotion as a precedent for any non-LF-2 sibling (per R-LF2-5).
- **MUST** carry zero dark bands on home as a Causa-binding inheritance (NOT a permission to dark-band elsewhere).

### 13.23 · Naskh selector scope · do NOT relax

- **MUST NOT** strip the `body.cs-lf-lf-2` selector scope on the AR Naskh swap (per R-LF2-6).
- **MUST NOT** move the swap to `:root`.
- **MUST NOT** introduce a Causa-specific selector (`body.cs-lf-causa` or similar).
- **MUST** inherit the family-level scope verbatim · per AC-13.

---

## §14 · Walk gates inherited from LF-2

Causa clears each gate independently at A.6 review-lock and at workflow C multilingual walk:

- **F2-WALK-1**: Hero photo full-bleed at 1920/1440/1280/1100 · 8/4 below-fold split renders correctly at 1100+ · stacked at ≤880.
- **F2-WALK-2**: KPI tuple in hero overlay reads contrast-AA against the photo's bottom-left luminance region · translucent dark plate behind the overlay if the cool-light photo has variable luminance.
- **F2-WALK-3**: Drop-cap renders at 84px GT Sectra obsidian-tinted on cream paragraph 1 · 3 pull-quotes interspersed · sticky 4-link side-rail anchors to actual page sections.
- **F2-WALK-4**: Single-portrait masthead reads environmental-not-studio at 1280 + 720 · bio + 4 credentials legible at 880 · stacks above portrait at ≤720.
- **F2-WALK-5**: 3+1 magazine grid hero card spans rows 1-3 at 1100+ · stacks to 4-up at ≤720 with hero card first.
- **F2-WALK-6**: Cream-paper navbar at 1920/1440/1280/1100 · split-line masthead readable · trailing filled CTA · hamburger drawer at ≤880 with the same masthead split.
- **F2-WALK-7**: 4-col footer at 1100+ · 2-col at 880 · 1-col stack at ≤720 with whistleblowing column NEVER collapsed into a sub-link of contact.
- **F2-WALK-8**: AR locale renders Naskh h1 (`Noto Naskh Arabic` first in fontFamily computed-style) · Latin wordmark + Latin numerics preserved · zero Naskh leakage to LF-1/LF-3/LF-4/LF-5 (probe Continua AR h1 = Kufi).
- **F2-WALK-9**: Voice anchor verbatim on exactly 2 home surfaces · em-word identical on both · 12 em-word audit on home (CS-TYPE-02) passes 12/12.
- **F2-WALK-10**: Zero dark sections on home (body-class probe + screenshot review at 1920 must show no `--primary` background bands besides the navbar and footer chrome).
- **F2-WALK-11**: 5 locales × 5 page kinds + 5 locales × 4 case-detail = 45+ routes 200 anonymously at workflow C.
- **F2-WALK-12**: Frozen-sibling regression on Pragma · Cornice · Fiscus · Solaria · Continua = 5 × 200 anonymous + 0 px wireframe drift on each at every gate.

---

## §15 · Risks register (LF-2 inherited · Causa-specific re-fires)

The 8 LF-2 risks per `cornice-lf2-reference-pack.md §8` re-fire on Causa. Each is mitigated at A.5 build, NOT at A.6 review-lock.

| Risk | Mitigation at A.5 |
|---|---|
| **R-LF2-1** Single-portrait stock-headshot collapse | Curator binds environmental composition triple at A.3 (50s-or-senior + chambers-with-codices-mid-ground + environmental-NOT-studio-backdrop) BEFORE A.5 build · Cassazionista in chambers with codices · NOT LinkedIn-style flat-light headshot. |
| **R-LF2-2** Founder gender / name / pronouns mismatch | Lock founder identity at A.5 build · verify portrait + name + pronouns + role + bio + intro + team-card role + studio-founder-eyebrow ALL agree before A.6 review-lock · Cornice's Marta-vs-Marco precedent informs the audit. |
| **R-LF2-3** Hero overlay luminance vs KPI tuple contrast | KPI tuple inside hero photo's bottom-left credit-overlay clears AA against the photo's bottom-left luminance · translucent dark plate (alpha-30 obsidian) behind the overlay if cool-light photo has variable luminance. |
| **R-LF2-4** Magazine grid collapsing into a generic gallery | Cases ranked editorially at A.4 copy-authoring · the hero card is unambiguously the lead landmark sentence (largest · most ambitious h3 · longest em-word) · the 3 small cards are supporting items. |
| **R-LF2-5** CS-TONE-03 demotion mistakenly extended to non-LF-2 siblings | Causa carries zero dark bands as inheritance (NOT permission) · the orchestrator gates this at planner-brief sign-off. |
| **R-LF2-6** Naskh leakage to non-LF-2 AR siblings | `body.cs-lf-lf-2` selector preserved verbatim · do NOT strip · do NOT move to `:root` · do NOT re-bind to `body.cs-lf-causa` · workflow D probe verifies Continua AR h1 = Kufi after Causa build. |
| **R-LF2-7** 4-col-with-whistleblowing column dropping at ≤720px | Responsive auditor at A.6 walks the footer at 720 + 480 · whistleblowing column reachable in one tap on mobile · NOT collapsed into a sub-link of "contact." |
| **R-LF2-8** Cream-paper navbar contrast at lower-luminance rooms | Contrast-accessibility scorecard verifies 5-link inline row + masthead descriptor + filled trailing CTA clear AA on bone background · focus ring (obsidian) reads on cream nav · NOT against the dark navbar of LF-1/LF-3/LF-4. |

### Causa-specific additional risks (NEW · planner-surfaced at A.2)

| Risk | Mitigation |
|---|---|
| **R-CAU-1** Bottle-green hex collision with Continua pine `#0F3A30` (≤6 ΔE distance) | Planner verifies hex distance ≥6 ΔE at A.5 build · target `#14342B`-class · side-by-side test at 1920 + screenshot vs Continua home. |
| **R-CAU-2** Empty courtroom interior reading as Continua's library reading-room (interior-warm-mahogany adjacency) | Curator binds cool-light + zero-mahogany + zero-books-on-desk + vertical timber + bone walls at A.3 · explicit reject criteria for any URL where mahogany/horizontal-partner-desk dominates the frame. |
| **R-CAU-3** Cassazionista credential vocabulary collision with Fiscus's Cassazionista line | Causa's credential **set** reads forensic-publishing register (Albo Avvocati + ENCA + pubblicazioni in massimario) NOT Fiscus's mixed Albo+revisione register · planner authors the 4-credential list at A.4 with this constraint. |
| **R-CAU-4** "Materie" as nav label could read SaaS-product-categories | Materie in Italian forensic register reads "areas of law" (e.g., "le materie di diritto" / "le materie penali") · planner verifies the term reads correctly with the typology ribbon at slot-3 backing the nav label. |
| **R-CAU-5** Fascicolo as ordinary noun appearing in body copy could trigger CTA mental model collision | Fascicolo is BANNED only as the CTA mental model per AC-8 · planner allows it as a body-copy noun where forensic register requires it (e.g., "il fascicolo processuale di parte") · A.6 critic verifies fascicolo never appears in CTA-shape contexts. |
| **R-CAU-6** Booking-flag cohort drift if test_medical_and_restaurant_templates_have_booking_flag is brittle | Causa is litigation-shaped · `has_booking=False` · planner verifies the test cohort at A.5 build · adds Causa to the FALSE cohort if necessary (single explicit-literal test edit, NOT a behavior change). |

---

## §16 · The exact next action after this brief

> **Hold this brief for orchestrator sign-off.** On sign-off, Phase X.6 Step 2 = workflow A.3 imagery curator pack at `factory/reports/causa/causa-imagery-pack.md`. The curator at A.3 reads §4 (hero subject class · empty courtroom interior · cool-light · zero people · vertical timber + bone walls + backup codex-spread fallback), §5 (leadership composition · senior Cassazionista in chambers · chambers + codices + law tomes · zero drafting tools · zero mahogany), §6 (4 case photos · cool-light · object-led OR architectural-detail-led), and binds **6 Pexels URLs minimum** in NEW `business-legale` pool with zero overlap grep against `business-{corporate,architecture,fiscal,coaching,stewardship}`. **No application code, registry, or tier change at Step 2.** A.4 copy authoring is Step 3. A.5 build is Step 4 and is gated on A.4 copy sign-off + A.3 imagery sign-off + this brief sign-off.

This brief is **paper-only**. It is the planner contract; A.3 is the imagery curator's deliverable.
