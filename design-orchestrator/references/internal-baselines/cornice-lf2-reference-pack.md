# Cornice · canonical LF-2 reference pack

**Status**: reference v1 · post public flip · LF-2 first occupant
**Date**: 2026-05-01
**Source template**: Cornice (`cornice-architettura`) · `tier=published_live` · 5 locales · LF-2 · Editorial Spread
**Audience**: planner · builder · style-critic · browser-verifier when shaping a **future LF-2 sibling**.

**Companion files**:
- `corporate-suite-live-family-map.md` (5-sibling state)
- `corporate-suite-distinctness-matrix.md` (3-column · pending refresh)
- `corporate-suite-reference-pack.md` (3-column · pending refresh)
- `factory/reports/cornice/cornice-{a5-it-build,a6-it-review-lock,workflowC-multilingual,workflowD-release-decision,public-flip}.md`
- `factory/reports/hardening/corporate-suite-layout-{variance-rules,family-matrix}.md`

**Purpose**: Cornice is the cluster's first and only LF-2 occupant. This pack captures what Cornice is, what makes it genuinely a different family rather than a Pragma re-skin, and what a future LF-2 second occupant must NOT copy from it. Read this BEFORE filing an intake for any portfolio-of-work-led firm.

---

## §1 · One-paragraph summary

Cornice is a single-principal Milanese architecture studio (Marta Roveri · STUDIO DI ARCHITETTURA · DAL 2008) whose proof is its case-bundle, not its partner roster or its calendar or its KPI tuple. The home reads as a publication, not a website: a full-bleed Bologna golden-hour portico hero with a credit-overlay KPI tuple at the bottom-left, an 8/4 below-fold split with a serif h1 left and a side-quoted intro right, a rust drop-cap narrative essay with three pull-quotes and a sticky 4-link side-rail, a sentence-ribbon of architectural typologies, a single-portrait masthead of the founder with a 4-credential bio, a 3+1 magazine grid of cases (1 hero card + 3 small), and a hairline-bordered cream CTA closer. The chrome reads as editorial: a cream-paper navbar with a split-line masthead (`CORNICE / studio di architettura`) + filled-rust trailing CTA, a 4-col footer with a whistleblowing column. The voice anchor `Ogni progetto è un argomento costruito, non un servizio reso.` lands verbatim on the hero h1 and the CTA closer h2; the italic em moves with the curatorial noun across 5 locales (`argomento → argument → argument → argumento → حُجَّة`). The AR locale uses a LF-2-scoped Naskh h1 swap (selector: `body.cs-lf-lf-2`) — the cluster default Kufi h1 is preserved on every other family. Zero dark bands on home (CS-TONE-03 demoted at the family level, declared and ratified). 4-col-with-whistleblowing footer is shared with LF-5 by intent; column content is sub-cluster-specific.

---

## §2 · Why Cornice is genuinely LF-2, not a new skin

The challenge LF-2 poses (and that LF-3, LF-4, LF-5 also posed at their own enrollments) is "how is this different from a palette swap of the existing cluster shape?" Cornice answers it on **9 of 9 layout dimensions** vs Pragma (LF-1), **9 of 9** vs Fiscus (LF-3), **8 of 9** vs Solaria (LF-4 · L3=absent shared), and **8 of 9** vs Continua (LF-5 · L9=4-col-with-whistleblowing shared with distinct content).

Concretely:

### L1 hero geometry · stacked-editorial (NOT split-55-45)
The hero is one section in two stacked layers: a full-bleed editorial photo TOP with a credit-overlay positioned absolute inside the photo (KPI tuple at bottom-left + caption on the right edge), and a paper-coloured 8/4 grid BELOW with serif h1 + actions LEFT and side-quote RIGHT. The hero is **not** a 55/45 grid — it is a vertically-stacked composition with the photo full-bleed and the typographic content below the fold of the hero section. This is the load-bearing structural difference: Pragma, Fiscus, Solaria all ship a 55/45 grid that puts type and photo in side-by-side columns. Continua ships an object-overlay where the h1 sits ON the photo's lower-third. Cornice puts the photo above and the type below — the cinematic editorial composition every architecture monograph uses on its opening spread.

### L2 section sequence · B (NOT A, A+slot4, C, or D)
The section list on home: `cs-hero · cs-narrative · cs-sectors-ribbon · cs-leadership-single · cs-cases-magazine · cs-cta-closer-cream`. **Six sections, not eight or nine.** Pillars are replaced by the narrative band; KPI band is absent (KPI lives in hero overlay); trust marquee is absent (sectors-ribbon absorbs it); leadership is one card, not a grid. The wireframe is materially shorter than every other sibling's home page — a deliberate editorial pacing choice.

### L3 mid-strip differentiator slot · absent (shared with LF-4 by chance, different mechanism)
LF-2 has no named cadence cell. The narrative essay covers the cadence-cell role by giving the visitor a paragraph + three pull-quotes + an anchor-rail to move through the studio's method. LF-4 also ships L3=absent, but Solaria's mechanism is the manifesto + percorsi at slots 2 and 3. Cornice's mechanism is the essay at slot 2. Same value, different shape.

### L4 pillars treatment · essay-with-anchors (NOT numbered-grid, manifesto-replacement, or 2x2-with-image)
`cs-narrative` is a 2-col grid: a rust drop-cap (Cormorant 84px) on paragraph 1 with three pull-quotes interspersed (each carrying its own italic em-word: `prima · autore · regola`), and a sticky 4-link side-rail anchoring "Servizi · Progetti · Pubblicazioni · Studio." Replaces the pillars `<section>` entirely. Cornice has no `cs-pillars` block.

### L5 KPI placement · hero-overlay (NOT band-at-3, band-at-4, or band-at-5)
The KPI tuple `(novanta fascicoli · 2008 · 38 menzioni)` lives **inside** the hero photo's bottom-left credit-overlay frame. Not on a separate dark band. Not in the meta-strip. Not on the hero typographic side. Inside the photo. This is the move that makes LF-2 demote CS-TONE-03 (one dark band per home) at the family level — the home page ships zero dark bands because the editorial register doesn't tolerate a slab of inverted polarity in the middle of a magazine spread.

### L6 leadership presence · single-portrait-feature (NOT typographic-grid, photo-grid, absent, or pillar-photo)
`cs-leadership-single` is a 2-col grid: ONE large environmental portrait LEFT (the senior architect at her studio with drafting tools mid-ground · 50s · environmental-NOT-studio-backdrop) + h2 + role + 2-paragraph bio + 4-credential list RIGHT. Not a 3-card grid. Not a 4-card grid. Not omitted. Not a portrait-row. **One portrait, masthead-scale.** This is the family's load-bearing cell — the senior-mid-career architect must read as "real architect at her studio" not "stock LinkedIn headshot." A.6 review-lock fixed the founder gender mismatch (RDNE Stock 5915290 photo of a woman + bio originally named "Marco" → renamed to "Marta Roveri" with feminine Italian throughout).

### L7 cases-preview shape · magazine-grid (NOT list-row or timeline)
`cs-cases-magazine` is a 2-col CSS grid with one hero card spanning rows 1–3 on the left and three small cards stacked on the right. Each card carries: photo + eyebrow + h3 (with italic em on the curatorial noun: `geometria · lotto · argomento · minore`) + body + pill. **3+1, not list-row, not timeline.** The hero card is twice as tall as the small cards — a cinematic asymmetry that reads as a magazine contents page.

### L8 navbar geometry · split-wordmark-top (NOT sticky-top primary-bg or condensed-minimal-top)
The navbar uses the `cs-nav--lf2` modifier: cream background (NOT the cluster default primary-bg dark band), split-line masthead `CORNICE` above `studio di architettura` below, 5-link inline row (`Lo studio · Archivio · Servizi · Progetti · Contatti`), filled-rust trailing CTA pill (NOT outline-on-cream like LF-1's CTAs · NOT phone-right like LF-1/LF-3/LF-4). The cream-paper nav is the family's chrome signature — it reads as a publication masthead, not a corporate-banner.

### L9 footer structure · 4-col-with-whistleblowing (shared primitive with LF-5)
The 4th column is `cs-foot-col--whistleblowing` carrying the canale interno (D.lgs. 24/2023). LF-2 inherits this primitive from LF-5 (Continua's enrollment shipped it first); Cornice's enrollment widened the conditional in `_base.html` to fire for both LF-2 and LF-5. The column-content is sub-cluster-specific — Cornice's whistleblowing channel is the architecture studio's appropriate channel; Continua's is the stewardship firm's. Same footer shape, different content.

---

## §3 · Load-bearing differentiators

These are the cells that, if removed or copied verbatim by a future LF-2 occupant, collapse Cornice's identity. They are the *non-substitutable* elements.

### D1 · The voice anchor noun `argomento` (and its non-translation across locales)
`Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` — the curatorial-thesis sense of `argomento` (NOT topic, NOT subject, NOT theme — *argument-as-a-built-thesis*) is the load-bearing word. The em moves with the curatorial sense in every locale: argument (EN, FR · cognate · Architectural Review register · L'Architecture d'Aujourd'hui register) · argumento (ES · Arquitectura Viva register) · حُجَّة / ḥujja (AR · curatorial-thesis equivalent · MENA architectural-press register · NOT موضوع/topic, NOT حالة/case-study). The anchor lands verbatim on **exactly two surfaces** — hero h1 and CTA closer h2 — and the recurrence on a curatorial noun is what makes the architectural register unmistakable in the first 30 seconds.

### D2 · Cormorant Garamond + Source Sans 3 typography pair
Cormorant Garamond is the Garamond revival the architectural-press world uses (book-jacket scale at 84px drop-cap, 44–72px h1, 32–48px h2). Source Sans 3 is the cluster's first non-Inter, non-Plex sans body. The pair reads as "this is a book about architecture, not a corporate website about architecture services." A future LF-2 occupant cannot use this pair.

### D3 · Graphite + pietra-serena + terracotta-rust palette · with rust deployed display-side-only
Graphite (`#1c1d20`) is the chrome primary; pietra-serena (`#cdc9c0`) is the warm cool secondary; terracotta-rust (`#a14a2c`) is the WARM display-class accent. Critical rule: rust appears **only** on display-typographic surfaces (drop-cap · pull-quote em · magazine card numerals · CTA-closer button · focus ring). It NEVER appears on chrome (the navbar is pietra-serena cream, not rust). This separation is the resolution of the Continua palette adjacency risk — Continua's brass is also warm-display, but Continua's brass is chrome-only (in the navbar wordmark accent and footer crest), so the surface-class read is opposite.

### D4 · Bologna golden-hour portico hero subject
Exterior architectural · stone-warm · architectural-shadow · zero people · landscape orientation · ratio 16:9 (full-bleed hero). The subject is **not** an interior, not a person, not a desk, not a building façade in flat daylight. The golden-hour stone-architectural-shadow read at 1 second is "Italian portico architecture" — different from Continua's library reading-room interior, different from Pragma's boardroom, different from Fiscus's desk, different from Solaria's 1:1 conversation. The subject-class read at 1 second IS the differentiator.

### D5 · Cream-paper navbar with split-line masthead
`cs-nav--lf2` modifier swaps the cluster's default primary-bg dark navbar for a pietra-serena cream-paper background with a split-line masthead `CORNICE / studio di architettura`. The trailing CTA is filled-rust pill, not outline-on-cream. The phone-right is removed (the studio's contact lives in the contatti page). This is the chrome signature — a navbar that reads as a publication masthead.

### D6 · Single-portrait-feature leadership masthead
ONE environmental portrait of the founder, masthead-scale, paired with a 2-paragraph bio + 4-credential list. The portrait must read environmental (the room is half the subject) — the senior architect at her studio with drafting tools mid-ground, NOT a studio-backdrop LinkedIn headshot. The 4 credentials carry real albo IDs (OAPPC Milano · MIBAC commission marks · published monographs · concorso wins).

### D7 · 3+1 magazine grid for cases
2-col CSS grid · 1 hero card spanning rows 1–3 on the left · 3 small cards stacked on the right. Each card carries photo + eyebrow + h3 (italic em on the curatorial noun) + body + pill. The asymmetric 3+1 is the cinematic magazine-spread reference — a generic gallery (3-up · 4-up · masonry) does not produce the same editorial read.

### D8 · Hairline-bordered cream CTA closer + zero dark bands on home
`cs-cta-closer-cream` is the only sibling-level CTA closer that is NOT a dark band. The voice anchor recurrence sits on cream paper with hairline rust borders + a filled-rust button. Combined with the hero-overlay KPI placement (no dark KPI band on home), the home ships **zero dark sections**. CS-TONE-03 (one dark band per home) is demoted at the LF-2 family level — explicitly declared at the planner brief, ratified at A.6 review-lock, walked at workflow C. This is **not** a generic permission to skip dark bands; it is a family-scoped declaration tied to the editorial-publication register.

### D9 · LF-2-scoped Naskh AR h1 swap
`html[dir="rtl"] body.cs-lf-lf-2 { --heading: 'Noto Naskh Arabic', 'Cormorant Garamond', Georgia, serif; }`. Naskh reads editorial-publication (Casabella/Domus/Architectural Review register); Kufi reads display-monumental (Pictet/family-office register). LF-2's editorial register favours humanist Naskh forms over Kufi geometry. The selector-scope (`body.cs-lf-lf-2`) ensures zero leakage into LF-1/LF-3/LF-4/LF-5 — verified at workflow D and re-verified at the public flip (Continua AR LF-5 h1 still computes to `Noto Kufi Arabic`).

### D10 · "Apri un fascicolo progetto" CTA + fascicolo mental model
The CTA is not "book a call" or "schedule an appointment" — it is "open a project file." The mental model is dossier-bound, not call-bound. The conversion form asks for project scope + budget range + timeline horizon, not contact details + reason. This conversion pattern matches the studio's actual intake (architects open project dossiers, they don't book discovery calls).

---

## §4 · Anti-collapse rules for future LF-2 occupants

A second LF-2 occupant inherits the family's L1–L9 tuple verbatim and must differentiate **inside** the cells. This section enumerates the binding rules — read before filing an intake.

### AC-1 · Inherit the L1–L9 tuple verbatim
A second LF-2 occupant ships the same 9-cell tuple: `stacked-editorial · B · absent · essay-with-anchors · hero-overlay · single-portrait-feature · magazine-grid · split-wordmark-top · 4-col-with-whistleblowing`. **Do not flip cells.** A sibling that flips one of these cells (e.g., changes leadership to a 3-card grid) is no longer LF-2 — it is LF-{NEW}.

### AC-2 · Differentiate via skin axes, not layout axes
The second LF-2 occupant's distinctness vs Cornice scores against the 4 skin axes (voice · palette · imagery · typography) at ≥4/5. Layout axes are shared by family. The matrix scoring is asymmetric: high vs Cornice on skin · zero on layout (which is intended).

### AC-3 · Voice anchor must NOT be a curatorial-thesis cognate
`argomento / argument / argumento / حُجَّة` is taken. A second LF-2 occupant cannot use any direct cognate (theme / argument / topic / thesis / claim / case in the case-study sense). It must pick a different curatorial noun whose load-bearing translation lands cleanly across 5 locales — `evidenza` (evidence-led legal · `evidenza → evidence → preuve → evidencia → دليل`), `tracciato` (independent directorship · `tracciato → record → tracé → trazado → سجل`), `metodo` (taken by Solaria), `dossier` (overlap with `fascicolo`), `inchiesta` (investigation-led practice · `inchiesta → inquiry → enquête → investigación → تحقيق`).

### AC-4 · Hero photography subject must NOT be Italian portico architecture
Cornice's Bologna golden-hour portico is taken. A second LF-2 occupant cannot ship any northern-Italian-portico, any golden-hour stone-architectural-shadow exterior, or any subject that reads "Italian classical architecture" at 1 second. Open territory: northern-European brick (Hamburg / Antwerp) · Mediterranean modernist (Ibiza / Marbella) · contemporary timber (Scandinavian) · industrial-conversion interior · brutalist concrete · alpine-stone vernacular. The subject-class read at 1 second must produce a different geographical / material register.

### AC-5 · Heading serif must NOT be Cormorant Garamond
Cornice claims Cormorant Garamond. Open territory for a second LF-2 occupant: GT Sectra · Recoleta · PT Serif · Lora · Source Serif · Spectral · Crimson Pro (taken by Continua). The pair is heading + body together; the second occupant picks both fresh.

### AC-6 · Body sans must NOT be Source Sans 3
Cornice claims Source Sans 3. Open territory: Public Sans · Manrope · Work Sans · IBM Plex Sans (taken by Fiscus) · Inter (taken by Pragma + Solaria — strongly avoid). Spectral-as-sans is open.

### AC-7 · Palette must NOT be in Cornice's neighbourhood
Cornice's graphite + pietra-serena + terracotta-rust is taken. The next LF-2 occupant cannot use:
- Any warm grey + warm rust/copper/terracotta combination (Cornice's signature).
- Any palette where the warm display accent is rust-family.
- Any palette where the secondary is a warm cool stone tone (pietra-serena adjacency).

Open palette territory specifically for LF-2 (orthogonal to Cornice + the other 4 siblings):
- Bottle-green + bone + obsidian (forest editorial · evidence-led legal).
- Burgundy + cream + slate (jewel-tone editorial · longitudinal research).
- Deep teal + champagne + cream (cool editorial · independent directorship).
- Plum + cream + bronze (warm-cool editorial · inchiesta-led practice).
- Charcoal + rope + ivory (matte-on-matte editorial · methodology-led firm).
- Sage + stone + dusty-ochre (muted editorial · conservation studio · BUT careful: dusty-ochre adjacency with Solaria's ocra).

### AC-8 · CTA copy must NOT be in the fascicolo / dossier semantic family
"Apri un fascicolo progetto" is taken. The mental model "open a dossier" is Cornice's claim. A second LF-2 occupant cannot ship "Apri un dossier · Apri un fascicolo · Open a brief · Open a record · Open a folder · Open a case file" or any direct semantic equivalent. Open mental models for LF-2: "Submit an evidence brief" (evidence-led legal) · "Request an inquiry" (inchiesta-led) · "Open a methodology session" (audit-led methodology) · "Apri una scheda di mandato" (independent directorship · scheda not fascicolo).

### AC-9 · Leadership single-portrait must read environmental, NOT studio-backdrop
The portrait subject must be 50s-or-senior, the room must be half the subject (drafting tools / archive shelves / library / atelier visible behind the person), the framing must be 3/4 or environmental. **Not** a flat-light LinkedIn headshot. **Not** a studio-backdrop corporate portrait. The A.6 review-lock specifically called out "single-portrait stock-headshot collapse" as the family's load-bearing risk. A second LF-2 occupant inherits this risk and the anti-pattern guard.

### AC-10 · Magazine grid hero card must read as the issue's contents page
The 3+1 grid reads as a magazine spread when the hero card is genuinely the lead story (largest photo · most ambitious h3 · most curatorial em-word) and the three small cards are supporting items. If the hero card is "just one of four cases sized differently," the grid collapses into a generic gallery. The second LF-2 occupant's content team must rank cases editorially before building the grid — the lead story is a curatorial decision, not an alphabetical accident.

### AC-11 · Cream-paper navbar is taken at the chrome layer
Cornice's `cs-nav--lf2` cream-paper masthead is the family's chrome signature. A second LF-2 occupant inherits the cream-paper, the split-line masthead shape, the filled trailing CTA pill, and the absence of phone-right. Differentiation in the chrome happens via:
- The wordmark itself (different studio name + descriptor pair).
- The trailing CTA fill colour (matched to the new accent — but NOT rust).
- The 5-link nav labels (named after the studio's actual sections — not "Studio · Archivio · Servizi · Progetti · Contatti" verbatim).

### AC-12 · 4-col-with-whistleblowing footer column content
The 4th column (`cs-foot-col--whistleblowing`) is shape-shared between LF-2 and LF-5. The column content is sub-cluster-specific. Cornice's column surfaces the architecture studio's whistleblowing channel (canale interno · responsabile della prevenzione · email · privacy reference). A second LF-2 occupant fills the column with its own sub-cluster's appropriate channel — NOT a copy-paste of Cornice's content.

### AC-13 · AR Naskh swap is the family's, not Cornice's
The Naskh h1 swap (`body.cs-lf-lf-2`) is selector-scoped to the LF-2 family. A second LF-2 occupant inherits it without re-declaring. The Latin wordmark and Latin numerals are preserved per CS-NAV-06 / CS-FOOT-03. Do not re-bind the Naskh selector to a sub-class — the family-level scope is correct.

### AC-14 · Zero-dark-bands-on-home is the family's, not Cornice's
The CS-TONE-03 demotion is family-scoped. A second LF-2 occupant inherits zero-dark-bands-on-home as a binding constraint, not a permission. The home page ships zero dark sections; KPI lives in hero overlay; CTA closer is hairline-bordered cream. **Do not introduce a dark band to "ground the page"** — that breaks the family's editorial register.

### AC-15 · Voice anchor lives on EXACTLY 2 surfaces of home
Hero h1 + CTA closer h2. **Not** the navbar wordmark. **Not** the side-quote (the side-quote em moves with a verb-form derived from the anchor noun). **Not** an interstitial badge. Two surfaces, verbatim, em-on-the-same-noun. The recurrence is what makes the curatorial register unmistakable; widening it dilutes the recurrence.

### AC-16 · Walking budget reflects LF-2 entry cost
The first LF-2 occupant cost workflow A.5 → A.6 → C → D → flip (5 passes, ~3 days end-to-end). The second LF-2 occupant should expect lower entry cost (the family is now familiar, A.6 risks are documented, the chrome is reusable) — likely workflow A.5 → A.6 → C → flip (4 passes), with workflow D folded into C if the multilingual walk lands clean. Plan accordingly.

---

## §5 · What future LF-2 siblings must NOT copy from Cornice (explicit)

| Element | Reason it is non-substitutable |
|---|---|
| Voice anchor `argomento` and its 5-locale curatorial-thesis cognates | Anchor noun + recurrence on hero h1 + CTA closer is Cornice's identity |
| Cormorant Garamond heading serif | Heading serif locks the architectural-press register; Cornice claimed it first |
| Source Sans 3 body sans | Body sans locks the publication body register; Cornice claimed it first |
| Graphite + pietra-serena + terracotta-rust palette | Warm-display-on-cool-chrome polarity is Cornice's; rust deployment is its signature |
| Bologna golden-hour portico hero photograph + any northern-Italian-portico subject class | Hero photo is the 1-second read; this subject-class is taken |
| Single-principal Milanese architecture studio sub-cluster framing (Marta Roveri · STUDIO DI ARCHITETTURA · DAL 2008 · 90 fascicoli · 38 menzioni) | The studio's identity itself; an occupant in this exact sub-cluster collides at the matrix |
| `Lo studio · Archivio · Servizi · Progetti · Contatti` 5-link nav | Page labels chosen for Cornice's editorial method; the second occupant picks fresh labels |
| The 4 case slugs `biblioteca-pietrasanta-concorso · via-volpe-roma-residenziale · palazzo-lignari-bologna-restauro · cornice-fronte-minore-saggio` | Case study material; the second occupant ships its own |
| `argomento / argomenta / geometria / lotto / argomento / minore` em-word set across the home | Em-word audit anchors the curatorial motif; the second occupant chooses 12 fresh em-words |
| The 4 credentials (OAPPC Milano · MIBAC · monografia · concorsi) on the leadership masthead | Real credentials specific to Marta Roveri; the second occupant carries its founder's actual credentials |
| The fascicolo mental model in the contact form (project scope + budget range + timeline horizon) | Conversion pattern matched to architecture intake; the second occupant builds its own intake form |
| The 6 Pexels URLs in `business-architecture` pool | Cross-cluster URL grep enforces zero overlap; the second occupant scouts a fresh pool |
| The exact 3+1 magazine grid composition (left hero spans rows 1–3 + right column 3 cards) | Grid shape is family-shared; **content** assignments must differ — the second occupant doesn't copy Cornice's hero-card-which-case |

---

## §6 · What future LF-2 siblings INHERIT from Cornice (verbatim)

| Element | Why it is family-level, not template-level |
|---|---|
| L1–L9 tuple `stacked-editorial · B · absent · essay-with-anchors · hero-overlay · single-portrait-feature · magazine-grid · split-wordmark-top · 4-col-with-whistleblowing` | Family signature — that is what makes a sibling LF-2 |
| Cream-paper navbar shape (split-line masthead · filled trailing CTA · no phone-right · 5-link inline) | Chrome signature of LF-2 |
| 4-col-with-whistleblowing footer shape (4 columns including a `cs-foot-col--whistleblowing`) | Compliance posture shared with LF-5 |
| Zero dark bands on home (CS-TONE-03 family-scoped demotion) | Editorial register requires it |
| LF-2-scoped Naskh AR h1 swap (`body.cs-lf-lf-2`) | Editorial register requires Naskh over Kufi |
| Hairline-bordered cream CTA closer with voice anchor verbatim recurrence | Family signature CTA shape |
| Sticky 4-link side-rail in the narrative band | Essay-with-anchors mechanism |
| Three pull-quotes interspersed in the narrative essay (each with own italic em-word) | Family pacing element |
| Drop-cap on paragraph 1 of the narrative essay (84px serif, accent-tinted) | Family typographic signature |
| KPI tuple inside hero photo's bottom-left credit-overlay frame | Family signature for L5=hero-overlay |
| Single-portrait masthead requiring environmental-not-studio framing | Family load-bearing cell |
| Magazine 3+1 grid for cases (1 hero card + 3 small) | Family L7 signature |
| Voice anchor verbatim on exactly 2 home surfaces (hero h1 + CTA closer h2) | Family recurrence rule |

---

## §7 · LF-2 walk gates the second occupant must clear

The walk gates Cornice cleared at workflow D and re-cleared at public flip:

### Family layout gates (BLOCKING)
- **B-LAYOUT-1**: 1920px wireframe overlay vs each existing sibling shows ≥30% bounding-box-area difference.
- **B-LAYOUT-2**: `<section class="cs-*">` list differs by ≥2 entries from each existing sibling.
- **B-LAYOUT-3**: Live L1–L9 classification matches the LF-2 declaration · ≥4/9 dimensions different vs every existing sibling.

### LF-2-specific walk gates
- **F2-WALK-1**: Hero photo full-bleed at 1920/1440/1280/1100 · 8/4 below-fold split renders correctly at 1100+ · stacked at ≤880.
- **F2-WALK-2**: KPI tuple in hero overlay reads contrast-AA against the photo's bottom-left luminance region (or has a translucent dark plate behind it).
- **F2-WALK-3**: Drop-cap renders at 84px serif accent-tinted on paragraph 1 of narrative · 3 pull-quotes interspersed · sticky 4-link side-rail anchors to actual page sections.
- **F2-WALK-4**: Single-portrait masthead reads environmental-not-studio at 1280 + 720 · bio + 4 credentials legible at 880 · stacks above portrait at ≤720.
- **F2-WALK-5**: 3+1 magazine grid hero card spans rows 1–3 at 1100+ · stacks to 4-up at ≤720 with hero card first.
- **F2-WALK-6**: Cream-paper navbar at 1920/1440/1280/1100 · split-line masthead readable · trailing filled CTA · hamburger drawer at ≤880 with the same masthead split.
- **F2-WALK-7**: 4-col footer at 1100+ · 2-col at 880 · 1-col stack at ≤720 with whistleblowing column NEVER collapsed into a sub-link of contact.
- **F2-WALK-8**: AR locale renders Naskh h1 (`Noto Naskh Arabic` first in fontFamily computed-style) · Latin wordmark + Latin numerics preserved · zero Naskh leakage to LF-1/LF-3/LF-4/LF-5 (probe Continua AR h1 = Kufi).
- **F2-WALK-9**: Voice anchor verbatim on exactly 2 home surfaces · em-word identical on both · 12 em-word audit on home (CS-TYPE-02) passes 12/12.
- **F2-WALK-10**: Zero dark sections on home (the body-class probe + screenshot review at 1920 must show no `--primary` background bands besides the navbar and footer chrome).
- **F2-WALK-11**: 5 locales × 5 page kinds + 5 locales × N case-detail = 45+ routes 200 anonymously (where N depends on the second occupant's case count).
- **F2-WALK-12**: Frozen-sibling regression on Pragma · Cornice · Fiscus · Solaria · Continua = 5 × 200 anonymous + 0 px wireframe drift on each.

---

## §8 · Risks specific to LF-2 second occupant (planner brief checklist)

The risks Cornice surfaced and resolved · the second occupant inherits the resolution AND the risk re-fires.

### R-LF2-1 · Single-portrait stock-headshot collapse
The single portrait must read environmental, not LinkedIn-headshot. Cornice resolved this by curator-binding to environmental composition + binding triple (50s-or-senior + drafting-tools-mid-ground + environmental-NOT-studio-backdrop). The second occupant must bind the same triple at curator scout time — pre-build, not mid-build.

### R-LF2-2 · Founder gender / name / pronoun mismatch on the masthead
A.6 review-lock caught Cornice's portrait (woman) + bio (Marco · masculine Italian) mismatch. The second occupant must verify portrait + name + pronouns + role + bio + intro + team-card role + studio-founder-eyebrow at A.5 build, not at A.6.

### R-LF2-3 · Hero overlay luminance vs h1 contrast
The h1 sits below-fold on cream paper (not on the photo) for Cornice — the contrast risk is on the KPI tuple inside the hero's bottom-left overlay, NOT the h1. The KPI tuple must clear AA against the photo's bottom-left luminance region. If the photo is variable-luminance, a translucent dark plate is required behind the overlay.

### R-LF2-4 · Magazine grid collapsing into a generic gallery
The hero card must be editorially the lead story. If the four cases are all "equally good," the grid collapses. The second occupant ranks cases at copy-authoring time, not at build time.

### R-LF2-5 · CS-TONE-03 family-scoped demotion mistakenly extended to non-LF-2 siblings
The zero-dark-bands rule is LF-2-scoped. A future non-LF-2 sibling that invokes "LF-2 set the precedent" to demote CS-TONE-03 in another family is in error. The orchestrator gates this at planner-brief sign-off.

### R-LF2-6 · Naskh leakage to non-LF-2 AR siblings
The Naskh h1 swap is `body.cs-lf-lf-2`-scoped. A future build that strips the selector or moves it to `:root` leaks Naskh into Continua's LF-5 AR render. The probe at workflow D + public flip catches it · the second occupant must not relax the scope.

### R-LF2-7 · 4-col-with-whistleblowing column dropping at ≤720px
The whistleblowing column must remain reachable in one tap on mobile. Collapsing it into a sub-link of "contact" breaks CS-FOOT-02. Cornice's responsive auditor passes this at 720 + 480; the second occupant's auditor must pass it too.

### R-LF2-8 · Cream-paper navbar contrast at lower-luminance rooms
The navbar background is pietra-serena (`#cdc9c0`-class). The 5-link inline row + masthead descriptor + filled trailing CTA must clear AA on cream. Cornice's contrast-accessibility scorecard verified this; the second occupant's must too — **especially** in hover/focus states where the focus ring is gold and must read against the cream nav, not against the dark navbar of LF-1/LF-3/LF-4.

---

## §9 · The intake question for the next LF-2 candidate

Before opening an LF-2 second-occupant intake, the planner answers:

1. **Is the candidate's professional fit genuinely portfolio-of-work-led?** Evidence-led litigation · independent directorship case-bundle · audit-led methodology with published methodology pieces · longitudinal research practice with publications · inchiesta-led journalism agency · conservation studio with restoration case-bundle. **Not**: an advisory firm with case studies (LF-1) · a regulated practice with deadlines (LF-3) · a method-declared single-practitioner (LF-4) · a stewardship custodial firm (LF-5).
2. **Does the candidate have ≥4 publishable case studies with editorial weight?** The 3+1 magazine grid demands a lead story + 3 supporting items. A candidate with ≤3 cases or with cases of equal weight collapses the grid.
3. **Does the candidate's voice register tolerate a curatorial noun anchor?** The em-word recurrence is the load-bearing copy move. If the candidate's brand voice is "service-oriented" or "outcome-oriented," the curatorial register doesn't fit — re-route to LF-{NEW} or wait.
4. **Does the candidate's hero photography subject differ materially from Bologna golden-hour portico?** The 1-second subject-class read must produce a different geographical / material register.
5. **Does the candidate have a single principal whose portrait carries the masthead?** The single-portrait-feature is the family's L6 cell. A multi-partner firm collides — re-route to LF-1 or LF-{NEW}.
6. **Does the candidate's compliance posture warrant a 4-col-with-whistleblowing footer?** D.lgs. 24/2023 applies (Italian regulated practice). If the candidate is non-Italian or non-regulated, the 4th column needs a different content shape.
7. **Does the candidate's heading serif / body sans / palette / CTA-noun all clear vs Cornice on the matrix?** The intake fills the row; the planner verifies ≥4/5 vs Cornice on skin axes.

If the answer to (1) is "no" or to (2) is "no," do not open LF-2 — open LF-{NEW} or hold.

---

## §10 · One-line summary

**Cornice is genuinely LF-2 because every load-bearing cell of its home page composes for a magazine-spread read instead of an institutional-banner read** — the stacked-editorial hero with KPI in photo overlay, the rust-drop-cap narrative essay with three pull-quotes and a sticky anchor-rail, the cream-paper masthead navbar with split-line wordmark, the single environmental portrait masthead, the 3+1 magazine grid of cases, the hairline-bordered cream CTA closer, the LF-2-scoped Naskh AR h1, and the zero-dark-bands-on-home discipline. **A future LF-2 sibling inherits all of that verbatim and differentiates inside the cells via voice anchor, palette, hero photography subject, heading serif, body sans, CTA mental model, and case-bundle content** — never by flipping cells of the L1–L9 tuple, because flipping cells exits the family.
