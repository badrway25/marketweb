"""Forms for customer checkout + seller dashboard operations.

Kept plain Django — crispy-forms is available but the commerce skins
render premium markup manually, so the forms only contribute
validation + field introspection.
"""
from __future__ import annotations

from django import forms

from apps.commerce.models import Order, Product, ProductVariant


class CheckoutForm(forms.Form):
    """Customer-facing checkout form.

    Single-step: shipping address + email + shipping method + optional
    note. No billing address in v1 — shipping doubles as billing.
    """

    full_name = forms.CharField(label="Nome e cognome", max_length=200)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Telefono", max_length=40, required=False)
    line1 = forms.CharField(label="Indirizzo", max_length=240)
    line2 = forms.CharField(
        label="Civico / scala / interno (opz.)", max_length=240, required=False
    )
    city = forms.CharField(label="Città", max_length=140)
    postal_code = forms.CharField(label="CAP", max_length=40)
    region = forms.CharField(label="Provincia / regione", max_length=140, required=False)
    country = forms.CharField(label="Paese", max_length=80, initial="Italia")
    shipping_method = forms.ChoiceField(label="Spedizione", choices=[])
    customer_note = forms.CharField(
        label="Note per il venditore (opz.)",
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False,
    )

    def __init__(self, *args, shipping_methods=None, **kwargs):
        super().__init__(*args, **kwargs)
        if shipping_methods is not None:
            self.fields["shipping_method"].choices = [
                (m.code, f"{m.title} — {m.price:.2f} €") for m in shipping_methods
            ]


# ── Seller dashboard forms ─────────────────────────────────────────

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title", "subtitle", "short_description", "long_description",
            "collection", "base_price", "compare_at_price", "sku_root",
            "badge", "edition_number", "material", "made_in", "creator_name",
            "hero_image_url", "status", "featured", "order",
        ]

    def __init__(self, *args, storefront=None, **kwargs):
        super().__init__(*args, **kwargs)
        if storefront is not None:
            self.fields["collection"].queryset = storefront.collections.filter(is_active=True)


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = [
            "sku", "option1", "option2", "option3",
            "price_override", "stock", "is_active", "image_url", "order",
        ]


class OrderStatusForm(forms.Form):
    fulfillment_status = forms.ChoiceField(
        label="Stato fulfillment",
        choices=Order.FulfillmentStatus.choices,
    )
    tracking_carrier = forms.CharField(
        label="Corriere", max_length=80, required=False
    )
    tracking_number = forms.CharField(
        label="Numero tracking", max_length=140, required=False
    )
