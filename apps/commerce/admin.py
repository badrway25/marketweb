"""Django admin integration for commerce models.

Inline editing for variants and images where it reduces friction.
"""
from django.contrib import admin

from apps.commerce.models import (
    Address,
    Cart,
    CartItem,
    Collection,
    Order,
    OrderItem,
    PaymentIntent,
    Product,
    ProductImage,
    ProductVariant,
    ShippingMethod,
    Storefront,
)


@admin.register(Storefront)
class StorefrontAdmin(admin.ModelAdmin):
    list_display = ("template", "skin", "currency", "payment_provider", "is_operational")
    list_filter = ("skin", "is_operational", "payment_provider")
    search_fields = ("template__name", "template__slug")


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("title", "storefront", "slug", "order", "is_active")
    list_filter = ("storefront", "is_active")
    search_fields = ("title", "slug")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "storefront", "collection", "base_price", "status", "featured")
    list_filter = ("storefront", "status", "featured", "collection")
    search_fields = ("title", "slug", "sku_root", "material", "creator_name")
    inlines = [ProductImageInline, ProductVariantInline]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("sku", "product", "variant_title", "price", "stock", "is_active")
    list_filter = ("product__storefront", "is_active")
    search_fields = ("sku", "product__title")


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ("title", "storefront", "code", "price", "is_active")
    list_filter = ("storefront", "is_active")


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ("unit_price",)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("pk", "storefront", "session_key", "user", "is_active", "item_count", "subtotal")
    list_filter = ("storefront", "is_active")
    inlines = [CartItemInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = (
        "product", "variant", "product_title", "variant_title", "sku",
        "unit_price", "quantity", "line_total", "image_url",
    )
    can_delete = False


class PaymentIntentInline(admin.TabularInline):
    model = PaymentIntent
    extra = 0
    readonly_fields = ("provider", "provider_reference", "amount", "currency", "status", "succeeded_at")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "reference", "storefront", "customer_name", "grand_total",
        "status", "payment_status", "fulfillment_status", "created_at",
    )
    list_filter = ("storefront", "status", "payment_status", "fulfillment_status")
    search_fields = ("reference", "customer_name", "customer_email")
    readonly_fields = (
        "uuid", "reference", "subtotal", "shipping_total", "grand_total", "currency",
        "confirmed_at", "shipped_at", "delivered_at", "cancelled_at",
    )
    inlines = [OrderItemInline, PaymentIntentInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "city", "postal_code", "country")
    search_fields = ("full_name", "email", "city")
