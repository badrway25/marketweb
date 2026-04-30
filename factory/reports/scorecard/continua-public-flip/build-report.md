# build-report · Continua · Public Flip · 2026-04-30

**Verdict**: GREEN · build clean · cascade applied as documented · zero source / template / HTML edits beyond the 2 required by the workflow D Q5 cascade

---

## 1 · What was built

The pre-flip workflow D pass certified Continua as "release-ready in principle" but withheld the tier flip pending the user parallel-verification handshake. This pass executes the cascade, nothing else.

No new template · no new archetype · no new migration · no new view · no new selector · no new chrome partial · no new SCSS · no new image · no new fixture · no new locale module.

---

## 2 · Source / config edits

| File | Lines touched | Change |
|---|---|---|
| `TEMPLATE_REGISTRY.json` | Continua row (~336–338) | `status: "draft"` → `"published"` · `tier: "draft"` → `"published_live"` · `tier_reason` rewritten to consolidate workflow A → A.5 → B → C → D → public-flip audit trail |
| `apps/catalog/tests.py` | 7 literal swaps · L824 / L862 / L868 / L1134 / L1141 / L1554 / L1556 | All `22` → `23` (and `"22+"` → `"23+"`) on the explicit-literal public-count assertions per `DECISIONS.md` "literal-counts beat dynamic `len()` in public-count tests" rationale |

That's it. Two files touched. No `apps/editor/`, no `apps/projects/`, no `apps/commerce/`, no `apps/catalog/views.py · selectors.py · models.py`, no `templates/**`, no DNA, no imagery_pool, no theme_safety.

---

## 3 · Why the trust counter required no template / view edit

`apps/pages/views.py:94` already binds:

```python
ctx["trust_counters"] = {
    "templates_live": WebTemplate.objects.filter(
        tier=WebTemplate.Tier.PUBLISHED_LIVE
    ).count(),
    ...
}
```

…and `templates/pages/home.html:32` and `:170` consume it as `{{ trust_counters.templates_live }}+`. So the moment `sync_template_tiers` lifted Continua's DB row from `DRAFT` to `PUBLISHED_LIVE`, the rendered string transitioned `22+` → `23+` automatically. Verified live in §5.

This is the same dynamic-counter binding Pragma's S22 / Solaria's Pass D also relied on. No 1-character edit to any HTML was needed (workflow D §2 Q5 acknowledged this with "Check before editing — the registry-derived path may already be authoritative").

---

## 4 · Management command output

```
$ python manage.py sync_template_tiers
System check identified some issues:

WARNINGS:
business-corporate: (corporate_suite.W001) corporate-suite imagery pool
'business-corporate' is grandfathered under LEGACY_EXEMPT_KEYS and ships
6 non-Pexels url(s) pending AP3 retro-curation. The archetype accepts
this; the gatekeeper must cite it explicitly (O7 precondition).
  continua-stewardship: draft -> published_live

1 tier(s) updated. Catalog distribution: 23 published_live / 0 draft.
```

The `corporate_suite.W001` advisory is the same warning every prior corporate-suite pass has shown; it's the AP3 retro-curation backlog (legacy `business-corporate` imagery pool grandfather) and is unchanged by this flip. Cited per the O7 precondition contract — not a flip blocker.

Single row updated. No collateral writes. Distribution lands at the documented post-flip target: **23 published_live / 0 draft**.

---

## 5 · Live trust counter sanity

```
$ curl -sS http://127.0.0.1:8052/ | grep -oE 'mw-home-trust-n[^>]*>[^<]+'
mw-home-trust-n">23+        ← templates_live
mw-home-trust-n">15         ← categories_active
mw-home-trust-n">52         ← clusters_active
mw-home-trust-n">5          ← locales_supported
```

Confirms the dynamic counter did inherit the DB tier flip without a view / template edit.

---

## 6 · Build hygiene

- **Static files**: no static asset added or removed; `collectstatic` not required.
- **Migrations**: zero generated; the flip is data-only on an existing field with an existing index.
- **Translations**: zero touched; locale modules carry rendered content per the corporate-suite registry pattern, no `.po` involved.
- **Linter**: no new code paths; ruff / black surface area unchanged from pre-flip.

---

## 7 · Scope guardrails — verified

- `apps/editor/**` UNTOUCHED
- `apps/projects/**` UNTOUCHED
- `apps/commerce/**` UNTOUCHED
- `apps/catalog/template_content_continua*.py` UNTOUCHED (5 locale modules)
- `apps/catalog/views.py · selectors.py · models.py · imagery_pool.py · theme_safety.py` UNTOUCHED
- `templates/live_templates/business/corporate-suite/**` UNTOUCHED
- `templates/pages/home.html` UNTOUCHED
- DNA registry · seed command · migrations UNTOUCHED
- No new archetype / template / migration

---

## 8 · Verdict

**GREEN.** Build is clean, cascade is minimal-and-complete, scope is tight, sync_template_tiers reports the documented 23/0 split, the trust counter inherits the new value without code change, and the only test churn is the 7 explicit-literal public-count tripwires that exist exactly to be flipped on a Wave-2 merge like this one.
