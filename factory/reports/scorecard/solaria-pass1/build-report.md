# build-report · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` · category `business` · archetype `corporate-suite`
**Run-ISO**: `20260426T0907Z`
**Branch**: `phase-x4-solaria-controlled-reentry-pass1` · forked from hardening tip `075e623` (post Step 2E P1E final GO).
**Reporter**: Claude (Opus 4.7) acting as `template-builder`.

---

## §1 · Source state at intake

Solaria entered pass 1 as the paused two-commit Wave 2 Pilot #2 trail on `phase-x4-wave2-solaria-coaching-v1`:

- `e8f38b5` · Commit A: solaria-coaching draft (IT-only, ~935 LOC content tree, ORIGINAL CREAM PALETTE `#F7F3EC` — known-bad).
- `6b70d56` · Commit B (palette polarity fix): swap to dark-foreground `#2B2A28 / #C8621A / #8B5A2B` AFTER live walk diagnosed cream-on-cream rendering. **This is the source of truth for Solaria's palette in pass 1.**

The Solaria branch was NOT rebased into the hardening branch during the X.4a cycle (R-SOL-2 binding throughout). Pass 1 re-introduces the Solaria infrastructure as fresh additions on the controlled-reentry branch, NOT via merge / cherry-pick — the hardening cycle's two new modules (`apps/catalog/checks.py`, `apps/catalog/imagery_policy.py`, plus `theme_safety.py` extensions) had not existed at Commit A authoring time.

## §2 · Files re-introduced (Solaria-local delta)

| # | File | Lines | Status |
|---|---|---:|---|
| 1 | `apps/catalog/template_content_solaria.py` | 949 | NEW · IT content tree from `e8f38b5` |
| 2 | `apps/catalog/template_content.py` | +10 | M · import + register slug→content dict entry |
| 3 | `apps/catalog/preview_imagery.py` | +20 | M · `business-coaching` 6-URL Pexels pool |
| 4 | `apps/catalog/template_dna.py` | +65 | M · `solaria-coaching` DNA on `corporate-suite` |
| 5 | `apps/catalog/management/commands/seed_templates.py` | +75 | M · TEMPLATE_METADATA + SEED_TEMPLATES (post-fix palette) |
| 6 | `apps/catalog/tests.py` | +2 | M · solaria-coaching in `booking_slugs` |
| 7 | `TEMPLATE_REGISTRY.json` | +~30 | M · Solaria entry · tier=draft · post-fix palette |

Total: **~1150 lines added** (947 of which are the IT content tree). Zero deletions. Zero edits to `apps/editor`, `apps/projects`, `apps/commerce`, `apps/catalog/views.py`, `apps/catalog/urls.py`, `apps/catalog/models.py`, `apps/catalog/migrations`, or any skin-folder template (B3 + B4 + B7 honored).

## §3 · Builder L\* self-check (CIELAB)

Solaria primary `#2B2A28` analyzed against the canonical cream paper `#F7F4EC`:

- WCAG relative luminance: **0.024**
- L\* (CIE Lab): **≈ 17.2**
- Contrast ratio vs cream: **12.56 : 1** — AAA body (≥ 7.0 floor).
- Δ L\* vs cream paper (L\* ≈ 96.5): **≈ 79.3** — well above the ≥ 60 archetype floor.

Comparison to Pragma (`#1E293B`, ratio 14.18) and Fiscus (`#1F2937`, ratio 13.22): Solaria sits at the lower contrast end of the three but still above AAA by a comfortable 5+ ratio buffer. **Polarity-fix from Commit A's `#F7F3EC` (ratio 1.07) → Commit B's `#2B2A28` (ratio 12.56) is the load-bearing change** that lets the palette enter the hardened branch at all.

## §4 · CI floor capture

### §4.1 · `manage.py check`

Transcript: `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/check-clean.log`

```
System check identified some issues:

WARNINGS:
business-corporate: (corporate_suite.W001) corporate-suite imagery pool 'business-corporate' is grandfathered under LEGACY_EXEMPT_KEYS and ships 6 non-Pexels url(s) pending AP3 retro-curation. The archetype accepts this; the gatekeeper must cite it explicitly (O7 precondition).

System check identified 1 issue (0 silenced).
```

**Zero `corporate_suite.E001 / E002 / E003` errors.** The single `W001` is the expected Pragma legacy grandfather, NOT Solaria.

### §4.2 · `manage.py test apps.catalog`

Transcript: `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/test-run.txt`

```
Ran 171 tests in 2.438s
OK
```

Catalog distribution after seed: **21 published_live / 1 draft** (the 1 draft = Solaria · expected per pass-1 plan).

### §4.3 · Voice anchor verbatim grep

Solaria IT voice anchor (mandatory blueprint seed): `"Il coaching non è terapia e non è consulenza."`

```
$ grep -n "Il coaching non è terapia e non è consulenza" apps/catalog/template_content_solaria.py
142:        "headline":    "Il coaching non è <em>terapia</em> e non è <em>consulenza</em>.",
```

The home `headline` resolves to `<h1>` text without the `<em>` tags after Django auto-escape, so the live DOM contains the verbatim anchor (verified separately in `browser-verifier.md`).

### §4.4 · Pexels-only grep on `business-coaching` pool

```
$ grep -n "business-coaching" apps/catalog/preview_imagery.py
…
"business-coaching": [
    "https://images.pexels.com/photos/7979456/pexels-photo-7979456.jpeg?auto=compress&cs=tinysrgb&w=1600",
    "https://images.pexels.com/photos/5756579/pexels-photo-5756579.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "https://images.pexels.com/photos/9064347/pexels-photo-9064347.jpeg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/12934369/pexels-photo-12934369.jpeg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/34601/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/31236101/pexels-photo-31236101.jpeg?auto=compress&cs=tinysrgb&w=800",
],
```

**6 / 6 URLs match `images.pexels.com`** in the canonical 6-slot shape. `corporate_suite.E002` (non-Pexels) is silent. `corporate_suite.E003` (canonical shape) is silent. `business-coaching` is NOT in `LEGACY_EXEMPT_KEYS` — Pexels-only is enforced by build-time error, not warning.

### §4.5 · Pragma legacy grandfather (O7) acknowledgment

`corporate_suite.W001` warning surfaces `business-corporate` on every `manage.py check`. The grandfather contract is honored by the build (not silently relied upon). Per **R-SOL-10**, the Solaria scorecard must cite `O7` explicitly — see `release-gatekeeper.md §3.1` and `scorecard.md §6 · E1`.

### §4.6 · D-054 docstring inspection

`apps/catalog/template_content_solaria.py:1-88` — the module docstring at `e8f38b5` already encodes the reciprocal D-054 10-gate triangulation:

- vs Fiscus (10 gates): cluster · visual style · voice anchor · primary CTA · client relation · service unit · credentials · palette · imagery direction · typography
- vs Pragma (10 gates): cluster · price tier · audience · org scale · service unit · voice · primary CTA · visual style · credentials · structure emphasis

Pragma's + Fiscus's docstrings on the hardening tip already triangulate against Solaria-as-placeholder per P1D refresh. **R-SOL-11 satisfied by construction with zero pass-1 docstring edits.**

## §5 · Anti-pattern guardrail grep (blueprint §13)

Source: `apps/catalog/template_content_solaria.py:20-33` lists the 13 forbidden anti-patterns. Each grepped against the runtime DOM at `/templates/business/solaria-coaching/preview/?preview=1`:

| Anti-pattern | DOM hits |
|---|---:|
| `sblocca` | 0 |
| `unlock your potential` | 0 |
| `mindset vincente` | 0 |
| `Einstein` / `Jung` / `Gandhi` / `Steve Jobs` | 0 / 0 / 0 / 0 |
| `mountain peak` | 0 |
| `best version of yourself` / `versione migliore di te` | 0 / 0 |
| `trasforma la tua vita` / `transform your life` | 0 / 0 |
| `lorem ipsum` / `dolor sit amet` | 0 / 0 |

**0 anti-pattern hits across the entire IT walk** (BRWS-FEEL-03 floor met).

## §6 · Builder verdict

**PASS** · all 6 build-side checks (palette, imagery, voice anchor, anti-pattern, D-054 docstring, CI floor) green at the controlled-reentry tip. Solaria is enrolled, build-time gate-passing, and ready for the downstream agent legs (style-critic / contrast / responsive / browser / gatekeeper).

The single `corporate_suite.W001` Pragma grandfather warning surfaces in the transcript per design — the builder is recording it here, not silencing it.
