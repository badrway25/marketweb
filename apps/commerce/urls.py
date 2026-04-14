"""Commerce URL routes.

Two namespaces mounted under the project root:
- /shop/<storefront>/...   customer
- /dashboard/<storefront>/...   seller
"""
from django.urls import path

from apps.commerce.views import (
    AddToCartView,
    CartView,
    CheckoutView,
    DashboardHomeView,
    OrderConfirmationView,
    OrderDetailView,
    OrdersListView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductUpdateView,
    ProductsListView,
    RemoveCartItemView,
    ShopView,
    UpdateCartItemView,
    VariantCreateView,
    VariantDeleteView,
    VariantUpdateView,
)

app_name = "commerce"

urlpatterns = [
    # ── Customer storefront ──────────────────────────────────────────
    path(
        "shop/<slug:storefront_slug>/",
        ShopView.as_view(),
        name="shop",
    ),
    path(
        "shop/<slug:storefront_slug>/collezione/<slug:collection_slug>/",
        ShopView.as_view(),
        name="shop_collection",
    ),
    path(
        "shop/<slug:storefront_slug>/p/<slug:product_slug>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "shop/<slug:storefront_slug>/cart/",
        CartView.as_view(),
        name="cart",
    ),
    path(
        "shop/<slug:storefront_slug>/cart/add/",
        AddToCartView.as_view(),
        name="cart_add",
    ),
    path(
        "shop/<slug:storefront_slug>/cart/<int:item_id>/update/",
        UpdateCartItemView.as_view(),
        name="cart_update",
    ),
    path(
        "shop/<slug:storefront_slug>/cart/<int:item_id>/remove/",
        RemoveCartItemView.as_view(),
        name="cart_remove",
    ),
    path(
        "shop/<slug:storefront_slug>/checkout/",
        CheckoutView.as_view(),
        name="checkout",
    ),
    path(
        "shop/<slug:storefront_slug>/order/<uuid:order_uuid>/",
        OrderConfirmationView.as_view(),
        name="order_confirmation",
    ),

    # ── Seller dashboard ─────────────────────────────────────────────
    path(
        "dashboard/<slug:storefront_slug>/",
        DashboardHomeView.as_view(),
        name="dashboard_home",
    ),
    path(
        "dashboard/<slug:storefront_slug>/products/",
        ProductsListView.as_view(),
        name="dashboard_products",
    ),
    path(
        "dashboard/<slug:storefront_slug>/products/new/",
        ProductCreateView.as_view(),
        name="dashboard_product_new",
    ),
    path(
        "dashboard/<slug:storefront_slug>/products/<int:product_pk>/",
        ProductUpdateView.as_view(),
        name="dashboard_product_edit",
    ),
    path(
        "dashboard/<slug:storefront_slug>/products/<int:product_pk>/delete/",
        ProductDeleteView.as_view(),
        name="dashboard_product_delete",
    ),
    path(
        "dashboard/<slug:storefront_slug>/products/<int:product_pk>/variants/new/",
        VariantCreateView.as_view(),
        name="dashboard_variant_new",
    ),
    path(
        "dashboard/<slug:storefront_slug>/products/<int:product_pk>/variants/<int:variant_pk>/",
        VariantUpdateView.as_view(),
        name="dashboard_variant_edit",
    ),
    path(
        "dashboard/<slug:storefront_slug>/products/<int:product_pk>/variants/<int:variant_pk>/delete/",
        VariantDeleteView.as_view(),
        name="dashboard_variant_delete",
    ),
    path(
        "dashboard/<slug:storefront_slug>/orders/",
        OrdersListView.as_view(),
        name="dashboard_orders",
    ),
    path(
        "dashboard/<slug:storefront_slug>/orders/<uuid:order_uuid>/",
        OrderDetailView.as_view(),
        name="dashboard_order_detail",
    ),
]
