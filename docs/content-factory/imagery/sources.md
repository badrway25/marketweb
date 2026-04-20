# Imagery Sources · Allowed + Workflow

**Status**: binding source list for Wave 2+ templates. Any source not on this list is rejected at review.

**Scope**: defines where imagery comes from, how to query it, how to authenticate (when relevant), and how to record attribution.

---

## 1 · Allowed sources (ranked)

### 1.1 · Pexels · PRIMARY

- **Tier**: Primary. Session 47 (D-077) adopted Pexels as the catalog's primary stock-photo CDN.
- **License**: Pexels License — free for commercial use, no attribution required. Attribution recorded in pack metadata anyway for traceability.
- **Auth**: API key required for programmatic search.
- **Env var**: `PEXELS_API_KEY`
- **Key handling**:
  - Never commit the key to git (any file under the repo tree).
  - Set locally via `$env:PEXELS_API_KEY="<key>"` (PowerShell) or `export PEXELS_API_KEY="<key>"` (bash).
  - The helper `apps/catalog/_pexels_helper.py` (Session 47) is `.gitignored` and reads the key from env at runtime only.
- **Search endpoint**: `https://api.pexels.com/v1/search?query=<q>&per_page=<n>&orientation=<landscape|portrait|square>`
- **Rate limit**: 200 requests/hour on free tier. Curators throttle accordingly.

**Workflow**:
1. Export `PEXELS_API_KEY` in the shell (never write to a tracked file).
2. Use curl or the helper to query. Example:
   ```
   curl -H "Authorization: $PEXELS_API_KEY" \
        "https://api.pexels.com/v1/search?query=editorial+restaurant+plated+dish&per_page=30&orientation=landscape"
   ```
3. Collect candidate URLs + photographer credits from the JSON response.
4. Apply the curation protocol (see `CURATION_PROTOCOL.md`).

### 1.2 · Unsplash · SECONDARY

- **Tier**: Secondary. Use when Pexels doesn't yield a cluster-appropriate result. Requires stronger human review because Unsplash has a broader quality range.
- **License**: Unsplash License — free for commercial use, no attribution required.
- **Auth**: None for URL-level usage (no API needed). API is optional for programmatic discovery.
- **URL pattern**: `https://images.unsplash.com/photo-<id>?w=<width>&...`
- **Review discipline**:
  - Check for category mismatch (Unsplash search is less curated than Pexels).
  - Photographer attribution recorded in pack metadata.
  - Resolution check: Unsplash serves sized URLs — request `w=1600` or `w=1920` for hero.

**Workflow**:
1. Search on `https://unsplash.com/s/photos/<query>`.
2. Open candidate photo, right-click → copy image URL.
3. Apply the curation protocol (stronger review than Pexels).

### 1.3 · Custom photography · POST-WAVE 2

- **Tier**: Not allowed in Wave 2 MVP. Reserved for post-Wave 2 brand evolution.
- **Rationale**: custom photography requires photographer agreements, model release forms, and a rights-management pipeline we do not yet operate.
- **Enablement**: when introduced, a dedicated "custom photography" protocol will be written, including storage paths, release forms, and attribution records.

---

## 2 · Forbidden sources

The following are **never** acceptable in Wave 2:

| Source | Reason |
|---|---|
| Shutterstock | Paywalled; license cost doesn't scale. |
| Adobe Stock | Paywalled. |
| Getty Images | Paywalled. |
| iStock | Paywalled. |
| Random Google Images scraping | Licensing unclear; frequent embedded branding. |
| Instagram posts | No commercial-reuse license by default. |
| Behance project images | License varies per project; often not CC0. |
| Screenshots of other websites | Nearly always copyright infringement. |
| AI-generated images (Midjourney, DALL·E, etc.) | Out of scope for Wave 2; licensing / quality / semantic-coherence all open questions. Revisit post-Wave 2. |

A PR that references any of these sources is rejected at review.

---

## 3 · Attribution recording

For each URL in an imagery pack, record (at minimum):

- **URL** (permalink to the image, not a temporary CDN-signed URL)
- **Photographer name** (Pexels returns this in the `photographer` field; Unsplash shows it on the page)
- **Source** (Pexels / Unsplash)
- **License** (Pexels License / Unsplash License)
- **Dimensions** (width × height)
- **Date curated** (YYYY-MM-DD)

Example row:

```markdown
- **URL**: https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg
- **Photographer**: Daria Shevtsova (Pexels)
- **Source**: Pexels · Pexels License
- **Dimensions**: 1920×1280
- **Date curated**: 2026-04-20
```

---

## 4 · Query hygiene

Good search queries are **specific, multi-word, and tied to the cluster's terminology dictionary**. Bad queries are single-word generics.

**Good queries** (pull from cluster blueprint §4 Terminology + §8 Imagery direction):
- `editorial restaurant plated dish warm tones`
- `dental clinic chair bright minimal`
- `boutique hotel lobby warm wood evening light`
- `artisan workshop hands clay pottery`

**Bad queries** (produce generic stock fallback fodder):
- `restaurant`
- `office`
- `team`
- `business`
- `doctor`

**Reviewer rule**: the curator documents 3-5 actual queries used in the pack file header, so future rework can replay the curation intent.

---

## 5 · Workflow summary (1-pager)

```
1.  Read cluster blueprint (identity, voice, imagery direction, anti-patterns)
2.  Read imagery/CURATION_PROTOCOL.md + imagery/blacklist.md
3.  Export PEXELS_API_KEY in shell (never in a file)
4.  Design 3-5 multi-word queries tied to blueprint terminology
5.  Query Pexels · collect 60-100 candidates into a scratchpad
6.  If gaps, fall back to Unsplash with stronger review
7.  For each candidate:
    a. curl -I to verify 200 + content-type image/*
    b. Record dimensions (must meet role-specific threshold)
    c. Write semantic caption (what IS in the image, not what we want)
    d. Write coherence statement (how the image fits the cluster)
    e. Cross-cluster duplication check (grep across imagery/packs/)
    f. Blacklist pattern scan
8.  Down-select to 20-40 URLs per pack
9.  Produce imagery/packs/<cluster-slug>.md per the protocol template
10. Reviewer LGTM (different person than curator)
11. Unblock copy author
```

---

## 6 · Storage + fetching policy

- **Imagery URLs are stored as strings in content registries / template metadata**. The site does NOT download and re-host images in Wave 2 — we link directly to the source CDN (Pexels or Unsplash).
- **No vendoring**: do not copy imagery into `static/images/` unless post-Wave 2 custom photography pipeline opens.
- **CDN trust**: Pexels and Unsplash are reliable CDNs at scale. We have not observed 404s on historical URLs. Commit 3's `check_imagery_pack.py` nevertheless runs a curl check at review time to catch any outliers.

---

## 7 · When this doc updates

- New primary/secondary source added → update §1 + rebase all existing packs through a reviewer pass.
- Licensing change on an allowed source → immediate policy review.
- Failure incident (e.g. a CDN takes down a URL we reference) → add to `blacklist.md` historical incidents table + decide whether to harden via re-curation or vendoring (post-Wave 2 discussion).

---

**End of sources list. PR authors cite this file in imagery-related PR descriptions.**
