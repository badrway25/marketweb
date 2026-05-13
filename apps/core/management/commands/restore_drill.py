"""``restore_drill`` — T38 verification that a backup file is restorable.

Given a backup file produced by ``backup_db``, the drill:

  1. Detects the engine from the file extension (override with ``--engine``).
  2. Creates a SANDBOX target (never touches the live DB):
       - SQLite:    a temp ``.sqlite3`` file
       - PostgreSQL: a temp DB ``<original>_drill_<ts>`` on the same cluster
  3. Loads the backup into the sandbox:
       - SQLite:    file copy (the dump itself IS a valid sqlite3 file)
       - PostgreSQL: ``psql -f <dump.sql>``
  4. Opens the sandbox and runs SELECT COUNT(*) on a small set of
     sentinel tables (``django_migrations``, ``auth_user`` /
     ``accounts_user``, ``core_auditlogentry``) — proves the schema
     loaded + rows are queryable.
  5. Cleans up the sandbox unless ``--keep-sandbox``.

Why sandbox-only (never overwrite live)
---------------------------------------
A restore that overwrites production is a destructive operation and
the brief explicitly asks for a DRILL — verification that the
backup is restorable, not the actual restoration. Overwriting the
live DB belongs to incident-response runbooks (see
``docs/bootstrap.md``), where the operator manually stops the app
+ swaps the file + restarts. That sequence is OS / orchestrator
specific and is intentionally NOT automated here.

What "restorable" means in this drill
-------------------------------------
A backup PASSES the drill when ALL THREE conditions hold:

  - The dump opens / replays without error.
  - ``django_migrations`` exists and has ≥ 1 row (i.e. the
    schema is the one produced by a migrated DB, not an empty file).
  - At least one of the user-model / audit-log tables exists with
    ≥ 0 rows (i.e. application tables are present — schema fidelity).

The drill does NOT verify byte-identical fidelity to the source.
That would require a full read-back + diff, which is heavy + brittle.
The current set of checks catches the failure modes that actually
happen in practice: dump truncation, schema drift, corrupted file.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import subprocess
import tempfile
import time
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import connection


# Engine label → file extension produced by backup_db. The drill
# resolves engine from suffix unless the operator overrides via --engine.
_EXT_TO_ENGINE = {
    ".sqlite3": "sqlite",
    ".sql": "postgresql",
}

# Sentinel tables we expect the dump to carry. The drill is happy
# if AT LEAST ONE of them exists and is queryable (different test
# fixtures and different DB profiles ship different subsets — we
# want the drill to pass on any reasonable marketweb snapshot).
SENTINEL_TABLES = (
    "django_migrations",
    "accounts_user",
    "core_auditlogentry",
)


class Command(BaseCommand):
    help = (
        "Verify a backup file is restorable: load it into a sandbox "
        "DB and run a small set of read queries. Never overwrites the "
        "live DB."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "backup_path",
            help="Path to the backup file produced by `backup_db`.",
        )
        parser.add_argument(
            "--engine",
            choices=("sqlite", "postgresql"),
            default=None,
            help=(
                "Override engine auto-detection from the file extension. "
                "Useful when the file was renamed."
            ),
        )
        parser.add_argument(
            "--keep-sandbox",
            action="store_true",
            help=(
                "Do NOT delete the sandbox DB after verification. "
                "Useful when investigating a failed drill."
            ),
        )

    # ── handle ────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        backup_path = Path(options["backup_path"]).resolve()
        if not backup_path.exists():
            raise CommandError(f"Backup file not found: {backup_path}")
        if not backup_path.is_file():
            raise CommandError(f"Backup path is not a file: {backup_path}")

        engine = options["engine"] or self._infer_engine(backup_path)
        self.stdout.write(f"Backup file : {backup_path}")
        self.stdout.write(f"Engine      : {engine}")
        self.stdout.write(f"Size        : {backup_path.stat().st_size} bytes")

        keep_sandbox = options["keep_sandbox"]

        if engine == "sqlite":
            sandbox, cleanup = self._sandbox_sqlite(backup_path)
        elif engine == "postgresql":
            sandbox, cleanup = self._sandbox_postgresql(backup_path)
        else:
            raise CommandError(f"Unsupported engine: {engine}")

        try:
            self.stdout.write(f"Sandbox     : {sandbox}")
            counts = self._verify(engine, sandbox)
        except Exception:
            cleanup()
            raise

        # Verification result. We need AT LEAST django_migrations to
        # exist + at least one sentinel app table.
        found_app = [t for t, c in counts.items() if c is not None and t != "django_migrations"]
        migrations_ok = counts.get("django_migrations") is not None and counts["django_migrations"] > 0

        for table, count in counts.items():
            if count is None:
                self.stdout.write(f"  {table:<24}  (absent)")
            else:
                self.stdout.write(f"  {table:<24}  {count} row(s)")

        if not migrations_ok:
            cleanup()
            raise CommandError(
                "Drill FAILED — django_migrations is missing or empty. "
                "The backup is not a migrated marketweb DB snapshot."
            )
        if not found_app:
            cleanup()
            raise CommandError(
                "Drill FAILED — no marketweb application table (accounts_user, "
                "core_auditlogentry) found in the dump. The backup is "
                "likely corrupted or from an unmigrated DB."
            )

        if keep_sandbox:
            self.stdout.write(self.style.WARNING(
                f"Sandbox retained at {sandbox} (--keep-sandbox). "
                "Delete it manually when done."
            ))
        else:
            cleanup()

        self.stdout.write(self.style.SUCCESS(
            "Drill PASSED — backup is restorable + structurally intact."
        ))

    # ── engine inference ─────────────────────────────────────────────

    @staticmethod
    def _infer_engine(backup_path: Path) -> str:
        ext = backup_path.suffix.lower()
        engine = _EXT_TO_ENGINE.get(ext)
        if not engine:
            raise CommandError(
                f"Cannot infer engine from file extension {ext!r}. "
                f"Pass --engine sqlite or --engine postgresql to override."
            )
        return engine

    # ── SQLite sandbox ───────────────────────────────────────────────

    def _sandbox_sqlite(self, backup_path: Path):
        """Copy the backup to a temp sandbox path. Returns
        ``(sandbox_path, cleanup_callable)``."""
        fd, sandbox_str = tempfile.mkstemp(
            prefix="marketweb-restore-drill-",
            suffix=".sqlite3",
        )
        os.close(fd)
        sandbox = Path(sandbox_str)
        shutil.copy2(backup_path, sandbox)

        def cleanup():
            try:
                sandbox.unlink(missing_ok=True)
            except OSError:
                pass

        return sandbox, cleanup

    # ── PostgreSQL sandbox ───────────────────────────────────────────

    def _sandbox_postgresql(self, backup_path: Path):
        """Create a sandbox DB on the same cluster, ``psql -f`` the
        dump into it, return (sandbox_dbname, cleanup_callable)."""
        s = connection.settings_dict
        live_db = s["NAME"]
        ts = time.strftime("%Y%m%d%H%M%S")
        sandbox_db = f"{live_db}_drill_{ts}"

        # createdb
        self._run_psql_admin(s, ["createdb", sandbox_db])

        # psql -f <dump.sql> --dbname=<sandbox>
        try:
            self._run_psql_admin(
                s,
                ["psql", "--dbname", sandbox_db, "--file", str(backup_path), "-v", "ON_ERROR_STOP=1"],
            )
        except CommandError:
            # If the load failed, drop the half-created sandbox so we
            # don't leak it.
            self._safe_dropdb(s, sandbox_db)
            raise

        def cleanup():
            self._safe_dropdb(s, sandbox_db)

        return sandbox_db, cleanup

    @staticmethod
    def _run_psql_admin(settings_dict, cmd: list[str]) -> None:
        """Run a `createdb`/`dropdb`/`psql` invocation with the
        Django connection credentials."""
        from apps.core.management.commands.backup_db import Command as BackupCommand

        # Prepend host/port/user flags to whatever the caller passed.
        host = settings_dict.get("HOST") or "127.0.0.1"
        port = str(settings_dict.get("PORT") or "5432")
        user = settings_dict.get("USER") or ""
        env = BackupCommand._build_postgres_env(settings_dict)

        binary = cmd[0]
        rest = cmd[1:]
        full = [binary, "--host", host, "--port", port, "--username", user, *rest]
        try:
            subprocess.run(full, env=env, check=True, capture_output=True, text=True)
        except FileNotFoundError as exc:
            raise CommandError(
                f"{binary} not found on PATH. Install postgresql-client."
            ) from exc
        except subprocess.CalledProcessError as exc:
            raise CommandError(
                f"{binary} failed (exit {exc.returncode}). stderr:\n{exc.stderr}"
            ) from exc

    @classmethod
    def _safe_dropdb(cls, settings_dict, dbname: str) -> None:
        """Best-effort dropdb — log but don't re-raise."""
        try:
            cls._run_psql_admin(settings_dict, ["dropdb", "--if-exists", dbname])
        except CommandError:
            # The drill's primary signal is already reported; a failing
            # cleanup is a secondary signal that the operator will see
            # in the leftover DB.
            pass

    # ── verification ─────────────────────────────────────────────────

    def _verify(self, engine: str, sandbox) -> dict[str, int | None]:
        """Run SELECT COUNT(*) on the sentinel tables. Returns a dict
        mapping table name → row count, or None if the table is absent.
        """
        if engine == "sqlite":
            return self._verify_sqlite(sandbox)
        return self._verify_postgresql(sandbox)

    @staticmethod
    def _verify_sqlite(sandbox_path: Path) -> dict[str, int | None]:
        con = sqlite3.connect(f"file:{sandbox_path}?mode=ro", uri=True)
        try:
            cur = con.cursor()
            cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
            existing = {row[0] for row in cur.fetchall()}
            out: dict[str, int | None] = {}
            for table in SENTINEL_TABLES:
                if table in existing:
                    cur.execute(f"SELECT COUNT(*) FROM {table}")
                    out[table] = cur.fetchone()[0]
                else:
                    out[table] = None
            return out
        finally:
            con.close()

    def _verify_postgresql(self, sandbox_db: str) -> dict[str, int | None]:
        s = connection.settings_dict
        host = s.get("HOST") or "127.0.0.1"
        port = str(s.get("PORT") or "5432")
        user = s.get("USER") or ""
        env = self._build_pg_env(s)

        out: dict[str, int | None] = {}
        for table in SENTINEL_TABLES:
            # psql -c "SELECT COUNT(*) FROM {table}" → row or error
            cmd = [
                "psql",
                "--host", host, "--port", port, "--username", user,
                "--dbname", sandbox_db,
                "-tA",  # tuples-only + unaligned (one number per line)
                "-c", f"SELECT COUNT(*) FROM {table}",
            ]
            res = subprocess.run(cmd, env=env, capture_output=True, text=True)
            if res.returncode != 0:
                # Table likely absent. Heuristic: psql exit 1 with
                # "does not exist" in stderr.
                if "does not exist" in (res.stderr or ""):
                    out[table] = None
                    continue
                # Other error: surface it.
                raise CommandError(
                    f"psql count on {table} failed: {res.stderr}"
                )
            try:
                out[table] = int((res.stdout or "0").strip())
            except ValueError:
                out[table] = None
        return out

    @staticmethod
    def _build_pg_env(settings_dict):
        env = os.environ.copy()
        password = settings_dict.get("PASSWORD")
        if password:
            env["PGPASSWORD"] = password
        return env
