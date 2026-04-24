from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.catalog"
    verbose_name = "Catalog"

    def ready(self):
        # Phase X.4a Step 2 · P0-1 / P0-2: register build-time gates for
        # the corporate-suite archetype. The checks promote the Step 1A
        # palette-safety + Step 1C imagery-policy contracts from
        # ``UserWarning`` (runtime) to ``django.core.checks.Error``
        # (build-time), so a regression fails CI before review.
        from django.core.checks import Tags, register

        from apps.catalog.checks import (
            check_corporate_suite_imagery,
            check_corporate_suite_palettes,
        )

        register(check_corporate_suite_palettes, Tags.compatibility)
        register(check_corporate_suite_imagery, Tags.compatibility)
