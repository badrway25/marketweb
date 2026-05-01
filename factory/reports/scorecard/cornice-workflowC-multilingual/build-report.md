# Build report · Cornice · workflow C multilingual

```yaml
phase:        X.5 Cornice · workflow C
date:         2026-05-01
verdict:      GREEN
```

## What shipped

4 new locale modules + 3 minimal wiring edits.

| File | Status | Lines | Purpose |
|---|---|---|---|
| `apps/catalog/template_content_cornice_en.py` | created | 1,083 | EN locale tree mirroring CORNICE_CONTENT_IT shape |
| `apps/catalog/template_content_cornice_fr.py` | created | 1,107 | FR locale tree |
| `apps/catalog/template_content_cornice_es.py` | created | 1,082 | ES locale tree |
| `apps/catalog/template_content_cornice_ar.py` | created | 1,088 | AR locale tree (formal MSA / الفصحى) |
| `apps/catalog/template_content.py` | modified | +5 / -5 | imports + locale-tree dispatch |
| `templates/live_templates/business/corporate-suite/_base.html` | modified | +7 / -1 | Naskh import + LF-2-scoped --heading override |
| `TEMPLATE_REGISTRY.json` | modified | +5 / -3 | locales [it]→[it,en,fr,es,ar] · rtl true · tier_reason rewritten |

Single source of truth for Pexels URLs: each new locale module imports
the URL constants from `template_content_cornice.py` (matches Solaria
Pass B / Continua Pass B precedent · prevents drift).

## Voice-anchor verbatim policy

The IT voice anchor lives on exactly two surfaces of the home page
(hero h1 + CTA-closer h2). Workflow C preserves this byte-equivalent
recurrence in every locale:

| Locale | Voice anchor | Em-noun |
|---|---|---|
| IT | `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` | argomento |
| EN | `Every project is a built <em>argument</em>, not a service rendered.` | argument |
| FR | `Chaque projet est un <em>argument</em> construit, non un service rendu.` | argument |
| ES | `Cada proyecto es un <em>argumento</em> construido, no un servicio prestado.` | argumento |
| AR | `كلّ مشروع <em>حُجَّة</em> مبنيّة، لا خدمة مُسداة.` | حُجَّة |

## AR Naskh-vs-Kufi (planner-brief §11 resolved)

Cluster default: Noto Kufi Arabic on headings, Amiri on body.
LF-2 editorial register favours humanist Naskh forms over Kufi
geometry — Kufi reads display-monumental (Pictet/family-office),
Naskh reads editorial-publication (Casabella/Domus/Architectural
Review). **Decision shipped: Noto Naskh Arabic on LF-2 headings;
Amiri body preserved; Latin wordmark + Latin Marta Roveri
preserved**. Selector-scoped to `body.cs-lf-lf-2` so every other
RTL skin keeps Kufi.

## Untouched

- apps/editor / apps/projects / apps/commerce — zero edits
- LF-2 layout files (`lf2/styles.html`, `lf2/content.html`) — zero edits
- LF-1 / LF-3 / LF-4 / LF-5 layout files — zero edits
- Other archetype templates — zero edits
- DNA registry / imagery pool / imagery policy — zero edits

## Tier

`draft` preserved. Public catalog still 23 published_live + 1 draft.
