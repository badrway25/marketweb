# Bootstrap

Operational entry point for new collaborators on `marketweb`. Three
modes are supported, ordered from lightest to most prod-shaped.

## 1. Native dev (lightest · default for day-to-day work)

```sh
python -m venv .venv
. .venv/Scripts/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py seed_templates   # populate the catalog
python manage.py runserver
```

- Settings profile defaults to `marketweb.settings.dev` (SQLite at
  `db.sqlite3`, dev-only SECRET_KEY fallback, console email backend).
- Listens on `http://127.0.0.1:8000/`.
- No env file needed for this mode.

Test suite:

```sh
python manage.py test apps.catalog
```

## 2. Docker · single-container (no Postgres)

For verifying the production-shaped runtime without spinning up a
Postgres alongside.

```sh
cp .env.example .env
# Fill at minimum:
#   DJANGO_SECRET_KEY=<50+ random chars>
#   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
#   DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:8000
#   DJANGO_ALLOW_SQLITE_PROD=1     # opt-in SQLite-on-disk for the smoke
#   DJANGO_SECURE_SSL_REDIRECT=0
#   DJANGO_SECURE_HSTS_SECONDS=0

docker build -t marketweb:dev .
docker run --rm -p 8000:8000 --env-file .env marketweb:dev
```

- Default entrypoint runs gunicorn against `marketweb.wsgi`.
- Uses the prod settings profile (per `marketweb/wsgi.py`).
- Image is single-stage, `python:3.13-slim` based, drops to a non-root
  user — see comments in `Dockerfile`.

## 3. Docker Compose · prod-shaped local stack (web + Postgres)

Closer to a real deploy: gunicorn + Postgres 16, bind-mounted media.

```sh
cp .env.example .env
# Fill DB credentials in addition to the §2 minimum:
#   DATABASE_NAME=marketweb
#   DATABASE_USER=marketweb
#   DATABASE_PASSWORD=<choose>
#   DATABASE_HOST=db
#   DATABASE_PORT=5432

docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py seed_templates
docker compose exec web python manage.py createsuperuser
```

- Compose v2 syntax (`docker compose ...`, no `version:` key).
- Postgres data persists in the `db_data` volume; user-uploaded media
  in the `media_data` volume.
- `web` waits on the `db` healthcheck before starting.

## CI

GitHub Actions at `.github/workflows/ci.yml` runs on every push +
PR to `main`/`master` (and on `phase-*` / `sprint-*` topic branches):

- **tests** (blocking) — `pip install` + `manage.py check` +
  `manage.py test apps.catalog`.
- **deploy-check** (non-blocking) — `manage.py check --deploy`
  against the prod profile with synthetic env. Surfaces config
  drift at PR time.
- **lint** (non-blocking) — `ruff check apps/ marketweb/`. Surfaces
  lint debt without gating merges; auto-fix locally with
  `ruff check --fix apps/ marketweb/`.

## Out of scope (intentional)

The Sprint 0 · T5+T6 baseline is deliberately small. The following
are tracked separately and will land via dedicated passes:

- WhiteNoise / static-file CDN wiring (Sprint 2).
- Multi-stage Docker / distroless base / image-size budget.
- Image push to a registry (publish step in CI) — done only when a
  deploy target is decided.
- Celery + Redis containers (no celery broker is configured today
  even though the dependency is installed; see `prod.py` "Out of
  scope" header).
- Pre-commit hooks (could land in a follow-up hygiene pass).

**Wired by later passes:**
- Sentry SDK observability — wired by T19 (2026-05-10). Init gated
  by `SENTRY_DSN`; dev / CI / local stay dormant. See
  `marketweb/sentry.py` and the `SENTRY_*` block in `.env.example`.
- WhiteNoise static-file serving — wired by T22 (2026-05-10) so
  gunicorn alone serves `/static/`. See the `Dockerfile` and the
  `Static files · WhiteNoise` block in `marketweb/settings/prod.py`.
- django-axes brute-force protection — wired by T23 (2026-05-10).
  5 failed `(ip, username)` attempts → 1h lockout (429). Auto-
  disabled in `manage.py test`. See the `AXES_*` block in
  `marketweb/settings/base.py` and `.env.example`.
- Admin 2FA via django-otp — wired by T27 (2026-05-11). `/admin/`
  now requires password + a 6-digit TOTP code. Customer
  `/account/login/` stays single-factor.

## 4. Admin 2FA enrollment (T27 · required for every staff user)

After T27, the `/admin/` gate requires both a valid password AND a
6-digit TOTP code from an authenticator app (Google Authenticator /
Authy / 1Password / Bitwarden / ...). A fresh superuser CANNOT log
in to `/admin/` until they enroll a TOTP device.

```sh
# 1. Create the superuser as usual (no TOTP yet).
python manage.py createsuperuser

# 2. Provision the TOTP device + print the provisioning URI.
python manage.py setup_admin_totp <username>
```

The command prints an `otpauth://totp/...` URI on stdout. Scan it
with the authenticator app (most apps have a "scan QR code" or
"paste URI" option). From that point on, the next `/admin/login/`
asks for username + password + the 6-digit code shown in the app.

Operator notes:

- The URI contains the raw shared secret. Do not paste it into
  ticketing systems, do not screen-share it during pairing, do
  not save the terminal scrollback to a shared drive.
- To rotate the secret (e.g. lost phone): re-run
  `python manage.py setup_admin_totp <username> --force`. The
  previously enrolled authenticator app stops working.
- The command refuses to enroll a non-staff user (admin TOTP would
  have no effect outside `/admin/`).
- Customer-facing `/account/login/` is intentionally unchanged
  — customer 2FA is out-of-scope for this baseline.

### OTP session re-verification (T29)

After T29, the OTP-verified state on `/admin/` has a max-age
of `OTP_ADMIN_REVERIFY_SECONDS` (default **8 hours**), independent
of `SESSION_COOKIE_AGE`. After that window the admin is bounced
to `/admin/login/` to re-enter password + TOTP, even if their
session cookie is still valid.

Tighten via env for sensitive contexts:

```sh
OTP_ADMIN_REVERIFY_SECONDS=3600   # 1h
OTP_ADMIN_REVERIFY_SECONDS=900    # 15min
```

Customer `/account/login/` is unaffected — T29 is path-scoped at
`/admin/`.

### Audit log (T31)

After T31 the project ships a read-only audit feed at
`/admin/core/auditlogentry/` covering sensitive mutations on
three models: `accounts.User`, `catalog.WebTemplate`, and
`commerce.Order`. Each entry stores the actor (admin user or
"system" for management commands), action (CREATED / UPDATED /
DELETED / PUBLISHED / UNPUBLISHED / ROLE_CHANGED), target object,
JSON diff of the watched fields, and timestamp.

Built-in Django `LogEntry` (admin-UI actions only) is also
surfaced at `/admin/admin/logentry/` for the same operator
audience. Both admins are tamper-resistant: no add / delete UI,
and the change form renders in view-only mode (only a "Chiudi"
button — no save).

Password values are NEVER serialized into the audit table (the
`DENYLISTED_FIELDS` guard in `apps.core.audit` enforces this even
if a future edit accidentally adds `password` to a watched-fields
list). Cosmetic edits to non-watched fields produce no audit row.

### Audit retention + alerting (T32)

**Retention.** The audit table is pruned by a management command:

```sh
# Inspect what would be deleted (no DB write)
python manage.py prune_audit_log --dry-run

# Delete rows older than the configured window (default 365d)
python manage.py prune_audit_log --yes

# Override the window for one invocation
python manage.py prune_audit_log --older-than 90 --yes
```

Recommended cron recipe (nightly at 03:30 UTC):

```cron
30 3 * * *  cd /app && python manage.py prune_audit_log --yes
```

Defaults are env-tunable via `AUDIT_LOG_RETENTION_DAYS` (default
365). Without `--yes` and `--dry-run` the command requires an
interactive `yes` confirmation — safe for accidental invocations.

**Alerting.** Every audit row written with `action in
{role_changed, deleted}` triggers two things:

1. A WARNING line on the `marketweb.audit` logger (kv-formatted in
   prod, picked up by Loki / Datadog / CloudWatch Logs Insights).
2. An email to `AUDIT_ALERT_RECIPIENTS` (comma-separated list). If
   the list is empty (dev default), no email is sent — only the
   log line.

Configure recipients in the deploy env:

```sh
AUDIT_ALERT_RECIPIENTS=ops@example.com,founder@example.com
```

The kill-switch `AUDIT_ALERTS_ENABLED=0` is break-glass only —
silently disables both channels. Default ON.

### Explicit service-layer audit events (T33)

Some business events do not reduce to a "field X changed on model
Y" — e.g. *cancel an order for a stated reason*. The semantic of
the operation is lost in T31's diff-style capture.

`apps.core.audit.audited(...)` is the decorator that closes that
gap. Decorate a service function with an explicit `action` label
and a list of kwargs to capture as metadata; on successful return
the decorator writes an extra audit row carrying the semantic
event alongside the signal-driven UPDATED row.

```python
from apps.core.audit import audited
from apps.core.models import AuditLogEntry

@audited(
    action=AuditLogEntry.Action.ORDER_CANCELLED,
    target_arg="order",
    metadata_args=("reason",),
)
def cancel_order(*, order, reason=""):
    ...
    return order
```

Already wired in `apps/commerce/services.py` for:
- `cancel_order` → action=`order_cancelled`, metadata=`{reason}`
- `mark_order_paid` → action=`order_paid`, metadata=`{note}`

The decorator writes ONLY on successful return — exceptions
propagate without an audit row. The T31 signal-driven UPDATED
row is also emitted (the two are complementary, not duplicates).

**T35 extension** — three additional flows are decorated using the
same pattern, with no decorator changes:
- `set_order_fulfillment` (commerce) → action=`order_fulfillment_changed`,
  metadata=`{fulfillment_status, tracking_carrier, tracking_number}`.
  Complementary with T31 signal `updated` (Order is tracked).
- `publish_project` (projects) → action=`project_published`. CustomerProject
  is NOT in TRACKED_MODELS, so this explicit row is the ONLY audit trace.
- `unpublish_project` (projects) → action=`project_unpublished`. Same
  rationale as publish — the only audit trace for the unpublish event.

### Sentry forensic breadcrumbs from audit alerts (T34)

When `SENTRY_DSN` is set (production opt-in path), every WARN-level
log line from the `marketweb.audit` logger — i.e. every T32
`audit_alert` for `role_changed`/`deleted` plus T33's defensive
warnings — becomes a Sentry **breadcrumb** with structured `data`:

```
breadcrumb.category = "marketweb.audit"
breadcrumb.level    = "warning"
breadcrumb.data     = {
  audit_action     : "role_changed",
  audit_actor      : "alice@example.com",
  audit_target_type: "Accounts | user",
  audit_target     : "bob@example.com",
  audit_changes    : { "is_staff": { "old": false, "new": true } },
  audit_request_ip : "10.0.0.7",
}
```

If a Sentry event (typically an unhandled 500) fires shortly after,
the breadcrumb is attached to that event — answering "what happened
right before this crash" with filterable structured fields, not flat
text.

The breadcrumb stream is pinned via an explicit
`LoggingIntegration(level=WARNING, event_level=ERROR)` in
`marketweb/sentry.py` — INFO-level chatter does not become
breadcrumbs, ERROR-level logs continue to become full Sentry events.
Dev / CI / local stay dormant (no DSN ⇒ no init), unchanged from T19.

### Audit log export (T36)

`python manage.py export_audit_log` emits the `AuditLogEntry` table
to JSONL (default) or CSV, on stdout or to a file. Use it for
incident review, monthly archive, DSAR handoff, or any case where
clicking through `/admin/core/auditlogentry/` is not enough.

```sh
# Full dump, JSONL, stdout (pipe to a file or to jq)
python manage.py export_audit_log > audit-2026-05-11.jsonl

# Last 30 days, role/delete events only
python manage.py export_audit_log --since 2026-04-11 \
    --action role_changed --action deleted

# CSV archive for the legal team
python manage.py export_audit_log --format csv \
    --output audit-2026-05.csv --since 2026-05-01 --until 2026-06-01
```

Filters: `--action LABEL` (repeatable), `--actor SUBSTR` (substring
on `actor_repr`, case-insensitive), `--target-type APP.MODEL`,
`--since`, `--until`, `--limit`. Order is chronological ASC. The
`changes` JSON passes through the T31/T33 write-time DENYLIST — the
exporter does not re-scrub.

### Browser-side security headers (T37)

`marketweb/security_headers.py::SecurityHeadersMiddleware` adds the
four browser-side headers Django's `SecurityMiddleware` does NOT
ship out of the box:

- `Content-Security-Policy` — host allowlist for jsdelivr (Bootstrap),
  Google Fonts, Stripe + clickjacking + form-action + base-uri +
  object-src lockdown.
- `Permissions-Policy` — opts out of camera, microphone, geolocation,
  USB, payment-request, FLoC, Topics.
- `Cross-Origin-Resource-Policy: same-origin`.
- `X-Permitted-Cross-Domain-Policies: none`.

CSP keeps `'unsafe-inline'` for `script-src` and `style-src` — the
project uses inline `style="..."` attributes + inline `<script>`
blocks in ~15 templates (Stripe payment IIFE, project editor,
commerce dashboards, skin templates). The pragmatic concession is
documented in the module docstring. The HOST allowlist still
blocks external script injection.

Dev and prod ship the SAME policy values so developers see CSP
violations in their local browser console BEFORE prod. In prod the
middleware is positioned ABOVE WhiteNoise so static files served
via WhiteNoise also receive the four headers.

### Backup baseline (T38)

Two management commands cover the daily backup lifecycle:

```sh
# Write a timestamped DB dump under BACKUP_DIR (default backups/)
python manage.py backup_db

# Override output / retention
python manage.py backup_db --output-dir /var/backups/marketweb --keep 14

# Verify a dump file is restorable WITHOUT touching the live DB
python manage.py restore_drill backups/marketweb-sqlite-20260511-185226.sqlite3
```

The backup command dispatches on `connection.vendor`:
- **SQLite**: stdlib `sqlite3.Connection.backup()` — atomic online
  backup, no external binary required, safe against concurrent
  readers.
- **PostgreSQL**: `pg_dump --format=plain --no-owner --no-privileges`
  — requires `pg_dump` on PATH. Inside the docker compose stack,
  run via `docker compose exec db pg_dump ...` instead (the
  `postgres:16-alpine` image bundles the binary).

The restore drill opens the dump in a sandbox (a temp SQLite file or
a `<dbname>_drill_<ts>` Postgres DB), queries the sentinel tables
`django_migrations`, `accounts_user`, `core_auditlogentry`, and
deletes the sandbox. It NEVER overwrites the live DB — actual
restoration is a destructive runbook step, intentionally manual.

Retention: `--keep N` (default `settings.BACKUP_KEEP_COUNT` = 7)
keeps only the newest N files matching the same prefix + engine.
Files with another prefix in the same directory are never touched.
Pruning runs ONLY AFTER a successful write, so a failed backup
never deletes yesterday's snapshot.

Cron recipe (operator):

```cron
# Daily 03:00 local time, retain last 7
0 3 * * *  cd /app && python manage.py backup_db

# Pipe to cold storage (S3 / R2 / B2) — operator-side, out of scope
0 4 * * *  aws s3 cp /var/backups/marketweb/$(ls -t /var/backups/marketweb | head -1) s3://my-bucket/db-backups/
```

Restoration (production runbook, intentionally NOT automated):

```sh
# 1. Stop the app so no concurrent writers exist.
systemctl stop marketweb            # or: docker compose stop web

# 2. SQLite: replace the file.
cp /var/backups/marketweb/marketweb-sqlite-2026-05-11-030000.sqlite3 /app/db.sqlite3

# 2'. Postgres: drop+recreate+restore.
dropdb marketweb && createdb marketweb
psql marketweb -f /var/backups/marketweb/marketweb-postgres-2026-05-11-030000.sql

# 3. Restart and verify.
systemctl start marketweb
python manage.py check
```

Run `python manage.py restore_drill <file>` BEFORE swapping the
live DB. The drill catches truncated / corrupted / unmigrated
dumps in 1-2 seconds — much cheaper than discovering it AFTER
deleting the live DB.

If you need any of these, file an item before adding it — the
baseline must stay small enough that a new collaborator can read
all of `Dockerfile + compose + ci.yml + this doc` in one sitting.
