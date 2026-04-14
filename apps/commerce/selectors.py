"""Read-side queries for commerce flows.

Thin layer between views and the ORM — everything that returns a
queryset or a single object lives here. Views never compose filters.
"""
from __future__ import annotations

from typing import Optional

from django.db.models import Prefetch, Q

from apps.commerce.models import (
    Cart,
    Collection,
    Order,
    Product,
    ProductVariant,
    ShippingMethod,
    Storefront,
)


# ── Storefront ─────────────────────────────────────────────────────

def get_operational_storefront(slug: str) -> Optional[Storefront]:
    return (
        Storefront.objects
        .filter(template__slug=slug, is_operational=True)
        .select_related("template", "template__category", "template__brand")
        .first()
    )


def get_storefront(slug: str) -> Optional[Storefront]:
    """Returns a storefront regardless of operational state — used by
    seller dashboard, which must see the storefront even while dark."""
    return (
        Storefront.objects
        .filter(template__slug=slug)
        .select_related("template", "template__category", "template__brand")
        .first()
    )


# ── Product catalog ────────────────────────────────────────────────

def list_active_products(
    storefront: Storefront,
    *,
    collection_slug: Optional[str] = None,
    in_stock_only: bool = False,
    search: Optional[str] = None,
    sort: str = "recent",
):
    qs = (
        Product.objects
        .filter(storefront=storefront, status=Product.Status.ACTIVE)
        .select_related("collection")
        .prefetch_related(
            Prefetch("variants", queryset=ProductVariant.objects.filter(is_active=True)),
            "images",
        )
    )
    if collection_slug:
        qs = qs.filter(collection__slug=collection_slug)
    if search:
        qs = qs.filter(
            Q(title__icontains=search)
            | Q(short_description__icontains=search)
            | Q(material__icontains=search)
            | Q(creator_name__icontains=search)
        )
    if in_stock_only:
        qs = qs.filter(variants__is_active=True, variants__stock__gt=0).distinct()

    if sort == "price_asc":
        qs = qs.order_by("base_price")
    elif sort == "price_desc":
        qs = qs.order_by("-base_price")
    elif sort == "featured":
        qs = qs.order_by("-featured", "order")
    else:
        qs = qs.order_by("order", "-created_at")
    return qs


def get_product_detail(
    storefront: Storefront, product_slug: str
) -> Optional[Product]:
    return (
        Product.objects
        .filter(storefront=storefront, slug=product_slug, status=Product.Status.ACTIVE)
        .select_related("collection", "storefront__template")
        .prefetch_related(
            Prefetch(
                "variants",
                queryset=ProductVariant.objects.filter(is_active=True).order_by("order", "pk"),
            ),
            "images",
        )
        .first()
    )


def list_collections(storefront: Storefront):
    return Collection.objects.filter(storefront=storefront, is_active=True)


def get_collection(storefront: Storefront, slug: str) -> Optional[Collection]:
    return Collection.objects.filter(storefront=storefront, slug=slug, is_active=True).first()


def list_featured_products(storefront: Storefront, limit: int = 6):
    return (
        list_active_products(storefront, sort="featured")
        .filter(featured=True)[:limit]
    )


def list_related_products(product: Product, limit: int = 4):
    qs = (
        Product.objects
        .filter(
            storefront=product.storefront,
            status=Product.Status.ACTIVE,
        )
        .exclude(pk=product.pk)
        .select_related("collection")
    )
    if product.collection_id:
        qs = qs.filter(collection=product.collection)
    return qs.order_by("order")[:limit]


# ── Cart ───────────────────────────────────────────────────────────

def get_active_cart(storefront: Storefront, session_key: str) -> Optional[Cart]:
    return (
        Cart.objects
        .filter(storefront=storefront, session_key=session_key, is_active=True)
        .prefetch_related(
            "items",
            "items__variant",
            "items__variant__product",
        )
        .first()
    )


# ── Shipping ───────────────────────────────────────────────────────

def list_shipping_methods(storefront: Storefront):
    return ShippingMethod.objects.filter(storefront=storefront, is_active=True)


# ── Orders ─────────────────────────────────────────────────────────

def list_storefront_orders(storefront: Storefront, *, status: Optional[str] = None):
    qs = (
        Order.objects
        .filter(storefront=storefront)
        .select_related("shipping_address", "shipping_method")
        .prefetch_related("items")
    )
    if status:
        qs = qs.filter(status=status)
    return qs


def get_order_by_uuid(storefront: Storefront, uuid) -> Optional[Order]:
    return (
        Order.objects
        .filter(storefront=storefront, uuid=uuid)
        .select_related(
            "shipping_address", "billing_address", "shipping_method", "storefront__template"
        )
        .prefetch_related("items", "payment_intents")
        .first()
    )


def get_order_by_reference(reference: str) -> Optional[Order]:
    """Used by seller dashboard search — scoped to storefront downstream."""
    return (
        Order.objects
        .filter(reference=reference)
        .select_related("storefront", "shipping_address", "shipping_method")
        .prefetch_related("items")
        .first()
    )


def dashboard_stock_summary(storefront: Storefront):
    """Lightweight stock snapshot for the seller dashboard home."""
    products = Product.objects.filter(storefront=storefront).prefetch_related("variants")
    total_variants = 0
    sold_out = 0
    low = 0
    for p in products:
        for v in p.variants.all():
            if not v.is_active:
                continue
            total_variants += 1
            if v.stock == 0:
                sold_out += 1
            elif v.stock <= 2:
                low += 1
    return {
        "total_products": products.count(),
        "total_variants": total_variants,
        "sold_out": sold_out,
        "low_stock": low,
    }
