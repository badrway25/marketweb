import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap as sitemap_view
from django.urls import include, path

# T43 · public discovery surface — sitemap.xml + robots.txt
from apps.catalog.sitemaps import SITEMAPS
from apps.pages.views import robots_txt

# T27 · 2FA on /admin/ via django-otp.
# Re-classify the default `admin.site` AdminSite instance as an
# OTPAdminSite — this preserves every ModelAdmin already registered
# via @admin.register(...) (the registry lives on the instance, not
# the class) while flipping the gate to require `is_verified()` on
# top of the standard is_active + is_staff check.
#
# Why a class swap and not a fresh instance:
#   - All app admin.py files register against `admin.site`. A fresh
#     OTPAdminSite() instance would have an empty registry until
#     each app re-registered against it (~70 ModelAdmins to migrate).
#   - The class swap is the canonical django-otp pattern (see
#     django-otp docs · "Integrating with Django's admin").
#
# Side effect: the standard /admin/login/ form is replaced by
# OTPAdminAuthenticationForm, which adds an `otp_token` field +
# `otp_device` select. Customer-facing /account/login/ is NOT
# affected (it uses a separate CustomerLoginView).
from django_otp.admin import OTPAdminSite

admin.site.__class__ = OTPAdminSite

urlpatterns = [
    # Admin (now an OTPAdminSite — see comment above)
    path("admin/", admin.site.urls),
    # T43 · public discovery surface. Mounted at the project root so
    # crawlers find them at the canonical paths /sitemap.xml and
    # /robots.txt. The sitemap delegates to per-section registries
    # in apps.catalog.sitemaps (static / categories / templates).
    # robots.txt is dynamic — it builds the Sitemap absolute URL
    # from the request host so crawlers see the right origin.
    path(
        "sitemap.xml",
        sitemap_view,
        {"sitemaps": SITEMAPS},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", robots_txt, name="robots_txt"),
    # App routes
    path("", include("apps.pages.urls")),
    path("templates/", include("apps.catalog.urls")),
    path("account/", include("apps.accounts.urls")),
    path("editor/", include("apps.editor.urls")),
    path("projects/", include("apps.projects.urls")),
    path("", include("apps.commerce.urls")),
    # API
    path("api/v1/", include("apps.core.urls")),
]

# T24 · env-gated triggers for the branded 400/403/500 error templates.
# Mounted ONLY when DJANGO_T24_TRIGGERS=1; default-off in prod so the
# paths do not exist for real traffic. See marketweb/_error_triggers.py.
if os.environ.get("DJANGO_T24_TRIGGERS", "").strip().lower() in {"1", "true", "yes", "on"}:
    urlpatterns += [path("__error/", include("marketweb._error_triggers"))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
