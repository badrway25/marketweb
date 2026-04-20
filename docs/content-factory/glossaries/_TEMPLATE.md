# Macro-Category Glossary · `<macro-category-slug>`

**Status**: boilerplate. Copy to `glossaries/<macro-slug>.md` and fill.

**Purpose**: hold terms that recur across multiple clusters under the same macro-category. Cluster blueprints reference this file rather than redefining the same terms. When a term diverges between clusters (e.g. `maître` for fine-dining vs `cameriere` for trattoria), the cluster blueprint overrides — the glossary is the baseline.

**Scope**: 40-80 terms per macro-category. Fewer = anemic glossary. More = drift into encyclopedia territory.

---

## How to use this glossary

- **Cluster blueprints reference this file** via the pointer in `cluster_blueprints/<cluster>.md §4`.
- **Cross-cluster consistency**: if two clusters disagree on terminology, the glossary defines the neutral baseline and each cluster blueprint documents its deviation.
- **Locale columns**: fill EN / FR / ES / AR ONLY when the locale actually diverges from a straight translation. Otherwise leave blank — IT + translator notes from the locale author are enough.
- **Forbidden synonyms**: the glossary is the authority for what NOT to say. Reviewer flags any occurrence of a forbidden synonym in authored content.
- **Tone note**: how the term behaves — is it formal, editorial, neutral, customer-facing, internal-only?

---

## Macro-category identity

- **Macro slug**: `<e.g. restaurant>`
- **Human name (IT)**: `<e.g. Ristorante & food>`
- **Clusters under this macro**: `<list cluster slugs in this macro, e.g. fine-dining, trattoria, street-casual, bar-bistrot, bakery-pasticceria>`
- **Tone band** (range across this macro): `<e.g. from formal-editorial (fine-dining) to informal-local (trattoria) — all warm, none clinical>`

---

## Terminology table

| Term (IT) | Definition / usage | Forbidden synonyms | Tone / locale note | EN | FR | ES | AR |
|---|---|---|---|---|---|---|---|
| `<e.g. carta>` | menu of a restaurant / what is offered to the guest | `elenco piatti` (too administrative) | editorial · never "list" | menu | carte | carta | قائمة |
| `<e.g. stagione>` | seasonal sourcing narrative | `tempo` (too vague) | warm · editorial | season | saison | temporada | موسم |
| `<e.g. cantina>` | house wine selection | `lista vini` | preferred on "carta" page | cellar | cave | bodega | قبو |
| `<e.g. maître>` | front-of-house lead | `cameriere capo` (too common) | formal · keep IT in IT copy | maître | maître | maître | — |
| ... (add rows) | ... | ... | ... | ... | ... | ... | ... |

Fill 40-80 rows. Structured alphabetically or by section (e.g. "front-of-house", "kitchen", "guest journey").

---

## Cross-cluster divergence table

When two or more clusters under this macro-category disagree on a term, document here. This is where the cluster blueprint overrides start.

| Term (IT) | Cluster A usage | Cluster B usage | Why different |
|---|---|---|---|
| `<e.g. benvenuto>` | `<fine-dining: "amuse-bouche">` | `<trattoria: "antipastino della casa">` | voice difference · same concept |
| ... | ... | ... | ... |

---

## Forbidden patterns across this macro-category

Patterns that no cluster blueprint under this macro should use. Reviewer hard-fails on occurrence.

- ❌ `<e.g. "miglior ristorante" — superlative without evidence>`
- ❌ `<e.g. "tradizione millenaria" — cliché tempo-emoji>`
- ❌ `<e.g. "cucina genuina" — empty marketing claim>`
- ❌ `<e.g. "chef stellato" as Instagram-bio filler — only when factually true>`

---

## Changelog

| Date | Author | Change |
|---|---|---|
| `<2026-04-XX>` | `<Phase Lead>` | Initial glossary from _TEMPLATE.md |

---

**End of glossary template. 1 per macro-category. 15 total expected over X.3 + Wave 2.**
