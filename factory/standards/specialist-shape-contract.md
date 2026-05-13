# Specialist Shape Contract

**Phase**: Wave 1 — Pass-5 follow-up · **Date**: 2026-05-12 · **Status**: BLOCKING for any new `specialist` template.

**Scope**: This document is the authoritative shape contract for the `specialist` medical archetype. It governs **every** future template that reuses `specialist` — i.e. shares the HTML skin under `templates/live_templates/medical/specialist/` and the DNA `archetype: "specialist"` key.

**Existing reuses at write time**:

| Slug | Brand | Polarity / accent | Geography | Sub-discipline | Cluster pass |
|---|---|---|---|---|---|
| `cardio-studio-specialistico` | Studio Marani Cardiologia | `#9c2a2a` ledger-red (prime instance) | Roma · Parioli | cardiology | pre-Wave-1 |
| `dermatologia-elite-roma` | Studio Ricciardi Dermatologia | `#3d5437` forest-green | Roma · Veneto | dermatology | pre-Wave-1 (1st reuse) |
| `denti-co-studio` | Denti+Co Studio Dentistico Associato | `#2BC4A4` fresh-mint | Milano · Brera | dentistry | Wave 1 T45 + T46 (2nd reuse) |

**Audience**: every agent and human who decides whether a new `specialist` template may be built, may merge, or may flip to `published_live` — release-gatekeeper, template-planner, template-builder, copy-translation-agent, browser-verifier, plus any reviewer signing off a PR against this archetype.

This standard is overdue. It should have been written between the Denti T46 close and the petro-veterinario T51 build that is about to land; it was not, and the Petro builder will be the first one to write a `specialist` reuse without an in-repo derivation reference. The sibling `factory/standards/classic-gold-shape-contract.md` (939 lines · written at T48 close for the same reason on the lawyer side) is the structural model this document mirrors verbatim.

The contract exists because the deterministic test surface cannot catch a class of error the rendering surface raises silently: **the page-data dimension shapes for `specialist` are different from `classic-gold` and different again from `fine-dining`** (3-tuples in some places · 4-tuples in services · flat dicts in others · a top-level `posts` list that is NOT nested inside `pubblicazioni` · a 4th `richiedi-visita` page kind that has no analogue in `classic-gold` at all). Without a written contract, the next builder will re-derive the shape implicitly from `template_content_denti.py` — slow, error-prone, and divergent.

---

## 0 · How to use this document

1. **Before any new `specialist` build** — read §1 → §17 in order. The Validation Checklist (§17) is the BLOCKING gate. Every item is a hard pre-flight.
2. **Every rule tagged `[BLOCKING]` is unconditional** — its violation prevents `tier: published_live`. No exceptions. Trap catalog (§16) calls out the defects that historically flipped through CLI green and were caught only on the browser walk or the multilingual sub-agent review.
3. Pair this document with:
   - `factory/standards/corporate-suite-blocking-rules.md` (the BLOCKING / REQUIRED / STRONG / GUIDELINE four-tag model used throughout).
   - `factory/standards/classic-gold-shape-contract.md` (the sibling lawyer-side contract; this `specialist` contract mirrors its structure deliberately).
   - `factory/references/template-inventory.md` (catalog state at the time of write).
   - `factory/references/anti-pattern-library.md` (AP-* incident anchors).
4. **Honesty over completeness** — where a key is observed in Denti but not Cardio (or vice versa), this document notes the divergence and identifies which one is the canonical anchor going forward. The default canonical anchor is **Denti** because it is the most recent build (T45+T46 · 2026-05-11) and the most thoroughly authored (888 lines in `template_content_denti.py` · richer `home` block · `trattamenti_tabs` · `percorso` · `location` · `faq` · explicit `richiedi-visita` flat-fields fallback).

---

## 1 · Purpose & scope

### 1.1 · What this standard governs

This contract governs **the shape**, not the semantics:

1. Which **HTML files** live in the skin folder and what they render.
2. Which **registry keys** must exist in `TEMPLATE_REGISTRY.json` and in `apps/catalog/template_dna.py` for an entry to be a valid `specialist` template.
3. Which **page-data keys** the rendering templates dereference at runtime — split per page-kind (home, about, services, team, blog_list, contact, appointment), with required sub-shapes.
4. The **distinctness scoreboard** that a new reuse must satisfy versus every prior reuse (Cardio + Derm + Denti).
5. The **trap catalog** — known defects that previously escaped the CLI but were caught on the browser walk, in second-look review, or in sub-agent translator hand-off.

### 1.2 · What this standard does NOT govern

- **Voice & tone copy** — that is `factory/agents/copy-translation-agent.md` + the per-template module docstring contract.
- **Imagery curation** — that is `factory/standards/corporate-suite-imagery-standard.md` (notwithstanding the `specialist` skin's editorial Pexels / Unsplash mix; the imagery surface rules are unchanged: zero PlayStation gamepads, zero generic stock).
- **Browser verification rubric** — that is `factory/standards/corporate-suite-browser-rubric.md` for the Playwright MCP recipes (specific to `specialist`'s `.sp-*` selectors).
- **Quality scorecard layers** — see `factory/standards/corporate-suite-quality-scorecard.md`.

This document only answers: *what does the skin need from the content tree to render without raising `TemplateSyntaxError` or producing visibly broken markup?* If the skin says `{% for num, title, blurb in page_data.signature_visits %}` and the content tree gives a list of dicts, the page raises `ValueError: too many values to unpack` (or, worse, renders dict-repr strings inline) — that is the class of error this contract prevents.

### 1.3 · BLOCKING / REQUIRED / STRONG / GUIDELINE

This document uses the four-tag severity model from `corporate-suite-blocking-rules.md` §2:

- `[BLOCKING]` — violation blocks merge and unconditionally blocks `published_live` flip.
- `[REQUIRED]` — violation blocks `published_live`; allowed to land at `draft` with a tracked TODO.
- `[STRONG]` — violation allowed only with a written deviation note in the module docstring + second reviewer.
- `[GUIDELINE]` — taste; document the reason if you break it.

---

## 2 · Archetype identity

### 2.1 · The shape signature

`specialist` is the **studio specialistico privato d'alta gamma · monoculo medico** archetype. From `apps/catalog/template_dna.py:56`:

```python
"specialist": "High-end specialist — editorial magazine layout with serif drama."
```

The signature is non-negotiable:

| Dimension | Required value (or band) | Source of truth |
|---|---|---|
| `archetype` | `"specialist"` literal | `template_dna.py:1424,1491,1544` |
| `density` | `"very-airy"` | `template_dna.py:1432,1499,1552` |
| `tone` | `"prestigious"` | `template_dna.py:1433,1500,1553` |
| `card_style` | `"editorial-large"` | `template_dna.py:1430,1497,1550` |
| `button_style` | `"ghost-underline"` | `template_dna.py:1431,1498,1551` |
| `navbar_style` | `"minimal-serif"` | `template_dna.py:1427,1494,1547` |
| `footer_style` | `"centered-minimal"` | `template_dna.py:1428,1495,1548` |
| `section_order` first three | `["nav", "editorial-hero", "drop-cap", ...]` | `template_dna.py:1429,1496,1549` |

### 2.2 · Palette polarities (canonical · diverge from these)

The three existing instances stake out three distinct polarities for the archetype. Any fourth reuse **must** pick a fourth distinct polarity that does NOT collapse to a recolor of red / forest-green / mint.

| Instance | `primary` (ink) | `secondary` (paper) | `accent` | Mood |
|---|---|---|---|---|
| Cardio | `#1c1612` ink-near-black | `#f7f3ee` cream paper | `#9c2a2a` ledger-red (bordeaux-cardiologico) | clinico-discreto · cardiology |
| Derm | `#1c1612` ink-near-black | `#f7f3ee` cream paper | `#3d5437` forest-green | dermatology-editorial · luxe-clinical |
| Denti | `#0F2D40` deep clinical blue | `#F7F3EE` cream paper | `#2BC4A4` fresh-mint | dentistry-bright · accessible-premium |
| **Fourth reuse candidate (Petro slot)** | propose | propose | must NOT be red, forest-green, or mint | propose |

Plausible 4th polarities (illustrative for the Petro veterinary cluster, not prescriptive — the planner is free to invent):

- **veterinary-warm** — `#2A1F12` cuoio + cream + `#C28A3A` ambra-miele (warm-clinical, animal-care kinship).
- **veterinary-pewter** — `#1C1F22` peltro + cream + `#7A8D94` blu-azzurro (sober-clinical, contemporary).
- **veterinary-terracotta** — `#1F1817` ink + paper + `#B3573D` terracotta (umano-animale grounding).

Source: `TEMPLATE_REGISTRY.json:717-721` (Cardio) · `TEMPLATE_REGISTRY.json:761-765` (Derm) · `TEMPLATE_REGISTRY.json:807-811` (Denti).

### 2.3 · Typography

The skin reads `theme.heading_font` and `theme.body_font` directly (see `_base.html:10,28-29,72-73`). Both fonts must:

- Be available on Google Fonts (no self-host).
- Provide italic for the `<em>` headline emphasis (the skin uses `h1 em` italic across every hero and section heading).
- Provide weight 400/500/600/700 and ital 400/500 (the skin requests both axes — see `_base.html:10`).
- Be present in the font-pairing taxonomy at `template_dna.py`. Used pairings:

| Instance | Heading | Body |
|---|---|---|
| Cardio | Cormorant Garamond | Inter |
| Derm | Bodoni Moda | Inter |
| Denti | DM Serif Display | Inter |

**[BLOCKING] `SP-T-01`**: Heading font MUST be a serif with strong italic (the entire `sp-hero h1`, `sp-hero .intro`, `sp-hero .right .quote`, `sp-history`, etc. depend on serif italic distinction). All three existing instances pick a different serif.

**[BLOCKING] `SP-T-02`**: A new reuse's heading font MUST NOT be Cormorant Garamond, Bodoni Moda, or DM Serif Display. The font-pairing axis is one of the three load-bearing distinctness axes (§15, axis 3).

**[STRONG] `SP-T-03`**: Body font SHOULD be Inter (all three instances use it). Inter is the de-facto body for the archetype; an alternative (e.g. Public Sans, Manrope) is allowed only with a written deviation note documenting why the editorial tabular-figure feel survives the swap.

### 2.4 · Hero / navbar / footer styles

The skin permits three hero variants — two are observed (`editorial-serif` for Cardio + Derm · `editorial-magazine` for Denti) and one further variant (`split-consultive`) is reserved for a hypothetical future reuse but not currently rendered (the DNA value is informational; the skin branches on `hero_variant` in `home.html:744`). The navbar and footer styles MUST stay in lockstep with the hero. Source: `template_dna.py:1426-1428, 1493-1495, 1546-1548`.

| Style key | Cardio value | Derm value | Denti value | Notes |
|---|---|---|---|---|
| `hero_style` | `editorial-serif` | `editorial-serif` | `editorial-magazine` | Skin checks `home.html:744` `{% if page_data.hero_variant == "editorial-magazine" %}` |
| `navbar_style` | `minimal-serif` | `minimal-serif` | `minimal-serif` | all three identical · skin does not branch |
| `footer_style` | `centered-minimal` | `centered-minimal` | `centered-minimal` | all three identical · skin does not branch |

**[BLOCKING] `SP-H-01`**: `page_data.home.hero_variant` is read at render time at `home.html:744`. If a reuse picks `hero_style: "editorial-magazine"` in DNA, the content tree's `home.hero_variant` MUST be the string `"editorial-magazine"` verbatim — the skin does an `==` comparison, NOT a startswith. Mismatching the DNA `hero_style` and the content `hero_variant` ships the wrong hero silhouette.

**[BLOCKING] `SP-H-02`**: The editorial-magazine hero variant requires `page_data.home.chief.portrait` to be a valid URL (skin reads it at `home.html:746` as `background-image: url('{{ page_data.chief.portrait }}')`). Cardio/Derm use `editorial-serif` and DO NOT render the hero portrait — but a future reuse picking `editorial-magazine` MUST ship the chief portrait or the hero left column will render an empty grey rectangle.

### 2.5 · Density / tone / conversion_pattern

From `template_dna.py:1432-1436, 1499-1510, 1552-1556`:

| Key | Cardio | Derm | Denti | Permitted values for new reuses |
|---|---|---|---|---|
| `density` | `"very-airy"` | `"very-airy"` | `"very-airy"` | `"very-airy"` only — `specialist` cannot be `medium` or `dense`; the 90-px hero paddings + 64-72-px section gaps are load-bearing |
| `tone` | `"prestigious"` | `"prestigious"` | `"prestigious"` | `"prestigious"` is the canonical value. A deviation (`luxe-clinical`, `editorial-medical`, `prestigious-warm`) is acceptable with a written note |
| `conversion_pattern` | `"private-request"` | `"private-request"` | `"booking-widget"` | Two patterns observed. `private-request` is the slow, low-pressure intake (Cardio + Derm); `booking-widget` is the calendar-style intake (Denti). NO `book-now-pay-now`, `add-to-cart`, `strategy-call`. The archetype's promise is *editorial, considered medical contact*, even when the CTA is calendar-style |
| `imagery_key` | `"medical-cardiology"` | `"medical-dermatology"` | `"medical-dental"` | MUST be a dedicated key in `preview_imagery.IMAGERY_CONFIG` — never share with a sibling cluster |

**[BLOCKING] `SP-D-01`**: `density != "very-airy"` blocks `published_live`.

**[BLOCKING] `SP-D-02`**: `conversion_pattern` MUST be one of `{private-request, booking-widget}`. Other patterns (`book-now-pay-now`, `add-to-cart`, `strategy-call`, `instant-quote`) block merge. The archetype's promise is *medical contact*, not e-commerce.

**[REQUIRED] `SP-D-03`**: The `conversion_pattern` value in DNA MUST be coherent with the `home.primary_cta` verb in the content tree:
- `private-request` ↔ CTA verb in the family of `"Richiedi visita privata"` (Cardio · Derm) / `"Richiedi un consulto"` / `"Prenota una prima visita"`.
- `booking-widget` ↔ CTA verb in the family of `"Prenota igiene"` (Denti) / `"Prenota online"` / `"Prenota appuntamento"`.

Picking `conversion_pattern: "private-request"` with `primary_cta: "Prenota online"` is an SP-D-03 violation: the DNA and content disagree about the conversion mechanic and the appointment-page form rendering will pick the wrong default.

---

## 3 · HTML skin folder

The folder `templates/live_templates/medical/specialist/` is the canonical skin. D-051 Option A applies: **a `specialist` reuse adds ZERO new HTML files**. All differentiation lives in the DNA `content` block, the content tree, and (in some cases) `preview_archetype` for the preview generator only.

### 3.1 · File table

| File | Lines | Page-kind it renders | Top-level page-data keys it dereferences |
|---|---:|---|---|
| `_base.html` | 650 | chrome (nav + footer) for all pages | `site.*`, `chrome.*`, `theme.*`, `template.*`, `pages`, `locale_switcher`, `is_rtl`, `preview_project`, `brand.*` |
| `home.html` | 1117 | `home` | `hero_variant`, `eyebrow`, `headline`, `intro`, `primary_cta`, `primary_href`, `secondary_cta`, `secondary_href`, `facts`, `manifesto_drop_cap`, `manifesto`, `hero_sidebar_top_label`, `hero_sidebar_quote`, `hero_sidebar_author`, `hero_sidebar_pulse`, `anchor_nav`, `signature_visits_label`, `signature_visits_heading`, `signature_visits_intro`, `signature_visits`, `trattamenti_tabs` (Denti only), `chief_label`, `chief_heading`, `chief.{name,role,bio,portrait}`, `percorso.{label,heading,intro,steps[]}`, `press`, `press_label`, `tecnologie` (Cardio only), `gallery_strip` (Derm only), `credentials` (Derm only), `testimonianza` (Cardio only), `before_after` (Derm-extensible), `editorial_feed` (extensible), `insurance` (extensible), `faq.{label,heading,items[]}`, `cta_heading`, `cta_primary_label`, `cta_secondary_label`, `location.{label,heading,intro,details,hours_short,cta_label,cta_href,map_fallback_image}` |
| `about.html` | 171 | `about` | `eyebrow`, `headline`, `intro`, `history[]`, `studio_image`, `studio_image_caption`, `method_title`, `method_paragraphs[]`, `values_label`, `values_heading`, `values[]`, `cta_heading`, `cta_primary_label`, `cta_secondary_label` |
| `services.html` | 148 | `services` | `eyebrow`, `headline`, `intro`, `service_image`, `service_image_caption`, `treatments[]`, `footnote_heading`, `footnote`, `cta_heading`, `cta_primary_label`, `cta_secondary_label` |
| `team.html` | 102 | `team` | `eyebrow`, `headline`, `intro`, `doctors[]`, `portrait_city` |
| `blog_list.html` | 126 | `blog_list` | `eyebrow`, `headline`, `intro`, `lead_image`, plus `posts` from the top-level content tree |
| `blog_detail.html` | 125 | `blog_detail` (per-post URL) | per-post `kicker`, `title`, `date`, `read_min`, `author`, `lede`, `body[]`, plus `footer_strap`, `empty_body_fallback_paragraphs` from `blog_list` page-data |
| `contact.html` | 193 | `contact` | `eyebrow`, `headline`, `intro`, `blocks[]`, `form_title`, `form_intro`, `form_placeholders.{first_name,last_name,email,phone,subject,message}`, `form_helpers.{...}` (may be empty dict), `form_consent`, `form_submit_note`, `hours_heading`, `hours[]`, `transport_heading`, `transport[]` |
| `appointment.html` | 220 | `appointment` (specialist-only kind, no analogue in classic-gold) | `eyebrow`, `headline`, `intro`, `process_label`, `process_heading`, `process[]`, `form_title`, `form_band_side_note`, `form_band_side_note_small`, `form_sections[]` (optional · falls back to flat `form_fields`), `form_fields[]`, `upload_field`, `consent`, `submit_label`, `form_submit_note`, `footnote` |

### 3.2 · D-051 Option A · zero new HTML

**[BLOCKING] `SP-HTML-01`** — A new `specialist` reuse MUST NOT add or modify files under `templates/live_templates/medical/specialist/`. If you find yourself wanting to change `home.html` to fit your content, you are deriving a new archetype (rename and isolate the skin) — not reusing `specialist`.

This rule is what made the T45 Denti build land in 1 day instead of 4: zero new HTML, all the work was in the content tree. The pattern was first proven by the Derm reuse (which validated that Cardio's skin could carry a forest-green dermatology brand without touching a single template file).

### 3.3 · CSS prefix invariant

All component CSS classes are prefixed `.sp-` (e.g. `.sp-hero`, `.sp-hero-em`, `.sp-history`, `.sp-method`, `.sp-fields`, `.sp-chief`, `.sp-percorso`, `.sp-press`, `.sp-faq`, `.sp-cta`, `.sp-treatments`, `.sp-team`, `.sp-doctors`, `.sp-posts`, `.sp-article`, `.sp-form`). The skin's RTL block and responsive breakpoints all target `.sp-*`.

**[STRONG] `SP-HTML-02`** — Do not rename the prefix even if your brand wordmark starts with a different letter. The skin's chrome, RTL block, and breakpoints all target `.sp-*`. Renaming breaks the cascade.

### 3.4 · The 9-file specialist surface vs the 8-file classic-gold surface

This is the key skin-shape divergence from `classic-gold`: `specialist` has **9 HTML files**, not 8. The 9th file is `appointment.html` (220 lines) which renders the `appointment` page-kind for the `richiedi-visita` slug. This page-kind has NO analogue in `classic-gold` (lawyers route appointment-style requests through the `contact` page only). The `specialist` skin treats the appointment as a first-class page so that:

- A patient who clicks "Richiedi visita privata" or "Prenota igiene" lands on a dedicated form-with-process-strip page (NOT a generic contact form).
- The form structure is opinionated: 4-step process strip up top · long flat form with sections + flat fallback below.

**[BLOCKING] `SP-HTML-03`** — Every `specialist` reuse MUST register a 7th page with `kind: "appointment"` AND populate the corresponding page-data dict (§12). Skipping the appointment page silently breaks the home-page primary CTA href.

---

## 4 · DNA registration

A `specialist` template's entry in `apps/catalog/template_dna.py` MUST contain all the keys listed below. Denti is the canonical example (verbatim from `template_dna.py:1490-1540`):

```python
"denti-co-studio": {
    "archetype":          "specialist",
    "preview_archetype":  "specialist-denti",
    "hero_style":         "editorial-magazine",
    "navbar_style":       "minimal-serif",
    "footer_style":       "centered-minimal",
    "section_order":      ["nav", "editorial-hero", "drop-cap",
                           "fields", "press", "footer"],
    "card_style":         "editorial-large",
    "button_style":       "ghost-underline",
    "density":            "very-airy",
    "tone":               "prestigious",
    "imagery_direction":  "dental-clinical — operatory, patient-forward "
                          "portraits, zero close-up bocche aperte",
    "imagery_key":        "medical-dental",
    "conversion_pattern": "booking-widget",
    "font_pairing":       ("DM Serif Display", "Inter"),
    "content": { ... see §4.3 ... },
},
```

### 4.1 · Required keys

| Key | Type | Required? | Notes |
|---|---|---|---|
| `archetype` | str | **[BLOCKING]** | literal `"specialist"` |
| `hero_style` | str | **[BLOCKING]** | one of `{"editorial-serif", "editorial-magazine"}` (`split-consultive` reserved but not currently rendered) |
| `navbar_style` | str | **[BLOCKING]** | `"minimal-serif"` only |
| `footer_style` | str | **[BLOCKING]** | `"centered-minimal"` only |
| `section_order` | list[str] | **[REQUIRED]** | first item `"nav"`, second `"editorial-hero"`, third `"drop-cap"` |
| `card_style` | str | **[REQUIRED]** | `"editorial-large"` only |
| `button_style` | str | **[REQUIRED]** | `"ghost-underline"` only |
| `density` | str | **[BLOCKING]** | `"very-airy"` only |
| `tone` | str | **[REQUIRED]** | canonical `"prestigious"` |
| `imagery_direction` | str | **[REQUIRED]** | one-line editorial brief for imagery-curator |
| `imagery_key` | str | **[BLOCKING]** | dedicated key in `preview_imagery.IMAGERY_CONFIG` |
| `conversion_pattern` | str | **[BLOCKING]** | `private-request` OR `booking-widget` (§2.5) |
| `font_pairing` | tuple[str, str] | **[BLOCKING]** | (heading, body); heading MUST be a NEW serif (§2.3 SP-T-02) |
| `content` | dict[str, Any] | **[BLOCKING]** | see §4.3 |
| `preview_archetype` | str | **[STRONG]** | only if you need a different preview-composition file |

### 4.2 · `preview_archetype` — when to set it

All three existing instances set `preview_archetype` (Cardio: `"specialist-cardio"` · Derm: `"specialist-derm"` · Denti: `"specialist-denti"`) because the preview-generator looks up `templates/preview_compositions/medical/<preview_archetype>.html`. **[STRONG] `SP-PREV-01`** — every `specialist` reuse SHOULD set a unique `preview_archetype` so the preview card surfaces the brand-specific accent + portrait + headline. The bare-`"specialist"` fallback exists but produces a generic preview.

### 4.3 · `content` block — DNA-side copy

The DNA's `content` block holds the **preview-card** copy plus a small subset of fields used by the editor as starter values. It is NOT the full content tree. Required keys (verbatim from Denti · `template_dna.py:1512-1539`):

| Key | Type | Notes |
|---|---|---|
| `eyebrow` | str | preview hero eyebrow |
| `headline` | str (with `<em>`) | preview hero headline · the noun-em italic anchor (§14) |
| `subhead` | str | preview hero subhead |
| `primary_cta` | str | preview CTA verb (`"Richiedi visita privata"` or `"Prenota igiene"` etc) |
| `phone` | str | E.164-ish formatted |
| `drop_cap` | str (1 char) | first letter of `intro_paragraph` |
| `intro_paragraph` | str | preview manifesto body — the dropped-cap continues from `drop_cap` |
| `fields` | list[tuple[str, str, str]] (2 items typical) | preview signature visits: `(num, title, blurb)` |
| `hero_meta` | list[tuple[str, str]] (3 items) | preview meta-strip rows: `(label, value)` |
| `credit_left`, `credit_right` | tuple[str, str] | preview credit cells |
| `press` | list[str] (4-5 items) | logo-marquee labels |
| `nav_links` | list[str] (4-5 items) | preview navbar labels |

The full content tree (with all seven page-kinds populated) lives in `apps/catalog/template_content.py` (Cardio inline · Derm inline) or `apps/catalog/template_content_<slug>.py` (Denti and any future reuse) — see §5.

**[STRONG] `SP-DNA-01`** — New reuses SHOULD follow the Denti pattern (dedicated `template_content_<slug>.py` module) rather than inline Cardio/Derm pattern. The dedicated module is easier to translate, easier to review per-locale, and matches the established Denti + Atto precedent. Cardio + Derm being inline is a legacy of pre-Wave-1 builds.

---

## 5 · Page-data top-level shape

The page-data tree is the **per-locale** dict imported from `template_content_<slug>_<locale>.py` (Denti pattern) or declared inline as `<SLUG>_CONTENT_<LOCALE>` (Cardio + Derm pattern). From `apps/catalog/template_content.py:2659-2688`, Denti's tree is registered as:

```python
"denti-co-studio": {
    "it": DENTI_CONTENT_IT,
    "en": DENTI_CONTENT_EN,
    "fr": DENTI_CONTENT_FR,
    "es": DENTI_CONTENT_ES,
    "ar": DENTI_CONTENT_AR,
},
```

Each `*_CONTENT_*` dict has the same top-level shape (verbatim from `template_content_denti.py:57-66`):

```python
DENTI_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Studio",         "kind": "home"},
        {"slug": "studio",          "label": "Lo Studio",      "kind": "about"},
        {"slug": "visite",          "label": "Trattamenti",    "kind": "services"},
        {"slug": "medici",          "label": "Dentisti",       "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Pubblicazioni",  "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contatti",       "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Prenota igiene", "kind": "appointment"},
    ],
    "site": { ... },           # chrome (rendered by _base.html)
    "home": { ... },           # rendered by home.html
    "studio": { ... },         # rendered by about.html (kind=about)
    "visite": { ... },         # rendered by services.html (kind=services)
    "medici": { ... },         # rendered by team.html (kind=team)
    "pubblicazioni": { ... },  # rendered by blog_list.html
    "posts": [ ... ],          # posts list (each post powers blog_detail.html) · TOP-LEVEL
    "contatti": { ... },       # rendered by contact.html
    "richiedi-visita": { ... } # rendered by appointment.html
}
```

### 5.1 · Top-level keys

| Key | Type | Required? | Read by |
|---|---|---|---|
| `pages` | list[dict] | **[BLOCKING]** | `_base.html:583,598,617` (nav + footer iterations) |
| `site` | dict | **[BLOCKING]** | `_base.html` (chrome: logo, address, phone, email, hours, license, footer_intro) |
| `home` | dict | **[BLOCKING]** | `home.html` |
| `studio` | dict | **[BLOCKING]** | `about.html` (page slug from `pages[]`) |
| `visite` | dict | **[BLOCKING]** | `services.html` |
| `medici` | dict | **[BLOCKING]** | `team.html` |
| `pubblicazioni` | dict | **[BLOCKING]** | `blog_list.html` |
| `posts` | list[dict] | **[BLOCKING]** | `blog_detail.html` (top-level, NOT nested · see §10.2) |
| `contatti` | dict | **[BLOCKING]** | `contact.html` |
| `richiedi-visita` | dict | **[BLOCKING]** | `appointment.html` |

**[BLOCKING] `SP-PD-01`** — All 10 keys are mandatory. The view layer does `page_data = content[page.slug]` (semantic — see `apps/catalog/views.py`). A missing key 404s the corresponding route.

**[BLOCKING] `SP-PD-02`** — The 7 page slugs are **SHAPE-PARITY invariant** across all locale files. The `label` value MAY be translated (e.g. IT `"Studio"` → EN `"Practice"` → AR `"المركز"`), but the `slug` MUST be the literal Italian token in every locale tree. The view layer routes by slug. Trap §16.3.

### 5.2 · `pages[]` shape

Each entry is a dict with three keys (verbatim from `template_content_denti.py:59-65`):

```python
{"slug": "home", "label": "Studio", "kind": "home"}
```

- `slug` — URL segment; matches the page-data dict key (except `home` → the dict key is also `"home"`).
- `label` — navbar/footer link text (translated per locale).
- `kind` — page-kind discriminator (see §13).

**[BLOCKING] `SP-PD-03`** — `pages[]` MUST list exactly the 7 slugs in the exact order above: `home, studio, visite, medici, pubblicazioni, contatti, richiedi-visita`. The order is reproduced in the navbar at `_base.html:583,598`; reordering the list reorders the user's navigation.

### 5.3 · `site` shape

The chrome data is read by `_base.html`. Observable keys (verbatim from `template_content_denti.py:68-85`):

| Key | Type | Read at | Notes |
|---|---|---|---|
| `logo_initial` | str (1-2 chars) | `_base.html:594` (`.sp-nav .crest`) | crest letters |
| `logo_word` | str | `_base.html:595,612` | brand name |
| `tag` | str | (reserved for nav-tag display) | short eyebrow on nav |
| `phone` | str | `_base.html:628` | telephone display |
| `email` | str | (footer / contact cross-reference) | inst. email |
| `address` | str | `_base.html:627` | one-line address |
| `hours_compact` | str | (footer compact hours) | one-line hours |
| `hours_footer_rows` | list[str] | (footer additional hours) | additional rows |
| `license` | str | (footer · OMCeO / Iscrizione albo medico) | medical-board registration line |
| `footer_intro` | str | `_base.html:613` | paragraph in footer brand column |

**[REQUIRED] `SP-SITE-01`** — `license` MUST cite a real medical-board registration format (`"Iscrizione OMCeO <city> <code>"` or analogue per region). The specialist archetype's credibility leans on this footer line; a placeholder ("TODO: registration") is a public-flip blocker.

---

## 6 · Page-data: `home`

The home dict feeds `home.html`. Verbatim shape (anchored to `template_content_denti.py:87-421` · the most thoroughly authored home block).

### 6.1 · Hero variant switch

**[BLOCKING] `SP-HOME-01`** — `hero_variant` is read at `home.html:744` and MUST be one of `{"editorial-magazine", "split-consultive"}` (default). Cardio uses `"split-consultive"` (the default fallback path); Derm uses `"editorial-magazine"`; Denti uses `"editorial-magazine"`. The string must match the DNA `hero_style` (§2.4 SP-H-01).

### 6.2 · Hero block

| Key | Type | Render at |
|---|---|---|
| `hero_variant` | str | `home.html:744` (`{% if ... == "editorial-magazine" %}`) |
| `eyebrow` | str | `home.html:748,765` |
| `headline` | str (with `<em>` italic emphasis) | `home.html:749,766` (uses `\|safe`) |
| `intro` | str | `home.html:750,767` |
| `primary_cta`, `primary_href` | str (slug ref) | `home.html:757,769` |
| `secondary_cta`, `secondary_href` | str (slug ref) | `home.html:758,770` |
| `hero_sidebar_top_label` | str | `home.html:775` (editorial-serif variant only) |
| `hero_sidebar_quote` | str | `home.html:779` |
| `hero_sidebar_author` | str | `home.html:780` |
| `hero_sidebar_pulse` | **list[tuple[str, str]]** (3 items) | `home.html:752,783` unpacks `for label, value in ...` |

**[BLOCKING] `SP-HOME-02`** — `hero_sidebar_pulse` MUST be 2-tuples, NOT dicts. The skin uses positional unpacking `for label, value in ...`. A dict-shaped pulse entry will iterate as keys and render the dict-repr literally. Trap §16.1.

**[BLOCKING] `SP-HOME-03`** — `hero_sidebar_pulse` is exactly 3 items of `(label, value)`. Both editorial-serif and editorial-magazine variants render exactly 3 pulse cells.

**[BLOCKING] `SP-HOME-04`** — When `hero_variant == "editorial-magazine"`, `chief.portrait` MUST be a non-empty URL (used at `home.html:746` as the hero portrait background). Empty string + editorial-magazine variant → grey empty hero. See §2.4 SP-H-02.

### 6.3 · Facts band (3-fact)

| Key | Type | Render at |
|---|---|---|
| `facts` | **list[tuple[str, str]]** (exactly 3 items) | `home.html:792` unpacks `for num, lbl in ...` |

**[BLOCKING] `SP-HOME-05`** — `facts` is exactly 3 items of `(number, label)`. All three existing instances ship 3 facts (Cardio: 15 anni · 1.200 visite · 4 ospedali · Derm: 18 anni · 2.400 mappature · 3 sale · Denti: 12 anni · 3.400 igieni · 4 dentisti). The skin grids 3 columns; a 4th fact wraps and breaks the band.

### 6.4 · Manifesto with drop-cap

| Key | Type | Render at |
|---|---|---|
| `manifesto_drop_cap` | str (exactly 1 char) | `home.html:811` (prepended to manifesto) |
| `manifesto` | str | `home.html:811` (continues from drop-cap) |

**[BLOCKING] `SP-HOME-06`** — `manifesto_drop_cap` is the first letter of the manifesto sentence. The skin concatenates them (`{{ page_data.manifesto_drop_cap }}{{ page_data.manifesto }}`), so the `manifesto` string MUST start with the letter that follows the drop-cap (Denti drop-cap `"L"` + manifesto `"a salute orale..."` → "La salute orale..."). A mismatch produces a typo on the page.

### 6.5 · Anchor subnav (optional)

| Key | Type | Render at |
|---|---|---|
| `anchor_nav` | **list[tuple[str, str]]** (4-5 items) | `home.html:800,803` (`{% if page_data.anchor_nav %}`) unpacks `for anchor_id, anchor_label in ...` |

Optional. Denti ships 5 anchors (metodo · trattamenti · percorso · medico · studio); Cardio + Derm omit the key. The skin gracefully no-renders when the key is absent.

### 6.6 · Signature visits (numbered 4-item ledger)

| Key | Type | Render at |
|---|---|---|
| `signature_visits_label` | str | `home.html:861` |
| `signature_visits_heading` | str (with `<em>`) | `home.html:862` (`\|safe`) |
| `signature_visits_intro` | str | `home.html:863` |
| `signature_visits` | **list[tuple[str, str, str]]** (exactly 4 items) | `home.html:866` unpacks `for num, title, blurb in ...` |

**[BLOCKING] `SP-HOME-07`** — `signature_visits` is a list of 3-tuples `(num, title, blurb)`. NOT a list of dicts. This is the most common shape-mismatch trap for a builder coming from `classic-gold` (where the equivalent `services` is a list of dicts). See trap §16.2.

**[BLOCKING] `SP-HOME-08`** — `signature_visits` is exactly 4 items. All three existing instances ship 4 numbered visits (Cardio: 4 · Derm: 4 · Denti: 4). The skin renders four 01/02/03/04 numbered ledger rows; 3 reads thin · 5+ visually breaks the dark ledger band.

### 6.7 · Trattamenti tabs (Denti-only · optional)

| Key | Type | Render at |
|---|---|---|
| `trattamenti_tabs.label` | str | `home.html:956` (`{% if page_data.trattamenti_tabs %}`) |
| `trattamenti_tabs.heading` | str (with `<em>`) | `home.html:957` |
| `trattamenti_tabs.intro` | str | `home.html:958` |
| `trattamenti_tabs.tabs` | list[dict] (4 items typical) | `home.html:961,965` iterates and reads `.id`, `.label`, `.eyebrow`, `.heading`, `.body`, `.items` (list of 2-tuples), `.cta_label`, `.cta_href` |

**[STRONG] `SP-HOME-09`** — `trattamenti_tabs` is optional but, when present, MUST have exactly 4 tabs (matching the 4 `signature_visits`). Denti uses it as a deep-dive complement to the signature visits; a future reuse may pick the same pattern OR skip the block entirely.

### 6.8 · Chief (lead doctor)

| Key | Type | Render at |
|---|---|---|
| `chief_label` | str | `home.html:883` |
| `chief_heading` | str (with `<em>`) | `home.html:884` |
| `chief.name` | str | `home.html:776,890` |
| `chief.role` | str | `home.html:889` |
| `chief.bio` | str | `home.html:891` |
| `chief.portrait` | str (URL) | `home.html:746,887` |

**[BLOCKING] `SP-HOME-10`** — `chief.portrait` MUST be a data-driven URL value coming from the content tree. The skin reads `{{ page_data.chief.portrait }}` at both `home.html:746` (hero, editorial-magazine variant) and `home.html:887` (chief section). Hardcoding the URL in the HTML skin (the T49 fine-dining trap pattern, see `factory/references/anti-pattern-library.md` AP-T49-hero-url) ships every reuse with the prime instance's portrait. Trap §16.4.

### 6.9 · Percorso (patient journey · optional)

| Key | Type | Render at |
|---|---|---|
| `percorso.label`, `percorso.heading`, `percorso.intro` | str | `home.html:1033-1035` (`{% if page_data.percorso %}`) |
| `percorso.steps` | list[dict] | `home.html:1037` iterates and reads `.num`, `.icon`, `.title`, `.desc`, `.duration` |

Denti ships 5 steps; Cardio + Derm omit the block. **[STRONG] `SP-HOME-11`** — when present, `percorso.steps` SHOULD be 4-5 items.

### 6.10 · Press strip (logo marquee)

| Key | Type | Render at |
|---|---|---|
| `press_label` | str | `home.html:903` |
| `press` | **list[str]** (5 items) | `home.html:904` |

**[REQUIRED] `SP-HOME-12`** — `press` is 5 uppercase logo-style strings (medical journals + lifestyle outlets). Cardio: 5 · Derm: 5 · Denti: 5. The press strip's visual rhythm depends on 5 elements.

### 6.11 · Optional content blocks (instance-specific)

Each is rendered behind an `{% if page_data.<key> %}` guard. Skipping all of them is acceptable; mixing them is acceptable.

| Block key | Shape | Used by | Render at |
|---|---|---|---|
| `tecnologie.{label,heading,items[]}` | items: list[dict] with `icon, title, desc` | Cardio | `home.html:814-819` |
| `gallery_strip.{label,images[]}` | images: list[tuple[str, str]] (url, caption) | Derm | `home.html:846-850` |
| `credentials.{label,items[]}` | items: list[tuple[str, str, str]] (abbr, desc, since) | Derm | `home.html:909-913` |
| `testimonianza.{quote,author,context}` | flat dict | Cardio | `home.html:924-929` |
| `before_after.{label,heading,disclaimer,pairs[]}` | pairs: list of image-pair dicts | (extensible · Derm-ready) | `home.html:986-991` |
| `editorial_feed.{label,items[]}` | items: list[tuple[str, str, str]] (url, meta, title) | (extensible) | `home.html:1014-1018` |
| `insurance.{items[]}` | items: list[tuple[str, str, str]] (fig, title, desc) | (extensible) | `home.html:1064-1067` |

### 6.12 · FAQ accordion

| Key | Type | Render at |
|---|---|---|
| `faq.label` | str | `home.html:936` (`{% if page_data.faq %}`) |
| `faq.heading` | str (with `<em>`) | `home.html:937` |
| `faq.items` | **list[tuple[str, str]]** (4-6 items) | `home.html:939` unpacks `for question, answer in ...` |

**[BLOCKING] `SP-HOME-13`** — `faq.items` is 2-tuples `(question, answer)`, NOT dicts.

### 6.13 · Location (map + address details · optional)

| Key | Type | Render at |
|---|---|---|
| `location.{label,heading,intro}` | str | `home.html:1080-1086` (`{% if page_data.location %}`) |
| `location.map_fallback_image` | str (URL) | `home.html:1080` (background) |
| `location.details` | list[tuple[str, str]] | `home.html:1088` unpacks `for d_lbl, d_val in ...` |
| `location.hours_short` | list[tuple[str, str]] | `home.html:1096` unpacks `for day, hours in ...` |
| `location.cta_label`, `location.cta_href` | str | `home.html:1100` |

Denti ships the full block (4 details + 3 hours); Cardio + Derm omit it.

### 6.14 · Final CTA band

| Key | Type | Render at |
|---|---|---|
| `cta_heading` | str (with `<em>`) | `home.html:1106` |
| `cta_primary_label` | str | `home.html:1108,1115` |
| `cta_secondary_label` | str | `home.html:1109` |

Note the CTA hrefs are hardcoded in the skin (`richiedi-visita` and `contatti`) — they reference the canonical slugs, NOT page_data keys. This is intentional (the CTA always sends to the appointment + contact pages).

---

## 7 · Page-data: `studio` (about)

The studio dict feeds `about.html`. Verbatim shape (anchored to `template_content_denti.py:423-503`).

### 7.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `about.html:117-119` |

### 7.2 · History timeline

| Key | Type | Render at |
|---|---|---|
| `history` | **list[tuple[str, str]]** (4-5 items) | `about.html:123` unpacks `for year, text in ...` |

**[BLOCKING] `SP-ABOUT-01`** — `history` is **2-tuples** `(year, text)`, NOT 3-tuples like classic-gold's `(year, headline, body)`. This is a per-archetype shape difference and a common cross-contamination trap when a builder works on both archetypes in the same session. Cardio + Derm + Denti all use 2-tuples.

Verbatim from Denti (`template_content_denti.py:435-451`):

```python
"history": [
    ("2013", "Fondazione dello studio associato in Via Manzoni ..."),
    ("2016", "Avvio del reparto implantologico con TAC cone-beam ..."),
    ("2019", "Adozione della scansione intraorale iTero ..."),
    ("2022", "Apertura del laboratorio ortodontico interno ..."),
    ("2025", "Lo studio chiude l'anno con quattro associati ..."),
],
```

### 7.3 · Studio image (optional)

| Key | Type | Render at |
|---|---|---|
| `studio_image` | str (URL) | `about.html:131,134` (`{% if page_data.studio_image %}`) |
| `studio_image_caption` | str | `about.html:135` |

### 7.4 · Method paragraphs

| Key | Type | Render at |
|---|---|---|
| `method_title` | str | `about.html:142` |
| `method_paragraphs` | **list[str]** (2-4 items) | `about.html:144` iterates as `for p in ...` |

### 7.5 · Values

| Key | Type | Render at |
|---|---|---|
| `values_label` | str | `about.html:152` |
| `values_heading` (with `<em>`) | str | `about.html:153` |
| `values` | **list[tuple[str, str]]** (exactly 4 items) | `about.html:155` unpacks `for title, blurb in ...` |

**[BLOCKING] `SP-ABOUT-02`** — `values` is exactly 4 **2-tuples** `(title, blurb)`. NOT 3-tuples (classic-gold), NOT dicts (specialist temptation). Denti's four values: "Diga di gomma sempre" · "Foto prima e dopo" · "Preventivo scritto" · "Follow-up programmato".

### 7.6 · CTA

| Key | Type | Render at |
|---|---|---|
| `cta_heading` (with `<em>`) | str | `about.html:165` |
| `cta_primary_label`, `cta_secondary_label` | str | `about.html:167,168` |

Note: the about-page CTA links are hardcoded in the skin (`medici` for primary, `richiedi-visita` for secondary).

---

## 8 · Page-data: `visite` (services)

The visite dict feeds `services.html`. Verbatim shape (anchored to `template_content_denti.py:506-585`).

### 8.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `services.html:106-108` |

### 8.2 · Service image (optional)

| Key | Type | Render at |
|---|---|---|
| `service_image` | str (URL) | `services.html:111,114` (`{% if page_data.service_image %}`) |
| `service_image_caption` | str | `services.html:115` |

### 8.3 · Treatments list

| Key | Type | Render at |
|---|---|---|
| `treatments` | **list[tuple[str, str, str, str]]** (5-12 items) | `services.html:121` unpacks `for name, meta, desc, price in ...` |

**[BLOCKING] `SP-SVC-01`** — `treatments` is **4-tuples** `(name, meta, desc, price)`, NOT dicts and NOT 3-tuples. This is the single most divergent shape in the contract: every other tuple in the specialist archetype is either a 2-tuple or 3-tuple; `treatments` is a 4-tuple because the skin renders a price column on every services card. Trap §16.5.

Verbatim from Denti (`template_content_denti.py:521-572`):

```python
"treatments": [
    ("Igiene professionale singola",
     "45 min · senza richiesta del medico curante",
     "Charting parodontale, indice di sanguinamento ...",
     "€ 95"),
    ("Piano annuale di mantenimento",
     "annuale · 2 igieni + 1 controllo + radiografie endorali",
     "Due igieni semestrali calendarizzate ...",
     "€ 220"),
    # ... 6 more
],
```

**[BLOCKING] `SP-SVC-02`** — Service tuple position is positional: `(name, meta, desc, price)`. Swapping `meta` and `desc` ships visually-broken cards (meta string in the long description row and vice versa). Cardio + Derm + Denti all preserve the same positional order.

**[BLOCKING] `SP-SVC-03`** — `price` is a string (locale-formatted currency), NOT a number. Use `"€ 95"`, `"€ 1.850"`, `"su preventivo"`, `"incluso"`. The skin treats the price as a styled label.

### 8.4 · Footnote

| Key | Type | Render at |
|---|---|---|
| `footnote_heading` | str | `services.html:136` |
| `footnote` | str | `services.html:137` |

### 8.5 · CTA

| Key | Type | Render at |
|---|---|---|
| `cta_heading` (with `<em>`) | str | `services.html:142` |
| `cta_primary_label`, `cta_secondary_label` | str | `services.html:144,145` |

The CTA href targets are hardcoded in the skin (`richiedi-visita` + `contatti`).

---

## 9 · Page-data: `medici` (team)

The medici dict feeds `team.html`. Verbatim shape (anchored to `template_content_denti.py:587-656`).

### 9.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `team.html:72-74` |

### 9.2 · Doctors list

| Key | Type | Render at |
|---|---|---|
| `doctors` | **list[dict]** (3-5 items) | `team.html:78` |
| `portrait_city` | str | `team.html:82` (`d.portrait_city\|default:page_data.portrait_city`) |

Each doctor dict required keys (verbatim from Denti · `template_content_denti.py:598-653`):

| Doctor key | Type | Required? | Used at |
|---|---|---|---|
| `name` | str | **[BLOCKING]** | card heading |
| `role` | str | **[BLOCKING]** | card eyebrow |
| `bio` | str | **[REQUIRED]** | card body paragraph |
| `portrait` | str (URL) | **[REQUIRED]** | card portrait background |
| `portrait_city` | str | **[GUIDELINE]** | per-doctor city override; defaults to page-level `portrait_city` |
| `tags` | list[str] | **[GUIDELINE]** | optional Cardio-style specialization tags |
| `links` | list[tuple[str, str]] | **[GUIDELINE]** | optional PubMed / ORCID links (Cardio convention) |

**[BLOCKING] `SP-TEAM-01`** — doctor dict keys are `{name, role, bio, portrait}`. NOT classic-gold's `{name, role, specialization, foro, year, bio}`. The medical archetype tracks role (specialization-as-prose) inside `role` itself, not in a separate `specialization` field. Cardio + Derm + Denti all converge on this shape.

**[BLOCKING] `SP-TEAM-02`** — Every doctor portrait MUST be a unique URL (no two doctors share a portrait). The portrait is part of the brand's editorial signature; reusing a single portrait across the team reads as a stock-content shortcut and fails the imagery walk.

**[REQUIRED] `SP-TEAM-03`** — `doctors` list MUST be 3-5 items. 1-2 items reads thin and breaks the grid; 6+ dilutes the editorial-team feel. Cardio: 3 · Derm: 3-4 · Denti: 4.

Compressed example (see `apps/catalog/template_content_denti.py:598-608` for full):

```python
{
    "name":  "Dr.ssa Chiara Vespa",
    "role":  "Direttore sanitario · Conservativa & endodonzia",
    "bio":   "Specialista in odontoiatria conservativa formatasi ...",
    "portrait": _CHIEF_PORTRAIT,
},
```

---

## 10 · Page-data: `pubblicazioni` (publications · blog_list)

The pubblicazioni dict feeds `blog_list.html`. Verbatim shape (anchored to `template_content_denti.py:658-679`).

### 10.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `blog_list.html:89-91` |
| `lead_image` | str (URL) | `blog_list.html:97` (background-image on lead post) |
| `footer_strap` | str | `blog_detail.html:121` (footer bottom strap) |
| `empty_body_fallback_paragraphs` | list[str] | `blog_detail.html:114` fallback when post body is empty |

### 10.2 · `posts` (top-level, NOT under `pubblicazioni`)

The post list lives at the **top level** of the content tree (alongside `home`, `studio`, etc.), NOT nested under `pubblicazioni`. This is a deliberate architecture: each post is reachable at `/pubblicazioni/<slug>/` and the view layer scans `content["posts"]` independent of the `pubblicazioni` page.

Each post dict required keys (verbatim from `template_content_denti.py:684-735` · 4 posts):

| Post key | Type | Notes |
|---|---|---|
| `slug` | str | URL segment |
| `kicker` | str | category eyebrow on detail page |
| `title` | str | full post title |
| `date` | str (e.g. "12 marzo 2025") | locale-aware human date |
| `read_min` | int OR str (Cardio uses int 6, 4, 5; Denti uses int 8, 12, 6, 5) | reading-time minutes — INT preferred |
| `author` | str | doctor name |
| `lede` | str | summary paragraph |
| `body` | list[tuple[str, str \| list]] | rich-body cells; each `(kind, text)`. Cardio ships full bodies; Denti ships `lede` only and falls back to `empty_body_fallback_paragraphs`. |

The `body` 2-tuple kinds observed in Cardio: `"p"`, `"h2"`, `"ol"` (text is a `list[str]`), `"blockquote"`. The skin branches on each kind at `blog_detail.html:101-117`.

**[BLOCKING] `SP-PUB-01`** — `posts` is at the **top level** of the content tree, not nested. The skin reads `posts` (NOT `page_data.posts`) at `blog_list.html:95,109`. Nesting it under `pubblicazioni` silently 404s every post route. Trap §16.6.

**[REQUIRED] `SP-PUB-02`** — `posts` count is 4-6. Fewer than 4 reads thin; more than 6 dilutes the editorial-calendar feel. Cardio: 5 · Derm: 4-5 · Denti: 4.

**[STRONG] `SP-PUB-03`** — At least the first post (the lead post) SHOULD ship a populated `body` (not rely on `empty_body_fallback_paragraphs`). The lead post is the one that anchors the editorial credibility of the blog page.

---

## 11 · Page-data: `contatti` (contact)

The contatti dict feeds `contact.html`. Verbatim shape (anchored to `template_content_denti.py:741-802`).

### 11.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `contact.html:96-98` |

### 11.2 · Info blocks

| Key | Type | Render at |
|---|---|---|
| `blocks` | **list[tuple[str, str, str]]** (exactly 4 items) | `contact.html:105` unpacks `for label, value, sub in ...` |

**[BLOCKING] `SP-CONTACT-01`** — `blocks` is **3-tuples** `(label, value, sub)`, NOT dicts. The four SVG icons (pin · phone · email · clock) are hardcoded in the skin and visually pair with the four block entries in order. The 4-item count is also fixed.

Verbatim from Denti (`template_content_denti.py:750-763`):

```python
"blocks": [
    ("Sede",     "Via Manzoni 18\n20121 Milano", "Piano nobile · ingresso indipendente"),
    ("Telefono", "+39 02 7770 4488",             "Risposta in giornata lavorativa"),
    ("Email",    "studio@denticostudio.it",      "Per richieste non urgenti"),
    ("Orari",    "Lun – Ven · 8:30 – 19:30...",  "Domenica chiuso"),
],
```

### 11.3 · Form

| Key | Type | Render at |
|---|---|---|
| `form_title` | str | `contact.html:115` |
| `form_intro` | str | `contact.html:116` |
| `form_placeholders` | **dict[str, str]** (keys: first_name, last_name, email, phone, subject, message) | `contact.html:117` |
| `form_helpers` | **dict[str, str]** (same keys as placeholders · may be empty `{}`) | `contact.html:117` |
| `form_consent` | str | `contact.html:149,153` |
| `form_submit_note` | str | `contact.html:161-164` (`{% if page_data.form_submit_note %}`) |

**[BLOCKING] `SP-CONTACT-02`** — `form_placeholders` keys are exactly `{first_name, last_name, email, phone, subject, message}`. NOT a list, NOT a dict-of-dicts. The skin does `{% with ph=page_data.form_placeholders %}` and reads `ph.first_name` etc. Missing keys render an empty placeholder.

**[GUIDELINE] `SP-CONTACT-03`** — `form_helpers` may be `{}` (empty dict · Denti pattern) when the field labels are self-explanatory, or a full helper dict (Cardio pattern) when the form has its own micro-copy register.

### 11.4 · Hours

| Key | Type | Render at |
|---|---|---|
| `hours_heading` | str | `contact.html:174` |
| `hours` | **list[tuple[str, str, str]]** (exactly 7 items: Mon-Sun) | `contact.html:175` unpacks `for day, am, pm in ...` |

**[BLOCKING] `SP-CONTACT-04`** — `hours` is exactly 7 **3-tuples** `(day, am, pm)`. NOT 5 items (Mon-Fri), NOT dicts. Saturday + Sunday rows MUST be present (use `"Chiuso"` / `"—"` strings when closed). The skin renders all 7 rows; missing weekend rows breaks the week grid.

Verbatim from Denti (`template_content_denti.py:785-793`):

```python
"hours": [
    ("Lunedì",    "8:30 – 13:00", "14:00 – 19:30"),
    # ... Mar/Mer/Gio/Ven
    ("Sabato",    "9:00 – 13:00", "—"),
    ("Domenica",  "—",            "Chiuso"),
],
```

### 11.5 · Transport

| Key | Type | Render at |
|---|---|---|
| `transport_heading` | str | `contact.html:183` |
| `transport` | **list[tuple[str, str]]** (3-4 items) | `contact.html:184` unpacks `for label, text in ...` |

**[BLOCKING] `SP-CONTACT-05`** — `transport` is **2-tuples** `(label, text)`, NOT 3-tuples (no `sub` field on transport rows).

---

## 12 · Page-data: `richiedi-visita` (appointment)

The richiedi-visita dict feeds `appointment.html`. Verbatim shape (anchored to `template_content_denti.py:808-887` and `template_content.py:752-851` for Cardio).

This is the page-kind that has no analogue in `classic-gold`: a dedicated appointment-with-form page driven by the `conversion_pattern` DNA key (§2.5).

### 12.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `appointment.html:87-89` |

### 12.2 · Process strip

| Key | Type | Render at |
|---|---|---|
| `process_label` | str | `appointment.html:93` |
| `process_heading` (with `<em>`) | str | `appointment.html:94` |
| `process` | **list[tuple[str, str, str]]** (exactly 4 items) | `appointment.html:97` unpacks `for num, title, blurb in ...` |

**[BLOCKING] `SP-APP-01`** — `process` is exactly 4 **3-tuples** `(num, title, blurb)`. Cardio + Denti both ship 4 numbered process steps; the skin renders 01/02/03/04. Departure breaks the strip rhythm.

### 12.3 · Form

| Key | Type | Render at |
|---|---|---|
| `form_title` | str | `appointment.html:110` |
| `form_band_side_note` | str | `appointment.html:112` |
| `form_band_side_note_small` | str (optional) | `appointment.html:113-114` (`{% if ... %}`) |
| `form_sections` | list[dict] (optional · 4 sections typical) | `appointment.html:121-122` (`{% if page_data.form_sections %}`) |
| `form_fields` | list[dict] (8-9 fields typical) | `appointment.html:151,175` |
| `upload_field` | dict (optional · `{name,label,helper,accept,multiple,primary,link,meta}`) | `appointment.html:130-131` |
| `consent` | str | `appointment.html:197` |
| `submit_label` | str | `appointment.html:202` |
| `form_submit_note` | str (optional) | `appointment.html:205-208` |
| `footnote` | str | `appointment.html:218` |

**[BLOCKING] `SP-APP-02`** — Each `form_fields[]` dict has shape `{name, label, type, required, placeholder?, helper?, options?, full_width?}`. The `type` value MUST be one of `{text, email, tel, number, select, textarea}`. Skin behaviour for `select` requires the `options: list[str]` key (without it, the select renders empty).

**[STRONG] `SP-APP-03`** — `form_sections[]` are optional but, when present, MUST reference field `name` values declared in `form_fields[]` via their `fields` list. The literal sentinel `"__upload__"` slots the upload field into a section. The skin falls back to a flat field list when `form_sections` is absent (see `appointment.html:121,175`). Denti chose the flat-fallback path (no `form_sections`); Cardio uses the 4-section structure.

**[BLOCKING] `SP-APP-04`** — `consent` MUST cite a real GDPR Art. 6 / data-protection clause with a DPO contact. The specialist archetype's appointment intake collects health-context information; a placeholder consent string is a public-flip blocker. Trap §16.7.

### 12.4 · Cardio vs Denti divergence

The richiedi-visita page is the surface where the `conversion_pattern` axis shows up most visibly:

- **Cardio (private-request)**: 8 form fields organized in 4 `form_sections` (Chi sei · Di che visita hai bisogno · Documenti utili · Descrivi il caso) + 1 `upload_field` for ECG / lab reports. Form_band_side_note: *"Le richieste compilate con cura sono lette dal medico per intero — quelle frettolose, no."*
- **Denti (booking-widget)**: 7 form fields in a flat list (no `form_sections`) + no `upload_field`. Form_band_side_note: *"Risposta entro 24 ore lavorative. Per le urgenze cliniche chiamate direttamente il +39 02 7770 4488."*

Both are valid. A new reuse picks the pattern consistent with its DNA `conversion_pattern` (§2.5, SP-D-03).

---

## 13 · `page_kind` mapping

The skin selection is **page-kind driven**, not page-slug driven. The view layer maps the slug to a kind via `pages[].kind`, then looks up the rendering template.

Observed mapping (from `template_content_denti.py:58-66` and the skin folder):

| Slug (canonical) | `kind` | Template file |
|---|---|---|
| `home` | `home` | `medical/specialist/home.html` |
| `studio` | `about` | `medical/specialist/about.html` |
| `visite` | `services` | `medical/specialist/services.html` |
| `medici` | `team` | `medical/specialist/team.html` |
| `pubblicazioni` | `blog_list` | `medical/specialist/blog_list.html` |
| (each `posts[].slug`) | `blog_detail` | `medical/specialist/blog_detail.html` |
| `contatti` | `contact` | `medical/specialist/contact.html` |
| `richiedi-visita` | `appointment` | `medical/specialist/appointment.html` |

**[BLOCKING] `SP-KIND-01`** — `kind` values are exactly the 8 listed (`home`, `about`, `services`, `team`, `blog_list`, `blog_detail`, `contact`, `appointment`). Other kinds (`menu`, `gallery`, `reservations`, `case_study`) belong to restaurant / portfolio archetypes; using them on `specialist` will fail the template lookup.

**[BLOCKING] `SP-KIND-02`** — `appointment` is the specialist-unique kind. A reuse that does NOT register a 7th page with `kind: "appointment"` violates SP-HTML-03 AND breaks the home-page CTA which sends to the appointment route.

Note the slug convergence: all three existing instances pick the same IT slugs (`home / studio / visite / medici / pubblicazioni / contatti / richiedi-visita`). This is INTENTIONAL — the slug pattern is locale-independent: when a Cardio AR locale renders `/pubblicazioni/`, the URL path is the Italian token even though the navbar label is Arabic. **[STRONG] `SP-KIND-03`** — new reuses SHOULD keep the canonical IT slug names verbatim. A deviation (e.g. `trattamenti` instead of `visite`) is allowed but creates a SHAPE-PARITY break that the planner must document explicitly.

---

## 14 · Voice anchor pattern

The voice anchor is a noun-em phrase that the brand repeats across surfaces. It is the brand's compact memory: render it in the hero headline (with `<em>` italic), in the manifesto, in at least one signature-visit label, and ideally in the appointment-page eyebrow. Each new reuse MUST pick a distinct anchor.

### 14.1 · Existing anchors

| Instance | Anchor (IT) | EN | FR | ES | AR | Approx surface count (IT/EN/FR/ES/AR) |
|---|---|---|---|---|---|---|
| Cardio | `su misura` | tailored / bespoke | sur mesure | a medida | حسب القياس | (cross-surface across 5 locales) |
| Derm | `carta d'identità` | identity (card) | carte d'identité | tarjeta de identidad | بطاقة هوية | (cross-surface across 5 locales) |
| Denti | `igiene` | hygiene | hygiène | higiene | النظافة الفموية | 16 / 26 / 17 / 14 / 12 (T46 multilingual close) |

**Denti baseline (T46 sub-agent translator close)**: the voice anchor `igiene` surfaces 16 times in IT, 26 times in EN, 17 times in FR, 14 times in ES, and 12 times in AR. This asymmetry is documented in `TEMPLATE_REGISTRY.json:844` (Denti tier_reason) — EN ramps up because English "hygiene" is also the operational name for the Denti hygiene-as-product offering (multiple service-card names + bookable item names use the word literally). AR dips because MSA prefers the longer compound `النظافة الفموية` (oral hygiene) and the AR translator condensed surfaces where prose would have become awkward.

### 14.2 · Verbatim-in-translation rule

The translator-agent MUST preserve the chosen anchor verbatim across all 5 locales — not transliterated, not literally calqued, but **identified to its register equivalent**:

- EN: institutional / clinical-premium register (FT Health, NYT Wellness, JAMA-adjacent prose).
- FR: `vous` register equivalent of the EN target (Le Monde Santé, Conseil National de l'Ordre des Médecins).
- ES: peninsular `usted` register (El País Sociedad, El País Buena Vida).
- AR: MSA premium medical register (Asharq Al-Awsat health pages) with Latin proper names preserved via `unicode-bidi: isolate` + Latin digits per the specialist-AR house style first established by Cardio (D-059 RTL pilot, Session 23) and re-applied by Denti T46.

See `TEMPLATE_REGISTRY.json:844` for the Denti T46 surface-count accounting — this is the canonical pattern.

**[BLOCKING] `SP-VOICE-01`** — Translator may not "improve" the anchor's locale variant. The anchor is THE name. Once `igiene` is set, the EN counterpart is `hygiene` everywhere it appears, not `cleaning`/`oral care`/`prevention` ad-hoc.

**[BLOCKING] `SP-VOICE-02`** — A new reuse's anchor MUST be distinct from `su misura`, `carta d'identità`, and `igiene` at the semantic level (not just lexically). `personalizzato` is too close to `su misura`. Candidates: `riabilitazione`, `prevenzione`, `vigilanza`, `accompagnamento`, `seguito`, `prossimità` (depending on the medical sub-discipline).

**[BLOCKING] `SP-VOICE-03`** — The anchor MUST surface ≥ 8 times in IT (the baseline locale). The Denti baseline of 16/26/17/14/12 sets the floor; a build that ships only 4 anchor surfaces in IT reads as one-shot brand language, not as a repeated brand signature.

---

## 15 · Distinctness scoreboard (D-054)

A new reuse MUST diverge from every prior reuse on at least 8 of the 12 axes. The Cardio · Derm · Denti columns are pre-filled.

| # | Axis | Cardio | Derm | Denti | New reuse (Petro slot) — propose |
|---:|---|---|---|---|---|
| 1 | Medical sub-discipline | cardiology | dermatology | dentistry | (4th sub-discipline — veterinary cluster) |
| 2 | Accent polarity | `#9c2a2a` ledger-red | `#3d5437` forest-green | `#2BC4A4` fresh-mint | (4th polarity · §2.2 · NOT red/green/mint) |
| 3 | Font pairing | Cormorant Garamond + Inter | Bodoni Moda + Inter | DM Serif Display + Inter | (4th pairing · §2.3 SP-T-02) |
| 4 | Voice anchor | `su misura` | `carta d'identità` | `igiene` | (4th anchor · §14.2 SP-VOICE-02) |
| 5 | Conversion CTA | `private-request` (`Richiedi visita privata`) | `private-request` (`Prenota una prima visita`) | `booking-widget` (`Prenota igiene`) | (third verb category — paid/subscription/community/etc) |
| 6 | Lead-doctor gender | Dr. Marani (M) | Dr.ssa Ricciardi (F) | Dr.ssa Vespa (F) | (M lead recommended to balance F·F prior) |
| 7 | Geography (city · district) | Roma · Parioli | Roma · Veneto | Milano · Brera | (NEW city OR NEW region · NOT Roma NOT Milano) |
| 8 | Imagery direction | clinical-cardiovascular (ECG, stethoscope, consultation · Unsplash) | aesthetic-clinical (skin, dermatoscopy, treatment rooms · Unsplash) | dental-clinical (operatory, patient-forward portraits · Pexels `medical-dental`) | (4th imagery key in `IMAGERY_CONFIG` · NEW Pexels OR Unsplash pool) |
| 9 | Hero variant | `editorial-serif` | `editorial-serif` | `editorial-magazine` (portrait-driven) | (third variant · OR ship a distinct serif/magazine balance) |
| 10 | Service catalog shape | 6 treatments · diagnostic-procedural (€ 140-980) | 8 treatments · clinical+aesthetic (€ N/A on cards · upper-end) | 8 treatments · routine-priced (€ 95-3.200) | (different catalog · 5-12 items · distinct price band) |
| 11 | Optional home blocks pattern | `tecnologie` + `testimonianza` | `gallery_strip` + `credentials` | `trattamenti_tabs` + `percorso` + `location` + `faq` | (4th composition · pick distinct optional blocks) |
| 12 | Price tier (registry `price`) | € 109 (premium) | € 115 (premium) | € 75 (standard) | (4th tier · distinct from 75/109/115) |

**[BLOCKING] `SP-D-04`** — Score ≥ 8/12 vs every prior reuse, with at least one of {axis 2 (accent), axis 4 (voice anchor), axis 8 (imagery key)} divergent. Same accent OR same anchor OR same imagery direction = the templates collapse into recolors of each other. This is the same gate Denti passed at T45 (proven against Cardio + Derm) and the same one the Petro build must pass against Cardio + Derm + Denti.

The scorecard is enforced by review at PR time. See `TEMPLATE_REGISTRY.json:839` for Denti's `reuse_notes` field — the canonical example of how a new reuse documents its distinctness against every prior reuse in a single paragraph.

---

## 16 · Trap catalog

Defects observed during the Cardio (pre-Wave-1), Derm (pre-Wave-1), and Denti (T45 + T46 · 2026-05-11) builds. Each defect: what · symptom · root cause · prevention.

### 16.1 · `hero_sidebar_pulse` shape (3-tuple vs dict)

- **What**: builder wrote `hero_sidebar_pulse` as `list[dict]` (`[{label, value}, ...]`) instead of `list[tuple[str, str]]`.
- **Symptom**: hero right column renders `{'label': 'Studio', 'value': '...'}` literally; or the iterator `for label, value in page_data.hero_sidebar_pulse` raises `ValueError: too many values to unpack`.
- **Root cause**: classic-gold migration cross-contamination (classic-gold's analogous `hero_meta_strip` is also a 2-tuple, so this trap is rarer than the next one).
- **Prevention**: §6.2's SP-HOME-02 BLOCKER. CLI does NOT catch tuple-unpacking failures inside `{% for %}`.

### 16.2 · `signature_visits` shape from `classic-gold`

- **What**: builder copy-pasted classic-gold's home `practice` shape, which is also 3-tuples, but with field positions `(num, title, blurb)` — accidentally writing dicts instead because they were reading the `services.html` (services-page) classic-gold shape which IS dicts.
- **Symptom**: home renders `{'num': '01', ...}` literally in the signature-visits ledger; or the iterator raises `ValueError: too many values to unpack`.
- **Root cause**: classic-gold has the inverse pattern (home is 3-tuples · services is dicts) — a builder who learned classic-gold from the services-page may default to dicts.
- **Prevention**: §6.6's SP-HOME-07 BLOCKER. The mnemonic: in `specialist`, the home `signature_visits` is 3-tuples; the services-page `treatments` is **4-tuples** (NOT dicts).

### 16.3 · 7-page slug parity break across locales

- **What**: a translator sub-agent translated the slugs along with the labels (e.g. IT `pubblicazioni` → EN `publications` → FR `publications`).
- **Symptom**: the EN locale produces `/templates/medical/<slug>/publications/` instead of `/pubblicazioni/`, and the view layer 404s because `content["publications"]` does not exist.
- **Root cause**: translator sub-agent over-applied i18n to URL segments.
- **Prevention**: §5.1's SP-PD-02 BLOCKER. The voice-anchor preservation directive includes a slug-preservation reminder; the multilingual pre-flight checklist (§17.3) explicitly enumerates the 7 canonical slugs.

### 16.4 · Hero portrait URL hardcoded in skin

- **What**: a builder hardcoded the chief portrait URL directly in `home.html` (the T49 fine-dining trap pattern).
- **Symptom**: every reuse ships with the prime instance's portrait; the editor cannot swap the portrait without editing the skin file.
- **Root cause**: shortcut. The skin author thought "the portrait is always Dr. Marani so I'll just inline it"; the second reuse (Derm) inherited the wrong portrait.
- **Prevention**: §6.8's SP-HOME-10 BLOCKER. The portrait MUST be read from `page_data.chief.portrait` (already-correct in the current skin · see `home.html:746,887`). Any future skin edit that re-introduces a hardcoded URL fails the chrome-authoring contract.

### 16.5 · `treatments` 4-tuple positional swap

- **What**: builder wrote `treatments` as 4-tuples but swapped `meta` and `desc` positions (e.g. `(name, desc, meta, price)`).
- **Symptom**: services-page cards render the long description in the meta-eyebrow slot and the short meta string in the body — visually broken.
- **Root cause**: positional unpacking is unforgiving; CLI does not catch position swaps.
- **Prevention**: §8.3's SP-SVC-01 / SP-SVC-02 BLOCKERs. The mnemonic: `(name, meta, desc, price)` reads left-to-right top-to-bottom of the card.

### 16.6 · `posts` nested under `pubblicazioni`

- **What**: builder nested `posts` inside `pubblicazioni` (`content["pubblicazioni"]["posts"] = [...]`) instead of at top level.
- **Symptom**: blog_list page renders the page header but lists zero posts; every `/pubblicazioni/<slug>/` route 404s because `content["posts"]` is missing.
- **Root cause**: intuition — "posts belong to the pubblicazioni page, so they should be nested there."
- **Prevention**: §10.2's SP-PUB-01 BLOCKER. The skin reads `posts` (top-level context variable provided by the view layer), NOT `page_data.posts`.

### 16.7 · Placeholder GDPR consent string

- **What**: builder left `consent: "TODO: GDPR consent text"` in `richiedi-visita`.
- **Symptom**: appointment page renders the placeholder string on a live consent checkbox. Major credibility break for a medical site.
- **Root cause**: appointment-page consent feels like boilerplate and gets deferred.
- **Prevention**: §12.3's SP-APP-04 BLOCKER. Every reuse MUST cite GDPR Art. 6 with a real DPO email (typically `dpo@<brand-domain>`).

### 16.8 · `hero_variant` ↔ DNA `hero_style` mismatch

- **What**: DNA declared `hero_style: "editorial-magazine"` but content tree forgot to set `home.hero_variant = "editorial-magazine"` (or set it to `"split-consultive"` by copy-pasting from a sibling).
- **Symptom**: home page renders the default split-consultive hero with the wrong styling expectation. The portrait does NOT render because the editorial-magazine branch is not taken at `home.html:744`.
- **Root cause**: DNA and content tree are authored in different files; mismatch is silent.
- **Prevention**: §2.4's SP-H-01 BLOCKER. The pre-flight checklist (§17.2) calls out the cross-check explicitly.

### 16.9 · Font / palette / anchor convergence (D-054 collapse)

- **What**: a new reuse picked one of the three existing font pairings (Cormorant / Bodoni / DM Serif) or one of the three existing accent polarities (red / green / mint) or a near-duplicate voice anchor.
- **Symptom**: D-054 score drops below 8/12; the new reuse reads as a recolor of an existing instance.
- **Root cause**: the new builder did not read the prior reuses' DNA before authoring.
- **Prevention**: §15's SP-D-04 BLOCKER. The pre-flight checklist (§17.1) requires writing the D-054 scoreboard against every prior reuse in the new template's module docstring.

### 16.10 · Doctor gender + city + age homogeneity

- **What**: a new reuse picked another male lead doctor in Roma, age 50s — matching one of the prior instances on multiple secondary axes.
- **Symptom**: cluster facet reads as a single brand wearing different colors.
- **Root cause**: the planner anchored on the most accessible Italian-male-cardiologo / dermatologo archetype without checking the prior reuses.
- **Prevention**: §15 axes 6 + 7. Denti picked a female lead in Milano specifically to balance Cardio's Roma-male + Derm's Roma-female on two axes simultaneously; the next reuse should consider male + Bologna / Torino / Napoli / Padova / Verona OR female + new region.

---

## 17 · Validation checklist (BLOCKING gate)

The next `specialist` reuse MUST pass every check below in sequence. A reviewer may not skip a step. A failure at any step blocks `published_live` flip and (for steps 1-3) blocks even the draft-landing merge.

### 17.1 · Pre-build (registry + DNA + seed + cluster)

- [ ] **Registry entry exists** in `TEMPLATE_REGISTRY.json` with the required keys: `slug`, `name`, `category: "medical"`, `brand_name`, `tagline`, `palette` (primary/secondary/accent), `typography`, `personality`, `archetype: "specialist"`, `hero_style`, `navbar_style: "minimal-serif"`, `density: "very-airy"`, `tone: "prestigious"`, `conversion_pattern`, `live_preview: true`, `live_pages` (7 slugs + `pubblicazioni/<post>`), `locales` (5: it/en/fr/es/ar), `rtl: true`, `archetype_reuse: true`, `reuse_notes`, `price`, `featured`, `status`, `tier: "draft"`, `tier_reason`.
- [ ] **`live_pages`** lists slugs (NOT kinds). Use Denti's list as the template (`["home", "studio", "visite", "medici", "pubblicazioni", "contatti", "richiedi-visita"]`) plus `"pubblicazioni/<post>"` for per-post routes (Cardio/Derm convention) — Denti omitted the per-post route from its `live_pages` list, which is a documented Denti divergence; new reuses SHOULD follow the Cardio/Derm pattern and include the per-post route.
- [ ] **`archetype_reuse: true`** + `reuse_notes` written. The reuse_notes MUST enumerate the 12 D-054 axes (§15) versus EACH prior reuse (Cardio + Derm + Denti + any reuse landed in the meantime) and assert score ≥ 8.
- [ ] **DNA entry exists** in `apps/catalog/template_dna.py` with the 14 required keys (§4.1). Verify `archetype: "specialist"`, `density: "very-airy"`, `imagery_key` is a NEW dedicated key in `IMAGERY_CONFIG`.
- [ ] **`IMAGERY_CONFIG`** has a new dedicated `imagery_key` with 4-8 curated Pexels (preferred) or Unsplash URLs from the appropriate X.3 pack. Zero overlap with `medical-cardiology`, `medical-dermatology`, or `medical-dental` pools.
- [ ] **Brand registered** in `apps/catalog/brand_registry` (the seed migration path used by `manage.py seed_brands`). Honesty: this is enforced by existing tests; if you skip it the test suite fails immediately, which is the correct outcome.
- [ ] **Cluster facet** updated in catalog tests if a new medical sub-discipline is introduced (cardiology / dermatology / dentistry / veterinary / etc are separate facets).
- [ ] **DNA-vs-content cross-check**: DNA `hero_style` matches content `home.hero_variant`; DNA `conversion_pattern` matches content `home.primary_cta` verb (§2.5 SP-D-03).

### 17.2 · Build (content tree shape-parity)

- [ ] **`template_content_<slug>.py`** created in `apps/catalog/` (preferred over inline · SP-DNA-01). Module docstring includes the D-054 axes diff against EACH prior reuse, not just one.
- [ ] **Top-level shape** matches §5.1 exactly: `pages`, `site`, `home`, `studio`, `visite`, `medici`, `pubblicazioni`, `posts`, `contatti`, `richiedi-visita`. All 10 keys are MANDATORY. The 7 page slugs are exactly: `home, studio, visite, medici, pubblicazioni, contatti, richiedi-visita` (§5.2 SP-PD-03).
- [ ] **`home`** dict has all keys from §6, with `hero_sidebar_pulse` as 3 2-tuples, `facts` as 3 2-tuples, `signature_visits` as exactly 4 3-tuples, `faq.items` as 2-tuples, `chief.portrait` as a NON-HARDCODED data-driven URL. Trap §16.1, §16.2, §16.4.
- [ ] **`studio`** dict has all keys from §7, with `history` as 4-5 **2-tuples** (NOT 3-tuples like classic-gold), `values` as exactly 4 2-tuples.
- [ ] **`visite`** dict has `treatments` as 5-12 **4-tuples** `(name, meta, desc, price)`. Trap §16.5.
- [ ] **`medici`** dict has `doctors` as 3-5 dicts with shape `{name, role, bio, portrait}` (NOT classic-gold's 6-key shape).
- [ ] **`pubblicazioni`** dict has page header + `lead_image` + `footer_strap` + `empty_body_fallback_paragraphs`; `posts` is at the top level of the content tree (NOT nested). Trap §16.6.
- [ ] **`contatti`** dict has `blocks` as exactly 4 3-tuples, `hours` as exactly 7 3-tuples (full Mon-Sun), `transport` as 2-tuples, `form_placeholders` with the 6 canonical keys.
- [ ] **`richiedi-visita`** dict has `process` as exactly 4 3-tuples, `form_fields` with valid `type` values, `consent` citing GDPR Art. 6 with a real DPO email. Trap §16.7.
- [ ] **`apps/catalog/template_content.py`** imports the new `*_CONTENT_IT` module and registers it in `TEMPLATE_CONTENT` dict (note: the dict symbol is `TEMPLATE_CONTENT`, not `LIVE_CONTENT` — the spec brief refers to it generically as the live-content registry).
- [ ] **`manage.py check`** + **`manage.py test apps.catalog`** green.
- [ ] **`manage.py generate_previews --only <slug>`** produces a preview without raising.

### 17.3 · Multilingual (sub-agent translator pattern)

- [ ] **4 sub-agent translators** dispatched in parallel for EN/FR/ES/AR. Each translator receives the full IT module + the voice-anchor preservation directive (§14.2) + the slug-preservation directive (§5.1 SP-PD-02) + the `corporate-suite-design-standard.md` register guidance.
- [ ] **Voice anchor preserved verbatim-in-translation** across all 5 locales. Anchor surfaces counted (≥ 8 per locale · §14.2 SP-VOICE-03) — see Denti baseline of 16/26/17/14/12 for the kind of asymmetry that is acceptable.
- [ ] **`template_content_<slug>_en.py`**, `_fr.py`, `_es.py`, `_ar.py` all created at shape-parity with IT (same 10 top-level keys, same 7-page slug list, same tuple positions). Total ≈ 4 × ~880-1,100 lines (Denti: 3,516 lines across 4 locales).
- [ ] **Imports added** to `template_content.py` (`from apps.catalog.template_content_<slug>_<locale> import ..._CONTENT_<LOCALE>`).
- [ ] **AR-specific**: Latin proper names preserved via `unicode-bidi: isolate` chrome on `<bdi>` spans, Latin digits per the specialist-AR house style established by Cardio D-059 RTL pilot. Trap §16.3.
- [ ] **Staff `?preview=1` walk green**: 5 locales × 7 page-kinds = 35 routes return 200. Use `scripts/walk_preview.py` (or the equivalent) and attach the verdict to the T-report.

### 17.4 · Public flip (test cascade + anonymous walk + regression)

- [ ] **Tier flipped** in registry from `draft` to `published_live` via `manage.py sync_template_tiers` (NOT by hand-edit alone — the sync command is the contract).
- [ ] **Tier reason updated** to a single multi-fact paragraph that records: build pass-N · multilingual workflow · contrast walk verdict · anonymous walk verdict · cluster count delta · feature count delta · price-tier count delta. Use Denti's tier_reason as the template (`TEMPLATE_REGISTRY.json:844`).
- [ ] **`manage.py test apps.catalog`** green AFTER the flip — the catalog count assertions must be updated in the same PR. The specialist cluster facet count (Cardio + Derm + Denti = 3 · the new reuse bumps to 4) is one of the tracked assertions.
- [ ] **Anonymous public walk** green: hit every `live_pages[]` route at every `locales[]` value (≥ 7×5 = 35 routes), unauthenticated, in a fresh browser session. Verify the `?preview=1` query-string is NOT required.
- [ ] **AAA contrast walk** on ≥ 8 surfaces at 1440×900 + mobile (390×844). Document the pass/fail per surface in the T-report. Acceptable AA-but-not-AAA failures (e.g. ghost-underline button by-design muting at 4.x:1) must be explicitly noted as such, not silently passed.
- [ ] **Regression on previously-flipped `specialist` instances** (Cardio + Derm + Denti): unchanged. Walk a sample of routes for each to confirm no rendering regression from the shared skin.

### 17.5 · Sign-off

- [ ] **release-gatekeeper** signs off after reviewing §17.1-§17.4. The gatekeeper has unconditional authority to send the PR back at any point.
- [ ] **T-report** authored under `factory/reports/<wave>/<pass>-<slug>.md` with: build summary · multilingual summary · contrast walk · anonymous walk · D-054 scoreboard · cluster/feature/tier deltas · open follow-ups.
- [ ] **CLAUDE.md / SESSION_LOG.md / DECISIONS.md** updated per the project's coordination conventions.

The checklist is the gate. Every item is BLOCKING-grade for `published_live`. Most items are also BLOCKING-grade for merge (§17.1 + §17.2). Skip nothing.

---

## Appendix · canonical citations

For convenience, the canonical files cited by this contract:

- `apps/catalog/template_dna.py:56` — `specialist` archetype docstring.
- `apps/catalog/template_dna.py:1423-1466` — Derm DNA entry (1st reuse).
- `apps/catalog/template_dna.py:1490-1540` — Denti DNA entry (canonical example for §4 · most thoroughly authored).
- `apps/catalog/template_dna.py:1543-1586` — Cardio DNA entry (prime instance).
- `apps/catalog/template_content.py:79-1085` — Cardio inline content tree (`CARDIO_CONTENT_IT` · pre-Wave-1 inline pattern).
- `apps/catalog/template_content.py:1587-2616` — Derm inline content tree (`DERMATOLOGIA_CONTENT_IT` · pre-Wave-1 inline pattern).
- `apps/catalog/template_content_denti.py:1-888` — Denti dedicated content module (canonical example for §5-§12 · preferred pattern · SP-DNA-01).
- `apps/catalog/template_content.py:2659-2688` — `TEMPLATE_CONTENT` LIVE_CONTENT registration for the three specialist instances.
- `templates/live_templates/medical/specialist/_base.html` — chrome (650 lines).
- `templates/live_templates/medical/specialist/home.html` — home renderer (1,117 lines · 9-file specialist set's heaviest skin).
- `templates/live_templates/medical/specialist/about.html` — about/studio renderer (171 lines).
- `templates/live_templates/medical/specialist/services.html` — services/visite renderer (148 lines).
- `templates/live_templates/medical/specialist/team.html` — team/medici renderer (102 lines).
- `templates/live_templates/medical/specialist/contact.html` — contact/contatti renderer (193 lines).
- `templates/live_templates/medical/specialist/appointment.html` — richiedi-visita renderer (220 lines · specialist-unique kind).
- `templates/live_templates/medical/specialist/blog_list.html` — pubblicazioni renderer (126 lines).
- `templates/live_templates/medical/specialist/blog_detail.html` — single-post renderer (125 lines).
- `TEMPLATE_REGISTRY.json:711-754` — Cardio registry entry.
- `TEMPLATE_REGISTRY.json:755-800` — Derm registry entry.
- `TEMPLATE_REGISTRY.json:801-845` — Denti registry entry (canonical example for §17.1 + §17.4 tier_reason patterns · documents the T46 multilingual close).
- `factory/standards/corporate-suite-blocking-rules.md` — sibling standard, source of the four-tag severity model.
- `factory/standards/classic-gold-shape-contract.md` — sibling lawyer-side contract; this `specialist` contract mirrors its structure.

— End of contract.
