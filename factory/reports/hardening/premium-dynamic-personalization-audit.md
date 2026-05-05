# Premium · Dynamic · Personalization · system-level audit

```yaml
report_type:        hardening-diagnosis (paper-only · zero source change)
date:               2026-05-04
agent:              orchestrator-side audit (Phase X.7 hardening · post-Causa A.5b imagery re-curate)
trigger:            user signal — "the latest templates still feel too similar and not dynamic enough"
                    (treated as load-bearing · NOT as subjective noise · per ORCHESTRATOR.md §6.10)
inputs_consumed:
  - factory/reports/hardening/corporate-suite-post-cornice-state.md
  - factory/reports/hardening/corporate-suite-{layout-divergence-plan,layout-variance-rules,layout-family-matrix,family-backfill}.md
  - factory/reports/hardening/post-cornice-{next-candidate-readiness,reference-hardening}.md
  - factory/reports/hardening/sixth-sibling-territory-scout.md
  - design-orchestrator/references/internal-baselines/corporate-suite-{live-family-map,distinctness-matrix,reference-pack,layout-family-assignment}.md
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md
  - design-orchestrator/ORCHESTRATOR.md (§6 anti-drift · §7 user goal restatement)
  - apps/catalog/template_dna.py (DNA vocabulary + 22-archetype registry)
  - apps/catalog/template_content_{pragma,cornice,fiscus,solaria,continua,causa,...}.py (per-template content modules)
  - templates/live_templates/business/corporate-suite/_layouts/{lf1,lf2,lf5}/content.html (32-line dispatcher + 3 family scaffolds)
  - templates/live_templates/{agency,medical,restaurant,portfolio,real-estate,ecommerce,lawyer}/* (the non-corporate-suite archetypes for cross-cluster comparison)
  - factory/reports/causa/causa-a6-it-review-lock.md (the most recent corporate-suite lock evidence)
  - factory/reports/imagery/causa-legale-a5b/* (most recent imagery re-curate · binding evidence on the imagery-axis monoculture)
  - MEMORY.md (program closure + recent phase checkpoints)
status_tag:         AUDIT-COMPLETE · 7 GAPS NAMED · RECOMMENDATION: HARDEN-FIRST
verdict:            The user's signal is correct. The latest 6 corporate-suite siblings are
                    structurally distinct (L1-L9 layout families) but tonally monomorphic
                    (one premium-editorial-Italian grammar). The system can produce 6 skins of
                    one grammar, not 50/100/200 truly different templates, until a documented
                    second tonal grammar lands.
next_action:        Open Phase X.7 hardening (premium-tonal-divergence + dynamic-feel + customer-
                    customization). Hold further corporate-suite enrollment AND any new cluster
                    enrollment until at least one of the three audit-named gates lands.
```

The question this audit answers — restated brutally so it cannot drift:

> Are we actually on track to produce **hundreds of customizable templates that feel
> truly different, premium, modern, dynamic, and professional** — or are we still
> over-relying on **one premium-editorial grammar**?

**Answer: we are over-relying on one premium-editorial grammar. Six concrete signals,
named in §3 below, prove it.** The L1–L9 layout-family system genuinely solved the
DOM-overlay sameness identified at the divergence plan, but it solved it inside the
*same tonal envelope* — Italian premium-editorial with serif-italic-em + cream paper
+ Pexels editorial photography + Lei register + hairline borders + "Apri un X" CTA
inflection. That envelope reads as one grammar at first scroll regardless of which
LF the page dispatched to.

The non-corporate-suite archetypes (agency-digital-studio with violet sprint-console
chrome · cinematic-photographer with fullbleed EXIF dark hero · ultra-luxury-cinematic
real-estate with champagne concierge wordmark · agency-creative-studio with serif-
index-asterisk navbar) demonstrate the **machine can produce other grammars** — the
DNA registry already enumerates 22 layout archetypes, 19 hero styles, 21 navbars,
18 footers, 18 cards, 18 buttons, 18 tones, 18 conversion patterns. The variety is
encoded. **It just hasn't been exercised in any of the most recent six builds.**

This audit is the case for stopping enrollment and exercising it.

---

## §1 · What is genuinely strong now (the platform earned this · do not regress it)

These are the things that work. The hardening pass must NOT touch them.

### S1 · The L1–L9 layout-family system at the structural layer
Five families (LF-1 Boardroom Vertical · LF-2 Editorial Spread · LF-3 Compliance
Calendar · LF-4 Manifesto-First · LF-5 Stewardship Object-Hero) live side-by-side
in `_layouts/{lf1,lf2,lf5}/content.html` (LF-3/4 share LF-1's scaffold with cell
overrides). The dispatcher at `templates/live_templates/business/corporate-suite/
home.html` reads `template.layout_family` and routes correctly. **9 of 10 sibling
pairs ≥5/9 layout-distinct** (post-Cornice state report §2). One pair (Pragma↔
Fiscus = 2/9) is a documented near-occupant § decision — accepted, not violated.

### S2 · The pipeline is a recipe, not a discovery
Continua and Cornice both walked `intake → A.5 IT-only build → A.6 review-lock →
workflow C multilingual → workflow D release-decision → user-handshake → public
flip cascade` end-to-end with **zero re-discovery**. Causa is currently mid-walk
(A.6 partial → A.5b imagery re-curate → A.6b pending). The user-handshake gate
(R-SOL-8 · D-102) held both flips. The 7-literal tier-flip cascade in
`release-gatekeeper.md §6` works verbatim per sibling.

### S3 · Selector-scoped chrome variation without leakage
LF-2's `body.cs-lf-lf-2 { --heading: 'Noto Naskh Arabic' }` Naskh AR h1 swap was
verified live to NOT leak into LF-1/3/4/5. The Continua public flip post-walk
re-confirmed Continua's AR h1 still computed to `Noto Kufi Arabic` after
Cornice's LF-2 selector landed. The mechanism is sound.

### S4 · Voice-anchor verbatim across 5 locales
Five anchors cleared the contract: Pragma (decisional gravity) · Fiscus (presidio
scadenze) · Solaria (`terapia` / `consulenza` 2-em contrast pair · CS-EXEC-01
exception) · Continua (`generazioni → generations / générations / generaciones /
الأجيال`) · Cornice (`argomento → argument / argumento / حُجَّة`) · Causa
(`evidenza → evidence / preuve / evidencia / دليل`). The em-noun travels with
the SENSE not the cognate. Translator briefs work.

### S5 · 0 px frozen-sibling regression discipline
Continua's LF-3→LF-5 migration + Cornice's LF-2 introduction + Causa's draft +
Causa's A.5b imagery restore all shipped with **0/N wireframe drift on the rest
of the cluster** at every flip and at every interim review-lock. The layout-
router has held under five real layout additions.

### S6 · Editor program A.6 → A.17b closed
19 archetypes enrolled · 9/9 families closed · D-099 sentinel retirement
binding · 375/375 + 834/834 tests. The corporate-suite cluster is layered on
top of a closed editor pipeline. The editor side is done.

### S7 · Domain isolation
Five (now six) corporate-suite rollouts, never one of them touched
`apps/editor`, `apps/projects`, `apps/commerce`. The archetype boundary is
real, enforced, and respected. Causa's A.5b imagery re-curate was a 1-file
change (`apps/catalog/template_content_causa.py` 10 URL constants). Scope
discipline is the house style.

### S8 · DNA vocabulary registry (`apps/catalog/template_dna.py`)
22 layout archetypes · 19 hero styles · 21 navbars · 18 footers · 18 cards ·
18 buttons · 4 density profiles · **18 tones** · 18 conversion patterns · ≥10
imagery directions · per-archetype `font_pairing` overrides. **The variety is
encoded at the DNA layer.** This is the single most important fact in this
audit: the machine is not vocabulary-poor. It is *exercise-poor* on the
vocabulary it owns.

### S9 · Cross-cluster archetype diversity already on disk
- `agency/agency-creative-studio` — editorial-studio · `serif-index-asterisk` nav · `colophon-press` footer · `editorial-index-dossier` cards · `ghost-serif-dossier` button · `editorial-quote-cover` hero · 395 lines of sui-generis home.html.
- `agency/agency-digital-studio` — digital-product-studio · `pill-sprint-chip` violet nav · `shiplog-console` footer · `sprint-console` cards · `glow-sprint-arrow` button · `product-console-hero` · 425 lines.
- `restaurant/fine-dining` — `editorial-plate` hero · `concierge-press` footer · `course-index` cards · `ghost-gold-serif` button · 831 lines.
- `portfolio/cinematic-photographer` — `fullbleed-exif` hero · `exif-credits` footer · `filmstrip-series` cards · `ghost-mono-bracket` button · 398 lines.
- `real-estate/ultra-luxury-cinematic` — `fullbleed-editorial-cover` hero · `concierge-coords` footer · `property-dossier` cards · `ghost-champagne` button.
- `business/startup-saas-landing` — `centered-manifesto-product` hero · `pill-floating-glow` nav · `shiplog-countdown` footer · `feature-glow` cards · `glow-pill` button.

These templates **do not feel like the corporate-suite cluster**. They prove the
machine can ship a cosmic-violet sprint-console SaaS landing AND a champagne
concierge real-estate dossier AND a film-EXIF photography portfolio AND a serif-
italic-pull-quote agency hero. Six distinct grammars on disk. **The recent six
all-corporate-suite enrollments did not exercise any of them.**

---

## §2 · What still feels too samey across recent templates (concrete · not generic)

The user's "too similar" is not subjective. It is a **catalogued tonal monoculture**
across the latest 6 builds (Pragma · Cornice · Fiscus · Solaria · Continua ·
Causa). The mechanism is six-fold:

### Sameness #1 · One typographic envelope across all six
Every single one of the six ships:
- Serif heading + sans body (CS-TYPE-01).
- Italic `<em>` on a load-bearing word in h1 (CS-TYPE-02).
- One dark band per home — OR a family-scoped demotion that compensates with
  a cream CTA closer (LF-2 only).
- Cream-paper section baseline.
- Hairline borders on `cs-cta-closer-cream` and on hover affordances.
- Tabular numerals on every figure.
- 100×72 padding · max-width 1400px (CS-RHYTHM-01).

That is not a constraint per template — that is the **cluster contract**
(`corporate-suite-reference-pack.md §2`). It is, by design, the Italian-premium-
editorial register. **And every one of the six reads as that register at
first scroll.** A user opening Pragma and Cornice and Causa side-by-side does
not see "three different studios"; they see "three palette-and-photography
variants of one premium-editorial template."

The L1–L9 system fixed the DOM-overlay sameness. It did NOT fix the tonal-envelope
sameness. The tonal envelope is the cluster contract by construction.

### Sameness #2 · One CTA inflection ("Apri un X" / "Fissa un X" / "Avvia un X")
Six CTAs, one inflection family:
- "Fissa una call privata" (Pragma)
- "Apri un fascicolo progetto" (Cornice)
- "Primo appuntamento" (Fiscus)
- "Prenota una discovery call" (Solaria)
- "Avvia un dialogo di mandato" (Continua)
- "Apri un parere preliminare" (Causa)

Every one is *italian polite imperative + abstract noun*. None is "Buy", "Sign up",
"Book online", "Get a quote" (which would read SaaS — banned by CS-CTA-02). None
is "Visit the office", "Send a sample", "Tour our studio" (which would feel
concrete and physical). The inflection itself is part of the sameness — six
distinct ABSTRACTIONS of the same underlying gesture (open a private channel
with a partner before transacting).

This is by design (boardroom-button convention · CS-CTA-01 § decision
2026-04-26 · "filled-on-cream reads SaaS, ratified do not re-litigate"). **It
is also the reason the cluster will not produce a dynamic SaaS template, an
e-commerce template, or a delivery-shaped service template under its current
contract.**

### Sameness #3 · One imagery register (Pexels editorial · zero people OR environmental portrait)
Five live + one draft sibling, six imagery directions, one register:
- Pragma: boardroom long-table 1-4 people (warm institutional)
- Cornice: Bologna golden-hour portico zero people (warm exterior)
- Fiscus: tidy desk + tax documents 0-1 people (warm-neutral institutional)
- Solaria: 1:1 conversation 2 people (cool minimal)
- Continua: library reading-room interior zero people (warm interior)
- Causa: empty courtroom interior + senior man with codex zero/environmental (cool/honey)

All Pexels (Pragma's Unsplash is grandfathered W001). All compositional-restraint
photography. All cool-or-warm muted-light register. All zero-energetic-action.
Five of six are interior architectural; the sixth (Cornice) is exterior
architectural. **Not one is an outdoor street, a product-in-context, a tool-in-
hand, a map, an icon-system, a diagram, an illustration, a 3D render, or a UI
screenshot.**

The Causa A.5b re-curate report (`§4 hardest slot`) made the case explicit:
"Pexels' courtroom pool is heavily skewed toward gavel close-ups, Lady Justice
statues, lawyer-portrait stock; cool-lit empty European chamber interiors are a
thin sub-pool." The sub-pool is thin **because the cluster has chosen one register
and is now reaching the tail of that register's available pool.** The seventh
sibling will hit the same tail.

### Sameness #4 · One section-rhythm vocabulary (cs-hero · cs-pillars · cs-kpi · cs-cta)
Even with five layout families, the home page's "atomic vocabulary" reads from
a fixed set:
- `cs-hero` (always first · always editorial-grade · always 100×72)
- `cs-pillars` OR essay-replacement (always 3-4 cards OR a substituted single block)
- `cs-kpi-band` OR overlay (3-4 stats with tabular numerals)
- `cs-sectors-ribbon` (always present except in LF-2 where narrative essay absorbs)
- `cs-leadership` (typographic-grid · single-portrait · pillar-photo · or absent)
- `cs-cases-preview` (list-row · magazine-grid · timeline)
- `cs-cta-closer-cream` OR dark CTA band (always last)

Six concrete shapes. The motion vocabulary across them: low motion, staggered
reveals on scroll, marquee 110s OR static, text fade-in only, NO parallax, NO
scroll-snap, NO video, NO lottie. **Identical motion contract across all six.**

That is correct per `corporate-suite-distinctness-matrix.md §1.11` ("motion is a
cluster invariant — restraint is the brand"). It is also load-bearing for the
samey-feel signal: a site that does not move does not feel dynamic regardless
of what its copy says.

### Sameness #5 · One audience-verb register (interview · read · schedule · declare · entrust · plead)
The audience-verb is the single-word answer to "what is the visitor doing on this
page?" Six verbs, one mode: each is a **deliberative verb** about a private
professional engagement. Not one is energetic ("explore", "ship", "launch",
"buy", "watch", "play"), tactile ("touch", "taste", "fit"), or social ("share",
"join", "invite"). The cluster is positioned at the gravitas-end of professional
service, and within that band it is exercising six points; outside that band, it
has no shipped vocabulary at all.

### Sameness #6 · One "premium = restraint + serif italic em + cream paper + editorial photography" definition
`corporate-suite-reference-pack.md §8` operationalises premium as
- Generous restraint (100×72 padding, accent budget ≤3 hits per viewport).
- Elegant = serif italic-em + boardroom buttons + one dark band.
- Modern = CSS custom properties + RTL via logical properties + focus-visible.
- Professional = real albo IDs + boardroom KPIs + zero hyperbole.

That is **one definition of premium**. The four bullets are the same four bullets
across every cluster scorecard. They are correct for the editorial-Italian
register — and they are not the only definition of premium.

A digital-product premium grammar reads "premium = motion fidelity + tactile
response + measured velocity + accent-as-data". A jewel-box e-commerce premium
reads "premium = product-craft photography + slow product-orbit motion + cream-
on-cream tonal layering + grounded copy". A high-fashion editorial premium reads
"premium = full-bleed look-book + serial composition + minimum chrome + AAAA
contrast type". A bespoke service premium reads "premium = warm voice + maker-in-
frame photography + handwritten flourish + named colophon".

**The cluster has one definition. The market has many.** The samey-feel signal
is partly *that*: the user is sensing that "premium" has been collapsed to
"editorial-italian-restraint", and is right.

---

## §3 · Family inheritance vs clone-drift (which similarities are acceptable)

Not all sameness is bad. Some of it is the cluster's identity. The audit's
job is to draw the line cleanly.

### Acceptable family inheritance (do NOT remove · this is the cluster contract)

1. **Cluster invariants** (`corporate-suite-reference-pack.md §2`): serif heading
   + italic-em + cream paper + 100×72 padding + max-width 1400px + tabular
   numerals + locale pill + Pexels-only + voice-anchor verbatim across 5 locales
   + `:focus-visible` gold ring + density ceilings (CS-DENSITY-*).
   **Why acceptable**: these are what makes a cluster a cluster. Removing any
   of them breaks the corporate-suite identity. They are correctly enforced.

2. **L1–L9 family-shared cells per CS-LAYOUT-22**: when a sibling joins LF-2
   second-occupant, it inherits the L1–L9 tuple verbatim and differentiates
   inside the cells. Cornice ↔ Causa share L9 = `4-col-with-whistleblowing` by
   intent (D.lgs. 24/2023 forensic-firm cohort) with different column content.
   **Why acceptable**: family-shared structure with differentiated content is
   exactly what L1–L9 was designed for.

3. **Whistleblowing column shared between LF-2 and LF-5**: D.lgs. 24/2023
   compliance posture is the same; column content differs (architecture firm vs
   stewardship vs litigation channel).
   **Why acceptable**: legal compliance grammar should look uniform; the SHAPE
   is the rule, the CONTENT is the differentiator.

4. **The voice-anchor "italic em on a load-bearing word in h1, recurring on the
   CTA closer" pattern**: shared across all five LF-2 + LF-5 + LF-1 + LF-3
   + LF-4 occupants.
   **Why acceptable**: it is the cluster's typographic signature. Removing it
   would break the cluster's identity. Different cluster, different signature.

5. **The "no hyperbole · no lorem ipsum · real albo IDs · Lei register" content
   contract**: every sibling ships under it.
   **Why acceptable**: it is the SHIP-quality bar. The bar is correct.

### Unacceptable clone-drift (this is the samey-feel signal · address)

1. **One typographic envelope across all 6 corporate-suite siblings**.
   Five different serifs, five different sans, but **one combined effect** —
   all read editorial-Italian-publication-restrained. There is no "plot-twist"
   sibling whose typography reads, e.g., kinetic / display-condensed / hand-
   drawn / monospaced / mono+serif duo / variable-axis playful. Every one
   chose a *humanist or transitional* serif and a *neutral* sans.
   **Why this is clone-drift**: differentiation is happening inside one tonal
   envelope that the cluster never escapes. A user opening Causa and Pragma
   and Solaria does not see "three professional grammars"; they see "three
   tonal variants of one professional grammar".

2. **One CTA inflection across all 6** (italian polite imperative + abstract
   noun). Six abstractions of the same gesture. No concrete-action CTA, no
   energetic CTA, no transactional CTA, no waitlist CTA, no "ask anything"
   conversational CTA.
   **Why this is clone-drift**: the CTA is the action moment. Sharing one
   inflection across six sibling templates is the strongest single signal of
   tonal monoculture a user could feel.

3. **One imagery register**: editorial-Pexels-restrained. Five interior + one
   exterior architectural. Not one product-in-context, not one tool-in-hand,
   not one icon-illustration, not one map / diagram / 3D render / UI mock.
   **Why this is clone-drift**: imagery is what a first-time visitor reads
   in the first 200ms. Six visually-restrained editorial photographs is
   six instances of the same visual idea.

4. **One motion contract**: low motion · staggered reveals · marquee 110s OR
   none · text fade-in only · NO parallax · NO scroll-snap · NO video · NO
   lottie. Identical across all six.
   **Why this is clone-drift**: motion is *the* "feels dynamic" axis. A
   uniform motion contract collapses any opportunity for dynamic feel. The
   cluster has explicitly chosen to forbid it ("restraint is the brand"); that
   is acceptable for THIS cluster — and unacceptable as a definition of
   "premium" globally.

5. **One section-vocabulary**: the `cs-hero · cs-pillars · cs-kpi · cs-leadership
   · cs-cases-preview · cs-cta` atom set. Six recombinations of the same atoms.
   Not one section type that is sui generis to a sibling. (Compare: agency-
   digital-studio's `sprint-console · shiplog · capability-grid` set is sui
   generis. Cinematic-photographer's `filmstrip-series · exif-credits` set is
   sui generis.)
   **Why this is clone-drift**: the cluster defined an atom set and stayed
   inside it. The atom set is editorial-generic — fine for one or two
   instances; constraining at six.

The line between #1 (acceptable) and #2 (unacceptable) is whether the sameness
is a **named contract** that can be replaced when a different cluster ships,
or whether it is an **un-named default** that is propagating because no one
challenged it. Items #1-#5 of "Unacceptable" above are un-named — they live
as cluster habits, not as cluster decisions. They should be either named as
contract (and therefore explicitly bounded to corporate-suite) or replaced
in part by the next cluster's contract.

---

## §4 · Where the system under-delivers on "dynamic"

"Dynamic" is the user's word. It maps to several distinct mechanisms in
real interfaces — none of which the cluster currently exercises.

### Dynamic axis 1 · motion · NOT exercised
The corporate-suite motion vocabulary is fade-in + staggered reveals + marquee.
That is *quiet motion*. It is not *dynamic motion*. Dynamic motion vocabulary
the system does NOT have:
- Scroll-driven layout transforms (sticky-revealed sections, parallax-on-fold,
  scroll-snap on hero galleries).
- View-transitions API for page-to-page (would feel app-like).
- Hover-hint animations on cards (subtle tilt, lift, accent-glow).
- Live data tickers (already encoded in `agency-digital-studio`'s
  `shiplog-console` footer — but never invoked outside it).
- Interactive numerals (KPI counters animating on first-view).
- Cursor-aware accents (subtle vignette / spotlight effects).
- Programmatic typography (variable-axis morphing on emphasis words).
- Audio-reactive elements (for music/podcast/event clusters · OUT OF SCOPE
  for B2B but the system has zero infrastructure).

The `prefers-reduced-motion` honor is correct and important — but the cluster
is already at the "reduced motion" baseline by default. There is no "full
motion" vocabulary to reduce from.

### Dynamic axis 2 · interaction · NOT exercised at the home-page level
A home page can be dynamic in ways that don't require motion:
- Filterable case-study grid (click a sector chip → grid reflows).
- Live availability calendar embedded in hero (booking-shaped sites).
- Real-time stock count / price (e-commerce).
- Map-driven listings (real-estate · already encoded in `mass-market` archetype's
  `cover-search` hero · never invoked beyond that template).
- Configurator (you choose options → preview updates).
- Wizard / multi-step intake (instead of one big form).

The corporate-suite home is a **scrolling document**. It does not interact;
it informs. That is correct for boardroom-advisory and curatorial-architecture;
it is incorrect for any sibling whose audience needs to *do* something on the
home page (book a class, view a listing, configure a product, request a quote).

### Dynamic axis 3 · personalization · NOT exercised
Distinct from "user customization" (§5 below) which is editor-side. *Personalization*
is run-time tailoring of what the visitor sees:
- Locale-aware copy (already done via the 5-locale system — the only personalization
  axis active).
- Geo-aware hero photography (Milan visitor sees Milan hero · NOT exercised).
- Time-aware content (during business hours show "call now" · outside hours show
  "leave a message" · NOT exercised).
- Returning-visitor copy ("welcome back" vs "first time" · NOT exercised).
- Segment-aware sectors-ribbon (the ribbon's first 3 cells reorder based on the
  visitor's referrer · NOT exercised).
- Booking-flow integration with availability (the calendar reflects real
  appointment slots · NOT exercised).

The cluster's compliance posture (privacy + cookie law) is restrictive enough
that a few of these (geo-aware, returning-visitor) require explicit consent
gates. That is fine. But there is also no system for the orchestrator to
*offer* the consent gate, so the personalization axis is closed by default,
not by decision.

### Dynamic axis 4 · feedback · NOT exercised
The home page has no feedback mechanism: no "was this helpful" toggle, no
"questions?" inline prompt, no "schedule a 5-min call" floating button (the
SaaS playbook · banned in corporate-suite by `CS-CTA-02`), no chat widget. The
nearest thing is the locale-pill switcher.

This is correct for the gravitas register: a board-mandate prospect does not
want a chat widget intercepting their reading. It is *also* the absence of an
entire dynamic-feel category. A sibling whose audience would tolerate it
(coaching · wellness · agency · e-commerce) cannot have it because the cluster
contract forbids it.

### What "dynamic" would concretely require to ship at premium quality
- A **second motion vocabulary** with a tier-name and a `motion_profile` DNA
  field (e.g., `quiet-editorial` · `sprint-console` · `gallery-cinematic` ·
  `studio-craft` · `concierge-restrained`). Each profile binds an enumerated
  set of motion tokens. Today every sibling ships under an unnamed default.
- A **second interaction vocabulary** parallel to motion: `static-document` ·
  `filterable-grid` · `live-availability` · `wizard-intake` · `configurator` ·
  `map-driven`. Each binds a per-section interaction contract.
- An optional **personalization layer** behind a consent gate, off by default,
  with a documented set of permitted axes. Today nothing exists.
- An optional **feedback layer** behind the same gate. Today nothing exists.

None of these is in scope for the next pass. **All four are the work that turns
"premium static brochures with five locales" into "premium dynamic interfaces
with five locales".** The user's "not dynamic enough" maps to the absence of
all four axes simultaneously.

---

## §5 · Where the system under-delivers on "user-customizable"

"User-customizable" means the marketplace customer can take a template and
make it theirs through the editor — content, palette, imagery, structure —
without breaking it. Critically, this is editor-side work, which the audit
brief explicitly forbids touching. So the following is observation only.

### Customization axis 1 · copy · STRONG (editor closed at A.17b)
The editor program closed at 19 archetypes (`MEMORY.md`). 375/375 + 834/834
tests. Vertex demonstrated 284 fields. The `__meta__/uid/order` row contract
is sound. Copy customization is a solved problem at the editor layer.

### Customization axis 2 · palette · WEAK (no per-customer palette swap shipped)
Today a template ships with a frozen 3-token palette (`primary` · `secondary` ·
`accent`). The customer cannot ship "Cornice with our company palette" without
either (a) editing the source (loses upgrade path) or (b) the orchestrator
authoring a new template variant (the wrong scaling pattern · explodes
catalog count).

What the system is missing:
- An editor-side palette picker that swaps the three tokens with the user's
  brand colours, *with constraint enforcement* (CS-PAL-01 L\* ≤ 40 on cream ·
  CS-PAL-05 ≤3 accent hits per viewport · auto-derive `primary-tinted` /
  `accent-faded` for hover states).
- A live preview of the swap before commit.
- A versioned "brand palette" stored on `accounts.User` or
  `projects.CustomerProject`.

This is a known editor gap. It is OUT OF SCOPE for this audit but it is the
single largest "user-customizable" deficit.

### Customization axis 3 · imagery · WEAK (asset upload exists · no smart fit)
The `ProjectAsset` system from A.4 (`phase_a4_customer_image_upload.md`) lets
the customer upload images and bind them to template image slots. The system
correctly stores them under `/media/`. What it does NOT do:
- Smart cropping for hero geometries (the customer uploads a portrait into a
  16:9 hero slot · the system does not propose a crop · the result looks
  amateur).
- Slot-aware quality validation (warn if upload is <1600 wide on a hero slot ·
  warn if EXIF orientation is wrong · warn if subject is centered when the
  template needs an off-center subject for the credit overlay).
- Pexels-direct integration (let the customer search Pexels inline · respects
  the cluster's CS-IMG-SRC-01 contract automatically).

### Customization axis 4 · structure · WEAK (no per-customer section reorder)
The customer cannot reorder sections, hide a section they don't need (e.g., a
single-coach can omit the leadership block · only LF-4 supports it natively),
add a section they do need (a calendar where the template has none), or
choose between multiple variants of a section (e.g., 3-card vs 4-card pillars).

The L1–L9 system *is* the section-structure language, but the customer cannot
choose an LF without the orchestrator re-spec'ing the template. Section
choice is a planner privilege today.

### Customization axis 5 · typography · ABSENT
The customer cannot swap heading serif or body sans. Today the font_pairing is
hard-coded per template (`apps/catalog/template_dna.py · TEMPLATE_DNA[<slug>]
.font_pairing = ('Cormorant Garamond', 'Source Sans 3')`). There is no editor
affordance for font swap, no constraint-aware picker, no licensing model for
non-Google fonts.

### Customization axis 6 · motion · ABSENT (because the system has one motion vocabulary)
The customer cannot dial up motion. They cannot dial it down (it is already
minimal). They cannot opt into a different motion register. Per §4 above, the
motion vocabulary is uniform.

### What "user-customizable" would concretely require
1. **Palette swap with constraint enforcement** — the highest-value gap.
2. **Smart imagery upload + crop + Pexels inline picker** — second highest.
3. **Section pick-list per archetype** — let a customer choose between 2-3
   pre-validated section variants for slots that allow it (e.g., LF-1's L4
   pillars treatment can be `numbered-grid` OR `vertical-stagger` if the
   variant is pre-built).
4. **Typography pair-set picker** — N pre-validated heading+body pairs per
   archetype (e.g., Cornice ships with 3 serif options + 3 sans options
   curated against the L\* contrast rule).
5. **Motion profile picker** (only after a 2nd motion vocabulary lands per §4).

Items 1-4 are achievable at the editor layer with NO change to the design
system. Item 5 depends on §4 work. **None is in scope for this audit · all
should be in scope for the next 2 hardening passes.**

---

## §6 · Process weight vs visible product outcome

ORCHESTRATOR.md §6.1 is explicit:

> "It must never become more prose than templates. If the document count in
> design-orchestrator/ grows in a pass while the catalog template count or
> quality does not, the pass was a process pass, not a product pass."

Honest count, post-Causa:

| Counter | Pre-corporate-suite-cluster work | Now |
|---|---|---|
| `factory/reports/hardening/*.md` | 5 | 16 |
| `design-orchestrator/references/internal-baselines/*.md` | 4 | 8 |
| `factory/reports/causa/*.md` (single sibling) | 0 | 7 |
| `factory/reports/cornice/*.md` (single sibling) | 0 | 5 |
| `factory/reports/continua/*.md` + scorecard subdirs | 0 | many |
| `factory/reports/imagery/<sibling>/*.md` × 2 per sibling | 0 | 6 (Cornice · Causa · Causa-A.5b) |
| Catalog templates `published_live` | ~19 (editor program) + 0 | 24 (5 corporate-suite live + Causa draft) |
| Corporate-suite siblings published_live | 0 | 5 |

**Corporate-suite cluster delivered: +5 published siblings + Causa draft.**
**Corporate-suite cluster cost: ~30+ new docs spread across hardening reports,
internal baselines, per-sibling pipeline reports (×3 stages × 5 siblings),
imagery packs, scorecards, browser-verification reports.**

Per-sibling cost (averaged): ~6-8 dedicated reports · several hundred lines
each · plus updates to the orchestrator's reference layer (which was pointed
out as 3 days stale at post-Cornice and finally refreshed at post-Cornice-
reference-hardening).

**Is this too documentation-heavy? Yes.** Concretely:

1. The 4-stage pipeline (intake → A.5 → A.6 → C → D → flip) emits a multi-
   page report at every stage. A typical sibling carries ≥6 reports. A typical
   report is ≥400 lines.
2. The hardening reports themselves are repeat-defenders of decisions made
   in earlier hardening reports. (Compare: `corporate-suite-layout-divergence-
   plan.md` · `corporate-suite-layout-variance-rules.md` · `corporate-suite-
   layout-family-matrix.md` · `corporate-suite-layout-family-backfill.md` —
   four distinct files for the same conceptual content, in service of one
   structural insight.)
3. The orchestrator's reference layer (`design-orchestrator/references/
   internal-baselines/`) duplicates content from the hardening reports for
   "reads at intake". The duplication is intentional but it doubles the
   maintenance surface; the post-Cornice reference hardening pass demonstrated
   that 3 of those 4 files were 3 days stale relative to the live cluster.
4. The Causa F1 finding required a 4-report cascade: A.6 review-lock found
   the issue · A.5b imagery re-curate fixed it · pool-selection.md selected
   the fix · reviewer-lgtm.md validated it. **Every one of those reports is
   load-bearing**, so the bloat is not gratuitous — but it is also a clear
   demonstration that the system's response to a single curator hallucination
   is several thousand lines of paper.

The diagnosis is NOT "the docs are wasteful". The diagnosis is:

> **The docs are correct AND they consume a process budget that is now
> visibly larger than the product budget.**

Two consecutive process passes (post-Cornice reference hardening · this audit)
without a new product-side capability landing is the warning sign
ORCHESTRATOR.md §6.1 names verbatim. **The next pass MUST land a product-
side capability** OR the process load becomes the bottleneck on its own.

The pass after this one CANNOT be another doc pass. Either:
- (a) build a 2nd-grammar template (e.g., a non-corporate-suite cluster archetype
  not yet shipped — there are several in DNA and zero in catalog after the
  editor program), OR
- (b) build a 2nd-motion-vocabulary or palette-swap or smart-imagery-upload
  (per §4 / §5) — a real product capability, not a refresh of an existing one.

This audit IS one more doc pass. It is justified ONLY because it names the
gates the next product pass should aim at. **If the pass after this one is
also a doc pass, the orchestrator is in violation of §6.1.**

---

## §7 · What would block scaling to 50 / 100 / 200 truly different templates

Honest projection. Six corporate-suite siblings took ~8 weeks of orchestrator
time across `2026-04-12` (Solaria's pass1) → `2026-05-04` (Causa A.5b). Six
templates / 8 weeks ≈ 0.75 templates per week per cluster. Linear extrapolation
to 50 templates: **66 weeks · 1.3 years · single-cluster dependency**. That
is not a factory. That is a craftsman's bench.

The constraints on real scaling, in priority order:

### Block 1 · One tonal grammar per cluster
The corporate-suite cluster owns ONE grammar (Italian-premium-editorial). Within
it, the L1–L9 system mints up to ~12-15 truly distinct siblings before tonal
fatigue (the `argomento`-`generazioni`-`evidenza` pattern is already showing
strain at six — the next anchor noun will compete with three adjacent claims).
**Beyond ~12-15 siblings, the cluster needs a second tonal grammar OR a second
cluster.**

### Block 2 · No 2nd cluster has a closed standards stack
`apps/catalog/template_dna.py` registers 22 archetypes across 8 categories.
**Only one category (corporate-suite, 5 + 1 draft) has shipped under the closed
hardening pipeline** (planner-brief · A.5/6 · workflow C/D · public flip ·
DISTINCTNESS_RULES · CS-LAYOUT-* · cluster reference pack). The other 16
archetypes either shipped under the older editor program (which is stylistically
strong but has a different rigor floor) OR exist only as DNA stubs.

To scale, every cluster needs its own closed standards stack at corporate-
suite parity:
- `factory/standards/<cluster>-design-standard.md`
- `factory/standards/<cluster>-blocking-rules.md`
- `factory/standards/<cluster>-quality-scorecard.md`
- `factory/standards/<cluster>-imagery-standard.md`
- `factory/standards/<cluster>-multi-agent-sop.md`
- `factory/standards/<cluster>-browser-rubric.md`
- `design-orchestrator/references/internal-baselines/<cluster>-{distinctness-
  matrix,reference-pack,layout-family-assignment,live-family-map}.md`

That is ~13 docs per cluster × N clusters. **The standards-authoring cost is
itself a doc-pass cost that does not produce a template directly.**

### Block 3 · Imagery pool exhaustion is real
Causa A.5b §4 is the canary: "Pexels' courtroom pool is genuinely thin · 1
strong primary at premium quality". Each new sibling expands the cross-cluster
URL union (5 live pools · ~30 URLs · grew to 6 with Causa). At 50 siblings the
union covers ~250+ URLs. At 100 siblings, ~500+. **Pexels does not have 500+
genuinely premium-editorial-grade Italian-Cassazionista-binding-triple-cleared
URLs.**

The existing imagery pool model (cluster-keyed CS-IMG-POOL-03 + cross-cluster
grep CS-IMG-SRC-04) does not scale beyond ~20 distinct pools without one of:
- A second imagery source (generated · custom · stock-licensed) — currently
  banned.
- An imagery synthesis layer (composite imagery from base assets + templating).
- A wider Pexels exhaust budget per pool (≥50 backups per pool · multiplies
  curator time).
- A second imagery cluster grammar (e.g., illustration-led · diagram-led ·
  product-led · UI-led · iconography-led) where Pexels is supplemented or
  replaced.

### Block 4 · The pipeline is per-sibling, not per-batch
Every sibling walks `intake → A.5 → A.6 → C → D → flip` as an individual run.
Multilingual is sequential (IT first, then EN/FR/ES/AR added at workflow C).
There is no batch-mode, no parallel-locale build, no
brand-system-instantiation-from-DNA. The pipeline parallelism is N×1, not 1×N.

For 50 templates this is 50 individual sequential walks. Even with the
recipe-as-recipe-not-discovery improvement, a sibling is ~5-8 working days
(Cornice · Causa). **50 × 6 days ≈ 300 working days = 60 weeks single-track.**

### Block 5 · The user-handshake gate is unbatched
Every flip from `tier=draft` to `published_live` requires a user handshake.
This is correct (`R-SOL-8` · `D-102`) for a high-quality bar. **It is also a
serial bottleneck.** At 50 templates, that is 50 user-handshakes — not
intractable, but not parallelizable below the user's review-throughput limit.

### Block 6 · Doc-rate exceeds template-rate (per §6 above)
Each sibling produces ≥6 dedicated reports. Each cluster produces ≥4 internal-
baseline reference docs. Each hardening pass produces ≥2 reports. At 50
templates: ≥300 reports. The orchestrator's working set will be unreadable.

### Block 7 · No explicit retirement protocol
Per `corporate-suite-post-cornice-state.md §5.R8`: "the cluster has no
documented retirement protocol". At 50 live templates, the probability of needing
to retire one (legal · brand-conflict · imagery-license-revocation · user
request) approaches certain. The system has no shape for it.

The seven blocks compound. **Without addressing at least three of them, scaling
beyond ~12 templates per cluster (or beyond ~3-4 closed clusters) hits the
combined ceiling.**

---

## §8 · Exact recommended next hardening phase (Phase X.7)

Three gates · explicitly named · ordered by priority. **None is "build the 7th
corporate-suite sibling".**

### Gate X.7a · Ship a 2nd-cluster archetype at corporate-suite parity
**Pick one**: agency-creative-studio (Vertex's editorial-quote-cover hero, with
serif-italic pull-quote register, colophon-press footer · already in DNA + on
disk · never shipped under the hardening pipeline) OR cinematic-photographer
(`fullbleed-exif` hero + filmstrip-series cards · same situation) OR ultra-
luxury-cinematic real-estate (`fullbleed-editorial-cover` + concierge-coords
footer).

**What this gate produces**:
- The first cluster outside corporate-suite to walk the full 5-stage pipeline.
- Forces the standards stack at parity (`<cluster>-design-standard.md` etc.).
- Forces a 2nd imagery register (e.g., cinematic-photographer's EXIF dark
  fullbleed is incompatible with the cream-paper editorial register).
- Forces a 2nd CTA inflection (`Richiesta privata` · `[ AVVIA SESSIONE ]` ·
  `Visualizza dossier`).
- Forces a 2nd tonal grammar (cinematic-authorial · editorial-agency · digital-
  sprint · concierge-luxury).
- Forces a 2nd typographic envelope (e.g., display-condensed + monospaced ·
  variable-axis · sans-mono duo).

**What this gate explicitly does NOT do**:
- Add a 7th corporate-suite sibling.
- Refactor the editor.
- Change tier or registry.
- Public-flip on day 1 (D-102 cadence preserves the IT-only floor).

**Cost estimate**: ~8 sessions, comparable to Cornice's pass. The risk is
medium-high because no one cluster has walked the pipeline before, but the
recipe is documented; the standards stack copying-from-corporate-suite is the
single largest unknown.

### Gate X.7b · Add a 2nd motion vocabulary
Define `motion_profile` as a DNA dimension (`apps/catalog/template_dna.py`).
Enumerate at least 3 profiles:
- `quiet-editorial` (current · corporate-suite default · no change).
- `sprint-console` (energetic · digital-product · ship-log animation · live
  metric chip · scroll-progress).
- `gallery-cinematic` (slow · photography · fade transitions · scroll-snap
  on hero strip).

For each profile, declare:
- Hero animation contract (text fade · scroll parallax · snap-fold).
- Card hover contract (none · lift · tilt · accent-glow).
- Marquee/ticker contract (none · 110s · 60s · live-data).
- KPI animation contract (static · count-up · live-update).
- Reduced-motion fallback per profile (always honoured).

Gate X.7b can ship under Gate X.7a (the new cluster picks its profile) OR
under a separate sub-pass. The lighter route is to bundle.

**Why this matters for the user signal**: a 2nd motion profile is the single
fastest unlock for "feels dynamic". Without it, every new template the system
ships under the corporate-suite contract continues to feel quiet because
quiet-editorial is the only motion vocabulary on disk.

### Gate X.7c · Editor-side palette swap with constraint enforcement
Per §5 above: this is the highest-value customization gap. Scope:
- New editor field on `WebTemplate`: `customer_palette_overrides` (JSONB).
- Editor UI: a 3-token palette picker (primary · secondary · accent).
- Constraint enforcement: CS-PAL-01 (L\* ≤ 40 on cream) · CS-PAL-05 (≤3
  accent hits per viewport) · auto-derive `primary-tinted` for hover states.
- Live preview: a "preview your palette" pane that re-renders the home
  with the customer's tokens.
- Versioning: a customer can save N palette presets per project.

**Why this matters for "user-customizable"**: today the customer cannot make
Cornice "their" Cornice. With palette swap, they can — without breaking the
typography contract, the layout family, the imagery, or the copy. It is the
single most visible customer-facing change.

**Scope guard**: this gate touches `apps/editor` and `apps/projects`, which
the audit brief forbids touching for THIS pass. Therefore Gate X.7c is the
recommended **next pass after X.7a/b** — not the immediate next.

### Gate X.7d (deferred · later) · Per-cluster standards-authoring
After X.7a ships one new cluster, the second new cluster is the moment to
build a `<cluster>-standards-template/` skeleton — a copy-paste-and-fill base
for the 7-doc standards stack that the orchestrator no longer authors from
scratch. This converts the per-cluster authoring cost from ~13 reports to
~13 cell-edits in a pre-built template.

Defer until 2 clusters have shipped under the new pipeline; the abstraction
is wrong if attempted before.

### Sequencing recommendation

```
NEXT 2 PASSES (mandatory):
  Phase X.7a · ship 1 new cluster (recommend: agency-creative-studio / Vertex
              hardening to corporate-suite parity · the editorial-quote-cover
              + colophon-press shape is the cleanest non-corporate-suite
              starting point).
  Phase X.7b · land motion_profile DNA dimension (bundle with X.7a's standards
              stack).

PASS AFTER (recommended):
  Phase X.7c · editor-side palette-swap (enters apps/editor scope · separate
              brief required).

LATER:
  Phase X.7d · per-cluster standards-authoring template (after 2nd new cluster).
```

**Specifically: do NOT add a 7th corporate-suite sibling until X.7a closes.**
The cluster has reached the strain point in its current grammar (Causa's hardest
slot was the thinnest at A.5b · the 7th's hardest slot will be thinner). Pushing
through anyway is the path that produces 12 corporate-suite siblings and zero
of any other grammar — and the user's signal predicts what the catalog will
look like at that point.

---

## §9 · Strongest conclusion

The corporate-suite cluster's L1–L9 layout-family system is a real engineering
achievement. It produces five (six with Causa) DOM-overlay-distinct siblings
that pass every distinctness gate. **It does NOT produce six tonally-distinct
templates.** All six read as instances of one grammar — Italian-premium-
editorial-restrained — which is the cluster's contract by design and is correct
for a single cluster.

The mistake would be to read "six L1–L9-distinct siblings" as "the factory
produces six different premium templates". It does not. It produces six skin
variations of one premium template — the boardroom-grade Italian-editorial
template. That is the *first* of the premium grammars the factory needs to
own. The user is correctly sensing that "first" hasn't moved to "second".

The DNA registry already names 22 layout archetypes spanning 8 categories with
real diversity in hero / nav / footer / card / button / tone / conversion /
motion vocabulary. The non-corporate-suite archetypes already on disk
(agency-digital-studio, cinematic-photographer, ultra-luxury-cinematic, etc.)
demonstrate the machine's capacity for genuinely different grammars. **What
the system has not done is exercise that capacity under the post-corporate-
suite hardening pipeline.** Six recent passes all reinforced the same grammar
because every one of them targeted the same cluster.

The next product pass must break the cluster boundary. Not by building a new
corporate-suite sibling — by walking a different cluster through the full
pipeline once. That single act produces:
- The 2nd standards stack (which becomes the template for the 3rd, 4th, ...).
- The 2nd imagery register (which breaks the Pexels-courtroom-pool exhaustion
  curve).
- The 2nd CTA inflection (which breaks the "Apri un X" monoculture).
- The 2nd motion vocabulary (which directly fixes the user's "not dynamic
  enough" signal).
- The 2nd tonal envelope (which directly fixes the user's "too similar" signal).

A single new-cluster pass dissolves four of the six top sameness signals. The
cost is one Cornice-equivalent pass + the standards-stack-authoring overhead
(~30% extra). The benefit is the catalog ceasing to read as "six versions of
one template."

---

## §10 · Top 7 system gaps (ordered by impact on the user signal)

| # | Gap | Severity | Scope | Resolution path |
|---|---|---|---|---|
| **1** | **One tonal grammar across all 6 latest templates** (Italian-premium-editorial) — every recent template inherits cluster contract that fixes the typographic envelope, CTA inflection, imagery register, and motion register simultaneously | **CRITICAL** | factory + standards + DNA | Phase X.7a · ship a 2nd cluster archetype under the full pipeline |
| **2** | **One motion vocabulary** (quiet-editorial · marquee-or-none · text-fade-in only · no parallax · no scroll-snap · no live-data) — the user's "not dynamic enough" signal directly maps to this | **HIGH** | DNA + standards | Phase X.7b · add `motion_profile` DNA dimension + 2 alternate profiles (`sprint-console` · `gallery-cinematic`) |
| **3** | **One CTA inflection** (italian polite imperative + abstract noun) shipped 6× across all six recent templates · 6 abstractions of the same gesture | **HIGH** | content-authoring contract + DNA | Bundles with X.7a; the new cluster ships a non-`Apri/Fissa/Avvia/Prenota` mental model (e.g., `[ Apri sessione ]` for digital-studio · `Visualizza dossier` for luxury) |
| **4** | **One imagery register** (Pexels editorial · zero-people OR environmental · cool-or-warm muted) — Causa A.5b proved the pool is now genuinely thin · 7th sibling will scrape the bottom | **HIGH** | imagery sourcing + standards | New cluster brings new pool key (e.g., `agency-creative-craft` · `photography-cinematic` · `luxury-property-dossier`) with fresh subject classes |
| **5** | **No editor-side palette swap** — customers cannot make a corporate-suite template "theirs" without orchestrator-side re-authoring | **HIGH** | editor + projects (out of scope this pass) | Phase X.7c · editor-side palette picker with CS-PAL-01/05 enforcement (separate pass · enters editor scope) |
| **6** | **Process weight exceeds product weight** — ~30 hardening + reference + per-sibling docs per cluster · doc rate now ≈ template rate · ORCHESTRATOR.md §6.1 anti-drift signal | **MEDIUM-HIGH** | meta-process | The next pass MUST land a product capability (not a 4th hardening report) · this audit is the last permitted process pass before product unlock |
| **7** | **No 2nd-cluster standards stack precedent** — the orchestrator has authored corporate-suite's stack from scratch · re-authoring 13 docs per new cluster is a doc-pass cost that pre-blocks scaling | **MEDIUM** | standards + design-orchestrator | Defer until 2nd cluster ships; THEN abstract the standards-stack as a template (Phase X.7d) |

Three additional named-but-secondary gaps (not in the top 7 but tracked):
- No retirement protocol (`corporate-suite-post-cornice-state.md §5.R8`).
- No batch-mode pipeline (each sibling is a serial walk).
- No personalization layer (geo · time · returning-visitor — gated by privacy
  posture · not blocked by it).

---

## §11 · Explicit recommendation

> **HARDEN FIRST. Specifically: ship Phase X.7a (one non-corporate-suite cluster
> walked through the full hardening pipeline) before any other template work.
> Bundle Phase X.7b (`motion_profile` DNA dimension + 2 alternate profiles)
> into X.7a. Hold the 7th corporate-suite sibling and any cross-cluster
> enrollment until X.7a closes.**

The case for "build more templates now" relies on the assumption that the next
template will be different from the last six. Inside the corporate-suite
cluster contract, that is structurally false: the next sibling will inherit the
contract that made the last six feel similar, and produce a 7th similar
sibling. Six similar templates is a bug · seven is the same bug repeated.

The case for "harden first" is direct: the user signal is correct, the system
gaps are named and bounded, the resolution is a single new-cluster pass plus a
DNA-dimension addition, both of which are cost-bounded and product-positive
(not process-positive). The hardening is *the* product unlock for the next
phase of catalog growth.

This audit closes itself. Phase X.7a opens next.
