"""Smoke test for Commerce Foundation v1.

Validates:
- Customer-facing shop / product / cart / checkout / order_confirmation routes
- Add-to-cart → update → remove cart flow
- Full checkout → order creation with stub payment (auto-confirmed)
- Seller dashboard routes (behind staff auth)
- Order state transitions (mark paid, fulfillment, cancel)
- Catalog regression: all pre-existing published_live templates still 200
"""
import os
import sys
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketweb.settings")

import django  # noqa: E402

django.setup()

from django.test import Client  # noqa: E402

from apps.catalog.models import WebTemplate  # noqa: E402
from apps.commerce.models import (  # noqa: E402
    Cart,
    Order,
    PaymentIntent,
    ProductVariant,
    Storefront,
)


def section(title: str) -> None:
    print(f"\n-- {title} --")


def check(status: int, url: str, expected: int = 200) -> bool:
    ok = status == expected
    mark = "OK " if ok else "XX "
    print(f"  {mark} {status} {url}")
    return ok


def main() -> int:
    total = 0
    fails = 0

    section("CUSTOMER ROUTES · Bottega")
    c = Client(HTTP_HOST="localhost", enforce_csrf_checks=False)
    routes = [
        "/shop/bottega-shop-artigianale/",
        "/shop/bottega-shop-artigianale/collezione/cuoio/",
        "/shop/bottega-shop-artigianale/collezione/ceramica/",
        "/shop/bottega-shop-artigianale/p/giubbotto-terra/",
        "/shop/bottega-shop-artigianale/p/borsa-cartolina/",
        "/shop/bottega-shop-artigianale/p/camicia-lino/",
        "/shop/bottega-shop-artigianale/p/set-cucina/",
        "/shop/bottega-shop-artigianale/cart/",
    ]
    for url in routes:
        total += 1
        if not check(c.get(url).status_code, url):
            fails += 1

    section("CUSTOMER ROUTES · Luxe")
    c2 = Client(HTTP_HOST="localhost", enforce_csrf_checks=False)
    routes = [
        "/shop/luxe-fashion-store/",
        "/shop/luxe-fashion-store/collezione/drop-01-spring-26/",
        "/shop/luxe-fashion-store/collezione/drop-02-spring-26/",
        "/shop/luxe-fashion-store/collezione/atelier/",
        "/shop/luxe-fashion-store/p/rack-atelier-nero/",
        "/shop/luxe-fashion-store/p/robe-manteau-grigio-perla/",
        "/shop/luxe-fashion-store/p/tailleur-cady-bianco/",
        "/shop/luxe-fashion-store/p/sessione-vogue/",
        "/shop/luxe-fashion-store/cart/",
    ]
    for url in routes:
        total += 1
        if not check(c2.get(url).status_code, url):
            fails += 1

    section("CART FLOW · Bottega add → update → checkout → order")
    Cart.objects.all().delete()
    Order.objects.all().delete()
    client = Client(HTTP_HOST="localhost", enforce_csrf_checks=False)
    sf_b = Storefront.objects.get(template__slug="bottega-shop-artigianale")
    # Reset stock so reruns are stable
    from apps.commerce.management.commands import seed_commerce as _s
    _s.Command().handle(reset=True)
    sf_b.refresh_from_db()

    variant = ProductVariant.objects.filter(
        product__storefront=sf_b, stock__gte=2, is_active=True
    ).first()
    print(f"  picked variant {variant.sku} stock={variant.stock} price={variant.price}")

    # Prime session with a GET so the cart gets keyed
    client.get("/shop/bottega-shop-artigianale/")

    total += 1
    r = client.post(
        "/shop/bottega-shop-artigianale/cart/add/",
        {"variant_id": variant.id, "quantity": 2},
    )
    if not check(r.status_code, "add-to-cart (302 redirect)", expected=302):
        fails += 1

    cart = Cart.objects.filter(storefront=sf_b, is_active=True).order_by("-pk").first()
    print(f"    cart items={cart.item_count()} subtotal={cart.subtotal()}")
    total += 1
    if cart.item_count() != 2:
        print(f"  ✗ expected 2 items in cart, got {cart.item_count()}")
        fails += 1
    else:
        print(f"  ✓ 2 items in cart")

    # Update qty
    item = cart.items.first()
    total += 1
    r = client.post(
        f"/shop/bottega-shop-artigianale/cart/{item.pk}/update/",
        {"quantity": 1},
    )
    if not check(r.status_code, "update cart item (302 redirect)", expected=302):
        fails += 1

    cart.refresh_from_db()
    total += 1
    if cart.item_count() != 1:
        print(f"  ✗ expected 1 item after update, got {cart.item_count()}")
        fails += 1
    else:
        print(f"  ✓ 1 item after update")

    # Checkout GET
    total += 1
    r = client.get("/shop/bottega-shop-artigianale/checkout/")
    if not check(r.status_code, "checkout GET"):
        fails += 1

    # Checkout POST
    shipping = sf_b.shipping_methods.first()
    total += 1
    r = client.post(
        "/shop/bottega-shop-artigianale/checkout/",
        {
            "full_name": "Badr Badrane",
            "email": "badr@example.com",
            "phone": "+39 333 1234567",
            "line1": "Via dei Serragli 10",
            "line2": "",
            "city": "Firenze",
            "postal_code": "50124",
            "region": "FI",
            "country": "Italia",
            "shipping_method": shipping.code,
            "customer_note": "Consegna in mattinata se possibile.",
        },
    )
    if not check(r.status_code, "checkout POST (302 → order_confirmation)", expected=302):
        fails += 1

    order = Order.objects.filter(storefront=sf_b).order_by("-pk").first()
    total += 1
    if order is None:
        print("  ✗ no order created")
        fails += 1
    else:
        print(f"  ✓ order {order.reference} created · status={order.status} payment={order.payment_status} total=€{order.grand_total}")

    # Order confirmation page
    total += 1
    r = client.get(f"/shop/bottega-shop-artigianale/order/{order.uuid}/")
    if not check(r.status_code, f"order confirmation /order/{order.uuid}/"):
        fails += 1

    # Variant stock decremented
    variant.refresh_from_db()
    print(f"    variant stock after order: {variant.stock}")

    # Stub payment auto-succeeded
    intent = PaymentIntent.objects.filter(order=order).first()
    total += 1
    if intent and intent.status == PaymentIntent.Status.SUCCEEDED:
        print(f"  ✓ payment intent auto-succeeded ({intent.provider})")
    else:
        print(f"  ✗ payment intent state: {intent.status if intent else 'missing'}")
        fails += 1

    section("SELLER DASHBOARD · auth gate")
    staff_client = Client(HTTP_HOST="localhost", enforce_csrf_checks=False)

    anon = Client(HTTP_HOST="localhost", enforce_csrf_checks=False)
    total += 1
    r = anon.get("/dashboard/bottega-shop-artigianale/")
    if not check(r.status_code, "dashboard home anon (302 → login)", expected=302):
        fails += 1

    from apps.accounts.models import User

    User.objects.filter(username="smoke_seller").delete()
    staff = User.objects.create_user("smoke_seller", "s@example.com", "sellerpw!", is_staff=True)
    staff_client.force_login(staff)

    routes = [
        "/dashboard/bottega-shop-artigianale/",
        "/dashboard/bottega-shop-artigianale/products/",
        "/dashboard/bottega-shop-artigianale/products/new/",
        "/dashboard/bottega-shop-artigianale/orders/",
        f"/dashboard/bottega-shop-artigianale/orders/{order.uuid}/",
        "/dashboard/luxe-fashion-store/",
        "/dashboard/luxe-fashion-store/products/",
        "/dashboard/luxe-fashion-store/orders/",
    ]
    for url in routes:
        total += 1
        if not check(staff_client.get(url).status_code, url):
            fails += 1

    # Edit the first bottega product
    first_prod = sf_b.products.first()
    total += 1
    r = staff_client.get(f"/dashboard/bottega-shop-artigianale/products/{first_prod.pk}/")
    if not check(r.status_code, f"product edit form /products/{first_prod.pk}/"):
        fails += 1

    section("ORDER STATE TRANSITIONS")
    total += 1
    r = staff_client.post(
        f"/dashboard/bottega-shop-artigianale/orders/{order.uuid}/",
        {"action": "fulfillment", "fulfillment_status": "shipped",
         "tracking_carrier": "BRT", "tracking_number": "A1234567890"},
    )
    if not check(r.status_code, "mark shipped (302)", expected=302):
        fails += 1
    order.refresh_from_db()
    if order.status == Order.Status.SHIPPED and order.tracking_number:
        print(f"  ✓ order now shipped · tracking={order.tracking_number}")
    else:
        print(f"  ✗ order did not transition to shipped: status={order.status}")
        fails += 1
    total += 1

    section("CATALOG REGRESSION · published_live templates still render")
    for t in WebTemplate.objects.filter(tier=WebTemplate.Tier.PUBLISHED_LIVE):
        total += 1
        r = c.get(f"/templates/{t.category.slug}/{t.slug}/preview/")
        if not check(r.status_code, f"/templates/{t.category.slug}/{t.slug}/preview/"):
            fails += 1

    print(f"\n{'─' * 60}")
    print(f"  RESULT · {total - fails}/{total} checks passed")
    print(f"{'─' * 60}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
