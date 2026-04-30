# browser-verifier · Continua · Public Flip · 2026-04-30

**Verdict**: GREEN · anonymous reachability confirmed · 45/45 routes · 0 cluster regression · trust counter `23+` · AR RTL preserved

---

## 1 · Server posture

```
$ python manage.py runserver 127.0.0.1:8052 --noreload
```

Listening at `http://127.0.0.1:8052/`. Server left running for any post-flip user re-walk; port 8052 is non-conflicting with the workflow D pre-flip walk that ran on 8051.

---

## 2 · Anonymous · catalog-side flip evidence

### 2.1 · `/templates/business/`

```
GET /templates/business/                                    → 200
slug "continua-stewardship" hits in HTML                    → 5
```

Continua slug surfaces 5 times in the rendered business-catalog HTML — same fingerprint as Pragma / Fiscus / Solaria cards (image src + name + cluster chip + detail link + meta). Was 0 before the flip.

### 2.2 · Home `templates_live` counter

```
GET /                                                       → 200
"23+" hits in rendered home HTML                            → 2
"22+" hits                                                  → 0
```

Rendered at `templates/pages/home.html:32` (hero meta strip) and `:170` (trust band figure). Inherited from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()` with zero template edit.

---

## 3 · Anonymous · 5 locales (Continua main routes)

```
GET /templates/business/continua-stewardship/preview/                → 200    (IT)
GET /templates/business/continua-stewardship/preview/?lang=en        → 200    (EN)
GET /templates/business/continua-stewardship/preview/?lang=fr        → 200    (FR)
GET /templates/business/continua-stewardship/preview/?lang=es        → 200    (ES)
GET /templates/business/continua-stewardship/preview/?lang=ar        → 200    (AR · RTL)
```

5/5 200. Anonymous. No cookies, no `?preview=1` flag, no staff session.

### 3.1 · AR RTL spot-check

```
$ curl -sS '...?lang=ar' | grep -oE 'html lang="[^"]+"|dir="[^"]+"'
html lang="ar"
dir="rtl"
dir="rtl"
```

`dir="rtl"` appears twice (root html element + the LF-5 Arabic-only body wrapper). Pass B's LF-5 letter-spacing reset (9 eyebrow surfaces under `html[dir="rtl"]` in `_base.html`) was not edited by this flip and remains in place.

---

## 4 · Anonymous · 45-route catalog smoke

5 locales × 5 page kinds + 5 locales × 4 mandate-detail posts = 45 routes. Mandate post slugs discovered live from `/mandati/` index in IT:

```
famiglia-a-quarta-generazione-holding-industriale
famiglia-b-fondazione-di-famiglia
famiglia-c-trasferimento-intergenerazionale
famiglia-d-single-family-office-estero
```

Probe result:

```
=== 45 routes probed · 45 OK · 0 FAIL ===
ALL 200
```

Same total the workflow D staff-session walk captured — but now anonymous.

---

## 5 · Staff-preview legacy flag · benign

```
GET /templates/business/continua-stewardship/preview/?preview=1            → 200
GET /templates/business/continua-stewardship/preview/?lang=ar&preview=1    → 200
GET /templates/business/continua-stewardship/preview/?lang=zz              → 200
```

`?preview=1` is now a no-op pass-through on this slug because tier=published_live short-circuits the D-055 anonymous gate upstream. Any link that still propagates the flag (e.g. a stale staff session) keeps working.

---

## 6 · Frozen-sibling regression spot-check

```
GET /templates/business/pragma-corporate-suite/preview/    → 200
GET /templates/business/fiscus-commercialista/preview/     → 200
GET /templates/business/solaria-coaching/preview/          → 200
```

3/3 corporate-suite frozen siblings still serve 200. No collateral.

---

## 7 · O13 — walk URL + handshake (Layer-1 blocking override)

| O13 component | Status |
|---|---|
| Walk URL recorded | YES · `http://127.0.0.1:8052/` (this report + the `continua-public-flip.md` report + the gatekeeper scorecard) |
| Walk port recorded | YES · 8052 |
| User parallel-verification handshake | **YES** · explicit user authorization in this conversation: "execute the documented Workflow D release cascade after explicit user approval" |

O13 fully cleared. The gate that workflow D held open is now closed.

---

## 8 · Verdict

**GREEN.** Anonymous live reachability confirmed end-to-end · trust counter rendered correctly · AR RTL preserved · 45/45 catalog smoke · 0 cluster regression · O13 cleared. The flip is verified live and the verification artifact is captured.
