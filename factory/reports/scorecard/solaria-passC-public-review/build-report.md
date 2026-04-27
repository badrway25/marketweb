# Solaria · Pass C · build report

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching · **Pass**: C
**Date**: 2026-04-27 · **Run-ISO**: `20260427T1000Z`
**Branch**: `phase-x4-solaria-passC-public-review`
**Voice**: build/CI-style. Plain status, no celebration.

---

## 1 · Outcome

**GREEN** — clean test pass + clean system check + the only modified
behaviour is observably correct in the browser.

| Probe | Result |
|---|---|
| `python manage.py test` | **546 / 546 OK** (158.8 s) |
| `python manage.py test apps.catalog` | **171 / 171 OK** (2.2 s) |
| `python manage.py check` | 1 pre-existing W001 (Pragma Unsplash grandfather); **0 new warnings** |
| `python manage.py check --deploy` | not exercised (dev pass) |

No new unit tests were added. The Pass C edit is a no-op for non-staff
users (`staff_preview` is False everywhere except a logged-in staff
session that explicitly opted into `?preview=1`), and the existing test
suite simulates anonymous and customer users only — so existing tests
neither needed updates nor were silently relaxed by the change.

A regression check on the staff-preview leak is performed live in the
browser (see `browser-verifier.md` §4) by fetching all 11 internal
hrefs from the IT home in the same authenticated session and asserting
all return 200. That check is binary and the live result was 11/11.

---

## 2 · Files changed

8 files, 41 insertions, 25 deletions.

```
TEMPLATE_REGISTRY.json                                                       | 10 +++++++---
apps/catalog/views.py                                                        | 14 +++++++++++++-
templates/live_templates/business/corporate-suite/_base.html                 | 20 ++++++++++----------
templates/live_templates/business/corporate-suite/about.html                 |  2 +-
templates/live_templates/business/corporate-suite/case_study_detail.html     |  4 ++--
templates/live_templates/business/corporate-suite/case_study_list.html       |  4 ++--
templates/live_templates/business/corporate-suite/home.html                  | 10 +++++-----
templates/live_templates/business/corporate-suite/services.html              |  2 +-
```

Breakdown:

- **`apps/catalog/views.py`** — 1 hunk in `LiveTemplateView.setup`
  capturing `self.staff_preview = _staff_preview_mode(request)` (instead
  of computing it inline only for the tier-gate check), and 1 hunk in
  `get_context_data` exposing `ctx["staff_preview"]`. No new symbols,
  no new imports.

- **`templates/live_templates/business/corporate-suite/*.html`** — 20
  occurrences of the same pattern replaced across 6 files. Pattern
  before: `{% if locale != default_locale %}?lang={{ locale }}{% endif %}`.
  Pattern after: same plus a sibling `{% if staff_preview %}&preview=1{% endif %}`
  branch and a fallback `{% elif staff_preview %}?preview=1{% endif %}`.
  The language-switcher inside `_base.html` carries the same shape
  with `entry.code` instead of `locale`.

- **`TEMPLATE_REGISTRY.json`** — 1 stanza for `solaria-coaching`:
  `locales` widened from `["it"]` → all 5 locales, `rtl` flipped from
  `false` → `true`, and the `tier_reason` paragraph rewritten to
  consolidate Pass A + B + C narrative. `tier` itself stays `"draft"`
  on purpose.

No edits to `apps/editor/`, `apps/projects/`, `apps/commerce/`, no new
archetypes, no new templates, no new Python modules.

---

## 3 · Server / process

```
$ python manage.py runserver 127.0.0.1:8731 --noreload
Watching for file changes with StatReloader
Performing system checks...
… (1 W001 grandfather warning, pre-existing)
Django version 5.2.7, using settings 'marketweb.settings'
Starting development server at http://127.0.0.1:8731/
Quit the server with CTRL-BREAK.
```

Server stays up at `http://127.0.0.1:8731/` for the user's own walk.

---

## 4 · Imagery policy gate

`corporate_suite.E002 / E003` build-time imagery checks remain silent
on `solaria-coaching`. Pass A's 6-URL Pexels pool stays the only image
source. No imagery URLs were added, modified, or removed.

`corporate_suite.W001` continues to fire on `business-corporate`
(Pragma) — this is a documented archetype-level grandfather under
`LEGACY_EXEMPT_KEYS` and is not a Solaria concern.

---

## 5 · Migration / DB / seed posture

No migrations created, no schema changes, no seed-templates changes.
The DB row for `solaria-coaching` keeps `tier="draft"` — confirmed
post-pass:

```
total objects: 22
published_live: 21
draft: 1
solaria-coaching → tier=draft
```

The public catalog count (21) is unchanged from Pass B.

---

## 6 · Lint / static-analysis

Not exercised by this pass — Pass C does not introduce Python logic
beyond a 2-line view edit. The template edits are template-language
only, no Python or JS code paths added.

---

## 7 · What "GREEN" means here

Pass C's GREEN means three things and only three things:

1. The test suite still passes (546/546).
2. `manage.py check` reports no new warnings (only the pre-existing
   Pragma W001).
3. The single behavioural change introduced (staff-preview flag
   propagation on internal hrefs in corporate-suite templates) was
   verified live in the browser to do exactly what the docstring
   claims, and to be a strict no-op for every non-staff or non-draft
   request shape (live regression check in `browser-verifier.md`).

GREEN does **not** mean Solaria is approved for public flip. The flip
cascade is held under separate user authorisation per
`release-gatekeeper.md`.
