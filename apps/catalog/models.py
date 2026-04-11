from django.db import models

from apps.core.models import SlugModel, TimestampedModel


class Category(TimestampedModel, SlugModel):
    """Marketplace category (e.g., Agency, Restaurant, Medical)."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Icon class name (e.g., Bootstrap icon or FontAwesome)",
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Tag(TimestampedModel, SlugModel):
    """Flexible tag for template search and filtering."""

    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class WebTemplate(TimestampedModel, SlugModel):
    """A website template listing — the main marketplace product."""

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        REVIEW = "review", "In Review"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"

    class Tier(models.TextChoices):
        # Public, shippable: satisfies the full D-053 Live Preview Law.
        # Visible in every public surface (homepage, listing, category,
        # detail, search, related). D-055 made this binary — there is no
        # intermediate `published_static` tier.
        PUBLISHED_LIVE = "published_live", "Published Live"
        # Not yet shippable: fails at least one D-053 gate. Hidden from
        # every public surface. Staff can still reach it via `?preview=1`
        # per D-055 so authors can QA in progress.
        DRAFT = "draft", "Draft"

    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="templates",
    )
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="templates")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        db_index=True,
    )
    # D-055: binding public-tier gate. Default is `draft` so any newly
    # seeded template is invisible until it passes the D-053 gate and is
    # explicitly promoted to `published_live`.
    tier = models.CharField(
        max_length=20,
        choices=Tier.choices,
        default=Tier.DRAFT,
        db_index=True,
        help_text=(
            "Public tier per D-055. `published_live` templates appear in the "
            "public catalog; `draft` templates are hidden and reachable only "
            "by staff via the `?preview=1` query string."
        ),
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_free = models.BooleanField(default=False)
    preview_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False, db_index=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-featured", "order", "-created_at"]

    def __str__(self):
        return self.name

    @property
    def preview_asset(self):
        """Canonical preview image for this template.

        Explicitly filters `asset_type == preview` — never falls back to
        "whatever happens to be first in the assets relation". If multiple
        preview rows exist (defensive — the pipeline enforces one), the
        lowest-`order` one wins.

        Prefetch-aware: if the caller already called
        ``prefetch_related('assets')`` we iterate that cache instead of
        issuing a fresh query. Otherwise falls through to a filtered query.
        """
        cache = getattr(self, "_prefetched_objects_cache", None) or {}
        if "assets" in cache:
            candidates = [
                a for a in self.assets.all()
                if a.asset_type == TemplateAsset.AssetType.PREVIEW
            ]
            candidates.sort(key=lambda a: (a.order, a.pk))
            return candidates[0] if candidates else None
        return (
            self.assets.filter(asset_type=TemplateAsset.AssetType.PREVIEW)
            .order_by("order", "pk")
            .first()
        )


class TemplateBrand(TimestampedModel):
    """Unique brand identity for a web template (OneToOne)."""

    template = models.OneToOneField(
        WebTemplate,
        on_delete=models.CASCADE,
        related_name="brand",
    )
    brand_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200, blank=True)
    palette = models.JSONField(
        default=dict,
        blank=True,
        help_text='Color palette, e.g. {"primary": "#1a1a2e", "secondary": "#16213e", "accent": "#e94560"}',
    )
    typography = models.CharField(
        max_length=200,
        blank=True,
        help_text='Font pairing description, e.g. "Inter + Playfair Display"',
    )
    personality = models.CharField(
        max_length=200,
        blank=True,
        help_text='Visual personality, e.g. "minimal, bold, tech-forward"',
    )
    logo_concept = models.TextField(
        blank=True,
        help_text="Description of logo concept for this brand",
    )

    class Meta:
        ordering = ["brand_name"]

    def __str__(self):
        return f"{self.brand_name} ({self.template.name})"


class TemplateAsset(TimestampedModel):
    """File asset attached to a web template (images, thumbnails, previews)."""

    class AssetType(models.TextChoices):
        THUMBNAIL = "thumbnail", "Thumbnail"
        PREVIEW = "preview", "Preview Image"
        SCREENSHOT = "screenshot", "Screenshot"
        SOURCE = "source", "Source File"
        OTHER = "other", "Other"

    template = models.ForeignKey(
        WebTemplate,
        on_delete=models.CASCADE,
        related_name="assets",
    )
    file = models.FileField(upload_to="template_assets/%Y/%m/")
    asset_type = models.CharField(
        max_length=20,
        choices=AssetType.choices,
        default=AssetType.PREVIEW,
    )
    alt_text = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "asset_type"]

    def __str__(self):
        return f"{self.get_asset_type_display()} — {self.template.name}"
