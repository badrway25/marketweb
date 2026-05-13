# Audit Report — Phase 2: Stabilization (v15)

**Data:** 2026-05-13
**Branch:** `phase-x7e-lf2-variance-and-causa-retrofit`
**Modalità:** modifiche solo su v15, master read-only
**Esito:** verde con 2 finding P1 minori (non bloccanti)
**Raccomandazione:** v15 **PRONTO** per fast-forward merge verso master, dopo OK utente

---

## 1. Stato Git

### Iniziale (pre Fase 2)
- Branch: `phase-x7e-lf2-variance-and-causa-retrofit`
- HEAD: `8ef3970` ("X.6 workflow C: ship Causa multilingual rollout")
- Working tree: 66 file modificati + 85 untracked critici (settings package, audit infra, 8 brand pack, Dockerfile, error templates, ecc.)
- Diff stat: +11.727 / −5.703 righe
- 0 stash, 254 commit ahead of master

### Finale (post Fase 2)
- Branch: `phase-x7e-lf2-variance-and-causa-retrofit`
- HEAD: `35cc16a` ("chore(snapshot): preserve in-flight WIP before phase-2 stabilization")
- 152 file/+74.781 −5.703 nel commit snapshot
- Working tree pulito (solo 2 artefatti audit untracked: `docs/audit/2026-05-13/ruff_stats.txt`, `test_run.log` — committabili a fine fase)
- 0 stash, 255 commit ahead of master

---

## 2. Salvataggio WIP X.6 (composito)

### Patch backup (commit-safe)
Triple safety net creato in `docs/audit/2026-05-13/`:
| File | Dimensione | Contenuto |
|---|---|---|
| `wip_modified_files.patch` | 1.049 KB | `git diff HEAD` completo dei 66 file modificati |
| `wip_untracked_archive.tar.gz` | 932 KB | Archivio compresso degli 85 file untracked |
| `wip_untracked_files.txt` | 3,1 KB | Lista untracked |
| `wip_initial_status.txt` | 5,9 KB | Snapshot `git status -uall --porcelain` |

### Strategia scelta: commit snapshot (non stash)
**Motivazione:** lo stash avrebbe rimosso `marketweb/settings/` (untracked) lasciando `asgi.py`/`urls.py` (modificati per importare il nuovo package) con import rotti — Django non sarebbe potuto partire.

### Commit
```
35cc16a chore(snapshot): preserve in-flight WIP before phase-2 stabilization
```
Reversibile con `git reset --soft HEAD~1`. Include:
- Sprint 0 deploy baseline (Dockerfile, docker-compose.yml, settings split, error templates)
- Security hardening T19-T43 (Sentry, WhiteNoise, axes, OTP, CSP, audit log)
- 8 nuovi brand content pack (albergo, atto, denti, gemma, madou, petro, podere, sapori) × 5 locale
- X.5-X.7 retrofit content (casa, lex, pragma, salute, causa)
- Phase 1 audit report

---

## 3. Ambiente Python

### Venv dedicato
- Path: `.venv-v15/` (interno al worktree v15)
- Python: 3.13.5
- pip: aggiornato 25.1.1 → 26.1.1
- Vecchio `.venv` condiviso (disallineato, aveva Django 6.0.4) **non toccato**

### Dipendenze installate (61 pacchetti)
Tutte le versioni richieste in `requirements.txt`:
- Django **5.2.7** LTS, djangorestframework 3.16.1, drf-spectacular 0.29.0
- django-axes 7.0.2, django-otp 1.7.0 (T23/T27)
- celery 5.6.2, django-celery-beat 2.9.0
- stripe 14.1.0, Pillow 12.1.0
- psycopg 3.2.3 + binary, gunicorn 23.0.0, whitenoise 6.8.2, sentry-sdk 2.19.2
- ruff 0.15.9, black 26.3.1, pytest 9.0.3
- crispy-bootstrap5 2026.3, django-crispy-forms 2.6

---

## 4. Risultati controlli

### `manage.py check` — **OK**
5 warning controllati, tutti `corporate_suite.W003` (accent contrast) sui template:
- `causa-legale` (1.46:1), `continua-stewardship` (3.88:1), `cornice-architettura` (3.03:1), `fiscus-commercialista` (1.30:1), `solaria-coaching` (2.45:1)

Tutti **safe-degraded** via token `--accent-text-on-primary-safe` in `apps.catalog.theme_safety`. Dichiarati "no remediation blocks CI". Zero ERROR.

### `manage.py makemigrations --check --dry-run` — **1 finding P1**
```
Migrations for 'commerce':
  apps/commerce/migrations/0004_alter_storefrontmember_id.py
    ~ Alter field id on storefrontmember
```
Migration di drift su `commerce.StorefrontMember.id`. Da generare in una fase successiva (non bloccante per il merge: l'attuale dev/test funziona perché `--run-syncdb` ha applicato gli `id` di default).

### `manage.py test` — **680 / 680 OK** (192,3 s)
```
Found 680 test(s).
Ran 680 tests in 192.284s
OK
```
Zero fail, zero error. Test DB seeded automaticamente da `seed_templates` (30 published_live + 1 draft, 2 entry travel skip per assenza skin).

### `ruff check .` — **147 finding (non bloccanti)**
Breakdown:
| Categoria | Count | Auto-fix |
|---|---|---|
| F401 unused-import | 48 | sì |
| F541 f-string-missing-placeholders | 38 | sì |
| E701 multiple-statements-on-one-line | 20 | no |
| E402 module-import-not-at-top | 13 | no |
| F841 unused-variable | 13 | no |
| E401 multiple-imports-on-one-line | 7 | sì |
| E731 lambda-assignment | 5 | no |
| E702 multiple-statements-semicolon | 3 | no |

93/147 auto-fixable. Zero finding di sicurezza/correttezza.

### `black --check` — **247 file da riformattare** (vs 56 conformi)
La codebase non è black-formatted. Auto-fixable con `black .` (esclusioni `.venv-v15`, `factory/reports`, `design-orchestrator`, `127-design`).

### Audit registry ↔ skin folders — **3 P1 + 2 P2**

**Skin tree su disco:** 8 verticali, 19 archetypi (agency 2, business 2, ecommerce 2, lawyer 2, medical 4, portfolio 2, real-estate 2, restaurant 3).

**Registry:** 33 template in 9 categorie (aggiunge `travel`).

**P1 — registry incomplete** (3 template `published` senza `archetype`/`live_preview`/`live_pages`):
- `lex-studio-legale` (lawyer)
- `juris-avvocato-moderno` (lawyer)
- `villa-immobili-lusso` (real-estate)

I file skin esistono e funzionano (verificato in browser), ma le entry registry sono "magre" rispetto agli altri 30 template. Pages live navigano via fallback. Da arricchire per coerenza dati.

**P2 — travel pending** (skin folder mancante):
- `albergo-borgo` → expects `travel/ultra-luxury-cinematic`
- `podere-agriturismo` → expects `travel/artisan-workshop`

Entry registry corrette, ma `templates/live_templates/travel/` non esiste ancora. `seed_templates` correttamente skippa con messaggio `(not in DB, skipped)`. Phase D nel roadmap.

**Orphan archetypes su disco** (esistono ma nessuna entry registry li punta esplicitamente):
- `lawyer/modern-transparent` — verosimilmente usato da `juris` via fallback
- `real-estate/ultra-luxury-cinematic` — verosimilmente usato da `villa` via fallback

---

## 5. Tracking staticfiles/ e db.sqlite3

| Risorsa | On disk | Tracciato | `.gitignore` | Esito |
|---|---|---|---|---|
| `db.sqlite3` | 1.003 KB | NO | `db.sqlite3` (riga 18) | **OK** (rischio R4 chiuso) |
| `staticfiles/` | esiste | NO | `/staticfiles/` (riga 20) | **OK** (rischio R3 chiuso) |
| `media/` | esiste | NO | `/media/` (riga 22) | **OK** |
| `.env*` (real) | nessuno | NO | `.env`, `.env.local`, `.env.production` | **OK** |
| `*.png` | screenshots locali | 0 PNG tracciati | `*.png` (riga 51) | **OK** |

Tutti i rischi di tracking sospettati in Fase 1 (R3, R4) si sono rivelati **non-issue**: il `.gitignore` di v15 è già strutturato correttamente.

---

## 6. Browser QA — 10 pagine verificate

**Server:** `runserver 8000 --noreload` in background (task id `bcqg5vj4o`), DEBUG=1, dev settings.
**URL base:** `http://127.0.0.1:8000`
**Status:** ancora attivo a fine sessione, pronto per ispezione manuale.

| # | URL | Pagina | HTTP | Title | Console errors | Note |
|---|---|---|---|---|---|---|
| 1 | `/` | Home IT | 200 | "Home — Template Web Premium" | 1 (favicon.ico 404) | Hero "Il sito web della tua professione" + "32+ template premium · 52 professioni · 5 lingue" |
| 2 | `/templates/` | Templates list | 200 | "Template — Template Web Premium" | 0 | "32 template disponibili", filtri, paginazione |
| 3 | `/templates/categories/` | Categories list | 200 | "Categorie — Template Web Premium" | 0 | — |
| 4 | `/templates/medical/` | Category medical | 200 | "Medico — Template — Template Web Premium" | 0 | — |
| 5 | `/templates/medical/cardio-studio-specialistico/` | Template detail | 200 | "Cardio — Studio Specialistico — Template Web Premium" | 0 | — |
| 6 | `/templates/medical/cardio-studio-specialistico/preview/` | Live preview IT | 200 | "Studio Marani — Studio" | 0 | Brand-applied multi-page |
| 7 | `/templates/medical/cardio-studio-specialistico/preview/?lang=ar` | Live preview AR/RTL | 200 | "Studio Marani — المركز" | 0 | Title arabo, da verificare layout |
| 8 | `/account/login/` | Login | 200 | "Accedi — Template Web Premium" | 0 | — |
| 9 | `/templates/lawyer/lex-studio-legale/` | Lawyer detail | 200 | "Lex — Studio Legale — Template Web Premium" | 0 | — |
| 10 | `/templates/business/pragma-corporate-suite/preview/` | Business preview | 200 | "Pragma Advisors — Studio" | 0 | — |

**Auth gate verificato:** `/projects/` redireziona correttamente a `/account/login/?next=/projects/`.

**Screenshot salvati nel worktree v15** (root): `qa-01-home-it.png`, `qa-02-templates-list.png`, ..., `qa-10-business-pragma-preview.png`. Da gitignore esistente `*.png` non vanno in commit.

---

## 7. Anomalie trovate durante Phase 2

### P1 — Template comment leakage (Django syntax)
**File:** `templates/base.html` righe 11-15, 24-28, 31-36, 74-79.
**Problema:** I commenti `{# T43 · ... #}` sono **multi-line**, mentre la sintassi `{# #}` di Django è **single-line only** (vedi docs Django). Risultato: i ~2KB di testo dei commenti vengono renderizzati come testo dentro `<head>` su **ogni pagina pubblica**.
**Impatto:**
- SEO: text node spuri tra meta tag possono confondere alcuni crawler
- Page weight: ~2KB inutili × N pagine
- Professionalità: la fonte della pagina espone commenti interni dello sviluppatore
**Fix proposto:** convertire ogni blocco `{# ... #}` multi-line in `{% comment %}...{% endcomment %}`. Stesso fix in `templates/pages/home.html:7` (e qualsiasi altro multi-line `{# #}` da grepare).
**Severità:** P1 (visibile su tutte le pagine pubbliche, fix banale).

### P1 — Migration drift `commerce.StorefrontMember.id`
`makemigrations --check` segnala `~ Alter field id on storefrontmember`. Da generare con `python manage.py makemigrations commerce` e applicare. Non bloccante per dev/test ma necessario per deploy pulito.

### P2 — Registry data quality
3 template (`lex-studio-legale`, `juris-avvocato-moderno`, `villa-immobili-lusso`) sono `published` ma senza `archetype`/`live_preview`/`live_pages` nel registry. Le pagine funzionano per fallback, ma la coerenza dati è rotta.

### P2 — Travel category pending
`albergo-borgo` e `podere-agriturismo` registry-only senza skin folder. Phase D del roadmap. Fix attuale: filtrare dal seed o aggiungere flag `pending_implementation` per non comparire come 33 template "live" quando in DB sono 32.

### P3 — Favicon fallback
`base.html` linka solo `favicon.svg`. Browser legacy richiede `favicon.ico` → 404 in console. Aggiungere route `/favicon.ico` o un file fisico per silenziare.

### P3 — Deuda formale
- ruff 147 finding (93 auto-fix con `ruff check --fix`)
- black: 247 file da riformattare (`black .` risolve)
Nessun impatto runtime, ma misura di igiene professionale.

---

## 8. File modificati durante Phase 2

| File | Tipo | Motivo |
|---|---|---|
| `docs/AUDIT_REPORT_2026-05-13_PHASE1_COMPARATIVE_BASELINE.md` | nuovo | Report Fase 1 |
| `docs/AUDIT_REPORT_2026-05-13_PHASE2_STABILIZATION.md` | nuovo (questo) | Report Fase 2 |
| `docs/audit/2026-05-13/wip_modified_files.patch` | nuovo | Backup WIP |
| `docs/audit/2026-05-13/wip_untracked_archive.tar.gz` | nuovo | Backup untracked |
| `docs/audit/2026-05-13/wip_untracked_files.txt` | nuovo | Lista untracked |
| `docs/audit/2026-05-13/wip_initial_status.txt` | nuovo | Stato git iniziale |
| `docs/audit/2026-05-13/ruff_stats.txt` | nuovo | Stat lint |
| `docs/audit/2026-05-13/test_run.log` | nuovo | Log test |

**Nessuna modifica al codice produttivo** è stata fatta. L'unico commit creato (`35cc16a`) è uno snapshot atomico del WIP preesistente — non scrive logica nuova, solo conserva quella già nel working tree.

---

## 9. Rischi residui

| # | Severità | Descrizione | Mitigazione |
|---|---|---|---|
| RR1 | **P1** | Template comment leakage in `base.html` | Fix banale `{# %}` → `{% comment %}`. Non bloccante per merge ma da fixare presto |
| RR2 | **P1** | Migration drift commerce.StorefrontMember | `makemigrations commerce` + commit + migrate |
| RR3 | P2 | Registry P1 (3 template magri: lex/juris/villa) | Arricchire entry con archetype/live_preview/live_pages |
| RR4 | P2 | Travel pending (2 brand senza skin) | Filtrare o flag `pending_implementation` |
| RR5 | P3 | favicon.ico 404 | Aggiungere fallback |
| RR6 | P3 | Deuda formale ruff/black | `ruff --fix` + `black .` in PR dedicato |
| RR7 | P2 | 60+ worktree git aperti | Cleanup pianificato (con OK utente) |
| RR8 | P2 | Catalog reads "32 template disponibili" su listing ma registry dice 33 published | 33 registry − 1 ancora draft − 2 travel skip = 30 in DB; UI mostra 32. Da audit DB ↔ UI numerico |

Nessun **P0** identificato. Server live e stabile.

---

## 10. Raccomandazione finale per FF-merge

✅ **v15 PRONTO per fast-forward merge verso master**, alle seguenti condizioni:

1. **OK utente** sul commit snapshot `35cc16a` (lo conservo o lo ricompongo in commit logici prima del merge?)
2. **Fix RR1 + RR2 prima del merge?** (consigliato: sì, sono fix banali e RR1 è visibile in produzione)
3. Strategia confermata: `git checkout master && git merge --ff-only phase-x7e-lf2-variance-and-causa-retrofit`
4. Tag preventivo del vecchio master: `git tag v0.1-pre-mvp 9736da4` per non perdere il riferimento storico
5. NO force-push, NO branch delete senza ulteriore OK

### Cosa NON è stato fatto (da Fase 3 in avanti, con tua autorizzazione)
- Fix RR1 (comment leakage)
- Fix RR2 (migration drift)
- Arricchimento registry RR3
- Cleanup worktree RR7
- Audit UI/UX premium sui 33 brand
- Editor end-to-end QA
- Hardening prod settings (CSP enforce, SSL redirect)
- Performance audit (N+1, asset weight)
- Accessibilità WCAG 2.1 AA pass

---

## 11. Server status alla chiusura

- **Stato:** **ATTIVO**
- **Porta:** `8000`
- **URL base:** `http://127.0.0.1:8000`
- **Background task ID:** `bcqg5vj4o`
- **Settings module:** `marketweb.settings` (dev profile via `__init__.py` → `.dev`)
- **DB:** SQLite `db.sqlite3` (15 categorie, 33 WebTemplate, 32 live)
- **Migrazioni:** applicate (con un warning su commerce drift, vedi RR2)

Per fermarlo manualmente: vedi `taskkill /F /PID <pid>` dopo `netstat -ano | findstr :8000`.
