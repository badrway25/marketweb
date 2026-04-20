# Content Factory · Runbook

**Phase**: X.3 · Commit 1 (docs scaffolding).
**Status**: binding for all Wave 2+ template authoring.
**Scope**: how a new template moves from zero to published_live without reopening editor/enrollment architecture.

This runbook is the **operational contract** the factory follows to scale the catalog from 20 templates to 80+ (and eventually 200+) using the 19 archetypes enrolled during the A.6 → A.17b program. Skipping any step here reopens the failure modes catalogued in the blacklist (Session 31 imagery disaster, D-047 locale-leak incidents, D-054 differentiation drift).

---

## 1 · Binding invariants (non-negotiable)

1. **Zero new archetypes in Wave 2.** Every new template rides one of the 19 enrolled archetypes. A cluster that needs a novel page kind, novel indexed shape, or novel interaction primitive is NOT a Wave 2 candidate — it waits for a dedicated structural phase (post-X.3).
2. **Zero touches to `apps/editor`, `apps/projects`, `apps/commerce`, `templates/live_templates/`, `static/editor/`.** D-099 program closure stays intact. Any factory step that feels like it needs to touch these paths is wrong about its own scope.
3. **Imagery curator step happens BEFORE copy authoring.** Not in parallel. Not after. Not "we'll fix imagery later". See §2.
4. **IT is master locale.** EN / FR / ES / AR follow. No parallel IT authoring across sub-agents — the master IT copy tree is the source of truth.
5. **Playwright MCP browser verification is mandatory** for every Wave 2 template merge and for every public-surface commit in X.3+ (exceptions: docs-only commits, Python-tests-only commits). See §6.
6. **D-054 10-gate differentiation** applies between sibling templates in the same cluster. A cluster with 2+ templates must show a measurable visual + tonal difference on each of the 10 gates.
7. **D-047 chrome-authoring rule** stays binding: no IT locale literals in skin `_base.html`. Every locale string flows through `chrome` / `site.*` keys.

---

## 2 · Operational pipeline · end-to-end

The pipeline runs as a **5-day cadence** per cluster (parallelizable across clusters, serial within a cluster). Day counts are upper bounds; experienced authors can compress.

```
Day 0 · Phase Lead
  - Pick cluster from backlog (pilot_batch/x4_wave2_first_10.md)
  - Assign one Imagery Curator, one IT Copy Author, four Locale Authors, one Reviewer
  - Ensure cluster blueprint exists in cluster_blueprints/<slug>.md
  - Ensure terminology glossary exists in glossaries/<macro-category>.md

Day 1 · Imagery Curator  (BLOCKING · nothing downstream starts until LGTM)
  - Read cluster blueprint (identity, audience, voice, anti-patterns)
  - Select 20-40 image URLs from allowed sources (imagery/sources.md)
  - Run validation (imagery/CURATION_PROTOCOL.md §4): curl-check + semantic caption + cross-cluster duplication check + resolution + licensing
  - Produce imagery/packs/<cluster-slug>.md
  - Reviewer LGTM on imagery pack (phase gate)

Day 2 · IT Copy Author
  - Read cluster blueprint + glossary + imagery pack
  - Author the IT content tree (all page kinds declared by the archetype)
  - Propose 3-6 core search_keywords + aliases (contract in search_keywords/AUTHORING_CONTRACT.md)
  - Declare use_cases, audience, price_tier, feature_flags matching the blueprint expectations
  - Commit: IT content tree + template metadata

Day 3 · Parallel Locale Authors (EN · FR · ES · AR)
  - 4 sub-agents run in parallel, each claims one locale
  - Source of truth is the IT content tree from Day 2
  - Translate + localize + adapt tone per native idiom (D-054 differentiation allowed to breathe across locales)
  - AR author also performs RTL layout sanity on a local preview
  - Each locale produces one content tree with zero key drift vs IT master
  - Commit: 4 locale trees in parallel

Day 4 · Reviewer  (BLOCKING · no merge until LGTM)
  - Run acceptance checklist (§5 below)
  - Cross-locale parity check (all 5 locales carry identical keys)
  - D-047 chrome-authoring check (no locale literals in skin)
  - D-054 10-gate differentiation check vs siblings in same cluster
  - Imagery blacklist re-verification (spot-check 3-5 random URLs)
  - Run `python manage.py test apps` locally → expect green
  - Run `python smoke_full.py` locally → expect +5 (or +10 if posts) new routes HTTP 200
  - Playwright MCP browser walk per §6 checklist
  - LGTM or remand with explicit rework note (not "doesn't feel right")

Day 5 · Phase Lead
  - Merge to phase-integration-baseline-v15
  - Push
  - Update TEMPLATE_REGISTRY.json tier if relevant
  - Update SESSION_LOG.md + DECISIONS.md if new operational clarification surfaced
```

---

## 3 · Cluster assignment rules

- **Exclusive claim** — one cluster is owned by one sub-agent team for at most 5 calendar days. Past that, the cluster is returned to the backlog and re-assigned.
- **Backlog priority** — strictly follow `pilot_batch/x4_wave2_first_10.md` for the first 10 templates. Deviation from the pilot list requires Phase Lead sign-off.
- **No double-work** — a cluster in flight is flagged by a PR draft + a note in the cluster blueprint. Two authors never work on the same cluster simultaneously.
- **Parallel clusters ok** — up to 3-4 clusters can run in parallel if Imagery Curator capacity allows (the curator is the bottleneck).

---

## 4 · Locale discipline

| Locale | Role | Native-speaker review |
|---|---|---|
| IT | Master · source of truth | Required at all times (native speaker Phase Lead) |
| EN | Tier-1 · business default | Recommended (not blocking for MVP Wave 2) |
| FR | Tier-1 · European business | Recommended |
| ES | Tier-2 · Mediterranean business | Pass-through acceptable for MVP; native review before go-live |
| AR | Tier-2 · **RTL + typography review BLOCKING** | Native review blocking (Arabic script correctness + right-to-left layout integrity) |

**Zero key drift across locales.** Every content tree ships exactly the same set of keys. A key missing in one locale fails D-098 gate and breaks typeahead/facet/discovery surfaces that index cross-locale.

**Phone numbers / prices / dates / addresses** localized per locale. Never hardcoded in a skin template.

---

## 5 · Reviewer acceptance checklist

Before any Wave 2 template merges to baseline, the Reviewer confirms **all** of:

- [ ] Imagery pack produced + all URLs curl-validated (status 200, content-type image/*, ≥ 1600×900 for hero, ≥ 800×800 for portraits)
- [ ] Imagery blacklist check clean (no Session 31 pattern matches: category mismatch · generic stock · cross-cluster reuse · low resolution · noisy CTA bg · watermark · cultural insensitivity)
- [ ] 5 locale content trees present (`it`, `en`, `fr`, `es`, `ar`) with identical key sets
- [ ] D-047 chrome-authoring clean (zero IT locale literals in `_base.html` or any skin)
- [ ] D-054 10-gate differentiation confirmed vs sibling templates in the same cluster (or N/A if cluster has only this template)
- [ ] `search_keywords` honor contract: 3-6 core · aliases · IT-first · no stuffing · no stop-words · no competitor brand names
- [ ] `use_cases` array aligns with template page kinds (e.g. `appointment-booking` only if archetype supports booking kind; `sell-online` only if `has_shop=True`)
- [ ] `audience` array populated with at least 1 valid slug from the 5 canonical audience slugs (`freelance · smb · studio · agency · enterprise`)
- [ ] `price_tier` choice justified via cluster blueprint rationale
- [ ] 7 feature flags set coherently with both the archetype capability and the cluster expectations (flags that don't match archetype capability raise in review)
- [ ] `profession_cluster` FK points to a cluster whose `category` equals the template's `category` (invariant enforced at test layer)
- [ ] `visual_style` FK exists and matches the cluster blueprint's visual-style expectations (or an approved deviation documented in the PR)
- [ ] `python manage.py check` → 0 issues
- [ ] `python manage.py test apps` → all green (no regression; new tests added for the new template if applicable)
- [ ] `python smoke_full.py` → new public routes (detail + preview home + inner pages + posts where applicable) all HTTP 200 across 5 locales
- [ ] Playwright MCP browser walk per §6 green
- [ ] `TEMPLATE_REGISTRY.json` updated if tier changes

---

## 6 · Playwright MCP mandatory browser verification

Required for every Wave 2 template merge and for every X.3+ commit that touches a public catalog/homepage surface.

### 6.1 · Per-template (Wave 2)

| Surface | Must verify |
|---|---|
| `/templates/<cat>/<slug>/` | Detail pills render: cluster · visual style · price tier · feature chips · use-case list with real labels |
| `/templates/<cat>/<slug>/preview/` (home, IT) | Hero content rendered · real brand voice · no lorem ipsum · no IT locale-string leak into skin |
| `/templates/<cat>/<slug>/preview/?lang=ar` | `<html dir="rtl" lang="ar">` in markup · no horizontal overflow on 1440px or 1024px viewport · typography RTL-aware |
| `/templates/for-role/<role>/` (if cluster is linked) | New template appears in the role-discovery grid |
| `/templates/for-use-case/<use-case>/` (if use-case is declared) | New template appears in the use-case discovery grid |
| `/templates/search/typeahead/?q=<core-keyword>` | New template appears in the typeahead JSON response |
| `/templates/?cluster=<cluster-slug>` | New template appears in the faceted list |

### 6.2 · Per X.3+ commit (public surface touched)

Any commit that touches `templates/catalog/`, `templates/pages/`, `static/css/`, `static/js/`, `apps/pages/views.py`, `apps/catalog/views.py`, `apps/catalog/selectors.py`, or `apps/catalog/urls.py` requires a mandatory browser walk on:

- `/` (homepage hero + chips + role grid + use-case grid + trust strip + featured + final CTA)
- `/templates/` (facet sidebar + card pills + no dict leak)
- One cluster detail page (e.g. `/templates/clusters/specialist/`)
- One role discovery page (e.g. `/templates/for-role/medici/`)
- One use-case discovery page (e.g. `/templates/for-use-case/sell-online/`)
- One template detail page (e.g. `/templates/ecommerce/luxe-fashion-store/`)
- One AR RTL live preview (e.g. `/templates/agency/vertex-creative-agency/preview/?lang=ar`) to verify editor live-preview architecture stays untouched

**Acceptance**: zero blocking console errors (favicon.ico 404 is pre-existing and allowed); all surfaces return HTTP 200; visible pills/badges/counters render with correct styling; no layout drift observed at 1440×900 viewport.

---

## 7 · What must never be delegated blindly

These decisions require Phase Lead or senior Reviewer sign-off. Sub-agents must stop and escalate, not decide.

- **Brand identity choice** — brand name, palette, typography pairing, personality. Phase Lead decides.
- **D-054 differentiation framing** — when a new template is visually close to a sibling, senior Reviewer decides whether the 10 gates are crossed.
- **Imagery final acceptance** — curator produces, senior Reviewer signs off. Two-eyes rule before LGTM.
- **`profession_cluster` / `category` / `archetype` FK assignment** — Phase Lead + senior Reviewer. A wrong FK is a long-tail bug (discovery surfaces mis-index the template).
- **Feature flag decisions** — Reviewer validates coherence with archetype capability. Setting `has_shop=True` on a non-commerce archetype is a reviewer-catchable error.
- **Price tier assignment** — Reviewer validates via cluster blueprint rationale. Random premium/standard assignment is not allowed.
- **Merge to `phase-integration-baseline-v15`** — always Phase Lead. No direct push without review.
- **Adding a new archetype** — out of scope for X.3/Wave 2 entirely. Requires a separate structural phase opened by Phase Lead with explicit D-099 amendment.
- **Touching `apps/editor/`, `apps/projects/`, `apps/commerce/`, `templates/live_templates/`, `static/editor/`** — never. D-099 program closure binding.

---

## 8 · Style consistency across 52 clusters

Running 52 cluster blueprints in parallel (potentially across many sub-agents) risks stylistic drift. Mitigations:

1. **Boilerplate first** (Commit 1): every cluster blueprint uses the same section structure from `cluster_blueprints/_TEMPLATE.md`. A blueprint missing a section fails review.
2. **Glossary convergence** (Commit 2+): terms that appear across multiple clusters in the same macro-category are lifted into `glossaries/<macro>.md`. Cluster blueprints reference the glossary rather than redefining.
3. **Tone band per macro-category**: `business` cluster blueprints share a corporate-institutional tone range; `restaurant` cluster blueprints share a warm-editorial range; `medical` shares a clinical-trustworthy range. Extreme tone swings (tech-hype on a medical cluster) fail D-054 and review.
4. **Style cross-references**: every cluster blueprint names 2-3 sibling clusters it should feel adjacent to (for tone) and 2-3 it must feel distinct from (for differentiation).
5. **Quarterly convergence sweep**: Phase Lead reviews all cluster blueprints once per quarter for drift. Minor edits rolled into a single "factory consistency" commit.

---

## 9 · Throughput & bottlenecks

Expected bottleneck: **Imagery Curator step**. Plan accordingly.

- **Target**: 2 clusters curated per day (1 curator · realistic)
- **Parallel capacity**: 2-3 curators → 4-6 clusters/day
- **Wave 2 pilot (10 templates)**: imagery packs ready in ~5 calendar days with 2 curators
- **Wave 2 full (60 templates to reach 80 total)**: ~10-15 calendar days with 3 curators, assuming no rework

**De-risking**:
- Pre-stage 20+ imagery packs in `imagery/packs/` before Wave 2 launches (Commit 3 of X.3 covers the first 10).
- Encourage curators to batch by macro-category (a `medical` curator curates 5-6 medical clusters in a row, reusing vetted URLs across clusters within reasonable variance).

---

## 10 · Handover signals

X.3 is **complete** when:

- All 9 files in `docs/content-factory/` exist and are reviewed (Commit 1 target)
- 10 pilot cluster blueprints are filled out (Commit 2 target)
- 10 imagery packs are curated + validated (Commit 3 target)
- Related-templates selector helper landed (Commit 4 target)
- NOT NULL flip migration landed (Commit 5 target · piggyback)

X.4 Wave 2 authoring can open when X.3 is complete. X.3 itself does not author any new template.

---

**End of runbook. This document is binding for all Wave 2+ authoring. Deviations require Phase Lead sign-off documented in the PR description.**
