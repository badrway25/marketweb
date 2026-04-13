# Editor Schema Blueprint (Session 30 — 2026-04-13)

Blueprint concreto per la futura personalizzazione cliente dei template
marketweb. **Questo documento non implementa l'editor**: specifica la forma
dello schema e i vincoli di edit, così che quando il worktree `editor/`
verrà acceso sia chiaro quali campi sono editabili, con quali tipi, con
quali varianti, e quali invarianti devono essere preservati.

Source of truth: `apps/catalog/template_content.py`, `apps/catalog/template_dna.py`,
`apps/catalog/template_i18n.py`. Gli skin folder `templates/live_templates/<cat>/<arch>/`
sono gli executor del blueprint.

Il modello di lettura è:
`CustomerProject` → `ProjectContent` → (per regione) snapshot del ramo del
content registry che il customer ha modificato, più un overlay di design tokens
(palette, fonts, densità, icon pack) che sovrascrivono `TemplateBrand`.

---

## 1. Component registry — elenco delle regioni editabili per archetipo

Un componente è l'unità di personalizzazione minima: ha un `kind` (tipo di
regione), una `key` (dove sta nel content registry), un insieme di `fields`
tipizzati, un elenco di `variants` a cui il customer può passare, e un set
di `constraints` (soft/hard) che l'editor deve far rispettare.

### 1.1 `nav` — Navbar

| Field                  | Type          | Edit? | Constraints                        | RTL-aware |
|------------------------|---------------|-------|------------------------------------|-----------|
| `logo.image`           | `image`       | ✓     | optional, max 200KB, PNG/SVG/WebP  | —         |
| `logo.wordmark`        | `text`        | ✓     | max 32 chars, single line          | ✓         |
| `logo.initial`         | `text`        | ✓     | exactly 1 char (crest)             | ✓         |
| `alignment`            | `select`      | ✓     | `left` / `center` / `right`        | auto-flip |
| `variant`              | `select`      | ✗     | DNA-locked to `navbar_style`       | —         |
| `items[]`              | `list<link>`  | ✓     | 3–8 items, reorderable             | ✓         |
| `items[].label`        | `text`        | ✓     | max 24 chars                       | ✓         |
| `items[].page_ref`     | `page_ref`    | ✓     | must resolve to existing page      | —         |
| `items[].visible`      | `toggle`      | ✓     | —                                  | —         |
| `cta.enabled`          | `toggle`      | ✓     | —                                  | —         |
| `cta.label`            | `text`        | ✓     | max 24 chars                       | ✓         |
| `cta.page_ref`         | `page_ref`    | ✓     | —                                  | —         |
| `search.enabled`       | `toggle`      | ✓     | —                                  | —         |
| `background.mode`      | `select`      | ✓     | `solid` / `transparent` / `blur`   | —         |
| `background.color`     | `color_token` | ✓     | picker scoped to brand palette     | —         |
| `density`              | `select`      | ✓     | `compact` / `default` / `spacious` | —         |

**Variant locks (DNA):** il `navbar_style` (solid-phone / pill-floating /
minimal-serif / serif-centered / warm-bar / bold-pill / index-rule /
fullbleed-dark) è proprietà DNA e **non è editabile**. Cambia solo se il
customer passa all'archetipo gemello (Option A split) — è una scelta
architetturale, non un tuning.

**Invariante cross-field:** se `logo.image` è vuoto, il fallback è
`logo.initial + logo.wordmark` (già implementato in `_base.html`).

---

### 1.2 `hero` — Hero section

| Field                  | Type              | Edit? | Constraints                              | RTL-aware |
|------------------------|-------------------|-------|------------------------------------------|-----------|
| `variant`              | `select`          | ✓     | Scoped to DNA `hero_style` family         | —         |
| `media.type`           | `select`          | ✓     | `image` / `video` / `typography`         | —         |
| `media.image`          | `image`           | ✓     | min 1600×900, optimized                  | —         |
| `media.video_url`      | `url`             | ✓     | MP4/WebM, muted autoplay only            | —         |
| `media.overlay`        | `range`           | ✓     | 0.0–0.8 (darkness)                       | —         |
| `eyebrow`              | `text`            | ✓     | max 60 chars                             | ✓         |
| `headline`             | `richtext`        | ✓     | max 120 chars, `<em>` only               | ✓         |
| `intro`                | `richtext`        | ✓     | max 400 chars, inline tags only          | ✓         |
| `alignment`            | `select`          | ✓     | `left` / `center` / `right` (content box) | auto-flip |
| `primary_cta.label`    | `text`            | ✓     | max 28 chars                             | ✓         |
| `primary_cta.page_ref` | `page_ref`        | ✓     | —                                        | —         |
| `secondary_cta.*`      | same              | ✓     | optional                                 | ✓         |
| `stats[]`              | `list<fact>`      | ✓     | 0–4 facts, each `{num, label}`           | ✓         |
| `sidebar.enabled`      | `toggle`          | ✓     | applies only to `split-consultive`       | —         |
| `sidebar.quote`        | `richtext`        | ✓     | optional                                 | ✓         |
| `sidebar.author`       | `text`            | ✓     | optional                                 | ✓         |
| `sidebar.pulse[]`      | `list<label,val>` | ✓     | 0–3 rows                                 | ✓         |

**Variant locks:** il `hero_style` DNA (split-booking / editorial-serif /
full-bleed-manifesto / editorial-plate / typographic-index-ledger /
fullbleed-exif / warm-photo-frame / product-cutout) controlla la
composizione strutturale. Il customer sceglie l'immagine/video/colore,
non la geometria.

---

### 1.3 `section` — Sezioni generiche (manifesto, facts, visits, etc.)

Una sezione generica condivide lo stesso shape: blocco contenuto +
opzioni di layout + visibilità. Specializzazioni per `kind`.

| Field                    | Type          | Edit? | Notes                                    |
|--------------------------|---------------|-------|------------------------------------------|
| `visibility`             | `toggle`      | ✓     | Mostra/nasconde l'intera sezione         |
| `order`                  | `integer`     | ✓     | Indice nell'array `section_order`        |
| `kind`                   | `enum`        | ✗     | Locked to DNA — es. `facts`, `manifesto` |
| `label`                  | `text`        | ✓     | Eyebrow max 40 chars                     |
| `heading`                | `richtext`    | ✓     | `<em>` only, max 140 chars               |
| `intro`                  | `richtext`    | ✓     | Max 600 chars                            |
| `body`                   | `richtext`    | ✓     | Max 2000 chars, limited tags             |
| `items[]`                | `list`        | ✓     | Varianti per `kind` (cards, steps, ...)  |
| `background.mode`        | `select`      | ✓     | `paper` / `paper-2` / `dark` / `custom`  |
| `background.image`       | `image`       | ✓     | Optional, solo se `mode=custom`          |
| `background.color`       | `color_token` | ✓     | Brand-palette scoped                     |
| `layout.variant`         | `select`      | ✓     | 2-3 choices per `kind`                   |
| `layout.alignment`       | `select`      | ✓     | `left` / `center` / `right` / `justify`  |
| `layout.density`         | `select`      | ✓     | `compact` / `default` / `airy`           |
| `cta.enabled`            | `toggle`      | ✓     | —                                        |
| `cta.heading`            | `richtext`    | ✓     | Max 120 chars                            |
| `cta.primary.label`      | `text`        | ✓     | Max 28 chars                             |
| `cta.secondary.label`    | `text`        | ✓     | Optional                                 |

**Section kinds** (vocabolario da estendere nell'editor UI):

| Kind                  | Items shape                                            |
|-----------------------|--------------------------------------------------------|
| `facts`               | `[(num, label)]` · stagger + counter                   |
| `manifesto`           | single paragraph + drop-cap char                       |
| `signature_services`  | `[(num, title, blurb, icon?)]` · 1–6 items             |
| `team_list`           | `[{name, role, bio, portrait, tags?}]` · 1–12 items    |
| `pricelist`           | `[(name, meta, desc, price)]`                          |
| `timeline_steps`      | `[{num, icon, title, desc, duration}]`                 |
| `trust_strip`         | `[(fig, title, desc)]`                                 |
| `map_location`        | `{address, map_image, details[], hours_short[], cta}`  |
| `gallery_strip`       | `[(url, caption)]` + hover/lightbox                    |
| `tabs`                | `[{id, label, eyebrow, heading, body, items, cta}]`    |
| `compare_slider`      | `[{before_image, after_image, title, context}]`        |
| `editorial_feed`      | `[(url, meta, title)]`                                 |
| `process_cards`       | `[{icon, title, meta, desc}]`                          |
| `wine_program`        | `{sommelier{}, pairings[], cellar_facts[]}`            |
| `producer_showcase`   | `[{portrait, name, role, area, blurb}]`                |
| `press_strip`         | `[string]` marquee-able                                |
| `testimonial_quote`   | `{quote, author, context}`                             |
| `faq_accordion`       | `[(question, answer)]`                                 |
| `awards_grid`         | `[(badge, title, desc)]`                               |
| `seasonal_highlight`  | `{title, subtitle, text, cta}`                         |

**Add/remove items**: per sezioni con `items[]`, il customer può
`add/remove/reorder`, entro min/max per `kind` (es. team_list 1–12,
tabs 2–5, awards 2–6). Min < target < max è un soft-constraint:
l'editor mostra warning ma non blocca.

---

### 1.4 `form` — Form sections (contact / appointment / reservations)

| Field                       | Type           | Edit? | Notes                              |
|-----------------------------|----------------|-------|------------------------------------|
| `fields[]`                  | `list<field>`  | ✓     | Add/remove/reorder, min 2 fields   |
| `fields[].label`            | `text`         | ✓     | Max 40 chars, required             |
| `fields[].placeholder`      | `text`         | ✓     | Max 80 chars                       |
| `fields[].type`             | `select`       | ✓     | `text`/`email`/`tel`/`textarea`/`select`/`date` |
| `fields[].required`         | `toggle`       | ✓     | —                                  |
| `fields[].visible`          | `toggle`       | ✓     | Hide without deleting              |
| `fields[].options[]`        | `list<string>` | ✓     | Only for `select` type             |
| `fields[].full_width`       | `toggle`       | ✓     | Span 2 cols                        |
| `submit.label`              | `text`         | ✓     | Max 28 chars                       |
| `submit.success_message`    | `richtext`     | ✓     | —                                  |
| `style.variant`             | `select`       | ✓     | `floating` / `stacked` / `inline`  |
| `style.border_radius`       | `select`       | ✓     | `none` / `sm` / `md` (brand-scoped) |

**Hard constraint**: un form `appointment` deve sempre contenere almeno
i campi `name` + `email` + `phone` + `date`. L'editor può nasconderli
ma non rimuoverli (per non perdere la semantica conversion-CTA D-054).

---

### 1.5 `contact` — Contact / location block

| Field                   | Type            | Edit? | Notes                                   |
|-------------------------|-----------------|-------|-----------------------------------------|
| `address`               | `richtext`      | ✓     | Max 200 chars, multi-line               |
| `phone`                 | `text`          | ✓     | Formatted                               |
| `email`                 | `text`          | ✓     | Validated                               |
| `map.embed_provider`    | `select`        | ✓     | `static_image` / `google` / `mapbox`    |
| `map.coordinates`       | `lat,lng`       | ✓     | Required if `static_image`              |
| `map.image`             | `image`         | ✓     | Fallback always present                 |
| `hours[]`               | `list<row>`     | ✓     | `[(label, hours)]`                      |
| `channels[]`            | `list<channel>` | ✓     | WhatsApp/Instagram/LinkedIn buttons     |
| `layout.variant`        | `select`        | ✓     | `map-left` / `map-right` / `map-top`    |

---

### 1.6 `blog` — Blog / journal

| Field                   | Type       | Edit? | Notes                                    |
|-------------------------|------------|-------|------------------------------------------|
| `enabled`               | `toggle`   | ✓     | Blog can be turned off entirely          |
| `listing.variant`       | `select`   | ✓     | `grid` / `compact-list` / `cover-lead`   |
| `listing.featured_post` | `post_ref` | ✓     | Optional, selects 1 post to hero-feature |
| `listing.per_page`      | `integer`  | ✓     | 4 / 8 / 12                               |
| `listing.show_meta`     | `toggle`   | ✓     | Author, date, reading time               |
| `post.layout`           | `select`   | ✓     | `editorial-column` / `wide-prose`        |
| `post.lede_enabled`     | `toggle`   | ✓     | Drop-cap intro paragraph                 |
| `post.related_enabled`  | `toggle`   | ✓     | Show related posts                       |
| `parent_slug`           | `text`     | ✗     | Auto from content registry               |

---

### 1.7 `footer` — Footer

| Field                     | Type             | Edit? | Notes                                   |
|---------------------------|------------------|-------|-----------------------------------------|
| `columns[]`               | `list<col>`      | ✓     | 2–4 columns, reorderable                |
| `columns[].title`         | `text`           | ✓     | Max 32 chars                            |
| `columns[].items[]`       | `list<link>`     | ✓     | Free list of links                      |
| `contact_summary.enabled` | `toggle`         | ✓     | Embed address/phone/email block         |
| `social[]`                | `list<channel>`  | ✓     | IG / FB / LinkedIn / TikTok / custom    |
| `legal[]`                 | `list<link>`     | ✓     | Privacy / cookies / terms               |
| `credit_line`             | `text`           | ✓     | Max 120 chars                           |
| `license`                 | `text`           | ✓     | Optional: professional license          |
| `variant`                 | `select`         | ✓     | `4col-corporate` / `2col-compact` / `spa-social` |

---

### 1.8 `locale` — Localization container

Un customer project può ospitare più locali. Ogni locale è una
fotografia indipendente del content tree, keyed per `locale_code`.

| Field              | Type          | Edit? | Notes                                       |
|--------------------|---------------|-------|---------------------------------------------|
| `locales[]`        | `list<code>`  | ✓     | Subset di `SUPPORTED_LOCALES`               |
| `default_locale`   | `select`      | ✓     | Must be in `locales[]`                      |
| `fallback_policy`  | `select`      | ✓     | `hide_missing` / `fallback_to_default`      |
| `rtl_locales`      | `derived`     | ✗     | Auto da `RTL_LOCALES` (ar only today)       |
| `per_locale_tree`  | `content_map` | ✓     | Il customer edita ogni locale indipendente  |

**Translation quality gate**: ogni locale deve passare una soglia (es.
"80% dei campi text non-IT sono non-vuoti e diversi dal default"). Se
sotto soglia, il locale è marcato `draft` e non appare nel language
switcher pubblico — stesso paradigma di `WebTemplate.tier`.

---

## 2. Design controls (tokens scope)

Questi controlli agiscono sui CSS custom properties che gli skin leggono
(`--primary`, `--accent`, `--paper`, `--rule`, `--heading`, `--body`, etc.)
e sui token motion (`--lm-rise`, `--lm-dur-slow`). Sono globali al
template, non per-sezione.

| Control             | Type           | Scope        | Constraints                                |
|---------------------|----------------|--------------|--------------------------------------------|
| `palette.primary`   | `color`        | `--primary`  | Contrast ≥ 4.5:1 vs background             |
| `palette.secondary` | `color`        | `--secondary`| —                                          |
| `palette.accent`    | `color`        | `--accent`   | Contrast ≥ 3:1 vs `paper`                  |
| `palette.paper`     | `color`        | `--paper`    | Light surface                              |
| `palette.paper_2`   | `color`        | `--paper-2`  | Secondary surface                          |
| `font.heading`      | `font_ref`     | `--heading`  | Curated list (safe Google Fonts)           |
| `font.body`         | `font_ref`     | `--body`     | Curated list; must have weight 400+600     |
| `font.scale`        | `select`       | type scale   | `compact` / `default` / `editorial`        |
| `radius`            | `select`       | btn / card   | `none` / `sm` / `md` / `pill`              |
| `icon_pack`         | `select`       | svg inline   | `line` / `duotone` / `filled`              |
| `image_treatment`   | `select`       | filters      | `natural` / `editorial` / `cinematic`      |
| `text_alignment`    | `select`       | body default | `left` / `justify`                         |
| `layout_alignment`  | `select`       | grid skew    | `balanced` / `leading-left` / `leading-right` |
| `section_density`   | `select`       | padding unit | `compact` / `default` / `airy` / `very-airy` |
| `motion_profile`    | `select`       | `--lm-*`     | `clinical` / `editorial` / `cinematic` / `off` |

**Curated Google Fonts** (no arbitrary Google Fonts): Inter, Plus Jakarta
Sans, Cormorant Garamond, Bodoni Moda, Playfair Display, Lato, Caveat,
Big Shoulders Display, Archivo, Syne, Manrope, Merriweather, Libre
Baskerville, Nunito Sans, Quicksand, Noto Naskh Arabic, Noto Kufi Arabic,
Amiri. Tutti con `wght` range 400–700+ per evitare il D-040 font-miss
regression.

**Hard constraint**: il customer non può impostare palette low-contrast
— se il check fallisce, l'editor propone l'accent shift automatico
(non blocca, suggerisce).

---

## 3. Section order (riordinamento globale)

Il content registry espone `section_order: ["hero", "facts", "manifesto",
"signature_visits", ...]`. L'editor presenta un drag-and-drop con
vincoli:

- `hero` sempre primo, non spostabile
- `cta` sempre ultimo, non spostabile
- `sticky_cta` non appare nell'ordine (è un overlay)
- tutte le altre sono riordinabili
- la visibilità è indipendente dall'ordine (un blocco nascosto mantiene
  la sua posizione, ricomparirà esattamente lì)

**Per-archetype default order**: ogni archetipo spedisce il suo
`section_order` di default via DNA. L'override del customer viene
memorizzato come diff rispetto al default (non come snapshot), così
che se la baseline dell'archetype aggiunge una nuova sezione, il
customer la vede apparire al posto corretto.

---

## 4. Page registry (multi-page editor)

L'array `pages[]` nel content registry guida l'editor per creare/rimuovere
pagine.

| Field         | Type       | Edit? | Notes                                    |
|---------------|------------|-------|------------------------------------------|
| `slug`        | `text`     | ✓*    | URL-safe; `home` locked; altre editabili |
| `label`       | `text`     | ✓     | Visible in nav                           |
| `kind`        | `enum`     | ✗     | Page kind — legato al template HTML      |
| `visible`     | `toggle`   | ✓     | Pagina esiste ma non in nav              |
| `published`   | `toggle`   | ✓     | Unlisted fino a publish                  |
| `seo.title`   | `text`     | ✓     | Max 70 chars                             |
| `seo.description` | `text` | ✓     | Max 160 chars                            |
| `seo.og_image`| `image`    | ✓     | Optional                                 |

**Hard constraint**: le baseline pages per categoria (D-053 Live Preview
Law) devono essere presenti per mantenere il `published_live` tier.
L'editor blocca la rimozione di una baseline page con un warning
esplicito.

Le **nuove pagine** sono un opt-in: il customer può aggiungerle solo se
corrispondono a `kind` supportati dallo skin archetype (`case_study_detail`,
`property_detail`, ...). L'editor mostra solo i kind supportati.

---

## 5. Invarianti globali (editor contract)

Queste regole sono invariabili — l'editor le impone tramite validation
o le nega lato UI.

1. **D-047 chrome-authoring contract**: ogni stringa visibile proviene
   da un campo del content registry. L'editor non espone mai "testi
   hardcoded nello skin" perché semplicemente non esistono. Se l'utente
   vuole cambiare un label di nav, modifica `pages[].label`, non HTML.
2. **D-053 Live Preview Law**: il customer non può demolire la baseline
   di pagine minime (es. togliere `services` da un medical template).
   L'editor mostra "Pagina richiesta per il tier premium" e blocca
   l'eliminazione, non la visibility toggle.
3. **D-054 Premium Differentiation Law**: il customer non può settare
   il suo template in un modo che lo faccia apparire identico a un
   sibling DNA. L'editor blocca combinazioni palette+font+hero+section_order
   che ricadano dentro una distanza ≤ 2/10 del sibling.
4. **D-057 Tier migration**: `tier=published_live` richiede che il
   content tree del customer sia **completo** (zero campi required
   vuoti sulle baseline pages). L'editor pubblica con `draft` finché
   non passa il check di completeness.
5. **D-058 motion**: il customer può cambiare `motion_profile`
   (`off` / `clinical` / `editorial` / `cinematic`) ma non i singoli token.
   Questo garantisce interaction-quality floor senza frammentazione.
6. **D-059 i18n**: il language switcher appare automaticamente quando
   `locales[].length > 1`. Il customer non edita il widget — edita solo
   i tree per-locale.

---

## 6. Field types (per editor UI design)

Tipi atomici riutilizzabili dall'editor UI. Ogni tipo ha un widget
canonico (input/textarea/picker/uploader) e uno schema di validazione.

| Type          | UI widget                    | Stored as                         |
|---------------|------------------------------|-----------------------------------|
| `text`        | Single-line input            | `str`                             |
| `richtext`    | WYSIWYG con whitelist tags   | `str` (sanitized HTML)            |
| `textarea`    | Multi-line input             | `str`                             |
| `url`         | URL input + validation       | `str`                             |
| `email`       | Email input + validation     | `str`                             |
| `integer`     | Number input                 | `int`                             |
| `range`       | Slider                       | `float`                           |
| `toggle`      | Switch                       | `bool`                            |
| `select`      | Dropdown                     | `str` (enum)                      |
| `image`       | Uploader + library picker    | `{url, alt, width, height}`       |
| `video`       | Upload or URL (hosted)       | `{url, poster, duration}`         |
| `color`       | Color picker (palette scope) | `str` (hex/hsl)                   |
| `color_token` | Palette-scoped picker        | reference to `palette.*` key      |
| `font_ref`    | Curated Google Font picker   | `{family, weights[]}`             |
| `link`        | `{label, href|page_ref}`     | composite                         |
| `page_ref`    | Internal page selector       | `str` (page slug)                 |
| `post_ref`    | Internal post selector       | `str` (post slug)                 |
| `lat,lng`     | Map picker                   | `{lat: float, lng: float}`        |
| `list<T>`     | Reorderable list of `T`      | `[T]` with `min/max` constraints  |
| `channel`     | Social channel picker        | `{kind, handle, url}`             |
| `icon`        | Icon picker (curated set)    | `str` (icon key)                  |
| `content_map` | Locale-keyed tree editor     | `{locale: tree}`                  |

---

## 7. Persistence model (editor storage, non implementato)

Suggerimento per quando l'editor verrà acceso. Non è parte di questo
blueprint (niente codice), ma è esplicitato per completezza.

```
CustomerProject
  ├─ id (UUID)
  ├─ template_base: FK(WebTemplate)  # archetype source
  ├─ snapshot_dna: JSONField          # DNA at fork time
  ├─ tier: enum (draft / published)
  ├─ locales: [enum]
  ├─ default_locale: enum
  ├─ created_at, updated_at
ProjectContent (one-to-many)
  ├─ project: FK(CustomerProject)
  ├─ locale: str
  ├─ key_path: str                    # es. "home.percorso.steps[2].title"
  ├─ value: JSONField                 # tipizzato per field_type
  ├─ field_type: enum                 # text/image/...
  ├─ updated_at
ProjectDesignTokens (one-to-one)
  ├─ project: FK
  ├─ palette: JSONField               # {primary, secondary, accent, paper, paper_2}
  ├─ fonts: JSONField                 # {heading, body}
  ├─ radius, icon_pack, image_treatment, motion_profile: enum
  ├─ density: enum
ProjectRevision (optional audit log)
  ├─ project, changed_by, changeset: JSONField, created_at
```

**Read path**: il live renderer legge da `CustomerProject` come se il
project fosse un content registry bespoke. L'assemblaggio è:

1. Parte da `template_base.template_content` (baseline IT tree + locali).
2. Overlaya i `ProjectContent` per-locale (sparse diff, non snapshot).
3. Applica `ProjectDesignTokens` agli CSS custom properties via
   `_base.html` style block (inline override dopo il default).
4. Il view `LiveTemplateView` accetta `project_uuid=` e carica dal DB
   invece che dal registry statico.

Il content registry statico resta invariato — diventa il *fallback
seed* per ogni nuovo project.

---

## 8. Scalabilità (come questo si estende)

- **Nuovi kind di sezione** (es. `product_grid` per ecommerce): aggiungi
  al vocabolario `kind` + schema items + renderer nell'archetype skin.
  Zero impatto sui template esistenti.
- **Nuovi archetipi** (es. agency `bold-grid`): il DNA include
  `section_order` + `navbar_style` default; le varianti del customer
  sono limitate entro le famiglie DNA.
- **Nuovi locali** (es. tedesco): aggiungi al `SUPPORTED_LOCALES` +
  ogni template fornisce il tree DE (copy native) + editor lo espone
  automaticamente.
- **Editor in-page (live preview)**: il rendering è già server-side
  con zero JS dependencies — il customer edita un form, submit,
  reload della preview. Un futuro SPA editor può diffare i field
  values verso l'API `/api/v1/projects/{uuid}/content/` senza cambiare
  il renderer.
- **250 template target**: la forma registro-based scala linearmente.
  Ogni template aggiunge 1 DNA entry + 1 content block (multi-locale)
  + (eventualmente) 1 skin folder — pattern provato 20 volte.

---

## 9. Cosa questa sessione NON implementa (per chiarezza)

- ❌ Nessun codice editor (view, form, API endpoint, serializer, SPA).
- ❌ Nessuna migrazione DB (`ProjectContent`, `CustomerProject` non sono
  tabelle).
- ❌ Nessun cambio a `LiveTemplateView`: continua a leggere dal content
  registry statico.
- ❌ Nessun endpoint `/api/v1/projects/`.
- ❌ Nessuna UI di amministrazione customer.

**Questo documento è il contratto**. Il worktree `editor/` verrà aperto
quando Phase 2g3.7 sarà chiuso (20/20 template `published_live`) — a
quel punto questa specifica diventerà il TODO implementativo.

---

## 10. Pointer a decisioni
- D-047 Chrome-Authoring Contract — base per "tutto editabile proviene dal registro"
- D-053 Live Preview Law — baseline pages required
- D-054 Premium Differentiation Law — 10 dimensioni di differenziazione
- D-055/D-057 Template Tier Model — `published_live` vs `draft`
- D-058 Live Motion Language — motion profile come scelta discreta, non per-token
- D-059/D-063 i18n/RTL Pilot Architecture — locale-keyed content tree, native voice
- D-062 Ultra Premium Live Pass — interaction library extensible
- D-064 (Session 30) Premium Component Depth & Editor Blueprint — this document
