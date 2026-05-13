# Audit Report — Phase 1: Comparative Baseline (master vs v15)

**Data:** 2026-05-13
**Esecutore:** Claude Code (Opus 4.7 1M)
**Modalità:** read-only, nessuna modifica al codice durante la fase
**Target principale:** `mw-integration-baseline-v15`
**Riferimento storico:** `marketweb/` (master)

---

## 1. Sintesi esecutiva

| Dimensione | `marketweb/` (master) | `mw-integration-baseline-v15` |
|---|---|---|
| Branch | `master` @ `9736da4` | `phase-x7e-lf2-variance-and-causa-retrofit` |
| Ultimo commit | 2026-04-12 | 2026-05-13 |
| Commit avanti su master | — | +254 (0 indietro) |
| File diff vs master | — | 1.009 file, +333.018 / −3.729 righe |
| Template live (cartelle skin) | 2 verticali (medical, restaurant) | 8 verticali (agency, business, ecommerce, lawyer, medical, portfolio, real-estate, restaurant) |
| Template in `TEMPLATE_REGISTRY.json` | registry pre-MVP | 33 published in 9 categorie (aggiunge `travel`) |
| Locali coperti | IT | IT, EN, FR, ES, AR (incl. RTL arabo) |
| Settings | `settings.py` monolitico | `settings/{base,dev,prod}.py` env-driven |
| Sicurezza | Solo Django default | django-axes, django-otp, CSP, audit log, OTP re-verify, branded 405/429 |
| Pagamenti | Solo riferimento a Stripe | Stripe + stub fallback + multi-storefront |
| Deploy | Nessun artefatto | Dockerfile, docker-compose.yml, Gunicorn, WhiteNoise, Sentry, .env.example |
| Factory di template | — | `factory/agents/` (10 agent role), `design-orchestrator/`, content-factory pipeline |
| QA / Smoke | — | 8 smoke_*.py + `tests/test_check_imagery_pack.py` + `apps/<x>/tests.py` |

**Verdetto:** v15 è la baseline di lavoro reale; master è pre-MVP e va archiviato come riferimento storico.

---

## 2. Stato sano? — runnability check

`python manage.py check` su v15 fallisce con `ModuleNotFoundError: No module named 'axes'`. Causa: il `.venv` condiviso ha Django 6.0.4 e mancano `django-axes`, `django-otp`, `celery`, `stripe`, `sentry-sdk`, `whitenoise`, `gunicorn`, `psycopg`.

È un blocker tecnico (P0 ambient) ma non un bug del codice: `requirements.txt` v15 elenca correttamente le dipendenze (Django 5.2.7 LTS). Va ricreato un venv pulito.

---

## 3. Cosa esiste solo in v15

### 3.1 Configurazione & deploy (production-leaning)
- `marketweb/settings/{base,dev,prod}.py` — split env-driven con helper `env()` zero-dipendenze
- `marketweb/security_headers.py` — CSP, Permissions-Policy, Cross-Origin-Resource-Policy
- `marketweb/middleware.py` — `AdminOtpReverifyMiddleware`, `BrandedMethodNotAllowedMiddleware`
- `marketweb/sentry.py`, `marketweb/_error_triggers.py`
- `Dockerfile`, `docker-compose.yml`, `.dockerignore`, `.env.example` (228 righe)
- `.github/` workflows
- `staticfiles/` (collectstatic output — verificare se intenzionale)

### 3.2 Apps Django potenziate
- `core` → `audit.py`, `middleware.py`, `urls.py`, management commands (backup_db, prune_audit_log, export_audit_log, restore_drill)
- `accounts` → `forms.py`, `selectors.py`, `services.py`, `urls.py`, `views.py`, `setup_admin_totp`
- `catalog` → `checks.py`, `cs_contrast_audit.py`, `imagery_policy.py`, `preview_imagery.py`, `sitemaps.py`, `template_content.py` + ~30 moduli per-brand × per-locale, `template_dna.py`, `theme_safety.py`
- `editor` → `models.py`, `rendering.py`, `schema.py`, `selectors.py`, `services.py`, `urls.py`
- `commerce` → `payments.py`, `content.py`, `i18n.py`, `views/{customer,seller}.py`, `forms.py`
- `projects` → `services.py`, `selectors.py`, `urls.py`, `views.py`, management commands
- `pages` → `models.py`, `selectors.py`, `services.py`, `urls.py`

### 3.3 Template, design system, asset
- `templates/live_templates/` — 8 verticali con archetypi
- `templates/preview_compositions/` — composizioni preview per ogni verticale
- `templates/commerce/`, `templates/projects/`, `templates/accounts/`, `templates/catalog/`, `templates/includes/`
- `127-design/` — design tokens + fonts (18 font asset)
- `static/css/` arricchito, `static/js/editor/`, `static/editor/`

### 3.4 Factory di produzione template (multi-agent workflow)
- `factory/agents/` — 10 ruoli: template-planner, template-builder, copy-translation-agent, imagery-curator, style-critic, contrast-accessibility-auditor, responsive-auditor, browser-verifier, release-gatekeeper, template-editor-fixer
- `factory/reports/` — 388 file di report di esecuzione (lineage tracciabile)
- `factory/standards/`, `factory/references/`
- `design-orchestrator/` — workflow, dry-runs, candidates, references (114 file)
- `docs/content-factory/` — 31 documenti operativi
- `prompts/claude/` — orchestrator/backend/UI roles

### 3.5 QA & test
- 8 smoke runner top-level (smoke_full.py, smoke_commerce.py, smoke_ecommerce_rollout.py, smoke_i18n_*, smoke_forms.py, smoke_pixel_perfection.py, smoke_chiara_perfection.py)
- `tests/test_check_imagery_pack.py`
- `apps/<x>/tests.py` arricchiti
- `screenshots/` come ground truth visiva
- `scripts/` con utility CLI

### 3.6 Documentazione di sessione
- `SESSION_LOG.md` (769 KB), `DECISIONS.md` (416 KB), `AGENT_HANDOFF.md` (291 KB), `TODO_NEXT.md` (160 KB)
- `EDITOR_SCHEMA_BLUEPRINT.md`, `PROFESSION_PRESET_TAXONOMY.md` (14 categorie × 28-30 archetypi × 75-90 preset target), `CATALOG_EXPANSION_STRATEGY.md`

---

## 4. Cosa esiste solo in master (e va valutato)

Praticamente nulla di codice produttivo: master è un sottoinsieme stretto di v15.

- `marketweb/settings.py` (monolitico) — rimosso e sostituito da `settings/` in v15
- `templates/live_templates/{medical,restaurant}` — varianti pre-DNA, in v15 più mature
- `templates/preview_compositions/{agency,lawyer,portfolio,real-estate}.html` come file flat (placeholder) — in v15 sostituite dai veri compositori sotto la rispettiva sottocartella

→ **Nessun lavoro unico in master vale la pena salvare.**

---

## 5. Working tree non committato presente in v15

66 file modificati (+11.727/-5.703 righe), più decine di untracked critici tra cui:
- `marketweb/settings/` (intero package), `marketweb/{middleware,security_headers,sentry,_error_triggers}.py`
- `apps/core/{audit,middleware}.py` + migrazioni iniziali + management commands
- `apps/accounts/management/commands/setup_admin_totp.py`
- `apps/catalog/sitemaps.py`, `cs_contrast_audit.py`, `tests_contrast.py`
- 8 nuovi brand × 5 locale = ~40 file template_content_<brand>_<locale>.py
- `.dockerignore`, `.env.example`, `.github/workflows/ci.yml`, `Dockerfile`, `docker-compose.yml`
- HTML error templates (400/403/403_csrf/404/405/500/axes_lockout)
- `factory/standards/*-shape-contract.md`, `factory/reports/execution-2026-05-13/T61_*.md`
- `static/favicon.svg`, `docs/bootstrap.md`, `_verify_es_shape.py`

**Coerenza:** il working tree è coerente al suo interno (asgi/urls/wsgi modificati per puntare al nuovo `settings/` package che è untracked) ma incoerente rispetto a HEAD. Il delta è composito (Sprint 0 deploy + security hardening T19-T43 + 8 nuovi brand + X.5/X.6/X.7 retrofit).

**Decisione di salvataggio (Fase 2):** commit snapshot atomico, non stash — perché lo stash rimuoverebbe `marketweb/settings/` lasciando `asgi.py`/`urls.py` con import rotti.

---

## 6. Rischi nel consolidamento v15 → master

| # | Rischio | Severità | Mitigazione |
|---|---|---|---|
| R1 | Perdere il WIP composito non committato | Alto | Commit snapshot + patch backup (Fase 2 step 1) |
| R2 | 60+ worktree git aperti bloccano operazioni sui ref | Medio | Censimento e prune mirato dopo OK utente |
| R3 | `staticfiles/` committato genera diff rumorosi | Medio | Valutare aggiunta a `.gitignore` |
| R4 | `db.sqlite3` committato (dati seed/dev binari) | Medio-basso | Confermare ground-truth seed o residuo |
| R5 | Migration history non verificata cross-app | Medio | `makemigrations --check --dry-run` dopo install deps |
| R6 | `.venv` condiviso disallineato con `requirements.txt` | Alto (ambient) | Ricreare venv dedicato a v15 |
| R7 | `ALLOWED_HOSTS = ["*"]` in dev | Basso | Verifica in `settings/prod.py` |
| R8 | `SECRET_KEY` fallback dev-only | Basso | OK come da `base.py` design |
| R9 | 33 template registry vs 19 cartelle skin (riuso archetipi o gap) | Medio | Audit dedicato registry ↔ skin (Fase 2) |

---

## 7. Versione più completa e affidabile

v15 vince su ogni asse misurabile: funzionalità (+254 commit, +333k righe), catalogo (33 brand vs 0 in registry / 2 verticali in master), sicurezza (axes, OTP, CSP, audit log), i18n (5 locale + RTL), deploy (Docker + Sentry + WhiteNoise + Gunicorn), QA (smoke + factory agent), architettura (settings split + services/selectors).

L'unica area "in debito" rispetto al modello dichiarato è Phase A (Editor Foundation): l'editor c'è (`apps/editor/{models,rendering,schema,services}.py`) ma è ancora fronte di lavoro attivo (vedi `EDITOR_SCHEMA_BLUEPRINT.md`).

---

## 8. Piano consigliato per consolidamento (autorizzato a fasi)

### Fase 2 — Stabilizzazione di v15 (autorizzata)
1. Salvare il WIP composito con backup patch + commit snapshot
2. Riallineare venv dedicato a v15
3. `manage.py check` verde
4. `makemigrations --check --dry-run`
5. Audit registry ↔ skin folders
6. Linting (ruff + black)
7. Browser QA flusso pubblico

### Fase 3 — Decisione governance (con utente)
Strategia di consolidamento approvata: **B — fast-forward merge** da `phase-x7e-...` verso `master`. Non distruttiva, conserva lineage, no force-push. Autorizzata solo dopo report Fase 2 verde.

### Fase 4 — Cleanup worktree (con utente)
Inventariare i 60+ worktree e prune mirato in batch piccoli.

### Fase 5 — Audit di qualità approfondito (sessione successiva)
UI/UX premium audit, editor E2E QA, prod readiness, performance, accessibilità WCAG 2.1 AA.

---

## 9. Operazioni NON effettuate in Fase 1

- Nessuna modifica al codice
- Nessun git commit/stash/reset/checkout
- Nessun `pip install`
- Nessun `makemigrations`/`migrate`
- Nessun avvio server
- Nessun accesso a `.env` o credenziali (verificato: `.env.example` contiene solo placeholder)
