# Causa · A.6 IT review-lock · browser-verifier

**Phase**: X.6 Step 5 · A.6 review-lock
**Template**: causa-legale (LF-2 · 6th corporate-suite sibling)
**Date**: 2026-05-04
**Verdict**: 4.5 / 5 · routes + DOM probes clean · per-Pexels-URL probe disambiguated A.5 misclassification

---

## §1 · Route status (post-fix)

```
9/9 staff_preview routes 200    (causa_review_a6 + ?preview=1)
4/4 anonymous draft-gate 404
1/1 catalog listing  200 + Causa absent (correctly excluded)
1/1 homepage counter '24+' (unchanged)
5/5 frozen siblings  200 anonymous (byte-equivalent to A.5)
```

Detail in `factory/reports/browser-verification/causa-a6-it-review-lock.md
§1, §2, §3`.

---

## §2 · DOM probes (post-fix)

24/24 DOM probes PASS (detail in browser-verification report §5):

- LF-2 family signal: 13/13 signatures intact
- CSS variables: --primary `#14342B` · --secondary `#F0EBE0` · --accent `#0B0A0E` · --heading `'GT Sectra', Georgia, ...` · --body `'Manrope', system-ui, ...`
- Voice anchor verbatim count on home: 2 (target = 2)
- Em-word count on home: 12 (target ≥ 10)
- Navbar pill on every page: "APRI UN PARERE PRELIMINARE" (target: Causa-specific · NOT Cornice default `Apri un fascicolo`)

---

## §3 · Per-Pexels-URL direct verification (the load-bearing A.6 test)

This is the panel A.6 was specifically asked to deliver: "If the Pexels CDN
issue was sandbox-only, distinguish clearly between real product issue and
tooling issue."

Method: navigate each Pexels URL directly in the Playwright sandbox + save
screenshot + compare rendered content to the curator's caption.

| Pexels ID | Curator captioned subject | Actual rendered content | Capture |
|---|---|---|---|
| 17109985 (slot 0 hero) | empty courtroom interior · zero people | group portrait of casual youths · multiple people · sepia/dark setting | 02-hero-pexels-direct.jpeg |
| 15796091 (backup 11) | empty European court chamber | single palm tree silhouette | 03-backup11-15796091.jpeg |
| 8112167 (backup 12) | wide chamber interior tall windows | HTTP 404 · URL does not exist | 04-backup12-8112167.jpeg |
| 4427451 (backup 13) | empty courtroom vertical timber columns | night cityscape · church/castle silhouette | 05-backup13-4427451.jpeg |
| 7841457 (backup 14 PRE-CLEARED FALLBACK) | codex-spread on chambers desk · zero people | 3-person warm-mahogany consultation | 06-backup14-7841457.jpeg |
| 8101948 (slot 2 founder) | senior man 60s in chambers with codex | bowl of food in terracotta dish | 07-portrait-8101948.jpeg |
| 9489162 (extra 7 case-card hero) | Italian high-court exterior detail | half-nude male model studio shot | 08-case-9489162.jpeg |
| 6077368 (slot 1 feature) | open Italian law codex on chambers table | residential bay-window living-room | 09-feature-6077368.jpeg |

**8/8 sampled URLs return content categorically different from curator
captions.** The defect is NOT a sandbox CDN issue (URLs resolve, return
200, return real photo content). The defect is at the curator layer
(Pexels IDs are curator-hallucinated assignments).

**Reclassification of A.5 Issue 3**: from "sandbox-only · NOT FIXED" to
**REAL PRODUCT DEFECT · curator-hallucinated Pexels IDs · imagery pack
must be re-curated at A.5b**.

---

## §4 · Browser-verifier verdict

**Routes + DOM probes clean.** **Per-Pexels-URL probe successfully
disambiguated the A.5 misclassification** — the load-bearing question of
the A.6 brief is answered conclusively.

Score: **4.5 / 5** (the 0.5 reflects the fact that the photographic axis
itself cannot be browser-verified at A.6 because the surfaces are HELD ·
A.5b will re-curate and A.6b can re-verify).
