# Summary · Cornice · workflow C multilingual

```yaml
phase:        X.5 Cornice · workflow C (multilingual rollout)
date:         2026-05-01
verdict:      GREEN · review-ready · workflow D held for user-handshake
agent_role:   workflow-c-multilingual-builder
```

## What shipped

Cornice (5th corporate-suite sibling · 1st LF-2 occupant) goes from
1 locale (it) to **5 locales** (it · en · fr · es · ar) on top of
the locked LF-2 IT shape (A.6 review-lock).

- **4 new content modules** (template_content_cornice_{en,fr,es,ar}.py)
  · ~4,360 new lines · same keys as CORNICE_CONTENT_IT, only values
  translated.
- **3 minimal wiring edits**:
  - `template_content.py` — 4 new imports + 4 dict entries flipped
    from IT-fallback to per-locale modules.
  - `_base.html` — added `Noto+Naskh+Arabic` to the `is_rtl` font
    import + a 6-line `--heading` override scoped to `body.cs-lf-lf-2`
    (planner-brief §11 decision realised).
  - `TEMPLATE_REGISTRY.json` — locales `[it]` → `[it,en,fr,es,ar]` ·
    `rtl: false` → `rtl: true` · `tier_reason` rewritten · `tier:
    "draft"` preserved.

## Voice anchor verbatim-in-translation

| Locale | Voice anchor | Em-noun |
|---|---|---|
| IT | `Ogni progetto è un argomento costruito, non un servizio reso.` | argomento |
| EN | `Every project is a built argument, not a service rendered.` | argument |
| FR | `Chaque projet est un argument construit, non un service rendu.` | argument |
| ES | `Cada proyecto es un argumento construido, no un servicio prestado.` | argumento |
| AR | `كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة.` | حُجَّة |

The phrase recurs verbatim on hero h1 + CTA-closer h2 in every locale
(2-surface verbatim recurrence preserved across all 5).

## AR Naskh-vs-Kufi (planner-brief §11 resolved)

The cluster default for Arabic is Noto Kufi Arabic on headings, used
by every existing AR-RTL skin. LF-2's editorial register favours
humanist Naskh forms (Casabella/Domus/Architectural Review style),
not Kufi geometry (Pictet/family-office style). Workflow C ships
Cornice AR with **Noto Naskh Arabic** on headings, **Amiri** on body,
selector-scoped to `body.cs-lf-lf-2` so every other RTL skin
(Continua AR, Solaria AR, Pragma AR, Fiscus AR) keeps Kufi
unchanged.

Verified live:
- Cornice AR: `--heading: "Noto Naskh Arabic", "Cormorant Garamond",
  Georgia, serif`
- Continua AR (LF-5): `--heading: "Noto Kufi Arabic", "Crimson Pro",
  Georgia, serif` (no leakage)

## Walk + frozen-sibling regression

5-locale walk via Playwright MCP (mandatory per task constraints)
across 9 routes × 5 locales. 11 captures saved.

Frozen siblings: 4 × 5 locales = 20 anonymous routes — all 200, no
chrome regression, no font leakage. Continua AR walk verified live
to keep Noto Kufi Arabic.

## Tier + test suite

`tier: "draft"` preserved. Public catalog count unchanged (23
published_live + 1 draft = 24).

Test suite: 546 tests, 545 pass, 1 pre-existing failure
(`test_medical_and_restaurant_templates_have_booking_flag` ·
Continua-related · documented in v15 baseline as not Cornice-
related). Same outcome as A.6 review-lock.

## Server / URL handed back

- Server: `python manage.py runserver 8052 --noreload`
- URL: `http://127.0.0.1:8052/`
- Auth: `cornice_review` · `cornice-review-password` · staff +
  superuser
- Routes: 9 staff-preview routes × 5 locales = 45 reachable with
  `?preview=1` and `?lang=xx`
- Tier: `draft` (anonymous: 404 · staff: 200)

Server stays open for the user-handshake review.

## Locale-pointer pages

- IT home: `/templates/business/cornice-architettura/preview/?preview=1`
- EN home: `/templates/business/cornice-architettura/preview/?lang=en&preview=1`
- FR home: `/templates/business/cornice-architettura/preview/?lang=fr&preview=1`
- ES home: `/templates/business/cornice-architettura/preview/?lang=es&preview=1`
- AR home: `/templates/business/cornice-architettura/preview/?lang=ar&preview=1`

## Verdict

**GREEN · review-ready.** All constraints met:
- LF-2 preserved exactly (zero edits to layout files)
- voice anchor preserved verbatim
- AR handled with explicit Naskh decision + RTL parity verified
- frozen siblings 0/4 regression
- distinctness 5/5 axes × 5 locales = 25/25
- test suite holds
- tier=draft preserved

If user signals **GO** → workflow D (public flip + cascade).
If user signals **HOLD on a locale** → narrow re-author of that
locale module.
