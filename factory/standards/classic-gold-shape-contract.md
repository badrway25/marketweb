# Classic-Gold Shape Contract

**Phase**: Wave 1 — Pass-5 follow-up · **Date**: 2026-05-12 · **Status**: BLOCKING for any new `classic-gold` template.

**Scope**: This document is the authoritative shape contract for the `classic-gold` lawyer archetype. It governs **every** future template that reuses `classic-gold` — i.e. shares the HTML skin under `templates/live_templates/lawyer/classic-gold/` and the DNA `archetype: "classic-gold"` key.

**Existing reuses at write time**:

| Slug | Brand | Polarity / accent | Geography | First seen |
|---|---|---|---|---|
| `lex-studio-legale` | Studio Legale Ferri | `#C5A55A` ledger-gold | Roma · Milano | pre-Wave-1 (prime instance) |
| `atto-notai-associati` | Studio Notarile Conti–Sironi–Verri | `#1F3A5F` ink-blue (notarial-archive) | Milano (Distretto Notarile) | T47/T48 (1st reuse) |

**Audience**: every agent and human who decides whether a new `classic-gold` template may be built, may merge, or may flip to `published_live` — release-gatekeeper, template-planner, template-builder, copy-translation-agent, browser-verifier, plus any reviewer signing off a PR against this archetype.

This standard exists because T47 caught a class of error that the deterministic test surface cannot catch: **the page-data dimension names for `classic-gold` are different from `specialist`** (3-tuples vs flat dicts, etc.). Without a written contract, the next builder will re-derive the shape implicitly from `template_content_atto.py` — slow, error-prone, and divergent.

---

## 0 · How to use this document

1. **Before any new `classic-gold` build** — read §1 → §16 in order. The Validation Checklist (§16) is the BLOCKING gate. Every item is a hard pre-flight.
2. **Every rule tagged `[BLOCKING]` is unconditional** — its violation prevents `tier: published_live`. No exceptions. Trap catalog (§15) calls out the seven defects that historically flipped through CLI green and were caught only on the browser walk.
3. Pair this document with:
   - `factory/standards/corporate-suite-blocking-rules.md` (the BLOCKING / REQUIRED / STRONG / GUIDELINE four-tag model used throughout).
   - `factory/references/template-inventory.md` (catalog state at the time of write).
   - `factory/references/anti-pattern-library.md` (AP-* incident anchors).
4. **Honesty over completeness** — where a key is observed in Atto but not Lex (or vice versa), this document notes the divergence and identifies which one is the canonical anchor going forward.

---

## 1 · Purpose & scope

### 1.1 · What this standard governs

This contract governs **the shape**, not the semantics:

1. Which **HTML files** live in the skin folder and what they render.
2. Which **registry keys** must exist in `TEMPLATE_REGISTRY.json` and in `apps/catalog/template_dna.py` for an entry to be a valid `classic-gold` template.
3. Which **page-data keys** the rendering templates dereference at runtime — split per page-kind (home, about, services, team, blog_list, contact), with required sub-shapes.
4. The **distinctness scoreboard** that a new reuse must satisfy versus every prior reuse (Lex + Atto).
5. The **trap catalog** — known defects that previously escaped the CLI but were caught on the browser walk or in second-look review.

### 1.2 · What this standard does NOT govern

- **Voice & tone copy** — that is `factory/agents/copy-translation-agent.md` + the per-template module docstring contract.
- **Imagery curation** — that is `factory/standards/corporate-suite-imagery-standard.md` (notwithstanding `classic-gold` ≠ corporate-suite, the imagery surface rules are identical: editorial Pexels, no Unsplash demo, no PlayStation gamepads).
- **Browser verification rubric** — that is `factory/standards/corporate-suite-browser-rubric.md` for the Playwright MCP recipes (specific to `classic-gold`'s `.lx-*` selectors).
- **Quality scorecard layers** — see `factory/standards/corporate-suite-quality-scorecard.md`.

This document only answers: *what does the skin need from the content tree to render without raising `TemplateSyntaxError` or producing visibly broken markup?* If the skin says `{{ page_data.practice.0.0 }}` and the content tree gives a flat dict, the page renders wrong — that is the class of error this contract prevents.

### 1.3 · BLOCKING / REQUIRED / STRONG / GUIDELINE

This document uses the four-tag severity model from `corporate-suite-blocking-rules.md` §2:

- `[BLOCKING]` — violation blocks merge and unconditionally blocks `published_live` flip.
- `[REQUIRED]` — violation blocks `published_live`; allowed to land at `draft` with a tracked TODO.
- `[STRONG]` — violation allowed only with a written deviation note in the module docstring + second reviewer.
- `[GUIDELINE]` — taste; document the reason if you break it.

---

## 2 · Archetype identity

### 2.1 · The shape signature

`classic-gold` is the **istituzionale studio legale / notarile** archetype. From `apps/catalog/template_dna.py:75`:

```python
"classic-gold": "Istituzionale studio legale — ink page with gold monogram
                 crest, serif drama headline, vertical rule ledger, numbered
                 practice areas and partner portrait cards. Forensic,
                 notarile, high-trust."
```

The signature is non-negotiable:

| Dimension | Required value (or band) | Source of truth |
|---|---|---|
| `archetype` | `"classic-gold"` literal | `template_dna.py:509,559` |
| `density` | `"airy"` | `template_dna.py:517,566` |
| `tone` | `"<noun>-notarile"` (forensic-notarile · institutional-notarile · …) | `template_dna.py:518,567` |
| `card_style` | `"<noun>-ledger"` (practice-area-ledger · atto-area-ledger · …) | `template_dna.py:515,564` |
| `button_style` | `"serif-<noun>-border"` (serif-gold-border · serif-archive-border · …) | `template_dna.py:516,565` |
| `section_order` first three | `["ink-nav", "ledger-hero", <ledger>]` | `template_dna.py:514,563` |

### 2.2 · Palette polarities (canonical · diverge from these)

The two existing instances stake out two of the three plausible polarities for the archetype. Any third reuse **must** pick a third distinct polarity.

| Instance | `primary` (ink) | `secondary` (accent rule) | `accent` (italic em) | Mood |
|---|---|---|---|---|
| Lex | `#1A1A2E` (notte-blu) | `#C5A55A` (gold) | `#8B0000` (bordeaux) | ledger-prestige · forensic |
| Atto | `#0F1A2A` (ink-notarile) | `#F1ECE4` (paper-2) | `#1F3A5F` (ink-blue · notarial-archive) | archivio · pubblica fede |
| **Third reuse candidate** | propose | must NOT be gold and must NOT be ink-blue | propose | propose |

Plausible 3rd polarities (illustrative, not prescriptive — the planner is free to invent):
- **labor-law** — `#2A1F12` cuoio + `#A47F4A` brass + `#6E2A1A` mattone (industrial-craft mood).
- **family-office** — `#101B1E` verde-foresta + `#D7C9A8` champagne-opaco + `#3A5A3F` salvia (private-bank discretion).
- **commercialista-classic** — `#1B1F2E` ardesia + `#B89968` ottone-spazzolato + `#234D52` petrolio (forensic-fiscal).

Source: `TEMPLATE_REGISTRY.json:852-856` (Lex) and `TEMPLATE_REGISTRY.json:890-894` (Atto).

### 2.3 · Typography

The skin reads `theme.heading_font` and `theme.body_font` directly (see `_base.html:10,34-35`). Both fonts must:

- Be available on Google Fonts (no self-host).
- Provide italic for the `<em>` headline emphasis (the skin uses `h1 em` italic, `_base.html:91`).
- Be present in the font-pairing taxonomy at `template_dna.py`. Used pairings:

| Instance | Heading | Body |
|---|---|---|
| Lex | Cormorant Garamond | Inter |
| Atto | Source Serif 4 | Public Sans |

**[BLOCKING] `CG-T-01`**: Heading font MUST be a serif with strong italic (the entire `lx-hero h1 em`, `lx-history .year-cell` etc. depend on serif italic distinction).

**[STRONG] `CG-T-02`**: Body font SHOULD be a humanist sans with tabular-figure support — the stats band uses `font-variant-numeric: tabular-nums` (`_base.html:96-100`).

### 2.4 · Hero / navbar / footer styles

The skin permits two hero variants (one per existing instance) and they MUST stay in lockstep with the navbar and footer styles. Source: `template_dna.py:511-513,560-563`.

| Style key | Lex value | Atto value | Notes |
|---|---|---|---|
| `hero_style` | `split-ledger-monogram` | `split-archive-monogram` | both render `.lx-hero` two-column; right column has monogram crest + meta-strip |
| `navbar_style` | `ledger-monogram` | `archive-monogram` | both render `.lx-nav` with `.crest` |
| `footer_style` | `ledger-institutional` | `archive-institutional` | both render `.lx-foot` with 4-column top |

**[REQUIRED] `CG-H-01`**: The three style triples MUST be cohesive (all "ledger" or all "archive" or all "<noun>"). The skin does not branch on the style key — it is a labeling convention enforced by review. Picking `hero_style: split-ledger-monogram` with `navbar_style: archive-monogram` is a `CG-H-01` violation.

### 2.5 · Density / tone / conversion_pattern

From `template_dna.py:517-521, 566-570`:

| Key | Lex | Atto | Permitted values for new reuses |
|---|---|---|---|
| `density` | `"airy"` | `"airy"` | `"airy"` only — `classic-gold` cannot be `medium` or `dense`; the 100-px section paddings are load-bearing |
| `tone` | `"forensic-notarile"` | `"institutional-notarile"` | any `<noun>-notarile` or `forensic-<noun>` or `institutional-<noun>` — the suffix anchors the archetype |
| `conversion_pattern` | `"private-consultation"` | `"primo-incontro-orientamento"` | any low-pressure intake pattern. NO `strategy-call`, `book-now`, `add-to-cart`. The CTA on `classic-gold` is editorial and slow |
| `imagery_key` | `"lawyer-classic"` | `"lawyer-notary"` | MUST be a dedicated key in `preview_imagery.IMAGERY_CONFIG` — never share with a sibling cluster |

**[BLOCKING] `CG-D-01`**: `density != "airy"` blocks `published_live`.

**[BLOCKING] `CG-D-02`**: `conversion_pattern` referencing automated calendar booking / e-commerce-style funnel blocks merge. The archetype's promise is *slow institutional contact*.

---

## 3 · HTML skin folder

The folder `templates/live_templates/lawyer/classic-gold/` is the canonical skin. D-051 Option A applies: **a `classic-gold` reuse adds ZERO new HTML files**. All differentiation lives in the DNA `content` block, the content tree, and (in some cases) `preview_archetype` for the preview generator only.

### 3.1 · File table

| File | Lines | Page-kind it renders | Page-data keys it dereferences (top-level) |
|---|---:|---|---|
| `_base.html` | 601 | chrome (nav + footer) for all pages | `site.*`, `chrome.*`, `theme.*`, `template.*`, `pages`, `locale_switcher`, `is_rtl`, `preview_project` |
| `home.html` | 372 | `home` | `eyebrow`, `headline`, `intro`, `primary_cta`, `primary_href`, `secondary_cta`, `secondary_href`, `hero_credit_left`, `hero_credit_right`, `hero_meta_strip`, `practice_label`, `practice_heading`, `practice_intro`, `practice`, `stats_heading`, `stats`, `partners_label`, `partners_heading`, `partners_intro`, `partners`, `publications_label`, `publications`, `cta_label`, `cta_heading`, `cta_intro`, `cta_primary`, `cta_primary_href`, `cta_secondary`, `cta_secondary_href` |
| `about.html` | 172 | `about` | `eyebrow`, `headline`, `intro`, `history_label`, `history_heading`, `history_intro`, `history`, `values_label`, `values_heading`, `values_intro`, `values`, `coordinates_label`, `coordinates`, `cta_heading`, `cta_intro`, `cta_primary`, `cta_primary_href` |
| `services.html` | 143 | `services` | `eyebrow`, `headline`, `intro`, `services`, `svc_lead_label`, `svc_jurisdiction_label`, `process_label`, `process_heading`, `process`, `cta_heading`, `cta_intro`, `cta_primary`, `cta_primary_href` |
| `team.html` | 117 | `team` | `eyebrow`, `headline`, `intro`, `lawyers`, `lawyer_specialization_label`, `lawyer_foro_label`, `lawyer_year_label` |
| `contact.html` | 237 | `contact` | `eyebrow`, `headline`, `intro`, `form_label`, `form_heading`, `form_intro`, `form_sections`, `form_fields`, `upload_field`, `form_consent`, `form_submit_label`, `form_submit_note`, `offices_label`, `offices`, `office_*_label`, `channels_label`, `channels`, `footnote` |
| `blog_list.html` | 145 | `blog_list` | `eyebrow`, `headline`, `intro`, `lead_image`, plus `posts` from the top-level content tree |
| `blog_detail.html` | 131 | `blog_detail` (per-post URL) | per-post `kicker`, `title`, `date`, `read_min`, `author`, `lede`, `body[]`, plus `footer_strap`, `empty_body_fallback_paragraphs` from `blog_list` page-data |

### 3.2 · D-051 Option A · zero new HTML

**[BLOCKING] `CG-HTML-01`** — A new `classic-gold` reuse MUST NOT add or modify files under `templates/live_templates/lawyer/classic-gold/`. If you find yourself wanting to change `home.html` to fit your content, you are deriving a new archetype (rename and isolate the skin) — not reusing `classic-gold`.

This rule is what made the T47 Atto build land in 1 day instead of 4: zero new HTML, all the work was in the content tree. See `apps/catalog/template_content_atto.py:1088-1096` for the explicit "chrome-authoring contract" docstring that codifies D-047.

### 3.3 · CSS prefix invariant

All component CSS classes are prefixed `.lx-` (legacy from "Lex" → the prime instance). The skin uses `.lx-nav`, `.lx-hero`, `.lx-practice`, `.lx-stats-band`, `.lx-partners-prev`, `.lx-publications`, `.lx-cta`, `.lx-lead`, `.lx-section`, `.lx-foot`, `.lx-history`, `.lx-services`, `.lx-form`, `.lx-contact-wrap`.

**[STRONG] `CG-HTML-02`** — Do not rename the prefix even if your brand wordmark starts with a different letter. The skin's RTL block and the responsive breakpoints (e.g. `_base.html:455-505`) all target `.lx-*`. Renaming breaks the cascade.

---

## 4 · DNA registration

A `classic-gold` template's entry in `apps/catalog/template_dna.py` MUST contain all the keys listed below. Atto is the canonical example (verbatim from `template_dna.py:508-556`):

```python
"atto-notai-associati": {
    "archetype":          "classic-gold",
    "preview_archetype":  "classic-gold-notary",     # optional · §4.2
    "hero_style":         "split-archive-monogram",
    "navbar_style":       "archive-monogram",
    "footer_style":       "archive-institutional",
    "section_order":      ["ink-nav", "ledger-hero", "atti-ledger",
                           "notai-portraits", "registries", "contact-archive"],
    "card_style":         "atto-area-ledger",
    "button_style":       "serif-archive-border",
    "density":            "airy",
    "tone":               "institutional-notarile",
    "imagery_direction":  "notarile-archivio-istituzionale — codici, ceremonie di firma, biblioteca legale, sigillo pubblico",
    "imagery_key":        "lawyer-notary",
    "conversion_pattern": "primo-incontro-orientamento",
    "font_pairing":       ("Source Serif 4", "Public Sans"),
    "content": { ... see §4.3 ... },
},
```

### 4.1 · Required keys

| Key | Type | Required? | Notes |
|---|---|---|---|
| `archetype` | str | **[BLOCKING]** | literal `"classic-gold"` |
| `hero_style` | str | **[BLOCKING]** | from §2.4 catalog |
| `navbar_style` | str | **[BLOCKING]** | cohesive with hero_style |
| `footer_style` | str | **[BLOCKING]** | cohesive with hero_style |
| `section_order` | list[str] | **[REQUIRED]** | first item `"ink-nav"`, second `"ledger-hero"` |
| `card_style` | str | **[REQUIRED]** | `"<noun>-ledger"` |
| `button_style` | str | **[REQUIRED]** | `"serif-<noun>-border"` |
| `density` | str | **[BLOCKING]** | `"airy"` only |
| `tone` | str | **[REQUIRED]** | suffix `-notarile` or prefix `forensic-`/`institutional-` |
| `imagery_direction` | str | **[REQUIRED]** | one-line editorial brief for imagery-curator |
| `imagery_key` | str | **[BLOCKING]** | dedicated key in `preview_imagery.IMAGERY_CONFIG` |
| `conversion_pattern` | str | **[BLOCKING]** | low-pressure intake (no `book-now`) |
| `font_pairing` | tuple[str, str] | **[REQUIRED]** | (heading, body) Google Font names |
| `content` | dict[str, Any] | **[BLOCKING]** | see §4.3 |
| `preview_archetype` | str | **[STRONG]** | only if you need a different preview-composition file |

### 4.2 · `preview_archetype` — when to set it

Atto sets `preview_archetype: "classic-gold-notary"` because the preview-generator looks up `templates/preview_compositions/lawyer/<preview_archetype>.html`. If your reuse's preview card needs different copy/imagery than Lex's prime, declare a separate composition. If not, omit the key and inherit Lex's `classic-gold` composition.

See `apps/catalog/management/commands/generate_previews.py` for the dispatch logic.

### 4.3 · `content` block — DNA-side copy

The DNA's `content` block holds the **preview-card** copy plus a small subset of fields used by the editor as starter values. It is NOT the full content tree. Required keys (verbatim from Atto · `template_dna.py:523-555`):

| Key | Type | Notes |
|---|---|---|
| `eyebrow` | str | preview hero eyebrow |
| `headline` | str (with `<em>`) | preview hero headline |
| `subhead` | str | preview hero subhead |
| `primary_cta`, `secondary_cta` | str | preview CTA verbs |
| `phone` | str | E.164-ish formatted |
| `monogram` | str (2-3 chars) | crest letters |
| `nav_links` | list[str] (5 items) | preview navbar labels |
| `meta_strip` | list[tuple[str, str]] (3 items) | preview meta-strip rows |
| `hero_credit_left`, `hero_credit_right` | tuple[str, str] | preview credit cells |
| `practice_label`, `practice_heading` | str | preview ledger heading |
| `practice` | list[tuple[str, str, str]] (4 items) | preview practice rows: `(num, title, blurb)` |
| `stats_label` | str | dark band heading |
| `stats` | list[tuple[str, str]] (4 items) | `(num, label)` |
| `publications` | list[str] (5-6 items) | logo-marquee labels |

The full content tree (with all six page-kinds populated) lives in `apps/catalog/template_content_<slug>.py` — see §5.

---

## 5 · Page-data top-level shape

The page-data tree is the **per-locale** dict imported from `template_content_<slug>_<locale>.py`. From `apps/catalog/template_content.py:2695-2700`, Atto's tree is registered as:

```python
"atto-notai-associati": {
    "it": ATTO_CONTENT_IT,
    "en": ATTO_CONTENT_EN,
    "fr": ATTO_CONTENT_FR,
    "es": ATTO_CONTENT_ES,
    "ar": ATTO_CONTENT_AR,
},
```

Each `*_CONTENT_*` dict has the same top-level shape (verbatim from `template_content_atto.py:37-45`):

```python
ATTO_CONTENT_IT: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Studio",        "kind": "home"},
        {"slug": "studio",        "label": "Lo Studio",     "kind": "about"},
        {"slug": "pratiche",      "label": "Aree di Atti",  "kind": "services"},
        {"slug": "avvocati",      "label": "I Notai",       "kind": "team"},
        {"slug": "pubblicazioni", "label": "Pubblicazioni", "kind": "blog_list"},
        {"slug": "contatti",      "label": "Contatti",      "kind": "contact"},
    ],
    "site": { ... },          # chrome (rendered by _base.html)
    "home": { ... },          # rendered by home.html
    "studio": { ... },        # rendered by about.html (kind=about)
    "pratiche": { ... },      # rendered by services.html (kind=services)
    "avvocati": { ... },      # rendered by team.html (kind=team)
    "pubblicazioni": { ... }, # rendered by blog_list.html
    "posts": [ ... ],         # posts list (each post powers blog_detail.html)
    "contatti": { ... },      # rendered by contact.html
}
```

### 5.1 · Top-level keys

| Key | Type | Required? | Read by |
|---|---|---|---|
| `pages` | list[dict] | **[BLOCKING]** | `_base.html:544,569` (nav + footer iterations) |
| `site` | dict | **[BLOCKING]** | `_base.html` (chrome) |
| `home` | dict | **[BLOCKING]** | `home.html` |
| `studio` | dict | **[REQUIRED]** | `about.html` (page slug from `pages[]`) |
| `pratiche` | dict | **[REQUIRED]** | `services.html` |
| `avvocati` | dict | **[REQUIRED]** | `team.html` |
| `pubblicazioni` | dict | **[REQUIRED]** | `blog_list.html` |
| `posts` | list[dict] | **[REQUIRED]** | `blog_detail.html` |
| `contatti` | dict | **[REQUIRED]** | `contact.html` |

The slug names are conventional but NOT enforced — `pages[].slug` is the canonical identifier and the page-data dict is keyed by it. Atto chose `pratiche / avvocati / pubblicazioni` to match Lex's IT slugs verbatim; that **maximizes locale-independence** because the URL pattern is the same across IT/EN/FR/ES/AR. Honesty note: this is a stronger pattern than slug-per-locale and Lex established the precedent.

### 5.2 · `pages[]` shape

Each entry is a dict with three keys (verbatim from `template_content_atto.py:38-45`):

```python
{"slug": "home", "label": "Studio", "kind": "home"}
```

- `slug` — URL segment; matches the page-data dict key (except `home` → the dict key is also `"home"`).
- `label` — navbar/footer link text.
- `kind` — page-kind discriminator (see §12).

**[BLOCKING] `CG-PD-01`** — `pages[].slug` MUST be the same key used in the top-level dict. The view layer does `page_data = content[page.slug]` (semantic — see `apps/catalog/views.py`).

### 5.3 · `site` shape

The chrome data is read by `_base.html`. Verbatim observable keys (from `template_content_atto.py:48-84`):

| Key | Type | Read at | Notes |
|---|---|---|---|
| `logo_initial` | str (2-3 chars) | `_base.html:540` (`.lx-nav .crest`) | crest letters |
| `logo_word` | str | `_base.html:541,564` | brand name |
| `tag` | str | `_base.html:553` (`.lx-nav .phone .tag`) | short eyebrow on nav |
| `phone` | str | `_base.html:554,580` | telephone display |
| `email` | str | `_base.html:581` | inst. email |
| `address` | str | `_base.html:579` | one-line address |
| `hours_compact` | str | `_base.html:582` | one-line hours |
| `hours_footer_rows` | list[str] | `_base.html:583` | additional footer hours rows |
| `license` | str | `_base.html:591` | order/bar registration line |
| `nav_cta` | str | (reserved for nav CTA button when shown) | |
| `footer_intro` | str | `_base.html:565` | paragraph in footer brand column |
| `foot_studio`, `foot_pages`, `foot_contact`, `foot_offices` | str | `_base.html:563,568,578,586` | column headers |
| `offices_footer_rows` | list[str] | `_base.html:587` | footer offices column |
| `case_practice_label`, `case_year_label`, `case_outcome_label`, `case_lead_label` | str | blog_detail / cross-page meta | locale-aware labels |

---

## 6 · Page-data: `home`

The home dict feeds `home.html`. Verbatim shape (anchored to `template_content_atto.py:89-237`):

### 6.1 · Hero block

| Key | Type | Render at |
|---|---|---|
| `eyebrow` | str | `home.html:270` |
| `headline` | str (with `<em>` italic emphasis) | `home.html:271` (uses `\|safe`) |
| `intro` | str | `home.html:272` |
| `primary_cta`, `primary_href` | str (slug ref) | `home.html:274` |
| `secondary_cta`, `secondary_href` | str (slug ref) | `home.html:275` |
| `hero_credit_left` | **tuple[str, str]** | `home.html:278` reads `.0` and `.1` |
| `hero_credit_right` | **tuple[str, str]** | `home.html:279` reads `.0` and `.1` |
| `hero_meta_strip` | **list[tuple[str, str]]** (3 items) | `home.html:287-289` unpacks `for label, value in ...` |

**[BLOCKING] `CG-HOME-01`** — `hero_credit_left`/`hero_credit_right` MUST be 2-tuples, NOT dicts. The skin uses positional indexing (`.0` / `.1`). A dict-shaped credit cell will render `{'tag': 'Direzione', 'value': '...'}` literally on the page. See trap §15.1.

**[BLOCKING] `CG-HOME-02`** — `hero_meta_strip` is exactly 3 items of `(label, value)`. Lex meta_strip is 3 rows; Atto meta_strip is 3 rows. The skin's grid uses a fixed gap, the 4-row case visually breaks the monogram-vs-strip balance.

### 6.2 · Practice-area ledger

| Key | Type | Render at |
|---|---|---|
| `practice_label` | str | `home.html:297` |
| `practice_heading` | str (with `<em>`) | `home.html:298` (`\|safe`) |
| `practice_intro` | str | `home.html:300` |
| `practice` | **list[tuple[str, str, str]]** (exactly 4 items on home) | `home.html:303` unpacks `for num, title, blurb in ...` |

**[BLOCKING] `CG-HOME-03`** — `practice` is a list of 3-tuples `(num, title, blurb)`. NOT a list of dicts. Compare to the `pratiche` page-data (§8) where `services` IS a list of dicts. This is the canonical T47 trap: a builder coming from `specialist` will assume dicts everywhere.

Atto's home practice (verbatim, `template_content_atto.py:125-151`):

```python
"practice": [
    ("01", "Rogiti di compravendita immobiliare", "Redazione del rogito ..."),
    ("02", "Successioni e dichiarazioni",         "Apertura della successione ..."),
    ("03", "Atti societari e operazioni straordinarie", "Costituzione di società ..."),
    ("04", "Mutui ipotecari e garanzie reali",    "Atti di mutuo fondiario ..."),
],
```

### 6.3 · Stats band (dark)

| Key | Type | Render at |
|---|---|---|
| `stats_label` | str | (visual eyebrow above stats heading — convention) |
| `stats_heading` | str | `home.html:316` |
| `stats` | **list[tuple[str, str]]** (exactly 4 items) | `home.html:317` unpacks `for num, label in ...` |

**[BLOCKING] `CG-HOME-04`** — `stats` is exactly 4 items. The skin grids `grid-template-columns: 0.9fr repeat(4, 1fr)` (`home.html:148`). Any other count visually breaks the dark band.

### 6.4 · Partners preview

| Key | Type | Render at |
|---|---|---|
| `partners_label` | str | `home.html:328` |
| `partners_heading` | str | `home.html:329` |
| `partners_intro` | str | `home.html:330` |
| `partners` | **list[dict]** (exactly 3 items) | `home.html:333` iterates and reads `.role`, `.name`, `.foro`, `.bio` |

Partner dict required keys: `name`, `role`, `foro`, `bio`. See verbatim shape at `template_content_atto.py:172-210`. Note the partner dict's `foro` key is overloaded: Atto uses it for "Distretto Notarile di Milano · iscritta al ruolo dal 2007" (notary district + role enrollment); Lex uses it for "Foro di Roma dal 1986 · Cassazionista dal 1999" (bar + cassation). The key name stays `foro` for skin-parity.

**[BLOCKING] `CG-HOME-05`** — `partners` is exactly 3 dicts. The skin grids `grid-template-columns: repeat(3, 1fr)` (`home.html:182`).

### 6.5 · Publications ribbon

| Key | Type | Render at |
|---|---|---|
| `publications_label` | str | `home.html:346` |
| `publications` | **list[str]** (5-7 items) | `home.html:348,352,353` (logo-marquee repeated 3×) |

Publications are uppercase logo-style strings (institutional journals, not full URLs). Verbatim from Atto (`template_content_atto.py:214-221`):

```python
"publications": [
    "NOTARIATO", "RIVISTA DEL NOTARIATO", "GUIDA AL DIRITTO",
    "CNN NOTIZIE", "RIVISTA TRIMESTRALE DI DIRITTO E PROCEDURA",
    "FEDERNOTAI",
],
```

### 6.6 · Final CTA band

| Key | Type | Render at |
|---|---|---|
| `cta_label`, `cta_heading`, `cta_intro` | str | `home.html:362-364` |
| `cta_primary`, `cta_primary_href` | str | `home.html:367` |
| `cta_secondary`, `cta_secondary_href` | str | `home.html:368` |

---

## 7 · Page-data: `studio` (about)

The studio dict feeds `about.html`. Verbatim shape (anchored to `template_content_atto.py:242-359`):

### 7.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `about.html:103-105` |

### 7.2 · History timeline

| Key | Type | Render at |
|---|---|---|
| `history_label`, `history_heading`, `history_intro` | str | `about.html:112,113,115` |
| `history` | **list[tuple[str, str, str]]** (5-6 items) | `about.html:118` unpacks `for year, title, body in ...` |

**[BLOCKING] `CG-ABOUT-01`** — `history` is 3-tuples `(year, headline, body)`. NOT dicts with `date`/`title`/`text` keys.

Verbatim from Atto (`template_content_atto.py:263-299`):

```python
"history": [
    ("2007", "Iscrizione al ruolo del notaio fondatore",
     "La Notaio dott.ssa Maria Beatrice Conti viene iscritta al ruolo ..."),
    ("2011", "Atti pubblici trilingui",
     "Lo studio inizia a ricevere atti pubblici redatti in italiano ..."),
    ("2014", "Ingresso del Notaio Andrea Sironi",
     "Il Notaio dott. Andrea Sironi, già praticante di lungo corso ..."),
    # ... 3 more
],
```

### 7.3 · Values (method)

| Key | Type | Render at |
|---|---|---|
| `values_label`, `values_heading` (with `<em>`), `values_intro` | str | `about.html:133-135` |
| `values` | **list[tuple[str, str, str]]** (exactly 4 items) | `about.html:138` unpacks `for num, title, body in ...` |

**[BLOCKING] `CG-ABOUT-02`** — `values` is exactly 4 3-tuples `(num, title, body)`. Both Lex and Atto stake out four principles ("Quattro principi non negoziabili" · "Quattro principi non negoziabili"). The skin's grid is two-column 2×2.

### 7.4 · Coordinates

| Key | Type | Render at |
|---|---|---|
| `coordinates_label` | str | `about.html:151` |
| `coordinates` | **list[tuple[str, str]]** (1-3 items) | `about.html:153` unpacks `for city, addr in ...` |

**[BLOCKING] `CG-ABOUT-03`** — `coordinates` is 2-tuples `(label, value)`. Atto has 2 entries (one sede + the Distretto Notarile); Lex has 2 entries (Roma sede + Milano sede). Either pattern is acceptable.

Verbatim from Atto (`template_content_atto.py:343-347`):

```python
"coordinates": [
    ("Milano · sede",      "Via Manin 12 · 20121 · Porta Nuova"),
    ("Distretto Notarile", "Milano · Consiglio Notarile dei Distretti Riuniti"),
],
```

### 7.5 · CTA

| Key | Type | Render at |
|---|---|---|
| `cta_heading`, `cta_intro` | str | `about.html:165-166` |
| `cta_primary`, `cta_primary_href` | str | `about.html:169` |

Note: studio has a single CTA (no secondary). Home has both primary + secondary.

---

## 8 · Page-data: `pratiche` (services)

The pratiche dict feeds `services.html`. Verbatim shape (anchored to `template_content_atto.py:364-558`):

### 8.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `services.html:91-93` |

### 8.2 · Services list

| Key | Type | Render at |
|---|---|---|
| `svc_lead_label` | str | `services.html:110` |
| `svc_jurisdiction_label` | str | `services.html:111` |
| `services` | **list[dict]** (5-12 items) | `services.html:99-111` |

Each service dict has these required keys (verbatim from Atto · `template_content_atto.py:381-516`):

| Service key | Type | Required? | Used at |
|---|---|---|---|
| `num` | str (e.g. "01") | **[BLOCKING]** | `services.html:102` (`{{ svc.num }} / {{ page_data.services\|length }}`) |
| `title` | str | **[BLOCKING]** | service card title |
| `blurb` | str | **[BLOCKING]** | service card body |
| `scope` | list[str] (3-5 items) | **[REQUIRED]** | bulleted detail list |
| `lead` | str | **[REQUIRED]** | `services.html:110` partner-responsible name |
| `jurisdiction` | str | **[REQUIRED]** | `services.html:111` registry / court / district |

**[BLOCKING] `CG-SVC-01`** — `services` is a list of dicts (NOT 3-tuples). This is the **inverse** of the home `practice` shape: home's `practice` is 3-tuples, services-page `services` is dicts. The skin needs the richer per-service surface (scope + lead + jurisdiction) only on the dedicated page.

**[BLOCKING] `CG-SVC-02`** — Service dict shape MUST be `{num, title, blurb, scope, lead, jurisdiction}` — NOT the `specialist`-style `{procedure, duration, price}`. A `classic-gold` service is procedural-institutional (responsible partner + competent district), not transactional (price + duration). See trap §15.2.

Compressed example (see `apps/catalog/template_content_atto.py:381-400` for the full block):

```python
"services": [
    {
        "num":   "01",
        "title": "Rogiti di compravendita immobiliare",
        "blurb": "Redazione del rogito notarile ...",
        "scope": [
            "Visura catastale e ispezione ipotecaria",
            "Verifica della regolarità urbanistica e APE",
            "Preliminare di compravendita registrato",
            "Rogito pubblico letto al comparente",
        ],
        "lead":          "Notaio dott. Stefano Verri",
        "jurisdiction":  "Milano · Distretto Notarile",
    },
    # ... 6 more
],
```

### 8.3 · Process strip

| Key | Type | Render at |
|---|---|---|
| `process_label`, `process_heading` | str | `services.html:121-122` |
| `process` | **list[tuple[str, str, str]]** (exactly 4 items) | `services.html:125` unpacks `for num, title, desc in ...` |

**[BLOCKING] `CG-SVC-03`** — `process` is 3-tuples (not dicts). Four steps each.

### 8.4 · CTA

| Key | Type | Render at |
|---|---|---|
| `cta_heading`, `cta_intro` | str | `services.html:137-138` |
| `cta_primary`, `cta_primary_href` | str | `services.html:140` |

---

## 9 · Page-data: `avvocati` (team)

The avvocati dict feeds `team.html`. Verbatim shape (anchored to `template_content_atto.py:563-639` and `template_content_lex.py:644-…`):

### 9.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `team.html:86-88` |

### 9.2 · Lawyers list

| Key | Type | Render at |
|---|---|---|
| `lawyer_foro_label` | str | `team.html:109` |
| `lawyer_year_label` | str | `team.html:110` |
| `lawyer_specialization_label` | str | `team.html:108` |
| `lawyers` | **list[dict]** (3-14 items) | `team.html:93-110` |

Each lawyer dict has these required keys (verbatim from Atto · `template_content_atto.py:581-638`):

| Lawyer key | Type | Required? | Used at |
|---|---|---|---|
| `name` | str | **[BLOCKING]** | card heading |
| `role` | str | **[BLOCKING]** | card eyebrow |
| `specialization` | str | **[REQUIRED]** | `team.html:108` |
| `foro` | str | **[REQUIRED]** | `team.html:109` |
| `year` | str | **[REQUIRED]** | `team.html:110` |
| `bio` | str | **[REQUIRED]** | card body paragraph |

**[BLOCKING] `CG-TEAM-01`** — lawyer dict keys are `{name, role, specialization, foro, year, bio}`. NOT `{name, title, area, court, since, description}`. The skin reads `lawyer.specialization`, `lawyer.foro`, `lawyer.year` verbatim.

Honesty divergence: the `home.partners[]` shape uses `{name, role, foro, bio}` (4 keys); the `avvocati.lawyers[]` shape uses `{name, role, specialization, foro, year, bio}` (6 keys). The `home.partners[]` is a preview of the team page and intentionally lighter — DO NOT collapse them. Lex's home `partners` is 3 items (sample of 14 lawyers); Atto's home `partners` is 3 items (=all 3 notai). The 3-cap on home is grid-driven (§6.4).

Compressed lawyer example (see `apps/catalog/template_content_atto.py:582-601`):

```python
{
    "name":           "Notaio dott.ssa Maria Beatrice Conti",
    "role":           "Notaio fondatore dello studio",
    "specialization": "Atti societari · M&A · donazioni · procure trilingui",
    "foro":           "Distretto Notarile di Milano",
    "year":           "Iscritta al ruolo dal 2007",
    "bio":            "Fondatrice dello Studio Notarile Conti–Sironi–Verri ...",
},
```

---

## 10 · Page-data: `pubblicazioni` (publications · blog_list)

The pubblicazioni dict feeds `blog_list.html`. Verbatim shape (anchored to `template_content_atto.py:644-673`):

### 10.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `blog_list.html:107-109` |
| `lead_image` | str (URL) | `blog_list.html:116` (background-image on lead post) |
| `footer_strap` | str | (footer bottom strap) |
| `empty_body_fallback_paragraphs` | list[str] | `blog_detail.html` fallback when post body is empty |

### 10.2 · `posts` (top-level, NOT under `pubblicazioni`)

The post list lives at the **top level** of the content tree (alongside `home`, `studio`, etc.), NOT nested under `pubblicazioni`. This is a deliberate architecture: each post is reachable at `/pubblicazioni/<slug>/` and the view layer needs to scan `content["posts"]` independent of the `pubblicazioni` page.

Each post dict required keys (verbatim from `template_content_atto.py:676-896`):

| Post key | Type | Notes |
|---|---|---|
| `slug` | str | URL segment |
| `kicker` | str | category eyebrow on detail page |
| `title` | str | full post title |
| `date` | str (e.g. "Aprile 2026") | locale-aware human date |
| `read_min` | str (numeric · "7", "10") | reading-time minutes |
| `author` | str | notary/lawyer name |
| `lede` | str | summary paragraph |
| `body` | list[tuple[str, str]] | rich-body cells; each `(kind, text)` |

The `body` 2-tuple kinds observed in Atto: `"p"`, `"h2"`, `"blockquote"`. The skin renders each kind to a matching tag (see `blog_detail.html`).

**[REQUIRED] `CG-PUB-01`** — `posts` count is 4-6. Fewer than 4 reads thin; more than 6 dilutes the editorial calendar feel.

**[BLOCKING] `CG-PUB-02`** — `posts` is at the **top level** of the content tree, not nested. Compare `template_content.py:2696-2700` — the per-locale dict imports already include `posts`.

---

## 11 · Page-data: `contatti` (contact)

The contatti dict feeds `contact.html`. Verbatim shape (anchored to `template_content_atto.py:902-1084`):

### 11.1 · Page header

| Key | Type | Render at |
|---|---|---|
| `eyebrow`, `headline` (with `<em>`), `intro` | str | `contact.html:93-95` |

### 11.2 · Form

The form is highly structured. Required keys:

| Key | Type | Render at |
|---|---|---|
| `form_label`, `form_heading`, `form_intro` | str | `contact.html:101-103` |
| `form_sections` | list[dict] (2-5 sections) | `contact.html:107` |
| `form_fields` | list[dict] | `contact.html:115,136,159` |
| `upload_field` | dict | `contact.html:115,116` |
| `form_consent` | str | `contact.html:182` |
| `form_submit_label`, `form_submit_note` | str | `contact.html:188,194` |

Each `form_sections[]` dict: `{num: str, title: str, meta: str, fields: list[str]}` where `fields` is a list of field-name strings (and the literal sentinel `"__upload__"` to slot the upload field).

Each `form_fields[]` dict: `{name, label, type, required, ...}` plus optional `placeholder`, `helper`, `options` (for selects), `full_width` (bool).

The `upload_field` dict: `{name, label, helper, accept, multiple, primary, link, meta}`.

See `template_content_atto.py:924-1025` for the full canonical example with 9 fields + 1 upload + 4 sections.

### 11.3 · Offices

| Key | Type | Render at |
|---|---|---|
| `offices_label` | str | `contact.html:203` |
| `offices` | **list[dict]** (1-3 items) | `contact.html:204` |
| `office_address_label`, `office_area_label`, `office_phone_label`, `office_email_label`, `office_hours_label` | str | `contact.html:209-213` |

Each office dict: `{city, tag, address, area, phone, email, hours}`.

### 11.4 · Channels

| Key | Type | Render at |
|---|---|---|
| `channels_label` | str | `contact.html:220` |
| `channels` | **list[tuple[str, str, str]]** (2-4 items) | `contact.html:222` unpacks `for name, value, meta in ...` |

**[BLOCKING] `CG-CONTACT-01`** — `channels` is 3-tuples `(name, value, meta)`, NOT dicts.

### 11.5 · Footnote

| Key | Type | Render at |
|---|---|---|
| `footnote` | str | `contact.html:233` |

---

## 12 · `page_kind` mapping

The skin selection is **page-kind driven**, not page-slug driven. The view layer maps the slug to a kind via `pages[].kind`, then looks up the rendering template.

Observed mapping (from `template_content_atto.py:38-45` and the skin folder):

| Slug (Atto) | Slug (Lex) | `kind` | Template file |
|---|---|---|---|
| `home` | `home` | `home` | `lawyer/classic-gold/home.html` |
| `studio` | `studio` | `about` | `lawyer/classic-gold/about.html` |
| `pratiche` | `pratiche` | `services` | `lawyer/classic-gold/services.html` |
| `avvocati` | `avvocati` | `team` | `lawyer/classic-gold/team.html` |
| `pubblicazioni` | `notabili` | `blog_list` | `lawyer/classic-gold/blog_list.html` |
| (each `posts[].slug`) | (each `posts[].slug`) | `blog_detail` | `lawyer/classic-gold/blog_detail.html` |
| `contatti` | `contatti` | `contact` | `lawyer/classic-gold/contact.html` |

**[REQUIRED] `CG-KIND-01`** — `kind` values are exactly the 7 listed (`home`, `about`, `services`, `team`, `blog_list`, `blog_detail`, `contact`). Other kinds (`menu`, `gallery`, `reservations`) belong to restaurant / portfolio archetypes; using them on `classic-gold` will fail the template lookup.

Note the slug divergence: Lex calls the blog page `notabili` (cause notabili / "notable cases"), Atto calls it `pubblicazioni` (publications). Both have `kind: "blog_list"`. The slug serves the brand voice; the `kind` serves the rendering. **[STRONG] `CG-KIND-02`** — new reuses SHOULD pick a slug that reads natural in IT first, then carry to EN/FR/ES/AR via the locale-independent shape (§5.1 honesty note).

---

## 13 · Voice anchor pattern

The voice anchor is a noun-em phrase that the brand repeats across surfaces. It is the brand's compact memory: render it in the hero headline, in the studio-page headline, in at least one services-page surface, and in the contact-page eyebrow. Each new reuse MUST pick a third **distinct** anchor.

### 13.1 · Existing anchors

| Instance | Anchor (IT) | EN | FR | ES | AR | Surfaces |
|---|---|---|---|---|---|---|
| Lex | `riservatezza` | confidentiality | confidentialité | reserva | (per Lex AR file) | hero · CTA copy · contact eyebrow |
| Atto | `atto pubblico` | public deed | acte authentique | escritura pública | الوثيقة الرسمية | hero · studio headline · pratiche heading · contact eyebrow (8+ surfaces, see registry tier_reason §926) |

### 13.2 · Verbatim-in-translation rule

The translator-agent MUST preserve the chosen anchor verbatim across all 5 locales — not transliterated, not literally calqued, but **identified to its register equivalent**:

- EN: institutional newspaper of record register (FT Law · NYT Wellness).
- FR: `vous` register equivalent of the EN target (Les Echos · Conseil Supérieur du Notariat).
- ES: peninsular `usted` register (El País Sociedad).
- AR: MSA premium register (Asharq al-Awsat) with Latin proper names preserved via `unicode-bidi: isolate` + Latin digits per the classic-gold-AR house style.

See `TEMPLATE_REGISTRY.json:926` for Atto's verbatim-in-translation accounting (T48 tier_reason) — this is the canonical pattern.

**[BLOCKING] `CG-VOICE-01`** — Translator may not "improve" the anchor's locale variant. The anchor is THE name. Once `riservatezza` is set, the EN counterpart is `confidentiality` everywhere it appears, not `discretion`/`privacy`/`reserve` ad-hoc.

**[BLOCKING] `CG-VOICE-02`** — A new reuse's anchor MUST be distinct from `riservatezza` and `atto pubblico` at the semantic level (not just lexically). `discrezione` is too close to `riservatezza`. Candidates: `mandato` · `patrocinio` · `successione` · `pubblica fede` (already taken in Atto's surrounding copy) · `passaggio generazionale` (family-office direction).

---

## 14 · Distinctness scoreboard (D-054)

A new reuse MUST diverge from every prior reuse on at least 8 of the 12 axes. The Lex vs Atto column is pre-filled.

| # | Axis | Lex | Atto | New reuse — propose |
|---:|---|---|---|---|
| 1 | Brand archetype | 1-founder boutique | 3-notary association | |
| 2 | Accent polarity | `#C5A55A` ledger-gold | `#1F3A5F` notarial-archive ink-blue | (third polarity · §2.2) |
| 3 | Font pairing | Cormorant Garamond + Inter | Source Serif 4 + Public Sans | (third pairing) |
| 4 | Voice anchor | `riservatezza` | `atto pubblico` | (third anchor · §13.2) |
| 5 | Conversion CTA | private-consultation (paid retainer) | primo-incontro-orientamento (free intake) | (third low-pressure pattern) |
| 6 | Founder type | Avv. Prof. Ferri (academic singolo) | 3 notai associati (collegiate pubblici ufficiali) | (third profile) |
| 7 | Geography | Roma + Milano dual-foro | Milano singolo Distretto | (different region OR different scope) |
| 8 | Imagery direction | legal-heritage-ink (libri · gavel · ritratti senior) | notarile-archivio-istituzionale (codici · ceremonie firma · biblioteca · sigillo) | (third imagery key in `IMAGERY_CONFIG`) |
| 9 | Service catalog | 12 pratiche · societario/famiglia/lavoro/penale | 7 atti · rogiti/testamenti/società/mutui | (different catalog · 5-12 items) |
| 10 | Proof surface | firm KPIs (62 anni · 14 avvocati · 2.400+ cause · 96% favorevole) | institutional credentials (Distretto Notarile · iscrizione al ruolo 2007/2014/2021) | (third proof surface) |
| 11 | CTA verb | "Richiedi una consulenza riservata" | "Richiedi un primo incontro" | (third verb) |
| 12 | Sub-page slug for blog kind | `notabili` (cause notabili) | `pubblicazioni` | (third slug, conceptually distinct) |

**[BLOCKING] `CG-D-03`** — Score ≥ 8/12 vs every prior reuse, with at least one of {axis 2, axis 4, axis 8} divergent. Same accent OR same anchor OR same imagery direction = the templates collapse into recolors of each other.

The scorecard is the same one that earned Atto its T48 approval (`TEMPLATE_REGISTRY.json:921` — "D-054 axes scoreboard ≥ 8 vs Lex confirmed: 11 axes diverse").

---

## 15 · Trap catalog

Seven defects observed during T47 (Atto build) and T48 (Atto multilingual + public flip). Each defect describes itself · its symptom · its root cause · its prevention.

### 15.1 · Page-data shape mismatch (3-tuple vs dict)

- **What**: builder wrote `practice` as `list[dict]` (specialist-style) instead of `list[tuple[str, str, str]]`.
- **Symptom**: home renders `{'num': '01', 'title': '...', 'blurb': '...'}` literally in the practice ledger; the iterator `for num, title, blurb in page_data.practice` raises `ValueError: too many values to unpack`.
- **Root cause**: builder came from the `specialist` archetype and assumed dict shape everywhere.
- **Prevention**: §6.2 / §7.2 / §7.3 / §8.3 in this document. CLI does NOT catch this — Django's template rendering is silent on tuple-unpacking failures inside `{% for %}`.

### 15.2 · Service dict shape from `specialist`

- **What**: builder copy-pasted the `specialist` service shape `{procedure, duration, price}`.
- **Symptom**: services page renders empty `lead` / `jurisdiction` rows.
- **Root cause**: assumption that `services` is locale-independent across archetypes. It is NOT — see §8.2.
- **Prevention**: §8.2's CG-SVC-02 BLOCKER. Read this file before writing the content tree.

### 15.3 · `live_pages` list mistakes

- **What**: registry `live_pages` lists the page kinds (`["home", "about", ...]`) instead of the slugs (`["home", "studio", "pratiche", "avvocati", "pubblicazioni", "contatti"]`).
- **Symptom**: 404 on every non-home route because the URL resolver looks up by slug.
- **Root cause**: confusion between `pages[].slug` (URL) and `pages[].kind` (template selector).
- **Prevention**: registry pre-flight in §16 step 1. The canonical Atto list is at `TEMPLATE_REGISTRY.json:904-911`.

### 15.4 · RTL Latin-bidi isolation for proper names + Latin digits

- **What**: AR locale renders `الوثيقة الرسمية Conti-Sironi-Verri 2007` with `Conti-Sironi-Verri` flipped or with `2007` flipped.
- **Symptom**: visual breakage on AR routes; an Arabic-reading visitor sees junk.
- **Root cause**: AR translator did not wrap Latin proper names with `<bdi>` / did not use the `unicode-bidi: isolate` house style.
- **Prevention**: §13.2's verbatim-in-translation rule + the Atto T48 precedent (`TEMPLATE_REGISTRY.json:926` — "Latin proper names preserved via unicode-bidi isolate, Latin digits per the classic-gold-AR house style precedent established by Lex").

### 15.5 · Hero plate hardcoded URL pattern

- **What**: builder hardcoded `_NOTARY_HERO = "https://images.pexels.com/photos/.../"` directly in the content tree.
- **Symptom**: works; but the imagery-curator can't re-curate without editing the content file, and the imagery-pack scanner (`scripts/check_imagery_pack.py`) can't validate.
- **Root cause**: shortcut.
- **Prevention**: declare imagery in `IMAGERY_CONFIG` and reference by key; only inline a URL if the imagery has no equivalent pool. See `apps/catalog/template_content_atto.py:28-34` for the actual current pattern (module-level constants — acceptable for a per-template story but not for a shared cluster).

### 15.6 · Tier flip cascading test assertions

- **What**: flipping `tier: draft → published_live` cascades into `apps.catalog.tests` because tests count `published_live` templates per cluster/feature/price-tier.
- **Symptom**: test failure like `AssertionError: expected 25, got 26 for has_rtl feature count`.
- **Root cause**: tier-aware aggregation in catalog tests.
- **Prevention**: every public flip must run `python manage.py test apps.catalog` and update the count assertions in the same PR. T48 was a precedent: see `TEMPLATE_REGISTRY.json:926` — "CATALOG count 26 → 27 · classic-gold cluster facet 1 → 1 · has_rtl features 26 → 27 · premium price-tier count bumped accordingly".

### 15.7 · Skin literal strings leaking past D-047

- **What**: skin templates contain literal strings like "Distretto Notarile di Milano" or "Conti" hardcoded.
- **Symptom**: every reuse inherits the literal; new reuses ship with another brand's surname on the page.
- **Root cause**: D-047 violation; chrome-authoring contract bypassed.
- **Prevention**: the Atto docstring at `apps/catalog/template_content_atto.py:1088-1096` codifies the rule — "Every visible string in the lawyer/classic-gold skin templates must come from THIS file (or from chrome.* / dna.content.*). Zero literal 'Conti', 'Sironi', 'Verri', '2007', 'Milano', 'via Manin', notai names, headline text, or other brand-specific strings in the .html files."

---

## 16 · Validation checklist (BLOCKING gate)

The next `classic-gold` reuse MUST pass every check below in sequence. A reviewer may not skip a step. A failure at any step blocks `published_live` flip and (for steps 1-3) blocks even the draft-landing merge.

### 16.1 · Pre-build (registry + DNA + seed + cluster)

- [ ] **Registry entry exists** in `TEMPLATE_REGISTRY.json` with the 17 required keys: `slug`, `name`, `category`, `brand_name`, `tagline`, `palette` (primary/secondary/accent), `typography`, `personality`, `archetype: "classic-gold"`, `hero_style`, `navbar_style`, `density: "airy"`, `tone`, `conversion_pattern`, `live_preview: true`, `live_pages`, `locales`, `rtl: true`, `archetype_reuse: true`, `reuse_notes`, `price`, `featured`, `status`, `tier: "draft"`, `tier_reason`.
- [ ] **`live_pages`** lists slugs (NOT kinds). Use Atto's list as the template (`["home", "studio", "pratiche", "avvocati", "pubblicazioni", "contatti"]`). Trap §15.3.
- [ ] **`archetype_reuse: true`** + `reuse_notes` written. The reuse_notes MUST enumerate the 11+ D-054 axes (§14) versus every prior reuse and assert score ≥ 8.
- [ ] **DNA entry exists** in `apps/catalog/template_dna.py` with the 14 required keys (§4.1). Verify `archetype: "classic-gold"`, `density: "airy"`, `imagery_key` is a NEW dedicated key in `IMAGERY_CONFIG`.
- [ ] **`IMAGERY_CONFIG`** has a new dedicated `imagery_key` with 4-8 curated Pexels URLs from the appropriate X.3 pack (notary-commercialista / labor-law / family-office / …). Zero overlap with `lawyer-classic` or `lawyer-notary` pools.
- [ ] **Brand registered** in `apps/catalog/brand_registry` (the seed migration path used by `manage.py seed_brands`). Honesty: this is enforced by existing tests; if you skip it the test suite fails immediately, which is the correct outcome.
- [ ] **Cluster facet** updated in catalog tests if a new cluster is introduced.

### 16.2 · Build (content tree shape-parity)

- [ ] **`template_content_<slug>.py`** created in `apps/catalog/`. Module docstring includes the D-054 axes diff against EACH prior reuse, not just one.
- [ ] **Top-level shape** matches §5.1 exactly: `pages`, `site`, `home`, `studio`, `pratiche`, `avvocati`, `pubblicazioni`, `posts`, `contatti`. Optional keys allowed at top level; the 9 listed are MANDATORY.
- [ ] **`home`** dict has all keys from §6, with `practice` as 3-tuples, `stats` as 4 2-tuples, `partners` as 3 dicts, `hero_credit_*` as 2-tuples, `hero_meta_strip` as 3 2-tuples. Trap §15.1.
- [ ] **`studio`** dict has all keys from §7, with `history` as 5-6 3-tuples, `values` as 4 3-tuples, `coordinates` as 2-tuples.
- [ ] **`pratiche`** dict has `services` as 5-12 dicts with shape `{num, title, blurb, scope, lead, jurisdiction}`. Trap §15.2.
- [ ] **`avvocati`** dict has `lawyers` as 3-14 dicts with shape `{name, role, specialization, foro, year, bio}`.
- [ ] **`pubblicazioni`** dict has the page header + `lead_image` + fallbacks; `posts` is at top level (NOT nested). Trap §15.6.
- [ ] **`contatti`** dict has the form structure (`form_sections`, `form_fields`, `upload_field`), `offices` list of dicts, `channels` as 3-tuples, `footnote`. Trap §15.7 reminder.
- [ ] **`apps/catalog/template_content.py`** imports the new `*_CONTENT_IT` module and registers it in `LIVE_CONTENT` dict.
- [ ] **`manage.py check`** + **`manage.py test apps.catalog`** green.
- [ ] **`manage.py generate_previews --only <slug>`** produces a preview without raising.

### 16.3 · Multilingual (sub-agent translator pattern)

- [ ] **4 sub-agent translators** dispatched in parallel for EN/FR/ES/AR. Each translator receives the full IT module + the voice-anchor preservation directive (§13.2) + the `corporate-suite-design-standard.md` register guidance.
- [ ] **Voice anchor preserved verbatim-in-translation** across all 5 locales. Anchor surfaces counted (≥ 8 per locale) — see `TEMPLATE_REGISTRY.json:926` Atto baseline (8 EN · 16 FR · 20 ES · 13 AR).
- [ ] **`template_content_<slug>_en.py`**, `_fr.py`, `_es.py`, `_ar.py` all created at shape-parity with IT (same top-level keys, same list lengths, same tuple positions). Total ≈ 4 × ~1,100 lines.
- [ ] **Imports added** to `template_content.py` (`from apps.catalog.template_content_<slug>_<locale> import ..._CONTENT_<LOCALE>`).
- [ ] **AR-specific**: Latin proper names preserved via `unicode-bidi: isolate`, Latin digits per the classic-gold-AR house style. Trap §15.4.
- [ ] **Staff `?preview=1` walk green**: 5 locales × N page-kinds = 30+ routes return 200. Use `scripts/walk_preview.py` (or the equivalent) and attach the verdict.

### 16.4 · Public flip (test cascade + anonymous walk + regression)

- [ ] **Tier flipped** in registry from `draft` to `published_live` via `manage.py sync_template_tiers` (NOT by hand-edit alone — the sync command is the contract).
- [ ] **Tier reason updated** to a single multi-fact paragraph that records: build pass-N · multilingual workflow · contrast walk verdict · anonymous walk verdict · cluster count delta · feature count delta · price-tier count delta. Use Atto's tier_reason as the template (`TEMPLATE_REGISTRY.json:926`).
- [ ] **`manage.py test apps.catalog`** green AFTER the flip — the catalog count assertions must be updated in the same PR. Trap §15.6.
- [ ] **Anonymous public walk** green: hit every `live_pages[]` route at every `locales[]` value (≥ N×5 routes), unauthenticated, in a fresh browser session. Verify the `?preview=1` query-string is NOT required.
- [ ] **AAA contrast walk** on ≥ 8 surfaces at 1440×900 + mobile (390×844). Document the pass/fail per surface in the T-report. Acceptable AA-but-not-AAA failures (e.g. ghost-button by-design muting at 4.56:1) must be explicitly noted as such, not silently passed. See `TEMPLATE_REGISTRY.json:926` for Atto's 9/11-PASS precedent + the 2 honest findings.
- [ ] **Regression on previously-flipped `classic-gold` instances** (Lex + Atto): unchanged. Walk a sample of routes for each to confirm no rendering regression from the shared skin.

### 16.5 · Sign-off

- [ ] **release-gatekeeper** signs off after reviewing §16.1-§16.4. The gatekeeper has unconditional authority to send the PR back at any point.
- [ ] **T-report** authored under `factory/reports/<wave>/<pass>-<slug>.md` with: build summary · multilingual summary · contrast walk · anonymous walk · D-054 scoreboard · cluster/feature/tier deltas · open follow-ups.
- [ ] **CLAUDE.md / SESSION_LOG.md / DECISIONS.md** updated per the project's coordination conventions.

The checklist is the gate. Every item is BLOCKING-grade for `published_live`. Most items are also BLOCKING-grade for merge (§16.1 + §16.2). Skip nothing.

---

## Appendix · canonical citations

For convenience, the canonical files cited by this contract:

- `apps/catalog/template_dna.py:75` — `classic-gold` archetype docstring.
- `apps/catalog/template_dna.py:508-556` — Atto DNA entry (canonical example for §4).
- `apps/catalog/template_dna.py:558-605` — Lex DNA entry.
- `apps/catalog/template_content_atto.py:37-1085` — Atto content tree (canonical example for §5-§11).
- `apps/catalog/template_content_atto.py:1088-1096` — D-047 chrome-authoring contract (cited by trap §15.7).
- `apps/catalog/template_content_lex.py:52-…` — Lex content tree.
- `apps/catalog/template_content.py:2695-2700` — Atto LIVE_CONTENT registration.
- `apps/catalog/template_content.py:2887-2891` — Lex LIVE_CONTENT registration.
- `templates/live_templates/lawyer/classic-gold/_base.html` — chrome (601 lines).
- `templates/live_templates/lawyer/classic-gold/home.html` — home renderer (372 lines).
- `templates/live_templates/lawyer/classic-gold/about.html` — about/studio renderer (172 lines).
- `templates/live_templates/lawyer/classic-gold/services.html` — services/pratiche renderer (143 lines).
- `templates/live_templates/lawyer/classic-gold/team.html` — team/avvocati renderer (117 lines).
- `templates/live_templates/lawyer/classic-gold/contact.html` — contact/contatti renderer (237 lines).
- `templates/live_templates/lawyer/classic-gold/blog_list.html` — pubblicazioni renderer (145 lines).
- `templates/live_templates/lawyer/classic-gold/blog_detail.html` — single-post renderer (131 lines).
- `TEMPLATE_REGISTRY.json:847-864` — Lex registry entry.
- `TEMPLATE_REGISTRY.json:885-927` — Atto registry entry (canonical example for §16.1 + §16.4 tier_reason patterns).
- `factory/standards/corporate-suite-blocking-rules.md` — sibling standard, source of the four-tag severity model.

— End of contract.
