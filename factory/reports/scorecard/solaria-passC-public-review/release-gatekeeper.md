# Solaria · Pass C · release gatekeeper

**Voice**: release gatekeeper. Holds the line on what GREEN actually
authorises.

**Reference**: `factory/standards/corporate-suite-blocking-rules.md`,
`factory/standards/corporate-suite-quality-scorecard.md`,
`factory/reports/solaria/solaria-alignment-reset.md` (the user-facing
plain-language read).

---

## 1 · The decision the gatekeeper has to make

Pass C's GREEN authorises **review-readiness as a draft template**.

It does NOT authorise:

- the public-flip cascade (`tier: draft → published_live`),
- the homepage trust-counter increment (21 → 22),
- the public-listing card surface,
- the discovery-facet exposure,
- the anonymous-visitor walk that the alignment-reset framed as the
  Pass-C-after-Pass-C deliverable.

Those five are bundled into a single deliberate authorisation step
named here as **Pass D · public flip**. The gatekeeper is explicit
that Pass D is held until the user looks at the Pass C captures and
review-path walkthrough personally and authorises the flip.

This is not the gatekeeper being conservative for its own sake. It is
the alignment-reset's own §4 read: "It becomes not acceptable if
[staff-gating] starts to replace the real review flow." Pass C closes
the *technical* legitimacy gap of the staff-gated review path; the
*decision* of whether staff-gated review is enough or whether the
user wants the public surface is — by the alignment-reset's own logic
— a user decision, not a gatekeeper decision.

---

## 2 · What the Pass C scorecard returns GREEN on

| Panel | Verdict | Evidence |
|---|---|---|
| build-report.md | GREEN | 546/546 tests, 1 W001 unchanged |
| style-critic.md | GREEN | no visual regression; image-rhythm preserved |
| contrast-accessibility.md | GREEN | AAA pairs preserved, focus order unchanged |
| responsive-auditor.md | GREEN | overflow 0 / -15 at 1440 / 1024 / 390 |
| browser-verifier.md | GREEN | 11/11 internal hrefs → 200 from staff session |

These five panels deliver the answer to the alignment-reset's
"reviewable by a human stakeholder?" question: **yes, by a stakeholder
holding the staff credentials in `summary.md` §6.**

---

## 3 · What the Pass C scorecard does NOT return GREEN on

| Item | Status | Why it isn't GREEN here |
|---|---|---|
| Public-tier flip | **HELD** | User authorisation pending; cascade described in §4 below |
| `templates_live == 22` | **NOT FLIPPED** | DB row still `tier=draft` |
| Public listing card | **NOT VERIFIED** | Card not rendered while `tier=draft`; verifying requires the flip |
| Anonymous walk | **NOT POSSIBLE** | Solaria 404s for non-staff; flip is a precondition |
| Discovery-facet surface | **NOT REACHABLE** | Same — facet count includes only published_live |

The release-gatekeeper does not pretend these items are GREEN. It
classifies them as **HELD pending Pass D authorisation**. The phrase
"Solaria is approved for release" should not be used about Pass C; the
correct phrase is "Solaria is approved for staff-gated stakeholder
review."

---

## 4 · The Pass D cascade, documented to the line

For when the user authorises the flip. This is a small, well-defined
diff that should be in its own commit on its own branch.

### 4.1 Test-file edits

```diff
# apps/catalog/tests.py

- self.assertEqual(qs.count(), 21)                          # line 822
+ self.assertEqual(qs.count(), 22)

- self.assertEqual(counts["total"], 21)                     # line 860
+ self.assertEqual(counts["total"], 22)

- self.assertEqual(counts["price_tiers"].get("standard"), 8) # line 865
+ self.assertEqual(counts["price_tiers"].get("standard"), 9)

- self.assertEqual(counts["features"].get("has_rtl"), 21)   # line 866
+ self.assertEqual(counts["features"].get("has_rtl"), 22)

- self.assertEqual(counters["templates_live"], 21)          # line 1132
+ self.assertEqual(counters["templates_live"], 22)

- self.assertIn("21+", body)                                # line 1139
+ self.assertIn("22+", body)

- self.assertEqual(qs.count(), 21)                          # line 1552
+ self.assertEqual(qs.count(), 22)

- self.assertEqual(counts["total"], 21)                     # line 1554
+ self.assertEqual(counts["total"], 22)
```

8 lines.

### 4.2 Registry flip

```diff
# TEMPLATE_REGISTRY.json (solaria-coaching block)

- "tier": "draft",
+ "tier": "published_live",
```

1 line.

### 4.3 Sync DB tier from registry

```bash
python manage.py sync_template_tiers
```

The command is established (used during X.4a step2 for the wave-1
seed). It reads `TEMPLATE_REGISTRY.json` and updates the `WebTemplate`
rows in the DB.

### 4.4 Verify post-flip

The user opens
`http://127.0.0.1:8731/templates/business/` as an anonymous visitor and
sees Solaria's card alongside Pragma + Fiscus. They open
`http://127.0.0.1:8731/` and see the trust counter read `22+`. They
walk the IT and AR home pages with no staff session. If those three
checks pass, Pass D is GREEN; if any fail, Pass D opens an issue and
does not commit until resolved.

### 4.5 What Pass D does NOT include

- **No featured grid change.** Solaria stays `featured=False` per its
  seed; promoting it to featured is a separate marketing decision.
- **No new imagery.** The Pass A 6-URL Pexels pool stands.
- **No new locale.** The 5-locale tree from Pass B stands.
- **No DNA / archetype edits.** The corporate-suite contract stands.

---

## 5 · The minimum bar Pass C clears

Per `factory/standards/corporate-suite-quality-scorecard.md`, the
review-ready bar for a corporate-suite enrollee is:

- ✓ All 5 locales present (Pass B)
- ✓ RTL working for AR (Pass B)
- ✓ Voice anchor preserved across locales (Pass B)
- ✓ AAA contrast on chrome (X.4a step2)
- ✓ Responsive at 1440 / 1024 / 880 / 720 / 390 (X.4a step1D)
- ✓ Pexels-only imagery, archetype `corporate_suite.E002 / E003` silent (Pass A)
- ✓ Test suite green (546/546 in Pass C)
- ✓ Internal nav reachable end-to-end from a single entry point (**Pass C**)

The last item was the only one Pass C inherited as red. It is now
green.

---

## 6 · Final verdict

**Pass C release-gatekeeper: GREEN for staff-gated stakeholder
review. HELD on public flip pending user authorisation per Pass D
spec in §4.**

The user should walk the captures in
`factory/reports/browser-verification/solaria-passC-public-review.md`
§2, then walk the live server using the script in
`factory/reports/solaria/solaria-passC-public-review.md` §7, and only
then decide whether to authorise Pass D. The gatekeeper is explicit
that an authorised "yes" requires looking at the captures, not just
trusting the GREEN.
