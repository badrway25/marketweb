"""Seed the 12 catalog VisualStyle rows (X.2 Commit 2 · seed-only).

VisualStyle is the shared token-bundle descriptor introduced in X.2
Commit 1. This seed command populates the 12 base styles that the
public catalog gallery exposes as a facet and that per-template
backfill (Commit 3) maps each template to.

Idempotent: re-running the command creates zero duplicates. The slug
is the natural key; ``get_or_create`` gates every row and existing
records are left untouched so an operator can tune attributes in the
admin without the next seed run overwriting them.
"""

from django.core.management.base import BaseCommand

from apps.catalog.models import VisualStyle


# 12 base visual styles. Order field groups the catalog sidebar facet:
# editorial tier first, dashboard tier second, minimal tier third,
# expressive/display tier fourth, specialty tier fifth.
VISUAL_STYLES = [
    {
        "slug": "editorial-warm",
        "label": "Editorial warm",
        "palette_family": "warm",
        "typography_stack": "serif-editorial",
        "density_profile": "editorial-sparse",
        "order": 10,
    },
    {
        "slug": "editorial-cool",
        "label": "Editorial cool",
        "palette_family": "cool",
        "typography_stack": "serif-editorial",
        "density_profile": "editorial-sparse",
        "order": 20,
    },
    {
        "slug": "editorial-noir",
        "label": "Editorial noir",
        "palette_family": "noir",
        "typography_stack": "serif-editorial",
        "density_profile": "editorial-sparse",
        "order": 30,
    },
    {
        "slug": "dashboard-dark",
        "label": "Dashboard dark",
        "palette_family": "dark",
        "typography_stack": "sans-modern",
        "density_profile": "dashboard-dense",
        "order": 40,
    },
    {
        "slug": "dashboard-light",
        "label": "Dashboard light",
        "palette_family": "neutral",
        "typography_stack": "sans-modern",
        "density_profile": "dashboard-dense",
        "order": 50,
    },
    {
        "slug": "minimal-light",
        "label": "Minimal light",
        "palette_family": "neutral",
        "typography_stack": "sans-modern",
        "density_profile": "minimal-card",
        "order": 60,
    },
    {
        "slug": "minimal-mono",
        "label": "Minimal mono",
        "palette_family": "neutral",
        "typography_stack": "mono-tech",
        "density_profile": "minimal-card",
        "order": 70,
    },
    {
        "slug": "bold-display",
        "label": "Bold display",
        "palette_family": "bold",
        "typography_stack": "display-bold",
        "density_profile": "minimal-card",
        "order": 80,
    },
    {
        "slug": "cinematic-fullbleed",
        "label": "Cinematic fullbleed",
        "palette_family": "noir",
        "typography_stack": "display-bold",
        "density_profile": "fullbleed-cinematic",
        "order": 90,
    },
    {
        "slug": "typographic-first",
        "label": "Typographic first",
        "palette_family": "neutral",
        "typography_stack": "serif-editorial",
        "density_profile": "editorial-sparse",
        "order": 100,
    },
    {
        "slug": "magazine-hybrid",
        "label": "Magazine hybrid",
        "palette_family": "warm",
        "typography_stack": "serif-editorial",
        "density_profile": "magazine-hybrid",
        "order": 110,
    },
    {
        "slug": "classic-serif",
        "label": "Classic serif",
        "palette_family": "neutral",
        "typography_stack": "serif-editorial",
        "density_profile": "editorial-sparse",
        "order": 120,
    },
]


class Command(BaseCommand):
    help = "Seed the 12 catalog VisualStyle rows (idempotent)."

    def handle(self, *args, **options):
        created_count = 0
        existing_count = 0
        for data in VISUAL_STYLES:
            _, created = VisualStyle.objects.get_or_create(
                slug=data["slug"],
                defaults={
                    "label": data["label"],
                    "palette_family": data["palette_family"],
                    "typography_stack": data["typography_stack"],
                    "density_profile": data["density_profile"],
                    "badge": data.get("badge", ""),
                    "order": data["order"],
                    "is_active": True,
                },
            )
            if created:
                created_count += 1
                self.stdout.write(f"  Created: {data['label']}")
            else:
                existing_count += 1
                self.stdout.write(f"  Exists:  {data['label']}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone. {created_count} visual styles created, "
                f"{existing_count} already existed. "
                f"Total in DB: {VisualStyle.objects.count()}."
            )
        )
