"""Customer-facing commerce views — shop, product, cart, checkout,
order, policies, order lookup, payment (Stripe).

All pages pull `?lang=xx` from the querystring and render in the
selected locale (IT default, EN/FR/ES/AR supported). The chrome
dict + product/collection/storefront translations are resolved
upstream (LocaleMixin) and handed to the template under `chrome`,
`locale`, `html_dir`, `locale_switcher`, `product_l10n`, etc.
"""
from __future__ import annotations

import json

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, TemplateView

from apps.commerce import content, i18n as commerce_i18n, payments, selectors, services
from apps.commerce.forms import CheckoutForm, OrderLookupForm
from apps.commerce.models import Cart, Order, PaymentIntent, ProductVariant, Storefront


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


def _localize_shipping_methods(methods, locale):
    return [
        {
            "code":     m.code,
            "price":    m.price,
            "is_active": m.is_active,
            **m.localized(locale),
        }
        for m in methods
    ]


def _translate_error(exc: services.CommerceError, chrome: dict) -> str:
    """Map a service-layer CommerceError to its localized chrome message.

    The error carries `code` + `params`. We look up `msg_<code>` in chrome
    (falls back to IT via get_chrome's backfill) and format with params.
    If the key is missing we fall back to the exception's IT string so
    nothing renders raw Python repr text.
    """
    template = chrome.get(f"msg_{exc.code}") if exc.code else None
    if not template:
        return str(exc)
    try:
        return template.format(**(exc.params or {}))
    except Exception:
        return str(exc)


def _localize_collections(storefront, locale):
    out = []
    for c in storefront.collections.all():
        if not c.is_active:
            continue
        block = (c.translations or {}).get(locale) or (c.translations or {}).get("it") or {}
        out.append({
            "slug":     c.slug,
            "title":    block.get("title") or c.title,
            "subtitle": block.get("subtitle") or c.subtitle,
        })
    return out


# ── Locale mixin ───────────────────────────────────────────────────

class LocaleMixin:
    """Resolves `?lang=` once and injects locale + chrome into context.

    Subclasses that need the storefront must set `self.storefront`
    in dispatch before calling super().get_context_data; every
    customer-facing view already does this.
    """

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.locale = commerce_i18n.resolve_locale(request)

    def get_locale_context(self, storefront: Storefront | None = None) -> dict:
        chrome = commerce_i18n.get_chrome(self.locale)
        switcher = commerce_i18n.locale_switcher_entries(self.locale)
        ctx = {
            "locale":          self.locale,
            "html_dir":        commerce_i18n.html_dir(self.locale),
            "is_rtl":          commerce_i18n.is_rtl(self.locale),
            "chrome":          chrome,
            "locale_switcher": switcher,
            "lang_qs":         commerce_i18n.preserve_lang_qs(self.locale),
        }
        if storefront is not None:
            block = content.get_storefront_content(storefront.slug, self.locale)
            ctx["storefront_content"] = block
            ctx["storefront_tagline"] = block.get("tagline", "")
            ctx["storefront_footer_bio"] = block.get("footer_bio", "")
            ctx["storefront_shipping_policy"] = block.get("shipping_policy", storefront.shipping_policy)
            ctx["storefront_return_policy"] = block.get("return_policy", storefront.return_policy)
            ctx["storefront_bank_instructions"] = block.get(
                "bank_transfer_instructions", storefront.bank_transfer_instructions
            )
            ctx["collections_i18n"] = _localize_collections(storefront, self.locale)
        return ctx


# ── Shop (collection listing) ──────────────────────────────────────

class ShopView(LocaleMixin, ListView):
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
        locale_ctx = self.get_locale_context(self.storefront)
        ctx.update(locale_ctx)
        ctx["storefront"] = self.storefront
        ctx["collections"] = selectors.list_collections(self.storefront)
        ctx["current_collection"] = (
            selectors.get_collection(self.storefront, self.collection_slug)
            if self.collection_slug else None
        )
        # Decorate products with localized payload for ergonomic templates.
        ctx["products_l10n"] = [
            {"obj": p, **p.localized(self.locale)}
            for p in ctx[self.context_object_name]
        ]
        ctx["search"] = self.search
        ctx["sort"] = self.sort
        ctx["cart"] = _cart_context(self.request, self.storefront)
        return ctx


# ── Product detail ─────────────────────────────────────────────────

class ProductDetailView(LocaleMixin, DetailView):
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
        ctx.update(self.get_locale_context(self.storefront))
        ctx["storefront"] = self.storefront
        variants = list(self.object.variants.all())
        ctx["variants"] = variants
        # Pick a sane default variant: first in-stock one. If every variant is
        # out of stock, leave default_variant_id=None so the submit button is
        # disabled and the form cannot 404 with variant_id="".
        default_vid = next((v.id for v in variants if v.is_active and v.stock > 0), None)
        ctx["default_variant_id"] = default_vid
        ctx["can_add_to_cart"] = default_vid is not None
        ctx["images"] = list(self.object.images.all())
        related = selectors.list_related_products(self.object)
        ctx["related"] = related
        ctx["related_l10n"] = [{"obj": p, **p.localized(self.locale)} for p in related]
        ctx["product_l10n"] = self.object.localized(self.locale)
        ctx["cart"] = _cart_context(self.request, self.storefront)
        return ctx


# ── Cart ───────────────────────────────────────────────────────────

class CartView(LocaleMixin, TemplateView):
    def get_template_names(self):
        return [_skin_template(self.storefront, "cart")]

    def dispatch(self, request, *args, **kwargs):
        self.storefront = _resolve_storefront(kwargs["storefront_slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(self.get_locale_context(self.storefront))
        ctx["storefront"] = self.storefront
        cart = _cart_context(self.request, self.storefront)
        ctx["cart"] = cart
        methods = list(selectors.list_shipping_methods(self.storefront))
        ctx["shipping_methods"] = methods
        ctx["shipping_methods_l10n"] = _localize_shipping_methods(methods, self.locale)
        # Pre-localize line items for templates that want to avoid per-loop lookups.
        ctx["cart_lines"] = [
            {
                "item":    item,
                "product": item.variant.product,
                "l10n":    item.variant.product.localized(self.locale),
            }
            for item in cart.items.select_related("variant", "variant__product").all()
        ]
        return ctx


class AddToCartView(View):
    def post(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        variant_id = request.POST.get("variant_id") or ""
        quantity = int(request.POST.get("quantity", "1") or 1)
        chrome = commerce_i18n.get_chrome(commerce_i18n.resolve_locale(request))
        lang_qs = commerce_i18n.preserve_lang_qs(commerce_i18n.resolve_locale(request))
        # Guard: no variant selected (first was out-of-stock, or picker broke
        # client-side). Don't 404 — return to the product with a clear message.
        if not variant_id.strip().isdigit():
            messages.error(request, chrome.get("msg_pick_variant", "Scegli una variante."))
            referer = request.POST.get("referer") or request.META.get("HTTP_REFERER") or \
                reverse("commerce:shop", args=[storefront_slug])
            return redirect(referer)
        variant = ProductVariant.objects.filter(
            pk=variant_id, product__storefront=storefront, is_active=True,
        ).first()
        if variant is None:
            messages.error(request, chrome.get("msg_variant_unavailable",
                                               "Variante non disponibile."))
            return redirect(reverse("commerce:shop", args=[storefront_slug]) + lang_qs)
        try:
            services.add_to_cart(cart=cart, variant=variant, quantity=quantity)
            locale = commerce_i18n.resolve_locale(request)
            title = variant.product.localized(locale).get("title") or variant.product.title
            tmpl = chrome.get("msg_added_to_cart", "{title} aggiunto al carrello.")
            messages.success(request, tmpl.format(title=title))
        except services.CommerceError as exc:
            messages.error(request, _translate_error(exc, chrome))
        return redirect(reverse("commerce:cart", args=[storefront_slug]) + lang_qs)


class UpdateCartItemView(View):
    def post(self, request, storefront_slug, item_id):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        quantity = int(request.POST.get("quantity", "1") or 1)
        locale = commerce_i18n.resolve_locale(request)
        chrome = commerce_i18n.get_chrome(locale)
        try:
            services.update_cart_item(cart=cart, item_id=item_id, quantity=quantity)
        except services.CommerceError as exc:
            messages.error(request, _translate_error(exc, chrome))
        qs = commerce_i18n.preserve_lang_qs(locale)
        return redirect(reverse("commerce:cart", args=[storefront_slug]) + qs)


class RemoveCartItemView(View):
    def post(self, request, storefront_slug, item_id):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        services.remove_cart_item(cart=cart, item_id=item_id)
        qs = commerce_i18n.preserve_lang_qs(commerce_i18n.resolve_locale(request))
        return redirect(reverse("commerce:cart", args=[storefront_slug]) + qs)


# ── Checkout ───────────────────────────────────────────────────────

class CheckoutView(LocaleMixin, View):
    def _context(self, request, storefront, form, cart):
        methods = list(selectors.list_shipping_methods(storefront))
        ctx = {
            "storefront": storefront,
            "cart": cart,
            "form": form,
            "shipping_methods": methods,
            "shipping_methods_l10n": _localize_shipping_methods(methods, self.locale),
        }
        ctx.update(self.get_locale_context(storefront))
        return ctx

    def get(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        if cart.items.count() == 0:
            messages.info(request, commerce_i18n.get_chrome(self.locale)["msg_empty_cart"])
            return redirect(
                reverse("commerce:shop", args=[storefront_slug])
                + commerce_i18n.preserve_lang_qs(self.locale)
            )
        shipping = list(selectors.list_shipping_methods(storefront))
        form = CheckoutForm(
            shipping_methods=shipping,
            chrome=commerce_i18n.get_chrome(self.locale),
            locale=self.locale,
        )
        return render(
            request,
            _skin_template(storefront, "checkout"),
            self._context(request, storefront, form, cart),
        )

    def post(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        cart = _cart_context(request, storefront)
        shipping = list(selectors.list_shipping_methods(storefront))
        form = CheckoutForm(
            request.POST,
            shipping_methods=shipping,
            chrome=commerce_i18n.get_chrome(self.locale),
            locale=self.locale,
        )
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
            messages.error(request, _translate_error(exc, commerce_i18n.get_chrome(self.locale)))
            return render(
                request,
                _skin_template(storefront, "checkout"),
                self._context(request, storefront, form, cart),
            )
        # Route depending on payment provider state
        latest = order.payment_intents.order_by("-created_at").first()
        lang_qs = commerce_i18n.preserve_lang_qs(self.locale)
        if latest and latest.provider == Storefront.PaymentProvider.STRIPE \
                and latest.status == PaymentIntent.Status.INITIATED:
            return HttpResponseRedirect(
                reverse("commerce:payment_page", args=[storefront_slug, order.uuid]) + lang_qs
            )
        return HttpResponseRedirect(
            reverse("commerce:order_confirmation", args=[storefront_slug, order.uuid]) + lang_qs
        )


class OrderConfirmationView(LocaleMixin, TemplateView):
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
        ctx.update(self.get_locale_context(self.storefront))
        ctx["storefront"] = self.storefront
        ctx["order"] = self.order
        # Localized snapshot line items — fall back to order snapshot titles
        # because translations on the actual Product row may have changed
        # after purchase.
        ctx["items"] = list(self.order.items.all())
        ctx["latest_intent"] = self.order.payment_intents.order_by("-created_at").first()
        ctx["shipping_method_l10n"] = (
            self.order.shipping_method.localized(self.locale)
            if self.order.shipping_method_id else {}
        )
        return ctx


# ── Stripe payment page ────────────────────────────────────────────

class PaymentPageView(LocaleMixin, TemplateView):
    """Render the Stripe Elements page for an INITIATED intent.

    Customers land here after a checkout whose storefront uses
    stripe, complete the card, and are redirected to
    /order/<uuid>/ — the PaymentIntent is confirmed server-side
    via the Stripe webhook (or the return_url query params for dev).
    """

    template_name = "commerce/payment/stripe.html"

    def dispatch(self, request, *args, **kwargs):
        self.storefront = _resolve_storefront(kwargs["storefront_slug"])
        self.order = selectors.get_order_by_uuid(self.storefront, kwargs["order_uuid"])
        if self.order is None:
            raise Http404("Ordine non trovato.")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(self.get_locale_context(self.storefront))
        ctx["storefront"] = self.storefront
        ctx["order"] = self.order
        intent = (
            self.order.payment_intents
            .filter(provider=Storefront.PaymentProvider.STRIPE)
            .order_by("-created_at")
            .first()
        )
        ctx["intent"] = intent
        client_secret = (intent.payload or {}).get("client_secret") if intent else ""
        publishable_key = getattr(settings, "STRIPE_PUBLISHABLE_KEY", "")
        ctx["stripe_config_json"] = json.dumps({
            "publishableKey": publishable_key,
            "clientSecret":   client_secret,
            "returnUrl":      self.request.build_absolute_uri(
                reverse("commerce:order_confirmation",
                        args=[self.storefront.slug, self.order.uuid])
                + commerce_i18n.preserve_lang_qs(self.locale)
            ),
            "isConfigured":   bool(publishable_key and client_secret),
        })
        ctx["stripe_configured"] = bool(publishable_key and client_secret)
        return ctx


class RetryPaymentView(LocaleMixin, View):
    """Customer-side retry for a failed payment.

    Re-dispatches via payments.dispatch(). If the provider is
    Stripe we redirect to the payment page; otherwise we go back
    to the order confirmation.
    """

    def post(self, request, storefront_slug, order_uuid):
        storefront = _resolve_storefront(storefront_slug)
        order = selectors.get_order_by_uuid(storefront, order_uuid)
        if order is None:
            raise Http404()
        try:
            intent = services.retry_payment(order=order)
        except services.CommerceError as exc:
            messages.error(request, _translate_error(exc, commerce_i18n.get_chrome(self.locale)))
            return redirect(
                reverse("commerce:order_confirmation", args=[storefront_slug, order_uuid])
                + commerce_i18n.preserve_lang_qs(self.locale)
            )
        lang_qs = commerce_i18n.preserve_lang_qs(self.locale)
        if intent.provider == Storefront.PaymentProvider.STRIPE \
                and intent.status == PaymentIntent.Status.INITIATED:
            return redirect(
                reverse("commerce:payment_page", args=[storefront_slug, order_uuid]) + lang_qs
            )
        return redirect(
            reverse("commerce:order_confirmation", args=[storefront_slug, order_uuid]) + lang_qs
        )


# ── Stripe webhook ─────────────────────────────────────────────────

@method_decorator(csrf_exempt, name="dispatch")
class StripeWebhookView(View):
    """Stripe signed-event receiver.

    Mounted off the commerce namespace; takes no slug — a single
    Stripe account serves every storefront on this deployment.
    """

    def post(self, request):
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
        webhook_secret = getattr(settings, "STRIPE_WEBHOOK_SECRET", "")

        if not webhook_secret:
            return HttpResponseBadRequest("Webhook not configured.")

        try:
            import stripe
            stripe.api_key = getattr(settings, "STRIPE_SECRET_KEY", "")
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except ImportError:
            return HttpResponseBadRequest("Stripe package not installed.")
        except Exception as exc:  # noqa: BLE001 — stripe raises SignatureVerificationError
            return HttpResponseBadRequest(f"Invalid signature: {exc}")

        payments.handle_stripe_webhook_event(event)
        return HttpResponse(status=200)


# ── Policies + order lookup ────────────────────────────────────────

class PoliciesView(LocaleMixin, TemplateView):
    """Shipping + returns + contact policy page, per storefront + locale."""

    def get_template_names(self):
        return [_skin_template(self.storefront, "policies")]

    def dispatch(self, request, *args, **kwargs):
        self.storefront = _resolve_storefront(kwargs["storefront_slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(self.get_locale_context(self.storefront))
        ctx["storefront"] = self.storefront
        ctx["cart"] = _cart_context(self.request, self.storefront)
        return ctx


class OrderLookupView(LocaleMixin, View):
    """Self-service order lookup: customer enters reference + email."""

    template_name_override = "order_lookup"

    def _render(self, request, storefront, form):
        ctx = {
            "storefront": storefront,
            "form": form,
            "cart": _cart_context(request, storefront),
        }
        ctx.update(self.get_locale_context(storefront))
        return render(
            request,
            _skin_template(storefront, "order_lookup"),
            ctx,
        )

    def get(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        form = OrderLookupForm(chrome=commerce_i18n.get_chrome(self.locale))
        return self._render(request, storefront, form)

    def post(self, request, storefront_slug):
        storefront = _resolve_storefront(storefront_slug)
        chrome = commerce_i18n.get_chrome(self.locale)
        form = OrderLookupForm(request.POST, chrome=chrome)
        if not form.is_valid():
            return self._render(request, storefront, form)

        ref = form.cleaned_data["reference"].strip().upper()
        email = form.cleaned_data["email"].strip().lower()
        order = (
            Order.objects
            .filter(storefront=storefront, reference=ref, customer_email__iexact=email)
            .first()
        )
        if order is None:
            messages.error(request, chrome["lookup_not_found"])
            return self._render(request, storefront, form)
        return redirect(
            reverse("commerce:order_confirmation", args=[storefront_slug, order.uuid])
            + commerce_i18n.preserve_lang_qs(self.locale)
        )
