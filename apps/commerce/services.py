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


# ── Errors ─────────────────────────────────────────────────────────

class CommerceError(Exception):
    """Base class for commerce service errors surfaced to the UI."""


class OutOfStockError(CommerceError):
    """Requested quantity exceeds what the variant currently holds."""


class EmptyCartError(CommerceError):
    pass


class InvalidShippingMethod(CommerceError):
    pass


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
        raise CommerceError("Quantity must be at least 1.")
    if variant.product.storefront_id != cart.storefront_id:
        raise CommerceError("Variant belongs to a different storefront.")
    if not variant.is_active:
        raise CommerceError("Variant is not available for sale.")

    existing = cart.items.filter(variant=variant).first()
    new_qty = (existing.quantity if existing else 0) + quantity
    if new_qty > variant.stock:
        raise OutOfStockError(
            f"Only {variant.stock} unit(s) left for {variant.product.title}."
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
            f"Only {item.variant.stock} unit(s) left for {item.variant.product.title}."
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
        raise InvalidShippingMethod(f"Shipping method '{code}' is not available.")
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
        raise EmptyCartError("Il carrello è vuoto.")

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
                f"{variant.product.title}: disponibili {variant.stock}, "
                f"richiesti {item.quantity}."
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

    # Dispatch payment.
    intent = _dispatch_payment(order)

    # Reflect intent on order if auto-succeeded (stub provider).
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


# ── Payment dispatch ───────────────────────────────────────────────

def _dispatch_payment(order: Order) -> PaymentIntent:
    provider = order.storefront.payment_provider
    if provider == Storefront.PaymentProvider.STUB:
        return _handle_stub(order)
    if provider == Storefront.PaymentProvider.OFFLINE_BANK_TRANSFER:
        return _handle_offline_bank_transfer(order)
    # Unknown provider = initiated, awaiting seller intervention.
    return PaymentIntent.objects.create(
        order=order,
        provider=provider,
        amount=order.grand_total,
        currency=order.currency,
        status=PaymentIntent.Status.INITIATED,
    )


def _handle_stub(order: Order) -> PaymentIntent:
    return PaymentIntent.objects.create(
        order=order,
        provider=Storefront.PaymentProvider.STUB,
        amount=order.grand_total,
        currency=order.currency,
        status=PaymentIntent.Status.SUCCEEDED,
        succeeded_at=timezone.now(),
        payload={"note": "stub provider · auto-confirmed"},
    )


def _handle_offline_bank_transfer(order: Order) -> PaymentIntent:
    return PaymentIntent.objects.create(
        order=order,
        provider=Storefront.PaymentProvider.OFFLINE_BANK_TRANSFER,
        amount=order.grand_total,
        currency=order.currency,
        status=PaymentIntent.Status.AWAITING_TRANSFER,
        payload={
            "instructions": (
                order.storefront.bank_transfer_instructions
                or "Pagamento con bonifico bancario — il venditore invierà le coordinate via email."
            ),
            "reference": order.reference,
        },
    )


# ── Seller operations ──────────────────────────────────────────────

@transaction.atomic
def mark_order_paid(*, order: Order, note: str = "") -> Order:
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


@transaction.atomic
def set_order_fulfillment(
    *,
    order: Order,
    fulfillment_status: str,
    tracking_carrier: str = "",
    tracking_number: str = "",
) -> Order:
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


@transaction.atomic
def cancel_order(*, order: Order, reason: str = "") -> Order:
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
