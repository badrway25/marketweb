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


class ProfessionCluster(TimestampedModel, SlugModel):
    """Profession-level cluster under a macro-category (X.2 Commit 1).

    A ``Category`` (agency, restaurant, medical, ...) contains many
    ``ProfessionCluster`` rows (creative, fine-dining, specialist, ...).
    Each ``WebTemplate`` may point to one cluster; the cluster is the
    granularity at which the catalog filters, search facets, and role/
    use-case discovery pages live.

    ``search_aliases`` stores space-separated terms the typeahead
    endpoint treats as additional prefix-match candidates (``chef``,
    ``stellato``, ``haute cuisine`` for the ``fine-dining`` cluster,
    etc.). Plain text, not a list — a single ``ILIKE`` over the column
    is sufficient for the MVP.
    """

    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="profession_clusters",
    )
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Icon class name (Bootstrap / FontAwesome).",
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    search_aliases = models.TextField(
        blank=True,
        default="",
        help_text=(
            "Space-separated alias terms for typeahead prefix matching "
            "(e.g. 'chef stellato haute-cuisine ristorante-gourmet')."
        ),
    )

    class Meta:
        ordering = ["category__order", "category__name", "order", "name"]
        indexes = [
            models.Index(fields=["is_active", "category"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class VisualStyle(TimestampedModel):
    """Shared visual-style descriptor referenced by many templates (X.2 Commit 1).

    A ``VisualStyle`` is a token bundle (palette family, typography
    stack, density profile, optional badge) that catalog filters expose
    as a facet. A given template points to exactly one style, but many
    templates share the same style — this is the reuse lever that
    decouples content+archetype from visual expression.

    ``VisualStyle`` does NOT inherit ``SlugModel`` because it carries
    a ``label`` rather than a ``name``; the slug is authored explicitly
    via seed commands (X.2 Commit 2), not auto-derived.
    """

    slug = models.SlugField(max_length=80, unique=True, db_index=True)
    label = models.CharField(max_length=120)
    palette_family = models.CharField(
        max_length=40,
        blank=True,
        help_text="e.g. 'warm', 'cool', 'dark', 'noir', 'neutral'.",
    )
    typography_stack = models.CharField(
        max_length=60,
        blank=True,
        help_text="e.g. 'serif-editorial', 'sans-modern', 'mono-tech'.",
    )
    density_profile = models.CharField(
        max_length=40,
        blank=True,
        help_text="e.g. 'editorial-sparse', 'dashboard-dense', 'minimal-card'.",
    )
    badge = models.CharField(
        max_length=20,
        blank=True,
        help_text="Optional marker shown in catalog cards, e.g. 'new', 'popular'.",
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "slug"]

    def __str__(self):
        return self.label


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

    class PriceTier(models.TextChoices):
        """Catalog-level price bucket used by filter facets (X.2 Commit 1).

        Distinct from the numeric ``price`` column — this is a coarse
        filter bucket ('free / standard / premium') surfaced as a
        checkbox-group facet in the gallery sidebar. Nullable during
        the X.2 backfill window; will be flipped to required in a
        follow-up commit after Commit 3 backfill validates.
        """

        FREE = "free", "Free"
        STANDARD = "standard", "Standard"
        PREMIUM = "premium", "Premium"

    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="templates",
    )
    # X.2 Commit 1 · additive 2-level taxonomy hook. Nullable during the
    # backfill window so existing rows don't require an immediate data
    # migration. Commit 3 populated all 20 MVP rows; X.3 Commit 5 (this
    # flip) tightens the contract to ``null=False`` — every template now
    # carries a profession_cluster and a visual_style by schema law.
    # ``category`` FK stays untouched for backward compatibility — every
    # cluster carries its own category FK so the two fields are kept
    # consistent at seed + backfill time.
    profession_cluster = models.ForeignKey(
        ProfessionCluster,
        on_delete=models.PROTECT,
        related_name="templates",
    )
    visual_style = models.ForeignKey(
        VisualStyle,
        on_delete=models.PROTECT,
        related_name="templates",
    )
    # X.2 Commit 1 · catalog discovery metadata. JSONField is used for
    # the open-ended lists (use_cases, audience) where the valid set is
    # expected to grow across waves without a schema migration. The
    # feature facets below use explicit BooleanField columns instead —
    # small closed set, indexable, and straightforward for ILIKE-free
    # filtering.
    use_cases = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "Array of use-case slugs (e.g. ['online-ordering', 'reservations', "
            "'menu-digital']). Surfaced as catalog filter + role/use-case "
            "discovery pages."
        ),
    )
    audience = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "Array of audience slugs (e.g. ['freelance', 'smb', 'agency', "
            "'enterprise']). Drives the 'Per ruolo' discovery block."
        ),
    )
    search_keywords = models.TextField(
        default="",
        blank=True,
        help_text=(
            "Space-separated terms fed into the typeahead endpoint as "
            "additional prefix-match candidates. Plain text, lowercase, "
            "accent-insensitive matching is done at query time."
        ),
    )
    price_tier = models.CharField(
        max_length=20,
        choices=PriceTier.choices,
        null=True,
        blank=True,
        db_index=True,
        help_text="Catalog filter bucket — coarser than the numeric `price`.",
    )
    # X.2 Commit 1 · explicit feature facets. Closed set · boolean
    # columns let the gallery sidebar aggregate counts in a single
    # ``Count`` query per facet without JSONField operators.
    has_shop = models.BooleanField(default=False, db_index=True)
    has_booking = models.BooleanField(default=False, db_index=True)
    has_portfolio = models.BooleanField(default=False, db_index=True)
    has_blog = models.BooleanField(default=False, db_index=True)
    has_video = models.BooleanField(default=False, db_index=True)
    has_rtl = models.BooleanField(default=False, db_index=True)
    is_multi_page = models.BooleanField(default=False, db_index=True)
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
