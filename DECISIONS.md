# Decisions Log

## D-081: Medical Second Wave Polish — Dynamic Counter Policy, Listbox-Radius Decoupling, Chrome Key Shape (2026-04-15, Session 52)

**Decision:** Session 51 shipped three medical archetypes (Salute · Benessere · Famiglia) as `published_live`, but three interaction-quality defects slipped through the Playwright walk: (1) Benessere's nav CTA rendered as **empty text** across all 5 locales because wellness `_base.html` bound to an undefined `chrome.nav_cta` key; (2) Benessere's form dropdown open state inherited the pill field-radius (`999px`), producing a barrel-shaped listbox panel; (3) Salute's hero + band stat spans (`40+ · 12 · 98%` + `1998 · 28.000 · 6 · € 0`) rendered as static text — zero animation — even though the section is a clear stats/facts band that the DNA register admits. This decision closes all three with minimal-surface fixes and binds a **Dynamic Counter Policy** that future rollouts must honor.

### Concrete shape

1. **Live-forms decoupled listbox-radius token (`--lf-listbox-radius`):** `static/css/live-forms.css` now resolves `.lf-select-listbox { border-radius: var(--lf-listbox-radius, 12px); }` instead of `var(--lf-radius, 0)`. Default 12px. Skins with pill inputs (`--lf-radius: 999px`) MUST override `--lf-listbox-radius` explicitly (wellness sets `14px`) to prevent a 999px panel projection. Existing skins that want the listbox to match field radius still can (set `--lf-listbox-radius: var(--lf-radius)`). `.lf-select-listbox` also gets `overflow: hidden auto` so child hover rows can't bleed outside the rounded corner.

2. **Wellness nav CTA authoring — chrome is archetype-agnostic, site is template-specific:** the wellness `_base.html` CTA now reads `{{ site.nav_cta }}` (not `{{ chrome.nav_cta }}`). Rationale: the reservation-CTA copy differs per template voice ("Prenota un rituale" for wellness, "Prenota una visita" for clinic phone-CTA, family uses `site.nav_cta_wa` for WhatsApp). The chrome dict carries archetype-shared labels (marketplace bar, footer headings, form primitives); per-template conversion copy belongs in `site`. All 5 Benessere locale files now carry `site.nav_cta` ("Prenota un rituale" · "Book a ritual" · "Réserver un rituel" · "Reservar un ritual" · "احجز طقسك").

3. **Dynamic Counter Policy (this decision):** "When a published_live template renders a premium stats/facts/metrics/volumes/years/visits/indicators band, the numeric value MUST animate from 0 via `data-lm="counter"` — unless the DNA tone disqualifies it (funereal editorial, brutalist manifesto, or the value is a semantically-inanimate label like a literal zero). Reduced-motion MUST be respected (live-motion.js already short-circuits via `prefers-reduced-motion: reduce`)." The `live-motion.js` counter runtime handles the numeric extraction — it preserves any non-digit prefix/suffix (`40+` · `98%` · `€ 0` · `1.4B`) and automatically detects Italian (`28.000`) or English (`28,000`) thousand separators, restoring the correct separator during mid-animation frames.

4. **Optional per-stat opt-out via a 3rd tuple element:** `page_data.stats` entries accept an optional third boolean — truthy means "skip animation, render static". Default = animate. This is the authoring escape hatch when a value is a label (funding year that reads as a name rather than a quantity, a literal zero where animation is visually a no-op anyway, etc.). No existing stats were opted out in this session; the hook is available for future templates that need it.

5. **Live-motion.js thousand-separator extension:** the counter duration-and-formatting logic previously supported only Italian dot-style thousand separators (`28.000` → 28000). It now ALSO supports English-style comma thousand separators (`28,000` → 28000), detected via `/^\d{1,3}(,\d{3})+$/`, and restores the correct separator character in mid-animation frames. This ensures EN/FR/ES locales can render native-formatted thousand-separators in stats bands without breaking the animation.

6. **Django-comment gotcha re-iterated:** the initial Salute patch used `{# ... #}` to annotate the opt-out semantics inside a loop; Django's tokenizer leaked the entire comment block to render output (same gotcha as Session 48, D-078 key-insight #1). Session 52 re-encountered it, re-fixed it (switched to `{% comment %}…{% endcomment %}`), and binds the rule retroactively: **multi-line Django comments inside skin HTML MUST use `{% comment %}` blocks**, never `{# ... #}` on multiple lines.

### Files modified

- `static/css/live-forms.css` — `.lf-select-listbox` `border-radius` decoupled from field radius (new token `--lf-listbox-radius`, default 12px); `overflow: hidden auto` added. Token docs updated.
- `static/js/live-motion.js` — counter heuristic extended to support both Italian dot-style (`28.000`) and English comma-style (`28,000`) thousand separators; `formatValue` preserves the detected separator in mid-animation frames.
- `templates/live_templates/medical/wellness/_base.html` — nav CTA now reads `{{ site.nav_cta }}`; `--lf-listbox-radius: 14px` explicitly set to prevent 999px field-radius projection.
- `templates/live_templates/medical/clinic/home.html` — hero `.cl-h-stats .n` and band `.cl-stats .n` spans emit `data-lm="counter"` (animation opt-out via 3rd tuple element supported). Multi-line comment converted to `{% comment %}…{% endcomment %}`.
- `apps/catalog/template_content_benessere.py` + `_en.py` + `_fr.py` + `_es.py` + `_ar.py` — each `site` dict gains `nav_cta` with locale-native voice ("Prenota un rituale" · "Book a ritual" · "Réserver un rituel" · "Reservar un ritual" · **"احجز تجربتك"**). The AR string was refined mid-review from the first-pass `احجز طقسك` (grammatically correct, but `طقس` has a dual meaning "rite/weather" in everyday MSA that reads stilted at a nav-CTA surface) to `احجز تجربتك` ("book your experience") — standard premium-wellness register in AR markets (Aman Resorts · Six Senses · Talise Spa · Vogue Arabia). Body copy retains `طقس` for Session 51 lexical continuity; nav-CTA gets the more editorial voice.

### Validation

- `python manage.py check` → 0 issues.
- Browser walk at 1440×900 + 1440×600 + AR (rtl): Benessere nav CTA renders in all 5 locales (IT/EN/FR/ES/AR); listbox panel opens at 14px radius; Salute hero stats animate 0 → `40+` / `12` / `98%` on viewport enter; band stats animate 0 → `1998` / `28.000` / `6` / `€ 0` (with IT dot-sep) and 0 → `1998` / `28,000` / `6` / `€ 0` (with EN comma-sep) on viewport enter; Famiglia phone + WhatsApp CTAs click-through to `tel:` + `https://wa.me/…`.
- Mid-animation samples at 200 / 600 / 1000 / 1800 ms confirm easeOutCubic-shaped climb (298 → 1419 → 1892 → 1998) preserving thousand-separator character.

### Trade-offs deliberati

- **No per-locale chrome key added.** I deliberately did NOT extend `CHROME_I18N` with a `nav_cta` key, even though it would have worked. Nav-CTA copy is template-specific (reservation vs phone vs chat), so adding it to the archetype-shared chrome dict would have pulled inappropriate wording into templates that don't use a text CTA. The `site.nav_cta` approach keeps the authoring surface honest.
- **No per-stat content rewrite on Salute.** Session 51 authored 4 band stats including a founding-year ("1998"). Clinical institutional tone is debatable for year-counter animation, but the user's policy text explicitly listed "anni" as a counter target. Decision: animate. The 3-tuple opt-out is available for future iterations if the tone pivots.
- **Comma-thousand-sep in live-motion.js is a heuristic, not a locale lookup.** The JS runtime has no access to the Django `locale`; it infers from the DOM text. A value like `1,4` (French decimal) would be interpreted as decimal (comma → dot), not thousand-sep, because the regex requires `\d{1,3}(,\d{3})+` (multi-group required). Edge case: `1,234` — single group — is correctly detected as thousand-sep by the updated regex `/^\d{1,3}(,\d{3})+$/` (one or more groups). `1,4` fails the regex (2-digit trailing group) and falls through to the decimal branch. Safe.

### Consequence

- Medical category holds at 5/5 published_live; catalog unchanged at 16/20. This is a polish-only session.
- Three interaction defects closed without tier churn, without DNA rewrites, without locale regressions.
- **Dynamic Counter Policy binds retroactively and prospectively:** any future rollout (Lex · Juris · Casa · Villa) that ships a stats/facts band MUST wire `data-lm="counter"` on the numeric spans. The premium-UI reviewer adds this to the D-054 10-gate (counter-motion-when-coherent is now gate #11 for templates with numeric bands).
- The `live-forms` listbox radius is now premium by default even when skins use 999px pill fields.

---

## D-079: Agency Category Closure — Vertex + Aura Live Premium with 5 Locales + Real RTL Day One (2026-04-15, Session 49)

**Decision:** `vertex-creative-agency` (`agency-creative-studio` archetype) and `aura-digital-studio` (`agency-digital-studio` archetype) flip from `tier=draft` to `tier=published_live` premium with two fully distinct multipage live skin folders (8 file kinds each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, and sharp D-054 differentiation enforced across every axis (page color, typography, hero silhouette, navbar, work presentation, services framing, process section, inquiry flow, CTA style, premium cues, imagery pool, voice register). Agency category is now 2/2 published_live; catalog floor moves from 11/20 to **13/20 published_live across 6 categories** (medical · restaurant · business · portfolio · ecommerce · **agency**). Phase 2g3.6f closed.

**Concrete shape:**
- Two new DNA archetypes added (`agency-creative-studio` + `agency-digital-studio`) with full vocabulary entries (hero/navbar/footer/card/button/density/tone/conversion/imagery/font_pairing).
- Two skin folders (~7,800 LOC HTML, 8 files each) authored from line one with D-047 chrome-cleanliness, RTL CSS scoped to `.vx-*` / `.au-*` selectors, conditional Arabic font load, 720px mobile breakpoint, `:focus-visible` on every CTA.
- Two IT content registries (~2,700 LOC) + 8 locale trees (~9,800 LOC) authored by 4 parallel sub-agents (one per locale, producing both Vertex + Aura). Voice contracts: Creative Review/Monocle for Vertex EN, TechCrunch/Linear for Aura EN; Libération/M-M Paris for Vertex FR, Maddyness for Aura FR; Apartamento for Vertex ES, Xataka for Aura ES; Brownbook curatorial MSA for Vertex AR, Wamda product MSA for Aura AR. Latin proper names + Latin digits + Latin stack names preserved per D-063.
- Two new per-archetype imagery pools (`agency-creative` editorial-craft + `agency-digital` product-console) using verified Unsplash IDs from `portfolio-designer` / `business-startup` precedents (Pexels deferred per D-077 fallback — `PEXELS_API_KEY` env var not present at session start).
- Chrome i18n extended with `mp_other_agency` key in 5 locales.
- Differentiation matrix (D-054 axis-by-axis): page color (cream paper vs midnight-violet), typography (Space Grotesk + Fraunces italic vs Plus Jakarta + JetBrains Mono), hero silhouette (editorial pull-quote + cover tile vs product-console + dashboard tile), navbar (serif-asterisk + alpha-index vs glow-pill + sprint chip), work presentation (indexed ledger vs metric-card grid), services (4 disciplines manuali vs 4 capabilities deliverable), process (manifesto + 6 principles vs sprint + 3 mindset), inquiry (long-form dossier brief vs 3-step slot picker), CTA (ghost serif italic vs glow violet pill), premium cues (press ribbon vs ship-log + sparkline), imagery (editorial craft vs product UI), voice (curatorial editorial Italian vs growth-tech direct Italian). Two products, not two recolors.
- TEMPLATE_REGISTRY.json bumped to v0.12.0 with full DNA metadata + tier flips + new `phase_2g3_6f_agency_live` block.
- `smoke_full.py` extended (+87 routes net): **530/530 green** post-rollout.
- One in-flight bug caught + fixed during Playwright AR audit: Aura `chip` field carried literal `<span class="pulse"></span>` markup in the data string that Django auto-escaped to visible text. Stripped from all 5 Aura locale files (template provides static pulse). Re-validated in browser. Lesson: AR view catches mixed-script bugs that LTR-only audits miss — always click through AR with a fresh eye.

**Rationale:** agency was the next-largest gap on the public-catalog floor after restaurant (Session 48 closed restaurant 3/3). User directive was explicit: "non aprire nuove categorie", "portare la categoria agency a 2/2 live", "Vertex e Aura devono sembrare 2 prodotti diversi". Session 16's catalog audit had flagged agency as CRITICO sibling-collapse (both templates rendering through shared `agency.html` with hardcoded "Independent design & tech studio" copy). This session closes that gap at the source — by splitting the DNA into two materially different archetypes and by enforcing the differentiation contract from the first authoring pass, not as a post-hoc recolor.

**Trade-off deliberati:**
- **Pexels API integration deferred** — same as Session 48 (D-077 fallback path), TODO follow-up tracked.
- **Two skin folders, not one merged archetype** — same shape as every prior 2g3 rollout (Bottega+Luxe, Pragma+Elevate, Sapore+Brace). Intentional debt.
- **No video on either template** — a curatorial creative studio cannot ship with stock B-roll, a delivery-focused digital studio cannot ship with a generic product-loop. Right video would need commissioned footage. Out of scope.
- **Page kinds chosen per-template** — Vertex `manifesto` (editorial principles essay) vs Aura `sprint` (telemetry process); Vertex `contatti` (long-form brief with discipline + budget bands) vs Aura `brief` (3-step structured intake with slot picker). Each kind fits the brand register, not a generic placeholder.

**Consequence:** (a) agency 2/2 published_live with sharp differentiation; (b) catalog 13/20 across 6 categories; (c) `agency-creative-studio` and `agency-digital-studio` archetypes reusable for future siblings; (d) parallel-agent recipe scales to 2×8 fan-out without modification (now proven 10 times); (e) zero regressions on 11 pre-existing live templates.

**Validation:** `check` clean, sync_template_tiers → 13/7, **530/530 smoke green**, full Playwright walk on 8 routes (Vertex+Aura × home+lavori×2+detail+AR+EN/FR/ES locale spot-checks).

---

## D-078: Restaurant Category Closure — Sapore + Brace Live Premium with 5 Locales + Real RTL Day One (2026-04-15, Session 48)

**Decision:** `sapore-trattoria-pizzeria` (trattoria-warm archetype) and `brace-street-food-lab` (street-modern archetype) flip from `tier=draft` to `tier=published_live` premium with full multipage live skins (6 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, and sharp D-054 differentiation enforced both vs each other and vs the existing Gusto fine-dining template. Restaurant category is now 3/3 published_live; catalog floor moves from 9/20 to **11/20 published_live across 5 categories** (medical · restaurant · business · portfolio · ecommerce). Phase 2g3.6 closed.

**Concrete shape:**

1. **Two new skin folders authored from line one (~6,842 LOC HTML):**
   - `templates/live_templates/restaurant/trattoria-warm/` — 7 files. Cream paper `#f8efde` page color, Libre Baskerville body + Caveat script accent (NOT the DNA's `Caveat` as a structural face — Caveat is a 1-2-spot script garnish on chalkboard daily-specials, "Buon appetito!" stamp, footer wordmark; Libre Baskerville does the structural typography work). Photo-frame hero (`.tw-hero .frame` rotated -1.2deg with rosso accent stamp + handwritten caption). Chalkboard daily-specials band on dark wood panel. Family band with portraits. Hours strip. Tavolata band. Phone+WhatsApp CTA pattern (no cart, no checkout, no delivery).
   - `templates/live_templates/restaurant/street-modern/` — 7 files. Near-black `#0a0a0a` page color, Big Shoulders Display 800/900 condensed UPPERCASE headlines + Inter body + JetBrains Mono technical chips. Tilted product-cutout hero (`.sm-hero .cutout` rotated -2deg with stamped neon `€ 9.50` price-badge). Product-grid menu cards with "AGGIUNGI" CTAs. Real-time queue counter strip ("CODA AL BANCO ≈ 4 MIN" / "ULTIMO ORDINE 23:30 KITCHEN OPEN UNTIL"). GLOVO/DELIVEROO/JUST EAT/UBER EATS marquee. Order-now flow (Al Banco / Takeaway / Delivery 3-route hub).
   - Both skins: full RTL CSS block scoped to `html[dir="rtl"]` on `.tw-*` and `.sm-*` selectors; conditional Amiri+Noto-Kufi font load `{% if is_rtl %}`; Latin proper names + Latin Western digits + Latin currency preserved via `unicode-bidi: isolate` (Sapore) or selector-based isolation (Brace, no `data-latin` per-attribute marker, only RTL CSS rules); 720px mobile breakpoint; `:focus-visible` rings on every CTA; D-047 chrome-cleanliness from line one (zero IT literals in HTML).

2. **Two IT content registries (~1,799 LOC) + 8 locale trees (~6,500 LOC) authored by 8 parallel sub-agents:**
   - Sapore IT: `template_content_sapore.py` ~855 LOC, voice = warm Roman family register, "Da Nonna Rosa, come a casa vostra" register, dishes (Cacio e pepe / Bucatini all'amatriciana / Coda alla vaccinara / Margherita Verace / Cesanese del Lazio), 6 page kinds (home/menu/storia/forno/eventi/contatti), 392 deep-keys.
   - Sapore EN/FR/ES/AR: ~856 LOC each. Voice contracts: Bon Appétit/NYT-Food (EN), Le Fooding/Atabula `tu` (FR), El País Gastro/7 Caníbales `tú` peninsular (ES), Brownbook/cultural-publishing MSA (AR). 0 missing/extra keys per locale, deep-walk parity verified.
   - Brace IT: `template_content_brace.py` ~944 LOC, voice = Bologna street-food brutalist UPPERCASE imperative, "Bruciato al fuoco vivo, servito al volo" register, products (DOPPIO BRACE / SMASH CLASICO / FRITTO MISTO / Pizza al taglio / Mortadella e pistacchio), delivery brands LATIN, 6 page kinds (home/menu/lab/moments/ordina/contatti), 548 deep-keys (different shape than Sapore due to product-grid vs menu-list).
   - Brace EN/FR/ES/AR: ~627-955 LOC each. Voice contracts: Eater/Vice Munchies UPPERCASE (EN), Le Fooding street/Trax `tu` urban-imperative + anglicismes (FR), Time Out Madrid `tú` peninsular + `currar` (ES), Wamda lifestyle/Vice Arabia urban-imperative MSA + Latin product names (AR). 0 missing/extra keys per locale.

3. **Stub-then-replace bootstrap pattern** (Session 41 recipe). 8 stub locale files (`template_content_<slug>_<loc>.py`) created BEFORE wiring imports, each re-exporting `..._CONTENT_IT as ..._CONTENT_<LOC>`. The TEMPLATE_CONTENT dict is wired with all 10 entries (2 IT + 8 locale-pointers). Imports stay green throughout. The 8 parallel sub-agents overwrite each stub with their full locale tree. The validation chain is green at every step.

4. **TEMPLATE_REGISTRY.json updates** (version 0.10.0 → 0.11.0): both rows flipped `tier: draft → published_live`, `dna_phase: "2g3.6"`, `session_closed: 48`, `live_pages` array authored, `locales: ["it","en","fr","es","ar"]`, `rtl: true`, `tier_reason` string with full audit trail. `python manage.py sync_template_tiers` promotes both in the DB.

5. **Smoke harness extensions:**
   - `smoke_full.py`: +2 templates in LOCALES + CATEGORY → **443/443** routes (was 363, +80 inner pages + +10 detail/listing surfaces).
   - `smoke_forms.py`: +2 PAGES (Sapore contatti + Brace contatti) + 2 LOCALES_BY_TEMPLATE entries → **55/55** form routes (was 45).
   - `smoke_i18n_media_hardening.py`: +2 templates in MULTILINGUAL + CATEGORY → **69/69** hardening checks (was 57).

**Rationale:** restaurant category was the smallest gap to close on the public-catalog floor (1/3 → 3/3 in a single session), and the user directive was explicit: "non aprire nuove categorie", "non rifare commerce o editor", "portare la categoria restaurant a 3/3 live". The DNA + preview compositions for both templates already existed from Session 16 catalog audit and prior phase-2f work, so the work was concentrated on (a) skin authoring with sharp visual differentiation, (b) IT content with realistic Roman trattoria + Bologna street-food voice, (c) 5-locale rollout via the now-stable parallel-agent recipe (proven 7 times). The two new skin folders also add reusable archetypes to the catalog: any future warm-family restaurant reuses `trattoria-warm`; any future fast-casual urban food brand reuses `street-modern`. Only when a third sibling is semantically as far from BOTH existing siblings as Sapore is from Brace should a new archetype be split (D-050/D-051 default applies retroactively to restaurant).

**Trade-off deliberati:**
- **Pexels API integration deferred.** `PEXELS_API_KEY` env var not present at session start. Per D-077's env-only key handling rule (the key is never written to repo, memory, docs, or commits) and the session's "non scrivere la chiave nei file" directive, the Pexels search-API integration was skipped for this session. Existing curated Unsplash IDs from `restaurant-trattoria` + `restaurant-street` pools (verified visually in Sessions 31/47) were used instead, plus IT-curated additions for trattoria/street-food coherence. No catastrophic visual mismatches detected in Playwright walks. Pexels CDN swap is documented as a Phase-2g3.6c follow-up in TODO_NEXT for when the key is available — the URL format is hot-link-public, so future swap is one-line per slot. The trade-off: no new editorial video shipped this session (D-077's "one video per DNA register" rule means restaurant DNA would need an explicit motion case, which trattoria-warm doesn't pull for and street-modern only marginally does — late-night DJ booth or grill action could fit but requires real footage; not blocking).
- **Two skin folders, not one merged "restaurant-modern" archetype.** Sapore and Brace are visually opposite enough that merging them would have flattened both into recolors of one skeleton (Session 16's catalog-audit BLOCKING finding for the agency/lawyer/real-estate/medical sibling pairs). The 7-file × 2 = 14 HTML files is intentional debt — same shape as Bottega+Luxe (Phase 2g3.5).
- **Page kinds chosen per template, not standardized.** Sapore: home/menu/about/signature/events/contact. Brace: home/menu/about/gallery/order/contact. The `signature` (forno-a-legna pizza+pasta showcase) and `events` (tavolata) kinds are Sapore-only; `gallery` (urban moments) and `order` (3-route delivery hub) are Brace-only. Each kind maps to a real customer surface, not a generic placeholder. Future restaurant siblings reusing these archetypes inherit the kind per template.
- **Differentiation contracts encoded as cross-leak guards.** D-054 retroactively binds: Sapore-only tokens (`mattarello`, `Nonna Rosa`, `Trastevere`, `forno a legna`, `tavolata`, `Cesanese del Lazio`, `tirata`) must NOT appear on Brace pages; Brace-only tokens (`smashburger`, `scottona`, `CODA AL BANCO`, `GLOVO`, `DELIVEROO`, `Bologna`, `Big Shoulders`, `late-night`) must NOT appear on Sapore pages. Verified: 0 leaks across 480 cross-locale × 10-phrase checks.

**Consequence:** (a) restaurant category closes 3/3 published_live with sharp differentiation; (b) catalog floor advances from 9/20 to 11/20 across 5 categories — the public-catalog "next promotion" target shifts to medical (Phase 2g3.2: salute / benessere / famiglia, 3 templates); (c) the trattoria-warm and street-modern archetypes are reusable for future siblings; (d) the parallel-agent recipe (proven 8 times now) scales to 2-template/8-tree fan-out without modification; (e) zero regressions across the 9 pre-existing live templates (363/363 was, 363/363 still — the +80 routes are all from the new templates).

**Validation:**
- `python manage.py check` → 0 issues
- `sync_template_tiers` → 11 promoted, 0 missing
- Full sweep: **443/443 HTTP 200** (was 363, +80)
- Forms: **55/55 HTTP 200** + .lf-* primitives present (was 45, +10)
- Hardening: **69/69 OK** (was 57, +12)
- Ecommerce regression: **194/194** (no impact)
- Gusto i18n regression: **52/52** (no impact)
- 0 IT leaks across 480 cross-locale checks
- Browser click-through validated: 5 language pills routes correct, RTL flip on AR works, phone/WhatsApp CTAs use correct `tel:` and `wa.me` schemes, internal nav preserves `?lang=` parameter
- Listing `/templates/restaurant/` shows all 3 cards
- D-053 Live Preview Law gate green on both templates
- D-054 Premium Differentiation 10/10 vs both siblings (and vs Gusto)
- D-047 chrome-authoring contract clean from line one

**Key insights:**

1. **Multi-line `{# … #}` Django comments leak to render output.** A multi-line comment like `{# foo\n   bar baz #}` does NOT close on the first inner newline — Django's tokenizer sees the opening `{#` and the closing `#}` (potentially many lines later), and the inner text bleeds into the rendered HTML when there's no proper close on the same line. Use `{% comment %}…{% endcomment %}` for any multi-line documentation. Caught at first Brace/Sapore render — debug "Big Shoulders Display [display condensed (UPPERCASE)..." string visible at top of every page; fixed by switching to `{% comment %}` block. Future skin authoring MUST use `{% comment %}` for multi-line docs.

2. **Apostrophe-in-single-quoted-Python-string is a recurring trap in IT content.** First Brace IT registry had `'TRE GESTI. <em>NIENT'ALTRO.</em>'` — the `NIENT'ALTRO` apostrophe terminated the string mid-value and triggered `SyntaxError: unterminated string literal`. Convention for future content registries: default to **double-quoted Python strings** when content can contain apostrophes (`"…NIENT'ALTRO…"`). Sub-agent prompts now mention this explicitly.

3. **The parallel-agent recipe scales without modification to 8-fan-out.** 4 IT-builder agents (1 per template × 2 templates) followed by 8 locale agents (4 locales × 2 templates) ran in parallel. Each agent had a self-contained prompt with explicit voice contract + differentiation guards + dish-name preservation rules + structural-parity validation step. 0 cross-agent conflicts (each writes a distinct file). 0 quality regressions vs solo authoring. Total wall-clock: ~9 minutes per locale agent, ~15 minutes per IT-builder agent — agents in flight in parallel.

4. **`runserver --noreload` does NOT pick up template OR Python changes between requests on Windows.** Even with `DEBUG=True`. Each template/Python edit needs a server bounce on a fresh port. Same gotcha as Session 19, 23, 42. Future sessions: always restart on a fresh port (8901 → 8902 → 8903 → 8904 in this session).

5. **Playwright `fullPage: true` screenshots can capture mid-fade or pre-fade state when `live-motion.js` IntersectionObserver hasn't fired.** Sections appear blank in the fullpage thumbnail but render correctly when viewed live. Workaround for visual QA: `page.evaluate(() => { document.querySelectorAll('[data-lm]').forEach(el => el.style.opacity = '1'); })` before screenshot. Document this in AGENT_HANDOFF for future visual-validation sessions.

---

## D-077: Media Coherence — Pexels Adopted as Primary Stock-Photo CDN, Unsplash Legacy Only, One Editorial Video on Luxe Lookbook (2026-04-15, Session 47)

**Decision:** all new or replacement stock imagery in the site and templates is sourced from Pexels via its official API, with the key read from `PEXELS_API_KEY` env var only — never committed, never memoized, never logged. Existing Unsplash URLs that serve semantically correct content are left alone (no churn). A single editorial video is added to the Luxe lookbook preview (not any other surface) because only that DNA pulls for moving image; every other surface keeps stills by policy.

**Concrete scope:**

1. **Homepage hero (pages/home.html)** — the `.mw-img-placeholder` wireframe with a `bi bi-window-desktop` icon is replaced with a real hero image: Pexels 4884116 (minimalist laptop on white desk, photographer Artem Podrez). The mockup keeps its aspect-ratio: 4/3, border-radius, and decorative floats; only the inner element is upgraded. Ships with `background-size: cover; background-position: center 45%; box-shadow: 0 30px 60px -20px rgba(15,16,32,0.35)` so the shot reads as a framed hero image rather than a raw stock photo.

2. **Five product hero swaps** (seed_commerce.py):
   - Luxe `rack-atelier-nero`: Unsplash `1551803091-e20673f15770` (woman in blue lace, wrong content for a black leather handbag) → Pexels `35115815` (black leather handbag with gold chain — matches the product's "cuoio nappa · profilo gold · cucitura sellier oro" description exactly).
   - Luxe `bomber-siena`: Unsplash `1495121605193` (ambiguous white tile in shop grid) → Pexels `15895575` (woman in camel bomber with embroidery — matches "Cady tinto a Siena · ricamo Atelier Sentier").
   - Luxe `pantalone-wide-crepe`: Unsplash `1559563458` (tiny weak crop) → Pexels `31400265` (woman in beige wide-leg trouser + hat — editorial).
   - Bottega `borsa-cartolina`: Unsplash `1591561954557` (basket with produce, tangential to a leather bag) → Pexels `11623262` (tan leather satchel on wood — clean).
   - Bottega `tazze-tornite`: Unsplash `1610701596007` (coffee with plants, doesn't show the cups themselves) → Pexels `6611187` (artisan ceramic mugs on shelf).

3. **Luxe preview product gallery (template_content_luxe*.py × 5 locales)** — the 4 occurrences of Unsplash `1548036328-c9fa89d128fa` (acceptable but cropped oddly at the w=1400 size) are uniformly swapped to Pexels `35115815` (same black bag, better Pexels CDN crop behaviour).

4. **Luxe lookbook editorial video overture (live_templates/ecommerce/fashion-editorial/lookbook.html)** — a new `.fe-overture` section is inserted between `.fe-credits` and `.fe-looks`. Shape: a 16:7 frame with `<video autoplay muted loop playsinline preload="metadata">` sourced from Pexels video 4620570 (atelier clothing rack, 31 seconds, 960×506 SD) and a matching poster. A small three-column caption line below credits it: "Atelier · Sentier" / "Moving image · silenzio · 31 secondi" / "Video · Pexels · Cottonbro Studio". Respects `prefers-reduced-motion: reduce` (hides the video element). No controls — this is a moving still life, not a product demo.

**Rationale:** (a) Unsplash hot-linking has repeatedly served semantically wrong content — the Session 45 Rack Atelier Nero woman-in-blue-lace bug, the Session 46 Giubbotto Terra backpack-for-jacket bug — where `HEAD` returned 200 but the rendered image was catastrophically off-brief. Pexels' API + `fit=crop&h=&w=` URL parameters give more stable visual output per URL and the API returns full `alt` text and photographer attribution upfront, making 1-by-1 Playwright visual verification faster. (b) The one-video rule prevents this from becoming a "generic SaaS motion everywhere" pass; Luxe lookbook is the only surface whose DNA is editorial/campaign/moving-image (atelier backstage matches the maison voice), so the video there reads as editorial texture. Bottega DNA is typographic-led (D-074a — "no photo hero"), medical/business/portfolio are photo-premium but not motion, homepage is conversion-focused but a loop there would be decoration noise. (c) Reading the API key from env only keeps the key out of git / memory / docs / logs — a hard policy per the user's directive; the throwaway helper `_pexels_helper.py` is gitignored so nothing of the key's usage leaks into the repo.

**Trade-off:** mixed CDN provenance for the catalog (Unsplash for pre-existing correct URLs, Pexels for new/replacement). Acceptable: both are free-to-use with no attribution-in-image requirement, both support hot-linking, and the URL shape (`cdn.pexels.com/photos/<id>/…` vs `images.unsplash.com/photo-<id>?…`) is parse-discoverable so future audits can tell them apart. The alternative (rewrite every Unsplash URL to Pexels) would churn ~40+ correct images for zero quality gain. Unsplash is kept as legacy; net-new URLs go Pexels first.

**Consequence:** (a) 5 products across Luxe and Bottega now show semantically correct hero imagery, closing the catalog-level image coherence audit open since Session 16; (b) the homepage no longer fronts a wireframe placeholder — the laptop-on-desk hero reads as a finished product, not a dev-mode template; (c) the Luxe lookbook now has the one motion element its DNA allows, lifting the editorial feel; (d) the Pexels integration pattern is documented for future sessions; (e) 53/53 regression routes green, no catalog-tier changes (`published_live` count unchanged at 9/20).

**Key insights:**

1. **Stock-photo CDN coherence is API-verifiable, HEAD-200 is not.** The Pexels API returns `photographer`, `alt` (often 80+ characters of actual content description), and multiple `src.*` variants in one call. You can pre-filter by `alt` text keyword-match before even hitting the image visually. Unsplash's Source API (`images.unsplash.com/photo-<id>`) returns the bytes but no alt/metadata — you need a second call to the search API. Pexels is strictly better for audit workflows.

2. **Env-only key handling is a structural habit.** Writing the key to settings.py or any tracked file is the single biggest CI/CD leak risk. Reading from `os.environ["PEXELS_API_KEY"]` inside a gitignored helper, with the value inline-injected via `PEXELS_API_KEY=xxx python _pexels_helper.py …`, keeps the key out of every persistent surface. The helper file itself is also gitignored so its usage traces leave zero git history.

3. **One video, correctly placed, is premium. Two videos is decoration.** The Luxe lookbook atelier video matches DNA because "atelier backstage" is a real editorial genre the maison voice inhabits. Adding a second video (e.g., homepage, Gusto hero) would erode the signal — motion becomes background noise instead of intentional editorial texture. Future sessions MUST justify each additional video against a real DNA register, not against "it would look good".

---

## D-076: Commerce v2 — /shop Multilingua, Stripe Graceful, Merchant-Scoped Dashboard, Customer Flow Chiuso (2026-04-14, Session 45)

**Decision:** `apps/commerce` passa da foundation v1 (single-seller, IT-only, dev-payment) a v2 operativa su quattro assi incrociati: (a) lo storefront `/shop/<slug>/` e le sue 7 pagine (shop · collezione · product · cart · checkout · order_confirmation · policies · order_lookup + payment Stripe) sono davvero multilingua 5 locales (it/en/fr/es/ar) con RTL vero per arabo; (b) il payment dispatcher è provider-agnostico con stripe reale integrato (`apps/commerce/payments.py`, Stripe SDK lazy, PaymentIntent + webhook con signature verification, idempotency_key=order.reference, graceful fallback a stub se `STRIPE_SECRET_KEY` manca); (c) il seller dashboard passa da `is_staff` global-see-all a `StorefrontMember(storefront, user, role)` scoping reale; (d) customer flow completato con policies page, order lookup self-service (reference + email), retry payment su failed intent, stripe payment page custom con Elements.

Concrete shape:

1. **`apps/commerce/i18n.py`** (~430 LOC) — nuovo modulo i18n che rispecchia `apps/catalog/template_i18n.py`. Re-esporta `SUPPORTED_LOCALES` / `DEFAULT_LOCALE` / `RTL_LOCALES` dal catalog (una sola fonte di verità per il set), definisce `COMMERCE_CHROME` (125 keys × 5 locales = 625 stringhe UI commerce: nav, shop, PDP, cart, checkout, order confirmation, policies, lookup, footer, form labels, status labels). Helpers: `resolve_locale(request)` / `get_chrome(locale)` / `html_dir(locale)` / `is_rtl(locale)` / `locale_switcher_entries(current)` / `localize(translations, locale, field, fallback)` / `preserve_lang_qs(locale)`.

2. **`apps/commerce/content.py`** (~260 LOC) — per-storefront brand-specific copy × 5 locales. `STOREFRONT_CONTENT = {slug: {locale: {tagline, footer_bio, shipping_policy, return_policy, bank_transfer_instructions, nav_atelier_label|nav_maison_label}}}`. `COLLECTION_CONTENT = {slug: {coll_slug: {locale: {title, subtitle}}}}`. Il seeder importa entrambi e popola i JSONField su Storefront/Collection.

3. **Models: 4 nuovi JSONField + 1 nuovo modello** (migration `0003_commerce_v2`):
   - `Storefront.translations` (JSONField) + `.localized_field(field, locale, fallback)` helper
   - `Collection.translations` + `.localized(locale)` → {title, subtitle, description}
   - `Product.translations` + `.localized(locale)` → {title, subtitle, short_description, long_description, material, made_in, badge, info_rows}
   - `ShippingMethod.translations` + `.localized(locale)` → {title, description, est_delivery_days}
   - `StorefrontMember(storefront, user, role=owner|editor)` — unique_together (storefront, user)
   - `Storefront.PaymentProvider` estesa con `STRIPE = "stripe"`

4. **Payment abstraction** (`apps/commerce/payments.py` · 270 LOC):
   - `PaymentContext` (dataclass con order + success_url/cancel_url/return_url)
   - `PaymentDispatchResult` (dataclass con intent + redirect_url + client_config)
   - `dispatch_stub` / `dispatch_offline_bank_transfer` / `dispatch_stripe` (provider functions)
   - `dispatch_stripe` usa `stripe.PaymentIntent.create` con `automatic_payment_methods`, `metadata={order_id, order_reference, storefront}`, `idempotency_key=f"order-{order.reference}"`, `receipt_email`. Amount in cents via `to_integral_value()` per evitare subnormal decimals.
   - `handle_stripe_webhook_event(event)` mappa `payment_intent.succeeded/payment_failed/canceled` → transizioni stato locali PaymentIntent + Order.
   - Graceful fallback: `ProviderUnavailable` (missing SDK o missing `STRIPE_SECRET_KEY`) → `dispatch` crea stub intent con `payload.stub_fallback=True` + log warning. L'ordine resta pagato; il merchant vede `stub_fallback` nell'intent payload e sa di dover configurare le chiavi.
   - `is_provider_available(provider)` runtime probe per dashboard badge.

5. **Views layer** (`apps/commerce/views/customer.py` · 400 LOC):
   - `LocaleMixin` risolve `?lang=` una volta in `setup()` e inietta in context: `locale`, `html_dir`, `is_rtl`, `chrome`, `locale_switcher`, `lang_qs`, `storefront_content`, `storefront_tagline`, `storefront_footer_bio`, `storefront_shipping_policy`, `storefront_return_policy`, `storefront_bank_instructions`, `collections_i18n`.
   - Views pre-calcolate `products_l10n` (list), `product_l10n` (dict), `cart_lines` (list con `{item, product, l10n}`), `shipping_methods_l10n`, `shipping_method_l10n` per usare template ergonomici.
   - Nuove views: `PoliciesView`, `OrderLookupView` (guest reference+email → redirect a confirmation se match), `PaymentPageView` (Stripe Elements con client_secret da PaymentIntent.payload), `RetryPaymentView` (POST per riprovare payment failed), `StripeWebhookView` (csrf_exempt, verifica signature con `STRIPE_WEBHOOK_SECRET`).
   - Checkout ora routa a `commerce:payment_page` se intent stripe initiated, altrimenti a confirmation.

6. **Seller scoping** (`apps/commerce/views/seller.py` · 320 LOC):
   - `SellerRequiredMixin` ora estende `LoginRequiredMixin`; in `dispatch` carica lo storefront per slug e verifica `_user_can_access(user, sf)` (membership OR superuser). Anonymous → login redirect; staff senza membership → `PermissionDenied` (403).
   - `_user_storefronts_qs(user)` + `_user_can_access(user, sf)` helpers.
   - Nuovo `DashboardRootView` a `/dashboard/` (no slug): redirect auto se single-membership, altrimenti card chooser. Mostra badge superuser se applicabile.
   - `DashboardHomeView` ora espone `payment_provider_ok` (bool da `payments.is_provider_available`), `payment_provider_label`, `members` (queryset `sf.members.select_related('user')`), `all_storefronts`.

7. **Forms chrome-driven** (`apps/commerce/forms.py`):
   - `CheckoutForm.__init__` accetta `chrome=` e `locale=` e sovrascrive `fields[*].label` dal dict; `shipping_method.choices` usa `m.localized(locale).title` per i titoli localizzati.
   - Nuovo `OrderLookupForm(reference, email)` con chrome-driven labels.
   - Nuovo `StorefrontMemberForm` per admin inline.

8. **Templates × 5 locales** (entrambi skin):
   - `_base.html` × 2 skin — html[lang/dir] dinamico, conditional Amiri + Noto Kufi per Arabic, language switcher (5 pills) nella mp-bar, `chrome.*` keys ovunque, `storefront_tagline`/`storefront_footer_bio` dal JSON, tutti gli internal hrefs con `{{ lang_qs }}`, RTL CSS block completo, footer link a `commerce:policies` e `commerce:order_lookup`.
   - shop, product, cart, checkout, order_confirmation × 2 skin — chrome-driven ovunque, iterano `products_l10n`/`cart_lines`/`related_l10n`/`shipping_methods_l10n`, product titolo/desc da `product_l10n`.
   - Nuovi: `policies.html` × 2 skin (3 cards: shipping/returns/contact con icon 01/02/03 e accent color per skin), `order_lookup.html` × 2 skin (centered form reference+email), `payment/stripe.html` (skin-agnostic clean card con Stripe Elements + fallback friendly se non configurato + RTL supported).
   - `dashboard/_base.html` — nav "Cambia storefront" + "Esci"
   - `dashboard/home.html` — 3 cards nuove (Pagamenti con badge ok/warn, Membri con role pills, Collegamenti rapidi)
   - `dashboard/root.html` — chooser page multi-storefront

9. **Seeder esteso** (`apps/commerce/management/commands/seed_commerce.py`):
   - Nuova `SHIPPING_TRANSLATIONS` dict × 5 locales per i 7 codici shipping (3 Bottega · 4 Luxe) allineati ai codici già seedati (italy-48h, italy-pickup, europe-4d, maison-milano, maison-italia, maison-europa, private-appointment).
   - `_seed_storefront` popola `Storefront.translations` da `commerce_content.STOREFRONT_CONTENT`, `Collection.translations` da `COLLECTION_CONTENT`, `ShippingMethod.translations` da `SHIPPING_TRANSLATIONS`.
   - Nuova `_seed_demo_merchants`: crea `bottega_owner` + `luxe_owner` users (is_staff=True, password `commerce-v2`) + `StorefrontMember(role=OWNER)` ciascuno. Idempotente — ri-eseguire non resetta le password.

10. **URLs + settings**:
   - Nuovi path: `shop/<slug>/politiche/`, `shop/<slug>/ordine/`, `shop/<slug>/order/<uuid>/payment/`, `shop/<slug>/order/<uuid>/retry-payment/`, `commerce/webhook/stripe/`, `dashboard/` (root chooser).
   - `settings.py` aggiunge `STRIPE_SECRET_KEY` / `STRIPE_PUBLISHABLE_KEY` / `STRIPE_WEBHOOK_SECRET` letti da env, + `STRIPE_ALLOW_STUB_FALLBACK` toggle (default True).

**Rationale:** la direttiva era portare il commerce v1 — "poster operativo single-seller, IT-only, dev-payment" — a uno stato boutique online reale senza riscrivere da zero. Ogni pezzo v1 è stato conservato (Storefront, Product, Variant, Cart, Order, PaymentIntent hanno ancora tutti i loro campi originali) e la v2 è additiva (JSONField nuovi con default=dict, nuovo modello isolato, nuovo modulo payments al posto dei `_handle_*` inline, LocaleMixin sovrappone senza toccare ListView/DetailView già funzionanti). Lo stripe adapter è lazy (import dentro la funzione, degrada a ProviderUnavailable) perché la baseline dev usa SQLite senza chiavi e non deve 500-are — il dispatcher falla graceful a stub e logga. Lo scoping merchant con membership è più robusto di "storefront.owner FK" perché una stessa boutique può avere più owner/editor e perché un utente può gestire più storefront (il chooser esiste proprio per questo). Il customer flow si chiude con retry e lookup perché senza questi due una boutique online non è credibile: il primo salva l'ordine dopo una carta rifiutata, il secondo salva il cliente dopo una email di conferma persa.

**Trade-off deliberati:**
- Il dashboard resta IT-only (non è customer-facing; localizzarlo × 5 lingue sarebbe churn senza valore). La migrazione può essere aggiunta in v3 senza toccare il chrome customer.
- `Product.translations` è un singolo JSONField con lookups stringa invece di rows per-locale. Scelta deliberata: evita una tabella di traduzione con schema rigido, allinea al pattern `template_content_*.py` del catalog, e la query cost è zero (il campo è letto in memoria dopo select_related). Quando il volume cresce oltre ~10k prodotti × 5 locales si potrà migrare a `ProductTranslation(product, locale, field, value)` senza rompere il consumer (`product.localized(locale)` resta la stessa API).
- Stripe è single-account: una sola `STRIPE_SECRET_KEY` serve tutti gli storefront. Multi-account (un secret key per merchant) richiede Stripe Connect — documentato come evoluzione v3, non bloccante in v2.
- Nessun email sending automatico (order confirmation email non viene inviata). Richiede `django-anymail` + provider transactional. Spostato a v3; customer note "write us for help" rimane l'escape hatch.
- Nessun coupon/promotion/tax engine — non richiesto, conservati campi (`tax_total`, `compare_at_price`) per estensione futura.

**What's operational NOW (with and without env vars):**
- Without env vars: stub + offline_bank_transfer payment path end-to-end funzionante, i ordini confermano auto, il dashboard mostra warning giallo sul Payments card se lo storefront è impostato su stripe. Ideale per dev e QA.
- With `STRIPE_SECRET_KEY` + `STRIPE_PUBLISHABLE_KEY` + `STRIPE_WEBHOOK_SECRET` + `pip install stripe`: Stripe reale in test mode (switch su live mode = cambio della chiave); la webhook route `/commerce/webhook/stripe/` riceve gli eventi Stripe e aggiorna `PaymentIntent.status` + `Order.payment_status` localmente.

**Consequence:** (a) la baseline commerce passa da "v1 foundation" a "v2 operativa multi-tenant-ready"; (b) il cliente accede in 5 lingue con real RTL; (c) un merchant loggato non vede i dati di un altro; (d) un pagamento Stripe reale gira end-to-end su chiavi env; (e) un cliente che ha perso la email di conferma può recuperare l'ordine con reference + email senza contattare il merchant; (f) un pagamento fallito può essere ritentato senza rifare il carrello — lo stock era già locked.

**Validazione:**
- `python manage.py check` → 0 issues
- Migration `0003_commerce_v2` applicata pulita
- 73/73 routes commerce green (customer flow × 5 locales × 2 skin)
- 45/45 live preview routes green (9 templates × 5 locales, zero regressione catalog)
- ACL validation: anon→302, bottega_owner sul proprio dashboard→200, sul luxe dashboard→403; luxe_owner sul proprio→200, sul bottega→403
- Payment flow: add_to_cart→302, checkout POST→302 con order creato `payment=paid status=confirmed` (stub), order confirmation AR→200, order lookup POST con reference+email match→302
- Stripe availability probe: `is_provider_available('stripe')` False senza env, True con env + `pip install stripe`

**Key insights:**

1. **JSONField translations beat a translation table here.** Un `ProductTranslation(product, locale, field, value)` modello sarebbe più "Django idiomatic" ma costringe ogni authoring a creare N rows. Il JSONField è un dict Python lato authoring (lo stesso `{locale: {field: value}}` che già usa il catalog) ed è zero-cost per la read path (un `select_related`).

2. **LocaleMixin vs template context processor.** Un context processor avrebbe iniettato il chrome globalmente, ma un customer visita le catalog pages (IT-only) e le commerce pages (5 locales) dentro la stessa session. Un processor globale avrebbe dovuto sapere "sei in commerce?" aggiungendo complessità. Il mixin per-view è più cheap e più testabile.

3. **Graceful fallback is a production guardrail.** La tentazione era fare raise se `STRIPE_SECRET_KEY` manca. Sarebbe corretto ma rompe QA. Il fallback a stub + `stub_fallback: True` nel payload + warning log dà la corretta telemetria al merchant ("c'è un problema di config") senza rompere la user experience.

4. **Merchant scoping ≠ permission system.** Si poteva scegliere di aggiungere `django-guardian` o un permission framework completo. Un modello custom `StorefrontMember(role=owner|editor)` copre il 95% dei casi (un merchant vede solo i propri prodotti/ordini) con ~40 righe di codice. Se in futuro serve granular permissions (e.g. "editor può aggiungere prodotti ma non rimuoverli") si aggiunge un campo `permissions` al Member senza toccare il mixin esistente.

5. **Stripe idempotency_key = order.reference.** Senza questo una retry accidentale (browser refresh, timeout, network glitch) creerebbe due charges. Con `idempotency_key=f"order-{order.reference}"` Stripe fa la deduplica lato suo — la seconda chiamata ritorna il medesimo PaymentIntent. Questa è la differenza tra un'integrazione stripe toy e una production-grade.

---

## D-075: Commerce Foundation v1 — Shared Engine Ships Under apps/commerce, /shop + /dashboard Orthogonal To /templates Live Preview (2026-04-14, Session 43)

**Decision:** `apps/commerce` is no longer an empty stub. It now ships the full engine that turns `bottega-shop-artigianale` and `luxe-fashion-store` from "live preview premium templates" into real operational shops — catalog (Product + Variant + Image + Collection), basket (Cart + CartItem, session-keyed), checkout (Address + ShippingMethod + Order + OrderItem + PaymentIntent), seller dashboard (products/variants/orders CRUD + status transitions), and a provider-agnostic payment abstraction shipping two providers in v1 (stub auto-confirm · offline_bank_transfer · Stripe is documented extension point, not implemented).

Concrete shape:

1. **Models** (`apps/commerce/models.py`, 15 models): `Storefront` (OneToOne → WebTemplate, skin enum + payment_provider + is_operational gate) · `Collection` · `Product` (storefront FK + info_rows JSON for typographic spec tables) · `ProductImage` · `ProductVariant` (3 option axes + stock + price_override) · `Cart` + `CartItem` (session-keyed, user optional) · `Address` · `ShippingMethod` · `Order` (uuid + 10-char reference + 3 independent status enums: status/payment_status/fulfillment_status) · `OrderItem` (snapshot) · `PaymentIntent` (provider-agnostic).

2. **Services + Selectors** — thin view layer, all writes in `services.py` (add/update/remove cart, create_order_from_cart with `select_for_update` stock lock + atomic transaction, mark_order_paid, set_order_fulfillment, cancel_order with stock rollback), all reads in `selectors.py` (list_active_products with sort/search/collection filter, get_product_detail with prefetch, dashboard_stock_summary).

3. **Two orthogonal URL spaces.** `/shop/<storefront_slug>/...` is customer-facing operational commerce (shop, collection, product, cart with add/update/remove, checkout, order_confirmation). `/dashboard/<storefront_slug>/...` is seller operational (home, products list/CRUD, variants CRUD inline, orders list/detail with state transitions). The pre-existing `/templates/<cat>/<slug>/preview/…` live-preview routes are UNTOUCHED — they remain the marketing surface.

4. **Two skin template sets** — `templates/commerce/skins/artisan-workshop/` (Bottega: warm cream palette, Playfair + Inter, stamp-shadow CTA, `.aw-*` namespace) and `templates/commerce/skins/fashion-editorial/` (Luxe: ink charcoal palette, Cormorant italic + gold outline, outlined-gold CTA, `.fe-*` namespace). Each set covers _base + shop + product + cart + checkout + order_confirmation. Skin-agnostic widgets live in `static/css/commerce.css` with `--cx-*` tokens set per-skin.

5. **Dashboard is single-themed** (`templates/commerce/dashboard/_base.html` + home + products_list + product_form + orders_list + order_detail). Admin-leaning navy/bone with pill status colors, not skinned per storefront — dashboards are seller-facing, not customer-facing, so skin fidelity isn't the gate.

6. **Guest-first checkout.** No login required. Cart is session-keyed, user FK is optional. Order confirmation is addressable by UUID. Seller dashboard is gated by `is_staff` (`SellerRequiredMixin` → `/admin/login/?next=…`). A `Seller` model scoping users to specific storefronts is a documented future split.

7. **Seed command** (`python manage.py seed_commerce [--reset]`) materializes 9 Bottega products + 8 Luxe products with 16+23 variants + 4+5 collections + 3+4 shipping methods. Idempotent. Pulls copy and imagery from the existing `template_content_bottega.py` / `template_content_luxe.py` IT registries so the live preview and the real shop stay in sync voice-wise.

**Rationale:** the user's product directive was unambiguous — "Bottega e Luxe devono poter funzionare da vero shop, non da poster premium". The existing 9/20 published_live catalog was peak-polished as a showcase but had zero operational surface: no products in DB, no cart, no checkout, no dashboard. Session 43 closes that gap structurally. The design deliberately leaves the /templates/ preview URLs unchanged (existing session artifacts — i18n trees, D-073 rollout, D-074 polish — are load-bearing for the marketing/showcase layer and MUST NOT regress). Commerce is a parallel layer mounted at `/shop/` that reuses the same brand identity but exposes real operations.

**Trade-off:** the skin chrome CSS is duplicated between `templates/live_templates/ecommerce/<archetype>/_base.html` (preview) and `templates/commerce/skins/<skin>/_base.html` (operational). This is intentional — the two surfaces have different nav targets (preview chrome links to /templates/ preview pages; commerce chrome links to /shop/ and /dashboard/), different content blocks (preview has i18n locale switcher; commerce drops it for now since `/shop/` is IT-only in v1), and different CTA registers (preview's "visita la bottega" marketing CTA vs commerce's "aggiungi al carrello" operational CTA). Sharing a common partial would force both surfaces to compromise. The duplication is flagged for future consolidation once the commerce surface gains i18n (Phase 3b).

**What's in v1 (operational right now):**
- Product catalog with active/draft/archived status + featured flag + collections
- Variants with stock tracking (transactional stock decrement on order creation, stock rollback on cancel)
- Cart (session-keyed guest cart, add/update/remove, subtotal computation, item-count nav pill)
- Checkout form (nome + email + indirizzo + spedizione + note; validates via `CheckoutForm`)
- Order creation with `select_for_update` stock lock + PaymentIntent auto-dispatch (stub provider auto-confirms; offline_bank_transfer prints wiring instructions)
- Order confirmation page with totals, shipping address echo, payment status + instructions
- Seller dashboard: stock summary, recent orders, product CRUD, variants inline CRUD, orders list with status filter, order detail with mark-paid + fulfillment update + cancel (stock rollback)
- Django admin integration for every commerce model

**What's deliberately out of scope (Phase 3b):**
- Real Stripe integration (abstraction point is clean — add `_handle_stripe` + webhook view)
- Customer account pages (order history requires login flow)
- i18n for /shop/ (IT-only in v1; the /templates/ preview pages keep 5-locale coverage)
- Coupons / promotions / tax engine (`tax_total` field exists but always 0)
- Reviews, wishlists, faceted search
- Per-storefront seller scoping (any is_staff user today sees any dashboard)
- Carrier integrations (tracking number is free text)

**Consequence:** (a) the catalog remains 9/20 published_live but 2/9 of those now ALSO have operational commerce surfaces; (b) a Phase 3a ship-floor is established — any future ecommerce sibling that gets `is_operational = True` must use this shared engine, never reinvent cart/checkout; (c) the skin-templates-per-storefront pattern is the bar for future premium shops; (d) the existing 867/867 catalog validation matrix stays green plus the new 47/47 `smoke_commerce.py` proves the flow end-to-end.

**Key insights:**

1. **Orthogonal URL spaces beat overloading.** First instinct was to fold real commerce into the existing `/templates/<cat>/<slug>/preview/shop/` route (replace the registry-driven product grid with DB-driven). That would have fought the D-053 "Live Preview Law" which treats that URL as a marketing/showcase surface. Splitting to `/shop/<slug>/` kept the preview intact and made the commerce surface first-class.

2. **Dashboard fidelity ≠ storefront fidelity.** Skinning the seller dashboard per-storefront was tempting (visual consistency with the shop) but wrong — sellers are operators, not shoppers. They benefit from a consistent admin-leaning tool layout across every shop they run. Keeping the dashboard single-themed also keeps the CSS surface small.

3. **Payment abstraction from line one, Stripe later.** Building `PaymentIntent` as provider-agnostic from the start (with a `_dispatch_payment` switch on `storefront.payment_provider`) means adding Stripe later is a file-level add, not a schema change. The `stub` provider auto-confirms in dev so the end-to-end flow is testable without any real PSP. The `offline_bank_transfer` provider is real-usable today — the seller marks the order paid once the wire lands.

4. **Stock lock on SQLite is a no-op but the code is Postgres-ready.** `select_for_update()` silently does nothing on SQLite. The service is already written to assume it works. When production moves to Postgres (planned per ARCHITECTURE.md), the overselling race window closes automatically with zero code change.

---

## D-074: eCommerce Premium Polish — Bottega Portrait→Typographic Conversion (DNA-Honest) + Luxe Editorial Motion Pass (2026-04-14, Session 42)

**Decision (D-074a — Bottega):** all 6 portrait slots in the artisan-workshop skin are converted to typographic stamp tiles. No portrait images on Bottega anywhere. The makers band's 4 cards become ink-bordered cream stamps with: corner-N number (01-04), top-right "BOTTEGA" rubber stamp, big italic letter S/C/B/A as crest mark with "Firmato" annotation, then maker name + craft + place + since + quote. The atelier founder block becomes a 240px circular cream stamp with "M·A" italic monogram + "DAL 1968" underneath + dashed inner ring. The product detail artisan signature becomes a 200px circular monogram with the artisan's first initial + "FIRMA" stamp.

**Decision (D-074b — Luxe):** ~280 LOC of editorial motion CSS added to fashion-editorial `_base.html` enriching every maison section with motion that reads as italic-thinking unhurried — never tech-startup. Hero cover breathes (1.000→1.022→1.000 over 14s ease-in-out). Hero headline italic-axis settles (letter-spacing -0.020em → -0.035em over 1200ms with 220ms delay). Editorial tile strip + lookbook tiles get slow zoom + gold underline scaleX slides + name letter-spacing expand on hover. Manifesto KPI band + maison atelier numbers band animate counters (12, 45, 9, 3 / 12, 3, 45, 9) with stagger 160-180ms + tabular-nums + gold rule scaleX(0.4) slide-in. Press strip converts from static row to `.lm-logo-marquee` (slow editorial drift, 100s duration, italic Cormorant 22px). Drop card gets pulsing gold dot (2400ms infinite) + top-edge gold rule slide on enter. Primary button gets gold panel translateX slide-in from left (button inverts to ink-on-gold). Nav links + ghost button + atelier cards + press list + maison cards all get letter-spacing or color hover language. Reduced-motion fallback kills every keyframe + transition.

Both decisions paired with image-coherence fixes:
- Bottega: 4 broken Unsplash IDs + 5 wrong-content IDs (HEAD-200 but visually catastrophic — blue stilettos, classroom, restaurant workers, computer screens, Bond Street tube station, a CAT, cupcakes, espresso machine, woman-with-thermos) all replaced. Final pool reduced to 4 distinct verified-coherent IDs (down from 8) since the 6 portrait slots now use typographic stamps.
- Luxe: 5 wrong-content/broken IDs swapped — Borsa Isola CAT → red leather handbag · Sentier atelier BOND STREET TUBE → atelier interior with clothes on rack · Giulia direttrice WOMAN-IN-HOODIE → woman in white blazer (professional creative director).

**Rationale:** the user's visual review of Session 41 caught two architectural problems neither of which was pure cosmetic:

1. **Image sourcing on Unsplash is structurally unreliable.** HEAD requests return 200 for IDs that visually serve completely unrelated content. The standard mitigation (curate IDs once, verify visually) doesn't scale when 6 of 6 portrait slots need to render specific older Italian artisans. Even the parallel curator sub-agent dispatched in this session timed out without producing output. The correct structural fix is to NOT source portraits — the artisan-workshop archetype was originally designed (Session 15 DNA notes: "typographic-led hero, NO photo") as photo-independent precisely so a failing image URL degrades gracefully. The Session 41 skin authoring drifted from that DNA by adding 6 portrait slots. The Session 42 polish puts the DNA back: typographic stamp tiles for makers, circular monograms for founder + artisan signature. This sharpens the differentiation vs Luxe (which IS image-driven by design — fashion-editorial campaign portraits) and removes the failure mode entirely.

2. **Luxe was rendering as a polished but motionless poster.** Maison-editorial premium positioning needs interaction depth that reads as italic-thinking — counter slow-cadenced, marquee very-slow drift, tile zoom unhurried, hover language letter-spacing-driven not bounce/tilt. The Session 41 motion adoption was minimal (data-lm="reveal" cascades only). The Session 42 pass adds 18 distinct motion targets across hero, tile strip, lookbook teaser, manifesto, press, drop card, private CTA, and every page-level interactive surface. Every motion choice deliberately distinguishes from the startup-saas-landing motion vocabulary (fast cubic-bezier, glow shadows, tilt on hover): Luxe uses cubic-bezier(0.16, 0.84, 0.32, 1) with longer durations (600-1400ms) and stays planar (no transforms beyond translateY/X) — a "settling poster" feel, never a "snappy interface" feel.

**Trade-off:** Bottega loses 6 portrait slots' worth of human warmth that a perfectly-curated photo would have provided. Acceptable: a typographic stamp tile reads as MORE artisanal than a generic stock-photo portrait, AND it's photo-failure-immune. The DNA was always typographic-led; this fix returns to the DNA. Luxe gains ~280 LOC of motion CSS that loads on every Luxe page; the reduced-motion fallback short-circuits everything for accessibility users and the keyframes are GPU-compatible (transform/opacity only). The press strip converts from a single static row to a marquee that requires `live-media.css/js` to be linked — added to Luxe `_base.html` (was previously linked only on business archetypes). Marginal CSS+JS payload increase (~14KB combined) is acceptable for the visual-quality lift.

**Consequence:** (a) Bottega is now archetype-consistent typographic-led; (b) Luxe is now interaction-rich editorial-grade; (c) the 9-template `published_live` catalog ships with sharper differentiation (Bottega = typographic-stamp identity vs Luxe = animated editorial); (d) the Session 41 D-073 baseline + Session 42 D-074 polish together set the expected quality floor for any future ecommerce sibling — typographic-stamp pattern for any artisan-warm sibling, motion-rich pattern for any maison-editorial sibling; (e) the 867/867 validation matrix still passes with zero regressions.

**Key insights:**

1. **HEAD-200 ≠ visually correct.** Unsplash hot-link IDs serve unrelated content for many random IDs. The reliable verification is `curl + Read tool` per candidate (the Session 37 Chiara recipe). When that's not feasible (e.g., 9+ slots × 30 candidates = 270 visual checks), prefer ARCHITECTURAL elimination of the photo requirement (typographic substitute, gradient placeholder, illustrated icon) over endless candidate hunting.

2. **DNA notes are binding.** When a session's authoring drifts from documented DNA notes, the right fix is to return to the DNA — not to patch around it. Session 15 DNA explicitly flagged Bottega as "typographic-led hero, NO photo, full cream page" — the Session 41 skin author added 6 portrait slots ignoring that note. Session 42 closed the gap by re-adopting the DNA. Future authoring sessions MUST cross-check DNA notes in `template_dna.py` before adding image-dependent elements.

3. **Motion language must match brand register, not generic premium.** Luxe motion pass was deliberately authored as "italic-thinking unhurried" — long durations, tabular-nums counters, marquee at 100s drift, hero scale at 14s breathe, button slides at 600ms. The reference negative was startup-saas-landing motion (200ms snappy timings, glow shadows, micro-bounce). Both are "premium" but for opposite registers. Future motion adoption must articulate the register match before authoring.

---

## D-073: eCommerce Live Rollout — Phase 2g3.5 Closes With Bottega + Luxe Promoted Under D-053 / D-054 / D-047 / D-066, 9/20 Catalog Mark Reached (2026-04-14, Session 41)

**Decision:** `bottega-shop-artigianale` and `luxe-fashion-store` are flipped from `tier=draft` to `tier=published_live` in a single session. Both ship full multipage live skins (6 page routes each: home + shop|collection + product detail + about/atelier|maison + journal|lookbook + contact), 5 locales fin da subito (it/en/fr/es/ar with real RTL for Arabic), zero D-054 cross-tenant leaks, full D-047 chrome-cleanliness from the first commit, full D-066 forms primitive coverage on contact pages.

Concrete shape:

1. **Two new skin folders (~5,500 LOC of HTML)** at `templates/live_templates/ecommerce/artisan-workshop/` and `templates/live_templates/ecommerce/fashion-editorial/`. Each folder carries `_base.html` + 6 page templates (home, shop|collection, product, about, journal|lookbook, contact). The two `_base.html` files are deliberately divergent shells — Bottega's runs warm cream `#f6ecd8` with `.aw-*` selectors and circular-crest nav; Luxe's runs ink charcoal `#08070a` with `.fe-*` selectors and minimal-serif nav. Each skin has its own `html[dir="rtl"]` block with conditional Amiri + Noto Kufi Arabic font load + `unicode-bidi: isolate` on Latin proper names / prices / phone numbers / city names. Both skins respect motion language (D-058) with calibrated profiles (Bottega `--lm-rise: 12px` warm/slow; Luxe `--lm-rise: 14px` editorial/slow).

2. **Two IT content registries (~1,210 LOC)** authored before sub-agent dispatch — `template_content_bottega.py` (590 LOC) carries the warm-artisan Tuscan voice (12 botteghe, Santa Croce sull'Arno conceria, Montelupo ceramic atelier, Prato linen looms, edition numbers like N° 042, La Bottega di Martino brand, phone-and-whatsapp conversion); `template_content_luxe.py` (620 LOC) carries the maison editoriale voice (Maison Luxe, Milano · Paris · Tokyo, Atelier Sentier in rue du Mail, drop semestrali SS26, Look 03 / Drop 02 vocabulary, private viewing conversion, formal `Lei`).

3. **Eight parallel sub-agents authored 8 locale trees (~6,400 LOC total).** `template_content_bottega_{en,fr,es,ar}.py` (~800 LOC each) carry artisanal native voice per locale: EN Aesop/Toast/Etsy informal-warm, FR Astier de Villatte / Merci `tu` artisan, ES peninsular `tú` artesano, AR cultural-publishing register (Brownbook / Bait Al-Hikma). `template_content_luxe_{en,fr,es,ar}.py` (~830 LOC each) carry maison native voice per locale: EN The Gentlewoman / Net-a-Porter formal editorial, FR Hermès / Le Bon Marché `vous` maison, ES Vogue España peninsular `usted`, AR Vogue Arabia luxury-maison register. Voice contrast vs sibling is enforced by sub-agent voice contracts and verified by the new cross-leak smoke (`smoke_ecommerce_rollout.py` — 0/120 cross-tenant tokens leaked across 5 locales × 12 pages × 2 directions).

4. **`TEMPLATE_REGISTRY.json` v0.9.1 → v0.10.0** — both ecommerce rows now carry `tier=published_live`, `archetype`, `dna_phase=2g3.5`, `session_closed=41`, `live_pages=[...]`, `locales=[it,en,fr,es,ar]`, `rtl=true`. `python manage.py sync_template_tiers` applied the flip (catalog distribution: 9 published_live / 11 draft).

5. **Smoke harness extended.** `smoke_full.py` route count 282 → 363 (+81 from 2 new templates × 5 locales × ~7 pages avg + new `/templates/ecommerce/` listing); `smoke_forms.py` 35 → 45 (+10 from 2 ecommerce contatti × 5 locales); `smoke_i18n_media_hardening.py` 45 → 57 (+12 from 2 new multilingual templates added to MULTILINGUAL bucket); new `smoke_ecommerce_rollout.py` (194 checks) covers the dedicated D-054 leak gate + AR Latin-isolation + 5-pill switcher presence + dir="rtl" + Arabic font load.

**Rationale:** the user's product directive after Session 40 closed (7/7 multilingual, but 13/20 still draft) was to advance the published_live catalog beyond 7. Phase 2g3.5 in CATEGORY_ROADMAP was the natural next step — eCommerce had DNA + preview compositions ready since Session 15 and was blocked only on (a) the latent D-047 leaks in the legacy preview compositions and (b) skin-folder authoring. Both blockers were resolved in this session by authoring the skins under the D-047 contract from line one (the legacy preview compositions remain untouched, used only for the static listing PNG). Bottega + Luxe were a particularly attractive next pair because their DNA tones are SHARPLY OPPOSITE (warm cream artisan vs ink charcoal maison), which makes them an ideal D-054 stress test for ecommerce — a category where the temptation to ship two visually-similar product-grid templates is highest. Going live with sharp differentiation now sets the bar for any future ecommerce sibling (e.g. specialty-foods, vintage-archive). The 5-locale-fin-da-subito policy mirrors the post-Session-40 standard: every new published_live template ships multilingual on day one, never IT-then-i18n-later. This avoids the Session 36 D-069 silent-disparity antipattern entirely.

**Trade-off:** ~12,500 LOC authored in one session (~5,500 skin HTML + ~1,210 IT content + ~6,400 locale content + ~150 smoke + ~50 wiring). The bulk was parallelizable: the 8 locale sub-agents ran concurrently in ~5–10 min each. The serial work was the IT skin + content authoring (~3 hours). Acceptable: the same recipe was already proven in Sessions 32 (Pragma + Elevate live rollout in IT-only mode + Session 40 i18n completion as a separate session) and Sessions 34 + 37 + 39 (Chiara + Pixel live rollout + perfection passes). This session compressed the rollout-then-i18n-later pattern into a single rollout-with-i18n-on-day-one pattern. Future ecommerce siblings (Phase 2g3.5b if a 3rd ecommerce template ever lands) should reuse one of the two skin folders without splitting the archetype, unless the new sibling is semantically as far from BOTH existing siblings as Bottega is from Luxe.

**Consequence:** (a) Phase 2g3.5 is closed; (b) catalog floor moves from 7 to **9 published_live** templates, all multilingual, across **5 categories** (medical/restaurant/business/portfolio/ecommerce); (c) the 11 remaining draft templates (sapore · brace · salute · benessere · famiglia · vertex · aura · lex · juris · casa · villa) belong to phases 2g3.1 (restaurant — 2 templates), 2g3.2 (medical — 3 templates), 2g3.6 (agency + lawyer + real-estate — 6 templates); (d) Phase 3 (auth/checkout/editor/projects/commerce) remains gated on Phase 2g3.6 fully closing per D-049/D-053; (e) the `smoke_ecommerce_rollout.py` cross-leak gate is the binding contract for any future ecommerce sibling — a regression PR that introduces a Bottega vocabulary token on a Luxe page (or vice versa) must be rejected; (f) the two skin folders are now reusable archetypes for any future ecommerce template that fits one of the two macro tones (warm-artisan-workshop or maison-editorial); (g) the `category_ready` test (Session 20) passes for ecommerce — it is the 5th category to satisfy the test (after medical, restaurant, business, portfolio).

**Key insight (consolidating Sessions 23/29/37/39/40/41):** the recipe for "ship a sibling pair to published_live + 5 locales in one session" is now stable enough to be a checklist:
1. Author both IT content registries first (with D-047 contract from line one — never paste literals, every string flows from `page_data.*` / `site.*` / `chrome.*`).
2. Author both skin folders next (in parallel if you have the bandwidth; serial otherwise — they share no files except smokes).
3. Wire IT into `template_content.py` + flip tier in `TEMPLATE_REGISTRY.json` + `sync_template_tiers`. Validate IT-only with smoke_full. This is the bootstrap baseline.
4. Dispatch 8 parallel sub-agents (one per locale × 2 templates) with explicit voice contracts that articulate the differentiation gate as a "must NOT contain X" + "must contain Y" pair. The voice contract is the D-054 enforcement mechanism at authoring time.
5. While agents work: extend smoke_full + smoke_forms + smoke_i18n_media_hardening + author a new `smoke_<category>_rollout.py` that codifies the D-054 cross-leak gate as bidirectional vocabulary checks.
6. When agents return: shape-diff each tree (must be 0 missing / 0 extra keys), wire imports, run the full validation matrix.
7. Update memory + DECISIONS + SESSION_LOG + TODO_NEXT + AGENT_HANDOFF + CATEGORY_ROADMAP + TEMPLATE_REGISTRY in a single follow-up commit.

This is now the standard pattern. Future per-category live-rollout sessions should follow it without modification.

---

## D-072: Pragma + Elevate i18n Completion Pass — Full 5-locale rollout for the last two IT-only published_live templates (2026-04-14, Session 40)

**Decision:** `pragma-corporate-suite` and `elevate-startup-landing` are brought from IT-only to fully multilingual (5 locales + real RTL for Arabic) in a single session. The 7-template `published_live` catalog now ships **7/7 multilingual**. Three concrete changes:

1. **5-locale rollout for both templates (it/en/fr/es/ar).** Eight new content modules — `template_content_pragma_{en,fr,es,ar}.py` (846 / 880 / 852 / 848 LOC) and `template_content_elevate_{en,fr,es,ar}.py` (821 / 838 / 812 / 813 LOC) — each authored by a parallel sub-agent with a strict per-template per-locale voice contract. Pragma carries the **institutional B2B advisory voice** (FT/HBR/McKinsey-Quarterly EN, Les Echos vouvoiement FR with insecable spaces, Cinco Días/Expansión peninsular usted ES, MSA boardroom AR with Latin proper names + Western digits + dropped honorifics). Elevate carries the **SaaS / growth-tech founder-facing voice** (TechCrunch/Linear/Figma direct-`you` EN with contractions, Maddyness modern SaaS FR with `tu` and anglicismes, Xataka/K Fund peninsular `tú` ES with anglicismes, Wamda modern startup MSA AR with Latin product names + Latin acronyms). Voice contrast is deliberate and binding — D-054 differentiation is preserved across every locale (verified post-rollout: institutional markers in every Pragma locale, SaaS markers in every Elevate locale).

2. **9 D-047 leaks lifted from skin HTML.** Pragma corporate-suite (6 leaks): about-history narrative paragraph, services Durata/Lead-partner labels, case-study Practice/Anno/Durata/Lead/Lead-partner/Team-&-timeline labels (cross-page, lifted to `site.case_*_label`), case-study-list Practice/Timeline labels, contact office-grid Indirizzo/Zona/Telefono/Email labels. Elevate startup-saas-landing (3 leaks): pill-nav CTA fallback `{{ site.tag|default:"Inizia gratis" }}` → `{{ site.nav_cta }}` (the long-form tagline was being mis-used as a short CTA label, plus a hardcoded IT fallback); pricing CSS pseudo-element `content: 'Più scelto'` lifted to HTML `<span class="pop-badge">{{ page_data.highlight_badge }}</span>` rendered conditionally for highlight tier; contact office grid Sede/Trasporti/Modello labels.

3. **RTL CSS blocks added to both business archetypes' `_base.html`.** Each follows the Session 23/29/37 pattern: conditional Arabic font load (Amiri + Noto Kufi for Pragma's serif identity; Noto Naskh + Noto Kufi for Elevate's geometric SaaS identity); `html[dir="rtl"]` core block always-applied with font-stack swap, body 17px, letter-spacing flatten on chrome labels, button arrow flip `→` → `←`, eyebrow accent margin flip; `{% if is_rtl %}` page-level block with hero / head / footer grid flips, mockup `direction: rtl`, ship-log `direction: rtl`, pricing pop-badge repositioned, comparison/stack/office grids flipped, channel CTA arrow flipped. Latin wordmarks + Latin product names (Stripe, Linear, GrowthBook, Vercel) + Latin numerics (KPI values, version numbers, prices) explicitly retained in heading font with `unicode-bidi: isolate` so they read LTR within RTL flow. New `:focus-visible` rings on primary CTAs, ghost CTAs, nav links, language pills (sober accent outline, never browser-blue).

**Per-template per-locale acceptance:**

| Template | IT | EN | FR | ES | AR |
|---|---|---|---|---|---|
| pragma-corporate-suite | 867 (auth) | 846 LOC, 0 key diffs, FT/HBR institutional | 880 LOC, 0 key diffs, vouvoiement + insecable | 852 LOC, 0 key diffs, peninsular usted | 848 LOC, 0 key diffs, MSA boardroom + Latin digits |
| elevate-startup-landing | 836 (auth) | 821 LOC, 0 key diffs, SaaS direct-`you` | 838 LOC, 0 key diffs, modern SaaS + `tu` + insecable | 812 LOC, 0 key diffs, peninsular `tú` | 813 LOC, 0 key diffs, modern startup MSA + Latin product names |

**Option space considered and rejected:**

- **Option A — defer business i18n to Phase 3.** Rejected. The user explicitly demanded the 7/7 multilingual gate before any Phase 3 work resumes. Sessions 36/37/39 had already proved the recipe scales — pretending it didn't was a regression in honesty.
- **Option B — homogenize Pragma + Elevate voice to share locale trees.** Rejected. Pragma is institutional advisory, Elevate is SaaS growth-tech — D-054 differentiation requires they stay opposite in every locale. A shared tree would erase the brand contrast that makes the 10-gate D-054 test pass. Sub-agent voice contracts explicitly enforce the contrast.
- **Option C — sequential authoring by main session.** Rejected. ~6700 LOC of premium content × main author = many hours serial. 8 parallel sub-agents finished in ~4–8 min each; quality is auditable via shape diff (programmatic, 0 diffs across all 8 trees) + content-marker smoke + Playwright walk.
- **Option D — skip the RTL CSS and rely on Arabic content tree alone.** Rejected. Arabic content without `dir="rtl"` + RTL-aware skin CSS reads as broken. This is exactly the level of "fallback finto" the user explicitly forbade.

**Validation:**
- `python manage.py check` — 0 issues
- `smoke_full.py` — **282/282** routes HTTP 200 (was 226 → +56 new locale routes for pragma 6×4 + elevate 5×4)
- `smoke_forms.py` — **35/35** form routes HTTP 200 (was 27 → +8 new locale form routes)
- `smoke_i18n_media_hardening.py` — **45/45** hardening checks (pragma + elevate moved IT_ONLY → MULTILINGUAL)
- Regression: smoke_chiara_perfection 76/76 · smoke_pixel_perfection 80/80 · smoke_i18n_gusto 52/52 (zero degradation)
- Cross-tenant leak sweep: **0/40** D-047 leaks across 5 locales × 2 templates × 4 token classes
- D-054 differentiation: institutional markers (Practice/Pratique/Práctica/الممارسات + partner/associé/socio + CSRD) present in every Pragma non-IT locale; SaaS markers (MRR, Stripe, Linear, GrowthBook, Vercel) present in every Elevate non-IT locale
- Playwright walks: Pragma AR (Amiri body 17px, 5 pills, button arrow ←, hero "حيث تُتَّخذ القرارات التي تصنع الفرق."), Pragma AR contact form (10 fields fully Arabic), Pragma EN (FT-class CTA "Request a private call"), Elevate AR (Noto Naskh body, nav CTA "ابدأ مجاناً", pop-badge "الأكثر اختياراً" rendered from new HTML lift, v2.9 ship-log Latin Manrope), Elevate EN (TechCrunch hero "From waitlist to first MRR in fourteen days."), Cardio AR regression clean

**Catalog state after D-072:** **7/7 published_live templates ship in 5 locales** (cardio, dermatologia, gusto, chiara, pixel, **pragma**, **elevate**). Phase 2g3 multilingual coverage on the public catalog is closed. Phase 3 (auth/checkout/editor/projects/commerce) remains gated on Phase 2g3.7 (all 20 templates published_live) per D-049 + D-053 — 7/20 are now `published_live`, 13/20 still draft.

**Caveats (acceptable but documented):**
- Form placeholder names + phone country codes were localized per spec (e.g., Pragma ES uses "+34 ..." and "Ej. Alejandro" placeholders). Submission still goes nowhere (no backend action) — placeholder text choice, not a routing issue.
- Pragma's CONSOB license number (1148/2009) is preserved verbatim across locales; the wrapper text was localized ("CONSOB Independent Advisors registry no. 1148/2009" / "Inscription au registre CONSOB ..." / etc.) with the proper-noun "CONSOB" kept in Latin.
- Elevate's copy_kit Arabic locale correctly added "AR" to the kit's languages list (`IT + EN + FR + AR` instead of `IT + EN + FR`) — sub-agent caveat noted, deemed correct since the AR audience reads its own language list.
- Pricing format follows locale convention: "1.400 M €" ES with period thousand separator, "1,4 Md €" FR with comma decimal, "1,800" EN with US thousand separator, "1.4 B €" AR with Latin digits.
- Pragma RTL hero grid is `1fr 1.3fr` (image left, text right at 1.3fr) — opposite of LTR's `1.3fr 1fr` (text left at 1.3fr, image right). The 1.3fr text-column ratio is preserved on the reading-side column to match the IT visual weight.
- No new motion / forms / interactions / media infrastructure was introduced. Pure content + RTL CSS work.

**Branch:** `phase-business-i18n-completion-v1`. Not committed yet.

---

## D-070: Chiara Perfection Pass — Full 5-locale i18n + Editorial Imagery Replacement + Mobile Polish (2026-04-13, Session 37)

**Decision:** `chiara-portfolio-creativo` is brought to gold-standard product quality on a single template (no other live template touched in this session except smoke harness + cross-template chrome). Three concrete changes:

1. **5-locale rollout (it/en/fr/es/ar).** Four new content modules — `template_content_chiara_en.py` (951 LOC), `template_content_chiara_fr.py` (1003 LOC), `template_content_chiara_es.py` (964 LOC), `template_content_chiara_ar.py` (940 LOC) — each authored by a parallel sub-agent with native editorial-design voice per locale (Anglo-American Pentagram register · French classical étapes/Felix Pfäffli register with `vous` and `« »` · peninsular Spanish Visual/Mucho register with `usted` · formal MSA Arabic with cultural-publishing register). All proper names (Chiara Velluti, Triennale Milano, Adelphi, Querini Stampalia, Carlo Scarpa, Pentagram, Aiap, etc.) preserved verbatim across all locales — Latin script in AR. Italian address + phone + email + VAT preserved verbatim everywhere. Discipline taxonomy translated semantically per locale. All recently-added i18n labels (`ledger_full_link_label`, `ledger_count_prefix`/`unit`, `row_*_label`, `step_*`, `dossier_*_label`, `studio_*_label`, `capability_duration_label`) included in all 4 trees with exact structural parity to IT (verified: 0 missing keys, 0 extra keys per locale).

2. **Editorial-designer imagery replacement.** The 4 `featured_works` images and the founder portrait were generic laptop/coding/businessperson stock photos — the user's exact complaint about Chiara. Curated 5 new editorial-designer-coherent IDs through a sub-agent that downloaded each candidate via curl and inspected via Read tool: Triennale → tablet+display-letter+orange editorial mag (`photo-1611532736597-de2d4265fba3`); Adelphi → coordinated paperback book-spine stack (`photo-1497633762265-9d179a990aa6`); Querini → warm-lit Italian museum interior with vitrines + caption plaques (`photo-1564399579883-451a5d44ec08`); Velluti monograph → fountain-pen on handwritten manuscript (`photo-1455390582262-044cdead277a`); Founder → woman holding orange editorial grid-layout book in studio-neutral background (`photo-1544717305-2782549b5136`). Old laptop IDs scrubbed from the IT tree + propagated by script to all 4 locale trees so every locale ships the same imagery (5/5 swaps applied per locale, verified).

3. **Skin-HTML literal lift + mobile polish + RTL CSS + a11y focus.** Pre-session audit found 9 hardcoded Italian literal sites in the editorial-designer-grid skin HTML (home / project_list / project_detail / process / contact). All lifted to `page_data.*` content-registry fields so every label is locale-driven. New mobile breakpoints added: dark commissions band gutters collapse 56px → 20px, ed-press inline-styled grid heads forced to single-column with `min-width: 0` on grid items + h2 font-size override, ed-cta wrap collapses to 1fr at 720px, additional 480px breakpoint tightens hero h1 from 44px → 38px. Mobile horizontal overflow at 390px went from 124px (Session 36 baseline) to **−15px** (content fits with slack). New `html[dir="rtl"]` CSS block added to `editorial-designer-grid/_base.html` covering: Amiri body + Noto Kufi Arabic display font load (conditional on `is_rtl`), letter-spacing flatten on h1-h5 (Latin tracking is hostile to Arabic), eyebrow accent-rule flip, `.ed-btn-primary:after` arrow flip (`→` → `←`), .ed-ledger-full + .ed-dossier next arrows scaleX(-1), Latin wordmark font lock (Chiara Velluti Studio stays Latin in RTL), tabular-mono lock for Latin numeric runs (year/count/credits use JetBrains Mono in AR), page-level `.ed-hero` grid-template-columns swap + summary/deliverables `<li>` em-dash padding flip + client-code border-side flip + form consent border-side flip. Page-level flips guarded by `{% if is_rtl %}` so LTR loads zero RTL bytes. New `:focus-visible` rings on `.ed-btn-primary` + `.ed-btn-ghost` (2px accent outline + 4px offset, sober editorial-paper precision, never browser-blue).

**Per-locale acceptance:**

| Locale | Lines | Voice | Verified |
|---|---|---|---|
| IT (auth) | 970 | Italian editorial AD register | baseline |
| EN | 951 | Pentagram / Eye Magazine register | 0 key diffs · all routes 200 · "Forms that endure" rendered |
| FR | 1003 | étapes / Felix Pfäffli register · `vous` · `« »` · French ordinals (24ᵉ) | 0 key diffs · all routes 200 · "qui durent" rendered |
| ES | 964 | Visual / Mucho peninsular register · `usted` | 0 key diffs · all routes 200 · "que perduran" rendered |
| AR | 940 | Formal MSA cultural-publishing register · proper names Latin · Latin digits for technical data | 0 key diffs · all routes 200 · `dir="rtl"` + Amiri/Noto Kufi loaded · "أشكال" rendered |

**Option space considered and rejected:**

- **Option A — author 4 locale trees myself sequentially.** Rejected. ~3500 LOC of editorial content × 1 author would have run ~12h serial. Parallel sub-agents (one per locale) ran ~5–13 min each in parallel. Author quality is auditable via line-counts + structural parity check + browser walk + content-marker smoke; voice quality is auditable via spot-checks of signature phrases per locale.
- **Option B — defer locale rollout, just polish IT.** Rejected. The user explicitly said: "ogni template live deve arrivare a 5 lingue vere, non fallback finti." The template was demoting itself to "draft-quality" until it had the same locale depth as cardio/derm/gusto.
- **Option C — keep the laptop stock photos and just mute them with grayscale + opacity.** Rejected. The user explicitly flagged imagery quality as a blocker. Stylistic muting would still leave a designer's "Triennale catalog" represented by a person at a laptop — fundamentally off-brand.
- **Option D — commission paid stock photography via Pexels API or Adobe Stock.** Rejected. Same Unsplash/CC0 stack used elsewhere in the project; the curation methodology (download + Read inspection per candidate) is the audit substitute for paid licensing.
- **Option E — drop the featured_works visual grid entirely and let the typographic hero + ledger card carry the page.** Rejected. The lightbox grid is the home page's only photographic moment — removing it would push the page to "all-text" which contradicts D-068's premium-component-depth requirement and removes a legitimate editorial-grid identity element.

**Trade-off:**

- Caveats on 2 of 5 image picks (recorded in the curator's report): the Triennale image is a tablet showing display-type letter "A" plus an orange printed magazine — closer to "type ideation" than literal "art-book spread", but the only candidate the curator found that wasn't a laptop scene. The founder portrait is a smiling woman holding an editorial book — closer to "AD presenting work" than "AD-at-work-with-paste-ups" — but the only candidate that satisfied the no-laptop + no-phone + no-office + no-lifestyle constraint stack. Both flagged as acceptable but not gold; replacing them with bespoke Velluti-shoot photography is a future-tenant production task, not infrastructure.
- AR content tree contains some embedded Latin proper names (ALL of them, by D-070 rule) and Latin digits for technical data (years, page counts, paper weights). This is intentional — mixed-script editorial flow is part of the AR voice. The CSS `font-family` stack keeps Latin runs in JetBrains Mono / Latin fallback so they stay legible against Amiri body text.
- The 4 locale tree files add ~3850 LOC to `apps/catalog/`. This is content, not code complexity — it lives outside the views/services/selectors path. Future editor app (post Phase 2g3.7) will move this into a `TemplatePage` model, at which point these `.py` files become seed source for `seed_template_content.py`.
- Mobile polish required `!important` overrides on inline-styled `<div class="head" style="display:grid; ...">` blocks in `home.html`. Inline `style=` attributes have specificity 1,0,0,0 which beats normal class selectors. The cleaner refactor (move all inline-style grid heads to classed CSS) is deferred — the `!important` override is gated to `@media (max-width: 720px)` so it has zero impact on desktop.

**Consequence:**

- (a) Chiara becomes the **4th template** with full 5-locale coverage (after cardio · derm · gusto). Catalog state: 4/7 published_live with 5 locales, 3/7 IT-only (Pragma · Elevate · Pixel) — Pixel is the next natural target for Phase 2i.2c since it shares the portfolio category.
- (b) D-069 invariant ("switcher must match content") continues to bind. Chiara now correctly renders the 5-pill switcher because `template_content.get_available_locales("chiara-portfolio-creativo")` returns 5 codes; if a future session truncates Chiara's locale coverage, the switcher auto-shrinks.
- (c) New skin-HTML rule formalized: **every per-archetype skin under `templates/live_templates/<category>/<archetype>/`** must keep zero hardcoded Italian literals — labels go to `page_data.*` (single page) or `site.*` (cross-page chrome). The 9 lifted Chiara literals are the precedent. When Pixel ships its locale rollout, the same lift pattern applies (cinematic-photographer skin will need its own audit).
- (d) The editorial-designer-grid archetype is now **shared-hosting-ready** for a second portfolio template with zero new HTML — same recipe as specialist (Cardio + Derm) and fine-dining (Gusto). The chrome-authoring contract D-047 is preserved across the lift.
- (e) Mobile horizontal overflow on Chiara is **closed**. Pre-Session-37 baseline at 390px viewport: 124px overflow. Post-Session-37: -15px (fits with slack). The same inline-styled-grid pattern likely affects other published_live templates (Pragma + Elevate corporate sections) — flagged as a follow-up audit but out of Chiara's scope.
- (f) Founder portrait + featured_works images are now editorial-designer-coherent. The old laptop stock IDs are scrubbed from the IT tree AND the 4 new locale trees (5/5 swaps verified per locale via byte-level grep). Future image upgrades can land per-locale if a tenant wants region-specific portfolio shots.

**Non-negotiable quality floor:**

- Every chiara live route must render in 5 locales with structural parity (same `pages` slugs/kinds, same key shapes, locale-specific labels + content).
- No `<video>` element with placeholder source in any chiara page (D-069 still binding — chiara has no video block, never has, never will under the editorial-designer identity).
- No laptop/coding/businessperson stock photo in chiara imagery — editorial designer identity is print/type/paper/ink/signage/sketchbook/manuscript matter.
- Every CTA button has a `:focus-visible` ring (a11y minimum). Keyboard navigation must complete the full form flow without losing visible focus.
- Mobile horizontal overflow on chiara at 390px viewport: ≤ 0px (content always within viewport). This is now regression-tested by the Playwright walk, not just by the route smoke.
- Native voice per locale (no machine translation). Native typography conventions per locale (FR insecable spaces, ES `¿? ¡!` `« »`, AR `، ؛ ؟` and `« »`). Latin proper names everywhere — never transliterated to non-Latin scripts.

**Validation results (Session 37):**
- `python manage.py check`: 0 issues.
- `smoke_full.py`: **198/198 routes HTTP 200** (was 170 before Chiara × 4 new locale routes).
- `smoke_forms.py`: **27/27 form routes HTTP 200**.
- `smoke_i18n_media_hardening.py`: **45/45 hardening checks passed** (Chiara moved from IT_ONLY to MULTILINGUAL bucket — switcher must render).
- `smoke_chiara_perfection.py` (new, ~155 LOC): **76/76 checks passed** — covers (a) 5-locale signature-phrase render + active-pill render, (b) AR `dir="rtl"` + Amiri/Noto Kufi font load, (c) 4/5 new editorial image IDs present per locale + 0 old laptop IDs anywhere, (d) founder portrait swap × 5 locales, (e) IT-literal leak sweep on lifted labels × 4 non-IT × 5 pages = 20 leak checks, (f) 8 inner pages × 5 locales = 40 route checks.
- Playwright walk 1440×900 on IT/EN/FR/ES/AR home + AR project_detail + AR contact form: signature phrase rendered per locale, 5-pill switcher visible, AR has `dir="rtl"` + Latin wordmark stays Latin + Latin digits stay Latin in numeric meta + section grid flips. 4/4 featured project images visibly editorial (book-spine stack, museum interior, type-ideation tablet, fountain-pen-on-manuscript).
- Mobile sanity at 390×844: overflow `-15px` (fits with slack, no horizontal scrollbar).

---

## D-069: Live i18n & Media Coherence Hardening — Language switcher scoped to authored locales, placeholder videos removed, codec-theatre metadata stripped (2026-04-13, Session 36)

**Decision:** The motion/media/typography pass from Session 35 (D-068) introduced three `lm-video` blocks and a language switcher that both claimed more than the content delivered. This session narrows both to what is actually true for each of the 7 `tier=published_live` templates. No new primitives, no new categories, no new templates — a quality hardening pass on top of D-068.

**Per-template state after hardening:**

| Template | Locales authored | Switcher rendered | Video block | Marquee | Notes |
|---|---|---|---|---|---|
| Cardio (specialist) | 5 (it/en/fr/es/ar) | 5 pills | — | — | No media chrome; live-media.css/js unlinked (orphan) |
| Derm (specialist, shared) | 5 | 5 pills | — | — | Same skin folder as cardio — benefits for free |
| Gusto (fine-dining) | 5 | 5 pills | **REMOVED** (signature_video) | — | live-media.css/js + video tokens removed; atmosphere_teaser carries BTS mood |
| Pragma (corporate-suite) | 1 (it) | **HIDDEN** | — | sectors + trust_logos (real) | Marquee content is real institutional wordmarks — kept |
| Elevate (startup-saas-landing) | 1 (it) | **HIDDEN** | **CONVERTED** to demo invitation card | integrations (real SaaS tools) | Frame preserved, fake `<video>` + codec metadata removed, dual CTA to `/demo/` + `/prodotto/` |
| Chiara (editorial-designer-grid) | 1 (it) | **HIDDEN** | — | — | Featured_works lightbox grid kept; live-media.css/js + video tokens unlinked |
| Pixel (cinematic-photographer) | 1 (it) | **HIDDEN** | **REMOVED** (reel) | — | Filmstrip + EXIF strip already carry the cinematic identity; live-media.css/js + video tokens unlinked |

**Rationale for each removal / conversion:**

1. **Language switcher honesty.** The 4 IT-only templates rendered a 5-pill language switcher whose EN/FR/ES/AR entries silently fell back to Italian content via `pick_localized`. A premium marketplace advertising 5 locales that don't exist is a chrome that lies. `template_i18n.locale_switcher_entries()` is now template-aware — it accepts `available_locales` and returns an empty list when ≤1 locale is authored. The view (`LiveTemplateView.get_context_data`) calls `template_content.get_available_locales(slug)` and suppresses the switcher when there's only one locale. Every skin's switcher markup now sits inside `{% if locale_switcher %}`.

2. **Fake video asset retirement.** All 3 `lm-video` blocks (Gusto signature_video / Elevate product_video / Pixel reel) shared the same placeholder `src` — `commondatastorage.googleapis.com/.../ForBiggerBlazes.mp4`, a Big Buck Bunny sample MP4. Shipping a click-to-play that plays an animated bunny short is a demo artifact. D-068 acknowledged this in its trade-offs but kept the blocks for integration-demonstration purposes; Session 36 makes the call that integration-demonstration is a lower priority than catalog honesty. Two blocks removed outright (Gusto kitchen, Pixel reel) — the archetypes already carry their identity without video. One block converted (Elevate product_video → product_demo_card) — the frame is preserved as a premium dashboard-poster + dual-CTA invitation to `/demo/` (the existing form page) + `/prodotto/`. The placeholder asset URL now appears zero times in any rendered page body.

3. **Codec-theatre metadata stripped.** The three video blocks also carried pseudo-technical captions flagged in the user brief: `"Demo · 2:14 · 1080p"` (Elevate), `"Reel · 1080p · 24 fps"` + `"Play · 3:12"` (Pixel), `"Camere · Due fisse · 4K"` (Gusto). Per user directive these only belong where they reinforce identity, not as boilerplate — and all three cases were gratuitous. All gone with the blocks that hosted them.

4. **Orphan primitive links removed.** `live-media.css` + `live-media.js` are now linked only where a consumer exists: Pragma + Elevate base (marquee), plus no video anywhere. The specialist (cardio/derm), Chiara, Pixel, and fine-dining (Gusto) base files all unlink both. Orphan `--lm-video-*` / `--lm-marquee-*` tokens in their `:root` blocks removed. Orphan specificity-shielding selectors (e.g. `.lm-video .lm-video-play-label.cp-mono`) pruned.

5. **No new i18n content authored.** The 4 IT-only templates stay IT-only. The brief explicitly said "non è necessario forzare 5 lingue dove non esiste ancora la base completa". Extending Pragma / Elevate / Chiara / Pixel to 5 locales is a Phase 2i.2b ticket, not a hardening pass. The switcher suppression renders the current single-locale state coherently, and when a future session authors 4 new locale trees for a template, its switcher will automatically return to life (no further chrome work required — the `{% if locale_switcher %}` guards are already in place).

**Option space considered and rejected:**

- **Option A — show an IT-only "Italiano" pill on the 4 IT-only templates.** Rejected: a single pill with the currently-active language adds chrome noise without utility. Either the user can switch language or they can't; if they can't, hiding the switcher is the honest chrome.
- **Option B — keep the 5-pill switcher on the 4 IT-only templates but disable EN/FR/ES/AR pills (grayed out, cursor:not-allowed).** Rejected: gray pills advertise a feature that's coming, but their presence still invites a click that goes nowhere. A premium marketplace doesn't tease unimplemented features in the main chrome.
- **Option C — commission full EN/FR/ES/AR content trees for all 4 IT-only templates right now.** Rejected: out of scope for a hardening pass (each tree is ~1250 LOC of native-voice editorial content, budgeted ~3h per template per D-063; 4 × 3h = 12h of content authoring is a separate phase).
- **Option D — keep the placeholder Big Buck Bunny video with a clearer "demo-only" watermark.** Rejected: the user brief is explicit ("evita demo-looking artifacts" + "meglio nessun video che un video cheap o incoerente"). No watermarking makes a placeholder reel premium.
- **Option E — commission real brand video shoots now** (Gusto kitchen footage, Elevate product walkthrough screen recording, Pixel Carso reel). Rejected: content production is outside a platform hardening pass. When real assets exist, the `signature_video` / `product_video` / `reel` keys can be re-added with a production `src` and the blocks come back — the HTML/CSS infrastructure of the `lm-video` primitive stays in `live-media.css/js` as a latent capability.

**Trade-off:**

- The 3 live-template videos promised by D-068 go to zero. D-068's per-template contract row "YES — product demo block" / "YES — signature ambient block" / "YES — cinematic reel block" is superseded by D-069's "REMOVED / CONVERTED / REMOVED".
- Elevate's new demo_card is more useful than the old product_video: clicking the primary CTA lands the user on the existing `/demo/` form page, which collects qualified leads. The old video's play button led to a 30-second cartoon about animals. Net product value increases.
- The language switcher hiding means the 4 IT-only templates visually lose a chrome element that previously said "this template supports 5 locales". It now says (by absence) "this template is in Italian". For a premium marketplace this is the truthful message. When the next i18n rollout wave (Phase 2i.2b) brings Pragma / Elevate / Chiara / Pixel to 5 locales, the pills come back automatically.
- Orphan CSS+JS links removed reduce per-page payload ~20KB for 4 templates (cardio, derm, chiara, pixel). Free performance win.

**Consequence:**

- (a) D-068's counter + mono + typography work is preserved intact. D-069 does not touch any counter attribute, any `--mono` / `.sl-mono` / `.ed-mono` / `.cp-mono` utility, or any italic-axis h-em emphasis. D-068's Pragma + Elevate marquees stay (they use real institutional wordmarks and real SaaS integration names — already coherent).
- (b) **D-068's `lm-video` contract is NOT deprecated.** `live-media.css` + `live-media.js` remain available as a latent primitive. When a future template has a real signed MP4 and metadata that reinforces identity (not codec cues), it can re-introduce an `lm-video` block with zero infrastructure work.
- (c) D-059 (i18n pilot architecture) gains a new invariant: **the switcher must match the content**. A template whose `TEMPLATE_CONTENT[slug]` entry has only one locale key MUST NOT render a multi-pill switcher. `template_content.get_available_locales()` is now the source of truth; `LiveTemplateView` threads it through `ctx["available_locales"]` + `ctx["locale_switcher"]`. Every new skin authored from Phase 2g3 onwards must wrap its switcher markup in `{% if locale_switcher %}`.
- (d) Phase 2g3 rollout recipe gains an implicit step: when flipping a template to `published_live`, either (a) author all 5 locale trees (full Phase 2i.2 pass) OR (b) keep IT-only and ship with switcher auto-hidden. No middle ground — no template ships a 5-pill switcher backed by 1-locale content.
- (e) `EDITOR_SCHEMA_BLUEPRINT.md` should note: any future editor that lets a customer customize a template must only expose locale editing for locales the template registry declares. Hiding the switcher when coverage drops to 1 should happen automatically via the same `get_available_locales` check.
- (f) MEMORY.md preview-pipeline-gotchas gains a new gotcha: "adding a new content block (like signature_video) on the IT tree without mirroring it in the 4 locale trees creates content-depth disparity — the block disappears on EN/FR/ES/AR. Either author the block in all locales or scope it via a `{% if page_data.X %}` guard and document the IT-only intent."

**Non-negotiable quality floor:**

- The language switcher must match the content. Exact rule: `len(available_locales) > 1` is the only condition under which the switcher renders.
- No `<video>` element may ship with a placeholder `src` that points to animated-bunny / tech-demo / stock-studio assets. Either the source is a real brand asset or the block is not in the template.
- Video metadata (caption, meta rows, play-label) must describe the brand's reality. `4K`, `1080p`, `24 fps`, `H.264`, `Play 3:12`, and similar codec/technical cues are forbidden unless they are genuinely part of the template's identity (e.g. a cinematographer template whose clients filter by frame rate might legitimately show one).
- Every orphan CSS link + `<script>` tag removed as soon as its last consumer is deleted. No dead-weight primitives linked from skins that don't use them.
- D-047 chrome-authoring contract preserved: the `product_demo_card` content block flows through `page_data.*`; the skin reads `page_data.product_demo_card.primary_cta` / `primary_href` / `secondary_cta` / `secondary_href` / `caption` / `poster` — zero literal copy introduced in the skin HTML.

**Validation results (Session 36):**
- `python manage.py check`: 0 issues.
- `smoke_full.py`: **170/170 routes HTTP 200** (no regression vs Session 35 baseline).
- `smoke_forms.py`: **27/27 form routes HTTP 200** (no regression vs Session 33 baseline).
- `smoke_i18n_media_hardening.py` (new): **45/45 hardening checks passed** — 25 IT-only-no-switcher + 15 multilingual-switcher-present-with-5-pills + 7 forbidden-media-token scans + 3 specific block-presence/absence assertions (Elevate demo card renders, Pixel has no `.lm-video` / `.cp-reel`, Gusto has no `.lm-video` / `.fd-signature-video`).
- Playwright walk 1440×900: Elevate `/preview/` demo card renders cleanly (dashboard poster + dual CTA + editorial caption, no video tag, no switcher), Cardio FR 5-pill switcher intact, Gusto AR `dir=rtl` preserved, Pragma/Chiara/Pixel switcher absent end-to-end.

---

## D-068: Live Motion / Media / Typography Pass — Counter prefix + thousand-sep, lm-video + lm-logo-marquee primitives, per-skin mono accent (2026-04-13, Session 35)

**Decision:** The 7 `tier=published_live` templates receive a premium pass on three axes — motion (counters where credible), media (video + marquee + lightbox where genuinely coherent with the archetype), typography (per-template font character). New shared primitives (`static/css/live-media.css` + `static/js/live-media.js`) are introduced alongside live-motion + live-interactions + live-forms. The `animateCounter()` function in `live-motion.js` is extended to handle (a) leading non-digit prefix (`€ 1.4 B`, `+ 38%`), (b) Italian thousand-separator heuristic so `1.200` animates to 1200 (not 1.2). Backwards-compatible — every previously-working counter is unchanged.

**Per-template contract (BINDING for future skin work):**

| Template | Counters | Video | Marquee | Mono accent | Italic-axis h-em |
|---|---|---|---|---|---|
| Cardio (specialist) | preserved (3) | NO | NO | — | yes (wt 400) |
| Derm (shared specialist) | preserved (3) | NO (shared skin) | NO | — | yes (wt 400) |
| Gusto (fine-dining) | preserved (3) | **YES — signature ambient block** | NO | — | yes (wt 600) |
| Pragma (corporate-suite) | **YES — KPI × 4** | NO | **YES — sectors + trust** | — | yes (wt 600) |
| Elevate (startup-saas-landing) | **YES — × 9** (mockup 3 + metric 4 + founders 2) | **YES — product demo block** | **YES — integrations** | **JetBrains Mono** (.sl-mono) | — (gradient em preserved) |
| Chiara (editorial-designer-grid) | NO | NO | NO | **JetBrains Mono** (.ed-mono) | yes Syne (wt 700) |
| Pixel (cinematic-photographer) | NO | **YES — cinematic reel block** | NO | **JetBrains Mono** (.cp-mono) | — (uppercase preserved) |

**Video rationale (BINDING for future archetype reviews):** video appears only on the 3 archetypes where motion/cinema is part of the category vocabulary — fine-dining hospitality (Gusto), growth-tech SaaS (Elevate product demo CTA already said "Guarda la demo · 2 min"), photographer reel (Pixel — industry standard for cinematic photographers). Video does NOT appear on clinical specialist (cardio + derm — clinical authority is document-driven, not cinematic), corporate-suite institutional (Pragma — boardroom authority is document-driven), or editorial-designer (Chiara — typographic identity, the absence of imagery IS the identity). Adding video to those four would cheapen the archetype identity. The two new portfolio additions follow the same logic: Chiara gets a typographic-led featured-projects visual grid (no video, asymmetric grid, italic accent), Pixel gets a cinematic reel video block (yes video, EXIF strip, mono caption).

**lm-video contract:** `<figure class="lm-video" data-lm-media="video" data-lm-video-src="..." data-lm-video-poster="...">` with `<img class="lm-video-poster">` always rendered + `<button class="lm-video-play">` overlay. On first user click, JS creates `<video controls preload="metadata" playsinline>` + `<source>` + applies `is-playing` class which fades out poster + play button. **No autoplay, no iframes, no third-party tracking surface.** Esc-to-pause. If the video src 404s, the poster remains visible (silent failure). Per-skin tokens via 5 CSS custom properties: `--lm-video-radius`, `--lm-video-overlay`, `--lm-video-play-bg`, `--lm-video-play-fg`, `--lm-video-play-ring`.

**lm-logo-marquee contract:** `<div class="lm-logo-marquee" data-lm-media="logo-marquee">` with track that JS duplicates in place for seamless `-50%` keyframe loop. Hover-pauses. `prefers-reduced-motion: reduce` skips duplication and freezes the track (mask still fades edges so it reads as a wordmark strip rather than animated band). Per-skin tokens: `--lm-marquee-duration` (60s growth-tech up to 130s cinematic), `--lm-marquee-gap`, `--lm-marquee-color`, `--lm-marquee-rule`, `--lm-marquee-pad-y`.

**Counter prefix + Italian thousand-separator heuristic (`live-motion.js`):**
```js
// regex extended:
var match = original.match(/^(\D*?)(-?\d+(?:[.,]\d+)?)(.*)$/);
// prefix = match[1] (preserved verbatim)
// numeric = match[2]
// suffix = match[3] (preserved verbatim)

// Italian thousand-separator heuristic:
var thousandsMatch = /^(\d{1,3})\.(\d{3})$/.exec(rawNum);
if (thousandsMatch) {
  target = parseInt(thousandsMatch[1] + thousandsMatch[2], 10); // 1200 not 1.2
  isInt  = true;
  // formatValue() restores Italian thousand-sep on each frame via
  //   String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.')
}
```
This single change unlocks counters on Pragma's `€ 1.4 B`, Elevate's `+ 38%` and `↑ 22%`, and correctly handles cardio's existing `1.200 visite specialistiche / anno`. **Verified: every previously-working counter on cardio, derm, gusto continues to work identically.**

**Per-skin mono accent contract:** Three skins (Elevate, Chiara, Pixel) load JetBrains Mono via Google Fonts and expose a per-skin `--mono` CSS custom property + a single utility class (`.sl-mono`, `.ed-mono`, `.cp-mono`). The utility selectors are **specificity-shielded**: each utility's CSS rule lists the common per-skin chained selectors as additional alternates (e.g. `.sl-shiplog .row .ver.sl-mono` at specificity 0,0,4,0 to beat the existing `.sl-shiplog .list .ver` chain at 0,0,3,0). This avoids `!important` and keeps the cascade clean.

**Per-skin typography refinements (line-height, letter-spacing, font-feature-settings):**
- Cardio/Derm specialist: body 1.6→1.55, h1 letter-spacing -0.018em→-0.022em, italic h-em wt 400, font-feature-settings kern/liga/onum.
- Gusto fine-dining: italic h-em wt 600 (preserved 1.65 line-height for editorial reading rhythm), font-feature-settings kern/liga/onum/calt.
- Pragma corporate-suite: body 1.65→1.62, h1 letter-spacing -0.018em→-0.02em, italic h-em wt 600, font-feature-settings kern/liga/calt/onum.
- Elevate startup-saas: body 1.65→1.6, h1 letter-spacing -0.025em→-0.04em (tighter for tech), font-feature-settings kern/liga/calt/ss01, gradient em preserved.
- Chiara editorial-designer: body 1.65→1.55, h1 letter-spacing -0.025em→-0.035em (editorial precision), italic Syne wt 700, font-feature-settings kern/liga/ss01/calt.
- Pixel cinematic-photographer: h1 letter-spacing 0.005em→0.018em (loosened for cinematic measured rhythm), font-feature-settings kern/liga/ss01.
- Universal: tabular-nums + lining-nums on every metric/KPI/ledger numeric span so digits align column-wise during animation and at rest.

**Rationale:** The user brief flagged 5 concrete pain points: (a) "in alcuni nuovi template manca dinamismo, per esempio counters e motion sulle cifre" → wired counters on Pragma + Elevate (+ 9 founders) and verified cardio/derm/gusto preserved; (b) "vuole usare il più possibile JS in modo intelligente per dare movimento e stile" → +110 LOC of zero-dep IIFE for video lazy-boot + marquee duplication, no library, no bundle weight; (c) "non c'è ancora nessun template con una vera integrazione video 'normale'" → Gusto + Elevate + Pixel each get a real `<video controls preload="metadata" playsinline>` block with poster + per-skin token theming; (d) "vuole video e gallerie dove hanno davvero senso" → 3 video blocks placed on the 3 archetypes where they belong, NOT on the 4 where they would cheapen (cardio/derm/pragma/chiara explicitly excluded with documented reasoning); (e) "il font deve adattarsi fortemente al template" → 3 templates load JetBrains Mono as a third font, 4 templates get italic-axis h-em emphasis at differentiated weights, all 7 get tabular-nums on metric strips, and per-skin line-height + letter-spacing are now intentionally tuned per archetype (not a shared default).

**Option space considered and rejected:**
- **Option A — pull in a counter library** (CountUp.js, odometer.js, etc.): rejected. Bundle weight (15-30kB), dependency surface, doesn't solve the prefix/thousand-sep parsing we need for our specific Italian-vs-international format mix. Our 30-line extension to live-motion.js handles every case without a library.
- **Option B — embed YouTube/Vimeo iframes for video**: rejected explicitly per user brief ("non un embed brutto buttato dentro"). Iframes bring third-party tracking, cookie banners, branded chrome that breaks each skin's identity, and slower TTI. Native HTML5 with poster + click-to-play was the only approach that met the quality floor.
- **Option C — a CSS-only marquee with no JS**: rejected. To get a seamless `-50%` keyframe loop the track needs exactly two copies of the content. Either (a) authors duplicate the markup manually (annoying + bloats DOM) or (b) JS duplicates once at boot. Option (b) costs ~15 lines, lets authors write content once, and degrades fine without JS (track stays visible as a single static row under the mask).
- **Option D — autoplay-muted ambient hero loops on every template**: rejected. Autoplay is invasive on metered networks + accessibility-hostile + not consistent with the user's "no cheap embeds" instruction. The lm-video primitive supports `data-lm-video-autoplay="true" data-lm-video-muted="true"` for skins that genuinely want it, but no current template opts in.
- **Option E — counters everywhere on every metric-looking span**: rejected. Counters on cardio's "Studio Marani Cardiologia 15 anni di pratica clinica" feel credible. Counters on Chiara's "1 / 04 commission" feel cheap (typographic identity). Counters on Pixel's "Mamiya 7II ƒ8 1/250" feel wrong (it's not a metric, it's an EXIF spec). Per-template choice was made deliberately, not mechanically.

**Trade-off:**
- ~360 LOC of new static (CSS + JS for live-media.css/js) + ~30 LOC counter extension in live-motion.js. Paid once; amortized across the 7 current live skins + every future live skin.
- 3 video blocks ship with a CC-licensed Big Buck Bunny placeholder src (animated film, off-brand content) so the lm-video integration demonstrates end-to-end. Each block annotated with a `NOTE` comment in its content registry. Production templates fill in the real brand URL — the poster + caption typography carry brand identity uninterrupted.
- 3 skins now load JetBrains Mono as a third Google Font (Elevate, Chiara, Pixel — Pixel was already loading it). `font-display: swap` on the link prevents FOUT/FOIT issues. Bundle weight increase is ~12kB per template (typical Google Mono subset). Acceptable given the differentiation gain.
- The integrations marquee on Elevate is **additive** — the existing static integrations grid stays. The marquee sits below the grid as a 12-logo drift band. This was deliberate: removing the static grid would lose discoverability (each integration has a desc); the marquee adds rhythm without removing information.

**Consequence:**
- (a) `live-media.css` + `live-media.js` are now the binding shared primitives for video + marquee on every future `tier=published_live` skin. The contract is documented in the file headers.
- (b) The counter prefix + thousand-sep extension to `live-motion.js` is the canonical counter parser. Future templates can drop `data-lm="counter"` on any numeric span without worrying about prefix/suffix/Italian formatting.
- (c) Per-skin mono accent (3 skins) is the precedent for any future skin that wants a third font — declare `--mono` token + utility class with specificity-shielded selectors. `EDITOR_SCHEMA_BLUEPRINT.md` should grow a `font_mono` field in the per-skin design tokens scope (D-064 follow-up).
- (d) D-058 motion language is extended in scope (counter prefix + thousand-sep) without breaking changes. D-061 medical motion exclusion (no counters) is **softened** since cardio's facts strip already had 3 counters from before and this session preserves them — clarification: "no counters" applies to spectacular-feel counters (CountUp animations on splash screens), not to small clinical credibility numerics. Documented here.
- (e) D-053 acceptance checklist gains an implicit gate 12: any new `published_live` skin SHOULD declare per-skin video + marquee tokens in `_base.html :root` even if it doesn't render those primitives, so future content updates can opt in without touching CSS. Adding as a soft gate (not blocking like gate 11 forms tokens).
- (f) Phase 2g3 rollout for the next 13 draft templates gets a richer recipe: every category template can opt into counters where credible, choose its video stance (yes / no) per archetype, and pick a per-skin font character without needing new infrastructure.

**Non-negotiable quality floor:**
- Video is poster-first. The poster is always visible. Click-to-play is the only path to native HTML5. No autoplay invasive. No iframes. No third-party tracking.
- Counters parse prefix + suffix + Italian thousand-separator. They never produce nonsense intermediate values.
- Marquees pause on hover (CSS-only). Reduced-motion users see a static track with edge mask, not an animation.
- Mono accent fonts ship with `font-display: swap`. Latin glyphs stay Latin (no Arabic substitution on chef names / publication titles in RTL — same precedent as D-063).
- Italic-axis emphasis only on h-em, never on body em (which keeps its accent-color treatment from the chrome-authoring contract).
- D-047 chrome-authoring contract preserved: every new content key flows through `page_data.*`. Zero literal brand strings introduced into shared HTML.

**Validation results (Session 35):**
- `python manage.py check`: 0 issues.
- `smoke_full.py`: **170/170 routes HTTP 200** (no regression vs Session 34 baseline 170).
- `smoke_forms.py`: **27/27 form routes HTTP 200** (no regression vs Session 33 baseline 27).
- Browser walk Playwright 1440×900: 7 templates × 1-2 pages each verified — counters animate to final values (Pragma 22 / 180+ / € 1.4 B / 94%; Cardio 15 / 1.200 / 4 with thousand-sep correctly preserved; Elevate 9 counter elements all reach final), 3 video blocks render with poster + play orb + per-skin caption font, 3 marquees JS-duplicate and scroll, mono utility computed font is `"JetBrains Mono", ui-monospace, ...` on all 3 mono-using skins, italic h-em accent active at the documented per-skin weight on all 4 templates that use it.
- AR/RTL regression on cardio: `dir=rtl`, `lang=ar`, body font `"Noto Kufi Arabic", Inter, system-ui, sans-serif` — i18n unchanged.

---

## D-067: Portfolio Live Rollout — Phase 2g3.4 Closes With Chiara + Pixel Promoted Under D-053 / D-054 / D-047, Two New Page Kinds (project_detail / series_detail) Established (2026-04-13, Session 34)

**Decision:** Phase 2g3.4 closes by promoting the two portfolio templates to `published_live`. `chiara-portfolio-creativo` (editorial-designer-grid archetype) and `pixel-portfolio-fotografico` (cinematic-photographer archetype) ship full multi-page live previews with 5 page kinds each plus one detail kind: Chiara serves `home / studio / lavoro / processo / contatti` plus `project_detail` for the 3 dossiers under `/lavoro/<slug>/`; Pixel serves `home / serie / biografia / pubblicazioni / contatti` plus `series_detail` for the 3 series under `/serie/<slug>/`. Two new content registries (`apps/catalog/template_content_chiara.py` + `template_content_pixel.py`) registered in `TEMPLATE_CONTENT`. Two new skin folders (`templates/live_templates/portfolio/editorial-designer-grid/` + `templates/live_templates/portfolio/cinematic-photographer/`) authored under D-047 from line one. `mp_other_portfolio` chrome key added to all 5 locales of `CHROME_I18N` (forward-compat). `LiveTemplateView` and URL patterns required ZERO changes — the dispatcher's `_list` → `_detail` kind transformation generalizes naturally to the new `project_list / project_detail` and `series_list / series_detail` kinds.

**Differentiation gate (D-054 · 10/10 dimensions disjoint, recorded for reviewers):**

1. **Hero image direction** — Chiara has NO big hero photo (the hero IS the typography: huge Syne display headline + numbered project ledger card on the right) vs Pixel's fullbleed dominant cinematic photograph covering 78vh of the viewport.
2. **First-2 imagery** — Chiara uses studio work-in-progress macro shots (sketchbooks, paste-ups) from the `portfolio-designer` pool, integrated only as project-detail imagery, never as hero. Pixel uses the dominant hero + 4 filmstrip stills from the `portfolio-photographer` pool. Zero URL overlap between the two pools.
3. **Silhouette** — Chiara: hairline-rule sticky nav (78px, index-letter labels, status pill right) + 2-column typo hero (1.18fr/1fr). Pixel: floating dark sticky nav (64px, transparent backdrop blur, monospaced shutter mark, status pulse + bracket CTA right) + fullbleed cover hero with corner frame marks.
4. **Section order** — Chiara home: typo-hero → project-ledger card → capabilities 4-col → clients ribbon → press cards 3-col → commissions dark band → final cta. Pixel home: fullbleed hero → 4-cell EXIF strip → 4-frame filmstrip → about-excerpt dark band → 3-cell publications grid → final cta.
5. **Primary CTA phrase + pattern** — Chiara: "Richiedi il portfolio completo" with ghost-rule sans button (uppercase + thin underline + arrow that translates on hover). Pixel: "Apri la serie completa" with bracket-mono pattern (`[ ... ]` brackets in JetBrains Mono, accent ring on hover).
6. **Block rhythm / density** — Chiara: very-airy editorial chapters with 96px paddings, 56px col gaps, generous whitespace. Pixel: compact image-dense with 64px paddings, 24px gaps, image cards everywhere.
7. **Macro tone** — Chiara: cream paper #f3efe5 + ink #15130f + accent rule. Pixel: near-black #050505 + warm grey #e9e7e2 + accent pulse (red-glow dot in nav).
8. **Imagery direction** — Chiara: studio work-in-progress (founder portrait + sketches in dossier galleries — design-led artifacts). Pixel: cinematic photostill (low-key reportage hero + asymmetric 6-image gallery in series_detail — observational mood).
9. **Font pairing** — Chiara: Syne (variable display geometric sans) + Inter (body). Pixel: Archivo (geometric sans) + Inter (body) + JetBrains Mono (EXIF/bracket monospaced — exclusive to Pixel, never imported in Chiara skin).
10. **Inner-page contract** — Chiara has `process` (5-step indexed sequence + 5 capability cards with scope+duration) + `project_detail` (dossier with breadcrumb + meta strip + client code + serif-italic lead + summary box + essay sections + dark deliverables band + colophon credits + next-link). Pixel has `publications` (8 magazine cards + 6-row exhibitions ledger + 6 awards) + `series_detail` (cover hero + EXIF 4-cell strip + meta strip + essay + asymmetric 6-image gallery + per-series print-meta dark band + next-link). The two detail kinds are semantically and visually different: a designer's project dossier vs a photographer's series page.

**D-047 chrome-authoring contract preserved.** Initial leak sweep on the cinematic-photographer skin found 2 latent leaks (`_base.html:393-396` kit footer rows, `series_detail.html:304` print edition cells) — both lifted to the content registry within the same session by adding `site.kit_footer_rows` (3-item per-tenant list) and `post.print_meta` (4-pair per-series list). Re-sweep returned ZERO matches across both portfolio skin folders against a 16-token leak list (Chiara/Velluti/Tortona/Triennale/Adelphi/Querini/Lambrate/Pordenone/Lorenzo Bianchi/Pixel/Tadino/Trieste/Sozzani/Mamiya/Foam/Magnum). The portfolio skin folders are now safe to host a future second sibling (e.g. an editorial type-house using editorial-designer-grid, or a fashion photographer using cinematic-photographer) without re-authoring HTML.

**Rationale:** Phase 2g3.4 is the natural next step after Session 32's Business rollout (D-065). The two portfolio templates were the single most "ready" pair in the catalog after Phases 2g2x.1/2g2x.8/D-051/D-052 closed: DNA + preview composition + imagery pool + hero overflow triage all complete since Session 19. The only remaining gate was content registry + skin folder authoring, which Session 32's Pragma+Elevate work proved is a one-session lift when DNA is solid. Choosing portfolio over restaurant or medical (the other in-progress categories) was deliberate: portfolio has the strongest design contrast between siblings (typographic vs cinematic — opposites of the visual axis), so a successful rollout proves the per-archetype skin contract scales beyond the visually-close medical specialist twins (cardio + derm) and the hospitality fine-dining single (gusto). It also moves the catalog from 2 hot categories (business + medical) to 3 (business + medical + portfolio), strengthening the homepage featured pool from 5 to 7 cards and enabling the featured grid to show genuine diversity of disciplines (corporate / pediatric / typographic / cinematic / fine-dining) instead of the previous 5-card concentration.

The two new page kinds (`project_detail` and `series_detail`) generalize cleanly through the existing `LiveTemplateView` dispatcher logic (`page_kind.replace("_list", "_detail")`) — no view code change. This proves the dispatcher is general-purpose and Phase 2g3.5 (ecommerce: bottega + luxe with `product_list` / `product_detail`) and Phase 2g3.6 (real-estate with `property_list` / `property_detail`) can use the same pattern without further plumbing. The `_list` / `_detail` kind suffix convention is now the de-facto contract for any template that wants a sub-route hierarchy.

**Image dependency strategy:** Pixel's `home` and `series_detail` cover photos use direct Unsplash CDN URLs in the content registry rather than going through the curated stock imagery library used by `generate_previews`. This is intentional: the live preview renders against the live Unsplash CDN at request time (not against locally-cached PNGs the way preview compositions do), and the 12 Unsplash URLs in the Pixel registry have been hand-verified to exist + match the cinematic mood (low-key port at dawn, masseria stones, river portraits, Trieste atmosphere). If any URL ever goes 404, the live preview shows the page background (#050505 dark) under the gradient overlay — still legible (the typographic credit bar above stays readable). This is consistent with the "cinematic graceful degradation" pattern from the preview composition (Session 18). Chiara's content registry deliberately includes only ONE Unsplash URL (the founder portrait on `/studio`); the rest of Chiara is photo-independent because the editorial-designer-grid archetype is built to read as a designer studio without imagery.

**Trade-off:** ~5300 LOC of new code (1600 content + 3700 skin) for two templates is roughly proportional to the Pragma+Elevate authoring cost (~1200 + 4500 = 5700 LOC for two business templates — Session 32). No regression on the 5 previously-live templates (smoke confirmed 149 → 170 routes all 200, the +21 routes are all new portfolio routes). The contact form on Chiara and Pixel uses the `.lf-*` primitives layer (D-066) directly with custom per-skin token overrides — Chiara: editorial paper + ink focus + 0 radius + ink submit; Pixel: cinematic dark + accent ring + 0 radius + transparent submit-on-dark. Both forms are sectioned (4 sections each) with file upload on the optional 4th section. The Pixel skin imports JetBrains Mono via Google Fonts — third typography family beyond the DNA-declared Archivo + Inter. This is a deliberate exception: the cinematic-photographer archetype's identity depends on the EXIF/bracket monospaced typography (it's listed in the DNA `dna_notes` as "monospaced EXIF credit bar pinned to its bottom edge"), and neither Archivo nor Inter has a true monospaced cut. JetBrains Mono is a free open-source font with no licensing concerns. Documented here so future archetype reviews don't flag it as a third-font violation.

**Consequence:** (a) Phase 2g3.4 closes; (b) the catalog floor moves from 5/20 to **7/20 published_live**, with portfolio joining business as a 100%-live category; (c) the homepage featured pool now shows 7 templates (was 5), enabling D-057's featured-pool backfill to never collapse the homepage to <3 cards even if `featured=True` filtering tightens further; (d) the two new page kinds (`project_detail`, `series_detail`) and the `_list`/`_detail` suffix convention are now the documented contract for any future template that wants sub-route hierarchies — Phase 2g3.5 (ecommerce) should use `product_list`/`product_detail`, Phase 2g3.6 (real-estate) should use `property_list`/`property_detail`, agency could use `case_study_list`/`case_study_detail` (already proven in Pragma); (e) the editorial-designer-grid skin is now a candidate to host a future type-house or graphic-design-school template (D-047 lift confirms the per-tenant ledger + clients ribbon + capabilities are all content-driven); (f) the cinematic-photographer skin is now a candidate to host a future fashion or commercial photographer template (the `kit_footer_rows` and `print_meta` lifts confirm even the technical-equipment cells generalize); (g) Phase 2g3.5 (ecommerce: bottega + luxe — both with D-047 leak-lift blockers per Phase 2g2x.3 still pending) is the next category in line if 2g2x.3 leaks are lifted first; otherwise the next step is restaurant 2g3.1 (sapore + brace, also blocked by Phase 2g2x.3 leak lifts on `trattoria-warm.html` + `street-modern.html`); (h) the `mp_other_portfolio` chrome key is now in `CHROME_I18N` for all 5 locales — when portfolio i18n is taken up later (Phase 2i.4 or similar) the marketplace bar chrome is already in place; (i) `EDITOR_SCHEMA_BLUEPRINT.md` should grow `project_detail` and `series_detail` schema entries in a follow-up doc pass — both fit the existing per-page-kind contract from D-064 (editable list of dossiers, each with title/discipline/year/duration/sections/credits/print_meta or summary/deliverables/credits).

## D-066: Premium Forms System — Reusable `.lf-*` Primitives + Per-Skin Tokens + Custom Accessible Listbox + Contextual File Upload (2026-04-13, Session 33)

**Decision:** The forms on the 5 `tier=published_live` templates are rebuilt on top of a shared premium primitives layer (`static/css/live-forms.css` + `static/js/live-forms.js`) that every live-template skin opts into via a small token override block in its `_base.html :root`. The system ships: accessible custom listbox (ARIA combobox + listbox, full keyboard), native-file-input-backed upload with drag + chip + individual remove, custom consent checkbox with SVG check, section-grouped markup, reassurance submit bar, per-skin tone via ~20 CSS custom properties. Native `<select>` / `<input type="checkbox">` / `<input type="file">` remain underneath every enhanced control — form submission and server-side semantics unchanged. The contract is enforced for all future `tier=published_live` skins.

**The 4 skin tones (per-archetype token overrides):**
- Specialist (clinical · paper + gold): transparent bg, 0 radius, minimal underline, red-gold accent, paper listbox, primary-dark submit with gold underbar. Dark-band override (`.sp-form-band .lf-*`) for the appointment page's navy band flips every token to on-dark values.
- Fine-dining (hospitality · dark body + gold): transparent on dark, 14px pad-y, secondary-gold focus, dark warm listbox, gold flat submit with bg-dark arrow.
- Corporate-suite (institutional · paper-3 boxed): 1px border, boxed inputs (`--lf-pad-x: 16px`), emerald focus ring, paper-3 listbox, primary-navy submit with accent arrow.
- Startup-saas (growth-tech · glass cosmic + cyan glow): `rgba(0,0,0,0.32)` bg, 10px radius, cyan focus ring with glow, dark cosmic listbox, pill-radius accent-cyan submit.

**Contract invariants (all 4 skins):**
1. Every `<select>` lives inside `.lf-select` (JS upgrades to combobox+listbox on desktop, native on touch). Native `<select>` remains the form source of truth.
2. Every form control uses `.lf-control` (or is a child of `.lf-select` / `.lf-upload`). Custom focus ring via `--lf-ring` token.
3. Labels use `.lf-label`; required fields carry no mark, optional fields show a muted `<span class="lf-opt">` with the `chrome.form_optional` label. Per-field helper below control as `.lf-helper` (p).
4. Consent uses custom `.lf-check` with SVG check animation — no native checkbox.
5. File upload (where justified by page copy) uses `.lf-upload` with drop zone + meta + chip list + per-chip remove.
6. Submit bar uses `.lf-submit-bar` with primary `.lf-submit-primary` (arrow glyph that shifts +4px on hover and flips `scaleX(-1)` in RTL), reassurance `.lf-submit-note` (with clock icon), optional `.lf-submit-secondary` link.
7. Section grouping via `page_data.form_sections` list (each section: `{num, title, meta, fields: [name…]}`). Special sentinel `"__upload__"` picks up `page_data.upload_field`. Templates fall back to flat `form_fields` loop when `form_sections` missing (non-IT locales today).
8. Progressive enhancement: every control renders fine without JS (native `<select>` styled with custom caret, upload label opens native picker, checkbox is still clickable). `prefers-reduced-motion: reduce` zeroes all transitions.
9. RTL: `margin-inline-*` + `.lf-select-caret` on trailing edge + submit arrow `scaleX(-1)` swap.

**Chrome i18n extension:** 6 new keys × 5 locales in `CHROME_I18N` (`form_required`, `form_optional`, `form_select_placeholder`, `form_upload_browse_prefix`, `form_upload_browse_link`, `form_upload_remove`). 30 new translation entries total.

**File upload placement (contextual, not sprinkled):**
- Cardio + Dermatologia appointment: yes — "referti o esami recenti", aligned with the page's own copy "Allega gli esami recenti se vuoi" (intro).
- Pragma contact: yes — "company profile, one-pager di governance o NDA standard", aligned with "NDA reciproca" language and the institutional mandate flow.
- Elevate demo: yes — "deck, screenshot o Loom", aligned with the product-led demo flow.
- Gusto reservations: no — hospitality context doesn't want file uploads for dinner bookings.
- Medical contact pages: no — non-urgent admin questions don't need attachments.

**Rationale:** The user's brief flagged three concrete pain points: selects looked non-premium (native grey/blue), forms felt unstructured for 8–9 field pages, no attachment affordance where copy clearly implied one. The option space:

- Option A — CSS-only re-skin, keep native `<select>`: cheapest, but browsers vary and the dropdown panel stays un-themed. Rejected — can't reach the premium bar on the dropdown panel itself without replacing the control.
- Option B — Pull in a select library (Choices.js, SlimSelect, TomSelect): theoretically quick, but brings 30–100kB of deps, pagination/multi-select features we don't need, and a harder-to-theme-per-skin surface. Rejected — scope creep, bundle weight, and we'd still need to style 4 distinct skins on top of the library's CSS.
- Option C — Chosen: author a tiny zero-dep ARIA combobox (~260 lines of JS, ~490 lines of CSS) matched to our exact token shape. Pays once, reuses across 4 skins, no bundle cost, no upgrade treadmill.

The per-skin token approach (rather than scoped `.specialist-form .lf-*` selectors) keeps the CSS flat and composition-friendly for future skins (Phase 2g3.4+ portfolio/ecommerce/agency/lawyer/real-estate). A new skin declares ~20 `--lf-*` values in its `:root` and inherits the full primitive library.

**Trade-off:**
- ~750 lines of new static (CSS + JS). Paid once; amortized across the 5 current live skins + every future live skin.
- Sectioned form markup + per-field helper means the content registry carries more per-form data. Acceptable: matches the D-057 editor-blueprint direction (field-level metadata becomes the foundation for the future customer editor).
- `form_sections` / `upload_field` / `form_submit_note` / per-field `helper` / `form_consent` are added in IT for all 5 templates and translated for EN/FR/ES/AR ONLY for `form_submit_note` this session. Sections/upload/helper translations are flagged as follow-up — templates fall back gracefully (functional form with premium visuals, just missing the IT-specific enhancement copy). This is a deliberate scope choice: quality parity for existing chrome strings is preserved; adding native-voice translations for 4 locales × 3 multilingual templates × (sections + upload + helpers) in one session would either ship machine-translated copy (forbidden by D-059/D-063) or blow scope. Phase 2i.3 candidate.
- Native `<select>` still submits — but on touch devices (which we detect via `(hover: none) and (pointer: coarse)`) we deliberately keep the native picker because platform UX is superior. This means touch and desktop expose different visual controls. Trade-off accepted: both are premium in their own idiom.

**Consequence:**
- (a) The `.lf-*` primitive library becomes the contract for every future `tier=published_live` template's form authoring. New skins declare tokens, inherit everything else.
- (b) The custom listbox / upload / check / section primitives are now part of the live-template runtime, alongside motion (D-058/D-061) and interactions (D-062/D-064). Authoring cost for new forms drops significantly.
- (c) The `--lf-section-title-color` token (introduced mid-session when dark-on-dark legibility surfaced on fine-dining + startup-saas) formalizes that section title color is per-skin, not per-primitive.
- (d) The 5 form pages are visibly more premium: custom listbox, section grouping on the 4 heavier forms, helper text under every field in IT, reassurance next to the submit CTA, sensible file upload on 3 pages.
- (e) Follow-up work captured: (i) i18n copy parity for the IT-only enhancement fields, (ii) pre-existing specialist legacy mobile chrome (nav grid + footer 4-col) flagged as a candidate mobile polish pass.
- (f) The D-053 acceptance checklist (10 gates) gains an implicit gate 11: any new `published_live` skin MUST author its `--lf-*` tokens in `_base.html :root`. Adding this as an explicit gate in the Phase 2g3.4+ rollout recipe.

**Non-negotiable quality floor:**
- Form submissions remain driven by native controls — no JS-only UIs that break without JS.
- Every listbox must pass full keyboard access (↑↓ Home End Enter Space Esc typeahead).
- Every control must have `:focus-visible` ring + 3px outline via `--lf-ring`.
- Every form page must collapse to 1-column at ≤880px.
- Every form must carry a reassurance `.lf-submit-note` adjacent to the primary CTA.
- File upload added only where page copy references attachments (intro explicitly mentions them). Never decorative.

**Validation results (Session 33):**
- `python manage.py check`: 0 issues.
- Form-specific smoke: 27/27 routes HTTP 200 with all `.lf-*` primitives + `live-forms.css` + `live-forms.js` linked + `.lf-select` present on every select-bearing form.
- Full regression: 149/149 routes across detail + home + inner pages × 5 templates × locales + marketplace surfaces.
- Browser walk 1440×900: 4 skins × 1–2 form pages each = 9 form renderings verified (sections, enhanced selects, upload drop zone, consent checkbox, submit bar with note, secondary alternative link).
- RTL cardio AR: labels + placeholders + submit-note + arrow all correct.
- Mobile 390×844: form grids collapse to 1-column; pre-existing specialist chrome overflow documented as scope-out.

---

## D-065: Business Live Rollout — Phase 2g3.3 Closes With Pragma + Elevate Promoted Under D-053 / D-054 / D-047 (2026-04-13, Session 32)

**Decision:** Both business templates (`pragma-corporate-suite`, `elevate-startup-landing`) flip from `tier=draft` to `tier=published_live` after a single-session rollout that delivers (a) full per-template content registry blocks in dedicated files (`apps/catalog/template_content_pragma.py`, `apps/catalog/template_content_elevate.py`), (b) two complete per-archetype skin folders under `templates/live_templates/business/<archetype>/`, (c) full D-047 chrome contract from line one with one new chrome key (`mp_other_business`) added in all 5 locales for forward-compatibility, and (d) tier sync via the existing `sync_template_tiers` command. Pragma ships 6 routes (home/chi-siamo/competenze/case-studies + 3 case-study posts/contatti) and Elevate ships 5 routes (home/prodotto/prezzi/demo/contatti). Both are IT-only at promotion — the locale-keyed shape is in place but the EN/FR/ES/AR trees are deferred to a future Phase 2i pass that will follow the cardio/derm/gusto recipe (D-059, D-063).

**Rationale:** Phase 2g3.3 was the smallest possible rollout step — only 2 templates, both with D-050 DNA + preview compositions already authored in Session 17 — but it had to prove that the recipe established for the medical pilot (Sessions 11/14, D-046/D-047) and the restaurant pilot (Sessions 9/22) generalises beyond categories with archetype-reuse. Business is the first category where neither sibling reuses a previously-built skin folder; both archetypes (corporate-suite + startup-saas-landing) are written from scratch under the same chrome contract. The fact that this required **zero changes to `views.py` / `urls.py` / `selectors.py`** confirms that the architecture has reached a steady-state for the remaining 5 category rollouts (2g3.4 portfolio, 2g3.5 ecommerce, 2g3.6 agency/lawyer/real-estate). The choice to extract per-template content into dedicated files (rather than inline in `template_content.py`) was made because `template_content.py` had reached 2321 lines after Session 30 and adding ~1200 more lines for two business templates would have crossed a readability threshold — extracting to per-template files (one of which already exists as a pattern for the i18n trees in `template_content_<slug>_i18n.py`) keeps each file under 700 lines and review-friendly, with the top-level `TEMPLATE_CONTENT` registry in `template_content.py` acting purely as a thin importer/router. Future templates with substantial IT-only content (e.g. ecommerce, portfolio) should follow this extracted pattern.

**Trade-off:** Two new files in `apps/catalog/`. One new chrome key × 5 locales (10 lines added to `template_i18n.py`). Two new skin folders (~13 HTML files total: 2 base + 11 page templates). One JSON registry update (`tier`, `live_pages`, `locales`, `tier_reason` fields per template). One sync command run (`seed_templates` auto-runs `sync_template_tiers`). Footer chrome headings (`foot_studio`, `foot_pages`, `foot_contact`, `foot_offices`) live on `site.*` per template rather than `chrome.*` — this is a small departure from the medical specialist pattern (which puts `foot_*` on chrome) and reflects that the corporate-suite "studio" and the startup-saas-landing "studio" are semantically incompatible (an advisory firm vs a SaaS product). The medical/restaurant templates can keep their chrome-level `foot_*` keys as-is — the per-archetype escape hatch only kicks in when a category genuinely needs different vocabulary per archetype.

**Consequence:** (a) Phase 2g3.3 is closed in TODO_NEXT.md; (b) catalog now shows 5 of 20 templates `published_live` (medical 2 + restaurant 1 + business 2), category counts auto-updated via `selectors._published_filter`; (c) `CATEGORY_ROADMAP.md` business row marked as "DNA + skin folder + content all complete (Session 32)"; (d) `TEMPLATE_REGISTRY.json` tier_reason updated to record the Session 32 close; (e) the next gate is Phase 2g3.4 (Portfolio: Chiara editorial-designer-grid + Pixel cinematic-photographer) using the same recipe; (f) D-053 `mp_other_business` chrome key is now in `CHROME_I18N` for all 5 locales — when business i18n is later authored, the chrome-bar widget renders correctly without needing a follow-up i18n PR; (g) the per-template footer headings precedent (`site.foot_*` instead of `chrome.foot_*`) is documented here for the next archetype that has incompatible categorical vocabulary; (h) D-053 acceptance checklist verified: DNA ✓ · Content registry ✓ · Skin folder ✓ · Routes 200 (54/54) ✓ · D-047 leak sweep clean ✓ · Visual walk passed via rendered HTML inspection ✓ · Differentiation 10/10 vs sibling ✓ · Preview PNG regenerated ✓ · Tier flipped + synced ✓ · Motion adopted (live-motion.css linked, `data-lm` reveal/stagger across all home sections) ✓.

## D-064: Premium Component Depth & Editor Schema Blueprint — Differentiated enrichment of the 3 published_live + concrete future-editor contract (2026-04-13, Session 30)

**Decision:** The 3 `tier=published_live` templates (cardio, dermatologia-elite-roma, gusto-fine-dining) receive a targeted premium-component enrichment pass where **each template gets a distinct set of new sections** chosen to fit its archetype tone, not a shared shopping list. A concrete Editor Schema Blueprint (`EDITOR_SCHEMA_BLUEPRINT.md`, ~600 lines, in repo root) is authored in the same session to define — without implementation — what the future customer editor will let buyers personalize, which fields are edit-gated by DNA, and which invariants (D-047, D-053, D-054, D-057, D-058, D-059) the editor must uphold.

**Per-template new sections (all with distinct interaction patterns to preserve D-054 differentiation):**

| Template | New sections | New interactions |
|----------|-------------|-----------------|
| Cardio (specialist clinical) | anchor subnav + "Percorso paziente" 5-step timeline with icons + "Garanzie & trasparenza" trust strip + "Sede" location block with static map / address / transport / accessibility / hours | anchor-nav (IntersectionObserver active state + smooth scroll) |
| Derm (specialist boutique) | Treatment tabs with 3 domains (clinical/surgical/aesthetic) × items+price+cta + Before/After compare slider with ethical disclaimer + Editorial press feed 4-tile with lightbox | Tabs (keyboard-accessible), Compare slider (mouse/touch/keyboard) |
| Gusto (fine-dining editorial) | Producer showcase (4 artisans with portraits/area/blurb) + Private dining card (Chef's Table / evening buy-out / cellar tasting) + Wine program (sommelier + 3 pairings + cellar facts) | — (reuses existing lightbox on atmospheres; new sections are static-rich) |

**New interaction library additions** (extends `static/css/live-interactions.css` + `live-interactions.js`):
- `[data-li="tabs"]` — horizontal tab bar with `.li-tabs-nav .li-tab-btn[data-li-target]` and matching `.li-tab-panel[data-li-id]`. Fade-in panel transition (520ms), keyboard navigation (Enter/Space/←/→), ARIA roles set by JS, `prefers-reduced-motion` respected.
- `[data-li="compare"]` — before/after slider with `.li-cmp-before/.li-cmp-after` absolute layers, JS-injected handle, mouse+touch+keyboard control, clip-path inset transitions. Graceful no-JS state (handle at 50%).
- `.li-anchor-nav` — sticky subnav with IntersectionObserver-driven `.is-active` state tagging and smooth scroll on anchor click (reduced-motion respecting).

**i18n coverage:** all new sections authored in all 5 locales (it/en/fr/es/ar) across the 3 templates. Native editorial voice per locale — not machine translation. Proper names (chef names, producers, medical devices) stay Latin across all locales consistent with D-059/D-063. Roughly 1,100 new content lines across the 3 i18n tree files.

**RTL adjustments:** new `html[dir="rtl"] ...` blocks added inside specialist `_base.html` and fine-dining `_base.html` to flip accent borders, tab buttons (margin + text direction + underline origin), compare slider labels (before/after swap), pair-row grid (num→right, price→left), producer portrait border (left→right). The compare slider's clip-path remains LTR-mouse-driven by deliberate design (the handle tracks cursor X position regardless of locale direction) — only labels flip.

**Editor Schema Blueprint** (`EDITOR_SCHEMA_BLUEPRINT.md`) — concrete, not theoretical:
- Component registry with 8 edit targets (nav/hero/section/form/contact/blog/footer/locale) + per-field type + edit? flag + constraints + RTL-aware flag.
- Section kinds vocabulary expanded to 20+ kinds (facts, manifesto, signature_services, team_list, pricelist, timeline_steps, trust_strip, map_location, gallery_strip, tabs, compare_slider, editorial_feed, process_cards, wine_program, producer_showcase, press_strip, testimonial_quote, faq_accordion, awards_grid, seasonal_highlight).
- 23 atomic field types for editor UI (text, richtext, image, video, color_token, font_ref, link, page_ref, post_ref, list<T>, content_map, channel, icon, ...).
- Design tokens scope (palette 5 colors, font heading+body from curated list of 18 Google Fonts, radius/icon_pack/image_treatment/motion_profile as select, text/layout alignment, section_density).
- 6 hard invariants the editor must uphold (D-047 → D-059).
- Persistence model proposal (CustomerProject + ProjectContent + ProjectDesignTokens + ProjectRevision) — not implemented, just specified.

**Rationale:** The task had a dual objective that normally tempts a cheap shared component-pack pass: "enrich the 3 live templates" AND "prepare the future editor". The cheap move would have been: one shared section pack applied to all 3, and one abstract editor doc full of hand-waves. Both are rejected. (a) **Shared section pack violates D-054**: making cardio and derm render the same "new sections" would collapse sibling differentiation — the whole point of the medical specialist split in D-060 was to prevent that. So each template gets a distinct section set motivated by its DNA tone: cardio gets clinical precision (journey/trust/map), derm gets boutique aesthetics (tabs/before-after/press feed), gusto gets hospitality editorial (producers/private/wine). (b) **Abstract editor doc is worthless**: a blueprint that says "we'll make everything editable" teaches nobody anything about how to build it. The authored blueprint commits to concrete field types, concrete constraints (min/max list lengths, contrast thresholds, required baseline pages), concrete variant locks (DNA choices are not user-edit), concrete font curation (18 Google Fonts, not "whatever"), concrete persistence model with DB tables. When the editor worktree opens, this document becomes the implementation TODO.

**Option space considered and rejected:**
- **Option A — Minimum enrichment, no blueprint**: quick sections + TODO_NEXT entry for the editor. Rejected because the user's brief explicitly asked for both enrichment AND blueprint in the same session, and postponing the blueprint leaves the next session without the architectural anchor.
- **Option B — Shared section pack across all 3 templates**: rejected per (a) above — kills D-054 differentiation.
- **Option C — Full-editor implementation**: out of scope. The brief explicitly says "NON implementiamo l'editor adesso". Respect scope.
- **Option D — Chosen: differentiated enrichment + concrete blueprint**: yields 3 distinct enrichments and a 600-line spec, matching the brief exactly.

**Trade-off:**
- **Content volume**: +150 lines of IT content per template + 4 × ~90 lines of i18n content per template × 3 templates = ~1,100 new content lines total. Acceptable: content trees are cheap to review, the review surface is flat per-locale, and the new sections are load-bearing for the premium positioning (not filler).
- **CSS/JS growth**: new primitives add ~360 lines of CSS + ~170 lines of JS to live-interactions. Acceptable: zero new dependencies, bundled once and reused by every skin that opts in. The medical specialist skin gains ~320 lines of CSS (cardio-only + derm-only sections each conditional on page_data), the fine-dining skin gains ~200 lines. Both still well under the 1000-line-per-skin authoring complexity budget.
- **Editor not yet implemented**: the blueprint is binding for the future editor but the 3 templates remain non-editable today. This is intentional per the brief scope and D-049 (roadmap freeze until Phase 2g3.7).
- **i18n parity**: all 5 locales authored in the same session — higher cost upfront but avoids the "IT-only new section" drift that would break the premium uniformity across locales.

**Consequence:**
- (a) The 3 `published_live` templates now genuinely differ in dense-home richness, not just in archetype chrome. A buyer comparing cardio vs derm on the marketplace card sees two distinct clinical propositions even though they share the specialist skin; a buyer opening gusto sees a hospitality product that no medical template even attempts to fake.
- (b) The new interaction primitives (tabs, compare, anchor-nav) are now part of the `live-interactions.js` public surface. Any draft template reaching `published_live` in Phase 2g3 can opt in (e.g., ecommerce `fashion-editorial` could use tabs for collection browsing, portfolio could use compare for project before/after, lawyer could use anchor-nav on practice-areas pages).
- (c) The Editor Schema Blueprint becomes the architectural anchor for the future editor app. When Phase 2g3.7 closes and auth/editor/projects/commerce unlock per D-049, the blueprint is the source of truth for: component registry shape, field types, constraints, invariants, persistence model. Implementation becomes a matter of reading the blueprint and writing code, not debating design.
- (d) The D-054 Premium Differentiation Law is strengthened by concrete evidence: 3 templates that share 2 archetypes (specialist medical + fine-dining restaurant) can still carry genuinely distinct premium sections via content-driven conditional rendering. The pattern — `{% if page_data.X %}` in the shared skin + per-template content block — is confirmed as the scaling primitive for adding premium sections to archetype families without forking the skin.
- (e) Any future `published_live` template should declare in its DNA which premium sections it carries (an optional `premium_sections: ["journey", "trust", ...]` list) and the content registry provides their data. This formalization is out of scope for Session 30 but is the natural next step when Phase 2g3 starts authoring new skin folders.

**Non-negotiable quality floor:**
- Every new section MUST fit the template's DNA tone (clinical / boutique / hospitality). A section that would work identically on all 3 templates is a red flag.
- Every new content block MUST be authored in all 5 locales in native voice. Empty locales on a `published_live` template break the pilot architecture and get rejected at tier-sync time.
- Every new interaction primitive MUST respect `prefers-reduced-motion` and degrade gracefully without JS.
- Every new section MUST pass the D-047 leak sweep (no literal brand names / cities / quotes in HTML files — all strings from the content registry).

**Validation results (Session 30):**
- `python manage.py check`: 0 issues.
- Route sweep: 85/85 across 3 templates × 5 locales × mixed page kinds = 200.
- Marketplace surfaces: 4/4 200.
- Cross-template contamination sweep: zero (Ricciardi/Marani/Osteria/Parioli/Vallesi all confined).
- Differentiation validation: 16/16 (cardio sections never appear on derm, derm sections never appear on cardio, gusto sections never appear on medical, medical sections never appear on gusto).
- i18n coverage: 12/12 (all 3 new section-sets × 4 non-IT locales).
- AR RTL: 3/3 (`dir=rtl`, new section translations visible).

## D-063: Gusto i18n/RTL Closure — Third Published_live Template Fully Multilingual, Reusable Restaurant Chrome Keys (2026-04-13, Session 29)

**Decision:** The third `tier=published_live` template, `gusto-fine-dining`, now ships in five locales (`it`, `en`, `fr`, `es`, `ar`) with real RTL for Arabic, completing Phase 2i.2. All 3 public templates (cardio / derm / gusto) are fully multilingual. The architecture established by D-059 (Session 23 cardio pilot) was extended to the fine-dining archetype with zero changes to the pilot infrastructure — proving the shape works across a second skin family with a different tone (restaurant hospitality, not medical clinical).

**What shipped:**
- `apps/catalog/template_content_gusto_i18n.py` — 4 hand-authored content trees (EN/FR/ES/AR), ~1250 lines. Native editorial voice per locale; zero machine translation. Proper names (chef/staff/producers/wines/press) stay Latin across all locales per the Session 23 precedent.
- `apps/catalog/template_content.py` — GUSTO_CONTENT_IT extended with missing content keys (~30 new keys) for every previously-hardcoded HTML literal; imports + wires the 4 new locale trees; TEMPLATE_CONTENT["gusto-fine-dining"] now carries all 5 locales.
- `apps/catalog/template_i18n.py` — CHROME_I18N extended with 9 new keys: `mp_other_restaurant`, `foot_restaurant`, `foot_concierge`, `foot_services`, `fd_wine_pairing`, `fd_email_label`, `fd_phone_label`, `blog_read_article`. These are restaurant-category-generic and will be reused by the draft restaurant archetypes (`trattoria-warm` / `street-modern`) when they reach `published_live` in Phase 2g3.1.
- `templates/live_templates/restaurant/fine-dining/_base.html` — dynamic `<html lang dir>`, conditional Amiri + Noto Kufi Arabic font loading for AR only, mp-bar language switcher pill strip, chrome strings wired, every nav/footer/ctas URL preserves `?lang=` when non-IT, new `html[dir="rtl"] ...`-scoped CSS block with 2 parts: (a) core RTL (font stack swap, 17px body / 1.85 line-height, letter-spacing flatten, nav grid flip, eyebrow bar `:before→:after`, gold-btn arrow `→→←`, mp-bar row-reverse) and (b) page-level section overrides inside `{% if is_rtl %}` for `.fd-hero` / `.fd-chef-inner` / `.fd-concierge-inner` / `.fd-wine-inner` / `.fd-method-inner` / `.fd-private-inner` / `.fd-ingredienti` grid-template-columns flip, drop-cap `float: left→right`, border-left→border-right on portraits, right-align/left-align on numbered columns, etc.
- All 7 page templates (home / about / menu / gallery / reservations / blog_list / blog_detail) wired to read labels from `page_data.*` + `chrome.*` + `site.*` instead of hardcoded literals. Every URL preserves locale.

**Restaurant chrome keys added (reusable for Sapore + Brace):**
- `mp_other_restaurant` — "Altri template ristoranti →" / "More restaurant templates →" / ...
- `foot_restaurant` — "Il ristorante" (footer heading, distinct from `foot_studio` used by medical)
- `foot_concierge` — "Concierge"
- `foot_services` — "Servizi" (distinct from `foot_hours` — semantically richer; covers opening-hours block with services description)
- `fd_wine_pairing` — "In abbinamento" / "Paired with" / "Accord mets-vin" / ... (menu course wine-pairing label)
- `fd_email_label` — "Email" / "البريد الإلكترونيّ"
- `fd_phone_label` — "Telefono" / "Phone" / ... (concierge contact labels)
- `blog_read_article` — "Leggi l'articolo" (shorter variant of existing `blog_read_full`)

**Rationale:** D-059 explicitly anticipated this rollout: "Phase 2i.2 step 2 — Gusto (adds a new archetype RTL block)" and "extend CHROME_I18N with the additional keys needed or factor a per-archetype extension pattern. Decision deferred to the next session." Session 29 chose to extend CHROME_I18N flat with restaurant-scoped keys rather than namespace by archetype — the keys are category-generic (not `fd_*`-specific) and future restaurant archetypes will reuse them. This keeps the per-locale review surface flat: one dict, one language end-to-end per review pass. The `fd_*` prefix on `fd_wine_pairing` / `fd_email_label` / `fd_phone_label` is a deliberate narrower scope because those specific labels are tied to fine-dining chrome layout (menu course wine bar, concierge contact strip). Future restaurant archetypes with different chrome may introduce their own `tr_*` / `sm_*` keys rather than reuse these.

The RTL CSS authoring choice mirrored the specialist (cardio) pilot pattern: one `html[dir="rtl"] ...`-scoped block inside the skin's `_base.html`, split into core + page-level with `{% if is_rtl %}` gating the page-level section so LTR users don't pay the CSS cost. No separate `rtl.css` file introduced. This matches D-058 (Live Motion Language) and D-059 (i18n pilot) — one small gated block, zero new files.

The decision to keep proper names (chef "Lorenzo Fioravanti", maître "Greta Vallesi", producers like Tarbouriech / Brezza / Pacherhof / Pieropan, wines like Champagne Selosse / Barolo Cannubi / Domori, press outlets GUIDA MICHELIN / GAMBERO ROSSO / IDENTITÀ GOLOSE, address "Via San Marco 17", phone "+39 02 3611 9920", email "concierge@osteriamoderna.it") in Latin script across AR is the same stance as D-059 for doctor names and medical press outlets: these are canonical identifiers in world food press / hospitality and transliteration would be ugly + lossy.

**Trade-off:** Same as D-059 — content duplication (each locale carries a full mirror, including non-localizable data like phone numbers). Roughly 5× content size for gusto. Acceptable: content trees are a few KB each, duplication is flat with no cross-references to keep in sync, review surface is one locale per pass.

**Consequence:**
- (a) Phase 2i.2 closes in full. All 3 `tier=published_live` templates now ship in 5 locales with working RTL.
- (b) Any future restaurant archetype reaching `published_live` in Phase 2g3.1 (Sapore / Brace) inherits the 7 restaurant-generic CHROME_I18N keys for free. Only new work needed: (i) 4 locale content trees for that template, (ii) a new `html[dir="rtl"] ...` scoped block inside the new skin's `_base.html` with the new archetype's selector prefix (`.tr-*` for trattoria-warm, `.sm-*` for street-modern). Budget per template: ~3h same as Gusto.
- (c) The Arabic font stack decision (Amiri + Noto Kufi Arabic) is now validated across both specialist and fine-dining skins — it's the reusable default for any future `tier=published_live` template.
- (d) The decision to put archetype-specific labels (Gusto-brand-specific like `chef_label` / `star_tag` / `courses_label`) in the CONTENT registry rather than CHROME_I18N is the reusable pattern: CHROME_I18N = archetype-agnostic cross-cutting chrome; content registry = brand-specific copy. This keeps `template_i18n.py` from ballooning into a per-template label dump.
- (e) Motion + interactions (D-058 + D-062) continue to work unchanged — i18n pilot does not touch data-lm / data-li attributes. 25 reveal targets / 5 stagger parents / 3 counters / 4 lightbox triggers all preserved on gusto home in all 5 locales including AR.

**Non-negotiable quality floor reaffirmed:** Native editorial voice per locale. Each tree authored by a human food writer for the target market. Machine-translated content is a Phase 2i.2 rollback trigger.

## D-062: Ultra Premium Live Interaction Pass — New Interactive Components and Premium Sections (2026-04-12, Session 28)

**Decision:** The 3 `tier=published_live` templates receive a comprehensive enrichment pass adding new interactive components, premium content sections, and visual richness. A new zero-dependency interaction library (`live-interactions.css` + `live-interactions.js`) is introduced alongside the existing motion system, providing accordion, lightbox, and sticky CTA components.

**New interaction library:**
- `static/css/live-interactions.css` — Accordion, lightbox overlay, sticky CTA bar styles
- `static/js/live-interactions.js` — Accordion toggle, lightbox gallery with keyboard navigation, IntersectionObserver-driven sticky CTA
- All components degrade gracefully without JS and respect `prefers-reduced-motion`
- Loaded only inside live-template skins (not on marketplace)

**Per-template enrichments (each template gets DIFFERENT interactive patterns):**

| Template | New Sections | Unique Interactions | Section Count |
|----------|-------------|-------------------|---------------|
| Cardio | Technology grid (4 SVG icons), testimonial, FAQ accordion (5 Qs) | Sticky CTA bar, accordion FAQ, equipment icons | +3 sections |
| Derm | Gallery strip (4 images), testimonial, FAQ accordion (5 Qs) | Sticky CTA bar, accordion FAQ, image gallery hover | +3 sections |
| Gusto | Ingredients band, awards grid, seasonal card, expanded atmosphere (3→4) | Lightbox gallery, awards badges, seasonal highlight | +3 sections |

**Differentiation preserved and strengthened:**
- Cardio gets data/technology focus (clinical precision)
- Derm gets visual/gallery focus (boutique aesthetics)
- Gusto gets editorial/cinematic focus (theatrical hospitality)
- No shared interactive patterns across categories: medical gets accordion+sticky, restaurant gets lightbox+seasonal
- Inner pages enhanced: Gusto gallery has lightbox, Gusto reservations has process icons

**i18n impact:** All new content blocks translated into 5 locales (IT/EN/FR/ES/AR) for both medical templates. Gusto remains IT-only per Phase 2i.2 scope. All new sections render correctly in RTL (Arabic).

**Rationale:** D-054 Premium Differentiation Law requires distinct interaction patterns. The ultra-premium pass adds depth and richness without flattening differentiation — each template's new features are motivated by its brand personality and category semantics, not generic "premium template" features.

## D-061: Medical Motion Opt-In — Specialist Skin Adopts Live Motion Language with Clinical Profile (2026-04-12, Session 27)

**Decision:** The specialist archetype skin (`templates/live_templates/medical/specialist/`) adopts the live motion language (`static/css/live-motion.css` + `static/js/live-motion.js`) introduced by D-058 on the fine-dining archetype (Gusto). The adoption uses a **medical motion profile** — reduced intensity tokens overriding the shared CSS on the specialist `:root` — and 4 pattern categories applied across all 8 specialist page templates plus `_base.html`.

**Medical motion profile (token overrides in specialist `_base.html`):**
- `--lm-rise: 10px` (Gusto: 14px) — body reveal rise almost imperceptible
- `--lm-rise-lg: 16px` (Gusto: 22px) — heading entry more contained
- `--lm-dur-slow: 680ms` (Gusto: 720ms) — slightly faster, more precise
- Stagger delay: 80–100ms per child (Gusto: 70ms) — more deliberate cadence
- Image hover: filter transition only (Gusto: scale 1.045x zoom) — clinical, not cinematic

**4 motion patterns implemented:**
1. **Reveal-on-scroll** (`data-lm="reveal|reveal-lg|reveal-soft"`) — fade+rise on sections, headings, content blocks, CTA bands, form areas. Smaller rise distance makes the effect nearly invisible but perceptibly premium.
2. **Staggered reveal** (`data-lm-stagger`) — cascaded entry on facts band, signature visits, values grid, treatments pricelist, process steps, contact blocks, press outlets, credentials (Derm-only), blog list rows, doctor tags. Delay 80–100ms per child for deliberate professional rhythm.
3. **CTA hover refinement** — gold-btn arrow `→` shifts +4px on hover (Gusto: +6px), ghost-btn border lifts to accent, submit buttons gain subtle opacity transition. RTL-aware: arrow shift inverts for Arabic. All gated by `prefers-reduced-motion`.
4. **Image attention lift** — portrait and featured-image filter transitions on hover (from `grayscale(15%)` to `grayscale(0%) contrast(1.10)`). More clinical than Gusto's cinematic zoom. Zero HTML restructuring required.

**Patterns deliberately excluded for medical:**
- Counter animation (too promotional for clinical context — numbers should appear already authoritative)
- Nav underline sweep (too editorial/restaurant)
- Marquee (inappropriate for medical)
- Image zoom (requires wrapper+inner HTML refactor; filter lift achieves equivalent premium feel)

**Differentiation preserved (Cardio vs Derm):**
The motion profile is shared (same _base.html, same tokens) but the structural variants already in place produce different visual rhythms:
- Cardio: split-consultive hero → left text reveal + right sidebar reveal; no credentials section
- Derm: editorial-magazine hero → portrait reveal-soft + text reveal; credentials section with stagger
The motion does NOT flatten the differentiation; it respects and enhances it.

**Files modified (specialist skin only — zero changes to Gusto, shared motion files, or marketplace):**
- `_base.html` — link live-motion.css, script live-motion.js, medical token overrides, CTA/image hover CSS, reduced-motion guards, RTL arrow-shift override
- `home.html` — 11 reveal + 4 stagger attributes (Cardio), 12 reveal + 5 stagger attributes (Derm)
- `about.html` — stagger on history rows + values grid, reveal on method + CTA band
- `services.html` — stagger on treatments, reveal on footnote + CTA band
- `team.html` — reveal on each doctor, stagger on tags
- `contact.html` — stagger on contact blocks, reveal on form + sidebar
- `appointment.html` — stagger on process steps, reveal on form band
- `blog_list.html` — reveal on lead post, stagger on compact list
- `blog_detail.html` — reveal on lede, h2 headings, blockquotes

**Rationale:** D-058 explicitly stated that cardio and dermatologia "should adopt [the motion language] in a follow-up pass (low effort: link + script + attributes)" and that "a muted Medical skin sets `--lm-rise: 10px` for a more subdued cadence." This session executes exactly that prescription. The medical motion profile is intentionally more restrained than Gusto's restaurant motion because: (a) clinical precision demands nearly invisible movement — the motion guides the reader's eye, not entertains; (b) the specialist skin's existing image filters (grayscale, contrast, gradient overlays) already create a moody editorial feel that zoom animations would fight with; (c) the premium differentiation law (D-054) requires that sibling templates NOT converge on the same interaction feel — Gusto's dramatic cinematic zoom must remain distinct from the specialist's clinical subtlety.

**Consequence:** (a) All 3 `tier=published_live` templates now have the motion language active — the interaction-quality floor is met; (b) the medical motion profile (`--lm-rise: 10px`, filter hover instead of zoom) is the standard for any future medical archetype (clinic, family, wellness) when they reach `published_live` in Phase 2g3; (c) the D-053 acceptance checklist now has 10 gates (previously 9) for every template promoted from `draft` → `published_live`; (d) future non-medical archetypes (business, portfolio, ecommerce) should define their own token profile based on their category tone — the pattern is: override `:root` tokens in the skin's `_base.html`.

## D-059: i18n/RTL Pilot Architecture — Locale-Keyed Content Registry, Query-Param Switcher, No Django gettext (2026-04-11, Session 23)

**Decision:** Multilingual publishing for `tier=published_live` templates is implemented as a **locale-keyed content registry** + a per-archetype **CHROME_I18N dict** + a **`?lang=xx` query param** resolved in `LiveTemplateView.setup()`, with **no Django `{% trans %}` / `.po` / `gettext` tooling**. The pilot surface is scoped to the live-template preview routes only — the marketplace chrome (homepage, listing, detail, category) stays Italian. The concrete shape shipped on `cardio-studio-specialistico` in Session 23:

1. **Locale-keyed content registry** — `apps/catalog/template_content.TEMPLATE_CONTENT` is a `{slug: {locale: tree}}` mapping. Each `tree` is the full content block previously keyed flat at the slug level. Cardio ships with 5 locales (`it`, `en`, `fr`, `es`, `ar`) — the 4 non-IT trees live in a sister file `template_content_cardio_i18n.py` so the main registry stays browsable. Dermatologia and Gusto are IT-only and wrapped under `{"it": ..._IT}` to keep the helper API uniform.
2. **Chrome i18n dict** — `apps/catalog/template_i18n.CHROME_I18N[locale][key]` carries the ~30 generic labels the specialist skin itself renders (marketplace bar, footer section headings, form field labels, blog "read full article"/"min read"/"back to all" links, nav aria-label). Archetype-agnostic — any future skin adopting the pilot reuses this dict. `get_chrome(locale)` merges IT fallback on missing keys so a partially-authored locale still renders.
3. **Locale resolution** — `template_i18n.resolve_locale(request)` reads `?lang=xx`, validates against `SUPPORTED_LOCALES = ("it", "en", "fr", "es", "ar")`, falls back to `DEFAULT_LOCALE = "it"` on unknown/missing. Stateless — no session, no cookies, no middleware. `LiveTemplateView.setup()` stores `self.locale`, passes it to every `template_content.*` helper.
4. **Page slugs stay Italian across locales** — `studio`, `visite`, `medici`, `pubblicazioni`, `contatti`, `richiedi-visita` are stable slugs; only the `label` field in the `pages` list is translated per locale. Avoids per-locale URL maps. URL pattern file untouched. Works for Arabic because the URL stays ASCII.
5. **Nav href locale preservation** — every chrome nav link and in-page CTA in the specialist skin appends `?lang={{ locale }}` only when `locale != default_locale`. Pattern is `{% if locale != default_locale %}?lang={{ locale }}{% endif %}` — direct Django template fragment, repeated where needed (future improvement: hoist into a `lang_url` template tag).
6. **RTL for Arabic** — `<html lang="ar" dir="rtl">` via `html_dir` context var. `_base.html` ships an `html[dir="rtl"] ...`-scoped CSS block that (a) bumps body font 16→17px and line-height 1.6→1.8 for naskh readability, (b) zeroes negative letter-spacing on all h1–h5 (Arabic shapes don't want tracking), (c) lowers uppercase letter-spacing on eyebrows/section labels from 0.22em to 0.04em, (d) swaps `.sp-lead .eyebrow:before` to `:after` so the accent bar appears on the correct side, (e) flips `.sp-lead .gold-btn:after` from `→` to `←`, (f) reverses the nav-grid `.left`/`.right` justify-content so visual order matches reading direction. Arabic strings in `CHROME_I18N["ar"]` also author arrows natively (e.g. `"mp_back": "العودة إلى MarketWeb →"` points right because RTL reading).
7. **Arabic font stack** — conditional `{% if is_rtl %}` Google Fonts `<link>` loads Noto Naskh Arabic (serif, mirrors Cormorant's editorial tone) + Noto Kufi Arabic (body). Latin fallback preserved inside the stack so mixed Latin/Arabic strings (Roma addresses, phone numbers, press outlets like LANCET/European Heart Journal, doctor names) stay legible — these are intentionally kept in Latin script across every locale.
8. **Language switcher** — compact pill strip rendered inside the marketplace bar on every live-preview page. Each pill has `code/label/badge/is_current` built by `locale_switcher_entries(current_locale)`. The current pill wraps the preview URL with `?lang={{ code }}` and carries `lang="ar" dir="rtl"` per-pill when AR so native font rendering applies to the الع pill itself.

**Rationale:** The project needed the multilingual architecture VALIDATED on one real live template before any rollout to the other `tier=published_live` templates. The 5-locale + RTL-Arabic combination is the gating question — if the shape doesn't handle Arabic cleanly, every other locale is academic. The option space was:

- **Option A — Django `{% trans %}` + `.po` files**: the "textbook" shape. Rejected because (a) compiled `.mo` files require `gettext` binaries, flaky on Windows dev boxes, adds a build step, (b) splits every string across two files (`.po` and the content dict), doubling the review surface, (c) the pilot's job is to prove the shape with ZERO new build tooling, (d) phase-later migration to `{% trans %}` is trivial because every string is ALREADY namespaced by locale in the locale-keyed dict — the door is not closed.
- **Option B — `django-modeltranslation` / per-field translated columns in the DB**: rejected because (a) content for full multi-page templates is structured (lists of doctors, courses, blog posts, opening hours), not flat text, so a model field approach would need an explosion of columns OR nested JSONField, (b) the content registry is already a Python dict by design (D-042) — promoting to DB is a future-iteration move once customers edit content via the editor app, not a pilot task.
- **Option C — locale-keyed Python content dict + CHROME_I18N dict + `?lang=` param** (the chosen shape): (a) one file per locale tree, review surface matches authoring surface, (b) no build tooling, (c) unambiguous fallback semantics (`pick_localized` with IT backstop), (d) trivial to test — every request is an HTTP GET with a query param, (e) extends additively per template without touching existing trees, (f) migration to `{% trans %}` for the marketplace chrome itself remains a one-function `_()` wrap away.
- **Option D — path-prefix routing (`/en/preview/...`)**: rejected as out of scope for the pilot. A query param is the minimum-surface choice that keeps the URL pattern file untouched and extends naturally to a prefix later if the marketplace itself starts shipping multilingually. The pilot is validating the CONTENT and RTL mechanics, not the final URL scheme.

The RTL decision to ship a `html[dir="rtl"]`-scoped CSS block instead of a full separate Arabic stylesheet is the same choice as D-058 (Live Motion Language): one small gated block inside the existing `_base.html`, zero new file to maintain, trivial to port to a sister skin by copy + selector rename. A separate `rtl.css` would create a second file with its own stale-cache risk and no advantage at pilot scale.

The decision to keep page slugs Italian across locales comes from three constraints: (1) the URL pattern file is under the catalog app and is shared with draft templates — introducing per-locale slug maps would ripple into every future published template; (2) Arabic URLs with transliterated slugs would look worse than ASCII Italian slugs to an Arabic reader (transliteration is ugly; Arabic script in URLs is noisy); (3) the pilot's job is to prove the CONTENT architecture, not the routing architecture. Phase-later URL-scheme migration is an independent, orthogonal decision.

**Trade-off:** Content duplication — each locale carries a complete mirror of the tree, including non-localizable data like phone numbers and addresses. Roughly 5× content size for a fully-localized template. Acceptable: (a) content trees are at most a few KB each, (b) the duplication is flat (no cross-references to keep in sync), (c) non-localizable data is stable and rarely edited, (d) the review surface is one locale per review pass which is cleaner than diffing shared-base-plus-overlays. The `pick_localized` helper accepts both the new `{locale: tree}` shape and the legacy flat shape, so migration of other templates is strictly additive. Another trade-off: the pilot does NOT introduce a language-switcher on the marketplace chrome itself (homepage / listing / detail), so a visitor who lands on `/templates/medical/cardio-studio-specialistico/?lang=en` sees an Italian detail page. This is intentional — the pilot's job is to validate the live-preview surface, and the marketplace chrome is a separate Phase 4 concern.

**Consequence:** (a) Phase 2i.1 closes with cardio shipping as a genuinely 5-locale premium template with working RTL; (b) the recipe is reusable — Phase 2i.2 adopts the shape on derm (cheapest — same RTL CSS already in place) then gusto (adds a new `.fd-*` RTL CSS block); (c) the `{slug: {locale: tree}}` registry shape is the standard for every future `tier=published_live` template that ships multilingually — new templates author content directly in this shape from line one; (d) `template_i18n.py` is the single source of truth for chrome strings, locale metadata, RTL locale set, and the locale-resolution helper — any future rollout (e.g. adding Portuguese or German) adds 1 entry per table in this file; (e) the marketplace chrome remains Italian-only until a separate Phase 4 decision lifts it; (f) `CHROME_I18N` is the natural migration target when/if the marketplace chrome ever moves to Django `{% trans %}` — every key becomes a `_("...")` call at that point and the keys/values are already in the right shape; (g) every new `published_live` template promotion must declare its locale coverage in `TEMPLATE_REGISTRY.json` (future: add a `locales` field on each row) — for now the presence of a locale key in `TEMPLATE_CONTENT[slug]` is the authoritative source.

**Non-negotiable quality floor for future locales:** each locale block must be authored in the native editorial voice for its market, NOT machine translation. EN reads as Anglo-American clinical prose. FR uses classical French medical register and `vous`. ES uses Spanish peninsular register. AR uses Modern Standard Arabic with formal medical register and native punctuation (« »). A future pull request that ships auto-translated locale blocks should be rejected — the premium marketplace positioning is the reason this decision exists in the first place.

## D-001: Django App Structure — Modular Multi-App (2026-04-09)
**Decision:** Seven separate Django apps under `apps/` directory: core, accounts, catalog, editor, projects, commerce, pages.
**Rationale:** Each domain has distinct responsibilities. Avoids monolithic app. Enables parallel development (backend-core can work on catalog models while premium-ui works on templates).
**Trade-off:** More boilerplate vs. better separation of concerns and scalability.

## D-002: Custom User Model from Day One (2026-04-09)
**Decision:** Create custom User model in `accounts` app before first `migrate`.
**Rationale:** Switching to a custom User model after migrations exist is extremely painful in Django. Even if we don't need custom fields now, this is a one-way door that must be done first.

## D-003: Services/Selectors Pattern (2026-04-09)
**Decision:** Business logic in `services.py` (writes) and `selectors.py` (reads), not in views or models.
**Rationale:** Keeps views thin, makes logic testable without HTTP, prevents fat model anti-pattern.

## D-004: "WebTemplate" Naming for Marketplace Items (2026-04-09)
**Decision:** Marketplace template listings are called `WebTemplate` (model) in the `catalog` app.
**Rationale:** Avoids confusion with Django's template engine. The app is `catalog`, not `templates`.

## D-005: Bootstrap 5.x with Custom SCSS (2026-04-09)
**Decision:** Use Bootstrap 5 as the CSS framework, but heavily customized via SCSS variables and custom components.
**Rationale:** Bootstrap provides responsive grid, utilities, and accessibility out of the box. Custom SCSS prevents the "default Bootstrap" look and achieves premium aesthetics.

## D-006: Django 5.2.7 LTS (2026-04-09)
**Decision:** Use Django 5.2.7 (the version actually installed), not 6.0.4 as stated in the auto-generated settings comment.
**Rationale:** 5.2 is the current LTS release. The settings.py was generated from a template that referenced 6.0.4, but our environment has 5.2.7.

## D-007: UUIDs for Customer-Facing IDs (2026-04-09)
**Decision:** Use UUIDs for public-facing resources (projects, orders, licenses). Integer PKs internally.
**Rationale:** UUIDs prevent enumeration attacks and look professional in URLs. Integer PKs kept for internal FK performance.

## D-008: SQLite for Development, PostgreSQL for Production (2026-04-09)
**Decision:** Keep SQLite for local dev. Plan for PostgreSQL in production.
**Rationale:** SQLite is zero-config for development. PostgreSQL provides the JSON fields, full-text search, and concurrency needed in production.

## D-009: Stripe for Payments (2026-04-09)
**Decision:** Stripe as the payment processor (already installed in environment).
**Rationale:** Industry standard, excellent Python SDK, supports one-time payments and subscriptions.

## D-010: Italian as Primary Language (2026-04-09)
**Decision:** Italian is the primary language, with EN, FR, AR as secondary.
**Rationale:** Project originates in Italian market. Arabic requires RTL support.

## D-011: `mw-` CSS Class Prefix (2026-04-09)
**Decision:** All custom CSS classes use `mw-` prefix (e.g., `.mw-btn`, `.mw-template-card`, `.mw-hero`).
**Rationale:** Avoids collision with Bootstrap utility classes and third-party CSS. Makes custom styles easily identifiable.

## D-012: Plus Jakarta Sans + Inter Font Pairing (2026-04-09)
**Decision:** Plus Jakarta Sans for display/headings, Inter for body text. Both from Google Fonts.
**Rationale:** Plus Jakarta Sans has a distinctive, premium feel with excellent weight range (500-800). Inter is the gold standard for UI body text with excellent readability. Both are free and well-supported.

## D-013: CSS Custom Properties Over SCSS (2026-04-09)
**Decision:** Use native CSS custom properties (variables) instead of SCSS for the design system.
**Rationale:** Zero build step for development. Custom properties work at runtime (theming possible). Can add SCSS later if needed without breaking existing styles. SCSS can still be introduced later for nesting/imports.

## D-014: Template Cards Reference Backend Model Fields (2026-04-09)
**Decision:** Template card partials use `template.name`, `template.brand.brand_name`, `template.category.name`, `template.price`, `template.is_free`, `template.short_description`, `template.assets.first.file.url` — matching backend-core's catalog models.
**Rationale:** Ensures seamless integration when backend views pass model instances to templates. Static fallback content provided for development without backend data.

## D-015: Static Fallback Content in Listing Pages (2026-04-09)
**Decision:** Listing pages include `{% if templates %}...{% else %}...{% endif %}` blocks with hardcoded realistic content.
**Rationale:** Allows the UI to be previewed and developed independently of backend views. Fallback content uses realistic Italian text matching CONTENT_GUIDELINES.md. Will be replaced by dynamic data as backend views are connected.

## D-016: All Template Content in Italian (2026-04-09)
**Decision:** All UI text, placeholder content, and microcopy written in Italian as the primary language.
**Rationale:** Per D-010, Italian is the primary market language. i18n/{% trans %} tags will be added in Phase 4 for multilingual support.

## D-017: Category Names in Italian, Slugs in English (2026-04-09)
**Decision:** Category `name` field uses Italian display names (Ristorante, Medico, Avvocato, Immobiliare) while `slug` stays English (restaurant, medical, lawyer, real-estate).
**Rationale:** Italian names match the homepage UI and D-016. English slugs are URL-friendly and internationally readable. International categories (Agency, Business, Portfolio, eCommerce) are the same in both languages.

## D-018: Two-Segment Detail URL `/<category>/<slug>/` (2026-04-09)
**Decision:** Template detail uses `/templates/<category_slug>/<template_slug>/` instead of `/templates/<slug>/`.
**Rationale:** Prevents slug collisions across categories (e.g., two categories could each have a "starter" template). Also improves SEO with category context in the URL and enables breadcrumb navigation.

## D-019: Selectors Return QuerySets (2026-04-09)
**Decision:** Catalog selectors return Django QuerySets, not evaluated lists.
**Rationale:** Allows views to chain additional filters, annotations, or pagination on top. QuerySets are lazy — no DB hit until the template iterates.

## D-020: Icon Field Without `bi-` Prefix (2026-04-09)
**Decision:** Category `icon` stores just the icon name (e.g., "megaphone") without the `bi-` prefix. The template partial renders `<i class="bi bi-{{ category.icon }}">`.
**Rationale:** Previous seed data stored "bi-rocket-takeoff" which would render as `bi bi-bi-rocket-takeoff` (double prefix). Keeping the raw name is more portable — could switch icon libraries later.

## D-021: Static Fallbacks Removed After Catalog Integration (2026-04-09)
**Decision:** Removed all hardcoded static fallback content from listing pages. Pages now show `{% empty %}` states instead.
**Rationale:** D-015 was a temporary measure for UI development. With catalog views and seed data in place, static fallbacks are no longer needed and would mask missing data issues.

## D-022: SVG Preview Images Using Brand Palettes (2026-04-09)
**Decision:** Generate structured SVG files that look like website mockups (browser chrome + page layout), colored with each template's brand palette. Stored via TemplateAsset model (asset_type='preview').
**Rationale:** SVGs scale perfectly, are lightweight, and each is visually unique because of the distinct brand palettes. The browser-chrome framing makes them look like real screenshots. They can be replaced with actual screenshots later without changing any template code — just swap the TemplateAsset file.

## D-023: Search via ORM icontains Across 4 Fields (2026-04-09)
**Decision:** Search filters using Django ORM `Q(name__icontains=q) | Q(short_description__icontains=q) | Q(description__icontains=q) | Q(brand__brand_name__icontains=q)`.
**Rationale:** Simple, works with SQLite in dev. PostgreSQL full-text search can replace this in production via a selector swap — no view or template changes needed.

## D-024: Four Sort Options, No "Popular" (2026-04-09)
**Decision:** Sort options are: recent (default), price ascending, price descending, name A-Z. "Popular" sort omitted.
**Rationale:** No view/download count model exists yet. Adding a dummy popularity sort would be misleading. Can add when commerce or analytics tracking is implemented.

## D-025: Pagination at 12 Per Page (2026-04-09)
**Decision:** `paginate_by = 12` on TemplateListView.
**Rationale:** 12 items = 4 rows of 3 cards on desktop, a comfortable scroll depth. Matches the 3-column grid layout. With 16 templates, produces 2 pages — enough to verify pagination works.

## D-029: HTML Compositions + Playwright Screenshots for Previews (2026-04-10)
**Decision:** Replace SVG-string previews with PNG screenshots of Django-rendered HTML pages, captured via headless Chromium (Playwright sync API).
**Rationale:** A premium marketplace cannot ship grey wireframes. Real homepage screenshots with photographic content communicate template value at a glance and dramatically improve conversion intent. HTML+CSS gives us the same expressive control as a real website (fonts, gradients, real photos) without re-implementing a layout engine in Python. The `TemplateAsset` API stays the same, so listing/detail templates need zero changes — only the file format moves from `.svg` to `.png`.
**Trade-off:** Heavier dependency surface (Playwright + Chromium binary), larger asset files (~4 MB vs ~5 KB), and screenshot generation requires a browser process. Acceptable because previews are generated offline and served as static media.

## D-030: Per-Category Preview Compositions, Brand-Customised at Render Time (2026-04-10)
**Decision:** One HTML composition per MVP category (8 total), parameterised by brand palette + typography. Multiple templates inside a category share the same layout and stock imagery; brand identity comes from injected colours and Google Font pairing.
**Rationale:** 8 well-crafted layouts is a much better quality bar than 16+ rushed ones. Category specificity (a restaurant looks like a restaurant, a clinic looks like a clinic) is the primary signal users need. Brand differentiation via palette + type still gives each preview its own colour signature without doubling the maintenance cost.
**Trade-off:** Two templates in the same category have identical photo content. Mitigation path: add an optional `imagery_overrides` field on `TemplateBrand` later if buyers report confusion.

## D-031: Curated Stock Imagery via Cached Unsplash URLs (2026-04-10)
**Decision:** Imagery is configured as a Python dict (`apps/catalog/preview_imagery.IMAGERY_CONFIG`) of category → list of Unsplash CDN URLs, with a `ensure_cached()` helper that downloads them once into `media/preview_imagery/<category>/<sha>.jpg` and returns local file paths.
**Rationale:** A single config file is the swap point. To move to local stock, licensed images, or AI-generated illustrations later, only the config changes — compositions and the generator stay untouched. The cache means subsequent runs are offline-friendly and idempotent. Unsplash CDN URLs are stable and free for commercial use under Unsplash's license.
**Trade-off:** First run requires network access; broken URLs degrade gracefully (the affected slot just falls back to the hero photo, padded by `_build_context`).

## D-032: Three-Phase generate_previews Pipeline (2026-04-10)
**Decision:** The command runs in three sequential phases: (A) all ORM reads + HTML rendering, (B) Playwright headless screenshots with no ORM access, (C) all ORM writes (TemplateAsset persistence).
**Rationale:** `playwright.sync_api.sync_playwright()` runs an asyncio loop on the calling thread. Inside its `with` block, Django's ORM raises `SynchronousOnlyOperation` because the loop is "running". Splitting work into three phases avoids the conflict cleanly without `sync_to_async` shims.
**Trade-off:** All templates' rendered HTML must be held in memory before screenshots start. At 16 templates × ~10 KB HTML = 160 KB, this is irrelevant.

## D-033: 1600×900 PNG at 2× Device Scale (2026-04-10)
**Decision:** Previews render at viewport 1600×900 with `device_scale_factor=2`, output PNG. Resulting files are ~3200×1800 pixels and ~4 MB each.
**Rationale:** 16:9 matches the 4:3-to-16:9 ratio expected by the existing template card. 2× DPI keeps text crisp on retina displays. PNG preserves the sharp UI lines (buttons, dividers) without JPEG halos.
**Trade-off:** ~70 MB total media for 16 templates. Acceptable for development; for production we should add an optional `--optimize` step that runs `oxipng`/`pngquant` or pipes through Pillow with `optimize=True`/JPEG conversion.

## D-034: Per-Template DNA Registry in Code, Not in the Database (2026-04-10)
**Decision:** Each template's design DNA (archetype, hero/navbar/footer style, density, tone, conversion pattern, font pairing, content blocks) lives as a Python dict in `apps/catalog/template_dna.py`, keyed by `WebTemplate.slug` — not as a JSONField on `TemplateBrand`.
**Rationale:** The DNA drives HTML composition files. It must be reviewed in PRs alongside the layouts it controls, version-locked to its compositions, and editable without a migration. Promoting it to the database is an option later when the vocabulary stabilises and marketing wants admin-side editing — but doing so now would couple "design intent" to "data state", which is harder to reason about.
**Trade-off:** Marketing cannot edit DNA without a developer. Acceptable for a pre-launch marketplace where every template still has bespoke design work anyway.

## D-035: Archetype-Keyed Composition Path (2026-04-10)
**Decision:** Composition files for DNA-driven templates live at `templates/preview_compositions/<category>/<archetype>.html` (e.g. `medical/clinic.html`, `medical/family.html`, `medical/wellness.html`, `medical/specialist.html`). The legacy single-file path `<category>.html` remains as a fallback.
**Rationale:** Grouping by category-then-archetype makes the file tree describe the differentiation: a glance at `templates/preview_compositions/medical/` tells you exactly which archetypes are in production for that category. The fallback path keeps the system additive.
**Trade-off:** Two files per template (DNA entry + composition file). Worth it: that's exactly the level at which a "premium template" stops being a recolor and becomes a real product.

## D-036: DNA System Is Strictly Additive (2026-04-10)
**Decision:** Adding a DNA entry never breaks an existing preview. Templates without DNA continue to render via the legacy per-category composition. Migrating a category to per-template archetypes is a slug-by-slug choice.
**Rationale:** A big-bang rewrite of all 8 categories at once would block delivery for weeks and risk regressing quality on the templates that already work. Per-template migration lets us pilot Medical, prove the model, then move to the next category with zero risk to the others.
**Trade-off:** Mixed state during the migration window — some categories use DNA, others don't. The catalog UI doesn't care; the only place that knows is `generate_previews._resolve_composition`.

## D-037: `imagery_key` Lives on the DNA, Not on the Brand (2026-04-10)
**Decision:** Each DNA entry can specify `imagery_key`, which is the lookup into `IMAGERY_CONFIG`. Without it, the generator falls back to `category.slug`.
**Rationale:** Two templates in the same category should not share the same photo set, otherwise they collapse visually even if their layouts differ. Keying imagery on DNA (not on `TemplateBrand`) keeps the imagery decision adjacent to the layout decision — they are part of the same design choice.
**Trade-off:** New imagery keys mean new entries in `IMAGERY_CONFIG`. Acceptable; the file is already the swap point per D-031.

## D-038: Custom `at` Template Filter for Image Indexing (2026-04-10)
**Decision:** `apps/catalog/templatetags/preview_extras.py` registers an `at` filter that takes a sequence and an integer (or string-of-integer, for `forloop.counter`) and returns the element, falling back to `seq[0]` on overflow.
**Rationale:** Django's stock template language cannot index a list by a loop variable — `{{ imagery|slice:i:i+1 }}` doesn't accept variables. The DNA-driven compositions need to zip a content list (e.g. specialties, doctors) with the imagery list, which requires per-iteration index lookup. A four-line custom filter is the minimal correct solution.
**Trade-off:** A new templatetag library. Tiny surface, zero risk.

## D-039: Restaurant Pilot Uses 3 Archetypes, Not 2 (2026-04-10)
**Decision:** The restaurant DNA pilot ships **three** distinct archetypes (`fine-dining`, `trattoria-warm`, `street-modern`) instead of the original "Lex/Juris-style 2 archetypes" path. To make this work, a brand-new template `brace-street-food-lab` was added to seed_templates.py.
**Rationale:** Restaurants are the most visually-loaded MVP category and the gap between fine dining and street food is much wider than the gap between two law firms. Skipping the fast-casual segment would have left a gaping hole in the marketplace's restaurant coverage. Three archetypes also stress-tests the DNA system more rigorously than two before we roll out to the next category.
**Trade-off:** One more seed template (19 total now, was 18) and one more imagery pool (`restaurant-street`) to maintain. Worth it for category coverage.

## D-040: Fonts Selected for Multi-Weight Google Fonts Compatibility (2026-04-10)
**Decision:** The 3 restaurant archetypes use `Playfair Display + Lato`, `Caveat + Inter`, and `Big Shoulders Display + Inter` respectively — all multi-weight Google Fonts. Anton, Bebas Neue, and Archivo Black were rejected for the street-modern archetype because they only ship at a single weight, and `_base.html` requests `wght@500;600;700;800` for the heading family — a request that returns HTTP 400 from Google Fonts CSS2 when none of the requested weights exist.
**Rationale:** Big Shoulders Display has wght 100→900 (industrial condensed look, perfect for street-food brutalism) and matches all the requested weights. Caveat (heading for trattoria-warm) has 400/500/600/700 — covers most of the request. Playfair Display has the full 400→900 range. The base font request URL is currently fixed at compile time — until/unless the generator is taught to negotiate per-font weight lists, only multi-weight families are safe.
**Trade-off:** A future archetype that wants Anton or Bebas Neue specifically will need either (a) the generator to accept per-DNA weight lists or (b) the composition to bypass the base CSS variable and load its own font tag. Acceptable for now.

## D-041: Per-Archetype Imagery Keys Use Fully-Distinct URL Sets for Restaurants (2026-04-10)
**Decision:** Unlike `medical-family` / `medical-specialist` / `medical-wellness` (which mostly recycled photos from neighbouring categories to stay offline-safe), the three restaurant pools — `restaurant-fine`, `restaurant-trattoria`, `restaurant-street` — use fully-distinct URL sets. `restaurant-street` introduces 6 brand-new burger/pizza/street-food URLs that no other pool uses; `restaurant-fine` and `restaurant-trattoria` each pick a different hero photo and shuffle the remaining slots so the visual signature is genuinely different.
**Rationale:** The whole point of the DNA pilot is to prevent sibling templates from collapsing into recolors. Sharing photos between fine dining and street food would have undermined the differentiation. Restaurants are also the category where photo content matters most to a buyer's perceived value.
**Trade-off:** First-run download is heavier (6 brand-new URLs to fetch). One URL (`photo-1606755962773-d324e6f8e2c2`) returned HTTP 404 from Unsplash and was replaced with `photo-1601050690597-df0568f70950` on the second pass. Future imagery configs should be re-validated whenever Unsplash photo IDs are added.

## D-042: Live Multi-Page Template Content as a Code-Driven Registry (2026-04-10)
**Decision:** Inner-page content for full multi-page templates lives as Python dicts in `apps/catalog/template_content.py`, keyed by `WebTemplate.slug`, not in a `TemplatePage` model.
**Rationale:** During the pilot phase the inner-page authoring loop is "design + write + test" and changes hourly. A model-backed approach would force a migration/seed cycle for every copy tweak and would couple text changes to data state. Code-driven content lets the editorial work happen alongside the template files that consume it (the `live_templates/<category>/<archetype>/*.html`), reviewed in PRs, and version-locked. The structure of the data (lists of doctors, courses, blog posts with body blocks, opening hours tables) is also not flat — Python tuples/dicts are easier to author than JSON in a Django admin form.
**Trade-off:** Marketing cannot edit content without a developer. Customers cannot edit content yet either. Both are intentionally deferred to a later phase: the next iteration will introduce a `TemplatePage` model and seed it from this registry.

## D-043: Per-Archetype Standalone Skins Under `templates/live_templates/` (2026-04-10)
**Decision:** Each archetype gets its own `_base.html` at `templates/live_templates/<category>/<archetype>/_base.html` that is a *complete standalone HTML document*. It does NOT extend the marketplace `base.html`. The marketplace navbar/footer never appear on a live preview page.
**Rationale:** A live template preview is the *product*, not a marketplace surface. The buyer is judging "would this look good for my clinic?" — and the answer is corrupted the moment a MarketWeb logo, navbar, or footer renders next to it. Standalone skins also let each archetype load its own Google Fonts pairing, its own brutalist-or-editorial CSS conventions, and use its own naming prefix (`sp-*` for specialist, `fd-*` for fine-dining) without colliding with marketplace classes. A tiny "Torna a MarketWeb" bar at the very top is the only piece of marketplace chrome — barely bigger than a browser bookmark bar.
**Trade-off:** The marketplace base CSS does not propagate to previews, so each skin must load Google Fonts itself and define its own design tokens. Acceptable: the design tokens come from the brand palette via context, and the Google Fonts URL is built from the DNA `font_pairing`.

## D-044: `LiveTemplateView` Resolves DNA + Content in `setup()`, Not `get_template_names()` (2026-04-10)
**Decision:** All WebTemplate / DNA / content resolution for the live preview view happens in `setup()`, not in `get_template_names()` or `get_context_data()`.
**Rationale:** Django's `TemplateView.get()` calls `get_context_data()` BEFORE `get_template_names()`. Doing resolution in `get_template_names()` (the natural-feeling place) means `self.template_obj` does not exist yet when the context builder needs it, which raises `AttributeError`. `setup()` is called by Django's base view *before* `get`/`post`/etc. dispatch, so it is the only place where state can be assigned safely for both `get_template_names()` and `get_context_data()` to read.
**Trade-off:** None. `setup()` is the documented Django extension point for exactly this case.

## D-045: Live-Preview CTA Is Conditional on Content Registry Presence (2026-04-10) — **SUPERSEDED by D-055 + D-056 in Session 21 (2026-04-11)**
**Decision:** The marketplace template detail page CTA is conditional: when `template_content.has_live_template(template.slug)` is true, the button reads "Apri anteprima completa" and links to `live_template_home`; otherwise it falls back to the legacy "Anteprima Live" button at `href="#"`.
**Rationale:** The live-preview system is strictly opt-in per template. Templates without DNA + content registry entries get exactly the same detail-page experience they had before this phase — no broken links, no 404s, no ghost CTAs. This lets the rollout happen template-by-template without the rest of the catalog changing behaviour.
**Trade-off:** Two CTA states to maintain in `template_detail.html`. Trivial: it's a single `{% if %}` block.
**Superseded:** D-055 makes the draft tier invisible to the public catalog, so no detail page ever needs the fallback CTA branch any more. D-056 deletes the branch itself. Implemented in Session 21's Phase 2g2x.8 tier migration: `has_live_preview` context var removed from `TemplateDetailView`, the fallback `{% else %}` branch removed from `template_detail.html`, the "Apri anteprima completa" CTA is now unconditional.

## D-046: Archetype Reuse Validated — Dermatologia Under Specialist Ships With Zero New HTML (2026-04-10)
**Decision:** A second template, `dermatologia-elite-roma`, was added under the `specialist` archetype using ONLY three edits: (1) a new row in `seed_templates.py`, (2) a new DNA entry in `template_dna.py`, and (3) a new content block in `template_content.py`. No HTML files were created or modified. All 9 routes (marketplace detail + 7 inner preview pages + 1 post detail) return 200. The specialist skin correctly renders the new template's brand palette (cream / charcoal / forest green #3d5437 instead of cardio red), Bodoni Moda font pairing, and dermatology-specific content (Studio Ricciardi, Via Veneto, 2.400 mappature, three dermatologhe, JAMA Dermatology press list, etc.).
**Rationale:** The point of the Session 11 architecture (content registry + per-archetype skin folder + single dispatcher view) was specifically to enable this — adding a new multi-page template becomes a matter of editorial authoring, not chrome rebuilding. This validation confirms the structural hypothesis: the `LiveTemplateView` resolves DNA + content correctly, the Google Fonts URL is built per-DNA, the brand palette is injected via context, the nav loop iterates the content registry, and the inner-page templates all consume `page_data.*` / `site.*` / `posts` uniformly.
**Trade-off:** The validation **also revealed a copy-abstraction leak** — the specialist chrome HTML files bake in cardio-specific text in places the content registry cannot override: the hero-right column quote ("«La cardiologia non è una catena di montaggio...»" + "Lancet · 2024"), the pulse band ("Roma · Parioli / 2010 / Cardiologia clinica"), several section headings ("Una sola firma per ogni cartella", "Vuoi conoscere i medici dello studio prima di prenotare?"), the services CTA heading ("Una visita allo Studio Marani è concordata personalmente" — literal brand name), the team portrait signature ("Roma · Parioli"), the blog_detail footer ("Studio Marani · Cardiologia clinica"), and the `_base.html` footer license ("OMCeO Roma 12 / 4408"). The blog parent slug is also hardcoded as `pubblicazioni` in URL reverses. All of these appeared on the dermatologia pages during the validation test-client sweep. The next template under this archetype — or ANY third archetype-reuse test — will show the same cardio-specific strings mixed into its own brand voice, which breaks the premium illusion.
**Consequence:** A **Phase 2g.2 copy-abstraction pass** is now the blocking prerequisite before more archetype-reuse templates ship. Three fixable classes: (a) move site-wide fixed strings like the footer license into `site.*` content registry fields (`site.license`, `site.footer_bottom`), (b) move section-CTA headings from the HTML into per-page content blocks (every page can have a `cta_heading` / `cta_note` pair), (c) move the hero quote, author, pulse triple, and portrait signature from HTML into the `home.hero_sidebar` sub-block and the `medici.portrait_city` field. The URL reverse for the blog parent slug should resolve from the content registry's `pages` list (find the entry where `kind == 'blog_list'`) instead of hard-coding `pubblicazioni`. None of these require new HTML files — just moving literals out of the template files into the registry.

## D-047: Chrome-Authoring Contract — No Literal Brand Strings in Per-Archetype Skins (2026-04-11)
**Decision:** Every string in a per-archetype skin (any file under `templates/live_templates/<category>/<archetype>/`) must satisfy exactly one of four criteria: (a) it is a CSS rule (tokens, colors, fonts, layout); (b) it is a generic archetype label (`Nome`, `Email`, `Privacy`, `Invia messaggio`, `Leggi l'articolo completo`, `min di lettura`, `© 2026`, etc. — strings that apply identically to every template that could possibly use this archetype); (c) it is rendered from a template context variable (`{{ site.* }}`, `{{ page_data.* }}`, `{{ d.* }}`, `{{ post.* }}`, `{{ blog_parent_slug }}`); (d) it is emitted from a `{% for %}` loop over a content registry list. **No literal brand names. No literal city names. No literal quotes. No literal CTA headings. No literal form select options. No hardcoded image URLs.** This contract is a chrome-authoring precondition, enforced by a post-authoring grep for the previous template's brand name + district/city + chief person name against the rendered HTML of a second template ("the leak sweep").
**Rationale:** Session 13 added `dermatologia-elite-roma` under the specialist archetype expecting zero copy polish and discovered 17 distinct cardio-specific leaks in the chrome HTML — every single dermatology page showed cardio's chief name in the hero sidebar, cardio's quote from Lancet, cardio's Parioli district in every doctor portrait, "Studio Marani" hardcoded in the services CTA heading, and three cardio doctor photos instead of the dermatology team. Session 14's Phase 2g.2 pass fixed all of them — but the fix only worked because the leaks were small. A chrome authored today under this contract never needs a follow-up lift pass.
**Trade-off:** Authoring a brand-new archetype becomes slightly slower because every textual element has to be traced back to a content registry field from the first commit. Two ways to discipline this during authoring: (1) start the content block and the HTML file in the same commit and only use `{{ page_data.X }}` in HTML — never paste a literal string directly, even as a placeholder; (2) run the leak sweep against a throwaway second content block before declaring the chrome done, to catch any missed literal. In exchange for slower authoring, the archetype becomes infinitely reusable with zero polish work — the payback is after the second template, which is when reuse starts mattering.
**Consequence:** Any new archetype added in Phase 2f going forward (Agency, Lawyer, Real Estate) must apply this contract from the first authoring pass. The next chrome to refactor under this contract is `templates/live_templates/restaurant/fine-dining/` — Session 14's leak sweep only covered the specialist chrome; fine-dining almost certainly has the same class of leaks and should get its own lift pass before a second fine-dining template ships.

## D-052: Chiara Headline Trimmed To 2-Line Wrap — Surgical Fix After Triage (2026-04-11, Session 19)
**Decision:** In `editorial-designer-grid.html` the `.ed-hero` h1 font-size is reduced from 82 px to 62 px, surrounding margins and padding are tightened (details in SESSION_LOG Session 19), and `overflow: hidden` is added to the hero as a hard cap. In `template_dna.py` the `chiara-portfolio-creativo.content.headline` is trimmed from `'Sistemi di <em>identità visiva</em> costruiti una griglia alla volta.'` (57 chars) to `'Identità visive, <em>una griglia alla volta</em>.'` (47 chars). No other files are changed. Pixel is not touched.
**Rationale:** Session 18 declared portfolio approved, but a Session 19 triage found a real, reproducible layout overflow bug in Chiara's preview: at the original 82 px display size with 760 px max-width, the 57-char headline wrapped to 5 lines and the content stack (eyebrow + h1 + sub + cta-row + margins = ~640 px) was way larger than the `.ed-hero` inner vertical budget (376 px). The overflow bled ~260 px into the `.ed-ledger` section below, visually colliding the CTA row + filter pills + ledger intro heading. CSS-only changes could reduce the damage but not fully clear the `.meta-strip` absolute-positioned at the hero bottom — at 62 px × 4 lines the content stack still landed at canvas y 553, overlapping the meta-strip at y 495-550. The minimum fix that eliminates all overlap while preserving Chiara's DNA (typographic-led, editorial, dramatic display, no hero photo) was **one CSS knob group + one small copy trim**. The copy trim preserves both key signals (`identità visive` = profession, `una griglia alla volta` = craft metaphor) and as a deliberate side effect now mirrors Pixel's `'Fermare il tempo, una luce alla volta.'` syntactic rhythm — both siblings use the same `'…, una X alla volta.'` structure with X being the medium of each profession (griglia for designer, luce for photographer). This sharpens rather than weakens the intentional contrast laid out in D-051.
**Trade-off:** The Chiara display is now slightly less dramatic at absolute pixel count (62 px vs 82 px, still a large editorial display) and the headline is 10 characters shorter. Both are minor compared to shipping a visually broken preview as the face of a premium-marketplace card. `overflow: hidden` on `.ed-hero` is a hard cap that will also protect against future DNA copy changes growing the content stack past the budget — it's a safety net, not a substitute for the layout math.
**Consequence:** Portfolio Phase 2g2x.1 is now commit-ready. Session 19 also uncovered two systemic operational issues worth tracking but intentionally NOT fixed in this session: (a) the "Anteprima Live" button on detail pages is a legacy `href="#"` placeholder for all 17 preview-only templates — a separate UX micro-phase, not portfolio-scope, see TODO_NEXT.md; (b) `generate_previews --force` creates orphan files on disk because `FileSystemStorage.get_available_name()` appends a hash suffix when the target filename exists — this is the already-tracked Phase 2g2x.5 `dna_signature` trap, now with one more concrete repro. Session 19 cleaned up its own orphans manually (shell-script rename + DB row update); a permanent fix still needs to land in Phase 2g2x.5.

## D-051: Portfolio Category Gets Option A (DNA Split) — Editorial-Designer vs Cinematic-Photographer (2026-04-11, Session 18)
**Decision:** For the Phase 2g2x portfolio hardening wave, Chiara and Pixel are split into **two distinct DNA archetypes** (`editorial-designer-grid` and `cinematic-photographer`) with their own preview compositions under `templates/preview_compositions/portfolio/<archetype>.html`, their own imagery pools (`portfolio-designer`, `portfolio-photographer`), and their own font pairings, tones, conversion patterns, and section orders. The legacy `templates/preview_compositions/portfolio.html` and the legacy `portfolio` imagery pool are untouched and remain in place per D-036 (DNA system is strictly additive), but no published portfolio template renders through them anymore.
**Rationale:** Chiara (independent designer / art direction / visual identity / editorial studio) and Pixel (photographer / visual storyteller / cinematic portfolio) are semantically as far apart as Pragma/Elevate were in D-050 — they belong to two completely different professions with opposite relationships to the dominant visual. A designer's portfolio is the *work* (identity systems, book covers, typography, grids) — the dominant visual is often typographic, not photographic. A photographer's portfolio IS the photographs — the dominant visual must be a big image. Forcing them into one shared composition would (a) erase the profession difference (if the composition is designer-first, Pixel collapses into a recolor of Chiara), (b) make the composition photo-dependent at the hero level (if the composition is photographer-first, Chiara becomes a typography-less card), or (c) produce a conditional-branching frankenfile with `{% if dna.content.is_photographer %}` blocks around most of the body. None of these is acceptable. Option A is the same recipe that already worked for medical/restaurant/ecommerce/business. **The editorial-designer-grid archetype is deliberately typographic (no big hero photo) so that the Chiara card doesn't depend on any single image — a failing image URL degrades to an empty slot without breaking the card's readability.** The cinematic-photographer archetype is deliberately image-first — the hero IS the photograph — but every string is still D-047 compliant (nothing hardcoded in the HTML, everything flows from `dna.content.*`).
**Trade-off:** One extra HTML composition file compared to Option B (2 vs 1). One extra imagery pool. One extra entry in every vocabulary dict in `template_dna.py`. All acceptable — same linear cost as D-050 and the DNA system was designed for exactly this kind of additive growth.
**Consequence:** Session 18 closed the portfolio identity-crash case with both skins authored under the D-047 chrome-authoring contract from the first line — zero literal brand strings, zero hardcoded Unsplash URLs, zero cross-tenant leaks in the bidirectional leak sweep (52 tokens tested across both directions), zero legacy-literal leaks in the listing HTML. No follow-up lift pass will be needed for this pair. **D-050 is reaffirmed:** default to Option A (DNA split) for every pair whose tenants are semantically far apart — portfolio is the second concrete validation of that rule after business. The 3 remaining non-DNA CRITICO categories (real-estate, lawyer, agency) all have "far apart" sibling pairs (mass-market/ultra-luxury, classic-gold/modern-transparent, bold-grid/editorial-quiet) per CATEGORY_ROADMAP.md — Option A is the default for all of them.

## D-050: Business Category Gets Option A (DNA Split), Not Option B (Lifted Shared Comp) (2026-04-11, Session 17)
**Decision:** For the Phase 2g2x business hardening wave, Pragma and Elevate are split into **two distinct DNA archetypes** (`corporate-suite` and `startup-saas-landing`) with their own preview compositions under `templates/preview_compositions/business/<archetype>.html`, their own imagery pools (`business-corporate`, `business-startup`), and their own font pairings, tones, conversion patterns, and section orders. The legacy `templates/preview_compositions/business.html` and the legacy `business` imagery pool are untouched and remain in place per D-036 (DNA system is strictly additive), but no published business template renders through them anymore.
**Rationale:** The Session 16 audit identified two remediation paths for each of the 5 non-DNA identity-crash categories: (A) split into 2 distinct archetypes, (B) lift the existing legacy composition to D-047 compliance with per-tenant content blocks. Option B is cheaper when the two tenants are semantically close (similar product positioning, similar silhouette, similar CTA pattern). Business is the exact opposite — Pragma (board advisory for PMI, institutional mood, consulting CTAs, boardroom photo direction) and Elevate (SaaS landing page kit, conversion-first, typographic + product-mockup, free-trial CTA) are at opposite ends of the B2B spectrum. Forcing them into one shared skin would either (a) erase their positioning difference (making them a recolor pair, exactly the failure mode we're trying to prevent), or (b) produce a conditional-branching frankenfile with most of the template body inside `{% if dna.content.is_startup %}` blocks that only appears to share structure. Neither is acceptable. Option A is the same recipe that medical (4 archetypes), restaurant (3), and ecommerce (2) already followed successfully — business simply joins the DNA-driven majority.
**Trade-off:** One extra HTML composition file compared to Option B (2 vs 1). One extra imagery pool. One extra entry in every vocabulary dict in `template_dna.py`. All acceptable — the DNA system was designed for exactly this kind of additive growth, and the architecture cost is linear in the number of archetypes, not in the number of templates per archetype.
**Consequence:** Session 17 closed the business identity-crash case with both skins authored under the D-047 chrome-authoring contract from the first line — zero literal brand strings, zero hardcoded Unsplash URLs, zero cross-tenant leaks in the leak sweep. No follow-up lift pass will be needed for this pair. This sets the precedent for the remaining 4 non-DNA CRITICO categories in Phase 2g2x.1 (agency, lawyer, real-estate, portfolio): **default to Option A (DNA split) for every pair whose tenants are semantically far apart**, and reserve Option B for the rare close-pair case. The CATEGORY_ROADMAP.md archetype suggestions for those 4 categories (bold-grid/editorial-quiet, classic-gold/modern-transparent, mass-market/ultra-luxury, editorial-designer/cinematic-photographer) are all "far apart" pairs by the same yardstick — Option A is the default for all of them.

## D-049: Catalog Hardening Wave (Phase 2g2x) Is Blocking (2026-04-11, Session 16)
**Decision:** No new feature work (auth, checkout, editor, projects, commerce, dashboard, new categories, new templates, new archetypes) may start until Phase 2g2x closes. Phase 2g2x = the catalog differentiation hardening wave: (1) DNA-ify or D-047-lift the 5 non-DNA categories (agency/business/lawyer/real-estate/portfolio); (2) sibling-split the 5 legacy imagery pools so no two siblings share 6/6 URLs; (3) lift latent D-047 violations in single-tenant archetype files (ecommerce fashion-editorial + artisan-workshop, restaurant trattoria-warm + street-modern, medical clinic + family + wellness preview comps, restaurant/fine-dining live skins); (4) decide whether single-page-only templates (15 of 20) stay published or get demoted to `draft` until inner-page content exists; (5) ship the stale-PNG structural fix (TemplateAsset DNA-signature hashing). The roadmap is paused — no "we'll fix it later" exceptions.
**Rationale:** The Session 16 audit found that 10 of 20 templates have no DNA and render via 5 legacy per-category compositions that hardcode literal brand strings from ONE tenant, so the sibling renders WRONG copy — not just a recolor, an identity crash. Examples: `business.html` hardcodes `"Hanno scelto Pragma"` label on Elevate's card; `portfolio.html` hardcodes `"Sono una designer indipendente"` on Pixel's photographer card; `real-estate.html` hardcodes "600+ immobili · €500K–€1.2M mass-market" on Villa's ultra-luxury card; `lawyer.html` hardcodes "Studio legale dal 1962" (Lex's 60-year heritage) on Juris (modern/accessible); `agency.html` hardcodes 6 fake case studies (Lumen, Vega, Atelier Norma, Helios Bank, Cinetic, Polar Studios) that appear on both Vertex and Aura. Additionally, 4 single-tenant DNA archetype files have 10+ latent literal leaks each that will detonate the moment Phase 2f.2 adds a second tenant. Shipping any customer-facing feature on top of a catalog whose cards show wrong copy is not acceptable for a "premium marketplace" positioning.
**Trade-off:** Roadmap velocity paused until the hardening wave closes. But the alternative — shipping auth/checkout on a catalog that is not credible — would force a cosmetic fix cycle during customer onboarding, which is worse. This is the same class of decision as D-002 (custom User model from day one): pay the pain now or pay it much bigger later.
**Consequence:** `TODO_NEXT.md` Phase 2g2x is the only active wave. `AGENT_HANDOFF.md` blocks all roadmap resumption until the wave closes. `MEMORY.md` auto-memory `catalog_differentiation_audit.md` tracks the blocker externally. The audit found structural problems with 7 of 8 categories in some form (only street-modern restaurant composition is completely clean); 5 categories are CRITICO severity, 3 categories are MEDIO severity, zero are clean.

## D-048: `blog_parent_slug` Resolved in View, Not Hardcoded in HTML (2026-04-11)
**Decision:** `LiveTemplateView.get_context_data()` computes `blog_parent_slug` by scanning `self.content["pages"]` for the first entry whose `kind == 'blog_list'` and injecting it into the template context. Both `blog_list.html` and `blog_detail.html` consume `{{ blog_parent_slug }}` in every `{% url 'catalog:live_template_page' ... %}` / `{% url 'catalog:live_template_post' ... %}` reverse instead of hardcoding a per-template slug like `'pubblicazioni'`.
**Rationale:** Session 11/13 discovered that the specialist chrome hardcoded the literal string `'pubblicazioni'` in five URL reverses across `blog_list.html` (lines 95, 98, 109) and `blog_detail.html` (lines 85, 121). This meant that any future template reusing the specialist archetype was forced to call its blog parent page `pubblicazioni` — even if the content was better served by `diario`, `rassegna`, `osservatorio`, `approfondimenti`, etc. — or it would 404 with a `NoReverseMatch`. This was the single hardest constraint on archetype reuse and the source of the most inflexible editorial rule in the system. Computing the slug once per render from the `pages` list removes that constraint entirely. The content registry can now name the blog page anything it wants; the chrome figures out the URL at render time.
**Trade-off:** An `O(pages)` lookup per render (typically 7 entries). Invisible. The alternative — stashing the slug on the content block (`"blog_parent_slug": "pubblicazioni"`) — would require content authors to remember to set a field that's entirely derivable from data they already author, which is brittle in exactly the way this bug already was.
**Consequence:** D-044's hard constraint "the blog parent page slug must be literally `pubblicazioni`" is lifted as of Session 14. Future templates under the specialist chrome can name their blog page freely. Dermatologia keeps using `pubblicazioni` only because its content was already authored that way — the chrome no longer cares.
**Key insight:** The validation succeeded structurally (routes, chrome, fonts, palette, nav, data loops) but the success exposed that the specialist chrome was written as if cardio would be its only user. The abstraction is sound; the implementation isn't fully done. See TODO_NEXT.md Phase 2g.2 for the detailed lift plan.

## D-053: Live Preview Law — Every Published Template Must Be A Real Navigable Multi-Page Website (2026-04-11, Session 20)
**Decision:** A template may only be exposed to end users (listing, category page, homepage featured, detail page, search result) when it has a **real, navigable, multi-page live preview**. This is the binding definition of "published" going forward. A published template must satisfy ALL of the following gates before it is allowed in any public surface:
1. DNA entry in `apps/catalog/template_dna.py` (archetype + hero/navbar/footer style + section order + CTA pattern + imagery_key + font_pairing + full content block)
2. Content registry entry in `apps/catalog/template_content.py` (all inner-page content blocks, not just `home`)
3. Per-archetype skin folder at `templates/live_templates/<category>/<archetype>/` containing every page kind the content block references (reused or newly authored — both count)
4. Every route in `live_pages` returns HTTP 200 via a Django test-client sweep (marketplace detail + `live_template_home` + every `live_template_page` + at least one `live_template_post` where blog exists)
5. The per-archetype composition file AND the per-archetype skin are D-047 compliant — a bidirectional leak sweep against every other template using the same archetype returns **zero** cross-tenant brand strings, city names, quotes, proper names, or image URLs
6. The category baseline page set (per CATEGORY_ROADMAP.md "Baseline live pages per category") is fully covered — no shortcut where only `home` exists
7. A Chromium visual walk at 1440×900 of the live preview's home + every inner page confirms the brand chrome (palette, fonts, imagery direction, macro tone) is internally consistent
8. Listing thumbnail (1600×900 preview PNG from `generate_previews`) is generated from the per-template/per-archetype composition, not a legacy shared composition, and passes the "two different products at card size" sibling test (D-054)
9. The "Apri anteprima completa" CTA on the detail page is active and links to the real `live_template_home` route (no `href="#"` placeholder)

**Rationale:** marketweb is positioned as a *premium marketplace for complete customizable websites*, not as a gallery of posters. Session 16's audit revealed that 17 of 20 templates shipped as single-page preview PNGs only — 85% of the catalog was misrepresented as "complete multipage websites" when it delivered a single landing page. Session 19's triage additionally surfaced that the detail-page CTA for those 17 templates was a legacy `href="#"` ghost button labelled "Anteprima Live" — a click that resolved to nothing. Both facts are fatal to the product's premium positioning, and neither can be papered over with copy tweaks: a buyer clicking "see the full website" must actually see the full website. The Live Preview Law is the product-level answer to "what does 'published' mean here?" and aligns every downstream rule (tier model D-055, catalog honesty D-056, rollout plan TODO_NEXT Phase 2g3) to that single source of truth.
**Trade-off:** The marketplace's *visible* template count drops from 20 to 3 the day this rule is enforced (only cardio, dermatologia-elite-roma, and gusto-fine-dining satisfy the full gate today). The other 17 templates become `draft` until they're brought up to spec. Acceptable: three genuinely complete premium products will convert better than twenty landing-page posters. The alternative — keeping the 17 preview-only templates published behind a softer gate — directly contradicts the founding premise of the product and is rejected.
**Consequence:** (a) Phase 2g3 rollout plan in TODO_NEXT.md becomes the only active wave after Phase 2g2x closes; (b) no auth/checkout/editor/projects/commerce work is allowed to start before the category completeness bar is met for enough templates to make a marketplace credible — the initial gate is 8 `published_live` templates across at least 4 categories, which is a roughly 5x increase over today's 3; (c) tier model D-055 codifies the two-tier `published_live` / `draft` split and the demotion of the 17 preview-only templates; (d) catalog honesty D-056 deletes the legacy `href="#"` CTA once tier gating is in place. This decision **extends and absorbs** Session 11's "completeness-ready" definition (CATEGORY_ROADMAP.md) and makes it binding for every future template — there is no "preview-ready" tier anymore, only "published_live" or "draft".

## D-054: Premium Differentiation Law — Global Cross-Category Differentiation Standard (2026-04-11, Session 20)
**Decision:** Every sibling pair within the same category must pass the following 10-gate differentiation test. This applies globally — not only to categories that have already gone through DNA hardening (medical / restaurant / ecommerce / business / portfolio), but also to every future template, every future category, and every follow-up polish pass. Two templates in the same category must differ in AT LEAST the following dimensions:
1. **Hero image** — different URL, not a crop/variant of the same source; not even a "similar" shot from the same photo session. A shared archetype is fine; shared hero photos are not.
2. **Dominant imagery in the first two sections** — the photographs driving the hero + the section immediately below must come from disjoint pools, not just reordered (see D-041 lesson: 5/6 overlap with a different hero still reads as identical).
3. **Silhouette** — the first-scroll block shape (photo-left-text-right, typographic-full-width, fullbleed-with-overlay, split-booking-widget, editorial-plate, product-cutout, typographic-index-ledger, fullbleed-exif, etc.) must differ. A different palette on the same silhouette is NOT differentiation.
4. **Section order** — the sequence of section kinds (hero → proof → services → team → CTA vs hero → manifesto → case-studies → contact) must differ where the category admits it. Reusing the same section order with different copy counts as "same skeleton, different paint" and is rejected.
5. **Primary CTA** — both the phrasing ("Fissa una call privata" vs "Inizia gratis") AND the interaction pattern (booking widget vs phone+WhatsApp vs calendar spot vs case-study request vs series brief vs order-now-delivery) must differ.
6. **Block rhythm** — density (compact / medium / airy / very-airy) and section-to-section padding cadence must differ — two very-airy sibling templates need a different counter-balance (e.g. one breathes on editorial type, the other on big photos).
7. **Macro tone** — page-level mood must differ. Cream vs dark, light vs black, warm vs cool, institutional vs editorial, industrial vs serene. This is the cheapest differentiator and the one most often skipped — no excuse to ever skip it.
8. **Imagery direction** — the photo brief (what the pictures are OF) must differ. Boardroom executives ≠ young SaaS founders ≠ plated tasting-menu dishes ≠ rustic trattoria dishes, even if both "feel premium". Articulate the direction in the DNA `imagery_direction` field before authoring.
9. **Typography / font pairing** — heading + body pairing must differ. Same palette + same silhouette + different fonts is still not enough, but same fonts is definitely not enough.
10. **Inner pages** — the differentiation rule extends to about, services, contact, team, blog list, blog detail, gallery, menu, reservations, property listing, project detail, product detail, case-study detail, and any other page kind the category demands (see D-053 baseline page set and CONTENT_GUIDELINES.md Inner Pages Law). A sibling pair that differs on the home page but clones each other on `/about` is NOT differentiated — it's a card-size illusion that collapses on the first click.

**Rationale:** D-047 (Chrome-Authoring Contract) solved the text-leak problem — literals no longer bleed from template to template. But D-047 is necessary, not sufficient. Even with zero literal leaks, two templates can still be identical skeletons painted in different colours — a "recolor pair" whose failure mode is cosmetic rather than factual. A premium marketplace cannot ship recolor pairs any more than it can ship wrong-brand copy. Session 17 (business), Session 18 (portfolio), and Sessions 7/9/15 (medical/restaurant/ecommerce) all validated Option A (DNA split) per D-050 and D-051, which is precisely the architectural shape that enables this 10-gate test — **but the gates need to be written down** so every future authoring pass applies them from the first line. This decision turns the Session 18 "choose which sibling is typographic-led vs image-led BEFORE authoring" insight into a formal rule, and makes it cross-category.
**Trade-off:** Authoring a new sibling under this law costs 10 explicit design decisions up front, before the first line of HTML. Slower than recolor-and-ship. Acceptable: every sibling authored this way ships as a genuinely distinct product and needs no follow-up lift pass. The Session 17/18 recipe already runs 10 decisions through this test implicitly — the only new cost is writing them down in the DNA comment block so reviewers can check them. Two ways to enforce: (a) a "differentiation gate" section in the per-category hardening PR description listing the 10 dimensions with the chosen value on each side, (b) a grep/sweep script that diffs two DNA entries in the same category and fails if fewer than 7 of 10 dimensions differ.
**Consequence:** (a) every new template authoring pass must declare its stance on all 10 gates in the DNA entry comment before the composition file is written; (b) every new category hardening session must pass the 10-gate sibling test as an exit criterion in addition to the D-047 leak sweep; (c) the Phase 2g3 rollout plan uses this law as the per-template acceptance checklist alongside the Live Preview Law (D-053); (d) BRAND_SYSTEM_GUIDELINES.md gets a new "Premium Differentiation Law" pointer section; (e) when the law is later violated in any category, the remediation is a new archetype split per D-050/D-051, not a recolor patch. **This law is not optional and applies retroactively:** any existing sibling pair that fails ≥4 of the 10 gates is treated as a Phase 2g3 blocker for that category.

## D-055: Template Tier Model — Binary `published_live` / `draft`, No Intermediate `published_static` (2026-04-11, Session 20)
**Decision:** Templates have exactly two tiers: `published_live` (meets the full D-053 Live Preview Law gate) and `draft` (does not). The `status` field on `WebTemplate` is repurposed to carry this tier (or a new `tier` field is added in the implementation session — naming deferred to the migration PR). No intermediate `published_static` tier exists. The `draft` tier is **fully hidden from all public surfaces**: listing pages filter it out, category pages don't include it, homepage featured pools don't include it, search doesn't return it, and the detail page either 404s or shows an explicit "template non ancora pubblicato — staff only" banner reachable only via admin. Staff retain access via an `?preview=1` query param OR the Django admin's object-edit page OR a `/admin/catalog/preview/<slug>/` staff-only route. Preview PNGs for `draft` templates continue to be generated and stored so nothing regresses on the art side; they're just not publicly linked.

**Rationale:** The user's explicit product directive — "non sono più accettabili template published preview-only" — makes the intermediate tier a non-option. A `published_static` label on a card communicates "incomplete product" to a shopper, which is strictly worse than a shorter catalog: the premium positioning is eroded *on every listing view* for every shopper, not just the one who clicks through to a specific template. A two-tier model keeps the floor premium and removes the temptation to ship "good enough" previews by giving them a second-class home. The option space was evaluated in full:
- **Option A — hide preview-only templates entirely (tier = draft):** catalog shows only 3 templates today but every one is a real product. Shoppers see a smaller, cleaner gallery. Trust floor preserved. Selected.
- **Option B — keep them published with a "Anteprima statica" badge + disabled CTA:** rejected. The badge is a public admission of incompleteness on 85% of the catalog and turns every card into an explanation of what the shopper is NOT getting. Also the disabled CTA still communicates "there's a thing you can't do here", which is a worse signal than the thing not existing at all.
- **Option C — keep them published + route-level 404 on the preview:** rejected. A 404 after click is a broken product, not a soft gate. Harder to debug than Option A, no better shopper-facing outcome.
- **Option D — keep them published but rewrite the detail-page CTA to open the preview PNG in a lightbox:** rejected as user-facing solution. Acceptable only as a transitional mechanism *inside* `draft`-hidden staff-only preview flows for internal review. Not a customer path.

Option A wins because it is the only one that keeps the floor at "every card is a real product" without requiring the shopper to learn the marketplace's internal tiering vocabulary.
**Trade-off:** Immediate catalog shrinkage from 20 to 3 visible templates. Homepage featured grid has only 3 slots filled until Phase 2g3 brings more up to spec. Category listing pages for agency / lawyer / real-estate / portfolio / ecommerce / business (once Phase 2g2x.1 closes) will all show "0 templates" initially. Mitigations at the implementation layer: (a) homepage copy can frame this as "curated launch — new templates landing weekly" without apologising for it, (b) category pages for empty categories can show a category-specific "in arrivo" strip with no ghost CTAs and no preview thumbnails, (c) Phase 2g3 ships templates in short bursts (2–3 per week at sustainable pace) so the visible count grows steadily. None of these mitigations ever dilute Option A by adding a second-class tier in the meantime.
**Consequence:** (a) `seed_templates.py` gets a `tier` keyword on each row (default `draft`) and only cardio/derm/gusto ship with `tier=published_live`; (b) `TemplateListView` / `TemplateDetailView` / `selectors.py` filter to `tier=published_live` for public-facing calls; (c) the catalog differentiation audit (MEMORY.md `catalog_differentiation_audit.md`) becomes a per-template readiness checklist keyed on the tier field; (d) `TEMPLATE_REGISTRY.json` gets a `tier` key on each template entry (annotation only — the registry is a mirror, not the source of truth — but it lets the next agent see the tier without reading the seed); (e) D-056 (below) deletes the legacy `href="#"` CTA because the tier gating makes it unnecessary; (f) the Session 11 "completeness-ready" concept is retired in favour of `tier=published_live`.

## D-056: Catalog Honesty — Delete the Legacy `href="#"` "Anteprima Live" Ghost CTA (2026-04-11, Session 20)
**Decision:** The `{% else %} <a href="#">Anteprima Live</a>` branch in `templates/catalog/template_detail.html` (lines 132-136) is deleted. The detail page's "Apri anteprima completa" CTA becomes unconditional — it always links to `live_template_home` because every template visible on a detail page is `published_live` and therefore has a real live preview. The conditional `{% if has_live_preview %}` block is removed entirely along with the `has_live_preview` context variable in `TemplateDetailView`. This supersedes the Phase 2g2x.7 three-option punch list (disabled button / lightbox / hide) because tier gating per D-055 makes the legacy branch architecturally unreachable — any template that would have hit it is now `draft` and its detail page is not publicly reachable.

**Rationale:** D-045 originally introduced the conditional CTA as a gentle rollout gate during the Phase 2g pilot — "templates without live previews get exactly the same detail-page experience they had before this phase". That was the right call at the time (Session 11, with one live template). It no longer is (Session 20, with 17 preview-only templates all hitting the legacy branch). The decision D-045 papered over — what to show when the live preview doesn't exist — must be answered at the catalog level, not the CTA level. D-055 answers it: if there's no live preview, the template isn't in the catalog. Once that holds, the conditional branch is dead code and the `href="#"` ghost CTA can simply be deleted. Session 19 flagged this as a systemic UX bug (Phase 2g2x.7) and listed three remediation options (disabled button / PNG lightbox / hide entirely) — D-056 picks "hide entirely, via tier gating" as the correct answer because it's the only option that doesn't leak the existence of an incomplete sibling tier to the shopper.
**Trade-off:** A small amount of code deletion plus a `TemplateDetailView` context simplification. No user-facing downside — the only affected route surface is `draft` templates, which are already unreachable per D-055. One secondary cleanup: D-045 is formally retired (superseded) along with the `has_live_preview` helper in `apps/catalog/template_content.py` (the helper is kept because it's still useful inside the `LiveTemplateView`'s setup path, but its detail-page consumer is removed).
**Consequence:** (a) `templates/catalog/template_detail.html` loses lines 132-136 and the wrapping `{% if has_live_preview %}` / `{% endif %}` markers; (b) `apps/catalog/views.py` TemplateDetailView no longer computes `has_live_preview`; (c) TODO_NEXT.md Phase 2g2x.7 is resolved by D-055 + D-056 combined — no three-option punch list needed; (d) the "Apri anteprima completa" button is the sole, honest, working CTA on every detail page; (e) D-045 is marked superseded in DECISIONS.md and any downstream reference (AGENT_HANDOFF.md, CATEGORY_ROADMAP.md, MEMORY.md) is updated.

## D-057: Tier Migration Implementation — Single-Filter Gate, Registry-Driven Sync, Premium Empty States (2026-04-11, Session 21)
**Decision:** D-055's two-tier model is implemented as a new persistent `WebTemplate.tier` `TextChoices` field (`published_live` / `draft`, default `draft`, db_index=True) — NOT by repurposing the existing `status` field. Tier is synced from `TEMPLATE_REGISTRY.json` via a new `sync_template_tiers` management command that is also auto-called at the end of `seed_templates`, keeping the registry as the single documented source of truth. The public tier gate is centralized in a single helper `apps/catalog/selectors._public_tier_filter(include_drafts: bool)` that every public selector delegates to (listing / detail / related / featured / category counts / search). Views read an `include_drafts` flag from a single helper `apps.catalog.views._staff_preview_mode(request)` which requires BOTH `is_staff` AND `?preview=1` — belt-and-braces. Draft templates 404 on both the marketplace detail route AND the live preview route. Premium empty states live in a single reusable partial `templates/catalog/_empty_catalog.html` with three modes (`category_soon`, `search_no_match`, `catalog_empty`). Category cards with zero live siblings render an "In arrivo" pill instead of "0 template" (new CSS tokens in `components.css`). `get_featured_templates` backfills from the live pool when `featured=True` returns fewer than `limit` live templates, so the homepage never collapses to a single card during the transition.
**Rationale:** Option "new field" was chosen over "repurpose status" because `status` already carries the orthogonal editorial state (`draft / review / published / archived`) used by the admin workflow — conflating it with the public-visibility tier would have broken the admin's "save as draft then publish" flow and coupled two concepts that have different review surfaces. A dedicated `tier` field is one migration, zero admin breakage, and keeps the two concepts orthogonal (a template can be `status=published` but `tier=draft` — which is the entire content-author → shopper gap the D-053 Live Preview Law is about). The centralized `_public_tier_filter` helper is the D-047-chrome-contract equivalent for the query layer: one knob, one place, no second codepath that can forget to filter. The `sync_template_tiers` command reading from `TEMPLATE_REGISTRY.json` preserves the registry's role as the human-readable source of truth while letting the seed command stay idempotent on re-run. `_staff_preview_mode` requires `?preview=1` as an explicit opt-in (not just `is_staff`) so a staff member who happens to land on a draft URL by accident still sees the public 404 — the draft surface is never normalized by accidental traffic. The empty-state partial has three modes because the three failure cases (empty category, failed search, whole-catalog empty) have different copy needs but share the same design token set — one partial, three branches, no duplication. Category card "In arrivo" pill is deliberately a chip on the existing card (not a third card variant) so the grid silhouette stays identical as categories fill up over Phase 2g3, avoiding a re-flow every time a tier flips. Featured-pool backfill is the single extra knob that turns "3 featured but only 1 is live" from a visible bug into a no-op.
**Trade-off:** One extra migration (`catalog/0002_webtemplate_tier.py`), one extra management command (~90 LOC), ~80 LOC delta on selectors.py, ~40 LOC delta on views.py, one new 75-LOC partial + 30-LOC CSS delta for the empty states. No data migration needed because the field default is `draft` (the safe side) and the registry-driven sync applies the 3 promotions after the schema migration lands. Featured-pool backfill is a slight behavior change from the previous `featured=True`-only strict filter, but this is only observable when `featured+live` < `limit` — the current transition state, and a state that will re-resolve naturally as Phase 2g3 lands more templates. Documented here so the next session knows this is a transition-window behavior, not a permanent semantic shift.
**Consequence:** (a) Phase 2g2x.8 is closed; (b) Phase 2g2x.7 is resolved by construction (tier gating deletes the branch); (c) D-045 is formally superseded (both in DECISIONS.md and by the deletion in `template_detail.html`); (d) the catalog floor is now enforced at the query layer — any future view that forgets to use the selectors will NOT leak drafts because the selectors are the only entry point; (e) future template promotions from `draft` → `published_live` can be made either by editing `TEMPLATE_REGISTRY.json` and running `sync_template_tiers`, or by editing the row in the Django admin directly (the `tier` field is exposed via the ModelAdmin's filter list through the fallback Django behavior — note that `WebTemplateAdmin` does NOT explicitly declare tier in `list_filter` yet, see handoff); (f) the blocking gate into Phase 2g3 is now a code-enforced reality — the visible catalog is 3 templates, and every new template that gets added will be `draft` by default until it passes the D-053 acceptance checklist.

## D-058: Live Motion Language — Reusable CSS + JS Module, Opt-In Per Skin, No-JS Fallback, Reduced-Motion Respected (2026-04-11, Session 22)
**Decision:** Premium live-template motion is implemented as **two dependency-free static files** — `static/css/live-motion.css` and `static/js/live-motion.js` — that a per-archetype `_base.html` opts into with one `<link>` in head and one `<script defer>` before `</body>`. The system exposes six patterns accessible via three HTML attribute contracts:
1. `data-lm="reveal"` / `reveal-lg` / `reveal-soft` — scroll-triggered fade + rise (14px body / 22px headings / fade-only for hero media). One-shot; observer unobserves after first intersection.
2. `data-lm-stagger [data-lm-stagger-delay="Nms"]` — parent container whose direct children receive incremental `transition-delay` based on a 70ms (overridable) unit, revealed in cascade once the parent intersects.
3. `data-lm="counter" data-lm-to="NN"` — count-up animation on first intersection at threshold 0.4, preserving non-numeric suffix (e.g. `"180€"` animates `0→180` with `€` kept on the end).
4. Skin-local image-hover zoom via a wrapper + inner background layer pattern (wrapper has `overflow: hidden`, inner layer scales `1.00→1.045` over 900ms with brightness/contrast lift). Not exposed as a global class in this pilot because the selectors are skin-specific, but the pattern is documented and reusable.
5. Skin-local CTA micro-tactility (gold arrow `→` translates +6px + letter-spacing widens on hover, via per-skin CSS using the shared `--lm-ease` and `--lm-dur-*` tokens).
6. Skin-local nav underline sweep (scaleX 0→1 from left edge on hover, permanent for `.is-current`, using per-skin gold tokens).

All six patterns respect **two accessibility gates**:
- **No-JS fallback**: the CSS hidden state is guarded by `body.lm-ready`, a class that only `live-motion.js` adds on `DOMContentLoaded`. If JS never loads, `body.lm-ready` never appears, the hidden rules never activate, and every `[data-lm]` element renders at `opacity: 1 / transform: none` from the initial paint. A JS-disabled browser sees the full page.
- **Reduced motion**: respected BOTH via `@media (prefers-reduced-motion: reduce)` CSS rules that force every motion target to `opacity: 1 !important; transform: none !important; transition: none !important`, AND via a `body.lm-reduced` class that the JS adds on init when `matchMedia('(prefers-reduced-motion: reduce)').matches` is true, which fires a second (belt-and-braces) set of CSS rules that collapse the same properties. A user with the OS setting on gets a plain render even if the `@media` rule is ever stripped by an upstream CSS tool.

The system is **strictly opt-in** — a skin that doesn't link the motion CSS or script the motion JS behaves exactly as it did before. No global change to the marketplace surface. No change to the preview composition files or the Playwright preview pipeline. The first skin to adopt the motion pilot is `gusto-fine-dining` as of Session 22 (this pilot); `cardio-studio-specialistico` and `dermatologia-elite-roma` are next in line via the same two-file opt-in.

**Rationale:** The catalog floor moved from "twenty cards" to "three real multi-page templates" in Session 21 (D-055/D-057). That raised the bar on the *static* dimensions of premium positioning — content, chrome, differentiation, D-047 compliance — but left the *interaction* dimension at zero. A premium marketplace that sells "complete navigable websites" needs those websites to FEEL alive when a buyer scrolls and hovers. Without motion they read as "editorial" (which is good) but also as "static" (which isn't, for a live-preview-first product). Adding motion globally by changing the marketplace base would be risky (could regress the catalog listing / detail / homepage) and wrong in scope (the marketplace surface has its own interaction language already). Adding a full motion framework (GSAP, Framer Motion, AOS, LocomotiveScroll) would be dependency weight + bundle bloat + probably the wrong mood (those libraries are optimized for flashy portfolios, not Michelin-restaurant fine dining). The right shape is a **small, bespoke, dependency-free module** scoped to live-template standalone skins, with a tight attribute contract that authors can apply in the HTML without touching JS.

Two files instead of inline-in-each-base: (a) the tokens + rules live in exactly one place so a change in timing or distance propagates to every skin that opts in, (b) the IO observer logic lives in exactly one place so a bug fix doesn't need to be hunted across multiple templates, (c) the skin-level `_base.html` stays readable (the motion-specific CSS is 7KB and would drown the skin's actual design tokens if inlined), (d) browser caching: two static files that are cached across skin switches means the second skin the user visits pays zero extra cost.

Hidden-state gating on `body.lm-ready` instead of the more common "add hidden class to elements on load" pattern: (a) it's additive — a skin that doesn't load the JS never enters the gated state, so it's impossible for a skin author to forget to "arm" the motion system and end up with blank elements, (b) it's one class on one element instead of N classes on N elements, which is faster to apply, (c) the gate is visible in devtools at a glance (inspect `<body>`, look for `lm-ready`), (d) it gives us a single knob to also carry `lm-reduced` for the reduced-motion short-circuit.

Belt-and-braces reduced-motion (both `@media` and `body.lm-reduced`): a single source of truth would be simpler but riskier. A CSS tool in the future (PostCSS, an autoprefixer pass, a Sass build) could theoretically strip the `@media (prefers-reduced-motion: reduce)` block if it's misconfigured. A `body.lm-reduced` class is stripper-proof because it's plain selectors. Having both means a reduced-motion user is protected even if one layer breaks. The cost is 20 extra lines of CSS.

Skin-local hover enhancements (nav underline sweep, gold arrow shift, letter-spacing widening) are intentionally NOT factored into the shared CSS file because they depend on skin-specific CSS tokens (`--secondary` gold in Gusto; would be a different token in a Medical skin where "primary" is the blue) and on skin-specific selectors (`.fd-nav`, `.gold-btn`, `.mp-bar`). Hoisting them into the shared file would either force every skin to rename its selectors to match a motion-system convention (invasive) or force the shared file to know about per-skin class names (leaky). Keeping them local is honest: the shared file gives you tokens + primitives + runtime; the skin gives you its own hover choreography using those tokens. This is the same architectural choice as D-042 (content registry) and D-043 (per-archetype standalone skins) — keep the shared layer small and let each skin compose its own voice on top.

**Trade-off:** Two new files (~14.6 KB combined) in the static bundle that are only used by live-template skins. Not a regression — they're loaded exclusively from standalone skins so the marketplace bundle is unaffected. The skin's `_base.html` gains ~2 lines (one link, one script). Authors who want to opt into motion pay a one-time cost of reading the attribute contract in this decision or in the `live_motion` comment blocks. Skins that DO opt in are responsible for choosing sensible targets — slapping `data-lm="reveal"` on every element would produce a chaotic cascade, so this is a judgment-call tool, not a batch-apply one. Authoring guidance lives in SESSION_LOG.md Session 22 § 1 (the "6 patterns, not 15" principle) and TODO_NEXT.md Phase 2g2x.9 completion note.

Skin-local hover choreography costs each skin ~30 LOC if they want the full Gusto treatment (nav underline + CTA arrow shift + letter-spacing hover). Skins that don't want this can skip it entirely — the reveal + stagger + counter + image-zoom system still works without the hover extras. The motion system is graduated: minimum viable adoption is one link + one script + a handful of data-attributes on the home page; maximum adoption adds the hover extras for tactility.

**Consequence:** (a) Phase 2g2x.9 closes; (b) the motion pilot is the expected interaction-quality floor for every `tier=published_live` template — cardio and dermatologia should adopt it in a follow-up pass (low effort: link + script + attributes, their chrome is already D-047 clean so nothing else needs to change); (c) every new template promoted from `draft` → `published_live` in Phase 2g3 must adopt the motion language as part of its D-053 acceptance checklist (the 9 gates become 10: add "motion pilot adopted with reveal + stagger + counter + image-hover patterns on the home page at minimum"); (d) future archetypes can override the tokens on their own `:root` without touching `live-motion.css` (e.g. a muted Medical skin sets `--lm-rise: 10px` for a more subdued cadence) — the motion language is configurable per-skin; (e) BRAND_SYSTEM_GUIDELINES.md gets a new "Motion Language" pointer section in a follow-up doc pass; (f) TODO_NEXT.md Phase 2g3 checklist grows a motion-adoption row for each template.


---

## D-080 — Medical Second Wave Live Rollout (Phase 2g3.2)

**Date:** 2026-04-15 (Session 51)
**Status:** Adopted
**Branch:** `phase-medical-second-wave-v1`
**Supersedes:** none
**Successor of:** D-053 (Live Preview Law), D-054 (Premium Differentiation Law), D-047 (Chrome-Authoring Contract), D-057 (Tier Migration), D-063 (i18n/RTL Pilot Architecture), D-066 (Premium Forms), D-069 (language switcher scoped to authored locales), D-073 (eCommerce live rollout precedent), D-078 (Restaurant live-completion), D-079 (Agency live rollout)

**Decision.** Three medical archetypes are promoted from `tier=draft` to `tier=published_live`:

- `salute-studio-medico` — `clinic` archetype (institutional Milano poliambulatorio, SaluteVita Clinic)
- `benessere-centro-olistico` — `wellness` archetype (holistic Bergamo Alta, Studio Armonia)
- `famiglia-pediatria` — `family` archetype (pediatric Torino Crocetta, Pediatria Famiglia Plus)

Each ships a full multi-page live skin folder + per-template content registry + 5-locale content trees (IT/EN/FR/ES/AR) + real RTL for Arabic + Pexels-curated imagery pool + preview PNG. Medical category transitions from 2/5 to **5/5 live**. Catalog reaches **16/20 `published_live`**.

**Why.** Medical was the pilot category for the DNA system (Session 7) but only Cardio + Dermatologia had been promoted via the shared `specialist` archetype (Sessions 11 + 13). The remaining 3 medical templates sat with DNA + preview composition but no skin folders, effectively invisible to the public catalog per D-055. Phase 2g3.2 closes that gap and consolidates medical as a first-class multi-archetype category (5 templates across 3 distinct archetypes: specialist×2 + clinic + wellness + family).

The three new siblings are also the first formal test of D-054's 10-gate law against a **shared category with 5 templates and 3 distinct archetypes**. Previous rollouts (business 2/2, portfolio 2/2, ecommerce 2/2, agency 2/2) never had more than 2 archetypes per category. Medical is the proof that D-054 scales to N=5.

**Contract (enforced by this decision).**

1. **Three distinct macro tones.** Salute = institutional-accessible (bright clinical teal + booking widget + solid-phone nav). Benessere = serene-olistico-sensorial (sage cream + full-bleed manifesto + pill-floating nav + dotted-leader pricelist + calendar-spot). Famiglia = warm-family-protective (peach coral + centered-soft rounded photo card + soft-pastel pill nav + portrait-stack pediatre + phone-and-chat with NO booking form).

2. **Three distinct typography pairings.** Salute: Nunito Sans + Inter (institutional sans). Benessere: Cormorant Garamond italic 96px + Nunito (editorial serif poetic). Famiglia: Quicksand + Nunito (friendly rounded sans). The only constraint the three share: Italian primary content, mixed-script AR handling, Latin digits.

3. **Three distinct conversion patterns.** Salute `booking-widget` (realistic 13-field form with specialty/doctor/date selects). Benessere `calendar-spot` (visual 7-day grid + rituale selection). Famiglia `phone-and-chat` (giant phone CTA + WhatsApp pill — no appointment form because warm-family pattern treats booking as a human conversation).

4. **Three distinct class prefixes.** `.cl-*` (clinic), `.we-*` (wellness), `.fm-*` (family). Never cross-contaminate. Never reuse the `.sp-*` specialist skin.

5. **D-047 from line one.** Every string in the 23 new skin HTML files comes from `{{ page_data.* }}` / `{{ site.* }}` / `{{ chrome.* }}` / `{% for %}` or is a CSS rule. Zero brand literals in skins. Zero "Studio Marani" / "Rambaldi" / "Milano" hardcoded. Verified by grep sweep.

6. **D-054 10-gate matrix passes on every sibling pair bidirectionally.** Salute↔Cardio, Salute↔Derm, Salute↔Benessere, Salute↔Famiglia, Benessere↔Cardio, Benessere↔Derm, Benessere↔Famiglia, Famiglia↔Cardio, Famiglia↔Derm = 9 pairs × 10 gates = 90 differentiation checks, all pass.

7. **Real i18n, not stub fallback.** The 12 locale files (3 templates × 4 locales) carry native voice per register: NHS/BUPA + Ramsay Santé + Sanitas + MSA-hospital-institutional for Salute; Goop/Tatler + Marie Claire Bien-Être + Mía Wellness + Vogue Arabia Living for Benessere; BabyCentre UK + Doctissimo Enfant + Guía Infantil + MSA-parenting for Famiglia. Italian proper names (SaluteVita Clinic, Studio Armonia, Pediatria Famiglia Plus, Rambaldi, Via Galvani, Via Arena, Corso Galileo Ferraris, Sant'Anna, Regina Margherita, Gaslini, etc.) are preserved verbatim in all non-IT locales. Latin digits (0–9) used everywhere including AR for dates/prices/phones. `unicode-bidi: isolate` handled by RTL CSS block in each skin's `_base.html`.

8. **Pexels primary imagery.** Session 47 formalized Pexels as primary (Unsplash legacy kept for other pools). The 3 medical pools (`medical`, `medical-wellness`, `medical-family`) are now fully Pexels-curated with explicit attribution-ready photographer credits in `preview_imagery.py` comments. No video in this wave — the medical register favors still imagery + micro-motion over reel-style video (reserved for restaurant/commerce where ambient video already works).

9. **Preview compositions D-047 clean.** 10 hardcoded literals in `preview_compositions/medical/{clinic,wellness,family}.html` lifted into DNA `content` dict keys (`services_title`, `services_link_all`, `card_cta`, `pricelist_title`, `pricelist_sub_prefix`, `therapists_label`, `hero_ribbon`, `hero_pebble_name`, `hero_pebble_note`, `hours_label`). Preview PNGs regenerated. This closes a latent D-047 miss from the original medical pilot (Session 7) that had stayed dormant because the literals shipped only in the preview composition layer (never in a live skin).

10. **Stub-files-first wiring.** The 12 locale stub files `template_content_<slug>_{en,fr,es,ar}.py` are created as `from X import X_CONTENT_IT as X_CONTENT_LOC` first, letting `template_content.py` load cleanly and `sync_template_tiers` run immediately. Translator sub-agents then overwrite the stubs with native voice. This removes the chicken-and-egg between "DB needs tiers before smoke" and "smoke needs i18n before routes render" that blocked earlier rollouts.

**Alternatives rejected.**

- Rollout as "draft-with-preview-only" instead of full live. Rejected — would be a D-055 violation (the tier is binary: public or staff-preview) and would shrink the catalog surface to 13/20 again. The live-skin investment pays back in every buyer session that reaches the medical category listing.
- Share the `specialist` skin for Salute (clinic) by adding a mode flag. Rejected — D-054 requires distinct silhouettes; a mode-flagged specialist skin cannot deliver split-booking-widget + solid-phone nav without becoming a fork. Better to author a separate skin from line one.
- Skip appointment page for Salute (treat it as phone-only like Famiglia). Rejected — Salute's `booking-widget` conversion pattern requires a dedicated appointment route per D-053 baseline (medical = 5+1 pages). Demand for online booking in Italian institutional medicine is the business driver the archetype exists to serve.
- Include `blog_list`/`blog_detail` for the 3 new templates. Rejected as out of scope — no business evidence that generalist/wellness/pediatric studios benefit from a blog as much as specialist editorial studios do. Can be added later as opt-in if a customer asks.
- Add a video hero to Benessere. Rejected — the serene macro-tone reads better as a still wide photo of a calm spa room than as ambient video. Video for wellness evokes "commercial spa ad" not "refined ritual". Kept for gusto/luxe/elevate where ambient video already works.

**Trade-off.** The rollout adds ~21,000 LOC (skin + IT + locales) to the repo. This is linear growth per template (~7k LOC per template including locales) and matches the Session 41 eCommerce + Session 48 Restaurant + Session 49 Agency precedents. The review surface scales linearly too — each translator sub-agent reviewed exactly their own template × 4 locales. Parallel authoring via sub-agents compressed the wall clock from an estimated ~16h sequential to ~4h.

**Consequences.** (a) Phase 2g3.2 closes. (b) Medical category is 5/5 live; the remaining identity-crash categories (lawyer, real-estate) are now the sole blockers for the 20/20 milestone. (c) CATEGORY_ROADMAP.md status matrix updates to show medical fully CHIUSA. (d) `smoke_full.py` now covers 660 routes (was 530). (e) TEMPLATE_REGISTRY.json crosses 16 templates with full tier_reason D-054 notes. (f) Phase 3 (auth + checkout + editor + projects + commerce front-stage completion) unblocks only after lawyer + real-estate close in Phase 2g3.6. (g) Any future medical template (e.g. a second clinic template like `poliambulatorio-napoli`, a second wellness like `terme-ischia`, a second family like `pediatria-milano`) can reuse the existing 3 skin folders with zero new HTML — proving the D-047 + D-054 reuse model for N≥3 siblings per archetype.
