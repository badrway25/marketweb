"""Write-side orchestration for commerce flows.

Every state transition that touches the DB lives here. Views call
these; templates never touch the ORM.

Guard rails:
- Inventory is decremented on order creation (not at payment time).
  This matches the common "hold the stock at checkout" pattern and
  avoids race conditions where two customers confirm the same unit.
  If payment fails later, a compensating service (not in v1) would
  roll stock back; for the dev `stub` provider payment auto-succeeds
  so there is no race window.
- Payment provider dispatch is keyed off storefront.payment_provider.
  Adding Stripe is a matter of registering a new `_handle_<provider>`
  helper and a webhook endpoint.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from django.db import transaction
from django.utils import timezone

from apps.commerce.models import (
    Address,
    Cart,
    CartItem,
    Order,
    OrderItem,
    PaymentIntent,
    ProductVariant,
    ShippingMethod,
    Storefront,
)
from apps.commerce import payments
from apps.core.audit import audited
from apps.core.models import AuditLogEntry


# ── Errors ─────────────────────────────────────────────────────────
#
# Every service-layer error carries a stable `code` and a `params` dict so
# the calling view can translate the message via commerce chrome keys
# (apps/commerce/i18n.py → `msg_*`). The exception's string form remains an
# IT fallback so logs and admin surfaces still read.

class CommerceError(Exception):
    """Base class for commerce service errors surfaced to the UI."""
    code = "generic"

    def __init__(self, message: str = "", *, code: str | None = None, params: dict | None = None):
        super().__init__(message)
        if code:
            self.code = code
        self.params = params or {}


class OutOfStockError(CommerceError):
    """Requested quantity exceeds what the variant currently holds."""
    code = "out_of_stock"


class EmptyCartError(CommerceError):
    code = "empty_cart"


class InvalidShippingMethod(CommerceError):
    code = "invalid_shipping"


# ── Cart lifecycle ─────────────────────────────────────────────────

def get_or_create_cart(*, storefront: Storefront, session_key: str, user=None) -> Cart:
    cart = (
        Cart.objects
        .filter(storefront=storefront, session_key=session_key, is_active=True)
        .first()
    )
    if cart is None:
        cart = Cart.objects.create(
            storefront=storefront,
            session_key=session_key,
            user=user if (user and user.is_authenticated) else None,
        )
    elif user and user.is_authenticated and cart.user_id is None:
        cart.user = user
        cart.save(update_fields=["user"])
    return cart


@transaction.atomic
def add_to_cart(
    *, cart: Cart, variant: ProductVariant, quantity: int = 1
) -> CartItem:
    if quantity < 1:
        raise CommerceError("La quantità minima è 1.", code="cart_min_qty")
    if variant.product.storefront_id != cart.storefront_id:
        raise CommerceError("Articolo non disponibile in questo shop.",
                            code="cart_different_store")
    if not variant.is_active:
        raise CommerceError("Variante non in vendita.",
                            code="cart_inactive_variant")

    existing = cart.items.filter(variant=variant).first()
    new_qty = (existing.quantity if existing else 0) + quantity
    if new_qty > variant.stock:
        raise OutOfStockError(
            f"Rimangono solo {variant.stock} pezzi di {variant.product.title}.",
            params={"stock": variant.stock, "title": variant.product.title},
        )

    if existing:
        existing.quantity = new_qty
        existing.unit_price = variant.price
        existing.save(update_fields=["quantity", "unit_price", "updated_at"])
        return existing

    return CartItem.objects.create(
        cart=cart,
        variant=variant,
        quantity=quantity,
        unit_price=variant.price,
    )


@transaction.atomic
def update_cart_item(*, cart: Cart, item_id: int, quantity: int) -> Optional[CartItem]:
    """Set absolute quantity on a cart item. quantity <= 0 removes it."""
    item = cart.items.filter(pk=item_id).select_related("variant").first()
    if item is None:
        return None
    if quantity <= 0:
        item.delete()
        return None
    if quantity > item.variant.stock:
        raise OutOfStockError(
            f"Rimangono solo {item.variant.stock} pezzi di {item.variant.product.title}.",
            params={"stock": item.variant.stock, "title": item.variant.product.title},
        )
    item.quantity = quantity
    item.unit_price = item.variant.price
    item.save(update_fields=["quantity", "unit_price", "updated_at"])
    return item


def remove_cart_item(*, cart: Cart, item_id: int) -> bool:
    deleted, _ = cart.items.filter(pk=item_id).delete()
    return deleted > 0


def clear_cart(cart: Cart) -> None:
    cart.items.all().delete()


# ── Checkout / order creation ──────────────────────────────────────

@dataclass
class CheckoutPayload:
    """Form-backed payload for create_order."""
    full_name: str
    email: str
    phone: str = ""
    line1: str = ""
    line2: str = ""
    city: str = ""
    postal_code: str = ""
    region: str = ""
    country: str = "Italia"
    shipping_method_code: str = ""
    customer_note: str = ""


def _resolve_shipping(storefront: Storefront, code: str) -> ShippingMethod:
    method = ShippingMethod.objects.filter(
        storefront=storefront, code=code, is_active=True
    ).first()
    if method is None:
        raise InvalidShippingMethod(
            f"Metodo di spedizione '{code}' non disponibile.",
            params={"code": code},
        )
    return method


@transaction.atomic
def create_order_from_cart(
    *, cart: Cart, payload: CheckoutPayload, user=None
) -> Order:
    """Materialize an Order from a Cart.

    Decrements variant stock (transactional). Creates an immutable
    snapshot of every line. Dispatches a PaymentIntent based on the
    storefront's configured provider. Cart is marked inactive.
    """
    if cart.items.count() == 0:
        raise EmptyCartError("Il carrello è vuoto.", code="empty_cart")

    storefront = cart.storefront
    shipping_method = _resolve_shipping(storefront, payload.shipping_method_code)

    # Lock variants to avoid overselling under concurrent checkouts.
    locked_items = list(
        cart.items
        .select_for_update()
        .select_related("variant", "variant__product")
    )
    for item in locked_items:
        variant = ProductVariant.objects.select_for_update().get(pk=item.variant_id)
        if variant.stock < item.quantity:
            raise OutOfStockError(
                f"Rimangono solo {variant.stock} pezzi di {variant.product.title}.",
                params={"stock": variant.stock, "title": variant.product.title},
            )

    subtotal = sum((i.line_total() for i in locked_items), Decimal("0.00"))
    shipping_total = shipping_method.price
    grand_total = subtotal + shipping_total

    shipping_address = Address.objects.create(
        full_name=payload.full_name,
        line1=payload.line1,
        line2=payload.line2,
        city=payload.city,
        postal_code=payload.postal_code,
        region=payload.region,
        country=payload.country or "Italia",
        phone=payload.phone,
        email=payload.email,
    )

    order = Order.objects.create(
        storefront=storefront,
        user=user if (user and user.is_authenticated) else None,
        customer_name=payload.full_name,
        customer_email=payload.email,
        customer_phone=payload.phone,
        shipping_address=shipping_address,
        shipping_method=shipping_method,
        subtotal=subtotal,
        shipping_total=shipping_total,
        grand_total=grand_total,
        currency=storefront.currency,
        customer_note=payload.customer_note,
    )

    for item in locked_items:
        variant = item.variant
        product = variant.product
        hero = product.hero_image_url or (
            product.images.first().image_url if product.images.exists() else ""
        )
        OrderItem.objects.create(
            order=order,
            product=product,
            variant=variant,
            product_title=product.title,
            variant_title=variant.variant_title,
            sku=variant.sku,
            unit_price=item.unit_price,
            quantity=item.quantity,
            line_total=item.line_total(),
            image_url=hero or "",
        )
        # Stock decrement — guarded by select_for_update above.
        ProductVariant.objects.filter(pk=variant.pk).update(stock=variant.stock - item.quantity)

    # Dispatch payment via the provider abstraction. Stripe intents
    # start as INITIATED and need the customer to complete the
    # Elements flow on a follow-up page; stub + offline bank
    # transfer terminate synchronously here.
    result = payments.dispatch(payments.PaymentContext(order=order))
    intent = result.intent

    # Reflect intent on order if already terminal.
    order.refresh_from_db()
    if intent.status == PaymentIntent.Status.SUCCEEDED:
        order.payment_status = Order.PaymentStatus.PAID
        order.status = Order.Status.CONFIRMED
        order.confirmed_at = timezone.now()
        order.save(update_fields=["payment_status", "status", "confirmed_at", "updated_at"])

    # Consume cart.
    cart.is_active = False
    cart.save(update_fields=["is_active", "updated_at"])

    return order


@transaction.atomic
def retry_payment(*, order: Order) -> PaymentIntent:
    """Open a fresh PaymentIntent for an order whose previous attempt
    is in a terminal failed state.

    Used by the customer-facing retry CTA on the order confirmation
    page. No stock is touched — that was locked at order creation.
    """
    if order.payment_status == Order.PaymentStatus.PAID:
        raise CommerceError("Questo ordine è già stato pagato.", code="already_paid")
    result = payments.dispatch(payments.PaymentContext(order=order))
    return result.intent


# ── Seller operations ──────────────────────────────────────────────

@audited(
    action=AuditLogEntry.Action.ORDER_PAID,
    target_arg="order",
    metadata_args=("note",),
)
@transaction.atomic
def mark_order_paid(*, order: Order, note: str = "") -> Order:
    """Seller-side mark-as-paid for bank-transfer style flows.

    T33 · the ``@audited`` decorator writes an explicit
    ``order_paid`` AuditLogEntry on successful return, carrying the
    seller's free-form ``note`` as metadata. The T31 signal still
    fires the generic UPDATED row for the ``payment_status`` /
    ``status`` field changes; the two rows are complementary.
    """
    order.payment_status = Order.PaymentStatus.PAID
    if order.status == Order.Status.PENDING:
        order.status = Order.Status.CONFIRMED
        order.confirmed_at = timezone.now()
    order.save(update_fields=["payment_status", "status", "confirmed_at", "updated_at"])

    # Flip the latest awaiting intent to succeeded.
    intent = (
        order.payment_intents
        .filter(status=PaymentIntent.Status.AWAITING_TRANSFER)
        .order_by("-created_at")
        .first()
    )
    if intent:
        intent.status = PaymentIntent.Status.SUCCEEDED
        intent.succeeded_at = timezone.now()
        if note:
            intent.payload = {**intent.payload, "seller_note": note}
        intent.save(update_fields=["status", "succeeded_at", "payload", "updated_at"])
    return order


@audited(
    action=AuditLogEntry.Action.ORDER_FULFILLMENT_CHANGED,
    target_arg="order",
    metadata_args=("fulfillment_status", "tracking_carrier", "tracking_number"),
)
@transaction.atomic
def set_order_fulfillment(
    *,
    order: Order,
    fulfillment_status: str,
    tracking_carrier: str = "",
    tracking_number: str = "",
) -> Order:
    """Seller fulfillment state machine.

    T35 · the ``@audited`` decorator writes an explicit
    ``order_fulfillment_changed`` AuditLogEntry on successful
    return, carrying the new fulfillment_status + the tracking
    fields (when SHIPPED) as metadata. The T31 signal-driven
    UPDATED row is also emitted (Order is in TRACKED_MODELS) —
    the two are complementary, not duplicates.

    Failure path: when ``fulfillment_status`` is not a valid
    enum value, the function raises ``CommerceError`` BEFORE
    ``order.save()`` — neither the signal-driven UPDATED row nor
    the T35 explicit row is written.
    """
    valid = {c for c, _ in Order.FulfillmentStatus.choices}
    if fulfillment_status not in valid:
        raise CommerceError(f"Unknown fulfillment status: {fulfillment_status}")
    order.fulfillment_status = fulfillment_status
    now = timezone.now()
    if fulfillment_status == Order.FulfillmentStatus.SHIPPED:
        order.status = Order.Status.SHIPPED
        order.shipped_at = now
        order.tracking_carrier = tracking_carrier
        order.tracking_number = tracking_number
    elif fulfillment_status == Order.FulfillmentStatus.DELIVERED:
        order.status = Order.Status.DELIVERED
        order.delivered_at = now
    order.save()
    return order


@audited(
    action=AuditLogEntry.Action.ORDER_CANCELLED,
    target_arg="order",
    metadata_args=("reason",),
)
@transaction.atomic
def cancel_order(*, order: Order, reason: str = "") -> Order:
    """Seller / admin order cancellation.

    T33 · the ``@audited`` decorator writes an explicit
    ``order_cancelled`` AuditLogEntry on successful return, carrying
    the ``reason`` as metadata. The semantic event "this order was
    cancelled BECAUSE X" would otherwise be lost — the T31 signal
    only records the ``status`` field diff.
    """
    if order.status in {Order.Status.DELIVERED, Order.Status.CANCELLED}:
        raise CommerceError("Order cannot be cancelled from its current status.")

    # Return stock to each variant.
    for line in order.items.select_related("variant"):
        if line.variant is None:
            continue
        ProductVariant.objects.filter(pk=line.variant_id).update(
            stock=line.variant.stock + line.quantity
        )
    order.status = Order.Status.CANCELLED
    order.cancelled_at = timezone.now()
    if reason:
        order.seller_note = (order.seller_note or "") + f"\n[cancel] {reason}"
    order.save()
    return order
