# Solaria · Pass C · scorecard

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching · **Pass**: C
**Date**: 2026-04-27 · **Run-ISO**: `20260427T1000Z`
**Source rubric**: `factory/standards/corporate-suite-quality-scorecard.md`
**Aggregate verdict**: **GREEN for review-ready · HELD for public flip**

---

## 1 · Cell-by-cell

| Panel | Verdict | One-line read |
|---|---|---|
| build-report | **GREEN** | 546/546 tests, 1 W001 unchanged (Pragma grandfather), no new warnings |
| style-critic | **GREEN** | no visual regression; Pass A image-rhythm + Pass B locale parity preserved |
| contrast-accessibility | **GREEN** | AAA contrast pairs preserved; tab order unchanged; AR form labels Arabic |
| responsive-auditor | **GREEN** | overflow 0/-15 at 1440/1024/390; hamburger toggles ≤880; AR layout mirrors |
| browser-verifier | **GREEN** | 11/11 internal hrefs → 200 from staff session; tier gate intact for non-staff |
| release-gatekeeper | **GREEN (review-ready)** | review-path legitimised; public flip explicitly held |

6/6 panels GREEN under the *review-ready* mandate of Pass C.

The release-gatekeeper panel is also explicit that "GREEN" here
authorises **staff-gated stakeholder review**, not the public-flip
cascade. Pass D (public flip) is documented to the line in
`release-gatekeeper.md` §4 and is held until user authorisation.

---

## 2 · Anti-claims (load-bearing list, honest)

These are claims this scorecard explicitly does NOT make. Honest
restraint matters more than maximalist GREEN:

1. **Solaria is approved for public release.** No. Pass C does not
   authorise public flip. See gatekeeper §1 and §3.

2. **Public catalog count is now 22.** No. Public count remains 21 /
   22. The DB row for `solaria-coaching` keeps `tier="draft"`. The
   homepage trust counter still reads `21+`.

3. **An anonymous visitor can review Solaria.** No. An anonymous
   visitor going to any Solaria URL still gets 404. Review requires
   the staff credentials in `summary.md` §6.

4. **All 5 locales × all 5 pages × all 5 viewports were captured this
   pass.** No. Pass C captures 9 surfaces — the 5 locale homes at 1440,
   AR percorsi + AR contatti at 1440, AR home at 390, IT home at 1024.
   The Pass B run already exercised the deeper matrix; Pass C narrows
   to the surfaces that *change reachability* under the staff-preview
   fix.

5. **Pass C improves design quality.** No. Pass C is a navigation /
   query-string fix and a metadata correctness fix. Visual quality is
   inherited from Pass A (IT distinctness) and Pass B (locale parity).

6. **The fix touches all archetypes.** No. The fix lives in the 6
   `templates/live_templates/business/corporate-suite/*.html` files
   only, plus a 2-line view edit. Other archetypes (medical, lawyer,
   restaurant, real-estate, portfolio, agency, ecommerce, startup-saas,
   fine-dining) are unmodified. The fix benefits any future
   `tier=draft` corporate-suite enrollee transitively but is currently
   visible only on Solaria (Pragma + Fiscus are `published_live` and
   never set `staff_preview` to True).

---

## 3 · How the GREEN compounds with previous Solaria passes

| Pass | Closed | Outstanding after the pass |
|---|---|---|
| Pass A (IT distinctness) | image-rhythm gain (5 home photos vs 1) · voice anchor IT · palette polarity gate green | 4 locales · public flip |
| Pass B (multilingual) | 4 locale trees authored · RTL working · voice anchor verbatim across 5 locales | review-path legitimacy · public flip |
| Pass C (this pass) | review-path legitimacy (`&preview=1` propagation in 6 chrome files + 1 view) · registry honesty (locales+rtl) | **public flip only** |

After Pass C, the only outstanding item between Solaria and a real
shipped template is the deliberate Pass D public-flip cascade.

---

## 4 · Aggregate

```
Review-ready as draft:        GREEN ✓
Public-flip cascade ready:    GREEN ✓ (cascade documented, not executed)
Public flip authorised:       HELD  · pending user decision per gatekeeper §1
```

Solaria is review-ready. The Pass D commit is small, well-defined, and
will be executed when (and only when) the user authorises it.
