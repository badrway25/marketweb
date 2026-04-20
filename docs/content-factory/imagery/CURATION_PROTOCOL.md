# Imagery Curation Protocol · BINDING

**Status**: binding for every Wave 2+ template. Skip this and we reopen Session 31.

**Scope**: defines how imagery is curated, validated, and approved BEFORE copy authoring starts. Imagery is not a post-author polish step. It is the floor the copy sits on.

---

## Why this protocol exists · Session 31 context

On 2026-04-13, Session 31 exposed **~17 catastrophic imagery mismatches** across the public catalog:
- A PlayStation gamepad was used as a "map of Rome" on a real-estate template.
- A Bumble Bee tuna can was labelled "artisan ingredients" on a bottega.
- Hairstylists' portraits stood in as "before/after dermatology" on a medical template.
- A diamond ring portrayed an "oysterman's portrait" on a Luxe collection tile.

Each error was a trivial copy-paste from a search query that ignored semantics. None of them survived human semantic review. All of them survived the **author's** own review because the author was not the curator — the author trusted the URL without reading what the URL depicted.

**This protocol's binding rule**: URL-by-URL semantic review by a dedicated curator, one step before copy authoring. The curator's output is a file under `imagery/packs/<cluster-slug>.md`. The copy author cannot begin until this file is reviewer-approved.

---

## 1 · Binding pipeline position

```
Cluster backlog
     │
     ▼
[CURATOR STEP]  ← this protocol applies here
     │
     ▼
Imagery pack reviewed + approved
     │
     ▼
IT Copy Author begins
     │
     ▼
Locale authors · reviewer · merge
```

A cluster that reaches "IT Copy Author" without a signed-off imagery pack is a process violation. Phase Lead rejects the PR, the flow restarts from the curator step.

---

## 2 · Allowed sources (and only these)

| Source | Tier | Use | Key |
|---|---|---|---|
| **Pexels API** | Primary | Curated search + license clean | `PEXELS_API_KEY` env var · never committed |
| **Unsplash** | Secondary | Fine for editorial shots, needs stronger review | No API auth required for read-only URL usage |
| Paywalled stock (Shutterstock, Adobe Stock, Getty) | ❌ Forbidden in MVP | Licensing + cost + scaling | — |
| Random Google Images scraping | ❌ Forbidden | License-unclear | — |
| Custom photography | ⚠️ Post-Wave 2 only | Requires dedicated photographer + release forms | — |

Session 47 adopted Pexels as the primary stock-photo CDN. The workflow lives in `sources.md` (this directory).

**Attribution**: Pexels CC0 permits commercial use without attribution, but the curator still records the photographer name + URL in the pack file for traceability.

---

## 3 · Curator workflow

### 3.1 · Pre-work

1. Read the cluster blueprint in `cluster_blueprints/<cluster>.md` — specifically sections §3 Positioning, §5 Voice, §8 Imagery pack pointer, §13 Anti-patterns.
2. Read the blacklist in `imagery/blacklist.md` (this directory).
3. Read `imagery/sources.md` for the Pexels/Unsplash workflow.
4. Export `PEXELS_API_KEY` as an env var. Never write the key to any file under `docs/`, `apps/`, `static/`, `templates/`, or any file tracked by git.

### 3.2 · Discovery

- Run Pexels searches using cluster-specific queries sourced from the blueprint's terminology + voice anchors. Example for `fine-dining`: search queries `plated dish editorial`, `restaurant interior warm`, `chef hands preparation`, `wine pairing table`, `dining room low light`.
- Collect 60-100 candidate URLs into a scratchpad (not the final pack file).
- For each candidate, verify:
  - Content-Type is `image/jpeg` or `image/png`
  - Resolution ≥ 1600×900 for hero-class images; ≥ 800×800 for portraits
  - Subject matches cluster semantics (see §4 below)
  - No watermark, no brand logos, no competing product placement

### 3.3 · Semantic review (one-by-one)

For each candidate URL, the curator writes:
1. A **1-sentence semantic caption** describing what's actually in the image (not what we want it to be). Example: *"Plate of handmade tagliatelle with ragù, overhead shot, warm natural light, Italian editorial style."*
2. The **semantic role** the image plays on the template: `hero`, `about-portrait`, `gallery`, `menu-item`, `ingredient`, etc.
3. A **coherence justification** (1 sentence) mapping the image to the cluster's positioning.

A URL that cannot support all three statements is discarded — no ambiguity allowed.

### 3.4 · Cross-cluster duplication check

Before finalizing, compare every URL against all existing imagery packs. Rules:
- No URL may appear in 2+ imagery packs. One URL = one cluster.
- Exception: genuinely generic assets (e.g. a neutral paper-texture background) may repeat, but only with explicit documentation in both packs.
- Automated check: `scripts/check_imagery_pack.py` (to be delivered in X.3 Commit 3) will grep across all packs and fail on duplicates.

### 3.5 · Curation output

The curator produces a single file: `imagery/packs/<cluster-slug>.md` (to be created per-cluster in later commits).

Structure (mandatory):

```markdown
# Imagery Pack · <cluster-slug>

**Curator**: <name/handle>
**Date**: <YYYY-MM-DD>
**Blueprint reference**: cluster_blueprints/<cluster>.md
**Total URLs**: <n>  (target 20-40)

## Validation summary

- All URLs curl-validated: [ ] yes
- Content-type image/* verified: [ ] yes
- Resolution ≥ 1600×900 for hero: [ ] yes
- Resolution ≥ 800×800 for portraits: [ ] yes
- Cross-cluster duplication check: [ ] clean
- Blacklist patterns absent: [ ] verified (see imagery/blacklist.md)
- Licensing clean: [ ] Pexels/Unsplash CC0 confirmed

## URL list

### hero

1. https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg
   - **Caption**: <semantic caption>
   - **Role**: hero
   - **Coherence**: <why this fits the cluster>
   - **Photographer**: <name> (Pexels attribution)
   - **Resolution**: <wxh>

... (repeat for every URL)

### about-portrait

...

### gallery

...
```

Add sections per semantic role as required by the archetype.

---

## 4 · Semantic coherence criteria per cluster

A URL passes semantic review only if all hold:

- **Subject match** — the image depicts a subject that plausibly belongs to this profession. A barber-shop scene for a `fine-dining` cluster fails. A wine-cellar scene for a `fine-dining` cluster passes.
- **Mood match** — the image's visual mood (lighting, palette, composition) aligns with the cluster's voice anchor (blueprint §5).
- **No detected cultural mismatch** — generic Italian-trattoria clichés (red-checked tablecloth, straw-basket Chianti) on a `fine-dining` cluster fail. Same clichés on a `trattoria` cluster may pass if the voice anchor tolerates them.
- **No product placement** — a shot with a visible Nespresso machine in a `fine-dining` pack is rejected. Neutral unbranded equipment passes.
- **Diversity + representation where applicable** — team/portrait packs should not be a mono-demographic lineup unless the cluster has an explicit rationale (extremely rare). Default: diverse age, gender, ethnicity where plausible for Italian market.

---

## 5 · Validation order (strict · non-parallel)

1. **URL accessibility** — `curl -I <url>` returns 200 + `content-type: image/*`. Failing URLs are removed, not fixed.
2. **Resolution check** — follow the URL, confirm dimensions meet the threshold.
3. **Semantic caption** written per §3.3.
4. **Cross-cluster duplication check** per §3.4.
5. **Blacklist pattern scan** per `imagery/blacklist.md`.
6. **Licensing confirmation** per `imagery/sources.md`.
7. **Pack file produced + reviewer LGTM** per §3.5.

Step 1 failures auto-reject. Step 2-6 failures send the URL back to discovery. Only when all 6 pass does a URL land in the pack.

---

## 6 · Reviewer sign-off on imagery packs

Before the copy author is unblocked, a second reviewer (not the curator) signs off on the pack:

- [ ] Pack file exists at `imagery/packs/<cluster-slug>.md`
- [ ] 20-40 URLs total (not fewer, not more)
- [ ] Every URL carries caption, role, coherence statement, photographer
- [ ] Spot-check 3-5 random URLs: curl-validated, resolution confirmed, semantic match visible
- [ ] Cross-cluster duplication check clean (reviewer runs/spot-checks)
- [ ] Blacklist scan clean
- [ ] Licensing clean
- [ ] Pack aligns with blueprint §8 imagery direction (palette, composition, subjects)

On LGTM, the pack is marked approved and the IT Copy Author begins.

---

## 7 · Non-negotiables (summary)

- Imagery curator is **always** a different person/sub-agent from the copy author.
- No URL lands in a pack without semantic caption + coherence statement.
- No URL is reused across clusters.
- No paywalled stock.
- No raw Google Images URL.
- No author begins copy before the pack is reviewer-approved.
- No automated "AI image search" result is accepted without semantic review.
- No blacklist pattern survives review (see `blacklist.md`).

Violations are process failures, not judgment calls. A PR that skips this protocol is rejected by Phase Lead, and the cluster goes back to the backlog.

---

**End of protocol. Binding for Wave 2+.**
