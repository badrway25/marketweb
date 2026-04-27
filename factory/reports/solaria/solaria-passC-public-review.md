# Solaria · Pass C public-review readiness

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching · **Pass**: C
**Date**: 2026-04-27 · **Run-ISO**: `20260427T1000Z`
**Branch**: `phase-x4-solaria-passB-multilingual` (Pass C edits sit atop tip
`24fdde5` in the working tree; this report is written from the same tree
the verification ran against).
**Author**: Claude (Opus 4.7) · plain-language honest read.
**Audience**: project owner, deciding whether Solaria is ready for review
and whether the public-flip cascade should run now or later.

This document does ONE job: answer the four questions the alignment
reset and the user prompt put on the table.

1. Is Solaria still wrongly dependent on staff-gated preview?
2. What review path should be used now?
3. Is Solaria genuinely review-ready for a human stakeholder?
4. Should the tier/cascade flip happen now or later?

The rest of the file is the evidence behind the four answers.

---

## 1 · One-line verdict

**Solaria is review-ready as a draft. The staff-preview path is now
legitimate (not accidental). Public flip is held — by user instruction
and by honest read of the evidence.**

| Question | Answer |
|---|---|
| Wrongly dependent on staff-gated preview? | **No** — the staff path is now the deliberate review path. The wrongness Pass B left behind (broken nav inside a staff session) is fixed. |
| What review path should be used? | **Staff login + `?preview=1` on the Solaria home URL**, then click freely. All 5 locales × 5 pages now reachable in one session. |
| Review-ready for a human stakeholder? | **Yes**, by a stakeholder holding the staff credentials in §6 below. |
| Tier/cascade now or later? | **Later, on user authorization.** Cascade documented to the line in `release-gatekeeper.md §4`. Not auto-forced. |

---

## 2 · Why Pass C existed (the gap Pass B left behind)

After Pass B, Solaria had 5 authored locales rendering correctly when
each URL was typed by hand. But the *review path* was technically
broken: a stakeholder opening the staff-gated home with `?preview=1`
and then clicking any link — language switcher pill, in-page nav,
footer privacy/cookie/legal, mp-back, the case-study row tiles —
silently dropped `?preview=1` and 404'd on the next click. Solaria's
draft tier means the URL only resolves with `?preview=1`; without the
flag the request hits the tier gate (D-055) and 404s.

In practice that meant: a reviewer could see exactly the home page they
typed by hand, and nothing else. Staff-gated review was a useless
surface for actual stakeholder review. The alignment reset (§4) had
already flagged this risk: *"It becomes not acceptable if [staff-
gating] starts to replace the real review flow."* Pass C closes the
technical legitimacy gap so a single staff session is enough to walk
the whole template.

This was not foreseen during Pass A or Pass B because both were
verified by typing each URL by hand into Playwright. A real reviewer,
clicking through the site as a visitor would, finds the broken path
immediately — which is exactly the failure mode the alignment reset
warned was the next likely drift.

---

## 3 · What changed (the minimal correct fix)

8 files, 41 + / 25 - lines.

### 3.1 Source code (review-path legitimacy · 7 files)

```
apps/catalog/views.py                                           (+13/-1)
templates/live_templates/business/corporate-suite/_base.html    (+10/-10)
templates/live_templates/business/corporate-suite/about.html    (+1/-1)
templates/live_templates/business/corporate-suite/case_study_detail.html (+2/-2)
templates/live_templates/business/corporate-suite/case_study_list.html   (+2/-2)
templates/live_templates/business/corporate-suite/home.html     (+5/-5)
templates/live_templates/business/corporate-suite/services.html (+1/-1)
```

In `apps/catalog/views.py` (`LiveTemplateView`):

- `setup()` now stores `self.staff_preview = _staff_preview_mode(request)`
  instead of computing the bool inline only for the tier gate.
- `get_context_data()` exposes `ctx["staff_preview"]` so the corporate-
  suite skin can read it. No new symbols, no new imports.

In the 6 corporate-suite chrome templates, every internal `?lang=`
href builder grew a sibling `&preview=1` clause. Pattern:

```django
{# before #}
{% if locale != default_locale %}?lang={{ locale }}{% endif %}

{# after #}
{% if locale != default_locale %}?lang={{ locale }}{% if staff_preview %}&preview=1{% endif %}{% elif staff_preview %}?preview=1{% endif %}
```

20 occurrences replaced with the same 3-clause conditional, across
nav · language switcher · footer pages · footer legal · in-page CTAs ·
mp-back to template detail · mp-back to category listing ·
case-study row tiles · breadcrumb · next-case.

**Strict-superset property**: when `staff_preview` is False (which is
*every* request from a non-staff user, *every* request to a
`published_live` template, and *every* request that didn't carry
`?preview=1`), the rendered href is byte-identical to before. Pragma
and Fiscus pages (both `published_live`) render zero `&preview=1`
hrefs after the fix — verified live.

### 3.2 Registry honesty (1 file)

`TEMPLATE_REGISTRY.json` was carrying stale Pass-A metadata:
`locales: ["it"]` and `rtl: false`, even though Pass B authored all 5
locales and Arabic RTL is functioning. Pass C corrects:

```json
"locales": ["it", "en", "fr", "es", "ar"],
"rtl": true,
```

`tier` stays `"draft"` on purpose. The `tier_reason` paragraph was
rewritten to consolidate the Pass A + Pass B + Pass C narrative into
one passage.

### 3.3 What Pass C explicitly did NOT change

- **No tier flip.** Solaria stays `draft`. Public count remains 21 / 22.
- **No edits to `apps/editor`, `apps/projects`, `apps/commerce`.** Hard
  constraint from the user prompt.
- **No archetype CSS edits.** Zero changes to `.cs-*` rules in `_base.html`.
- **No new templates, no new imagery, no new locale trees, no new tests.**
- **No edits to homepage / discovery facets / listing card.** Those are
  Pass D territory.

---

## 4 · Why this is the minimal correct review path

Three options were considered before settling on this fix.

### Option A · Flip Solaria to `published_live` and skip Pass C

Lets the reviewer use a real anonymous walk. Rejected because the user
prompt says explicitly *"do not auto-force published_live"* and the
alignment reset says public flip is a *decision*, not a side-effect of
multilingual completion.

### Option B · Add a staff cookie that auto-includes `?preview=1`

Lets the reviewer omit the flag entirely. Rejected because (a) it
changes the tier-gate semantics globally, not just for Solaria — risky
when 21 other templates depend on the gate; (b) it would be a true
backdoor where today's behaviour is a deliberate one-flag opt-in;
(c) it pushes complexity into the request middleware where the
problem is actually local to one skin's hrefs.

### Option C · Propagate the flag explicitly through internal hrefs (the chosen fix)

- The flag is already there if you have it (the URL bar carries it).
- The fix only carries it forward for *staff* requests on *draft*
  templates — i.e., exactly the population Pass C targets.
- The fix is a strict superset of the prior behaviour for the other 21
  templates.
- The fix lives in 6 chrome files + 2 view lines. No middleware. No
  cookie. No global semantics change.

Option C is the smallest change that fixes the named problem without
changing anything else.

---

## 5 · Live evidence (what was actually checked in the browser)

Captures live at `factory/reports/browser-verification/solaria-passC-public-review/20260427T1000Z/`.
The browser walk narrative lives in
`factory/reports/browser-verification/solaria-passC-public-review.md`.

### 5.1 The 11/11 internal-href check

From the IT home opened with `?preview=1` in a staff session, fetch
every internal Solaria-bound href on the page:

```
solaria-coaching/?preview=1                        → 200
solaria-coaching/preview/?preview=1                → 200
solaria-coaching/preview/?lang=en&preview=1        → 200
solaria-coaching/preview/?lang=fr&preview=1        → 200
solaria-coaching/preview/?lang=es&preview=1        → 200
solaria-coaching/preview/?lang=ar&preview=1        → 200
business/?preview=1                                → 200
solaria-coaching/preview/il-coach/?preview=1       → 200
solaria-coaching/preview/percorsi/?preview=1       → 200
solaria-coaching/preview/casi/?preview=1           → 200
solaria-coaching/preview/contatti/?preview=1       → 200
```

11/11 → 200. Before the Pass C edits applied, the same 11 hrefs
returned 9 × 404 + 2 × 200 (only the home itself + the marketplace
back-link worked). Pass C lifted the count from 2 → 11.

### 5.2 The "no leak to public" gate check

Same authenticated session, omitting `?preview=1`:

```
GET /templates/business/solaria-coaching/preview/         → 404 ✓
GET /templates/business/solaria-coaching/                 → 404 ✓
```

Anonymous (no cookies) probes — a real visitor:

```
GET /                                              → 200, "21+" still in body
GET /templates/business/                          → 200, no Solaria card
GET /templates/business/solaria-coaching/         → 404
GET /templates/business/solaria-coaching/preview/ → 404
GET /templates/business/solaria-coaching/preview/?preview=1 → 404
                                                   (anonymous can't be staff)
GET /templates/business/solaria-coaching/preview/?lang=ar&preview=1 → 404
```

The fix only carries the flag forward when it was already explicitly
opted into by a logged-in staff user. It does not relax the gate.

### 5.3 The strict-superset check (Pragma + Fiscus regression sweep)

Pragma is `published_live`. Pulled live from its IT home rendered in
the same session: 26 internal Pragma-bound hrefs · 0 carry
`preview=1` · 26 carry no preview flag at all.

Pass C is a no-op for Pragma + Fiscus. No regression on the 21
`published_live` templates.

### 5.4 Per-locale identity (preserved from Pass B)

| Locale | dir | h1 | h1 font | overflowPx | banned hits |
|---|---|---|---|---|---|
| it | ltr | "Il coaching non è terapia e non è consulenza." | Fraunces | 0 | 0 |
| en | ltr | "Coaching is not therapy, and not consultancy." | Fraunces | 0 | 0 |
| fr | ltr | "Le coaching n'est ni une thérapie, ni du conseil." | Fraunces | 0 | 0 |
| es | ltr | "El coaching no es terapia, ni es consultoría." | Fraunces | 0 | 0 |
| ar | **rtl** | "التدريب ليس علاجاً نفسياً، وليس استشارة." | Noto Kufi Arabic | 0 | 0 |

Same as Pass B. Reproduced live in this pass to certify Pass C did not
silently re-route any page through a different content tree.

---

## 6 · How to review Solaria yourself (5-minute walk)

```bash
# 1. Server is already running. Open a private window so you can also
#    confirm the anonymous gate.
http://127.0.0.1:8731/

# 2. Log in as the staff QA user.
http://127.0.0.1:8731/account/login/
   user: solaria_qa_staff
   pass: solariapassA2026

# 3. Open Solaria home (Italian) with the preview flag.
http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1

# 4. Click — do not edit the URL bar — through every internal link:
#    · language switcher pills (IT → EN → FR → ES → AR)
#    · in-page nav links (Studio · Il Coach · Percorsi · Casi · Contatti)
#    · footer privacy / cookie / legal triplet
#    · mp-back ("← Studio successivo" · "Altri studi business")
#    · case-study row tiles (3 rows)
# Every click should land on a 200 page that renders correctly.

# 5. Compare against the two corporate-suite siblings:
http://127.0.0.1:8731/templates/business/pragma-corporate-suite/preview/
http://127.0.0.1:8731/templates/business/fiscus-commercialista/preview/
# Note: these are published_live, so no `?preview=1` is needed and no
# preview flag appears in any of their internal hrefs (strict superset).

# 6. To confirm the gate is intact, open in a separate private window:
http://127.0.0.1:8731/templates/business/                  # no Solaria card
http://127.0.0.1:8731/templates/business/solaria-coaching/ # 404
http://127.0.0.1:8731/                                     # trust counter says 21+
```

If steps 4 and 6 both work as described — staff session reaches
everywhere, anonymous session sees nothing — the review path is
legitimate.

---

## 7 · Honest residuals (load-bearing list)

These are claims this pass explicitly does NOT make. Honest restraint
matters more than maximalist GREEN.

1. **Public catalog count is now 22.** No. The DB row for
   `solaria-coaching` keeps `tier="draft"`. The homepage trust counter
   still reads "21+". An anonymous visitor going to any Solaria URL
   still gets 404.

2. **Pass C improves design quality.** No. Pass C is a navigation /
   query-string fix and a metadata correctness fix. Visual quality is
   inherited from Pass A (IT distinctness) and Pass B (locale parity);
   re-reviewed live to confirm no regression, but not extended.

3. **All 5 locales × all 5 pages × all 5 viewports were captured this
   pass.** No. Pass C captures 9 surfaces — the 5 locale homes at
   1440, AR percorsi + AR contatti at 1440, AR home at 390 mobile, IT
   home at 1024 tablet. The Pass B run already exercised the deeper
   matrix; Pass C narrows to surfaces that *change reachability* under
   the staff-preview fix, plus a sample to detect any layout
   regression.

4. **An anonymous visitor can review Solaria.** No. An anonymous
   visitor going to any Solaria URL still gets 404. Review requires
   the staff credentials in §6.

5. **The fix touches all archetypes.** No. The fix lives in
   `templates/live_templates/business/corporate-suite/*.html` (6 files)
   plus a 2-line view edit. Other archetypes (medical, lawyer,
   restaurant, real-estate, portfolio, agency, ecommerce, startup-saas,
   fine-dining) are unmodified. The fix benefits any future
   `tier=draft` corporate-suite enrollee transitively but is currently
   visible only on Solaria — Pragma + Fiscus are `published_live` and
   their `staff_preview` is always False.

6. **The hero filter (`grayscale 15% / contrast 1.04 / brightness
   0.97`) was tuned for Solaria's warm carbon-and-ochre palette.** No.
   This is an archetype-level CSS rule shared with Pragma + Fiscus and
   was deliberately not changed. Carried forward verbatim from Pass A
   §2.4 / Pass B §5.4.

---

## 8 · Tier / cascade decision

**HELD pending user authorization.**

The full Pass D cascade is documented to the line in
`factory/reports/scorecard/solaria-passC-public-review/release-gatekeeper.md §4`.
For convenience the diff is summarised here:

```diff
# 8 hardcoded count assertions in apps/catalog/tests.py:
- self.assertEqual(qs.count(), 21)                       (×2)
+ self.assertEqual(qs.count(), 22)
- self.assertEqual(counts["total"], 21)                  (×2)
+ self.assertEqual(counts["total"], 22)
- self.assertEqual(counts["price_tiers"].get("standard"), 8)
+ self.assertEqual(counts["price_tiers"].get("standard"), 9)
- self.assertEqual(counts["features"].get("has_rtl"), 21)
+ self.assertEqual(counts["features"].get("has_rtl"), 22)
- self.assertEqual(counters["templates_live"], 21)
+ self.assertEqual(counters["templates_live"], 22)
- self.assertIn("21+", body)
+ self.assertIn("22+", body)

# 1 line in TEMPLATE_REGISTRY.json:
- "tier": "draft",
+ "tier": "published_live",

# Then:
$ python manage.py sync_template_tiers     # syncs DB row from registry
$ python manage.py test apps.catalog       # 171 OK confirms cascade
```

Why this is **HELD now**:

- The user prompt is explicit: *"do not auto-force published_live"* and
  *"if public readiness is NOT yet justified, do not force it."*
- The alignment reset framed Pass C and Pass D as separate
  authorization steps. Pass C closes the technical legitimacy gap;
  Pass D is the public-flip *decision*, which the user must make after
  walking the Pass C captures and the live server.
- The release-gatekeeper panel of the scorecard
  (`release-gatekeeper.md §1`) is explicit that GREEN here authorises
  *staff-gated stakeholder review* — not the public-flip cascade.

Why this is **READY-WHEN-AUTHORIZED**:

- The cascade is small (8 test edits + 1 registry edit + 1 sync command)
  and fully documented.
- The 5-locale tree is in place; the Pexels imagery pool is clean; the
  archetype contracts are intact; the dark-warm carbon palette passes
  the build-time `corporate_suite.E001` gate.
- All preconditions in `corporate-suite-quality-scorecard.md` for
  review-ready promotion are met.

The decision belongs to the user, not the gatekeeper.

---

## 9 · Final verdict

**Pass C: GREEN for review-ready as draft. HELD for public flip.**

Solaria is now a real reviewable template, in 5 locales, behind a
deliberate staff-preview gate. A non-confused human reviewer holding
the staff credentials in §6 can open the IT home, click everywhere,
and form an opinion on whether Solaria is ready to ship. That is the
deliverable the user prompt asked for.

The next step belongs to the user: walk the captures + the live server,
form a view, and either authorize Pass D (public flip) or hold it for
another iteration.

The agent will not run Pass D unless explicitly told to.

---

*End of Solaria · Pass C public-review readiness report. No `apps/editor`,
`apps/projects`, or `apps/commerce` files were modified to produce this
document. No tier was flipped.*
