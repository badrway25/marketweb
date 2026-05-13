# Audit Report — Phase 2.1: Pre-merge Hardening (v15)

**Data:** 2026-05-13
**Branch:** `phase-x7e-lf2-variance-and-causa-retrofit`
**Modalità:** modifiche solo su v15, master non toccato
**Esito:** verde, 2 P1 chiusi
**Raccomandazione:** v15 **READY** per fast-forward merge verso master

---

## 1. Stato Git iniziale (pre Fase 2.1)

- Branch: `phase-x7e-lf2-variance-and-causa-retrofit`
- HEAD: `35cc16a` (snapshot WIP composito)
- Working tree: 3 untracked (report Fase 2 + 2 audit log)
- Commit avanti su master: 255

## 2. Stato Git finale (post Fase 2.1)

```
570fea0 docs(audit): record post-fix test run logs (681/681 OK)
5017043 fix(commerce): close StorefrontMember.id migration drift
3288871 fix(templates): convert multi-line {# #} comments to {% comment %} blocks
2c8fa50 docs(audit): record v15 stabilization report
35cc16a chore(snapshot): preserve in-flight WIP before phase-2 stabilization
8ef3970 X.6 workflow C: ship Causa multilingual rollout (IT + EN/FR/ES/AR)
```

- HEAD: `570fea0`
- Working tree pulito (zero file untracked rilevanti — solo screenshots .png gitignored)
- 4 nuovi commit incrementali sopra `35cc16a` (snapshot)
- Commit avanti su master: 259 (era 255 + 4 di questa fase)
- 0 stash

## 3. Commit creati in Fase 2.1

| Hash | Tipo | Subject |
|---|---|---|
| `2c8fa50` | docs | `docs(audit): record v15 stabilization report` (3 file, +1.122 righe) |
| `3288871` | fix | `fix(templates): convert multi-line {# #} comments to {% comment %} blocks` (26 file, +123/-57) |
| `5017043` | fix | `fix(commerce): close StorefrontMember.id migration drift` (1 file, +18) |
| `570fea0` | docs | `docs(audit): record post-fix test run logs (681/681 OK)` (2 file, +883) |

Tutti i commit sono atomici, hanno messaggio descrittivo del "perché", nessun `--no-verify`, nessun bypass dei pre-commit hook.

## 4. Verifica segreti nei file dei 2 commit `docs(audit)`

Pattern scansionati su tutti i file aggiunti: `password=`, `secret_key=`, `api_key=`, `token=`, `sk_live`, `sk_test`, `AKIA`, `BEGIN.+PRIVATE`, `sessionid`, `csrftoken`, `django-insecure-<value>`, `AUTH_TOKEN`, `SENTRY_DSN`, `STRIPE_*`, cookie strings.

**Risultato:** 0 match reali. L'unica menzione di `SECRET_KEY` nei log è il messaggio standard del warning Django (`"dev-only SECRET_KEY fallback. Set DJANGO_SECRET_KEY..."`) — testo del warning, non un valore.

## 5. Fix P1.1 — Comment leakage in template Django

### Causa radice
Django parsa `{# ... #}` come commento SOLO quando apertura e chiusura sono sulla stessa riga (docs Django: "*A comment cannot span multiple lines*"). Quando un `{#` non trova `#}` prima del newline, il parser lo emette come testo letterale.

In `templates/base.html` (e in 24 altri template) i blocchi `{# T43 · ... #}` multilinea erano renderizzati come testo dentro `<head>` su **ogni pagina pubblica**, esponendo ~2 KB di commenti interni nel page source.

### Fix
28 blocchi multi-line convertiti in `{% comment %} ... {% endcomment %}` su 25 file:
- `templates/base.html` — 4 blocchi (canonical, og:image, twitter card, JSON-LD)
- `templates/pages/home.html` — 1 blocco
- `templates/catalog/template_list.html` — 1
- `templates/catalog/template_detail.html` — 1
- `templates/preview_compositions/<categoria>/<archetipo>.html` — 21 file × 1 blocco

Line endings normalizzati a LF per non inquinare il diff (Windows Python di default scrive CRLF).

### Test regression
Nuovo `apps/pages/tests.py::TemplateCommentLeakageRegressionTests` che fetcha `/`, `/templates/`, `/templates/categories/` e fallisce se il regex `\{#(?:(?!#\}).)*\n` matcha. Decorato con `@override_settings(AXES_ENABLED=False)` per non interferire con i rate-limit.

### Verifica
Sweep curl su 13 URL distinti (home, templates list, categories, 8 verticali, preview IT, preview AR) → 0 match di leakage. Browser snapshot Playwright su home + cardio-detail + cardio-preview: l'elemento `generic [active]` non contiene più la stringa `{# T43 · ...` come testo.

## 6. Fix P1.2 — Migration drift `commerce.StorefrontMember.id`

### Causa radice
La migration `0003_commerce_v2.py` ha creato `StorefrontMember` con:
```python
("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False))
```
mancando `verbose_name='ID'`, che Django attacca implicitamente a ogni pk auto. Lo state engine vede quindi drift → segnala `AlterField`.

Il drift è **metadata only**: `verbose_name` è usato solo per le label dell'admin, non incide sullo schema DB. Confermato leggendo la migration generata: l'unico cambio è l'aggiunta di `verbose_name='ID'`.

### Fix
Generata `apps/commerce/migrations/0004_alter_storefrontmember_id.py` via `manage.py makemigrations commerce` standard. Applicata con `manage.py migrate` senza errori.

### Verifica
`python manage.py makemigrations --check --dry-run` ora ritorna **`No changes detected`** — drift chiuso.

## 7. Controlli post-fix

| Controllo | Esito | Note |
|---|---|---|
| `python manage.py check` | ✅ OK | 5 warning `corporate_suite.W003` invariati, safe-degraded |
| `python manage.py makemigrations --check --dry-run` | ✅ `No changes detected` | drift commerce chiuso |
| Full test suite `python manage.py test` | ✅ **681 / 681 OK** (183s) | +1 vs Fase 2 (nuovo regression test) |
| Test mirati `apps.pages apps.commerce` | ✅ 1/1 OK | commerce ha 0 unit test propri (debt P3) |

## 8. Browser QA post-fix

Server riavviato dopo la modifica template (task `bcwi4vigh`, porta 8000).
URL verificati nel browser + curl sweep:

| URL | HTTP | Leakage matches | Esito |
|---|---|---|---|
| `/` | 200 | 0 | ✅ |
| `/templates/` | 200 | 0 | ✅ |
| `/templates/categories/` | 200 | 0 | ✅ |
| `/templates/medical/` | 200 | 0 | ✅ |
| `/templates/medical/cardio-studio-specialistico/` | 200 | 0 | ✅ |
| `/templates/medical/cardio-studio-specialistico/preview/` | 200 | 0 | ✅ |
| `/templates/medical/cardio-studio-specialistico/preview/?lang=ar` | 200 | 0 | ✅ titolo `Studio Marani — المركز` |
| `/templates/agency/` | 200 | 0 | ✅ |
| `/templates/business/` | 200 | 0 | ✅ |
| `/templates/lawyer/` | 200 | 0 | ✅ |
| `/templates/restaurant/` | 200 | 0 | ✅ |
| `/templates/portfolio/` | 200 | 0 | ✅ |
| `/templates/real-estate/` | 200 | 0 | ✅ |
| `/templates/ecommerce/` | 200 | 0 | ✅ |

**Screenshot Playwright** (gitignored come `*.png`): `qa-post-01-home-clean.png`, `qa-post-02-cardio-detail-clean.png`, `qa-post-03-cardio-preview-clean.png`, `qa-post-04-cardio-ar-rtl-clean.png`.

**Console errors:** zero su tutte le pagine (a parte il favicon.ico 404 noto e tracciato come P3 RR5).

## 9. File modificati / aggiunti in Fase 2.1

### Modificati (26 file)
- `templates/base.html`
- `templates/pages/home.html`
- `templates/catalog/template_list.html`
- `templates/catalog/template_detail.html`
- `templates/preview_compositions/agency/{agency-creative-studio,agency-digital-studio}.html`
- `templates/preview_compositions/business/{corporate-suite,startup-saas-landing}.html`
- `templates/preview_compositions/ecommerce/{artisan-workshop,fashion-editorial}.html`
- `templates/preview_compositions/lawyer/{classic-gold,modern-transparent}.html`
- `templates/preview_compositions/medical/{clinic,family,specialist,specialist-cardio,specialist-derm,wellness}.html`
- `templates/preview_compositions/portfolio/{cinematic-photographer,editorial-designer-grid}.html`
- `templates/preview_compositions/real-estate/{mass-market,ultra-luxury-cinematic}.html`
- `templates/preview_compositions/restaurant/{fine-dining,street-modern,trattoria-warm}.html`
- `apps/pages/tests.py` (regression test)

### Nuovi (6 file)
- `apps/commerce/migrations/0004_alter_storefrontmember_id.py`
- `docs/AUDIT_REPORT_2026-05-13_PHASE2_STABILIZATION.md`
- `docs/AUDIT_REPORT_2026-05-13_PHASE2_1_PRE_MERGE_HARDENING.md` (questo)
- `docs/audit/2026-05-13/ruff_stats.txt`
- `docs/audit/2026-05-13/test_run.log`
- `docs/audit/2026-05-13/test_run_post_fix.log`
- `docs/audit/2026-05-13/test_targeted.log`

## 10. Rischi residui post Fase 2.1

| # | Severità | Descrizione | Stato |
|---|---|---|---|
| RR1 | ~~P1~~ → **chiuso** | Template comment leakage | Risolto da `3288871` + test regression |
| RR2 | ~~P1~~ → **chiuso** | Migration drift commerce | Risolto da `5017043` |
| RR3 | P2 | 3 entry registry magre (lex/juris/villa) | Documentato in Phase 2 §4 — fix lavorabile post-merge |
| RR4 | P2 | Travel category pending (no skin folder) | Phase D roadmap |
| RR5 | P3 | favicon.ico 404 | Aggiungere route fallback o file fisico |
| RR6 | P3 | Deuda formale (147 ruff + 247 black) | PR dedicato post-merge |
| RR7 | P2 | 60+ worktree git aperti | Cleanup con OK utente |
| RR8 | P2 | Listing UI dice "32" vs registry 33 / DB 30+1 | Audit numerico DB ↔ UI |

**Nessun P0. Nessun P1 aperto.** Tutti i finding sono P2 / P3 e non bloccanti per il fast-forward merge.

## 11. Raccomandazione finale

✅ **v15 READY per fast-forward merge verso master.**

### Pre-merge checklist (allineato a Decisione 6 del briefing)
Prima del merge, mostrerò:
1. `git branch --show-current` (deve essere `master` dopo il checkout)
2. `git rev-parse master` (l'hash attuale di master, presumibilmente ancora `9736da4`)
3. il comando esatto del tag: `git tag v0.1-pre-mvp-master-2026-05-13 <hash-master>`
4. il comando esatto del merge: `git merge --ff-only phase-x7e-lf2-variance-and-causa-retrofit`

Eseguirò solo dopo tuo OK esplicito.

### Server status alla chiusura
- **Stato:** ATTIVO
- **Porta:** `8000`
- **URL base:** `http://127.0.0.1:8000`
- **Background task ID:** `bcwi4vigh` (precedente `bcqg5vj4o` e `blhqw8pze` stoppati nella sessione)
- **Settings:** `marketweb.settings` profilo dev
- **DB:** SQLite, migrations 100% applicate (incluso 0004 commerce)
- **Templates:** post-fix LF-normalized, zero leakage

Per arresto manuale: `taskkill /F /PID <pid>` dopo `netstat -ano | findstr :8000`.
