"""``prune_audit_log`` — T32 retention command for AuditLogEntry.

Deletes ``AuditLogEntry`` rows whose ``timestamp`` is older than the
configured retention window. Intended to be run on a schedule (cron,
GitHub Actions Cron, Kubernetes CronJob — operator's choice; the
project does not ship a scheduler).

Default age (days) reads from ``settings.AUDIT_LOG_RETENTION_DAYS``
(env-driven, default 365). The ``--older-than`` flag overrides on a
per-invocation basis without touching the deploy env.

Safety mechanisms
-----------------
- ``--dry-run`` prints what WOULD be deleted; no DB write.
- Without ``--dry-run`` AND without ``--yes`` the command requires
  interactive confirmation (``y`` / ``yes``). This prevents an
  accidental ``python manage.py prune_audit_log`` from wiping the
  table when piped through `xargs` or run from an unattended shell.
- Counts the matching rows BEFORE deletion and prints the count,
  so the operator always sees the impact magnitude.

Cron recipe (operator)
----------------------
    # Every night at 03:30 UTC, prune entries older than 365d
    30 3 * * *  cd /app && python manage.py prune_audit_log --yes

For more aggressive policies pass ``--older-than``:

    python manage.py prune_audit_log --older-than 90 --yes   # 90d
    python manage.py prune_audit_log --older-than 30 --yes   # 30d
"""
from __future__ import annotations

import sys
from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = (
        "Delete AuditLogEntry rows older than the configured retention "
        "window (default: settings.AUDIT_LOG_RETENTION_DAYS = 365)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--older-than",
            type=int,
            default=None,
            help=(
                "Override retention age in days for this invocation. "
                "If omitted, falls back to settings.AUDIT_LOG_RETENTION_DAYS."
            ),
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print what would be deleted; perform no DB write.",
        )
        parser.add_argument(
            "--yes",
            action="store_true",
            help=(
                "Skip the interactive 'are you sure?' confirmation. "
                "Required when running from cron / non-interactive shells."
            ),
        )

    def handle(self, *args, **options):
        # Lazy import — keeps `manage.py help` listable even if the
        # apps registry is not yet populated.
        from apps.core.models import AuditLogEntry

        cli_days = options["older_than"]
        days = cli_days if cli_days is not None else getattr(
            settings, "AUDIT_LOG_RETENTION_DAYS", 365
        )
        if days < 0:
            raise CommandError(
                f"--older-than must be >= 0; got {days}. "
                "(Pass 0 to delete every audit row — operator beware.)"
            )

        cutoff = timezone.now() - timedelta(days=days)
        qs = AuditLogEntry.objects.filter(timestamp__lt=cutoff)
        count = qs.count()

        self.stdout.write(
            f"Audit log retention window: {days} day(s) "
            f"(cutoff = {cutoff.isoformat()})"
        )
        self.stdout.write(f"Matching rows to delete: {count}")

        if count == 0:
            self.stdout.write(self.style.SUCCESS(
                "Nothing to prune. Audit table is within retention window."
            ))
            return

        if options["dry_run"]:
            self.stdout.write(self.style.WARNING(
                "DRY RUN — no rows were deleted."
            ))
            # Show a tiny preview so the operator can sanity-check the cutoff.
            preview = list(qs.order_by("-timestamp")[:3].values_list(
                "timestamp", "action", "target_repr",
            ))
            if preview:
                self.stdout.write("Sample of would-delete rows (newest first):")
                for ts, action, repr_ in preview:
                    self.stdout.write(f"  - {ts.isoformat()} · {action} · {repr_}")
            return

        if not options["yes"]:
            if not sys.stdin.isatty():
                raise CommandError(
                    "Refusing to prune without --yes on a non-interactive "
                    "stdin. Add --yes if you are running from cron, or "
                    "run again with --dry-run from a terminal first to "
                    "inspect what would be removed."
                )
            self.stdout.write(self.style.WARNING(
                f"About to PERMANENTLY DELETE {count} AuditLogEntry rows."
            ))
            response = input("Type 'yes' to confirm: ").strip().lower()
            if response not in {"y", "yes"}:
                self.stdout.write("Aborted — no rows deleted.")
                return

        deleted, _ = qs.delete()
        self.stdout.write(self.style.SUCCESS(
            f"Pruned {deleted} AuditLogEntry row(s) older than {days} day(s)."
        ))
