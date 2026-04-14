"""Commerce Foundation v1 — Session 43 (Phase 3a).

Shared commerce engine that turns published_live ecommerce templates
(bottega-shop-artigianale, luxe-fashion-store) into operational shops.

Design principles:
- Shared engine. One set of models, two storefront skins dress it.
- Storefront = one WebTemplate with a commerce config. The skin
  archetype (artisan-workshop / fashion-editorial) selects the
  customer-facing template path.
- Money stored as Decimal(10, 2); currency per-storefront; no
  mixed-currency carts in v1.
- Guest checkout is a first-class path. Carts are session-keyed;
  users may optionally be attached. Order never requires auth.
- Payment is provider-agnostic via PaymentIntent. v1 ships two
  providers: `stub` (dev — auto-confirms) and `offline_bank_transfer`
  (real — prints wiring instructions). Stripe is a documented
  extension point, not implemented here.
- Fulfillment + payment statuses are tracked independently on Order,
  mirroring real commerce engines. Order.status is the high-level
  roll-up.
- No refunds flow, no reviews, no wishlists, no promotions in v1.
  Those are deliberately out of scope; the shape accommodates them
  without schema churn.
"""
from __future__ import annotations

import uuid
from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F, Sum
from django.utils.text import slugify

from apps.catalog.models import WebTemplate
from apps.core.models import TimestampedModel


# ── Storefront ─────────────────────────────────────────────────────

class Storefront(TimestampedModel):
    """A WebTemplate promoted to operational commerce.

    One row per WebTemplate that ships a real shop. The skin archetype
    drives which commerce skin directory serves product/cart/checkout
    pages. `is_operational` is the commerce-side equivalent of
    `WebTemplate.tier == published_live`: a storefront must be
    operational before its /shop/ URLs resolve.
    """

    class Skin(models.TextChoices):
        ARTISAN_WORKSHOP = "artisan-workshop", "Artisan Workshop"
        FASHION_EDITORIAL = "fashion-editorial", "Fashion Editorial"

    class PaymentProvider(models.TextChoices):
        STUB = "stub", "Stub · auto-conferma (dev)"
        OFFLINE_BANK_TRANSFER = "offline_bank_transfer", "Bonifico bancario"
        # STRIPE = "stripe", "Stripe" — extension point, not implemented v1

    template = models.OneToOneField(
        WebTemplate,
        on_delete=models.CASCADE,
        related_name="storefront",
    )
    skin = models.CharField(max_length=40, choices=Skin.choices)
    currency = models.CharField(max_length=3, default="EUR")
    currency_symbol = models.CharField(max_length=4, default="€")
    # "+39 055 …" — echoed on order confirmation, invoice lines.
    contact_phone = models.CharField(max_length=40, blank=True)
    contact_email = models.EmailField(blank=True)
    # Primary payment provider. v1 ships stub + offline_bank_transfer.
    payment_provider = models.CharField(
        max_length=40,
        choices=PaymentProvider.choices,
        default=PaymentProvider.STUB,
    )
    # Static policies rendered on customer-facing pages and email bodies.
    shipping_policy = models.TextField(
        blank=True,
        help_text="Shown on product + cart + checkout pages.",
    )
    return_policy = models.TextField(blank=True)
    bank_transfer_instructions = models.TextField(
        blank=True,
        help_text="Rendered on order confirmation when offline_bank_transfer is the provider.",
    )
    is_operational = models.BooleanField(
        default=False,
        help_text=(
            "Commerce-side shippability gate. A storefront must be "
            "operational before its /shop/ routes resolve publicly."
        ),
    )

    class Meta:
        ordering = ["template__name"]

    def __str__(self) -> str:
        return f"{self.template.name} storefront"

    @property
    def slug(self) -> str:
        return self.template.slug

    @property
    def skin_path(self) -> str:
        """Directory under templates/commerce/skins/ for this storefront."""
        return self.skin


# ── Catalog: Collection + Product + Variant + Image ────────────────

class Collection(TimestampedModel):
    """Merchandising grouping within a storefront.

    Bottega collections: Cuoio · Ceramica · Lino & tessuti · Conserve.
    Luxe collections: Drop 01 Spring 26 · Drop 02 Spring 26 · Atelier.
    """

    storefront = models.ForeignKey(
        Storefront,
        on_delete=models.CASCADE,
        related_name="collections",
    )
    slug = models.SlugField(max_length=140)
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=240, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]
        unique_together = [("storefront", "slug")]

    def __str__(self) -> str:
        return f"{self.storefront.slug} · {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(TimestampedModel):
    """A sellable item in a storefront catalog."""

    class Status(models.TextChoices):
        DRAFT = "draft", "Bozza"
        ACTIVE = "active", "Attivo"
        ARCHIVED = "archived", "Archiviato"

    storefront = models.ForeignKey(
        Storefront,
        on_delete=models.CASCADE,
        related_name="products",
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    slug = models.SlugField(max_length=160)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(
        max_length=240,
        blank=True,
        help_text="Sub-head rendered on product detail (e.g. 'Cuoio del Valdarno · cucito a sella').",
    )
    short_description = models.CharField(max_length=320, blank=True)
    long_description = models.TextField(blank=True)

    # Master SKU root. Variants append their own suffix.
    sku_root = models.CharField(max_length=40, blank=True)
    # Base price. Variants can override.
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    # Strike-through / compare-at. Optional.
    compare_at_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        help_text="Shown as strike-through if > base_price.",
    )
    # Editorial short marker shown as a ribbon / chip.
    badge = models.CharField(
        max_length=40, blank=True,
        help_text="Pezzo unico · Edizione · Drop 01 · Atelier · etc.",
    )
    # Edition number — displayed on artisan products (3 / 8) + fashion looks (Look 03).
    edition_number = models.CharField(max_length=40, blank=True)

    # Provenance / authorship (renders on product detail + PDP info row).
    material = models.CharField(max_length=160, blank=True)
    made_in = models.CharField(max_length=140, blank=True)
    creator_name = models.CharField(
        max_length=140, blank=True,
        help_text="Bottega: artisan name. Luxe: atelier / textile house.",
    )

    # Status + featured + display order.
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    featured = models.BooleanField(default=False, db_index=True)
    order = models.PositiveIntegerField(default=0)

    # Primary image URL (kept as URL in v1 to reuse curated Unsplash assets).
    hero_image_url = models.URLField(blank=True)

    # Freeform specs dict — rendered as a typographic table on PDP.
    # Shape: [{"label": "Materia", "value": "Cuoio del Valdarno · concia vegetale"}, ...]
    info_rows = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["order", "-featured", "title"]
        unique_together = [("storefront", "slug")]
        indexes = [
            models.Index(fields=["storefront", "status"]),
            models.Index(fields=["storefront", "featured"]),
        ]

    def __str__(self) -> str:
        return f"{self.storefront.slug} · {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    # ── Derived state ──────────────────────────────────────────────

    def total_stock(self) -> int:
        agg = self.variants.filter(is_active=True).aggregate(s=Sum("stock"))
        return int(agg["s"] or 0)

    @property
    def is_sold_out(self) -> bool:
        """True when no active variant has stock."""
        return self.total_stock() <= 0

    @property
    def is_low_stock(self) -> bool:
        """Rough low-stock signal: any variant with 1–2 units left."""
        return self.variants.filter(is_active=True, stock__gt=0, stock__lte=2).exists()

    @property
    def display_price(self) -> Decimal:
        """Cheapest active variant price, fallback to base_price."""
        lowest = (
            self.variants.filter(is_active=True, price_override__isnull=False)
            .order_by("price_override")
            .values_list("price_override", flat=True)
            .first()
        )
        if lowest is not None and lowest < self.base_price:
            return lowest
        return self.base_price


class ProductImage(TimestampedModel):
    """Extra images for the PDP gallery strip."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image_url = models.URLField()
    alt_text = models.CharField(max_length=240, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "pk"]

    def __str__(self) -> str:
        return f"{self.product.title} #{self.order}"


class ProductVariant(TimestampedModel):
    """A concrete SKU under a Product.

    Up to 3 option axes (option1/2/3) — e.g. Taglia, Colore, Edizione.
    Labels are free-form text because the axes differ per product.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
    )
    sku = models.CharField(max_length=80, unique=True)

    # Axis labels live on Product-derived shape; each variant snaps values.
    option1 = models.CharField(max_length=80, blank=True)
    option2 = models.CharField(max_length=80, blank=True)
    option3 = models.CharField(max_length=80, blank=True)

    price_override = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "pk"]

    def __str__(self) -> str:
        return f"{self.product.title} · {self.variant_title or 'default'}"

    @property
    def price(self) -> Decimal:
        if self.price_override is not None:
            return self.price_override
        return self.product.base_price

    @property
    def variant_title(self) -> str:
        """Human label composed of option axes."""
        parts = [p for p in [self.option1, self.option2, self.option3] if p]
        return " · ".join(parts)

    @property
    def in_stock(self) -> bool:
        return self.is_active and self.stock > 0


# ── Cart ───────────────────────────────────────────────────────────

class Cart(TimestampedModel):
    """A draft basket, scoped to a single storefront.

    Carts are session-keyed. A user FK is optional (guest ok). On
    checkout submit the cart is consumed — `is_active` flips False and
    a new cart is opened on next add.
    """

    storefront = models.ForeignKey(
        Storefront,
        on_delete=models.CASCADE,
        related_name="carts",
    )
    session_key = models.CharField(max_length=64, db_index=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="carts",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-updated_at"]
        indexes = [
            models.Index(fields=["storefront", "session_key", "is_active"]),
        ]

    def __str__(self) -> str:
        return f"Cart {self.pk} · {self.storefront.slug}"

    def item_count(self) -> int:
        agg = self.items.aggregate(s=Sum("quantity"))
        return int(agg["s"] or 0)

    def subtotal(self) -> Decimal:
        total = Decimal("0.00")
        for item in self.items.all():
            total += item.line_total()
        return total


class CartItem(TimestampedModel):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.PROTECT,
        related_name="cart_items",
    )
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    # Snapshot the price at add time so a price bump doesn't silently
    # change the customer's basket total.
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["pk"]
        unique_together = [("cart", "variant")]

    def __str__(self) -> str:
        return f"{self.variant} × {self.quantity}"

    def line_total(self) -> Decimal:
        return self.unit_price * self.quantity


# ── Addresses + Shipping ───────────────────────────────────────────

class Address(TimestampedModel):
    """A postal address captured at checkout.

    Flattened on purpose: no contact book, no user history. Every
    order owns its own shipping + billing rows.
    """

    full_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    line1 = models.CharField(max_length=240)
    line2 = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=140)
    postal_code = models.CharField(max_length=40)
    region = models.CharField(max_length=140, blank=True)
    country = models.CharField(max_length=80, default="Italia")
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        return f"{self.full_name}, {self.city}"


class ShippingMethod(TimestampedModel):
    """A purchasable shipping option per storefront."""

    storefront = models.ForeignKey(
        Storefront,
        on_delete=models.CASCADE,
        related_name="shipping_methods",
    )
    code = models.SlugField(max_length=40)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=240, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    est_delivery_days = models.CharField(
        max_length=40, blank=True,
        help_text="e.g. '48 ore in Italia · 4 giorni in Europa'.",
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "price"]
        unique_together = [("storefront", "code")]

    def __str__(self) -> str:
        return f"{self.storefront.slug} · {self.title}"


# ── Orders ─────────────────────────────────────────────────────────

def _generate_reference() -> str:
    # Short human reference (uuid4 hex stub — collision risk negligible at this scale)
    return uuid.uuid4().hex[:10].upper()


class Order(TimestampedModel):
    """Immutable record of a purchase."""

    class Status(models.TextChoices):
        PENDING = "pending", "In attesa"
        CONFIRMED = "confirmed", "Confermato"
        SHIPPED = "shipped", "Spedito"
        DELIVERED = "delivered", "Consegnato"
        CANCELLED = "cancelled", "Annullato"

    class PaymentStatus(models.TextChoices):
        UNPAID = "unpaid", "Da pagare"
        PAID = "paid", "Pagato"
        REFUNDED = "refunded", "Rimborsato"
        FAILED = "failed", "Fallito"

    class FulfillmentStatus(models.TextChoices):
        UNFULFILLED = "unfulfilled", "Da preparare"
        PACKING = "packing", "In preparazione"
        SHIPPED = "shipped", "Spedito"
        DELIVERED = "delivered", "Consegnato"
        RETURNED = "returned", "Reso"

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)
    reference = models.CharField(max_length=12, unique=True, default=_generate_reference, db_index=True)

    storefront = models.ForeignKey(
        Storefront,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="orders",
    )

    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=40, blank=True)

    shipping_address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name="orders_shipped_to",
    )
    billing_address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name="orders_billed_to",
        null=True, blank=True,
        help_text="If null, shipping address doubles as billing.",
    )
    shipping_method = models.ForeignKey(
        ShippingMethod,
        on_delete=models.PROTECT,
        related_name="orders",
    )

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    tax_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="EUR")

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, db_index=True)
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
        db_index=True,
    )
    fulfillment_status = models.CharField(
        max_length=20,
        choices=FulfillmentStatus.choices,
        default=FulfillmentStatus.UNFULFILLED,
        db_index=True,
    )

    customer_note = models.TextField(blank=True)
    seller_note = models.TextField(blank=True)

    # Populated when fulfillment_status transitions to shipped.
    tracking_carrier = models.CharField(max_length=80, blank=True)
    tracking_number = models.CharField(max_length=140, blank=True)

    confirmed_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["storefront", "status"]),
            models.Index(fields=["storefront", "-created_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.reference} · {self.storefront.slug}"


class OrderItem(TimestampedModel):
    """Snapshot of a purchased line.

    Snapshots are deliberate: products can be renamed/archived after
    purchase, but the order must always render what was bought.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="order_items",
    )
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="order_items",
    )

    product_title = models.CharField(max_length=200)
    variant_title = models.CharField(max_length=200, blank=True)
    sku = models.CharField(max_length=80, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)

    class Meta:
        ordering = ["pk"]


# ── Payment abstraction ────────────────────────────────────────────

class PaymentIntent(TimestampedModel):
    """Provider-agnostic payment attempt against an Order.

    v1 ships two providers:
    - `stub`: dev auto-confirm; used to prove the end-to-end flow works
      without leaving the dev environment.
    - `offline_bank_transfer`: real usable path; creates the intent as
      `awaiting_transfer`. The seller marks it paid manually from the
      dashboard once the bank wire lands.

    Stripe is a deliberate extension point: adding it is a matter of
    mapping `create_intent` / `confirm_intent` / webhook events to
    this table. Not implemented in v1.
    """

    class Status(models.TextChoices):
        INITIATED = "initiated", "Avviato"
        AWAITING_TRANSFER = "awaiting_transfer", "In attesa di bonifico"
        SUCCEEDED = "succeeded", "Riuscito"
        FAILED = "failed", "Fallito"
        CANCELLED = "cancelled", "Annullato"

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="payment_intents",
    )
    provider = models.CharField(max_length=40)
    provider_reference = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="EUR")
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.INITIATED)
    payload = models.JSONField(default=dict, blank=True)
    succeeded_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.order.reference} · {self.provider} · {self.status}"
