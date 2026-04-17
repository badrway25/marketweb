"""Garbage-collect orphan ProjectAsset rows and files.

A.5 · honours the D-094 promise. Default mode is DRY-RUN: prints
what would be deleted without touching filesystem or DB. Pass
``--apply`` to execute the cleanup. Scope can be narrowed to a
single project with ``--project=<uuid>``. Grace period (default
24h) protects assets created recently from a race with an
in-flight autosave.

Usage::

    # Dry-run, all projects, 24h grace (default)
    python manage.py gc_project_assets

    # Apply, single project, custom grace
    python manage.py gc_project_assets --apply --project=<uuid> --grace=6

Operator-facing command only. Not scheduled, not cron-wired, not
exposed via HTTP — see A.5 scope discipline.
"""
from __future__ import annotations

from django.core.management.base import BaseCommand, CommandError

from apps.projects import services
from apps.projects.models import CustomerProject


def _format_bytes(n: int) -> str:
    if n >= 1024 * 1024:
        return f"{n / (1024 * 1024):.1f} MB"
    if n >= 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n} B"


class Command(BaseCommand):
    help = "Remove ProjectAsset rows + files that are no longer referenced."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply", action="store_true", default=False,
            help="Execute the deletion. Without this flag the command is dry-run.",
        )
        parser.add_argument(
            "--project", type=str, default=None,
            help="Scope the scan to a single project (by uuid).",
        )
        parser.add_argument(
            "--grace", type=float, default=24.0,
            help="Grace period in hours. Assets younger than this are skipped. Default 24.",
        )

    def handle(self, *args, **options):
        apply_mode = bool(options["apply"])
        grace = float(options["grace"])
        if grace < 0:
            raise CommandError("--grace must be >= 0")

        project = None
        scope_label = "all projects"
        if options["project"]:
            project = CustomerProject.objects.filter(uuid=options["project"]).first()
            if project is None:
                raise CommandError(f"Project {options['project']} not found.")
            scope_label = f"project {project.uuid}"

        mode_label = "APPLY" if apply_mode else "DRY-RUN"
        self.stdout.write(
            f"GC project assets \u2014 mode {mode_label} \u00b7 grace {grace}h \u00b7 scope: {scope_label}"
        )

        orphans = services.find_unreferenced_assets(project=project, grace_hours=grace)
        self.stdout.write(f"Candidate orphans found: {len(orphans)}")

        if not orphans:
            self.stdout.write("")
            self.stdout.write("Nothing to clean up.")
            return

        stats = services.delete_unreferenced_assets(orphans, dry_run=not apply_mode)
        self.stdout.write("")
        marker = "\u2713" if apply_mode else "-"
        for asset, path in zip(orphans, stats["paths"]):
            size = _format_bytes(asset.size_bytes or 0)
            self.stdout.write(f"  {marker} {path:60} {size}")
        self.stdout.write("")

        freed = _format_bytes(stats["bytes_freed"])
        if apply_mode:
            self.stdout.write(
                f"Deleted: {stats['deleted']} / {stats['scanned']} "
                f"(skipped {stats['skipped']}). Freed {freed}."
            )
            for err in stats["errors"]:
                self.stdout.write(self.style.ERROR(f"  ! {err}"))
        else:
            self.stdout.write(
                f"Would free: {freed} across {stats['scanned']} files."
            )
            self.stdout.write("No changes made (dry-run). Re-run with --apply to delete.")
