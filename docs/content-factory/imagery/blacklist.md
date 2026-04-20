# Imagery Blacklist · Anti-patterns

**Status**: binding reviewer reference. Every imagery pack is checked against this list before the copy author is unblocked.

**Purpose**: catalog the failure modes documented during Sessions 31, 37, 38, 42, 47, and earlier. Reviewer uses each section as a pass/fail gate — no vague "feels wrong" rejections; every rejection cites a specific line from this list.

---

## 1 · Category mismatch

**Pattern**: image subject does not belong to the cluster profession. The most expensive failure mode, caught or missed at review time.

**Session 31 examples** (all shipped to production before fix):
- PlayStation gamepad used as "map of Rome" on a real-estate cluster.
- Bumble Bee tuna can labelled "artisan ingredients" on a `bottega` cluster.
- Hairstylists' portraits used as "before/after dermatology" on a medical specialist template.
- A diamond ring used as "oysterman's portrait" on a Luxe editorial tile.

**Reviewer rule**: open each URL, look at the image for 3+ seconds, ask "does a person in this profession recognize this as their world?" If the answer is "no" or "only if I squint", reject.

**Automated assist**: none. Semantic review is human-only.

---

## 2 · Generic stock fallback

**Pattern**: image is clearly a generic stock asset used to fill a slot the curator didn't care about. Symptoms:
- "Generic laptop on clean white desk"
- "Smiling businesswoman shaking hands in vague office"
- "Chef holding a plate, looking at camera, perfectly lit"
- "Multi-ethnic team pointing at a whiteboard"

These shots scream "stock fallback" to any reader. They reduce perceived premium quality instantly.

**Reviewer rule**: if the image could slot into 10+ unrelated clusters without changing meaning, it's a generic stock fallback. Reject.

**Exception**: for very abstract sections (e.g. a neutral "trust strip" background), a deliberately generic asset can be appropriate. Flag it explicitly in the pack caption so the reviewer knows the intent.

---

## 3 · Cross-cluster reuse

**Pattern**: the same URL appears in 2+ cluster imagery packs.

**Session 38 example**: `preview_imagery.py` `portfolio-photographer[0-1]` literally reused `restaurant-fine[0-1]` URLs under a "proven offline-safe" rationale. Fixed by swapping all 6 URLs. The rationale ("offline-safe") was code-level, not semantic — which is how this snuck in.

**Reviewer rule**:
- Curator runs a grep across `imagery/packs/*.md` for each candidate URL before inclusion.
- Reviewer spot-checks 3-5 random URLs by grepping at review time.
- One URL = one cluster. Exceptions (genuinely generic textures) must be documented in both packs with an identical rationale line.

**Automated assist**: `scripts/check_imagery_pack.py` (X.3 Commit 3) will grep across packs and fail on duplicates before merge.

---

## 4 · Low resolution

**Pattern**: the image looks sharp on the curator's 1440×900 laptop but pixellates on a 1920×1080 hero.

**Thresholds** (non-negotiable):
- Hero / full-bleed / cover images: **≥ 1600×900 pixels**
- Portrait / team shots: **≥ 800×800 pixels**
- Gallery / thumbnail: **≥ 1200×900 pixels**

**Reviewer rule**: curl the image, check dimensions in the response or by downloading a sample. Any image below threshold is rejected — upscaling is not a fix.

**Automated assist**: `check_imagery_pack.py` will fetch HEAD + parse Content-Length + first KB to extract dimensions, flag below-threshold.

---

## 5 · Noisy CTA background

**Pattern**: hero image is visually busy, and the copy author tries to overlay a CTA on top. Result: low-contrast button, unreadable subtitle, or a CTA that sits in a "soup" zone.

**Examples**:
- A hero plate shot with high-key lighting + cluttered background + a white "Prenota" button → invisible CTA.
- A dining-room shot with string lights covering 40% of the frame → no clean CTA zone.
- A portrait with a busy bookshelf behind → headline overlaps with book spines.

**Reviewer rule**: every hero image must have a **clean CTA zone** — a region of ≥ 400×200 pixels with low visual entropy (solid color, dark vignette, or soft-focus) where text + button can be placed without additional overlay tricks. If the image doesn't provide this natively, reject.

**Exception**: skins that apply a full-opacity dark gradient over the image (D-060 specialist premium split pattern) can tolerate busier images. Document the skin-level overlay in the pack caption.

---

## 6 · Watermark / ID visible

**Pattern**: the image carries a stock-provider watermark, filename ID, or caption burned-in.

**Examples**:
- "Shutterstock preview" watermark in a corner.
- Filename "AdobeStock_123456.jpg" appearing in the URL path in a way that gets indexed.
- An Instagram-style caption burned into the image.
- Stock-provider QR code or barcode visible.

**Reviewer rule**: zero tolerance. A watermark on a public-facing template signals "not a real business". Reject.

**Pexels/Unsplash assets** do not have watermarks — this failure mode indicates the source was not one of the allowed sources, which is itself a process violation.

---

## 7 · Cultural insensitivity / stereotype

**Pattern**: the image reproduces a cultural cliché or stereotype that would embarrass the profession or alienate readers.

**Examples**:
- `fine-dining` cluster using a "man with monocle + top hat" caricature of fine dining.
- `medical` cluster using a "white coat + stethoscope against white background" cliché that reads as stock-doctor.
- `notary-commercialista` cluster using "dusty old books + quill pen" aesthetic that contradicts "modern professional service".
- Regional stereotypes: using Leaning Tower of Pisa for any Italian template; using Vespa + Colosseum for any Rome-based template.
- Representation issues: all-male leadership team for a cluster whose customer base is gender-balanced; all-young-beautiful faces for a medical template where patients span ages.

**Reviewer rule**: ask "would a professional in this field say 'this is me' or 'this is the clichéd version of me'?" If it's the clichéd version, reject.

---

## 8 · Over-processed / heavy filter

**Pattern**: the image has been Photoshop-overdone: extreme saturation, HDR halos, unrealistic skin smoothing, colour grading that reads as Instagram filter.

**Examples**:
- Teal-and-orange grading on a supposedly natural food shot.
- Skin smoothed to a porcelain finish on a portrait that should read as credible (a notary, a doctor).
- HDR sky with haloing around buildings on a real-estate shot.
- Saturation cranked to 150% on "vibrant market" shots.

**Reviewer rule**: the visual grammar should match the cluster's voice anchor. An over-processed image on an `editorial-warm` or `classic-serif` visual style fails.

---

## 9 · Text / UI mockup in-image

**Pattern**: the image contains visible text, phone mockups with fake UI, "hero mockup" laptop screens with dummy content, price tags, speech bubbles, infographics, or on-image brand copy.

**Examples**:
- A laptop on a desk with a fake "MarketWeb Dashboard" screen.
- A menu card photograph with real visible prices (contradicts the idea that menu is editable content in the template).
- An infographic "3 reasons to choose us" overlaid on a lifestyle shot.

**Reviewer rule**: images are visual context, not copy carriers. Any embedded text, price, or brand-language fails. The skin applies typography on top of clean imagery, not on top of other imagery's typography.

---

## 10 · Licensing smell

**Pattern**: the image looks "too good" — clearly professionally produced — and the URL doesn't resolve to a Pexels / Unsplash / clearly CC0 source.

**Examples**:
- Image hotlinked from a random agency portfolio.
- Image from a Behance project that doesn't declare CC0.
- Image from a Google Images result where the top result is a paywalled stock URL.
- Image from a personal Instagram without explicit commercial-reuse permission.

**Reviewer rule**: if the URL is not on an allowed source (see `sources.md`), reject. No "it looks fine, probably CC0" calls.

---

## Reviewer checklist (compact)

For each URL in a candidate pack:

- [ ] Category match (not a PlayStation-as-Roma-map situation)
- [ ] Not generic stock fallback
- [ ] Not reused in another cluster pack
- [ ] Resolution ≥ threshold for its semantic role
- [ ] Clean CTA zone if hero
- [ ] No watermark or burned-in text
- [ ] No cultural cliché / stereotype
- [ ] Not over-processed
- [ ] No UI mockup or visible in-image text
- [ ] Licensing clean (Pexels/Unsplash CC0)

**Reject on any miss.** No partial credit. No "we'll fix later".

---

## Historical incidents

| Session | Date | Pattern triggered | Fix cost |
|---|---|---|---|
| Session 31 | 2026-04-13 | §1 Category mismatch × 17 | ~4 hours of URL swaps + session dedicated to re-curation |
| Session 38 | 2026-04-14 | §3 Cross-cluster reuse (Pixel/Gusto collision · 6 URLs) | 1 file, 1 pool, 6 swaps |
| Session 42 | 2026-04-14 | §10 Licensing + §8 Over-processed (Bottega portrait stock) | Converted 6 portraits to typographic stamps (DNA-honest fix) |
| Session 47 | 2026-04-15 | Source upgrade (Unsplash-only → Pexels primary) | Workflow change, not a rejection |
| Session 50 | 2026-04-15 | §1 + §4 (Aura preview 404 hero URL · agency pipeline) | 3 fixes; lesson: rollout recipe must include preview generation per new template |

**Every one of these incidents was avoidable.** The protocol exists to make "avoidable" = "actually avoided".

---

**End of blacklist. Reviewer cites line numbers / section numbers when rejecting. No vague rejections.**
