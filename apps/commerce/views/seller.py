"""Seller dashboard views — products, variants, orders.

Merchant-scoped: every dashboard view checks that the authenticated
user has a `StorefrontMember` row for the requested storefront
(or is a superuser). A staff user without membership cannot see
another seller's data — the previous v1 behaviour (any is_staff
sees everything) is gone.
"""
from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView, UpdateView
from django.views.generic.edit import CreateView

from apps.commerce import payments, selectors, services
from apps.commerce.forms import OrderStatusForm, ProductForm, ProductVariantForm
from apps.commerce.models import Order, Product, ProductVariant, Storefront, StorefrontMember


# ── Access control ─────────────────────────────────────────────────

def _user_storefronts_qs(user):
    """All storefronts this user can administer.

    Superusers see every storefront in the system; members see only
    the ones their StorefrontMember row links to.
    """
    if not user.is_authenticated:
        return Storefront.objects.none()
    if user.is_superuser:
        return Storefront.objects.all()
    return Storefront.objects.filter(members__user=user).distinct()


def _user_can_access(user, storefront: Storefront) -> bool:
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return StorefrontMember.objects.filter(
        storefront=storefront, user=user
    ).exists()


class SellerRequiredMixin(LoginRequiredMixin):
    """Login + storefront-membership gate for every dashboard view.

    Subclasses set `self.storefront` in dispatch via `_resolve()`
    so the storefront is loaded exactly once.
    """

    login_url = "/admin/login/"

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.get("storefront_slug")
        if slug is None:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        sf = selectors.get_storefront(slug)
        if sf is None:
            raise Http404("Storefront non trovato.")
        if not _user_can_access(request.user, sf):
            raise PermissionDenied(
                "Non hai accesso a questo storefront. "
                "Contatta il proprietario per essere aggiunto come membro."
            )
        self.storefront = sf
        return super().dispatch(request, *args, **kwargs)


# ── Dashboard root (no slug) — pick a storefront ───────────────────

class DashboardRootView(LoginRequiredMixin, TemplateView):
    """Lands the seller on a list of their storefronts.

    Single-membership users get auto-redirected straight to that
    storefront's home. Multi-membership and superusers see a chooser.
    """

    template_name = "commerce/dashboard/root.html"
    login_url = "/admin/login/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        storefronts = list(_user_storefronts_qs(request.user))
        if len(storefronts) == 1 and not request.user.is_superuser:
            return redirect("commerce:dashboard_home", storefronts[0].slug)
        self._storefronts = storefronts
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefronts"] = self._storefronts
        ctx["is_superuser"] = self.request.user.is_superuser
        return ctx


# ── Dashboard home ─────────────────────────────────────────────────

class DashboardHomeView(SellerRequiredMixin, TemplateView):
    template_name = "commerce/dashboard/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        sf = self.storefront
        ctx["storefront"] = sf
        ctx["recent_orders"] = selectors.list_storefront_orders(sf)[:6]
        ctx["stock_summary"] = selectors.dashboard_stock_summary(sf)
        ctx["product_count"] = sf.products.count()
        ctx["open_orders_count"] = (
            selectors.list_storefront_orders(sf)
            .exclude(status=Order.Status.DELIVERED)
            .exclude(status=Order.Status.CANCELLED)
            .count()
        )
        ctx["payment_provider_ok"] = payments.is_provider_available(sf.payment_provider)
        ctx["payment_provider_label"] = sf.get_payment_provider_display()
        ctx["members"] = sf.members.select_related("user")
        ctx["all_storefronts"] = list(_user_storefronts_qs(self.request.user))
        return ctx


# ── Products ───────────────────────────────────────────────────────

class ProductsListView(SellerRequiredMixin, ListView):
    template_name = "commerce/dashboard/products_list.html"
    context_object_name = "products"
    paginate_by = 30

    def get_queryset(self):
        return (
            Product.objects.filter(storefront=self.storefront)
            .select_related("collection")
            .prefetch_related("variants")
            .order_by("order", "title")
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        return ctx


class ProductCreateView(SellerRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = "commerce/dashboard/product_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["storefront"] = self.storefront
        return kwargs

    def form_valid(self, form):
        form.instance.storefront = self.storefront
        response = super().form_valid(form)
        messages.success(self.request, f"Prodotto '{form.instance.title}' creato.")
        return response

    def get_success_url(self):
        return reverse(
            "commerce:dashboard_product_edit",
            args=[self.storefront.slug, self.object.pk],
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["is_create"] = True
        return ctx


class ProductUpdateView(SellerRequiredMixin, UpdateView):
    form_class = ProductForm
    template_name = "commerce/dashboard/product_form.html"
    pk_url_kwarg = "product_pk"

    def get_queryset(self):
        return Product.objects.filter(storefront=self.storefront)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["storefront"] = self.storefront
        return kwargs

    def get_success_url(self):
        return reverse(
            "commerce:dashboard_product_edit",
            args=[self.storefront.slug, self.object.pk],
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["variants"] = self.object.variants.all()
        ctx["variant_form"] = ProductVariantForm()
        return ctx


class ProductDeleteView(SellerRequiredMixin, View):
    def post(self, request, storefront_slug, product_pk):
        product = get_object_or_404(Product, pk=product_pk, storefront=self.storefront)
        title = product.title
        product.delete()
        messages.success(request, f"Prodotto '{title}' eliminato.")
        return redirect("commerce:dashboard_products", storefront_slug)


# ── Variants ───────────────────────────────────────────────────────

class VariantCreateView(SellerRequiredMixin, View):
    def post(self, request, storefront_slug, product_pk):
        product = get_object_or_404(Product, pk=product_pk, storefront=self.storefront)
        form = ProductVariantForm(request.POST)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.product = product
            variant.save()
            messages.success(request, f"Variante '{variant.sku}' creata.")
        else:
            for field, errors in form.errors.items():
                for err in errors:
                    messages.error(request, f"{field}: {err}")
        return redirect("commerce:dashboard_product_edit", storefront_slug, product_pk)


class VariantUpdateView(SellerRequiredMixin, View):
    def post(self, request, storefront_slug, product_pk, variant_pk):
        variant = get_object_or_404(
            ProductVariant,
            pk=variant_pk,
            product__pk=product_pk,
            product__storefront=self.storefront,
        )
        form = ProductVariantForm(request.POST, instance=variant)
        if form.is_valid():
            form.save()
            messages.success(request, f"Variante '{variant.sku}' aggiornata.")
        else:
            for field, errors in form.errors.items():
                for err in errors:
                    messages.error(request, f"{field}: {err}")
        return redirect("commerce:dashboard_product_edit", storefront_slug, product_pk)


class VariantDeleteView(SellerRequiredMixin, View):
    def post(self, request, storefront_slug, product_pk, variant_pk):
        variant = get_object_or_404(
            ProductVariant,
            pk=variant_pk,
            product__pk=product_pk,
            product__storefront=self.storefront,
        )
        variant.delete()
        messages.success(request, "Variante eliminata.")
        return redirect("commerce:dashboard_product_edit", storefront_slug, product_pk)


# ── Orders ─────────────────────────────────────────────────────────

class OrdersListView(SellerRequiredMixin, ListView):
    template_name = "commerce/dashboard/orders_list.html"
    context_object_name = "orders"
    paginate_by = 30

    def get_queryset(self):
        self.status_filter = self.request.GET.get("status") or None
        return selectors.list_storefront_orders(self.storefront, status=self.status_filter)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["status_filter"] = self.status_filter
        ctx["statuses"] = Order.Status.choices
        return ctx


class OrderDetailView(SellerRequiredMixin, DetailView):
    template_name = "commerce/dashboard/order_detail.html"
    context_object_name = "order"
    slug_url_kwarg = "order_uuid"
    slug_field = "uuid"

    def get_queryset(self):
        return (
            Order.objects
            .filter(storefront=self.storefront)
            .select_related("shipping_address", "billing_address", "shipping_method")
            .prefetch_related("items", "payment_intents")
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["storefront"] = self.storefront
        ctx["status_form"] = OrderStatusForm(initial={
            "fulfillment_status": self.object.fulfillment_status,
            "tracking_carrier": self.object.tracking_carrier,
            "tracking_number": self.object.tracking_number,
        })
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")
        try:
            if action == "mark_paid":
                services.mark_order_paid(order=self.object)
                messages.success(request, "Pagamento registrato.")
            elif action == "cancel":
                services.cancel_order(
                    order=self.object,
                    reason=request.POST.get("reason", ""),
                )
                messages.success(request, "Ordine annullato e stock ripristinato.")
            elif action == "fulfillment":
                form = OrderStatusForm(request.POST)
                if form.is_valid():
                    services.set_order_fulfillment(
                        order=self.object,
                        fulfillment_status=form.cleaned_data["fulfillment_status"],
                        tracking_carrier=form.cleaned_data.get("tracking_carrier") or "",
                        tracking_number=form.cleaned_data.get("tracking_number") or "",
                    )
                    messages.success(request, "Stato fulfillment aggiornato.")
                else:
                    for field, errs in form.errors.items():
                        for err in errs:
                            messages.error(request, f"{field}: {err}")
        except services.CommerceError as exc:
            messages.error(request, str(exc))
        return redirect(
            "commerce:dashboard_order_detail",
            self.storefront.slug,
            self.object.uuid,
        )
