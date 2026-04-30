# Browser verification · Continua · Public Flip · 2026-04-30

**Server**: `python manage.py runserver 127.0.0.1:8052 --noreload`
**Port**: 8052
**Tip**: `c319aeb` (workflow D pre-flip) → public-flip working tree
**Branch**: `phase-x4-continua-public-flip`
**Verifier**: gatekeeper · post-cascade live walk · anonymous (no staff session)

---

## 1 · Anonymous reachability (Layer-1 gate)

The flip's load-bearing claim is "Continua is publicly visible to anonymous visitors". Verified end-to-end with `curl` (no cookies · no `?preview=1` flag · no staff user) against the running dev server.

```
$ curl -sS -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8052/templates/business/
200

$ curl -sS http://127.0.0.1:8052/templates/business/ | grep -c continua-stewardship
5

$ for loc in it en fr es ar; do
    curl -sS -o /dev/null -w "$loc → %{http_code}\n" \
      "http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=$loc"
  done
it → 200
en → 200
fr → 200
es → 200
ar → 200
```

All anonymous probes 200. Continua's slug surfaces 5 times in the rendered business-catalog HTML (card name + cluster chip + image src + detail anchor + meta dataset) which is the same fingerprint Pragma / Fiscus / Solaria emit at this catalog band, so the Continua card is rendering with the standard cluster-card primitive (no orphan / no half-card).

---

## 2 · Home page trust counter (Layer-2 visible signal)

```
$ curl -sS http://127.0.0.1:8052/ | grep -oE 'mw-home-trust-n[^>]*>[^<]+'
mw-home-trust-n">23+
mw-home-trust-n">15
mw-home-trust-n">52
mw-home-trust-n">5

$ curl -sS http://127.0.0.1:8052/ | grep -oE '23\+ template'
23+ template
```

The hero meta strip (`templates/pages/home.html:32`) and the trust-band figure (`:170`) both render `23+`. Inherited from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()` — no template / view edit was needed; the dynamic binding flipped automatically when `sync_template_tiers` lifted Continua's row.

---

## 3 · AR RTL parity (Layer-1 critical · O17 / CS-TYPE-05)

```
$ curl -sS 'http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=ar' \
    | grep -oE 'html lang="[^"]+"|dir="[^"]+"' | head -3
html lang="ar"
dir="rtl"
dir="rtl"
```

`html lang="ar" dir="rtl"` shipped to anonymous visitors. The Pass B LF-5 letter-spacing reset extension (`_base.html` · 9 LF-5 eyebrow surfaces · `html[dir="rtl"]` scoped) was not edited by the flip and remains in place.

---

## 4 · 45-route catalog smoke (5 locales × 5 pages + 5 locales × 4 mandate posts)

Probed live with a Python script discovering mandate slugs from `/mandati/` index in IT, then walking all 5 locales × all 5 page kinds (`home`, `chi-siamo`, `custodia`, `mandati`, `contatti`) plus all 5 locales × 4 discovered mandate posts.

Discovered post slugs:

```
famiglia-a-quarta-generazione-holding-industriale
famiglia-b-fondazione-di-famiglia
famiglia-c-trasferimento-intergenerazionale
famiglia-d-single-family-office-estero
```

```
=== 45 routes probed · 45 OK · 0 FAIL ===
ALL 200
```

Same 45/45 the workflow D staff-session walk captured at port 8051 — but now anonymous at port 8052. Confirms the public flip preserves every route the legitimate D-055 staff-preview path was already serving.

---

## 5 · Staff-preview legacy flag remains benign

```
GET /templates/business/continua-stewardship/preview/?preview=1                   → 200
GET /templates/business/continua-stewardship/preview/?lang=ar&preview=1           → 200
GET /templates/business/continua-stewardship/preview/?lang=zz                     → 200   (locale fallthrough is clean)
```

Any link still propagating `?preview=1` (e.g. a stale staff session that hasn't refreshed) continues to work. Tier=published_live short-circuits the D-055 anonymous gate upstream of the preview-flag check, so the flag is now a benign no-op for this slug.

---

## 6 · Frozen-sibling regression spot-check

```
GET /templates/business/pragma-corporate-suite/preview/                          → 200
GET /templates/business/fiscus-commercialista/preview/                           → 200
GET /templates/business/solaria-coaching/preview/                                → 200
```

The 3 frozen corporate-suite siblings still serve 200 anonymously. No cross-template collateral.

---

## 7 · Verdict

**GREEN.** Continua is publicly reachable to anonymous visitors in all 5 locales · catalog band lists the slug · home counter renders `23+` · AR RTL preserved · 45/45 route smoke · 0 cluster regressions.

The flip is live.
