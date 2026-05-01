"""Phase X.5 · Cornice (5th corporate-suite sibling · 1st LF-2 occupant).

Backfills `WebTemplate.layout_family` for the Cornice slug. The seed
command creates the WebTemplate row with the empty default; this
migration sets the LF-2 family slot so the corporate-suite home shell
dispatches to `_layouts/lf2/` rendering instead of LF-1's default.

The migration is strictly additive — every other corporate-suite sibling
keeps the layout_family value set in `0006_webtemplate_layout_family.py`.

    cornice-architettura → LF-2

If the row does not yet exist (seed has not run), the update is a no-op
and re-running `seed_templates` will create the row at empty default;
re-running this migration in `RunPython` mode is idempotent.
"""
from __future__ import annotations

from django.db import migrations


CORNICE_FAMILY = {
    "cornice-architettura": "LF-2",
}


def backfill_cornice_layout_family(apps, schema_editor):
    WebTemplate = apps.get_model("catalog", "WebTemplate")
    for slug, family in CORNICE_FAMILY.items():
        WebTemplate.objects.filter(slug=slug).update(layout_family=family)


def clear_cornice_layout_family(apps, schema_editor):
    WebTemplate = apps.get_model("catalog", "WebTemplate")
    WebTemplate.objects.filter(slug__in=CORNICE_FAMILY.keys()).update(
        layout_family=""
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_webtemplate_layout_family"),
    ]

    operations = [
        migrations.RunPython(
            backfill_cornice_layout_family,
            reverse_code=clear_cornice_layout_family,
        ),
    ]
