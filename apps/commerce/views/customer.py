"""Customer-facing commerce views — shop, product, cart, checkout, order."""
from __future__ import annotations

from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from apps.commerce import selectors, services
from apps.commerce.forms import CheckoutForm
from apps.commerce.models import Cart, ProductVariant, Storefront


# ── Shared helpers ─────────────────────────────────────────────────

def _ensure_session(request):
    if not request.session.session_key:
        request.session.save()
    return request.session.session_key


def _resolve_storefront(slug: str) -> Storefront:
    sf = selectors.get_operational_storefront(slug)
    if sf is None:
        raise Http404("Storefront non disponibile.")
    return sf


def _skin_template(storefront: Storefront, name: str) -> str:
    return f"commerce/skins/{storefront.skin_path}/{name}.html"


def _cart_context(request, storefront: Storefront):
    session_key = _ensure_session(request)
    cart = services.get_or_create_cart(
        storefront=storefront,
        session_key=session_key,
        user=request.user,
    )
    return cart


# ── Shop (collection listing) ──────────────────────────────────────

class ShopView(ListView):
    context_object_name = "products"
    paginate_by = 24

    def get_template_names(self):
        return [_skin_template(self.storefront, "shop")]

    def dispatch(self, request, *args, **kwargs):
        self.storefront = _resolve_storefront(kwargs["storefront_slug"])
        self.collection_slug = kwargs.get("collection_slug")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.search = self.request.GET.get("q", "").strip()
        self.sort = self.request.GET.get("sort", "recent")
        return selectors.list_active_products(
            self.storefront,
            collection_slug=self.collection_slug,
            search=self.search or None,
            sort=self.sort,
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["collections"] = selectors.list_collections(self.storefront)
        ctx["current_collection"] = (
            selectors.get_collection(self.storefront, self.collection_slug)
            if self.collection_slug else None
        )
        ctx["search"] = self.search
        ctx["sort"] = self.sort
        ctx["cart"] = _cart_context(self.request, self.storefront)
        return ctx


# ── Product detail ─────────────────────────────────────────────────

class ProductDetailView(DetailView):
    context_object_name = "product"

    def get_template_names(self):
        return [_skin_template(self.storefront, "product")]

    def dispatch(self, request, *args, **kwargs):
        self.storefront = _resolve_storefront(kwargs["storefront_slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        product = selectors.get_product_detail(self.storefront, self.kwargs["product_slug"])
        if product is None:
            raise Http404("Prodotto non trovato.")
        return product

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["variants"] = list(self.object.variants.all())
        ctx["images"] = list(self.object.images.all())
        ctx["related"] = selectors.list_related_products(self.object)
        ctx["cart"] = _cart_context(self.request, self.storefront)
        return ctx


# ── Cart ───────────────────────────────────────────────────────────

class CartView(TemplateView):
    def get_template_names(self):
        return [_skin_template(self.storefront, "cart")]

    def dispatch(self, request, *args, **kwargs):
        self.storefront = _resolve_storefront(kwargs["storefront_slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["cart"] = _cart_context(self.request, self.storefront)
        ctx["shipping_methods"] = selectors.list_shipping_methods(self.storefront)
        return ctx


class AddToCartView(View):
    def post(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        variant_id = request.POST.get("variant_id")
        quantity = int(request.POST.get("quantity", "1") or 1)
        variant = get_object_or_404(
            ProductVariant,
            pk=variant_id,
            product__storefront=storefront,
            is_active=True,
        )
        try:
            services.add_to_cart(cart=cart, variant=variant, quantity=quantity)
            messages.success(request, f"{variant.product.title} aggiunto al carrello.")
        except services.CommerceError as exc:
            messages.error(request, str(exc))
        return redirect(reverse("commerce:cart", args=[storefront_slug]))


class UpdateCartItemView(View):
    def post(self, request, storefront_slug, item_id):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        quantity = int(request.POST.get("quantity", "1") or 1)
        try:
            services.update_cart_item(cart=cart, item_id=item_id, quantity=quantity)
        except services.CommerceError as exc:
            messages.error(request, str(exc))
        return redirect(reverse("commerce:cart", args=[storefront_slug]))


class RemoveCartItemView(View):
    def post(self, request, storefront_slug, item_id):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        services.remove_cart_item(cart=cart, item_id=item_id)
        return redirect(reverse("commerce:cart", args=[storefront_slug]))


# ── Checkout ───────────────────────────────────────────────────────

class CheckoutView(View):
    def _context(self, request, storefront, form, cart):
        return {
            "storefront": storefront,
            "cart": cart,
            "form": form,
            "shipping_methods": selectors.list_shipping_methods(storefront),
        }

    def get(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        if cart.items.count() == 0:
            messages.info(request, "Il carrello è vuoto.")
            return redirect(reverse("commerce:shop", args=[storefront_slug]))
        shipping = list(selectors.list_shipping_methods(storefront))
        form = CheckoutForm(shipping_methods=shipping)
        return render(
            request,
            _skin_template(storefront, "checkout"),
            self._context(request, storefront, form, cart),
        )

    def post(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        shipping = list(selectors.list_shipping_methods(storefront))
        form = CheckoutForm(request.POST, shipping_methods=shipping)
        if not form.is_valid():
            return render(
                request,
                _skin_template(storefront, "checkout"),
                self._context(request, storefront, form, cart),
            )
        payload = services.CheckoutPayload(
            full_name=form.cleaned_data["full_name"],
            email=form.cleaned_data["email"],
            phone=form.cleaned_data.get("phone") or "",
            line1=form.cleaned_data["line1"],
            line2=form.cleaned_data.get("line2") or "",
            city=form.cleaned_data["city"],
            postal_code=form.cleaned_data["postal_code"],
            region=form.cleaned_data.get("region") or "",
            country=form.cleaned_data.get("country") or "Italia",
            shipping_method_code=form.cleaned_data["shipping_method"],
            customer_note=form.cleaned_data.get("customer_note") or "",
        )
        try:
            order = services.create_order_from_cart(
                cart=cart, payload=payload, user=request.user,
            )
        except services.CommerceError as exc:
            messages.error(request, str(exc))
            return render(
                request,
                _skin_template(storefront, "checkout"),
                self._context(request, storefront, form, cart),
            )
        return HttpResponseRedirect(
            reverse("commerce:order_confirmation", args=[storefront_slug, order.uuid])
        )


class OrderConfirmationView(TemplateView):
    def get_template_names(self):
        return [_skin_template(self.storefront, "order_confirmation")]

    def dispatch(self, request, *args, **kwargs):
        self.storefront = _resolve_storefront(kwargs["storefront_slug"])
        self.order = selectors.get_order_by_uuid(self.storefront, kwargs["order_uuid"])
        if self.order is None:
            raise Http404("Ordine non trovato.")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["order"] = self.order
        ctx["items"] = list(self.order.items.all())
        ctx["latest_intent"] = self.order.payment_intents.order_by("-created_at").first()
        return ctx
