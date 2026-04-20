# Search Keywords · Authoring Contract

**Status**: binding for every template's `WebTemplate.search_keywords` value and for cluster `search_aliases` (used by the typeahead endpoint `/templates/search/typeahead/`).

**Scope**: what constitutes a valid `search_keywords` string. Keywords are what the catalog typeahead matches against first (before cluster name and role label). A lazy `search_keywords` tanks discovery.

---

## 1 · Contract summary

| Rule | Spec |
|---|---|
| Primary language | **Italian (IT)**, lowercase, accent-aware |
| Core term count | **3 to 6 words** (compound words with hyphen count as 1) |
| Alias term count | **0 to 8 words**, reinforcing the core |
| Synonyms | Allowed when profession uses a non-IT term natively (e.g. `haute-cuisine`, `smart-working`); not for pure anglicisms |
| Stop-word junk | **Forbidden** (`il`, `la`, `lo`, `di`, `a`, `in`, `con`, `su`, `per`, `tra`, `fra`, `e`) |
| Stuffing | **Forbidden**: a term may not appear more than once; obvious repetition (e.g. `pizza pizzeria pizze`) is a violation |
| Geo-neutral | Default **yes**. Geo-specific terms (city names) only if the template's positioning is explicitly geo-locked (e.g. `dermatologia-elite-roma` may carry `roma`) |
| Brand hijacking | **Forbidden**: no competitor brand names (`wix`, `wordpress`, `squarespace`, `shopify`, `cognome-concorrente`) |
| Locale mixing | Allowed sparingly for multi-locale discoverability (e.g. `michelin haute-cuisine` on a `fine-dining` template) |
| Separator | Single space between terms. Compound words use hyphen (`fine-dining`, `studio-legale`). No commas, no pipes |

---

## 2 · Format specification

The `search_keywords` field is a single space-separated string, lowercase, with hyphenated compound words.

**Good**:
```
ristorante stellato chef haute-cuisine gourmet michelin degustazione
```

**Bad** (for each reason):
```
"ristorante, stellato, chef, ..."         → commas not allowed
"Ristorante Stellato Chef"                → must be lowercase
"ristorante pizzeria ristoranti pizze"    → stuffing + repetition
"ristorante il migliore di milano"        → stop-word junk + geo + superlative
"wordpress restaurant template"            → competitor brand hijack + English first
```

---

## 3 · Core vs alias

- **Core** (3-6 terms): the terms a customer searching for this profession would realistically type. Include the profession name + the 2-3 most distinguishing features.
- **Alias** (0-8 terms): regional synonyms, industry slang, complementary concepts.

The two sets are merged into a single `search_keywords` value. The cluster-level `ProfessionCluster.search_aliases` field (introduced in X.2 Commit 1) complements the template-level field — the typeahead endpoint searches both.

**Example split (before merging)**:

Cluster `fine-dining`:
- Core (5): `ristorante stellato chef haute-cuisine gourmet`
- Alias (5): `michelin fine-dining alta-cucina degustazione cena-degustazione`
- Merged (10): `ristorante stellato chef haute-cuisine gourmet michelin fine-dining alta-cucina degustazione cena-degustazione`

Template `gusto-fine-dining` (specific to the Tuscan editorial brand):
- Core (4): `gusto gourmet michelin chef-toscano`
- Alias (4): `vigneto stelle-michelin stellato prezzemolo-toscano`

Each layer contributes differently: cluster covers the profession discovery; template covers brand + regional specifics.

---

## 4 · Ten worked examples

### 4.1 · `fine-dining`

```
ristorante stellato chef haute-cuisine gourmet michelin fine-dining degustazione cena-degustazione alta-cucina
```

Core: `ristorante stellato chef haute-cuisine gourmet` · Alias: `michelin fine-dining degustazione cena-degustazione alta-cucina`.

### 4.2 · `trattoria`

```
trattoria pizzeria osteria menu tradizionale regionale pizza famiglia-italiana
```

Core: `trattoria pizzeria osteria menu tradizionale` · Alias: `regionale pizza famiglia-italiana`. Avoid `migliore`, `autentica` (superlative stuffing).

### 4.3 · `dental`

```
dentista odontoiatra igiene-dentale implantologia ortodonzia studio-dentistico impianto faccetta
```

Core: `dentista odontoiatra igiene-dentale implantologia ortodonzia` · Alias: `studio-dentistico impianto faccetta`. No `sorriso perfetto` (cliché).

### 4.4 · `veterinary`

```
veterinario clinica-animali ambulatorio-veterinario animali-domestici cane gatto esotici
```

Core: `veterinario clinica-animali ambulatorio-veterinario animali-domestici` · Alias: `cane gatto esotici`. Avoid `miglior-veterinario-della-città` (geo + superlative).

### 4.5 · `classic-law`

```
avvocato studio-legale civile penale commerciale consulenza-legale contenzioso diritto-civile
```

Core: `avvocato studio-legale civile penale commerciale` · Alias: `consulenza-legale contenzioso diritto-civile`. No `successo-garantito` (forbidden promise).

### 4.6 · `modern-law-tech`

```
avvocato ip startup diritto-tech privacy gdpr proprietà-intellettuale legal-tech
```

Core: `avvocato ip startup diritto-tech privacy gdpr` · Alias: `proprietà-intellettuale legal-tech`. `ip` and `gdpr` are legitimate industry acronyms — allowed.

### 4.7 · `financial-services`

```
commercialista fiscale finanza tasse contabilità dichiarazione-redditi wealth-management revisore
```

Core: `commercialista fiscale finanza tasse contabilità` · Alias: `dichiarazione-redditi wealth-management revisore`. Do not stuff with `esperto`, `specialista` (generic).

### 4.8 · `photographer`

```
fotografo fotografia moda ritratto architettura fine-art still-life fotografo-editoriale
```

Core: `fotografo fotografia moda ritratto architettura` · Alias: `fine-art still-life fotografo-editoriale`. Avoid `migliore-fotografo` + `instagram-style`.

### 4.9 · `artisan-workshop`

```
artigiano atelier maker bottega produzione-artigianale made-in-italy laboratorio terroir
```

Core: `artigiano atelier maker bottega produzione-artigianale` · Alias: `made-in-italy laboratorio terroir`. Do not mix with `e-commerce` verbatim — the cluster is `artisan-workshop`, discovery already routes to ecommerce macro-category via the cluster FK.

### 4.10 · `wedding-venue`

```
wedding matrimonio location sposi wedding-planner villa-eventi ricevimento organizzazione-matrimoni
```

Core: `wedding matrimonio location sposi wedding-planner` · Alias: `villa-eventi ricevimento organizzazione-matrimoni`. Avoid `matrimonio-sogno` (cliché).

---

## 5 · Anti-patterns (hard fails)

The reviewer rejects the `search_keywords` value for any of:

- ❌ **Fewer than 3 core terms** — keyword coverage is too thin for typeahead to rank this template.
- ❌ **More than 14 terms total** — stuffing for discovery gaming.
- ❌ **Stop-words present** (`il`, `la`, `di`, `a`, `in`, `per`, `con`, ...).
- ❌ **Superlatives without evidence** (`migliore`, `top-1`, `#1`, `leader`, `eccellente`, `premier`).
- ❌ **Generic adjective stuffing** (`professionale`, `serio`, `affidabile`, `innovativo`, `moderno` × 3).
- ❌ **Competitor brand hijack** (`wordpress-alternative`, `shopify-competitor`, `wix-better`).
- ❌ **Repetition** of the same root (`pizza pizzeria pizze pizzaiolo` — one root, one term).
- ❌ **All-English or all-non-IT** on an IT-first catalog.
- ❌ **Geo-specific without rationale** (`roma milano napoli` when template is not geo-locked).
- ❌ **Trademark-sensitive terms** (`michelin` is ok as a factual reference if the business truly has/aims for a star; otherwise it's keyword hijack).

---

## 6 · Locale alignment

The `WebTemplate.search_keywords` field is **not locale-keyed**. It's a single IT-first string used by the typeahead endpoint across all locales.

**Rationale**: the typeahead is a discovery affordance, not content. IT is the primary market. International customers searching in EN/FR/ES can still match compound terms like `haute-cuisine` or brand-neutral terms like `michelin`. Full localization of search_keywords is out of scope for Wave 2.

If a template truly needs locale-specific discoverability (e.g. a Paris-focused `haute-cuisine` template needing FR-dominant keywords), the author flags it in the PR and reviewer decides case-by-case. No blanket policy for locale-split search_keywords.

---

## 7 · Cluster-level `search_aliases` relationship

`ProfessionCluster.search_aliases` (X.2 Commit 1) is the cluster-wide alias pool. The typeahead endpoint ILIKE-matches on both `WebTemplate.search_keywords` and `ProfessionCluster.search_aliases` simultaneously, so:

- **Cluster aliases** capture profession-wide terms (`stellato`, `michelin`, `haute-cuisine` for `fine-dining`).
- **Template keywords** capture brand + template-specific terms (`gusto`, `toscano`, `prezzemolo`).

Authors should **not** duplicate all cluster aliases into every template's keywords. That's wasted character budget. Keep the template keywords brand-specific + 1-2 high-salience cluster terms.

---

## 8 · Examples of good vs bad full values

### Good

```
fiscus commercialista fiscale ires ivasi dichiarazione-redditi studio-tributario
```

- 7 terms · all IT · compound hyphenated · brand-first (`fiscus`) + 2 cluster-salience (`commercialista`, `fiscale`) + 4 niche (`ires`, `iva`, `dichiarazione-redditi`, `studio-tributario`).
- Zero stop-words. Zero stuffing.

### Bad (annotated)

```
il migliore studio fiscale di milano esperto in tasse, iva, bilancio, dichiarazioni
```

- Stop-words (`il`, `di`, `in`). Superlative (`migliore`). Geo (`milano`) without justification. Commas. Generic adjective (`esperto`). Redundancy (`tasse` + `iva` + `bilancio` + `dichiarazioni` is 4 angles of the same thing — fine if IT-spread, but lazy stuffing is the real issue).

---

## 9 · Review ordering

When a reviewer validates the `search_keywords` value:

1. **Split into tokens** on whitespace.
2. **Count tokens** → 6 ≤ count ≤ 14. Out of range → reject.
3. **Scan for stop-words** → any present → reject.
4. **Scan for repetition** → same root token twice → reject.
5. **Scan for superlatives** against the list in §5 → any present → reject.
6. **Scan for competitor brand terms** → any present → reject.
7. **Scan for generic adjective stuffing** → 3+ generic adjectives in a row → reject.
8. **Compare against cluster blueprint §7 Search Keywords Pack** → misalignment flag to author (not an auto-reject, but the author must justify).
9. **Green**: ship.

A compact reviewer form is in `reviewer_checklist.md` (this directory).

---

**End of contract. Binding for Wave 2+ templates. Updates require Phase Lead sign-off.**
