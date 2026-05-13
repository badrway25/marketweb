# Fashion-Editorial Shape Contract

**Phase**: Wave 2 — Pass-5 (T61) · **Date**: 2026-05-13 · **Status**: BLOCKING for any new `fashion-editorial` template.

**Scope**: Authoritative shape contract for the `fashion-editorial` archetype. Governs **every** future template that reuses `fashion-editorial` — i.e. shares the HTML skin under `templates/live_templates/ecommerce/fashion-editorial/` and the DNA `archetype: "fashion-editorial"` key.

**Existing reuses at write time**:

| Slug | Brand | Polarity / accent | Geography | Sub-discipline | Pass |
|---|---|---|---|---|---|
| `luxe-fashion-store` | Maison Luxe | `#C3A36A` champagne-gold on ink | Milano · Via Senato | prêt-à-porter editorial | pre-Wave-2 (prime instance) |
| `gemma-gioielleria` | Gemma · Atelier di Alta Gioielleria | `#9F7373` rosé on near-black ink + parchment cream | Milano · Brera | alta gioielleria editorial | Wave 2 T61 (1st reuse · IT-only draft) |

**Audience**: every agent and human who decides whether a new `fashion-editorial` template may be built, may merge, or may flip to `published_live` — release-gatekeeper, template-planner, template-builder, copy-translation-agent, browser-verifier, plus any reviewer signing off a PR against this archetype.

This contract was authored **during** the T61 Gemma build (contract-precedes-build pattern · per T56 ultra-luxury-cinematic + T58 artisan-workshop precedent). The pattern: write the contract *while* the first reuse is being authored so that the structural grammar is fixed at the same moment the second instance lands. Saves ~4 shape bugs per first reuse and catches the silent-drift class (dict-key typos that render `200` with empty bands rather than `500`).

The contract exists because the deterministic test surface (`apps.catalog.tests`) cannot catch a class of error the rendering surface raises silently: **the `fashion-editorial` page-data shapes are dense, editorial, and authored at magazine-spread granularity**. Without a written contract, the next builder would re-derive the shape implicitly from `template_content.py` (Luxe inline · 252-path tree) — slow, error-prone, and divergent.

---

## 0 · How to use this document

1. **Before any new `fashion-editorial` build** — read §1 → §9 in order. The Validation Checklist (§10) is the BLOCKING gate. Every item is a hard pre-flight.
2. **Every rule tagged `[BLOCKING]` is unconditional** — its violation prevents `tier: published_live`. No exceptions. Trap catalog (§9) calls out the defects that historically flipped through CLI green and were caught only on the browser walk or the multilingual sub-agent review.
3. Pair this document with:
   - `factory/standards/corporate-suite-blocking-rules.md` (the BLOCKING / REQUIRED / STRONG / GUIDELINE four-tag model used throughout).
   - `factory/standards/specialist-shape-contract.md` (the sibling medical contract; this document mirrors its structural conventions).
   - `factory/standards/classic-gold-shape-contract.md` (lawyer-side sibling).
   - `factory/references/template-inventory.md` (catalog state at the time of write).
4. **Honesty over completeness** — where a key is observed only in Luxe but is plausibly optional for a different jewelry/fashion brand, this document explicitly tags the divergence. The default canonical anchor is **Luxe** because at write time it is the only `published_live` instance (Gemma lands at `draft`).

---

## 1 · Purpose & scope

### 1.1 · What this standard governs

1. Which **HTML files** live in the skin folder and what they render.
2. Which **registry keys** must exist in `TEMPLATE_REGISTRY.json` and in `apps/catalog/template_dna.py` for an entry to be a valid `fashion-editorial` template.
3. Which **page-data keys** the rendering templates dereference at runtime — split per page-kind (`home`, `collection`, `product`, `about`, `lookbook`, `contact`), with required sub-shapes.
4. The **distinctness scoreboard** that a new reuse must satisfy versus every prior reuse (Luxe + Gemma + future).
5. The **trap catalog** — known defects that previously escaped the CLI but were caught on the shape-walk or in second-look review.

### 1.2 · What this standard does NOT govern

- **Voice & tone copy** — that is `factory/agents/copy-translation-agent.md` + the per-template module docstring contract.
- **Imagery curation** — that is `factory/standards/corporate-suite-imagery-standard.md` (notwithstanding the `fashion-editorial` skin's editorial Pexels / Unsplash mix; the imagery surface rules are unchanged: zero PlayStation gamepads, zero generic stock).
- **Browser verification rubric** — that is `factory/standards/corporate-suite-browser-rubric.md` for the Playwright MCP recipes (specific to `fashion-editorial`'s `.fe-*` selectors).
- **Quality scorecard layers** — see `factory/standards/corporate-suite-quality-scorecard.md`.

This document only answers: *what does the skin need from the content tree to render without raising `TemplateSyntaxError` or producing visibly broken markup?* If the skin says `{% for n, title, credit, image in page_data.lookbook_teaser_tiles %}` and the content tree gives a list of 3-key dicts, the page raises `ValueError: too many values to unpack` (or, worse, renders dict-repr strings inline) — that is the class of error this contract prevents.

### 1.3 · BLOCKING / REQUIRED / STRONG / GUIDELINE

This document uses the four-tag severity model from `corporate-suite-blocking-rules.md` §2:

- `[BLOCKING]` — violation blocks merge and unconditionally blocks `published_live` flip.
- `[REQUIRED]` — violation blocks `published_live`; allowed to land at `draft` with a tracked TODO.
- `[STRONG]` — violation allowed only with a written deviation note in the module docstring + second reviewer.
- `[GUIDELINE]` — taste; document the reason if you break it.

---

## 2 · Archetype identity

### 2.1 · The shape signature

`fashion-editorial` is the **maison de couture · numbered-edition · private-viewing** archetype. The skin reads like a print magazine: oversized serif headlines, edition-tag chips, a manifesto drop-cap, an atelier numbers strip, a lookbook teaser with 3 wide credit tiles, a press logo band, a drop announcement, and a private-viewing card. Conversion is **request-driven, never add-to-cart-driven** — the primary CTA always opens a private-viewing intake (Luxe: `Richiedi una sessione privata` · Gemma: `Prenotate una visita privata`), never a checkout.

| Dimension | Required value (or band) | Source of truth |
|---|---|---|
| `archetype` | `"fashion-editorial"` literal | `template_dna.py` luxe + gemma entries |
| `density` | `"very-airy"` | both instances |
| `hero_style` | `"editorial-serif"` | both instances |
| `navbar_style` | `"minimal-serif"` | both instances |
| `footer_style` | `"centered-minimal"` | both instances |
| `card_style` | `"editorial-large"` | both instances |
| `button_style` | `"ghost-gold-serif"` | both instances |
| `section_order` first three | `["nav", "editorial-cover", "edition-strip"]` | both instances |

### 2.2 · Palette polarities (canonical · diverge from these)

The two existing instances stake out two distinct polarities. A third reuse **must** pick a polarity that does NOT collapse to a recolor of champagne-gold or rosé.

| Instance | `primary` (ink) | `secondary` (paper) | `accent` | Mood |
|---|---|---|---|---|
| Luxe | `#1A1817` ink near-black | `#F3EDE3` warm cream | `#C3A36A` champagne-gold | prêt-à-porter editorial · maison de couture |
| Gemma | `#0F0E14` ink (cooler, near-black with violet undertone) | `#F1ECDF` parchment cream (warmer than Luxe) | `#9F7373` rosé | alta gioielleria · auteur-jeweler |
| **Third reuse candidate** | propose | propose | must NOT be champagne-gold, rosé, or recolor thereof | propose |

Plausible 3rd polarities (illustrative, not prescriptive):

- **perfumer-bronze** — `#1F1715` ink + `#EFE6D6` cream + `#8C6A3D` antique bronze (parfumerie de niche).
- **leather-cordovan** — `#19120F` near-black + `#EBE2D2` linen + `#7A2E2A` cordovan oxblood (high-end maroquinerie).
- **scarves-indigo** — `#11141B` deep indigo + `#F0EAD8` ivory + `#3D5A80` cobalt (foulards artisanaux).

Source: `apps/catalog/management/commands/seed_templates.py` SEED_TEMPLATES rows.

### 2.3 · Typography

The skin reads `theme.heading_font` and `theme.body_font` directly. Both fonts must:

- Be available on Google Fonts (no self-host).
- Provide italic for the headline emphasis (the skin uses `h1 em` italic across every hero and section heading).
- Provide weight 400/500/600/700 and ital 400/500.
- Be present in the font-pairing taxonomy at `template_dna.py`. Used pairings:

| Instance | Heading | Body |
|---|---|---|
| Luxe | Cormorant Garamond | Montserrat |
| Gemma | Bodoni Moda | Inter |

**[BLOCKING] `FE-T-01`**: Heading font MUST be a serif with strong italic AND a high contrast modulation (didone / transitional). The hero, manifesto, and lookbook headlines all rely on serif-italic dramatic distinction. Geometric or grotesque serifs are not permitted.

**[BLOCKING] `FE-T-02`**: A new reuse's heading font MUST NOT be Cormorant Garamond OR Bodoni Moda. The font-pairing axis is one of the load-bearing distinctness axes (§8, axis 3). Candidates open: Playfair Display SC, Editorial New (custom), Italiana, Cormorant SC, Cardo, EB Garamond Italic-heavy.

**[STRONG] `FE-T-03`**: Body font SHOULD be a humanist or geometric sans with good tabular-figure rendering (used for price columns, edition numbers, `n` indices). Luxe → Montserrat · Gemma → Inter. Both pass. Alternative (e.g. Public Sans, IBM Plex Sans) is allowed with a written deviation note.

### 2.4 · Hero / navbar / footer styles

| Style key | Luxe value | Gemma value | Notes |
|---|---|---|---|
| `hero_style` | `editorial-serif` | `editorial-serif` | only variant observed |
| `navbar_style` | `minimal-serif` | `minimal-serif` | both identical · skin does not branch |
| `footer_style` | `centered-minimal` | `centered-minimal` | both identical · skin does not branch |

**[BLOCKING] `FE-H-01`**: All three chrome keys (`hero_style`, `navbar_style`, `footer_style`) are SAME-by-design across reuses — they are chrome axes (D-054 §15) and intentionally collapse. Diverging here means you are deriving a new archetype, not reusing `fashion-editorial`.

### 2.5 · Density / tone / conversion_pattern

| Key | Luxe | Gemma | Permitted values for new reuses |
|---|---|---|---|
| `density` | `"very-airy"` | `"very-airy"` | `"very-airy"` only — the 90-px hero paddings + magazine-spread section gaps are load-bearing |
| `tone` | `"prestigious"` | `"auteur-jeweler"` | A descriptive tone string. Must NOT collapse to a generic `"modern"`, `"clean"`, `"luxury"`. Should be a 1-2-word noun phrase that names the maker's posture (e.g. `prestigious`, `auteur-jeweler`, `perfumer-essayist`, `archivist-restorer`). |
| `conversion_pattern` | `"private-request"` | `"private-viewing-jewelry"` | MUST be of the **request-family**. Permitted: `private-request`, `private-viewing`, `private-viewing-jewelry`, `private-viewing-leather`, `private-viewing-perfumer`. Forbidden: `add-to-cart`, `book-now-pay-now`, `instant-quote`, `strategy-call` — these collapse the editorial promise into commerce. |
| `imagery_key` | `"ecommerce"` | `"jewelry-atelier"` | MUST be a dedicated key in `apps/catalog/preview_imagery.py`. Reusing a sibling cluster's key is a §9 trap (FE-IMG-01). |

**[BLOCKING] `FE-D-01`**: `density != "very-airy"` blocks `published_live`. The skin's whitespace is the spine of the editorial silhouette.

**[BLOCKING] `FE-D-02`**: `conversion_pattern` MUST be from the request-family (see table above). Other patterns block merge. The archetype's promise is *editorial restraint into private discovery*, not e-commerce.

**[REQUIRED] `FE-D-03`**: The `conversion_pattern` value in DNA MUST be coherent with the `home.primary_cta` verb in the content tree:
- `private-request` ↔ CTA verb in the family of `"Richiedi una sessione privata"` (Luxe) / `"Richiedi un appuntamento"`.
- `private-viewing-jewelry` ↔ CTA verb in the family of `"Prenotate una visita privata"` (Gemma) / `"Riservate un'appuntamento al banco"`.

Picking `conversion_pattern: "private-request"` with `primary_cta: "Aggiungi al carrello"` is an FE-D-03 violation: the DNA and content disagree about the conversion mechanic.

---

## 3 · HTML skin folder

The folder `templates/live_templates/ecommerce/fashion-editorial/` is the canonical skin. D-051 Option A applies: **a `fashion-editorial` reuse adds ZERO new HTML files**. All differentiation lives in the DNA `content` block, the content tree, and (optionally) `preview_archetype` for the preview generator only.

### 3.1 · File table

| File | Page-kind it renders | Notes |
|---|---|---|
| `_base.html` | chrome (nav + footer) for all pages | reads `site.*`, `chrome.*`, `theme.*`, `template.*`, `pages`, `locale_switcher`, `is_rtl`, `brand.*` |
| `home.html` | `home` | the magazine cover · 17 distinct bands · richest page in the archetype |
| `collection.html` | `collection` | season-filtered product grid · 9-item products list at canonical instance count |
| `product.html` | `product` | look detail · gallery + info rows + atelier portrait + provenance steps + related items |
| `about.html` | `about` | maison statement + ateliers grid + direction portrait + press strip + numbers strip + visit card |
| `lookbook.html` | `lookbook` | masthead + credits table + 6-look grid + pullquote + notes + shop card |
| `contact.html` | `contact` | hero + form (8 fields) + maison cards (3 cities) + FAQ |

**Total: 7 HTML files** (1 base + 6 page kinds). NO blog list/detail (the archetype routes editorial content through `lookbook`, not a chronological blog).

### 3.2 · D-051 Option A · zero new HTML

**[BLOCKING] `FE-HTML-01`** — A new `fashion-editorial` reuse MUST NOT add or modify files under `templates/live_templates/ecommerce/fashion-editorial/`. If you find yourself wanting to change `home.html` to fit your content, you are deriving a new archetype (rename and isolate the skin) — not reusing `fashion-editorial`.

This rule is what made the T61 Gemma build land in 1 day (FASE B-E completed cleanly): zero new HTML, all the work was in the content tree + DNA + registry + seed.

### 3.3 · CSS prefix invariant

All component CSS classes are prefixed `.fe-` (e.g. `.fe-cover`, `.fe-edition`, `.fe-manifesto`, `.fe-numbers`, `.fe-lookbook-teaser`, `.fe-press`, `.fe-drop`, `.fe-private`, `.fe-tiles`, `.fe-credits`, `.fe-looks`, `.fe-pullquote`, `.fe-notes`, `.fe-shop`, `.fe-form`, `.fe-maison-cards`, `.fe-faq`).

**[STRONG] `FE-HTML-02`** — Do not rename the prefix even if your brand wordmark starts with a different letter. The skin's chrome, RTL block, and breakpoints all target `.fe-*`.

### 3.4 · The 6-page surface

The `fashion-editorial` skin ships **6 page kinds**: home, collection, product, about, lookbook, contact. The page **slugs are author-chosen** (URL identifiers, can be localized within the maison's voice) but the **page kinds are fixed**. Examples:

| Kind | Luxe slug | Gemma slug | Localizable? |
|---|---|---|---|
| `home` | `home` | `home` | NO — `home` is the canonical slug |
| `collection` | `collezione` | `collezione` | YES |
| `product` | `product` | `pezzo` | YES (Gemma chose `pezzo` to read as "single piece of jewelry") |
| `about` | `maison` | `casa` | YES (Gemma chose `casa` to read as "la casa Gemma") |
| `lookbook` | `lookbook` | `lookbook` | YES (often kept English by trade convention) |
| `contact` | `contatti` | `concierge` | YES (Gemma chose `concierge` to read as a private-viewing intake) |

**[BLOCKING] `FE-SLUG-01`** — Slugs in the `pages` list MUST match the top-level dict keys exactly. If `pages[2].slug == "pezzo"`, the content tree MUST contain a `pezzo:` top-level key with the product page-data dict (not `product:`). The view resolver uses `page_kind` (not `slug`) to find the HTML file, but the page-data lookup uses the slug.

**[BLOCKING] `FE-SLUG-02`** — Slugs MUST be consistent across all locales. The locale switcher routes by slug. If IT uses `pezzo` and EN uses `piece`, the locale switch from IT → EN on the product page raises 404 because EN's pages list never declares `pezzo`. Canonical rule: **author the slugs in IT first, then keep them verbatim across all locales** (the labels translate; the slugs do not). All Wave 1 + Wave 2 templates follow this rule.

---

## 4 · DNA registration

A `fashion-editorial` template's entry in `apps/catalog/template_dna.py` MUST contain all the keys listed below. Gemma is the canonical example (verbatim from `template_dna.py` Gemma entry):

```python
"gemma-gioielleria": {
    "archetype":          "fashion-editorial",
    "preview_archetype":  "fashion-editorial-gemma",
    "hero_style":         "editorial-serif",
    "navbar_style":       "minimal-serif",
    "footer_style":       "centered-minimal",
    "section_order":      ["nav", "editorial-cover", "edition-strip", ...],
    "card_style":         "editorial-large",
    "button_style":       "ghost-gold-serif",
    "density":            "very-airy",
    "tone":               "auteur-jeweler",
    "imagery_direction":  "jewelry-atelier — close-up macro of brilliant cuts...",
    "imagery_key":        "jewelry-atelier",
    "conversion_pattern": "private-viewing-jewelry",
    "font_pairing":       ("Bodoni Moda", "Inter"),
    "content": { ... see §4.3 ... },
},
```

### 4.1 · Required keys

| Key | Type | Required? | Notes |
|---|---|---|---|
| `archetype` | str | **[BLOCKING]** | literal `"fashion-editorial"` |
| `hero_style` | str | **[BLOCKING]** | `"editorial-serif"` only |
| `navbar_style` | str | **[BLOCKING]** | `"minimal-serif"` only |
| `footer_style` | str | **[BLOCKING]** | `"centered-minimal"` only |
| `section_order` | list[str] | **[REQUIRED]** | first three `["nav", "editorial-cover", "edition-strip"]` |
| `card_style` | str | **[REQUIRED]** | `"editorial-large"` only |
| `button_style` | str | **[REQUIRED]** | `"ghost-gold-serif"` only |
| `density` | str | **[BLOCKING]** | `"very-airy"` only |
| `tone` | str | **[REQUIRED]** | descriptive 1-2-word phrase (§2.5) |
| `imagery_direction` | str | **[REQUIRED]** | one-line editorial brief for imagery-curator |
| `imagery_key` | str | **[BLOCKING]** | dedicated key in `apps/catalog/preview_imagery.py` |
| `conversion_pattern` | str | **[BLOCKING]** | from request-family (§2.5) |
| `font_pairing` | tuple[str, str] | **[BLOCKING]** | (heading, body); heading MUST be a NEW serif (§2.3 FE-T-02) |
| `content` | dict[str, Any] | **[BLOCKING]** | see §4.3 |
| `preview_archetype` | str | **[STRONG]** | only if you need a different preview-composition file |

### 4.2 · `preview_archetype` — when to set it

Gemma sets `preview_archetype: "fashion-editorial-gemma"`. Luxe does not (uses the bare archetype name). **[STRONG] `FE-PREV-01`** — every new `fashion-editorial` reuse SHOULD set a unique `preview_archetype` so the preview card surfaces the brand-specific accent + portrait + headline.

### 4.3 · `content` block — DNA-side copy

The DNA's `content` block holds the **preview-card** copy plus a small subset of fields used by the editor as starter values. It is NOT the full content tree. Required keys:

| Key | Type | Notes |
|---|---|---|
| `eyebrow` | str | preview hero eyebrow |
| `headline` | str (with `<em>`) | preview hero headline · the noun-em italic anchor |
| `subhead` | str | preview hero subhead |
| `primary_cta` | str | preview CTA verb (`"Prenotate una visita privata"` for Gemma) |
| `address` | str | maison address one-liner |
| `drop_cap` | str (1 char) | first letter of `intro_paragraph` |
| `intro_paragraph` | str | preview manifesto body |
| `press` | list[str] (4-5 items) | logo-marquee labels |
| `nav_links` | list[str] (5-6 items) | preview navbar labels |

The full content tree (with all 6 page-kinds populated) lives in `apps/catalog/template_content_<slug>.py` (e.g. `template_content_gemma.py` · 239 paths) — see §5.

---

## 5 · Content tree shape (top-level)

The full content tree is a Python module exporting a single dict assigned to `<SLUG>_CONTENT_<LOCALE>` (e.g. `GEMMA_CONTENT_IT`, `LUXE_CONTENT_FR`). At write time both instances export only IT (Gemma) or all 5 locales (Luxe IT/EN/FR/ES/AR). The dict's root keys are FIXED:

```python
GEMMA_CONTENT_IT = {
    "pages":     [...],   # list of 6 page entries (slug + kind + label)
    "site":      {...},   # chrome (logo/address/phone/hours/footer labels)
    "home":      {...},   # home page-data
    "collezione":{...},   # collection page-data
    "pezzo":     {...},   # product page-data (slug-renamed for Gemma)
    "casa":      {...},   # about page-data (slug-renamed for Gemma)
    "lookbook":  {...},   # lookbook page-data
    "concierge": {...},   # contact page-data (slug-renamed for Gemma)
}
```

**[BLOCKING] `FE-ROOT-01`** — The 6 page-section dicts MUST be keyed by the **slug** (author-chosen), not by the **kind**. The view resolver uses the slug → page-entry → page-data lookup chain.

**[BLOCKING] `FE-ROOT-02`** — The `pages` list MUST contain exactly 6 entries, in declared order: home, collection, product, about, lookbook, contact (by kind). The navbar renders entries in this order; reordering ships a navbar with wrong tabs.

### 5.1 · `pages` list shape

Each entry is a dict with keys `{slug, kind, label}`. Example (Gemma IT):

```python
"pages": [
    {"slug": "home",       "kind": "home",       "label": "Atelier"},
    {"slug": "collezione", "kind": "collection", "label": "Collezione"},
    {"slug": "pezzo",      "kind": "product",    "label": "Pezzo"},
    {"slug": "casa",       "kind": "about",      "label": "La casa Gemma"},
    {"slug": "lookbook",   "kind": "lookbook",   "label": "Editoriale"},
    {"slug": "concierge",  "kind": "contact",    "label": "Concierge"},
],
```

**[BLOCKING] `FE-PAGES-01`** — `kind` values MUST be from the fixed set `{home, collection, product, about, lookbook, contact}`. Custom kinds (e.g. `editorial`, `journal`, `archive`) raise `TemplateDoesNotExist` because no matching HTML file exists in the skin.

**[BLOCKING] `FE-PAGES-02`** — `slug` values MUST be URL-safe (`[a-z0-9-]+`), and MUST match the corresponding top-level dict key in the content tree (FE-ROOT-01).

### 5.2 · `site` block (chrome)

Required keys (verbatim from Gemma · 30 keys total):

| Key | Type | Notes |
|---|---|---|
| `logo_initial` | str | single-char glyph for compact navbar |
| `logo_word` | str | full wordmark |
| `logo_subline` | str | wordmark subline (e.g. "Atelier di Alta Gioielleria") |
| `tag` | str | top-bar season/edition chip |
| `phone` | str | maison phone (E.164-ish) |
| `private_phone_label` | str | label preceding the phone in private-viewing card |
| `email` | str | maison email |
| `private_email_label` | str | label preceding the email |
| `address` | str | maison street address |
| `showroom_paris` | str | optional Paris satellite address |
| `showroom_tokyo` | str | optional Tokyo satellite address |
| `hours_compact` | str | one-liner hours for navbar |
| `hours_footer_rows` | list[dict] | footer hours table (2-3 rows of `{label, value}`) |
| `license` | str | small-print legal line (P.IVA / VAT) |
| `footer_intro` | str | footer-top short paragraph |
| `nav_cta` | str | navbar primary CTA label |
| `nav_cta_kind` | str | `"private"` or `"shop"` — drives navbar CTA styling |
| `foot_studio` | str | footer column 1 label |
| `foot_pages` | str | footer column 2 label |
| `foot_contact` | str | footer column 3 label |
| `foot_offices` | str | footer column 4 label |
| `office_rows` | list[dict] | 3 city cards: `{city, address, phone, hours}` |
| `currency_symbol` | str | `"€"` (or `"£"` / `"$"`) |
| `collection_label` | str | meta-strip label preceding the collection name |
| `drop_label` | str | meta-strip label preceding the drop announcement |
| `season_label` | str | meta-strip label preceding the season |
| `shipping_label`, `shipping_value` | str, str | shipping promise row |
| `viewing_label`, `viewing_value` | str, str | private-viewing promise row |
| `waitlist_label` | str | waitlist chip label |
| `rsvp_label` | str | RSVP chip label |

**[BLOCKING] `FE-SITE-01`** — All 30 keys MUST be present even if empty-string. The skin dereferences each one in the chrome `_base.html` and a missing key renders the literal `{{ site.foo }}` placeholder (not an empty string).

**[STRONG] `FE-SITE-02`** — `nav_cta_kind` SHOULD be `"private"` for fashion-editorial reuses (matches the request-family conversion pattern). `"shop"` is permitted but reads less archetype-coherent.

---

## 6 · Per-page page-data shape

This is the meat of the contract. Each of the 6 page-data dicts has a fixed shape. The skin's templates dereference these keys via `{{ page_data.foo }}` / `{% for x in page_data.bar %}`. A typo, a tuple-vs-dict swap, or a missing list item silently degrades the band (rare 500-class errors except where unpacking).

### 6.1 · `home` page-data (47 keys · 1117-line cover spread)

The home page is the richest page-kind in the archetype. It is a magazine cover — 17 bands deep. Required keys (full enumeration):

| Key | Type | Notes |
|---|---|---|
| `issue`, `issue_label` | str, str | edition number + label (e.g. "Inverno 2026", "Edizione") |
| `cover_styling_label`, `cover_styling_name` | str, str | photographer credit |
| `cover_label`, `cover_subject` | str, str | model / subject credit |
| `cover_image` | str (URL) | the full-bleed cover photograph |
| `eyebrow`, `headline`, `headline_credit_line`, `intro` | str | hero copy |
| `primary_cta`, `primary_href` | str, str | the request-family CTA + URL anchor |
| `secondary_label`, `secondary_name` | str, str | secondary CTA (often "esplora collezione") |
| `edition_label`, `edition_subline` | str, str | meta-strip edition row |
| `tiles` | list[dict] (4 items · keys `{id, tag, name, price, image}`) | 4 hero product tiles |
| `manifesto_label`, `manifesto_heading`, `manifesto_text` | str | the drop-cap manifesto |
| `atelier_numbers_label`, `atelier_numbers` | str, list[dict] (4 items · keys `{value, label}`) | numbers strip |
| `lookbook_teaser_label`, `lookbook_teaser_heading`, `lookbook_teaser_intro` | str | lookbook teaser intro |
| `lookbook_teaser_link`, `lookbook_teaser_href` | str, str | teaser CTA |
| `lookbook_teaser_tiles` | list[dict] (3 items · keys `{title, credit, image}`) | 3 wide credit tiles |
| `press_label`, `press_intro` | str, str | press strip preamble |
| `press_items` | list[dict] (5 items · keys `{magazine, issue, title, byline}`) | 5 press cards |
| `drop_label`, `drop_heading`, `drop_subhead` | str | drop announcement |
| `drop_metadata` | list[dict] (4 items · keys `{label, value}`) | drop metadata strip |
| `drop_cta`, `drop_cta_href` | str, str | drop CTA |
| `private_label`, `private_heading`, `private_intro` | str | private-viewing card |
| `private_primary`, `private_primary_href` | str, str | primary private CTA |
| `private_secondary`, `private_secondary_href` | str, str | secondary private CTA |

**[BLOCKING] `FE-HOME-01`** — All 47 keys MUST be present. Missing keys render literal `{{ }}` placeholders.

**[BLOCKING] `FE-HOME-02`** — `tiles` MUST have **exactly 4 items**. The grid CSS hard-codes 4 columns. 3 items leaves a hole; 5 wraps into a second row that breaks the spread.

**[BLOCKING] `FE-HOME-03`** — `lookbook_teaser_tiles` MUST have **exactly 3 items**. The skin's grid is 3-wide.

**[BLOCKING] `FE-HOME-04`** — `atelier_numbers` MUST have **exactly 4 items**. The numbers strip is 4-wide.

**[BLOCKING] `FE-HOME-05`** — `drop_metadata` MUST have **exactly 4 items**. The drop strip is 4-wide.

**[BLOCKING] `FE-HOME-06`** — `press_items` MUST have **exactly 5 items**. The press strip is 5-wide.

**[STRONG] `FE-HOME-07`** — `cover_image`, `tiles[].image`, `lookbook_teaser_tiles[].image` MUST be valid URLs (HTTPS, CDN-served, no localhost). The skin renders them as `background-image: url(...)` and a broken URL leaves a grey rectangle.

### 6.2 · `collection` page-data (16 keys)

| Key | Type | Notes |
|---|---|---|
| `season_chip`, `eyebrow`, `headline`, `intro` | str | hero strip |
| `filter_label`, `filter_groups` | str, list[dict] (3 items · keys `{label, options}`) | filter sidebar |
| `sort_label`, `sort_options` | str, list[dict] (4 items · keys `{value, label}`) | sort dropdown |
| `result_count`, `result_subtitle` | str, str | result count strap |
| `products` | list[dict] (9 items · keys `{id, n, name, meta, drop, price, tag, available, image}`) | the 9-item product grid |
| `featured_product_id` | str | the product `id` to feature large in the grid |
| `footer_note_label`, `footer_note` | str, str | small-print bottom strap |

**[BLOCKING] `FE-COLL-01`** — `products` MUST have **exactly 9 items**. The grid renders 3 wide × 3 rows; with a `featured_product_id` flag one of the 9 renders large. 8 items breaks the grid; 10+ wraps.

**[BLOCKING] `FE-COLL-02`** — Each product MUST have all 9 sub-keys. `available` MUST be boolean (drives the "sold out" badge); `n` is a 2-digit string (e.g. `"01"`); `tag` is a 1-2 word categorical chip.

### 6.3 · `product` page-data (39 keys)

The product page (Luxe: `product`, Gemma: `pezzo`) renders one look in editorial depth.

| Key | Type | Notes |
|---|---|---|
| `id`, `n`, `name`, `subtitle`, `price`, `vat_note`, `tag`, `intro` | str | hero strap |
| `gallery` | list[dict] (5 items · keys `{caption, image}`) | 5-image editorial gallery |
| `gallery_caption_styling`, `gallery_caption_photo`, `gallery_caption_location` | str | gallery credit row |
| `info_label`, `info_rows` | str, list[dict] (8 items · keys `{label, value}`) | spec table |
| `size_label`, `size_options` | str, list[dict] (2 items · keys `{label, hint}`) | size selector |
| `color_label`, `color_options` | str, list[dict] (3 items · keys `{name, hex, hint}`) | colorway swatches |
| `edition_label`, `edition_value`, `edition_note` | str | edition strap |
| `atelier_label`, `atelier_name`, `atelier_founded`, `atelier_text`, `atelier_portrait` | str | atelier credit card |
| `buy_primary`, `buy_primary_href`, `buy_secondary`, `buy_note` | str | request-family CTA pair |
| `care_label`, `care_intro`, `care_items` | str, str, list[dict] (4 items · keys `{label, text}`) | care instructions |
| `provenance_label`, `provenance_heading`, `provenance_steps` | str, str, list[dict] (4 items · keys `{n, title, blurb}`) | provenance 4-step |
| `related_label`, `related_intro`, `related_items` | str, str, list[dict] (3 items · keys `{id, n, name, meta, price, image}`) | 3 related looks |

**[BLOCKING] `FE-PROD-01`** — `gallery` MUST have **exactly 5 items**, `info_rows` 8 items, `size_options` 2 items, `color_options` 3 items, `care_items` 4 items, `provenance_steps` 4 items, `related_items` 3 items. The skin's grids and CTAs hard-code these counts.

**[BLOCKING] `FE-PROD-02`** — `provenance_steps[]` MUST have keys `{n, title, blurb}` (NOT `num`/`step`/`description`). This is the artisan-workshop silent-bug class adapted: the wrong keys render `200` with empty step bands.

**[BLOCKING] `FE-PROD-03`** — `info_rows[]` MUST be 2-key dicts `{label, value}`, NOT 2-tuples. Tuple shape unpacks but the skin uses `{{ row.label }}` so tuple-shape renders the literal `('Materiale', 'Oro 18kt')` repr inline.

### 6.4 · `about` page-data (22 keys)

Luxe: `maison`. Gemma: `casa`.

| Key | Type | Notes |
|---|---|---|
| `eyebrow`, `headline`, `intro` | str | hero strap |
| `statement_label`, `statement_heading`, `statement_text` | str | maison statement card |
| `ateliers_label`, `ateliers_heading`, `ateliers_intro` | str | ateliers preamble |
| `ateliers` | list[dict] (3 items · keys `{city, place, role, since, head, team, image}`) | ateliers grid |
| `direction_label`, `direction_name`, `direction_role`, `direction_text`, `direction_portrait` | str | the founder/direction card |
| `direction_quote`, `direction_quote_attribution` | str, str | the maker's pullquote |
| `press_label`, `press_heading`, `press_items` | str, str, list[dict] (5 items · keys `{magazine, issue, title, byline}`) | press strip |
| `numbers_label`, `numbers_items` | str, list[dict] (4 items · keys `{value, label}`) | numbers strip |
| `visit_label`, `visit_heading`, `visit_text`, `visit_primary`, `visit_primary_href` | str | visit-card CTA |

**[BLOCKING] `FE-ABOUT-01`** — `ateliers` MUST have **exactly 3 items**, `press_items` 5, `numbers_items` 4.

### 6.5 · `lookbook` page-data (18 keys)

| Key | Type | Notes |
|---|---|---|
| `issue`, `issue_label`, `issue_n` | str | masthead |
| `eyebrow`, `headline`, `intro` | str | hero |
| `credits_label`, `credits_rows` | str, list[dict] (8 items · keys `{label, value}`) | credits table |
| `looks_label`, `looks_intro`, `looks` | str, str, list[dict] (6 items · keys `{n, title, outfit, credit, image}`) | the 6-look grid |
| `pullquote`, `pullquote_attribution` | str, str | mid-grid quote |
| `notes_label`, `notes_intro`, `notes_items` | str, str, list[dict] (3 items · keys `{label, text}`) | editor's notes |
| `shop_label`, `shop_heading`, `shop_intro`, `shop_primary`, `shop_primary_href`, `shop_secondary`, `shop_secondary_href` | str | shop card |

**[BLOCKING] `FE-LOOK-01`** — `looks` MUST have **exactly 6 items**, `credits_rows` 8, `notes_items` 3.

### 6.6 · `contact` page-data (12 keys + form_fields list)

Luxe: `contatti`. Gemma: `concierge`.

| Key | Type | Notes |
|---|---|---|
| `eyebrow`, `headline`, `intro` | str | hero |
| `form_section_label`, `form_section_intro` | str | form preamble |
| `form_helper_required`, `form_submit_button`, `form_submit_note` | str | form chrome |
| `form_fields` | list[dict] (8 items · keys `{name, label, type, required, options}`) | the 8-field form |
| `card_label`, `maison_cards` | str, list[dict] (3 items · keys `{city, address, phone, email, hours}`) | maison cards |
| `faq_label`, `faq_items` | str, list[dict] (4 items · keys `{q, a}`) | FAQ |

**[BLOCKING] `FE-CONT-01`** — `form_fields[]` MUST have keys `{name, label, type, required, options}` — `options` is a list (empty for non-select fields, populated for `select` and `radio` types).

**[BLOCKING] `FE-CONT-02`** — `faq_items[]` MUST be 2-key dicts `{q, a}`, NOT 2-tuples. (This is the silent-bug class first observed in `template_content_sapori.py` per `factory/standards/artisan-workshop-shape-contract.md` §6.)

---

## 7 · Multilingual locale parity

`fashion-editorial` ships in 5 locales at canonical instance count: `it` (primary), `en`, `fr`, `es`, `ar` (RTL). Each locale is a separate `<SLUG>_CONTENT_<LOCALE>` constant in `apps/catalog/template_content.py` or `template_content_<slug>.py`.

**[BLOCKING] `FE-LOC-01`** — Every locale MUST declare **the same `pages` list shape** (same 6 slugs + same 6 kinds, only the `label` differs). The view's slug → page_kind lookup runs identically across locales.

**[BLOCKING] `FE-LOC-02`** — Every locale MUST produce **the same dict-path count** as the IT canonical (Luxe IT: 252 paths · Gemma IT: 252 paths). The shape walker is the gate. A locale with 247 paths instead of 252 means a band is missing and will render empty.

**[BLOCKING] `FE-LOC-03`** — The **voice anchor** declared in the DNA `voice_anchor` field (e.g. `"gioielleria d'autore"` for Gemma) MUST appear **verbatim in IT** AND **verbatim untranslated in EN/FR/ES/AR**. This is the brand-recognition invariant: the maison's voice anchor is a proper noun phrase that survives translation. Translators MUST preserve it literally.

**[BLOCKING] `FE-LOC-04`** — Latin proper names (city names, person names, atelier names) in AR MUST be wrapped in `<bdi>` or use `unicode-bidi: isolate` to prevent RTL/LTR mixing artifacts. The skin handles this in `_base.html` via the `is_rtl` flag, but content authors MUST not insert raw Latin strings into AR copy without isolation.

**[STRONG] `FE-LOC-05`** — Body copy density SHOULD be comparable across locales (within ±20% character count for a given paragraph). A massively shortened FR translation breaks the editorial rhythm.

---

## 8 · D-054 distinctness scoreboard

Per D-054 (template inventory · 14-axis distinctness rubric), every new `fashion-editorial` reuse MUST score **distinct on ≥8 of 14 axes** versus EVERY prior reuse.

| # | Axis | Type | Status |
|---|---|---|---|
| 1 | brand name (logo_word) | CONTENT | MUST differ |
| 2 | brand tag / season chip | CONTENT | MUST differ |
| 3 | voice anchor (IT noun phrase) | CONTENT | MUST differ (proper noun) |
| 4 | persona name + bio | CONTENT | MUST differ |
| 5 | city / address | CONTENT | SHOULD differ (Milano twice is OK if different street) |
| 6 | home headline | CONTENT | MUST differ |
| 7 | home intro | CONTENT | MUST differ |
| 8 | home manifesto_text | CONTENT | MUST differ |
| 9 | product names (9 SKUs in collezione + tiles) | CONTENT | MUST differ (zero overlap) |
| 10 | price range | CONTENT | SHOULD differ |
| 11 | tone (DNA) | DNA | SHOULD differ |
| 12 | conversion_pattern (DNA) | DNA | MAY differ within request-family |
| 13 | imagery_key (DNA) | DNA | MUST differ |
| 14 | lookbook headline | CONTENT | MUST differ |

**Chrome axes (intentionally SAME)**:

- `archetype` — always `"fashion-editorial"`
- `hero_style` — always `"editorial-serif"`
- `navbar_style` — always `"minimal-serif"`
- `footer_style` — always `"centered-minimal"`
- `card_style` — always `"editorial-large"`

**Gemma vs Luxe scoreboard (T61, 2026-05-13)**: 10/14 distinct (floor 8 → PASS).

**[BLOCKING] `FE-DIST-01`** — A new reuse with <8 distinct axes blocks `published_live`. Run the scoreboard at FASE D and document the result in the build report.

---

## 9 · Trap catalog

Known defects that escaped the CLI silently and were caught only on the shape-walk, browser review, or sub-agent translator hand-off.

### FE-TRAP-01 · Wrong home dict keys
**Class**: silent render-200 with empty bands.
**Cause**: builder authors home page-data from memory/imagination instead of cross-referencing the canonical Luxe shape, ending up with `atelier_label`/`tiles_label`/`link_all` (Gemma first draft) instead of canonical `cover_image`/`issue`/`cover_styling_label`/`headline_credit_line`/`secondary_label`/`secondary_name`/`edition_label`/`edition_subline`/`issue_label`/`manifesto_label`/`manifesto_heading`/`manifesto_text`/`atelier_numbers_label`/`drop_subhead`/`drop_cta`/`drop_cta_href`/`press_intro`.
**Detection**: shape walker that diffs against Luxe canonical keys. The T61 Gemma build caught 19 missing/extra keys at first parity check before any view rendered.
**Mitigation**: this contract §6.1 enumerates all 47 home keys. Read it BEFORE authoring.

### FE-TRAP-02 · `provenance_steps` wrong sub-key
**Class**: silent render-200 with empty step bands.
**Cause**: authoring `{num, step, description}` instead of canonical `{n, title, blurb}`. The skin reads `{{ s.n }}{{ s.title }}{{ s.blurb }}` so wrong keys leave the band rendering empty triangles.
**Detection**: visual review of provenance section after first render. NOT caught by CLI tests.
**Mitigation**: §6.3 FE-PROD-02 specifies the exact 3-key shape.

### FE-TRAP-03 · `info_rows` or `faq_items` as tuples
**Class**: dict-repr leakage in markup.
**Cause**: authoring `info_rows = [("Materiale", "Oro 18kt"), ...]` instead of `[{"label": "Materiale", "value": "Oro 18kt"}, ...]`. The skin uses `{{ row.label }}` (Django dot-attr that DOES NOT auto-unpack tuples) so the literal `('Materiale', 'Oro 18kt')` Python-repr appears in markup.
**Detection**: visual review. NOT caught by CLI.
**Mitigation**: §6.3 FE-PROD-03 + §6.6 FE-CONT-02.

### FE-TRAP-04 · Slug rename without dict-key rename
**Class**: TemplateDoesNotExist OR Http404.
**Cause**: declaring `pages[2].slug == "pezzo"` in the IT pages list but leaving the top-level dict keyed `"product"`. The view's `find_page` lookup matches the slug, then `template_content.get_content()` returns the tree, but the page-data lookup in `get_context_data` does `self.content[self.page_entry["slug"]]` which raises KeyError.
**Detection**: first staff-preview GET on the renamed page.
**Mitigation**: §3.4 FE-SLUG-01.

### FE-TRAP-05 · Slug drift across locales
**Class**: locale-switcher 404.
**Cause**: authoring IT with `concierge` slug and EN with `contact` slug. The locale switcher passes the current slug across locales; EN doesn't declare `concierge` so the route 404s.
**Detection**: cross-locale walk on the renamed page.
**Mitigation**: §3.4 FE-SLUG-02. Author slugs in IT and freeze them across locales.

### FE-TRAP-06 · Off-by-count grid items
**Class**: visual breakage (hole in grid, second-row wrap).
**Cause**: authoring `tiles` with 3 instead of 4 items, or `looks` with 5 or 7 instead of 6.
**Detection**: visual review.
**Mitigation**: §6 enumerates exact counts per list. Cross-check with the shape walker count map.

### FE-TRAP-07 · Cross-category resolver missing
**Class**: TemplateDoesNotExist.
**Cause**: declaring a `fashion-editorial` template in a non-ecommerce category (e.g. a luxury hotel re-using the magazine spread) without setting `skin_source_category: "ecommerce"` in the DNA. The view's resolver looks up `live_templates/<category>/fashion-editorial/home.html` and fails.
**Detection**: first GET on home.
**Mitigation**: `apps/catalog/views.py:380` resolver reads `self.dna.get("skin_source_category", category_slug)`. Set `skin_source_category: "ecommerce"` in DNA for cross-category reuses. (Pattern introduced by T56 ultra-luxury-cinematic cross-category reuse.)

### FE-TRAP-08 · `voice_anchor` translation
**Class**: brand-recognition loss.
**Cause**: translator agent renders `"gioielleria d'autore"` (Gemma voice anchor) as `"signature jewelry"` (EN) / `"joaillerie d'auteur"` (FR). The voice anchor is a proper noun phrase and must survive translation literally.
**Detection**: post-translator shape-parity walk + cross-locale grep for the IT phrase.
**Mitigation**: §7 FE-LOC-03. Brief translators on the verbatim rule in the per-locale prompt.

### FE-TRAP-09 · Imagery key collision
**Class**: silent imagery-pool reuse → preview cards look identical.
**Cause**: declaring `imagery_key: "ecommerce"` for a jewelry reuse instead of a dedicated `"jewelry-atelier"` key. The preview generator pulls from the shared pool and gemma + luxe + future reuses all surface the same hero stock.
**Detection**: visual review of catalog preview grid.
**Mitigation**: §2.5 + §8 axis 13. Always add a dedicated key in `apps/catalog/preview_imagery.py` with 6 distinct URLs.

---

## 10 · Validation checklist

This is the BLOCKING gate. A new `fashion-editorial` template may not flip to `published_live` until every item below is green.

### A · DNA registration
- [ ] `archetype: "fashion-editorial"` literal
- [ ] All 14 required DNA keys present (§4.1)
- [ ] `font_pairing` heading is NOT Cormorant Garamond OR Bodoni Moda (FE-T-02)
- [ ] `conversion_pattern` is from the request-family (FE-D-02)
- [ ] `imagery_key` is a dedicated key in `preview_imagery.py` (FE-IMG / FE-D-01)
- [ ] If reusing across category, `skin_source_category: "ecommerce"` is set (FE-TRAP-07)

### B · Content tree
- [ ] `pages` list has exactly 6 entries with the fixed kind set (FE-PAGES-01)
- [ ] Each slug in `pages` matches a top-level dict key (FE-ROOT-01, FE-SLUG-01)
- [ ] `site` block has all 30 keys (FE-SITE-01)
- [ ] `home` block has all 47 keys (FE-HOME-01)
- [ ] `tiles` = 4 items, `lookbook_teaser_tiles` = 3, `atelier_numbers` = 4, `drop_metadata` = 4, `press_items` = 5 (FE-HOME-02..06)
- [ ] `collection.products` = 9 items, each with all 9 sub-keys (FE-COLL-01..02)
- [ ] `product.gallery` = 5, `info_rows` = 8, `size_options` = 2, `color_options` = 3, `care_items` = 4, `provenance_steps` = 4, `related_items` = 3 (FE-PROD-01)
- [ ] `provenance_steps[]` keys are `{n, title, blurb}` (FE-PROD-02)
- [ ] `info_rows[]` are dicts, not tuples (FE-PROD-03)
- [ ] `about.ateliers` = 3, `press_items` = 5, `numbers_items` = 4 (FE-ABOUT-01)
- [ ] `lookbook.looks` = 6, `credits_rows` = 8, `notes_items` = 3 (FE-LOOK-01)
- [ ] `contact.form_fields` has 8 items with full 5-key shape (FE-CONT-01)
- [ ] `contact.faq_items[]` are dicts, not tuples (FE-CONT-02)

### C · Multilingual
- [ ] All 5 locales (it/en/fr/es/ar) populated at canonical instance count
- [ ] All locales have identical `pages` list shape (FE-LOC-01)
- [ ] All locales have identical dict-path count (FE-LOC-02)
- [ ] `voice_anchor` appears verbatim in every locale (FE-LOC-03)
- [ ] AR uses `<bdi>` or unicode-bidi isolate for Latin proper names (FE-LOC-04)

### D · Distinctness
- [ ] D-054 14-axis scoreboard ≥8 distinct vs every prior reuse (FE-DIST-01)
- [ ] Chrome SAME axes intentionally collapsed (5 axes)

### E · Palette & contrast
- [ ] Body text vs background: AAA-normal (≥7:1) at primary/background pair
- [ ] Accent on background: at least AA-large (≥3:1)
- [ ] Ghost-accent on dark band degrades via `--accent-text-on-primary-safe` token

### F · Walk
- [ ] All 6 staff-preview routes render 200 with content (no literal `{{ }}` placeholders)
- [ ] Cross-locale walk on each route: all 5 locales × 6 routes = 30 GET 200s
- [ ] Public access (without `?preview=1`) returns 404 while draft (D-055 tier gate)
- [ ] Luxe regression: all 6 Luxe routes still 200 after seed
- [ ] catalog tests pass: `python manage.py test apps.catalog --keepdb`

### G · Documentation
- [ ] `TEMPLATE_REGISTRY.json` entry with `tier_reason` + `reuse_notes` documenting D-054 scoreboard
- [ ] `seed_templates.py` TEMPLATE_METADATA + SEED_TEMPLATES row
- [ ] Build report under `factory/reports/execution-<date>/T<N>_<...>.md`

---

## 11 · Change log

- **2026-05-13** — T61 · contract authored during Gemma build (1st reuse · contract-precedes-build pattern per T56/T58 precedent). Establishes the 6-page surface, 252-path Luxe canonical, 14-axis D-054 scoreboard, and 9-trap catalog. Status: live for all future `fashion-editorial` reuses.
