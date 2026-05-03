# Sixth-sibling recommended intake · Causa

**Status**: paper-only · Phase X.6 Step 0 · locked recommended candidate · NOT a planner brief
**Date**: 2026-05-03
**Target**: corporate-suite 6th sibling · post-Cornice next intake
**Companion files**: `factory/reports/hardening/sixth-sibling-territory-scout.md` · `sixth-sibling-shortlist.md` · `cornice-lf2-reference-pack.md` · `corporate-suite-{distinctness-matrix,reference-pack,layout-family-assignment,live-family-map}.md` · `next-template-brief-schema.md`
**Hard constraints honoured**: paper-only · no application code · no registry · no tier · no apps/{editor,projects,commerce} · no new archetype · zero silent reuse of any of the 5 live siblings' grammar.

---

## §1 · Identity

| Field | Value |
|---|---|
| Working studio name | **Causa** |
| Slug | `causa-legale` |
| Cluster | corporate-suite |
| Sub-cluster | studio-legale-cassazionista · evidence-led litigation boutique |
| Family hypothesis | **LF-2 second occupant** (inherits L1–L9 verbatim per `cornice-lf2-reference-pack.md §AC-1`) |
| Audience profile | imprese e privati con contenzioso complesso · ricorsi in Cassazione · responsabilità professionale · contenzioso bancario · diritto amministrativo regolatorio · contenzioso tributario · ENCA / albo CTU expert testimony |
| Org scale | 1 senior Cassazionista (50s-or-senior · founder · single-principal masthead) + 2-3 associati · 1 sede Milano (Italian-readable; **NOT Bologna** to avoid Cornice geographic adjacency) |
| Locales at A.5 | `[it]` only · per D-102 cadence · others added at workflow C |
| Tier at A.5 | `draft` · per D-102 default |
| Nearest two siblings (for triangulation) | **Cornice** (LF-2 family-shared structure · skin axes must clear ≥4/5) · **Continua** (closest cool-on-cool palette adjacency · interior hero subject adjacency) |

---

## §2 · Family hypothesis · LF-2 second occupant binding

The 6th sibling inherits the LF-2 L1–L9 tuple verbatim. **Do not flip cells.**

```
L1 · stacked-editorial          (full-bleed photo TOP · 8/4 below-fold)
L2 · B section sequence         (cs-hero · cs-narrative · cs-sectors-ribbon · cs-leadership-single · cs-cases-magazine · cs-cta-closer-cream)
L3 · absent                     (no named cadence cell · narrative essay covers role)
L4 · essay-with-anchors         (drop-cap p1 + 3 pull-quotes + sticky 4-link side-rail)
L5 · hero-overlay               (KPI in photo bottom-left credit-overlay frame)
L6 · single-portrait-feature    (1 environmental portrait + 2-paragraph bio + 4 credentials)
L7 · magazine-grid              (3+1 · 1 hero card spans rows 1-3 + 3 small cards)
L8 · split-wordmark-top         (cream-paper navbar with split-line masthead + filled trailing CTA · NO phone-right)
L9 · 4-col-with-whistleblowing  (4th column = D.lgs. 24/2023 channel)
```

Inherited verbatim from Cornice's reference pack §6:
- Cream-paper navbar shape (split-line masthead · filled trailing CTA · 5-link inline · no phone-right).
- Zero dark bands on home (CS-TONE-03 family-scoped demotion · do NOT introduce a dark band to "ground the page").
- LF-2-scoped Naskh AR h1 swap (`html[dir="rtl"] body.cs-lf-lf-2 { --heading: 'Noto Naskh Arabic', ... }`) · do NOT re-bind selector to a sub-class.
- Hairline-bordered cream CTA closer with voice anchor verbatim recurrence.
- Sticky 4-link side-rail in the narrative band.
- Three pull-quotes interspersed in the narrative essay (each with own italic em-word).
- Drop-cap on paragraph 1 of narrative (84px serif · accent-tinted).
- KPI tuple inside hero photo's bottom-left credit-overlay frame.
- Single-portrait masthead requiring environmental-not-studio framing.
- Magazine 3+1 grid for cases (1 hero card + 3 small).
- Voice anchor verbatim on exactly 2 home surfaces (hero h1 + CTA closer h2).

Differentiation lives at the SKIN layer (voice · palette · imagery · typography · CTA mental model · case-bundle content · navbar wordmark · footer column content). Per AC-2: layout axes are family-shared; skin axes must score ≥4/5 vs Cornice.

---

## §3 · Anti-collision rules · what Causa must NOT repeat

Lifted from `corporate-suite-distinctness-matrix.md §1` and `cornice-lf2-reference-pack.md §5`. Each cell of the 5 live siblings is named explicitly so the planner cannot drift.

### Must NOT repeat from Pragma (LF-1)
- KPI tuple `(HQ · Equipe · Mandati)` as meta-strip · navy + emerald + cream macro tone · boardroom long-table hero · "Fissa una call privata" CTA · Merriweather heading · Inter body · "Partner · Senior Associate · Counsel" credentials.

### Must NOT repeat from Cornice (LF-2 first occupant — load-bearing)
- `argomento` voice anchor · or any direct curatorial-thesis cognate (`argument` / `argumento` / `حُجَّة` / theme / topic / thesis / claim / case-in-the-case-study sense).
- Cormorant Garamond heading · Source Sans 3 body.
- Graphite + pietra-serena + terracotta-rust palette · or any warm-grey + warm-rust/copper combination · or any palette where the warm display accent is rust-family.
- Bologna or any northern-Italian-portico exterior · any golden-hour stone-architectural-shadow exterior · any "Italian classical architecture" 1-second read.
- "Apri un fascicolo progetto" CTA · the fascicolo / dossier / "open a folder/file/case" mental model.
- `Lo studio · Archivio · Servizi · Progetti · Contatti` 5-link nav labels (pick fresh).
- Marta Roveri · STUDIO DI ARCHITETTURA · DAL 2008 wordmark + descriptor pair.
- The 4 case slugs `biblioteca-pietrasanta-concorso · via-volpe-roma-residenziale · palazzo-lignari-bologna-restauro · cornice-fronte-minore-saggio`.
- The 4 credentials (OAPPC Milano · MIBAC · monografia · concorsi).
- The 6 Pexels URLs in `business-architecture` pool (CS-IMG-SRC-04 grep · automated zero-overlap enforcement).

### Must NOT repeat from Fiscus (LF-3)
- Fiscal-calendar-strip · slot-4 cycle `(mese · scadenza · ambito)` · tidy desk + documents hero · IBM Plex Serif/Sans · warm-neutral + blu-notte + gold palette · "Primo appuntamento" CTA + P.IVA/CF intake · "Iscritto Sezione A · Cassazionista · Revisore Legale" credentials.
  - **Note**: Fiscus claims "Cassazionista" as a credential vocabulary item. Causa's leadership masthead carries Cassazionista as the founder's actual title (the firm IS a Cassazionista boutique) — but the **credential set** must read differently. Causa's credentials lead with **Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario** (forensic-publishing register), NOT "Iscritto Sezione A · Cassazionista · Revisore Legale" (Fiscus's mixed Albo+revisione register).

### Must NOT repeat from Solaria (LF-4)
- Manifesto block at slot-2 · percorso-cadenza-strip · 3-percorsi enumeration · method-cadenza strip · 1:1 conversation hero · Fraunces serif · warm-carbon + ocra + caramel palette · "Prenota una discovery call" CTA · TWO em-wraps in headings · "ICF-PCC · EMCC Senior Practitioner · AICP" credentials · L6=absent (Causa SHIPS leadership · single-principal does not mean L6 omitted in LF-2).

### Must NOT repeat from Continua (LF-5 — closest palette/imagery adjacency)
- Object-overlay hero geometry · 2-corner credit overlays · governance-cycle slot-2 · 4-pillar 2×2 matrix · pillar-photo leadership · timeline cases · condensed-minimal navbar · pine + pewter + brass palette (cool-on-cool with WARM metallic chrome accent) · Crimson Pro + Public Sans typography · library reading-room interior (any interior-warm-mahogany horizontal-partner-desk) · `generazioni` voice anchor · "Avvia un dialogo di mandato" CTA + family-office mandate-dialogue mental model.
  - **Critical triangulation**: Causa's bottle-green is cool-on-cool BUT with **zero metallic** (the third token is obsidian neutral · NOT brass-chrome metallic). The polarity strategy is "full cool · matte-on-matte" — opposite to Continua's "cool-with-warm-chrome-only-metallic." The hero photography is courtroom interior · cool-light · vertical timber + bone walls · NOT mahogany horizontal partner-desk · the subject-class read at 1 second is "litigation chamber" not "stewardship reading-room."

### Cluster-invariant prohibitions (CS-LAYOUT-20 · non-negotiable)
- Inter as body sans (Pragma + Solaria already · 3rd use collapses cluster body-sans differentiation).
- Geometric sans on headings (CS-TYPE-01).
- Lorem ipsum (CS-MARKET-02).
- Unsplash URLs (CS-IMG-SRC-01 · Pexels-only).
- Fake credentials (CS-EXEC-03 · "Certified X Expert" banned).
- `--primary-2: #2c3e6b` hardcoded (AP7 · CS-PAL-03).
- Any URL appearing in `business-{corporate,architecture,fiscal,coaching,stewardship}` pools (CS-IMG-SRC-04).

---

## §4 · Tone

| Field | Value |
|---|---|
| Tone label | evidence-first · litigation-precise · public-record register |
| Register | `Lei` polite Italian · forensic-publication voice · third-person studio voice ("Lo studio incardina · Lo studio sostiene") |
| Stance | evidence-as-the-argument · "we plead what is incardinated, not what is opined" · adversarial-resolution oriented |
| Audience verb | **plead** (the visitor is asking whether this firm will litigate a complex case before a court) |
| First-30-second read (target) | "an evidence-led Cassazionista boutique · we'd entrust a landmark case to them" |
| Stakeholder one-liner (target) | "evidence-led Cassazionista litigation · public-record proof" |
| What it must NOT read as | a SaaS · an advisory firm (Pragma) · an architecture studio (Cornice) · a tax studio (Fiscus) · a coach (Solaria) · a family-office (Continua) · a corporate-banner law firm (the generic legal-website default) |

The "remove the studio name — would it still work?" CS-TONE-05 test must pass: a reader who never sees the wordmark must still read "this is an evidence-led Cassazionista boutique" from the first scroll alone.

---

## §5 · Hero subject class · the 1-second read

| Field | Value |
|---|---|
| Hero subject class | **empty courtroom interior** · architectural-aula · vertical timber + bone walls · cool-light · zero people · landscape-or-portrait depending on candidate URL |
| Imagery direction (DNA) | **legal-courtroom-interior** (or `legal-aula-interior` if the latter parses cleaner in the seeder) |
| Pool source | new pool `business-legale` · Pexels-only · 6 URLs minimum · zero overlap with `business-{corporate,architecture,fiscal,coaching,stewardship}` (CS-IMG-SRC-04 grep · automated) |
| Subject density | zero people · interior-architectural |
| Color temperature | cool light · daylight through high windows or muted interior · NOT warm-mahogany (Continua) · NOT golden-hour (Cornice) |
| Why this works | The aula di tribunale is a 1-second-readable "this firm pleads in court" cue. Different geographical / material register from Cornice's exterior portico AND from Continua's mahogany reading-room. Object-led + zero-people composition fits LF-2's editorial-publication register without colliding with Cornice's exterior architecture or Continua's interior stewardship-archive. |

Backup subject class (if courtroom-interior pool is too thin at curator scout): **legal-codex spread on a desk** (open law tome with annotations + brass stamp/seal · close-up object-led · zero people). Still object-led + zero-people, still LF-2-fitting; risk = visual proximity to Fiscus's "tidy desk + documents" — mitigated by close-up zoom on the codex (NOT a wide desk shot).

---

## §6 · Section rhythm · LF-2 B verbatim

```
slot-1 · cs-hero                  · stacked-editorial · empty courtroom photo TOP · 8/4 below-fold (h1 LEFT · side-quote RIGHT)
slot-2 · cs-narrative             · evidence-led method essay · drop-cap p1 (bone-tinted on cool · NOT rust) · 3 pull-quotes (each 1 em-word) · sticky 4-link side-rail (Studio · Materie · Pubblicazioni · Contatti — NOT verbatim from Cornice)
slot-3 · cs-sectors-ribbon        · 12-cell typology row carrying legal practice areas (Penale tributario · Civile contrattualistica · Amministrativo regolatorio · Contenzioso bancario · Responsabilità professionale · Recupero crediti complesso · Diritto societario contenzioso · Tributario · Esecuzioni · Lavoro complesso · CTU forense · ENCA mediation)
slot-4 · cs-leadership-single     · single-portrait masthead · senior Cassazionista in chambers · 2-paragraph bio · 4 credentials
slot-5 · cs-cases-magazine        · 3+1 grid · 1 hero card (lead landmark sentenza) + 3 small (supporting sentenze · all public-record)
slot-6 · cs-cta-closer-cream      · cream paper · hairline obsidian borders · filled-bottle-green CTA pill · voice anchor verbatim
```

Six sections · zero dark bands on home · CS-TONE-03 inherited demotion (LF-2 family-scoped).

---

## §7 · CTA personality

| Field | Value |
|---|---|
| Primary CTA copy | **"Apri un parere preliminare"** |
| Mental model | **parere-screening-then-mandate** · the firm gives a preliminary legal opinion before deciding to take the case · evidence-and-jurisdiction intake (NOT contact + reason · NOT P.IVA/CF · NOT NDA · NOT discovery-call · NOT mandate-dialogue · NOT fascicolo) |
| Conversion form fields | (oggetto del contenzioso · grado di giudizio attuale · controparte · fascia di valore · urgenza · evidenza preliminare allegabile · giurisdizione) |
| CTA closer h2 (voice anchor surface 2) | verbatim recurrence of hero h1 anchor sentence (em on `evidenza`) |
| Tone | evidence-bound · screening-before-mandate · forensic-publication register |
| Must NOT be | "Get started free" · "Sign up" · "Iscriviti gratis" (CS-CTA-02) · "Fissa una call privata" / "Apri un fascicolo progetto" / "Primo appuntamento" / "Prenota una discovery call" / "Avvia un dialogo di mandato" (taken) · any fascicolo / dossier / "open a case file" mental model (AC-8) |

---

## §8 · Multilingual expectation

Per D-102 cadence: A.5 ships **IT only**. Workflow C (post review-lock + user handshake) extends to **5 locales (IT/EN/FR/ES/AR)** with AR RTL parity.

Voice anchor recurrence across locales (CS-EXEC-01 · F2 · per `cornice-lf2-reference-pack.md §D1` LF-2 rule):

| Locale | Anchor sentence (working draft · planner re-bids) | em-word |
|---|---|---|
| IT | `Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.` | `evidenza` |
| EN | `Every ruling is <em>evidence</em> on the record — not an opinion defended.` | `evidence` |
| FR | `Chaque décision est une <em>preuve</em> versée au dossier — non une opinion défendue.` | `preuve` |
| ES | `Cada sentencia es una <em>evidencia</em> incardinada — no una opinión defendida.` | `evidencia` |
| AR | `كلُّ حكمٍ <em>دليلٌ</em> مُثبَتٌ في السجل، لا رأيٌ يُدافَع عنه.` | `دليل` |

The em moves with the **public-record-evidence sense** in every locale (NOT proof-as-statistics, NOT testimony, NOT clue — *evidence-on-the-record*). Translator brief at workflow C carries this as a binding contract.

AR h1 inherits **Naskh** via LF-2 family-scope (`body.cs-lf-lf-2` selector · zero leakage to LF-1/LF-3/LF-4/LF-5 · re-verified at workflow D + public flip per `cornice-lf2-reference-pack.md §D9`).

Voice anchor lives on **exactly 2 home surfaces**: hero h1 + CTA closer h2 (per AC-15). NOT on the navbar wordmark, NOT on the side-quote, NOT on an interstitial.

---

## §9 · Skin axes · concrete values

| Axis | Value | Rationale (vs which sibling) |
|---|---|---|
| Heading serif | **GT Sectra** (or Source Serif Pro as licence-fallback) | ≠ Merriweather/Cormorant/Plex Serif/Fraunces/Crimson Pro · forensic-publication register · matrix §1.4 open-territory pre-fill |
| Body sans | **Manrope** | ≠ Inter/Source Sans 3/Plex Sans/Public Sans · matrix §1.4 open-territory · Inter explicitly prohibited (cluster body-sans differentiation gate) |
| Italic em strategy | one em per heading on `evidenza` · 2-surface verbatim recurrence (LF-2 family rule) · NOT two-em contrast pair (Solaria's exception) | per AC-15 |
| Palette primary | **bottle-green** (e.g. `#14342B`-class · L\* ≤ 40 on cream · `is_primary_safe_on_cream()` PASS · NOT pine `#0F3A30` Continua) | full cool · evidence-led-forest register |
| Palette secondary | **bone** (e.g. `#F0EBE0`-class · warmer than pietra-serena `#cdc9c0` · cooler than fiscus's warm-neutral cream) | matte-on-matte editorial · ≠ pietra-serena (Cornice) ≠ pewter (Continua) ≠ warm-neutral (Fiscus) |
| Palette accent | **obsidian** (e.g. `#0B0A0E`-class · deep neutral · zero metallic) | ≠ rust (Cornice display-only) · ≠ brass (Continua chrome-only) · ≠ emerald/gold/caramel (Pragma/Fiscus/Solaria) · third polarity dimension per matrix §1.3 ("matte-on-matte without metallic") |
| Macro tone | bottle-green + bone + obsidian (full cool · matte-on-matte · zero metallic) | clean polarity differentiator vs Continua's cool-with-warm-metallic |
| Hero geometry | stacked-editorial (LF-2 inheritance) | per AC-1 |
| Hero meta-strip | KPI-in-hero-overlay `(N landmark sentenze · pubblicazioni in massimario · anni di patrocinio)` | LF-2 family-shared shape · DIFFERENT cell content from Cornice's `(novanta fascicoli · 2008 · 38 menzioni)` per AC-2 |
| Hero credit overlay | `(Albo Avvocati Milano · Cassazionista dal AAAA)` | ≠ `(Direzione, Anno fondazione)` (Pragma + Fiscus) · ≠ `(Disciplina, Anno)` (Continua) · ≠ KPI tuple (Cornice) |
| Section sequence | LF-2 B verbatim | per AC-1 |
| Pillars treatment | essay-with-anchors (LF-2 inheritance) | per AC-1 · evidence-led method essay |
| KPI placement | hero-overlay (LF-2 inheritance) | per AC-1 |
| Leadership composition | single-portrait masthead (LF-2 inheritance) · senior Cassazionista in chambers · NOT studio-with-drafting-tools (Cornice) · NOT mahogany partner-desk (Continua) | per AC-1 + AC-9 environmental-not-studio binding |
| Leadership credentials | Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario · Albo CTU | ≠ Cornice (OAPPC/MIBAC) · ≠ Fiscus (Sezione A/Revisore Legale) · ≠ Pragma (Partner/Senior/Counsel) · ≠ Solaria (ICF/EMCC/AICP) · ≠ Continua (Custode/Governance/Compliance fiduciaria) |
| Cases-preview shape | magazine-grid 3+1 (LF-2 inheritance) · public-record proof | per AC-1 + AC-10 hero-card-as-lead-story binding |
| Proof tactic | **public-record** (sentenze citate · giurisprudenza · massimario · expert testimony engagements) | matrix §1.10 open-territory · ≠ numeric (Pragma/Fiscus) · ≠ curatorial-architectural (Cornice) · ≠ qualitative-method (Solaria) · ≠ longitudinal (Continua) |
| Trust band | sectors ribbon only · NO trust marquee · LF-2 family signature (per Cornice walk) | per Cornice precedent · sectors-ribbon absorbs trust function |
| Navbar | LF-2 cream-paper masthead (`cs-nav--lf2`) · split-line `CAUSA / studio legale` · 5-link inline (`Studio · Materie · Pubblicazioni · Contenzioso · Contatti`) · filled-bottle-green trailing CTA pill (NOT rust · NOT brass) · NO phone-right | per AC-11 inheritance · DIFFERENT wordmark + CTA fill colour |
| Footer | 4-col-with-whistleblowing (LF-2 + LF-5 family-shared primitive) · 4th column = D.lgs. 24/2023 forensic-firm channel | per AC-12 inheritance · DIFFERENT column content (forensic-firm channel · NOT architecture studio's, NOT stewardship firm's) |
| AR h1 | Naskh (LF-2 family-scoped · `body.cs-lf-lf-2`) | per AC-13 inheritance · do NOT re-bind |
| Voice anchor | `evidenza → evidence → preuve → evidencia → دليل` · 2-surface verbatim recurrence (hero h1 + CTA closer h2) | per AC-3 (NOT a curatorial-thesis cognate) · per AC-15 (exactly 2 surfaces) |
| CTA primary | "Apri un parere preliminare" · parere-screening mental model | per AC-8 (NOT fascicolo / dossier semantic family) |
| Motion | inherited cluster invariant · low motion · staggered reveals · `prefers-reduced-motion` honored · NO marquee (LF-2 family signature) | matrix §1.11 · do NOT differentiate via motion |
| Stakeholder one-liner | "evidence-led Cassazionista litigation · public-record proof" | passes CS-TONE-05 distinctness · audience verb = "plead" (unclaimed) |

---

## §10 · Review posture

| Gate | Posture |
|---|---|
| Walk gates inherited from LF-2 | F2-WALK-1 through F2-WALK-12 per `cornice-lf2-reference-pack.md §7` · all 12 gates apply verbatim · the 2nd LF-2 occupant clears each independently |
| Risks inherited from LF-2 | R-LF2-1 through R-LF2-8 per `cornice-lf2-reference-pack.md §8` · all 8 risks re-fire on Causa · planner brief mitigates each at A.5 build, not at A.6 |
| Walk budget | per AC-16: lower entry cost than Cornice's first occupancy · expect 4 passes (A.5 → A.6 → C → flip) · workflow D folded into C if multilingual walk lands clean |
| User-handshake gates | tier flip held until explicit user authorization · per R-SOL-8 / CS-BLOCK-13 / D-102 cadence · same shape as Continua + Cornice flips |
| Review-lock posture | tier=draft preserved through A.5 + A.6 · public flip cascade (registry + sync_template_tiers + 7 explicit-literal test bumps + related-templates rebinding if Causa promotion bumps anyone past category-fallback ceiling) deferred until user handshake |
| Frozen-sibling regression budget | 0 px wireframe drift on Pragma · Cornice · Fiscus · Solaria · Continua at every gate (per F2-WALK-12 · 5 × 200 anonymous + 0 px wireframe) |
| Booking-flag cohort | Causa is litigation-shaped · `has_booking=False` likely (lawyer cohort defaults FALSE in `apps/catalog/tests.py · test_medical_and_restaurant_templates_have_booking_flag`) · planner verifies the test cohort at A.5 build |
| Image curator clearance | new `business-legale` Pexels pool · 6 URL minimum · zero overlap grep against the 5 existing pools · curator-bind environmental-not-studio composition for the masthead portrait BEFORE build (R-LF2-1 mitigation) |

---

## §11 · The five "must clear at intake" questions (per `cornice-lf2-reference-pack.md §9`)

1. **Is Causa's professional fit genuinely portfolio-of-work-led?** **YES.** A Cassazionista boutique's proof is its case-bundle (sentenze citate, giurisprudenza, expert testimony in massimario, ENCA mediations). The firm pleads cases; its history is its publication.
2. **Does Causa have ≥4 publishable case studies with editorial weight?** **YES (planned).** A real Cassazionista boutique typically has multiple landmark sentences per year; Causa's content brief at A.5 ships 4 cases (1 hero landmark + 3 supporting). Planner authors them at A.5.
3. **Does Causa's voice register tolerate a curatorial noun anchor?** **YES.** `evidenza` lands as a forensic-publication noun, not a service-oriented or outcome-oriented one. The em recurrence reads as a method statement, not a marketing claim.
4. **Does Causa's hero photography subject differ materially from Bologna golden-hour portico?** **YES.** Empty courtroom interior · cool light · zero people · vertical timber + bone walls. Different geographical (courtroom-not-portico), different material (timber+bone-not-stone), different temperature (cool-not-golden-hour) registers.
5. **Does Causa have a single principal whose portrait carries the masthead?** **YES.** Single-principal Cassazionista (the firm's founder · 50s-or-senior). 2-3 associati support but do not appear on the masthead — they live in a Studio page if needed.

All 5 questions clear. The LF-2 second-occupant intake is authorized at the family-fit level. Sibling 6 plan sign-off proceeds at workflow A.2 once the user authorizes the territory.

---

## §12 · The exact next action after this intake

> **Hold for user authorization of the territory (Causa · evidence-led Cassazionista litigation boutique · LF-2 second occupant).** On authorization, open Phase X.6 Step 1 = workflow A.2 planner brief at `factory/reports/causa/causa-planner-brief.md`. The planner brief copies §1, §3, §9 of this intake into the brief verbatim (per CS-EXEC-02 anti-drift binding), files the 5×12 collision-check matrix per `next-template-brief-schema.md §2`, fills `template_dna_fields` per `next-template-brief-schema.md §3`, and locks the curator pack for `business-legale` Pexels URLs. **No application code, registry, or tier change at Step 1.** Build (workflow A.5) is Step 2 and is gated on planner-brief sign-off at Step 1.

This intake is **paper-only**. It is the recommended candidate, not a build authorization.

---

## §13 · Strongest conclusion

**Causa — evidence-led Cassazionista litigation boutique at LF-2 second occupant — is the recommended 6th sibling.**

The territory is the right next move because:
- It validates LF-2 as a re-runnable family (the cluster's first scaling test for family repeatability).
- It expands the catalog with a genuinely missing professional fit (lawyer at premium tier) and a missing proof tactic (public-record).
- It scores 5/5 vs every live sibling on skin axes and inherits LF-2's L1–L9 verbatim per AC-1 (layout-axis distinctness is family-shared by intent).
- It has no near-occupant § decision to file (CS-LAYOUT-12 is satisfied by family inheritance).
- It has the lowest unknown-cost of the three serious candidates (the recipe is documented end-to-end in `cornice-lf2-reference-pack.md`).
- It does not bundle family-extensibility-test (LF-6 activation) with sub-cluster build, preserving the post-Cornice readiness pass's discipline of "one objective per session."

**Phase X.6 Step 1 (workflow A.2 planner brief · paper-only) may start once the user authorizes the territory.** Until then, Phase X.6 is held at Step 0 = these three files.
