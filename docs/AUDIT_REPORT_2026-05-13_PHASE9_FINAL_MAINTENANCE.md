# Audit Report — Phase 9 (Final Maintenance)

**Data:** 2026-05-14
**Modalità:** maintenance post-cleanup — investigazione branch remoto, drop stash safe, pulizia orphan dir, ricreazione venv
**Esito:** ✅ repository operativo dal worktree principale, test suite green, stash droppato con backup, orphan dir svuotata

---

## 1. Esito investigazione `origin/phase-x4-continua-public-flip`

**Lavoro fatto:** solo read-only (`git log`, `git diff --stat`, `git diff --name-status`). Nessun merge, nessun cherry-pick, nessuna delete.

### 1.1 Commit unico
- SHA: `8b3ccc1`
- Tag attic già esistente: `attic/phase9/phase-x4-continua-public-flip/2026-05-13` (creato in Phase 9.D)
- Subject: `X.5 LF-2: define Cornice fifth sibling pilot and distinctness proof`

### 1.2 Diff vs `origin/master`
```
427 files changed, 7,374 insertions(+), 139,224 deletions(-)
```

### 1.3 Interpretazione
La massiva **deletion** (139k righe rimosse) indica che il branch è un **fossile antico** rispetto a master, NON che ha lavoro unico. Files come `.dockerignore`, `.env.example`, `.github/workflows/ci.yml`, `Dockerfile`, `apps/catalog/sitemaps.py`, `apps/accounts/management/commands/setup_admin_totp.py`, le migration `0007_cornice_layout_family.py` / `0008_causa_layout_family.py`, e ~30 moduli `template_content_<brand>_<locale>.py` appaiono come "deleted" nel branch vs master — significa che il branch è stato creato PRIMA che master integrasse tutto questo lavoro (Sprint 0 + X.4-X.7).

Il "1 commit unico" `8b3ccc1` è la **definizione iniziale** del pilot Cornice LF-2, lavoro che è stato poi rifuso/rifatto in master attraverso la pipeline `phase-x5-cornice-*` (interamente integrata in master e ora cancellata in Phase 7/9).

### 1.4 Decisione raccomandata
**ARCHIVE-CANDIDATE — safe da rimuovere quando vorrai.** Il commit unico è già preservato in 2 luoghi:
1. Tag locale `attic/phase9/phase-x4-continua-public-flip/2026-05-13`
2. Il branch remoto stesso `origin/phase-x4-continua-public-flip`

**Quando rimuoverlo:** dopo aver verificato che il tag attic locale è davvero raggiungibile e nessun tool/CI esterno fa più reference al remoto. Comando: `git push origin --delete phase-x4-continua-public-flip` (richiede tuo OK separato).

**Per ora resta non toccato come da regola Phase 9.**

---

## 2. Drop `stash@{0}`

### 2.1 Verifica pre-drop

```
git stash list -n 3:
  stash@{0}: On master: WT cosmetic drift on master before FF merge 2026-05-13

git stash show --stat stash@{0}:
  apps/accounts/migrations/0001_initial.py |  90 ++++++-------
  apps/catalog/migrations/0001_initial.py  | 208 +++++++++++++++----------------
  2 files changed, 149 insertions(+), 149 deletions(-)
```

Contenuto verificato: solo cosmetic drift (timestamp Django autogenerato `2026-04-09 16:15` → `17:37` + line endings CRLF → LF) su 2 file di migration. **Nessun cambio di schema o codice funzionale.**

### 2.2 Backup creato pre-drop
- Path: `C:/tmp/sitoBadr2/_marketweb_cleanup_backups/2026-05-13-phase9/stash-cosmetic-drift/`
- File salvati: `stash.patch` (18.445 byte, 308 righe), `stash-stat.txt` (196 byte), `stash-list.txt` (77 byte)
- Verificato: la patch contiene il diff completo recuperabile manualmente in qualsiasi momento via `git apply` sul backup

### 2.3 Drop eseguito
```
$ git stash drop stash@{0}
Dropped stash@{0} (44a7eff6b7ce86955369c3e7e0934de45914b04f)

$ git stash list
(empty)
```

✅ Stash droppato. Repository ora ha 0 stash.

---

## 3. Orphan dir v15 cleanup

### 3.1 Verifica safety pre-delete
- ✅ `git worktree list` mostra solo `C:/tmp/sitoBadr2/marketweb` — orphan v15 NON è più worktree git attivo
- ✅ `Test-Path C:/tmp/sitoBadr2/mw-integration-baseline-v15` → True (esisteva)
- ✅ Path target ≠ `C:/tmp/sitoBadr2/marketweb` (verificato esplicitamente)
- ✅ Dimensione pre-delete: **775,6 MB** (Get-ChildItem -Recurse sum)
- ✅ Backup top-level salvato in `_marketweb_cleanup_backups/2026-05-13-phase9/orphan-v15-pre-delete-inventory/top-level-ls.txt` (58 entry top-level)

### 3.2 Esecuzione
1. **Step 1:** `Remove-Item -Path "$orphan" -Recurse -Force` (PowerShell)
   - Risultato: ~99% rimosso, ma residui 573 file `node_modules/.pnpm/...` (path molto lunghi)
2. **Step 2:** `rm -rf C:/tmp/sitoBadr2/mw-integration-baseline-v15` (bash MSYS)
   - Risultato: tutti i 573 file ripuliti, **0 file rimasti, 0 byte di contenuto**
   - Però la directory in sé non si rimuove: `rm: cannot remove: Device or resource busy`

### 3.3 Stato finale
- ⚠️ **Phantom empty dir** persiste: `C:/tmp/sitoBadr2/mw-integration-baseline-v15` esiste come cartella vuota inerte (0 byte)
- Causa probabile: lock di Windows file system (antivirus / file indexer / handle residuo)
- **Impatto:** zero — la dir non contiene niente, non interferisce con Git, non occupa spazio reale
- **Risoluzione manuale (opzionale):** rimuovibile in qualsiasi momento via `rmdir` dopo riavvio, oppure via Explorer

### 3.4 Spazio recuperato
**~775 MB liberati** (venv-v15 + nested .git my-voltagent-app/skills + altri file v15). Loss controllata: ricostruibile da `requirements.txt` + ri-clone tool esterni se mai servissero.

---

## 4. Ricreazione `marketweb/.venv`

### 4.1 Ambiente
- **Path:** `C:/tmp/sitoBadr2/marketweb/.venv/`
- **Comando creazione:** `python -m venv C:/tmp/sitoBadr2/marketweb/.venv`
- **Python:** **3.13.5** (system: `C:/Python313/python.exe`)
- **pip:** aggiornato 25.1.1 → 26.1.1
- **Gitignored:** ✅ (`.gitignore` esclude `.venv/`)

### 4.2 Dipendenze installate (61 pacchetti)
Tutte coerenti con `requirements.txt`:

```
Django==5.2.7 (LTS, conforme target)
djangorestframework==3.16.1
drf-spectacular==0.29.0
django-filter==25.2
django-crispy-forms==2.6
crispy-bootstrap5==2026.3
Pillow==12.1.0
stripe==14.1.0
celery==5.6.2
django-celery-beat==2.9.0
psycopg==3.2.3 + psycopg-binary==3.2.3
gunicorn==23.0.0
sentry-sdk==2.19.2
whitenoise==6.8.2
django-axes==7.0.2
django-otp==1.7.0
black==26.3.1
ruff==0.15.9
pytest==9.0.3
+ deps transitive: amqp, asgiref, attrs, billiard, certifi, charset_normalizer,
  click + click-{didyoumean,plugins,repl}, colorama, cron-descriptor,
  django-timezone-field, idna, inflection, iniconfig, jsonschema +
  jsonschema-specifications, kombu, mypy-extensions, packaging, pathspec,
  platformdirs, pluggy, prompt-toolkit, pygments, python-crontab,
  python-dateutil, pytokens, PyYAML, referencing, requests, rpds-py,
  six, sqlparse, typing_extensions, tzdata, tzlocal, uritemplate, urllib3,
  vine, wcwidth
```

### 4.3 Verifiche operative

| Check | Esito |
|---|---|
| `python manage.py check` | ✅ verde — 5 warning `corporate_suite.W003` invariati (safe-degraded, già noti) |
| `python manage.py makemigrations --check --dry-run` | ✅ **No changes detected** |
| `python manage.py test --verbosity=1` | ✅ **681 tests OK in 188.7s** |

Log completo salvato in `docs/audit/2026-05-13/test_run_phase9_maintenance.log`.

### 4.4 Coerenza con Phase 2 baseline
- Stesso conteggio test (681) ✅
- Stessa Django version (5.2.7 LTS) ✅
- Stesse warning safe-degraded (`causa-legale`, `continua-stewardship`, `cornice-architettura`, `fiscus-commercialista`, `solaria-coaching` per W003) ✅
- Nessuna regression rispetto al venv-v15 del Phase 2 ✅

---

## 5. Stato Git finale

```
On branch master
nothing to commit (modulo 1 file untracked: log test di questa fase)

HEAD = 5bf4422ec55e4ca32c6dc11cb2b467860f5ee361
origin/master = 5bf4422ec55e4ca32c6dc11cb2b467860f5ee361
sync = YES

worktree: 1 — C:/tmp/sitoBadr2/marketweb [master]
branch locali: 1 — master
branch remoti: 3 + 1 simbolico
  - origin/master                              5bf4422 (KEEP)
  - origin/phase-integration-baseline-v15      5bf4422 (KEEP temporaneo)
  - origin/phase-x4-continua-public-flip       8b3ccc1 (KEEP — investigato, archive-candidate futuro)
  - origin/HEAD -> origin/master               (puntatore simbolico)
stash: 0 (droppato in §2)
tag: 14 totali
  - 2 originali: v0.1-pre-mvp-master-2026-05-13, a2-4-deterministic-field-targeting-stable
  - 12 attic/phase9/.../2026-05-13 (safety net)
.venv: ✅ ricreato in marketweb/.venv, 681/681 test OK
```

---

## 6. Branch locali finali (1)
- `master` (HEAD `5bf4422`)

## 7. Branch remoti finali (3 + simbolico)
- `origin/master` — KEEP
- `origin/phase-integration-baseline-v15` — KEEP temporaneo (1-2 settimane, come da decisione utente)
- `origin/phase-x4-continua-public-flip` — KEEP, archive-candidate futuro
- `origin/HEAD -> origin/master` — puntatore simbolico

## 8. Worktree finali (1)
- `C:/tmp/sitoBadr2/marketweb` (master)

---

## 9. Conferme di sicurezza

| Verifica | Esito |
|---|---|
| Nessun force push usato | ✅ |
| Nessun reset/rebase/squash | ✅ |
| Nessun branch remoto cancellato in questa fase | ✅ (i 29 erano già stati cancellati in Phase 9.E precedente) |
| `origin/phase-integration-baseline-v15` non toccato | ✅ |
| `origin/phase-x4-continua-public-flip` non toccato (solo investigato read-only) | ✅ |
| Tag `v0.1-pre-mvp-master-2026-05-13` intatto | ✅ |
| Tag `a2-4-deterministic-field-targeting-stable` intatto | ✅ |
| 12 tag attic intatti | ✅ |
| `master` e `origin/master` intatti | ✅ |
| Backup stash creato PRIMA del drop | ✅ in `_marketweb_cleanup_backups/2026-05-13-phase9/stash-cosmetic-drift/` |
| Backup orphan v15 (top-level listing) creato PRIMA del delete | ✅ |
| Backup NON committati nel repo | ✅ (sotto `_marketweb_cleanup_backups/`, esterno) |
| Nessun token/credenziale stampato | ✅ |

---

## 10. Raccomandazione prossima fase

Il repository è ora **operativamente snello e pronto per il lavoro di sviluppo**. Possibili direzioni:

### 10.A — Lavoro di prodotto (priorità alta)
1. **Phase A — Editor Foundation** (gate D-085 per nuove categorie/template)
2. **Fix RR3 (registry magre lex/juris/villa)** — arricchire entry registry
3. **Fix RR5 (favicon.ico 404)** — aggiungere fallback
4. **Phase B — Trades + Local food retail** (catalog expansion §9 della roadmap)

### 10.B — Cleanup formale (priorità bassa)
1. **Deuda formale ruff (147) + black (247 file)** — PR cleanup dedicato
2. **Eliminazione `origin/phase-integration-baseline-v15`** dopo 1-2 settimane (decisione utente)
3. **Eliminazione `origin/phase-x4-continua-public-flip`** dopo confirmation che il commit unico è davvero ridondante
4. **Rimozione phantom empty dir** `C:/tmp/sitoBadr2/mw-integration-baseline-v15` (`rmdir` dopo riavvio o via Explorer)

### 10.C — Manutenzione opzionale
- `git gc` standard (non `--aggressive`) per packing
- Verifica setup CI workflow `.github/workflows/ci.yml` sul nuovo default branch master

---

## 11. Operazioni NON eseguite (per rispetto delle regole)

- ❌ Force push mai usato
- ❌ Nessun reset/rebase/squash
- ❌ Nessun branch remoto cancellato in questa sotto-fase
- ❌ `origin/phase-integration-baseline-v15` non toccato
- ❌ `origin/phase-x4-continua-public-flip` non cancellato (solo investigato)
- ❌ Tag non toccati
- ❌ `master` / `origin/master` intatti
- ❌ Nessun backup committato nel repo principale
- ❌ Nessun token/credenziale esposto in chat o report
