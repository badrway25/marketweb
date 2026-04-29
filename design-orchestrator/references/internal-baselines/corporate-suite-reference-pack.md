# Corporate-suite internal reference pack

**Status**: operational v1 · **Date**: 2026-04-28
**Source templates**: Pragma (advisory · `published_live`) · Fiscus (commercialista · `published_live`) · Solaria (coaching · `draft`, controlled re-entry, IT 5-locale GREEN, public flip held)
**Audience**: planner · builder · style-critic · browser-verifier when shaping the **next** corporate-suite sibling.
**Companion files**: `corporate-suite-distinctness-matrix.md` (sibling diff) · `next-template-brief-schema.md` (intake template).
**How to use**: read this once at intake to know what is already taken, what is reusable, and what is dangerous to copy. Cross-reference rule IDs in `factory/standards/corporate-suite-design-standard.md`.

---

## 1 · What each current template does best · do NOT clone

The single move that gives each template its identity. The next sibling must NOT do the same move on the same axis.

### Pragma — boardroom gravity
- **Best move**: hero KPI-strip ("22 anni · 180+ mandati · €1.4 B · 94%") sits ON TOP of the sectors ribbon, reading as institutional weight before the first scroll. This is the "decisions that matter" anchor made visual.
- **Don't copy**: KPI tuple in the hero meta-strip with €/years/clients/% as the four cells. The next sibling's hero meta-strip must declare a DIFFERENT proof-shape (process, cadence, certification, jurisdiction, etc.).
- **Don't copy**: the trio Headquarters / Equipe senior / Mandati attivi as the meta-strip composition.
- **Don't copy**: navy + emerald + cream macro tone.

### Fiscus — calendar-as-proof
- **Best move**: fiscal-calendar-strip in the hero (replacing the generic KPI tuple) — proves the firm's value lives in the calendar. Voice anchor "L'adempimento corretto, non la trovata" is paid off by showing the visitor a calendar, not numbers.
- **Don't copy**: hero meta-strip leading with Sede / Albo / Clienti as the three cells. Already taken.
- **Don't copy**: the section-order beat `hero → pillars → kpi → fiscal-calendar → sectors → cases → cta`. The fiscal-calendar slot is Fiscus's claim.
- **Don't copy**: warm-neutral cream + blu-notte + gold filigrana macro tone.
- **Don't copy**: scrivania + documenti hero photography. Already the Fiscus visual.

### Solaria — declared method
- **Best move**: percorso-cadenza-strip ("inizio dichiarato → cadenza → fine dichiarata") as the hero meta-strip. Voice anchor "Il coaching non è terapia e non è consulenza" is paid off structurally — the visitor SEES the bounded path.
- **Best move**: leadership cards ship REAL portrait photos above the fold (CS-IMG-SEC-03 first exercise on this archetype). Pragma + Fiscus use typographic-only leadership.
- **Don't copy**: percorso-cadenza-strip composition. Already Solaria's.
- **Don't copy**: 3-percorsi enumeration with explicit session count + cadence. Already taken.
- **Don't copy**: minimal-light + warm-earth (ocra/caramel) macro tone.
- **Don't copy**: 1:1 conversation hero photography. Already the Solaria visual.

---

## 2 · Reusable premium patterns (DO inherit verbatim)

These are skin-level / archetype-level patterns. The next sibling MUST inherit them — they are the cluster's premium contract, not a stylistic choice.

| Pattern | Source rule | Why reuse |
|---|---|---|
| 55/45 hero split · serif h1 LEFT + one full-bleed editorial photo RIGHT | CS-HERO-01 | Cluster silhouette · differentiation happens in palette/voice/imagery, NOT in hero shape. |
| Italic `<em>` on one load-bearing word per heading · no uppercase, no bold for emphasis | CS-TYPE-02 | Restraint-as-emphasis is the cluster typography signature. Breaking it reads SaaS. |
| `padding: 100px 72px; max-width: 1400px; margin: 0 auto` on every section wrapper | CS-RHYTHM-01 | The padding IS the rhythm. Compressing it is the most common silent quality loss. |
| Tabular numerals on every KPI figure (`.num` / `font-variant-numeric: tabular-nums`) | CS-TYPE-03 | Without it, "180+" and "94%" misalign across locales. Invisible until RTL. |
| One dark band per home placed at position 3 (KPI band) | CS-TONE-03 / CS-RHYTHM-03 | Editorial punctuation. Two dark bands reads aggressive. Three reads SaaS funnel. |
| Sticky dark navbar with `--primary` background + accent CTA at the trailing edge | CS-NAV-01 / CS-NAV-04 | Palette identity flows through chrome. The single accent CTA is the chrome's only colored element. |
| Outline-only primary CTA on cream paper · solid accent fill ONLY in the dark `.cs-cta` band | CS-CTA-01 § decision (2026-04-26) | Boardroom-button convention. Filled-on-cream reads SaaS. Ratified, do not re-litigate. |
| `:focus-visible` gold ring (accent color · 2px outline · 4px offset) | CS-NAV-02 / E1 | Keyboard accessibility AND the cluster's signature interactive moment. |
| Locale switcher as a pill with `lang` + `dir` per link | CS-NAV-03 / D5 | Multilingual is mandatory. Pill shape is the cluster convention. |
| Anonymized proof = sectors text ribbon + association marquee (NEVER fake client logos) | CS-COMP-01 | Advisory secreto professionale. Same constraint applies to lawyer / coaching / fiduciary. |
| Three-column footer · brand + sitemap + contact · `--primary` background | CS-FOOT-01 | Match navbar polarity. Footer is the chrome's bookend. |
| Voice anchor preserved verbatim across all 5 locales | CS-EXEC-01 / F2 | The single sentence that carries the template. Translates but stays identifiable. |

---

## 3 · Risky inherited / shared patterns (audit before reuse)

These are real artifacts in today's skin that work for the existing three but **must be re-evaluated** before the next sibling ships. They are the load-bearing fault lines.

### R1 · `--primary-2` hardcoded in `_base.html:20`
- Value is `#2c3e6b` (Pragma's navy). Hurts every non-Pragma palette.
- AP7 known issue. CS-PAL-03 prohibits it. Today still in the skin.
- **Action for next sibling**: do not introduce code that reads `--primary-2`. If you need a tinted primary, derive server-side from the three palette tokens.

### R2 · No `<720px` hero stack in the corporate-suite skin
- AP2. Hero stays horizontal on mobile. Fixed in agency archetype, NOT yet in corporate-suite.
- CS-HERO-07 / CS-RESPONSIVE-01 require this fix as a ship gate.
- **Action for next sibling**: add `@media (max-width: 720px) { .cs-hero { grid-template-columns: 1fr; } }` to the skin BEFORE first build. Do not ship without it.

### R3 · Pragma still on Unsplash imagery (legacy `business-corporate` pool)
- CS-IMG-SRC-01 mandates Pexels. Pragma was grandfathered.
- **Action for next sibling**: Pexels-only from URL #1. No Unsplash, no AI imagery, no custom photography. CS-IMG-SRC-01 has no exception for new templates.

### R4 · `body.mw-is-editor-preview` guard on click-to-edit affordances
- A4 / A5 pattern · `_base.html:441`. Already correct.
- **Action for next sibling**: when copying skin partials, never strip the `body.mw-is-editor-preview` guard from a `:hover` rule. Editor-only affordances must NOT leak into `/templates/<slug>/live/` (CS-MARKET-01).

### R5 · Hero meta-strip composition copies easily into siblinghood collapse
- All three siblings used the meta-strip differently (KPI tuple · fiscal-calendar · percorso-cadenza). The shape itself is reusable; the **composition** is the differentiation surface.
- **Action for next sibling**: choose a meta-strip composition that names the firm's PROOF SHAPE (e.g. "iscrizione → giurisdizioni → contenzioso pendenti", "albo → numero pratica → ricorsi vinti", "data fondazione → numero notai → atti rogati"). Do not reuse one of the three existing shapes.

### R6 · `cs-` class prefix is mandatory; Bootstrap classes cannot replace it
- CS-COMP-07. New components must follow `cs-{name}`.
- **Action for next sibling**: do not import `container-fluid row col-md-4` to avoid writing CSS. The scoped prefix is what keeps the archetype editable in isolation.

### R7 · Voice anchor copied without the load-bearing italic-em wrap
- F2 / CS-EXEC-01. Anchor lives in `home.html` h1 with `<em>` on the load-bearing word.
- **Action for next sibling**: when authoring the IT anchor, decide which word carries the italic BEFORE the planner sign-off. The word must survive translation (translator brief tells the FR/ES/AR translator which word to italicise post-translation). Solaria's anchor uses TWO em-wraps (`terapia`, `consulenza`); that is acceptable only when the anchor is built on a contrast pair. Default is one em-wrap.

---

## 4 · Imagery rhythm observations

### What the three packs actually do
- **Pragma (`business-corporate`)**: boardroom long-table (hero) · corporate atrium (feature) · executive portraits (slots 2-3) · industrial facility + conference detail (slots 4-5). **Mood**: serious daylight, deep depth-of-field, NO smiles in portraits. **Subject density**: 1-2 people max per frame.
- **Fiscus (`business-fiscal`)**: tidy desk with laptop + documents + eyeglasses (hero) · contemporary office interior (feature) · giacca-senza-cravatta portraits (slots 2-3) · tax documents close-up (slot 4) · law/regulation bookshelf (slot 5). **Mood**: warm-neutral institutional, document-centric. **Subject density**: documents foregrounded, people incidental.
- **Solaria (`business-coaching`)**: 1:1 conversation in bright meeting room (hero) · man writing in notebook (feature) · woman with clipboard (slot 2) · confident businesswoman arms-crossed (slot 3) · open notebook + pen on wood desk (slot 4) · warm home-office with plants (slot 5). **Mood**: minimal-light, conversational, human. **Subject density**: people foregrounded with object support.

### Rhythm rules the cluster follows
1. **Slot 0 (hero) sets the entire mood.** It is THE photo a first-time visitor remembers. Treat it as the brand decision — choose it before copy.
2. **Slot 1 (feature) is the "wide context" shot.** Used on `about.html` hero and as second-section accent on home. Reads as institutional environment.
3. **Slots 2-3 (portraits)** are square-ish (≥800×800), match the firm's actual age/gender mix, NEVER use the gray-silhouette placeholder, NEVER reuse slot 0.
4. **Slot 4 (detail)** is the "what we do" close-up — documents, instruments, artifacts. Replaces "fake handshake" stock with semantic proof.
5. **Slot 5 (ambient)** is the "where we work" environmental shot — bookshelf, atrium, plant-lit corner. Reads as place.
6. **Zero URL overlap across siblings** (CS-IMG-SRC-04). The grep is automated. New URLs only.

### Risks observed (don't repeat)
- Pragma's slot 5 conference detail blurs into Fiscus's institutional bookshelf if the next sibling re-uses bookshelf semantics. **Pick a non-bookshelf ambient.**
- Solaria's slot 2 (woman with clipboard) and slot 3 (businesswoman arms-crossed) are both 30-something Caucasian; the next portrait-bearing sibling needs visible age/gender/ethnicity diversity OR a different framing entirely (3/4 profile, side light, environmental portrait).
- All three heroes have a single human focal point (Pragma: 4-person table · Fiscus: implied solo at desk · Solaria: 2-person 1:1). Next sibling can break this by going **object-led** (e.g. legal codex spread on a desk, notary seal on parchment, fiduciary safe deposit ledger) — with people incidental or absent.

---

## 5 · Typography rhythm observations

### Heading family taken
| Sibling | Heading | Body | Notes |
|---|---|---|---|
| Pragma | Merriweather | Inter | Transitional serif · most "newspaper editorial" of the three. |
| Fiscus | IBM Plex Serif | IBM Plex Sans | Document-pair · consistent family across heading + body · most "tax-form formal." |
| Solaria | Fraunces | Inter | Humanist serif · most warm/contemporary · supports varied OpenType features. |

### What the next sibling can choose (orthogonal to above)
- **Lora** (Polish-Italian transitional · contemporary book-jacket reading)
- **Source Serif Pro** (Adobe sans/serif duo · works with Source Sans body)
- **PT Serif** (Russian transitional · narrower x-height than Merriweather)
- **Cormorant Garamond** (Garamond revival · more elegant/luxury · careful at small sizes)
- **GT Sectra** (modern editorial · sharper personality · paid)
- **Recoleta** (display serif · use for h1 only, pair with neutral body)
- **Spectral** (humanist · highly readable at body sizes if paired across heading+body)
- **Crimson Pro** (book-jacket reading · classical ratios)

### Typography rules the cluster follows
1. **Serif h1 + sans body, never inverted** (CS-TYPE-01). Geometric sans on headings is blocked (Montserrat, Poppins, Raleway).
2. **Italic `<em>` is the only emphasis mechanism in headings** — no bold, no uppercase, no color shift. CS-TYPE-02.
3. **Heading scale is restrained**: hero h1 44-72px · section h2 32-48px · card h3 22-28px (CS-TYPE-04). NO 96px neon display.
4. **Eyebrow / label uppercase tracking 0.22em · body tracking 0** (CS-TYPE-05). RTL resets all 0.22em to 0.
5. **Arabic locale swaps to Noto Kufi heading + Amiri body** under `html[dir="rtl"]` (CS-TYPE-06). Latin wordmark + `.num` keep Latin heading font.

### Risks observed
- Pragma + Solaria share Inter as body. Two of three is fine; if the next sibling also picks Inter, three of four feels like the cluster is "Inter-on-anything." **Strongly prefer a different sans body** for the next sibling (IBM Plex Sans is taken; Source Sans Pro, Spectral, Public Sans, Manrope-as-body are open).

---

## 6 · Section pacing observations

### What home looks like across the three
- **Pragma**: hero → 3-pillar advisory grid → KPI band (dark) → sectors ribbon → leadership (3 partners) → cases (3-6) → CTA.
- **Fiscus**: hero → 3-pillar competence grid → KPI band (dark) → fiscal-calendar-strip → sectors ribbon → cases → CTA.
- **Solaria**: hero → manifesto → 3 percorsi enumeration → KPI band (dark) → method-cadenza-strip → cases → CTA. (No leadership block — single-coach focus.)

### Cluster constants (do not vary)
- ONE dark band on home (the KPI band, position 3-4). CS-TONE-03.
- Hero is always position 1, CTA closer is always last.
- No two adjacent sections share function (CS-RHYTHM-04).
- Pillars section is 3 or 4 cards, NEVER 6 (CS-DENSITY-02).
- KPI band is 3 or 4 stats, NEVER 5+ (CS-DENSITY-04).

### Cluster variables (the next sibling chooses one to claim)
- **Position 4-5 mid-strip** (Fiscus = fiscal-calendar · Solaria = method-cadenza · Pragma omits this beat). Open variants: `process-cadence`, `jurisdiction-strip`, `licensure-timeline`, `methodology-stages`, `compliance-cycle`. Pick one, name it, ship it as the differentiator.
- **Leadership block**: present (Pragma 3 partners · Fiscus 4 ODCEC) or absent (Solaria, single-coach). The next sibling decides based on org shape — if it's a multi-partner firm, present; if it's a sole practitioner, omit and shift weight to method/manifesto.
- **Sectors ribbon label**: "Settori di intervento" (Pragma) · "Settori dei clienti" (Fiscus) · "Profili dei coachee" (Solaria). The label IS the audience-positioning. Choose one that names the firm's view of who it serves.

---

## 7 · Navbar & footer observations

### Navbar — what is identical, what varies
**Identical (do not change)**: sticky · `background: var(--primary)` · 5-7 links · locale-pill · trailing accent CTA · `:focus-visible` gold ring · 4 link states (default/hover/focus/active) · Latin wordmark under RTL (CS-NAV-06).

**Varies**:
- **Wordmark style**: Pragma "Pragma Advisors" (full word + descriptor) · Fiscus "Fiscus" (single word) · Solaria "Solaria" (single word). Single word is the cluster default; full descriptor reads enterprise.
- **Nav links count**: Pragma 5 (`Chi siamo · Competenze · Settori · Board advisory · Contatti`) · Fiscus 5 (`Lo studio · Competenze · Scadenze · Casi seguiti · Contatti`) · Solaria 5 (`Il metodo · Il coach · Percorsi · Casi · Contatti`). Five is the cluster default.
- **CTA label** mirrors the conversion pattern: Pragma "Fissa una call privata" · Fiscus "Primo appuntamento" · Solaria "Prenota una discovery call". The next sibling's CTA is part of the voice; do not reuse.

### Footer — what is identical, what varies
**Identical**: 3 columns (brand + sitemap + contact) · `--primary` background · legal row at bottom · Latin wordmark + Latin numerics under RTL · footer stacks to 1 column at ≤720px (CS-FOOT-05 — currently MISSING in skin, fix at first build).

**Varies**: legal row content. Whistleblowing link is REQUIRED for commercialista/law/advisory clusters per D.lgs. 24/2023; optional elsewhere (CS-FOOT-02). The next sibling's planner names the legal row up front.

---

## 8 · What "premium" concretely looks like in this archetype

The four-adjective decomposition from CS §1, in operational vocabulary:

### Premium = generous restraint
- 100×72 section padding. 1400 max-width. 96-100px vertical rhythm.
- One editorial photo per surface. No 4-up grids on hero. No gradient sweeps.
- Accent color appears ≤ 2-3 times per viewport (CS-PAL-05).
- Tabular numerics on every figure.
- Hero photo carries a credit overlay reading "Reportage / Studio X / City" — moves the photo from "stock" to "editorial".

### Elegant = serif italic-em + boardroom buttons
- Serif heading + italic `<em>` on the load-bearing word.
- One dark band on home (the KPI band).
- Outline primary on cream + filled accent on the dark CTA band. Polarity inversion is the cluster's signature CTA move.
- Letter-spacing 0.22em ONLY on uppercase eyebrow labels. Body and headings = 0.

### Modern = CSS custom properties + RTL via logical properties + focus-visible
- Three-token palette (`primary / secondary / accent`). No fourth.
- Logical properties (`margin-inline-start`, `padding-block-end`) so RTL works without duplicate CSS.
- Gold `:focus-visible` outline, never browser-default blue.
- Reduced-motion honored (`@media (prefers-reduced-motion: reduce)`).
- Three real breakpoints: 1100 · 880 (contact) · 720.

### Professional = verifiable credentials + boardroom KPIs + zero hyperbole
- Credentials are real albo IDs (ODCEC, CONSOB, ICF-PCC, Cassazionista). No "Certified Life Transformation Expert".
- KPIs are clean rounded figures ("180+", "94%", "€ 1.4 B"). No fake-precise decimals.
- First-person-plural firm voice ("Noi seguiamo…"). Never product-voice ("Our platform helps you…").
- No marketing hyperbole bank: "sblocca il tuo potenziale", "trasforma la tua vita", Einstein quotes — banned at standards level (CS-EXEC-04).
- Anonymized proof only (sectors ribbon + association marquee, never client logos for advisory clusters).

---

## 9 · Standing red flags that signal "feels like AI-generated SaaS"

If the next sibling shows ANY of these in a live walk, treat it as a 0/5 distinctness fail regardless of other scores (DISTINCTNESS_RULES §6):

- Inter on headings (geometric sans on h1)
- Purple gradient hero
- Cards-in-cards nesting
- Gray text on colored background
- Three accent buttons in the hero
- "Get started free" / "Sign up now" CTA copy
- Emoji in body or headings
- Exclamation marks outside testimonial quotes
- Backdrop-blur effects
- Celebrity quote (Einstein/Jung/Gandhi/Jobs)
- Mountain-peak hero photography
- "Trusted by 10,000+ clients" unverifiable claim
- "Made with Marketweb" footer attribution

The Impeccable detector and `factory/references/anti-pattern-library.md` are the canonical lists. This pack lifts the highest-impact ones for fast scan.

---

## 10 · Quick lookup — current cluster occupation

| Axis | Pragma | Fiscus | Solaria | Open territory for next |
|---|---|---|---|---|
| Sub-cluster | corporate advisory | commercialista presidio | executive coaching | notarile · law · fiduciary · revisione · brokerage · architecture-firm · independent-director |
| Voice anchor | decisional gravity | adempimento corretto | bounded percorso | jurisdiction-first · evidence-first · stewardship · custodial · longitudinal-care |
| Macro tone | navy + emerald + cream | warm-neutral + blu-notte + gold | warm-carbon + ocra + caramel | forest + brass · plum + cream · burgundy + pearl · deep-teal + champagne · sage + stone · charcoal + copper |
| Heading serif | Merriweather | IBM Plex Serif | Fraunces | Lora · Source Serif · PT Serif · Cormorant · Spectral · Crimson Pro · GT Sectra · Recoleta |
| Body sans | Inter | IBM Plex Sans | Inter | Source Sans · Public Sans · Spectral (sans) · Manrope · Work Sans (avoid Inter) |
| Hero meta-strip | KPI tuple | fiscal-calendar | percorso-cadenza | jurisdiction-strip · licensure-timeline · methodology-stages · compliance-cycle · custody-shape |
| Hero photography | boardroom long-table | tidy desk + documents | 1:1 conversation | object-led (codex/seal/ledger) · environmental-portrait · architectural-interior · workshop · library-reading-room |
| Conversion pattern | private-call · NDA-ready | appointment-request · P.IVA form | discovery-call · open-access | mandate-brief · scope-meeting · custodial-onboard · public-hearing-booking |
| Credentials axis | CONSOB + Bocconi | ODCEC + Revisore | ICF + EMCC + Co-Active | Albo Avvocati · Cassazionista · Albo Notai · ABI · Assogestioni · OAM · ANC |

When the next intake lands, fill the same row in `corporate-suite-distinctness-matrix.md` and verify ≥4 of 5 differentiation axes (DISTINCTNESS_RULES §1).

---

## 11 · One-paragraph summary

The corporate-suite cluster is occupied by a boardroom-advisory (Pragma · navy + emerald · KPI hero), a commercialista-presidio (Fiscus · warm-neutral + gold + blu-notte · fiscal-calendar hero), and an executive-coach (Solaria · warm-earth + ocra + caramel · percorso-cadenza hero). The cluster invariant is **institutional-advisory tone · serif heading + italic-em emphasis · one dark band on home · cream paper + outline-primary CTA · Pexels-only imagery · voice anchor verbatim across 5 locales · 55/45 hero split**. The next sibling MUST inherit those invariants and MUST claim a fresh palette family, fresh heading serif, fresh hero meta-strip composition, and fresh hero photography subject. If any one of those four is borrowed from an existing sibling without compensating differentiation on the others, the matrix scores ≤3/5 and the planner re-specs.
