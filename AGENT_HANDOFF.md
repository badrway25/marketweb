# Agent Handoff

Last updated: 2026-04-11 — after **Session 23 i18n/RTL Pilot Cardio (Phase 2i.1)**

## 🌐 Session 23 — i18n/RTL Pilot Cardio: Read This If You're Touching Localization (2026-04-11)

**Session 23 shipped the first multilingual publishing architecture on a `tier=published_live` template.** Cardio-studio-specialistico now renders in 5 locales (it/en/fr/es/ar) with real RTL for Arabic. This is the reusable recipe for Phase 2i.2 rollout to dermatologia and gusto. Short read, load-bearing:

- **D-059 — i18n/RTL Pilot Architecture.** Locale-keyed content registry (`TEMPLATE_CONTENT[slug][locale] → content tree`) + `CHROME_I18N[locale][key]` dict for the ~30 chrome labels the skin itself renders + `?lang=xx` query-param resolved in `LiveTemplateView.setup()` + RTL-scoped CSS block inside each archetype `_base.html`. **No Django `{% trans %}` / `.po` / `gettext` tooling** was introduced — the pilot's job was to prove the shape with ZERO new build tooling. Phase-later migration to `{% trans %}` for the marketplace chrome itself is trivial because every string is already locale-namespaced.
- **Where it shipped:** `apps/catalog/template_i18n.py` (new) + `apps/catalog/template_content_cardio_i18n.py` (new, 4 non-IT content trees) + `apps/catalog/template_content.py` (top-level shape changed to `{slug: {locale: tree}}`, derm/gusto wrapped under `{"it": ..._IT}`) + `apps/catalog/views.py` (`LiveTemplateView` threads locale) + all 9 specialist skin files (`_base.html` + home/about/services/team/contact/appointment/blog_list/blog_detail; `team.html` needed zero edits).
- **Validation:** 51/51 smoke test green (45 cardio routes × 5 locales + 6 regression/negative). Playwright walk at 1440×900 on IT/EN/AR/FR/ES home + AR contact + FR services + ES blog detail confirmed layout integrity. Mobile sanity at 390×844 confirmed zero new horizontal overflow.
- **Rejected:** Django `{% trans %}` (build-step tooling, splits strings across files), `django-modeltranslation` (wrong shape for structured content), per-locale URL maps (out of pilot scope), machine translation (violates premium positioning).

### What's next for the i18n pilot (Phase 2i.2, in order)

**Step 1 — Dermatologia (cheapest, same skin):**
- [ ] Create `apps/catalog/template_content_dermatologia_i18n.py` with 4 hand-authored content trees (EN/FR/ES/AR). Use the Session 23 voice guidelines: EN Anglo-American clinical, FR classical French + `vous`, ES peninsular, AR formal MSA + native punctuation (« »).
- [ ] Update `TEMPLATE_CONTENT["dermatologia-elite-roma"]` in `template_content.py` to import all 5 locale keys.
- [ ] Run the route sweep + Playwright walk.
- [ ] Budget: ~1.5h — no new HTML, no new CSS, the specialist skin's RTL block is already in place.

**Step 2 — Gusto (adds a new RTL CSS block for the fine-dining archetype):**
- [ ] Create `apps/catalog/template_content_gusto_i18n.py` with 4 hand-authored content trees for the 7 gusto pages. **Note the tone differs** — gusto is dark-editorial Michelin fine dining, not medical clinical. EN is "one service per night" not "a tailored consultation". AR needs Arabic restaurant vocabulary, not medical vocabulary.
- [ ] Author a new `html[dir="rtl"] ...` CSS block inside `templates/live_templates/restaurant/fine-dining/_base.html`. Copy the shape from the specialist `_base.html` RTL block and rename the selectors (`.sp-*` → `.fd-*`). Flip `.fd-nav`, `.fd-hero`, `.fd-chef .portrait`, `.fd-courses`, `.fd-form-band`, etc.
- [ ] Gusto's `_base.html` has its own set of ad-hoc literal labels (different from specialist). Either extend `CHROME_I18N` with the additional keys or factor a per-archetype extension pattern. Decision deferred to the next session.
- [ ] Budget: ~3h — new content trees + new RTL CSS + chrome wiring.

### Do NOT do (i18n pilot scope)

- Do NOT introduce Django `{% trans %}` / `.po` / `gettext` tooling. D-059 is explicit about this.
- Do NOT translate draft templates. Only `tier=published_live` templates are in Phase 2i scope.
- Do NOT translate the marketplace chrome (homepage, listing, detail, category). That's a Phase 4 decision.
- Do NOT use machine translation on any locale block. The pilot's quality floor is native editorial voice. A PR that ships auto-translated content should be rejected.
- Do NOT change URL patterns to add per-locale prefixes (`/en/preview/...`). The pilot uses `?lang=xx` query param and the URL pattern file is untouched. Prefix routing is a Phase 4 decision tied to the marketplace chrome migration.
- Do NOT translate page slugs. Only labels change per locale. `studio`, `visite`, `medici`, `pubblicazioni`, `contatti`, `richiedi-visita` stay Italian across every locale — avoids per-locale URL maps and works for Arabic (ASCII URLs).
- Do NOT remove the IT fallback in `pick_localized`. The transitional shape where derm+gusto get English CHROME but Italian CONTENT is load-bearing during Phase 2i.2 rollout — templates without a locale block must still render.
- Do NOT strip Latin from the Arabic font stack. The font-family override for `--heading` and `--body` keeps `{{ theme.heading_font }}` as a fallback so mixed Latin/Arabic strings (doctor names, press outlets, dates, phone numbers, addresses) stay legible.
- Do NOT apply negative `letter-spacing` or 0.22em uppercase tracking on Arabic h1-h5 or chrome labels. Arabic glyphs don't want Latin typographic conventions — the `html[dir="rtl"]` block zeroes them explicitly.

### Gotcha: Django template variable identifiers cannot begin with `_`

First draft of `_base.html` used `{% url ... as _base_url %}` inside the language switcher loop. Django's `FilterExpression` rejected it with `TemplateSyntaxError: Variables and attributes may not begin with underscores: '_base_url'`. Renamed to `lang_base_url`. If you see this error in any future work, the fix is always "rename the variable to remove the leading underscore".

### Gotcha: stale runserver (same class as Session 19 + 22)

First browser walk showed zero language pills because the `runserver --noreload` process on port 8765 was still serving the pre-edit HTML from memory. Killed + restarted on port 8766 — correct fresh HTML. Lesson unchanged from prior sessions: if the browser walk shows "my edits aren't landing" but the file-on-disk confirms they ARE, restart runserver on a fresh port before blaming anything else.

---

Previous (still relevant):
Last updated before Session 23: 2026-04-11 — after **Session 22 Motion Pilot Gusto (Phase 2g2x.9)**

## 🎬 Session 22 — Motion Pilot Gusto: Read This If You're Animating Anything (2026-04-11)

**Session 22 added a small, reusable, dependency-free premium motion system to the first tier=published_live template.** This is the interaction-quality floor for every future `published_live` template. Short read, but load-bearing:

- **D-058 — Live Motion Language.** Two static files — `static/css/live-motion.css` + `static/js/live-motion.js` — exposing a 3-attribute contract (`data-lm="reveal|reveal-lg|reveal-soft|counter"`, `data-lm-stagger`, `data-lm-to`) plus a wrapper+inner-bg image-hover pattern. Strictly opt-in per skin: one `<link>` in `<head>` + one `<script defer>` before `</body>`. No-JS fallback via `body.lm-ready` gate. Reduced-motion via `@media` + `body.lm-reduced` double guard.
- **Where it shipped:** `templates/live_templates/restaurant/fine-dining/_base.html` links the two files, and all 7 inner pages (home / menu / about / gallery / reservations / blog_list / blog_detail) tag their reveal targets.
- **Patterns used:** scroll-reveal (fade + rise), staggered children (70–110ms unit), count-up on home facts (suffix preserved), image-zoom on hover (900ms slow scale via inner `.bg` layer inside an `overflow: hidden` wrapper), CTA arrow shift + letter-spacing widening, nav underline sweep.
- **Rejected:** parallax, sliders, bounce easing, blur-in, loud marquees. See SESSION_LOG Session 22 § 1.

### What's next for the motion pilot (not blocking Phase 2g3, but cheap)

**Opt-in pass for the other two `published_live` templates:**
- [ ] Cardio (`templates/live_templates/medical/specialist/_base.html`) — link motion CSS + JS, tag reveals on the specialist skin pages. Should be a short session because the chrome is already D-047 clean. Dermatologia-elite-roma shares the same skin so it benefits for free.
- [ ] BRAND_SYSTEM_GUIDELINES.md gets a new "Motion Language" pointer section citing D-058.

**Phase 2g3 impact:**
- Every template flipped from `draft` → `published_live` MUST adopt the motion pilot as part of its D-053 acceptance checklist. The checklist in TODO_NEXT.md § 2g3.0 grew a new row: "Motion pilot adopted — reveal + stagger on home page at minimum, counters where numeric facts exist, image-hover where image frames exist." This is the interaction-quality floor; minimum opt-in is cheap (link + script + a handful of attributes).

### Do NOT do (motion pilot scope)

- Do NOT add the motion pilot to the marketplace surface (`base.html`, listing pages, detail page). The system is scoped to standalone live-template skins. The marketplace has its own interaction language.
- Do NOT apply motion to the preview composition files under `templates/preview_compositions/`. Those files are captured as static PNGs by Playwright and the reveal hidden-state would produce blank screenshots.
- Do NOT add heavyweight animation libraries (GSAP, AOS, Framer Motion, LocomotiveScroll). The whole point of the pilot is zero dependencies. If a specific archetype needs something the pilot doesn't offer, extend the pilot — don't bypass it.
- Do NOT break the no-JS fallback. The `body.lm-ready` gate is load-bearing: without it a JS-disabled user sees a blank page.
- Do NOT skip `prefers-reduced-motion`. Both the `@media` rule AND the `body.lm-reduced` class must continue to collapse motion cleanly.
- Do NOT apply `data-lm-stagger` to a parent whose direct children use `display: contents` — opacity/transform don't work on box-less elements. Fall back to plain `data-lm="reveal"` on the wrapper. See SESSION_LOG Session 22 § 5 "gotchas".
- Do NOT bulk-apply `data-lm="reveal"` to every element. The pilot is a judgment-call tool, not a batch-apply one. The Gusto adoption picked ~18 reveal targets on the home page out of ~50+ eligible elements — the unchosen ones stay instant so the cadence has contrast.

### Gotcha: stale runserver

Session 22 hit a Windows + StatReloader edge case where the initial runserver process kept serving pre-edit HTML after rapid template file changes, even though the files on disk had the updates. Killing the process and restarting on a fresh port produced the correct fresh HTML. Same class of repro as Session 19's ghost dev-server. If you ever think "my edits aren't landing" but `grep` of the files confirms they ARE on disk, just restart runserver before blaming template cache or ALLOWED_HOSTS.

---

## 🛑 Session 20 — Policy Binding: Read This Before Anything Else (2026-04-11)

**Session 20 was documentation-only — no code, no HTML, no previews, no commits of anything except doc deltas.** But it re-defined the product's floor with four formal decisions you MUST read before touching any catalog-facing work:

- **D-053 — Live Preview Law.** A template is `published_live` only when it has DNA + content registry + skin folder + all routes 200 + D-047 leak sweep clean + visual walk + card-size sibling test + preview PNG + working CTA. No exceptions.
- **D-054 — Premium Differentiation Law.** Every sibling pair must differ on 10 dimensions (hero image / dominant imagery / silhouette / section order / CTA phrasing+pattern / block rhythm / macro tone / imagery direction / typography / inner pages). Applies globally, retroactively, across every category and every template.
- **D-055 — Template Tier Model.** Two tiers only: `published_live` (public) / `draft` (hidden). No intermediate `published_static`. Today only 3 of 20 templates satisfy `published_live` — the other 17 must be demoted to `draft` in Phase 2g2x.8.
- **D-056 — Catalog Honesty.** The legacy `href="#"` "Anteprima Live" CTA gets deleted as part of Phase 2g2x.8. D-045 is superseded. Phase 2g2x.7's three-option punch list is absorbed by tier gating.

Read `DECISIONS.md` D-053 → D-056 in full before you start. They are the source of truth. This file is the summary.

### What's next — in order, no skipping

**Step A — Finish Phase 2g2x.1 on 3 CRITICO categories** (still the blocking roadmap gate per D-049):
- `real-estate.html` identity crash (Casa mass-market vs Villa ultra-luxury) — recommended first, cleanest pair
- `lawyer.html` identity crash (Lex 1962 heritage vs Juris modern/accessible) — second
- `agency.html` identity crash (Vertex bold vs Aura minimal — 6 shared fake case studies) — third, heaviest leak surface
- Use the Session 17 + Session 18 Option A recipe. Author under D-047 from line one. Bidirectional leak sweep + route sweep + Chromium visual walk per category.

**Step B — Phase 2g2x.8 tier migration** (cheapest implementation wave that makes the policy bind):
- Add `tier` field to `WebTemplate` (or repurpose `status`)
- Seed cardio / dermatologia-elite-roma / gusto-fine-dining as `published_live`, everyone else as `draft`
- Filter listing / detail / homepage / category / search to `tier='published_live'`
- Delete the `href="#"` branch in `templates/catalog/template_detail.html` lines 132-136 and the `has_live_preview` context var
- Ship a category-page empty state ("in arrivo") for categories that temporarily show zero live templates
- Add staff `?preview=1` escape hatch for in-progress work
- Exit criteria in `TODO_NEXT.md` Phase 2g2x.8

After Step B lands, the visible catalog is 3 real, complete, navigable products. That is the policy-compliant floor.

**Step C — Phase 2g3 live-preview rollout** (the long wave that brings the 17 drafts up to `published_live`):
- Order: restaurant → medical → business → portfolio → ecommerce → agency/lawyer/real-estate (last three blocked until Step A closes)
- Per-template acceptance checklist in `TODO_NEXT.md` Phase 2g3.0 — run it end-to-end on every single template
- Baseline live page-kind set per category in `CATEGORY_ROADMAP.md` — every skin must cover the baseline minimum
- Phase 2g3.7 exit criteria = Phase 3 unblock gate. Auth / checkout / editor / projects / commerce do NOT start before this gate.

### Do NOT do

- Do NOT open auth / checkout / editor / projects / commerce / dashboard — these are gated on Phase 2g3.7 per D-049 + D-053
- Do NOT add new categories or new templates before the 20 existing ones are all `published_live`
- Do NOT ship a template with "home page only + inner pages coming later" — D-053 says the inner pages are part of the gate
- Do NOT introduce a `published_static` tier or any variant — D-055 rejected Options B/C/D explicitly
- Do NOT preserve the `href="#"` CTA in any form — D-056 deletes it
- Do NOT treat the Premium Differentiation Law as optional polish — D-054 is a hard gate
- Do NOT skip the category-page empty state when a category becomes temporarily empty — leaving a ghost grid is worse than showing "in arrivo"

### Doc delta from Session 20

Touched in this session:
- `DECISIONS.md` — added D-053, D-054, D-055, D-056 (marked D-045 as superseded in the D-056 consequences)
- `TODO_NEXT.md` — added Phase 2g2x.8 (tier migration) + Phase 2g3 (live preview rollout, 2g3.0–2g3.7)
- `CATEGORY_ROADMAP.md` — added baseline live pages per category + rollout order + cumulative milestones + category-ready test
- `BRAND_SYSTEM_GUIDELINES.md` — added Premium Differentiation Law pointer (appendix)
- `CONTENT_GUIDELINES.md` — added Inner Pages Law pointer (appendix)
- `TEMPLATE_REGISTRY.json` — v0.7.3 → v0.8.0, `tier` field on every row
- `SESSION_LOG.md` — Session 20 entry prepended
- `AGENT_HANDOFF.md` — this section
- `memory/live_preview_policy_session20.md` + `memory/MEMORY.md` index — new auto-memory entry

Not touched: any code, any HTML, any CSS, any preview PNG, any migration, any view, any seed, any CLAUDE.md.

---

## ✅ Session 19 — Portfolio Blocker Cleared (2026-04-11)

**Session 18 declared portfolio approved, but a manual verification pass found a real layout-overflow bug in Chiara's detail preview.** A strictly-scoped Session 19 triage confirmed the bug was reproducible, surgically fixed it with the minimum possible footprint, and cleared the commit blocker.

### The fix (D-052)
- `templates/preview_compositions/portfolio/editorial-designer-grid.html`: `.ed-hero` padding tightened (72 72 42 → 52 72 38), `overflow: hidden` added as safety net; `.ed-left h1` dropped from 82 px to 62 px with matching line-height / letter-spacing / margin-top / max-width adjustments; `.ed-left .sub` + `.ed-left .cta-row` margins tightened.
- `apps/catalog/template_dna.py`: `chiara-portfolio-creativo.content.headline` trimmed from 57 chars to 47 chars. New headline: `'Identità visive, <em>una griglia alla volta</em>.'`. Both key signals preserved (`identità visive` = profession, `una griglia alla volta` = craft metaphor). The trim also creates a deliberate syntactic parallel with Pixel's `'Fermare il tempo, una luce alla volta.'` — both siblings now use the `'…, una X alla volta.'` structure with X being the medium of each profession.

### Validation that held (Session 19 delta)
- `python manage.py check` — clean
- `python manage.py generate_previews --only chiara-portfolio-creativo --force` — green
- Orphan cleanup — all three `_<hash>.png` intermediate files removed, final asset restored to canonical `chiara-portfolio-creativo-preview.png` via shell (media/ now has exactly one PNG per template)
- Playwright visual walk at 1440×900 on a fresh dev server: portfolio listing, Chiara detail, Pixel detail all clean, zero overlap. Differentiation vs Pixel strengthened (not weakened) via the headline parallel.

### Three operational gotchas surfaced during Session 19

1. **Stale dev-server ghost.** The first browser walk showed legacy "Ogni progetto una storia" content in the Chiara detail page. Root cause: a **stale `runserver --noreload` process (PID 29132)** was still listening on port 8765 from a prior session's worktree and serving a completely different PNG at the same URL as what was physically on disk. **Before any visual walk, kill lingering `runserver` processes on your target port** — or just use a fresh port. Python `urllib.request.urlopen()` + a cache-busting `?v=N` query string is the fastest way to confirm the dev server is serving the same bytes as disk.
2. **`generate_previews --force` creates orphan files.** Django's `FileSystemStorage.get_available_name()` appends a `_<hash>.png` suffix when the target filename exists, and `generate_previews.py:211-216` deletes the DB row but not the old file. Each `--force` run stacks a new orphan on top of the previous one. This is the Phase 2g2x.5 structural trap with one more concrete repro. For now, manually clean up post-regen and rename back to the canonical filename + update DB via shell. Permanent fix still deferred.
3. **"Anteprima Live" CTA is a legacy `href="#"` placeholder** for 17 of 20 templates (every template that isn't cardio / dermatologia / gusto). This is NOT a portfolio-scope bug — it's D-045's intentional gating meeting a legacy placeholder label. Do not fix in any per-category hardening session. Tracked as TODO_NEXT.md Phase **2g2x.7** with three remediation options.

## ⛔ ROADMAP STILL PAUSED — 3 of 5 CRITICO categories remain

**Per D-049 (Session 16), the roadmap is paused until Phase 2g2x closes.** Session 17 closed **business** (D-050). Session 18 closed **portfolio** (D-051) + Session 19 cleared its blocker (D-052). The remaining 3 identity-crash CRITICO categories are still open:
- `real-estate.html` hardcodes "600+ immobili · €500K–€1.2M mass-market" → Villa (ultra-luxury) shows mass-market language
- `lawyer.html` hardcodes "Studio legale dal 1962" → Juris (modern) shows Lex's 60-year heritage
- `agency.html` hardcodes 6 fake case-study names → both Vertex and Aura show the same clients

## ✅ Session 18 — Portfolio Closed (2026-04-11)

**Portfolio is no longer an identity-crash pair.** Chiara and Pixel are now split into two distinct DNA archetypes:
- `chiara-portfolio-creativo` → `editorial-designer-grid` archetype (cream paper `#f3efe5`, Syne + Inter, typographic hero with NO big photo, project index card with numbered ledger, 3-card case-study panel, clients ribbon + studio coordinates split footer, "Richiedi il portfolio completo" ghost sans-rule CTA, `portfolio-designer` imagery pool)
- `pixel-portfolio-fotografico` → `cinematic-photographer` archetype (near-black `#050505`, Archivo + Inter uppercase tracked, fullbleed dominant photo hero with corner frame marks and series-counter chip, monospaced EXIF credit bar pinned to hero bottom, 4-frame filmstrip gallery of series stills, 4-cell EXIF footer, `[ Apri la serie completa ]` ghost-bracket CTA, `portfolio-photographer` imagery pool)

Both skins were authored under the D-047 chrome-authoring contract from the first line — zero literal brand strings, zero hardcoded image URLs. The bidirectional leak sweep (52 tokens tested) returned zero cross-tenant contamination in both directions. The listing HTML leak sweep for all 9 legacy literals returned zero matches. Django test client returned 200 on all 5 portfolio routes. Visual regression at 1440×900 on `/templates/portfolio/` via Playwright MCP confirms the two cards read as two completely different products AND two completely different professions at card size — Chiara is unambiguously a designer studio (typographic grid, project ledger, clients ribbon with "CASA EDITRICE · FESTIVAL POESIA · FONDAZIONE · VINO D'AUTORE · MUSEO CIVICO · RIVISTA D'ARCHITETTURA") and Pixel is unambiguously a photographer ("FERMARE IL TEMPO, UNA LUCE ALLA VOLTA", EXIF bar with "Pellicola Medio formato 120 · Ottica Fisso 80mm · f/2.8 · Stampa Fine art · tiratura 12", filmstrip with 4 named series: "Le ore rubate / Campi lunghi / Stanze vuote / La città senza persone").

**Key insight reaffirmed for the next 3 categories:** The editorial-designer-grid archetype is **deliberately typographic (no big hero photo)**, so the Chiara card's readability does NOT depend on any single image URL. The hero IS the typography. This is the right pattern whenever the sibling's "visual opposite" has a weak image pool or you want to de-risk against image-download failures. The cinematic-photographer archetype is the opposite — the hero IS the photograph. Choose which side of this dichotomy each sibling lands on *before* authoring the composition.

**The Session 18 recipe (plus Session 17) is now a proven template for the remaining 3 CRITICO categories.** See SESSION_LOG.md Session 18 for the full Chiara-vs-Pixel differentiation matrix, bidirectional leak-sweep method, and the 52-token list for the sweep. See D-051 for the architectural decision rationale.

## ✅ Session 17 — Business Closed (2026-04-11)

**Business is no longer an identity-crash pair.** Pragma and Elevate are now split into two distinct DNA archetypes:
- `pragma-corporate-suite` → `corporate-suite` archetype (institutional navy + boardroom photo, Merriweather serif, advisory pillar cards + KPI strip, "Fissa una call privata" ghost CTA, `business-corporate` imagery pool)
- `elevate-startup-landing` → `startup-saas-landing` archetype (cosmic gradient, Manrope sans, typographic manifesto with NO big photo, glowing product-mockup card, "Inizia gratis" glow pill + "Guarda la demo" secondary, `business-startup` imagery pool)

Both skins were authored under the D-047 chrome-authoring contract from the first line — zero literal brand strings, zero hardcoded image URLs. The bidirectional leak sweep returned zero cross-tenant contamination in both directions. Django test client returned 200 on all 5 business routes. Visual regression at 1440×900 on `/templates/business/` confirms the two cards read as two completely different products at card size.

**The Session 17 recipe is the template for the remaining 4 CRITICO categories.** See SESSION_LOG.md Session 17 for the full differentiation matrix, leak-sweep method, and lessons-for-next-category list. See D-050 for the architectural decision rationale (Option A DNA split vs Option B lifted shared composition — Option A won and should stay the default).

**Additionally**, 4 single-tenant DNA archetype files have 10+ latent D-047 literal leaks each that will detonate on reuse:
- `ecommerce/fashion-editorial.html` — 12+ Luxe literals
- `ecommerce/artisan-workshop.html` — 10+ Bottega literals
- `restaurant/trattoria-warm.html` — "Trastevere · dal 1987"
- `restaurant/fine-dining/*.html` live skin — 5 files leak Gusto (Phase 2g.3 already planned)

**And**, 17 of 20 templates are single-page previews only. The marketplace positions as "complete multipage websites" but delivers landing-page posters for 85% of the catalog.

### What the next agent does first

1. Read `SESSION_LOG.md` Sessions 17 and 18 for the hardening recipe (portfolio is the most recent proven template; business is the first). Session 18 adds the "typographic-led vs image-led" dichotomy insight for choosing which sibling gets which side.
2. Read `DECISIONS.md` D-049 (blocking rule), D-050 (Option A DNA split default), and D-051 (portfolio validation of the default).
3. Read `TODO_NEXT.md` Phase 2g2x for the exact punch list (2g2x.1 through 2g2x.6). Business AND portfolio (2g2x.1) are marked `[x]`; the next 3 are open.
4. Pick **ONE** of the remaining 3 CRITICO categories and run the Session 17/18 recipe end-to-end:
   - **Recommended order:** real-estate (next cleanest "far apart" pair — Casa's mass-market vs Villa's ultra-luxury) → lawyer → agency (largest leak surface with 6 case-study wordmarks). This front-loads the cleanest wins while the recipe is fresh and back-loads the heaviest lift.
   - For each: add 2 archetype entries to `template_dna.py` (vocabulary + 2 DNA content blocks), add 2 imagery pools to `preview_imagery.py` (hand-verify URLs download), author 2 D-047-compliant compositions under `templates/preview_compositions/<category>/`, generate previews via `--only <slug>` (one at a time), run a bidirectional leak sweep, run a Django test-client 5-route sanity check, run a Chromium visual walk at 1440×900.
5. Do NOT start any feature work outside this wave. Not auth, not checkout, not editor, not new templates, not new categories. Do NOT touch any category other than the one you're currently closing in this session.
6. Each category close should end with: (a) bidirectional leak sweep clean, (b) `check` + `seed_templates` + `generate_previews` all green, (c) 5/5 routes return 200, (d) Chromium visual walk confirms differentiation at card size, (e) `SESSION_LOG.md` / `DECISIONS.md` / `TODO_NEXT.md` / `AGENT_HANDOFF.md` / `TEMPLATE_REGISTRY.json` / the auto-memory index all updated.

### Gotcha: Django test client + ALLOWED_HOSTS
Session 18 hit a small trap on the route sweep: `DEBUG=True` with `ALLOWED_HOSTS=[]` does NOT auto-allow `testserver` (only `localhost`/`127.0.0.1`/`::1`), and the Django test client uses `testserver` as the default Host header. If you run a test-client sweep via `manage.py shell`, monkey-patch it in-session:

```python
from django.conf import settings
settings.ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1']
```

Don't edit `settings.py` for this — it's a local-only concern and the monkey-patch is scoped to the shell session. For the Chromium visual walk, the runserver's real Host header is what matters, so `ALLOWED_HOSTS=[]` with `DEBUG=True` is fine at `127.0.0.1:<port>`.

### Minimum bar for "this wave is done" (exit criteria)

See TODO_NEXT.md Phase 2g2x.6. Summary: every sibling pair in every category must look like two different products at card size, no per-archetype file has any literal brand string, and every published template has either inner pages or is demoted to draft.

---

## Session 16 — Catalog Differentiation Hard Audit (2026-04-11)

**Question asked:** Are the catalog's sibling templates credible distinct products, or are they still recolors / identity-crash prototypes? Produce a severe, blocking-or-not verdict before the roadmap continues.

**Answer:** **Catalog not approvable.** See above. Verdict: hardening phase 2g2x is blocking. Read the new Phase 2g2x in TODO_NEXT.md and D-049 in DECISIONS.md. The audit found problems in 7 of 8 categories; only the `restaurant/street-modern` composition is fully clean. 5 categories are CRITICO severity (full identity crash), 3 categories are MEDIO severity (latent D-047 violations and cross-pool imagery leaks).

---

## Session 15 (archived) — Visual Polish & Preview Fixes (2026-04-11)

## Session 15 — Visual Polish & Preview Fixes (2026-04-11)

**Question asked:** A visual review of the current marketplace UI found four concrete product-quality problems visible directly on cards and category pages. Fix them without expanding scope: (1) Dermatologia card shows a grey placeholder, (2) restaurant category hero is clipped/unbalanced, (3) Gusto+Sapore still too similar at card size, (4) Luxe+Bottega essentially identical at card size.

**Answer:** **All four fixed, verified visually and via 37-route regression.**

### Root causes
1. **Dermatologia had zero preview TemplateAssets.** Session 13 explicitly skipped preview regeneration when validating archetype reuse ("validation is about the live preview, not the thumbnail"). The marketplace card rendered its `mw-img-placeholder` fallback — a grey `bi-window-desktop` icon.
2. **Hidden second leak in `templates/preview_compositions/medical/specialist.html`.** Session 14 covered the `live_templates/medical/specialist/*.html` chrome but missed the preview composition. It still hardcoded `Dr. R. Marani`, `Roma · Parioli`, `SC Cardiologia` in the hero meta + credit blocks. Regenerating derm's preview naively would have shown the cardiologist's name on the dermatology card.
3. **Restaurant category hero too cramped.** `.mw-page-hero` used `padding-top: 7rem` against a 77px fixed navbar — only a 35px gap navbar→breadcrumb. `max-width: 36rem` on the subhead left the right side dead on wide screens. No `min-height` → hero collapsed to ~330px.
4. **Gusto + Sapore PNGs on disk were stale** — legacy `restaurant.html` renders from before Session 10's fix pass. Session 12 claimed to have regenerated them but the fix did not land in this worktree.
5. **Luxe + Bottega had no DNA at all.** Both rendered through the single legacy `ecommerce.html` composition that hardcodes every string and pulls from the same pool. The only difference was the brand name in the navbar.

### Fixes applied
1. **Dermatologia preview.** Moved `Dr. R. Marani / Roma · Parioli / SC Cardiologia` out of `specialist.html` literals into new DNA fields `hero_meta`, `credit_left`, `credit_right` on both Cardio and Dermatologia content blocks. The composition now does `{% for label, value in dna.content.hero_meta %}` and reads `dna.content.credit_left.0/1`. Ran `generate_previews --only dermatologia-elite-roma` — the card now shows "Dr.ssa L. Ricciardi · 18 anni · 2.400+ pazienti · Studio Roma · Via Veneto · Specialità Dermatologia" with the forest-green accent + Bodoni Moda pairing. Regenerated Cardio too to verify the composition change is a no-op for it (confirmed).
2. **Restaurant hero.** Rewrote `.mw-page-hero` in `static/css/components.css`: `padding-top: calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` (64px clearance), `padding-bottom: var(--mw-space-10)` (80px), `min-height: 22rem`, vertical-centered flex, subhead `max-width: 46rem`, clamped responsive h1, dual radial gradient background (indigo top-right + amber bottom-left), `overflow: hidden`, `position: relative` + container z-index. Measured after: 64px navbar→breadcrumb gap, 373px hero height.
3. **Gusto / Sapore.** Clean-delete recipe (remove asset row + canonical file + any orphan suffix, re-run `generate_previews --only <slug>` without `--force`). The Session 10 DNA compositions for `restaurant/fine-dining.html` and `restaurant/trattoria-warm.html` render correctly — they just needed a fresh pass. Gusto = fully DARK charcoal + italic Playfair + full-bleed plate + gold course index. Sapore = fully CREAM + handwritten Caveat + polaroid scrapbook + recipe card. With Brace (yellow brutalist) unchanged, the 3 restaurant cards now occupy three opposite ends of the visual spectrum.
4. **Luxe / Bottega (new ecommerce DNA pilot).** Added 2 archetypes to `LAYOUT_ARCHETYPES`: `fashion-editorial`, `artisan-workshop`. DNA entries for both (using existing `ecommerce` imagery pool — Session 10's lesson: controlling macro tone is cheaper than URL hunting). Authored two new compositions under `templates/preview_compositions/ecommerce/`:
   - **fashion-editorial.html** (Luxe) — fully DARK #08070a, gold #B8860B accents, italic Cormorant Garamond 108px "Il nuovo corpo del vestire", fashion-model full-bleed cover L, editorial product strip with gold price labels at bottom.
   - **artisan-workshop.html** (Bottega) — fully CREAM #f6ecd8 with subtle grain, terracotta accent, huge Libre Baskerville 108px "Pezzi unici cuciti & fatti in bottega", rubber-stamped info panel rotated 0.8deg, 4-up N°-labeled edition cards. NO hero photo — typographic-led.
   
   Both compositions use the SAME imagery pool. The visual differentiation comes from macro tone (BLACK vs CREAM), font family (italic serif vs rustic serif), layout structure (photo-led vs typographic-led), and accent color. At thumbnail size, they read as two completely different products.

5. **Orphan file cleanup.** Session 12 left 4 orphan-suffixed files with DB rows pointing to them. Renamed each orphan to its canonical name and updated the DB. Zero orphan files now exist.

### Hard validation
- **`python manage.py check` — clean.**
- **37-route regression sweep via Django test client:** homepage + 5 category pages + 10 detail pages + 7 cardio inner + 7 derm inner + 6 gusto inner + 1 gusto post. **All 37 return 200.**
- **Cardio-leak audit** re-run on all 7 dermatology pages after the preview-composition change: **zero leaks.** Session 14's abstraction still holds.
- **Visual verification via Chromium (Playwright):** homepage featured grid shows new Gusto, `/templates/restaurant/` shows 3 distinct cards + balanced hero, `/templates/medical/` shows 5 medical cards all with valid previews (derm no longer a placeholder), `/templates/ecommerce/` shows Luxe (dark fashion) and Bottega (cream artisan) as instantly distinguishable products.

### What to do next

**Highest leverage: Phase 2f.2 — Ecommerce DNA expansion.** Two ecommerce archetypes now exist (`fashion-editorial`, `artisan-workshop`) but each hosts exactly one template. Validate reuse the same way the `specialist` archetype was validated in Session 13: add a second template under each archetype with ONLY a seed row + DNA entry, zero new HTML files. Then run a leak audit on the rendered preview to find any literal `Maison Luxe`, `Firenze`, `Santa Croce`, `Giulia Maison`, `Milano · Parigi · Tokyo`, etc. that snuck into the composition authoring pass. Lift them into DNA content fields per the D-047 chrome-authoring contract. The reward is that the two new ecommerce archetypes become fully reusable and the next ecommerce template ships without any copy polish.

**Second priority: Phase 2g.3 — Fine-Dining copy-abstraction lift** on `templates/live_templates/restaurant/fine-dining/` (documented in TODO_NEXT.md). This was already the highest-priority item before Session 15 and is still pending.

### Lessons from Session 15 (read these before the next pilot)

1. **"Validation skipped the thumbnail" is a user-facing bug.** Session 13's reasoning was that archetype reuse is about the live preview, not the marketplace card. But the marketplace card is the FIRST thing a buyer sees. Any future archetype-reuse validation must end with `generate_previews --only <slug>` and a visual check of the card in the listing. Skipping the thumbnail is not "smaller scope" — it leaves a broken product visible to users.

2. **D-047 applies to preview compositions too, not just live-template chrome.** Session 14 lifted `templates/live_templates/medical/specialist/*.html` and celebrated zero leaks. But `templates/preview_compositions/medical/specialist.html` still had 3 cardio literals that would have surfaced on any non-cardio template sharing that archetype. The rule generalizes: **every string in any per-archetype file (live-template chrome OR preview composition) must be a CSS rule, a generic archetype label, a DNA content field, or a loop item.** Apply it to both kinds of files every time.

3. **Macro tone trumps imagery, confirmed at a third pilot.** Luxe and Bottega share the exact same imagery pool yet read as two completely different products at card size because one composition is fully BLACK and the other is fully CREAM. Session 10 established this for Restaurant; Session 15 confirmed it for Ecommerce. **Before hunting for new Unsplash URLs on the next DNA pilot, first decide whether the compositions can carry the difference on macro tone alone.** If they can, it's free. URL hunting is expensive (HTTP 404s, hand-verification, Session 9 mistakes).

4. **Stale-PNG timing trap is still unfixed structurally.** Sessions 8, 10, 12, 15 all hit it independently. The clean-delete recipe works but is operator-dependent. The proper fix from TODO_NEXT Phase 2d — either auto `--force` when DNA mtime > asset mtime, or hash the DNA into a `dna_signature` field on TemplateAsset and compare on every run — is the next DX polish priority. Until then, any DNA edit on an existing slug requires the clean-delete recipe.

5. **`position: fixed` navbar + `padding-top: Xrem` on hero is a hidden coupling.** The previous 7rem worked with a 64px navbar but became cramped once the navbar grew to 77px. Encoded it as `calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` so the coupling is explicit. Long-term: measure the navbar height via JS on page load and expose as a CSS custom property so the hero always clears it.

---

## Session 14 — Specialist Copy-Abstraction Lift (2026-04-11)

**Question asked:** Can the specialist chrome HTML files be made truly reusable — so a third specialist template (after Cardio and Dermatologia) ships with zero copy polish — by moving every hardcoded cardio literal out of HTML into the content registry, WITHOUT adding any new HTML files?

**Answer:** **Yes.** Phase 2g.2 is closed. All 17 leak points identified in Session 13's audit are resolved via purely mechanical moves. The specialist archetype is now editorially reusable.

### What changed
Eleven files modified, zero added, zero deleted:
- `apps/catalog/template_content.py` — CARDIO_CONTENT + DERMATOLOGIA_CONTENT gained ~30 new fields each, grouped semantically under existing blocks (`site.license`, `site.hours_footer_rows`, `home.hero_sidebar_*`, `home.chief.portrait`, `home.signature_visits_*`, `home.chief_label`/`heading`, `home.press_label`, `home.cta_*`, `studio.values_*`, `studio.cta_*`, `visite.footnote_heading`, `visite.cta_*`, `medici.portrait_city`, per-doctor `doctors[i].portrait`, `pubblicazioni.lead_image`, `pubblicazioni.footer_strap`, `pubblicazioni.empty_body_fallback_paragraphs`, `contatti.form_placeholders`, `contatti.hours_heading`, `contatti.transport_heading`, `richiedi-visita.process_label`/`heading`, `richiedi-visita.form_band_side_note`/`_small`, `richiedi-visita.submit_label`). The `richiedi-visita.form_fields` list was **reshaped** from `(label, placeholder, type)` tuples into richer dicts `{label, type, full_width, placeholder OR options}` so the appointment form's two selects can loop their options from data instead of being hand-written.
- `apps/catalog/views.py` — `LiveTemplateView.get_context_data()` now computes `blog_parent_slug` from the content registry's `pages` list (first entry where `kind == 'blog_list'`). Template blog URL reverses consume this variable instead of hardcoding `'pubblicazioni'`. **D-044's hardcoded-blog-slug constraint is lifted** — see D-048.
- Nine HTML files under `templates/live_templates/medical/specialist/` — every cardio literal swapped for `{{ page_data.* }}`, `{{ site.* }}`, loop iteration, or `blog_parent_slug`. The `team.html` `nth-child` portrait CSS rules are gone, replaced with per-doctor inline styles (which also removes the 3-doctor cap). The `appointment.html` hand-written form is gone, replaced with a single generic field loop.

### Hard validation
1. **`python manage.py check` — clean.**
2. **Route sweep — 25/25 green** via Django test client:
   - Cardio: 9 routes (marketplace detail + 7 inner preview pages + 1 post detail)
   - Dermatologia: 9 routes (same structure)
   - Gusto regression: 7 routes (marketplace detail + 6 inner pages + 1 post detail)
3. **Cardio-leak sweep on dermatologia — ZERO leaks.** Rendered HTML of all 8 dermatologia pages was grepped for 26 cardio literals (`Marani`, `OMCeO Roma 12 / 4408`, `cardiologia`, `Cardiologia`, `Parioli`, `catena di montaggio`, `Lancet`, `Riccardo Marani`, `Salieri`, `Lombardi`, `Prima visita`, `Secondo parere`, `Programma prevenzione`, `Visita di controllo`, `ecocardiograf`, `Holter`, `ECG`, `Policlinico Umberto`, `Braunwald`, `Institut de Cardiologie`, etc.). **All 8 pages came back clean.**
4. **Positive content sweep — Cardio 52/52, Dermatologia 46/46** expected strings all present. The content blocks still drive every field the chrome reads.
5. **Template file grep — zero hardcoded Unsplash URLs, zero cardio-brand literals** in any of the 9 specialist chrome files.

### The chrome-authoring contract (D-047)

Every string in a per-archetype skin must satisfy exactly one of four criteria:
1. **CSS rule** (color, font, layout — the visual identity)
2. **Generic archetype label** — applies identically to every template that could use this archetype (`Nome`, `Email`, `Privacy`, `Invia messaggio`, `Leggi l'articolo completo`, `© 2026`, etc.)
3. **Template context variable** (`{{ site.* }}`, `{{ page_data.* }}`, `{{ d.* }}`, `{{ post.* }}`, `{{ blog_parent_slug }}`)
4. **Loop iteration** over a content registry list

**Never:** literal brand name, literal city name, literal quote, literal CTA heading, literal form select option, hardcoded image URL.

This contract is now a chrome-authoring precondition for Phase 2f (Agency, Lawyer, Real Estate archetype splits) and Phase 2g.3 (fine-dining copy-abstraction lift). Applied from the first authoring pass of any new skin, it eliminates the need for a follow-up lift pass entirely.

### What to do next
**Phase 2g.3 — repeat this exact lift on `templates/live_templates/restaurant/fine-dining/`.** The fine-dining chrome was authored during Session 11 in the same style as the specialist chrome and almost certainly has the same class of leaks (Lorenzo Fioravanti brand-name references, Brera district in the chef portrait, hardcoded Michelin press list labels, hardcoded `'diario'` URL reverses in blog files, hardcoded Unsplash URLs for chef/plate/room photos). The recipe is documented in TODO_NEXT.md Phase 2g.3:
1. Add a second fine-dining template (suggested: `tartufo-truffle-house` — Piedmont truffle restaurant, autumn menu, different chef/brand) with ONLY a seed row + DNA entry + content block.
2. Run the leak sweep against it: grep rendered HTML for `Fioravanti`, `Osteria Moderna`, `Brera`, `Tarbouriech`, `Vallesi`, `Otto atti`, `Barolo Cannubi`, etc.
3. For each leak, add a structured field in the appropriate block and update both Gusto and the new template's content.
4. Replace any hardcoded `'diario'` URL reverses with `blog_parent_slug` (already computed in the view).
5. Replace any hardcoded image URLs with inline `style="background-image: url('{{ ... }}')"` reading from per-item fields.
6. Re-run a full regression sweep (Cardio 9 + Derm 9 + Gusto 7 + new template 7 = 32 routes).

After Phase 2g.3 closes, both archetypes in use are proven reusable and the pattern is general. Then resume Phase 2f DNA rollout (Agency, Lawyer, Real Estate) applying D-047 from the first authoring pass of every new skin.

## Session 13 — Archetype Reuse Validation (2026-04-10)

**Question asked:** Can a new full multi-page template be added under an existing archetype (the Medical `specialist` archetype, previously single-tenant by Cardio) with ONLY three edits — one seed row, one DNA entry, one content block — and **zero** new HTML files? This was the Option A validation path proposed at the end of Session 12.

**Answer:** **Yes, structurally.** `dermatologia-elite-roma` (Studio Ricciardi Dermatologia · Via Veneto 116 · forest green accent `#3d5437` · Bodoni Moda + Inter · three dermatologhe · six treatments · five publications) now ships as a full navigable 7-inner-page website on the same specialist chrome as Cardio. All 9 routes (marketplace detail + home + 6 inner pages + 1 post detail) return 200 via Django test client. `git status` confirms three modified `.py` files (`seed_templates.py`, `template_dna.py`, `template_content.py`) and zero modified or new HTML files. 19-URL regression sweep on Cardio + Gusto + catalog pages all 200. **The Session 11 architecture works as intended for content-driven reuse.**

**BUT editorially the chrome leaks.** The same audit that confirmed the 200 statuses also found that cardio-specific copy is baked into the HTML in 17 distinct sites across 7 files, appearing on every single dermatology page. The most visible leaks: (1) `OMCeO Roma 12 / 4408` on every page's footer (wrong license number for the derm studio), (2) `«La cardiologia non è una catena di montaggio...»` quote in the home hero's right column, (3) `Roma · Parioli` in the home pulse band and in every doctor's portrait signature, (4) `Studio Marani` brand name in the services CTA heading and the blog detail footer, (5) three hardcoded Unsplash portrait URLs in `team.html`'s nth-child CSS rules (Dermatologia's team shows Cardio's doctors' photos, and the 3-doctor cap is baked into the layout). See SESSION_LOG.md Session 13 for the full 17-row leak table.

**Why this is not a blocker for the validation verdict but IS a blocker for the next reuse template:** The architecture separates "chrome + data" correctly; the implementation simply baked sample copy into the chrome during the Session 11 authoring pass. Fixing it is a mechanical lift — move the literals out of `.html` files into new `site.*` / `page_data.*` / per-item fields in the content registry. No new HTML files, no new architecture. **See TODO_NEXT.md Phase 2g.2 for the exhaustive lift plan.**

### What changed in Session 13
**New template: `dermatologia-elite-roma`** — 2nd template on the `specialist` archetype
- `seed_templates.py` — new row, order=5, price €115, brand "Studio Ricciardi Dermatologia" with palette `{primary:#1c1612, secondary:#f7f3ee, accent:#3d5437}` and typography `Bodoni Moda + Inter`
- `template_dna.py` — new DNA entry keyed `dermatologia-elite-roma`, archetype `specialist`, all the specialist defaults, font_pairing overridden to `("Bodoni Moda", "Inter")`, fresh `content` block for the preview composition
- `template_content.py` — new `DERMATOLOGIA_CONTENT` dict with all 7 pages, 5 posts (first with full body), site chrome data, dermatology-specific copy throughout. Page slugs kept as `home / studio / visite / medici / pubblicazioni / contatti / richiedi-visita` to match the hardcoded `pubblicazioni` URL reverse in the blog files
- `TEMPLATE_REGISTRY.json` — version 0.6.0, dermatologia entry added with `archetype_reuse: true` flag
- `CATEGORY_ROADMAP.md` — specialist archetype now hosts 2 templates; reuse validation result logged
- `DECISIONS.md` — D-046 added (formal record of the validation result + the copy-leak finding + the Phase 2g.2 plan)

### Database delta
- `+1` WebTemplate row, `+1` TemplateBrand row, 0 new TemplateAssets (no PNG regenerated — validation is about the live preview, not the thumbnail)
- Medical category is now 5 templates (clinic, family, specialist ×2, wellness)
- Total marketplace: 20 templates / 20 brands / 19 preview assets

### The hard constraints discovered (critical for any future reuse)
1. **The blog parent page slug must be literally `pubblicazioni`.** `blog_list.html:95,98,109` and `blog_detail.html:85,121` hardcode `{% url 'catalog:live_template_page' ... 'pubblicazioni' %}` in URL reverses. Any other naming causes `NoReverseMatch`. Dermatologia's blog page is therefore called Pubblicazioni, not "Blog" or "Diario". **Phase 2g.2 fix:** compute `blog_parent_slug` in `LiveTemplateView.get_context_data()` from the content registry's `pages` list.
2. **The chrome caps the team at 3 doctors.** `team.html:70-72` uses `nth-child(1/2/3) .portrait { background-image: ... }`. A fourth doctor would render without a portrait. **Phase 2g.2 fix:** move to per-doctor `doctors[i].portrait` URLs.
3. **The chief doctor portrait image is shared** — `home.html:127` hardcodes a single Unsplash URL in inline CSS. Dermatologia's chief shows the same photo as Cardio's chief. **Phase 2g.2 fix:** move to `home.chief.portrait`.
4. **The blog-list lead post image is shared** — `blog_list.html:17` hardcodes another Unsplash URL. **Phase 2g.2 fix:** move to `pubblicazioni.lead_image` or `posts[0].hero_image`.
5. **The appointment page `<select>` options are hardcoded** — `appointment.html:166-180` bakes in the cardio visit types (Prima visita / Secondo parere / Programma prevenzione / Visita di controllo) instead of reading from `richiedi-visita.form_fields` which already exists in both content blocks. **Phase 2g.2 fix:** template loop over `form_fields`.
6. **Seven distinct section headings / CTA labels are literal cardio copy.** See the TODO_NEXT.md Phase 2g.2 checklist for the complete per-file enumeration.

## Session 12 — Template Polish Fixes (2026-04-10)

Two product-quality issues closed before the next pilot:

1. **Over-narrow inner-page layouts.** The live multi-page template skins used max-width 1100/1200/1280 which felt "compressed into the middle" of 1600-1920px displays. Bumped to a two-tier standard: **1400px** for medical/specialist wide sections, **1440px** for restaurant/fine-dining wide sections. The home manifesto had an additional double-constraint bug (`outer 1100px` + `inner p max-width: 36ch; margin: 0 auto`) producing a tiny ~450px centered column — fixed by removing the inner centering and widening to `68ch` left-aligned so the drop-cap anchors the frame's left edge. Blog detail pages stay at 760px intentionally (long-form reading column).

2. **Restaurant listing preview mismatch.** Two layers:
   - **Outer layer:** `template.assets.first` in the card + detail partials is fragile — default-ordering fetch, not filtered by asset_type. Replaced with a new `WebTemplate.preview_asset` property in `apps/catalog/models.py` that explicitly filters `asset_type == preview`, is prefetch-aware (iterates `_prefetched_objects_cache` when available), and returns `None` when no preview exists. Selector uses `Prefetch('assets', queryset=...filter(asset_type='preview'))` to ship a smaller payload.
   - **Inner layer (actual cause):** The gusto + sapore PNG files on disk were stale legacy `restaurant.html` renders — both showed the same wood-interior trattoria. Session 10's claimed regeneration never actually landed in this worktree. Fixed by deleting the stale asset rows + files and re-running `generate_previews --only <slug>` (no `--force`, so the canonical filename lands clean without an orphan suffix).

**Branch:** `template-polish-fixes` worktree (built on top of `template-completeness-pilot` → ... → `template-dna-system`, **none merged to master yet**).

**All three restaurant cards now read as three distinct products at thumbnail size** — Brace (yellow brutalist), Sapore (bright cream polaroid), Gusto (dark editorial Playfair). 20 routes verified 200 via Django test client, `python manage.py check` passes.

### Lessons from Session 12

- **`template.assets.first` is a bug magnet.** It returns "whatever's first by default `(order, asset_type)` ordering", which silently picks the wrong file the moment a template gains a second asset. Always filter by `asset_type` explicitly. The `WebTemplate.preview_asset` property encapsulates this rule once so templates never need to remember it.
- **Page-level max-widths of 1100-1280 are too narrow for 1600+ displays.** 1400-1440 is the new standard for wide content. Editorial narrow reading columns (blog articles) stay at ~720-800 because those are about line length, not frame width. **Never double-constrain** with outer `max-width` + inner `margin: 0 auto + max-width: Xch` on the same element tree — either widen the outer container and use `max-width: <NN>ch` on the text (left-aligned, drop-cap anchored to the frame's left edge), or keep the outer narrow and drop the inner centering. The double constraint creates compositions that look "floating in a void".
- **DNA-fallback timing trap is still live.** Gusto and Sapore's PNGs were stale despite Session 10's claim. Whatever the root cause (cross-branch drift, unrecorded regen, worktree sync), the fix recipe is the same every time: delete the asset row + canonical file first, then re-run `generate_previews --only <slug>` without `--force`. TODO_NEXT.md Phase 2d item 4 — "auto --force whenever the DNA file or composition path on disk is newer than the preview's TemplateAsset" — would catch this class of bug structurally. Strong candidate for the next DX polish pass.

## Current State (since Session 11, carried through 12)

**Two pilot templates now ship as full multi-page websites — not just preview screenshots.** The DNA system (Sessions 7-10) made each template's homepage visually unique. Session 11 added the missing piece: every template can now be a *navigable, complete website product*. Session 12 then polished the inner-page layout widths and hardened the preview-asset selection against the fragile `template.assets.first` fallback.

- **`cardio-studio-specialistico`** (Medical · specialist archetype): 8 navigable inner pages — Home, Lo Studio, Visite, Medici, Pubblicazioni (list + article detail), Contatti, Richiedi visita
- **`gusto-fine-dining`** (Restaurant · fine-dining archetype): 7 navigable inner pages — Casa, Filosofia, Menu (otto atti), Atmosfera, Diario (list + article detail), Prenota
- All 17 routes (8 + 7 + 2 marketplace detail) verified 200 via Django test client (Session 11), extended to 20 in Session 12
- The system is **strictly opt-in per template** — every other template in the catalog behaves exactly as before
- **New in Session 12:** `WebTemplate.preview_asset` property, selector uses `Prefetch` with filtered queryset, layout widths bumped to 1400/1440, home manifesto double-constraint fixed, stale gusto/sapore PNGs regenerated. Three restaurant cards now read as three distinct products at thumbnail size.

The marketplace template detail page now shows "Apri anteprima completa" (linking to the full live site) when content is registered, and falls back to the old "Anteprima Live" placeholder otherwise.

Branch: `template-polish-fixes` worktree (built on top of `template-completeness-pilot` → ... → `template-dna-system`, **none merged to master yet**).

## Session 11 — Template Completeness Pilot Phase

Three architectural layers introduced:

1. **Content registry** — `apps/catalog/template_content.py`. Python dict keyed by `WebTemplate.slug` holding the page list, per-page content blocks (eyebrow, headline, sections, lists), and a `posts` list for blog/news inner pages. All Italian, all realistic, no boilerplate.

2. **Per-archetype standalone skin** — `templates/live_templates/<category>/<archetype>/`. Each archetype gets its own `_base.html` that is a *complete HTML document* (NOT extending the marketplace `base.html`), loading the DNA's font pairing and brand palette. Each page kind (`home.html`, `about.html`, `services.html`, `team.html`, `blog_list.html`, `blog_detail.html`, `contact.html`, `appointment.html`, `menu.html`, `gallery.html`, `reservations.html`) extends that base and overrides `extra_css` + `content`.

3. **Single dispatcher view** — `LiveTemplateView` in `apps/catalog/views.py`. Resolves WebTemplate → DNA → content registry in `setup()` (NOT `get_template_names`, see D-044 trap), computes the template path `live_templates/<category>/<archetype>/<page-kind>.html`, returns 404 if either DNA or content is missing.

Three new URL patterns:
```
/templates/<cat>/<slug>/preview/                         → live_template_home
/templates/<cat>/<slug>/preview/<page>/                  → live_template_page
/templates/<cat>/<slug>/preview/<page>/<post_slug>/      → live_template_post
```

### What makes a template "complete" now

A template earns the "Apri anteprima completa" CTA on its detail page once it has BOTH:
1. A DNA entry in `apps/catalog/template_dna.py` (archetype + chrome decisions)
2. A content registry entry in `apps/catalog/template_content.py` (the editorial copy for every page)

Without either, it falls back to the legacy `Anteprima Live` placeholder and the new URL space returns 404. Every template that's been in the catalog before Session 11 still works exactly as it did.

### What is now reusable across all future templates
- `LiveTemplateView` and the three URL patterns
- The content-registry pattern (`template_content.py`) — adding a new template = adding ONE new top-level dict
- The per-archetype skin folder structure — any new template that picks an existing archetype gets the chrome FOR FREE, just needs content
- Brand palette → CSS variable injection
- Nav loop with `is-current` highlight
- Footer pattern with site-data block

### What still needs per-archetype work
- Each NEW archetype needs its own `_base.html` (intentionally bespoke — that's the point of DNA)
- Each NEW archetype's page kinds need their own page templates (a `menu.html` is meaningless for a medical template)

## Old: Session 10 — Restaurant Pilot Fix Pass

Visual review of Session 9 found that **only Brace was clearly distinct**. Gusto and Sapore had two overlapping problems:

1. **Imagery overlap**: `restaurant-fine` and `restaurant-trattoria` pools shared 5 of 6 URLs (only the hero differed). Session 9's claim of "fully-distinct URL sets" was wrong — only Brace's pool was actually distinct.
2. **Same macro silhouette**: both compositions were "cream paper top + dark band bottom". At thumbnail size the dark/cream split dominated and made them read as the same skeleton.

### Fix applied
- **Imagery pools**: both `restaurant-fine` and `restaurant-trattoria` rebuilt with 6 hand-checked URLs each, **zero overlap**. Fine got 6 dark plated dish photos. Trattoria got 6 bright sunny rustic photos. Each candidate was downloaded and visually inspected via the Read tool before committing — caught one clothing-store image and replaced it.
- **`restaurant/fine-dining.html` rewritten**: pivoted from cream-paper to **fully dark charcoal page** (no cream anywhere, no contrast band, full-bleed plate close-up hero, italic Playfair throughout, course list on the same dark background separated only by hairline gold rules).
- **`restaurant/trattoria-warm.html` rewritten**: pivoted from cream-with-dark-chalkboard to **fully bright cream page** (no dark areas at all, two stacked tilted polaroid scrapbook photos with washi tape, huge Caveat handwritten headline, cream washi-tape recipe card replacing the dark chalkboard, no dark hours band).
- **Brace left untouched** — already strongly distinct (yellow brutalist).

Result: 3 cards now occupy three opposite ends of the visual spectrum — dark editorial / bright handwritten / yellow brutalist.

## Session 9 — Restaurant Pilot Phase 2f.1 (superseded by Session 10 fix for Gusto/Sapore)

Replicated the medical DNA pilot for the Restaurant category. Three brand-new HTML compositions, three distinct imagery pools, one new seed template. Visually validated — but the Session 9 imagery pool was wrong (5/6 URL overlap between fine and trattoria) and the compositions had structurally similar bottom dark bands. Both fixed in Session 10.

| Layer            | Before                                          | After                                                                       |
|------------------|-------------------------------------------------|-----------------------------------------------------------------------------|
| Restaurant templates | 2 (Gusto, Sapore)                           | 3 (added Brace — Street Food Lab)                                           |
| Restaurant archetypes | 1 (legacy fallback only)                   | 3 (fine-dining, trattoria-warm, street-modern)                              |
| Restaurant compositions | 1 (legacy `restaurant.html`)             | 4 (legacy + 3 new under `restaurant/<archetype>.html`)                      |
| Restaurant imagery pools | 1 (`restaurant`)                         | 4 (`restaurant`, `restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) |
| Total templates  | 18                                              | 19                                                                          |

The DNA system is still **strictly additive** — templates without a DNA entry continue to render via the legacy per-category composition. The legacy `templates/preview_compositions/restaurant.html` is retained as a safety net for any future restaurant template not yet pulled into an archetype.

## What makes the 3 restaurant templates genuinely different (not recolors) — post Session 10

| Slug                       | Archetype       | Page macro tone   | Hero composition                                    | Navbar         | Card mood                  | Display Font           |
|----------------------------|-----------------|-------------------|-----------------------------------------------------|----------------|----------------------------|------------------------|
| gusto-fine-dining          | fine-dining     | **fully DARK** charcoal #0b0907 | full-bleed plated dish R · italic serif text L  | serif-centered (dark + gold rule) | course-index on same dark bg, gold dotted leaders | Playfair Display       |
| sapore-trattoria-pizzeria  | trattoria-warm  | **fully BRIGHT** cream #fff4da | two tilted polaroids L · handwritten Caveat R   | warm-bar (cream + phone CTA) | cream-paper recipe card with washi tape | Caveat (handwritten)   |
| brace-street-food-lab      | street-modern   | **bright YELLOW** #FFE600 | giant condensed display L · tilted burger product R | bold-pill (black floating) | brutalist black product grid w/ corner badges | Big Shoulders Display  |

**The macro tone column is the critical one** — this is the lesson from Session 10's fix pass. At thumbnail scale, page-level color regions dominate over hero details. Two templates with the same "cream top, dark bottom" silhouette will read as similar regardless of what's in each section. The fix is to make the WHOLE PAGE one consistent macro tone (dark / cream / yellow) so the entire silhouette is different from card to card.

Differences also span hero composition (full-bleed plate L vs polaroid scrapbook L vs tilted product cutout R), navbar shape (centered serif wordmark with gold rule vs cream warm-bar with phone CTA vs floating black pill), card stride (5-row dotted-leader course index on dark vs 5-day cream washi-tape recipe card vs 4-up brutalist product grid), button language (gold-underlined serif ghost vs rustic rounded with red+green tilted shadow vs brutalist block-bold with hard offset shadow), density (very-airy → medium → compact), and copy tone (editorial chef → familiar warm → energetic bold).

## What's Working

| Page                          | URL                                        | Status (port 8101) |
|-------------------------------|--------------------------------------------|--------------------|
| Homepage featured grid        | `/`                                        | Salute (clinic), Pragma, Vertex, Lex, Chiara, Gusto in featured grid |
| Template listing (all)        | `/templates/`                              | 19 templates × paginated |
| Template listing (medical)    | `/templates/medical/`                      | 4 medical templates × 4 visibly different archetypes (regression OK) |
| Template listing (restaurant) | `/templates/restaurant/`                   | 3 restaurant templates × 3 visibly different archetypes |
| Template detail (each restaurant) | `/templates/restaurant/<slug>/`        | Gallery shows the new archetype PNG |
| Template detail (each medical)| `/templates/medical/<slug>/`               | Gallery shows the new archetype PNG |

## How the DNA system works

```
apps/catalog/template_dna.py
  ├── Vocabulary dicts: LAYOUT_ARCHETYPES, HERO_STYLES, NAVBAR_STYLES,
  │                     FOOTER_STYLES, CARD_STYLES, BUTTON_STYLES,
  │                     DENSITY_PROFILES, TONES, CONVERSION_PATTERNS,
  │                     IMAGERY_DIRECTIONS
  ├── TEMPLATE_DNA: dict[slug, dna]  # the registry (7 entries: 4 medical + 3 restaurant)
  └── get_dna(slug), has_dna(slug)

apps/catalog/templatetags/preview_extras.py
  └── `at` filter — `{{ imagery|at:forloop.counter }}` for safe loop indexing

apps/catalog/preview_imagery.py
  └── Per-archetype keys:
      • medical-family / medical-specialist / medical-wellness  (recycle existing URLs, offline-safe)
      • restaurant-fine / restaurant-trattoria / restaurant-street  (fully-distinct URL sets)

apps/catalog/management/commands/generate_previews.py
  ├── _resolve_composition(template, dna)
  │     → with DNA: preview_compositions/<category>/<archetype>.html
  │     → without:  preview_compositions/<category>.html
  ├── Pre-warms imagery by *imagery_key*, not just category slug
  └── DNA's `font_pairing` overrides brand.typography parsing

templates/preview_compositions/medical/
  ├── clinic.html      — institutional, split-hero with booking widget, 4-up icons
  ├── family.html      — pastel pill nav, organic-shape portrait, intro trio + hours strip
  ├── specialist.html  — minimal serif nav, editorial headline, drop cap, 01/02 fields, press band
  └── wellness.html    — full-bleed hero, glass pill nav, dotted-leader pricelist, therapists strip

templates/preview_compositions/restaurant/
  ├── fine-dining.html    — centered serif wordmark, editorial split-plate, course index, concierge tile, press strip
  ├── trattoria-warm.html — cream warm-bar nav, polaroid photo card, Caveat handwritten manifesto, chalkboard daily specials, family + hours band
  └── street-modern.html  — black floating pill nav, giant condensed display + tilted product cutout + price badge, 4-up product grid, delivery strip
```

Run with `python manage.py generate_previews [--force] [--only <slug>]`.

## Database State

- 8 categories (unchanged)
- **19** templates (was 18; +1 restaurant: brace-street-food-lab)
- 19 brands
- 19 preview assets — 4 medical + 3 restaurant now use the new per-archetype compositions
- ~70 cached source photos across 11 pools (3 new restaurant pools added in Session 9)

## For Next Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, TODO_NEXT.md, this file, then `apps/catalog/template_dna.py` + `apps/catalog/template_content.py` (the two registries the reuse validation depended on), then `apps/catalog/views.py` → `LiveTemplateView` (the dispatcher view), then open any file under `templates/live_templates/medical/specialist/` to see the chrome that now hosts two templates (Cardio + Dermatologia).

**The highest-impact next task is Phase 2g.2 — the copy-abstraction lift** on the specialist chrome, documented exhaustively in TODO_NEXT.md. It's a mechanical move-literals-out-of-HTML-into-content-registry pass — no new HTML files, no new architecture, just pulling hardcoded cardio strings out of 7 files and wiring them to new `site.*` / `page_data.*` / per-item fields. When done, re-running the Session 13 leak audit on the dermatologia pages should show zero cardio-specific strings, and the next archetype-reuse template (e.g. a third specialist, or the first fine-dining reuse) will ship without any copy polish.

### Lessons from Session 10 — read these before designing any new category

1. **Imagery pool distinctness is non-negotiable.** Two pools that share even 5 of 6 URLs will produce sibling templates that look identical, regardless of how different the compositions are. When designing a new category's pools, write down the URL list and visually verify zero overlap. Hand-check every Unsplash candidate by downloading via curl and reading the file with the Read tool — HTTP 200 just means the photo exists, not that it shows what you expect (Session 10 caught a clothing store image that way).
2. **Page-level macro tone trumps hero details.** A "cream top, dark bottom" composition will always look similar to another "cream top, dark bottom" composition at thumbnail size, even if the content within each section is wildly different. Solution: make each composition's WHOLE PAGE one consistent macro tone, and pick a different macro tone for each sibling. Restaurant settled on dark / bright cream / yellow — three opposite ends of the spectrum.
3. **Dark bands at the bottom of cream layouts are a trap.** They feel safe and editorial, but they collapse two-region silhouettes into "the same shape with different details". Avoid the pattern entirely.
4. **Browser cache trap when verifying.** Playwright Chromium aggressively caches preview PNGs. After regenerating, the listing page may show the OLD images. Force-refresh by mutating `img.src` with a `?cb=<timestamp>` query string via `browser_evaluate`, OR navigate directly to `/media/.../preview.png?v=<n>` first.

### Watch out for the Session 8/9 timing trap (still unfixed)
When you add a DNA entry to a slug that *already* has a generated preview, that preview was rendered through the legacy fallback and is now stale. The `generate_previews` "skip if exists" branch will not regenerate it. Always run `python manage.py generate_previews --force --only <slug>` after creating or modifying a DNA entry for an existing template — **AND** delete the canonical-named PNG file on disk first, otherwise Django storage will append a random suffix to the new file (the DB row will still point correctly to the suffixed file, so functionally fine, but the disk gets cluttered with orphans). Session 10 also taught us to clear `media/preview_imagery/<key>/` when imagery URLs change so the new ones get downloaded fresh.

The clean recipe used in Session 9 to avoid the orphan trap:
```bash
# 1. Delete the row + canonical file + any suffixed file via a small Django shell snippet
python -c "import django, os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','marketweb.settings'); django.setup(); ..."
# 2. Then re-run WITHOUT --force so the new file lands at the canonical name (no collision)
python manage.py generate_previews --only <slug>
```

### Immediate next step (highest impact) — Phase 2g.2
**~~Add a third template~~ The archetype-reuse validation was completed in Session 13 with `dermatologia-elite-roma` under the `specialist` archetype. Structurally it worked (zero new HTML files, all 9 routes 200). But the audit uncovered 17 distinct copy leaks in the chrome that must be fixed before the next reuse template ships. See TODO_NEXT.md Phase 2g.2 for the full lift plan.**

After Phase 2g.2 closes, run the same validation on the restaurant side — add a second `fine-dining` template (e.g. `tartufo-truffle-house`) under the Gusto chrome and repeat the leak audit. The fine-dining chrome likely has the same class of literals baked in; a second lift pass will be needed there too.

Then resume Phase 2f DNA rollout: Agency → Lawyer → Real Estate archetype splits. When authoring each new archetype's skin, apply the Session 13 lesson from the start: **every string in a per-archetype skin must either be a CSS rule or come from `site.*` / `page_data.*` / loop items** — no literal brand-like text, no literal city names, no literal CTA labels.

### Phase 2f — DNA rollout to other categories (still pending)
The DNA rollout from Sessions 7-10 stopped after Restaurant. Three more categories still need archetype splits — Agency (3 archetypes), Lawyer (2), Real Estate (2). See the previous handoff note for the recipe; the constraint is now both:
1. Distinct preview compositions per archetype (Sessions 7-10 lessons)
2. Inner-page chrome under `templates/live_templates/<category>/<archetype>/` if the new templates are to ship as full sites (Session 11 architecture)

### Phase 2d polish (still pending from previous sessions)
1. Optimize PNG file sizes (~4 MB → ~500 KB via Pillow `optimize=True` or oxipng)
2. Cormorant Garamond on dark backgrounds reads thin (Lex, Villa, Cardio specialist) — consider bumping weight or swapping serif at low luminance
3. Add `media/preview_imagery/` to .gitignore
4. **DNA-fallback timing trap safety net** — see TODO_NEXT.md for options (a/b/c)
5. **`--force` orphan cleanup** — auto-delete the canonical file before saving so Django storage doesn't suffix
6. **Imagery URL validation** — Session 9 hit one HTTP 404 from Unsplash; a `--validate-imagery` flag would catch these before a full regeneration run

### Phase 3 (Interactivity & Accounts) — unchanged
1. Tag seeding and filtering
2. User authentication views
3. Commerce flow
4. Editor + projects integration
5. Live demo iframe per template

### Key Files for the DNA System (preview screenshots — Sessions 7-10)
- `apps/catalog/template_dna.py` — DNA registry + vocabulary (the source of truth)
- `apps/catalog/templatetags/preview_extras.py` — `at` filter for image indexing in loops
- `apps/catalog/preview_imagery.py` — `IMAGERY_CONFIG` with per-archetype keys
- `apps/catalog/management/commands/generate_previews.py` — DNA-aware pipeline
- `templates/preview_compositions/<category>/<archetype>.html` — bespoke per-template preview HTML (1600x900 fixed)
- `templates/preview_compositions/<category>.html` — legacy fallback for non-DNA templates

### Key Files for the Live Template System (multi-page websites — Session 11)
- `apps/catalog/template_content.py` — content registry (per-template page copy + helpers `has_live_template`/`get_content`/`find_page`/`find_post`)
- `apps/catalog/views.py` — `LiveTemplateView` (resolves DNA + content in `setup()`, dispatches to per-archetype/page-kind template)
- `apps/catalog/urls.py` — three URL patterns: `live_template_home`, `live_template_page`, `live_template_post`
- `templates/live_templates/<category>/<archetype>/_base.html` — standalone HTML doc for the archetype (NOT extending `base.html`)
- `templates/live_templates/<category>/<archetype>/<page-kind>.html` — per-page-kind layouts (home, about, services, team, blog_list, blog_detail, contact, appointment, menu, gallery, reservations)
- `templates/catalog/template_detail.html` — conditional CTA (`Apri anteprima completa` if content registered)

### Constraints (unchanged)
- Do not redesign architecture or model structure
- Preserve premium UI — listing/detail/card templates should not be modified for preview changes
- Follow services/selectors pattern for new business logic
- Italian content (D-016)
- Update coordination files at end of session

## Coordination Rules

- Backend-core owns: models, migrations, admin, services, selectors, management commands
- Premium-UI owns: templates/, static/, design system, frontend components
- **Real-preview-assets** owns: `apps/catalog/preview_imagery.py`, `apps/catalog/management/commands/generate_previews.py`, `templates/preview_compositions/`
- **Template-DNA-system** owns: `apps/catalog/template_dna.py`, `apps/catalog/templatetags/preview_extras.py`, `templates/preview_compositions/<category>/<archetype>.html` files
- **DNA-pilot sessions** (medical, restaurant, ...) own per-category vocabulary additions in `template_dna.py`, the per-category composition folder, and the matching imagery pool keys
- **Template-completeness-pilot** owns: `apps/catalog/template_content.py`, `LiveTemplateView`, the live preview URL patterns, `templates/live_templates/<category>/<archetype>/` skin folders
- All sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md, TEMPLATE_REGISTRY.json, BRAND_SYSTEM_GUIDELINES.md, CATEGORY_ROADMAP.md at end
