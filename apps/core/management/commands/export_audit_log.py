"""``export_audit_log`` — T36 export command for AuditLogEntry.

Emits rows from ``apps.core.models.AuditLogEntry`` to JSONL (default)
or CSV, either on stdout or to a file. The command is the operator
surface for:

  - Incident review (filter by ``--action`` / ``--actor`` / date range).
  - Internal periodic review (full dump, monthly CSV archive).
  - Data Subject Access Request / compliance handoff (filter by
    ``--actor`` substring to extract a specific user's footprint).
  - Hand-off to non-technical operators (CSV opens in Excel/Google
    Sheets without translation).

Scope (deliberately narrow)
---------------------------
- Exports ONLY the AuditLogEntry table — not the underlying targets,
  not the LogEntry built-in Django admin history, not the Sentry feed.
  Cross-table joins remain the consumer's job (CSV+VLOOKUP, jq, BI).
- No async / job scheduler. The command runs synchronously and streams
  row-by-row via ``.iterator()`` so memory stays O(1) for arbitrary
  table sizes.
- No "give me everything ever" failsafe. Operators who run an
  unfiltered export get an unfiltered export — the table is already
  retention-bounded by T32's ``prune_audit_log``.

Sanitization
------------
The ``changes`` JSON is **not** re-scrubbed here. T31's signal
receivers (``_resolve_action`` + the CREATE-path ``_emit_post_save``)
and T33's ``_write_explicit_entry`` both consult ``DENYLISTED_FIELDS``
at write time — by the moment a row is in the DB its ``changes`` is
already password-free / token-free. Adding a second filter at export
would lie about the table contents and silently mask real bugs (a
denylist regression would go unnoticed because the exporter hid it).

Fields excluded from output (by design)
---------------------------------------
- ``actor_id`` — FK to AUTH_USER_MODEL. Internal PK, unstable across
  environments. The survival-snapshot ``actor_repr`` is the
  human-meaningful field for forensic timelines (and it outlives
  user deletion via ``on_delete=SET_NULL``).
- ``target_content_type`` FK PK — same reasoning. The dotted
  ``app_label.ModelName`` string is exported instead.

Usage examples
--------------
    # Full dump, JSONL, stdout (pipe to a file).
    python manage.py export_audit_log > audit-2026-05-11.jsonl

    # CSV to disk.
    python manage.py export_audit_log --format csv --output audit.csv

    # Last 24h, role changes only.
    python manage.py export_audit_log \\
        --since 2026-05-10T00:00:00 \\
        --action role_changed --action deleted

    # All entries authored by a specific operator.
    python manage.py export_audit_log --actor alice@example.com

    # All entries on a single model.
    python manage.py export_audit_log --target-type accounts.User
"""
from __future__ import annotations

import csv
import json
import sys
from datetime import date, datetime, time

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.utils.dateparse import parse_date, parse_datetime


class Command(BaseCommand):
    help = (
        "Export AuditLogEntry rows to JSONL or CSV. Filterable by "
        "action, actor, target type, and date range. Use for incident "
        "review, periodic archive, or DSAR fulfilment."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--format",
            choices=("jsonl", "csv"),
            default="jsonl",
            help="Output format. Default: jsonl (newline-delimited JSON).",
        )
        parser.add_argument(
            "--output",
            default=None,
            help=(
                "Output file path. If omitted, writes to stdout. The file "
                "is opened with utf-8 encoding; CSV uses newline='' as "
                "required by the csv module."
            ),
        )
        parser.add_argument(
            "--action",
            action="append",
            default=[],
            metavar="LABEL",
            help=(
                "Filter by action label (exact match). Repeatable: "
                "--action role_changed --action deleted. Use the raw "
                "TextChoices value (see apps.core.models.AuditLogEntry.Action)."
            ),
        )
        parser.add_argument(
            "--actor",
            default=None,
            metavar="SUBSTR",
            help=(
                "Filter by case-insensitive substring match on actor_repr. "
                "Matches the snapshot, so survives a username rename or "
                "user deletion."
            ),
        )
        parser.add_argument(
            "--target-type",
            default=None,
            metavar="APP.MODEL",
            help=(
                "Filter by target ContentType, e.g. accounts.User or "
                "commerce.Order. Raises if the model is unknown."
            ),
        )
        parser.add_argument(
            "--since",
            default=None,
            metavar="ISO",
            help=(
                "Inclusive lower bound on timestamp. Accepts YYYY-MM-DD "
                "(00:00 in TIME_ZONE) or a full ISO datetime."
            ),
        )
        parser.add_argument(
            "--until",
            default=None,
            metavar="ISO",
            help=(
                "Exclusive upper bound on timestamp. Same accepted formats "
                "as --since."
            ),
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=None,
            metavar="N",
            help="Cap the number of rows emitted. Must be >= 0.",
        )

    # ── handle ────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        from apps.core.models import AuditLogEntry

        qs = AuditLogEntry.objects.all().select_related(
            "target_content_type",
        ).order_by("timestamp", "pk")

        if options["action"]:
            qs = qs.filter(action__in=options["action"])

        if options["actor"]:
            qs = qs.filter(actor_repr__icontains=options["actor"])

        if options["target_type"]:
            ct = self._resolve_content_type(options["target_type"])
            qs = qs.filter(target_content_type=ct)

        if options["since"]:
            qs = qs.filter(timestamp__gte=self._parse_bound(options["since"]))

        if options["until"]:
            qs = qs.filter(timestamp__lt=self._parse_bound(options["until"]))

        if options["limit"] is not None:
            if options["limit"] < 0:
                raise CommandError("--limit must be >= 0.")
            qs = qs[: options["limit"]]

        out_path = options["output"]
        fmt = options["format"]

        # Open output destination. We wrap stdout so the csv module
        # (which calls ``write(str)``) works against Django's OutputWrapper.
        stream, close_after = self._open_stream(out_path, fmt)
        try:
            if fmt == "jsonl":
                count = self._write_jsonl(stream, qs.iterator(chunk_size=500))
            else:
                count = self._write_csv(stream, qs.iterator(chunk_size=500))
        finally:
            if close_after:
                stream.close()

        # Summary goes to stderr so stdout stays clean for piping
        # (e.g. ``manage.py export_audit_log | jq .`` works unchanged).
        self.stderr.write(self.style.SUCCESS(
            f"Exported {count} AuditLogEntry row(s)"
            + (f" to {out_path}." if out_path else " to stdout.")
        ))

    # ── filter resolution ────────────────────────────────────────────

    def _resolve_content_type(self, dotted: str) -> ContentType:
        """Return the ContentType for ``"app_label.ModelName"`` or
        raise ``CommandError`` with an operator-friendly message."""
        if "." not in dotted:
            raise CommandError(
                f"--target-type must be of the form app_label.ModelName; "
                f"got {dotted!r}."
            )
        app_label, _, model_name = dotted.partition(".")
        try:
            return ContentType.objects.get(
                app_label=app_label,
                model=model_name.lower(),
            )
        except ContentType.DoesNotExist as exc:
            raise CommandError(
                f"Unknown --target-type {dotted!r}: no ContentType matches "
                f"app_label={app_label!r}, model={model_name.lower()!r}."
            ) from exc

    def _parse_bound(self, raw: str) -> datetime:
        """Parse a CLI date/datetime bound into an aware ``datetime``.

        Accepts ``YYYY-MM-DD`` (treated as 00:00 in the active TZ) and
        full ISO 8601 datetimes (parsed with ``parse_datetime``; if
        naïve, made aware in the active TZ)."""
        dt = parse_datetime(raw)
        if dt is None:
            d = parse_date(raw)
            if d is None:
                raise CommandError(
                    f"Could not parse {raw!r} as YYYY-MM-DD or ISO datetime."
                )
            dt = datetime.combine(d, time.min)
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt

    # ── stream helpers ────────────────────────────────────────────────

    def _open_stream(self, path: str | None, fmt: str):
        """Return ``(stream, close_after)``.

        - ``path=None`` → return a stdout shim that the csv module can
          ``.write()`` to (Django's ``OutputWrapper.write`` accepts a
          single string arg, but uses different defaults than a real
          file). ``close_after=False``.
        - ``path=...`` → open the file with ``newline=""`` for CSV
          (the csv module requires this to avoid double line breaks
          on Windows) and ``newline="\\n"`` for JSONL.
        """
        if path is None:
            return _StdoutFileShim(self.stdout), False
        newline = "" if fmt == "csv" else "\n"
        return open(path, "w", encoding="utf-8", newline=newline), True

    # ── writers ───────────────────────────────────────────────────────

    def _row_to_dict(self, row) -> dict:
        """Project an AuditLogEntry row to the exported field set.

        Kept as a single helper so JSONL and CSV writers agree on the
        field list. The ``changes`` value passes through unchanged for
        JSONL; the CSV writer JSON-serialises it as a string.
        """
        target_type = ""
        ct = row.target_content_type
        if ct is not None:
            target_type = f"{ct.app_label}.{ct.model}"
        ts = row.timestamp.isoformat() if row.timestamp else ""
        return {
            "timestamp": ts,
            "actor_repr": row.actor_repr or "",
            "action": row.action,
            "target_type": target_type,
            "target_object_id": row.target_object_id or "",
            "target_repr": row.target_repr or "",
            "changes": row.changes or {},
            "request_ip": row.request_ip or "",
        }

    EXPORT_FIELDS = (
        "timestamp",
        "actor_repr",
        "action",
        "target_type",
        "target_object_id",
        "target_repr",
        "changes",
        "request_ip",
    )

    def _write_jsonl(self, stream, rows) -> int:
        """Emit one JSON object per line. ``ensure_ascii=False`` so
        Unicode actor_repr values stay readable in editors."""
        count = 0
        for row in rows:
            stream.write(
                json.dumps(self._row_to_dict(row), ensure_ascii=False) + "\n"
            )
            count += 1
        return count

    def _write_csv(self, stream, rows) -> int:
        """Emit a CSV with the same field list as JSONL.

        ``changes`` is JSON-serialised into a single cell — operators
        opening the CSV in Excel see a literal ``{"status": ...}`` string
        per row, which preserves the semantic detail without flattening
        into an unbounded set of columns.
        """
        writer = csv.DictWriter(stream, fieldnames=self.EXPORT_FIELDS)
        writer.writeheader()
        count = 0
        for row in rows:
            d = self._row_to_dict(row)
            d["changes"] = json.dumps(d["changes"], ensure_ascii=False)
            writer.writerow(d)
            count += 1
        return count


class _StdoutFileShim:
    """Adapter so ``csv.writer`` (which expects a real file with a
    ``write(str)`` signature) can target Django's ``OutputWrapper``.

    ``OutputWrapper.write`` defaults to appending a newline; the csv
    module and the jsonl writer already terminate their own lines, so
    we pass ``ending=""`` to suppress the implicit newline. We accept
    a single string argument — which is exactly what csv.writer and
    our jsonl writer pass.
    """

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def write(self, s: str) -> int:
        self._wrapped.write(s, ending="")
        return len(s)
