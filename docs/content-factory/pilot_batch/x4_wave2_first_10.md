# Wave 2 · Pilot Batch (first 10 templates)

**Status**: approved in X.3 Step 0 Planning Audit. Binding for X.4 Wave 2 authoring kickoff.

**Scope**: the first 10 new templates the Content Factory produces after X.3 closes. All 10 ride existing enrolled archetypes (zero new archetypes). All 10 stay within D-099 program closure (zero touches to editor/projects/commerce/live_templates/static-editor).

**Post-pilot catalog state**: 20 + 10 = **30 templates editable**. Cluster coverage rises from 20/52 populated to 30/52.

**Gating**: this batch does not start until X.3 Commits 1-3 are green (scaffolding · cluster blueprints for all 10 pilot clusters · imagery packs for all 10 pilot clusters).

---

## Batch table

| # | Proposed brand slug | Source archetype | Target cluster | Visual style | Rationale |
|---|---|---|---|---|---|
| 1 | `fiscus-commercialista` | `corporate-suite` (Pragma) | `financial-services` | `dashboard-light` | Pragma shape reused for commercialista · financial dashboards + lead-capture fit existing corporate-suite page kinds · zero structural novelty · high B2B demand |
| 2 | `solaria-coaching` | `corporate-suite` (Pragma) | `coaching` | `minimal-light` | Same archetype, different cluster · business coach voice · light minimal style · widens Pragma family with zero schema touch |
| 3 | `zenith-consulting` | `corporate-suite` (Pragma) | `professional-services` | `dashboard-dark` | Third Pragma variant, dark enterprise style · tests variant matrix limits on single archetype · widens D-054 differentiation against Pragma + Solaria + Fiscus |
| 4 | `madou-pasticceria` | `fine-dining` (Gusto) | `bakery-pasticceria` | `editorial-warm` | Restaurant archetype stretched to bakery · menu kind preserved · reservation kind optional · editorial warm style coherent with Gusto neighbors |
| 5 | `cucina-di-rione` | `trattoria-warm` (Sapore) | `bar-bistrot` | `editorial-warm` | Trattoria archetype reused for bar-bistrot · deep-path menu section model (Sapore precedent) transfers · cluster positioning shifts to informal-quartiere |
| 6 | `denti-co-studio` | `specialist` | `dental` | `minimal-light` | Specialist archetype is shared (Cardio+Derm · A.9) · third template on same schema · dental terminology from medical glossary · cluster still inside medical macro-category boundary |
| 7 | `petro-veterinario` | `specialist` | `veterinary` | `minimal-light` | Fourth specialist variant · opens veterinary cluster · pet-focused imagery pack required · no new archetype, clinical-minimal visual style continuity |
| 8 | `atto-notai-associati` | `classic-gold` (Lex) | `notary-commercialista` | `classic-serif` | Lex classic-gold archetype reused for notary · terminology glossary `lawyer` covers both notary and notaio · classic serif style reinforces institutional positioning |
| 9 | `fotogramma-films` | `cinematic-photographer` (Pixel) | `videomaker` | `cinematic-fullbleed` | Portfolio archetype reused for videomaker · Pixel shell already supports video-adjacent content · cluster affine, minimal copy delta |
| 10 | `sapori-di-langa` | `artisan-workshop` (Bottega) | `wine-food-boutique` | `typographic-first` | Ecommerce archetype Bottega reused for wine/food boutique · typographic-first visual style coherent with artisanal positioning · food differentiation minimal, cluster genuinely different |

---

## Distribution summary

### By macro-category

- **Business**: 3 (Fiscus · Solaria · Zenith)
- **Restaurant**: 2 (Madou · Cucina di Rione)
- **Medical**: 2 (Denti+Co · Petro)
- **Lawyer**: 1 (Atto)
- **Portfolio**: 1 (Fotogramma)
- **Ecommerce**: 1 (Sapori di Langa)
- **6 macro-categories covered** (of 15 total)

### By source archetype (of 19 enrolled)

- `corporate-suite` · 3 templates
- `specialist` · 2 templates
- `fine-dining` · 1 template
- `trattoria-warm` · 1 template
- `classic-gold` · 1 template
- `cinematic-photographer` · 1 template
- `artisan-workshop` · 1 template
- **7 archetypes used** (of 19 total)

### By visual style (of 12)

- `dashboard-light` · 1
- `minimal-light` · 3
- `dashboard-dark` · 1
- `editorial-warm` · 2
- `classic-serif` · 1
- `cinematic-fullbleed` · 1
- `typographic-first` · 1
- **7 visual styles used** (of 12 total)

### By cluster (new clusters activated)

Clusters that go from 0 templates → 1 template via this batch:
- `financial-services`
- `coaching`
- `professional-services`
- `bakery-pasticceria`
- `bar-bistrot`
- `dental`
- `veterinary`
- `notary-commercialista`
- `videomaker`
- `wine-food-boutique`

**10 new clusters activated.** Post-pilot: 30/52 clusters populated (up from 20/52).

---

## Per-template execution notes

### 1 · `fiscus-commercialista`

- **Blueprint dependency**: `cluster_blueprints/financial-services.md` (X.3 Commit 2)
- **Imagery pack**: `imagery/packs/financial-services.md` (X.3 Commit 3) — direction: desks with paperwork + focused professional portraits + warm-neutral corporate palette. No clichéd calculator close-ups.
- **Feature flags expected**: `has_booking=True` (consulenza request) · `has_portfolio=False` · `has_blog=False` · others per blueprint
- **Price tier**: `standard`
- **Audience**: `["smb", "freelance"]`
- **D-054 framing**: distinct from Pragma's generic corporate feel via `dashboard-light` palette + `commercialista`-specific terminology + smaller audience focus (SMB/freelance vs enterprise)

### 2 · `solaria-coaching`

- **Blueprint dependency**: `cluster_blueprints/coaching.md`
- **Imagery**: bright lifestyle + workshop scenes + one-to-one settings · avoid "business coach in suit pointing at whiteboard" cliché
- **Feature flags**: `has_booking=True` · `has_portfolio=False`
- **Price tier**: `standard`
- **Audience**: `["smb", "freelance"]`
- **D-054**: distinct from Pragma + Fiscus via `minimal-light` style + coaching-specific voice (process-led, not balance-sheet-led)

### 3 · `zenith-consulting`

- **Blueprint dependency**: `cluster_blueprints/professional-services.md`
- **Imagery**: dark-mode dashboards + consulting-room moments + editorial business portraits
- **Feature flags**: `has_booking=True` · `has_portfolio=True` (case-studies style) · optional `has_blog` for insights
- **Price tier**: `premium`
- **Audience**: `["enterprise", "smb"]`
- **D-054**: dark dashboard style differentiates against the 2 lighter Pragma variants · case-studies section uses the `posts`-as-project-detail pattern already proven on Aura

### 4 · `madou-pasticceria`

- **Blueprint dependency**: `cluster_blueprints/bakery-pasticceria.md`
- **Imagery**: patisserie close-ups + warm oven light + Italian baking heritage aesthetic
- **Feature flags**: `has_booking=True` (reservation optional) · `has_shop=False` (MVP · no e-commerce)
- **Price tier**: `premium` (positioning with Gusto)
- **Audience**: `["smb"]`
- **D-054**: distinct from Gusto via bakery-specific terminology + dessert-forward hero + different chef narrative (pasticciere vs chef)

### 5 · `cucina-di-rione`

- **Blueprint dependency**: `cluster_blueprints/bar-bistrot.md`
- **Imagery**: neighborhood bistrot vibes + warm evening light + casual dining scenes
- **Feature flags**: `has_booking=True`
- **Price tier**: `standard`
- **Audience**: `["smb", "freelance"]`
- **D-054**: distinct from Sapore (trattoria) via shift toward bistrot/quartiere positioning, not traditional-regional

### 6 · `denti-co-studio`

- **Blueprint dependency**: `cluster_blueprints/dental.md`
- **Imagery**: clean dental operatory + patient-forward portraits + understated clinical palette · zero "perfect smile teeth close-up" stock
- **Feature flags**: `has_booking=True`
- **Price tier**: `standard`
- **Audience**: `["smb", "studio"]`
- **D-054**: distinct from Cardio/Derm via dental-specific terminology + brighter clinical palette + chair/equipment imagery specific to dental practice

### 7 · `petro-veterinario`

- **Blueprint dependency**: `cluster_blueprints/veterinary.md`
- **Imagery**: animal-forward (pets in consultation, not hunting/sport) · clinical but warm
- **Feature flags**: `has_booking=True`
- **Price tier**: `standard`
- **Audience**: `["smb", "studio"]`
- **D-054**: distinct from Cardio/Derm/Denti via animal-focused imagery + terminology (`animali-domestici`, `ambulatorio-veterinario`)

### 8 · `atto-notai-associati`

- **Blueprint dependency**: `cluster_blueprints/notary-commercialista.md`
- **Imagery**: formal office interiors + archival aesthetic + document-centric scenes · no dusty-books cliché
- **Feature flags**: `has_booking=True` (consulenza notarile)
- **Price tier**: `premium`
- **Audience**: `["studio", "smb"]`
- **D-054**: distinct from Lex/Juris via notary-specific terminology (`atti-notarili`, `rogito`) + more institutional palette

### 9 · `fotogramma-films`

- **Blueprint dependency**: `cluster_blueprints/videomaker.md`
- **Imagery**: behind-the-scenes film sets + cinematic stills + video-adjacent portraits · avoid "generic DSLR close-up" stock
- **Feature flags**: `has_portfolio=True` · `has_video=True` (cluster-specific)
- **Price tier**: `premium`
- **Audience**: `["freelance", "studio"]`
- **D-054**: distinct from Pixel (photography) via film-production terminology + reel-forward hero

### 10 · `sapori-di-langa`

- **Blueprint dependency**: `cluster_blueprints/wine-food-boutique.md`
- **Imagery**: vineyard + producer portraits + bottle/ingredient close-ups · Langa territory aesthetic
- **Feature flags**: `has_shop=True` (ecommerce cluster) · `has_blog=True` (journal) · `has_booking=False`
- **Price tier**: `premium`
- **Audience**: `["smb", "freelance"]`
- **D-054**: distinct from Bottega via wine-food-specific terminology + Piedmont-Langhe positioning (geo-specific justified) + editorial-vineyard imagery

---

## Non-goals for this batch

- ❌ No new archetypes.
- ❌ No new page kinds.
- ❌ No editor/preview-bridge/live-template surface changes.
- ❌ No commerce backend changes (Sapori di Langa uses Bottega's existing shop surface).
- ❌ No new feature flags beyond the 7 established in X.2.
- ❌ No visual-style additions beyond the 12 established in X.2.
- ❌ No locale addition beyond the 5 canonical (it/en/fr/es/ar).
- ❌ No new ROLE_DISCOVERY entries (pilot batch aligns with existing roles).

---

## Exit criteria for the batch

The Wave 2 pilot is complete when:

- [ ] 10 templates merged to `phase-integration-baseline-v15`
- [ ] Each template passes the reviewer acceptance checklist (`runbook.md` §5)
- [ ] Each template's live preview routes return HTTP 200 across 5 locales (IT · EN · FR · ES · AR)
- [ ] Each template's detail page shows correct cluster pill, visual-style pill, price-tier badge
- [ ] Each template's typeahead match works for core keywords
- [ ] Each template's cluster-detail page lists the template
- [ ] Playwright MCP browser walk green on the 10 templates' detail + home-preview surfaces (sampling AR preview for at least 3 templates)
- [ ] Smoke count increases from 854 to approximately 954-1054 routes (each new template adds ~10 new routes at 5 locales × 2 pages avg)

Post-exit: open Wave 2 full run (remaining ~50 templates to reach 80+ catalog target), using the same recipe.

---

**End of pilot batch spec. Binding for Wave 2 kickoff in X.4.**
