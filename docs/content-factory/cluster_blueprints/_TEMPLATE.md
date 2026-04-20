# Cluster Blueprint · `<cluster-slug>`

**Status**: boilerplate template. Copy this file to `cluster_blueprints/<cluster-slug>.md` and fill every section. Missing sections fail review.

**Blueprint contract**: a cluster blueprint is the single document the IT Copy Author consults to produce a new template. Its job is to make the author decisions deterministic — same blueprint → same voice, same terminology range, same imagery style, same differentiation framing.

**Scope guardrail**: a blueprint describes content + visual + keyword + imagery. It NEVER prescribes new page kinds, new interaction primitives, new archetypes. If a cluster "needs" something structurally novel, it is NOT a Wave 2 candidate. Escalate.

---

## 1 · Identity

- **Cluster slug**: `<e.g. fine-dining>`
- **Cluster human name** (IT): `<e.g. Fine dining>`
- **Macro-category**: `<e.g. restaurant>`
- **Archetypes that serve this cluster**: `<e.g. fine-dining>` (current enrolled archetypes only · no new)
- **Cluster enrolled since**: `<e.g. X.2 Commit 2>` / `<Wave 2 · template-N>`

### Identity summary (2-3 sentences · IT)

Describe who this profession is, what they do, and why a template in this cluster is distinct from adjacent clusters. Avoid marketing fluff. Aim for reader-verifiable accuracy.

Example (fine-dining): *"Ristoranti gourmet che ambiscono a una tavola d'autore: chef riconosciuto, carta a degustazione, servizio allineato a standard Michelin. Il sito deve comunicare ricerca, disciplina, e ospitalità senza scivolare nella formalità fredda."*

---

## 2 · Audience

- **Primary audience slugs** (select 1-3 from `freelance · smb · studio · agency · enterprise`): `<e.g. smb>`
- **End-customer of the template's customer** (who visits the site): `<e.g. cena speciale · anniversary · business dinner · food writers · critici gastronomici>`
- **Decision maker**: owner-chef / maître / marketing manager (describe which for this cluster)

---

## 3 · Positioning

### What the site must achieve (top 3)

1. `<e.g. comunicare lo stile di cucina e del chef>`
2. `<e.g. canalizzare prenotazioni>`
3. `<e.g. raccontare il percorso e i riconoscimenti>`

### What the site must avoid

- `<e.g. no photo-stock genericismo>`
- `<e.g. no claim "miglior ristorante d'Italia" non supportato>`
- `<e.g. no menu-PDF download · menu è content editabile>`

### Competitive positioning (2-3 adjectives)

`<e.g. editorial · chef-driven · understated>`

---

## 4 · Terminology dictionary

A profession-specific vocabulary the author uses naturally. Lists 20-40 terms. IT primary; mark `[en-fr-es-ar]` when a locale needs a specific variant.

| Term (IT) | Definition / usage | Forbidden synonym | Tone / locale note |
|---|---|---|---|
| `<e.g. degustazione>` | menu dello chef a percorso · 6-10 portate | `menu tasting` (anglismo) | editoriale · formale-caldo |
| `<e.g. cantina>` | selezione vini della casa | `wine list` | preferito su pagina "carta" |
| `<e.g. maître>` | responsabile di sala | `cameriere capo` (troppo quotidiano) | formale · keep in IT originale |
| ... | ... | ... | ... |

Aim for **20-40 rows**. Fewer = blueprint incompleto. More = sprawl.

---

## 5 · Voice & tone

- **Register**: `<e.g. formal-warm>` / `<informal-technical>` / `<editorial-critical>`
- **Sentence length preference**: `<e.g. short · declarative>` vs `<long · recursive>`
- **Pronouns**: `<e.g. prefer "voi" per ospitalità · avoid "tu" salvo micro-copy>`
- **Rhetorical devices allowed**: `<e.g. quotations from chefs · no bullet-point fetish · no exclamation marks>`
- **Rhetorical devices banned**: `<e.g. no startup-hype · no "rivoluzionario" · no "leader"

### Voice anchor (1 paragraph · IT)

Write a 3-4 line paragraph that the author reads aloud to calibrate tone. This is the single most important calibration in the blueprint.

Example: *"Parliamo di un mestiere che vive di precisione. La nostra voce è quella di chi ha cucinato davvero: passi brevi, dettagli concreti, rispetto per la materia. Non vendiamo, raccontiamo. Un cliente fidelizzato non arriva dal superlativo, arriva da come chiamiamo un piatto."*

---

## 6 · Copy skeleton by page kind

For each page kind the cluster's archetype(s) support, sketch the copy skeleton. Not full copy — scaffold only.

### Home
- Hero headline (IT): 8-12 words · must carry the chef/identity signal
- Hero lead: 2 lines · concrete, not abstract
- Secondary CTA: `<Prenota>` (map to archetype capability)
- 3-6 value props below the fold
- Signature section: `<specific to cluster>`

### About / Studio
- Origin story (3-5 paragraphs)
- Team bios (required fields per archetype registry)
- Recognitions / awards (if applicable)

### Services / Menu / Lavori / Pratiche / ...
- One section per archetype-supported page kind
- Field-level guidance: "3-6 items · each with title + short desc + optional meta"

### Contact
- Copy tone: `<e.g. welcoming · precise on booking expectations>`
- Fields to emphasize (tied to archetype capability)

Add as many page kinds as the archetype(s) support. Do NOT invent page kinds not in the archetype registry.

---

## 7 · Search keywords pack

### Core (3-6 · IT · lowercase · accent-aware)

```
<e.g. ristorante stellato chef haute-cuisine gourmet>
```

### Aliases (0-8)

```
<e.g. michelin fine-dining alta-cucina gastronomia cena-degustazione>
```

### Synonyms to include (cross-locale if relevant)

```
<e.g. haute-cuisine (fr), fine-dining (en), alta-cocina (es)>
```

### Terms to exclude (anti-stuffing)

```
<e.g. migliore · top · #1 · eccellente (stop-word / superlative stuffing)>
```

---

## 8 · Imagery pack pointer

Imagery pack for this cluster: `imagery/packs/<cluster-slug>.md`

**Mandatory before copy authoring starts.** See `imagery/CURATION_PROTOCOL.md`.

Blueprint-level imagery direction:
- **Subjects required**: `<e.g. plate close-ups · chef in action · dining room ambience · wine pairing · ingredients raw>`
- **Color palette guidance**: `<e.g. warm earthy · copper / wood / deep red · avoid neon, avoid pastel>`
- **Composition guidance**: `<e.g. editorial crop · candid over staged · avoid drone shots>`
- **Avoid**: `<e.g. stock "generic kitchen" · hand-model with utensils · Photoshop-overdone saturation>`

---

## 9 · Audience tags

Populate `WebTemplate.audience` JSONField with these slugs when a template is authored in this cluster:

```
["<e.g. smb>", "<e.g. freelance>"]
```

Limit: max 3 slugs. More = lazy targeting.

---

## 10 · Price tier rationale

**Recommended tier**: `<free · standard · premium>`

**Rationale** (1-2 sentences): `<e.g. premium because the imagery effort + editorial copy quality sits above the mass-market line; clusters with templated form scaffolding would be standard.>`

Authors can override in specific templates if justified; reviewer validates.

---

## 11 · Feature flag expectations

Baseline expectations for `WebTemplate.has_*` flags for templates in this cluster:

| Flag | Expected | Rationale |
|---|---|---|
| `has_shop` | `<True / False>` | `<e.g. False · restaurant cluster rarely sells online>` |
| `has_booking` | `<True / False>` | `<e.g. True · reservation is the primary conversion>` |
| `has_portfolio` | `<True / False>` | `<e.g. False · chef story is narrative, not portfolio>` |
| `has_blog` | `<True / False>` | `<e.g. optional · journal if cluster voice warrants>` |
| `has_video` | `<True / False>` | `<e.g. optional · per-template imagery decision>` |
| `has_rtl` | `True` (always) | D-098 · 5-locale RTL uniform |
| `is_multi_page` | `True` (always) | Templates ship multi-page by definition |

Deviations must be justified in the PR and approved by Reviewer.

---

## 12 · Example brand names

2-3 brand names that "sound right" for this cluster. Sub-agents can draw inspiration but must not reuse these verbatim on new templates (brand uniqueness invariant).

- `<e.g. Acàri — Cucina Contemporanea>`
- `<e.g. Cadamuro — Atelier del Gusto>`
- `<e.g. Quinta Fila — Tavola d'Autore>`

---

## 13 · Anti-patterns

What to never do in this cluster. Reviewer uses this list as a hard fail list.

- ❌ `<e.g. "migliore ristorante" / "tradizione millenaria" / superlatives without evidence>`
- ❌ `<e.g. stock photo "chef holding plate smiling at camera">`
- ❌ `<e.g. PDF menu · menu must be editable content>`
- ❌ `<e.g. Facebook-like testimonial wall · instead: 1-2 editorial press quotes>`
- ❌ `<e.g. Lorem ipsum placeholders at merge time>`

---

## 14 · D-054 differentiation notes

This cluster has **N** templates (current count: `<n>`). When adding a new template, verify all 10 D-054 gates produce a measurable difference vs each existing sibling.

### Sibling templates in cluster

- `<e.g. gusto-fine-dining>` — palette warm · Tuscan editorial · full RTL
- `<e.g. <next>-fine-dining>` — palette `<...>` · `<...>` · `<...>`

### 10-gate differentiation matrix (fill when adding sibling N+1)

| # | Gate | Template A | Template B (new) |
|---|---|---|---|
| 1 | Palette | `<warm earth>` | `<e.g. cool slate>` |
| 2 | Typography | `<Cormorant + Inter>` | `<e.g. Playfair + Roboto>` |
| 3 | Density | `<editorial-sparse>` | `<e.g. magazine-hybrid>` |
| 4 | Hero composition | `<plate close-up>` | `<e.g. dining-room ambience>` |
| 5 | Headline tone | `<declarative-quiet>` | `<e.g. poetic-evocative>` |
| 6 | Signature section | `<chef's words>` | `<e.g. sourcing map>` |
| 7 | Price tier | `<premium>` | `<e.g. standard>` |
| 8 | Audience tier | `<enterprise-SMB>` | `<e.g. freelance-SMB>` |
| 9 | Imagery saturation | `<muted>` | `<e.g. rich-high-contrast>` |
| 10 | Brand personality adjectives | `<understated · precise>` | `<e.g. celebratory · generous>` |

### Adjacency notes

This cluster feels adjacent to:
- `<e.g. trattoria>` (same macro-category, distinct tone)
- `<e.g. bakery-pasticceria>` (warm aesthetic, different conversion path)

This cluster must feel distinct from:
- `<e.g. street-casual>` (same macro-category, opposite tone)
- `<e.g. bar-bistrot>` (same macro-category, informal positioning)

---

## 15 · Changelog

| Date | Author | Change |
|---|---|---|
| `<2026-04-XX>` | `<Phase Lead>` | Initial blueprint from _TEMPLATE.md |

---

**End of cluster blueprint. Review → sign-off → author consumes.**
