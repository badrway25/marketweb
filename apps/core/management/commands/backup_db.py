"""``backup_db`` — T38 baseline DB dump command.

Writes a timestamped dump of the project database to
``settings.BACKUP_DIR`` (default ``BASE_DIR/backups/``) and prunes
older dumps to keep at most ``settings.BACKUP_KEEP_COUNT`` files
matching the same prefix + engine.

Supported engines (dispatched on ``connection.vendor``):

  - ``sqlite``    → stdlib ``sqlite3.Connection.backup()`` performs
                    an atomic online backup against the live DB
                    file. No external binary required. Safe with
                    concurrent reads/writes.
  - ``postgresql``→ subprocess ``pg_dump`` writing a plain-SQL dump.
                    Requires ``pg_dump`` on PATH and the DB
                    credentials reachable via ``connection.settings_dict``.

Filename shape (sortable lexicographically = chronologically):

    {prefix}-{engine}-{YYYYMMDD-HHMMSS}.{ext}

e.g. ``marketweb-sqlite-20260511-150000.sqlite3``,
     ``marketweb-postgres-20260511-150000.sql``.

Retention
---------
After a SUCCESSFUL backup write, we list the directory for files
matching ``{prefix}-{engine}-*.{ext}``, sort by mtime DESC, keep
the newest ``--keep`` (default ``settings.BACKUP_KEEP_COUNT`` = 7),
and ``os.unlink`` the rest. Files NOT matching the prefix+engine
glob are NEVER touched — operator-side ad-hoc dumps and other
projects' backups in the same directory are safe.

The retention rule runs ONLY AFTER the backup write succeeds. A
failed backup never deletes anything — operator never loses
yesterday's backup because today's failed.

Cron recipe
-----------
    # Daily at 03:00 local time, retain last 7
    0 3 * * *  cd /app && python manage.py backup_db

    # More aggressive (every 6h, retain last 28 ≈ one week of 6h-spaced backups)
    0 */6 * * * cd /app && python manage.py backup_db --keep 28

Out of scope (intentionally)
----------------------------
- Object storage upload (S3 / GCS / R2): operator pipes the
  output file to their cold-storage tool. See
  ``docs/bootstrap.md`` for a one-liner pattern.
- Encryption-at-rest (gpg / age): the dump is plain-format; if
  the host disk is not encrypted, that's an infrastructure
  decision out of project scope.
- Point-In-Time Recovery (PITR), WAL shipping, continuous
  archiving: enterprise patterns; this baseline targets daily
  cron-friendly snapshots.
- Byte-identical diff verification: the companion
  ``restore_drill`` command verifies "readable + structurally
  intact + non-empty", not "byte-identical to source".
"""
from __future__ import annotations

import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import connection


# File-extension + label per supported engine, keyed by the value
# Django sets on ``connection.vendor``.
_ENGINE_EXT = {
    "sqlite": "sqlite3",
    "postgresql": "sql",
}


class Command(BaseCommand):
    help = (
        "Write a timestamped DB dump to BACKUP_DIR. Supports SQLite "
        "(via stdlib sqlite3.Connection.backup) and PostgreSQL (via "
        "pg_dump subprocess). Retention prunes older dumps matching "
        "the same prefix+engine."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-dir",
            default=None,
            metavar="PATH",
            help=(
                "Directory where the dump is written. Default: "
                "settings.BACKUP_DIR (env BACKUP_DIR, "
                "default BASE_DIR/backups/)."
            ),
        )
        parser.add_argument(
            "--keep",
            type=int,
            default=None,
            metavar="N",
            help=(
                "Number of recent dumps to keep matching the same "
                "prefix+engine. Older files are pruned AFTER a "
                "successful write. Default: settings.BACKUP_KEEP_COUNT "
                "(env BACKUP_KEEP_COUNT, default 7). Pass 0 to disable "
                "pruning."
            ),
        )
        parser.add_argument(
            "--prefix",
            default="marketweb",
            metavar="NAME",
            help="Filename prefix (default: marketweb).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print what would happen; perform no DB read and no FS write.",
        )

    # ── handle ────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        engine = self._resolve_engine()
        ext = _ENGINE_EXT[engine]

        output_dir = Path(options["output_dir"] or settings.BACKUP_DIR)
        keep = options["keep"]
        if keep is None:
            keep = getattr(settings, "BACKUP_KEEP_COUNT", 7)
        if keep < 0:
            raise CommandError("--keep must be >= 0.")
        prefix = options["prefix"]

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{prefix}-{engine}-{timestamp}.{ext}"
        target = output_dir / filename

        self.stdout.write(f"Engine: {engine}")
        self.stdout.write(f"Output: {target}")
        self.stdout.write(f"Retention: keep {keep} most recent matching {prefix}-{engine}-*.{ext}")

        if options["dry_run"]:
            self.stdout.write(self.style.WARNING("DRY RUN — no file written, no retention applied."))
            return

        output_dir.mkdir(parents=True, exist_ok=True)

        # Dispatch on engine. Each writer returns the path on success
        # so we can size-check + size-print uniformly.
        if engine == "sqlite":
            self._backup_sqlite(target)
        elif engine == "postgresql":
            self._backup_postgresql(target)
        else:
            # _resolve_engine raises before we get here, defensive
            # raise-on-future-engine.
            raise CommandError(f"Unsupported engine: {engine}")

        size = target.stat().st_size
        self.stdout.write(self.style.SUCCESS(
            f"Wrote {target.name} ({size} bytes)"
        ))

        # Retention — strictly AFTER the write succeeded.
        if keep > 0:
            pruned = self._prune(output_dir, prefix, engine, ext, keep)
            if pruned:
                self.stdout.write(
                    f"Pruned {len(pruned)} older file(s): "
                    + ", ".join(p.name for p in pruned)
                )
            else:
                self.stdout.write("No older files to prune.")

    # ── engine resolution ────────────────────────────────────────────

    def _resolve_engine(self) -> str:
        """Return the short engine label for the active connection.

        Raises CommandError if the engine is one we do not handle —
        rather than producing a bogus dump file with the wrong
        extension.
        """
        vendor = connection.vendor  # "sqlite", "postgresql", "mysql", "oracle"
        if vendor not in _ENGINE_EXT:
            raise CommandError(
                f"DB engine {vendor!r} is not supported by backup_db. "
                f"Supported: {', '.join(sorted(_ENGINE_EXT))}."
            )
        return vendor

    # ── SQLite path ──────────────────────────────────────────────────

    def _backup_sqlite(self, target: Path) -> None:
        """Atomic online backup using the stdlib sqlite3 API.

        ``Connection.backup`` copies the source DB to the target
        connection page-by-page while honouring writer locks. Safe
        to run while the application has the source DB open
        (concurrent reads continue; writes are coordinated by
        SQLite's WAL). The result is a self-contained ``.sqlite3``
        file that can be opened by any sqlite3 client.

        Source selection:
          - Regular on-disk DB (``NAME = /path/to/db.sqlite3``):
            we open a fresh READ-ONLY ``file:.../mode=ro`` URI so a
            concurrent writer in the Django process keeps working.
          - In-memory / shared-cache URI (the Django test-runner
            default, ``file:memorydb_default?mode=memory&cache=shared``)
            or the bare ``:memory:`` literal: we reuse Django's own
            open connection (``connection.connection``) — there's no
            on-disk file to open with our own URI, and the test DB
            only exists for the duration of this process.
        """
        src_name = str(connection.settings_dict["NAME"])
        is_in_memory = src_name == ":memory:" or src_name.startswith("file:")

        if is_in_memory:
            # Use Django's live connection. ensure_connection() is a
            # no-op when one already exists.
            connection.ensure_connection()
            src = connection.connection
            owns_src = False
        else:
            if not Path(src_name).exists():
                raise CommandError(
                    f"SQLite source DB does not exist at {src_name!r}. "
                    "Has migrate run?"
                )
            src = sqlite3.connect(f"file:{src_name}?mode=ro", uri=True)
            owns_src = True

        dst = sqlite3.connect(str(target))
        try:
            with dst:
                src.backup(dst)
        finally:
            dst.close()
            if owns_src:
                src.close()

    # ── PostgreSQL path ──────────────────────────────────────────────

    def _backup_postgresql(self, target: Path) -> None:
        """``pg_dump --format=plain`` writing a SQL script.

        Plain format chosen so the dump is human-readable + restorable
        via ``psql -f file.sql`` (no ``pg_restore`` needed). The
        cost is larger files (no compression) — operator can pipe
        through gzip if size matters.

        Credentials are taken from ``connection.settings_dict`` and
        propagated via env (``PGPASSWORD``) and CLI flags. The
        ``pg_dump`` binary must be on PATH; otherwise the operator
        sees a precise CommandError pointing at the prerequisite.
        """
        s = connection.settings_dict
        cmd = [
            "pg_dump",
            "--format=plain",
            "--no-owner",          # restore on a different cluster without role headaches
            "--no-privileges",     # same — GRANTs are deploy-local
            "--dbname", s["NAME"],
            "--host", s.get("HOST") or "127.0.0.1",
            "--port", str(s.get("PORT") or "5432"),
            "--username", s.get("USER") or "",
            "--file", str(target),
        ]
        env = self._build_postgres_env(s)
        try:
            subprocess.run(cmd, env=env, check=True, capture_output=True, text=True)
        except FileNotFoundError as exc:
            raise CommandError(
                "pg_dump not found on PATH. Install postgresql-client "
                "(apt: postgresql-client, brew: libpq, alpine: postgresql-client) "
                "or run the backup via `docker compose exec db pg_dump ...` "
                "(see docs/bootstrap.md)."
            ) from exc
        except subprocess.CalledProcessError as exc:
            # Make the operator's job easy — surface stderr from pg_dump
            # directly so they don't have to dig.
            raise CommandError(
                f"pg_dump failed (exit {exc.returncode}). stderr:\n{exc.stderr}"
            ) from exc

    @staticmethod
    def _build_postgres_env(settings_dict) -> dict:
        """Build the env passed to pg_dump.

        Inherits the current process env (so ``PATH`` works) and
        layers ``PGPASSWORD`` from ``settings_dict["PASSWORD"]`` if
        present. Empty password is OK (trust auth on local).
        """
        import os
        env = os.environ.copy()
        password = settings_dict.get("PASSWORD")
        if password:
            env["PGPASSWORD"] = password
        return env

    # ── retention ────────────────────────────────────────────────────

    @staticmethod
    def _prune(output_dir: Path, prefix: str, engine: str, ext: str, keep: int) -> list[Path]:
        """Delete older backups matching prefix+engine, keeping the
        newest ``keep`` files. Returns the list of pruned paths."""
        pattern = f"{prefix}-{engine}-*.{ext}"
        matches = sorted(
            output_dir.glob(pattern),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        # Keep the newest `keep`, delete the rest.
        old = matches[keep:]
        for path in old:
            path.unlink()
        return old
