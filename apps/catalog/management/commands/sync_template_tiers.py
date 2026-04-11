"""
Sync WebTemplate.tier from TEMPLATE_REGISTRY.json.

TEMPLATE_REGISTRY.json is the documented source of truth for each
template's tier assignment (D-055, Session 20). This command reads
every row in the registry, looks up the matching WebTemplate by slug,
and applies the `tier` value.

Tier values accepted by the model (see WebTemplate.Tier):
    - "published_live"
    - "draft"

A row without a `tier` key is treated as `draft` — the binding default
per D-055. Unknown tier values abort with an error so a typo in the
registry can never silently downgrade the catalog.

Usage:
    python manage.py sync_template_tiers
    python manage.py sync_template_tiers --dry-run
"""

from __future__ import annotations

import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from apps.catalog.models import WebTemplate


DEFAULT_REGISTRY_PATH = Path(settings.BASE_DIR) / "TEMPLATE_REGISTRY.json"
VALID_TIERS = {t.value for t in WebTemplate.Tier}


class Command(BaseCommand):
    help = "Apply the `tier` field on every WebTemplate from TEMPLATE_REGISTRY.json."

    def add_arguments(self, parser):
        parser.add_argument(
            "--registry",
            type=Path,
            default=DEFAULT_REGISTRY_PATH,
            help="Path to TEMPLATE_REGISTRY.json (defaults to repo root).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print the planned changes without writing to the database.",
        )

    def handle(self, *args, **options):
        registry_path: Path = options["registry"]
        dry_run: bool = options["dry_run"]

        if not registry_path.exists():
            raise CommandError(f"Registry not found at {registry_path}")

        data = json.loads(registry_path.read_text(encoding="utf-8"))
        rows = data.get("templates", [])
        if not rows:
            raise CommandError("Registry contains no `templates` array")

        planned: list[tuple[str, str, str]] = []  # (slug, old, new)
        missing: list[str] = []

        for row in rows:
            slug = row.get("slug")
            if not slug:
                continue

            tier = row.get("tier", WebTemplate.Tier.DRAFT.value)
            if tier not in VALID_TIERS:
                raise CommandError(
                    f"Unknown tier '{tier}' on slug '{slug}'. "
                    f"Valid tiers: {sorted(VALID_TIERS)}"
                )

            try:
                tmpl = WebTemplate.objects.get(slug=slug)
            except WebTemplate.DoesNotExist:
                missing.append(slug)
                continue

            if tmpl.tier != tier:
                planned.append((slug, tmpl.tier, tier))
                if not dry_run:
                    tmpl.tier = tier
                    tmpl.save(update_fields=["tier"])

        # Report
        for slug, old, new in planned:
            self.stdout.write(f"  {slug}: {old} -> {new}")

        if missing:
            for slug in missing:
                self.stdout.write(
                    self.style.WARNING(f"  ? {slug} (not in DB, skipped)")
                )

        # Final counts from the DB after the writes (or current state in
        # dry-run) so the operator sees the resulting distribution.
        live = WebTemplate.objects.filter(
            tier=WebTemplate.Tier.PUBLISHED_LIVE
        ).count()
        draft = WebTemplate.objects.filter(
            tier=WebTemplate.Tier.DRAFT
        ).count()

        prefix = "[dry-run] " if dry_run else ""
        self.stdout.write(
            self.style.SUCCESS(
                f"\n{prefix}{len(planned)} tier(s) updated. "
                f"Catalog distribution: {live} published_live / {draft} draft."
            )
        )
