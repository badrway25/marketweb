"""Customer-facing auth views.

Phase A.1b introduces the real customer login/signup gate. Before this
phase the marketplace bounced anon users to ``/admin/login/`` — the
staff surface — which was fine for internal QA but incoherent with the
product promise ("clicca personalizza → autenticati → apri l'editor").

These views intentionally mirror what ``django.contrib.auth`` provides
out of the box; they exist so we can (a) swap the templates for a
branded, non-admin chrome and (b) honour ``?next=`` without relying on
the admin redirect whitelist.
"""
from __future__ import annotations

from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.utils.http import url_has_allowed_host_and_scheme

from apps.accounts.forms import CustomerLoginForm, CustomerSignupForm


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------

class CustomerLoginView(LoginView):
    """Branded login view used for the public customer surface."""

    template_name = "accounts/login.html"
    authentication_form = CustomerLoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Thread the ?next= value into the signup link so a customer who
        # realises they don't have an account yet doesn't lose the
        # originating template.
        next_url = self.request.GET.get("next") or self.request.POST.get("next") or ""
        signup_url = reverse("accounts:signup")
        if next_url and _is_safe_next(self.request, next_url):
            signup_url = f"{signup_url}?next={next_url}"
        ctx["signup_url"] = signup_url
        ctx["next"] = next_url
        return ctx


# ---------------------------------------------------------------------------
# Signup
# ---------------------------------------------------------------------------

@require_http_methods(["GET", "POST"])
def customer_signup(request):
    """Create a customer account, log them in, and honour ?next=."""
    if request.user.is_authenticated:
        return redirect(_resolve_next(request, default=reverse("projects:project_list")))

    next_url = request.GET.get("next") or request.POST.get("next") or ""

    if request.method == "POST":
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # T23 added a second auth backend (axes); when more than
            # one is configured Django needs an explicit backend arg
            # on direct `login()` calls (no ambiguity from `authenticate`).
            auth_login(
                request, user,
                backend="django.contrib.auth.backends.ModelBackend",
            )
            messages.success(
                request,
                f"Benvenuto, {user.username}! Il tuo account è pronto.",
            )
            return redirect(_resolve_next(request, default=reverse("projects:project_list")))
    else:
        form = CustomerSignupForm()

    login_url = reverse("accounts:login")
    if next_url and _is_safe_next(request, next_url):
        login_url = f"{login_url}?next={next_url}"

    return render(request, "accounts/signup.html", {
        "form": form,
        "next": next_url,
        "login_url": login_url,
    })


# ---------------------------------------------------------------------------
# Logout
# ---------------------------------------------------------------------------

@require_http_methods(["POST", "GET"])
def customer_logout(request):
    """Log the customer out and bounce back to the homepage."""
    auth_logout(request)
    messages.info(request, "Sessione chiusa. A presto.")
    return redirect("pages:home")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_safe_next(request, url: str) -> bool:
    return url_has_allowed_host_and_scheme(
        url=url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    )


def _resolve_next(request, *, default: str) -> str:
    candidate = request.GET.get("next") or request.POST.get("next")
    if candidate and _is_safe_next(request, candidate):
        return candidate
    return default
