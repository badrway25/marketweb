# Agent Handoff

Last updated: 2026-04-15 — after **Session 53 Lawyer + Real-Estate Live Rollout · CATALOG COMPLETE 20/20**

## Session 53 — CATALOG COMPLETE 20/20 · Read This Before Touching Any Lawyer / Real-Estate Skin, Lex/Juris/Casa/Villa Content, or the 4 New Pexels Pools (2026-04-15)

**What changed in Session 53.** Phase 2g3.7 closed. Catalog now **20/20 published_live**. Lex (`lex-studio-legale`, classic-gold archetype — Studio Legale Ferri, Roma, forensic-notarile), Juris (`juris-avvocato-moderno`, modern-transparent — Avv. Martini & Partners, Milano, advisory-modern tech boutique), Casa (`casa-agenzia-immobiliare`, mass-market — Domus Immobiliare, Milano+Torino, market-approachable), Villa (`villa-immobili-lusso`, ultra-luxury-cinematic — Villa Prestige, Milano+Portofino, editorial-concierge) have been authored from line one with full multipage live skins (6-8 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, Pexels-curated imagery pools, and sharp D-054 differentiation. **Phase 3 unblock gate MET.**

### What's binding (D-082)

1. **4 new reusable archetypes.** `classic-gold` (forensic-notarile ink+gold studio legale institutional) · `modern-transparent` (advisory-modern slate+blue tech-forward boutique) · `mass-market` (market-approachable navy+emerald+orange residential daylight) · `ultra-luxury-cinematic` (editorial-concierge black+champagne private-advisory). Any future lawyer or real-estate sibling can ship with ONLY a seed row + DNA entry + content block + 5 locale trees. **Zero new HTML per archetype.**

2. **D-054 10-gate matrix passes on every sibling pair, bidirectional.**
   - Lex ↔ Juris: fonts (Cormorant serif ↔ DM Sans sans), palette (ink+gold+bordeaux ↔ slate+blue+yellow), hero silhouette (split-ledger ↔ centered-manifesto), conversion (private-consultation ↔ strategy-call), heritage (1962 ↔ 2018).
   - Casa ↔ Villa: fonts (Poppins ↔ Cormorant), palette (daylight navy+emerald+orange ↔ black+champagne+white), hero (search-widget ↔ fullbleed editorial cover), cards (tile-specs ↔ dossier), geography (Italian urban ↔ Continental), price visibility (visible ↔ hidden), conversion (viewing-request ↔ private-viewing + NDA).
   - Lex/Juris ↔ Pragma/Elevate: no overlap in font pairings, imagery pools, or conversion vocabulary.
   - Casa/Villa ↔ Bottega/Luxe: different page kinds (no shop/cart/PDP), different card vocabularies, different conversion verbs.
   - Villa ↔ Luxe: despite shared Cormorant+dark-champagne DNA, Villa is real-estate advisory (property dossiers, NDA, concierge) while Luxe is fashion ecommerce (atelier, lookbook, stylist).

3. **D-047 chrome-cleanliness from line one.** All 32 new HTML skin files (`lawyer/classic-gold/` 8 + `lawyer/modern-transparent/` 8 + `real-estate/mass-market/` 8 + `real-estate/ultra-luxury-cinematic/` 8) + 4 preview compositions carry zero brand literals — every visible string flows from `{{ page_data.* }}` / `{{ site.* }}` / `{{ chrome.* }}` / `{{ dna.content.* }}` / `{% for %}` loops.

4. **`html[dir="rtl"]` CSS block + conditional Noto Naskh/Kufi/Amiri Arabic font load on all 4 bases.** Latin proper names (Studio Legale Ferri, Avv. Prof. Alberto Ferri, Avv. Giorgia Martini, Domus Immobiliare, Villa Prestige, Alessandra Visconti di Modrone, Via Piemonte 39, Via Solferino 40, all 14 lawyer names, 9 agent names, 4 private advisor names, street addresses, property names Villa Aurelia/Castello di Monterò/Penthouse Quadronno/Mas de la Mer, territory labels Portofino/Chianti/Costa Smeralda/Saint-Tropez/Capri/Val d'Orcia, publication names) preserved verbatim across all non-IT locales. Arabic numerals stay Latin (unicode-bidi: isolate per skin RTL block).

5. **Native voice per locale.** Lex EN reads as Slaughter-and-May, FR as Gide/Bredin Prat cabinet, ES as Garrigues despacho, AR as Al Tamimi MENA MSA institutional. Juris EN as Kirkland Startups/Orrick/Gunderson Dettmer, FR as Bredin Prat VC, ES as Cuatrecasas Startups, AR as Al Tamimi tech desk. Casa EN as Foxtons/Knight Frank, FR as Barnes/Century 21, ES as Engel & Völkers Spain retail, AR as Emirates Living/Better Homes. Villa EN as FT How to Spend It/Monocle Estates/Sotheby's, FR as Le Figaro Propriétés/Emile Garcin, ES as Vanity Fair Spain/Savills España, AR as Robb Report ME/Esquire ME editorial literary. Structural parity verified — same key paths at every level across all 5 locales.

6. **Page slugs stay Italian (URL-canonical).** Lex: home/studio/pratiche/avvocati/notabili/contatti. Juris: home/approccio/servizi/settori/insights/contatti. Casa: home/immobili/quartieri/agenzia/valutazione/contatti. Villa: home/collezione/territorio/studio/esperienza/concierge. Only `label` fields change per locale.

7. **Pexels primary imagery, 4 disjoint pools.** `lawyer-classic` (heritage ink), `lawyer-modern` (bright collaborative), `realestate-casa` (daylight attainable), `realestate-villa` (golden-hour rarefied). 6 URLs per pool, zero overlap across pools.

8. **D-081 dynamic counter policy — Lex/Juris/Casa/Villa all compliant.** Stats bands carry `data-lm="counter"` on every numeric span; "Prezzo su richiesta" on Villa stays static per editorial-tone exception.

9. **Page-kind choices (reference for future real-estate siblings):** Casa uses `project_list`/`project_detail` for immobili listings + details. Villa uses `blog_list`/`blog_detail` for collezione dossiers + property detail. Both use the same LiveTemplateView `_list→_detail` plumbing. The choice between the two is semantic, not structural.

10. **CHROME_I18N extensions.** `mp_other_lawyer` + `mp_other_realestate` added across all 5 locales. Future category additions should follow the same pattern.

### Do NOT do in a follow-up session without revisiting D-082 + CLAUDE.md

- **Do NOT add a 5th lawyer or 3rd real-estate template without checking archetype fit.** If it's "like Lex but Napoli", reuse `classic-gold/` skin. If "like Casa but Roma", reuse `mass-market/` skin. If "like Villa but Costa Smeralda", reuse `ultra-luxury-cinematic/` skin. NEVER duplicate a skin folder; extend the content registry.
- **Do NOT machine-translate legal terminology or real-estate vocabulary.** Use the native register per locale (codici italian references must keep the Italian anchor with native gloss: `Art. 2343 c.c.` → EN `Section 2343 of the Italian Civil Code` → FR `Art. 2343 du Code civil italien` → ES `Art. 2343 del Código Civil italiano` → AR `المادة 2343 من القانون المدني الإيطالي`).
- **Do NOT translate Italian proper names (people/places/institutions/property names/publications).** They stay Italian across EN/FR/ES/AR. For AR they appear in Latin script inside Arabic text (unicode-bidi: isolate).
- **Do NOT collapse the 4 Pexels pools back into two `lawyer` and `real-estate` pools.** The per-archetype separation is D-054 enforcement infrastructure.
- **Do NOT add prices to Villa listings.** The "Prezzo su richiesta" convention is a Villa-specific brand signal per editorial-concierge tone.
- **Do NOT add a cart/shop surface to Casa or Villa.** They are real-estate advisories, not ecommerce.
- **Do NOT retroactively animate Villa's "Prezzo su richiesta" label as a counter.** D-081 tone-exception applies.

### What to verify BEFORE the next major rollout

When Phase 3 authors begin wiring commerce/editor/projects to the 20 live templates:
- Every marketplace detail page (`/templates/<cat>/<slug>/`) returns HTTP 200 in all 5 locales
- Every live preview home (`/templates/<cat>/<slug>/preview/`) returns 200 in all 5 locales
- Every inner page (about/services/team/contact/etc per template) returns 200 in all 5 locales
- `smoke_full.py` reports **834/834 HTTP 200** (baseline verified 2026-04-15)

---

Last updated: 2026-04-15 — after **Session 52 Medical Second Wave Polish + Interaction Fix**

## Session 52 — Medical Polish: Read This Before Touching `live-forms.css`, `live-motion.js`, or Any Stats Band (2026-04-15)

**What changed in Session 52.** Polish-only session — no tier churn, no locale rework, no new skins. Closed three interaction defects left behind by Session 51's rollout: empty Benessere nav CTA, barrel-radius open listbox panel, static Salute stats.

### What's binding (D-081)

1. **`--lf-listbox-radius` exists and is the RIGHT knob to tune open-dropdown corners.** `.lf-select-listbox` in `static/css/live-forms.css` reads `var(--lf-listbox-radius, 12px)` — NOT `var(--lf-radius)`. Skins with pill fields (`--lf-radius: 999px`) MUST set `--lf-listbox-radius` explicitly to avoid a 999px-radius panel (wellness = 14px). Skins that want listbox-matches-field can set `--lf-listbox-radius: var(--lf-radius)`. Default 12px is safe.

2. **Dynamic Counter Policy binds for every stats band going forward.** When a published_live template renders a stats / facts / metrics / volumes / years / visits / indicators band, the numeric span MUST carry `data-lm="counter"` (unless the DNA tone disqualifies it — funereal editorial, brutalist manifesto, literal zeros). Reduced-motion is already respected by live-motion.js. Future rollouts (Lex · Juris · Casa · Villa) are gated on this. Premium-UI reviewer treats this as an implicit gate #11 on the D-054 matrix for templates with numeric bands.

3. **`live-motion.js` now handles both Italian AND English thousand separators.** `28.000` (IT dot-sep) → target 28000; `28,000` (EN comma-sep) → target 28000. The separator character is preserved through mid-animation frames. The regex is deliberately strict (`\d{1,3}(,\d{3})+` — multi-group required) so `1,4` (French decimal) stays a decimal.

4. **Per-stat animation opt-out = 3rd tuple element truthy.** Content registries can author `("1998", "Anno di fondazione", True)` — the truthy 3rd element tells the skin "render static, don't animate". Default = animate (2-tuple, or 3-tuple with falsy 3rd). This is the escape hatch when a value reads as a label rather than a quantity. Clinic uses this pattern in `home.html`; future skins with stats bands can copy.

5. **Multi-line Django comments inside skin HTML MUST use `{% comment %}…{% endcomment %}`.** The `{# … #}` form leaks to render output when it spans multiple lines (Django tokenizer quirk; same gotcha as Session 48 D-078 key-insight #1). This is now a hard rule for all future skin edits.

6. **Nav-CTA copy lives in `site.*`, not `chrome.*`.** Chrome is archetype-shared (marketplace bar, footer headings, form primitives); nav-CTA wording is template-specific (reservation vs phone vs chat). Wellness `_base.html` binds `{{ site.nav_cta }}`; every Benessere locale defines it. Do not add `nav_cta` to `CHROME_I18N` — wrong layer.

### Do NOT do in a follow-up session

- Do NOT revert `--lf-listbox-radius` back to inheriting `--lf-radius`. The decoupling is intentional. If a future skin wants matched radii, override explicitly.
- Do NOT author new stats bands without `data-lm="counter"`. If the DNA tone argues for static (e.g. editorial funereal voice), document the exception in the section comment.
- Do NOT add `chrome.nav_cta` to `CHROME_I18N`. Per-template voice lives in `site.nav_cta`.
- Do NOT use `{# … #}` on multiple lines inside skin HTML. Always `{% comment %}…{% endcomment %}` for annotation.
- Do NOT translate `site.nav_cta` with machine translation. The native register per locale matters — Benessere AR uses "احجز طقسك" (book your ritual), not a literal "reserve" verb.

---

Last updated: 2026-04-15 — after **Session 51 Medical Second Wave Live Rollout**

## Session 51 — Medical Second Wave Live Rollout: Read This Before Touching Any Medical Skin, Salute/Benessere/Famiglia Content, or the `medical`/`medical-wellness`/`medical-family` Pexels Pools (2026-04-15)

**What changed in Session 51.** The medical category is now **5/5 published_live**. Salute (`salute-studio-medico`, clinic archetype — SaluteVita Clinic, Milano Centrale institutional poliambulatorio), Benessere (`benessere-centro-olistico`, wellness archetype — Studio Armonia, Bergamo Alta olistico), and Famiglia (`famiglia-pediatria`, family archetype — Pediatria Famiglia Plus, Torino Crocetta pediatric) have been authored from line one with full multipage live skins (6-7 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, Pexels-curated imagery pools, and sharp D-054 differentiation enforced both vs each other AND vs Cardio/Derm specialist.

### What's binding (D-080)

1. **Salute + Benessere + Famiglia + Cardio + Derm must STAY DISTINCT across every locale.** 90 D-054 gate checks (9 pairs × 10 gates) pass. Voice contracts:
   - **Salute** (clinic institutional poliambulatorio): "La tua salute, il nostro lavoro quotidiano" register · split-booking widget hero · solid-phone nav · icon-grid 4-up SVG cards · medium density · 7-page (home/studio/servizi/prevenzione/medici/contatti/prenota). NHS/BUPA (EN), Ramsay Santé/Doctolib `vous` (FR), Sanitas peninsular `usted` (ES), MSA hospital-institutional (AR).
   - **Benessere** (wellness serene olistico): "Un respiro è la misura del nostro tempo" register · full-bleed-manifesto hero + gradient · pill-floating nav · dotted-leader pricelist rituali · calendar-spot CTA · Cormorant Garamond italic 96px · airy density · 7-page (home/filosofia/rituali/ambienti/professionisti/contatti/prenota). Goop/Tatler (EN), Marie Claire Bien-Être/Cinq Mondes (FR), Mía Wellness/Six Senses (ES), Vogue Arabia Living/Kinfolk (AR).
   - **Famiglia** (family warm pediatric): "Cresciamo insieme ai vostri bambini" register · centered-soft rounded photo card hero + SSN ribbon + pediatra pebble · soft-pastel rounded-pill nav · portrait-stack pediatre · phone-and-chat CTA (NO booking form) · Quicksand rounded friendly · airy density · 6-page (home/studio/visite/crescita/pediatre/contatti). BabyCentre UK/NCT (EN), Doctissimo Enfant/Magicmaman `vous` (FR), Guía Infantil `usted` (ES), MSA parenting-magazine (AR).
   - **Cardio + Derm** (specialist prestigious editorial): untouched in Session 51 — DO NOT modify.

2. **Three new skin folders are reusable archetype templates.** Future medical siblings:
   - Clinic generalist → reuse `templates/live_templates/medical/clinic/`. Drop content registry + DNA entry pointing archetype to `clinic`, swap palette tokens.
   - Wellness holistic → reuse `templates/live_templates/medical/wellness/`. Same pattern.
   - Family pediatric → reuse `templates/live_templates/medical/family/`. Same pattern.
   - Specialist consultive → reuse `templates/live_templates/medical/specialist/` (Cardio + Derm precedent since Session 14).
   - A hypothetical 6th medical sibling (`poliambulatorio-napoli`, `terme-ischia`, `pediatria-milano`) can ship with ONLY a seed row + DNA entry + content block + locale trees. **Zero new HTML needed** per archetype.

3. **D-047 chrome-cleanliness from line one.** All 23 new HTML files carry zero IT literals — every visible string flows from `page_data.*` / `site.*` / `chrome.*` / `{% for %}`. Future skin edits MUST keep this. Also: 10 preview-composition literals lifted into DNA `content` dict keys (`services_title`, `services_link_all`, `card_cta`, `pricelist_title`, `pricelist_sub_prefix`, `therapists_label`, `hero_ribbon`, `hero_pebble_name`, `hero_pebble_note`, `hours_label`) — preview compositions for medical are now clean too.

4. **`html[dir="rtl"]` CSS block + conditional Noto Naskh/Kufi Arabic font load on all 3 bases.** Each skin's `_base.html` carries a RTL token override block + Arabic font stack import conditional on `{% if is_rtl %}`. Latin proper names (SaluteVita Clinic, Studio Armonia, Pediatria Famiglia Plus, Elisa Conti, Sara Conti, Rambaldi, Via Galvani, Via Arena, Corso Galileo Ferraris, Sant'Anna, Regina Margherita, Gaslini, Palazzo Bonomi Suardi, etc.), prices (€ 85, € 320, € 920), phone numbers (+39 035 412 998, 011 549 21 88, 800 123 456), hours, all Latin Western digits stay Latin — `unicode-bidi: isolate` handled by RTL CSS rules.

5. **Native voice per locale, never machine translation.** Salute EN reads as native NHS; Benessere FR as native Marie Claire Bien-Être; Famiglia ES as native Guía Infantil. Structural parity: same key paths at every level across all 5 locales (verified via `diff`-style walk).

6. **Italian proper names (people/places/institutions) preserved verbatim across all locales.** Brand names, doctor names, neighbourhoods, insurance schemes (Inail, Unisalute, Generali Welion, RBM Salute, Previmedical, Caspie, MioDottore), Italian institutions (Gaslini, Sant'Anna, Regina Margherita, San Raffaele, Einaudi Ragazzi, OMCeO) — stay Italian across EN/FR/ES/AR. For AR, they appear in Latin script inside Arabic text (not transliterated).

7. **Page slugs stay Italian (URL-canonical).** Salute: home, studio, servizi, prevenzione, medici, contatti, prenota. Benessere: home, filosofia, rituali, ambienti, professionisti, contatti, prenota. Famiglia: home, studio, visite, crescita, pediatre, contatti. Only `label` fields change per locale.

8. **Pexels primary imagery with 3 disjoint pools** — `medical` (bright clinical teal), `medical-wellness` (sage serene), `medical-family` (peach warm pediatric). URLs are hot-linkable Pexels CDN with explicit `fit=crop` sizing. No video in this wave (medical register favors still photography + micro-motion over reel-style video).

9. **Stub-files-first pattern for locale wiring.** Before spawning translator sub-agents, create 12 locale stub files that `import X_CONTENT_IT as X_CONTENT_LOC`. This lets `sync_template_tiers` + smoke run immediately. Translator agents then overwrite stubs with native voice. Same pattern is recommended for future rollouts.

### Do NOT do in a follow-up session without revisiting D-080 + CLAUDE.md + this handoff

- **Do NOT add a 6th medical template without checking which archetype it belongs to.** If it's "just like Salute but for Napoli", reuse `clinic/` skin. If it's "just like Famiglia but for Milano", reuse `family/` skin. NEVER duplicate a skin folder; extend the content registry.
- **Do NOT machine-translate medical terminology.** Use the native register per locale (e.g., IT "bilancio di salute" → EN "well-child check-up" → FR "bilan de santé" → ES "revisión pediátrica" → AR "فحص طبي دوري"). Machine translation will break the D-080 voice contract.
- **Do NOT add blog_list/blog_detail to the 3 new medical templates** unless there's explicit business evidence. The current baselines per CATEGORY_ROADMAP D-053 cover them without blog.
- **Do NOT collapse the 3 Pexels pools back into one `medical` pool.** The per-archetype separation is D-054 enforcement infrastructure.
- **Do NOT touch specialist skin.** Cardio + Derm are untouched in Session 51; any regression there would be a D-060 violation.

---

Last updated: 2026-04-15 — after **Session 48 Restaurant Live Completion Premium**

## Session 48 — Restaurant Live Completion Premium: Read This Before Touching Any Restaurant, Sapore/Brace, or Trattoria-Warm/Street-Modern Skin Work (2026-04-15)

**What changed in Session 48.** The restaurant category is now **3/3 published_live**. Sapore (`sapore-trattoria-pizzeria`, trattoria-warm archetype) and Brace (`brace-street-food-lab`, street-modern archetype) have been authored from line one with full multipage live skins (6 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, and sharp D-054 differentiation enforced both vs each other and vs Gusto fine-dining.

### What's binding (D-078)

1. **Sapore + Brace + Gusto must STAY DISTINCT in voice across every locale.** D-054 differentiation is enforced by 0 IT-leak smoke (480 cross-locale checks). Voice contracts:
   - **Sapore** (warm Roman family-trattoria): "Da Nonna Rosa, come a casa vostra" register · phone+WhatsApp + reservation form · chalkboard daily-specials · family band · forno-a-legna · tavolata · Cesanese del Lazio · mattarello · tirata. Bon Appétit/NYT-Food (EN), Le Fooding `tu` (FR), El País Gastro `tú` peninsular (ES), Brownbook MSA (AR).
   - **Brace** (Bologna street-food brutalist): "Bruciato al fuoco vivo, servito al volo" UPPERCASE register · order-now (al banco/takeaway/delivery) · GLOVO/DELIVEROO/JUST EAT/UBER EATS · counter status mono chips · late-night DJ moments · smashburger · scottona · Big Shoulders Display 900. Eater (EN), Le Fooding street `tu` + anglicismes (FR), Time Out Madrid `tú` peninsular + `currar` (ES), Wamda urban-imperative MSA (AR).
   - **Gusto** (editorial fine-dining concierge): "Una serata in otto atti" register · concierge tile · sommelier · Michelin · 14 coperti · Playfair italic · Cormorant. Untouched in Session 48 — DO NOT modify.

2. **Both new skin folders are now reusable archetype templates.** Future restaurant siblings:
   - Warm-family register → reuse `templates/live_templates/restaurant/trattoria-warm/`. Drop in a new content registry, point the WebTemplate.archetype at `trattoria-warm`, swap palette tokens per the `--primary/--secondary/--accent` contract.
   - Fast-casual urban brand → reuse `templates/live_templates/restaurant/street-modern/`. Same pattern.
   - Only when a third sibling is semantically as far from BOTH existing siblings as Sapore is from Brace should a new archetype be split (D-050/D-051 default applies retroactively to restaurant).

3. **D-047 chrome-cleanliness from line one.** All 14 new HTML files (7 per skin) carry zero IT literals — every visible string flows from `page_data.*` / `site.*` / `chrome.*`. Future skin edits MUST keep this.

4. **`html[dir="rtl"]` CSS block + conditional Amiri/Noto-Kufi font load on both bases.** Sapore uses Amiri body + Noto Kufi Arabic display (warm classical for the family-trattoria voice). Brace uses Amiri + Noto Kufi (urban-brutalist register). Latin proper names (Trattoria Da Nonna Rosa, Rosa Trezzi, Marco Trezzi, Giulia Trezzi, Trastevere, Roma, Via dei Salumi, Lazio, Amatrice / Brace Street Lab, Bologna, Via Indipendenza, Tortellini), prices (€ 9.50, € 12.00), phone numbers, hours (12:00 – 24:00), Latin Western digits all stay Latin via `unicode-bidi: isolate` (Sapore) or RTL CSS rules (Brace).

5. **Native voice per locale, never machine translation.** Sapore EN reads as native NYT Food; Brace EN reads as native Eater. Sapore FR uses `tu` warm-trattoria; Brace FR uses `tu` urban-imperative — DIFFERENT registers despite both being tutoyer. Same delineation for ES/AR.

6. **Italian dish/proper names preserved across all locales.** Cacio e pepe, Carbonara, Bucatini all'amatriciana, Coda alla vaccinara, Tonnarelli, Margherita Verace, Cesanese del Lazio, Saltimbocca alla romana / Margherita, Diavola, Mortadella di Bologna, Pizza Rossa, San Marzano DOP, scottona piemontese, Tiramisù — all stay Italian across EN/FR/ES/AR.

7. **Page slugs stay Italian (URL-canonical).** Sapore: home, menu, storia, forno, eventi, contatti. Brace: home, menu, lab, moments, ordina, contatti. Only `label` fields change per locale. Slugs are IT — never translate.

### Reusable recipe (now proven 8 times)

Cardio · Derm · Gusto · Chiara · Pixel · Pragma+Elevate · Bottega+Luxe · **Sapore+Brace**:

1. Audit DNA + skin folder + content registry state for both templates
2. Author IT skin folder via parallel sub-agent (1 per template) — explicit DNA contract, palette tokens, font stack, chrome-key list (D-047), RTL block, 720px breakpoint, `:focus-visible`
3. Author IT content registry per template (~500-900 LOC each)
4. Stub locale modules (re-export IT) so imports stay green during bootstrap
5. Wire into TEMPLATE_CONTENT
6. Flip `tier` in TEMPLATE_REGISTRY.json + `python manage.py sync_template_tiers`
7. IT-only smoke (12/12 routes for 2 templates × 6 pages)
8. Dispatch 8 parallel locale sub-agents (4 locales × 2 templates) with explicit voice contracts + differentiation guards + dish-name preservation rules + structural-parity validation step
9. When agents return: parse-validate, key-parity check vs IT, live-route check at `?lang=xx`, IT-leak sweep
10. Update `smoke_full.py` + `smoke_forms.py` + `smoke_i18n_media_hardening.py` to include new templates
11. Browser click-through validation across all 5 locales
12. Update memory + DECISIONS + SESSION_LOG + TODO_NEXT + AGENT_HANDOFF + CATEGORY_ROADMAP + TEMPLATE_REGISTRY in single follow-up commit

### Do NOT do

- Do NOT collapse Sapore + Brace voices into one shared register — they must stay sharply distinct across every locale.
- Do NOT add chalkboard/family-band/Caveat-script Sapore-only patterns to Brace, or order-now/AGGIUNGI/counter-status/neon-yellow Brace-only patterns to Sapore. The cross-leak smoke enforces this.
- Do NOT touch Gusto fine-dining — it's the third leg of the restaurant category and was untouched per directive. 52/52 gusto i18n regression is the binding gate.
- Do NOT use machine translation for any locale block. The quality floor is native Bon Appétit/Le Fooding/El País Gastro/Brownbook (Sapore) and native Eater/Trax/Time Out Madrid/Wamda (Brace) editorial voice per template per locale.
- Do NOT translate Italian page slugs. Sapore stays `home/menu/storia/forno/eventi/contatti`. Brace stays `home/menu/lab/moments/ordina/contatti`. Only labels change per locale.
- Do NOT introduce a real cart/checkout/payment flow on either template. Conversion patterns are deliberate demos: phone-and-whatsapp + reservation form (Sapore) and order-now hub with simulated counter status + delivery partners marquee (Brace). A real commerce engine for restaurants is a Phase 4+ topic, out of scope.
- Do NOT touch the 9 already-multilingual templates (cardio/derm/gusto/chiara/pixel/pragma/elevate/bottega/luxe) when working on Sapore+Brace. Regression smokes (363/363 was, 363/363 still) are the binding gate. The hardening smoke (69/69 OK) verifies 11/11 multilingual coverage.
- Do NOT add Big Shoulders Display or JetBrains Mono to Sapore. Sapore is Libre Baskerville + Source Sans 3 + Caveat (script accent only).
- Do NOT add Libre Baskerville or Caveat to Brace. Brace is Big Shoulders Display + Inter + JetBrains Mono.
- Do NOT use multi-line `{# … #}` Django comments in any new skin file. Use `{% comment %}…{% endcomment %}`. The `{# foo\n   bar #}` form leaks inner text to render output (caught at first Brace/Sapore render in Session 48; both fixed).

### Gotchas (Session 48)

- **Multi-line `{# … #}` Django comments leak.** Caught at first Brace/Sapore render — debug "Big Shoulders Display [display condensed (UPPERCASE)..." string visible at top of every page; fixed by switching to `{% comment %}` block. Future skin authoring MUST use `{% comment %}` for multi-line docs.
- **Apostrophe-in-single-quoted-Python-string IT content.** First Brace IT registry had `'TRE GESTI. <em>NIENT'ALTRO.</em>'` — the apostrophe terminated the string mid-value. Convention: default to **double-quoted Python strings** when content can contain apostrophes. Sub-agent prompts now mention this explicitly.
- **`runserver --noreload` does NOT pick up template OR Python changes between requests on Windows.** Even with `DEBUG=True`. Each template/Python edit needs a server bounce on a fresh port (8901 → 8902 → 8903 → 8904 in this session). Same gotcha as Session 19, 23, 42.
- **Playwright `fullPage: true` screenshots can capture mid-fade or pre-fade state.** When `live-motion.js` IntersectionObserver hasn't fired on a section yet, that section appears blank in the thumbnail but renders correctly when scrolled into view. Workaround: `page.evaluate(() => { document.querySelectorAll('[data-lm]').forEach(el => el.style.opacity = '1'); })` before screenshot.
- **PEXELS_API_KEY env var was NOT present at session start.** Used existing curated Unsplash IDs from `restaurant-trattoria` + `restaurant-street` pools (Sessions 31/47 verified). Pexels CDN swap is a Phase-2g3.6c follow-up — the URL format `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=<w>&h=<h>&fit=crop` is hot-link-public so future swap is one-line per slot when key is provided.
- **`Caveat` font in DNA registry is NOT the structural face.** Sapore DNA declares `font_pairing = ("Caveat", "Inter")` but the actual structural typography is **Libre Baskerville + Source Sans 3** (with Caveat as a 1-2-spot script garnish on chalkboard daily-specials, "Buon appetito!" stamp, footer wordmark). The skin's `_base.html` hardcodes the Google Fonts link to load all 3 families — DO NOT rely on `theme.heading_font` for primary type on Sapore; the DNA's Caveat declaration is the script-accent contract.

---

## Session 45 — Commerce Completion v2: Read This Before Touching Any /shop/, /dashboard/, Payment, i18n, or Merchant Work (2026-04-14)

**What changed in Session 45.** `apps/commerce` è passato da foundation v1 (IT-only, dev-payment, is_staff global) a v2 operativa. Le 4 modifiche load-bearing:

### 1. Multilingua /shop/ — 5 locales via chrome dict + translations JSONField
- `apps/commerce/i18n.py` è la nuova fonte di verità per le stringhe chrome commerce. `COMMERCE_CHROME` ha ~125 keys × 5 locales. Re-esporta `SUPPORTED_LOCALES`/`DEFAULT_LOCALE`/`RTL_LOCALES` da `apps/catalog/template_i18n.py` (non riallinearle indipendentemente).
- `apps/commerce/content.py` porta il per-storefront brand copy (tagline, footer_bio, shipping_policy, return_policy, bank_transfer_instructions) × 5 locales. Il seeder lo popola su `Storefront.translations`.
- `Storefront`, `Collection`, `Product`, `ShippingMethod` hanno tutti `translations` JSONField con shape `{locale: {field: value}}` + helper `.localized(locale)`.
- `LocaleMixin` (in views/customer.py) è l'unico punto in cui si risolve `?lang=` — chiamare `self.get_locale_context(storefront)` per ottenere il context bundle.
- **Regola:** ogni internal `commerce:*` URL DEVE avere `{{ lang_qs }}` appeso: `{% url 'commerce:cart' storefront.slug %}{{ lang_qs }}`. Se saltate questo, la locale si perde al primo click.
- **Regola:** NON leggere `product.title` direttamente nei template — usate `product_l10n.title` o `products_l10n` iteration. Il fallback IT è già gestito da `localized()`.

### 2. Payment — Stripe real-path via env vars, graceful fallback altrimenti
- `apps/commerce/payments.py` è il dispatcher. `dispatch(PaymentContext(order))` sostituisce il vecchio inline `_dispatch_payment` rimosso da `services.py`.
- Stripe è lazy-imported: senza `stripe` package o senza `STRIPE_SECRET_KEY` → `ProviderUnavailable` raise → `dispatch` falla a stub con `payload.stub_fallback=True` + warning log.
- Idempotency: `idempotency_key=f"order-{order.reference}"` — retry del medesimo ordine ritorna il medesimo PaymentIntent, no double-charge.
- Webhook: `/commerce/webhook/stripe/` (csrf_exempt). Verifica signature con `STRIPE_WEBHOOK_SECRET`. Gestisce `payment_intent.succeeded`/`payment_failed`/`canceled`.
- Env vars: `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_ALLOW_STUB_FALLBACK` (default `"1"`).
- **Regola:** NON chiamare `_handle_stub` o `_handle_stripe` direttamente — sempre `payments.dispatch()`.

### 3. Merchant scoping — StorefrontMember table
- Nuovo modello `StorefrontMember(storefront, user, role=owner|editor)` unique_together.
- `SellerRequiredMixin` ora extende `LoginRequiredMixin` e in `dispatch()` verifica `_user_can_access(user, storefront)` (membership OR superuser). Anonymous → login redirect. Staff senza membership → 403 `PermissionDenied`.
- Nuova view `DashboardRootView` a `/dashboard/` — chooser page o auto-redirect se single-membership.
- **Regola:** NON usare `user.is_staff` come gate per visibility di uno storefront. Ogni query dashboard deve scope-filter per `storefront=self.storefront` (il mixin pre-carica il storefront autorizzato).
- Demo users creati dal seeder: `bottega_owner` / `commerce-v2`, `luxe_owner` / `commerce-v2`.

### 4. Customer flow — policies + lookup + retry + Stripe Elements page
- `PoliciesView` a `/shop/<slug>/politiche/` — renderizza shipping/returns/contact policy localized.
- `OrderLookupView` a `/shop/<slug>/ordine/` — guest self-service: reference + email → 302 a confirmation se match, altrimenti re-render con messaggio.
- `RetryPaymentView` POST-only a `/shop/<slug>/order/<uuid>/retry-payment/` — richiama `services.retry_payment()` che re-dispatcha via `payments.dispatch`. Per Stripe → 302 a payment_page; altrimenti → 302 a confirmation.
- `PaymentPageView` a `/shop/<slug>/order/<uuid>/payment/` — renderizza `templates/commerce/payment/stripe.html` (Stripe Elements + fallback friendly).

### Seeder workflow
- `python manage.py seed_commerce` è idempotente e ri-esegue popolamento translations + merchant users.
- Se aggiungi un nuovo shipping method code, aggiorna `SHIPPING_TRANSLATIONS` nello stesso file — senza entry, ship_method renderizza solo in IT.

### Validation matrix da rieseguire dopo modifiche
- `python manage.py check` → 0 issues
- Commerce smoke (73/73): shop/cart/checkout/policies/ordine × 5 locales × 2 skin + product × 3 locales × 2 skin + collection × 2
- Live preview regression (45/45): 9 templates × 5 locales, must stay green
- ACL matrix (7/7): anon/bottega_owner/luxe_owner × 3 dashboard paths
- Customer flow: add_to_cart→302, checkout POST→302, order confirmation AR→200, order lookup POST match→302

### Non fare
- Non modificare `/templates/<cat>/<slug>/preview/*` routes o live_templates templates — zona marketing intoccabile, protetta da 45/45 regression.
- Non aggiungere hardcoded `?lang=` in un template — usa `{{ lang_qs }}`.
- Non chiamare il vecchio `_dispatch_payment` — è stato rimosso.
- Non gate dashboard su `is_staff` — usa StorefrontMember.
- Non committare chiavi Stripe reali in `settings.py` — solo env vars.

---

## Session 43 — Commerce Foundation v1: Read This Before Touching Any Commerce, Cart, Checkout, Order, or Seller Dashboard Work (2026-04-14)

**Session 43 closed Phase 3a** — `apps/commerce` is no longer empty stub. It now ships a full operational engine for shops (Product/Variant/Cart/Order/PaymentIntent) with two skin template sets serving Bottega + Luxe at `/shop/<storefront>/…`, a seller dashboard at `/dashboard/<storefront>/…`, and a provider-agnostic payment abstraction (stub + offline_bank_transfer in v1, Stripe documented extension point).

### What's binding (D-075)

1. **`/shop/<slug>/...` and `/dashboard/<slug>/...` are the operational surfaces. `/templates/<cat>/<slug>/preview/...` stays the marketing surface.** D-053 Live Preview Law still binds the preview URL space. NEVER fold commerce operations into the preview routes — they must remain untouched. When a user visits a Bottega live preview they see the Session 41+42 showcase; when they visit `/shop/bottega-shop-artigianale/` they see the real operational shop. The two surfaces are peers, not versions.

2. **`Storefront.is_operational` is the commerce-side shippability gate** — parallels `WebTemplate.tier == published_live`. Both Bottega + Luxe are operational in v1. Future ecommerce templates must flip BOTH `tier=published_live` (preview visible) AND create a `Storefront` row with `is_operational=True` (shop visible).

3. **Inventory is decremented on order creation, not at payment time.** The `create_order_from_cart` service uses `select_for_update` to lock variants inside a transaction. For the `stub` dev provider payment auto-succeeds so there's no race window; for real providers (Stripe later, offline_bank_transfer today) the order sits at `payment_status=UNPAID` while stock is already held. A compensating "release held stock on payment failure" service is a Phase 3b add.

4. **Guest checkout is first-class.** Cart is session-keyed (`request.session.session_key`). User FK is optional on both Cart and Order. Checkout form does not require login. Order confirmation page is addressable by UUID (shared link). Do NOT introduce login gates on any `/shop/` route.

5. **Seller dashboard gate is `is_staff` today.** `SellerRequiredMixin` redirects anon/non-staff to `/admin/login/?next=…`. A `Seller` model scoping users to specific storefronts is a documented Phase 3b split.

6. **Payment providers are registered in the `Storefront.PaymentProvider` enum.** v1 enum has `stub` + `offline_bank_transfer`. Adding Stripe means: (a) add `STRIPE = "stripe"` to the enum, (b) add `_handle_stripe(order)` to `services._dispatch_payment`, (c) create a webhook view that resolves PaymentIntent by `provider_reference` and transitions status, (d) add a `STRIPE_SECRET_KEY` setting. No model migration needed.

7. **Skin template duplication is DELIBERATE in v1.** `templates/commerce/skins/<skin>/_base.html` files duplicate structural CSS from `templates/live_templates/ecommerce/<archetype>/_base.html`. The two surfaces have different nav targets (commerce chrome links to `/shop/`, preview chrome links to `/templates/`), different CTA registers (operational vs marketing), and different locale coverage (commerce is IT-only v1, preview has 5 locales). Consolidate when commerce gets i18n in Phase 3b.

### Reusable recipe (for adding a new operational storefront)

When a 3rd ecommerce template ever ships a real shop:
1. Flip `tier=published_live` via the existing sync_template_tiers pipeline (Session 41 recipe).
2. Decide which skin to reuse: `artisan-workshop` for warm-artisan macros (Aesop/Toscana/soulful), `fashion-editorial` for maison-editorial macros (Hermès/Vogue/gold-on-ink). If the sibling is semantically as far from both as Bottega is from Luxe, only then split a new skin under `Storefront.Skin`.
3. Extend `seed_commerce.py` with a new `_seed_storefront(...)` call passing `template_slug`, the collections list, products list, shipping methods.
4. `python manage.py seed_commerce` — idempotent, safe to run repeatedly.
5. If a new skin: add its directory under `templates/commerce/skins/<new-skin>/` with the 5 page templates. Set `--cx-*` tokens in `_base.html`. The `commerce.css` widget CSS follows automatically.
6. Run `smoke_commerce.py` — it dispatches routes dynamically from Storefront.objects.all() (extend smoke_commerce if adding a 3rd storefront to verify the new routes).

### Do NOT do

- Do NOT fold real commerce operations into `/templates/…/preview/…` URLs. Those URLs are bound by D-053 to the marketing/showcase surface.
- Do NOT add login requirements to `/shop/` customer routes. Guest checkout is first-class.
- Do NOT bypass the `SellerRequiredMixin` on dashboard views — it's the auth gate.
- Do NOT decrement stock in templates or views. Stock mutations live in `apps/commerce/services.py`. Views call services.
- Do NOT remove the `select_for_update` lock from `create_order_from_cart` — it's silent no-op on SQLite dev but activates on production Postgres.
- Do NOT add Stripe directly to `views/customer.py`. Add it to the `_dispatch_payment` switch in `services.py` to keep the provider abstraction intact.
- Do NOT touch `templates/live_templates/**` when working on commerce — those are the preview/showcase templates and must stay frozen. Session 41 D-073 + Session 42 D-074 set the bar; commerce parallels, doesn't replace.
- Do NOT translate commerce UI strings into other locales yet. Commerce i18n is Phase 3b. The commerce pages are IT-only in v1; the preview pages keep their 5 locales.
- Do NOT add a 3rd shipping method "shortcut" like `italy-express` without going through `seed_commerce` or admin — shipping methods are per-storefront scoped and must be created via Storefront.shipping_methods.

### Gotchas (Session 43)

- **Windows `manage.py shell -c` console encoding (cp1252) breaks Unicode print output.** Use plain ASCII in smoke script output, or set `PYTHONIOENCODING=utf-8`. Smokes that use `·`, `→`, `←`, box-drawing chars will crash with `UnicodeEncodeError` on a fresh Windows shell.
- **Django Test Client rejects `testserver` hostname when `ALLOWED_HOSTS = []`.** Pass `Client(HTTP_HOST="localhost")` explicitly. `DEBUG=True` defaults to `['localhost', '127.0.0.1', '[::1]']` — not testserver.
- **`session.session_key` is None until the session is saved.** Calling `request.session.save()` forces it to materialize. The commerce helper `_ensure_session` handles this; don't inline the access in views.
- **`select_for_update` on SQLite is a no-op, the lock fires on Postgres only.** Dev works, production gains the lock automatically. If you test concurrent checkout flows on SQLite, they won't deadlock — they just race like any other SQLite writes.
- **Cart.item_count() is a `Sum` aggregate, not `.count()`.** Calling `.count()` returns the number of CartItem rows (distinct variants), not the total quantity. Use `item_count()` for the nav pill number.
- **Category.subtitle may be empty** on seeded collections. Templates that render `{{ current_collection.subtitle }}` should use `|default:current_collection.title` as fallback. Already applied in the shop.html templates.
- **UpdateCartItemView accepts quantity=0 to mean "remove"** per the service contract. Don't assume the POST body has qty > 0 — the front-end qty input has min="0" because setting to 0 is an intentional remove gesture.

---



## Session 42 — eCommerce Premium Polish: Read This Before Touching Any eCommerce Image, Motion, or DNA Drift Work (2026-04-14)

**Session 42 closed two blockers** the user flagged on Session 41 review: (1) Bottega had visible image gaps + 9 visually-wrong Unsplash IDs (HEAD-200 but rendering blue stilettos / classroom / cat / cupcakes / Bond Street tube / etc.); (2) Luxe was rendering as a polished but motionless poster, lacking the editorial premium presence its maison register requires.

### What's binding (D-074)

1. **Bottega is now archetype-honest typographic-led.** All 6 portrait slots (4 makers in home + founder in atelier + artisan signature in product detail) converted to typographic stamp tiles. NO portrait images on Bottega anywhere. Future ecommerce siblings that fit the warm-artisan macro tone reuse this typographic-stamp pattern (`.aw-maker` with corner-N + BOTTEGA stamp + italic letter crest + name/craft/place/since/quote · `.aw-founder .monogram` circular cream stamp · `.aw-pdp .artisan .monogram` smaller circular). DO NOT re-add portrait images to Bottega — the artisan-workshop DNA was always typographic-led (Session 15 DNA notes); Session 41 drifted, Session 42 returned to the DNA.

2. **Luxe ships ~280 LOC of editorial motion** that reads as italic-thinking unhurried. Hero scale-breathe (14s ease-in-out), italic-axis settle on h1 (1200ms cubic-bezier), counter on KPI bands (slow stagger 160-180ms with tabular-nums), press logo marquee (100s drift), drop card pulsing gold dot, primary button gold panel slide-in, nav links + ghost button + tile + atelier card + maison card + variant pill all get letter-spacing or color hover language. Cubic-bezier(0.16, 0.84, 0.32, 1) is the Luxe motion ease — DO NOT use startup-saas-landing's 200ms snappy timings or glow shadows on Luxe. The reduced-motion fallback is mandatory and already wired.

3. **Image-coherence rule binding for all future authoring:** HEAD-200 ≠ visually correct on Unsplash. The `curl + Read tool` per candidate verification (Session 37 Chiara recipe) is the reliable check. When 6+ slots need verification of specific photographic content (older Italian artisans, fashion editorial models, etc.), prefer ARCHITECTURAL elimination of the photo requirement (typographic substitute, gradient placeholder) over endless candidate hunting. The Session 41 → 42 lesson: respect documented DNA notes BEFORE adding image-dependent elements.

4. **The press strip pattern (`.lm-logo-marquee` from `live-media.css/js`) is now linked in Luxe `_base.html`** — also linked in Pragma + Elevate + Cardio + Derm + Gusto / Chiara / Pixel where used. Future templates that need a logo marquee just need `<link>` + `<script>` + the `<div class="lm-logo-marquee">...<div class="lm-logo-marquee-track">...` markup. The `live-motion.js` duplicates the track automatically for seamless looping.

### Reusable recipe (Session 41 + 42)

When a `published_live` ecommerce template ships from now on:
1. Cross-check DNA notes in `template_dna.py` BEFORE adding ANY image-dependent element. If DNA says "typographic-led", honor it.
2. Author the IT skin + content first under D-047 (every string from `page_data.*` / `site.*` / `chrome.*`).
3. For maker / founder / artisan signature blocks: default to typographic stamp tiles (Bottega pattern) unless the DNA explicitly calls for image portraits AND a verified photo source exists. Fashion-editorial templates (Luxe pattern) default to image portraits with `data-latin` markers preserving Latin proper names + isolated unicode-bidi for AR.
4. Wire IT, flip tier, run sync_template_tiers, validate IT-only with smoke_full.
5. Dispatch 8 parallel sub-agents for locale trees (one per locale × 2 templates) with explicit voice contracts.
6. For motion: choose ONE motion register per archetype and stay in it. Artisan-warm = slow warm 12px rise + 560ms cubic-bezier + paper-shadow stamp lift (no zoom/parallax). Maison-editorial = slow editorial 14-22px rise + 1100-1400ms cubic-bezier + tabular-num counters + scaleX gold underline slides (no glow/bounce). SaaS = snappy 200ms + glow shadows (Elevate pattern, NOT for ecommerce).
7. Validate the full 8-suite matrix + run the dedicated cross-leak smoke for the category.

### Do NOT do

- Do NOT add portrait images to Bottega ever again. The artisan-workshop DNA is typographic-led. Maker stamps + monogram circles are the only acceptable identity markers.
- Do NOT use startup-saas-landing motion timings on Luxe (200ms snappy bounce). Luxe motion is 600-1400ms cubic-bezier(0.16, 0.84, 0.32, 1) — italic-thinking unhurried.
- Do NOT trust HEAD-200 Unsplash IDs blindly. Always visual-verify (Read tool can render JPGs).
- Do NOT introduce real cart/checkout/payment on either template. Conversion patterns stay phone-and-whatsapp (Bottega) and private-request (Luxe).
- Do NOT change `live-media.css/js` linking on Luxe — it now needs the marquee primitive. Pragma + Elevate + Luxe link it; the other 6 `published_live` don't.
- Do NOT touch the 7 pre-existing live templates (cardio/derm/gusto/chiara/pixel/pragma/elevate). 867/867 regression matrix is the gate.

### Gotchas (Session 42)

- **Image-curator sub-agent timed out at 0 bytes output.** The dispatch worked, the agent never wrote. The pivot to architectural typographic conversion was the right call. For future visual-curation needs of >5 slots, dispatch the curator sub-agent BUT also have a typographic fallback ready in case it stalls.
- **Django dev server `--noreload` does NOT auto-pick up file changes.** Bounce on a fresh port after every Python/template edit (8801 → 8802 → 8803 → 8804 → 8805 in this session). Session 19's ghost-server gotcha returns periodically — always restart on a different port to be safe.
- **Same Unsplash ID can render different content at different sizes.** `photo-1543163521-1bf539c55dd2` rendered as a knit pullover at 600×600 thumb but blue floral stilettos at 900×900 product hero. The CDN serves a smart crop based on the dimensions request, and the crop can yield completely different visual content. Always verify at FULL size, not thumbnail size.
- **Marquee CSS `flex: 1; min-width: 0` is required** when `.lm-logo-marquee` lives inside a flex container with other siblings (the press strip's "lbl" label). Without it, the marquee track collapses or overflows. Already applied via `.fe-press .lm-logo-marquee { flex: 1; min-width: 0 }`.
- **Counter values get truncated mid-animation in screenshots.** "44" appearing instead of "45" on a viewport screenshot doesn't mean the counter is broken — it means the screenshot was taken at frame 0.95 of the 1400ms animation. Wait 2s then re-screenshot for the final value, or accept that mid-animation values are visible in a Playwright walk.

---

## Session 41 — eCommerce Live Rollout: Read This Before Touching Any eCommerce or Sibling-Pair Live-Rollout Work (2026-04-14)

**Session 41 closed Phase 2g3.5** — `bottega-shop-artigianale` and `luxe-fashion-store` are flipped to `tier=published_live` with full multipage skins + 5 locales (it/en/fr/es/ar) + real RTL on day one. Catalog floor is now **9/20 published_live across 5 categories** (medical/restaurant/business/portfolio/ecommerce), 9/9 multilingual.

### Catalog state

- 9/20 published_live: cardio · derm · gusto · pragma · elevate · chiara · pixel · **bottega** · **luxe**.
- 11/20 draft: sapore · brace (restaurant Phase 2g3.1) · salute · benessere · famiglia (medical Phase 2g3.2) · vertex · aura (agency Phase 2g3.6) · lex · juris (lawyer Phase 2g3.6) · casa · villa (real-estate Phase 2g3.6).
- Phase 3 (auth/checkout/editor/projects/commerce) remains gated on Phase 2g3.6 closing per D-049/D-053.

### What's binding (D-073)

1. **Bottega + Luxe must STAY OPPOSITE in voice across every locale.** D-054 differentiation is enforced by the new `smoke_ecommerce_rollout.py` cross-leak gate (15 Bottega-only tokens + 16 Luxe-only tokens × 5 locales × 12 pages × 2 directions = 120 leak checks, must always be 0/120). A regression PR that introduces a Bottega vocabulary token on a Luxe page (or vice versa) must be rejected. Voice contracts: Bottega = warm artisan Toscana (Aesop EN, Astier FR `tu`, peninsular `tú` ES, Brownbook AR cultural-publishing); Luxe = maison editoriale (Gentlewoman EN formal, Hermès FR `vous`, Vogue España `usted`, Vogue Arabia luxury-maison AR).
2. **Both ecommerce skin folders are now reusable archetypes.** A future ecommerce sibling that fits the warm-artisan macro tone reuses `templates/live_templates/ecommerce/artisan-workshop/`. A future ecommerce sibling that fits the maison-editorial macro tone reuses `templates/live_templates/ecommerce/fashion-editorial/`. Only when a third sibling is semantically as far from BOTH existing ones as Bottega is from Luxe should a new archetype be split (D-050/D-051 default).
3. **D-047 chrome-cleanliness applied from line one.** Both `_base.html` files + all 12 page templates carry zero IT literals — every label flows from `page_data.*` / `site.*` / `chrome.*`. Future skin edits MUST keep this.
4. **`html[dir="rtl"]` CSS block + conditional Amiri/Noto-Kufi font load on both bases.** Bottega uses Amiri body + Noto Kufi Arabic display (warm classical for the artisan voice). Luxe uses Amiri body + Noto Kufi Arabic display (classical for the maison voice). Latin proper names (La Bottega di Martino, Maison Luxe, Vogue Italia, The Gentlewoman, Hermès, Bottega Veneta, Lesage, Goyard, IMG Models, Grand Hôtel Villa d'Este, Setificio Tessitura Como, Maglificio Lanifer Biella, Conceria della Madonna, Atelier Sentier, Severino Falchi, Caterina Lippi, Bruno Ricci, Adele Pignatelli, Giulia Maison, Carla Sozzani, Letizia Carrera, Jean-Luc Berthier, Yumi Tanaka), prices (€ 420, € 95, € 2.480, € 1.290, € 860), edition numbers (N° 042, 3/8, Look 03, Drop 02, SS26), phone numbers (+39 055 234 11 90, +39 02 7600 1492, +33 1 4296 4720, +81 3 6450 5018), Italian city names (Firenze, Toscana, Santa Croce sull'Arno, Montelupo Fiorentino, Prato, Greve in Chianti, Milano, Brera, Sentier, Aoyama) all stay Latin via `unicode-bidi: isolate` (Bottega) or `[data-latin]` markup attribute (Luxe).
5. **Native voice per locale, never machine translation.** Bottega EN reads as native Aesop. Luxe EN reads as native The Gentlewoman. Bottega FR uses `tu` + `« »`. Luxe FR uses `vous` + `« »` + insecable spaces. Bottega ES uses `tú` + peninsular vocabulary. Luxe ES uses `usted` + peninsular maison vocabulary. Bottega AR uses cultural-publishing register. Luxe AR uses luxury-maison register. Future content edits MUST follow these per-locale per-template voice contracts.
6. **WhatsApp link is a Bottega-only conversion pattern.** Bottega's nav CTA + final CTA + contact card all expose WhatsApp via `{{ site.whatsapp_link }}`. Luxe NEVER carries WhatsApp — its conversion is private viewing by appointment. The cross-leak smoke enforces this: "WhatsApp" appearing on a Luxe page = D-054 violation.
7. **Page slugs stay Italian (URL-canonical).** Bottega: home, shop, product, atelier, journal, contatti. Luxe: home, collezione, product, maison, lookbook, contatti. Only `label` fields change per locale (e.g., "Catálogo" vs "Catalogue" vs "Shop" vs "الكتالوج"). Slugs are IT — never translate.

### Reusable recipe (now proven 6 times: Cardio · Derm · Gusto · Chiara · Pixel · Pragma + Elevate · **Bottega + Luxe**)

The Session 23/29/37/39/40/41 recipe is now stable enough to be a checklist:
1. Author both IT content registries first (D-047 from line one — never paste literals, every string flows from `page_data.*` / `site.*` / `chrome.*`).
2. Author both skin folders next.
3. Wire IT into `template_content.py` + flip tier in `TEMPLATE_REGISTRY.json` + `python manage.py sync_template_tiers`. Validate IT-only with `smoke_full.py`.
4. Dispatch 8 parallel sub-agents (one per locale × 2 templates) with explicit voice contracts that articulate the differentiation gate as a "must NOT contain X" + "must contain Y" pair.
5. While agents work: extend `smoke_full.py` + `smoke_forms.py` + `smoke_i18n_media_hardening.py` + author a new `smoke_<category>_rollout.py` that codifies the D-054 cross-leak gate.
6. When agents return: run the full validation matrix (manage.py check + 4 smokes + 3 regression smokes).
7. Update memory + DECISIONS + SESSION_LOG + TODO_NEXT + AGENT_HANDOFF + CATEGORY_ROADMAP + TEMPLATE_REGISTRY in a single follow-up commit.

When opening any future ecommerce session, read `ecommerce_live_rollout_session41.md` in memory before starting.

### Do NOT do

- Do NOT collapse Bottega + Luxe voices into one shared register — they must stay sharply distinct across every locale.
- Do NOT use machine translation for any locale block. The quality floor is native Aesop / Gentlewoman / Astier / Hermès / Vogue España / Vogue Arabia editorial voice per template per locale.
- Do NOT introduce a real cart/checkout/payment/auth flow on either ecommerce template. The conversion patterns are deliberate demos: phone-and-whatsapp (Bottega) and private-request (Luxe). A real commerce engine is Phase 3 work, gated on Phase 2g3.6 closing.
- Do NOT translate Italian page slugs (`shop`, `product`, `atelier`, `journal`, `contatti`, `collezione`, `maison`, `lookbook`) to non-IT equivalents — URLs stay canonical Italian, only labels change per locale.
- Do NOT add WhatsApp anywhere on Luxe — it's the Bottega-only conversion marker.
- Do NOT add Drop/Lookbook/Private Viewing vocabulary anywhere on Bottega — they're Luxe-only maison markers.
- Do NOT touch the 7 already-multilingual templates (cardio/derm/gusto/chiara/pixel/pragma/elevate) when working on ecommerce. Regression smokes (76/76 chiara · 80/80 pixel · 52/52 gusto · 363/363 full sweep) are the binding gate.

### Gotchas (Session 41)

- **Add `product` to `pages` array even if it's a detail page.** First validation pass failed because the registries had `product` as a content block but not in the `pages` list — the LiveTemplateView's `find_page` lookup 404'd. The simplest fix is to add it as a navigable page (`{"slug": "product", "label": "Pezzo|Look", "kind": "product"}`). For a "real" product detail with multiple drilldown variants, the post mechanism (`/preview/<page>/<post_slug>/`) would be the right path, but requires a content registry with a `posts` list.
- **`smoke_forms.py` `lf-select` marker is exact-match `class="lf-select"`.** A `<select class="lf-select lf-input">` element does NOT match. The reference pattern (Pragma/Elevate use it) is `<div class="lf-select" data-lf-label="…"><select class="lf-input">…</select></div>` — wrap the native select in a `lf-select` div, put `lf-input` on the select.
- **8 stub locale files needed during bootstrap.** When the import-block at the bottom of `template_content.py` references `BOTTEGA_CONTENT_EN` etc. but the sub-agents haven't authored them yet, Python ImportError aborts the whole catalog. Workaround: create stub files first that re-export `..._CONTENT_IT as ..._CONTENT_EN` so the import succeeds; sub-agents overwrite each stub with their full locale tree. The validation chain stays green throughout.
- **The legacy preview composition files (`templates/preview_compositions/ecommerce/{artisan-workshop,fashion-editorial}.html`) still carry their original 10+/12+ Bottega/Luxe literals.** They are deliberately untouched in this session. They are used only for the static listing PNG via the Playwright pipeline. Lifting them is a separate, cosmetic-only Phase 2g2x.3 leftover that doesn't affect the live preview tier — and is now particularly low-priority because the live preview is the primary surface, the static listing PNG is decorative.
- **`Maglificio Lanifer` was first listed in BOTTEGA_ONLY_TOKENS in the smoke** (typo from the cross-leak audit) — it's actually a Luxe-only fabric house (Lanifer Biella). The smoke includes a sanity-fix `tuple(t for t in BOTTEGA_ONLY_TOKENS if t != "Maglignifico Lanifer")` to strip it. Future tokens authored for cross-leak must be verified against both content trees before being added to the gate.
- **`data-latin` HTML attribute is a Luxe-only convention** for marking Latin proper names that need `unicode-bidi: isolate` in RTL CSS. Bottega's RTL CSS uses selector-based isolation instead (`html[dir="rtl"] .aw-nav .wm` etc.). Both work — the choice is per-archetype style, not a contract. Future templates can pick either pattern but must not mix them on the same skin.

---

## Session 40 — Pragma + Elevate i18n: Read This Before Touching Any Multilingual or Business Template Work (2026-04-14)

**Session 40 closed Phase 2g3.3b** — the 7-template `published_live` catalog now ships **7/7 multilingual** with real RTL for Arabic. `pragma-corporate-suite` and `elevate-startup-landing` were the last 2 IT-only live templates. Both keep their sharply distinct voices: Pragma institutional B2B advisory · Elevate SaaS growth-tech.

### Catalog state

- 7/7 published_live ship in 5 locales: cardio · dermatologia · gusto · chiara · pixel · **pragma** · **elevate**.
- Multilingual coverage on the public catalog is closed. Phase 3 (auth/checkout/editor/projects/commerce) remains gated on Phase 2g3.7 (all 20 templates published_live) per D-049 + D-053. 7/20 published_live, 13/20 still draft.

### What's binding (D-072)

1. **Pragma + Elevate must STAY OPPOSITE in voice across every locale.** D-054 differentiation is enforced by sub-agent voice contracts. Pragma uses formal institutional registers (FT/HBR EN, vouvoiement FR, peninsular usted ES, MSA boardroom AR with dropped honorifics). Elevate uses SaaS founder-facing registers (TechCrunch/Linear EN with contractions, modern SaaS FR with `tu`, peninsular `tú` ES with anglicismes, modern startup MSA AR with Latin product names + Latin acronyms). Future content edits MUST preserve this. A regression PR that homogenizes the two templates into one voice should be rejected.
2. **9 D-047 leaks lifted** are now `page_data.*` / `site.*` fields. Future skin edits MUST keep this — no IT labels in HTML, ever. Particular gotcha: `pricing.html` `Più scelto` was a CSS pseudo-element `content: 'Più scelto';` (CSS-generated content can't be localized via Django templates) — it was moved to HTML `<span class="pop-badge">{{ page_data.highlight_badge }}</span>` rendered conditionally. Don't revert to CSS pseudo-element badges for any locale-bound text.
3. **Both business archetypes have full `html[dir="rtl"]` CSS blocks** with conditional Arabic font load + page-level grid flips inside `{% if is_rtl %}` + Latin wordmark / Latin product name / Latin numeric isolation via `unicode-bidi: isolate`. Skin edits that add new components MUST add their RTL-flip rules in the same commit (otherwise AR ships visually broken).
4. **Native voice per locale, never machine translation.** Pragma EN reads as native FT/HBR. Elevate EN reads as native TechCrunch/Linear. Pragma FR uses vouvoiement + insecable spaces. Elevate FR uses `tu` + insecable spaces + anglicismes. Pragma ES uses peninsular `usted`. Elevate ES uses peninsular `tú`. Pragma AR uses MSA boardroom with dropped honorifics. Elevate AR uses modern startup MSA with Latin product names. Future content edits MUST follow these per-locale voice contracts.
5. **Latin proper names + Latin product names + Latin acronyms preserved across all locales.** Pragma: partner Italian names (Federico Seregni, Caterina Foschini, Marco Lavezzi, Sabina Erlanger, Lorenzo Pellizzari, Giulia Antinori), Italian institutions (Bocconi, Insead, Cattolica, Politecnico, Bonelli Erede, McKinsey), CONSOB acronym, technical acronyms (CSRD, ESG, M&A, EBITDA). Elevate: founder Italian names, all SaaS product names (Stripe, Linear, Slack, Vercel, PostHog, GrowthBook, Loops, Cal.com, Plain, Resend, Cloudflare, Netlify, Next.js, React, Postgres, Prisma, Neon, Clerk, JetBrains Mono), version strings (v2.5–v3.0), all SaaS acronyms (MRR, ARR, A/B, PMF, KPI, CLI). Latin Western digits (1, 2, 3, …) used for prices/percentages/years in AR per MENA business-press convention.

### Reusable recipe (now proven 5 times: Cardio · Derm · Gusto · Chiara · Pixel · **Pragma + Elevate**)

The Session 23/29/37/39 recipe scales to a 2-template, 8-tree fan-out without modification. The only addition: an upfront D-047 leak sweep on BOTH skin folders before authoring (otherwise the new locale trees inherit IT-hardcoded labels). For business templates specifically, also lift any CSS pseudo-element content (`::before content: "…"`) to HTML rendered from a content field — CSS-generated content cannot be localized through Django templates.

When opening any future i18n session that touches business templates, read `business_i18n_completion_session40.md` in memory before starting.

### Do NOT do

- Do NOT collapse Pragma + Elevate voices into one shared register — they must stay sharply distinct across every locale.
- Do NOT use machine translation for any locale block. The quality floor is native FT/HBR/Les Echos/Cinco Días/Wamda/Maddyness editorial voice per template per locale.
- Do NOT add CSS pseudo-element `content: '…';` for any locale-bound visible text. Lift to HTML rendered from `page_data.*` / `site.*` / `chrome.*`.
- Do NOT touch the 5 already-multilingual templates (cardio/derm/gusto/chiara/pixel) when working on business templates. Regression smokes (76/76 chiara · 80/80 pixel · 52/52 gusto · 282/282 full sweep) are the binding gate.
- Do NOT translate Italian page slugs (`prodotto`, `prezzi`, `demo`, `contatti`, `chi-siamo`, `competenze`, `case-studies`) to non-IT equivalents — URLs stay canonical Italian, only labels change.

---

## Session 37 — Chiara Perfection: Read This Before Touching Any Locale Rollout (2026-04-13)

**Session 37 brought `chiara-portfolio-creativo` to gold-standard product quality** — full 5-locale i18n (it/en/fr/es/ar) + editorial-designer-coherent imagery (laptop stock photos retired) + skin-HTML literal lift × 9 sites + mobile horizontal overflow fix (124px → -15px) + `html[dir="rtl"]` CSS block + a11y focus rings. Single template only — no other live template touched except smoke harness + cross-template chrome.

### Catalog state

- 4/7 published_live ship in 5 locales: **cardio · derm · gusto · chiara**.
- 3/7 IT-only: **pragma · elevate · pixel** (next targets for Phase 2i.2c-d).

### What's binding (D-070)

1. **Every chiara live route renders in 5 locales** with structural parity (same `pages` slugs/kinds, same key shapes, locale-specific labels + content). Verified via `smoke_chiara_perfection.py`.
2. **Skin HTML zero-leak.** The 9 hardcoded Italian literals previously in `editorial-designer-grid/*.html` are now `page_data.*` fields. Future skin edits MUST keep this — no labels in HTML, ever. Smoke checks this on lift sites.
3. **Editorial-designer imagery only.** No laptop / coding / businessperson / generic-office stock photos in any chiara surface. The 5 new IDs (`photo-1611532736597-de2d4265fba3` Triennale, `photo-1497633762265-9d179a990aa6` Adelphi, `photo-1564399579883-451a5d44ec08` Querini, `photo-1455390582262-044cdead277a` Velluti, `photo-1544717305-2782549b5136` Founder) are the references. Old laptop IDs are scrubbed.
4. **Native voice per locale**, never machine translation. FR uses `vous` + `« »` + insecable spaces + French ordinals (24ᵉ). ES uses `usted` form throughout. AR keeps proper names in Latin script + Latin digits for technical data + uses `، ؛ ؟` and `« »`.
5. **Mobile horizontal overflow at 390px viewport: ≤ 0px.** Inline-styled `<div class="head" style="display:grid; grid-template-columns: 0.45fr 1fr">` patterns require `!important` overrides at `@media (max-width: 720px)` to collapse — the Session 37 home.html fix is the precedent.
6. **a11y focus rings on every CTA.** `.ed-btn-primary` + `.ed-btn-ghost` have `:focus-visible` 2px accent outline + 4px offset. Future buttons must follow.

### Reusable recipe (now proven 4 times: Cardio · Derm · Gusto · Chiara)

1. **Lift literals** out of skin HTML into `page_data.*` content fields BEFORE authoring locale trees. Otherwise the 4 non-IT trees miss labels.
2. **Spawn 4 parallel sub-agents**, one per locale (EN/FR/ES/AR). Give each: full IT source path, exhaustive voice guidelines (proper names verbatim, taxonomy translations, typography conventions, idiomatic register), output spec (Python module mirroring IT shape exactly).
3. **Spawn 1 image curation sub-agent** (if imagery is off-brand). Method: download via curl + inspect via Read tool per candidate, reject laptops/phones/lifestyle, output verified IDs with rationale per slot.
4. **In parallel** to the agents: do the RTL CSS block + Arabic font conditional + mobile breakpoint fixes + a11y focus rings on the skin's `_base.html`. These are 100% skin-side, don't need content trees ready.
5. When agents return: verify structural parity via deep keyset diff (must be 0 missing / 0 extra per locale). Wire imports into `template_content.py` `TEMPLATE_CONTENT` dict. Apply image swaps to all 4 locale trees via batch script. Extend `smoke_full.py` LOCALES list. Migrate template from `IT_ONLY` to `MULTILINGUAL` in `smoke_i18n_media_hardening.py`. Add a per-template content-marker smoke (signature phrase per locale + RTL marker + image swap verify + IT-leak sweep).
6. Run full validation matrix: `check`, `smoke_full`, `smoke_forms`, `smoke_i18n_media_hardening`, `smoke_<template>_perfection`. All must be green. Playwright walk on 1440×900 × 5 locales + 390×844 mobile.

### Do NOT do

- Do NOT use machine translation for any locale block. The quality floor is native editorial voice. A PR that ships auto-translated content should be rejected.
- Do NOT add new content blocks to chiara IT tree without mirroring in all 4 non-IT trees at the same commit (D-069 silent-disparity rule — adding to IT only creates content-depth disparity that the `{% if page_data.X %}` guard hides).
- Do NOT use laptop/coding/businessperson stock photos anywhere in chiara. Editorial designer identity is print/type/paper/ink/signage/manuscript matter only.
- Do NOT remove the `html[dir="rtl"]` CSS block from `editorial-designer-grid/_base.html` even if no AR content exists later — it's load-bearing for any RTL locale future-state.
- Do NOT translate page slugs. Only `label` fields change per locale. URLs stay Italian (`/lavoro/`, `/processo/`, `/contatti/`).
- Do NOT transliterate proper names in AR. Chiara stays "Chiara", not "كيارا". Triennale stays Latin.
- Do NOT introduce Django gettext / .po / middleware. D-059 still binding.
- Do NOT open auth / checkout / editor / projects / commerce / dashboard / new categories / new templates.

### Gotchas (Session 37)

- **Django template tag literals inside CSS comments are still parsed.** A CSS comment like `/* guarded by {% if is_rtl %} below */` will be interpreted as an actual `{% if %}` tag (with no matching `{% endif %}` in scope) and crash `TemplateSyntaxError`. Workaround: use plain text in CSS comments, never reproduce literal tag syntax. Caught + fixed during Session 37.
- **Inline `style=` attributes have specificity 1,0,0,0** — beats normal class selectors. To override an inline style at a media query, use `[style]` attribute selector + `!important`. Session 37 mobile fix uses `.ed-press .head h2[style] { font-size: 28px !important; max-width: 100% !important; }`.
- **CSS Grid items default to `min-width: auto`** (= min-content). For text, min-content is the longest single word. Italian "pubblicazioni" or Arabic display words can force a grid column wider than the viewport. Fix: explicit `min-width: 0` on grid children at mobile breakpoints. Session 37 added this for `.ed-press .head[style] > *`.
- **Browser cache + dev server combo is a pitfall.** After major template changes, kill + restart dev server on a fresh port (e.g. 8767 vs 8765). The Session 37 mobile fix appeared not to apply until the server was bounced — same class as Session 19's ghost-server gotcha and Session 23's stale `runserver --noreload` trap.
- **Smoke patterns must avoid Romance-language word collisions.** Italian "Disciplina" / "Colophon" / "Metro" are valid Spanish/English/French words too — checking for them as "IT leak" produces false positives on EN/FR/ES pages. Session 37 smoke restricts the leak pattern to IT-specific phrasings ("Sintesi del progetto", "Deliverable consegnati", "Sequenza", "Indirizzo", "Ingresso", "Orari", "Equipe" without French acute accent, etc.).
- **Latin proper names + Latin digits + Arabic body text** is the editorial AR voice — don't transliterate. The CSS `font-family` stack keeps Latin runs in JetBrains Mono / Latin fallback so they stay legible against Amiri body. The cardio/derm/gusto AR pages all do this; chiara now joins.
- **Sub-agent prompts must mention the actual IT key shape.** Session 37 prompt initially mentioned `ledger_count_format` / `step_index_format` (placeholder format-strings) but the IT source actually uses pair-form keys (`_prefix` + `_unit`). All 4 sub-agents independently caught this via deep-comparison and corrected to mirror the true IT shape — flagged as a lesson for future locale rollouts: always read the IT source first, not the prompt's key list.

---

## Session 36 — i18n & Media Coherence: Read This Before Adding New Blocks or Promoting IT-Only Templates (2026-04-13)

**Session 36 is a hardening pass on Session 35's motion/media work (D-068).** The 7 `tier=published_live` templates now satisfy two coherence gates the user flagged:

1. **Language switcher honesty.** The 4 IT-only templates (Pragma, Elevate, Chiara, Pixel) no longer show a 5-pill switcher that silently fell back to Italian. `locale_switcher_entries(current_locale, available_locales)` is now template-aware, and `LiveTemplateView` computes `available_locales` via `template_content.get_available_locales(slug)`. When `len <= 1`, the switcher context value is an empty list and every skin's markup is guarded by `{% if locale_switcher %}`. The 3 multilingual templates (Cardio, Derm, Gusto) keep their 5-pill strip as before.

2. **Media honesty.** The 3 `lm-video` blocks introduced in Session 35 all shipped with the same Big Buck Bunny placeholder MP4 and codec-theatre metadata. They are now resolved per-archetype:
   - **Gusto signature_video** — REMOVED (content block + HTML + CSS). The atmosphere_teaser lightbox already carries BTS mood.
   - **Pixel reel** — REMOVED. The filmstrip + EXIF strip + series index already carry the cinematic identity.
   - **Elevate product_video** — CONVERTED to `product_demo_card`: same cosmic-glass frame + dashboard poster, now with a dual CTA overlay pointing to `/demo/` + `/prodotto/`. No `<video>` tag, no codec metadata.
   - **Pragma + Elevate marquees** — kept (real institutional B2B wordmarks + real SaaS integration names).

Orphan `live-media.css/js` links + `--lm-video-*` tokens pruned from bases that no longer consume them (Cardio, Derm, Gusto, Chiara, Pixel). Pragma + Elevate still link the primitive because they render marquees.

### Current stable state

- 7/20 templates `tier=published_live` (unchanged from Session 34).
- All 7 pass D-069 coherence gates.
- 170/170 full route sweep + 27/27 form sweep + 45/45 new hardening smoke (`smoke_i18n_media_hardening.py`) all green.
- `live-media.css/js` remains in the repo as a latent capability — re-introduce when a real signed MP4 and on-brand metadata exist.

### What to do next (priority order)

1. **Phase 2g3.5 — agency CRITICO lift.** Same D-047 + D-054 recipe as Sessions 17 / 18 / 32 / 34. Blocking roadmap gate per D-049.
2. **Phase 2i.2b — IT-only template locale rollout.** Author EN/FR/ES/AR content trees for Pragma / Elevate / Chiara / Pixel (one per session, ~3h each per D-063 budget). When `TEMPLATE_CONTENT[slug]` gains a second locale key, the switcher reappears automatically — the `{% if locale_switcher %}` guards installed in Session 36 already handle the re-activation.
3. **Phase 2g2x.1 remainder** — lift lawyer + real-estate CRITICO. Same DNA-split recipe (Sessions 17–19 precedent).
4. **Editor app** — do NOT start until Phase 2g3.7 closes. D-049 roadmap freeze still in effect. When it starts, `EDITOR_SCHEMA_BLUEPRINT.md` is the contract.

### Do NOT do

- Do NOT re-introduce a placeholder MP4 as an `lm-video` src. Either the source is a real brand asset or the block is not in the template. D-069 is binding.
- Do NOT ship a 5-pill language switcher on a template whose `TEMPLATE_CONTENT[slug]` has only one locale key. D-069 is binding.
- Do NOT add codec-theatre metadata (`4K`, `1080p`, `24 fps`, `Play · 3:12`) to any block where it does not genuinely reinforce the template's identity.
- Do NOT add a new content block on the IT tree without either (a) mirroring it in the 4 non-IT locale trees at the same commit or (b) documenting that the block is IT-only-intentional in a comment adjacent to the key. Silent content-depth disparity between locales is the Session 35 antipattern that produced the Session 36 cleanup.
- Do NOT revert the `live-media.css/js` unlinking on cardio/derm/chiara/pixel/gusto bases unless you are re-adding a real `lm-video` block at the same commit. Orphan primitive links are payload dead-weight.
- Do NOT open auth / checkout / editor / projects / commerce / dashboard / new categories / new templates.

### Gotchas (Session 36)

- **CSS rules for `.mp-lang*` appear in the inline `<style>` block on every page** — this is structural, not rendered chrome. Smoke tests for "switcher absent" must look for `<div class="mp-lang"` / `<nav class="mp-lang"` opening tags, not the class name alone. `smoke_i18n_media_hardening.py` does this correctly.
- **The `--lm-video-*` CSS custom properties were spread across many `:root` blocks.** Removing them requires touching every skin `_base.html` that linked live-media.css speculatively (cardio/derm/gusto/chiara/pixel). Pragma + Elevate keep their `--lm-marquee-*` tokens because they still render marquees.
- **Elevate's `.sl-product-video .head .sec-label.sl-mono` specificity-shielded selector** must be renamed to `.sl-demo-card .head .sec-label.sl-mono` after the video→demo_card conversion, otherwise the mono utility silently stops working on that element. Check any rule that chains on deprecated class names whenever a section is renamed.
- **The `--lm-video-*` specificity rule `.lm-video .lm-video-play-label.cp-mono` in the cinematic-photographer base** was orphaned after the reel removal. Pruning it was part of the cleanup. Same class of orphan risk for any future skin that declares `.lm-video` specificity-shielding rules: if the block is later removed, the rule becomes dead.
- **Elevate's existing `.sl-btn` has a `::after { content: '→' }` globally.** Adding a custom `<span class="arr">→</span>` inside a button duplicates the arrow. The demo card uses the standard `.sl-btn` primary + `.sl-btn.secondary` classes and lets the global arrow handle the glyph. When extending a button class, check for `::after` content before adding custom glyphs.

---

## Session 30 — Premium Component Blueprint: Read This Before Adding Sections or Opening the Editor (2026-04-13)

**Session 30 enriched the 3 `tier=published_live` templates with DISTINCT premium sections per archetype AND authored a concrete Editor Schema Blueprint** (~600 lines, `EDITOR_SCHEMA_BLUEPRINT.md` in repo root). The blueprint is binding for the future customer-personalization editor app.

### What was added (distinct per template by design)

| Template | New sections | New interactions |
|----------|-------------|-----------------|
| Cardio | anchor subnav + "Percorso paziente" 5-step timeline + "Garanzie & trasparenza" trust strip + location block with static map | anchor-nav (IO active state + smooth scroll) |
| Derm | Treatment tabs (3 domains: clinica/chirurgia/estetica) + Before/After compare slider with ethical disclaimer + Editorial press feed 4-tile | Tabs (keyboard nav), Compare slider (mouse/touch/keyboard) |
| Gusto | Producer showcase (4 artisans) + Private dining card (Chef's Table / evening buy-out / cellar tasting) + Wine program (sommelier + pairings + cellar facts) | — (reuses existing lightbox) |

All sections conditional on `page_data.X` so the shared specialist skin never renders the wrong set on the wrong template.

### New interaction primitives (live-interactions.css/js)

- `[data-li="tabs"]` — keyboard-accessible tab bar with fade panel transitions.
- `[data-li="compare"]` — before/after slider, mouse+touch+keyboard, clip-path driven.
- `.li-anchor-nav` — sticky subnav with IntersectionObserver active state.

All zero-dep, `prefers-reduced-motion` aware, graceful without JS.

### i18n coverage

All new sections authored in all 5 locales (it/en/fr/es/ar) for all 3 templates. Native editorial voice per locale — no machine translation. Proper names stay Latin across AR.

### Current stable state

- 3 published_live with FULL premium depth (~650+ lines per home, dense with motion + interactions + per-archetype sections).
- 85/85 routes 200 across all locales + pages.
- Cross-contamination zero. Differentiation strong.
- 17 drafts unchanged.

### Editor Schema Blueprint (EDITOR_SCHEMA_BLUEPRINT.md)

Concrete (not theoretical). Covers:
- Component registry: 8 edit targets (nav/hero/section/form/contact/blog/footer/locale).
- 20+ section kinds with items shapes.
- 23 atomic field types for editor UI.
- Design tokens scope (palette/fonts/radius/motion_profile/density/alignment).
- 6 hard invariants (D-047, D-053, D-054, D-057, D-058, D-059).
- Persistence model (CustomerProject + ProjectContent + ProjectDesignTokens) — specified, not migrated.

When Phase 2g3.7 closes and the editor worktree opens, this document is the implementation TODO. Read it end-to-end before touching `apps/editor/`.

### Do NOT do

- Do NOT add premium sections to drafts. Phase 2g3 authoring follows a different flow (full skin folder, then enrichment).
- Do NOT replicate the same section set across the 3 templates — that would collapse the D-054 differentiation earned in Sessions 26/28/30.
- Do NOT start implementing the editor until Phase 2g3.7 is green. D-049 roadmap freeze is still in effect.
- Do NOT add arbitrary Google Fonts to templates. The blueprint curates 18. Anything else regresses D-040.
- Do NOT modify `live-motion.css` tokens per-template — use motion_profile from the blueprint.
- Do NOT machine-translate any locale block. Native editorial voice remains non-negotiable.
- Do NOT add `href="#"` placeholders. Every CTA must resolve.
- Do NOT wire a compare slider inside an RTL-first section without confirming label flip works. The drag itself is LTR-mouse-driven by design.

### What to do next (priority order)

1. **Phase 2g3.1** — author Sapore + Brace restaurant skin folders. They inherit restaurant-generic CHROME_I18N keys from Session 29 for free. When their homes are ready, they can optionally opt into a subset of new primitives (e.g., anchor-nav for long trattoria menus; tabs for Brace delivery vs dine-in).
2. **Phase 2g2x.1 remainder** — lift agency / lawyer / real-estate CRITICO. Same Option A recipe (Sessions 17–19 precedent, now with even more authored sections to reference).
3. **Phase 2i.3 deferred** — marketplace chrome i18n lives when Phase 3 unblocks.
4. **Editor app** — do NOT start until 2g3.7 green. When it starts, `EDITOR_SCHEMA_BLUEPRINT.md` is the contract.

### Gotchas (Session 30)

- Clip-path animation on the compare slider is JS-driven (inline `clipPath` overrides CSS). To flip direction per-locale, change the JS, not the CSS.
- The `.sp-compare .cmp-box` container MUST have `tabindex="0"` for keyboard accessibility. Missing it breaks ←/→ control.
- The anchor-nav IntersectionObserver rootMargin is `-100px 0px -50% 0px` — tuned so a section "becomes active" when it's ~halfway up the viewport, not as soon as a pixel touches top.
- Windows cp1252 console cannot print Arabic in stdout. Smoke scripts need `sys.stdout.reconfigure(encoding='utf-8')` or ASCII-only output. Same gotcha as Session 29.
- New section CSS blocks (e.g., `.sp-tabs`, `.sp-compare`) live in the SHARED specialist `home.html` style block. Cardio renders the CSS but not the HTML (content-conditional). This is intentional: the CSS cost is negligible (~40KB unminified), and splitting into two home.html files would break the D-046 archetype-reuse recipe.

---

## Session 29 — Gusto i18n/RTL: Read This Before Touching Multilingual Publishing (2026-04-13)

**Session 29 closed Phase 2i.2 in full.** All 3 `tier=published_live` templates (cardio, dermatologia-elite-roma, gusto-fine-dining) now ship in 5 locales (it/en/fr/es/ar) with real RTL for Arabic. The pilot architecture (D-059) is validated across two archetypes — specialist (medical) and fine-dining (restaurant).

### What was added
- `apps/catalog/template_content_gusto_i18n.py` — 4 hand-authored content trees (EN/FR/ES/AR) for gusto, ~1250 lines, restaurant-hospitality native voice per locale.
- 9 new CHROME_I18N keys × 5 locales: `mp_other_restaurant`, `foot_restaurant`, `foot_concierge`, `foot_services`, `fd_wine_pairing`, `fd_email_label`, `fd_phone_label`, `blog_read_article`. These are restaurant-category-generic → reusable by draft Sapore + Brace in Phase 2g3.1.
- Gusto-specific content keys on `GUSTO_CONTENT_IT` for every previously-hardcoded HTML literal (~30 new keys across home/filosofia/menu/atmosfera/diario/prenota).
- `html[dir="rtl"]` CSS block inside `fine-dining/_base.html` — core RTL tokens always applied, page-level `.fd-*` flips inside `{% if is_rtl %}` so LTR pays zero CSS cost.
- Conditional Amiri + Noto Kufi Arabic Google Fonts (only loads for AR).
- Language switcher pill strip in mp-bar, `?lang=` URL preservation on every nav/footer/CTA link.
- Reservations form rewritten as a `{% for field in page_data.form_fields %}` loop with conditional rendering by type + index.

### Current stable state
- **3 published_live templates:** cardio + derm (medical specialist archetype, i18n in 5 locales since Session 23/24) + gusto (fine-dining archetype, i18n in 5 locales since Session 29).
- **All 3 have motion active** (D-058 + D-061) and ultra-premium sections (D-062).
- **17 draft templates:** hidden from public, IT-only.
- **52/52 routes green** in Session 29 smoke test (35 gusto + 10 cardio regression + 5 derm regression + 2 negative).

### The reusable recipe (now proven twice)
1. Create `template_content_<slug>_i18n.py` with 4 locale trees (EN/FR/ES/AR). Premium editorial voice per locale. No machine translation.
2. Wire into TEMPLATE_CONTENT registry (4 lines: import + 4 locale keys).
3. Extend CHROME_I18N with archetype-generic keys if needed (restaurant-generic keys from Session 29 are already done for any future restaurant archetype).
4. Add all hardcoded HTML labels to the `*_IT` content block as new keys, then mirror in the 4 locale trees.
5. Wire HTML templates: `{{ chrome.* }}` for cross-archetype chrome, `{{ page_data.* }}` for brand-specific labels, `{{ site.* }}` for site-wide chrome (wordmark, copyright, footer hours).
6. Add `?lang=` preservation to every URL: `{% url '...' %}{% if locale != default_locale %}?lang={{ locale }}{% endif %}`.
7. Author `html[dir="rtl"] ...` CSS block inside the archetype's `_base.html` with (a) core typography tweaks (Amiri + Noto Kufi Arabic, 17px body / 1.85 line-height, letter-spacing flatten, arrow/bar flips), plus (b) page-level section flips inside `{% if is_rtl %}` for grid flipping + border-side swap + drop-cap float + column alignments.

Budget per template: ~3h (same as Session 29 estimate).

### What to do next (in priority order)
1. **Phase 2g3** — live skin folder authoring for draft templates, cheapest-first per CATEGORY_ROADMAP.md. Restaurant first (Sapore + Brace) — they'll inherit the 7 restaurant-generic CHROME_I18N keys for free, and the i18n/RTL pattern is proven.
2. **Phase 2g2x.1 remainder** — lift the 3 CRITICO categories (agency, lawyer, real-estate) with DNA splits. Pattern proven in Sessions 17–19.
3. **Phase 2i.3 (deferred to Phase 4)** — marketplace chrome i18n. Keep `CHROME_I18N` as the natural migration target if/when the marketplace surface moves to Django `{% trans %}`.

### Do NOT do
- Do NOT re-author the i18n architecture — the pilot closed in full. D-059 + D-063 are binding.
- Do NOT introduce Django gettext/.po/middleware. Same as Session 23/24/29.
- Do NOT translate draft templates. Only `tier=published_live` is in 2i scope.
- Do NOT translate marketplace chrome (homepage, listing, detail, category, search) — deferred to Phase 4.
- Do NOT modify cardio or derm i18n content without a documented reason. They're load-bearing regression baselines.
- Do NOT touch Gusto motion tokens (`--lm-rise: 14px`, image zoom, nav sweep) — they're intentionally different from the medical clinical profile.
- Do NOT add counter animations to medical templates (D-061 exclusion).
- Do NOT machine-translate any new locale block. Native editorial voice is the non-negotiable quality floor.
- Do NOT strip Latin from the Arabic font stack — mixed Latin/Arabic strings (chef names, producer names, wine names, press outlets, phone, email, address) must stay legible.
- Do NOT apply negative `letter-spacing` or 0.22em uppercase tracking on Arabic headings/chrome labels — the `html[dir="rtl"]` core block explicitly zeroes these.
- Do NOT open auth/checkout/editor/projects/commerce (Phase 3 gated by Phase 2g3.7).
- Do NOT add new categories or templates before the 20 existing are all `published_live`.

### Gotchas (Session 29)
- **Django template `split` filter doesn't exist.** Don't try to split a slash-separated string inside the template — expose the options as a separate list field in the content registry (`occasion_options`).
- **Windows cp1252 console can't print Unicode ✓/✗.** Use ASCII `OK`/`FAIL` labels in smoke-test scripts.
- **Arabic drop-caps need manual letter selection.** Can't grab `text[0]` in a template — choose the drop-cap letter at authoring time per locale (e.g. "ق" for the manifesto, "د" for the blog body).
- **Latin wordmark must stay Latin in RTL.** The restaurant brand name "Osteria Moderna" should render in Playfair, not Amiri — explicit `html[dir="rtl"] .fd-nav .logo .name` override pins the font.

---

## Session 27 — Medical Motion Opt-In: Read This Before Touching Specialist Motion (2026-04-12)

**Session 27 applied the live motion language (D-058) to the specialist archetype with a clinical motion profile (D-061).** Both `cardio-studio-specialistico` and `dermatologia-elite-roma` now have scroll reveals, staggered entry, CTA hover refinement, and image attention lift — all more restrained than Gusto's restaurant motion.

### What was added
- `live-motion.css` + `live-motion.js` linked in specialist `_base.html`
- Medical motion profile tokens: `--lm-rise: 10px`, `--lm-rise-lg: 16px`, `--lm-dur-slow: 680ms`
- 4 pattern categories across all 8 page templates: reveal-on-scroll, stagger, CTA hover, image filter lift
- RTL-aware arrow shift on gold-btn hover
- `prefers-reduced-motion` guards on all hover enhancements

### Current stable state
- **3 published_live templates:** cardio + derm (with motion + i18n 5 locales), gusto (with motion, IT-only)
- **All 3 have motion active** — the interaction-quality floor from D-058 is fully met
- **17 draft templates:** hidden from public
- **34/34 routes green**, zero regressions, zero cross-contamination

### Motion differentiation (important for future work)
- **Gusto** — `--lm-rise: 14px`, image zoom (scale 1.045x), nav underline sweep, cinematic feel
- **Medical** — `--lm-rise: 10px`, image filter lift (no zoom), no nav sweep, clinical precision
- These profiles must remain distinct per D-054 premium differentiation law
- Future archetypes should define their own token profile

### What to do next (in priority order)
1. **Phase 2g2x.1** — lift the 3 remaining CRITICO categories (agency, lawyer, real-estate) with DNA splits. The pattern is proven (Sessions 17–19).
2. **Phase 2i.2 step 2** — gusto i18n (new `.fd-*` RTL CSS block + 4 content trees). ~3h budget.
3. **Phase 2g3** — live skin folder authoring for draft templates, cheapest-first order per TODO_NEXT. Each new `published_live` template must adopt the motion language as gate 10 of D-053.

### Do NOT do
- Do NOT modify Gusto's motion tokens or attributes — they are intentionally different from medical
- Do NOT add counter animations to medical templates (excluded by D-061 as too promotional)
- Do NOT re-scatter fixes into new worktrees without consolidating back
- Do NOT open auth/checkout/editor/projects/commerce (Phase 3 gated by Phase 2g3.7)
- Do NOT add new categories or templates
- Do NOT reopen drafts or change tiering policy
- Preview PNGs should be regenerated with `--force` whenever a preview composition changes

---

Previous (still relevant):

## Session 23 — i18n/RTL Pilot Cardio: Read This If You're Touching Localization (2026-04-11)

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
