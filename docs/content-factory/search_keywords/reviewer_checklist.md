# Search Keywords · Reviewer Checklist

**Status**: 1-page, compact, reviewer-usable at merge time. Pairs with `AUTHORING_CONTRACT.md`.

**Use**: open the template PR, find the `search_keywords` value (on the template model instance or in the seed registry). Run through the checklist. Every box must be checked.

---

## Quick pass

- [ ] **Token count**: 6 ≤ count ≤ 14 (whitespace-separated)
- [ ] **Lowercase**: all tokens lowercase, accents preserved
- [ ] **IT-first**: at least 60% of tokens are Italian (non-IT acronyms like `ip`, `gdpr`, `smart-working` allowed if industry-native)
- [ ] **No commas, pipes, or other separators** between tokens
- [ ] **Compound words use hyphen**: `fine-dining`, `studio-legale`, `dichiarazione-redditi` (not `fine dining`)

---

## Content check

- [ ] **3-6 core terms** identifiable (profession name + 2-3 distinguishing features)
- [ ] **0-8 alias terms** complementing the core
- [ ] **No stop-words**: `il`, `lo`, `la`, `di`, `a`, `in`, `per`, `con`, `su`, `tra`, `fra`, `e`, `o`
- [ ] **No superlatives without evidence**: `migliore`, `top-1`, `#1`, `leader`, `eccellente`, `premier`, `autentica`
- [ ] **No generic adjective stuffing**: `professionale`, `serio`, `affidabile`, `innovativo`, `moderno` × 3+
- [ ] **No repetition**: same root token does not appear twice (`pizza pizzeria pizze` = violation)
- [ ] **No competitor brand hijack**: `wordpress`, `wix`, `shopify`, `squarespace`, `cognome-concorrente-diretto`
- [ ] **No trademark misuse**: `michelin` only if the brand has or aims for a star factually; similar for any protected mark

---

## Geo / locale check

- [ ] **Geo-neutral by default**: no city/region tokens (`roma`, `milano`, `toscana`, `sicilia`) UNLESS the template's positioning is explicitly geo-locked (e.g. `dermatologia-elite-roma`). Geo inclusion is justified in the PR description.
- [ ] **IT-first**: the value is written for Italian discovery first. English/French synonyms appear only when profession uses them natively.

---

## Alignment check

- [ ] **Cluster blueprint alignment**: open `docs/content-factory/cluster_blueprints/<cluster>.md` §7 "Search keywords pack". The template's `search_keywords` draws from this pack + adds brand/template-specific terms. Pure misalignment (e.g. a `fine-dining` template with `artisan maker` keywords) flagged.
- [ ] **Cluster search_aliases not duplicated wholesale**: the template-level `search_keywords` is not a copy of the cluster's `ProfessionCluster.search_aliases`. The split is: cluster alias captures profession-wide terms; template keywords capture brand + niche.
- [ ] **No locale-split**: `search_keywords` is a single IT-first string, not 5 locale variants. Locale-split only with Phase Lead approval for genuinely geo/locale-locked cases.

---

## Smoke

- [ ] **Typeahead match verification**: after merge, `/templates/search/typeahead/?q=<one-core-keyword>` returns this template in the templates pool. Quick Playwright or `curl` check.
- [ ] **Facet filter verification**: `/templates/?cluster=<cluster>` still returns this template (confirms cluster FK coherent).

---

## Reject conditions (hard)

If any of these hits, reject with a citation to the rule and request rework:

- ❌ Count < 6 or count > 14
- ❌ Any stop-word present
- ❌ Repetition of the same root
- ❌ Superlative / generic-adjective stuffing visible
- ❌ Competitor brand mention
- ❌ Commas / pipes / uppercase
- ❌ Zero IT tokens (all English/other)

---

## Remand format

If rework is needed, reviewer writes ONE sentence in the PR:

> ❌ `search_keywords` fails rule §5 item N (AUTHORING_CONTRACT.md): `<short reason>`. Example fix: `<short example>`.

Author rework + re-request review. No multi-round negotiation — the rules are explicit.

---

## Green format

If pass, reviewer writes:

> ✅ `search_keywords` ok · `<n>` tokens · IT-first · cluster-aligned.

Merge.

---

**End of reviewer checklist. Binding for Wave 2+ template PRs.**
