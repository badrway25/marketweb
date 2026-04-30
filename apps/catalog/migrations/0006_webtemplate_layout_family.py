"""Phase X.4b · CS-LAYOUT-22 · add layout_family to WebTemplate.

Adds a short string column carrying the corporate-suite layout-family
slot (LF-1..LF-6). Backfills the four current corporate-suite siblings
according to the family-backfill report so the LF-5 rebuild can
dispatch by family without a second migration:

    pragma-corporate-suite → LF-1
    fiscus-commercialista  → LF-3
    solaria-coaching       → LF-4
    continua-stewardship   → LF-5

Every other template stays at the empty default ('') because the field
is corporate-suite-specific. The corporate-suite shell treats an empty
layout_family as the LF-1 default so the dispatch is strictly additive.
"""
from __future__ import annotations

from django.db import migrations, models


CORPORATE_SUITE_FAMILY = {
    "pragma-corporate-suite": "LF-1",
    "fiscus-commercialista":  "LF-3",
    "solaria-coaching":       "LF-4",
    "continua-stewardship":   "LF-5",
}


def backfill_layout_family(apps, schema_editor):
    WebTemplate = apps.get_model("catalog", "WebTemplate")
    for slug, family in CORPORATE_SUITE_FAMILY.items():
        WebTemplate.objects.filter(slug=slug).update(layout_family=family)


def clear_layout_family(apps, schema_editor):
    WebTemplate = apps.get_model("catalog", "WebTemplate")
    WebTemplate.objects.filter(slug__in=CORPORATE_SUITE_FAMILY.keys()).update(
        layout_family=""
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_taxonomy_v2_not_null"),
    ]

    operations = [
        migrations.AddField(
            model_name="webtemplate",
            name="layout_family",
            field=models.CharField(
                blank=True,
                db_index=True,
                default="",
                help_text=(
                    "Corporate-suite layout family slot (LF-1..LF-6). Empty "
                    "for templates outside the corporate-suite cluster. "
                    "Drives the shared home shell's family dispatch."
                ),
                max_length=8,
            ),
        ),
        migrations.RunPython(
            backfill_layout_family,
            reverse_code=clear_layout_family,
        ),
    ]
