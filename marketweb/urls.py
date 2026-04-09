from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
