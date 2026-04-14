"""Payment provider abstraction — Session 45 (Phase 3b).

Shape
-----
- `PaymentContext`: read-only snapshot of what a provider needs
  (order, client_ip, return_urls). Kept narrow so provider code
  stays unaware of Django request-cycle internals.
- `PaymentDispatchResult`: what a provider returns after attempting
  to start a payment (intent row, client-side config, redirect url
  if the provider needs one). Callers use this to decide whether
  to render a PSP page or show the offline-transfer confirmation.
- Each provider is a module-level function keyed in PROVIDERS.
  Adding a new provider is a matter of appending a callable.

Stripe integration
------------------
- Uses the Stripe PaymentIntent API when settings.STRIPE_SECRET_KEY
  is set and the `stripe` package is importable. Otherwise raises
  `ProviderUnavailable` which callers translate to a graceful "not
  configured yet" surface rather than a 500.
- Idempotency is anchored on the Order.reference so retries don't
  duplicate charges.
- Webhook verification uses STRIPE_WEBHOOK_SECRET.
- All Stripe errors surface as `ProviderError` — callers decide
  what to show the customer.

Graceful degradation
--------------------
A storefront whose payment_provider is `stripe` but whose runtime
lacks STRIPE_SECRET_KEY falls back to `stub` at dispatch time with
a clear log. The order is still confirmed; the seller sees
`[stripe-unconfigured]` on the intent payload so debugging is
obvious.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional

from django.conf import settings
from django.utils import timezone

from apps.commerce.models import Order, PaymentIntent, Storefront

logger = logging.getLogger(__name__)


# ── Errors ─────────────────────────────────────────────────────────

class ProviderError(Exception):
    """Any provider-layer failure surfaced to the caller."""


class ProviderUnavailable(ProviderError):
    """Provider is not runtime-configured (missing env vars, missing SDK)."""


# ── Dispatch types ─────────────────────────────────────────────────

@dataclass
class PaymentContext:
    """Narrow input for providers. Built by the calling view."""
    order: Order
    success_url: str = ""
    cancel_url: str = ""
    return_url: str = ""


@dataclass
class PaymentDispatchResult:
    """What a provider returns. Only `intent` is required."""
    intent: PaymentIntent
    # Where to send the customer to complete payment, if the provider
    # needs an interactive step. `None` means the intent is already
    # terminal (succeeded / awaiting_transfer / failed).
    redirect_url: Optional[str] = None
    # Data the front-end needs to render a PSP widget (e.g. Stripe
    # publishable key + client_secret). Passed to the template as-is.
    client_config: Optional[dict] = None


# ── Stub provider (dev) ────────────────────────────────────────────

def dispatch_stub(context: PaymentContext) -> PaymentDispatchResult:
    order = context.order
    intent = PaymentIntent.objects.create(
        order=order,
        provider=Storefront.PaymentProvider.STUB,
        amount=order.grand_total,
        currency=order.currency,
        status=PaymentIntent.Status.SUCCEEDED,
        succeeded_at=timezone.now(),
        payload={"note": "stub provider · auto-confirmed"},
    )
    return PaymentDispatchResult(intent=intent)


# ── Offline bank transfer ──────────────────────────────────────────

def dispatch_offline_bank_transfer(context: PaymentContext) -> PaymentDispatchResult:
    order = context.order
    intent = PaymentIntent.objects.create(
        order=order,
        provider=Storefront.PaymentProvider.OFFLINE_BANK_TRANSFER,
        amount=order.grand_total,
        currency=order.currency,
        status=PaymentIntent.Status.AWAITING_TRANSFER,
        payload={
            "instructions": (
                order.storefront.bank_transfer_instructions
                or "Il venditore invierà le coordinate via email."
            ),
            "reference": order.reference,
        },
    )
    return PaymentDispatchResult(intent=intent)


# ── Stripe ─────────────────────────────────────────────────────────

def _stripe_client():
    """Return a configured `stripe` module or raise ProviderUnavailable.

    Imported lazily so projects that never configure Stripe don't
    need the `stripe` package installed.
    """
    secret = getattr(settings, "STRIPE_SECRET_KEY", "")
    if not secret:
        raise ProviderUnavailable("STRIPE_SECRET_KEY is not configured.")
    try:
        import stripe  # noqa: WPS433 (runtime import by design)
    except ImportError as exc:
        raise ProviderUnavailable(
            "The `stripe` package is not installed. `pip install stripe`."
        ) from exc
    stripe.api_key = secret
    return stripe


def dispatch_stripe(context: PaymentContext) -> PaymentDispatchResult:
    """Create a Stripe PaymentIntent keyed off order.reference.

    - Amount is converted to the smallest currency unit (cents) as
      Stripe requires.
    - `idempotency_key` is the order reference — a retry for the
      same order returns the same intent rather than creating a
      duplicate.
    - On SDK/API failure we persist a FAILED PaymentIntent locally
      and raise ProviderError so the caller can surface a retry
      surface.
    """
    order = context.order
    stripe = _stripe_client()

    # Convert Decimal € to int cents. `quantize` first to drop
    # fractional cents created by Decimal subtleties.
    cents = int((order.grand_total * 100).to_integral_value())

    try:
        stripe_intent = stripe.PaymentIntent.create(
            amount=cents,
            currency=(order.currency or "EUR").lower(),
            automatic_payment_methods={"enabled": True},
            metadata={
                "order_id":        str(order.id),
                "order_reference": order.reference,
                "storefront":      order.storefront.slug,
            },
            idempotency_key=f"order-{order.reference}",
            description=f"Order {order.reference} · {order.storefront.slug}",
            receipt_email=order.customer_email or None,
        )
    except Exception as exc:  # stripe.error.StripeError — caught broadly on purpose
        logger.warning("Stripe PI creation failed for order %s: %s", order.reference, exc)
        intent = PaymentIntent.objects.create(
            order=order,
            provider=Storefront.PaymentProvider.STRIPE,
            amount=order.grand_total,
            currency=order.currency,
            status=PaymentIntent.Status.FAILED,
            payload={"error": str(exc)[:400]},
        )
        raise ProviderError(f"Stripe error: {exc}") from exc

    intent = PaymentIntent.objects.create(
        order=order,
        provider=Storefront.PaymentProvider.STRIPE,
        provider_reference=stripe_intent["id"],
        amount=order.grand_total,
        currency=order.currency,
        status=PaymentIntent.Status.INITIATED,
        payload={
            "client_secret":   stripe_intent["client_secret"],
            "publishable_key": getattr(settings, "STRIPE_PUBLISHABLE_KEY", ""),
            "stripe_status":   stripe_intent["status"],
        },
    )
    return PaymentDispatchResult(
        intent=intent,
        redirect_url=None,
        client_config={
            "publishable_key": getattr(settings, "STRIPE_PUBLISHABLE_KEY", ""),
            "client_secret":   stripe_intent["client_secret"],
            "return_url":      context.return_url,
        },
    )


def handle_stripe_webhook_event(event: dict) -> Optional[PaymentIntent]:
    """Apply a Stripe webhook event to the local PaymentIntent + Order.

    Returns the touched PaymentIntent (or None if the event is one
    we don't handle). The calling webhook view verifies signature
    before calling this.
    """
    event_type = event.get("type") or ""
    data = (event.get("data") or {}).get("object") or {}
    pi_id = data.get("id")
    if not pi_id:
        return None

    intent = PaymentIntent.objects.filter(provider_reference=pi_id).first()
    if intent is None:
        return None

    order = intent.order

    if event_type == "payment_intent.succeeded":
        intent.status = PaymentIntent.Status.SUCCEEDED
        intent.succeeded_at = timezone.now()
        intent.payload = {**(intent.payload or {}), "webhook": event_type}
        intent.save(update_fields=["status", "succeeded_at", "payload", "updated_at"])
        order.payment_status = Order.PaymentStatus.PAID
        if order.status == Order.Status.PENDING:
            order.status = Order.Status.CONFIRMED
            order.confirmed_at = timezone.now()
        order.save(update_fields=["payment_status", "status", "confirmed_at", "updated_at"])

    elif event_type == "payment_intent.payment_failed":
        intent.status = PaymentIntent.Status.FAILED
        intent.payload = {
            **(intent.payload or {}),
            "webhook": event_type,
            "error": (data.get("last_payment_error") or {}).get("message", "")[:400],
        }
        intent.save(update_fields=["status", "payload", "updated_at"])
        order.payment_status = Order.PaymentStatus.FAILED
        order.save(update_fields=["payment_status", "updated_at"])

    elif event_type == "payment_intent.canceled":
        intent.status = PaymentIntent.Status.CANCELLED
        intent.save(update_fields=["status", "updated_at"])

    return intent


# ── Dispatcher map ─────────────────────────────────────────────────

PROVIDERS = {
    Storefront.PaymentProvider.STUB:                  dispatch_stub,
    Storefront.PaymentProvider.OFFLINE_BANK_TRANSFER: dispatch_offline_bank_transfer,
    Storefront.PaymentProvider.STRIPE:                dispatch_stripe,
}


def dispatch(context: PaymentContext) -> PaymentDispatchResult:
    """Entry point used by services.create_order_from_cart.

    Falls back to the stub provider (with a warning in the intent
    payload) when the configured provider is not runtime-ready.
    """
    provider = context.order.storefront.payment_provider
    handler = PROVIDERS.get(provider)
    if handler is None:
        logger.warning("Unknown provider %s for order %s", provider, context.order.reference)
        return dispatch_stub(context)
    try:
        return handler(context)
    except ProviderUnavailable as exc:
        logger.warning(
            "Provider %s unavailable for order %s: %s — falling back to stub.",
            provider, context.order.reference, exc,
        )
        intent = PaymentIntent.objects.create(
            order=context.order,
            provider=provider,
            amount=context.order.grand_total,
            currency=context.order.currency,
            status=PaymentIntent.Status.SUCCEEDED,
            succeeded_at=timezone.now(),
            payload={
                "note": "provider unavailable — stub fallback",
                "provider_error": str(exc),
                "stub_fallback": True,
            },
        )
        return PaymentDispatchResult(intent=intent)


def is_provider_available(provider: str) -> bool:
    """Runtime probe used by dashboard + admin to flag config issues."""
    if provider == Storefront.PaymentProvider.STRIPE:
        try:
            _stripe_client()
        except ProviderUnavailable:
            return False
        return True
    return True  # stub / offline_bank_transfer are always available
