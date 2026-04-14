"""Forms for customer checkout + seller dashboard operations.

Labels on the customer-facing forms (CheckoutForm, OrderLookupForm)
are chrome-driven so they render in the active locale. Seller-side
forms stay IT-only (dashboard is not localized in v2).
"""
from __future__ import annotations

from django import forms

from apps.commerce.models import Order, Product, ProductVariant, StorefrontMember


class CheckoutForm(forms.Form):
    """Customer-facing checkout form — labels pulled from chrome."""

    full_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=40, required=False)
    line1 = forms.CharField(max_length=240)
    line2 = forms.CharField(max_length=240, required=False)
    city = forms.CharField(max_length=140)
    postal_code = forms.CharField(max_length=40)
    region = forms.CharField(max_length=140, required=False)
    country = forms.CharField(max_length=80, initial="Italia")
    shipping_method = forms.ChoiceField(choices=[])
    customer_note = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False,
    )

    def __init__(self, *args, shipping_methods=None, chrome=None, locale="it", **kwargs):
        super().__init__(*args, **kwargs)
        c = chrome or {}
        # Apply locale labels.
        self.fields["full_name"].label     = c.get("f_full_name",    "Nome e cognome")
        self.fields["email"].label         = c.get("f_email",        "Email")
        self.fields["phone"].label         = c.get("f_phone",        "Telefono")
        self.fields["line1"].label         = c.get("f_line1",        "Indirizzo")
        self.fields["line2"].label         = c.get("f_line2",        "Civico / scala")
        self.fields["city"].label          = c.get("f_city",         "Città")
        self.fields["postal_code"].label   = c.get("f_postal_code",  "CAP")
        self.fields["region"].label        = c.get("f_region",       "Provincia")
        self.fields["country"].label       = c.get("f_country",      "Paese")
        self.fields["shipping_method"].label = c.get("f_shipping_method", "Metodo")
        self.fields["customer_note"].label = c.get("f_customer_note", "Note")
        # Populate shipping choices using the localized title of each method.
        if shipping_methods is not None:
            choices = []
            for m in shipping_methods:
                label_block = m.localized(locale)
                title = label_block.get("title") or m.title
                price = f"{m.price:.2f} €"
                choices.append((m.code, f"{title} — {price}"))
            self.fields["shipping_method"].choices = choices


class OrderLookupForm(forms.Form):
    """Customer self-service order lookup — reference + email."""

    reference = forms.CharField(max_length=20)
    email = forms.EmailField()

    def __init__(self, *args, chrome=None, **kwargs):
        super().__init__(*args, **kwargs)
        c = chrome or {}
        self.fields["reference"].label = c.get("f_order_reference", "Numero ordine")
        self.fields["email"].label = c.get("f_email", "Email")


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


class StorefrontMemberForm(forms.ModelForm):
    """Add/edit a member of a storefront (admin UI)."""

    class Meta:
        model = StorefrontMember
        fields = ["user", "role"]
