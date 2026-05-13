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
        #
        # Phase X.4b · AP-4 pass 1 (P0-3 / P0-4): two additional checks
        # codify the accent-on-primary text-floor invariant
        # (DS-16 / BO-08 / BLOCK-11), one per enrolled palette and one
        # per chrome CSS rule. Together they convert AP-4 from prose-only
        # to mechanically caught.
        from django.core.checks import Tags, register

        from apps.catalog.checks import (
            check_corporate_suite_accent_contrast,
            check_corporate_suite_chrome_accent_text,
            check_corporate_suite_imagery,
            check_corporate_suite_palettes,
        )

        register(check_corporate_suite_palettes, Tags.compatibility)
        register(check_corporate_suite_imagery, Tags.compatibility)
        register(check_corporate_suite_accent_contrast, Tags.compatibility)
        register(check_corporate_suite_chrome_accent_text, Tags.compatibility)
