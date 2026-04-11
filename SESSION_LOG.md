# Session Log

## Session 19 — Phase 2g2x.1 Portfolio Triage + Surgical Fix (2026-04-11)

**Agent:** Portfolio blocker triage + surgical CSS/copy fix.
**Goal:** Session 18 declared portfolio approved, but a manual verification pass found two real issues worth triaging before commit: (1) the "Anteprima Live" CTA on the detail page did nothing useful for most templates, and (2) the full-size preview of Chiara on `/templates/portfolio/chiara-portfolio-creativo/` appeared to have a visual overlap/rendering glitch. This session executed a severe triage first, then a strictly-scoped fix for the single real blocker.

### Part 1 — Triage outcome

Two findings:

1. **The "Anteprima Live" button is a legacy gating placeholder, not a portfolio-scope bug.** `templates/catalog/template_detail.html:132-136` has an `{% if has_live_preview %} ... {% else %} <a href="#">Anteprima Live</a> {% endif %}` branch. `has_live_preview` resolves via `template_content.has_live_template(slug)` → `slug in TEMPLATE_CONTENT`. `TEMPLATE_CONTENT` only has 3 entries (cardio / dermatologia / gusto), so **17 of 20 templates** hit the `href="#"` placeholder branch, including both Chiara and Pixel. Cardio detail confirmed in browser to show the correct "Apri anteprima completa" → `/preview/` link with `target="_blank"`. D-045 documents this gating as intentional. This is a system-wide UX issue affecting all preview-only templates, **not caused by and not in scope of portfolio hardening**. Deferred to a future micro-phase (see Next micro-step).

2. **Chiara's preview composition HAS a real, reproducible layout overflow bug.** Confirmed by reading the generated PNG directly and by a cache-busted browser walk. Root cause: `editorial-designer-grid.html:92-93` sets `.ed-hero { height: 490px; padding: 72px 72px 42px; }` → 376 px of inner vertical space, but with `.ed-left h1 { font-size: 82px; line-height: 0.97; max-width: 760px; margin-top: 36px; }` the 57-char headline `'Sistemi di <em>identità visiva</em> costruiti una griglia alla volta.'` wraps to 5 lines (~397 px) and the full content stack (eyebrow + h1 + sub + cta-row + margins) needs ~640 px. With `.ed-hero` having no `overflow: hidden`, ~260 px of content bleeds down into `.ed-ledger` and `.ed-ribbon` below. The rendered PNG shows the "RICHIEDI IL PORTFOLIO COMPLETO" CTA, the filter pills (`TUTTO · IDENTITÀ · EDITORIA · ART DIRECTION`), and the ledger intro heading `Progetti selezionati · ventidue case study` all visually colliding. Reproduces after `--force` regeneration → it's a CSS/copy bug, not a stale render.

### Part 2 — Ghost dev-server gotcha (operational)

During the triage's first browser walk the detail page showed "Ogni progetto una storia" — the **legacy** `portfolio.html` content Session 18 claimed to have eliminated. This looked alarming until a process audit showed TWO listeners on port 8765: PID 29132 (`runserver --noreload`, started 11:24 **from a prior session's worktree**) and the current session's new pair. PID 29132 was answering new connections and serving a completely different PNG at the same URL (3.3 MB, legacy content) than what was physically on disk (725 KB, new broken `'Sistemi'` content). Killing 29132 brought Python urllib and the cache-busted browser back into agreement with the filesystem. **New lesson:** before any visual walk, kill any lingering `runserver` processes on your target port. Added to the preview-pipeline gotchas list.

### Part 3 — Stale-PNG trap reproduced (confirmation of Phase 2g2x.5)

Two consecutive `generate_previews --only chiara-portfolio-creativo --force` runs both produced suffixed filenames (`_lEh35gE.png`, `_0NgBTC3.png`, `_TJW36Ho.png`) because Django's `FileSystemStorage.get_available_name()` appends a hash when the target filename already exists on disk. The `--force` path in `generate_previews.py:211-216` deletes the old DB row but **does not delete the file on disk**, so each regen creates a new orphan on top of the previous one. This is the Phase 2g2x.5 `dna_signature` trap — already known, still deferred, now with a concrete repro on top of the existing Session 8/10/12/15 evidence. Session 19 cleaned up its own orphans manually by moving the final asset file back to the canonical filename and updating the DB row.

### Part 4 — Surgical fix applied

Scope: strictly Chiara. Zero other files touched outside the surgical set.

**Files modified (Session 19 delta only):**

| File | Change |
|------|--------|
| `templates/preview_compositions/portfolio/editorial-designer-grid.html` | `.ed-hero` padding `72 72 42` → `52 72 38`; added `overflow: hidden` as hard cap against any future content bleed. `.ed-left h1` font-size `82` → `62`, line-height `0.97` → `0.98`, letter-spacing `-0.04em` → `-0.035em`, margin-top `36` → `22`, max-width `760` → `720`. `.ed-left .sub` margin-top `34` → `20`, max-width `520` → `560`, font-size `15` → `14`, line-height `1.7` → `1.6`. `.ed-left .cta-row` margin-top `38` → `22`, gap `28` → `22`. Added a block-leading comment documenting the vertical budget math. |
| `apps/catalog/template_dna.py` | `chiara-portfolio-creativo` → `content.headline` trimmed from `'Sistemi di <em>identità visiva</em> costruiti una griglia alla volta.'` (57 chars, wrapped to 4-5 lines at 62-82 px display) to `'Identità visive, <em>una griglia alla volta</em>.'` (47 chars, wraps to 2 lines at 62 px display). Both key semantic signals preserved: `identità visive` (Chiara's profession) and `una griglia alla volta` (Chiara's craft metaphor). As a deliberate side effect, the new headline now mirrors Pixel's `'Fermare il tempo, una luce alla volta.'` syntactic rhythm — both siblings use the same `'…, una X alla volta.'` structure with X being the medium of each profession (griglia for designer, luce for photographer), strengthening rather than weakening the differentiation. An inline comment in `template_dna.py` documents the reason for the trim so the rationale survives future edits. |

Why CSS alone wasn't enough: at 62 px h1 + 720 max-width the old 57-char headline still wrapped to 4 lines (h1 height 243 px), and the content stack bottom landed at canvas y 553 — which visually overlapped `.meta-strip` (absolute-positioned at canvas y 495-550 inside the hero). With the trimmed copy, h1 wraps to 2 lines (122 px), stack bottom lands at y 432, and there's a clean 63 px gap to the meta-strip. Pure CSS would have required dropping h1 font-size below ~50 px or restructuring the meta-strip's positioning — either of which would have been a much bigger change to Chiara's DNA than a 10-character copy trim that preserved both signature signals.

### Hard validation (Session 19 delta)

- `python manage.py check` — **clean** (0 silenced)
- `python manage.py generate_previews --only chiara-portfolio-creativo --force` — green, rendered with `[editorial-designer-grid]` label, new PNG written
- Orphan cleanup — old suffixed files (`_lEh35gE`, `_0NgBTC3`, `_TJW36Ho`) removed, final asset restored to canonical `chiara-portfolio-creativo-preview.png` filename, DB row updated via shell to point at the canonical name. `media/template_assets/2026/04/` now contains **exactly one Chiara PNG and one Pixel PNG** — no orphans.
- Playwright Chromium visual walk at 1440×900 on a fresh dev server:
  - `/templates/portfolio/` listing — two cards unmistakably distinct at card size. Pixel: dark cinematic, fullbleed photo. Chiara: cream paper, typographic hero with `Identità visive, una griglia alla volta.` headline visible. **PASSES.**
  - `/templates/portfolio/chiara-portfolio-creativo/` detail — preview image is clean. Headline 2 lines, subhead 3 lines, CTA row + meta-strip + project index card + ledger panel + clients ribbon all properly separated. **Zero overlap.** **PASSES.**
  - `/templates/portfolio/pixel-portfolio-fotografico/` detail — untouched, identical to pre-session state. Dark cinematic hero + EXIF bar + filmstrip + footer. **PASSES.**
- Direct raw-PNG inspection at `/media/template_assets/2026/04/chiara-portfolio-creativo-preview.png` with cache-bust — final rendering matches the spec.

### Exit state

- **Chiara blocker: closed.** Layout is clean, no overlap, meta-strip properly preserved, identity still typographic-led, differentiation vs Pixel unchanged (actually strengthened via headline parallel).
- **Pixel: untouched.** Zero edits to `cinematic-photographer.html` or `pixel-portfolio-fotografico` DNA.
- **Working tree is clean** apart from the deliberate Session 19 delta: `editorial-designer-grid.html` modification, `template_dna.py` headline trim, the canonical PNG file re-emitted at 717 KB, and the updated session/decisions/todo/handoff/registry/memory docs.
- **Phase 2g2x.1 portfolio category** is now truly ship-ready. Commit unblocked. Per D-049 the full wave commit + PR still waits for the 3 remaining CRITICO categories (real-estate / lawyer / agency) to close, but the portfolio-scope work no longer has a blocker.

### Risks residui / what Session 19 explicitly did NOT touch

- **"Anteprima Live" legacy placeholder** — confirmed systemic, deferred. Needs its own micro-phase: hide the button / swap to a PNG lightbox / label as disabled state. 17 of 20 templates affected.
- **Phase 2g2x.5 stale-PNG structural fix** — reproduced during this session's regen loop, still deferred. Manual orphan cleanup is a workaround, not a fix.
- **Ghost `--noreload` dev servers** — new operational lesson logged for the pipeline gotchas memory: always check `netstat` for stale listeners before a visual walk.
- **3 CRITICO categories** (real-estate, lawyer, agency) — unchanged, still open, still the next micro-step.

### Next micro-step

Commit portfolio hardening now (Session 18 + Session 19 work, one commit) — then pick the next CRITICO category from the remaining 3 per the recommended order (real-estate → lawyer → agency) and run the Session 17/18 recipe end-to-end. Do not batch. Before each visual walk, kill any lingering `runserver` processes on the target port.

---

## Session 18 — Phase 2g2x.1 Portfolio Hardening (2026-04-11)

**Agent:** Portfolio category DNA split — second implementation wave of Phase 2g2x (catalog hardening, per D-049), following the Session 17 business recipe.
**Goal:** Close the `portfolio` identity-crash case. Make Chiara and Pixel two clearly distinct products at card size — different profession, different imagery, different silhouette, different CTA pattern, different section order — without quick-recoloring the legacy `portfolio.html` composition or touching any other category.

### Technical audit (confirmed the Session 16 findings)
Neither `chiara-portfolio-creativo` nor `pixel-portfolio-fotografico` had a DNA entry, so both resolved to legacy `templates/preview_compositions/portfolio.html` via `CATEGORY_TO_COMPOSITION["portfolio"]`. The legacy composition hardcodes literal designer-specific copy in eight places, catastrophically wrong for Pixel (who is a photographer):

| File | Line | Literal |
|------|------|---------|
| `portfolio.html` | 102 | `Selected work · 2018 — 2026` |
| `portfolio.html` | 103 | `Ogni progetto<br>una storia.` |
| `portfolio.html` | 104 | `Sono una designer indipendente che lavora con brand, editori e artisti. Identità visive, art direction, libri e siti su misura — niente di pre-confezionato.` |
| `portfolio.html` | 107 | `Independent designer · Milano` |
| `portfolio.html` | 113 | `Featured · Atlas Magazine` |
| `portfolio.html` | 130 | `Atelier Norma` (project tile) |
| `portfolio.html` | 133 | `Atlas Issue 14` (project tile) |
| `portfolio.html` | 136 | `Lumen Studio` (project tile) |
| `portfolio.html` | 139 | `Polare — Visual Series` (project tile) |

Both templates pulled from the single legacy `portfolio` imagery pool (6 shared URLs) — macro tone + photos identical. The effect was an identity-crash: Pixel (photographer) rendered as a designer with designer-specific copy and identical photos to Chiara.

### Strategy chosen — Option A (DNA split, 2 archetypes) per D-050
Chiara (indep designer / art direction / editorial / systemic studio) and Pixel (photographer / visual storyteller / cinematic portfolio) are semantically as far apart as Pragma/Elevate were in Session 17 — they demand entirely different silhouettes, dominant visuals, CTA patterns, and macro tones. A forced-shared skin would either erase the profession difference (recolor pair) or collapse into a conditional-branching frankenfile. Option A is the same recipe that already worked for business.

Two new archetypes:
- **`editorial-designer-grid`** (Chiara) — cream paper page, typographic drama, **NO big hero photo**, numbered project index on the right, ledger of case-study cards, clients ribbon footer. The hero IS the typography. Tone: `editorial-designer`. Conversion: `case-study-request` ("Richiedi il portfolio completo").
- **`cinematic-photographer`** (Pixel) — fully dark page, **dominant fullbleed photograph** covering ~62% of the canvas, film-strip EXIF credit bar pinned to the hero bottom, filmstrip gallery of series stills, 4-cell EXIF footer. The hero IS the photograph. Tone: `cinematic-authorial`. Conversion: `series-brief` ("[ Apri la serie completa ]").

### Files added / modified (portfolio scope only)
- `apps/catalog/template_dna.py` — 2 new DNA entries (`chiara-portfolio-creativo`, `pixel-portfolio-fotografico`), 2 new layout archetypes (`editorial-designer-grid`, `cinematic-photographer`), vocabulary extensions across 10 dicts (hero_style × 2, navbar_style × 2, footer_style × 2, card_style × 2, button_style × 2, tone × 2, conversion_pattern × 2, imagery_direction × 2).
- `apps/catalog/preview_imagery.py` — 2 new pools (`portfolio-designer`, `portfolio-photographer`). Zero URL overlap with each other, zero overlap with legacy `portfolio` pool. Legacy pool relabelled with explanatory comment per D-036 (kept, architecturally unused by any published template).
- `templates/preview_compositions/portfolio/editorial-designer-grid.html` — NEW. Cream paper chrome with typographic hero left + project index card right, ledger-row panel, clients ribbon + studio coordinates footer. D-047 compliant from the first line — zero literal brand strings, zero hardcoded image URLs.
- `templates/preview_compositions/portfolio/cinematic-photographer.html` — NEW. Fully dark with fullbleed photo hero, corner frame marks, film-strip EXIF credit bar, filmstrip gallery row, monospaced-style bracketed CTAs. D-047 compliant from the first line.
- Session docs: `SESSION_LOG.md`, `DECISIONS.md` (+D-051), `TODO_NEXT.md`, `AGENT_HANDOFF.md`, `TEMPLATE_REGISTRY.json` (v0.7.2).

### Differentiation matrix — Chiara vs Pixel
| Dimension                 | Chiara (editorial-designer-grid) | Pixel (cinematic-photographer) |
|---------------------------|------------------------------------|-------------------------------|
| Profession positioning    | Indep designer · art direction · visual identity | Photographer · visual storyteller · still-life |
| Macro tone                | Cream paper (`#f3efe5`) + coral accent | Near-black (`#050505`) + red accent |
| Hero silhouette           | Two-column typographic — huge Syne headline LEFT + project index card RIGHT. **NO big hero photo.** | Fullbleed dominant photograph covering 62% of the canvas. **The hero IS the photo.** |
| Dominant image            | None (hero is typographic). Only small accent tiles. | Full-bleed moody low-key still (cinematic photostill pool). |
| Section order             | rule-nav → typographic-hero → project-ledger → clients-ribbon | fullbleed-dark-nav → fullbleed-hero → exif-bar → filmstrip-gallery → exif-credits |
| Navbar                    | Hairline rule + asterisk wordmark + index-letter links + "Nuove commesse" status chip | Transparent dark + circular shutter wordmark + uppercase tracked links + "Disponibile per commissioni" pulse + `[ Richiedi commissione ]` bracket CTA |
| Primary CTA               | "Richiedi il portfolio completo" — ghost sans-rule, editorial | "[ Apri la serie completa ]" — ghost mono-bracket, technical |
| Typography pairing        | Syne + Inter (designer-display) | Archivo + Inter (uppercase tracked, technical) |
| Narrative pattern         | Numbered project ledger + categories filter + clients ribbon | Series counter (06/42) + EXIF bar + filmstrip of 4 series stills + credits cells |
| Imagery pool              | `portfolio-designer` (design workspace artifacts) | `portfolio-photographer` (cinematic photostills) |
| Imagery overlap with sib. | 0 URLs | 0 URLs |

### Stale-PNG check
Worktree started with no `media/` directory and no pre-existing TemplateAssets, so there was nothing to go stale. Session 18 did not hit the timing trap. Phase 2g2x.5 (dna_signature structural fix) still deferred.

### Hard validation
- **`python manage.py check`** — clean (0 issues silenced)
- **`python manage.py seed_templates`** — 20/20 templates created idempotently, no errors
- **`python manage.py generate_previews`** — 20/20 green (2 portfolio templates first via `--only`, then 18 remaining in one pass). New archetype labels logged: `[editorial-designer-grid]` for Chiara and `[cinematic-photographer]` for Pixel.
- **Bidirectional leak sweep** on rendered HTML of both templates:
  - **Chiara → Pixel**: grepped 26 Chiara-specific tokens (`Chiara`, `identità visiva`, `sistemi visivi`, `Casa editrice`, `Festival di poesia`, `Fondazione culturale`, `Vino naturale`, `Museo civico`, `Rivista d'architettura`, `art direction`, `editorial`, `designer`, `Studio indipendente`, `Archivio lavori`, `Progetti selezionati`, `Packaging`, `Wayfinding`, `Identità · Editoria` + all 8 legacy literals) — **zero Chiara-brand leaks in Pixel**. The only hits were: (a) a self-referential CSS comment in `cinematic-photographer.html` that names the opposite archetype for documentation ("Deliberate visual opposite of editorial-designer-grid"), and (b) the word "editoriale" inside Pixel's own subhead "commissioni editoriali" — used correctly in the photographer sense of "editorial commissions". Neither is a cross-tenant leak.
  - **Pixel → Chiara**: grepped 25 Pixel-specific tokens (`Pixel`, `ore rubate`, `Campi lunghi`, `Stanze vuote`, `città senza persone`, `Fotografia documentaria`, `fotograf`, `pellicola`, `obiettivo`, `camera oscura`, `still-life`, `reportage`, `ritratto`, `commissioni editoriali`, `Dodici anni`, `EXIF`, `Spring 2026`, `Fine art`, `Medio formato`, `tiratura`, `fine-art`, `Serie corrente`, `Apri la serie`) — **zero Pixel-brand leaks in Chiara**.
  - **Legacy literal sweep** on both rendered HTMLs: grepped `Sono una designer`, `Selected work · 2018`, `Atlas Magazine`, `Independent designer`, `Atelier Norma`, `Lumen Studio`, `Polare — Visual`, `Ogni progetto.*storia`, `Atlas Issue` — **zero legacy literals** in either rendered HTML.
  - **Hardcoded URL sweep** on `templates/preview_compositions/portfolio/` — **zero hardcoded `images.unsplash.com` URLs** in either new composition.
- **Listing page leak sweep**: dumped `/templates/portfolio/` HTML (13 494 bytes) and grepped for all 9 legacy literals — **zero matches**. Both cards render with their correct brand names ("Pixel — Portfolio Fotografico" · Pixel Photography) and ("Chiara — Portfolio Creativo" · Chiara Studio).
- **Django test client route sweep**: 5/5 routes return 200 — `/`, `/templates/`, `/templates/portfolio/`, `/templates/portfolio/chiara-portfolio-creativo/`, `/templates/portfolio/pixel-portfolio-fotografico/`.
- **Chromium visual walk at 1440×900** on `/templates/portfolio/` via Playwright MCP — both cards visible side-by-side, unmistakably distinct at card size. Pixel reads as a dark cinematic card with fullbleed low-key image; Chiara reads as a cream paper card with typographic headline and project index. Full-size preview PNGs (3200×1800) spot-checked and confirmed to match the differentiation matrix above.

**The two cards read as two completely different products, two completely different professions, two completely different narrative patterns. The identity-crash is closed.**

### Risks residui / what's NOT done
- **3 of 5 CRITICO categories still open:** agency, lawyer, real-estate. Recommended next order per AGENT_HANDOFF: real-estate → lawyer → agency. Same Session 17/18 recipe.
- **MEDIO items still open** (Phase 2g2x.3): D-047 lift on ecommerce fashion-editorial + artisan-workshop, restaurant trattoria-warm + street-modern, medical clinic/family/wellness preview comps, and the restaurant fine-dining live skin (Phase 2g.3).
- **Template completeness gap still open** (Phase 2g2x.4): 17 of 20 templates are preview-only. Chiara and Pixel are not exceptions — both remain preview-only (no content registry, no live-template skin folder). Per scope rule "do not introduce live multipage portfolio if not existing", Session 18 did not add inner pages.
- **Stale-PNG structural fix still deferred** (Phase 2g2x.5). Session 18 did not hit the trap because the worktree started empty.
- **Worktree not merged.** `phase-2g2x-portfolio-hardening-v2` branch, last commit `b967e99` was Session 17's business hardening fix; Session 18 work is uncommitted. Per D-049 gate, commit + PR after all 5 CRITICO categories close.

### Next micro-step
Pick ONE of the 3 remaining CRITICO categories. Recommended order: **real-estate** (Villa's ultra-luxury vs Casa's mass-market is the next cleanest "far apart" pair and has the mass-market price-range `€500K–€1.2M` literal that's the most visible leak) → lawyer → agency. Run the Session 17/18 playbook end-to-end in a fresh worktree, apply D-047 from line one, and do NOT skip the Chromium visual walk.

---

## Session 17 — Phase 2g2x.1 Business Hardening (2026-04-11)

**Agent:** Business category DNA split — first implementation wave of Phase 2g2x (catalog hardening, per D-049).
**Goal:** Close the `business` identity-crash case. Make Pragma and Elevate two clearly distinct products at card size — different imagery, different silhouette, different CTA pattern, different section order, different positioning — without quick-recoloring the legacy composition or touching any other category.

### Strategy chosen — Option A (DNA split, 2 archetypes)
The Session 16 audit offered two paths: (A) split into 2 distinct archetypes with their own compositions, or (B) lift the legacy composition into a D-047-compliant shared skin with per-tenant DNA content blocks. **Option A was selected** because Pragma (board advisory) and Elevate (SaaS landing) are semantically far apart — they demand entirely different silhouettes, section orders, CTA patterns, and dominant visuals. A forced-shared skin would either erase the differentiation or collapse into a conditional-branching frankenfile that only appears to share structure. Option A is the same recipe that already worked for medical (4 archetypes), restaurant (3), and ecommerce (2).

### What changed
**Five files modified, two files added, zero files deleted.**

| File | Change |
|------|--------|
| `apps/catalog/template_dna.py` | Added 2 archetypes to `LAYOUT_ARCHETYPES` (`corporate-suite`, `startup-saas-landing`). Added 2 hero styles (`split-executive`, `centered-manifesto-product`). Added 2 navbar styles, 2 footer styles, 2 card styles, 2 button styles, 2 tones, 2 conversion patterns, 2 imagery directions. Added **2 DNA entries** — `pragma-corporate-suite` and `elevate-startup-landing` — each with a full content block driving every literal the composition renders. |
| `apps/catalog/preview_imagery.py` | Added 2 new imagery pools: `business-corporate` (6 executive/boardroom/HQ/manufacturing URLs) and `business-startup` (6 dashboard/laptop/code/open-plan URLs). Zero URL overlap between the two pools and zero overlap with the legacy `business` pool. Legacy `business` pool kept with an inline header comment explaining it is architecturally unused by any published business template but preserved per D-036 (DNA system is additive). |
| `templates/preview_compositions/business/corporate-suite.html` | **NEW.** Photo-led institutional split hero. Solid navy full-bleed navbar, serif headline left with meta strip, boardroom photo right with credit ribbon, 3-up advisory pillar cards with serif numerals, floating KPI strip over navy band, sectors ribbon at the very bottom. Merriweather + Inter. Every text string flows from `{{ dna.content.* }}` or `{{ brand_name }}`. |
| `templates/preview_compositions/business/startup-saas-landing.html` | **NEW.** Typographic manifesto on a cosmic primary/secondary gradient with neon accent glow. Thin pulse launch banner at the top, floating pill navbar with glowing CTA, centered 92px manifesto headline with gradient highlight, feature-pills row, glowing product-mockup card overlapping the hero bottom (chrome bar + 3 metrics including price), social-proof wordmark row and live ship-log + next-release chip at the bottom. **Intentionally photo-light** — no big hero photo — so Elevate's card does not lean on imagery for differentiation. Manrope + Inter. Zero literals outside DNA content fields. |
| `SESSION_LOG.md` · `DECISIONS.md` · `TODO_NEXT.md` · `AGENT_HANDOFF.md` · `TEMPLATE_REGISTRY.json` | Updated to reflect the new business DNA split and the Phase 2g2x progress. |

The legacy `templates/preview_compositions/business.html` and the legacy `business` imagery pool are **intentionally untouched**. Per D-036 (DNA system is strictly additive), they remain in place as the fallback for any future template that might want to render through them. Both currently published business templates now bypass them entirely via DNA resolution.

### Differentiation matrix (final)
| Axis | Pragma · corporate-suite | Elevate · startup-saas-landing |
|---|---|---|
| Macro tone | Cream `#eef0f3` page + solid navy header band | Cosmic primary/secondary gradient + neon accent glow |
| Hero silhouette | 55/45 split: serif headline + meta strip L · boardroom photo R | Centered typographic manifesto, NO photo, product-mockup card overlap |
| Dominant visual | Full-bleed boardroom photograph `{{ imagery.0 }}` | Glowing product-mockup card with 3 metric readouts |
| Typography | Merriweather (serif, institutional) + Inter | Manrope (geometric sans, tech) + Inter |
| Navbar | Full-bleed solid navy, left-aligned links, phone CTA right | Floating pill, centered, glowing primary CTA button |
| Primary CTA | `Fissa una call privata` (ghost outline on navy) | `Inizia gratis` (glow pill) + `Guarda la demo · 2 min` secondary |
| Section order | hero → advisory pillars → KPI strip → sectors ribbon | launch banner → pill-nav → manifesto hero → product mockup → social proof → ship log |
| Positioning copy | Board advisory / M&A / governance / PMI | Conversion landing / GTM kit for SaaS & startup / waitlist → MRR |
| Imagery pool | `business-corporate` (6 URLs) | `business-startup` (6 URLs) — fully disjoint set |
| Density profile | airy | medium |
| Tone vocabulary | advisory-sober | growth-tech |

### Hard validation
- **`python manage.py check` — clean.**
- **`python manage.py seed_templates` — 20 templates, 0 created (idempotent re-run).**
- **`python manage.py generate_previews` — 18 rendered, 2 skipped.** Pragma and Elevate were generated earlier via `--only` targeted runs. The `business-corporate` pool fetched 6/6 Unsplash URLs; `business-startup` fetched 6/6. No 404s.
- **Leak sweep — zero cross-tenant contamination in both directions:**
  - Rendered Elevate HTML contains none of 21 Pragma-token strings tested: `"Hanno scelto Pragma"`, `"Marco Bianchi"`, `"Vectra Industries"`, `"NORDEA"`, `"VECTRA"`, `"FINOVA"`, `"ATLAS"`, `"info@pragmacorp.it"`, `"Parliamone"`, `"Consulenza strategica · B2B"`, `"Servizi di consulenza"`, `"Strategia commerciale"`, `"Trasformazione digitale"`, `"Ottimizzazione processi"`, `"Sostenibilità ESG"`, `"Soluzioni concrete per"`, `"far crescere"`, `"Affianchiamo le PMI italiane"`, `"Richiedi una call"`, `"Clienti soddisfatti"`, `"€45M"`.
  - Rendered Pragma HTML contains none of 28 Elevate-token strings tested: `"waitlist"`, `"MRR"`, `"quattordici giorni"`, `"Inizia gratis"`, `"Guarda la demo"`, `"Stripe"`, `"A/B test"`, `"Edge analytics"`, `"Copy kit italiano"`, `"elevate.app"`, `"Live A/B"`, `"Adottato da 240 startup italiane"`, `"FLUX"`, `"NOVA"`, `"QUANTA"`, `"HELIX"`, `"RIFT"`, `"CASP"`, `"Plan Launch"`, `"CLI deploy"`, `"Ship log live"`, `"v2.9"`, `"Serie A"`, `"Q2 2026"`, `"GrowthBook"` …
- **Hardcoded-URL sweep:** neither rendered HTML contains a literal `https://images.unsplash.com/…` URL. Every imagery slot resolves through the `{{ imagery.N }}` context variable, which is populated from cached file:// URIs at render time.
- **Django test-client route sweep — 5/5 green:**
  - `/` 200
  - `/templates/` 200
  - `/templates/business/` 200
  - `/templates/business/pragma-corporate-suite/` 200
  - `/templates/business/elevate-startup-landing/` 200
- **Preview-asset wiring verified:** `WebTemplate.preview_asset` on both slugs returns the new canonical PNG filename. The business category listing HTML references both preview filenames and both brand names (only their own) — no cross-tenant brand mentions.
- **Visual regression via Chromium (Playwright)** at 1440×900 on `/templates/business/`: the two cards are unmistakably distinct. Elevate card = dark cosmic gradient + neon-cyan manifesto headline + glowing product mockup. Pragma card = cream/navy institutional split + boardroom photo + serif "Dove si prendono le decisioni che contano". Macro tone, silhouette, dominant visual, and positioning copy all differ.

### Why this closes the business identity-crash case
The Session 16 verdict was: "Elevate's card renders Pragma's copy". After Session 17:
1. Neither template resolves through the legacy `business.html` composition anymore — both have DNA entries, so `_resolve_composition` routes them to their archetype-specific files.
2. The legacy `"Hanno scelto Pragma"` label, client wordmark row, "Marco Bianchi" testimonial, B2B consulting CTAs, and the 4 consulting service cards have **all been removed from Elevate's render path**. They still exist in `business.html` for any future template that explicitly opts into the legacy file, but no published template does.
3. The two new skins were authored under the D-047 chrome-authoring contract from the first line — every string lives in `dna.content.*` or pulls from `brand_name`. No follow-up "lift pass" will ever be needed for this pair.
4. The imagery pools are fully disjoint: executive boardroom photos vs startup product/dashboard photos. Additionally the startup composition deliberately avoids a big hero photo, so even at 200×120 card thumbnail size the difference is readable entirely from macro tone + typographic silhouette.
5. The positioning copy is now genuinely different: Pragma headline reads as advisory gravitas ("Dove si prendono le decisioni che contano"); Elevate reads as growth conversion ("Dalla waitlist al primo MRR in quattordici giorni").

### Lessons (carry forward for Phase 2g2x.1.next — agency/lawyer/real-estate/portfolio)
1. **Option A (DNA split) is the default for semantically-far siblings.** Only reach for Option B (D-047 lift of shared composition + per-tenant content) when the two tenants are genuinely close. Business, real-estate (ultra-luxury vs mass-market), portfolio (designer vs photographer), and agency (bold vs editorial) are all "far apart" by the same yardstick — they should all follow Option A.
2. **Author under D-047 from line one.** The specialist chrome needed a 17-leak lift in Session 14 because it was authored before the contract. Both new business skins ship with zero leaks because every string was driven from DNA on the first pass. The marginal cost is negligible (write the DNA field and the HTML reference in the same commit).
3. **Startup composition pattern: photo-light by design.** The new `startup-saas-landing.html` shows that a dark gradient + product mockup card + typographic manifesto carries the whole above-the-fold mood without any big hero photo. This is a reusable pattern for any future "conversion-first" category that wants to avoid shared-photo pitfalls entirely. Imagery pools become small fallback sets for accent tiles only.
4. **Preview-only worktrees need to seed + migrate + generate from scratch.** The `mw-business-hardening-v2` worktree had no `db.sqlite3` or `media/` on entry. The three-step warm-up (`migrate` → `seed_categories` → `seed_templates` → `generate_previews`) is the standard path; budget for it when spawning a new worktree.
5. **Card-size differentiation is confirmed at card size, not just at full-res preview.** The test that matters is a Chromium walk through the category listing page at 1440×900 with the cards in their real grid context. Both renders individually at 1600×900 might look different, but visual regression at listing scale is what buyers actually see.

### What comes next — Phase 2g2x.1 continuation
Business is closed. The next 4 CRITICO categories remain:
- [ ] **Agency** — vertex + aura (DNA split suggested: `bold-grid` + `editorial-quiet`)
- [ ] **Lawyer** — lex + juris (`classic-gold` + `modern-transparent`)
- [ ] **Real-estate** — casa + villa (`mass-market` + `ultra-luxury-cinematic`)
- [ ] **Portfolio** — chiara + pixel (`editorial-designer` + `cinematic-photographer`)

Each follows the same Session 17 recipe: 2 archetypes + 2 DNA content blocks + 2 D-047-compliant compositions + 2 disjoint imagery pools. No shortcuts. All MEDIO-severity items (2g2x.3 D-047 lifts on single-tenant archetype files, 2g2x.2 medical imagery pool realignment) also remain open. The wave exit criteria in TODO_NEXT.md Phase 2g2x.6 still gate Phase 3.

---

## Session 16 — Catalog Differentiation Hard Audit (2026-04-11)

**Agent:** Audit only — no implementation
**Goal:** Determine whether the catalog's sibling templates are credible distinct products, or whether they're still recolors / identity-crash prototypes. Produce a severe, concrete, blocking-or-not verdict before any further roadmap work.

### Method
1. Read all repo memory files (CLAUDE.md → TEMPLATE_REGISTRY.json)
2. Inventoried every WebTemplate row across 8 categories (20 templates) and matched each to its DNA state + content registry state + archetype tenancy
3. Inspected `apps/catalog/template_dna.py`, `apps/catalog/template_content.py`, `apps/catalog/preview_imagery.py`, `apps/catalog/management/commands/seed_templates.py`
4. Read every `templates/preview_compositions/<category>.html` legacy composition and every `templates/preview_compositions/<category>/<archetype>.html` DNA composition
5. Walked the `templates/live_templates/` tree (only 2 archetypes authored: `medical/specialist/`, `restaurant/fine-dining/`)
6. Grepped for literal brand leaks in every composition file (fine-dining, trattoria-warm, street-modern, clinic, family, wellness, specialist, fashion-editorial, artisan-workshop)
7. Measured imagery-pool URL overlap between sibling pools

### Verdict: **CATALOG NON APPROVABILE — hardening phase bloccante richiesta**

### Severity breakdown
| Category     | Severity  | Templates                                  | Nature |
|--------------|-----------|--------------------------------------------|--------|
| agency       | **CRITICO** | vertex-creative-agency · aura-digital-studio | Sistemico — no DNA, shared `agency.html` con 6 case-study letterali (Lumen, Vega, Atelier Norma, Helios Bank, Cinetic, Polar Studios). Cards are wrong-content, not recolor |
| business     | **CRITICO** | pragma-corporate-suite · elevate-startup-landing | Sistemico — `business.html` hardcodes `"Hanno scelto Pragma"` label, Marco Bianchi/Vectra testimonial, Nordea/Vectra/Finova/Atlas clients. Elevate renders Pragma's copy |
| lawyer       | **CRITICO** | lex-studio-legale · juris-avvocato-moderno | Sistemico — `lawyer.html` hardcodes "Studio legale dal 1962", full 4-area practice grid (societario/famiglia/lavoro/penale), M. Bianchi review. Juris renders Lex's heritage |
| real-estate  | **CRITICO** | casa-agenzia-immobiliare · villa-immobili-lusso | Sistemico — `real-estate.html` hardcodes "600+ immobili", €500K–1.2M price box (mass-market), specific Brera listing. Villa renders mass-market copy |
| portfolio    | **CRITICO** | chiara-portfolio-creativo · pixel-portfolio-fotografico | Sistemico — `portfolio.html` hardcodes "Sono una designer indipendente", "Featured · Atlas Magazine", h1 "Ogni progetto una storia". Pixel (photographer) renders Chiara's designer copy |
| medical      | **MEDIO** | cardio-studio-specialistico · dermatologia-elite-roma | Combinato — DNA system works; Sessions 14+15 closed 17 chrome leaks + 3 preview-comp leaks; BUT (a) `medical-specialist` imagery pool shares 5/6 URLs with `lawyer` pool so both render a lawyer-portrait hero, (b) hero photo is identical for both siblings, (c) `medical-family` pool is 100% URL-overlap with base `medical` pool |
| restaurant   | **MEDIO** (live-only) | gusto (+ latent for sapore/brace) | Live-pages-only — 3 preview compositions are solid, cards read as 3 distinct products. But `live_templates/restaurant/fine-dining/*` has 5 files with Gusto literal leaks (Fioravanti / Brera / Otto atti / Barolo / Selosse / Bresse / Michelin) — Phase 2g.3 already flagged. `trattoria-warm.html` preview comp has "Trastevere · dal 1987 · cucina romana di famiglia" hardcoded |
| ecommerce    | **MEDIO** (latente) | luxe-fashion-store · bottega-shop-artigianale | Preview-only — single-tenant archetypes work at card size via macro-tone split (Session 15). BUT both compositions have massive D-047 violations: `fashion-editorial.html` has 12+ Luxe literals (Carla Sozzani, Giulia Maison, Issue 12, Rack Atelier, Bomber Siena, Milano·Parigi·Tokyo, Grand Hôtel Villa d'Este, "Accedi al lookbook"); `artisan-workshop.html` has 10+ Bottega literals (Firenze·dal 1968, Santa Croce sull'Arno, Montelupo, Prato, "Ceramica"/"Tessitura" nav, "12 botteghe", "Mai sopra 50"). Will detonate the moment Phase 2f.2 adds a second fashion/artisan template |

### Secondary but cross-cutting
- **17/20 templates are preview-PNG-only.** Only cardio, derm (via specialist reuse), and gusto have inner pages. The marketplace sells "completed multipage websites" but delivers single-page posters for 85% of the catalog. The user's concern "il prodotto è fatto di template completi multipagina" is not yet met at catalog level — this is a completeness gap, not just a differentiation gap
- **Stale-PNG timing trap** (recurring class since Sessions 8/10/12/15). No structural fix — TODO_NEXT Phase 2d item 4 still open. Next session that regenerates should plan it
- **Preview-comp and live-template chrome are authored as if archetypes are single-tenant**, even though D-047 was formalized in Session 14 to prevent exactly this. Session 15 confirmed D-047 applies to preview compositions too, but only patched `medical/specialist.html`. The rule is honored only in the files that were audited post-D-047 (specialist chrome + specialist preview comp). Every other per-archetype file predates D-047 and has never been leak-swept

### Root-cause map (technical)
| Source of truth              | Issue                                                                                |
|------------------------------|--------------------------------------------------------------------------------------|
| `apps/catalog/template_dna.py` | Only 10 of 20 templates have DNA. 10 fall through to legacy per-category composition |
| `templates/preview_compositions/agency.html` etc (5 files) | Author-as-prototype literals never lifted to DNA content fields |
| `templates/preview_compositions/ecommerce/fashion-editorial.html` | Authored Session 15 with 12+ literals baked in — violates D-047 |
| `templates/preview_compositions/ecommerce/artisan-workshop.html` | Same class — 10+ literals |
| `templates/preview_compositions/restaurant/trattoria-warm.html` | `Trastevere · dal 1987` hardcoded |
| `templates/preview_compositions/medical/family.html` | `Dr.ssa Rambaldi` hardcoded (latent — single tenant) |
| `templates/live_templates/restaurant/fine-dining/` (8 files) | 5 files have Gusto brand leaks (Phase 2g.3 already planned) |
| `apps/catalog/preview_imagery.py` | Sibling pools 100% URL-overlap (agency/business/lawyer/real-estate/portfolio); `medical-specialist` 5/6 from lawyer pool; `medical-family` 100% from `medical` pool |
| `apps/catalog/template_content.py` | Inner-page content exists for only 3 templates — the live-preview coverage is 15% of the catalog |

### Minimal technical plan (no scope creep)
1. **Phase 2g2x.1 — Legacy-comp lift to D-047.** For each of the 5 non-DNA categories, either (a) split into 2 archetypes with its own composition + DNA entry, OR (b) lift the existing `<category>.html` to parse `dna.content.*` fields and add minimal DNA entries for each tenant. Option (a) is cleaner and matches the medical/restaurant pattern; option (b) is cheaper but requires both tenants to author DNA content. Either way: **no new HTML file needs to be created for any template — existing 5 legacy comps become 5 DNA-driven comps OR become 10 archetype comps**
2. **Phase 2g2x.2 — Imagery pool sibling-split.** For each of the 5 legacy categories, replace the single 6-URL pool with two sibling-distinct pools per Session 10 recipe (`<category>-A` + `<category>-B`, hand-checked via Read for visual distinctness, zero URL overlap)
3. **Phase 2g2x.3 — Lift latent leaks under D-047.** `restaurant/trattoria-warm.html`, `restaurant/street-modern.html`, `medical/family.html`, `medical/clinic.html`, `medical/wellness.html`, `ecommerce/fashion-editorial.html`, `ecommerce/artisan-workshop.html` — grep each for literal brand strings and move them to the DNA `content` block, using Session 14's mechanical recipe
4. **Phase 2g2x.4 — Medical specialist imagery pool.** Replace the lawyer-pool-derived hero photo in `medical-specialist` with a real medical-specialist-appropriate URL set (2 templates × different photo subsets, OR have them share the pool and macro-tone differentiate via accent). Fix `medical-family` pool overlap with base `medical` pool
5. **Phase 2g2x.5 — Single-page template demotion.** Templates with no live inner-page content should either (a) be marked as `draft` / unpublished until their inner pages exist, OR (b) receive inner-page content following the cardio/derm/gusto pattern. This is the "completeness gap" fix. Ship decision: keep them `published` but flag them as "preview-only" with a Coming Soon badge, OR hide them from listing until complete
6. **Phase 2g2x.6 — Stale-PNG structural fix** (TODO_NEXT Phase 2d item 4): add DNA-signature hashing on TemplateAsset so regeneration is automatic

### Categories that MUST be corrected before roadmap resumes
All 5 non-DNA categories (**CRITICO**): agency, business, lawyer, real-estate, portfolio.
Latent-leak fixes for restaurant/ecommerce/medical (**MEDIO**) can be done in a second wave but should not be skipped — they will detonate on reuse.

### What NOT to do yet (hard boundaries)
- No auth / checkout / editor / projects / commerce / dashboard / accounts / cart / stripe work
- No new categories
- No new templates to ANY category
- No new archetypes
- No broad refactors outside this audit scope
- No forced merges to main

### Files modified in Session 16
- `SESSION_LOG.md` — this entry (audit findings)
- `DECISIONS.md` — D-049 added (audit verdict + blocking rule)
- `TODO_NEXT.md` — Phase 2g2x inserted as the blocking wave before any roadmap item
- `AGENT_HANDOFF.md` — Session 16 handoff + "do not resume roadmap" directive
- `CATEGORY_ROADMAP.md` — severity column added per category, DNA-rollout order updated

### Memory files updated (auto-memory)
- `catalog_differentiation_audit.md` (new project memory)
- `MEMORY.md` (pointer added)

---

## Session 15 — Visual Polish & Preview Fixes (2026-04-11)

**Agent:** Visual polish pass
**Goal:** Four concrete product-quality fixes visible directly in the marketplace UI: (1) dermatologia card shows a grey placeholder, (2) restaurant category hero is clipped/unbalanced, (3) Gusto+Sapore still too similar at card size, (4) Luxe+Bottega identical at card size.

### Root causes identified
1. **Missing dermatologia preview.** Session 13's validation run deliberately skipped PNG regeneration ("0 new TemplateAssets — validation is about the live preview, not the thumbnail"). The `dermatologia-elite-roma` WebTemplate row had zero preview assets, so `preview_asset` returned `None` and `_template_card.html` rendered its `mw-img-placeholder` fallback (a grey `bi-window-desktop` icon).
2. **Hidden second leak in the specialist preview composition.** Session 14's copy-abstraction lift covered the 9 `live_templates/medical/specialist/*.html` chrome files but did NOT touch `templates/preview_compositions/medical/specialist.html`. It still hardcoded `Dr. R. Marani`, `Roma · Parioli`, and `SC Cardiologia` in the hero meta + credit blocks. Regenerating the dermatology preview as-is would have rendered the cardiologist's name on the dermatology card.
3. **Restaurant category hero cramped + unbalanced.** `.mw-page-hero` used `padding-top: 7rem` (112px) against a 77px fixed navbar, leaving a 35px gap between navbar bottom and breadcrumb top — too tight for a premium site. `max-width: 36rem` on the subhead made the right side of the hero dead space on wide screens, and no `min-height` meant the hero collapsed to ~330px.
4. **Gusto + Sapore PNGs on disk were stale.** Same timing-trap class that Sessions 8/10/12 fought repeatedly: the files were legacy `restaurant.html` renders from before the Session 10 fix pass redesigned fine-dining as fully dark and trattoria as fully cream. Session 12 claimed to have regenerated them but the fix did not land in this worktree. The DB rows pointed at canonical filenames; the files themselves were old.
5. **Luxe + Bottega had no DNA at all.** Both templates rendered through the single legacy `ecommerce.html` composition that hardcodes every string ("Stile / senza / compromessi", "I più desiderati del mese", identical product names) and pulls from the same imagery pool. The only difference was the brand name in the navbar. Ecommerce was not yet a DNA-pilot category.

### Actions taken

**Fix 1 — Dermatologia preview**
- Added `hero_meta`, `credit_left`, `credit_right` fields to BOTH `cardio-studio-specialistico` and `dermatologia-elite-roma` DNA `content` blocks in `apps/catalog/template_dna.py`. Derm: `Dr.ssa L. Ricciardi / 18 anni / 2.400+ pazienti · Studio Roma · Via Veneto · Specialità Dermatologia`. Cardio: unchanged semantics, just moved from literals to DNA fields.
- Updated `templates/preview_compositions/medical/specialist.html` to loop over `dna.content.hero_meta` and read `dna.content.credit_left.0/1` + `credit_right.0/1` — zero cardio literals left in the composition.
- Ran `python manage.py generate_previews --only dermatologia-elite-roma` → new canonical `dermatologia-elite-roma-preview.png` lands with the correct dermatology brand/city/specialty.
- Regenerated cardio too (clean-delete recipe: remove DB row + canonical file + orphan suffix file, then re-run without `--force`) to verify the composition change didn't regress cardio rendering. **It didn't** — identical output.

**Fix 2 — Restaurant category hero**
- Rewrote `.mw-page-hero` in `static/css/components.css`:
  - `padding-top: calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` — generous 64px clearance from navbar bottom to breadcrumb top (was 35px)
  - `padding-bottom: var(--mw-space-10)` — 80px (was 48px)
  - `min-height: 22rem` — hero no longer collapses on short copy
  - `display: flex; flex-direction: column; justify-content: center` — vertical centering inside the generous box
  - Subhead `max-width: 46rem` (was 36rem) — eats more of the wide-screen hero so the right isn't dead
  - H1 now `clamp(3xl, 3.8vw, 5xl)` — responsive at wide breakpoints
  - Background adds two radial gradients (indigo top-right + amber bottom-left) and `overflow: hidden` — subtle depth instead of flat dark
  - `position: relative` + `.mw-page-hero > .container { position: relative; z-index: 1 }` — decorative overlays don't swallow content
- Measured after: navbar→breadcrumb gap = 64px (was 35px), hero height = 373px (was 330px), no dead pixel regions on wide viewport.

**Fix 3 — Gusto / Sapore differentiation**
- Clean-delete recipe applied to both: remove asset row, remove canonical file, remove any orphan-suffix file, re-run `generate_previews --only <slug>` without `--force`.
- Confirmed the DNA-path `restaurant/fine-dining.html` + `restaurant/trattoria-warm.html` compositions from Session 10 render correctly. Generated PNGs:
  - **Gusto** — fully DARK charcoal page, italic Playfair "Una serata in otto atti", single full-bleed plated-dish hero photo, gold dotted-leader numbered course index over black with "€ 180 / persona".
  - **Sapore** — fully BRIGHT cream page, two tilted polaroid photos, handwritten Caveat "Da Nonna Rosa, come a casa vostra", red+green cream recipe card with weekly specials, no dark regions.
- With Brace (yellow brutalist) unchanged, the three restaurant cards now occupy three opposite ends of the visual spectrum: **YELLOW / CREAM / DARK**. Instantly distinguishable at card size.

**Fix 4 — Luxe / Bottega differentiation (NEW ecommerce DNA pilot)**
- Added 2 archetypes to `LAYOUT_ARCHETYPES` in `template_dna.py`: `fashion-editorial` (Luxe) and `artisan-workshop` (Bottega).
- Added DNA registry entries for both templates with archetype, font pairing, and minimal content block (compositions read the headline + eyebrow only; no further leaks possible since every other string is either a CSS rule or a generic archetype label per D-047).
- Authored two new compositions:
  - `templates/preview_compositions/ecommerce/fashion-editorial.html` — fully DARK #08070a ink charcoal page, gold #B8860B accents, italic Cormorant Garamond 108px "Il nuovo corpo del vestire", fashion-model full-bleed cover left, issue tag + styling credit + 4-up editorial product strip with gold price labels at bottom. Uses the existing `ecommerce` imagery pool, indices reassigned: hero=0 (fashion model), tiles=5,4,3,0.
  - `templates/preview_compositions/ecommerce/artisan-workshop.html` — fully BRIGHT #f6ecd8 cream page with subtle grain/pattern background, terracotta accent, huge Libre Baskerville 108px "Pezzi unici cuciti & fatti in bottega" with orange italic emphasis, rubber-stamped info panel rotated 0.8deg with bottega specs, 4-up labeled edition cards at bottom (each with N° number, edition numerator/denominator, artisan provenance, pezzo-unico tag). NO hero photo — typographic-led. Uses the same `ecommerce` pool for the 4 small product tiles. At card size, zero hero photo overlap with Luxe.
- Regenerated both PNGs. Deliberate macro tone choice applies Session 10's core lesson: sibling templates must differ at PAGE LEVEL, not just in accent details. Luxe = black. Bottega = cream. Instantly distinguishable.

**Orphan file cleanup (housekeeping)**
- Session 12 left 4 orphan-suffixed preview files on disk with DB rows pointing to them (`_5utrvms`, `_iasDI4Y`, `_yYaOuCE`, `_wWIztM1`). Renamed each orphan to its canonical name and updated the DB row so each template has one file with one canonical name. Zero orphan files now exist in `media/template_assets/2026/04/`.

### Validation

1. **`python manage.py check` — clean** (run twice: after DNA edits, after composition edits).
2. **37-route regression sweep via Django test client:**
   - Homepage, full template list, 5 category pages (medical, restaurant, ecommerce, lawyer, agency)
   - 10 template detail pages (all 5 medical + all 3 restaurant + both ecommerce)
   - 7 cardio live preview pages
   - 7 dermatologia live preview pages
   - 6 gusto live preview pages
   - **All 37 return 200.**
3. **Cardio-leak audit on dermatology pages — re-ran.** Grepped rendered HTML of all 7 dermatologia inner pages for 9 cardio literals (`Marani`, `Parioli`, `OMCeO Roma 12 / 4408`, `Cardiologia`, `ecocardiograf`, `Visita cardiologica`, `LANCET`, `European Heart`). **All 7 pages clean.** The specialist chrome stays clean after the preview-composition edit.
4. **Visual verification via Playwright-driven Chromium:**
   - Homepage featured grid shows new Gusto composition (dark editorial).
   - `/templates/restaurant/` shows Brace/Sapore/Gusto as three obviously different products. Hero is no longer clipped, has 64px navbar clearance and generous breathing room.
   - `/templates/medical/` shows all 5 medical templates with valid previews (no grey placeholder for dermatology).
   - `/templates/ecommerce/` shows Luxe (dark fashion) and Bottega (cream artisan) instantly distinguishable.

### Files modified (Session 15)
- `apps/catalog/template_dna.py` — +2 archetypes (`fashion-editorial`, `artisan-workshop`), +2 DNA entries (luxe, bottega), +3 fields on each specialist DNA (`hero_meta`, `credit_left`, `credit_right`)
- `templates/preview_compositions/medical/specialist.html` — literals → DNA field reads
- `templates/preview_compositions/ecommerce/fashion-editorial.html` — NEW file (Luxe archetype)
- `templates/preview_compositions/ecommerce/artisan-workshop.html` — NEW file (Bottega archetype)
- `static/css/components.css` — `.mw-page-hero` redesigned (padding, min-height, gradients, relative positioning)
- `media/template_assets/2026/04/dermatologia-elite-roma-preview.png` — NEW preview (was missing)
- `media/template_assets/2026/04/cardio-studio-specialistico-preview.png` — regenerated (same visual, now from DNA fields)
- `media/template_assets/2026/04/gusto-fine-dining-preview.png` — regenerated (now fully dark fine-dining)
- `media/template_assets/2026/04/sapore-trattoria-pizzeria-preview.png` — regenerated (now fully cream trattoria)
- `media/template_assets/2026/04/luxe-fashion-store-preview.png` — regenerated from new fashion-editorial archetype
- `media/template_assets/2026/04/bottega-shop-artigianale-preview.png` — regenerated from new artisan-workshop archetype
- 4 orphan-suffixed files renamed back to canonical

### Lessons from Session 15

- **"Validation skipped the thumbnail" is a user-facing bug.** Session 13 explicitly deferred PNG regeneration when adding Dermatologia, reasoning that validation was about the live preview not the marketplace card. But the marketplace card is the FIRST thing a buyer sees — a grey placeholder on a card is a broken product. Any future archetype-reuse add must regenerate the preview as the final step, no exceptions.
- **Per-archetype compositions need the same copy-abstraction contract (D-047) as live-template chrome.** Session 14 lifted `templates/live_templates/medical/specialist/*.html` but left `templates/preview_compositions/medical/specialist.html` with 3 cardio literals. Any time two templates share an archetype, the PREVIEW composition is as much chrome as the live template is — it needs the same rule: every string is either a CSS rule, a generic archetype label, a DNA content field, or a loop item. Never a literal brand name, city, or specialty.
- **Macro tone trumps imagery at card size, AGAIN.** Luxe and Bottega share the exact same `ecommerce` imagery pool (zero URL changes in `preview_imagery.py`) yet at card size they look radically different because one composition is fully BLACK and the other is fully CREAM. The compositions differ in page background, font family, hero structure (photo-led vs typographic-led), and accent color. Session 10 was right: fighting over imagery distinctness is expensive (URL hunting, HTTP 404s, hand-verification); controlling macro tone is free and does more of the visual work.
- **Stale PNGs are a recurring class of bug.** Sessions 8, 10, 12, 15 all independently hit the timing trap where a DNA change left the old preview on disk with a DB row pointing at it. Session 12's `WebTemplate.preview_asset` property fixed the read side but not the write side. The proper structural fix (from TODO_NEXT Phase 2d) is still unimplemented: either auto `--force` when DNA mtime > asset file mtime, or hash the DNA into the asset row and compare on every run. Until then, the clean-delete recipe (remove row + canonical file + orphan suffix, re-run without `--force`) is the only reliable path.
- **`position: fixed` navbar + `padding-top: Xrem` on hero is a hidden coupling.** 7rem looked fine with a 64px navbar but became cramped once the navbar grew to 77px. Encoded it as `calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` so a future navbar resize stays coupled explicitly. Long-term: measure the navbar height via JS on page load and expose as CSS variable.

### What's next

See TODO_NEXT.md Phase 2g.3 (fine-dining copy lift) + Phase 2f.2 (ecommerce DNA expansion — add at least one more fashion and one more artisan template to validate the two new archetypes for reuse, same way derm validated specialist).

---

## Session 1 — Orchestrator Bootstrap (2026-04-09)

**Agent:** Orchestrator
**Goal:** Inspect repo, define architecture, create all coordination files, prepare for parallel workstreams.

### Actions Taken
1. Inspected repository — fresh Django 5.2.7 scaffold, no commits, no apps, no requirements.txt
2. Discovered actual environment: Python 3.13.5, Django 5.2.7 (not 6.0.4), rich package set including DRF, Stripe, Celery, Pillow, crispy-bootstrap5
3. Designed 7-app modular architecture (core, accounts, catalog, editor, projects, commerce, pages)
4. Established services/selectors pattern for business logic
5. Created all coordination files:
   - CLAUDE.md — project guidance for Claude Code
   - ARCHITECTURE.md — app structure, layered pattern, URL scheme, frontend/static layout
   - DECISIONS.md — 10 architectural decisions documented
   - TODO_NEXT.md — prioritized task lists for both workstreams
   - CATEGORY_ROADMAP.md — 8 MVP categories + post-MVP expansion
   - CONTENT_GUIDELINES.md — writing style per category, brand identity rules
   - BRAND_SYSTEM_GUIDELINES.md — visual design system specification
   - AGENT_HANDOFF.md — clear instructions for backend-core and premium-ui
   - TEMPLATE_REGISTRY.json — empty registry scaffold
   - SESSION_LOG.md — this file
6. Prepared phased implementation roadmap (5 phases, MVP first)
7. Set up requirements.txt with pinned core dependencies

### Files Created
- CLAUDE.md
- ARCHITECTURE.md
- DECISIONS.md
- TODO_NEXT.md
- CATEGORY_ROADMAP.md
- CONTENT_GUIDELINES.md
- BRAND_SYSTEM_GUIDELINES.md
- AGENT_HANDOFF.md
- TEMPLATE_REGISTRY.json
- SESSION_LOG.md
- requirements.txt

### Key Decisions Made
- D-001 through D-010 (see DECISIONS.md)
- Most critical: Custom User model must be created BEFORE first migrate

### Next Steps
- **Backend-core:** Create app scaffolds, custom User model, core base models, catalog models, admin — see AGENT_HANDOFF.md
- **Premium-UI:** Create design system, base template, homepage, navigation, card components — see AGENT_HANDOFF.md

## Session 2 — Premium UI Phase 1 (2026-04-09)

**Agent:** Premium-UI
**Goal:** Build the complete frontend foundation — design system, templates, components, and listing pages.

### Actions Taken
1. Created `templates/` directory structure: base.html, includes/, pages/, catalog/
2. Created `static/` directory structure: css/, js/, images/brand/
3. Updated `settings.py`: added TEMPLATES DIRS and STATICFILES_DIRS (minimal Python change)
4. Built **design-system.css** — full CSS custom properties system: colors (primary/secondary/accent/neutrals), typography scale (1.25 ratio, Plus Jakarta Sans + Inter), spacing (8px base), shadows, transitions, buttons, badges, dividers, utility classes
5. Built **components.css** — navbar (fixed, backdrop-blur, mobile slide-out), template card (hover lift/shadow/image zoom), category card (icon animate on hover), hero section, stats bar, footer, filter bar, detail page components, breadcrumbs, tags
6. Built **pages.css** — homepage-specific styles, featured/category/listing grids, steps section, testimonials, detail tabs, empty state
7. Built **base.html** — Bootstrap 5.3 CDN, Google Fonts, design system CSS, RTL-ready lang/dir attributes, semantic blocks
8. Built **_navbar.html** — sticky navbar with brand mark, desktop nav links, CTA buttons, mobile hamburger with slide-out menu + overlay
9. Built **_footer.html** — 5-column layout (brand, marketplace, categories, support, company), social icons, copyright
10. Built **_hero.html** — reusable hero component with configurable content
11. Built **_template_card.html** — reusable card with dynamic model fields (image, category badge, brand name, title, description, price, hover actions)
12. Built **_category_card.html** — reusable card with icon, name, template count
13. Built **pages/home.html** — full homepage: hero, trust bar (stats), 8 category cards, 6 featured template cards, 3-step how-it-works, 3 testimonials, gradient CTA section. All content in Italian, no lorem ipsum.
14. Built **catalog/category_list.html** — page hero + breadcrumb + category grid with static fallback
15. Built **catalog/template_list.html** — page hero + breadcrumb + filter bar (search/category/sort) + template grid + pagination placeholder
16. Built **catalog/template_detail.html** — breadcrumb, gallery, tabbed description/features/reviews, sticky sidebar (price, CTA, meta info, tags), related templates section
17. Built **main.js** — navbar scroll effect (requestAnimationFrame), mobile menu open/close with overlay, Escape key close, responsive resize handler

### Files Created (14 new files)
- `static/css/design-system.css` — 290 lines, full design system
- `static/css/components.css` — 430 lines, all component styles
- `static/css/pages.css` — 190 lines, page-specific styles
- `static/js/main.js` — 70 lines, navbar + mobile menu
- `templates/base.html` — master template
- `templates/includes/_navbar.html` — sticky navbar with mobile menu
- `templates/includes/_footer.html` — multi-column footer
- `templates/includes/_hero.html` — reusable hero section
- `templates/includes/_template_card.html` — template listing card
- `templates/includes/_category_card.html` — category card
- `templates/pages/home.html` — full homepage
- `templates/catalog/category_list.html` — category listing
- `templates/catalog/template_list.html` — template listing with filters
- `templates/catalog/template_detail.html` — template detail with sidebar

### Files Modified (1 file)
- `marketweb/settings.py` — added TEMPLATES DIRS and STATICFILES_DIRS

### Key Design Decisions
- D-011: `mw-` CSS prefix for all custom classes to avoid Bootstrap collisions
- D-012: Plus Jakarta Sans for headings, Inter for body — premium Google Font pairing
- D-013: CSS custom properties (not SCSS) for zero-build-step development
- D-014: All template cards include dynamic model field references compatible with backend-core models
- D-015: Static fallback content in listing pages for development without backend data
- D-016: Italian content throughout, formal "Lei" register, no lorem ipsum

### Next Steps
- Wire category card href attributes to actual URL routes when backend views are ready
- Replace placeholder images with real template screenshots
- Add RTL bundle switching logic (detect lang=ar, swap Bootstrap CSS)
- Build accounts/ and commerce/ templates (login, register, cart, checkout)
- Connect template_card to real WebTemplate queryset data

## Session 3 — UI Integration Fix & Polish (2026-04-09)

**Agent:** Premium-UI
**Goal:** Diagnose and fix navbar duplication and layout breakage after backend/UI merge. Polish visual output.

### Root Cause Found
**Bootstrap 5.3.3 CSS failed to load due to an incorrect SRI integrity hash** in `base.html`. The `<link>` tag was present with the correct href, but the browser rejected the file because the `sha384-...` hash didn't match the actual file content from jsdelivr CDN. This meant:
- **Zero Bootstrap CSS loaded** — no grid system, no responsive utilities, no component styles
- `d-lg-none` had no effect → mobile slide-out menu rendered visibly on desktop = **duplicate navbar**
- `.container`, `.row`, `.col-*` had no effect → broken grid layouts throughout
- `d-none d-lg-flex` had no effect → desktop nav links and mobile elements all visible simultaneously

The Bootstrap JS bundle had the same SRI hash issue.

### Actions Taken
1. Used Playwright to inspect the running page — confirmed `display: block` on the mobile menu element that should have been `display: none` via `d-lg-none`
2. Enumerated loaded stylesheets — discovered Bootstrap CSS completely absent (only 5 sheets: Google Fonts, Bootstrap Icons, and 3 custom CSS files)
3. Confirmed `link.sheet === null` (failed load) while `link.href` was correct — pointed to SRI hash mismatch
4. Updated Bootstrap CDN from 5.3.3 (bad SRI) to **5.3.8** (current, correct SRI hashes) for both CSS and JS
5. Verified fix: Bootstrap loaded, `d-lg-none` works, mobile menu hidden, grid system functional
6. **Polish fixes:**
   - Category grid: changed from `auto-fill, minmax(180px)` to `repeat(4, 1fr)` for balanced 4+4 layout
   - Hero padding: consolidated padding-top (7rem for navbar clearance) and added bottom padding
   - Typography: added explicit `margin-top: 0` on headings to prevent Bootstrap reboot conflicts
   - Links: added `!important` on `text-decoration: none` to override Bootstrap's reboot link underlines
   - Card title: added `!important` on font-size to prevent global h3 size from overriding card context
   - `_hero.html` partial: removed `mw-home-hero` class (should be generic, not page-specific)

### Files Modified (5 files)
- `templates/base.html` — Bootstrap CDN 5.3.3→5.3.8 with correct SRI hashes (CSS + JS)
- `static/css/design-system.css` — Link `text-decoration: none !important`, heading `margin-top: 0`
- `static/css/components.css` — Hero `padding-bottom`, card title `font-size !important`
- `static/css/pages.css` — Category grid `repeat(4, 1fr)` with responsive breakpoints, hero padding
- `templates/includes/_hero.html` — Removed `mw-home-hero` class from generic partial

### Key Takeaway
The entire "duplicate navbar" and "broken layout" was a single root cause: **bad SRI hash on Bootstrap CDN link**. No template inheritance issues, no duplicate includes — the HTML structure was always correct.

## Session 4 — Catalog Integration Phase 1 (2026-04-09)

**Agent:** Catalog Integration
**Goal:** Connect the premium UI templates to real database-backed querysets. Implement catalog views, selectors, URLs, seed data, and wire all pages to real Category and WebTemplate models.

### Actions Taken
1. **Fixed seed_categories.py** — Removed `bi-` prefix from icon field (partial already adds it), updated category names to Italian display names (Ristorante, Medico, Avvocato, Immobiliare), enriched descriptions
2. **Created `apps/catalog/selectors.py`** — 7 selector functions: `get_active_categories`, `get_active_categories_with_counts`, `get_published_templates`, `get_featured_templates`, `get_templates_by_category`, `get_template_detail`, `get_related_templates`
3. **Created `apps/catalog/views.py`** — `CategoryListView`, `TemplateListView` (with optional category filtering via URL kwarg), `TemplateDetailView` with related templates
4. **Wired `apps/catalog/urls.py`** — 4 URL patterns: `/templates/` (all), `/templates/categories/` (category list), `/templates/<category_slug>/` (filtered), `/templates/<category_slug>/<slug>/` (detail)
5. **Updated `apps/pages/views.py`** — `HomePageView` now passes `categories` (with annotated counts) and `featured_templates` (limit=6) to context
6. **Updated `templates/pages/home.html`** — Replaced 8 hardcoded category cards with `{% for category in categories %}` loop using `_category_card.html` partial. Replaced 6 hardcoded template cards with `{% for tmpl in featured_templates %}` loop using `_template_card.html` partial. Updated hero CTA and "Vedi Tutti" links to `{% url 'catalog:template_list' %}`
7. **Updated `templates/includes/_category_card.html`** — Added real URL via `{% url 'catalog:template_list_by_category' category.slug %}`, updated count to use annotated `template_count`
8. **Updated `templates/includes/_template_card.html`** — Added real URLs to card title, "Scopri" button, and eye preview action via `{% url 'catalog:template_detail' template.category.slug template.slug %}`. Added `floatformat:0` to price display
9. **Updated `templates/catalog/template_detail.html`** — Fixed breadcrumb links (Template → `/templates/`, Category → `/templates/<slug>/`), wired related templates section with `{% for %}` loop
10. **Updated `templates/catalog/template_list.html`** — Replaced static fallback with dynamic `{% for %}` + `{% empty %}` pattern, made category dropdown dynamic with `onchange` navigation, fixed breadcrumbs
11. **Updated `templates/catalog/category_list.html`** — Removed static fallback, uses dynamic `{% for %}` loop
12. **Updated `templates/includes/_navbar.html`** — Wired "Template" and "Categorie" nav links to real URLs (both desktop and mobile)
13. **Created `apps/catalog/management/commands/seed_templates.py`** — 16 realistic WebTemplate + TemplateBrand entries across all 8 MVP categories (2 per category), matching homepage copy exactly (Vertex Studio, Osteria Moderna, SaluteVita Clinic, Chiara Studio, Pragma Corp, Studio Legale Ferri)
14. **Seeded database** — 8 categories + 16 templates with brands, all status=published, 6 featured

### Files Created (3 new files)
- `apps/catalog/selectors.py` — 7 selector functions for catalog reads
- `apps/catalog/views.py` — 3 class-based views (CategoryList, TemplateList, TemplateDetail)
- `apps/catalog/management/commands/seed_templates.py` — 16 templates with brand identities

### Files Modified (8 files)
- `apps/catalog/urls.py` — 4 URL patterns (was empty)
- `apps/catalog/management/commands/seed_categories.py` — Italian names, fixed icons, richer descriptions
- `apps/pages/views.py` — HomePageView now passes real querysets
- `templates/pages/home.html` — Dynamic category and featured template loops
- `templates/includes/_category_card.html` — Real URLs and annotated counts
- `templates/includes/_template_card.html` — Real URLs and formatted prices
- `templates/includes/_navbar.html` — Real URLs for Template and Categorie links
- `templates/catalog/template_detail.html` — Fixed breadcrumbs, wired related templates
- `templates/catalog/template_list.html` — Dynamic data, dynamic filter dropdown
- `templates/catalog/category_list.html` — Removed static fallback

### Key Decisions
- D-017: Category names in Italian for display, English slugs for URLs
- D-018: Two-segment URL for detail (`/<category>/<slug>/`) to avoid slug collisions across categories
- D-019: Selectors return querysets (not lists) to allow further filtering and pagination
- D-020: Icon field stores Bootstrap icon name without `bi-` prefix (partial adds the prefix)

### Verified Pages (Playwright)
- `http://127.0.0.1:8099/` — Homepage: 8 categories with counts, 6 featured templates, all links working
- `http://127.0.0.1:8099/templates/` — All 16 templates, dynamic category dropdown, breadcrumbs
- `http://127.0.0.1:8099/templates/agency/` — Filtered to 2 agency templates, correct title and description
- `http://127.0.0.1:8099/templates/agency/vertex-creative-agency/` — Full detail page with breadcrumbs, related templates
- `http://127.0.0.1:8099/templates/categories/` — All 8 categories with counts and links

## Session 5 — Catalog Enhancements Phase 1 (2026-04-09)

**Agent:** Catalog Enhancements (worktree: catalog-enhancements)
**Goal:** Add template preview images, search, sort, and pagination to the catalog listing page.

### Actions Taken
1. **Created `generate_previews.py` management command** — Generates branded SVG mockup images for all published templates. Each SVG is a 1200x675 (16:9) website mockup with browser chrome (traffic lights + URL bar), navbar, hero section, content cards, and footer — all colored using the template's brand palette. Two layout variants (split-hero and centered-hero) alternate for visual variety.
2. **Updated `selectors.py`** — Added `prefetch_related("assets")` to `get_published_templates()` to eliminate N+1 queries on listing pages. Added `get_listing_templates()` for combined search/sort/filter with keyword-based search across name, description, short_description, and brand_name. Added `SORT_OPTIONS` and `SORT_LABELS` dictionaries for sort configuration.
3. **Updated `views.py`** — Added `paginate_by = 12` to `TemplateListView`. Replaced separate category/queryset logic with `get_listing_templates()`. Added `search_query`, `current_sort`, `sort_options`, and `filter_query_string` to template context.
4. **Updated `template_list.html`** — Wrapped filter bar in `<form method="get">`. Search input now submits as `?q=` param and preserves value. Sort dropdown submits form on change. Category dropdown preserves search/sort params when navigating. Pagination uses `page_obj` with page number links and preserves all filter params. Empty state shows search query feedback and "Cancella ricerca" button. Template count uses `paginator.count` for accurate total.
5. **Generated 16 preview assets** — Ran `generate_previews` command, creating TemplateAsset records (type=preview) for all 16 templates. SVGs stored in `media/template_assets/2026/04/`.

### Files Created (1 new file)
- `apps/catalog/management/commands/generate_previews.py` — SVG preview generator with 2 layout variants

### Files Modified (3 files)
- `apps/catalog/selectors.py` — Added asset prefetch, `get_listing_templates()`, sort constants
- `apps/catalog/views.py` — Added pagination, search/sort handling, filter context
- `templates/catalog/template_list.html` — Form-based filter bar, working pagination, empty state

### Key Decisions
- D-022: SVG-based preview images using brand palettes (not Pillow PNGs or CSS-only placeholders)
- D-023: Search uses Django ORM `icontains` across 4 fields (name, short_description, description, brand_name)
- D-024: Sort options: recent, price asc/desc, name A-Z (no "popular" — no view count model yet)
- D-025: Pagination at 12 per page (4 rows of 3 on desktop)

### Verified Pages (Playwright)
- `http://127.0.0.1:8098/` — Homepage with SVG preview images in featured cards
- `http://127.0.0.1:8098/templates/` — 16 templates, pagination (page 1 of 2), filter bar
- `http://127.0.0.1:8098/templates/?q=studio&sort=price_asc` — Search returns 7 results, sorted by price
- `http://127.0.0.1:8098/templates/?q=zzzznotfound` — Empty state with feedback and clear button
- `http://127.0.0.1:8098/templates/restaurant/` — Category filter: 2 restaurant templates
- `http://127.0.0.1:8098/templates/restaurant/gusto-fine-dining/` — Detail page with SVG gallery image

## Session 6 — Real Preview Assets Phase 2 (2026-04-10)

**Agent:** Real Preview Assets (worktree: real-preview-assets)
**Goal:** Replace abstract SVG previews with realistic image-based homepage screenshots so each template card actually communicates the look-and-feel of a real website.

### Problem
Phase 1 SVG previews (and the unreleased "preview-realism phase 1" 8-layout SVGs) still felt like wireframes. They communicated category at best, but never visual richness. Buyers cannot judge a template marketplace from grey rectangles.

### Pipeline
1. **Curated stock imagery library** (`apps/catalog/preview_imagery.py`)
   - `IMAGERY_CONFIG`: 8 categories × 6 Unsplash CDN URLs each (hero, feature, 4 cards)
   - `ensure_cached(category_slug)` downloads + caches to `media/preview_imagery/<category>/<sha>.jpg`
   - Subsequent runs hit local files; nothing leaves the machine
   - Swap images/sources later by editing the config — no other code changes needed

2. **HTML preview compositions** (`templates/preview_compositions/*.html`)
   - One template per MVP category: `restaurant`, `medical`, `lawyer`, `agency`, `business`, `real-estate`, `portfolio`, `ecommerce`
   - Shared `_base.html` with brand-palette CSS variables, Google Fonts (heading + body), 1600×900 fixed viewport, navbar/button utilities
   - Each composition is a believable homepage: hero with photo+headline+CTA, content grid (menu/services/practice areas/products/listings/case studies), realistic Italian copy, brand color injected via context vars
   - All copy in Italian (D-016)

3. **Playwright generator rewrite** (`apps/catalog/management/commands/generate_previews.py`)
   - **Three-phase pipeline** to avoid Django ORM ↔ Playwright sync-loop conflicts:
     - Phase A — materialise queryset, render HTML strings, gather imagery cache (all ORM access)
     - Phase B — open Chromium, navigate to each rendered HTML temp file via `file://`, screenshot 1600×900 at `device_scale_factor=2`
     - Phase C — persist `TemplateAsset` rows pointing at the new PNG files
   - `--force` regenerates and replaces; `--only <slug>` targets a single template
   - Heading/body Google Font pair derived from `TemplateBrand.typography` (with sensible fallbacks for paid fonts like Satoshi → Manrope)
   - Auto-darkens primary, computes contrast text colour via WCAG-ish luminance, pads imagery list so missing slots fall back gracefully

### What changed under the hood
| Layer            | Before                                  | After                                                       |
|------------------|-----------------------------------------|-------------------------------------------------------------|
| Asset format     | Inline SVG wireframe                    | 1600×900 PNG screenshot of real HTML                       |
| Photo content    | None (colored rectangles)               | Real Unsplash photos: restaurants, doctors, justice, …     |
| Layout source    | String-formatted SVG in Python          | Django HTML templates per category                          |
| Brand fidelity   | Palette only                            | Palette + typography pair + accent contrast                |
| Reproducibility  | Deterministic Python                    | Cached images + headless Chromium screenshot               |

`TemplateAsset` model and `template.assets.first.file.url` template usage are unchanged — the pipeline swap is invisible to the rest of the app.

### Files Created (11)
- `apps/catalog/preview_imagery.py` — imagery config + cache helper
- `templates/preview_compositions/_base.html` — shared chrome + brand vars
- `templates/preview_compositions/restaurant.html`
- `templates/preview_compositions/medical.html`
- `templates/preview_compositions/lawyer.html`
- `templates/preview_compositions/agency.html`
- `templates/preview_compositions/business.html`
- `templates/preview_compositions/real-estate.html`
- `templates/preview_compositions/portfolio.html`
- `templates/preview_compositions/ecommerce.html`
- `media/preview_imagery/<category>/*.jpg` — 47 cached stock photos (gitignored)

### Files Modified (1)
- `apps/catalog/management/commands/generate_previews.py` — full rewrite (HTML + Playwright pipeline)

### Verified (Playwright MCP, port 8096)
- `/` — Homepage featured grid: all 6 cards now show real-imagery previews (restaurant interior + food, lady justice + practice areas, doctor + service cards, dark agency case studies, corporate hero, portfolio gallery)
- `/templates/` — Listing grid renders the same PNGs in 12-per-page paginator
- `/templates/restaurant/gusto-fine-dining/` — Detail page gallery shows the Gusto preview, related templates section shows Sapore preview

### Key Decisions
- D-029: HTML compositions + Playwright screenshots (replace pure-SVG)
- D-030: Per-category compositions (not per-template) — keeps template count down, brand differentiation via palette/typography
- D-031: Cache-first imagery via Unsplash CDN URLs in a swappable config
- D-032: Three-phase command (ORM → Playwright → ORM) to avoid SynchronousOnlyOperation
- D-033: PNG output at 1600×900 with 2× device scale factor (~4 MB/file, ~70 MB total)

### Known limitations / next steps
- Both ecommerce templates currently share the same product photos because compositions are per-category. Brand differentiation is visible via palette/typography but the photos are identical. To fully personalise per template, add an optional `imagery_overrides` dict on `TemplateBrand` and merge it into the context. (Same applies to all other category-pairs.)
- Cormorant Garamond hero text on dark backgrounds (lawyer, villa) renders thin. Either bump brand-specific font weight or swap to a heavier serif when the brand pairing requires it.
- File sizes are large (~4 MB each at 2× DPI). For production we should pipe screenshots through PIL JPEG compression or Pillow `optimize=True` PNG to bring per-card download under 500 KB.

## Session 7 — Template DNA System Phase 1 (2026-04-10)

**Agent:** Template DNA System (worktree: template-dna-system)
**Goal:** End the "two templates in the same category look like recolors of each other" problem. Replace the per-category preview composition with a per-template DNA system, prove it on the Medical category with 4 genuinely distinct archetypes.

### Problem
After Phase 2c (real preview assets), each category had ONE HTML composition. Two medical templates differed only by palette + Google Font pair, which is not enough to credibly sell them as separate products in a premium marketplace. Sibling templates collapsed into recolors of the same skeleton.

### Solution: Template DNA
Each template now has a structured "DNA" record (in code, keyed by slug) that drives a unique HTML composition. The DNA captures **layout archetype**, hero/navbar/footer style, section order, card style, button style, density, tone of copy, conversion pattern, font pairing, and per-archetype imagery key — i.e. all the dimensions a buyer would use to perceive a template as its own product.

Templates without a DNA entry fall back to the legacy per-category composition, so the system is strictly additive — adding DNA never breaks existing previews.

### Architecture
```
apps/catalog/template_dna.py
  ├── Vocabulary dicts (LAYOUT_ARCHETYPES, HERO_STYLES, NAVBAR_STYLES, ...)
  ├── TEMPLATE_DNA: dict[slug, dna] — the registry
  └── get_dna(slug), has_dna(slug)

apps/catalog/templatetags/preview_extras.py
  └── `at` filter — safe sequence index lookup so compositions can loop
      and pull `{{ imagery|at:forloop.counter }}` per card

apps/catalog/preview_imagery.py
  └── 3 new keys: medical-family, medical-specialist, medical-wellness
      (each draws from a curated mix of already-cached Unsplash URLs so
      every archetype gets a distinct photo set)

apps/catalog/management/commands/generate_previews.py
  ├── _resolve_composition(template, dna): picks
  │     preview_compositions/<category>/<archetype>.html
  │     when DNA exists, falls back to legacy <category>.html otherwise
  ├── pre-warms imagery by *imagery_key* (not just category) so sibling
  │     templates pull from different pools
  └── DNA's `font_pairing` overrides brand.typography parsing

templates/preview_compositions/medical/
  ├── clinic.html      — institutional split-hero + booking widget + 4-up icons
  ├── family.html      — pastel pill nav + organic-shape portrait + intro trio + hours strip
  ├── specialist.html  — minimal serif nav + huge editorial headline + drop cap + 01/02 fields + press band
  └── wellness.html    — full-bleed hero + glass pill nav + dotted-leader pricelist + therapists strip
```

### What now makes templates within Medical truly different
| Slug                            | Archetype  | Hero               | Navbar         | Cards            | Conversion       | Tone           |
|---------------------------------|------------|--------------------|----------------|------------------|------------------|----------------|
| salute-studio-medico            | clinic     | split-booking      | solid-phone    | icon-grid 4-up   | booking-widget   | institutional  |
| benessere-centro-olistico       | wellness   | full-bleed         | pill-floating  | pricelist        | calendar-spot    | serene         |
| famiglia-pediatria (NEW)        | family     | centered-soft      | soft-pastel    | portrait-stack   | phone-and-chat   | warm-family    |
| cardio-studio-specialistico (NEW) | specialist | editorial-serif    | minimal-serif  | editorial-large  | private-request  | prestigious    |

These four are not recolors. They differ in: page background colour family, navbar shape and position, hero composition (split vs centered vs editorial vs full-bleed), card stride (4-up icon vs 3-up portrait vs 2-up serif vs 2-col pricelist), button shape (rounded vs pill vs ghost-underline), density (medium → very-airy), and copy tone (institutional → warm → prestigious → serene).

### Files Created (8)
- `apps/catalog/template_dna.py` — DNA registry + vocabulary
- `apps/catalog/templatetags/__init__.py`
- `apps/catalog/templatetags/preview_extras.py` — `at` filter
- `templates/preview_compositions/medical/clinic.html`
- `templates/preview_compositions/medical/family.html`
- `templates/preview_compositions/medical/specialist.html`
- `templates/preview_compositions/medical/wellness.html`
- (no schema migration — DNA is a Python registry, not a model field)

### Files Modified (3)
- `apps/catalog/preview_imagery.py` — 3 new imagery keys (medical-family, medical-specialist, medical-wellness)
- `apps/catalog/management/commands/generate_previews.py` — DNA-aware composition resolver, per-template imagery_key, font_pairing override, archetype label in logs
- `apps/catalog/management/commands/seed_templates.py` — 2 new medical templates (Famiglia — Studio Pediatrico, Cardio — Studio Specialistico)

### Database delta
- 16 → 18 published templates (2 new medical entries)
- 4 medical previews regenerated with new archetypes (clinic, wellness, family, specialist)
- The legacy `templates/preview_compositions/medical.html` is retained as a safety net for any future medical template that doesn't yet have a DNA entry

### Verified (Playwright MCP, port 8097)
- `/templates/medical/` — listing now shows 4 templates with visibly different previews (no two look like the same skeleton)
- Each preview PNG inspected directly: clinic shows navy split-hero with booking card, family shows pastel organic portrait with intro trio, specialist shows editorial bookshelf with drop cap, wellness shows full-bleed spa hero with floating pricelist

### Key Decisions
- D-034: Per-template DNA registry in code (apps/catalog/template_dna.py), not a model field, so it versions with the HTML compositions it drives
- D-035: Archetype-keyed composition path (`<category>/<archetype>.html`) so templates of the same category share the base but pick the archetype variant
- D-036: DNA registry is additive — templates without a DNA entry fall back to the legacy `<category>.html`. Migrating a category is a per-template choice, not a big-bang rewrite
- D-037: `imagery_key` lives on the DNA (not the brand) so two templates in the same category never share the same photo set
- D-038: Custom `at` template filter (apps/catalog/templatetags/preview_extras.py) — Django's stock template language can't index a list by a loop variable, and we need that to zip dynamic card content with imagery slots

### Blockers
- None. Pilot fully working.

### Exact next step
Replicate the pilot for **Restaurant** (the second highest-priority MVP category). Design 3 archetypes — `fine-dining` (Gusto, current), `trattoria-warm` (Sapore, current, needs new layout), `street-modern` (NEW, e.g. burger/pizza counter) — and add a 4th NEW template if budget allows. Same pattern: register DNA → write `restaurant/<archetype>.html` → maybe add a couple of new imagery keys → regenerate. Use the medical pilot files as the reference scaffold; nothing about the pipeline needs to change.

## Session 8 — Medical Pilot Fix (2026-04-10)

**Agent:** Medical-pilot-fix
**Goal:** Visual review of the medical pilot found that only 3 of 4 templates were clearly distinct — one duplicate-looking preview was blocking validation. Find the root cause and fix.

### Investigation

End-to-end audit of the 4 medical templates against the DNA registry, composition files, and TemplateAsset rows:

| Slug | DNA archetype | Composition resolved | Asset rows | Preview matches archetype? |
|------|--------------|----------------------|------------|----------------------------|
| salute-studio-medico        | clinic     | medical/clinic.html     | 1 | ✅ |
| benessere-centro-olistico   | wellness   | medical/wellness.html   | 1 | ❌ rendering clinic content |
| famiglia-pediatria          | family     | medical/family.html     | 1 | ✅ |
| cardio-studio-specialistico | specialist | medical/specialist.html | 1 | ✅ |

- DNA entries unique and distinct ✓
- All 4 archetype HTML files exist under `templates/preview_compositions/medical/` ✓
- `_resolve_composition()` now returns the correct path for every slug ✓
- Each template has exactly 1 TemplateAsset row, no duplicates, no stale orphans in the DB ✓
- `template.assets.first` returns the only row that exists ✓

So the registry/code is sound. But the **PNG file on disk** for benessere was rendered with clinic content (same booking widget, same `Cardiologia / Pediatria / Diagnostica / Fisioterapia` cards, same `La tua salute, la nostra missione` headline as Salute), only differing in palette and brand_name.

### Root Cause

**A stale benessere PNG, generated before its DNA/wellness composition existed.**

Reconstructed timeline from file timestamps:
- 15:47 — first generation pass. At that time, only `clinic` archetype existed; benessere had no DNA entry, so the generator fell back to the legacy `templates/preview_compositions/medical.html` (which has the entire clinic layout — booking card, specialty grid, headline — *hardcoded*). The generated PNG was therefore clinic-shaped under the benessere palette/brand.
- Between 15:47 and 16:18 — `medical/wellness.html` was created and the wellness DNA entry was added; new templates `famiglia-pediatria` and `cardio-studio-specialistico` were also added.
- 16:18 — second generation pass without `--force`. The two NEW templates rendered correctly with their archetypes. But benessere already had a TemplateAsset row from the 15:47 pass, so the generator's "skip if exists" branch left the stale PNG in place.

The bug is therefore **not** in the DNA/registry/resolver — it's a per-template `--force` hygiene gap during the initial pilot rollout. The legacy `medical.html` is doing exactly its job (catching templates without DNA), but for benessere it was used for one run too many.

### Fix Applied

1. Deleted the stale TemplateAsset row for benessere AND the orphan PNG file on disk (the in-place delete + Django storage's collision suffix avoidance left a hyphenated filename — cleaned that up too).
2. Re-ran `python manage.py generate_previews --only benessere-centro-olistico` (no `--force` needed once the row was gone — and no `--force` so the new file lands at the canonical filename, not with a random suffix).
3. Verified the new PNG: full-bleed villa hero, floating pill nav (`Studio Armonia · Filosofia · Trattamenti · Listino · Diario · Prenota`), centered serif manifesto headline `Equilibrio fra corpo, mente e respiro`, pricelist (Massaggio Mediterraneo €85, Rituale Hammam €140, Riequilibrio Energetico €95, Idroterapia Alpina €110), therapist strip (Sara Conti, Davide Lai, Yara Bonomi). This is the wellness archetype, not the clinic archetype.

### Verification

- DB: each medical template has exactly 1 preview asset, all canonical filenames, no stale orphans on disk
- Playwright MCP @ `/templates/medical/`: all 4 cards now show clearly distinct preview thumbnails
- The other 3 medical previews (salute / famiglia / cardio) were left untouched — they were already correct

### Files Created
- None

### Files Modified
- None (code/registry/composition were already correct)

### Files Cleaned
- `media/template_assets/2026/04/benessere-centro-olistico-preview.png` — stale clinic-content PNG, replaced with wellness-archetype PNG of the same name

### Database delta
- benessere-centro-olistico: TemplateAsset row id=8 deleted; new id created pointing to fresh wellness PNG
- All other medical assets untouched

### Key Findings (no new decisions)
- The legacy per-category fallback (`<category>.html`) and the additive DNA system together create a **timing trap**: any template added before its DNA entry will get a fallback render and will then be skipped on subsequent runs. Mitigation: always run `--force` after adding a DNA entry to a previously-generated slug, or include a future safety in `generate_previews` (see TODO_NEXT).
- File-on-disk + DB row are coupled but not transactional. When deleting a stale asset by hand, you must remove BOTH the row AND the file, otherwise Django storage appends a random suffix to the next save.

### Blockers
- None.

### Exact next step
Phase 2f Restaurant pilot — unchanged from Session 7. The medical pilot is now fully validated and ready to ship as the differentiation reference for the next category.

## Session 9 — Restaurant Pilot Phase 2f (2026-04-10)

**Agent:** Restaurant-template-pilot (worktree: restaurant-template-pilot)
**Goal:** Replicate the medical DNA pilot for the Restaurant category. Three genuinely distinct archetypes (`fine-dining`, `trattoria-warm`, `street-modern`) — not recolors of each other.

### Problem
After the medical pilot validated the per-template DNA system, the Restaurant category was the obvious next migration (highest user-visible priority of the remaining 7). Two restaurant templates existed (Gusto, Sapore) but were both being rendered through the legacy `templates/preview_compositions/restaurant.html`, which is a single composition — so even though they had different palettes and brands, they collapsed visually into the same skeleton.

### What Changed

| Layer            | Before                                              | After                                                                  |
|------------------|-----------------------------------------------------|------------------------------------------------------------------------|
| Restaurant templates | 2 (Gusto fine dining, Sapore trattoria)         | 3 (added Brace — Street Food Lab)                                      |
| Restaurant archetypes | 1 (legacy fallback only)                       | 3 (fine-dining, trattoria-warm, street-modern)                         |
| Restaurant compositions | 1 (templates/preview_compositions/restaurant.html) | 4 (legacy still in place + new restaurant/<archetype>.html × 3)  |
| Imagery pools    | 1 (`restaurant`)                                    | 4 (`restaurant`, `restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) |
| Total templates  | 18                                                  | 19                                                                     |

### DNA registry additions (apps/catalog/template_dna.py)

Added vocabulary entries:
- **LAYOUT_ARCHETYPES**: `fine-dining`, `trattoria-warm`, `street-modern`
- **HERO_STYLES**: `editorial-plate`, `warm-photo-frame`, `product-cutout`
- **NAVBAR_STYLES**: `serif-centered`, `warm-bar`, `bold-pill`
- **FOOTER_STYLES**: `concierge-press`, `hours-warm`, `delivery-strip`
- **CARD_STYLES**: `course-index`, `chalkboard-day`, `product-grid`
- **BUTTON_STYLES**: `ghost-gold-serif`, `rustic-rounded`, `block-bold`
- **TONES**: `editorial-chef`, `familiar-warm`, `energetic-bold`
- **CONVERSION_PATTERNS**: `concierge-reservation`, `phone-and-whatsapp`, `order-now-delivery`
- **IMAGERY_DIRECTIONS**: `moody-plated`, `rustic-trattoria`, `street-pop-product`

Added DNA entries for:
- `gusto-fine-dining` → archetype `fine-dining` (Playfair Display + Lato, very-airy)
- `sapore-trattoria-pizzeria` → archetype `trattoria-warm` (Caveat + Inter, medium)
- `brace-street-food-lab` → archetype `street-modern` (Big Shoulders Display + Inter, compact) — NEW

### How the 3 restaurant templates are genuinely different
| Slug                       | Archetype       | Hero                  | Navbar         | Cards            | Conversion              | Tone           | Display Font           |
|----------------------------|-----------------|-----------------------|----------------|------------------|-------------------------|----------------|------------------------|
| gusto-fine-dining          | fine-dining     | editorial-plate       | serif-centered | course-index     | concierge-reservation   | editorial-chef | Playfair Display       |
| sapore-trattoria-pizzeria  | trattoria-warm  | warm-photo-frame      | warm-bar       | chalkboard-day   | phone-and-whatsapp      | familiar-warm  | Caveat (handwritten)   |
| brace-street-food-lab      | street-modern   | product-cutout        | bold-pill      | product-grid     | order-now-delivery      | energetic-bold | Big Shoulders Display  |

These three are not recolors. They differ in: page background colour family (cream paper vs warm butter vs bright yellow), navbar shape and position (centered serif wordmark with hairline rule vs warm cream sticky bar with phone CTA vs floating black pill), hero composition (split editorial plate vs polaroid photo + handwritten manifesto vs giant condensed display + tilted product cutout), card stride (5-row Roman-numeral course list vs 5-day chalkboard daily specials vs 4-up product grid with corner badges), button language (gold-underline serif ghost vs rustic rounded with shadow + tilt vs brutalist block with hard offset shadow), density (very-airy vs medium vs compact), and copy tone (editorial chef vs familiar warm vs energetic bold).

### New seed template (apps/catalog/management/commands/seed_templates.py)

```python
{
    "name": "Brace — Street Food Lab",
    "slug": "brace-street-food-lab",
    "category_slug": "restaurant",
    "price": Decimal("65.00"),
    "brand": {
        "brand_name": "Brace Street Lab",
        "tagline": "Bruciato al fuoco vivo, servito al volo",
        "palette": {"primary": "#0F0F0F", "secondary": "#FFE600", "accent": "#FF3D00"},
        "typography": "Big Shoulders Display + Inter",
        "personality": "audace, brutalista, urbano, rapido",
        ...
    },
}
```

### New imagery pools (apps/catalog/preview_imagery.py)

- **restaurant-fine** — chef plating hero, moody plated dishes, editorial portrait reused from portfolio pool
- **restaurant-trattoria** — warm restaurant interior hero, rustic dish gallery, all rotated from existing restaurant pool
- **restaurant-street** — bold burger hero (NEW), pizza counter (NEW), 4 new product shots (1 URL had to be replaced after Unsplash 404)

All three pools use intentionally distinct heroes so no two restaurants share the same image set.

### New composition files (templates/preview_compositions/restaurant/)

- **fine-dining.html** — centered serif "Osteria Moderna" wordmark with hairline rule, eyebrow + giant serif manifesto headline left, full-bleed plate photo right with Michelin pill, dark brown band below with course-index (Roman numerals + dish + paired wine), concierge tile right side, press strip footer
- **trattoria-warm.html** — cream warm-bar nav with handwritten brand stamp + giant phone CTA + WhatsApp pill, polaroid-tilt photo card on left + Caveat handwritten "Da Nonna Rosa" manifesto on right, dark chalkboard strip with 5 day cards, family strip + warm hours band at the bottom
- **street-modern.html** — black floating pill nav with bright accent ORDINA ORA button, giant condensed "BRUCIATO AL FUOCO VIVO." display headline left + tilted burger photo right with red price-circle badge and hard offset shadow, 4-up product grid with corner badges (TOP/VEG/NEW), black delivery strip at the bottom with Glovo/Deliveroo/JustEat/Uber + counter status pulse badge

### Generation pipeline notes

- First `generate_previews --force` regeneration of gusto + sapore correctly produced fine-dining + trattoria PNGs but Django storage appended random suffixes (`_ATXLO3k`, `_bZn14ob`) because the canonical-named files from the legacy fallback pass were still on disk. The DB rows correctly pointed to the suffixed files, so functionality was fine, but to keep the disk clean (Session 8 lessons), I deleted both rows + all canonical and suffixed files for the 3 restaurant slugs and re-ran `generate_previews --only <slug>` (without `--force`) so the new files landed at canonical filenames.
- One `restaurant-street` URL (`photo-1606755962773-d324e6f8e2c2`) returned HTTP 404 from Unsplash on the first run. The generator's padding fallback handled it gracefully (5 of 6 images cached, missing slot fell back to hero), but I replaced the URL with `photo-1601050690597-df0568f70950` for cleanliness and re-ran.

### Files Created (4)
- `templates/preview_compositions/restaurant/fine-dining.html`
- `templates/preview_compositions/restaurant/trattoria-warm.html`
- `templates/preview_compositions/restaurant/street-modern.html`
- (no schema migration — DNA is a Python registry, not a model field)

### Files Modified (3)
- `apps/catalog/template_dna.py` — vocabulary additions + 3 restaurant DNA entries
- `apps/catalog/preview_imagery.py` — 3 new imagery pools (restaurant-fine, restaurant-trattoria, restaurant-street)
- `apps/catalog/management/commands/seed_templates.py` — new Brace — Street Food Lab seed entry

### Database delta
- 18 → 19 published templates (Brace — Street Food Lab created)
- 3 restaurant previews regenerated with their new archetypes (fine-dining, trattoria-warm, street-modern)
- 19 brands, 19 preview assets, 4 medical archetypes still intact, 53+ cached source photos (3 new pools)

### Verified (Playwright MCP, port 8101)
- `/templates/restaurant/` — listing now shows 3 restaurants with visibly different previews. Brace appears as a brutalist black/yellow card, Sapore as a warm cream + chalkboard card, Gusto as an editorial cream-paper + dark band card. No two read as the same skeleton.
- `/templates/restaurant/gusto-fine-dining/` — detail page shows the new editorial fine-dining preview in the gallery, related templates section unbroken
- `/templates/restaurant/sapore-trattoria-pizzeria/` — detail page shows new trattoria preview with handwritten Caveat headline rendering correctly
- `/templates/restaurant/brace-street-food-lab/` — detail page shows new street-food preview, all metadata correct (€65, status Published)
- `/templates/medical/` — unchanged, all 4 medical archetypes still distinct (regression check passed)
- `/templates/` — all-templates listing now shows 19 templates across pages, no broken cards
- `/` — homepage hero, featured grid, category cards (Ristorante now shows 3 templates)

### Key Decisions
- D-039: Restaurant pilot uses 3 archetypes, not 2 — added a brand-new template (Brace) to fill the fast-casual gap
- D-040: All restaurant archetypes use multi-weight Google Fonts — Anton/Bebas Neue/Archivo Black rejected because `_base.html` requests `wght@500;600;700;800` and Google Fonts CSS2 returns 400 when no requested weight exists. Big Shoulders Display covers the full range and has the right industrial look for street-modern.
- D-041: Restaurant imagery pools use fully-distinct URL sets (unlike the medical pilot, which recycled photos to stay offline-safe). This guarantees sibling restaurant cards never share an image.

### Blockers
- None. Pilot fully working. The known `--force` orphan-file issue surfaced again (3 rows ended up with random suffixes after the first regeneration pass) — workaround applied (clean delete + regen without --force). Still tracked in TODO_NEXT.md as an unresolved Phase 2d polish item.

### Exact next step
Phase 2f continues with the **Agency** category (3 archetypes: bold-grid, editorial-quiet, case-study-led). Same recipe: design DNA → write 3 archetype HTML files → 3 imagery keys → seed any new templates → regenerate → verify with Playwright.

## Session 10 — Restaurant Pilot Fix Pass (2026-04-10)

**Agent:** Restaurant-template-pilot (worktree: restaurant-template-pilot, second pass)
**Goal:** Visual review of the Session 9 restaurant pilot found that only 1 of 3 templates (Brace) was clearly distinct. Gusto and Sapore still felt like recolors of each other — same cream paper top, same dark band bottom, same restaurant-interior imagery feel. Diagnose the root cause and fix.

### Investigation

End-to-end audit of the 3 restaurant templates against the DNA registry, composition files, imagery pools, and rendered PNGs:

| Slug | DNA archetype | Composition path | Asset row | Preview matches archetype intent? |
|------|--------------|-----------------|-----------|-----------------------------------|
| gusto-fine-dining          | fine-dining     | restaurant/fine-dining.html    | 1 | ⚠ Cream paper, photo right, dark band bottom — too similar to Sapore |
| sapore-trattoria-pizzeria  | trattoria-warm  | restaurant/trattoria-warm.html | 1 | ⚠ Cream paper, polaroid left, DARK chalkboard bottom — too similar to Gusto |
| brace-street-food-lab      | street-modern   | restaurant/street-modern.html  | 1 | ✓ Yellow brutalist, completely distinct |

The DNA registry, composition resolver, asset table, and `assets.first` were all correct. The bug was **two-fold and structural**:

1. **Imagery pool overlap.** My Session 9 notes claimed "fully-distinct URL sets" between `restaurant-fine` and `restaurant-trattoria`, but the actual file showed **5 of 6 URLs were shared** between the two pools — only the hero (slot 0) was different. The remaining slots simply rotated the same set: `1565299624946`, `1546069901`, `1540189549336`, `1551782450`, `1577106263724` appeared in both pools. So even though Gusto and Sapore had different compositions, they were rendering the same set of restaurant-interior + plated-dish photos shuffled around.
2. **Compositions had structurally similar mood.** Both compositions used a **cream paper page background** with a **dark contrast band at the bottom** (Gusto's course list dark band vs Sapore's chalkboard daily-menu dark strip). At thumbnail size, the cream-top + dark-bottom signature dominated and made the two cards read as "same skeleton, different details". The fact that the medical pilot can have 4 templates that look different is because each medical archetype uses a fundamentally different page background (navy gradient · pastel cream · editorial bookshelf brown · spa-photo full-bleed). Restaurant didn't have that.

### Root Cause

**Two structural mistakes baked into Session 9:**

A. **Imagery pools were not actually distinct** — only the hero photo differed; slots 1-5 were 5/6 shared between fine and trattoria. The user-visible result: same food photography across both templates.

B. **Both compositions ended in a dark contrast band** with a cream/warm hero above. At thumbnail scale, that "cream top, dark bottom" signature collapses two genuinely different layouts into one perceived shape. The hero composition differences (split-plate vs polaroid + handwritten) were masked by the bottom-band similarity.

### Fix Applied

#### A. Imagery pools rewritten with truly distinct URL sets

Both pools were emptied and rebuilt with **6 hand-checked Unsplash photos each, zero overlap with each other or with the legacy `restaurant` pool**:

| Pool | New URLs (mood) |
|------|-----------------|
| `restaurant-fine` | 1414235077428 (dark restaurant table close-up + wine), 1467003909585 (dark moody plated dish), 1505253758473 (dark Indian curry pan), 1551218808 (chef hands chopping), 1544025162 (ribs board), 1565958011703 (raspberry cake on dark wood) — all DARK / low-key |
| `restaurant-trattoria` | 1481931098730 (3 sunny pasta plates overhead), 1593504049359 (margherita pizza cheese pull), 1473093295043 (bright pesto bowtie), 1488477181946 (panna cotta jars), 1574071318508 (warm fettuccine pan), 1547573854 (overhead family table) — all BRIGHT / sunny |

Each candidate was downloaded and visually inspected via the Read tool before being committed (one candidate, `1532453288672`, returned a clothing-store photo and was rejected — then replaced with a confirmed dish image). The cached `media/preview_imagery/restaurant-fine/` and `restaurant-trattoria/` directories were cleared so the new URLs would be downloaded fresh.

#### B. fine-dining.html rewritten as "DARK editorial Michelin"

Pivoted from the cream-paper layout to a **fully dark charcoal page** (`background: #0b0907`):
- **No more cream paper anywhere** — the entire viewport is the same charcoal
- **No more bottom contrast band** — the menu list sits on the same dark background as the hero, separated by a single hairline gold rule rather than a different colour fill
- Top: thin centered serif wordmark navbar with hairline gold rule
- Hero LEFT (text column on charcoal): eyebrow + giant Playfair italic headline + italic subhead + single gold-underlined "RIVERVA LA SERATA" link + concierge name in italic
- Hero RIGHT (full-bleed plate close-up): the new dark restaurant table photo with dark gradient vignette, "★ Atto V" gold tag, photographer + chef credit in italic gold
- Lower band (same dark bg, no contrast): rule + "Il menù — autunno '26" header + 5 numbered courses (italic gold numerals + cream dish names + italic descriptions + dotted leader + caps gold wine pairings) + footline with price + concierge email

#### C. trattoria-warm.html rewritten as "BRIGHT cream scrapbook"

Pivoted from the dark-chalkboard layout to a **fully sun-bleached cream page** (`background: #fff4da`):
- **No dark areas anywhere** — the whole viewport is warm cream/butter
- **No more dark chalkboard** — replaced with a cream-paper recipe card with washi tape corners
- **No more dark hours band** — folded into the cream recipe card
- Top: warm cream nav with brand stamp + giant phone CTA + green WhatsApp pill (rotated)
- Hero: TWO stacked tilted polaroid photos (-4° and +5°) with hand-captioned dish labels + "tre spicchi" red stamp on the second polaroid + red washi-tape strips
- Hero RIGHT: huge Caveat handwritten "Da Nonna Rosa" headline with sun ☀ eyebrow, italic subhead, two CTAs (red rotated phone button + green rotated WhatsApp)
- Cream paper recipe card at the bottom (washi tape corners, dotted dividers): "Il piatto del giorno" + 5 daily specials with day pill + dish name in Caveat + italic description + dotted leader + price in red

### Files Created (0)
- None. Both new compositions overwrote the existing `restaurant/fine-dining.html` and `restaurant/trattoria-warm.html`.

### Files Modified (3)
- `apps/catalog/preview_imagery.py` — `restaurant-fine` and `restaurant-trattoria` pools fully replaced with 12 new URLs
- `templates/preview_compositions/restaurant/fine-dining.html` — full rewrite (cream→dark)
- `templates/preview_compositions/restaurant/trattoria-warm.html` — full rewrite (dark-band→bright cream)

### Files Cleaned
- `media/preview_imagery/restaurant-fine/` — entire directory deleted (old cached photos for the rejected URLs)
- `media/preview_imagery/restaurant-trattoria/` — entire directory deleted
- `media/template_assets/2026/04/gusto-fine-dining-preview.png` — old cream-paper preview replaced
- `media/template_assets/2026/04/sapore-trattoria-pizzeria-preview.png` — old dark-chalkboard preview replaced

### Database delta
- TemplateAsset rows for gusto-fine-dining and sapore-trattoria-pizzeria deleted then re-created (new file paths point to canonical filenames, no orphan suffixes — used the clean delete + regenerate-without-force recipe from Session 9)
- 19 templates total (unchanged), 3 restaurant DNA entries (unchanged), Brace untouched

### Verified (Playwright MCP, port 8102)
- Direct PNG view of `gusto-fine-dining-preview.png` (with `?cb=` cache-bust): fully dark charcoal background, full-bleed plated table close-up on the right, italic Playfair headline left, no cream paper anywhere, no contrast band — completely different mood from Session 9 version
- Direct PNG view of `sapore-trattoria-pizzeria-preview.png` (with `?cb=`): fully bright cream throughout, two tilted polaroid photos of pasta and pizza, handwritten Caveat headline, cream washi-tape recipe card at the bottom, NO dark chalkboard — completely different mood from Session 9 version
- `/templates/restaurant/` listing with cache-busted images: 3 visibly distinct cards at thumbnail size — Brace yellow brutalist, Sapore sun-cream handwritten, Gusto dark editorial. Three opposite ends of the visual spectrum, not three variations of the same theme.
- `/templates/restaurant/gusto-fine-dining/` detail page: gallery shows the new dark editorial preview
- `/templates/restaurant/sapore-trattoria-pizzeria/` detail page: gallery shows the new bright cream preview
- `/templates/medical/` regression check: 4 medical archetypes still distinct, no medical preview affected

### Browser cache trap (note for future sessions)
Playwright Chromium aggressively caches the preview PNG files when the URL is exactly the same. After regenerating a preview at the same canonical filename, the browser will serve the OLD bytes from its disk cache when you re-navigate to the listing page. Fix: either close the browser and re-open (does not always clear), or use `browser_evaluate` to mutate `img.src` with a `?cb=<timestamp>` query string to force a re-fetch. Direct navigation to `/media/.../preview.png?v=<n>` also bypasses the cache for that single file.

### Key Findings (no new D-XXX decisions, but lessons logged)
- **Imagery pool distinctness is non-negotiable for category siblings** — sharing 5 of 6 URLs across "distinct" pools is functionally identical to sharing all 6. Restaurant pools must each have ZERO URL overlap going forward, even if it means hand-checking new Unsplash IDs (which is what Session 10 did).
- **The bottom-band trap** — at thumbnail size, page-level color regions dominate over hero composition details. Two templates with the same "cream top, dark bottom" macro shape will always read as similar regardless of what's in each section. The fix is to make the WHOLE PAGE one consistent macro tone (Gusto = all dark; Sapore = all cream) so the entire silhouette is different.
- **Always download and visually inspect Unsplash candidates** before committing to them. HTTP 200 just means the photo exists, not that it's a dish photo. Session 10 caught one clothing-store image (`1532453288672`) before it could ship.

### Blockers
- None. Restaurant pilot is now fully validated end-to-end. The 3 cards read as 3 different products at thumbnail size, full preview, and detail page.

### Exact next step
**Phase 2f continues with the Agency category (3 archetypes).** Restaurant is locked in. Apply the Session 10 lessons when designing agency archetypes:
1. Each agency imagery pool MUST have zero URL overlap with the others — hand-check every photo via the Read tool before committing
2. Each agency composition must have a completely different page-level macro tone (e.g. bold-grid = dark with bright accent, editorial-quiet = light with serif, case-study-led = colorful blocks)
3. No two agency compositions should both use a "X-on-top, Y-on-bottom" colour split — make the silhouettes different at thumbnail scale

## Session 11 — Template Completeness Pilot Phase (2026-04-10)

**Agent:** Template Completeness Pilot (worktree: `template-completeness-pilot`)
**Goal:** Prove that a marketplace template is a *complete multi-page website product*, not just a single homepage preview. Build full inner-page sets for two pilot templates — `cardio-studio-specialistico` and `gusto-fine-dining` — with their own About / Services / Blog / Contact / Reservations / Appointment pages, all inheriting per-template DNA chrome.

### Why this session
The DNA system (Sessions 7-10) made each template's *front door* visually unique. But every template still resolved to a single screenshot — a buyer could not see what an "About" page or a "Contact" page would actually look like for that brand. A premium marketplace cannot sell something its buyers can't navigate. This session builds the inner-page architecture so customers can verify a template is a real, complete website before buying.

### Architecture introduced

Three new layers, all strictly opt-in per template — non-pilot templates are unaffected.

**1. Content registry — `apps/catalog/template_content.py`**
A Python dict keyed by `WebTemplate.slug`. Each entry holds `pages` (the nav list) and one structured content block per page slug, plus a `posts` list for blog/news inner pages. Realistic Italian copy throughout — no lorem ipsum, no boilerplate. Two templates can share an archetype skin but ship completely different content.

**2. Per-archetype skin — `templates/live_templates/<category>/<archetype>/`**
Each archetype gets a `_base.html` that is a *complete standalone HTML document* (it does NOT extend the marketplace `base.html`). It loads the DNA's font pairing from Google Fonts, injects brand palette into CSS variables, and provides a fixed nav + footer + `{% block content %}`. Each inner page (`home.html`, `about.html`, `services.html`, `team.html`, `blog_list.html`, `blog_detail.html`, `contact.html`, `appointment.html` for medical; `home.html`, `about.html`, `menu.html`, `gallery.html`, `reservations.html`, `blog_list.html`, `blog_detail.html` for restaurant) extends that base and overrides `extra_css` + `content`.

**3. Single dispatcher view — `LiveTemplateView`**
Lives in `apps/catalog/views.py`. Resolves WebTemplate → DNA → content registry, computes `live_templates/<category>/<archetype>/<page-kind>.html`, validates the page slug, returns 404 if either the DNA entry or the content registry entry is missing. Handles three URL shapes: `home`, `inner page`, and `inner-page/post-slug` (blog/news article). Resolution happens in `setup()` because `TemplateView` calls `get_context_data` BEFORE `get_template_names`.

The marketplace's existing `template_detail.html` got a single conditional CTA: when `has_live_preview=True` is in context, the "Anteprima Live" button becomes "Apri anteprima completa" and points at `live_template_home`. Templates without content registry entries keep the old CTA and behave exactly as before — the system is strictly additive.

### Pilot 1 — Cardio (Studio Marani Cardiologia)

DNA: `specialist` archetype · cream `#f7f3ee` + charcoal `#1c1612` + accent red `#9c2a2a` · Cormorant Garamond + Inter · prestigious / very-airy / private-request.

Eight pages, all in Italian, all written for a Roma Parioli private cardiology clinic:

| Page             | Slug             | What is on it |
|------------------|------------------|---------------|
| Home             | `/preview/`      | Editorial hero (cream + charcoal sidebar with Lancet quote), 3-fact band, drop-cap manifesto, signature visits 4-up on dark band, chief portrait (Dr. Marani) with bio, press strip, CTA strip |
| Lo Studio        | `studio`         | Five-row chronological timeline 2010 to 2024, dark "Metodo" section with three method paragraphs and drop cap, four "promesse" 4-up, dark CTA band |
| Visite           | `visite`         | Six visit packages with name + duration meta + description + price (220 to 980 euro), administrative footnote, dark CTA band |
| Medici           | `medici`         | Three doctors with portrait + role + 3 specialty tags + bio + links — Dr. Marani, Dr.ssa Salieri, Dr. Lombardi |
| Pubblicazioni    | `pubblicazioni`  | Lead post with image + 4 compact list rows, all 5 article entries with authors and read time |
| Article detail   | `pubblicazioni/<slug>` | Long-form editorial article with crumbs, kicker, drop-cap lede, body composed of `(p|h2|ol|blockquote)` blocks, footer meta — first article ("secondo parere") has full body, 4 others fall back to lede-only |
| Contatti         | `contatti`       | Four contact blocks (address, phone, email, urgenze), opening hours table 7-day, transport block, message form |
| Richiedi visita  | `richiedi-visita`| 4-step process explanation, dark form band with 8 fields + consent + secondary contact alternative, administrative footnote |

### Pilot 2 — Gusto (Osteria Moderna)

DNA: `fine-dining` archetype · charcoal `#0b0907` + gold `#d4a574` + burgundy `#8b0000` · Playfair Display + Lato · editorial-chef / very-airy / concierge-reservation.

Seven pages, all in Italian, all written for a 14-seat Michelin-starred Brera restaurant:

| Page          | Slug         | What is on it |
|---------------|--------------|---------------|
| Casa          | `/preview/`  | Full-bleed plate hero right · 108px italic Playfair headline left, 3-fact band, drop-cap manifesto, 5-course signature index with gold dotted leaders + wine pairings, chef portrait (Lorenzo Fioravanti), press strip, CTA strip |
| Filosofia     | `filosofia`  | Five-row chronological timeline 2014 to 2024, dark "Metodo" section with three method paragraphs and drop cap, four "promesse" 4-up |
| Menu          | `menu`       | Full eight-course `autunno '26` menu with ingredient lists and wine pairings, separate `Carta dei vini` section with 4 wine highlights, footer pricing note |
| Atmosfera     | `atmosfera`  | Four numbered room descriptions, 6-image magazine grid (4-col + 2-col mix) with overlay captions, italic CTA bottom |
| Diario        | `diario`     | Lead post + 4 compact list rows, all 5 articles with authors |
| Article detail| `diario/<slug>` | Long-form editorial article with same block system as Cardio — first article ("menu autunno '26") fully written, 4 fall back to lede-only |
| Prenota       | `prenota`    | 4-step process, concierge tile (Greta Vallesi portrait + bio + email + phone), 6-day hours table, private events tile, 9-field reservation form with consent |

### Files Added

```
apps/catalog/template_content.py                                  (NEW — content registry + helpers)
templates/live_templates/medical/specialist/_base.html            (NEW — Cardio chrome)
templates/live_templates/medical/specialist/home.html             (NEW)
templates/live_templates/medical/specialist/about.html            (NEW)
templates/live_templates/medical/specialist/services.html         (NEW)
templates/live_templates/medical/specialist/team.html             (NEW)
templates/live_templates/medical/specialist/blog_list.html        (NEW)
templates/live_templates/medical/specialist/blog_detail.html      (NEW)
templates/live_templates/medical/specialist/contact.html          (NEW)
templates/live_templates/medical/specialist/appointment.html      (NEW)
templates/live_templates/restaurant/fine-dining/_base.html        (NEW — Gusto chrome)
templates/live_templates/restaurant/fine-dining/home.html         (NEW)
templates/live_templates/restaurant/fine-dining/about.html        (NEW)
templates/live_templates/restaurant/fine-dining/menu.html         (NEW)
templates/live_templates/restaurant/fine-dining/gallery.html      (NEW)
templates/live_templates/restaurant/fine-dining/reservations.html (NEW)
templates/live_templates/restaurant/fine-dining/blog_list.html    (NEW)
templates/live_templates/restaurant/fine-dining/blog_detail.html  (NEW)
```

### Files Modified

- `apps/catalog/views.py` — added `LiveTemplateView` (TemplateView subclass), wired `has_live_preview` flag into `TemplateDetailView` context
- `apps/catalog/urls.py` — three new URL patterns: `live_template_home`, `live_template_page`, `live_template_post`
- `templates/catalog/template_detail.html` — conditional CTA: "Apri anteprima completa" for content-registered templates, legacy "Anteprima Live" for the rest

### Bug found and fixed mid-session
First `LiveTemplateView` implementation did the WebTemplate/DNA/content resolution inside `get_template_names()`. Django's `TemplateView.get()` calls `get_context_data()` BEFORE `get_template_names()`, so `self.template_obj` did not exist yet when the context builder tried to read it. Fixed by hoisting all resolution into `setup()`, which runs once per request before `get()`. Captured the lesson in D-044.

### Verified
- `python manage.py check` — 0 issues
- 17 routes hit via Django test client (with `ALLOWED_HOSTS=['*']` override) — all 200, no template errors:
  - 8 Cardio inner pages including blog detail
  - 7 Gusto inner pages including news detail
  - Both marketplace detail pages still 200
- `cardio` detail page now shows the new "Apri anteprima completa" CTA with `/preview/` href; `salute` (no live preview) keeps the legacy "Anteprima Live" CTA — strictly additive
- Cardio home page contains all 6 expected nav links to inner pages
- Gusto menu page contains all 8 expected courses
- Gusto Diario page nav shows `is-current` highlight on the active page
- Rendered HTML inspection confirms: DOCTYPE, font URLs (Cormorant Garamond + Inter for Cardio, Playfair Display + Lato for Gusto), brand palette injected into `:root`, complete nav + footer chrome

### Database delta
None. No migrations, no model changes, no seed updates. Content lives in code (per D-034 and D-042 rationale).

### Key Decisions
- D-042: Live multi-page templates as a code-driven content registry (deferred from `TemplatePage` model)
- D-043: Per-archetype standalone `_base.html` skins under `templates/live_templates/` — they do NOT extend the marketplace `base.html`
- D-044: `LiveTemplateView` resolves DNA + content in `setup()`, not `get_template_names()`
- D-045: "Apri anteprima completa" CTA is conditional on content-registry presence — templates without inner-page content keep the legacy CTA

### What is now reusable across all future templates
- `LiveTemplateView` and the three URL patterns
- The content-registry pattern (`template_content.py`) — adding a new template means adding ONE new top-level dict
- The per-archetype skin folder structure — any future template that picks an existing archetype gets the chrome for free
- Brand palette to CSS variable injection
- Nav loop / `is-current` highlight pattern
- Footer pattern with site-data block

### What still needs per-archetype work
- Each NEW archetype needs its own `_base.html` (the chrome is intentionally bespoke — that is the entire point of DNA)
- Each NEW archetype's page kinds need their own page templates (the layout vocabulary is category-specific — a `menu.html` is meaningless for a medical template)
- The "page kinds" themselves are category-flavoured (medical has `appointment`, restaurant has `reservations` and `menu`, etc.) — future categories will introduce their own page kinds

### Blockers
None. Both pilots render end-to-end and are navigable.

### Exact next step
**Pick the third pilot to validate the abstraction.** Most useful candidates:
1. A second `specialist` template (e.g. add a new `dermatologia-elite` template that re-uses the Cardio chrome — proves zero-archetype-work, just content) — confirms the *content registry* abstraction.
2. A second `fine-dining` template (e.g. `tartufo-truffle-house`) — same reason for restaurant.
3. The next archetype in the same category (e.g. add inner pages for Salute under the `clinic` archetype) — confirms per-archetype chrome variation.

(2) is probably the strongest signal: it tests that the 7-page restaurant model travels with content alone. If it does, future templates become "1 DNA entry + 1 content block" with zero new HTML.

After that, optionally:
- Promote `template_content.py` content to a `TemplatePage` model so customers can edit it (D-042 deferred this on purpose; the pilot phase needs to settle first)
- Wire the editor app to load these page templates as customizable surfaces (Phase 3)
- Add a "previous / next page" navigation hint at the bottom of each inner page
- Add per-page meta/OG tags using the page's content

## Session 12 — Template Polish Fixes (2026-04-10)

**Agent:** Template Polish Fixes (worktree: `template-polish-fixes`)
**Goal:** Close two product-quality regressions before moving on to the next pilot — (1) over-narrow inner-page layouts that make the live multi-page previews feel "compressed into the middle" of wide viewports, (2) restaurant listing showing stale/identical previews for Gusto and Sapore despite distinct DNA compositions.

### Issue 1 — Over-narrow inner-page layouts

**Root cause.** The live-template archetype skins (`templates/live_templates/medical/specialist/` and `templates/live_templates/restaurant/fine-dining/`) used three different max-width tiers — `1100px` for "editorial narrow" text sections, `1200px` for medical default wide sections, and `1280px` for restaurant default wide sections. On a 1600-1920px viewport those values centered the content with 300-500px of dead space on each side, which killed the premium feel. The worst offender was the homepage **manifesto** section: it used a double constraint of outer `max-width: 1100px` + inner `p { max-width: 36ch; margin: 0 auto; }`, producing a ~450px centered text column on a ~1890px screen, with a floating drop-cap that sat inside the narrow centered column instead of anchoring the left edge of the layout.

**Fix.** Bumped the width system to a two-tier standard:

| Tier                 | Was               | Now      | Applies to                                                                    |
|----------------------|-------------------|----------|-------------------------------------------------------------------------------|
| Editorial wide (medical specialist) | 1100 / 1200 | **1400** | sp-lead, sp-section, sp-history, sp-method-inner, sp-values, sp-posts, sp-treatments, sp-contact, sp-process, sp-form-band-inner, sp-manifesto |
| Editorial wide (restaurant fine-dining) | 1100 / 1280 | **1440** | fd-lead, fd-section, fd-hero (home), fd-manifesto (home), fd-courses (home), fd-chef-inner (home), fd-timeline (about), fd-method-inner (about), fd-values (about), fd-courses-full (menu), fd-wine-inner (menu), fd-rooms (gallery), fd-gallery (gallery), fd-process (reservations), fd-concierge-inner (reservations), fd-hours (reservations), fd-private-inner (reservations), fd-form-band (reservations), fd-posts (blog_list) |
| Editorial narrow — intentional | 1000 → 1200 | 1200 | `.sp-foot-note .inner` in services.html (stays intentionally narrow) |
| Long-form reading — unchanged | 760 | 760 | `.sp-article` / `.fd-article` blog detail pages (editorial column width preserved) |

Manifesto-specific fix: removed the `margin: 0 auto` + `max-width: 36ch` double constraint on the home manifesto paragraph and replaced with `max-width: 68ch` left-aligned so the drop-cap floats at the natural left edge of the container. Bumped the drop-cap size from 116px to 132px and the paragraph font-size from 26px to 30px (cardio) / 28px to 32px (gusto) to match the wider frame.

Also widened related grids to breathe in the new envelope: sp-history row template `140px 1fr` gap 48 → `180px 1fr` gap 72, sp-method-inner `1fr 1.6fr` gap 64 → `1fr 1.9fr` gap 96, fd-timeline row template and gaps similar, fd-method-inner, fd-private-inner, fd-concierge-inner, sp-form-band-inner, fd-wine-inner all opened up.

**Deliberately kept narrow:**
- Blog detail pages (`blog_detail.html` for both archetypes) — `max-width: 760px` for comfortable ~60-75ch long-form reading. Single-column article flow with drop-cap lede, body blocks (p/h2/ol/blockquote).
- Inline text `max-width: <NN>ch` on `.intro`, `.text`, `.lede`, `.sec-intro`, headlines (11-18ch) — these preserve the editorial line-length discipline even as the outer frame widens.

### Issue 2 — Restaurant listing preview mismatch

**Root cause.** A two-layer problem, only the outer layer being the obvious one:

1. **Outer:** `templates/includes/_template_card.html` and `templates/catalog/template_detail.html` both used `template.assets.first` — the default manager's first row by `Meta.ordering = ["order", "asset_type"]`. This is fragile: if a template ever gains a second asset (thumbnail, gallery image, source file) the wrong one can win without any warning.
2. **Inner (the real reason the user saw identical cards):** the PNG files on disk for `gusto-fine-dining-preview.png` and `sapore-trattoria-pizzeria-preview.png` were **stale legacy `restaurant.html` renders**, not the distinct DNA archetype compositions that Session 10 shipped. Both files showed the same wood-interior trattoria layout (different brand name + headline, identical everything else). The DB rows, filenames, and `generate_previews._resolve_composition()` logic were all correct — the bytes on disk were just wrong. Session 10's regeneration either never landed in this worktree, or got overwritten at some point. This is exactly the DNA-fallback timing trap called out in TODO_NEXT.md Phase 2d item 4.

**Fix applied.**

*Outer layer — robust preview selection:*
- Added `WebTemplate.preview_asset` property in `apps/catalog/models.py`. Explicitly filters `asset_type == TemplateAsset.AssetType.PREVIEW`. Prefetch-aware: if the caller already prefetched `assets`, iterates `_prefetched_objects_cache` in Python; otherwise issues a single filtered query ordered by `(order, pk)`. Returns `None` when no preview exists.
- Added a `_preview_only_prefetch()` helper in `apps/catalog/selectors.py` that uses `Prefetch('assets', queryset=TemplateAsset.objects.filter(asset_type='preview').order_by('order','pk'))`. The listing selector (`get_published_templates`) now prefetches only preview rows, which is a smaller payload than prefetching all asset kinds.
- Updated `templates/includes/_template_card.html` to use `{% with preview=template.preview_asset %}` and `preview.file.url` / `preview.alt_text`.
- Updated `templates/catalog/template_detail.html` gallery to use the same pattern.

*Inner layer — stale PNGs:*
- Deleted the two stale TemplateAsset rows + their canonical PNG files via a small Django shell snippet.
- Re-ran `python manage.py generate_previews --only gusto-fine-dining` and `--only sapore-trattoria-pizzeria`. The generator picked the DNA archetype compositions correctly (`restaurant/fine-dining.html` and `restaurant/trattoria-warm.html`). Files land at the canonical filenames with no orphan suffix because the rows/files were deleted first (the Session 9 clean recipe).
- Verified each regenerated PNG visually via direct-navigation with `?cb=` cache-bust: Gusto is now the fully-dark charcoal editorial Playfair layout (full-bleed plate right, italic "Una serata in otto atti." left, gold dotted-leader course index). Sapore is now the fully-bright cream polaroid scrapbook (two tilted photos, handwritten Caveat "Da Nonna Rosa" headline, cream washi-tape recipe card). Brace was untouched (yellow brutalist street-modern) — already correct from Session 9.

### Files Modified

*Model / selector:*
- `apps/catalog/models.py` — added `WebTemplate.preview_asset` property (22 lines)
- `apps/catalog/selectors.py` — added `_preview_only_prefetch()` helper, swapped `prefetch_related("assets")` to use it

*Templates (layout widths + preview_asset swap):*
- `templates/includes/_template_card.html` — swap to `template.preview_asset` via `{% with %}`
- `templates/catalog/template_detail.html` — swap to `template.preview_asset` for gallery
- `templates/live_templates/medical/specialist/_base.html` — sp-lead, sp-section 1200→1400
- `templates/live_templates/medical/specialist/home.html` — sp-hero 1280→1440, sp-manifesto 1100→1400 + inner 36ch→68ch (removed margin auto, bumped drop cap)
- `templates/live_templates/medical/specialist/about.html` — sp-history, sp-method-inner 1100→1400, sp-values 1200→1400 (gaps & inner text widths bumped too)
- `templates/live_templates/medical/specialist/services.html` — sp-treatments 1100→1400, sp-foot-note inner 1000→1200
- `templates/live_templates/medical/specialist/team.html` — sp-doctors 1280→1440
- `templates/live_templates/medical/specialist/blog_list.html` — sp-posts 1100→1400
- `templates/live_templates/medical/specialist/contact.html` — sp-contact 1200→1400
- `templates/live_templates/medical/specialist/appointment.html` — sp-process 1200→1400, sp-form-band-inner 1100→1400
- `templates/live_templates/restaurant/fine-dining/_base.html` — fd-lead, fd-section 1280→1440
- `templates/live_templates/restaurant/fine-dining/home.html` — fd-manifesto 1100→1440 + inner 36ch→68ch (removed margin auto), fd-courses 1280→1440, fd-chef-inner 1280→1440
- `templates/live_templates/restaurant/fine-dining/about.html` — fd-timeline 1100→1440, fd-method-inner 1100→1440, fd-values 1280→1440
- `templates/live_templates/restaurant/fine-dining/menu.html` — fd-courses-full 1100→1400, fd-wine-inner 1100→1400
- `templates/live_templates/restaurant/fine-dining/gallery.html` — fd-rooms 1100→1400, fd-gallery 1280→1440
- `templates/live_templates/restaurant/fine-dining/reservations.html` — fd-process 1280→1440, fd-concierge-inner, fd-hours, fd-private-inner, fd-form-band all 1100→1400
- `templates/live_templates/restaurant/fine-dining/blog_list.html` — fd-posts 1100→1400

### Database delta
- Deleted stale TemplateAsset rows `id=5` (gusto-fine-dining-preview) and `id=6` (sapore-trattoria-pizzeria-preview) + their canonical PNG files.
- Re-ran `generate_previews --only gusto-fine-dining` and `--only sapore-trattoria-pizzeria` — created two fresh TemplateAsset rows pointing at the correct canonical filenames, rendered from the correct DNA archetype compositions.
- Total template / brand / asset counts unchanged (19 templates, 19 brands, 19 preview assets).

### Verified

*Listing card correctness:*
- `/templates/restaurant/` — three visibly distinct cards at thumbnail size: Brace (yellow brutalist), Sapore (bright cream scrapbook with polaroids), Gusto (fully dark editorial with charcoal + gold). Verified via `browser_evaluate` that each card's `img.src` points at the correct slug's PNG and that the SHA-1 hashes of the three fetched files are all different (5aec..., bf69..., cf3d...).
- Direct PNG navigation to `/media/.../gusto-fine-dining-preview.png?cb=1` confirms the new Gusto file is the dark Playfair editorial layout (NOT the legacy wood-interior).
- Direct PNG navigation to `/media/.../sapore-trattoria-pizzeria-preview.png?cb=1` confirms the new Sapore file is the bright cream polaroid scrapbook (NOT the legacy wood-interior).
- `/templates/medical/` regression check — still shows 4 distinct medical archetype cards.

*Layout width correctness:*
- Before/after side-by-side of Gusto home page (`/templates/restaurant/gusto-fine-dining/preview/`): the manifesto section now spans the full 1440px frame instead of sitting as a tiny centered column. The drop cap anchors the left edge. Timeline, course index, and chef portrait sections all breathe properly.
- Gusto filosofia (`/preview/filosofia/`): timeline rows span the wide frame, method block has generous 2-col layout, 4-up values grid uses the full width.
- Gusto menu (`/preview/menu/`): 8-course list is now wide enough that name + ingredients + wine pairing live together on one row without feeling cramped.
- Cardio home (`/preview/`): hero 2-col spreads wider, manifesto is a proper wide editorial column.
- Cardio studio (`/preview/studio/`): timeline + method block both widen correctly.
- Cardio pubblicazioni (`/preview/pubblicazioni/`): lead post 2-col spans the frame, list rows use the full width.
- Cardio article detail (`/preview/pubblicazioni/<slug>/`): still intentionally 760px narrow long-form reading column — preserved on purpose.

*Smoke test:*
- `python manage.py check` → 0 issues.
- 20 URLs via Django test client → all 200. Covered homepage, browse, both category listings, both pilot detail pages, all 7 Gusto inner pages, all 8 Cardio inner pages + the blog article detail.

### Key Findings (no new D-XXX decisions, but lessons logged)

- **`template.assets.first` is a bug magnet.** It returns "whatever's first by default ordering", which silently picks the wrong file the moment a template has multiple assets. Always filter by `asset_type` explicitly. The `WebTemplate.preview_asset` property encapsulates this rule once so templates never need to remember it.
- **Page-level max-widths of 1100-1280 are too narrow for 1600+ displays.** 1400-1440 is the new standard for wide content. Editorial narrow reading columns (blog articles) stay at ~720-800px — those are about line length, not frame width. Never double-constrain with outer `max-width` + inner `margin: 0 auto + max-width: Xch` on the same element tree — either widen the outer container and use `max-width: <NN>ch` on the text (left-aligned drop-cap anchored to the frame's left edge), or keep the outer narrow and drop the inner centering. The double constraint creates compositions that look "floating in a void".
- **The DNA-fallback timing trap is still live.** Gusto and Sapore's PNGs on disk were stale legacy renders, despite Session 10's claim of having regenerated them. Whatever the root cause (cross-branch drift, an unrecorded regen pass, worktree sync weirdness), the fix is the same: delete the asset row + file, re-run `generate_previews --only <slug>` without `--force` so the canonical filename lands clean. TODO_NEXT.md Phase 2d option (b) — "automatic --force whenever the DNA file or composition path on disk is newer than the preview's TemplateAsset" — would catch this class of bug structurally.

### Blockers
None. Both issues are fully resolved and validated end-to-end.

### Exact next step
Back to **Phase 2g.1 validation** — add a second template under an existing archetype (e.g. `tartufo-truffle-house` under `fine-dining`, or `dermatologia-elite-roma` under `specialist`) to prove the content-registry abstraction travels. With the wider width system and the `preview_asset` property in place, any new template picks up the improvements for free — no per-archetype CSS tweaks needed.

## Session 13 — Archetype Reuse Validation (2026-04-10)

**Agent:** Backend-Core + Content
**Worktree:** `archetype-reuse-validation`
**Goal:** Prove that a new full multi-page template can be added under an existing archetype with ONLY three edits — one seed row, one DNA entry, one content block — and ZERO new HTML files. Option B of the two validation paths proposed in Session 12's handoff: a second template on the Medical `specialist` archetype (`dermatologia-elite-roma`).

### The validation hypothesis
The Session 11 architecture was designed around a "content registry + per-archetype skin folder + single dispatcher view" separation. The theory: once an archetype's skin folder exists, dropping a new template under it should be a matter of editorial authoring (brand, palette, copy, images) rather than chrome rebuilding. Sessions 11 and 12 shipped two templates (Cardio + Gusto) but each was the *first* template under its archetype — the reuse path had never actually been exercised. Without a second template under an existing archetype, the reuse claim was untested.

### Chosen template
- **Slug:** `dermatologia-elite-roma`
- **Category:** medical
- **Archetype:** specialist (reused from `cardio-studio-specialistico`)
- **Brand:** Studio Ricciardi Dermatologia (Dott.ssa Alessandra Ricciardi + 2 colleagues)
- **Location:** Via Veneto 116, Roma (Ludovisi) — *not* Parioli, to make it visibly a different studio from the cardio pilot
- **Accent:** `#3d5437` forest green — *not* cardio's `#9c2a2a` clinical red
- **Font pairing:** `Bodoni Moda + Inter` — *not* cardio's `Cormorant Garamond + Inter`
- **Positioning:** Dermatologia clinica + chirurgica + estetica (3 pillars, different from cardio's clinical + second-opinion positioning)
- **Price:** €115 (vs. cardio €109)

### Actions taken
1. Read the specialist chrome files end-to-end (`_base.html`, `home.html`, `about.html`, `services.html`, `team.html`, `blog_list.html`, `blog_detail.html`, `contact.html`, `appointment.html`) to catalog every `{{ page_data.* }}` / `{{ site.* }}` / `{{ posts.* }}` key the chrome consumes — this is the "contract" a content block must satisfy. Also cataloged every *hardcoded string* in the chrome (cardio-specific text that content cannot override) to inform both the authoring constraints and the post-validation lesson log.
2. Added `SEED_TEMPLATES` entry for `dermatologia-elite-roma` in `apps/catalog/management/commands/seed_templates.py` with the new brand (name, tagline, palette, typography, personality, logo concept) — distinct from Cardio's across every dimension. Price €115, order=5, not featured.
3. Added DNA entry for `dermatologia-elite-roma` in `apps/catalog/template_dna.py` with `archetype="specialist"` and all the specialist defaults (hero_style, navbar_style, footer_style, section_order, card_style, button_style, density, tone, imagery_direction, imagery_key, conversion_pattern), but overriding `font_pairing` to `("Bodoni Moda", "Inter")` and populating a fresh `content` block for the preview composition.
4. Added `DERMATOLOGIA_CONTENT` dict to `apps/catalog/template_content.py` with the same structural key layout as `CARDIO_CONTENT` — 7 pages (home/studio/visite/medici/pubblicazioni/contatti/richiedi-visita), 5 blog posts (first with full `body` block), site-wide footer chrome data, and distinct Italian copy throughout: dermatology specialties, three dermatologhe with dermatopatologia/chirurgia/estetica roles, six treatment rows with pricing (visita €180 → percorso annuale €580), contact block pointing to Via Veneto 116, and a full "Modulo di richiesta" process block. Kept the `pubblicazioni` slug for the blog page because `blog_list.html` and `blog_detail.html` hardcode it in URL reverses.
5. Ran `python manage.py check` — 0 issues.
6. Ran `python manage.py seed_templates` — created one new row (`Dermatologia Elite — Studio Ricciardi`), all others untouched.
7. Verified the DB state via Django shell: slug present, category=medical, brand palette accent=`#3d5437`, `has_dna()` → True, `has_live_template()` → True, medical category now has 5 templates (was 4).
8. Ran the Django test client across all 9 routes with `ALLOWED_HOSTS=['*']` override for the in-process call:
   - `/templates/medical/dermatologia-elite-roma/` (marketplace detail) → 200
   - `/templates/medical/dermatologia-elite-roma/preview/` (home) → 200
   - `.../preview/studio/` → 200
   - `.../preview/visite/` → 200
   - `.../preview/medici/` → 200
   - `.../preview/pubblicazioni/` → 200
   - `.../preview/pubblicazioni/mappatura-nei-quando-farla/` (post detail) → 200
   - `.../preview/contatti/` → 200
   - `.../preview/richiedi-visita/` → 200
9. Content assertion sweep on the home page: confirmed the rendered HTML contains `Studio Ricciardi`, `carta d'identità`, `Bodoni Moda`, `#3d5437`, `Alessandra Ricciardi`, `JAMA Dermatology`, `Mappatura nevi digitale`, `Via Veneto 116`, and `2.400` — i.e., the new content is actually reaching the page, not silently falling back to Cardio's.
10. Cardio-leak sweep across all 8 dermatology pages: cataloged exactly which cardio-specific strings bleed through the chrome despite the content swap (see Findings below).
11. Regression sweep: 15 routes on `cardio-studio-specialistico` (all 7 inner pages + marketplace detail) and 8 routes on `gusto-fine-dining` (all 6 inner pages + blog detail + marketplace detail), plus homepage + `/templates/` + `/templates/medical/` + `/templates/restaurant/` — 19 total — ALL 200. No regression.

### Files Modified
- `apps/catalog/management/commands/seed_templates.py` — +29 lines (one new entry after Cardio)
- `apps/catalog/template_dna.py` — +42 lines (one new entry before Cardio, keyed as the "5th specialist" slot)
- `apps/catalog/template_content.py` — +355 lines (full `DERMATOLOGIA_CONTENT` block + one new line in `TEMPLATE_CONTENT` registry)
- `CATEGORY_ROADMAP.md` — marked specialist as hosting two templates
- `DECISIONS.md` — D-046 added
- `TEMPLATE_REGISTRY.json` — version bumped to 0.6.0, dermatologia entry added with `archetype_reuse: true` flag
- `TODO_NEXT.md` — Phase 2g.2 (copy-abstraction pass) added
- `AGENT_HANDOFF.md` — Session 13 section added
- `SESSION_LOG.md` — this entry

### Files NOT modified (the whole point of the validation)
- **Zero** HTML files touched. Not in `templates/live_templates/medical/specialist/`. Not in `templates/preview_compositions/`. Not in `templates/catalog/`. Not in `templates/includes/`. The Session 11 chrome absorbed the new template without a single `.html` edit. `git status` confirms three modified `.py` files and zero modified or new `.html` files.

### Database delta
- `+1` WebTemplate row (`dermatologia-elite-roma`)
- `+1` TemplateBrand row (`Studio Ricciardi Dermatologia`)
- `+0` TemplateAsset rows (no preview PNG generated — the validation is about the live preview, not the thumbnail)
- Total: 20 templates (was 19), 20 brands (was 19), 19 preview assets (unchanged)
- Medical category: 5 templates (was 4) — clinic, family, specialist ×2, wellness

### Verified end-to-end
- All 9 dermatology routes: 200 via Django test client
- Content correctly substituted: brand palette, fonts, headlines, facts, manifesto, signature visits, chief doctor name + bio, press list, all 7 inner pages, 5 blog posts, full body of the lead post
- Regression on Cardio + Gusto + marketplace pages: 19 routes, all 200
- `python manage.py check`: 0 issues
- `git status`: only 3 `.py` files modified, 0 HTML files touched

### Findings — the abstraction is **structurally reusable** but **editorially leaking**

The validation's primary hypothesis (routes 200 with zero HTML edits) succeeded on the first try. But the cardio-leak audit found that the specialist chrome was written as if Cardio would be its only tenant — cardio-specific text is baked into the HTML in seven distinct places, and **every** dermatology page shows at least one of them:

| Leak site                                 | Appears on       | What leaks                                                                  |
|-------------------------------------------|------------------|-----------------------------------------------------------------------------|
| `_base.html:240`                          | ALL 8 pages      | `© 2026 ... · Iscrizione OMCeO Roma 12 / 4408` (wrong license number)       |
| `home.html:199` (hero right quote)        | home             | `«La cardiologia non è una catena di montaggio. È un dialogo lungo ...»`     |
| `home.html:200` (quote author)            | home             | `— Lancet · 2024`                                                           |
| `home.html:203-205` (pulse triple)        | home             | `Roma · Parioli` / `2010` / `Cardiologia clinica`                           |
| `home.html:225` (section head)            | home             | `Sei percorsi clinici, una sola firma.` (literal cardio headline)            |
| `home.html:241` (section head)            | home             | `Una sola firma per ogni cartella.`                                         |
| `home.html:265` (CTA band)                | home             | `Ogni visita è concordata personalmente con il medico.`                     |
| `about.html:111` (values heading)         | studio           | `Quattro impegni che non cambiano mai.`                                     |
| `about.html:123-126` (CTA band)           | studio           | `Vuoi conoscere i medici dello studio prima di prenotare?` + `I tre medici dello studio →` (also assumes exactly 3) |
| `services.html:100` (CTA heading)         | visite           | `Una visita allo Studio Marani è concordata personalmente.` ← **literal brand name leak** |
| `team.html:70-72` (CSS portraits)         | medici           | 3 hardcoded Unsplash portrait URLs — caps the archetype at 3 doctors AND shows cardio's same photos for the dermatology team |
| `team.html:87` (portrait signature)       | medici           | `Roma · Parioli` (every doctor card)                                        |
| `blog_list.html:17` (lead post image)     | pubblicazioni    | Hardcoded Unsplash CSS background image                                     |
| `blog_list.html` + `blog_detail.html`     | pubblicazioni / post | `{% url ... 'pubblicazioni' %}` — the blog parent page slug is a literal, not looked up from the content registry |
| `blog_detail.html:120` (footer strap)     | post             | `Studio Marani · Cardiologia clinica` ← **literal brand leak**              |
| `appointment.html:142` (side-note)        | richiedi-visita  | Hardcoded marketing copy about "richieste compilate con cura"                |
| `appointment.html:166-180` (select)       | richiedi-visita  | Hardcoded visit-type options: `Prima visita / Secondo parere / Programma prevenzione / Visita di controllo` (the content registry `form_fields` list is never consulted for option rendering) |

The **Studio Marani brand name leaks twice** (services CTA + blog detail footer), the **Parioli district leaks twice** (home pulse + team portrait signature), and the **wrong medical license number** leaks on every single page. A real buyer would immediately see a mismatched brand mid-scroll.

**The abstraction is not broken — it's incomplete.** The contract (content registry keys the chrome consumes) is well-defined. The violation is that the original Session 11 authoring pass embedded cardio's *sample* copy directly as literals in the chrome, under the assumption that the chrome was still single-tenant. Fixing it requires moving those literals out of the HTML into the content registry (typically via new `site.*` or `page_data.*` sub-keys), NOT adding new HTML files.

### Why this doesn't block the validation result
The validation asked: "can a new template be created with one seed entry, one DNA entry, one content entry, and zero new HTML files?" The answer is **yes** — every route 200s, every content variable renders, the font/palette/nav all switch correctly. The leaks are a separate, pre-existing bug in the Session 11 authoring pass that the validation exposed. Without this validation we would not have found them.

### Key Decisions Made
- **D-046** added: formally documents the archetype-reuse validation result + the copy-leak finding + the Phase 2g.2 copy-abstraction lift plan

### Key Lessons for Future Archetype Authoring
1. **When building a skin folder that will host >1 template, every string that is NOT a CSS rule must come from context.** The sample copy used during Phase 1 authoring should not live in the HTML as a literal — it should live in the content block, and the HTML should read `{{ page_data.cta_heading }}` instead of inlining the heading. Concrete rules:
   - Section titles that vary by template → `page_data.<section>_heading`
   - CTA band headings and labels → `page_data.<section>_cta_heading` / `_cta_primary_label` / `_cta_secondary_label`
   - Pulse-bar / portrait-signature / footer-license values → `site.license`, `site.pulse_triple`, `medici.portrait_city`
   - Hero-sidebar quote + author → `home.hero_sidebar_quote` + `hero_sidebar_author`
   - URL reverses for page kinds (e.g. blog parent slug) → discovered from `pages` registry list at render time (find the entry where `kind == 'blog_list'`), not hardcoded
2. **Imagery in inline CSS is a reuse blocker.** `team.html`'s three nth-child background-image rules mean every template reusing the specialist chrome shares the same three doctor photos. Move to a `doctors[i].portrait` URL in the content registry, consumed via `style="background-image: url('{{ d.portrait }}')"`.
3. **The "pubblicazioni" slug lock is the most dangerous leak** because it silently limits the reuse pattern to templates whose blog parent page is literally named `pubblicazioni` — any other naming (e.g. `blog`, `news`, `diario`) causes a NoReverseMatch at the URL resolution step. The fix is to compute the blog parent slug in the dispatcher view and pass it as `blog_parent_slug` in context.
4. **The chrome's hardcoded 3-doctor cap** (via the three `nth-child` rules) means any fourth doctor added to a content block will render without a portrait. Move the portrait imagery into content and drop the cap.
5. **Validation must include a full leak audit, not just a 200-status check.** A 200 response proves the routes resolve; it does not prove the content swap is complete. Always grep the rendered HTML for the *previous* template's brand name and district/city to catch leaks early.

### Blockers
None. The validation produced a clean result *and* a clear action plan for the follow-up Phase 2g.2 work.

### Exact next step
**Phase 2g.2 — copy-abstraction lift pass on the specialist chrome.** Move every cardio-specific literal out of `templates/live_templates/medical/specialist/*.html` into either (a) new `site.*` fields consumed by `_base.html` (footer license, compact hours, etc.), (b) new `page_data.*` sub-fields consumed by each page file (section/CTA headings), or (c) new per-item imagery fields (`doctors[i].portrait`, `home.hero_sidebar.*`, `blog_list.lead_image`). Then update both `CARDIO_CONTENT` and `DERMATOLOGIA_CONTENT` to populate these new fields, and re-run the leak-audit sweep — it should show every dermatology page as clean of cardio-specific strings. After that, the next archetype-reuse template (e.g. a third specialist or the first fine-dining reuse) will ship without any copy polish.

After Phase 2g.2 closes, resume Phase 2f DNA rollout: Agency → Lawyer → Real Estate archetype splits, applying BOTH the Session 10 imagery-distinctness lesson and the Session 13 content-must-not-be-hardcoded lesson from the start of each new archetype's authoring pass.


## Session 14 — Specialist Copy-Abstraction Lift (2026-04-11)

**Agent:** Specialist Chrome Refactor
**Goal:** Execute Phase 2g.2 — move every cardio-specific literal out of the 9 files under `templates/live_templates/medical/specialist/` into structured fields in the content registry. Zero new HTML files. Preserve Cardio + Dermatologia behavior. Leave the chrome ready for a third specialist template with no copy polish needed.

### Branch / worktree
`specialist-copy-abstraction` (built on top of `archetype-reuse-validation` → ... → `template-dna-system`, **none merged to master yet**).

### What changed

**`apps/catalog/template_content.py`** — extended both `CARDIO_CONTENT` and `DERMATOLOGIA_CONTENT` with a structured set of new fields under their existing blocks. No new top-level keys, no new architectural concepts — every addition sits semantically where the chrome already consumed data:

| Block               | New fields                                                                                                                                                                   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `site`              | `license`, `hours_footer_rows` (list of strings)                                                                                                                             |
| `home`              | `hero_sidebar_top_label`, `hero_sidebar_quote`, `hero_sidebar_author`, `hero_sidebar_pulse` (list of `(label,value)`), `signature_visits_label`, `signature_visits_heading`, `signature_visits_intro`, `chief_label`, `chief_heading`, `press_label`, `cta_heading`, `cta_primary_label`, `cta_secondary_label`; and `home.chief.portrait` (per-chief URL) |
| `studio` (about)    | `values_label`, `values_heading`, `cta_heading`, `cta_primary_label`, `cta_secondary_label`                                                                                  |
| `visite` (services) | `footnote_heading`, `cta_heading`, `cta_primary_label`, `cta_secondary_label`                                                                                                |
| `medici` (team)     | `portrait_city`; and per-doctor `doctors[i].portrait` URL (removes the 3-doctor cap previously baked into `nth-child` CSS)                                                   |
| `pubblicazioni`     | `lead_image`, `footer_strap`, `empty_body_fallback_paragraphs` (list)                                                                                                        |
| `contatti`          | `form_placeholders` (dict: `first_name`/`last_name`/`email`/`phone`/`subject`/`message`), `hours_heading`, `transport_heading`                                               |
| `richiedi-visita`   | `process_label`, `process_heading`, `form_band_side_note`, `form_band_side_note_small`, `submit_label`; and `form_fields` **reshaped** from `(label, placeholder, type)` tuples into richer dicts: `{label, type, full_width, placeholder OR options}` — the template now loops over this instead of hand-writing the form |

**`apps/catalog/views.py`** — `LiveTemplateView.get_context_data()` now computes `blog_parent_slug` from the first page whose `kind == 'blog_list'`. This removes the D-044/Session 13 hard constraint that the blog parent page slug had to be literally `'pubblicazioni'`. (Dermatologia still calls its blog page `pubblicazioni` because the content was authored that way, but future templates can call it `diario`, `osservatorio`, `rassegna`, anything — the chrome no longer cares.)

**9 HTML files under `templates/live_templates/medical/specialist/`** — every cardio literal pulled out, replaced with `{{ page_data.* }}`, `{{ site.* }}`, loop iterations, or (for URLs) `blog_parent_slug`. Specifically:

- **`_base.html`** — footer license + hours footer rows now loop from `site.license` / `site.hours_footer_rows`. Removed hardcoded `OMCeO Roma 12 / 4408`, `Sabato · solo reperibilità`, `Domenica · chiuso`.
- **`home.html`** — hero right sidebar (top label, quote, attribution, pulse triple) now reads from `page_data.hero_sidebar_*`. Chief portrait URL moved from inline `background: url(...)` to inline `style="background-image: url('{{ page_data.chief.portrait }}')"`. Signature-visits section label/heading/intro, chief label/heading, press label, bottom CTA heading + two button labels all now come from `page_data.*`. Removed hardcoded Unsplash URL `photo-1559757148-5c350d0d3c56`.
- **`about.html`** — values label/heading + CTA band heading/primary label/secondary label all from `page_data.*`. Removed the "I tre medici" hardcoded count leak.
- **`services.html`** — footnote heading + CTA band heading/labels from `page_data.*`. Removed the "Studio Marani" brand-name leak (the most visible one in the entire chrome).
- **`team.html`** — the three `nth-child` CSS rules with hardcoded Unsplash URLs are **gone**. Each doctor now uses an inline `style="background-image: url('{{ d.portrait }}')"` computed from the content registry. The 3-doctor cap is removed — future specialist templates can have any number of doctors. Portrait signature reads `{{ d.portrait_city|default:page_data.portrait_city }}`.
- **`blog_list.html`** — lead post background image moved from CSS url() to inline style reading `page_data.lead_image`. All three hardcoded `'pubblicazioni'` URL reverses replaced with `blog_parent_slug`.
- **`blog_detail.html`** — both hardcoded `'pubblicazioni'` URL reverses replaced with `blog_parent_slug`. Breadcrumb and footer "Tutte le …" now use `{{ page.label }}` / `{{ page.label|lower }}`. Footer strap reads `page_data.footer_strap|default:site.logo_word`. Empty-body fallback paragraphs loop from `page_data.empty_body_fallback_paragraphs`.
- **`contact.html`** — form placeholders read from `page_data.form_placeholders` dict (keys: first_name, last_name, email, phone, subject, message). Sidebar headings `Orari di apertura` / `Come raggiungerci` now come from `page_data.hours_heading` / `page_data.transport_heading`.
- **`appointment.html`** — the hand-written `<form>` (8 fields, 2 hardcoded select blocks) **replaced** with a single `{% for f in page_data.form_fields %}` loop that handles `text`/`email`/`tel`/`number`/`textarea`/`select` via field-type branching and applies `full_width` to mark grid-full rows. The two select dropdowns that previously baked in Cardio's visit types now pull their options from `form_fields[i].options`. Process label, process heading, form band side note + small, and submit button label all from `page_data.*`.

### Database delta
None. Pure content + template refactor. 0 migrations, 0 seed changes, 0 new assets.

### Files touched
11 modified, 0 added, 0 deleted (verified via `git status`):

```
 M apps/catalog/template_content.py
 M apps/catalog/views.py
 M templates/live_templates/medical/specialist/_base.html
 M templates/live_templates/medical/specialist/about.html
 M templates/live_templates/medical/specialist/appointment.html
 M templates/live_templates/medical/specialist/blog_detail.html
 M templates/live_templates/medical/specialist/blog_list.html
 M templates/live_templates/medical/specialist/contact.html
 M templates/live_templates/medical/specialist/home.html
 M templates/live_templates/medical/specialist/services.html
 M templates/live_templates/medical/specialist/team.html
```

### Validation — it works

1. **`python manage.py check` — clean.**
2. **Full route sweep — 25/25 green via Django test client:**
   - Cardio: marketplace detail + 7 inner pages + 1 post detail = 9 routes (200)
   - Dermatologia: marketplace detail + 7 inner pages + 1 post detail = 9 routes (200)
   - Gusto regression: marketplace detail + 6 inner pages + 1 post detail = 8 routes (200)
3. **Cardio-leak sweep on dermatologia — ZERO leaks.** The sweep grepped the rendered HTML of all 8 dermatology pages for 26 cardio-specific literals (`Marani`, `OMCeO Roma 12 / 4408`, `cardiologia`, `Cardiologia`, `Parioli`, `catena di montaggio`, `Lancet`, `Riccardo Marani`, `Margherita Salieri`, `Andrea Lombardi`, `Salieri`, `Lombardi`, `Prima visita`, `Secondo parere`, `Programma prevenzione`, `Visita di controllo`, `ecocardiograf`, `Holter`, `ECG`, `Policlinico Umberto`, `Sant'Andrea di Roma`, `Braunwald`, `Institut de Cardiologie`, `Piccione`, `Tarbouriech`, `cardiolog`). **All 8 pages came back clean.** Session 13's 17 distinct leaks are now 0.
4. **Positive content sweep on Cardio — 52 expected cardio strings, all present.** The rendered Cardio HTML still contains every hallmark string (Studio Marani, Lancet quote, Riccardo Marani, Roma · Parioli, Richiedi visita privata, Ogni visita è concordata, Prima visita, Secondo parere, Programma prevenzione, Visita di controllo, Pubblicato su, all three doctor portraits by photo ID, the Studio Marani · Cardiologia clinica footer strap on the blog detail page, etc.). No regression.
5. **Positive content sweep on Dermatologia — 46 expected dermatology strings, all present.** Rendered HTML contains Studio Ricciardi, Alessandra Ricciardi, Via Veneto, JAMA Dermatology, Quattro aree cliniche, Un solo archivio, Cosa garantiamo, Le tre dermatologhe, Mappatura nevi, Chirurgia dermatologica, Medicina estetica, Invia richiesta, Studio Ricciardi · Dermatologia integrata footer strap, and the three new dermatologia portrait photo IDs (1594824476967, 1582750433449, 1666214280557). The derm content block still drives every field it used to drive.
6. **Template file grep — ZERO hardcoded Unsplash URLs** in any of the 9 specialist chrome files (was 4 before: 3 nth-child portraits in `team.html`, 1 chief portrait in `home.html`, 1 blog lead in `blog_list.html`).
7. **Template file grep — ZERO cardio-brand literals** in any of the 9 specialist chrome files. Previously every file leaked.

### What the chrome now guarantees

Every string in the 9 specialist chrome files now either:
- is a CSS rule (tokens, colors, fonts, layout), or
- is a generic archetype label (`Nome`, `Cognome`, `Email`, `Telefono`, `Oggetto`, `Messaggio`, `Invia messaggio`, `Privacy`, `Cookie`, `Note legali`, `Anteprima completa`, `← Torna a MarketWeb`, `Altri template medicali →`, `Tutti i medici`, `Lo studio`, `Pagine`, `Contatti`, `Orari`, `Leggi l'articolo completo`, `In alternativa:`, `parla con la segreteria`, `min di lettura`, `© 2026`), or
- is a template context variable (`{{ site.* }}`, `{{ page_data.* }}`, `{{ d.* }}`, `{{ post.* }}`, `{{ blog_parent_slug }}`, etc.), or
- comes from a `{% for %}` loop over a content registry list.

### Chrome-authoring contract (new — D-047)

Any future per-archetype skin (e.g. the Agency `editorial-quiet` skin, the Lawyer `modern-transparent` skin) must follow the same rule from its first authoring pass:

> **Every string in a per-archetype skin must either be a CSS rule or come from `site.*` / `page_data.*` / loop items. No literal brand names. No literal city names. No literal quotes. No literal CTA labels. No literal form select options. No hardcoded image URLs.**

Session 13's leak cost the next reuse template zero-copy-polish ambition. This contract prevents that from happening a second time.

### Lessons from Session 14

1. **"Abstract the literals, not the structure."** The chrome's visual structure (grid layouts, typography, colors, spacing, the `.sp-lead`/`.sp-section`/`.sp-chief`/`.sp-doctors`/`.sp-form-band` class system) was already correct. The leak was purely textual — every fix was a one-line `{{ page_data.X }}` substitution. This is a good sign for future reuse passes: if the visual identity is clean, a leak audit is genuinely mechanical.
2. **`form_fields` as dict-of-dicts beats tuples.** The old `(label, placeholder, type)` tuple format couldn't represent select options or full-width rows without the chrome hand-writing them. Switching to `{"label":..., "type":..., "placeholder":..., "options":[], "full_width":bool}` let the chrome template become a single generic form loop. This pattern is now the reference for any future archetype that has a form.
3. **`blog_parent_slug` is the simplest way to kill the hardcoded-URL-reverse trap.** Computing it once in the view from `pages[i].kind == 'blog_list'` means every blog URL reverse in the chrome becomes `{% url '...' cat slug blog_parent_slug post.slug %}`. No content block ever needs to know its own slug. This is the D-044 permanent fix (was: "the blog parent page slug must be literally `pubblicazioni`" — it is no longer).
4. **`nth-child` for per-item imagery is the hidden item-count cap.** The three `team.html` CSS rules (`nth-child(1)`, `nth-child(2)`, `nth-child(3)`) didn't just hardcode URLs — they capped the number of doctors at 3 and the chrome silently broke on a fourth. Moving portraits to per-doctor inline styles both fixes the URL leak AND removes the cap. General rule: **any per-item visual data that varies should live on the item, not the chrome.**
5. **Positive sweeps matter as much as negative sweeps.** Grepping for cardio literals proves the leak is gone. Grepping for dermatology's OWN hallmark strings proves the content block is still wired to every field the chrome reads. Both sweeps passed on the first run after the refactor — a good signal that the refactor was faithful.

### Blockers
None. Phase 2g.2 closes cleanly. The specialist archetype is now truly reusable.

### Exact next step
**Phase 2f continuation — add a second fine-dining template (e.g. `tartufo-truffle-house`) under the Gusto chrome and repeat the same leak-audit sweep on the `templates/live_templates/restaurant/fine-dining/` chrome.** Expect the same class of leaks there — brand-name strings, hardcoded Unsplash URLs for the chef portrait and dish photos, possibly hardcoded menu course counts or wine region labels in the `menu.html` file. Apply the exact same abstraction pattern: extend the content registry with structured fields, move every literal out of the HTML, re-run the 25-route sweep, re-run the leak sweep. When that closes, the archetype-reuse validation officially extends to both specialist AND fine-dining — and the pattern is proven general.

After that, resume Phase 2f DNA rollout: Agency → Lawyer → Real Estate archetype splits, applying **all three** lessons from the session arc: Session 10's imagery-distinctness rule, Session 11's content-registry-as-registry rule, Session 13's leak-audit-with-rendering-grep rule, and Session 14's chrome-authoring-contract rule (D-047) from the first authoring pass of every new skin.
